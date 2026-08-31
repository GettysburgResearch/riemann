# T-108518 — Certified off-critical-line zero: Z(s, 10i) has a real zero in (81/100, 41/50)

```text
Claim ID: T-108518
Status:   PROVED per instance (directed-rounding interval arithmetic
          with every truncation explicitly bounded; the 1-D Jacobi
          theta transformation is the one labelled classical import;
          iv.gamma enclosures independently checked by the reflection
          identity). Phenomenon classical (Bateman-Grosswald real
          zeros of rectangular Epstein zetas; CITATION-NEEDED);
          the certificate is the repo's first PROVED Epstein zero.
Created:  2026-08-31 (pass 3 continuation, Lane 4)
Programme: #764 (Epstein moduli lab, O-108503/C8)
Proof:    standalone/2026-08-31-epstein-wall-certificate/PROOF.md
Machine:  research/exploratory/2026-08-30-two-programme-pass/epstein/
          wall_certificate.py + wall_certificate.json (mpmath.iv,
          dps 120; float cross-check of the representation against
          Chowla-Selberg to ~1e-40 at two points)
RH status: RH and GRH are unproved. Epstein zetas are not the Riemann
          zeta; this classical-type off-line zero has no bearing on
          them.
```

## Statement

For `Q(m,n) = (m^2 + 100 n^2)/10` (modulus `z = 10i`, integral form
of discriminant -400), the Epstein zeta `Z_Q(s)` has a real zero
`sigma_0` with `81/100 < sigma_0 < 41/50` — strictly off the critical
line — and an FE-partner zero in `(9/50, 19/100)`. Certified via the
incomplete-gamma representation

```text
Lambda(s) = 1/(s-1) - 1/s + sum_{v != 0} [(pi Q)^{-s} Gamma(s, pi Q)
                               + (pi Q)^{s-1} Gamma(1-s, pi Q)]
```

with interval evaluation at rational points: `Lambda(3/4) > 1.11`,
`Lambda(17/20) < -1.15`, `Lambda(81/100) > 0.08`,
`Lambda(41/50) < -0.17` (all enclosures of width ~5e-18, tails
bounded by three explicit inequalities proved in the standalone
file).

## Why it matters for the lab

O-108503's entire zero atlas was NON_DIRECTED_HIGH_PRECISION; this
anchors the rectangular bifurcation story with a proof-grade point
and establishes the certification TEMPLATE (self-dual theta ->
incomplete-gamma series -> three tail bounds -> interval signs) that
the deposited complex-archipelago certification will extend.
```
