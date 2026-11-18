# Independent proof of the tapered prime array for the generator target

17 November 2026. Fix an integer \(k\ge2\), put \(h(s)=k^{1-s}-1\) and \(F_k(s)=\zeta(s)h(s)\), and let \(L=\log N\). Write \(V_N=\operatorname{span}\{\lfloor x/n\rfloor-\lfloor x\rfloor/n:2\le n\le N\}\) in the unit-step space with norm \(L^2([1,\infty),dx/x^2)\). I independently obtain the proposed limit under RH. The constant agrees with the best approximation in \(V_N\) and also with the larger ordinary-polynomial infimum in the full boundary norm. Both ordinate signs occur. The proof uses classical zeta convexity, Hadamard factorization and the unit-height zero count, and the previously checked compact test for the lower bound. No simplicity or reciprocal-derivative moment assumption enters. [Compact-test proof](../rstation48_fixed_prefix_lower_skeptic62.md) · [Generator membership proof](jump_generator63_single_member_skeptic.md)

## Target and ordinary coefficients

For \(n=\lfloor x\rfloor\) and \(q=\lfloor n/k\rfloor\), the target \(R_k(x)=\log((q!)^k k^{kq}/n!)\) has jump \((k\mathbf1_{k\mid n}-1)\log n\) at \(n\). It is the strong generator vector divided by \(i\), for the bounded step \(k\lfloor x/k\rfloor-\lfloor x\rfloor\). Summation by parts against this bounded step gives \(|R_k(x)|\ll_k\log(2+x)\). Absolute integration first on \(\Re s>1\) therefore yields \(MR_k(s)=-F'_k(s)/s\), with continuation to \(\Re s>0\). Mellin–Plancherel on the critical line uses \(dt/(2\pi)\) for this transform.

The meromorphic series to taper is

\[
 Z(s)=-\frac{F'_k(s)}{\zeta(s)}
 =h(s)\left(-\frac{\zeta'}{\zeta}(s)\right)-h'(s)
 =\sum_{d\ge1}w_k(d)d^{-s}\quad(\Re s>1).
\]

The coefficients are exactly \(k\mathbf1_{k\mid d}\Lambda(d/k)-\Lambda(d)+k\log k\,\mathbf1_{d=k}\), including the last term from \(-h'\). Multiplication by \(\zeta\) has Dirichlet coefficients \(\sum_{d\mid n}w_k(d)=(k\mathbf1_{k\mid n}-1)\log n\), an independent check of the normalization. At 1 the zero of \(h\) cancels the pole of \(\zeta\), so \(F_k\) is holomorphic and \(Z(1)=0\). At a distinct nontrivial zero \(\rho\) of multiplicity \(m_\rho\), \(Z\) has a simple pole with residue \(r_\rho=-m_\rho h(\rho)\) on RH. In particular one never introduces inverse zeta derivatives.

A separate finite check represented each logarithm by its prime-exponent coefficients and recovered the divisor-convolution identity in all 6,500 cases \(2\le k\le14\), \(1\le n\le500\), including composite \(k\). The series calculation proves the identity for every \(k,n\).

Set \(A_N(s)=\sum_{d\le N}w_k(d)(1-\log d/L)d^{-s}\) and \(B_N=A_N-A_N(1)\). The latter is exactly an anchored ordinary polynomial of length \(N\). Its physical image \(\zeta B_N/s\) is in \(V_N\), since the multiplier for its \(d\)-th term becomes \(d^{-s}-1/d\). There is no support loss at anchoring or at the taper endpoint.

## Perron identity with a full-line error estimate

Let \(D=-\zeta'/\zeta\) and \(T_t=2+|t|\). The following local controls justify the entire contour shift. For \(w=2+it\), the difference of completed log derivatives at \(z\) and \(w\) is the absolutely convergent sum \(\sum_\rho m_\rho((z-\rho)^{-1}-(w-\rho)^{-1})\). Terms with \(|\Im\rho-t|>1\) are \(O(\log T_t)\) in aggregate, by the unit-window zero count and the inverse-square difference, uniformly on a fixed small disk about \(1/2+it\). The nearer terms at \(w\) and the gamma and elementary terms are \(O(\log T_t)\), so

\[
 D(z)=-\sum_{|\gamma-t|\le1}\frac{m_\rho}{z-\rho}+O_{\mathrm{hol}}(\log T_t)
\]

on that disk, with a holomorphic bounded regular part. Cauchy's estimate and the bounded divided differences of \(h\) give at \(s=1/2+it\)

\[
 Z'(s)=-\sum_{|\gamma-t|\le1}\frac{r_\rho}{(s-\rho)^2}+O_k(\log T_t).
\]

This differentiates an analytic identity with a fixed local list, with no moving-cutoff derivative. The same Hadamard difference gives \(Z(-1+iy)\ll_k\log(2+|y|)\), as that line stays a fixed distance from every zero in the sum. On horizontal lines of arbitrarily large positive and negative height \(T\), keep distance \(c/\log(2+|T|)\) from every nearby zero ordinate. The height count gives such choices by deleting intervals of total length less than 1 in a unit interval. The difference formula then gives \(Z(z)\ll_k\log^2(2+|T|)\) throughout the horizontal bounded strip \(-1\le\Re z\le2\).

On the line \(\Re z=2\), absolutely convergent double Perron gives

\[
 A_N(s)=\frac1{2\pi iL}\int_{(2)}Z(z)\frac{N^{z-s}}{(z-s)^2}\,dz
\]

for the two needed real parts \(\Re s=1/2,1\). The inverse double kernel gives exactly \((\log N-\log d)_+\) before division by \(L\), including zero at \(d=N\). Shift to \(\Re z=-1\) along the good heights. For fixed \(N,s\) their integrals tend to zero by the quadratic denominator. The only poles besides the kernel point are the nontrivial zero poles of \(Z\); 1 is regular and the first trivial zero is left of the contour. Taking the residues, for \(s\) away from zeros one obtains

\[
 Z(s)-A_N(s)=-\frac{Z'(s)}L
   -\frac1L\sum_\rho\frac{r_\rho N^{\rho-s}}{(s-\rho)^2}
   -I_{-1,N}(s).
\]

The series is absolutely convergent at such \(s\). The left-line integral obeys \(|I_{-1,N}(\sigma+it)|\ll_k N^{-1-\sigma}\log T_t/L\) by integration against \(((1+\sigma)^2+(y-t)^2)^{-1}\). Thus the contour identity needs only pointwise horizontal convergence. Its residual estimates below apply uniformly on the whole boundary.

Under RH, \(|N^{\rho-s}|=1\) at the critical line. Define \(E_L(v)=(1-e^{-iLv})/(iLv)=\int_0^1 e^{-iLuv}\,du\), continuously at zero. Multiplying the identity by \(\zeta(s)/s\) and combining the local term of \(Z'\) with its residue gives the main residual

\[
 U_N(t)=\sum_{|\gamma-t|\le1}
       r_\rho\frac{\zeta(1/2+it)}{(1/2+it)(1/2+it-\rho)}\,E_L(t-\gamma).
\]

The omitted far sum before multiplication is bounded by \(L^{-1}\sum_{|\gamma-t|>1}|r_\rho|/(t-\gamma)^2\ll_k L^{-1}\log T_t\). This follows by unit-height bins, since \(|r_\rho|\ll_k m_\rho\) and the counts include multiplicity. The holomorphic error of \(Z'\) and the left integral obey the same or smaller bound. Classical convexity on a fixed strip about the line and Cauchy's estimate supply \(|\zeta(1/2+it)|+|\zeta'(1/2+it)|\ll T_t^\theta\) for some \(\theta<1/2\), for example \(3/8\). Consequently the difference from \(U_N\) is \(O_k(1/L)\) in full \(L^2(dt/(2\pi))\). At \(s=1\) the same Perron identity, \(Z(1)=0\), and absolute summation give \(A_N(1)=Z'(1)/L+O_k(N^{-1/2}/L)\). The anchor adds \(O_k(1/L)\) in boundary norm because \(\zeta(s)/s\) is square integrable there.

## Uniform summation and multiple zeros

The quotient \(\zeta(s)/(s-\rho)\) for \(|t-\gamma|\le1\) is bounded by the supremum of \(|\zeta'|\) on the segment between \(s\) and \(\rho\), so it is \(O(T_t^\theta)\) independently of gaps or multiplicity. At any \(t\) the sum of multiplicities in this window is \(O(\log T_t)\). Weighted Cauchy–Schwarz and \(\int |E_L(v)|^2,dv/(2\pi)=1/L\) therefore show

\[
 L\|U_{N,|\gamma|>Y}\|_2^2
 \ll_k \sum_{|\gamma|>Y}m_\rho\log(2+|\gamma|)(2+|\gamma|)^{-2+2\theta}.
\]

This upper bound tends to zero uniformly in \(N\) by the unit-height count. For a fixed finite set of zeros, take pairwise disjoint fixed neighborhoods of their ordinates. Outside each respective neighborhood its individual term has norm \(O(1/L)\) by \(|E_L(v)|\le2/(L|v|)\), and the restricted terms are orthogonal by their disjoint supports. The kernels \(L|E_L(v)|^2/(2\pi)\) are a mass-one approximate identity. Each diagonal contribution thus tends to \(|r_\rho\zeta'(\rho)/\rho|^2\). At a multiple zero the quotient \(\zeta(s)/(s-\rho)\) vanishes at \(s=\rho\), giving zero; at a simple zero \(r_\rho=-h(\rho)\). Fix the height first, take \(N\) to infinity, then exhaust the zeros using the uniform bound above. This proves

\[
 \lim_{N\to\infty}L\left\|MR_k-\frac{\zeta B_N}s\right\|_2^2
 =\sum_{\substack{\rho\text{ distinct},\ \Re\rho=1/2\\m_\rho=1}}
          \frac{|\zeta'(\rho)(k^{1-\rho}-1)|^2}{|\rho|^2}.
\]

The separate arguments for the contour, the uniform tail and the fixed-set limit matter. Taking the local limit at each zero alone would give no upper bound on the sum, and a sharp cutoff has a different Perron kernel.

## Optimality in both admissible spaces

The archived RST047 compact zeroth tests apply to every bounded-norm sequence \(u_N\in V_N\), regardless of the target. More explicitly, use order \(a=\lceil L\rceil\), scale \(N\), physical cutoff \(R=\lceil4NL\rceil\), and the Mellin weight \(\chi_a(x/N)+B_a(x/N)/\rho\), where \(\chi_a(z)=e^{-z}\sum_{j<a}z^j/j!\) and \(B_a(z)=e^{-z}z^a/\Gamma(a)\). Denote the functional by \(T_{\rho,N}\). Its proof bounds ordinary coefficients by \(O(N^{3/2})\) times the first-\(N\)-cell norm, removes the periodic mean exactly, and controls both Fourier and physical-tail errors by negative powers of \(N\). For each selected critical zero, \(T_{\rho,N}(u_N)=o(1)\) by exact zeta annihilation in the full Mellin transform. For finitely many distinct such zeros, the representer Gram divided by \(L\) tends to the identity. These are the target-independent portions of the checked proof. [RST047 compact-zero-jet estimates](../rstation48_fixed_prefix_lower_skeptic62.md)

For \(R_k\), the main \(\chi_a\) term tends to \(MR_k(\rho)\) by dominated convergence since \(|R_k(x)|\ll_k\log(2+x)\). On \(x\le N\) the bump is at most \(1/\Gamma(a)\); on \(x>N\) its global maximum is \(O(\sqrt a)\) by Stirling, giving a total bump pairing \(O_k(L^{3/2}N^{-1/2})+o(1)\). The same argument works for any bounded target. Thus the residual tests tend to \(MR_k(\rho)\), and projection onto a fixed finite set of test representers gives the lower bound \(\sum|MR_k(\rho)|^2\) after multiplying squared norm by \(L\). Bounded approximants suffice for a lower limit because the proposed array supplies a bounded scaled upper limit. Finally exhaust the fixed simple zero set. The lower bound agrees with the array constant.

The result also holds if one optimizes over all ordinary length-\(N\) polynomials \(A\) without anchoring in the full boundary norm. In physical coordinates on \((0,\infty)\) the approximants are combinations of \(v(x/n)\) with \(v(x)=\lfloor x\rfloor-x\), whose Mellin transform is \(\zeta(s)/s\). Extend the target by zero below 1. A bounded scaled squared residual then forces \(|A(1)|=O(L^{-1/2})\) by its exact below-one tail. Splitting the approximant into the anchored one plus \(A(1)v\) leaves the anchored sequence bounded in norm. The test pairings of \(v\) on \([1,\infty)\) are uniformly bounded by the preceding bounded-target argument. Thus the extra term is \(o(1)\) in every fixed residual test. The same projected lower bound applies, without requiring the norm change from removing \(A(1)v\) to be \(o(L^{-1/2})\). The anchored array supplies the matching upper bound in this larger space too.

The prescribed approximation therefore tends to zero under RH. Conversely, convergence of this anchored array in the full norm places \(R_k\) in the infinite anchored step closure. The proved single-generator membership criterion then gives RH, including when a hypothetical off-line zero is multiple. This converse concerns norm convergence of the actual tapered array and gives no claim about the untapered prime cutoff or publication priority. [Single-generator criterion](jump_generator63_single_member_skeptic.md)
