# Failure-Pipeline Monte Carlo

- **Primary model**: `qwen/qwen3.7-flash`
- **Fitted**: P(first success)=0.946, length=0.021, transient=0.0000, 429=0.0000, quota=0.0000
- **Config**: max_tries=3, keys=2, fallback=on

## Current-pipeline simulation

- **Failure rate**: 0.114% (observed 2.716%)
- **Average attempts per row**: 1.06

## Extrapolated failures at scale

| scale | expected | 95% CI | P(>1% failures) | P(>5% failures) |
|---:|---:|---:|---:|---:|
| 800 | 1 | 0-3 | 0.000 | 0.000 |
| 25,000 | 28 | 19-39 | 0.000 | 0.000 |
| 320,000 | 364 | 328-402 | 0.000 | 0.000 |

## Sensitivity sweep

| max_tries | fallback | simulated failure rate | avg attempts/row |
|---:|---|---:|---:|
| 1 | off | 2.940% | 1.03 |
| 1 | on | 0.114% | 1.06 |
| 2 | off | 2.862% | 1.03 |
| 2 | on | 0.114% | 1.06 |
| 3 | off | 2.862% | 1.03 |
| 3 | on | 0.114% | 1.06 |
| 5 | off | 2.862% | 1.03 |
| 5 | on | 0.114% | 1.06 |
