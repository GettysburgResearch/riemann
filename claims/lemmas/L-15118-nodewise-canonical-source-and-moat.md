# L-15118 — Root-free canonical source formulas and an explicit Cauchy moat

Claim ID: `L-15118`  
Status: **PROVED FINITE-DIMENSIONAL LEMMA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15111`; elementary interpolation and Cauchy determinants  
Scope: directed construction of the canonical Loewner matrix and a positive moat  
Related counterexample candidates: none

## 1. Setup

Let the distinct real nodes be

\[
 \lambda_1,\ldots,\lambda_n,
\]

let every target coordinate `p_i` be nonzero, and normalize

\[
 \sum_i p_i=1.
\]

Put

\[
 \Omega(s)=\prod_i(\lambda_i-s),
 \qquad
 \phi_i(s)=\frac{\Omega(s)}{\lambda_i-s},
 \qquad
 P(s)=\sum_i p_i\phi_i(s).
\]

The canonical source and matrix are

\[
 g_i=-\frac{P'(\lambda_i)}{P(\lambda_i)},
 \tag{L-15118.1}
\]

and

\[
 Q^{\rm can}_{ij}=
 \frac{g_i-g_j}{\lambda_i-\lambda_j}
 \quad(i\ne j),
 \qquad
 Q^{\rm can}p=0.
 \tag{L-15118.2}
\]

## 2. Direct coefficient formula

At one node,

\[
 P(\lambda_i)=p_i\phi_i(\lambda_i).
\]

Differentiating the Lagrange sum and dividing by this nonzero value gives

\[
 \boxed{
 g_i
 =-\sum_{j\ne i}
   \frac{1+p_j/p_i}{\lambda_i-\lambda_j}.}
 \tag{L-15118.3}
\]

Thus no polynomial expansion, root finder, or evaluation of `P'` is required.
The off-diagonal canonical matrix follows from ordinary divided differences,
and its diagonal is forced exactly by the known kernel:

\[
 \boxed{
 Q^{\rm can}_{ii}
 =-\frac1{p_i}
   \sum_{j\ne i}Q^{\rm can}_{ij}p_j.}
 \tag{L-15118.4}
\]

Equations (L-15118.3)--(L-15118.4) are often substantially better conditioned
than expanding a high-degree interpolation polynomial.

## 3. Cardinal/log-derivative form on an integer grid

Assume the nodes are `-N,...,N`.  Let

\[
 A(s)=\frac{\sin\pi s}{\pi}
      \sum_{j=-N}^{N}\frac{p_j}{s-j},
\]

so `A(n)=(-1)^n p_n` up to the fixed centering convention.  A removable-limit
calculation gives

\[
 \frac{A'(n)}{A(n)}
 =\sum_{j\ne n}\frac{p_j}{p_n(n-j)}.
\]

Hence

\[
 \boxed{
 g_n
 =-\left(H_{N+n}-H_{N-n}\right)
  -\frac{A'(n)}{A(n)}.}
 \tag{L-15118.5}
\]

If the physical frequency is

\[
 z=hs,
 \qquad h=\frac{2\pi}{L},
\]

and `F(z)=A(z/h)` up to a nonzero scalar and phase, then

\[
 \boxed{
 g_n
 =-\left(H_{N+n}-H_{N-n}\right)
  -h\frac{F'(hn)}{F(hn)}.}
 \tag{L-15118.6}
\]

This identity exposes the canonical source as a finite harmonic endpoint term
plus the sampled logarithmic derivative of the actual compact transform.  It is
the natural comparison point for the explicit arithmetic source in `L-15119`.

## 4. Exact interval construction

If

\[
 p_i\in[p_{i,-},p_{i,+}],
 \qquad 0\notin[p_{i,-},p_{i,+}],
\]

then (L-15118.3) can be evaluated with outward rational or ball arithmetic.
Every quotient `p_j/p_i` is directed, followed by exact node differences.
The diagonal is then evaluated using (L-15118.4), preserving the exact symbolic
kernel rather than allowing a rounded null eigenvalue to drift.

A rational center matrix `Q_0` and symmetric entry radii feed directly into the
kernel-pinned inertia transfer `L-15113`.

## 5. Explicit lower bound for the canonical positive moat

Assume `P` has `n-1` simple real roots

\[
 r_1,\ldots,r_{n-1}.
\]

Let

\[
 U_{ik}=\frac1{\lambda_i-r_k}.
\]

Then `L-15111` gives

\[
 Q^{\rm can}=UU^{\mathsf T}.
\]

Choose any `n-1` node indices and let `C` be the corresponding square Cauchy
minor.  Put

\[
 S=\|U\|_F^2
 =\sum_{i,k}\frac1{(\lambda_i-r_k)^2}.
\]

The smallest nonzero eigenvalue of `Q^can`, denoted `m_can`, satisfies

\[
 \boxed{
 m_{\rm can}
 \ge\frac{|\det C|^2}{S^{n-2}}.}
 \tag{L-15118.7}
\]

Indeed, the nonzero eigenvalues are those of `U^T U`.  Their product is at least
`|det C|^2` by Cauchy--Binet, while each of the largest `n-2` eigenvalues is at
most `Tr(U^T U)=S`.

The Cauchy determinant is explicit:

\[
 \boxed{
 |\det C|
 =\frac{
   \prod_{a<b}|\lambda_{i_a}-\lambda_{i_b}|
   \prod_{k<l}|r_k-r_l|
 }{
   \prod_{a,k}|\lambda_{i_a}-r_k|
 }.}
 \tag{L-15118.8}
\]

Thus rational root isolators give a directed positive moat without a floating
eigensolver.  In production a direct interval `LDL^T` lower bound on
`p^perp` will usually be sharper; (L-15118.7) is a universal fallback and a
useful conditioning diagnostic.

## 6. Gap audit

1. The root-free construction does not prove positivity; it constructs the
   canonical matrix whose inertia must be certified.
2. Formula (L-15118.6) must use the compact transform associated with the exact
   finite target, not unwindowed `Xi` samples.
3. A tiny coefficient interval may still produce a wide `g_i` interval when
   `p_i` is tiny.
4. The Cauchy moat can be extremely conservative when roots cluster.
5. Canonical positivity decides arbitrary special completion, not the fixed
   arithmetic scalar line.