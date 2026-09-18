# 04 — Persistent residuals, exact zero kernels, and tail localization

Source U4/A4, preserving U3's superseded bounds. Full proofs and the original
numerical programs are in retained sources stage 02. References: [B18], [H22],
[LS], [B01]. The source-dependent lower gain remains unproved.

## The weakest scale condition actually proposed

Since B_N is nested, E_N decreases to a limit L. The user's liminf can therefore
be replaced by a limit. If L>0, it suffices to find c(L)>0 and a set J of dyadic
indices such that

$$
\sum_{j\in J}\frac1{j\log j}=\infty,\qquad
E_{2^j}-E_{2^{j+1}}\ge\frac{c(L)}{j\log j}\quad(j\in J).
$$

Telescoping contradicts the finite total drop in E. Any positive c(L) works;
a particular c_0 L^2 is not essential. Bad scales may be discarded only while
the retained WEIGHTED sum diverges; infinitely many isolated scales need not do.
No such arithmetic lower bound was established.

Let P project onto B=closure union B_N. Then

$$
e_N=(I-P)1+(P-P_N)1=e_\infty+e_N^{\mathrm{tr}},
\quad \|e_\infty\|^2=L,\quad\|e_N^{\mathrm{tr}}\|^2=E_N-L.
$$

Every new b_n is orthogonal to e_infinity. Thus Schur gain sees only the
transient part and is at most E_N-L. A large TOTAL residual cannot supply a
lower bound on its correlation with the new family by generic Hilbert geometry.

## Exact kernels invalidate the leading-power shortcut

For Re z>1/2,

$$
h_z(k)=k(k+1)(k^{-\bar z}-(k+1)^{-\bar z}),\quad
\|h_z\|^2\le\frac{|z|^2}{2\Re z-1},
$$
$$
\langle1,h_z\rangle=1,\qquad
\langle b_n,h_z\rangle=\zeta(z)(1/n-n^{-z}).
$$

The norm bound follows by Cauchy--Schwarz on each interval [k,k+1]; summation
then integrates x^{-2 Re z}. At a right-side zero rho, every correlation with
b_n is EXACTLY zero and <e_N,h_rho>=1. Consequently

$$
E_N\ge1/\|h_\rho\|^2\ge(2\Re\rho-1)/|\rho|^2.
$$

In these weighted coordinates h_z~conj(z) k^{1-conj(z)}, not k^{z-1}.
Its lower-order terms are essential for exact annihilation. Correlations of
only the leading power cannot be substituted for those of the full vector.
No completeness assertion about all of B-perp is needed for this obstruction.

The proposed inference that small D forces off-line zeros to be few and very
near the line was corrected: the mass only weighs each displacement by roughly
1/gamma^2. Numerical improvements cannot exclude arbitrarily high hidden zeros.

## Coefficient bounds: the successive improvements

For any A=sum_{2<=n<=N}c_n b_n, set A(0)=0,

    a_1=sum c_n/n, a_n=-c_n for n>=2, u_d=A(d)-A(d-1).

The floor representation gives A(k)=sum a_n floor(k/n), u_d=sum_{n|d}a_n for
d<=N, and a=mu*u. For the optimal A_N, ||A_N||<=1 implies the first coarse
estimate |A_N(k)|<=sqrt(k(k+1)), |u_k|<=2k. Thus

    |c_{N,n}|<=2 sigma_1(n), sum |c_{N,n}|<=2N^2,
    tail_{k>K} ||e_N||^2 <= (1+2N^2)^2/(K+1).

This was the initial N^6 cutoff with an O(N^{-2}) error. It is retained as
history, not as the strongest bound.

A weighted difference estimate valid for EVERY finite A is

$$
\sum_{d\le N}|u_d|^2/d^2\le6\|A\|^2.
$$

Mobius inversion and Cauchy--Schwarz then give

$$
\sum_{n=2}^N|c_n|\le\sqrt6 N^{3/2}\|A\|,
\qquad \sum_{n=2}^N|c_n|^2/n^2\le6H_N^2\|A\|^2.
$$

For the second inequality, write a_n/n=sum_{j|n}(mu(j)/j)(u_{n/j}/(n/j)) and
use the triangle inequality for l2 dilation operators. In particular,

$$
G_N\succeq I/(6N^3),\qquad G_N\succeq I/(6N^2H_N^2).
$$

These bound finite conditioning, not the approximation error's asymptotics.
They validate the interval-gradient optimum enclosure in Chapter 03.

## Large-sieve cutoff for the unknown optimal coefficients

Periodic averaging is used here ONLY to bound a remote tail, not substituted
for the full weighted norm. The elementary covariance is

$$
\operatorname{Cov}_{\mathrm{per}}(b_m,b_n)
=(\gcd(m,n)^2-1)/(12mn).
$$

The full retained proof bounds the mean of A by
|mean(A)|^2<=N^2||A||^2 using Mobius inversion and summation by parts, with only
trivial bounds for finite Mobius sums. The gcd-squared matrix has row sums at
most N^2 H_N. Combining with the weighted coefficient bound gives

$$
\operatorname{Var}_{\mathrm{per}}(A)\le\tfrac12N^2H_N^3\|A\|^2,
\qquad M_{\mathrm{per}}(|e_N|^2)\le4N^2H_N^3.
$$

All Fourier frequencies of e_N have reduced denominators at most N. After
combining duplicates, the additive large sieve [LS] gives for every interval
of J consecutive integers

$$
\sum_{k=M+1}^{M+J}|e_N(k)|^2
\le(N^2+4\pi J)M_{\mathrm{per}}(|e_N|^2).
$$

Summing the weighted dyadic intervals beyond K proves

$$
\sum_{k>K}\frac{|e_N(k)|^2}{k(k+1)}
\le M_{\mathrm{per}}(|e_N|^2)
\left(\frac{8\pi}{K}+\frac{4N^2}{3K^2}\right)
\le\frac{108N^2H_N^3}{K},\quad K\ge N^2.
$$

Thus K=N^{2+epsilon} has a vanishing tail, and the explicit choice
K=ceil(N^2(1+log N)^5) has remainder at most 108/(1+log N)^2. This achieves a
nearly quadratic window WITHOUT a conjectural O(1) bound for each optimal
coefficient. It does not show that the sum inside that window tends to zero.

## What survived and what did not

The exact gain identity, the divergent-scale relaxation, coefficient estimates,
conditioning bounds and remote-tail theorem survive as proposed component
proofs. The stronger sufficient gain estimate was relaxed, not proved. The
nonzero-correlation argument for zero-generated vectors was refuted. Fixed
geometric decay is excluded by the classical lower bound. Periodic estimates
are legitimate for the displayed tail bound but not an interchangeable norm;
Chapter 06 makes that failure explicit.
