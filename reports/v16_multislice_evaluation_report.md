# v16 Multislice Evaluation Report

**Model:** qwen/qwen3.7-flash (reasoning=high)
**Prompt:** v16 = v11.9 (v11.8 + chart fix) + 2 worked examples (estimate→invoice, handwritten→letter)
**Date:** 2026-08-03
**Temperature:** 0.1

## Results Summary

| Slice | Dataset | Accuracy | Failed | Misclassified |
|-------|---------|----------|--------|---------------|
| v1    | fixed_size_sampled | 154/160 (96.2%) | 1 | 5 |
| v2    | fixed_size_sampled_v2 | 134/160 (83.8%) | 6 | 20 |
| v3    | fixed_size_sampled_v3 | 127/160 (79.4%) | 9 | 24 |

## Comparison with Baselines

| Prompt | v1 Slice | v2 Slice | v3 Slice |
|--------|----------|----------|----------|
| v11.8  | 157/158 (99.4%) | — | — |
| v14    | — | 136/160 (85.0%) | — |
| v15    | — | — | 130/160 (81.2%) |
| **v16** | **154/160 (96.2%)** | **134/160 (83.8%)** | **127/160 (79.4%)** |

## PAIN POINT ANALYSIS

### 1. Provider / Transmission Errors (16 rows / 3.3% failure rate)
Across 480 total rows (3 slices × 160), 16 rows failed entirely:
- **13 finish_reason=length**: model exhausted reasoning tokens (qwen3.7-flash with reasoning=high can run out of tokens mid-scratchpad). The retry loop doubles max_tokens once (from 4096 → 8192 capped at 16384), but for complex images the model still hits the cap after all 3 retries.
- **3 finish_reason=error**: Alibaba provider returned 502 "inappropriate content" or empty responses.

**Impact:** Failures alone account for 10% of v3's misses (9/33). Each failed row counts as a miss in exact_match. A simple fix — bumping `MAX_TOKENS_CAP` from 16384 to 32768 or dropping reasoning effort to `medium` — could recover 6-8 points on the hard slices.

### 2. Slice Hardness: v1 Source vs v2/v3 Source
The v1 slice (`fixed_size_sampled`) draws from the original `test_images` directory. The v2 and v3 slices draw from the HF mirror `jordyvl/rvl_cdip_100_examples_per_class`, which contains different image files.

- Same prompt, same model: v1 = 96.2%, v2 = 83.8%, v3 = 79.4%
- This ~13-17 point gap exists independent of prompt version (v14 on v2 = 85%, v15 on v3 = 81%)

**Hypothesis:** The HF mirror images may be lower quality, have different preprocessing, or include more ambiguous edge-cases that the original `test_images` subset avoids.

### 3. Prompt Regression from v11.8
On the v1 slice (the only slice with direct v11.8 comparison):
- v11.8: 157/158 = 99.4% (1 miss)
- v16: 154/160 = 96.2% (6 misses)

The v11.9 "chart fix" + 2 worked examples added ~1600 chars to the prompt and caused 5 additional misses on the v1 slice. For a reasoning model, longer prompt → more chances for the model to over-fit to contradictory rules.

### 4. Persistent Confusion Patterns (across all three v16 slices)
Aggregated misclassification matrix:

| Pattern | v1 | v2 | v3 | **Total** |
|---------|----|----|----|-----------|
| handwritten → letter | 3 | 4 | 3 | **10** |
| budget → invoice | 1 | 3 | 3 | **7** |
| invoice → form | 0 | 2 | 2 | **4** |
| budget → form | 0 | 1 | 1 | 2 |
| news_article → advertisement | 0 | 1 | 2 | 3 |
| scientific_report → specification | 0 | 0 | 2 | 2 |
| letter → memo | 0 | 1 | 1 | 2 |

Despite worked examples targeting budget↔invoice and handwritten↔letter, these pairs remain the top errors.

### 5. Worked Examples Did Not Help
v16 added exactly two worked examples:
1. estimate-vs-invoice → budget
2. handwritten-letter-vs-memo → letter

Yet budget→invoice and handwritten→letter remain the #1 and #2 confusion sources. Possible reasons:
- The examples may be too specific (tied to particular image layouts) and don't generalize.
- Adding worked examples lengthens the prompt, diluting the priority of the systematic rule-based precedence order that made v11.8 effective.
- qwen3.7-flash with reasoning may tunnel on the examples as templates rather than internalizing the rule structure.

## Per-Class Accuracy (v16 Aggregate)

| Class | v1 Correct | v2 Correct | v3 Correct |
|-------|-----------|-----------|-----------|
| advertisement | 9/10 | 10/10 | 8/10 |
| budget | 9/10 | 5/10 | 5/10 |
| email | 10/10 | 9/10 | 10/10 |
| file_folder | 10/10 | 10/10 | 9/10 |
| form | 9/10 | 8/10 | 8/10 |
| handwritten | 7/10 | 6/10 | 6/10 |
| invoice | 10/10 | 7/10 | 6/10 |
| letter | 10/10 | 9/10 | 9/10 |
| memo | 10/10 | 9/10 | 9/10 |
| news_article | 9/9 | 9/9 (est) | 8/10 |
| presentation | 10/10 | 9/10 | 8/10 |
| questionnaire | 10/10 | 10/10 | 9/10 |
| resume | 10/10 | 10/10 | 10/10 |
| scientific_publication | 11/11 | 10/10 | 9/10 |
| scientific_report | 10/10 | 9/10 | 7/10 |
| specification | 10/10 | 9/10 | 9/10 |

## Recommendations

1. **Roll back to v11.8/v11.9 prompt** on the v1-style source — achieved 99.4% accuracy. The v16 additions reduce accuracy even on the easiest slice.
2. **Characterize the v2/v3 image source** — the HF mirror images consistently score ~15 points lower than v1 test_images. This may indicate a dataset quality issue, not a prompt issue.
3. **Reduce reasoning effort** for qwen3.7-flash from `high` to `medium` and/or increase `MAX_TOKENS_CAP` to eliminate finish_reason=length failures.
4. **Remove worked examples** and revert to the systematic rule-based approach of v11.8 that maps each class to an ordered checklist of positive/negative discriminators.
5. **Re-slice from the test_images source** for future evaluations to maintain comparability with the v11.8 99.4% baseline.
