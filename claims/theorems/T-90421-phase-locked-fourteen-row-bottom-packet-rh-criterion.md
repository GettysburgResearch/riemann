# T-90421 — A phase-locked fourteen-row bottom packet is directly RH-equivalent

Claim ID: `T-90421`  
Title: The unique factor-16 phase-locked source converts the Riemann Hypothesis into critical growth of one explicit fourteen-row carry charge, equivalently one gauged three-scale filter of the two-row bottom charge  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Corrected: 2026-08-11 to restore the deleted column-one gauge  
Dependencies: `L-90423`, `L-90426`, corrected `L-90427`; classical `RH <=> M(x)=O_epsilon(x^(1/2+epsilon))`  
Scope: exact finite criterion; does not prove its critical estimate or RH

## 1. Critical hinge and its inverse coefficients

For an integer endpoint `X`, put

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X},
\qquad q\ge2.
\tag{T-90421.1}
\]

Let `c_X(n)` be the unique triangular coefficients satisfying

\[
\boxed{
w_X(q)=\sum_{n=q}^Xc_X(n)\beta_{nq}.
}
\tag{T-90421.2}
\]

The dyadic dipole bottom charge is

\[
\boxed{C_X=5c_X(2)+3c_X(3).}
\tag{T-90421.3}
\]

By `L-90426`, with the column-one-deleted Riesz sum,

\[
\boxed{C_X=-6\mathcal R_{\omega_2}^{\circ}(X).}
\tag{T-90421.4}
\]

## 2. Phase-locked fourteen-row charge

Let `Y_*(n)` be the explicit row weights of `L-90427.7` and define

\[
\boxed{
\mathcal C_*(X)=\sum_{n=2}^{15}Y_*(n)c_X(n).
}
\tag{T-90421.5}
\]

Finite pairing gives

\[
\boxed{
\mathcal C_*(X)=\mathcal R_{b_*}^{\circ}(X),
}
\tag{T-90421.6}
\]

where

\[
B_*(s)=\sum_{n\ge1}b_*(n)n^{-s}
 =\frac{Q_*(2^{-s})}{2\zeta(s)}.
\tag{T-90421.7}
\]

For aligned endpoints divisible by four, corrected `L-90427.15` yields

\[
\boxed{
\begin{aligned}
-6\mathcal C_*(X)
={}&C_X-3\sqrt2\,C_{X/2}+4C_{X/4}\\
&-6(4-3\sqrt2)\log X
 -6(3\sqrt2-8)\log2.
\end{aligned}}
\tag{T-90421.8}
\]

The logarithmic line is the exact deleted-column-one gauge. It is elementary and subpower, but it may not be omitted from an exact finite identity.

Equivalently, if

\[
\widehat C_X=C_X-6\log X,
\qquad
\widehat{\mathcal C}_*(X)=-6\mathcal R_{b_*}^{\rm full}(X),
\tag{T-90421.9}
\]

then the full Riesz sums obey the gauge-free relation

\[
\boxed{
\widehat{\mathcal C}_*(X)
 =\widehat C_X-3\sqrt2\,\widehat C_{X/2}
  +4\widehat C_{X/4}.
}
\tag{T-90421.10}
\]

## 3. Mellin transform and pole visibility

Because `b_*(1)=1`,

\[
\boxed{
\int_1^\infty\mathcal C_*(X)X^{-z-1}\,dX
 =\frac{B_*(z+1/2)-1}{z^2}.
}
\tag{T-90421.11}
\]

If `rho` is a zeta zero with `Re rho>1/2`, then `z=rho-1/2` is a pole unless

\[
Q_*(2^{-\rho})=0.
\]

By `L-90423`, the zeros of this numerator lie only on

\[
\operatorname{Re}\rho\in\{-1,0,1,2\},
\]

so no nontrivial open-strip zero is cancelled.

## 4. RH equivalence

Assume RH. Since `b_*` is a fixed finite dyadic convolution of `mu`, the classical Mertens bound under RH gives

\[
\sum_{n\le x}b_*(n)=O_\epsilon(x^{1/2+\epsilon}).
\tag{T-90421.12}
\]

Partial summation against `n^-1/2 log(X/n)` gives

\[
\boxed{
\mathcal C_*(X)=O_\epsilon(X^\epsilon)
\quad\text{for every }\epsilon>0.
}
\tag{T-90421.13}
\]

Conversely, (T-90421.13) makes (T-90421.11) holomorphic in every half-plane `Re z>epsilon`. The zero-safe numerator excludes every zeta zero with `Re rho>1/2+epsilon`. Letting `epsilon` tend to zero and using functional-equation symmetry yields RH.

Therefore

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathcal C_*(X)=O_\epsilon(X^\epsilon)
\quad\text{for every }\epsilon>0.
}
\tag{T-90421.14}
\]

Using (T-90421.8), this is equivalently the subpower estimate for the **gauged** phase-locked bottom combination

\[
\boxed{
\begin{aligned}
&C_X-3\sqrt2\,C_{X/2}+4C_{X/4}\\
&\qquad-6(4-3\sqrt2)\log X
 -6(3\sqrt2-8)\log2
 =O_\epsilon(X^\epsilon).
\end{aligned}}
\tag{T-90421.15}
\]

The explicit logarithm is already `O_epsilon(X^epsilon)`; it does not change the equivalence, only the exact finite normalization.

## 5. Five Möbius-adjoint states

Extend the target by `w_X(1)=0` and put

\[
u_m(X)=\sum_{k\le X/m}\mu(k)w_X(mk).
\tag{T-90421.16}
\]

Corrected `L-90427.17` gives the exact alternative normal form

\[
\boxed{
\mathcal C_*(X)
 =u_1(X)-\frac{15}{2}u_2(X)
  +\frac{35}{2}u_4(X)-15u_8(X)+4u_{16}(X).
}
\tag{T-90421.17}
\]

The `u_1` state is mandatory. A four-state formula obtained by deleting it is false in general.

## 6. Significance

The phase-locked filter unifies three formerly separate frontiers:

```text
PIG mean / factor-16 endpoint scalar;
dyadic opposite-parity source;
two-low-row carry charge.
```

The critical source has a positive inverse and zero bare field, while the entire carry consumer is finite-dimensional. What remains is not source typing or an infinite endpoint ledger; it is the critical estimate for the displayed finite charge.

The criterion is not a proof. In particular, phase lock and finite row support do not imply the bound (T-90421.13).

## 7. Proof boundary

Closed exactly here:

1. fourteen-row pairing;
2. corrected gauged two-row identity;
3. full gauge-free Riesz identity;
4. Mellin transform;
5. zero safety;
6. `RH =>` critical growth;
7. critical growth `=> RH`;
8. exact five-state Möbius-adjoint normal form.

Open:

1. unconditional critical growth of the finite charge;
2. any sufficient sign/variation theorem for it;
3. RH.
