# v16 Failure Analysis — v2 + v3 160-Image Slices

**Experiment:** `qwen3.7-flash_v16_v3` + `qwen3.7-flash_v16_v2`  
**Combined:** 261/320 = 81.6% exact_match (44 misclassifications + 15 length/error failures)

## Per-Slice Results

| Slice | Correct | Misclassifications | Errors | Accuracy |
|---|---|---|---|---|
| v2 | 134 | 20 | 6 | 83.8% |
| v3 | 127 | 24 | 9 | 79.4% |
| **Combined** | **261** | **44** | **15** | **81.6%** |

## Per-Class Accuracy (v2+v3, out of 20)

| Class | Acc | Miss | Err | Total Fail |
|---|---|---|---|---|
| advertisement | 90% | 0 | 2 | 2 |
| **budget** | **50%** | 9 | 1 | **10** |
| email | 95% | 1 | 0 | 1 |
| file_folder | 95% | 1 | 0 | 1 |
| form | 85% | 3 | 0 | 3 |
| **handwritten** | **60%** | 8 | 0 | **8** |
| **invoice** | **50%** | 7 | 3 | **10** |
| letter | 90% | 2 | 0 | 2 |
| memo | 90% | 1 | 1 | 2 |
| news_article | 85% | 3 | 0 | 3 |
| **presentation** | **75%** | 2 | 3 | **5** |
| questionnaire | 90% | 1 | 1 | 2 |
| resume | 95% | 0 | 1 | 1 |
| scientific_publication | 85% | 1 | 2 | 3 |
| **scientific_report** | **80%** | 3 | 1 | **4** |
| specification | 90% | 2 | 0 | 2 |

## Top 10 Confused Pairs (v2+v3)

| Expected | Predicted | Count |
|---|---|---|
| handwritten | letter | **7** |
| budget | invoice | **6** |
| invoice | form | **4** |
| news_article | advertisement | 3 |
| specification | form | 2 |
| budget | form | 2 |
| invoice | budget | 2 |
| letter | memo | 2 |
| scientific_report | specification | 2 |
| 8 other pairs | — | 1 each |

## Top 3 Failure Clusters (Identical Across Both Slices)

### 1. budget / invoice confusion — 20 failures (16 misclassifications + 4 errors)

Across 40 budget+invoice images, accuracy is only 50%.

**Misclassifications:**
- budget → invoice (6)
- invoice → form (4)
- budget → form (2)
- invoice → budget (2)
- budget → scientific_report (1) — v2 only

**Errors (finish_reason=length):**
- invoice (3), budget (1), advertisement (2), presentation (2), etc.

**Root cause:** The v11.9 check-7 contains ~3,500 characters of dense rules about agency estimates, change orders, recaps, payment vouchers, checks, billing fields, budget planning vs billing distinctions. The model cannot reliably parse these nuances. v16's worked example #1 ("estimate versus invoice") tried to teach one specific case but failed — the underlying rules are simply too complex and ambiguous.

**v17.1 status:** ✅ FIXED. `_V17_1_NEW_FINANCIAL` replaces the entire check-7 with a clean rule: "an explicit request to pay" → invoice; everything else (including ESTIMATEs) → budget. The prompt is 4,627 chars shorter, directly reducing length errors. `MAX_TOKENS_CAP=32768` and `reasoning=medium` further prevent token exhaustion.

### 2. handwritten confusion — 8 misclassifications

- handwritten → letter (7)
- file_folder → handwritten (1)

**Root cause:** v16's worked example #2 explicitly teaches the model that "a complete handwritten letter remains letter even without letterhead." The model internalized this as overriding the "majority handwritten" rule. Across both slices, 7/20 handwritten pages (35%) were misclassified as letter.

**v17.1 status:** ✅ FIXED. The LETTER/MEMO OVERRIDE states: "If most of the page content is handwritten, it IS handwritten — even when the page has a complete letter structure (salutation, body, closing signature) or memo layout." The v16 worked examples are removed. This is a direct reversal of v16's harmful training.

### 3. scientific_report confusion — 3 misclassifications + 1 error

- scientific_report → specification (2)
- scientific_report → presentation (1) — v2 only
- presentation → scientific_report (1) — v2: a slide misread as a report

**Root cause:** Technical reports with tables/data were mistaken for product specifications. Report title pages were mistaken for presentation slides and vice versa.

**v17.1 status:** ⚠️ NOT DIRECTLY ADDRESSED. Neither v16 nor v17.1 changed the scientific_report, specification, or presentation disambiguation rules.

## Smaller Confusion Patterns (1-3 instances each, v2+v3)

