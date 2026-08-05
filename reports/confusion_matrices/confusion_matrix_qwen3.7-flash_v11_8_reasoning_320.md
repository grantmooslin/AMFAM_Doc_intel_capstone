# Confusion Matrix — qwen3.7-flash_v11_8_reasoning_320

**Overall Accuracy:** 87.1% (277/318)  
**Dataset:** fixed_size_sampled_320  
**Model:** `qwen/qwen3.7-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v11_8_reasoning_320.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | `__inva` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **16** | . | . | . | 2 | . | . | . | . | . | . | . | . | . | . | . | . | 18 | 89% |
| `budget` | . | **16** | . | . | 1 | . | 2 | . | . | . | . | . | . | . | 1 | . | . | 20 | 80% |
| `email` | . | . | **20** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 20 | 100% |
| `file_folder` | . | . | . | **17** | . | . | . | . | . | . | 3 | . | . | . | . | . | . | 20 | 85% |
| `form` | . | . | . | 1 | **17** | . | 1 | . | . | . | . | . | . | . | . | 1 | . | 20 | 85% |
| `handwritten` | 1 | . | . | . | . | **18** | . | 1 | . | . | . | . | . | . | . | . | . | 20 | 90% |
| `invoice` | . | 1 | . | . | 3 | . | **16** | . | . | . | . | . | . | . | . | . | . | 20 | 80% |
| `letter` | . | . | . | . | . | . | . | **15** | 5 | . | . | . | . | . | . | . | . | 20 | 75% |
| `memo` | . | . | . | . | . | . | . | . | **20** | . | . | . | . | . | . | . | . | 20 | 100% |
| `news_article` | 2 | . | . | . | . | . | . | . | . | **18** | . | . | . | . | . | . | . | 20 | 90% |
| `presentation` | . | . | . | 2 | 1 | . | . | . | 1 | . | **16** | . | . | . | . | . | . | 20 | 80% |
| `questionnaire` | . | . | . | . | . | 1 | . | . | 1 | . | . | **17** | . | . | 1 | . | . | 20 | 85% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **20** | . | . | . | . | 20 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 2 | . | . | . | **17** | 1 | . | . | 20 | 85% |
| `scientific_report` | . | . | . | . | 4 | . | . | . | . | . | . | . | . | . | **16** | . | . | 20 | 80% |
| `specification` | . | . | . | . | 2 | . | . | . | . | . | . | . | . | . | . | **18** | . | 20 | 90% |
| `__invalid__` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `letter` | `memo` | 5 |
| `scientific_report` | `form` | 4 |
| `file_folder` | `presentation` | 3 |
| `invoice` | `form` | 3 |
| `advertisement` | `form` | 2 |
| `budget` | `invoice` | 2 |
| `news_article` | `advertisement` | 2 |
| `presentation` | `file_folder` | 2 |
| `scientific_publication` | `news_article` | 2 |
| `specification` | `form` | 2 |
| `budget` | `form` | 1 |
| `budget` | `scientific_report` | 1 |
| `form` | `file_folder` | 1 |
| `form` | `invoice` | 1 |
| `form` | `specification` | 1 |
| `handwritten` | `advertisement` | 1 |
| `handwritten` | `letter` | 1 |
| `invoice` | `budget` | 1 |
| `presentation` | `form` | 1 |
| `presentation` | `memo` | 1 |
