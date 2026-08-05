# Braintrust Experiment Report — qwen3.7-flash_v11_8_reasoning_160_t0_3

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v11.8`  
**Dataset:** `fixed_size_sampled` (10 per class × 16 classes = 159 images)  
**Image size:** 1024x1024  
**Reasoning:** effort=high, temperature=0.3  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **98.74%** (157/159) |
| Scored rows | 159 |
| Failed/empty rows | 1 |
| Total expected rows | 160 |
| Prompt tokens (avg) | 12,013.2 |
| Prompt cached tokens (avg) | 5,696.4 |
| Completion tokens (avg) | 1,712.5 |
| Completion reasoning tokens (avg) | 1,380.2 |
| Total tokens (avg) | 13,725.6 |
| Time to first token (avg) | 40.71s |
| Duration (avg) | 0.00s |
| Evaluation failures | 1 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 1,910,091 |
| Total completion tokens (measured) | 272,284 |
| Total tokens (measured) | 2,182,375 |
| **Expected cost** (list price × measured tokens) | **$0.0927** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.0700** |
| Difference (expected − actual) | $+0.0227 (+24.5%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.47 | $0.35 |
| 25,000 | $14.58 | $11.00 |
| 320,000 | $186.57 | $140.84 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v11_8_reasoning_160_t0_3.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 9 | 9 | 100% |
| `budget` | 9 | 10 | 90% |
| `email` | 10 | 10 | 100% |
| `file_folder` | 10 | 10 | 100% |
| `form` | 9 | 10 | 90% |
| `handwritten` | 10 | 10 | 100% |
| `invoice` | 10 | 10 | 100% |
| `letter` | 10 | 10 | 100% |
| `memo` | 10 | 10 | 100% |
| `news_article` | 9 | 9 | 100% |
| `presentation` | 10 | 10 | 100% |
| `questionnaire` | 10 | 10 | 100% |
| `resume` | 10 | 10 | 100% |
| `scientific_publication` | 11 | 11 | 100% |
| `scientific_report` | 10 | 10 | 100% |
| `specification` | 10 | 10 | 100% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v11_8_reasoning_160_t0_3.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v11_8_reasoning_160_t0_3.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v11_8_reasoning_160_t0_3.md)
