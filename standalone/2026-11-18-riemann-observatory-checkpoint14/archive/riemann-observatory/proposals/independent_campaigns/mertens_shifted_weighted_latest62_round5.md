# A Mertens bound gives a rate for a shifted Möbius array

17 November 2026. The proof below treats the stated Mertens estimate as a source input. The reading of its proof was scoped to the Perron application. The approximation rate and its converse are derived here, with priority unassessed.

## Statement and source inputs

Let \(s=1/2+it\). For \(q\ge1\), real or integer, use
\[
d_q(P)^2=\frac1{2\pi}\int_{\mathbb R}|1-\zeta(s)P(s)|^2\,|s|^{-2q}\,dt .
\]
Under RH, Theorem 1.4 of Bui–Florea–Heycock (arXiv:2610.27591v1, p. 4) at \(k=1\) gives constants \(C,K>0\) such that, for sufficiently large \(x\),
\[
|M(x)|=\left|\sum_{n\le x}\mu(n)\right|\le K\sqrt{x}\exp\!\left(C\sqrt{\frac{\log x}{\log\log x}}\right).
\tag{1}
\]
Balazard–de Roton's Proposition 2 gives \(J_\epsilon\ll\epsilon\) under RH as \(\epsilon\downarrow0\), where \(J_\epsilon=\|(1-\zeta(s)/\zeta(s+\epsilon))/s\|_2^2\) and \(\|\,\cdot\,\|_2\) uses \(dt/(2\pi)\). Their Proposition 1 already decomposes the error for the same shifted Möbius family into a ratio defect and a truncation defect. [Mertens input](https://arxiv.org/pdf/2610.27591v1#page=4) · [Ratio estimate and decomposition](https://arxiv.org/pdf/0812.1689v1#page=4)

Fix a real \(A>C\), put \(L=\log N\), and take \(N\) sufficiently large. Define
\[
\epsilon_N=\frac{A}{\sqrt{L\log L}},
\qquad
P_N(s)=\sum_{n\le N}\mu(n)n^{-s-\epsilon_N}.
\]
Then under RH, using (1), for every fixed integer \(q\ge2\),
\[
d_q(P_N)=O_{q,A,C,K}\big((\log N\log\log N)^{-1/4}\big).
\tag{2}
\]
The squared error is \(O_{q,A,C,K}((\log N\log\log N)^{-1/2})\). This is a full-sequence estimate. The proof extends (2) to every fixed real \(q>1\) using Lindelöf and Plancherel. For any fixed \(A>0\), even if it is chosen without reference to \(C\), convergence of \(d_q(P_N)\) to zero along any unbounded subsequence would imply RH.

## Abel summation and the weighted bound

More generally, suppose \(|M(x)|\le K\sqrt{x}\exp(F(\log x))\) for all sufficiently large \(x\), with \(F\) continuously differentiable, concave for sufficiently large arguments, and \(F(u)=o(u)\). For \(\epsilon>0\), the series for \(1/\zeta(z)\) converges locally uniformly on \(\Re z>1/2\) by partial summation and agrees with the Euler-product reciprocal on \(\Re z>1\). Under RH this identifies it throughout the half-plane by analytic continuation, with the reciprocal extended by zero at \(z=1\). For integer \(N\), the exact endpoint convention is
\[
\frac1{\zeta(s+\epsilon)}-\sum_{n\le N}\mu(n)n^{-s-\epsilon}
=-M(N)N^{-s-\epsilon}+(s+\epsilon)\int_N^\infty M(x)x^{-s-\epsilon-1}\,dx.
\tag{3}
\]
The integral converges absolutely for each fixed \(s+\epsilon\) and the upper endpoint vanishes by \(F(u)=o(u)\).

