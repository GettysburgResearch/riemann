# L-15613 — Phase-aware pole-free prime-error band

Claim ID: `L-15613`  
Title: Certified zero phases plus an explicit unmodeled-zero tail give a finite RH-valid interval for one raw prime-power window  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: `T-15404`; the smoothed von Mangoldt explicit formula; an explicit zero-count majorant  
Scope: proof-producing finite disproof bound for pole-free prime windows  
Related counterexample candidates: none

## 1. Pole-free raw prime statistic

Let

\[
 G\in C_c^\infty([A,B];\mathbb R),\qquad 0<A<B,
\]

and define its one-sided Laplace transform

\[
 g(z)=\int_A^B e^{-zu}G(u)\,du.
 \tag{1}
\]

Assume

\[
 g(1/2)=0.
 \tag{2}
\]

For `x>B`, put

\[
 Q_G(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}G(x-\log n).
 \tag{3}
\]

Only prime powers in the finite annulus

\[
 e^{x-B}\le n\le e^{x-A}
\]

contribute.

Under the explicit-formula normalization of `T-15404`,

\[
 \boxed{
 Q_G(x)=
 -\sum_\rho m_\rho e^{(\rho-1/2)x}g(\rho-1/2)
 -\sum_{j\ge1}e^{-(2j+1/2)x}g(-2j-1/2).}
 \tag{4}
\]

The first sum is over nontrivial zeros with multiplicity and the second over the
trivial zeros. Equation (2) cancels the zeta pole before the prime sum is
formed.

## 2. Selected phase model

Let

\[
 \mathcal Z=\{(\gamma_r,m_r):1\le r\le R\}
\]

be a proof-grade finite collection of actual critical-line zeros
`1/2+i gamma_r`, with multiplicities. Define the selected phase model

\[
 S_{\mathcal Z}(x)
 =-2\operatorname{Re}
   \sum_{r=1}^R m_r e^{i\gamma_r x}g(i\gamma_r).
 \tag{5}
\]

For an integer `M>=0`, define the retained trivial-zero model

\[
 T_M(x)
 =-\sum_{j=1}^M e^{-(2j+1/2)x}g(-2j-1/2).
 \tag{6}
\]

In production, zero ordinates and transforms are directed intervals. Equation
(5) denotes the exact quantity enclosed by that finite calculation.

## 3. Finite shell accounting

Let

\[
 0=T_0<T_1<\cdots<T_K=T
\]

be a finite ordinate partition. For every shell

\[
 I_k=(T_k,T_{k+1}],
\]

suppose:

1. `M_k` is a rigorous upper bound for the total multiplicity of positive-
   ordinate nontrivial zeros in `I_k`;
2. `r_k` is the total multiplicity of selected members of `mathcal Z` whose
   certified balls lie wholly in `I_k`;
3. `H_k` is a rigorous upper bound
   \[
    |g(it)|\le H_k\qquad(t\in I_k).
   \tag{7}
   \]

Then, under RH, the unselected zeros in `I_k` contribute at most

\[
 2(M_k-r_k)H_k
 \tag{8}
\]

to the absolute scalar error. No phase cancellation is used in this residual
budget; all selected phases remain in (5).

A sharp shell count can be obtained from two-sided cumulative bounds

\[
 L_N(t)\le N(t)\le U_N(t)
\]

through

\[
 \boxed{M_k=U_N(T_{k+1})-L_N(T_k).}
 \tag{9}
\]

Subtracting two upper bounds is not valid; upper-at-right minus lower-at-left is.
Exact Turing counts may replace (9) on any finite range.

## 4. Closed high-zero tail

Let `p>=2` be an integer and put

\[
 A_p=\|G^{(p)}\|_{L^1(\mathbb R)}.
 \tag{10}
\]

Integration by parts gives

\[
 |g(it)|\le A_p|t|^{-p}.
 \tag{11}
\]

Suppose the selected/shell calculation is complete through height `T>=e`, and
let `N_T=N(T)` be the exact positive-ordinate zero count through `T`. Let

\[
 U(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}
      +a_0\log t+b_0\log\log t+c_0
 \tag{12}
\]

be any proved upper bound for `N(t)` on `[T,infinity)`. Then

\[
 \sum_{\gamma>T}m_\gamma\gamma^{-p}
 \le
 \boxed{
 \mathfrak Z_p(T)
 :=-N_TT^{-p}
   +p\int_T^\infty U(t)t^{-p-1}\,dt.}
 \tag{13}
\]

Consequently the high-zero scalar tail is bounded by

\[
 \boxed{R_{\rm zero}^{>T}\le2A_p\mathfrak Z_p(T).}
 \tag{14}
\]

If no exact count is available, dropping the negative first term in (13) gives a
weaker valid bound.

### Bellotti--Wong specialization

The explicit estimate

\[
 a_0=0.10076,\qquad b_0=0.24460,\qquad c_0=8.08292
 \tag{15}
\]

is available for `T>=e`. For `p>1`, (13) is bounded explicitly by

