# Both signs of the centered Goldbach error in every factor-1.14 interval on RH

Assume RH. For both signs, every sufficiently large interval $[X,57X/50]$ contains centered Goldbach error of total mass $\gg X^2$. The directed certificate below uses the first 160 zeta zeros. A longer interval already follows from elementary estimates for the entire zero spectrum. With $B(x)=\sum_{m+n\le x}(\Lambda(m)-1)(\Lambda(n)-1)$ and $B_\pm(x)=\max(\pm B(x),0)$, every sufficiently large $X$ satisfies
\[
                  \int_X^{4X/3} B_\pm(x)\,dx\gg X^2.                  \tag{1}
\]
Together with the published $|B(n)|\ll n\log^3n$, this gives $\gg X/(\log X)^3$ integers of each sign where $B_\pm(n)\gg X$ in every such interval. This supplies an explicit common interval ratio in the RH case of the [attained-edge recurrence](nov18b-variance-goldbach.md).

## A smooth signed mass and its arithmetic absolute mass

Choose $\phi$ to be the convolution of three uniform probability densities on $[0,7/75]$ and a smooth nonnegative probability density supported on $[0,1/200]$. Its support is contained in $[0,7/25+1/200]\subset [0,\log(4/3))$. Put $w(u)=u^{-2}\phi(\log u)$. Then $\int u w(u)\,du=1$ and, with the Fourier convention $e^{itx}$,
\[
          |\widehat\phi(t)|\le\min\{1,(22/|t|)^3\}.                 \tag{2}
\]

For odd $n$, at least one member of every prime-power pair summing to $n$ is a power of two, so $\sum_{m+l=n}\Lambda(m)\Lambda(l)=O(\log^2 n)$. The elementary linear terms and the prime number theorem consequently give
\[
   B(n)-B(n-1)=\sum_{m+l=n}\Lambda(m)\Lambda(l)-2\psi(n-1)+n-1
              =-n+o(n).
\]
Pairing consecutive even and odd indices yields
\[
               X^{-1}\int |B(Xu)|w(u)\,du \ \ge\ 1/2-o(1).          \tag{3}
\]
Indeed their two absolute values have sum at least $n-o(n)$ and the weighted even Riemann sum tends to $\frac12\int u w(u)\,du$. Moving either weight by one mesh step costs $o(1)$ after normalization, by the bounded derivative of $w$ and $|B(n)|\ll n\log^3 n$. The same estimate replaces the discrete sum by the displayed integral.

