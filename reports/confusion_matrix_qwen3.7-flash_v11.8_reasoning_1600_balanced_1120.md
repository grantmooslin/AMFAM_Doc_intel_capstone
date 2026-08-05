# Confusion Matrix — qwen3.7-flash_v11.8_reasoning_1600_balanced_1120

**Overall Accuracy:** 82.6% (925/1120)  
**Dataset:** rvl_cdip_1600  
**Model:** `qwen/qwen3.7-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v11.8_reasoning_1600_balanced_1120.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | `__inva` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **57** | . | . | 2 | 3 | . | . | . | . | 1 | 7 | . | . | . | . | . | . | 70 | 81% |
| `budget` | . | **47** | . | . | 6 | . | 12 | . | . | . | 3 | . | . | . | 2 | . | . | 70 | 67% |
| `email` | 1 | . | **63** | . | 1 | . | . | . | 1 | . | 3 | 1 | . | . | . | . | . | 70 | 90% |
| `file_folder` | . | . | . | **63** | 2 | . | . | . | . | . | 5 | . | . | . | . | . | . | 70 | 90% |
| `form` | . | . | . | 2 | **61** | 1 | 1 | . | . | . | 1 | 2 | . | . | . | 2 | . | 70 | 87% |
| `handwritten` | 1 | . | . | 1 | 1 | **62** | . | . | . | . | 2 | 3 | . | . | . | . | . | 70 | 89% |
| `invoice` | . | 8 | . | . | 6 | . | **55** | 1 | . | . | . | . | . | . | . | . | . | 70 | 79% |
| `letter` | . | . | . | 1 | 2 | 2 | . | **49** | 16 | . | . | . | . | . | . | . | . | 70 | 70% |
| `memo` | . | 1 | . | . | 2 | . | . | 5 | **61** | . | . | . | . | . | . | 1 | . | 70 | 87% |
| `news_article` | 2 | . | 2 | 1 | . | . | . | . | 2 | **60** | 1 | . | . | 1 | 1 | . | . | 70 | 86% |
| `presentation` | 1 | 1 | . | 4 | 3 | 1 | . | . | 2 | 1 | **49** | . | . | . | 8 | . | . | 70 | 70% |
| `questionnaire` | . | . | . | 1 | 2 | 1 | . | . | . | . | 3 | **61** | . | . | 2 | . | . | 70 | 87% |
| `resume` | . | . | . | 1 | . | . | . | . | . | . | 1 | . | **67** | . | 1 | . | . | 70 | 96% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 4 | 1 | . | . | **59** | 6 | . | . | 70 | 84% |
| `scientific_report` | . | . | . | 3 | 7 | 3 | . | . | 1 | . | . | . | . | 2 | **50** | 4 | . | 70 | 71% |
| `specification` | . | . | . | . | 9 | . | . | . | . | . | . | . | . | . | . | **61** | . | 70 | 87% |
| `__invalid__` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `letter` | `memo` | 16 |
| `budget` | `invoice` | 12 |
| `specification` | `form` | 9 |
| `invoice` | `budget` | 8 |
| `presentation` | `scientific_report` | 8 |
| `advertisement` | `presentation` | 7 |
| `scientific_report` | `form` | 7 |
| `budget` | `form` | 6 |
| `invoice` | `form` | 6 |
| `scientific_publication` | `scientific_report` | 6 |
| `file_folder` | `presentation` | 5 |
| `memo` | `letter` | 5 |
| `presentation` | `file_folder` | 4 |
| `scientific_publication` | `news_article` | 4 |
| `scientific_report` | `specification` | 4 |
| `advertisement` | `form` | 3 |
| `budget` | `presentation` | 3 |
| `email` | `presentation` | 3 |
| `handwritten` | `questionnaire` | 3 |
| `presentation` | `form` | 3 |
