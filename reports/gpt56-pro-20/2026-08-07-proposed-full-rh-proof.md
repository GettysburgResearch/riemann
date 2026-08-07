# Full-proof attempt and internal refutation — critical Möbius local-to-Bohr route

Agent: `gpt56-pro-20`  
Date: 2026-08-07  
Issue: #228  
Branch: `agent/gpt56-pro-20/228-proposed-full-rh-proof`  
Current status: **GAP/BLOCKED; RH UNPROVED**

## Executive summary

This pass consolidated the repository’s global prime-Hardy, Haar, polygon, Brownian, analytic-totient, and CCM routes and attempted a complete proof through the analytic summatory-totient error.

The exact algebraic spine is strong:

1. the analytic totient error has a Mellin transform whose poles are off-critical zeta zeros;
2. the full-period Möbius fractional-part packet has an exact positive Jordan-totient square of size `O(D)`;
3. a critical physical local-to-Bohr estimate would give the RH-equivalent second moment.

A full proof manuscript was initially written around a claimed uniform Farey-cluster operator bound. Before handoff, an internal adversarial test found an exact counterexample to that operator estimate. The manuscript and PR status were corrected immediately.

The branch therefore contributes exact packet algebra, a useful finite regression, a rigorous no-go theorem, and the smallest scalar Möbius-specific blocker. It does **not** provide a valid proposed proof of RH.

## 1. Exact packet algebra retained

For

\[
f(t)=\{t\}^2-1/3,
\qquad
S_D(x)=\sum_{d\le D}\mu(d)f(x/d),
\]

and `0<=x<=D`,

\[
2E^{\rm AN}(x)
=1+S_D(x)+M_D/3+x^2R_D,
\]

where

\[
M_D=\sum_{d\le D}\mu(d),
\qquad
R_D=\sum_{d>D}\mu(d)/d^2.
\]

At a reduced Farey frequency `a/q`,

\[
b_D(a/q)
=\frac{iq}{2\pi a}U_q(D)
 +\frac{q^2}{2\pi^2a^2}V_q(D),
\]

with

\[
U_q(D)=\sum_{q\mid d\le D}\mu(d)/d,
\qquad
V_q(D)=\sum_{q\mid d\le D}\mu(d)/d^2.
\]

The complete Bohr energy is exactly

\[
\mathcal B_D
=\frac1{12}\sum_qJ_2(q)U_q(D)^2
 +\frac1{180}\sum_qJ_4(q)V_q(D)^2
\ll D.
\]

These identities are unconditional and retained as `L-22801`.

## 2. Attempted closure

The desired critical estimate is

\[
\int_{D/2}^{D}|2E^{\rm AN}(x)|^2dx
\ll_\varepsilon
D^{1+\varepsilon}(1+\mathcal B_D).
\]

It would imply

\[
\int_1^X|E^{\rm AN}(x)|^2dx
\ll_\varepsilon X^{2+\varepsilon},
\]

and hence RH by the exact Mellin argument of `T-9506`.

The attempted proof grouped Farey frequencies into width-`1/D` cells and claimed a subpower norm for the resulting divisor-coordinate operator.

## 3. Exact refutation

For the `r=1` cluster operator and any fixed positive cell index `k`, the numerator `a=1` occurs whenever

\[
D/(k+1/2)<q\le D/(k-1/2).
\]

There are `c_kD+O(1)` such denominators, and every corresponding entry is at least one because `J_2(q)<=q^2`. Thus the row norm is at least `c_k sqrt(D)`, and the operator norm cannot be subpower.

Changing any fixed finite set of low rows does not help. This refutes the load-bearing operator theorem. The result is retained as `R-22802`.

## 4. Correct remaining theorem

The actual Möbius vectors are highly special. The scalar estimate

\[
\int_{D/2}^{D}
\left|
1+S_D(x)+M_D/3+x^2R_D
\right|^2dx
\ll_\varepsilon
D^{1+\varepsilon}(1+\mathcal B_D)
\]

may still hold, but a proof must use the signs and divisor coupling of `U_q,V_q` before Cauchy–Schwarz. It is recorded as `T-22803` and remains open.

This is the same arithmetic obstruction seen in other coordinates:

- the prime-Hardy critical identity orbit;
- the signed common-cell semiprime form;
- local Möbius moments;
- the analytic-totient physical second moment;
- the square-screw negative exponent.

## 5. Exact finite regression

`X-22801` verifies the reduced coefficient identities, the Jordan Bohr energy, and exact physical integrals of the truncated centered packet for `D<=16`.

The maximum ratio

\[
\frac{\int_D^{2D}|S_D(x)|^2dx}{D\mathcal B_D}
\]

is

```text
32421033/18019750
=1.7991943839...
```

at `D=10`, below the retained finite ceiling `9/4`.

Proof-object SHA-256:

```text
0c606242167ca7b7ab213a0a2c9ac97fb8488591c43af1cdb78a2a2fb0e12c9c
```

This is reconnaissance only and does not include the completed endpoint channel.

## 6. Research conclusion

The pass did not deliver the requested full proof. It did achieve three useful things:

1. consolidated the global repository into one common arithmetic obstruction;
2. derived the exact reduced-Farey/Jordan packet that future work should use;
3. proved that a uniform large-sieve/operator shortcut cannot close the critical scale.

The smallest honest next target is the scalar Möbius near-resonance estimate `T-22803`. Any future proof must be visibly Möbius-specific and endpoint-complete.