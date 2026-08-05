# Braintrust Experiment Report — qwen3.7-flash_v11_smoke_full

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v11`  
**Dataset:** `qwen_misclassification_smoke_v1_v11` (misclassification smoke set: one image per v1–v11 miss, 239 rows; 238 scored)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **87.71%** (207/236) |
| Prompt tokens (avg) | 11,155.8 |
| Prompt cached tokens (avg) | 8,922.0 |
| Completion tokens (avg) | 2,040.0 |
| Completion reasoning tokens (avg) | 1,694.0 |
| Total tokens (avg) | 13,195.8 |
| Time to first token (avg) | 47.56s |
| Duration (avg) | 0.00s |
| Errors | 1 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 2,632,765 |
| Total completion tokens (measured) | 481,434 |
| Total tokens (measured) | 3,114,199 |
| **Expected cost** (list price × measured tokens) | **$0.1416** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.0906** |
| Difference (expected − actual) | $+0.0510 (+36.0%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.48 | $0.31 |
| 25,000 | $15.00 | $9.60 |
| 320,000 | $191.96 | $122.85 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v11_smoke_full.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 10 | 10 | 100% |
| `budget` | 29 | 39 | 74% |
| `email` | 0 | 0 | — |
| `file_folder` | 7 | 7 | 100% |
| `form` | 16 | 17 | 94% |
| `handwritten` | 12 | 12 | 100% |
| `invoice` | 34 | 40 | 85% |
| `letter` | 2 | 4 | 50% |
| `memo` | 7 | 7 | 100% |
| `news_article` | 6 | 16 | 38% |
| `presentation` | 25 | 25 | 100% |
| `questionnaire` | 23 | 23 | 100% |
| `resume` | 7 | 7 | 100% |
| `scientific_publication` | 6 | 6 | 100% |
| `scientific_report` | 22 | 22 | 100% |
| `specification` | 1 | 1 | 100% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v11_smoke_full.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v11_smoke_full.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v11_smoke_full.md)
