# Confusion Matrix — qwen3.7-flash_v14_reasoning_160_v2_retry

**Overall Accuracy:** 85.0% (136/160)
**Dataset:** fixed_size_sampled_v2
**Model:** `qwen/qwen3.7-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v14_reasoning_160_v2_retry.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | `__inva` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `budget` | . | **4** | . | . | 1 | . | 3 | . | . | . | 1 | . | . | . | 1 | . | . | 10 | 40% |
| `email` | . | . | **9** | . | 1 | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `file_folder` | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `form` | . | . | . | 1 | **7** | . | . | . | 1 | . | . | . | . | . | . | 1 | . | 10 | 70% |
| `handwritten` | . | . | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `invoice` | . | 2 | . | . | 3 | . | **5** | . | . | . | . | . | . | . | . | . | . | 10 | 50% |
| `letter` | . | . | . | . | . | 1 | . | **8** | 1 | . | . | . | . | . | . | . | . | 10 | 80% |
| `memo` | . | . | . | . | . | . | . | . | **10** | . | . | . | . | . | . | . | . | 10 | 100% |
| `news_article` | 1 | . | . | . | . | . | . | . | . | **9** | . | . | . | . | . | . | . | 10 | 90% |
| `presentation` | . | . | . | . | . | . | . | . | . | . | **9** | . | . | . | 1 | . | . | 10 | 90% |
| `questionnaire` | . | . | . | . | 1 | . | . | . | . | . | 1 | **8** | . | . | . | . | . | 10 | 80% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | . | 10 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | . | . | . | . | **9** | 1 | . | . | 10 | 90% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | 1 | . | . | . | **9** | . | . | 10 | 90% |
| `specification` | . | . | . | . | 1 | . | . | . | . | . | . | . | . | . | . | **9** | . | 10 | 90% |
| `__invalid__` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `budget` | `invoice` | 3 |
| `invoice` | `form` | 3 |
| `invoice` | `budget` | 2 |
| `budget` | `form` | 1 |
| `budget` | `presentation` | 1 |
| `budget` | `scientific_report` | 1 |
| `email` | `form` | 1 |
| `form` | `file_folder` | 1 |
| `form` | `memo` | 1 |
| `form` | `specification` | 1 |
| `letter` | `handwritten` | 1 |
| `letter` | `memo` | 1 |
| `news_article` | `advertisement` | 1 |
| `presentation` | `scientific_report` | 1 |
| `questionnaire` | `form` | 1 |
| `questionnaire` | `presentation` | 1 |
| `scientific_publication` | `scientific_report` | 1 |
| `scientific_report` | `presentation` | 1 |
| `specification` | `form` | 1 |
