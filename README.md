# TAUG: Tensor-Altered Unified Gravity

**A DHOST-Ia scalar-tensor cosmology with Fibonacci parameters and a falsifiable prediction for Euclid**

Author: Luciano Andrey Schadler (FAG Centro Universitário / Schadler Tech, Cascavel-PR, Brazil)

CREA-PR 29.232 | lucianoschadler44@gmail.com

---

## Key Results (v1.1 — Sessions S1–S31)

| Result | Value | Method |
|--------|-------|--------|
| σ₈ | 0.763 | EFTCAMB 82+ Boltzmann runs |
| αH | 1/8 = 0.125 | Fibonacci (1/F₆) |
| η = Φ/Ψ | 23/17 ≈ 1.353 | Exact algebraic |
| cs² | 193/388 | Subluminal |
| MCMC (Planck TTTEEE) | αH = 0.127 ± 0.052 | 9 chains, 9915 points |
| S₈ tension | 3.5σ → 0.3σ | Structural resolution |

## 🔴 Falsifiable Prediction — DEADLINE: October 21, 2026

**Euclid DR1** will measure gravitational slip η.

- **If η ≈ 23/17 = 1.353:** Post-Einsteinian gravity confirmed
- **If η = 1.00:** TAUG definitively refuted

There is no escape. The prediction is registered here BEFORE the data.

## Theory

TAUG is a DHOST-Ia (Degenerate Higher-Order Scalar-Tensor, Class Ia) theory in the GLPV subset. All parameters derive from Fibonacci numbers {F₅, F₆, F₇} = {5, 8, 13}:

```
αH = 1/8 = 1/F₆     (beyond-Horndeski coupling)
γ  = 5/8 = F₅/F₆    (kinetic mixing)
ν  = 5/13 = F₅/F₇   (BH ratio)
αT = 0               (GW170817 compatible)
```

Novel identity: **γ·ν = γ − ν = 25/104** (consequence of Fibonacci recursion F₇ = F₆ + F₅).

## Cross-Validation

- **EFTCAMB**: 82+ P(k) runs, 43 C_ℓ spectra, 9 calibration runs ✅
- **hi_class**: 6 data points (αH = 0–0.025), qualitative agreement ✅
- **Fortran PM N-body**: 128³ particles, scale-dependent P(k) ratio ✅
- **MCMC**: 9 independent chains, CamSpec2021 Planck TTTEEE ✅

## Repository Structure

```
paper/          — TAUG papers (v1.0 + v1.1)
figures/        — Paper figures
data/           — Results data (573 files on VPS)
  S30/          — Session S30 summary data
eftcamb_inis/   — EFTCAMB parameter files (reproducible!)
code/           — Verification scripts
scripts/        — Session scripts
```

## Reproduce

```bash
# Requires EFTCAMB: https://eftcamb.org
./camb eftcamb_inis/taug_rph_br005.ini    # → σ₈ = 0.763
./camb eftcamb_inis/taug_fib_c0500.ini    # → σ₈ = 0.887
```

## Methodology

This research was conducted using a **multi-AI collaborative system** (O1, O2, O3, O4) with:
- Cross-validation between 3 independent AI systems
- SANITY guard on every numerical output (✅/❌)
- Three verification paths: Julia BigFloat 512-bit, Python Fraction, SymPy
- 31 sessions, 18 days, March–April 2026
- 573 data files generated

## Citation

```bibtex
@article{Schadler2026TAUG,
  author  = {Schadler, Luciano Andrey},
  title   = {{TAUG}: A {DHOST-Ia} Scalar-Tensor Cosmology with Fibonacci
             Parameters and a Falsifiable Test for {Euclid}},
  year    = {2026},
  note    = {v1.1, Sessions S1--S31},
  url     = {https://github.com/lucianoschadler44-dot/TAUG-theory}
}
```

## License

CC BY 4.0

---

*"O diamante brilha onde o vácuo domina."* — Luciano Andrey Schadler, April 2026

Developed by [Schadler Tech](mailto:lucianoschadler44@gmail.com) | Cascavel-PR, Brazil
