# Braintrust Experiment Report — qwen3.7-flash_v11_8_reasoning_320

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v11.8`  
**Dataset:** `fixed_size_sampled_320` (20 per class × 16 classes = 318 images)  
**Image size:** 1024x1024  
**Reasoning:** high  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **87.11%** (277/318) |
| Scored rows | 318 |
| Failed/empty rows | 1 |
| Total expected rows | 319 |
| Prompt tokens (avg) | 12,013.2 |
| Prompt cached tokens (avg) | 7,587.0 |
| Completion tokens (avg) | 1,910.3 |
| Completion reasoning tokens (avg) | 1,560.7 |
| Total tokens (avg) | 13,923.5 |
| Time to first token (avg) | 42.61s |
| Duration (avg) | 0.00s |
| Evaluation failures | 1 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 3,820,182 |
| Total completion tokens (measured) | 607,490 |
| Total tokens (measured) | 4,427,672 |
| **Expected cost** (list price × measured tokens) | **$0.1936** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.1338** |
| Difference (expected − actual) | $+0.0598 (+30.9%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.49 | $0.34 |
| 25,000 | $15.22 | $10.52 |
| 320,000 | $194.80 | $134.60 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v11_8_reasoning_320.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 16 | 18 | 89% |
| `budget` | 16 | 20 | 80% |
| `email` | 20 | 20 | 100% |
| `file_folder` | 17 | 20 | 85% |
| `form` | 17 | 20 | 85% |
| `handwritten` | 18 | 20 | 90% |
| `invoice` | 16 | 20 | 80% |
| `letter` | 15 | 20 | 75% |
| `memo` | 20 | 20 | 100% |
| `news_article` | 18 | 20 | 90% |
| `presentation` | 16 | 20 | 80% |
| `questionnaire` | 17 | 20 | 85% |
| `resume` | 20 | 20 | 100% |
| `scientific_publication` | 17 | 20 | 85% |
| `scientific_report` | 16 | 20 | 80% |
| `specification` | 18 | 20 | 90% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v11_8_reasoning_320.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v11_8_reasoning_320.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v11_8_reasoning_320.md)
