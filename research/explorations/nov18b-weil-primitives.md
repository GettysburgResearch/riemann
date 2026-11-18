# Exact prime domination on a full interval of causal Dirichlet sums

**Proposed unconditional theorem.** Let \(q\to\infty\), \(T=2\pi q\), and \(U=\tfrac12\log q\). For a fixed positive integer \(k\), choose complex \(\lambda_j\) with \(\Re\lambda_j\ge0\). Put \(h_j(v)=e^{-\lambda_j v}\mathbf1_{v\ge0}\) and \(h=h_1*\cdots*h_k\) in the additive real variable. On the full interval \(0\le u\le U\) set
\[
 S(u)=\sum_{n\le e^u} n^{-1/2+iT}h(u-\log n),\qquad
 g(u)=e^{-iTu} S(u)\mathbf1_{[0,U]}(u).
\]
These functions extend across the gaps between the log integers. The case \(k=1\), \(\lambda_1=0\) is the ordinary running partial sum of zeta at the critical-line height, modulated by \(e^{-iTu}\). The unnormalized statement is
\[
 W(g)\ \ge\ 2(U-\log2)\int_0^{\log2}|h(v)|^2\,dv-o(1).
 \tag{1}
\]
In particular it is strictly positive for every sufficiently large carrier. Constants in the error may depend on the fixed poles. Step functions at jumps are evaluated up to null sets. They lie in the domain of the explicit formula by smooth approximation for the finite prime form, the poles and the logarithmically weighted Fourier norm.

The arithmetic conclusion is stronger than a leading estimate. For every \(U>0\) and real carrier \(T\), there is the exact identity
\[
 2U\|g\|^2-P(g)=2\int_0^U (U-u)|S(u)|^2du+
 \sum_{j=1}^k\int_0^U\!\int_0^U
   e^{-\Re\lambda_j|u-v|}e^{-i\Im\lambda_j(u-v)}
   S(v)\overline{S(u)}\,dv,du .
 \tag{2}
\]
All the double integrals are nonnegative. If \(k=1\) and \(\lambda_1=0\), the last term equals \(|\int_0^U S(v)dv|^2\). No cancellation estimate for a sum of primes or critical-line zero verification is used.

## Arithmetic proof

Use the lower shift \(Vg(u)=\sum_{d\le e^u}\Lambda(d)d^{-1/2}g(u-\log d)\), so the actual prime term equals \(P(g)=2\Re\int_0^U Vg(u)\overline{g(u)}du\). The upper truncation of \(g\) introduces no boundary contribution at this step, since \(u-\log d\le u\le U\). Complete divisor summation gives
\[
 e^{iTu}Vg(u)=\sum_{n\le e^u}(\log n)n^{-1/2+iT}h(u-\log n).
\]
The Laplace transform of \(h\) is \(H(s)=\prod_j(s+\lambda_j)^{-1}\) on \(\Re s>0\). The identity \(-H'/H=\sum_j(s+\lambda_j)^{-1}\) gives \(v h(v)=\sum_j(h_j*h)(v)\). Hence, on the integration interval,
\[
 e^{iTu}Vg(u)=uS(u)-\sum_j\int_0^u e^{-\lambda_j(u-v)}S(v)dv.
\]
Taking the Hermitian part yields (2). For \(a>0\) the kernel \(e^{-a|w|}e^{-ibw}\) has a nonnegative Fourier transform, the translate of \(2a/(a^2+t^2)\). For \(a=0\) it is a rank-one positive kernel. This proves its sign for complex inputs including both endpoints.

## Gamma and pole comparisons

The supremum and total variation of \(S\mathbf1_{[0,U]}\) are both \(O_h(\sqrt{e^U}(1+U)^{k+1})\). This follows by summing the individual absolute weights, since the profile and its variation up to \(U\) cost \(O_h((1+U)^{k+1})\), including its initial jump if present. Thus
\[
 |\widehat g(T+w)|\ll_h \sqrt{e^U}(1+U)^{k+2}\min(1,1/|w|).
\]
On \(|w|\le T/2\), the actual gamma multiplier differs from \(\log q\) by \(O((1+|w|)/T)\). Integrating the squared bound gives total absolute error \(O_h(e^U(1+U)^{2k+5}/T)\). On the complement, integrating \((\log(2+|T+w|)+\log q)/w^2\) gives the same order, by continuity of the digamma multiplier near zero and Stirling elsewhere. At the two poles integrate by parts with \(S(u)e^{\pm u/2}\); each value costs at most \(O_h(e^U(1+U)^{k+3}/T)\). Since \(e^U=\sqrt q\), the total absolute gamma error and pole term tend to zero. Combining with (2), using \(S=h\) on \([0,\log2)\), proves (1). The integral in (1) is positive because \(h(v)=v^{k-1}/(k-1)!+O_h(v^k)\) as \(v\downarrow0\).

The jump approximation needed for the usual smooth-test convention follows by convolution with smooth compact approximate identities. The Fourier-side dominated convergence bound comes from bounded variation and the \(1/|w|\) decay. For any fixed sufficiently large \(q\), arbitrarily accurate compact smooth approximations preserve the strict sign.

## What the reflected half does

The proof of (1) uses log-interval length \(U\), whereas the full Nyquist interval has length \(2U\). On the latter interval (2) still computes \(P\) exactly, but the gamma-minus-prime main term would now contain \(2(U-u)|S(u)|^2\) of changing sign. A balanced reflection alone can cancel the apparent positive reserve completely.

To see the cancellation as an exact continuous calculation, let \(a>0\), let \(Z\) be an absolutely continuous complex function on \([0,U]\) with square-integrable derivative and \(Z(0)=0\), and take \(|\eta|=1\) with \(Z(U)=\eta\overline{Z(U)}\). Define \(S\) on \([0,2U]\) using
\[
 S(u)=Z'(u)-aZ(u)\quad(0<u<U),\qquad
 S(2U-u)=-\eta\overline{Z'(u)+aZ(u)}\quad(0<u<U).
\]
For this precisely matched pair one has
\[
 2\int_0^{2U}(U-u)|S(u)|^2du+
    \int_0^{2U}\!\int_0^{2U}e^{-a|u-v|}S(v)\overline{S(u)}\,dv\,du=0.
 \tag{3}
\]
Indeed the first integral equals \(-4a\int_0^U|Z|^2\) by integration by parts, since \(|Z'+aZ|^2-|Z'-aZ|^2=2a(|Z|^2)'\). Extend \(Z\) to \(F\) by \(F(2U-u)=\eta\overline{Z(u)}\) and zero outside. The matching trace at \(U\) and zero at the two outer endpoints give \(S=(\partial-a)F\) without a point mass. Plancherel for the Poisson kernel makes the second integral \(2a\|F\|^2=4a\|Z\|^2\).

The same pair of derivatives occurs in the arithmetic sources. If \(S_\pm=\sum_{n\le e^u}n^{-1/2+iT}e^{\mp a(u-\log n)}\), their jumps coincide, and \(Z=(S_- - S_+)/(2a)\) satisfies \(S_+=Z'-aZ\), \(S_-=Z'+aZ\) away from the jumps. Equation (3) is a result about an exactly matched reflection. Relating the actual high half to that reflection with the correct signed error is a separate arithmetic question. In particular the positive Volterra term in (2) cannot supply that sign by itself.
