# R-23802 — Dependent Gamma domination is not an independent convolution factor

Claim ID: `R-23802`  
Title: The explicit coupling `G>=T` proves stochastic domination but not Gamma–carry convolution order  
Status: **PROPOSED EXACT SCOPE THEOREM / ROUTE CORRECTION**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23804`, `L-23805`, `L-23807`

## 1. The explicit coupling

Let `U_1,U_2` be independent with density

\[
 2u\,\mathbf 1_{0<u<1}\,du.
\]

Put

\[
 M=\lfloor U_2^{-2}\rfloor,
 \qquad
 T=\log\frac{M(M+1)}{M+U_1},
 \tag{R-23802.1}
\]

and

\[
 G=-4\log(U_1U_2).
 \tag{R-23802.2}
\]

`L-23804` shows that `T` has the carry law.  Each variable
`-4 log U_i` is exponential with rate `1/2`, so

\[
 G\sim\operatorname{Gamma}(2,1/2).
\]

Moreover

\[
 \boxed{G\ge T\quad\text{almost surely}.}
 \tag{R-23802.3}
\]

Indeed, (R-23802.3) is equivalent to

\[
 (U_1U_2)^4\le\frac{M+U_1}{M(M+1)}.
\]

If `M>=2`, then

\[
 (U_1U_2)^4\le U_2^4\le M^{-2}
 \le(M+1)^{-1}
 \le\frac{M+U_1}{M(M+1)}.
\]

If `M=1`, then

\[
 (U_1U_2)^4\le U_1^4\le\frac{1+U_1}{2}.
\]

Thus the coupling is an exact pointwise domination, not numerical evidence.

## 2. What domination proves

For every `s>=0`, (R-23802.3) gives only the Laplace order

\[
 \mathbb E e^{-sG}\le\mathbb E e^{-sT}.
 \tag{R-23802.4}
\]

Writing the two transforms as `G(s)` and `P(s)`, this says

\[
 0< A(s):=\frac{G(s)}{P(s)}\le1.
 \tag{R-23802.5}
\]

An independent residual `S>=0` with

\[
 G\overset d=T+S,
 \qquad S\perp T,
 \tag{R-23802.6}
\]

exists if and only if `A` is the Laplace transform of a positive measure;
equivalently, by Bernstein's theorem, `A` is completely monotone on the
positive real axis with the required boundary moment.  The single inequality
(R-23802.5) supplies none of the higher derivative signs.

A finite exact counterexample shows the logical gap.  Let `T_0` equal `0` or
`2`, each with probability `1/2`, and let `G_0=2`.  Then `G_0>=T_0` under the
obvious coupling, but

\[
 \frac{\mathbb E e^{-sG_0}}{\mathbb E e^{-sT_0}}
 =\frac{2}{1+e^{2s}}.
\]

Its third derivative at zero has the wrong sign for complete monotonicity.
Hence pointwise domination does not imply convolution order even in a two-point
model.

## 3. The residual in the explicit coupling is genuinely state dependent

Let

\[
 S_{\rm dep}=G-T.
\]

On a layer with `M=m`, write

\[
 v=m(m+1)e^{-T}-m.
\]

Conditionally on `T=t` in the interior of that layer, the possible values of
`-4 log U_2` lie in

\[
 [2\log m,\,2\log(m+1)),
\]

while `U_1=v` is fixed by `t` and `m`.  Therefore the conditional support of the
residual is

\[
 \boxed{
 \begin{aligned}
 I_m(t)=\big[&2\log m-4\log v-t,\\
             &2\log(m+1)-4\log v-t\big).
 \end{aligned}}
 \tag{R-23802.7}
\]

Both endpoints vary nontrivially with `t`.  Thus this coupling does not hide an
independent residual: its residual law changes with the carry state.

## 4. Sharp scalar minorants cannot repair the dependence

The compactness argument for `L-23807` has the following exact consequence.
Suppose cofinally there are scalar log-translation-covariant minorants `b_X`
with the sharp near-unit mass and exponential first-moment budgets of FGCM.
Tightness gives a probability limit `nu`, the finite convolution inequalities
pass to

\[
 \nu*p\le g,
\]

and equality of total masses forces

\[
 \nu*p=g.
\]

Laplace uniqueness then gives

\[
 \widehat\nu=A,
\]

so `nu` is precisely the canonical Möbius–Riesz factor of `L-23805`.  Hence
sharp scalar FGCM implies GCF.  A successful repair must therefore break the
common scalar convolution profile rather than disguise it.

## 5. Correct pivot

The coupling should be read as evidence for a **state-dependent transport**, not
for independence.  The finite carry system has the additional split coordinate
`j/n`.  Allowing nonnegative transport among those atomized split rows breaks
log-translation covariance while retaining exact finite carry and entropy
identities.  `L-23808/L-23809/T-23802` formulate that pivot.

## 6. Proof boundary

Proved here:

- the explicit domination `G>=T`;
- the exact distinction between Laplace order and convolution order;
- the state dependence of the residual in the displayed coupling;
- the scope consequence of the FGCM compactness theorem.

Not proved here:

- complete monotonicity of `A`;
- GCF;
- the atomized balanced transport theorem;
- RH.
