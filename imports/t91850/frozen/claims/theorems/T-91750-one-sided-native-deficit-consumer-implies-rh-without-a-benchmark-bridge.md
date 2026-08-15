# T-91750 — A subquadratic one-sided native deficit implies RH without a benchmark bridge

Claim ID: `T-91750`  
Status: **PROVED CONDITIONAL ENDPOINT CONSUMER ON THE FROZEN PRIME-SQUARE/LANDAU INPUTS**  
Created: 2026-08-15  
Frozen inputs: PR #352 at `906b5a477a1ed7c88a40db7569924f15f3d54b72`; PR #353 at `ed566f3198e236c54ba18049181016536f56d456`; `L-91377/L-91378`  
RH status: **conditional only on producing the native deficit estimate**

## 1. Native feasibility and the complete gap

For a native-feasible nonnegative physical row `d_X`, exact ordinary duality
gives

\[
 \mathcal H(d_X)\le P_\Lambda(X),
\tag{T-91750.1}
\]

where

\[
 P_\Lambda(X)=
 \sum_{q\le X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\]

The complete prime-power endpoint gap is

\[
 F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
\tag{T-91750.2}
\]

Therefore the exact native deficit

\[
 \Delta_X(d_X)=J_\Lambda(X)-\mathcal H(d_X)
\]

satisfies the one-sided inequality

\[
 \boxed{F_\Lambda(X)\le\Delta_X(d_X).}
\tag{T-91750.3}
\]

This step uses no comparison with `4 sqrt(X)`.

## 2. Prime-square moat

Let

\[
 A(X)=\sum_{p\le X}(\log p)r_X(p)
\]

be the prime-only endpoint. The unconditional prime-square occupancy theorem
of the frozen PR #353 gives

\[
 \boxed{
 A(X)=F_\Lambda(X)-\frac{C_{\rm pp}}4\log^2X
      +o(\log^2X),
 }
\tag{T-91750.4}
\]

with

\[
 C_{\rm pp}=-1-\zeta(1/2)
 =\frac12\int_1^\infty\{v\}v^{-3/2}\,dv>0.
\tag{T-91750.5}
\]

The positivity in (T-91750.5) is elementary and does not assume RH.

## 3. Subquadratic native deficit forces prime-endpoint negativity

Assume one has constructed feasible rows with

\[
 \boxed{\Delta_X(d_X)=o(\log^2X).}
\tag{T-91750.6}
\]

Equation (T-91750.3) gives

\[
 \limsup_{X\to\infty}
 \frac{F_\Lambda(X)}{\log^2X}\le0.
\]

Combining with (T-91750.4),

\[
 \limsup_{X\to\infty}
 \frac{A(X)}{\log^2X}
 \le-\frac{C_{\rm pp}}4<0.
\]

Hence

\[
 \boxed{A(X)<0}
\tag{T-91750.7}
\]

for every sufficiently large real `X`.

Notice that no two-sided estimate for `F_Lambda` is required. The nonnegative
native deficit supplies exactly the upper bound needed to fall below the
positive prime-square moat.

## 4. Landau converse

The frozen prime-endpoint Mellin transform is

\[
 \widehat A(z)=\frac1{z^2}
 \mathcal G\!\left(z+\frac12\right).
\]

Every zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad\delta>0,
\]

produces a genuine nonreal singularity at `z=delta+i gamma`, while the positive
real axis has no singularity after cancellation of the zeta pole.

If `A(e^t)` is eventually one-signed, Landau's one-sign theorem either makes the
Laplace integral holomorphic at that nonreal point or forces a singularity at
the real abscissa of convergence. Both alternatives contradict the pole audit.
Therefore eventual one-sidedness excludes every zero to the right of the
critical line; the functional equation gives RH.

Together with (T-91750.7),

\[
 \boxed{
 \Delta_X(d_X)=o(\log^2X)
 \Longrightarrow\mathrm{RH}.
 }
\tag{T-91750.8}
\]

## 5. Circularity firewall

The proof uses only:

```text
native feasibility -> F_Lambda <= native deficit;
unconditional positive prime-square moat;
eventual prime-endpoint one-sign -> RH by Landau.
```

It does **not** use any eventual estimate of

\[
 J_\Lambda(X)-4\sqrt X,
\]

which PR #484 correctly identifies as RH-bearing.

```text
ordinary feasibility -> F_Lambda<=Delta        EXACT
prime-square moat coefficient C_pp>0            UNCONDITIONAL / FROZEN
subquadratic native deficit -> A(X)<0            EXACT
prime endpoint eventual one-sign -> RH           FROZEN MELLIN/LANDAU THEOREM
benchmark bridge J_Lambda-4sqrt(X)                NOT USED
Riemann Hypothesis                               CONDITIONAL ON PRODUCER
```
