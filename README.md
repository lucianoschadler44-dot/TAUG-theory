# TAUG: Tensor-Altered Unified Gravity

**A DHOST-Ia scalar-tensor theory with Fibonacci parameters resolving the S₈ tension**

[![arXiv](https://img.shields.io/badge/arXiv-2026.XXXXX-b31b1b.svg)](https://arxiv.org/abs/2026.XXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

TAUG is a cosmological scalar-tensor theory within the DHOST-Ia class (GLPV subset) characterized by:
```
L = K(φ,X) + R + (1/32X²)L₃ + A₄(X)L₄ + A₅(X)L₅
```

All parameters derive from Fibonacci numbers {F₅, F₆, F₇} = {5, 8, 13}:

| Parameter | Value | Expression |
|-----------|-------|------------|
| αH | 1/8 = 0.125 | Beyond-Horndeski (1/F₆) |
| αB | 1/16 = 0.0625 | Braiding (αH/2) |
| αT | 0 | Tensor speed = c |
| αM | 3/16 = 0.1875 | Running Planck mass |
| β₁ | -1/16 | No graviton decay (αH+2β₁=0) |
| cs² | 193/388 ≈ 0.497 | Subluminal propagation |

## Key Predictions (Exact Fractions)

| Observable | TAUG | GR | Deviation |
|-----------|------|-----|-----------|
| μ_Ψ (Poisson) | 254/289 ≈ 0.879 | 1.000 | -12.1% |
| η = Φ/Ψ (slip) | 23/17 ≈ 1.353 | 1.000 | +35.3% |
| Σ (lensing) | 5080/4913 ≈ 1.034 | 1.000 | +3.4% |
| σ₈ | 0.763 | 0.812 | -6.0% |

## Smoking Gun: Euclid 2027

η = 23/17 = 1.353 is a **binary, falsifiable prediction**.
- If Euclid measures η ≈ 1.35 → post-Einstein gravity confirmed
- If Euclid measures η = 1.00 → TAUG definitively refuted

## MCMC Validation

9 independent MCMC chains (CamSpec2021 TTTEEE + emcee + cobaya) all find αH = 0.125 within 1σ:

| Chain | αH | σ | Tension |
|-------|-----|---|---------|
| P0 (TTTEEE full) | 0.1267 | 0.052 | 0.03σ |
| Combined (8 chains) | 0.136 | 0.013 | 0.84σ |

## S₈ Tension Resolution

TAUG resolves the S₈ tension (Planck vs DES/KiDS) from 3.5σ to 0.3σ **structurally** — not by parameter tuning.

## Requirements

- Python 3.10+ (numpy, scipy, sympy, emcee, cobaya)
- EFTCAMB (included in `code/`)
- Julia 1.9+ (optional, for BigFloat verification)

## Citation
```bibtex
@article{Schadler2026TAUG,
  author  = {Schadler, Luciano Andrey},
  title   = {TAUG: DHOST-Ia Scalar-Tensor Theory with Fibonacci Parameters},
  year    = {2026},
  journal = {arXiv preprint},
}
```

## License

MIT License. See [LICENSE](LICENSE).

## Contact

Luciano Andrey Schadler — lucianoschadler44@gmail.com
Schadler Tech | FAG Centro Universitário, Cascavel-PR, Brazil

## S26 Update (31 March 2026)

**New results since initial submission:**
- `σ₈(αH)` scan: 21 EFTCAMB points, `σ₈ = 0.817 − 0.402αH` (R²>0.999)
- **Key finding:** A₄_TAUG ≠ −A₃ → TAUG is genuinely DHOST-Ia (not GLPV)
  - This A₄ deviation is precisely what produces η=23/17 vs η≈1.13 (GLPV)
- η=23/17 confirmed algebraically: `2Σ/μΨ−1 = 23/17` (exact)
- μ₀=−0.121 within Planck 2020 at **0.27σ** (Frusciante+2025)
- CFT hierarchy mapped: M(3,4)→M(4,5)→M(5,6)→M(6,7)
- TAUGb [M(4,5), αH=1/10] identified as sister theory
- Euclid SNR forecast: SNR(η)=11.8σ (optimistic), SNR(μ₀)=12.1σ

**Papers analyzed:** LMNV 2017, Bellini+Sawicki 2014, Langlois 2018, BPZ 1984,
Charmousis+2019, Hirano+2019, DESI 2024, Euclid Frusciante+2025.
