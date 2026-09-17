# 05. Native Möbius energies, localization, and exact restoration

**Status:** proposed component proofs with classical transforms explicitly separated. No subpolynomial source upper bound is proved.

## 1. One source, two exponential representations

For a finite real source a_n, 1<=n<=N, define
\[
F_{a,N}(t)=\sum_{n\le N}a_n n^{-2}e^{-t/n}.
\]
Then
\[
\mathcal Q_0[a]=\int_0^\infty t^2|F_{a,N}(t)|^2dt
=\sum_{m,n\le N}\frac{2mn}{(m+n)^3}a_ma_n.
\]
The same Gram matrix gives
\[
\mathcal Q_0[a]=\int_0^\infty t^2\left|\sum_{n\le N}na_ne^{-nt}\right|^2dt.
\]
For complex sources insert conjugates in the second coefficient. The two source functions are not claimed equal; their complete squared norms agree. In this packet a_n=mu(n), unless a comparison source is explicitly labeled.

The form is nonnegative. Its diagonal is
\[
D(N)=\frac14\sum_{n\le N}\mu(n)^2/n
=\frac{1}{4\zeta(2)}\log N+O(1).
\]
Its off-diagonal part is
\[
B_0(N)=4\sum_{m<n\le N}\frac{mn\mu(m)\mu(n)}{(m+n)^3}.
\]
An O(log N) diagonal does not bound the signed cross terms.

## 2. Recovering a finite Mertens sum

Since \(\int_0^\infty tn^{-2}e^{-t/n}dt=1\),
\[
M(N)=\int_0^\infty tF_N(t)dt.
\]
Split at T. The initial part is at most sqrt(T Q_0(N)); the tail is at most
\[
\sum_{n\le N}(1+T/n)e^{-T/n}
\le N(1+T/N)e^{-T/N}.
\]
At T=4N log(2N), the last quantity is below 1. Hence
\[
|M(N)|\le2\sqrt{N\log(2N)\mathcal Q_0(N)}+1,
\]
\[
\mathcal Q_0(N)\ge\frac{(|M(N)|-1)_+^2}{4N\log(2N)}.
\]
The smoothing has not erased a large Mertens sum.

The same inequality holds for any |a_n|<=1. For a_n=d_(-alpha)(n), 0<alpha<1, Chapter 04's main term yields
\[
\mathcal Q_0[d_{-\alpha}](N)\gg_\alpha
N/(\log N)^{2\alpha+3}.
\]
This makes the failure of separate fractional-factor norm bounds quantitative.

## 3. Shifting power-free density indices changes detector resolution

For j>=0,
\[
F_{j,N}(t)=\sum_{n\le N}\mu(n)n^{-j-2}e^{-t/n}
=(-1)^jF_N^{(j)}(t).
\]
On the infinite entire-series side the same operation changes coefficients from 1/zeta(k+2) to 1/zeta(k+j+2).

Normalize
\[
\mathcal Q_j(N)=\frac{2^{2j+1}}{\Gamma(2j+3)}
\int_0^\infty t^{2j+2}|F_{j,N}(t)|^2dt.
\]
Finite expansion gives
\[
\mathcal Q_j(N)=2^{2j+1}\sum_{m,n\le N}
\frac{(mn)^{j+1}\mu(m)\mu(n)}{(m+n)^{2j+3}}
\]
\[
=\frac14\sum_{m,n\le N}\frac{\mu(m)\mu(n)}{\sqrt{mn}}
\operatorname{sech}^{2j+3}\left(\frac12\log\frac mn\right).
\]
Every j has the same diagonal D(N). For m=n+h with h=o(n), the kernel is locally like exp(-j h^2/(4n^2)), so the effective shift size is h~n/sqrt(j). This is a heuristic localization description; the rigorous comparisons use spectral multipliers, not entrywise approximation.

## 4. Mellin Plancherel and restoration

Let \(P_N(s)=\sum_{n\le N}\mu(n)n^{-s}\). Then
\[
\mathcal Q_j(N)=\frac1{2\pi}\int_{\mathbb R}W_j(\tau)
|P_N(1/2+i\tau)|^2d\tau,
\]
\[
W_j(\tau)=\frac{2^{2j+1}}{\Gamma(2j+3)}
|\Gamma(j+3/2+i\tau)|^2.
\]
The sign of tau is immaterial for real coefficients. Gamma recurrence gives
\[
\mathcal Q_0(N)\le A_j\mathcal Q_j(N),\quad
A_j=\frac{\sqrt\pi}{2}\frac{\Gamma(j+2)}{\Gamma(j+3/2)}
\sim\frac{\sqrt{\pi j}}2.
\]
This is a pointwise ordering of nonnegative Fourier multipliers, valid for any finite source. It is not deduced from an entrywise ordering of signed Gram matrices.

For \(g_N(u)=e^{3u/2}F_N(e^u)\), the stronger identity is
\[
A_j\mathcal Q_j(N)=\sum_{\ell=0}^j
 e_\ell\left((3/2)^{-2},(5/2)^{-2},\ldots,(j+1/2)^{-2}\right)
\|g_N^{(\ell)}\|_2^2.
\]
In particular (4/3)Q_1=Q_0+(4/9)||g_N'||_2^2. Localization after restoration adds positive derivative costs; it does not make the source automatically cheaper.

At j_N=ceil((log N)^4), restoration costs O(log^2N), hence any subpolynomial Q_(j_N) upper bound implies one for Q_0. Chapter 06 gives the every-prefix witness needed to use an arbitrary unbounded sparse sequence of cutoffs.