The complementary signed estimate on RH is
\[
                \left| X^{-1}\int B(Xu)w(u)\,du\right|<0.45         \tag{4}
\]
for every sufficiently large $X$. To derive it, write $z=1+it$. The smoothed identity from the Mellin formula for $F$ gives
\[
 \sum_n(\Lambda(n)-1)e^{-zn/X}
   =-\sum_\rho\Gamma(\rho)(X/z)^\rho+O((1+|t|)^A)
\]
with a fixed $A$ uniformly for $X\ge1$. This follows by the contour shift to $-1/2$ with the factor $z^{-s}$, as in (13) of the original estimate. The zero series in absolute value is $O(X^{1/2}(1+|t|)^A)$, since $\pi/2-|\arg z|\gg(1+|t|)^{-1}$. Use the bilateral Fourier inversion of $e^u w(u)$, extended by zero, and the identity $\int_0^\infty B(Xu)e^{-zu}\,du=z^{-1}(\sum_n a_n e^{-zn/X})^2$. The inverse transforms of $z^{-1-\rho-\rho'}$ are $u^{\rho+\rho'}/\Gamma(1+\rho+\rho')$ on $u>0$. The rapid Fourier decay of $e^u w(u)$ justifies the double-series interchange before inversion by the preceding absolute polynomial bound. The cross and error terms after normalization are $O_w(X^{-1/2})$. Thus, with multiplicity,
\[
 X^{-1}\int B(Xu)w(u)\,du
 =\sum_{\gamma,\gamma'}
   \frac{\Gamma(1/2+i\gamma)\Gamma(1/2+i\gamma')}
        {\Gamma(2+i(\gamma+\gamma'))}
   X^{i(\gamma+\gamma')}\widehat\phi(\gamma+\gamma')
   +O_w(X^{-1/2}).                                                  \tag{5}
\]

## Bounding the whole zero sum

Every positive ordinate exceeds $14$. On RH the classical identity $\sum_\rho|\rho|^{-2}=2+\gamma_{\rm E}-\log(4\pi)$ gives
\[
       \sum_{\gamma>0}\gamma^{-2}
       \le(1+1/784)(2+\gamma_{\rm E}-\log(4\pi))/2<0.024.
\]
Let $S=|\gamma+\gamma'|$, $m=\min(|\gamma|,|\gamma'|)$, and let $C_{\gamma,\gamma'}$ denote the gamma quotient in (5). The identities $|\Gamma(1/2+it)|^2=\pi/\cosh(\pi t)$ and $|\Gamma(2+it)|^2=(1+t^2)\pi |t|/\sinh(\pi|t|)$ give $|C_{\gamma,\gamma'}|\le 3 S^{-3/2}$ for equal signs. Using $S^4\ge16\gamma^2\gamma'^2$ and $S\ge28$ bounds their entire contribution by
\[
     \frac{2\cdot 3\cdot22^3}{16\sqrt{28}}\,(0.024)^2<0.436 .
\]

For opposite signs the same identities give $|C_{\gamma,\gamma'}|\le 2\pi e^{-\pi m}$ for all $S$ (including zero) and $|C_{\gamma,\gamma'}|\le3e^{-\pi m}S^{-3/2}$ for $S>0$. The first bound uses $\sinh(\pi S)\le\pi S e^{\pi S}$. If $\max(|\gamma|,|\gamma'|)\le2m$, multiply the first bound by $\gamma^2\gamma'^2\le4m^4$. If the maximum exceeds $2m$, it is at most $2S$ and $S\ge m$, so the second bound times (2) and $\gamma^2\gamma'^2$ is at most $12\cdot22^3 e^{-\pi m}/\sqrt m$. Both resulting bounds are below $10^{-10}$ at all $m\ge14$. Multiplying by $2(0.024)^2$ bounds the complete opposite-sign sum. This proves (4).

Finally $2B_\pm=|B|\pm B$. Subtraction of (4) from (3) leaves a positive fixed margin for each sign against $w$. Since $w$ is bounded, supported in $[1,4/3]$, and nonnegative, (1) follows. One may move the limits by a bounded number of integer mesh steps using the published pointwise upper bound.

[Goldston–Suriajaya, Theorem 4](https://arxiv.org/abs/2110.14250) · [Riemann zeta zero verification](https://arxiv.org/abs/2004.09765)

## A directed certificate for the factor $57/50$

Use three nonnegative uniform densities of respective widths $\ell_j=13p_j/10000$ with $p_j=51,34,15$, followed by a nonnegative smooth density of width $1/4000$. Their support ends at $0.13025<\log(57/50)$. The arithmetic lower bound (3) is identical. In the signed upper bound the three factor moduli are now $|\operatorname{sinc}(\ell_j S/2)|$, with $\operatorname{sinc} x=\sin(x)/x$. Thus their product is at most $A/S^3$, $A=8/(\ell_1\ell_2\ell_3)$. The smooth fourth factor has modulus at most one.

The [directed checker](nov18b-goldbach-parity-check.py) encloses the first 160 positive ordinates $\gamma_j$ using Arb, and puts $T=\gamma_{160}$. For pairs among them it sums the product of the three actual sinc moduli and the upper bound $\sqrt{2\pi}S^{-3/2}$ for the gamma quotient. This last bound follows from the same two exact gamma identities used above. Write $G=\sum_{j\le160}\gamma_j^{-2}$ and let $D$ be the stated upper bound $(1+1/784)(2+\gamma_{\rm E}-\log(4\pi))/2$ minus $G$. Then the contribution from all other equal-sign pairs is at most
\[
 \frac{2\sqrt{2\pi}A}{16\sqrt T}
 \left(D^2+2D\sum_{g=\gamma_1,\ldots,\gamma_{160}}
                  \frac{16(g/T)^2}{(1+g/T)^4}g^{-2}\right).
\]
Indeed $S\ge T$ for each such pair. For a pair with one low ordinate $g$ and one high ordinate $H$, the factor $16g^2H^2/(g+H)^4$ is bounded by its value at $H=T$, by monotonicity in $g/H\le1$. For two high ordinates the corresponding factor is at most one. Using the nonnegative tail bound $D$ then gives the expression above. For the opposite-sign argument the constant $22^3$ changes to $A$; the checker verifies the corresponding inequalities at $m=14$ and the bounding functions decrease thereafter.

At 96 bits the finite equal-sign contribution is at most $0.424232$, the remaining equal-sign contribution is at most $0.070495$, and the total including the opposite signs is less than $0.496$. Thus the strict gap below $1/2$ survives the $o(1)$ error and proves
\[
                 \int_X^{57X/50} B_\pm(x)\,dx\gg X^2 .
\]
The same pointwise envelope gives $\gg X/(\log X)^3$ integers in this shorter interval for each sign at magnitude $\gg X$. Run the checker with Python and the python-flint package.