\[
\begin{aligned}
\mathfrak Z_p(T)\le{}&-N_TT^{-p}\\
&+\frac{p}{2\pi}T^{1-p}
 \left[
  \frac{\log(T/(2\pi e))}{p-1}
  +\frac1{(p-1)^2}
 \right]\\
&+a_0T^{-p}\left(\log T+\frac1p\right)\\
&+b_0T^{-p}\left(
 \log\log T+\frac1{p\log T}
 \right)
+c_0T^{-p}.
\end{aligned}
 \tag{16}
\]

The `log log` integral was bounded using `1/log t<=1/log T`.

## 5. Trivial-zero remainder

If the first `M` trivial zeros are retained in (6), then for `d=x-B>0`,

\[
 |g(-\lambda)|\le e^{\lambda B}\|G\|_1.
\]

Therefore

\[
 \boxed{
 R_{\rm triv}^{>M}(x)
 \le
 \|G\|_1
 \frac{e^{-(2M+5/2)d}}{1-e^{-2d}}.}
 \tag{17}
\]

The trivial contribution can instead be evaluated to any desired directed
precision and (17) used only for its tail.

## 6. Final RH-valid band

Define

\[
\boxed{
\begin{aligned}
 B_{G,\mathcal Z}(x)
 ={}&2\sum_{k=0}^{K-1}(M_k-r_k)H_k\\
 &+2A_p\mathfrak Z_p(T)
 +R_{\rm triv}^{>M}(x).
\end{aligned}}
 \tag{18}
\]

Then RH implies

\[
 \boxed{
 |Q_G(x)-S_{\mathcal Z}(x)-T_M(x)|
 \le B_{G,\mathcal Z}(x).}
 \tag{19}
\]

Every term in (19) has a finite proof-producing interface:

- a complete prime-power interval for `Q_G(x)`;
- directed selected-zero phase intervals for `S_Z(x)`;
- directed finite trivial-zero terms;
- rational shell counts and transform envelopes;
- the rational high-zero and trivial tails.

If the directed interval for the left side is disjoint from
`[-B_(G,Z)(x),B_(G,Z)(x)]`, RH is false.

## 7. Explicit notched universal-window envelope

For the universal dyadic profile of `L-15405`, prepend notch lengths

\[
 r_\ell=\frac{2\pi}{\widetilde\gamma_\ell},
 \qquad1\le\ell\le q,
\]

and form the pole-free two-shift window of `T-15404`. On the imaginary axis,

\[
 \left|\frac{1-e^{-irt}}{irt}\right|
 \le\min\left\{1,\frac2{r|t|}\right\}.
\]

Hence its transform satisfies the fully explicit monotone envelope

\[
\boxed{
 |g(it)|\le
 3\left[
 \prod_{j\ge1}\min\left\{1,\frac{2^{j+1}}{|t|}\right\}
 \prod_{\ell=1}^q
 \min\left\{1,
 \frac{\widetilde\gamma_\ell}{\pi|t|}
 \right\}
 \right]^2.}
 \tag{20}
\]

This envelope is independent of unknown zeta zeros. Directed sine bounds around
certified notch balls can be inserted in the finite shells and are much sharper
than (20) near the designed ordinates.

For any integer `J` with `2^(J+1)<=T`, (20) gives on `t>=T`

\[
 |g(it)|\le C_{J,q}t^{-2(J+q)},
 \tag{21}
\]

where

\[
 C_{J,q}
 =3\left[
 2^{J(J+3)/2}
 \frac{\prod_{\ell=1}^q\widetilde\gamma_\ell}{\pi^q}
 \right]^2.
 \tag{22}
\]

Thus (14) may use `p=2(J+q)` and `A_p=C_(J,q)` without differentiating the
infinite-convolution density.

## 8. False-RH exposure

Assume additionally

\[
 g(z)\ne0\qquad(0<\operatorname{Re}z<1/2).
 \tag{23}
\]

This holds for the universal notched pole-free window: the dyadic and notch
factors have zeros only on the imaginary axis, while the pole-annihilating
factor has zeros on `Re z=1/2`.

If an off-line zero `rho` with `Re rho>1/2` exists, the Laplace transform of
`Q_G` has an uncancelled pole at `rho-1/2`. Hence `Q_G` is unbounded on the
right. The selected phase model is bounded, the right side of (19) is finite,
and the trivial tail decays. Therefore, for every fixed finite phase model and
valid finite bound, (19) fails along an unbounded sequence of translations.

The theorem does not locate that sequence without the unknown pole. It proves
that any certified finite failure is an unconditional off-line-zero witness.

## Gap audit

- The explicit-formula normalization remains an imported review gate.
- Selected zero balls must be actual zeros with certified multiplicities.
- Every prime power in (3), not merely every prime, is required.
- Formula (16) uses an explicit zero-count result; another proved upper bound can
  be substituted without changing the theorem.
- A midpoint violation is not a certificate.
- This theorem gives an RH-valid finite bound and a disproof interface. It does
  not prove that the bound holds for the Riemann prime statistic.
