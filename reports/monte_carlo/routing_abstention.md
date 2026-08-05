# Confidence-Gated Escalation Simulation

- **Escalated model accuracy**: 90% (assumed)
- **Escalated cost multiplier**: 3.0x

| alpha | escalated | kept | accuracy | 95% CI | cost factor |
|---:|---:|---:|---:|---:|---:|
| 1% | 15 | 1497 | 0.826 | 0.810-0.841 | 1.02x |
| 2% | 30 | 1482 | 0.831 | 0.816-0.846 | 1.04x |
| 5% | 76 | 1436 | 0.845 | 0.830-0.859 | 1.10x |
| 10% | 151 | 1361 | 0.864 | 0.850-0.878 | 1.20x |
| 15% | 227 | 1285 | 0.879 | 0.865-0.893 | 1.30x |
| 20% | 302 | 1210 | 0.891 | 0.877-0.904 | 1.40x |
| 30% | 454 | 1058 | 0.895 | 0.882-0.908 | 1.60x |
| 40% | 605 | 907 | 0.919 | 0.909-0.928 | 1.80x |
| 50% | 756 | 756 | 0.909 | 0.899-0.919 | 2.00x |

## Sensitivity to the escalated-model accuracy assumption

| alpha | accuracy @ acc-5pp | accuracy @ acc | accuracy @ acc+5pp |
|---:|---:|---:|---:|
| 1% | 0.826 | 0.826 | 0.827 |
| 2% | 0.830 | 0.831 | 0.832 |
| 5% | 0.842 | 0.845 | 0.847 |
| 10% | 0.859 | 0.864 | 0.869 |
| 15% | 0.872 | 0.879 | 0.887 |
| 20% | 0.881 | 0.891 | 0.901 |
| 30% | 0.880 | 0.895 | 0.910 |
| 40% | 0.899 | 0.919 | 0.939 |
| 50% | 0.884 | 0.909 | 0.934 |

## Baseline (no escalation)

Observed single-pass accuracy: **0.821** at cost 1.0x.

## How to use

Pick the smallest alpha whose accuracy meets the target; escalate the filenames in ``escalation_candidates.txt`` (top alpha fraction) through the stronger model and compare the measured vs simulated accuracy.
