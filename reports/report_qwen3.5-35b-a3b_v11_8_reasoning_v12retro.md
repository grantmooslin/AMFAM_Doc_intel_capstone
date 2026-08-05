# Braintrust Experiment Report — qwen3.5-35b-a3b_v11_8_reasoning_v12retro

**Model:** `qwen/qwen3.5-35b-a3b`  
**Prompt version:** `v11.8`  
**Dataset:** `qwen_v12_retroactive_eval` (3 per class × 16 classes = 52 images)  
**Image size:** 1024x1024  
**Reasoning:** effort=high  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **30.77%** (16/52) |
| Scored rows | 52 |
| Failed/empty rows | 0 |
| Total expected rows | 52 |
| Prompt tokens (avg) | 11,989.0 |
| Prompt cached tokens (avg) | 10,600.6 |
| Completion tokens (avg) | 5,034.0 |
| Completion reasoning tokens (avg) | 4,561.3 |
| Total tokens (avg) | 17,023.0 |
| Time to first token (avg) | 40.09s |
| Duration (avg) | 0.00s |
| Evaluation failures | 0 |

## Cost — Expected vs Actual

**List pricing:** $0.14/M input tokens, $1.0/M output tokens (`qwen/qwen3.5-35b-a3b`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 623,428 |
| Total completion tokens (measured) | 261,770 |
| Total tokens (measured) | 885,198 |
| **Expected cost** (list price × measured tokens) | **$0.3490** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.4359** |
| Difference (expected − actual) | $-0.0869 (-24.9%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $5.37 | $6.71 |
| 25,000 | $167.81 | $209.57 |
| 320,000 | $2148.00 | $2682.48 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.5-35b-a3b_v11_8_reasoning_v12retro.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 0 | 2 | 0% |
| `budget` | 1 | 4 | 25% |
| `email` | 0 | 0 | — |
| `file_folder` | 1 | 3 | 33% |
| `form` | 1 | 6 | 17% |
| `handwritten` | 0 | 1 | 0% |
| `invoice` | 5 | 8 | 62% |
| `letter` | 1 | 6 | 17% |
| `memo` | 0 | 0 | — |
| `news_article` | 1 | 2 | 50% |
| `presentation` | 2 | 5 | 40% |
| `questionnaire` | 1 | 3 | 33% |
| `resume` | 0 | 0 | — |
| `scientific_publication` | 0 | 2 | 0% |
| `scientific_report` | 1 | 6 | 17% |
| `specification` | 2 | 4 | 50% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.5-35b-a3b_v11_8_reasoning_v12retro.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.5-35b-a3b_v11_8_reasoning_v12retro.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.5-35b-a3b_v11_8_reasoning_v12retro.md)
