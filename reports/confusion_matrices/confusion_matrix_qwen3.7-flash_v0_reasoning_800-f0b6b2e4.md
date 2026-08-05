# Confusion Matrix — qwen3.7-flash_v0_reasoning_800-f0b6b2e4

**Overall Accuracy:** 66.1% (529/800)  
**Dataset:** rvl_cdip_800  
**Model:** `qwen/qwen3.7-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v0_reasoning_800-f0b6b2e4.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | `__inva` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **47** | . | . | . | 2 | . | . | . | . | . | . | . | . | . | . | 1 | . | 50 | 94% |
| `budget` | 1 | **12** | . | . | 12 | . | 7 | . | . | . | . | . | . | . | 2 | . | 16 | 50 | 24% |
| `email` | . | . | **48** | . | . | . | . | . | . | . | . | . | . | . | . | . | 2 | 50 | 96% |
| `file_folder` | 4 | . | . | **35** | 5 | 3 | . | . | . | . | 2 | . | . | . | . | . | 1 | 50 | 70% |
| `form` | . | . | . | . | **38** | 1 | . | 2 | 1 | . | . | . | . | . | . | . | 8 | 50 | 76% |
| `handwritten` | 5 | . | . | . | 1 | **21** | . | 4 | 1 | . | . | . | . | . | . | . | 18 | 50 | 42% |
| `invoice` | . | . | . | . | 11 | 1 | **28** | . | 1 | . | . | . | . | . | . | . | 9 | 50 | 56% |
| `letter` | . | . | . | . | . | . | . | **37** | 11 | . | . | . | . | . | . | . | 2 | 50 | 74% |
| `memo` | . | . | . | . | 1 | . | . | . | **48** | . | . | . | . | . | . | . | 1 | 50 | 96% |
| `news_article` | 2 | . | . | . | 1 | . | . | . | 1 | **42** | . | . | . | 2 | 1 | . | 1 | 50 | 84% |
| `presentation` | 1 | . | . | 4 | 1 | 1 | . | 1 | 4 | 5 | **15** | . | . | . | 2 | . | 16 | 50 | 30% |
| `questionnaire` | . | . | . | . | 8 | 2 | . | 3 | . | . | . | **24** | . | 1 | 3 | . | 9 | 50 | 48% |
| `resume` | 1 | . | . | . | 12 | . | . | . | . | 1 | . | . | **33** | . | . | . | 3 | 50 | 66% |
| `scientific_publication` | . | . | . | 1 | 1 | . | . | . | . | 3 | . | . | . | **44** | 1 | . | . | 50 | 88% |
| `scientific_report` | 1 | 1 | . | . | 3 | 2 | . | . | 1 | . | . | . | . | 6 | **30** | . | 6 | 50 | 60% |
| `specification` | . | . | . | . | 14 | . | . | . | . | . | . | . | . | . | 3 | **27** | 6 | 50 | 54% |
| `__invalid__` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `handwritten` | `__invalid__` | 18 |
| `budget` | `__invalid__` | 16 |
| `presentation` | `__invalid__` | 16 |
| `specification` | `form` | 14 |
| `budget` | `form` | 12 |
| `resume` | `form` | 12 |
| `invoice` | `form` | 11 |
| `letter` | `memo` | 11 |
| `invoice` | `__invalid__` | 9 |
| `questionnaire` | `__invalid__` | 9 |
| `form` | `__invalid__` | 8 |
| `questionnaire` | `form` | 8 |
| `budget` | `invoice` | 7 |
| `scientific_report` | `scientific_publication` | 6 |
| `scientific_report` | `__invalid__` | 6 |
| `specification` | `__invalid__` | 6 |
| `file_folder` | `form` | 5 |
| `handwritten` | `advertisement` | 5 |
| `presentation` | `news_article` | 5 |
| `file_folder` | `advertisement` | 4 |
