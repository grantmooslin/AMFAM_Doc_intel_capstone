# Confusion Matrix — qwen3.7-flash_v11.8_reasoning_800-f6f4648b

**Overall Accuracy:** 83.1% (665/800)  
**Dataset:** rvl_cdip_800  
**Model:** `qwen/qwen3.7-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v11.8_reasoning_800-f6f4648b.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | `__inva` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **44** | . | . | 1 | 1 | . | . | . | . | . | 4 | . | . | . | . | . | . | 50 | 88% |
| `budget` | . | **34** | . | . | 2 | . | 13 | . | 1 | . | . | . | . | . | . | . | . | 50 | 68% |
| `email` | . | . | **48** | . | 1 | . | . | . | . | . | 1 | . | . | . | . | . | . | 50 | 96% |
| `file_folder` | . | . | . | **42** | 2 | 1 | . | . | . | . | 5 | . | . | . | . | . | . | 50 | 84% |
| `form` | . | . | . | 2 | **40** | 1 | 2 | 1 | 1 | . | . | 2 | . | . | . | 1 | . | 50 | 80% |
| `handwritten` | 1 | . | . | . | 1 | **44** | . | . | . | . | 2 | 1 | . | . | 1 | . | . | 50 | 88% |
| `invoice` | . | 7 | . | . | 6 | 1 | **36** | . | . | . | . | . | . | . | . | . | . | 50 | 72% |
| `letter` | . | 1 | . | . | . | 1 | . | **38** | 10 | . | . | . | . | . | . | . | . | 50 | 76% |
| `memo` | . | . | 1 | . | 3 | . | . | 2 | **44** | . | . | . | . | . | . | . | . | 50 | 88% |
| `news_article` | 2 | . | . | . | 1 | . | . | . | 1 | **42** | . | . | . | 1 | 1 | . | 2 | 50 | 84% |
| `presentation` | . | 1 | . | 3 | 1 | 1 | . | . | 3 | . | **38** | . | . | . | 3 | . | . | 50 | 76% |
| `questionnaire` | . | . | . | . | . | 1 | . | . | 1 | . | 2 | **45** | . | . | 1 | . | . | 50 | 90% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **49** | . | . | . | 1 | 50 | 98% |
| `scientific_publication` | . | . | . | 1 | . | . | . | . | . | 3 | 1 | . | . | **43** | 2 | . | . | 50 | 86% |
| `scientific_report` | . | . | . | . | 6 | 2 | . | . | 1 | . | 1 | . | . | 2 | **34** | 4 | . | 50 | 68% |
| `specification` | . | . | . | . | 5 | . | . | . | . | 1 | . | . | . | . | . | **44** | . | 50 | 88% |
| `__invalid__` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `budget` | `invoice` | 13 |
| `letter` | `memo` | 10 |
| `invoice` | `budget` | 7 |
| `invoice` | `form` | 6 |
| `scientific_report` | `form` | 6 |
| `file_folder` | `presentation` | 5 |
| `specification` | `form` | 5 |
| `advertisement` | `presentation` | 4 |
| `scientific_report` | `specification` | 4 |
| `memo` | `form` | 3 |
| `presentation` | `file_folder` | 3 |
| `presentation` | `memo` | 3 |
| `presentation` | `scientific_report` | 3 |
| `scientific_publication` | `news_article` | 3 |
| `budget` | `form` | 2 |
| `file_folder` | `form` | 2 |
| `form` | `file_folder` | 2 |
| `form` | `invoice` | 2 |
| `form` | `questionnaire` | 2 |
| `handwritten` | `presentation` | 2 |
