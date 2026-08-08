# L-27906 — Complete endpoint scalar and its Mellin pole firewall

Claim ID: `L-27906`  
Title: The complete von-Mangoldt endpoint discrepancy has one explicit Mellin transform with an uncancelled pole at every zero to the right of the critical line  
Status: **PROPOSED COMPLETE EXACT TRANSFORM THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-27905`; elementary Dirichlet-series continuation  
Scope: exact scalar and conditional pole exclusion; no bound for the scalar

## 1. Complete endpoint scalar

Retain

\[
\dot b_X(m)
=2\sqrt m(1-\sqrt{m/X})\mathbf1_{m\le X}.
\]

Define

\[
\boxed{
\mathcal A_\Lambda(X)
=\sum_{q=p^a\le X}\Lambda(q)
 [v_q(\dot b_X)-q^{-1/2}].}
\tag{L-27906.1}

The divisor identity

\[
\sum_{q\mid n}\Lambda(q)=\log n
\]

gives the exact elementary representation

\[
\boxed{
\begin{aligned}
\mathcal A_\Lambda(X)
={}&\sum_{m=2}^{X}
2\sqrt m(1-\sqrt{m/X})
\log{m\over m-1}\\
&-\sum_{n\le X}{\Lambda(n)\over\sqrt n}.
\end{aligned}}
\tag{L-27906.2}

The first line is a completely explicit endpoint benchmark. All arithmetic oscillation is in the second line.

## 2. Mellin transform of the benchmark

For `Re z>0` and fixed `m`,

\[
\int_m^\infty
2\sqrt m(1-\sqrt{m/X})X^{-z-1}dX
={m^{1/2-z}\over z(z+1/2)}.
\tag{L-27906.3}

Initially for `Re z>1/2`, absolute convergence therefore gives

\[
\int_1^\infty
\left[
\sum_{m=2}^{X}\dot b_X(m)\log{m\over m-1}
\right]X^{-z-1}dX
={\Phi(z)\over z(z+1/2)},
\tag{L-27906.4}
\]

where

\[
\boxed{
\Phi(z)
=\sum_{m\ge2}
\log{m\over m-1}\,m^{1/2-z}.}
\tag{L-27906.5}

Since

\[
\log{m\over m-1}
={1\over m}+O(m^{-2}),
\]

we may write

\[
\boxed{
\Phi(z)
=\zeta(z+1/2)-1+R(z),}
\tag{L-27906.6}

where

\[
R(z)=\sum_{m\ge2}
\left(\log{m\over m-1}-{1\over m}\right)m^{1/2-z}
\]

is holomorphic for `Re z>-1/2`. Thus the benchmark term has a meromorphic continuation through the full open half-plane `Re z>0`, with only the displayed elementary singularities.

## 3. Mellin transform of the prime-power term

For `Re z>1/2`,

\[
\int_1^\infty
\left[
\sum_{n\le X}{\Lambda(n)\over\sqrt n}
\right]X^{-z-1}dX
={1\over z}
\left[-{\zeta'\over\zeta}(z+1/2)\right].
\tag{L-27906.7}

Subtracting gives

\[
\boxed{
\int_1^\infty
\mathcal A_\Lambda(X)X^{-z-1}dX
={\Phi(z)\over z(z+1/2)}
+{1\over z}{\zeta'\over\zeta}(z+1/2).}
\tag{L-27906.8}

Equation (L-27906.8) supplies the meromorphic continuation of the transform to `Re z>0` away from shifted zeta zeros and the elementary boundary points.

## 4. Off-line zeros are genuine poles

Let `rho` be a nontrivial zeta zero with

\[
\Re\rho>1/2
\]

and put

\[
z_\rho=\rho-1/2.
\]

The benchmark term in (L-27906.8) is holomorphic at `z_rho`: `Phi` contains `zeta`, not `1/zeta`, and `z_rho` is neither `0` nor `-1/2`.

If the multiplicity of `rho` is `m_rho`, then

\[
{\zeta'\over\zeta}(z+1/2)
={m_\rho\over z-z_\rho}+O(1).
\]

Therefore the transform of `A_Lambda` has the genuine residue

\[
\boxed{
\operatorname*{Res}_{z=z_\rho}
\int_1^\infty
\mathcal A_\Lambda(X)X^{-z-1}dX
={m_\rho\over z_\rho}\ne0.}
\tag{L-27906.9}

No finite Euler numerator or benchmark term cancels the pole.

## 5. Complete Endpoint Stability

Define

\[
\boxed{
\mathrm{CEP}:\qquad
\mathcal A_\Lambda(X)=o(\log X).}
\tag{L-27906.10}

If CEP holds, then for every `sigma>0`,

\[
\int_1^\infty
|\mathcal A_\Lambda(X)|X^{-\sigma-1}dX<\infty,
\]

and the Mellin transform is holomorphic on `Re z>0` by normal convergence on compact subsets.

Equation (L-27906.9) then excludes every zeta zero with real part greater than `1/2`. Functional-equation symmetry gives

\[
\boxed{
\mathrm{CEP}\Longrightarrow\mathrm{RH}.}
\tag{L-27906.11}

This is a direct pole-exclusion consumer, independent of the carry/WSTS route.

## 6. Prime-square reserve gives a second consumer

`L-27905` proves

\[
\mathcal A_{\mathbb P}(X)
\le
\mathcal A_\Lambda(X)
-c_{\rm pp}\log X+O(1)
\]

with `c_pp>0`. Hence CEP also gives

\[
\mathcal A_{\mathbb P}(X)<0
\]

cofinally, i.e. Endpoint Prime Domination. Together with cofinal shell crossing, this makes the WSTS charge exactly zero.

Thus CEP reaches RH in two compatible ways:

```text
complete endpoint Mellin pole exclusion;
prime-square reserve -> EPD -> WSTS -> RH.
```

## 7. Correct review target

Finite computation shows that `A_Lambda(X)` is not always nonpositive. A valid proof must therefore establish a rate such as CEP, not an incorrect one-sign theorem for the complete source.

The complete source is nevertheless better suited to the existing analytic machinery than the ordinary-prime endpoint scalar:

- it uses the true von Mangoldt sequence;
- the Selberg coefficient identity applies without prime-only Möbius inversion;
- the independent-frequency reflected square is available;
- prime squares are retained as a deterministic reserve rather than discarded.

A production proof should seek a reflected endpoint estimate of the form

\[
\mathcal A_\Lambda(X)
=O(1)+\text{a signed boundary of sublogarithmic size},
\]

or an averaged/Hardy estimate strong enough to imply (L-27906.10).

## 8. Proof boundary

Closed here, subject to review:

- the exact elementary endpoint formula;
- the benchmark Mellin transform and continuation;
- the complete transform identity;
- the uncancelled off-line pole;
- `CEP -> RH`;
- the second `CEP -> EPD -> RH` consumer.

Open:

- CEP itself;
- a reflected Selberg, semiprime, or explicit-formula proof of CEP;
- RH.
