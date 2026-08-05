# Braintrust Experiment Report — qwen3.5-35b-a3b_v11_8_reasoning_160

**Model:** `qwen/qwen3.5-35b-a3b`  
**Prompt version:** `v11.8`  
**Dataset:** `fixed_size_sampled` (10 per class × 16 classes = 157 images)  
**Image size:** 1024x1024  
**Reasoning:** effort=high  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **98.73%** (155/157) |
| Scored rows | 157 |
| Failed/empty rows | 3 |
| Total expected rows | 160 |
| Prompt tokens (avg) | 11,978.9 |
| Prompt cached tokens (avg) | 2,811.5 |
| Completion tokens (avg) | 2,588.2 |
| Completion reasoning tokens (avg) | 2,191.5 |
| Total tokens (avg) | 14,567.1 |
| Time to first token (avg) | 23.11s |
| Duration (avg) | 0.00s |
| Evaluation failures | 3 |

## Cost — Expected vs Actual

**List pricing:** $0.14/M input tokens, $1.0/M output tokens (`qwen/qwen3.5-35b-a3b`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 1,880,682 |
| Total completion tokens (measured) | 406,354 |
| Total tokens (measured) | 2,287,036 |
| **Expected cost** (list price × measured tokens) | **$0.6696** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.8280** |
| Difference (expected − actual) | $-0.1584 (-23.7%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $3.41 | $4.22 |
| 25,000 | $106.63 | $131.85 |
| 320,000 | $1364.89 | $1687.74 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.5-35b-a3b_v11_8_reasoning_160.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 10 | 10 | 100% |
| `budget` | 9 | 9 | 100% |
| `email` | 10 | 10 | 100% |
| `file_folder` | 10 | 10 | 100% |
| `form` | 8 | 10 | 80% |
| `handwritten` | 10 | 10 | 100% |
| `invoice` | 9 | 9 | 100% |
| `letter` | 10 | 10 | 100% |
| `memo` | 10 | 10 | 100% |
| `news_article` | 8 | 8 | 100% |
| `presentation` | 10 | 10 | 100% |
| `questionnaire` | 10 | 10 | 100% |
| `resume` | 10 | 10 | 100% |
| `scientific_publication` | 11 | 11 | 100% |
| `scientific_report` | 10 | 10 | 100% |
| `specification` | 10 | 10 | 100% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.5-35b-a3b_v11_8_reasoning_160.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.5-35b-a3b_v11_8_reasoning_160.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.5-35b-a3b_v11_8_reasoning_160.md)
