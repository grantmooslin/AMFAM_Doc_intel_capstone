# Confusion Matrix — gemini-2.5-flash-lite_v11_8_reasoning_160-d558f2bc

**Overall Accuracy:** 86.9% (139/160)  
**Dataset:** fixed_size_sampled  
**Model:** `google/gemini-2.5-flash-lite`

![Confusion Matrix](confusion_matrix_gemini-2.5-flash-lite_v11_8_reasoning_160-d558f2bc.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | `__inva` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **9** | . | . | . | . | . | . | . | . | 1 | . | . | . | . | . | . | . | 10 | 90% |
| `budget` | . | **7** | . | . | . | 1 | 2 | . | . | . | . | . | . | . | . | . | . | 10 | 70% |
| `email` | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `file_folder` | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `form` | . | 1 | . | 1 | **5** | . | . | . | . | . | . | . | . | . | 1 | 2 | . | 10 | 50% |
| `handwritten` | . | . | . | . | . | **9** | . | . | . | . | . | . | . | . | . | 1 | . | 10 | 90% |
| `invoice` | . | . | . | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `letter` | . | . | . | . | . | . | . | **9** | . | . | . | . | . | . | . | 1 | . | 10 | 90% |
| `memo` | . | . | . | . | . | . | . | . | **7** | . | . | . | . | . | . | 3 | . | 10 | 70% |
| `news_article` | . | . | . | . | . | . | . | . | . | **8** | . | . | . | 1 | . | . | . | 9 | 89% |
| `presentation` | . | . | . | . | 1 | . | . | . | . | 1 | **8** | . | . | . | . | . | . | 10 | 80% |
| `questionnaire` | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | . | . | 10 | 100% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **9** | 1 | . | . | . | 10 | 90% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | . | . | . | . | **9** | 2 | . | . | 11 | 82% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **9** | 1 | . | 10 | 90% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | 10 | 100% |
| `__invalid__` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `memo` | `specification` | 3 |
| `budget` | `invoice` | 2 |
| `form` | `specification` | 2 |
| `scientific_publication` | `scientific_report` | 2 |
| `advertisement` | `news_article` | 1 |
| `budget` | `handwritten` | 1 |
| `form` | `budget` | 1 |
| `form` | `file_folder` | 1 |
| `form` | `scientific_report` | 1 |
| `handwritten` | `specification` | 1 |
| `letter` | `specification` | 1 |
| `news_article` | `scientific_publication` | 1 |
| `presentation` | `form` | 1 |
| `presentation` | `news_article` | 1 |
| `resume` | `scientific_publication` | 1 |
| `scientific_report` | `specification` | 1 |
