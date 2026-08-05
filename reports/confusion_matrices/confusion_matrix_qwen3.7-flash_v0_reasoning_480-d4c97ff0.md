# Confusion Matrix — qwen3.7-flash_v0_reasoning_480-d4c97ff0

**Overall Accuracy:** 69.2% (332/480)  
**Dataset:** 2550×3300 padded PNGs, 50 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v0_reasoning_480-d4c97ff0.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **28** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 1 | 29 | 97% |
| `budget` | 1 | **13** | . | . | 9 | 2 | 2 | . | . | . | . | . | . | . | 1 | . | 28 | 46% |
| `email` | . | . | **28** | . | . | . | . | . | 2 | . | . | . | . | . | . | . | 30 | 93% |
| `file_folder` | 1 | . | . | **24** | 3 | . | . | . | . | . | 1 | . | . | . | . | . | 29 | 83% |
| `form` | . | . | . | . | **22** | . | . | 1 | 1 | . | . | . | . | . | 3 | 1 | 28 | 79% |
| `handwritten` | 3 | . | 1 | . | 3 | **16** | . | 5 | 1 | . | . | . | . | . | 1 | . | 30 | 53% |
| `invoice` | 1 | . | . | . | 10 | . | **17** | 1 | 1 | . | . | . | . | . | . | . | 30 | 57% |
| `letter` | . | . | . | . | . | . | . | **21** | 8 | . | . | . | . | . | . | . | 29 | 72% |
| `memo` | . | . | . | . | . | . | . | . | **30** | . | . | . | . | . | . | . | 30 | 100% |
| `news_article` | 1 | . | . | . | . | . | . | . | 1 | **24** | . | . | . | 2 | 1 | . | 29 | 83% |
| `presentation` | 2 | . | . | 3 | 1 | 1 | . | 1 | 3 | 6 | **11** | . | . | . | . | . | 28 | 39% |
| `questionnaire` | . | . | . | . | 5 | 2 | . | 2 | . | . | . | **17** | . | . | 4 | . | 30 | 57% |
| `resume` | . | . | . | . | 9 | . | . | . | . | . | . | . | **18** | 1 | . | . | 28 | 64% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 2 | . | . | . | **28** | . | . | 30 | 93% |
| `scientific_report` | . | . | . | . | 3 | . | . | 1 | 1 | . | . | . | . | 5 | **18** | . | 28 | 64% |
| `specification` | . | . | . | . | 8 | . | . | . | 1 | . | . | . | . | . | 2 | **17** | 28 | 61% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `invoice` | `form` | 10 |
| `budget` | `form` | 9 |
| `resume` | `form` | 9 |
| `letter` | `memo` | 8 |
| `specification` | `form` | 8 |
| `presentation` | `news_article` | 6 |
| `handwritten` | `letter` | 5 |
| `questionnaire` | `form` | 5 |
| `scientific_report` | `scientific_publication` | 5 |
| `questionnaire` | `scientific_report` | 4 |
| `file_folder` | `form` | 3 |
| `form` | `scientific_report` | 3 |
| `handwritten` | `advertisement` | 3 |
| `handwritten` | `form` | 3 |
| `presentation` | `file_folder` | 3 |
| `presentation` | `memo` | 3 |
| `scientific_report` | `form` | 3 |
| `budget` | `handwritten` | 2 |
| `budget` | `invoice` | 2 |
| `email` | `memo` | 2 |
