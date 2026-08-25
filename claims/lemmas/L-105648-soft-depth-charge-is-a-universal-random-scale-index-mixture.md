# L-105648 — Soft depth charge is a universal random-scale index mixture

Claim ID: `L-105648`  
Status: **PROVED EXACT FOR FINITE REDUCED INNER QUOTIENTS**  
Created: 2026-08-25  
Depends on: `L-105642--L-105647`; sibling `L-106431`, `L-106514`  
RH status: **not assumed**

## 1. Universal scale law

Define the probability density

\[
\boxed{
d\mu(s)={2s\over(1+s)^3}\,ds,
\qquad s>0.
}
\tag{L-105648.1}

Indeed,

\[
\int_0^\infty {2s\over(1+s)^3}\,ds=1.
\]

For every `x>=0`, split the integral at `s=x`.  Exact integration gives

\[
\begin{aligned}
\int_0^\infty
\min\left(1,{x\over s}\right)d\mu(s)
&=
\int_0^x{2s\over(1+s)^3}ds
+x\int_x^\infty{2\over(1+s)^3}ds\\
&={x^2\over(1+x)^2}+{x\over(1+x)^2}.
\end{aligned}
\]

Therefore

\[
\boxed{
{x\over1+x}
=
\int_0^\infty
\min\left(1,{x\over s}\right)d\mu(s).
}
\tag{L-105648.2}

## 2. One zero: soft charge is averaged exact index

Let a factor have depth `delta>0`, and let `H>0`.  Put

\[
x={2\delta\over H}.
\]

Then (L-105648.2) and `L-105647` give

\[
\boxed{
{2\delta\over H+2\delta}
=
\int_0^\infty
\min\left(1,{\delta\over Hs/2}\right)d\mu(s).
}
\tag{L-105648.3}

The integrand is the exact clipped logarithmic index of the one-factor
Blaschke product on the adaptive interior line

\[
y={Hs\over2}.
\]

Thus the familiar soft depth price is not a heuristic relaxation of degree.
It is a universal positive average of exact integer-index regularizations.

## 3. Complete finite quotient

Let

\[
U=\omega{A\over B}
\]

be the reduced finite quotient of `L-105647`, with numerator depths `eta_j`
and denominator depths `delta_k`.  Define its signed soft-depth functional

\[
\boxed{
\mathfrak D_H(U)
=
\sum_k{2\delta_k\over H+2\delta_k}
-
\sum_j{2\eta_j\over H+2\eta_j}.
}
\tag{L-105648.4}

Factorwise application of (L-105648.3), followed by finite summation, gives

\[
\boxed{
\mathfrak D_H(U)
=
\int_0^\infty
\mathfrak J_{Hs/2}(U)\,{2s\over(1+s)^3}\,ds.
}
\tag{L-105648.5}

Equivalently, after `y=Hs/2`,

\[
\boxed{
\mathfrak D_H(U)
=
\int_0^\infty
\mathfrak J_y(U)
{8Hy\over(H+2y)^3}\,dy.
}
\tag{L-105648.6}

The final kernel is itself a probability density on `(0,infinity)`.

Because `mathfrak J_y` is additive, equations (L-105648.5)--(L-105648.6)
remain exact with arbitrary horizontal clustering and arbitrary multiplicity.
No nonorthogonal model-space packet Gram appears.

## 4. Integer index as the zero-scale limit

For every fixed finite quotient,

\[
{2\delta\over H+2\delta}\longrightarrow1
\qquad(H\downarrow0).
\]

Therefore

\[
\boxed{
\lim_{H\downarrow0}\mathfrak D_H(U)
=\deg B-\deg A
=-\operatorname{wind}U.
}
\tag{L-105648.7}

The signed integer index is the zero-scale limit of a positive random-scale
average of interior logarithmic defects.

## 5. Relation to the Xi current metric

For the elementary exponential source metric, the one-zero model-space charge
is exactly

\[
{2\delta\over H+2\delta}.
\]

Hence (L-105648.3) identifies the reference owner law of `L-105646` with a
universal random adaptive-index law.  The Maxwell sandwich on PR #729 then
places the actual Xi current owner survival within three percent of this exact
physical logarithmic-index average throughout `0<=H<=1/2`.

For a finite product `B`, the additive sum

\[
\sum_k{2\delta_k\over H+2\delta_k}
\]

is an exact divisor functional and an upper bound for the exponential
model-space trace.  It is not asserted to equal that trace when the model
vectors are nonorthogonal.

## 6. Scope

This theorem closes the source-softness versus integer-index dictionary at the
finite divisor level.  It does not control the oriented phase-angle energy
`||H_U||_(S_2)^2`, the canonical-correlation defect between `K_A` and `K_B`, or
the pointwise Xi two-trace evaluation.  The degree-zero separator in
`R-105647` proves that those remaining quantities cannot be recovered from the
signed index alone.  Cofinal entire-function passage and RH remain open.
