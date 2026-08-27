# M-105360 — Hostile review contract for terminal Stieltjes transport

Claim ID: `M-105360`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

## Required audit order

1. Re-derive the nested-window identity

   \[
   H_{\rm in}=H_{\rm out}+\sum_{c\text{ in annulus}}{\rho_c\over z-c}.
   \]

2. At a general real anchor, verify

   \[
   {1\over(n+1)!}
   \left({d\over dz}\right)^{n+1}{\rho_c\over z-c}\Big|_{x_*}
   ={ -\rho_c\over(c-x_*)^{n+2}}.
   \]

3. Check the atom parameters

   \[
   t_c=(c-x_*)^{-1},
   \qquad
   w_c=-\rho_c(c-x_*)^{-2}.
   \]

4. In the symmetric origin coordinate, pair `c` with `-c` and verify

   \[
   s_c=c^{-2},
   \qquad
   W_c=-2\rho_c c^{-2}.
   \]

5. Verify both Stieltjes updates, including the extra factor `s_c` in the
   shifted matrix.
6. Freeze an inner window and matrix order before taking the cofinal outer
   limit. No uniform-in-order limit is used.
7. Keep `CRVH105330` and `TAIR105360` visibly open for Xi.

## Load-bearing orientation

The exact monotone relation is

\[
\boxed{
\text{inner matrix}
=
\text{outer matrix}
+
\text{positive annular atoms}
}
\]

when every crossed residue is nonpositive. The reverse relation subtracts a
positive matrix and has no monotonicity. Any review that swaps inner and outer
has reversed the theorem.

## Load-bearing signs

For `rho_c<=0`,

\[
w_c={-\rho_c\over(c-x_*)^2}\ge0.
\]

At the origin, one symmetric pair contributes

\[
{-2\rho_c\over c^{2n+2}}\ge0
\]

to `beta_n`. The safe-axis contribution is

\[
{-2\rho_c\over c^2+y^2}\ge0.
\]

All three formulas must agree.

## Quantifier firewall

`TAIR105360` is

\[
\forall k<\infty,
\quad
\liminf_{j\to\infty}
\lambda_{\min}(S_{k,N_j}^{(a)})\ge0.
\]

It does not require a bound uniform in `k`. Conversely, checking every fixed
order only up to a common finite ceiling does not establish the hierarchy.

## Scientific boundary

```text
atomic window transport                       PROVED EXACT
outer-to-inner PSD monotonicity                PROVED EXACT UNDER rho<=0
cofinal vanishing negative part suffices       PROVED EXACT
safe-axis scalar positivity -> Stieltjes PSD   FALSE
AATR105360 for Xi                              OPEN
CRVH105330 for Xi                              OPEN
TAIR105360 for Xi                              OPEN
Riemann Hypothesis                             UNPROVEN
```

The replay is exact rational algebra only. It does not evaluate Xi, prove a
terminal asymptotic, or certify any RH-bearing sign gate.
