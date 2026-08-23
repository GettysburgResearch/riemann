# M-105380 — Hostile review contract for Xi source moments and real-saddle concentration

Claim ID: `M-105380`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

## Required algebraic review

1. For odd `r`, rederive

   \[
   {F(z)\over F'(z)}
   ={\mathbb E[\sin(zU)/U]\over\mathbb E[\cos(zU)]}
   \]

   under the tilt `u^(r+1)Phi(u)`.
2. Verify the recurrence and the formulas for `a_1,a_2,a_3`.
3. Recompute both order-two determinants, especially the shifted numerator

   \[
   35x^2y+15xz_3-42y^2.
   \]

4. For even `r`, retain the central residue `rho_0=-E[X^(-1)]`, subtract it
   before expanding, and verify the three regularized coefficients.
5. Check the paired critical atom normalization against `L-105370`.
6. Reconstruct the tangent and cotangent Mittag--Leffler measures in
   `L-105382`.

## Required analytic review of L-105385

The exact replay does not authenticate the real-saddle theorem. Reviewers must
check:

1. first-summand dominance of the explicit Xi kernel with the first two
   logarithmic derivatives;
2. that the global maximizer enters the large-`u` concave region;
3. the saddle equation and curvature constants;
4. uniform payment of both tails relative to the central mass;
5. negative fixed moments near `u=0`;
6. the quantifier order

   ```text
   for every fixed k, there exists R_k;
   ```

   rather than a uniform derivative threshold for all orders.

No shifted complex contour or zero-location theorem is used in `L-105385`.

## Load-bearing parity normalizations

```text
odd tilt exponent   r+1;
even tilt exponent  r+2;
odd source model    tan(omega z)/(omega z);
even source model   1/(omega^2 z^2)-cot(omega z)/(omega z).
```

A parity or sign swap changes the source coefficients and invalidates the
capacity comparison.

## Sharp scope

The real-saddle theorem proves only

```text
for each fixed finite source order k,
high enough derivatives have A_k^(0),A_k^(1) positive definite.
```

It does not prove:

- one derivative order works for every `k`;
- realness or nonpositivity of the critical residues;
- domination `C<=A`;
- `OSCC105371`, `BRP105220`, or RH.

## Binding boundary

```text
odd/even source formulas                         PROVED EXACT
trigonometric source-critical saturation         PROVED EXACT
finite-order stability near saturation           PROVED EXACT
real-saddle fixed-moment concentration            PROVED / HOSTILE REVIEW
actual critical capacity matching                OPEN
all-order source positivity at one Xi level       OPEN
Riemann Hypothesis                                UNPROVEN
```
