# Endpoint countermodel for absolute Mellin evaluation on the zeta zeros

There exists a real \(C^\infty\) function satisfying the value bounds (B) of the Bombieri–Lagarias author manuscript, with finite \(p=3\) logarithmic strip norm, for which \(\sum_\rho|\widehat f(\rho)|=\infty\). This is an unconditional existence construction using Riemann–von Mangoldt counting and independent signs. It addresses absolute evaluation, and leaves convergence of the raw **signed** symmetric height sum at this endpoint unresolved. No canonical or priority decision is proposed. [Logarithmic sufficient condition](weighted135_critical_log_repair_review.md) · [Pinned manuscript, pp. 5–6](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf)

## Physical packets and size choices

Use the strip \(-1/4\le\beta\le5/4\), and fix a nonnegative \(C_c^\infty((-1/8,1/8))\) bump \(\psi\) with integral one. Choose disjoint positive integer ranges \([L_j,U_j]\) with \(L_{j+1}\ge U_j+3\) and with all \(L_j\) large. Write
\[
 S_j=\sum_{r=L_j}^{U_j}\frac1r\ge e^{4j},\qquad
 \lambda_j=\frac{e^{j/2}}{S_j},\qquad
 \mathcal C_j=\{n\in\mathbb Z:2^{L_j}\le n\le 2^{U_j+1}\}.
\]
For any chosen \(L_j\), the harmonic sum can be made as large as required by increasing the finite integer \(U_j\). There is no requirement that these ranges have sizes bounded by powers of \(j\). Set
\[
 a_{j,n}=\frac{\lambda_j}{n(\log n)^2},\qquad
 F(u)=\sum_{j\ge1}\psi(u-j)
             \sum_{n\in\mathcal C_j}\varepsilon_{j,n}a_{j,n}\cos(nu),
 \qquad f(x)=x^{-1/2}F(\log x),
\]
where the \(\varepsilon_{j,n}\) will be chosen in \(\{-1,1\}\). Every physical packet contains only finitely many carriers. The physically disjoint supports are locally finite, so \(f\) is real and \(C^\infty\) on \((0,\infty)\) for every sign choice. Also
\[
 \sum_{n\in\mathcal C_j}a_{j,n}\ll\lambda_j\le e^{-7j/2}.
\]
This follows from convergence of \(\sum_{n\ge2}1/(n(\log n)^2)\). Thus \(f(x)=O(x^{-4})\) at infinity and vanishes near zero and near \(1\). It satisfies (A) and (B), and the Mellin transform is represented by its integral on the entire stated strip. The sign choices do not affect any of these conclusions.

## Finite endpoint strip norm for all signs

As in the earlier repair, put \(w_3(t)=\sqrt{1+t^2}(\log(e+|t|))^3\), and define \(N_3\) by integrating \(w_3(t)|\widehat f(\beta+it)|^2\) over the chosen strip. Let
\[
 J_\beta(v)=\int \psi(u)e^{(\beta-1/2)u}e^{ivu}\,du .
\]
This has uniform rapid decay for \(\beta\) on the strip. Multiplication by the cosine places its two translates at the integer frequencies \(n,-n\), with an exterior factor \(a_{j,n}e^{(\beta-1/2)j}/2\) and phases of modulus one. For a finite sequence of integer carriers \(\nu\), moderation of \(w_3\) and rapid decay of \(J_\beta\) give
\[
 w_3(t)^{1/2}|J_\beta(t-\nu)|
 \ll_M w_3(\nu)^{1/2}(1+|t-\nu|)^{-M}.
\]
In particular the weighted Fourier norm of one packet is at most
\[
 C e^{(\beta-1/2)j}
       \left(\sum_{n\in\mathcal C_j}
              w_3(n)a_{j,n}^2\right)^{1/2}.
\]
For this almost-orthogonality bound, square the sum of envelopes by Cauchy–Schwarz using \(\sup_t\sum_{\nu\in\mathbb Z}(1+|t-\nu|)^{-M}<\infty\) for \(M>1\), then integrate the other factor. It is independent of the number of carriers, their signs and the physical translation phases.

For \(n\ge 2^{L_j}\), \(w_3(n)\asymp n(\log n)^3\), so the squared norm inside the parentheses is at most
\[
 C\lambda_j^2\sum_{n\in\mathcal C_j}\frac1{n\log n}
 \ll \lambda_j^2 S_j,
\]
by summation on the dyadic shells. Thus the full norm of packet \(j\), including its strip integral, is at most \(C e^{3j/4}\lambda_j\sqrt{S_j}=C e^{5j/4}/\sqrt{S_j}\le C e^{-3j/4}\). The sum of these bounds is finite. Triangle inequality gives \(N_3(\widehat f)<\infty\) for all sign choices. The physical value envelope also gives convergence of the Mellin integral, so its value is the sum of the packet transforms.

