# Braintrust Experiment Report — qwen3.7-flash_v0_reasoning_480-d4c97ff0

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v0`  
**Dataset:** `fixed_size_sampled_480` (30 per class × 16 classes = 480 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **69.17%** (332/480) |
| Scored rows | 480 |
| Failed/empty rows | 0 |
| Total expected rows | 480 |
| Prompt tokens (avg) | 525.4 |
| Prompt cached tokens (avg) | 0.0 |
| Completion tokens (avg) | 1,241.4 |
| Completion reasoning tokens (avg) | 1,150.8 |
| Total tokens (avg) | 1,766.8 |
| Time to first token (avg) | 30.61s |
| Duration (avg) | 0.00s |
| Evaluation failures | 0 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 252,208 |
| Total completion tokens (measured) | 595,855 |
| Total tokens (measured) | 848,063 |
| **Expected cost** (list price × measured tokens) | **$0.0850** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.0846** |
| Difference (expected − actual) | $+0.0004 (+0.5%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.14 | $0.14 |
| 25,000 | $4.43 | $4.41 |
| 320,000 | $56.68 | $56.39 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v0_reasoning_480-d4c97ff0.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 28 | 30 | 93% |
| `budget` | 13 | 30 | 43% |
| `email` | 28 | 30 | 93% |
| `file_folder` | 24 | 30 | 80% |
| `form` | 22 | 30 | 73% |
| `handwritten` | 16 | 30 | 53% |
| `invoice` | 17 | 30 | 57% |
| `letter` | 21 | 30 | 70% |
| `memo` | 30 | 30 | 100% |
| `news_article` | 24 | 30 | 80% |
| `presentation` | 11 | 30 | 37% |
| `questionnaire` | 17 | 30 | 57% |
| `resume` | 18 | 30 | 60% |
| `scientific_publication` | 28 | 30 | 93% |
| `scientific_report` | 18 | 30 | 60% |
| `specification` | 17 | 30 | 57% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v0_reasoning_480-d4c97ff0.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v0_reasoning_480-d4c97ff0.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v0_reasoning_480-d4c97ff0.md)