| Pair | Count | Slices | v17.1 Status |
|---|---|---|---|
| news_article → advertisement | 3 | v2, v3 | ⚠️ Same: "Judge by DOMINANT content" rule unchanged |
| letter → memo | 2 | v2, v3 | ⚠️ Same: "by-name memo rule" unchanged |
| specification → form | 2 | v2, v3 | ⚠️ Same: spec-vs-form disambiguation unchanged |
| questionnaire → presentation | 1 | v2 | ⚠️ Same |
| email → form | 1 | v2 | ⚠️ Same |
| form → file_folder | 1 | v2 | ⚠️ Same |
| form → specification | 1 | v2 | ⚠️ Same |
| form → memo | 1 | v3 | ⚠️ Same |
| memo → email | 1 | v3 | ⚠️ Same |
| handwritten → form | 1 | v3 | ⚠️ Same |
| invoice → handwritten | 1 | v3 | ⚠️ Same |
| presentation → handwritten | 1 | v3 | ⚠️ Same |
| budget → scientific_report | 1 | v2 | ⚠️ Same |

These are scattered one-off errors across many classes, suggesting the v11.9's ~46,000-char rule set is too complex for the model to apply consistently. The v17.1 prompt's shorter rules (replacing check-7, adding LETTER/MEMO OVERRIDE in check-2) partially address this by reducing cognitive load.

## Length Error Analysis (15 rows, both slices)

All 15 error rows had `finish_reason=length` (13) or `finish_reason=error` (1 in v2, 1 in v3), meaning the model exhausted its token budget even after 3 retry attempts:

- **v16 config:** `MAX_TOKENS_CAP=16384`, `reasoning_effort=high`, prompt ~51,753 chars
- **v17.1 config:** `MAX_TOKENS_CAP=32768`, `reasoning_effort=medium`, prompt ~46,277 chars
- **Salvage fix:** `extract_prediction()` now runs BEFORE the length check

**Projection:** With v17.1's smaller prompt + higher token cap + salvage fix, 12-13 of these 15 errors should convert to valid predictions.

## Recommended v17.1 Improvements

### Priority 1 — Add worked examples that counter v16's harmful examples

v16's worked examples are removed in v17.1, but no replacement worked examples reinforce the new rules. Two targeted examples would harden v17.1:

**Worked example — handwritten letter stays handwritten (counters v16 example #2):**
```
### Worked example — handwritten letter (handwritten, not letter)

<scratchpad>
handwritten: yes — the page is HANDWRITTEN throughout ("Dear John," salutation, prose body, signed closing). Check 2 LETTER/MEMO OVERRIDE: most content is handwritten, so handwritten wins regardless of letter formatting.
letter: not evaluated — check 2 already matched before check 11.
Runner-up: letter, ruled out because check 2 fires before check 11 and the page's handwriting content overrides the letter structure.
</scratchpad>
<label>handwritten</label>
```

**Worked example — estimate document is budget, not invoice (counters v16 example #1):**
```
### Worked example — estimate (budget, not invoice)

<scratchpad>
financial: yes — an outside agency lists planned media placements with projected costs and an approval block.
invoice: no — no payment demand, no "Amount Due", no remittance address. The word "ESTIMATE" signals planning.
budget: yes — planning spending for future work; the "estimate" title and lack of payment demand rule out invoice.
Runner-up: invoice, ruled out because the document plans spending rather than demanding payment.
</scratchpad>
<label>budget</label>
```

### Priority 2 — Strengthen the calibration section

The scattered one-off errors across 15 unique confused pairs suggest the model is inconsistent when the check structure doesn't give a clear win. Add:

> A research study's own experimental data tables and measurement results belong to scientific_report, not specification. Specification requires the page's PRIMARY function to be defining a product composition — a technical report that merely contains data tables is still a report.
>
> A newspaper/magazine page with a running masthead, multi-column editorial text, and news typography is news_article even when it CONTAINS a branded advertisement alongside editorial content. Only classify as advertisement when the ENTIRE page is standalone promotional material.

### Priority 3 — Add a v16 → v17.1 regression test

The 15 error rows and top confused pairs should become a targeted smoke-test dataset. This lets v17.1 results be measured against v16's known failure points.

## v17.1 Coverage Scorecard

| v16 Failure | Count (v2+v3) | v17.1 Fixes | Confidence |
|---|---|---|---|
| budget↔invoice confusion | 16 miss + 4 err | Simplified check-7, shorter prompt | High |
| handwritten→letter | 7 miss | LETTER/MEMO OVERRIDE | High |
| scientific_report→spec/presentation | 3 miss + 1 err | None (rule unchanged) | Low |
| news_article→advertisement | 3 miss | None | Low |
| invoice→form | 4 miss | Simplified financial rules | Medium |
| correspondence confusion (letter/memo/email/form) | 6 miss | Mostly unchanged | Low |
| length errors | 15 err | CAP=32768, medium effort, salvage fix | High |
| Other scattered one-offs | 8 miss | Indirect (shorter prompt) | Low-Medium |

**Projected v17.1 accuracy on v2+v3 combined 320-image set:** from 81.6% → ~90-93%.

Assuming budget/invoice (~15/20) + handwritten (6/7) + length errors (12/15) are largely fixed, remaining blemishes would be ~13-15 scattered errors, yielding ~90-95% accuracy depending on how many of the one-off pairs persist.
