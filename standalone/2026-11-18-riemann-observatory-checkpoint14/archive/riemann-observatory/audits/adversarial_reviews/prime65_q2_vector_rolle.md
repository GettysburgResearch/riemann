# Directly weighted Hardy variation for \(Q_2\)

Let \(Q_2(s)=2\,2^{-s}-1\), \(Z(t)\) be the real Hardy function, and \(G(t)=Z(t)Q_2(1/2+it)\). The two components of \(G(t)\) vanish simultaneously at every critical-line zero. Applying the two-sided variation argument to both components and using the sparse arithmetic of \(Q_2\) reduces the existing upper bound for the unconditional derivative series. It also gives
\[
 \limsup_{Y\to\infty}\frac{Y}{\log^4Y}
   \sum_{\substack{\rho=1/2+i\gamma\\|\gamma|>Y}}
      \frac{|\zeta'(\rho)|^2|Q_2(\rho)|^2}{|\rho|^2}
 \le\frac{2}{\sqrt{960}}=\frac{1}{4\sqrt{15}}.
\]
The sharp RH-conditional coefficient is \(1/(12\pi)\) by the shifted moment theorem. The proof here gives an unconditional bound on the critical-line series and uses no zero spacing assumptions. [Earlier real Hardy variation](prime64_main_term_moments.md) · [RH-conditional polynomial](prime64_q2_full_polynomial.md)

## Vector variation

On the interval supporting a real \(C^1\) two-sided cutoff \(\varphi\), put \(f=\varphi G\). Assume the cutoff is one on the selected height block and its value and first derivative are zero at the two outside endpoints. Its second derivative is allowed to be piecewise continuous. Write \(f=f_1+if_2\) with \(f_i\) real. For each \(f_i\), in every gap between selected zeros there is a zero of \(f_i'\) by Rolle's theorem. These points need not coincide for the two components. Both outer endpoints also have \(f_i'=0\). Hence the total variation of \((f_i')^2\) is at least twice the sum of its values at the selected zeros. The derivatives are absolutely continuous, so summing the resulting inequalities yields
\[
 \sum_{T<\gamma\le 2T} |\zeta'(\rho)Q_2(\rho)|^2
 \le \int \!\left(|f_1'f_1''|+|f_2'f_2''|\right)dt
 \le \|f'\|_2\,\|f''\|_2.                                         \tag{1}
\]
For the left side, \(G'(\gamma)=Z'(\gamma)Q_2(\rho)\) and \(|Z'(\gamma)|=|\zeta'(\rho)|\). Thus reflection costs a factor two in (1). This avoids replacing \(|Q_2|^2\) at every zero by its maximum.

## Effective normalized coefficients

For \(T\ge400\) use \(M=\lceil T/2\rceil\), \(H=\log T\), and \(A(s)\) and the Euler polynomial \(P(s)=\sum_{n\le M}n^{-s}\) of the earlier centered moment proof. Multiplication by \(Q_2\) gives an exact coefficient array in \(Q_2(s)P(s)=\sum_{n\le2M}d_n n^{-s}\):
\[
 d_n=\begin{cases}
 -1,&n\le M\text{ odd},\\
 1,&n\le M\text{ even},\\
 2,&M<n\le2M\text{ even},\\
 0,&M<n\le2M\text{ odd}.
 \end{cases}
\]
In particular, the squared coefficients through \(M\) are exactly 1. This preserves the \(Q_2\) leading centered logarithmic moments instead of multiplying them by three or six.

Take \(\ell_n=\log n-\tfrac12\log M\) and
\(P_j(t)=\sum_{n\le2M} d_n n^{-1/2}\ell_n^j e^{-it\log n}\).
For \(M<n\le2M\), \(|\ell_n|\le(H+0.70)/2\), since \(M\le T/2+1\) and \(\log 2+\log(1+2/T)<0.70\). On \([0.9T,2.1T]\), the weighted Hilbert inequality has error coefficient \(3\pi(n+1)\) as in equation (6) of the earlier proof. The part of the coefficient norm from \(n\le M\) is bounded by the same expression (7). The extra even indices give
\[
 \sum_{M<n\le2M,\ n\ {\rm even}}4/n
 =2\sum_{v=\lfloor M/2\rfloor+1}^{M}1/v
 \le2(\log2+1/(M-1))<1.4.
\]
There are at most \((M+1)/2\) such indices. Retain their actual spacing in the weighted Hilbert inequality. Every tail even has minimum log gap at least \(2/(n+2)\) except the first tail even when \(M\) is odd. That exceptional index has the lower bound \(1/(n+1)\). Using the usual even gap at the exceptional index would undercharge its coefficient by at most \(4n^{-1}\big[(n+1)-(n+2)/2\big]=2\). Hence the extra contribution to the Hilbert correction is at most \(3\pi(M+4.4)((H+0.70)/2)^{2j}\), and to the diagonal at most \(1.2(1.4)T((H+0.70)/2)^{2j}\). Since \(1.2(1.4)+3\pi(0.5025+4.4/400)<6.6\), the full norm satisfies
\[
 \|P_j\|_2^2
 \le T(H/2)^{2j}
 \left[\frac{1.2H}{2j+1}+6.4+6.6(1+0.70/H)^{2j}\right].            \tag{2}
\]
No estimates on generalized-prime arithmetic are needed for this finite-array identity.

The Hardy phase derivatives are unchanged by putting \(Q_2\) inside \(P_j\), so equation (5) of the earlier proof still applies. In the radius-\(1/4\) disks used for the Euler remainder, \(|Q_2(s)|\le1+2^{3/4}<2.7\). Thus \(Q_2R\) has derivative norm bound \(32.4j!4^jT^{1/8}\) by Cauchy's formula. For any \(V\ge400\), put \(h=\log V\) and define
\[
 u_j=2^{-j}\sqrt{\frac{1.2}{2j+1}
           +\frac{6.4+6.6(1+0.70/h)^{2j}}{h}},
 \qquad e_j=32.4j!4^jV^{-3/8}h^{-j-1/2}.
\]
Use \(a_0,a_1,a_2\) as in the earlier centered proof with these \(u_j,e_j\). By (2), the phase bounds and the Euler remainder, they bound the normalized derivative norms of \(G\) for \(T\ge V\). With the same cubic cutoffs and their derivative bounds, (1) yields the effective coefficient
\[
 K_{\rm v}(V)=2\left(a_1+\frac{15a_0}{Vh}\right)
              \left(a_2+\frac{30a_1}{Vh}+\frac{600a_0}{V^2h^2}\right).
\]
Use \(K_{\rm v}\) in place of \(K\) in equation (2) of the earlier centered proof. The derivation of the dyadic tail bound is identical. At \(Y=10000,J=8\), the resulting rigorous tail bound is less than \(1.790676\). With the certified finite partial at 10000, this gives \(0.61649875288731141829<C_2<2.40718\). The bound is independent of the asymptotic quartic-tail diagnostic. [Finite partial through 10000](prime64_q2_partial_tail_observation.md) · [Arb verification](../../scripts/prime65_q2_vector_rolle_checks.py)

## Unconditional thin-block coefficient

For a fixed \(0<\eta\le1\), replace the selected block by \(T<\gamma\le(1+\eta)T\), and use outer margins of length \(\delta T\) with \(0<\delta\le0.1\). The support stays inside \([0.9T,2.1T]\). In the main diagonal term in (2) replace \(1.2\) by \(\eta+2\delta\), its exact interval length divided by \(T\). All other terms remain \(O(T(\log T)^{2j})\) or smaller after squaring, in their contribution relative to the leading derivative estimate. More explicitly, (6) of the earlier proof and the coefficient sum in (2) give the phase-polynomial norm with leading squared coefficient \((\eta+2\delta)/[2^{2j}(2j+1)]\), and the phase shift terms involving lower derivatives and the Cauchy remainder are lower order. The product-rule cutoff costs \(O((\delta T)^{-1})\) and \(O((\delta T)^{-2})\); for fixed \(\eta,\delta\) these also affect only the lower order. Thus the two-sign block has weighted sum at most
\[
 \left[\frac{2(\eta+2\delta)}{\sqrt{960}}+o(1)\right]T\log^4T.
\]
All \(o(1)\) terms are uniform for \(T\ge Y\) as \(Y\to\infty\), at fixed \(\eta,\delta\). Sum over \(T=(1+\eta)^mY\), divide each block by \(T^2\), and use \(\sum_{m\ge0}(1+\eta)^{-m}=(1+\eta)/\eta\). For the leading coefficient, the terms involving \(m\log(1+\eta)\) from the logarithmic polynomial are lower order as \(Y\to\infty\). This bounds the limsup by \(2(\eta+2\delta)(1+\eta)/(\eta\sqrt{960})\). Taking \(\delta\downarrow0\) at fixed \(\eta\), then \(\eta\downarrow0\), gives the stated coefficient.
