# Braintrust Experiment Report — qwen3.7-flash_v0_reasoning_800-f0b6b2e4

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v0`  
**Dataset:** `rvl_cdip_800` (50 per class × 16 classes = 800 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **66.12%** (529/800) |
| Scored rows | 800 |
| Failed/empty rows | 0 |
| Total expected rows | 800 |
| Prompt tokens (avg) | 741.1 |
| Prompt cached tokens (avg) | 0.0 |
| Completion tokens (avg) | 1,552.1 |
| Completion reasoning tokens (avg) | 1,491.1 |
| Total tokens (avg) | 2,293.1 |
| Time to first token (avg) | 39.53s |
| Duration (avg) | 0.00s |
| Evaluation failures | 0 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 592,847 |
| Total completion tokens (measured) | 1,241,656 |
| Total tokens (measured) | 1,834,503 |
| **Expected cost** (list price × measured tokens) | **$0.1792** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.1773** |
| Difference (expected − actual) | $+0.0019 (+1.1%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.18 | $0.18 |
| 25,000 | $5.60 | $5.54 |
| 320,000 | $71.68 | $70.92 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v0_reasoning_800-f0b6b2e4.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 47 | 50 | 94% |
| `budget` | 12 | 50 | 24% |
| `email` | 48 | 50 | 96% |
| `file_folder` | 35 | 50 | 70% |
| `form` | 38 | 50 | 76% |
| `handwritten` | 21 | 50 | 42% |
| `invoice` | 28 | 50 | 56% |
| `letter` | 37 | 50 | 74% |
| `memo` | 48 | 50 | 96% |
| `news_article` | 42 | 50 | 84% |
| `presentation` | 15 | 50 | 30% |
| `questionnaire` | 24 | 50 | 48% |
| `resume` | 33 | 50 | 66% |
| `scientific_publication` | 44 | 50 | 88% |
| `scientific_report` | 30 | 50 | 60% |
| `specification` | 27 | 50 | 54% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v0_reasoning_800-f0b6b2e4.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v0_reasoning_800-f0b6b2e4.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v0_reasoning_800-f0b6b2e4.md)