## 5. A direct RH equivalence for all cutoffs

Under RH, the classical bound M(x)=O_epsilon(x^(1/2+epsilon)) and partial summation give
\[
|P_N(1/2+i\tau)|\ll_\epsilon(1+|\tau|)N^\epsilon.
\]
The Gamma moments are finite, so Q_0(N)=O_epsilon(N^epsilon), after relabeling epsilon.

Conversely, let F(t)=sum mu(n)n^(-2)e^(-t/n). Uniformly in t>=0,
\[
|F(t)-F_N(t)|\le1/N.
\]
If Q_0(N)=O_epsilon(N^epsilon), choose N=ceil(T^2). Then
\[
\int_0^Tt^2|F(t)|^2dt\le2Q_0(N)+2T^3/(3N^2)=O_\epsilon(T^\epsilon).
\]
Cauchy–Schwarz on dyadic intervals makes the Mellin integral of F absolutely convergent for 0<Re s<3/2. Chapter 04 then excludes off-critical zeros. Thus the subpower estimate is exactly RH-strength.

## 6. Which correlations have already been separated?

Write
\[
B_j(N)=\frac12\sum_{h=1}^{N-1}\sum_{n\le N-h}
\frac{\mu(n)\mu(n+h)}{\sqrt{n(n+h)}}
\operatorname{sech}^{2j+3}\left(\frac12\log(1+h/n)\right).
\]

### Far ratios

For 0<delta<=1, pairs with |log(m/n)|>=delta have total absolute contribution at most
\[
CN\exp(-j\delta^2/6).
\]
Extract sech^(2j)(delta/2) from the kernel and use log cosh(delta/2)>=delta^2/12; the remaining positive j=0 form is O(N). With j=log^4N and delta=sqrt(24 log N/j), this is O(N^(-3)). This leaves growing shifts h/n of size at most a constant/log^(3/2)N.

### Fixed multiplicative ratios

Set m=ad,n=bd with (a,b)=1. Then
\[
\mu(ad)\mu(bd)=\mu(a)\mu(b)\mu(d)^2 1_{(d,ab)=1}.
\]
The contribution of a fixed ordered ratio (a,b) is exactly
\[
\frac{\mu(a)\mu(b)}{4\sqrt{ab}}
\operatorname{sech}^{2j+3}\left(\frac12\log(a/b)\right)
H_{ab}(N/\max(a,b)),
\]
where
\[
H_q(X)=\sum_{d\le X,(d,q)=1}\mu(d)^2/d
=c_q\log X+C_q+O_q(X^{-1/2}),
\quad c_q=\zeta(2)^{-1}\prod_{p\mid q}\frac p{p+1}.
\]
Every fixed ratio is explicit. Every fixed nontrivial ratio is exponentially suppressed at growing depth, leaving reduced ratios tending to 1 with growing numerator and denominator.

### Fixed additive shifts

The logarithmically averaged two-point theorem [T15] gives
\(\sum_{n\le N}\mu(n)\mu(n+h)/n=o(\log N)\) for each fixed nonzero h. Multiplying by the depth weight changes it by O_h(log(j+2)): split at n~h sqrt(j+1), then bound the remaining weight error by h/n+(j+1)h^2/n^2. At j_N this is O_h(loglog N), so each fixed shift contributes o(log N).

This does not provide uniformity over the growing shifts needed for B_j.

## 7. The absolute localization budget cancels against restoration

A row-integral bound gives
\[
|B_j(N)|\le NI_j,\quad
I_j=\int_0^\infty e^u\operatorname{sech}^{2j+3}u\,du
=\frac{\sqrt\pi\Gamma(j+1)}{2\Gamma(j+3/2)}+\frac1{2j+2}
\ll(j+1)^{-1/2}.
\]
At j_N this saves log^2N, precisely the restoration loss. For the all-positive source 1, Q_0[1](N)~N/2. For fixed j, Q_j[1](N)~a_jN with
\[
a_j=\frac{\sqrt\pi\Gamma(j+1)}{2\Gamma(j+3/2)}-\frac1{2j+2}
\sim\frac{\sqrt\pi}{2\sqrt j}.
\]
This is a counterexample to a coefficient-blind absolute completion, not to the native Möbius target.

The actual short prefix also refutes a universal nonpositive covariance rule:
\[
Q_8(3)-D(3)=-2^{27}/3^{19}-3^9/2^{20}+2^{27}3^9/5^{19}>0.
\]
A positive finite value is compatible with a global subpower bound; it only blocks that stronger sign shortcut.

## 8. A signed resolution decomposition

For real r>0 let
\[
\mathcal P_r(N)=\frac14\sum_{m,n\le N}
\frac{\mu(m)\mu(n)}{\sqrt{mn}}\operatorname{sech}^{r}(\tfrac12\log(m/n)).
\]
Define A_r=P_r-P_(2r). Its diagonal vanishes exactly; its off-diagonal kernel is sech^r(z)(1-sech^r(z)), concentrated at |z|~r^(-1/2). For r_l=3*2^l,
\[
Q_0(N)=D(N)+\sum_{l<L}A_{r_l}(N)+O(N^{-3})
\]
once r_L>=48N^2 log N. There are O(log N) resolutions. This is an exact sign-preserving way to split multiplicative/additive covariance scales. No bound on the signed sum, nor on the stronger sum of absolute values, follows from the identity alone.
