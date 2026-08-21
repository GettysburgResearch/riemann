# L-32402 — Pointwise analysis–synthesis gap for the parity Euler filter bank

Claim ID: `L-32402`  
Title: The exact parity-paired Bézout synthesis has a strict pointwise multiplier budget below the closed-strip analysis reserve  
Status: **PROPOSED COMPLETE FINITE-FILTER LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #263 `L-26205` and `L-26206`  
Scope: local multiplier/filter-bank reserve; finite physical-block boundary routing remains separate

## 1. Analysis and synthesis filters

Retain

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2
\]

and the exact positive-coefficient Bézout polynomial

\[
\begin{aligned}
U(z)={}&\frac12
+\frac{21\sqrt2-22}{6}z
+\frac{6+\sqrt2}{6}z^2
+\frac{14-9\sqrt2}{3}z^3.
\end{aligned}
\tag{L-32402.1}
\]

PR #263 proves

\[
\boxed{U(z)p(z)+U(-z)p(-z)=1}
\tag{L-32402.2}
\]

and, on the complete critical annulus

\[
\frac12\le|z|\le\frac1{\sqrt2},
\]

\[
\boxed{|p(z)|^2+|p(-z)|^2\ge\frac{45}{4}.}
\tag{L-32402.3}
\]

## 2. Uniform pointwise synthesis norm

Every coefficient of `U` is positive. Hence for `|z|<=1/sqrt(2)`,

\[
|U(z)|\le U(1/\sqrt2),
\qquad
|U(-z)|\le U(1/\sqrt2).
\]

A direct simplification gives

\[
\boxed{
U(1/\sqrt2)=\frac{36-7\sqrt2}{12}.
}
\tag{L-32402.4}
\]

Therefore

\[
\boxed{
|U(z)|^2+|U(-z)|^2
\le
\frac{697-252\sqrt2}{36}
=:C_*.
}
\tag{L-32402.5}
\]

The comparison with the analysis reserve is exact:

\[
\boxed{
\frac{45}{4}-C_*
=\frac{63\sqrt2-73}{9}>0,
}
\tag{L-32402.6}
\]

because `63^2*2=7938>73^2=5329`.

Equivalently,

\[
\boxed{
\rho_*:=\frac{C_*}{45/4}
=\frac{697-252\sqrt2}{405}<1.
}
\tag{L-32402.7}
\]

## 3. Exact pointwise operator statements

For every vector `y=(y_+,y_-) in C^2`, Cauchy--Schwarz and (L-32402.5) give

\[
\boxed{
|U(z)y_++U(-z)y_-|^2
\le C_*(|y_+|^2+|y_-|^2).
}
\tag{L-32402.8}
\]

For an analyzed scalar source `f`,

\[
y=(p(z)f,p(-z)f),
\]

one has both exact reconstruction

\[
U(z)y_++U(-z)y_-=f
\tag{L-32402.9}
\]

and the strict analysis reserve

\[
|y_+|^2+|y_-|^2\ge\frac{45}{4}|f|^2.
\tag{L-32402.10}
\]

Thus the parity pair is a finite perfect-reconstruction frame with a strict pointwise separation between the analysis lower weight and the worst synthesis coefficient norm.

## 4. Why this is stronger than the old coefficient-budget observation

`L-26206` already noted

\[
2\sum_j u_j^2<45/4,
\]

but correctly warned that coefficient norms and analysis multipliers occupy different operator positions.

The present lemma places **both quantities pointwise in the same Fourier-multiplier coordinate**. It therefore survives arbitrary vertical frequency and the full closed critical annulus.

It still does not by itself prove a localized physical-block contraction: the synthesis shifts `0,log2,2log2,3log2` move a unit logarithmic block into finitely many neighboring blocks, and PR #241's local normal kernel couples independent frequencies. A valid completion must route those finite shifts and the endpoint/boundary rows explicitly.

## 5. Consequence for the full attack

The parity-filter source itself has an absolute strict reserve; neither loss of the inverse-zeta pole nor a large synthesis multiplier can be the final obstruction. The remaining question is now a finite-block charge-routing problem in which the available pointwise reserve is the explicit gap

\[
(63\sqrt2-73)/9.
\]

That reserve can be inserted into a physical Schur ledger without the normalization ambiguity of an arbitrary rescaling.

## 6. Proof boundary

Closed exactly: the pointwise analysis–synthesis multiplier gap on the complete critical annulus.

Open: its source-complete localized two-frequency block routing, the final strict recurrence, and RH.