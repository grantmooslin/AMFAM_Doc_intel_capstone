# Braintrust Experiment Report — qwen3.7-flash_v14_reasoning_160_v2_retry

**Model:** `qwen/qwen3.7-flash`
**Prompt version:** `v14`
**Dataset:** `fixed_size_sampled_v2` (10 per class × 16 classes = 160 images)
**Image size:** 1024x1024
**Reasoning:** enabled (effort=high), trace logged
**Max concurrency:** 8

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **85.00%** (136/160) |
| Scored rows | 160 |
| Failed/empty rows | 0 |
| Total expected rows | 160 |
| Prompt tokens (avg) | 12,959.8 |
| Prompt cached tokens (avg) | 7,164.8 |
| Completion tokens (avg) | 2,551.5 |
| Completion reasoning tokens (avg) | 2,173.1 |
| Total tokens (avg) | 15,511.3 |
| Time to first token (avg) | 54.75s |
| Duration (avg) | 0.00s |
| Evaluation failures | 0 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 2,073,572 |
| Total completion tokens (measured) | 408,242 |
| Total tokens (measured) | 2,481,814 |
| **Expected cost** (list price × measured tokens) | **$0.1153** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.0864** |
| Difference (expected − actual) | $+0.0289 (+25.1%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.58 | $0.43 |
| 25,000 | $18.01 | $13.50 |
| 320,000 | $230.56 | $172.75 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v14_reasoning_160_v2_retry.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 10 | 10 | 100% |
| `budget` | 4 | 10 | 40% |
| `email` | 9 | 10 | 90% |
| `file_folder` | 10 | 10 | 100% |
| `form` | 7 | 10 | 70% |
| `handwritten` | 10 | 10 | 100% |
| `invoice` | 5 | 10 | 50% |
| `letter` | 8 | 10 | 80% |
| `memo` | 10 | 10 | 100% |
| `news_article` | 9 | 10 | 90% |
| `presentation` | 9 | 10 | 90% |
| `questionnaire` | 8 | 10 | 80% |
| `resume` | 10 | 10 | 100% |
| `scientific_publication` | 9 | 10 | 90% |
| `scientific_report` | 9 | 10 | 90% |
| `specification` | 9 | 10 | 90% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v14_reasoning_160_v2_retry.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v14_reasoning_160_v2_retry.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v14_reasoning_160_v2_retry.md)
