# Exact amplification available from all common dilations of Möbius

The [single-zero test](nov18b-reciprocal-theta.md) at scales \(X/d\) pairs one kernel against every arithmetic function \(n\mapsto1_{d\mid n}\mu(n/d)\). Their common-dilation correlations can all be computed. This gives both the optimal infinite-sample amplification and a polynomial range where every finite-sample norm approximates its limit. These differ from the vertical zeta mollifier norms in the [companion calculation](nov18b-mollifier.md).

Put \(C_0=1/\zeta(2)\) and define \(u_d(n)=\sqrt{d/C_0}\,1_{d\mid n}\mu(n/d)\). Write \(\|a\|_B^2=\lim_{X\to\infty}X^{-1}\sum_{n\le X}|a(n)|^2\) on their finite span. For \(1/2\le\beta=\Re\rho<1\) the following is unconditional:
\[
 \sup_{c\ne0}\frac{|\sum_{d\le D} c_d d^{1/2-\rho}|^2}
                   {\|\sum_{d\le D}c_d u_d\|_B^2}
 = \frac{C(\rho)D^{2-2\beta}}{2-2\beta}
       +O_{\beta,\epsilon}(D^{1-\beta+\epsilon}).               \tag{1}
\]
Uniformly for \(1/2\le\beta<1\) and all imaginary parts, the leading factor satisfies
\[
 C(\rho)\asymp |\zeta(2-\rho)|^2\zeta(3-2\beta)                 \tag{2}
\]
with absolute comparison constants. The asymptotic error in (1) may depend on the distance to \(\beta=1\). For every coefficient vector on \([1,D]\), independently of its choice after seeing \(X\), one also has
\[
 \frac1X\sum_{n\le X}\left|\sum_{d\le D}c_d u_d(n)\right|^2
 =\left(1+O_\epsilon(D^{1+\epsilon}/\sqrt X)\right)
       \left\|\sum_{d\le D}c_du_d\right\|_B^2 .                  \tag{3}
\]
In particular this is a uniform relative asymptotic whenever \(D\le X^{1/2-\eta}\) for fixed \(\eta>0\).

## The prime-by-prime inverse Gram

For \(g=(d,e)\), write \(a=d/g,b=e/g\). In a common multiple \(n=[d,e]k\) the two Möbius factors give \(\mu(a)\mu(b)\mu(k)^2 1_{(k,ab)=1}\). The squarefree density with that coprimality is \(C_0\prod_{p\mid ab}p/(p+1)\). This follows by inserting \(\mu^2(k)=\sum_{h^2\mid k}\mu(h)\) and counting the coprime complements. Consequently the limiting Gram of the \(u_d\) is the tensor product over primes of tridiagonal Toeplitz matrices:
\[
 G_p(i,i)=1,\qquad G_p(i,i+1)=G_p(i+1,i)=-\frac{\sqrt p}{p+1},
 \qquad G_p(i,j)=0\quad(|i-j|>1).
\]
Equivalently let \(r=p^{-1/2}\) and take the unit circle with probability weight \(|1-rz|^2/(1+r^2)\) times normalized Haar measure. Its monomial Gram is exactly \(G_p\). Identify \(u_d\) with the monomial \(\prod_p z_p^{v_p(d)}\) in the finite tensor product meeting the indices.

The monic degree-\(k\) orthogonal polynomial and its squared norm are
\[
 P_{p,k}(z)=\sum_{j=0}^{k}r^{k-j}\frac{1-r^{2j+2}}{1-r^{2k+2}}z^j,
 \qquad h_{p,k}=\frac{1-r^{2k+4}}{(1+r^2)(1-r^{2k+2})}.
\]
Indeed its coefficients solve \(c_i-r(c_{i-1}+c_{i+1})/(1+r^2)=0\) for \(i<k\), \(c_{-1}=0,c_k=1\). The final inner product against \(z^k\) gives the norm. This also gives \(P_{p,0}=1, h_{p,0}=1\). The orthonormal polynomials \(O_d(z)=\prod_{p^k\parallel d}P_{p,k}(z_p)/\sqrt{h_{p,k}}\) are triangular on divisors, hence form a basis for any finite divisor-closed set. The squared norm of evaluation is exactly \(\sum_{d\le D}|O_d((p^{1/2-\rho})_p)|^2\) by finite Hilbert duality.

