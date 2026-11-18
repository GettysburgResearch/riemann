# How accurately can finitely many Dirichlet monomials mollify zeta?

Fix \(1/2<\sigma<1\) and write \(a=2\sigma\). For a finite Dirichlet polynomial \(M(s)=\sum_{d\in D}\lambda_d d^{-s}\) use the actual vertical mean
\[
 E_\sigma(M)=\lim_{T\to\infty}\frac1T\int_T^{2T}
 |1-\zeta(\sigma+it) M(\sigma+it)|^2\,dt .
\]
The sole limiting operation in this definition fixes every coefficient first. We obtain the sharp order
\[
 \inf_{|D|\le B,\;\lambda_d\in\mathbb C} E_\sigma(M)
 \asymp_\sigma B^{1-2\sigma}.                                      \tag{1}
\]
Even arbitrarily large, independently chosen integer frequencies have this lower bound. An initial segment attains the order. The conclusion gives a constraint on one way of detecting an individual off-line zero. It does not give a finite-height lower bound for mollifiers chosen after seeing that height.

## The exact mean and the optimal initial segment

The classical mean-square theorem for zeta at \(\sigma>1/2\) identifies it in vertical mean square with the limit of \(\sum_{n\le L}n^{-s}\). One direct proof first truncates at an integer \(Y\ge 4T\) of order \(T\), where the classical sharp truncation for zeta has error \(O_\sigma(T^{-\sigma})\) on \([T,2T]\), including the pole correction. The Dirichlet-polynomial mean value inequality bounds the mean square between the fixed cutoff \(L\) and \(Y\) by \(O(\sum_{n>L}n^{-2\sigma})\). Sending \(T\) and then \(L\) to infinity proves the assertion. Multiplication by the fixed finite \(M\) is bounded. Orthogonality of the exponentials \(n^{-it}\) therefore yields
\[
 E_\sigma(M)=\sum_{n\ge1}\frac{|e(n)|^2}{n^a},\qquad
 e=\mathbf1_{n=1}-\mathbf1*\lambda .
                                                               \tag{2}
\]
Here \(\mathbf1\) is identically one, \(*\) is Dirichlet convolution, and \(\lambda\) is zero off its support. The Gram matrix of \(\zeta(s)d^{-s}\) on a finite set is \(\zeta(a)[d,m]^{-a}\), and the only nonzero inner product of the target 1 with a basis element is the one for \(d=1\).

For any nonempty divisor-closed index set \(D\), put \(J_a(d)=d^a\prod_{p\mid d}(1-p^{-a})\). Since \((m,n)^a=\sum_{d\mid(m,n)}J_a(d)\), the Gram matrix factors as a diagonal scaling of the divisor-incidence matrix, \(\operatorname{diag}(J_a(d))\), and the transpose incidence matrix. Möbius inversion on \(D\) gives the \((1,1)\) entry of its inverse as \(\zeta(a)^{-1}\sum_{d\in D}\mu(d)^2/J_a(d)\). Projection onto that span gives
\[
 \min_{\operatorname{supp}\lambda\subset D} E_\sigma(M)
 =\frac1{\zeta(a)}\sum_{d\notin D}\frac{\mu(d)^2}{J_a(d)} .    \tag{3}
\]
The full Euler product in (3) is \(\zeta(a)\). Equivalently its normalized summands are the probability that the radical of an integer of law \(\mathbb P(n)=n^{-a}/\zeta(a)\) equals \(d\). Every prime occurs in that radical independently with probability \(p^{-a}\). Formula (3) is a Selberg quadratic-form calculation. It describes the available *total* mean-square budget exactly. For the different problem of mollifying on the critical line in height-dependent intervals, see [Radziwiłł](https://arxiv.org/abs/1207.6583).

For \(D=[1,N]\), the leading constant is explicit. Uniformly for \(1<a\le2\) and fixed \(0<\epsilon<1/2\),
\[
 E_{\min}=\frac{C(a)}{(a-1)\zeta(a)}N^{1-a}
          +O_\epsilon\big(N^{1/2+\epsilon-a}/\zeta(a)\big),\qquad
 C(a)=\prod_p\left(1+\frac{p^{-a-1}-p^{-2}}{1-p^{-a}}\right).      \tag{4}
\]
Indeed \(w(d)=\mu(d)^2d^a/J_a(d)\) is the convolution of \(\mathbf1\) with an arithmetic function \(g\) whose local Dirichlet factor is \(1+(p^{-a-s}-p^{-2s})/(1-p^{-a})\). Its series converges absolutely, uniformly in \(a\), on \(\Re s=1/2+\epsilon\). Replacing \(\lfloor x/n\rfloor\) by \(x/n\) in the convolution sum gives \(\sum_{d\le x} w(d)=C(a)x+O_\epsilon(x^{1/2+\epsilon})\). Partial summation proves (4). In particular, if \(a\downarrow1\), \(N\to\infty\), and \((a-1)\log N\to v\), the optimal mean-square error tends to \(e^{-v}\). The error may stay of order one even with a very long initial segment.

## Why sparse frequency choices cannot improve the power

This part applies to every finite support, with no divisor-closure or length hypothesis. Möbius inversion in (2) gives \(\mu*e=\mu-\lambda\). At every omitted squarefree \(m\) its absolute value is one. Choose \(b=(a-1)/2>0\) and put \(W_b(m)=\sum_{k\mid m} k^{-b}\). Weighted Cauchy–Schwarz gives
\[
 1\le W_b(m)\sum_{k\mid m}k^b|e(m/k)|^2
 \quad (m\text{ squarefree},\ m\notin D).                       \tag{5}
\]
For integer \(X\), at least \((2-\zeta(2))X\) integers up to \(X\) are squarefree by the union bound over square divisors. Also \(\sum_{m\le X}W_b(m)\le X\zeta(1+b)\). Set \(c=2-\zeta(2)>0\), \(K=2\zeta(1+b)/c\), and \(X=\lceil4B/c\rceil\). At least \(cX/4\) squarefree \(m\le X\) are omitted and satisfy \(W_b(m)\le K\). Sum (5), weighted by \(m^{-a}\), over these integers. Extending the nonnegative sum on the right gives
\[
 (c/4)X^{1-a}\le K\zeta(a-b) E_\sigma(M).
\]
This proves the lower bound in (1). Formula (4) supplies the upper bound. No bound on the individual coefficients was needed. Requiring real coefficients leaves the conclusion unchanged.

## Cost of excluding one zero by a global second moment

At a zero \(\rho\), the analytic residual \(1-\zeta M\) equals 1. On a fixed-radius disk about \(\rho\) avoiding the pole, its area integral of squared modulus is at least the disk area, by subharmonicity. Thus an argument seeking to pay less than this constant by integrating a uniform diagonal bound over a height interval of length \(T\) needs the normalized error below order \(1/T\). At fixed \(\sigma\), (1) puts the bulk threshold for this approach at \(B\asymp T^{1/(2\sigma-1)}\). At \(\sigma=3/4\) it already costs order \(T^2\) coefficients. For a disk one must account for its range of real parts. The statement concerns the cost predicted by the limiting diagonal alone. Locally adapted coefficients, higher moments and genuine cancellation of finite-height off-diagonal terms remain possible.
