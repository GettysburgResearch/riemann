# T-108519 — Certified COMPLEX off-critical-line zero at an exact archipelago-adjacent modulus (rigorous winding number 1)

```text
Claim ID: T-108519
Status:   PROVED per instance (directed-rounding complex-interval
          winding number: interval [0.97335, 1.02666] pins winding
          = 1 over 3696 contour steps, every step satisfying the
          exact-step lemma's conditions; three inline-proved sup-
          bound lemmas — Weierstrass Gamma modulus, two-line
          Euler-Maclaurin zeta bound, rotated-contour K-Bessel
          imaginary-order decay; imports labelled: Spouge (SIAM J.
          Numer. Anal. 31(3) 1994) for complex Gamma with explicit
          error, Jacobi theta transformation, and the classical
          Chowla-Selberg expansion used ONLY inside the Lipschitz
          sup bound). A first unpinned run and its bound-budgeting
          lesson are recorded in the standalone's status block.
Created:  2026-08-31 (pass 3 continuation, Lane 4 stage 2)
Programme: #764 (Epstein moduli lab, O-108503/C8)
Proof:    standalone/2026-08-31-epstein-complex-wall/PROOF.md
Machine:  research/exploratory/2026-08-30-two-programme-pass/epstein/
          wall_complex.py + wall_complex.json (mpmath.iv dps 30;
          adversarial-wave-style validation layer asserted pre-walk)
RH status: RH and GRH are unproved. Epstein zetas are not the
          Riemann zeta; nothing here bears on them.
```

## Statement

Let `z* = 4341/50000 + (3731/2500) i` (the C8 campaign's dirty
theta80 probe, exact-rationalized) and
`Q(m,n) = |m + n z*|^2 / y*`. Then `Z_Q(s)` has EXACTLY ONE zero
(with multiplicity) in the rectangle

```text
Re s in [83/100, 99/100],   Im s in [1221/100, 1238/100],
```

whose left edge is strictly right of the critical line: a PROVED
complex zero with `Re rho >= 0.83` (float location
`0.90837 + 12.29624 i`), giving with its conjugate and FE partners a
certified off-line quadruple.

## Why it matters for the lab

The C8 archipelago was FLOAT_DIAGNOSTIC; this pins one of its
adjacent moduli with a proof-grade complex zero — the first in the
repo — using the certification template T-108518 established, plus
the three new lemmas (the K-Bessel rotated-contour bound
`|K_{a+i mu}(x)| <= e^{-mu theta} K_a(x cos theta)` is the piece
that makes a REALISTIC Lipschitz bound possible at height t ~ 12).
The remaining archipelago statements (thinness, angular
intermittency, CM-proximity) stay labelled diagnostics; certifying
the SECOND off-line zero at this modulus (t ~ 18.9) and a clean
point of the 75-degree island are the deposited next targets.
```
