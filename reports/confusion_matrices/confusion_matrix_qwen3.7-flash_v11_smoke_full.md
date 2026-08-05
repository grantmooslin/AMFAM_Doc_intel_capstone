# Confusion Matrix — qwen3.7-flash_v11_smoke_full

**Overall Accuracy:** 87.7% (207/236)  
**Dataset:** qwen_misclassification_smoke_v1_v11  
**Model:** `qwen/qwen3.7-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v11_smoke_full.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `budget` | . | **29** | . | . | 6 | . | 4 | . | . | . | . | . | . | . | . | . | 39 | 74% |
| `email` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |
| `file_folder` | . | . | . | **7** | . | . | . | . | . | . | . | . | . | . | . | . | 7 | 100% |
| `form` | . | . | . | . | **16** | . | . | . | . | . | 1 | . | . | . | . | . | 17 | 94% |
| `handwritten` | . | . | . | . | . | **12** | . | . | . | . | . | . | . | . | . | . | 12 | 100% |
| `invoice` | . | 6 | . | . | . | . | **34** | . | . | . | . | . | . | . | . | . | 40 | 85% |
| `letter` | . | . | . | . | . | . | . | **2** | 2 | . | . | . | . | . | . | . | 4 | 50% |
| `memo` | . | . | . | . | . | . | . | . | **7** | . | . | . | . | . | . | . | 7 | 100% |
| `news_article` | . | . | . | . | . | . | . | . | . | **6** | . | . | . | 10 | . | . | 16 | 38% |
| `presentation` | . | . | . | . | . | . | . | . | . | . | **25** | . | . | . | . | . | 25 | 100% |
| `questionnaire` | . | . | . | . | . | . | . | . | . | . | . | **23** | . | . | . | . | 23 | 100% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **7** | . | . | . | 7 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | . | . | . | . | **6** | . | . | 6 | 100% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **22** | . | 22 | 100% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **1** | 1 | 100% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `news_article` | `scientific_publication` | 10 |
| `budget` | `form` | 6 |
| `invoice` | `budget` | 6 |
| `budget` | `invoice` | 4 |
| `letter` | `memo` | 2 |
| `form` | `presentation` | 1 |
