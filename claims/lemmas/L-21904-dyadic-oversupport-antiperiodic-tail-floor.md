# L-21904 — Dyadic oversupport gives an antiperiodic cardinal-tail floor

Claim ID: `L-21904`  
Title: A twice-period smooth cardinal has an exact half-grid annihilator and a uniform corrected-tail floor  
Status: **PROPOSED — EXACT FOURIER ALGEBRA; UNIFORM POISSON TAIL RATE EXPLICITLY ASSUMED/DERIVED FROM THE SAFE-SUPPORT GRAPH BOUND**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-15631`; `L-21504`; `L-21505`; `L-21506`; `L-21901`; elementary shifted Parseval  
Scope: ordinary corrected-tail metric for the complete cardinal quotient

## 1. Twice-period differential cardinals

Fix a period `L>0`, put

\[
 I_L=[-L/2,L/2],
 \qquad
 \omega_k={2\pi k\over L},
 \qquad
 \nu_j={(2j+1)\pi\over L}.
 \tag{L-21904.1}
\]

Let `eta in C_c^infinity((-a,a))`, `int eta=1`, and assume `L>4a`.  Replace the
length-`L` box in `L-15631` by the twice-period box

\[
 b_{2L}(t)={1\over2L}{\bf1}_{[-L,L]}(t),
 \qquad
 \chi_{2L}=b_{2L}*\eta.
 \tag{L-21904.2}
\]

Define

\[
 q^{(2)}_{k,L}(t)
 =
 { (\partial_t+1/2)
   [\chi_{2L}(t)e^{i\omega_kt}]
  \over i\omega_k+1/2}.
 \tag{L-21904.3}
\]

With

\[
 S_{2L}(w)={\sin(Lw)\over Lw},
 \qquad S_{2L}(0)=1,
 \tag{L-21904.4}
\]

one has

\[
 \widehat q^{(2)}_{k,L}(z)
 =S_{2L}(z-\omega_k)
  {iz+1/2\over i\omega_k+1/2}
  \widehat\eta(z-\omega_k).
 \tag{L-21904.5}
\]

Therefore

\[
 \boxed{
 \widehat q^{(2)}_{k,L}(\omega_j)=\delta_{kj},
 \qquad
 \widehat q^{(2)}_{k,L}(\nu_j)=0,
 \qquad
 \widehat q^{(2)}_{k,L}(i/2)=0.
 }
 \tag{L-21904.6}
\]

The second identity is the new ingredient: the raw source vanishes on the
complete antiperiodic half-grid while remaining cardinal on the periodic grid.

Let `f^(2)_(k,L)` be the corresponding even multiplicative source and put

\[
 h_{k,L}(t)=E(f^{(2)}_{k,L})(e^t).
 \tag{L-21904.7}
\]

By `L-21504`, each `h_(k,L)` is Schwartz on the logarithmic line.  Its
periodization contains exactly the `k`th periodic mode.

## 2. Sharp finite vector and corrected tail

At a zeta-safe support, divide by the diagonal arithmetic multiplier only after
support selection, as in `L-21506`.  In the resulting finite Fourier
coordinates, a coefficient vector `c=(c_k)_(|k|<=N)` represents

\[
 y_c(t)=\sum_{|k|\le N}c_k\phi_k(t){\bf1}_{I_L}(t),
 \qquad
 \phi_k(t)=L^{-1/2}e^{i\omega_kt},
 \tag{L-21904.8}
\]

and hence

\[
 \|y_c\|_2=\|c\|_{\ell^2}.
 \tag{L-21904.9}
\]

Let `h_c` be the corresponding exact global arithmetic radical and define the
complete corrected tail

\[
 \boxed{W_c=h_c-y_c.}
 \tag{L-21904.10}
\]

The zero-side identity of `L-21505` gives

\[
 Q_W(y_c,y_d)=Q_W(W_c,W_d)
 \tag{L-21904.11}
\]

for all finite coefficient vectors.

## 3. Exact antiperiodization identity

For a function whose translated cells are summable in `L2(I_L)`, define

\[
 (\mathcal A_Lg)(t)
 =\sum_{m\in\mathbb Z}(-1)^m g(t+mL),
 \qquad t\in I_L.
 \tag{L-21904.12}
\]

Its Fourier series uses the half-grid `nu_j`, and shifted Parseval gives

\[
 \langle\mathcal A_Lg,L^{-1/2}e^{i\nu_jt}\rangle
 =L^{-1/2}\widehat g(\nu_j).
 \tag{L-21904.13}
\]

Equation (L-21904.6) implies

\[
 \mathcal A_Lh_c=0.
 \tag{L-21904.14}
\]

Since `y_c` is supported in the fundamental interval,

\[
 \mathcal A_Ly_c=y_c.
 \tag{L-21904.15}
\]

Consequently

\[
 \boxed{\mathcal A_LW_c=-y_c.}
 \tag{L-21904.16}
\]

This identity is exact.  It does not use RH, a zero table, a prolate
asymptotic, or an estimate for a Poisson alias.

## 4. Two main cells and the negative-tail remainder

For `t in I_L`, write

\[
 W_m(t)=W_c(t+mL).
 \tag{L-21904.17}
\]

The underlying multiplicative source is supported in logarithmic coordinates
inside `[-L-a,L+a]`.  Hence its arithmetic image vanishes for `t>L+a`.
Because `L>4a`,

\[
 W_m=0\qquad(m\ge2).
 \tag{L-21904.18}
\]

Let

\[
 \mathcal E_Lc
 =\sum_{m\le-1}(-1)^mW_m.
 \tag{L-21904.19}
\]

Then (L-21904.16) becomes

\[
 W_0-W_1+\mathcal E_Lc=-y_c.
 \tag{L-21904.20}
\]

The Poisson formula of `L-21504`, applied at any fixed derivative order
`p>=3`, gives on `t<=-L/2`

\[
 |h_c(t)|
 \le C_p\,e^{(p-1/2)t}
 \|\text{source synthesis}(c)\|_{W^{p,1}}.
 \tag{L-21904.21}
\]

On the zeta-safe supports of `L-21506`, the inverse arithmetic multiplier and
the raw source graph are `exp(o(L))`.  Therefore, uniformly on every
`N=exp(o(L))` coefficient packet,

\[
 \boxed{
 \|\mathcal E_Lc\|_{L^2(I_L)}
 \le\epsilon_L\|c\|_2,
 \qquad
 \epsilon_L=\exp[-c_pL+o(L)]\longrightarrow0.
 }
 \tag{L-21904.22}
\]

For the quadratic-log packet, all losses are merely polynomial in `L` and one
may take any fixed `c_p<(p-1/2)/2` after enlarging the finite threshold.

## 5. Uniform ordinary-tail floor

Equations (L-21904.20) and (L-21904.22) give

\[
 \|W_0-W_1\|_2
 \ge(1-\epsilon_L)\|c\|_2.
 \tag{L-21904.23}
\]

The parallelogram inequality gives

\[
 \|W_0\|_2^2+\|W_1\|_2^2
 \ge{1\over2}\|W_0-W_1\|_2^2.
 \tag{L-21904.24}
\]

Since all remaining cells contribute nonnegative norm,

\[
 \boxed{
 \|W_c\|_2^2
 \ge {1\over2}(1-\epsilon_L)^2\|c\|_2^2.
 }
 \tag{L-21904.25}
\]

Thus the complete cardinal corrected-tail Gram satisfies

\[
 \boxed{
 D_{C,L}\succeq
 {1\over2}(1-\epsilon_L)^2G_{C,L}.
 }
 \tag{L-21904.26}
\]

The all-grid completion is therefore not merely algebraically surjective.  It
has a uniform ordinary-tail moat.

## 6. Quotient version after a fixed low packet

Let `W_R:R_L->L2(R)` be a fixed-dimensional low corrected-tail synthesis.  To
pass from the cardinal-only floor to a joint Schur floor, one must retain the
following explicit cell hypothesis; negative-cell decay alone is not enough:

\[
 \boxed{
 \|\mathcal A_L f\|_{L^2(I_L)}
 \le(\sqrt2+o(1))\|f\|_{L^2(\mathbb R)}
 \quad
 \text{for every }f\in\operatorname{Ran}(W_C\oplus W_R).
 }
 \tag{L-21904.27}
\]

For compact two-cell source images this follows from the same parallelogram
estimate as Section 5 plus the aggregate `o(1)` ledger for all remaining
translated cells.  A production use with a prolate/BV low source must verify
this joint translated-cell bound; it may not infer it from dimension alone.

Put

\[
 B_L=\Pi_N\mathcal A_LW_R(R_L)\subset E_N(L)
 \tag{L-21904.28}
\]

and choose the cardinal quotient `C_L` to be `G`-orthogonal to `B_L` and to the
finite low vectors themselves.  Then for all `c in C_L` and `r in R_L`,

\[
 \langle y_c,\mathcal A_LW_Rr\rangle=0.
 \tag{L-21904.29}
\]

Since `y_c in E_N(L)`, the high-Fourier part of `mathcal A_LW_Rr` is also
orthogonal to `y_c`; hence

\[
 \|\mathcal A_L(W_Cc+W_Rr)\|_2^2
 \ge\|y_c\|_2^2.
 \tag{L-21904.30}
\]

Combining this with (L-21904.27) gives

\[
 \boxed{
 \inf_{r\in R_L}
 \|W_Cc+W_Rr\|_2^2
 \ge[1/2-o(1)]\|c\|_2^2.
 }
 \tag{L-21904.31}
\]

Equivalently, the ordinary-tail Schur short of the cardinal block by the fixed
low packet has a uniform positive floor, **provided the declared joint-cell
bound (L-21904.27) is proved**.

The codimension added in (L-21904.28) is at most twice `dim R_L`; it does not
affect a growing complete Fourier diagonal.

## 7. Consequence and boundary

The unconditional-in-the-cardinal-frame conclusion is

```text
twice-period all-grid cardinals
=> complete ordinary corrected-tail floor >=1/2-o(1).
```

The hybrid low-packet quotient additionally requires the explicit joint-cell
hypothesis (L-21904.27).  This requirement is now stated rather than silently
inferred.

Neither conclusion proves the sign of the actual Weil form.  A hypothetical
off-line zero may still create a signed zero-side orbit.  That arithmetic sign
must be handled by the line-centered/actual-orbit theorem or by an independent
prime-side argument.

- The half-grid algebra and antiperiodization identity are exact.
- The decay rate (L-21904.22) follows from the declared safe-support graph bound
  and classical Poisson decay; production must bind its constants in the exact
  source normalization.
- The cardinal-only floor is complete under that graph bound.
- The quotient floor is conditional on the joint translated-cell operator
  bound (L-21904.27).
- No RH conclusion is claimed by this lemma alone.
