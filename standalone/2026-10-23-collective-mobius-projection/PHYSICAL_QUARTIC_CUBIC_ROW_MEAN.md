# The actual quartic cubic-numerator mean

23 October 2026. Source-dependent analytic candidate, with the full physical orientation retained. Independent review is requested. This is not a centered inverse estimate or a smaller fixed zero-free boundary.

Work over the Gaussian field with fixed bad primes and primary generators. Write alpha(c)=c/|c| and gamma4(c)=g4(1,c)/sqrt(Nc). Fix an integer ell different from zero. The squarefree physical row k occurs as the additive numerator k^3, rather than k, in Dunn--David--Hamieh--Lin, [arXiv:2306.11875v4](https://arxiv.org/html/2306.11875v4), hereafter DDHL. All fixed ray sectors are retained. The angular sign is part of the family.

## 1. Exact completion and finite family

For beta in the two primary classes modulo 4 define

\[
 D_{\beta,k,\ell}(s)=\sum_{\substack{c\ {m sf},\ (c,k)=1\\c\equiv\beta\ (4)}}
 \gamma_4(c)\alpha(c)^{-\ell}\chi_c(k)(Nc)^{-s}.
 \tag{Q1}
\]

The local Gauss formula DDHL (3.7), with v_p(k^3)=3, permits only modulus exponents 0 and 4 at p dividing k, and g4(k^3,p^4)=-Np^3. The fourth-power CRT cross factors are one. Consequently, with the source's raw Dirichlet variable equal to s+1/2,

\[
 \psi^{(4)}_\beta(s+1/2,k^3,\ell)
 =\prod_{p\mid k}(1-\alpha(p)^{-4\ell}(Np)^{1-4s})D_{\beta,k,\ell}(s).
 \tag{Q2}
\]

Thus the source completion (4.24) is exactly

\[
 Q_{\beta,k,\ell}(s)
 =L^{(k)}(4s-1,\alpha^{-4\ell})D_{\beta,k,\ell}(s).
 \tag{Q3}
\]

The superscript deletes primes dividing k and the fixed bad modulus. The full fourth-power variable is retained: its coefficient at d^4 is Nd times alpha(d)^(-4ell), with the natural mask (d,k)=1. It need not be coprime to the squarefree c.

Use instead the complete 24-dimensional source vector Q_i(s)=Z_{i1}(s+1/2,k^3,ell), and take the direct sum for ell and -ell. Equations (4.15)--(4.22) express every component as a fixed finite combination of the two beta series at numerators (-1)^a lambda^(2b) k^3. Because k is good, the source bound b<=ord_lambda(k^3)+5 is fixed. The coefficients are fixed bad-prime monomials and bounded periodic functions of k; split those row sectors before using a sieve. At every good prime dividing k the numerator valuation is still three, so Q2--Q3 and the same fourth-power completion hold, with an additional fixed column character. No growing family of local profiles is introduced. The two beta channels themselves are nonzero scalar multiples of source components by (4.15), so the vector bound implies their bound.

Theorem 1.1 of de Faveri, [arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), gives, for arbitrary coefficients on fourth-power-free columns and fourth-power-free rows, the norm

\[
 \Theta_4(K,Y)\ll(KY)^\epsilon
 [K+Y+K^{3/4}Y^{1/2}+K^{1/2}Y^{3/4}].             \tag{Q4}
\]

Squarefree row and column restriction is positive restriction. Finite reciprocity sectors put Q1 in precisely this family. Fixed column characters, the angular coefficient, and the natural shared-prime zeros are permitted. This is a primary input, not a claim about arbitrary metaplectic coefficients.

## 2. Mean on the right of the critical line

Put sigma=1/2+delta, with 0<delta<1/4, and L=1+|t|. For the complete finite vector just defined, the claimed estimate is

\[
 \sum_{Nk\asymp K}^{\rm sf}\|\mathbf Q_k(\sigma+it)\|^2
 \ll_{\ell,\delta,\epsilon}(KL)^\epsilon
 \{K+K^{3/2-3\delta}L^{3-6\delta}
       +K^{13/8-3\delta}L^{9/4-6\delta}\}.          \tag{Q5}
\]

In particular, at fixed height this is at most

\[
 K^\epsilon\{K+K^{13/8-3\delta}\},                 \tag{Q6}
\]

and is K^(1+epsilon) when delta>=5/24. Constants depend on the fixed nonzero angular integer; no moving-angular assertion is made.

Here is the absorption proof. A smooth Dirichlet truncation at Y, formed by the Gaussian Mellin factor exp(z^2)/z, has squared mean

\[
 O(K,Y)\ll(KY)^\epsilon
 [K+Y^{1-2\delta}+K^{3/4}Y^{1/2-2\delta}
                       +K^{1/2}Y^{3/4-2\delta}].  \tag{Q7}
\]

Indeed apply Q4 to each dyadic squarefree c block with its coefficient (Nc)^(-sigma), and sum by Minkowski. The first K term sums geometrically because delta>0. In the fourth-power completion, freezing d leaves the row mask (d,k)=1 and a rescaled c cutoff. Its absolute mass is bounded by the convergent ideal sum sum_d (Nd)^(-1-4delta). The slowly varying smooth profiles have uniform Mellin bounds. Bad-prime components are the fixed finite combinations already described. This also proves Q7 for the rapidly decreasing tail of the Gaussian truncation, by dyadic summation.

Proposition 4.3 of DDHL says that the gamma-completed source vector is entire for ell nonzero. Division by its gamma factors preserves entireness. Moving the Gaussian contour to Re z=-2delta therefore crosses just z=0. In the remaining integral the source equation (4.28) reflects s+z back to real part sigma. Its conductor factor is

\[
 N(k^3)^\delta=(Nk)^{3\delta},                    \tag{Q8}
\]

not K^(2delta). The angular root alpha(k)^(-3ell) has modulus one and the angular sign changes. On the reflected line the rational matrices A_ji(2^(-s_raw),ell) are uniformly bounded: Re s_raw=1-delta is away from their possible singular lines 1 and 5/4. The three gamma quotients in (4.26) have size at most a constant times (1+|t+v|)^(6delta); fixed angular mode causes no further variable factor. Thus, after Cauchy in v, the residual squared mean is bounded by

\[
 C_{\ell,\delta}K^{6\delta}Y^{-4\delta}
 \int_{\mathbb R} e^{-v^2}(1+|t+v|)^{12\delta}
 \sum_{Nk\asymp K}^{\rm sf}\|\mathbf Q_k(\sigma-i(t+v))\|^2\,dv,
 \tag{Q9}
\]

with harmless changes to the Gaussian and polynomial powers. Retain the phases in the exact identity; Q9 is only its norm bound.

Choose Y=C0 K^(3/2)L^3. Normalize by (KL)^epsilon0 times the braces in Q5. Gaussian convolution preserves each displayed height monomial up to a fixed constant, since 1+|t+v|<=L(1+|v|). The resulting residual coefficient is a constant times C0^(-4delta). Choose C0 large to make it less than 1/2. Substitution in Q7 yields the braces in Q5: its middle mixed term is bounded by the Y^(1-2delta) term because L>=1.

This supremum is finite before absorption. For each fixed dyad K, the source convexity argument (4.31)--(4.34), with its removable excluded neighborhoods filled by the maximum principle for the nonzero-angular entire functions, gives polynomial height growth at most L^(3-6delta+epsilon0/2) in the squared mean, with an arbitrary K-dependent constant. The first nonconstant height term in Q5 has exponent 3-6delta. Thus the normalized supremum over all t is finite, and absorption bounds it uniformly in K. There is no supremum over unbounded K in this finiteness argument. Shrinking the internal epsilon losses establishes Q5.

## 3. What the actual annular consumer gives

For fixed smooth compactly supported W let

\[
 S_k(D)=\sum_{\substack{c\ {m sf}\\(c,k)=1}}
 {\gamma_4(c)\alpha(c)^{-\ell}\chi_c(k)\over\sqrt{Nc}}
 W(Nc/D),                                         \tag{Q10}
\]

with the fixed beta sectors retained if needed. Mellin inversion on sigma=1/2+delta and Q3 gives

\[
 \sum_{Nk\asymp K}^{\rm sf}|S_k(D)|^2
 \ll (KD)^\epsilon D^{2\delta}
       [K+K^{13/8-3\delta}].                       \tag{Q11}
\]

Here the reciprocal of the ordinary Hecke factor in Q3 is bounded absolutely at Re(4s-1)=1+4delta, uniformly in k: adding the omitted Euler factors costs a bounded absolute Euler product. The integrated height powers in Q5 are absorbed by the rapid Mellin decay of W. This step uses no unproved zero-free half-plane.

At the physical relation K=D^2/H and H=D^a with 0<=a<=1, the first-Poisson prefactor H/D makes Q11 of size

\[
 D^{a-1+2\delta+(2-a)\max(1,13/8-3\delta)+\epsilon}.
 \tag{Q12}
\]

For 0<delta<=5/24 its exponent decreases with delta, since the slope is 3a-4<0. For delta>=5/24 it increases with slope 2. The best choice in this family is delta=5/24 and gives D^(17/12+epsilon). This is much too large for the desired inverse mean of scale H in the binding range. Also, Q11 covers only squarefree physical rows: the full inverse problem has further row strata. The proposed mean is therefore an orientation-correct component, not a repair of the missing centered moment. A row-scale completed mean on a shifted line does not become a row-scale raw annular mean without the D^(2delta) cost.

