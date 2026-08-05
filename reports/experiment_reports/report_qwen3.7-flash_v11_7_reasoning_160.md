# Braintrust Experiment Report — qwen3.7-flash_v11_7_reasoning_160

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v11.7`  
**Dataset:** `fixed_size_sampled` (10 per class × 16 classes = 159 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **98.11%** (156/159) |
| Prompt tokens (avg) | 11,779.1 |
| Prompt cached tokens (avg) | 7,415.1 |
| Completion tokens (avg) | 1,726.8 |
| Completion reasoning tokens (avg) | 1,390.1 |
| Total tokens (avg) | 13,505.9 |
| Time to first token (avg) | 40.11s |
| Duration (avg) | 0.00s |
| Errors | 1 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 1,872,879 |
| Total completion tokens (measured) | 274,556 |
| Total tokens (measured) | 2,147,435 |
| **Expected cost** (list price × measured tokens) | **$0.0919** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.0627** |
| Difference (expected − actual) | $+0.0292 (+31.8%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.46 | $0.32 |
| 25,000 | $14.45 | $9.86 |
| 320,000 | $184.91 | $126.17 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v11_7_reasoning_160.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 9 | 9 | 100% |
| `budget` | 9 | 10 | 90% |
| `email` | 10 | 10 | 100% |
| `file_folder` | 10 | 10 | 100% |
| `form` | 9 | 10 | 90% |
| `handwritten` | 10 | 10 | 100% |
| `invoice` | 10 | 10 | 100% |
| `letter` | 9 | 10 | 90% |
| `memo` | 10 | 10 | 100% |
| `news_article` | 9 | 9 | 100% |
| `presentation` | 10 | 10 | 100% |
| `questionnaire` | 10 | 10 | 100% |
| `resume` | 10 | 10 | 100% |
| `scientific_publication` | 11 | 11 | 100% |
| `scientific_report` | 10 | 10 | 100% |
| `specification` | 10 | 10 | 100% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v11_7_reasoning_160.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v11_7_reasoning_160.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v11_7_reasoning_160.md)
