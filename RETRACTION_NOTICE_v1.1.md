# RETRACTION NOTICE — TAUG paper v1.1

**Date:** April 11, 2026
**Author:** Luciano A. Schadler (lucianoschadler44@gmail.com)
**Repository:** github.com/lucianoschadler44-dot/TAUG-theory
**Affected file:** `paper/taug_paper.tex` (v1.1, sha256: 3d5f3add886faf63e07f8e14e8de3975a97a258ace7624ea942195f8ba0d9552)

---

## TL;DR

The central observational prediction of TAUG paper v1.1 — namely
the gravitational slip parameter η ≡ Φ/Ψ = 23/17 ≈ 1.353 (a 35%
deviation above General Relativity) — has been found inconsistent
with the rigorous DHOST-Ia formula derived from the foundational
references LMNV17 (arXiv:1703.03797) and Crisostomi-Lewandowski-
Vernizzi 2019 (arXiv:1903.11591).

**The correct prediction for the same TAUG parameters is η = 8/9 ≈
0.889 (an 11% deviation BELOW General Relativity).** The two values
lie on opposite sides of η = 1 — this is a qualitative reversal,
not a numerical correction.

The mathematical core of TAUG (the derivation of α_H = 1/8 from
conformal field theory M(5,6), the algebraic chain of EFT parameters,
the DEST-32 ghost-stability condition, and c_s² = 193/388) **survives
unchanged**. Only the observational interpretation requires correction.
A revised version v1.2 with the corrected predictions is provided.

---

## What was wrong in v1.1

Section III of paper v1.1 stated:

> "Working in the quasi-static approximation with scale-independent
> modifications, the modified Poisson equation and gravitational
> slip are: μ_Ψ = 8πG_N (1 - α_H α_B) = 254/289, η = Φ/Ψ = 23/17,
> c_s² = 193/388"

The formula η = 1 + 2α_M / Λ used to obtain 23/17 was applied
without explicit citation to a derivation valid for DHOST type-Ia
theories with α_H ≠ 0. We now find that:

1. **The formula η = 1 + 2α_M / Λ does not appear verbatim in any
   of the papers cited by the v1.1 reference list** (LMNV17,
   Bellini-Sawicki 2014, Crisostomi+2018, Crisostomi+2019). It is
   a Horndeski-like simplification that ignores the α_H-dependent
   terms which are the defining feature of DHOST-Ia.

2. **Two independent rigorous derivations from the literature give
   the same answer η = 8/9** for the TAUG parameters
   (α_H = 1/8, α_T = 0, β₁ = -1/16, α_M = 3/16):

   - **LMNV17, eq. on line 992 of `Pheno_DHOST_arXiv2.tex`** (Newtonian limit):
     ```
     Ψ = (1 + α_H)/(1 + α_T) · Φ
     ⟹ η = (1 + α_T)/(1 + α_H) = 1/(9/8) = 8/9
     ```

   - **Crisostomi+2019, Appendix B "Linear solutions" (`coefficientsapp2`),
     lines 956-962 of `Vainstein_DHOST_prd_v2.tex`** (cosmological QSA,
     dominant terms in matter source):
     ```
     μ_Φ = a²/[2 M² (1 - β₁)²]
     μ_Ψ = a² (1 - 2 β₁) / [2 M² (1 - β₁)²]
     ⟹ η = μ_Φ/μ_Ψ = 1/(1 - 2β₁) = 1/(9/8) = 8/9
     ```

3. **The Newton constant 8πG_N = 256/289 stated in v1.1** also does
   not match LMNV17 eq. on line 1022:
   ```
   8πG_N = 1 / [M² · ((1+α_H)²/(1+α_T) - β₃/2)]
         = 1 / (81/64) = 64/81 ≈ 0.790
   ```

---

## What survives

1. **α_H = 1/8** — derived from the conformal field theory M(5,6)
   Ising tricritical model via h₂,₁ = 1/8.
2. **α_T = 0** — structural consequence of Charmousis G₅ = 0.
3. **β₁ = -α_H/2 = -1/16** — Crisostomi 2019 stability constraint.
4. **α_B = α_H/2 = 1/16, α_M = 3α_H/2 = 3/16** — running M_P relations.
5. **α_K = +557/1544** — DEST-32 with ghost-stability sign-flip.
6. **c_s² = 193/388** — sound speed, subluminal, no instabilities.
7. **Algebraic chain 12/12 closes exactly** — verified by blind multi-AI
   cross-check in F1-012 (3/3 convergence).
8. **Temporal profile α_H(a) = α_H_max · 4a(1-a)** — Hulse-Taylor compatible.

---

## How the error was discovered

The error was discovered during a multi-AI session (S33-F1-013) on
April 11, 2026, through:

1. The principal researcher's R-G meta-question: *"if DESI 2024 confirms
   TAUG, why is there no media coverage?"*
2. AI agent O1 calculating η(z) with the temporal profile and finding
   η(z=0) = 1 EXACTLY, contradicting v1.1 Section III claim.
3. AI agent O5 performing verbatim grep of LMNV17 and Crisostomi+2019
   and locating the rigorous formulas.

The full session log, including five formal AI retractions in 12 hours,
is preserved as a methodology case study.

---

## Status

TAUG v1.2 is **observationally viable and not yet refuted**. The
revised predictions are within ~1.5σ of current DESI 2024 MG
constraints, and remain testable by Euclid DR1 in October 2026 at
the 1-2σ level.

The character of TAUG has changed: from "smoking-gun 35% slip
enhancement" to "modest 11% slip reduction" (η < 1), driven by the
small DHOST parameter β₁ = -1/16.

—Schadler, April 11, 2026
