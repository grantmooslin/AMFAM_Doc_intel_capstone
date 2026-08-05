# Confusion Matrix — qwen3.7-flash_v11_reasoning_320

**Overall Accuracy:** 83.8% (264/315)  
**Dataset:** fixed_size_sampled_320  
**Model:** `qwen/qwen3.7-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v11_reasoning_320.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **18** | . | . | . | 2 | . | . | . | . | . | . | . | . | . | . | . | 20 | 90% |
| `budget` | . | **13** | . | . | 4 | . | 2 | . | . | . | . | . | . | . | 1 | . | 20 | 65% |
| `email` | . | . | **20** | . | . | . | . | . | . | . | . | . | . | . | . | . | 20 | 100% |
| `file_folder` | . | . | . | **18** | . | . | . | . | . | . | 2 | . | . | . | . | . | 20 | 90% |
| `form` | . | . | . | 1 | **14** | . | 2 | 1 | . | . | . | . | . | . | . | 2 | 20 | 70% |
| `handwritten` | 1 | . | . | . | . | **19** | . | . | . | . | . | . | . | . | . | . | 20 | 95% |
| `invoice` | . | 2 | . | . | 3 | . | **15** | . | . | . | . | . | . | . | . | . | 20 | 75% |
| `letter` | . | . | . | . | . | . | . | **15** | 5 | . | . | . | . | . | . | . | 20 | 75% |
| `memo` | . | . | . | . | 1 | . | . | . | **19** | . | . | . | . | . | . | . | 20 | 95% |
| `news_article` | 1 | . | . | . | 1 | . | . | . | . | **15** | . | . | . | . | . | . | 17 | 88% |
| `presentation` | . | . | . | 2 | 3 | . | . | . | 1 | . | **14** | . | . | . | . | . | 20 | 70% |
| `questionnaire` | . | . | . | . | . | 1 | . | . | . | . | 1 | **17** | . | . | 1 | . | 20 | 85% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **20** | . | . | . | 20 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 2 | . | . | . | **18** | . | . | 20 | 90% |
| `scientific_report` | . | . | . | . | 3 | 1 | . | . | . | . | . | . | . | . | **14** | . | 18 | 78% |
| `specification` | . | . | . | . | 5 | . | . | . | . | . | . | . | . | . | . | **15** | 20 | 75% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `letter` | `memo` | 5 |
| `specification` | `form` | 5 |
| `budget` | `form` | 4 |
| `invoice` | `form` | 3 |
| `presentation` | `form` | 3 |
| `scientific_report` | `form` | 3 |
| `advertisement` | `form` | 2 |
| `budget` | `invoice` | 2 |
| `file_folder` | `presentation` | 2 |
| `form` | `invoice` | 2 |
| `form` | `specification` | 2 |
| `invoice` | `budget` | 2 |
| `presentation` | `file_folder` | 2 |
| `scientific_publication` | `news_article` | 2 |
| `budget` | `scientific_report` | 1 |
| `form` | `file_folder` | 1 |
| `form` | `letter` | 1 |
| `handwritten` | `advertisement` | 1 |
| `memo` | `form` | 1 |
| `news_article` | `advertisement` | 1 |
