# R-22301 — Standard Dirichlet-Hardy embedding misses the critical identity orbit

Claim ID: `R-22301`  
Title: Neither the standard H2 embedding nor the weak-product norm controls the boundary orbit required by T-22301  
Status: `PROPOSED — COMPLETE FUNCTIONAL-ANALYTIC NO-GO`  
Authoring agent: `gpt56-pro-19`  
Created: 2026-08-07  
Issue: #223  
Dependencies: elementary phase alignment; the definition of Dirichlet Hardy and weak-product norms

## 1. The tempting but invalid shortcut

For `sigma>0`, the formal prime ray

\[
 f_\sigma(s)
 =\sum_p\frac{\log p}{p^{1/2+\sigma}}p^{-s}
 \tag{R-22301.1}
\]

has square-summable coefficients, so it belongs to the Dirichlet Hardy space
`mathscr H^2`. Its square lies in the weak product

\[
 \mathscr H^2_0\odot\mathscr H^2_0.
\]

The required prime boundary value is

\[
 f_\sigma(it)=P_1(1/2+\sigma+it).
 \tag{R-22301.2}
\]

It is therefore tempting to invoke the classical local embedding of
`mathscr H^2`. That theorem evaluates a Dirichlet series on

\[
 \Re s=\frac12,
\]

which would give `P_1(1+sigma+it)`, not (R-22301.2). The target lies one full
half-plane step farther left, on the untwisted Bohr-boundary orbit.

This mismatch is load-bearing.

## 2. Universal weighted boundary embedding is false

Let `w` be any nonnegative continuous function with `w(0)>0`. There is no
constant `C_w` such that

\[
 \int_{\mathbb R}w(t)|f(it)|^2dt
 \le C_w\|f\|_{\mathscr H^2}^2
 \tag{R-22301.3}
\]

for all Dirichlet polynomials `f`.

### Proof

For an integer `N>=2`, put

\[
 f_N(s)=\frac1{\sqrt N}
 \sum_{n=N+1}^{2N}n^{-s}.
 \tag{R-22301.4}
\]

Then

\[
 \|f_N\|_{\mathscr H^2}=1.
 \tag{R-22301.5}
\]

Choose

\[
 0<\delta<\frac{1}{6\log2}.
\]

For `|t|<=delta`, after removing the common phase `N^{-it}`, all phases

\[
 \exp\{-it\log(n/N)\},
 \qquad N<n<=2N,
\]

lie in an arc of angular width below `1/3`. Their real parts in the bisecting
direction are at least `cos(1/6)`. Hence

\[
 |f_N(it)|
 \ge\sqrt N\cos(1/6)
 \qquad(|t|\le\delta).
 \tag{R-22301.6}
\]

By continuity, shrink `delta` if needed so that `w(t)>=w(0)/2` there. Therefore

\[
 \int w(t)|f_N(it)|^2dt
 \ge
 \delta w(0)N\cos^2(1/6),
 \tag{R-22301.7}
\]

which tends to infinity. QED.

For the safe multiplier in `T-22301`,

\[
 w_\sigma(t)=|\widehat H(\sigma+it)|^2
\]

has `w_sigma(0)>0` whenever `0<sigma<1/2`, because the transform has no zeros
in the open counterexample strip. Thus the no-go applies exactly at the desired
weight.

## 3. Weak products do not repair the problem

The same sequence disproves a universal critical weak-product embedding. Since

\[
 \|f_N^2\|_{\mathscr H^2\odot\mathscr H^2}
 \le\|f_N\|_{\mathscr H^2}^2=1,
 \tag{R-22301.8}
\]

but

\[
 \int w(t)|f_N(it)^2|dt
 =\int w(t)|f_N(it)|^2dt
 \to\infty,
 \tag{R-22301.9}
\]

there is no bounded map from the full weak product to the weighted identity
orbit required by `T-22301`.

This is consistent with the known subtlety of weak products and multiplicative
Hankel forms: a Bohr-torus product norm does not control an exceptional
one-parameter boundary orbit.

## 4. What remains possible

The no-go is universal, not ray-specific. It does not rule out the desired
estimate for the single arithmetic family

\[
 f_\sigma(s)=\sum_p\frac{\log p}{p^{1/2+\sigma}}p^{-s}.
\]

A proof must exploit at least one of:

1. the prime support and its exact Möbius/Selberg identities;
2. the fixed safe multiplier and its vanishing moments;
3. the one-dimensional semiprime coefficient structure of `L-22301`;
4. a restricted Carleson estimate valid only for this arithmetic ray.

## 5. Scope

This refutes the shortcut

```text
standard Dirichlet-Hardy embedding
or weak-product membership
=> T-22301 critical H1 bound.
```

It does not refute `T-22301`, and it does not prove divergence for the prime
ray. The special ray remains the exact RH-bearing object.
