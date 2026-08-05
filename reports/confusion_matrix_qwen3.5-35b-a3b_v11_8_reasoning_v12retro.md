# Confusion Matrix — qwen3.5-35b-a3b_v11_8_reasoning_v12retro

**Overall Accuracy:** 30.8% (16/52)  
**Dataset:** qwen_v12_retroactive_eval  
**Model:** `qwen/qwen3.5-35b-a3b`

![Confusion Matrix](confusion_matrix_qwen3.5-35b-a3b_v11_8_reasoning_v12retro.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | `__inva` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | . | . | . | 1 | 1 | . | . | . | . | . | . | . | . | . | . | . | . | 2 | 0% |
| `budget` | . | **1** | . | . | 1 | . | 2 | . | . | . | . | . | . | . | . | . | . | 4 | 25% |
| `email` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |
| `file_folder` | . | . | . | **1** | . | . | . | . | . | . | 2 | . | . | . | . | . | . | 3 | 33% |
| `form` | . | . | . | 1 | **1** | . | 1 | . | . | . | 1 | . | . | . | . | 1 | 1 | 6 | 17% |
| `handwritten` | 1 | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 1 | 0% |
| `invoice` | . | 1 | . | . | 1 | . | **5** | . | . | . | . | . | . | . | . | . | 1 | 8 | 62% |
| `letter` | . | . | . | . | . | . | . | **1** | 5 | . | . | . | . | . | . | . | . | 6 | 17% |
| `memo` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |
| `news_article` | . | . | . | . | . | . | . | . | . | **1** | . | . | . | 1 | . | . | . | 2 | 50% |
| `presentation` | . | . | . | 2 | . | . | . | . | . | . | **2** | . | . | . | . | . | 1 | 5 | 40% |
| `questionnaire` | . | . | . | . | . | 1 | . | . | . | . | . | **1** | . | . | . | . | 1 | 3 | 33% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 2 | . | . | . | . | . | . | . | 2 | 0% |
| `scientific_report` | . | . | . | . | 4 | . | . | . | . | . | . | . | . | . | **1** | . | 1 | 6 | 17% |
| `specification` | . | . | . | . | 2 | . | . | . | . | . | . | . | . | . | . | **2** | . | 4 | 50% |
| `__invalid__` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `letter` | `memo` | 5 |
| `scientific_report` | `form` | 4 |
| `budget` | `invoice` | 2 |
| `file_folder` | `presentation` | 2 |
| `presentation` | `file_folder` | 2 |
| `scientific_publication` | `news_article` | 2 |
| `specification` | `form` | 2 |
| `advertisement` | `file_folder` | 1 |
| `advertisement` | `form` | 1 |
| `budget` | `form` | 1 |
| `form` | `file_folder` | 1 |
| `form` | `invoice` | 1 |
| `form` | `presentation` | 1 |
| `form` | `specification` | 1 |
| `form` | `__invalid__` | 1 |
| `handwritten` | `advertisement` | 1 |
| `invoice` | `budget` | 1 |
| `invoice` | `form` | 1 |
| `invoice` | `__invalid__` | 1 |
| `news_article` | `scientific_publication` | 1 |
