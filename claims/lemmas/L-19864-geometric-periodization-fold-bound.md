# L-19864 — Geometric periodization folds are controlled by annular tail decay

Claim ID: `L-19864`  
Status: **PROVED ABSTRACT FOLD THEOREM; TARGET APPLICATION USES DECLARED RADIAL DECAY**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-07  
Dependencies: exact folded residual identity `L-19820`; multiplicative annular decomposition  
Scope: separates logarithmic folds from arithmetic Poisson aliases

## 1. Two different alias indices

The arithmetic tail contains Poisson samples indexed by

\[
 k=1,2,3,\ldots,
\]

where radial arguments are `kv`. The periodized finite residual contains a
different sum indexed by logarithmic cells

\[
 m\in\mathbb Z\setminus\{0\},
\]

where arguments are multiplied by powers of the period

\[
 \mu=e^L.
\]

A stationary-phase theorem for the `k`-sum does not by itself control the
`m`-fold. This lemma gives the exact independent estimate.

## 2. Fold operator

Let

\[
 I=[\mu^{-1/2},\mu^{1/2}]
\]

and let `t` be supported outside `I`. Define the fold into the central cell by

\[
 (\mathfrak F_Lt)(u)
 =\sum_{m\ne0}t(\mu^mu),
 \qquad u\in I.
 \tag{L-19864.1}
\]

The formula is interpreted in `L2(I,d*u)`. Separate its lower and upper parts;
by inversion symmetry it is enough to treat one side.

For `m>=1`, put

\[
 T_mt(u)=t(\mu^{-m}u),
 \qquad u\in I.
 \tag{L-19864.2}
\]

## 3. Abstract annular theorem

Assume there are `A_L>=1` and `0<q_L<1` such that

\[
 \boxed{
 \|T_mt\|_{L^2(I)}
 \le A_Lq_L^{m-1}\|t\|_{L^2(\mathbb R_+^*\setminus I)}
 \qquad(m\ge1).}
 \tag{L-19864.3}
\]

Then

\[
 \boxed{
 \|\mathfrak F_Lt\|_{L^2(I)}
 \le {2A_L\over1-q_L}\|t\|_2,}
 \tag{L-19864.4}
\]

and hence

\[
 \boxed{
 \|\mathfrak F_Lt\|_2^2
 \le {4A_L^2\over(1-q_L)^2}\|t\|_2^2.}
 \tag{L-19864.5}
\]

### Proof

Minkowski gives

\[
 \left\|\sum_{m\ge1}T_mt\right\|_2
 \le\sum_{m\ge1}\|T_mt\|_2
 \le {A_L\over1-q_L}\|t\|_2.
\]

Apply the same argument to the upper fold and add. QED.

A weighted Cauchy--Schwarz proof gives the same conclusion under the weaker
square-annular hypothesis

\[
 \sum_{m\ge1}q_L^{-(m-1)}\|T_mt\|_2^2
 \le A_L^2\|t\|_2^2.
 \tag{L-19864.6}
\]

## 4. Radial target specialization

For a normalized radial tail profile satisfying

\[
 |\rho_R(z)|\le {C(\log R)^C\over z}
 \qquad(z\ge2),
 \tag{L-19864.7}
\]

multiplicative scaling gives

\[
 \|T_mt\|_2
 \le C(\log R)^C\mu^{-(m-1)/2}\|t\|_2.
 \tag{L-19864.8}
\]

Thus one may take

\[
 q_L=\mu^{-1/2},
 \qquad
 A_L=C(\log R)^C,
 \tag{L-19864.9}
\]

and obtain

\[
 \boxed{
 \|\mathfrak F_Lt\|_2^2
 \le C(\log R)^C\|t\|_2^2.}
 \tag{L-19864.10}
\]

The same statement holds for a fixed or polylogarithmic packet after replacing
the scalar point bound by the corresponding row-operator bound.

## 5. Xi target specialization

For the exact Xi source, logarithmic Schwartz decay is stronger than
(L-19864.7). For every `B>0`,

\[
 \boxed{
 \|\mathfrak F_Lt_{\Xi}\|_2
 +\|t_{\Xi}\|_2
 \le C_Be^{-BL}.}
 \tag{L-19864.11}
\]

This supplies the target folded-tail estimate requested in the revised review.
Combined with the quadratic-log Fourier projection, the complete Xi residual
obeys (L-19862.8).

## 6. Relationship to the corrected residual

For an exact periodized vector, the complete residual is

\[
 W=t-\iota_L\mathfrak F_Lt.
\]

The two terms have disjoint physical supports, so

\[
 \|W\|_2^2
 =\|t\|_2^2+\|\mathfrak F_Lt\|_2^2.
 \tag{L-19864.12}
\]

Equation (L-19864.10) gives a target upper estimate; the positive second term
can never damage a complement lower index.

## 7. Proof boundary

- The abstract fold theorem and the separation of the `m` and `k` ledgers are
  exact.
- The normalized radial decay (L-19864.7) must be checked in the source-specific
  CCM normalization. It is available for the canonical Bessel profile and is
  far stronger for the Xi source.
- The theorem controls ordinary fold energy. The indefinite Weil comparison is
  the separate affine theorem `L-19865`.