Write \(E=\epsilon L-F(L)\) and \(\lambda=\epsilon-F'(L)\). If \(\lambda>0\), concavity gives \(F(u)-\epsilon u\le-E-\lambda(u-L)\) for all \(u\ge L\). In (3) the first term has modulus at most \(Ke^{-E}\). With \(u=\log x\), the integral has modulus at most \(Ke^{-E}/\lambda\), uniformly in \(t\). Thus for \(0<\epsilon\le1/4\) and \(q\ge2\),
\[
\left\|\frac{\zeta(s)}{|s|^q}
  \left(\frac1{\zeta(s+\epsilon)}-\sum_{n\le N}\mu(n)n^{-s-\epsilon}\right)\right\|_2
\ll_q K e^{-E}(1+\lambda^{-1})\left\|\frac{\zeta(s)}{s}\right\|_2.
\tag{4}
\]
Here \(|s+\epsilon|\le(1+2\epsilon)|s|\) and \(|s|\ge1/2\). The last norm is finite by classical critical-line convexity \(|\zeta(s)|\ll_\eta (1+|t|)^{1/4+\eta}\), taking \(0<\eta<1/4\). The remaining quotient defect is bounded in norm by \(2^{q-1}\sqrt{J_\epsilon}\). Minkowski therefore gives
\[
d_q(P_{N,\epsilon})\ll_q\sqrt{\epsilon}+K e^{-E}(1+\lambda^{-1})
\tag{5}
\]
under the ratio estimate and the stated hypotheses on \(F\).

For \(F=C\phi\), where \(\phi(u)=\sqrt{u/\log u}\), direct differentiation gives
\[
\phi'(u)=\frac{\log u-1}{2\sqrt{u}(\log u)^{3/2}},
\qquad
\phi''(u)=\frac{3-(\log u)^2}{4u^{3/2}(\log u)^{5/2}}.
\]
At \(\epsilon=\epsilon_N\) we have \(E=(A-C)\phi(L)\) and
\[
\lambda=\frac{A-(C/2)(1-1/\log L)}{\sqrt{L\log L}}
\asymp_{A,C}\epsilon_N.
\]
Since \(\phi(L)/\log L\to\infty\), the second term of (5) decays faster than every fixed power of \(L^{-1}\). This proves (2).

## Plancherel and the range of \(q\)

The integral in (3) is the Fourier transform, with kernel \(e^{-itu}\), of the real-variable function
\[
g(u)={\bf1}_{[L,\infty)}(u)e^{-(1/2+\epsilon)u}M(e^u).
\]
It belongs to \(L^1\cap L^2\). Plancherel for \(dt/(2\pi)\) and the tangent estimate give \(\|\widehat g\|_2=\|g\|_{L^2(du)}\le Ke^{-E}/\sqrt{2\lambda}\). The endpoint term of (3) is bounded in the product norm by \(2^{q-1}Ke^{-E}\|\zeta(s)/s\|_2\) for \(q\ge1\). For the integral term, the multiplier \(\zeta(s)(s+\epsilon)/|s|^q\) is bounded for any fixed \(q>1\) under Lindelöf, which follows from RH. Choose an exponent \(0<\eta<q-1\) in \(|\zeta(s)|\ll_\eta(1+|t|)^\eta\). This gives the analogue of (5) with \(1+\lambda^{-1/2}\) in place of \(1+\lambda^{-1}\). The \(q=1\) endpoint would require a separate estimate for the unbounded zeta multiplier. The upper bound here applies to \(q>1\).

For the converse use the established Hardy witness \(d_q(P)\ge\sqrt{2\beta-1}|\rho-1|/|\rho|^{q+1}\) at any nontrivial zero \(\rho=\beta+i\gamma\) with \(\beta>1/2\). The proof for real \(q\ge1\) follows the integer proof by using the analytic principal power of \(1/s\) in the right half-plane. Its modulus is \(|s|^{-1}\), and \(s^{-(q-1)}\) is a bounded analytic multiplier there. The uniform lower bound contradicts a subsequence with \(d_q(P_N)\to0\). The functional equation then places all nontrivial zeros on the line. [Hardy witness](../../audits/weighted_criterion_round2.md)

## Optional leading coefficient from the separate ratio calculation

The independent horizontal-ratio slope calculation implies a further consequence for this array, with its own proof dependency. In that proof replace \(d\nu=dt/(2\pi|s|^2)\) by \(|s|^{-2(q-1)}d\nu\). The multiplier is bounded and continuous for \(q\ge1\). On each fixed neighborhood of an isolated ordinate it enters the local rescaling through its value at that ordinate. Outside finitely many zero neighborhoods the original Poisson mass control still applies with the sup norm of the multiplier. The completion error remains \(O_q(\epsilon)\) in norm. This gives
\[
S_q=\lim_{\epsilon\downarrow0}\frac{1}{2\pi\epsilon}
\int_{\mathbb R}\left|1-\frac{\zeta(s)}{\zeta(s+\epsilon)}\right|^2\frac{dt}{|s|^{2q}}
=\sum_{\gamma}\frac{m_\gamma\big(1-\binom{2m_\gamma}{m_\gamma}/4^{m_\gamma}\big)}
{(1/4+\gamma^2)^q}.
\]
The positive, absolutely convergent sum runs over distinct ordinates of both signs. Since the truncation term is \(o(\sqrt{\epsilon_N})\), the reverse triangle inequality gives \(d_q(P_N)^2\sim S_q\epsilon_N\) for fixed \(q>1\). This describes the specified \(A\) and the specified array. [Ratio slope and exhaustion](../../audits/adversarial_reviews/horizontal_ratio_slope_director_adjudication_round5.md)

## Prior-source scope

The classical shifted Möbius approximants are due to Báez-Duarte. Balazard–de Roton use the same coefficients and the same split, and prove a \(q=1\) estimate at their chosen larger shift by a uniform-in-height argument using Perron contours. The difference in height weights prevents comparing the present bound as an improvement to that \(q=1\) theorem. The first-order logarithmic taper in Bettin–Conrey–Farmer has a different coefficient array and obtains a classical-distance asymptotic assuming additional control on inverse derivatives at the zeros. Ehm's weighted criterion supplies a prior qualitative \(q=2\) setting. [Báez-Duarte](https://arxiv.org/abs/math/0205003v1) · [Balazard–de Roton](https://arxiv.org/abs/0812.1689v1) · [Bettin–Conrey–Farmer](https://arxiv.org/abs/1211.5191) · [Ehm](https://arxiv.org/abs/2405.06349v2)

A limited web search on 17 November 2026 paired “Nyman”, “Mertens”, “shifted Möbius” and “weighted approximation”, and searched arXiv:2610.27591 together with “Nyman”, “Báez-Duarte” and “Beurling”. It returned the primary source inputs and older related criteria. The local checks covered the exact propositions in the archived manuscripts and existing priority notes. No exact antecedent for (2) with the new shift surfaced in this pass. Broader priority and optimality of the unrestricted weighted distance remain open in this record.
