# Full Report — qwen3.7-flash_v11.8_reasoning_1600_balanced_1120

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v11.8`  
**Dataset:** `rvl_cdip_1600` (70 per class × 16 classes = 1120 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **82.59%** (925/1120) |
| Scored rows | 1120 |
| Failed/empty rows | 0 |
| Failure rate | 0.0% |
| **Near-miss** (correct answer was model's runner-up) | **72** (6.4% of rows; 36.9% of all misses) |
| Runner-up coverage | 933/1120 completed rows |
| Prompt tokens (avg) | 11,999.7 |
| Prompt cached tokens (avg) | 7,569.8 |
| Completion tokens (avg) | 1,911.3 |
| Completion reasoning tokens (avg) | 1,567.9 |
| Total tokens (avg) | 13,910.9 |
| Time to first token (avg) | 45.63s |
| Duration (avg) | 0.00s |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 13,439,611 |
| Total completion tokens (measured) | 2,140,612 |
| Total tokens (measured) | 15,580,223 |
| **Expected cost** (list price × measured tokens) | **$0.6815** |
| **Actual cost** (OpenRouter billed, all calls incl. retries) | **$0.4937** |
| Difference (expected − actual) | $+0.1877 (+27.5%) |
| Cost coverage | 1120/1120 rows with billed cost |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.49 | $0.35 |
| 25,000 | $15.21 | $11.02 |
| 320,000 | $194.71 | $141.07 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v11.8_reasoning_1600_balanced_1120.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 57 | 70 | 81% |
| `budget` | 47 | 70 | 67% |
| `email` | 63 | 70 | 90% |
| `file_folder` | 63 | 70 | 90% |
| `form` | 61 | 70 | 87% |
| `handwritten` | 62 | 70 | 89% |
| `invoice` | 55 | 70 | 79% |
| `letter` | 49 | 70 | 70% |
| `memo` | 61 | 70 | 87% |
| `news_article` | 60 | 70 | 86% |
| `presentation` | 49 | 70 | 70% |
| `questionnaire` | 61 | 70 | 87% |
| `resume` | 67 | 70 | 96% |
| `scientific_publication` | 59 | 70 | 84% |
| `scientific_report` | 50 | 70 | 71% |
| `specification` | 61 | 70 | 87% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v11.8_reasoning_1600_balanced_1120.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v11.8_reasoning_1600_balanced_1120.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v11.8_reasoning_1600_balanced_1120.md)

### Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `letter` | `memo` | 16 |
| `budget` | `invoice` | 12 |
| `specification` | `form` | 9 |
| `invoice` | `budget` | 8 |
| `presentation` | `scientific_report` | 8 |
| `advertisement` | `presentation` | 7 |
| `scientific_report` | `form` | 7 |
| `budget` | `form` | 6 |
| `invoice` | `form` | 6 |
| `scientific_publication` | `scientific_report` | 6 |
| `file_folder` | `presentation` | 5 |
| `memo` | `letter` | 5 |
| `presentation` | `file_folder` | 4 |
| `scientific_publication` | `news_article` | 4 |
| `scientific_report` | `specification` | 4 |
| `advertisement` | `form` | 3 |
| `budget` | `presentation` | 3 |
| `email` | `presentation` | 3 |
| `handwritten` | `questionnaire` | 3 |
| `presentation` | `form` | 3 |

## Results Interpretation

### Overall

qwen3.7-flash with prompt **v11.8** classifies **925/1120 (82.6%)** of the 1120-image `rvl_cdip_1600` slice exactly. There are **0 failed/empty rows** (failure rate 0.0%) — the resilient retry loop recovered every transient provider error, so accuracy is measured over the full slice.

**Near-miss analysis:** 72 of the 195 misses (36.9%) were near-misses — the model got the answer wrong but named the correct class as its runner-up in the reasoning trace. 933/1120 rows had a parsable runner-up line. If runner-up confusion were fixed (e.g. sharpening the tie-break rules between the confused pairs below), accuracy would rise to approximately 89.0%.

### Strengths

- **`resume`**: 96% (67/70)
- **`file_folder`**: 90% (63/70)
- **`email`**: 90% (63/70)

### Weaknesses

- **`budget`**: 67% (47/70)
- **`letter`**: 70% (49/70)
- **`presentation`**: 70% (49/70)

### Top Confusion Patterns

The most frequent misclassifications are:
- **`letter` → `memo`**: 16 images
- **`budget` → `invoice`**: 12 images
- **`specification` → `form`**: 9 images
- **`invoice` → `budget`**: 8 images
- **`presentation` → `scientific_report`**: 8 images

The dominant failure mode is confusion between visually similar classes (`letter` ↔ `memo` `budget` ↔ `invoice` `specification` ↔ `form` ); the single largest confused pair accounts for 8% of all misses.

### Cost

The run billed **$0.4937** actual vs **$0.6815** list-price expected (+27.5%), averaging $0.000441/image. The gap is mostly prompt caching — 7,570 of 12,000 avg prompt tokens/row were cache hits (cached input billed at ~10% of the input price). Extrapolated linearly: $0.35 for 800 images, $11.02 for 25,000, and $141.07 for a 320,000-image production sweep.

### Recommendations

1. Address the 72 near-misses by adding tie-break disambiguation rules between the top confused pairs — this is the highest-leverage prompt change (up to ~6.4pp of accuracy).
2. Add worked counter-examples for the dominant pairs (`letter`→`memo`, `budget`→`invoice`, `specification`→`form`).
3. Review the misclassification reasoning traces linked above before iterating on the prompt — the raw reasoning often exposes the exact rule the model misfired on.
