# Final Results: qwen3.7-flash_v11.8_reasoning_1600_balanced_1120

- **Dataset**: rvl_cdip_1600
- **Model**: qwen/qwen3.7-flash
- **Prompt**: v11.8
- **Max tokens**: 8192

## Overall

- **Rows**: 1120
- **Completed**: 1120
- **Errors**: 0
- **Empty**: 0
- **exact_match**: 925/1120 (82.6%)
- **near_miss** (correct answer was the model's runner-up): 72/1120 (6.4% of rows; 36.9% of all misses)
- **runner_up coverage**: 933/1120 completed rows had a parsable runner-up

## Per-class accuracy

| Class | Correct | Total | Errors | Accuracy |
|---|---:|---:|---:|---:|
| advertisement | 57 | 70 | 0 | 81.4% |
| budget | 47 | 70 | 0 | 67.1% |
| email | 63 | 70 | 0 | 90.0% |
| file_folder | 63 | 70 | 0 | 90.0% |
| form | 61 | 70 | 0 | 87.1% |
| handwritten | 62 | 70 | 0 | 88.6% |
| invoice | 55 | 70 | 0 | 78.6% |
| letter | 49 | 70 | 0 | 70.0% |
| memo | 61 | 70 | 0 | 87.1% |
| news_article | 60 | 70 | 0 | 85.7% |
| presentation | 49 | 70 | 0 | 70.0% |
| questionnaire | 61 | 70 | 0 | 87.1% |
| resume | 67 | 70 | 0 | 95.7% |
| scientific_publication | 59 | 70 | 0 | 84.3% |
| scientific_report | 50 | 70 | 0 | 71.4% |
| specification | 61 | 70 | 0 | 87.1% |

## Near-miss rows (correct answer was the model's runner-up)

These rows were misclassified but the model named the correct class as its
second choice in the reasoning trace — the closest possible misses.

- `rvl_cdip__advertisement__0003.png`
- `rvl_cdip__advertisement__0064.png`
- `rvl_cdip__advertisement__0093.png`
- `rvl_cdip__advertisement__0094.png`
- `rvl_cdip__budget__0001.png`
- `rvl_cdip__budget__0028.png`
- `rvl_cdip__budget__0040.png`
- `rvl_cdip__budget__0041.png`
- `rvl_cdip__budget__0050.png`
- `rvl_cdip__budget__0053.png`
- `rvl_cdip__budget__0079.png`
- `rvl_cdip__budget__0091.png`
- `rvl_cdip__budget__0094.png`
- `rvl_cdip__budget__0100.png`
- `rvl_cdip__file_folder__0002.png`
- `rvl_cdip__file_folder__0027.png`
- `rvl_cdip__file_folder__0075.png`
- `rvl_cdip__file_folder__0098.png`
- `rvl_cdip__form__0045.png`
- `rvl_cdip__form__0075.png`
- `rvl_cdip__handwritten__0025.png`
- `rvl_cdip__invoice__0015.png`
- `rvl_cdip__invoice__0029.png`
- `rvl_cdip__invoice__0032.png`
- `rvl_cdip__invoice__0035.png`
- `rvl_cdip__invoice__0045.png`
- `rvl_cdip__invoice__0046.png`
- `rvl_cdip__invoice__0062.png`
- `rvl_cdip__invoice__0073.png`
- `rvl_cdip__invoice__0080.png`
- `rvl_cdip__invoice__0083.png`
- `rvl_cdip__letter__0004.png`
- `rvl_cdip__letter__0012.png`
- `rvl_cdip__letter__0024.png`
- `rvl_cdip__letter__0033.png`
- `rvl_cdip__letter__0042.png`
- `rvl_cdip__letter__0067.png`
- `rvl_cdip__letter__0072.png`
- `rvl_cdip__letter__0076.png`
- `rvl_cdip__letter__0080.png`
- `rvl_cdip__letter__0091.png`
- `rvl_cdip__letter__0093.png`
- `rvl_cdip__memo__0009.png`
- `rvl_cdip__memo__0026.png`
- `rvl_cdip__memo__0027.png`
- `rvl_cdip__memo__0035.png`
- `rvl_cdip__memo__0051.png`
- `rvl_cdip__memo__0053.png`
- `rvl_cdip__news_article__0010.png`
- `rvl_cdip__news_article__0032.png`
- `rvl_cdip__presentation__0016.png`
- `rvl_cdip__presentation__0029.png`
- `rvl_cdip__presentation__0040.png`
- `rvl_cdip__presentation__0059.png`
- `rvl_cdip__presentation__0066.png`
- `rvl_cdip__presentation__0100.png`
- `rvl_cdip__scientific_publication__0003.png`
- `rvl_cdip__scientific_publication__0027.png`
- `rvl_cdip__scientific_publication__0046.png`
- `rvl_cdip__scientific_publication__0051.png`
- `rvl_cdip__scientific_publication__0075.png`
- `rvl_cdip__scientific_publication__0086.png`
- `rvl_cdip__scientific_report__0042.png`
- `rvl_cdip__scientific_report__0045.png`
- `rvl_cdip__scientific_report__0049.png`
- `rvl_cdip__scientific_report__0062.png`
- `rvl_cdip__scientific_report__0081.png`
- `rvl_cdip__scientific_report__0083.png`
- `rvl_cdip__scientific_report__0086.png`
- `rvl_cdip__scientific_report__0093.png`
- `rvl_cdip__scientific_report__0097.png`
- `rvl_cdip__specification__0049.png`