## Actual zeta zeros supply a lower bound in expectation

Now make the signs independent Rademacher variables. For a zero \(\rho=\beta+i\gamma\), write the absolutely convergent series
\[
 \widehat f(\rho)=\sum_{j,n}\varepsilon_{j,n} b_{j,n}(\rho),
\]
where \(b_{j,n}\) is the Mellin transform of the corresponding unsigned single carrier. For \(\gamma\in(2^r,2^{r+1}]\) with \(L_j\le r\le U_j\), choose \(n\in\mathcal C_j\) nearest to \(\gamma\), so \(|\gamma-n|\le1/2\). The matching sign of the cosine contributes
\[
 \frac{a_{j,n}}2 e^{(\beta-1/2)j}
                    e^{i(\gamma-n)j}J_\beta(\gamma-n).
\]
For \(0\le\beta\le1\) and \(|v|\le1/2\), the real part of \(J_\beta(v)\) is bounded below by a positive constant, because the integrand's cosine is uniformly positive on the support. This controls the **modulus** of the matching term, with no claim about its rotating phase. The other sign of this same carrier contains \(J_\beta(\gamma+n)\) and is negligible in comparison for all large \(L_j\). Consequently
\[
 |b_{j,n}(\rho)|\gg e^{-j/2}\frac{\lambda_j}{2^r r^2}.
\]
The other carriers may contribute arbitrary phases. Their cancellation is handled by the independent signs, not by taking a pointwise lower bound for an unsigned block.

For a finite Rademacher sum of complex coefficients the \(L^2\) norm is the \(\ell^2\) norm of the coefficients, and its fourth moment is at most three times the square of its second moment, by expansion and grouping paired indices. Applying Paley–Zygmund to the squared modulus gives
\[
 \mathbb E|\widehat f(\rho)|\ \gg\
 \Bigl(\sum_{j,n}|b_{j,n}(\rho)|^2\Bigr)^{1/2}
 \;=\; \|\widehat f(\rho)\|_{L^2(\mathbb P)}.
\]
The finite-sum identities and inequality pass to this series by its absolute convergence for each \(\rho\), uniformly in the sign choice. In particular the expectation is at least a fixed multiple of the one matching carrier's size above.

The unconditional Riemann–von Mangoldt formula gives \(\gg 2^r r\) positive zero ordinates in \((2^r,2^{r+1}]\) for all sufficiently large \(r\), with multiplicity. This uses a dyadic count and imposes no short-interval spacing condition. It follows that the sum of expected absolute evaluations over each such shell is \(\gg e^{-j/2}\lambda_j/r\). Hence the expected sum over the entire \(j\)-th range is
\[
 \gg e^{-j/2}\lambda_j S_j=1
\]
up to a common positive lower constant. The zero strips \(0<\beta<1\) and conjugate multiplicities are the usual ones for the nontrivial zeta zeros. Positive ordinates alone suffice for this argument. [Riemann–von Mangoldt source used for the zero count](../../sources/equivalence_round2/titchmarsh1986.pdf)

## Turning expectation into existence with divergent absolute trace

Divergence of the expectation alone would be insufficient. For the finite height sum \(X_T=\sum_{0<\Im\rho\le T}|\widehat f(\rho)|\), the triangle inequality in \(L^2\), and the two Rademacher bounds at each zero, give
\[
 \|X_T\|_{L^2(\mathbb P)}
 \le \sum_{0<\Im\rho\le T}\|\widehat f(\rho)\|_{L^2(\mathbb P)}
 \ll \mathbb E X_T .
\]
The uniform constant makes Paley–Zygmund applicable again, giving
\(\mathbb P(X_T\ge\tfrac12\mathbb EX_T)\ge c>0\) whenever \(\mathbb EX_T>0\). The expected finite sums tend to infinity by the disjoint ranges. For any \(B>0\) choose \(T\) with \(\mathbb EX_T>2B\). Then \(\mathbb P(X_\infty>B)\ge c\) for the monotone limit \(X_\infty\). Taking \(B\to\infty\) proves that with positive probability the absolute sum diverges, hence some fixed real choice of all signs gives the claimed function. This proves existence of a counterexample, beyond merely showing that the earlier Cauchy–Schwarz sufficient test fails at \(p=3\).

The right-hand arithmetic terms in the manuscript are finite for every sign choice by the strong value decay and vanishing near 1. The example supplies no lower bound for signed symmetric partial sums and does not distinguish whether \(p=3\) can imply their convergence by another argument. It addresses the endpoint of the absolute evaluation estimate on the actual zero multiset. It does not claim field priority or an author-level finding. No canonical file was edited.
