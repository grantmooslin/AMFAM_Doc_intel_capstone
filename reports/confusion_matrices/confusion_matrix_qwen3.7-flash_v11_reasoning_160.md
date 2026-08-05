# Confusion Matrix — qwen3.7-flash_v11_reasoning_160

**Overall Accuracy:** 98.7% (156/158)  
**Dataset:** fixed_size_sampled  
**Model:** `qwen/qwen3.7-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v11_reasoning_160.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **9** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 9 | 100% |
| `budget` | . | **9** | . | . | . | . | 1 | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `email` | . | . | **9** | . | . | . | . | . | . | . | . | . | . | . | . | . | 9 | 100% |
| `file_folder` | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `form` | . | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `handwritten` | . | . | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `invoice` | . | 1 | . | . | . | . | **9** | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `letter` | . | . | . | . | . | . | . | **10** | . | . | . | . | . | . | . | . | 10 | 100% |
| `memo` | . | . | . | . | . | . | . | . | **10** | . | . | . | . | . | . | . | 10 | 100% |
| `news_article` | . | . | . | . | . | . | . | . | . | **9** | . | . | . | . | . | . | 9 | 100% |
| `presentation` | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | . | . | 10 | 100% |
| `questionnaire` | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | . | 10 | 100% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | 10 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | . | . | . | . | **11** | . | . | 11 | 100% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | 10 | 100% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **10** | 10 | 100% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `budget` | `invoice` | 1 |
| `invoice` | `budget` | 1 |
