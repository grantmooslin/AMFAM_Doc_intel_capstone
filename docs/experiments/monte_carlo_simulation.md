# Monte Carlo Simulation over the Braintrust Reasoning Corpus

The accumulated eval corpus — every manifest in `reports/manifests/`, the
reasoning traces backfilled from Braintrust spans, and the run-level context
(model, prompt, dataset, effort) — is a sample space: each completed row is a
draw from a per-image (and per prompt/model) label distribution. The
`monte_carlo_*` scripts treat the corpus that way and answer "what if" questions
with resampling and event simulation, at **zero model spend**. A small targeted
verification eval is the only step that spends credits.

## Pipeline

```bash
# 0. Build the joint corpus (manifests + reasoning backfill from Braintrust spans)
python scripts/braintrust/monte_carlo_corpus.py

# 1. Ensemble voting + confidence-gated escalation (accuracy/cost tradeoffs)
python scripts/braintrust/monte_carlo_ensemble.py

# 2. Paired-bootstrap prompt ablation (statistical gate for prompt iteration)
python scripts/braintrust/monte_carlo_prompt_ablation.py

# 3. Retry/failover/fallback pipeline failure simulation (production-scale risk)
python scripts/braintrust/monte_carlo_failures.py

# 4. Few-shot exemplar mining from correct near-miss reasoning traces
python scripts/braintrust/monte_carlo_exemplars.py

# 5. Spend-minimal verification recipe (prints the exact eval commands)
python scripts/braintrust/monte_carlo_verify.py --alpha 0.03
```

Corpus is cached at `reports/monte_carlo/corpus.jsonl`; rebuild idempotently with
`--rebuild`. Every phase writes markdown + PNG charts into `reports/monte_carlo/`.

## What each script answers

### 1. Ensemble + routing (`monte_carlo_ensemble.py`)
- Per-image label distribution from hard votes (predicted) plus soft votes
  (runner-up as a half-weight second choice).
- **accuracy(K)**: resample K draws per image, majority-vote, compare to ground
  truth, with bootstrap CIs. The K=1 curve is the simulated single-pass baseline.
- Per-image confidence = blend of vote dominance, label entropy, a near-miss
  signal (some observation named the expected class as its runner-up), and
  uncertainty phrasing in the reasoning.
- **Abstention/escalation**: route the lowest-confidence `alpha` fraction to a
  stronger model (parameterized accuracy + cost multiplier, with a ±5pp
  sensitivity band) and read the accuracy-vs-cost Pareto curve.

### 2. Prompt ablation (`monte_carlo_prompt_ablation.py`)
Per (model, prompt A, prompt B) pair, on the SHARED image set: paired bootstrap
of per-image deltas → mean delta, 95% CI, `P(A beats B)`, plus per-class and
per-confusion-pair deltas. This is the statistical gate for promoting a prompt
version (CI excluding zero with high P(win)), and it shows *where* a version
wins rather than just that it moved.

### 3. Failure pipeline (`monte_carlo_failures.py`)
Fits per-attempt probabilities from the corpus (first-attempt success, observed
row failure rate as the terminal probability, `finish_reason=length`, and retry
markers from `reports/eval_*.log`), then event-simulates the resilient runner's
retry/failover/fallback loop over 50K synthetic rows. Reports expected failure
rate, average attempts, extrapolated failures (and tail risk) at 800 / 25K /
320K scale, and a `max_tries` × fallback sensitivity sweep.

### 4. Exemplar mining (`monte_carlo_exemplars.py`)
For each confusion pair, finds correct traces whose `Runner-up:` line names the
decoy label (the model walked to the right answer while explicitly rejecting the
trap) — the gold few-shot examples for that pair. Monte Carlo random search
selects the subset with the largest expected error-flip gain under a token
budget, and writes a ready-to-paste exemplar appendix for the next prompt
version.

### 5. Verification (`monte_carlo_verify.py`)
Builds two small datasets (lowest-confidence escalation tail; top-confusion-pair
slice) and prints the exact eval commands. Default is a dry run; `--run-eval`
executes (the only real spend). Compare measured vs simulated accuracy on the
same images to validate the simulator before committing to a production change.

## Current findings (corpus: 4,641 rows / 1,512 images, qwen3.7-flash dominant)

- **Ensemble voting is a weak lever.** Simulated committee accuracy is 82.1% at
  K=1 → 85.3% at K=10 → 86.3% at K=25. Cross-run variance is small; majority
  voting buys at most ~4pp at 10-25x cost. The variance budget lives in prompt
  quality, not sampling noise.
- **Confidence-gated escalation is the accuracy lever.** Routing the lowest
  ~10-15% of images to a ~90%-accurate model buys +4-6pp at +20-30% cost;
  40% escalation reaches ~92% at 1.8x cost. The 40→50% step is non-monotonic
  (the band contains near-miss/uncertainty-flagged single-observation images),
  so the Pareto point should be chosen from the table, not extrapolated.
- **The fallback-model salvage is the failure lever.** With fallback on, the
  simulated failure rate drops from ~2.9% to ~0.11% — a ~25x reduction. At
  320K images: ~364 expected failed rows (95% CI 328-402), P(>1% failures) = 0.
  `max_tries` barely matters (1 vs 5 both ≈2.86% without fallback); the fallback
  pass is what eliminates failures.
- **Prompt progress is real but the newest steps are not yet proven.**
  v0→v17 +28.4pp (P=0.000), v0→v11.8 +13.0pp. But on shared images v11.8 beats
  v17 (P=0.94, +2.5pp) and v16 vs v17 is inconclusive (+0.6pp, P=0.57). v17 is
  not statistically better than v16 on the shared slice yet — worth a larger
  shared-image comparison before the next iteration.
- **Targeted exemplars could recover ~4% of the error pool.** Top actionable
  pairs: letter→memo (53), budget→invoice (52), invoice→form (41),
  specification→form (41). The `budget→invoice` pair has 8 usable near-miss
  traces but the 12K-char budget capped the selected appendix at 4 exemplars.
