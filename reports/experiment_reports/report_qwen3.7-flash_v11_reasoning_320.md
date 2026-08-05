# Braintrust Experiment Report — qwen3.7-flash_v11_reasoning_320

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v11`  
**Dataset:** `fixed_size_sampled_320` (20 per class × 16 classes = 320 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **83.81%** (264/315) |
| Prompt tokens (avg) | 11,165.5 |
| Prompt cached tokens (avg) | 8,874.7 |
| Completion tokens (avg) | 2,029.6 |
| Completion reasoning tokens (avg) | 1,680.7 |
| Total tokens (avg) | 13,195.1 |
| Time to first token (avg) | 46.27s |
| Duration (avg) | 0.00s |
| Errors | 3 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 3,517,131 |
| Total completion tokens (measured) | 639,337 |
| Total tokens (measured) | 4,156,468 |
| **Expected cost** (list price × measured tokens) | **$0.1886** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.1198** |
| Difference (expected − actual) | $+0.0688 (+36.5%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.48 | $0.30 |
| 25,000 | $14.97 | $9.51 |
| 320,000 | $191.62 | $121.72 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v11_reasoning_320.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 18 | 20 | 90% |
| `budget` | 13 | 20 | 65% |
| `email` | 20 | 20 | 100% |
| `file_folder` | 18 | 20 | 90% |
| `form` | 14 | 20 | 70% |
| `handwritten` | 19 | 20 | 95% |
| `invoice` | 15 | 20 | 75% |
| `letter` | 15 | 20 | 75% |
| `memo` | 19 | 20 | 95% |
| `news_article` | 15 | 17 | 88% |
| `presentation` | 14 | 20 | 70% |
| `questionnaire` | 17 | 20 | 85% |
| `resume` | 20 | 20 | 100% |
| `scientific_publication` | 18 | 20 | 90% |
| `scientific_report` | 14 | 18 | 78% |
| `specification` | 15 | 20 | 75% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v11_reasoning_320.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v11_reasoning_320.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v11_reasoning_320.md)
