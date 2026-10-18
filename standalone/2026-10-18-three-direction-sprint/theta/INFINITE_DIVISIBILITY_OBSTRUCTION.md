# Actual theta admits no nontrivial infinitely divisible padding

**Status: PROPOSED complete analytic obstruction, using the classical
Levy--Khintchine representation as an explicit import.** This extends
the Gaussian-factor warning to every nondegenerate infinitely divisible
convolution factor and to countable positive mixtures of such laws.
It blocks independent Poisson/rare-jump smoothing as a way to remove the
harmonic lattice. It establishes no improved zero-free region or RH.

## 1. A general subquadratic-growth theorem

Let X have finite two-sided exponential moments at every finite height:
`E exp(tX)<infinity` for all real t. Assume

\[
 \log Ee^{tX}=o(t^2)\qquad(t\to+\infty\text{ and }t\to-\infty). \tag{1}
\]

If `X=U+V` with U,V independent and U infinitely divisible, then U is
deterministic. The deterministic drift is allowed; the conclusion is
that its Gaussian variance and jump measure are both zero.

First, independence and positivity of the exponential imply that U,V
also have finite exponential moments at every finite real t. In
particular both have finite means, and Jensen gives

\[
 \log Ee^{tU}\le\log Ee^{tX}-tEV=o(t^2)+O(|t|). \tag{2}
\]

The classical Levy--Khintchine representation, continued to real MGFs
under these exponential-moment assumptions, is

\[
 K_U(t)=d t+\tfrac12\sigma^2t^2
 +\int_{\mathbb R\setminus\{0\}}
     [e^{tx}-1-tx1_{|x|\le1}]\,\nu(dx), \tag{3}
\]

where d is a finite real drift, sigma^2>=0, and
`integral min(1,x^2)nu(dx)<infinity`. This standard structural theorem
is the one imported probability result. A primary historical source is
Khintchine, *Zur Theorie der unbeschrankt teilbaren Verteilungsgesetze*,
Rec. Math.2(44) (1937),79--119,
[original journal record and full text](https://www.mathnet.ru/eng/sm5562).
The application below does not assume a zero drift or a symmetric U.

For |x|<=1 the integral's integrand is nonnegative, by exp(y)>=1+y.
For |x|>1 it is at least-1, and nu has finite mass there. Consequently

\[
 K_U(t)\ge\tfrac12\sigma^2t^2-|d||t|-\nu(|x|>1). \tag{4}
\]

If sigma^2>0, (4) contradicts (2) in either direction.

If nu is nonzero, it has positive finite mass q on an interval bounded
away from zero, either `[epsilon,L]` or `[-L,-epsilon]`, with
0<epsilon<L<infinity. Use positive t for the first case and negative t
for the second. That interval contributes at least

\[
 q e^{\epsilon|t|}-C(1+|t|).
\]

All remaining small jumps contribute nonnegatively, and all remaining
large jumps cost at most their finite mass. Thus

\[
 K_U(t)\ge q e^{\epsilon|t|}-C'(1+|t|) \tag{5}
\]

along one sign, again contradicting (2). Hence sigma^2=0 and nu=0,
so (3) reduces to the deterministic drift dt. This proves the theorem.

## 2. The actual theta law meets the full hypothesis

For the original theta variable T,

\[
 Ee^{tT}=\frac{\xi(1/2+t)}{\xi(1/2)}.
\]

All finite two-sided exponential moments exist, either from the complete
theta double-exponential tail or its entire Fourier identity. Stirling
and the absolutely convergent positive-real zeta series give

\[
 \log Ee^{tT}=\tfrac12|t|\log|t|+O(|t|), \tag{6}
\]

using xi symmetry for negative t. The sharper coefficients are derived
in HARMONIC_STAR.md; an independent complete theta-tail bound is given
in HERMITE_ARCHITECTURE.md. In particular (1) holds on both sides.

Thus actual theta has no nondegenerate Gaussian, Poisson, compound
Poisson or other infinitely divisible convolution factor. A signed
drift cannot repair the growth contradiction; it changes only O(|t|).

## 3. Countable mixtures and finite hidden-state schemes

Suppose the actual law were a countable positive mixture

\[
 \mathcal L(T)=\sum_{j\ge1}p_j\mu_j,\qquad p_j>0,\quad\sum_jp_j=1,
\]

where each mu_j is infinitely divisible. Its MGF obeys
`M_j(t)<=M_theta(t)/p_j` for every finite t, so each component has all
two-sided exponential moments and satisfies (1). Applying the proof
above directly to each component makes each mu_j deterministic.
The mixture would be countably atomic, contrary to the actual positive
continuous theta density. Therefore no such countable mixture exists.

This does not exclude an arbitrary uncountable mixture of point masses:
that would be just another description of any continuous distribution.
It excludes a finite or countable hidden-state construction whose
conditional limiting laws are infinitely divisible.

## 4. A direct spin-array corollary without a triangular-array import

Consider finite single-hub stars, with or without an observed hub, whose
largest leaf weight tends to zero and whose observable second moments
stay bounded. Conditional on the fair hub, the leaf spins are independent.
Let m_N be the full conditional mean (including the observed hub) and
v_N the conditional variance. Symmetry gives
`E Y_N^2=m_N^2+v_N`, so both are bounded. Pass to a subsequence with
m_N->m and v_N->v>=0.

For a centered leaf Z=w(sigma-E sigma), `|Z|<=2w`, and
`E|Z|^3<=2w Var(Z)`. Its characteristic logarithm at each fixed real z
is therefore

\[
 \log Ee^{izZ}=-\tfrac12z^2\operatorname{Var}Z
                 +O_z(w\operatorname{Var}Z), \tag{7}
\]

uniformly when max w is small. Taylor's full remainder and log(1+u)
give (7) directly. Summing over leaves bounds the total remainder by
`C_z(max w_N)v_N`, which tends to zero. The conditional limits are
therefore normal laws of means +/-m and common variance v, and the
unconditional limit has characteristic function

\[
 e^{-v z^2/2}\cos(mz). \tag{8}
\]

If v>0, (8) has a nonzero Gaussian convolution factor, excluded above.
If v=0, it has at most two atoms, also not the actual theta law. Hence
no such vanishing-leaf-weight star scheme can be a cofinal actual-theta
construction. This applies to biased leaves as well as a fair-spin bulk.

The general infinitely divisible theorem similarly prevents replacing a
persistent lattice by independent Poissonized jumps while retaining a
finite hidden-state mixture. A successful construction must retain a
different correlated, noninfinitesimal structure; no such construction
is proved by these obstructions.
