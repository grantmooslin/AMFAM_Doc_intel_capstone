# Braintrust Experiment Report — gemini-2.5-flash-lite_v11_8_reasoning_160-d558f2bc

**Model:** `google/gemini-2.5-flash-lite`  
**Prompt version:** `v11.8`  
**Dataset:** `fixed_size_sampled` (10 per class × 16 classes = 160 images)  
**Image size:** 1024x1024  
**Reasoning:** effort=max, temperature=0.2  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **86.88%** (139/160) |
| Scored rows | 160 |
| Failed/empty rows | 0 |
| Total expected rows | 160 |
| Prompt tokens (avg) | 6,591.8 |
| Prompt cached tokens (avg) | 4,372.6 |
| Completion tokens (avg) | 1,177.3 |
| Completion reasoning tokens (avg) | 1,005.3 |
| Total tokens (avg) | 7,769.1 |
| Time to first token (avg) | 6.99s |
| Duration (avg) | 0.00s |
| Evaluation failures | 0 |

## Cost — Expected vs Actual

**List pricing:** $0.1/M input tokens, $0.4/M output tokens (`google/gemini-2.5-flash-lite`, per OpenRouter model listing). Cached input priced at 10% of input (not applicable here — `cached_tokens` is 0 across the run).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 1,054,693 |
| Total completion tokens (measured) | 188,363 |
| Total tokens (measured) | 1,243,056 |
| **Expected cost** (list price × measured tokens) | **$0.1808** |
| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **$0.1134** |
| Difference (expected − actual) | $+0.0675 (+37.3%) |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.90 | $0.57 |
| 25,000 | $28.25 | $17.71 |
| 320,000 | $361.63 | $226.73 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_gemini-2.5-flash-lite_v11_8_reasoning_160-d558f2bc.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 9 | 10 | 90% |
| `budget` | 7 | 10 | 70% |
| `email` | 10 | 10 | 100% |
| `file_folder` | 10 | 10 | 100% |
| `form` | 5 | 10 | 50% |
| `handwritten` | 9 | 10 | 90% |
| `invoice` | 10 | 10 | 100% |
| `letter` | 9 | 10 | 90% |
| `memo` | 7 | 10 | 70% |
| `news_article` | 8 | 9 | 89% |
| `presentation` | 8 | 10 | 80% |
| `questionnaire` | 10 | 10 | 100% |
| `resume` | 9 | 10 | 90% |
| `scientific_publication` | 9 | 11 | 82% |
| `scientific_report` | 9 | 10 | 90% |
| `specification` | 10 | 10 | 100% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_gemini-2.5-flash-lite_v11_8_reasoning_160-d558f2bc.md)
  - [Confusion matrix heatmap](confusion_matrix_gemini-2.5-flash-lite_v11_8_reasoning_160-d558f2bc.png)
- [Misclassification reasoning traces](misclassification_reasoning_gemini-2.5-flash-lite_v11_8_reasoning_160-d558f2bc.md)