Set \(w(d)=d^{2\beta-1}|O_d((p^{1/2-\rho})_p)|^2\). This is multiplicative. With \(q=p^{\rho-1}\), the ratio \(P_{p,k}(p^{1/2-\rho})/(p^{1/2-\rho})^k\) is
\[
 \sum_{j=0}^{k}q^j\frac{1-r^{2(k-j+1)}}{1-r^{2k+2}} .
\]
In particular \(w(p^k)\ll(k+1)^2\) uniformly. For fixed \(\beta<1\), \(w(p)=1+O(p^{\beta-1}+1/p)\). Hence the Dirichlet series for \(v=w*\mu\) converges absolutely at every real \(s>\beta\) (use \(s>1/2\) for the higher powers). Convolving \(w=1*v\) and replacing the integer parts by their real arguments shows \(\sum_{d\le D}w(d)= C(\rho)D+O_{\beta,\epsilon}(D^{\beta+\epsilon})\), where
\[
 C(\rho)=\prod_p(1-1/p)\sum_{k\ge0}w(p^k)p^{-k}.
\]
Partial summation yields (1). For (2), \(w(p)=|1+q/(1+r^2)|^2/h_{p,1}\), which is \(1+2\Re q+|q|^2+O(1/p)\) uniformly for \(|q|\le1\). The error of the higher local terms in the logarithm is \(O(p^{-2})\), also uniformly. Summing gives \(2\log|\zeta(2-\rho)|+\log\zeta(3-2\beta)+O(1)\), including the finitely many small primes by positivity and uniform boundedness of their factors.

## The genuinely finite arithmetic norm

For \(Y>0\), squarefree counting by the same square-divisor expansion gives
\[
 \sum_{k\le Y,(k,m)=1}\mu(k)^2=
 C_0Y\prod_{p\mid m}\frac{p}{p+1}+O(\tau(m)\sqrt Y).
\]
For \(Y<1\) the bound follows directly; for larger \(Y\), count each coprime inner interval with error at most \(\tau(m)\) and extend the absolutely convergent squared-divisor main series. The error in the normalized \((d,e)\) Gram entry is therefore \(O_\epsilon(D^\epsilon\sqrt{(d,e)/X})\). Its absolute row sums are \(O_\epsilon(D^{1+\epsilon}/\sqrt X)\), since \(\sum_{e\le D}\sqrt{(d,e)}\le D\sum_{r\mid d}r^{-1/2}\).

It remains to compare the ordinary squared coefficient norm with the limiting Gram norm. A coefficient of the monomial indexed by \(n\mid d\) in \(O_d\) has modulus at most \(D^{o(1)}\sqrt{n/d}\). This follows term by term from the local formula and the fixed bound on \(h_{p,k}^{-1/2}\), since \(2^{\omega(d)}=D^{o(1)}\). If the orthonormal-basis coefficients are \(b_d\), Cauchy gives
\[
 \sum_{n\le D}\left(\sum_{k\le D/n}|b_{nk}|/\sqrt k\right)^2
   \le (1+\log D)\sum_{d\le D}\tau(d)|b_d|^2
   \ll_\epsilon D^\epsilon\sum_d|b_d|^2 .
\]
Thus \(\sum |c_d|^2\ll_\epsilon D^\epsilon\|\sum c_du_d\|_B^2\). Combining with the row-sum bound, adjusting \(\epsilon\), proves (3).

In the Gaussian test the coefficient of \(\sqrt d\,1_{d\mid n}\mu(n/d)\) is \(d^{1/2-\rho}\) times a known smooth cutoff very near one for \(d\ll X\). Without spatial cancellation, Cauchy on a segment of length of order \(X\) costs order \(X^{1-\beta}\) for the weighted test. The exact limiting amplification in (1) grows as \(D^{1-\beta}\), and (3) proves the limiting comparison for lengths strictly below \(\sqrt X\). This computes the cost of the complete common-dilation argument rather than assuming unrelated shifts to be independent. The actual additional signed cancellation on the observation interval is open.
