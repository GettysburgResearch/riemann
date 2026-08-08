# T-27202 — Subpower cycle debt implies RH

Claim ID: `T-27202`  
Title: A subpower cycle-optimized negative carry debt yields the sharp prime ramp and excludes every off-line zeta zero  
Status: **FULL CONDITIONAL PROPOSAL; CYCLE DEBT IS THE SOLE NEW HINGE**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-27205`; reviewed square-screw/rightmost-zero transfer  
Scope: complete deduction from one explicit finite optimization theorem

## 1. Cycle Debt Theorem

Fix one `0<eta<1/2`. Let `mathfrak N_eta(X)` be the exact finite quantity in
`L-27205`:

\[
\mathfrak N_\eta(X)
=
\min_{\partial d=r^{w_X}}
\sum_e\omega_e(-d_e)_+,
\]

where every edge is eta-balanced and

\[
\omega_e=\sum_q q^{-1/2}\chi_e(q).
\]

The proposed closing statement is

\[
\boxed{
\mathfrak N_\eta(X)=X^{o(1)}.}
\tag{T-27202.1}
\]

Call this the **Cycle Debt Theorem (`CDT`)**.

`CDT` is strictly weaker than exact Möbius Fragmentation Transport:

```text
MFT  => mathfrak N_eta(X)=0;
CDT  permits signed flows and asks only that their optimized negative
     capacity mass be subpower.
```

## 2. Sharp prime-ramp estimate

Choose an exact signed flow with debt

\[
\mathcal N_\omega(d)
\le\mathfrak N_\eta(X)+1.
\]

`L-27205` gives

\[
\begin{aligned}
\left|
P_X-
\sum_{q=2}^{X}q^{-1/2}\log(X/q)
\right|
&\le
A_\eta
\left[
K_X+2\mathcal N_\omega(d)
\right],
\end{aligned}
\tag{T-27202.2}
\]

where

\[
P_X
=
\sum_{p^a\le X}
 \frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac X{p^a},
\qquad
K_X=O((\log X)^2).
\]

Under `CDT`, the right side is `X^(o(1))`. Since

\[
\sum_{q=2}^{X}q^{-1/2}\log(X/q)
=4\sqrt X+O(\log X),
\]

we obtain

\[
\boxed{
P_X=4\sqrt X+X^{o(1)}.}
\tag{T-27202.3}
\]

The one-sided lower bound

\[
P_X\ge4\sqrt X-X^{o(1)}
\tag{T-27202.4}
\]

is already sufficient for the next step.

## 3. Square-screw transfer

At square endpoints `X=N^2`, the exact completed screw formula has the form

\[
\Psi(2\log N)
=4(N+N^{-1}-2)-P_{N^2}+O(\log N).
\tag{T-27202.5}
\]

Equation (T-27202.4) gives

\[
(\Psi(2\log N))_+=N^{o(1)}.
\tag{T-27202.6}
\]

The reviewed upper-envelope square-sampling/Landau theorem identifies the best
power exponent of this positive part with the horizontal displacement of the
rightmost nontrivial zeta zero. Hence that displacement is zero.

Functional-equation symmetry excludes zeros on the reflected side, and
therefore

\[
\boxed{\mathrm{RH}.}
\tag{T-27202.7}
\]

## 4. Proof-producing forms

Any one of the following proves `CDT` at endpoint `X`:

1. **Primal cycle certificate**
   ```text
   z_X,
   d_X=d_tree(r_X)+C_eta z_X,
   exact divergence and carry replay,
   sum_e omega_e(-d_X(e))_+ <= X^epsilon.
   ```

2. **Direct signed-flow certificate**
   ```text
   an eta-balanced signed split manifest d_X,
   exact target loads,
   subpower negative capacity debt.
   ```

3. **Uniform analytic producer**
   ```text
   a symbolic state-dependent cycle rule with a proved subpower debt bound.
   ```

The bounded-superadditive dual of `L-27205` provides adversarial lower
certificates and prevents a finite producer from concealing a large unresolved
debt.

## 5. Mandatory mutations

A proposed proof of `CDT` must retain:

- the directed pure-ternary failure at `X=10^7,n=63`;
- every balanced edge and cycle coefficient;
- exact node divergence and every carry column;
- the unweighted entropy metric of `L-27203`;
- the dyadic and `2/3` Mertens projections;
- the same-sign high-rank Möbius-cube mutation;
- the exact capacity weight, not an unweighted edge count.

## 6. Exact status

```text
cycle-debt finite primal/dual             PROPOSED COMPLETE
CDT => sharp prime ramp                   PROPOSED COMPLETE
sharp prime ramp => square-screw => RH    REVIEWED CONDITIONAL TRANSFER
CDT                                       OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```
