# TAUG — Topological Algebraic Unified Gravity

**Version 1.2 — April 11, 2026**
**Author:** Luciano A. Schadler
**Status:** observationally viable, awaiting Euclid DR1 (October 2026)

---

## ⚠ NOTICE — v1.1 → v1.2 retraction

The previous version (v1.1) contained an error in the slip formula
that propagated to the central observational prediction. The
mathematical core (α_H = 1/8 derivation, algebraic chain, ghost
stability) is unchanged. **The observational prediction has been
corrected from η = 23/17 to η = 8/9.** See `RETRACTION_NOTICE_v1.1.md`
for the full explanation.

---

## What TAUG is

TAUG is a specific point in the parameter space of Degenerate
Higher-Order Scalar-Tensor (DHOST) theories of type Ia, defined by
fixing the EFT-of-dark-energy parameters to rational fractions
derived from a conformal field theory argument involving the
M(5,6) Ising tricritical model.

| Parameter | Value | Origin |
|-----------|-------|--------|
| α_H | 1/8 | CFT M(5,6) h₂,₁ (tricritical Ising) |
| α_T | 0 | Charmousis G₅ = 0 (structural) |
| α_B | 1/16 | = α_H/2 |
| β₁ | -1/16 | = -α_H/2 (Crisostomi 2019 stability) |
| α_M | 3/16 | = 3α_H/2 (running M_P) |
| α_K | +557/1544 | DEST-32, sign-flip for no-ghost |
| c_s² | 193/388 | sound speed (subluminal, stable) |
| β₃ | 0 | Horndeski sub-class |

The temporal profile is:
```
α_H(a) = (1/8) · 4 · a · (1-a)
```
which gives α_H = 0 at z = 0 (recovering GR exactly today, passing
solar-system tests trivially) and at z → ∞ (recovering GR in the
early universe, passing CMB tests trivially). The peak occurs at
z = 1, where TAUG modifications are maximal.

---

## Predictions (TAUG v1.2)

All predictions below are derived rigorously from verbatim formulas
in the DHOST-Ia literature.

### Newton constant (LMNV17 line 1022)
```
8πG_N = 1 / [(1 + α_H)²/(1 + α_T) - β₃/2] = 64/81 ≈ 0.7901
```
21.0% reduction relative to canonically normalized graviton coupling.

### Slip parameter (LMNV17 line 992 + Crisostomi+2019 App.B)
```
η ≡ Φ/Ψ = 8/9 ≈ 0.8889
```
**11% reduction below GR** at peak of α_H profile.

### Modified Poisson coefficients
```
μ_Φ/μ_GR = 256/289 ≈ 0.886
μ_Ψ/μ_GR = 288/289 ≈ 0.997
μ₀ ≡ μ_Φ - 1 = -33/289 ≈ -0.114
Σ₀ = (μ_Φ + μ_Ψ)/2 - 1 = -17/289 ≈ -0.059
η₀ = η - 1 = -1/9 ≈ -0.111
```

### Sound speed
```
c_s² = 193/388 ≈ 0.4974
```
Subluminal, no-ghost, no-gradient instability.

---

## Comparison with current data

### DESI 2024 MG (arXiv:2411.12026, ΛCDM background)

| Quantity | DESI measurement | TAUG v1.2 | Tension |
|----------|-----------------|-----------|---------|
| μ₀ | +0.05 ± 0.22 | -0.114 | 0.75σ |
| Σ₀ | +0.008 ± 0.045 | -0.059 | 1.48σ |
| η₀ | +0.09 +0.36/-0.60 | -0.111 | 0.34σ |

**TAUG v1.2 is compatible with DESI 2024 within ~1.5σ** in all three
parameters.

### DES Y6
S₈ = 0.789 ± 0.012 — TAUG-EFTCAMB best-fit S₈ = 0.777 (1σ compatible).

---

## Forecast Euclid DR1 (October 2026)

| σ(η₀) Euclid | Tension TAUG vs GR central=0 |
|--------------|---------------------|
| 0.05 | 2.22σ |
| 0.075 | 1.48σ |
| 0.10 | 1.11σ |

**TAUG v1.2 will be tested by Euclid DR1 at the 1-2σ level.**

---

## What v1.2 does NOT predict (correcting v1.1 errors)

| v1.1 (incorrect, RETRACTED) | v1.2 (corrected) |
|-----------------|------------------|
| η = 23/17 ≈ 1.353 (35% MORE deflection) | η = 8/9 ≈ 0.889 (11% LESS deflection) |
| 8πG_N = 256/289 | 8πG_N = 64/81 |
| μ_Ψ = 254/289 | μ_Ψ = 288/289 |
| Smoking-gun "binary" 35% deviation | Modest 11% deviation peaked at z ≈ 1 |
| Refutable at 7σ by Euclid DR1 | Refutable at 1-2σ by Euclid DR1 |

---

## Methodological note

The TAUG project is developed under a multi-AI blind verification
protocol (MDCA-IA). The discovery and correction of the v1.1 error
in real time, including five formal AI retractions in 12 hours, is
documented as a case study for a separate methodology paper.

The principle that emerged: **independent multi-AI convergence on
an incomplete premise is not equivalent to truth.** Human R-G
meta-questions remain irreplaceable.

---

## Files

- `paper/taug_paper_v1.2_skeleton.tex` — corrected paper skeleton
- `paper/taug_paper_v1.1_RETRACTED.tex` — DEPRECATED v1.1
- `RETRACTION_NOTICE_v1.1.md` — formal retraction
- `eftcamb_inis/` — EFTCAMB input files
- `derivations/` — symbolic derivation scripts

---

## Citation

```
@article{schadler2026taug_v12,
  author = {Schadler, Luciano A.},
  title = {{TAUG: A CFT-Anchored Point in DHOST-Ia Parameter Space (v1.2 corrected)}},
  year = {2026},
  note = {Version 1.2, GitHub: lucianoschadler44-dot/TAUG-theory},
}
```

**Sempre progredir, nunca regredir.**
