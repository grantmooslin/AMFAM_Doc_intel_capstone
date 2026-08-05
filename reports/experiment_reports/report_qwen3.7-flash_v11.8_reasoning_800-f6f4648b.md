# Braintrust Experiment Report — qwen3.7-flash_v11.8_reasoning_800-f6f4648b

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v11.8`  
**Dataset:** `rvl_cdip_800` (50 per class × 16 classes = 800 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **83.12%** (665/800) |
| Scored rows | 800 |
| Failed/empty rows | 0 |
| Total expected rows | 800 |
| Prompt tokens (avg) | 11,986.0 |
| Prompt cached tokens (avg) | 7,325.6 |
| Completion tokens (avg) | 1,906.5 |
| Completion reasoning tokens (avg) | 1,559.2 |
| Total tokens (avg) | 13,892.5 |
| Time to first token (avg) | 47.31s |
| Duration (avg) | 0.00s |
| Evaluation failures | 0 |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing). Cached input priced at 10% of input — this run had heavy prompt caching (7,326 avg cached tokens/image, ~61% of prompt tokens), so expected cost below applies the cache discount to cached tokens.

> Note: token/cost metrics are measured from the original run (experiment `qwen3.7-flash_v11.8_reasoning_800`); the final resume run's spans logged no usage because 797/800 rows were manifest-cache hits.

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 9,588,811 |
| &nbsp;&nbsp;of which cached (10% rate) | 5,860,992 |
| Total completion tokens (measured) | 1,524,217 |
| Total tokens (measured) | 11,113,028 |
| **Expected cost** (cache-adjusted list price × measured tokens) | **$0.3276** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.3427** |
| Difference (expected − actual) | $+0.0151 (+4.6%) |

### Scale-up projections (cache-adjusted list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.33 | $0.34 |
| 25,000 | $10.24 | $10.71 |
| 320,000 | $131.04 | $137.08 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v11.8_reasoning_800-f6f4648b.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 44 | 50 | 88% |
| `budget` | 34 | 50 | 68% |
| `email` | 48 | 50 | 96% |
| `file_folder` | 42 | 50 | 84% |
| `form` | 40 | 50 | 80% |
| `handwritten` | 44 | 50 | 88% |
| `invoice` | 36 | 50 | 72% |
| `letter` | 38 | 50 | 76% |
| `memo` | 44 | 50 | 88% |
| `news_article` | 42 | 50 | 84% |
| `presentation` | 38 | 50 | 76% |
| `questionnaire` | 45 | 50 | 90% |
| `resume` | 49 | 50 | 98% |
| `scientific_publication` | 43 | 50 | 86% |
| `scientific_report` | 34 | 50 | 68% |
| `specification` | 44 | 50 | 88% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v11.8_reasoning_800-f6f4648b.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v11.8_reasoning_800-f6f4648b.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v11.8_reasoning_800-f6f4648b.md)
