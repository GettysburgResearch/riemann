# Both signs of the third Mertens mean in every sufficiently late window

Write \(J(X)=e^{-\gamma_E}\int_2^X E_3(t)\,dt\), with the actual finite Euler product as in the [third Mertens mean note](zhao-third-mertens-nov18.md). Suppose \(\Theta=1\). For all sufficiently large \(u\) the interval
\[
 [e^u,\exp(u+C F(u)\log(2u/F(u)))]
\]
contains points \(X_+,X_-\) with \(\pm J(X_\pm)\ge X_\pm\exp(-2F(u))\). Here \(F\) is the infimum of the zero lines \((1-\beta)u+\log\gamma\) and the line \(u/2\), and \(C\) is absolute. In particular every \([Y,Y^{1+\epsilon}]\), for each fixed \(\epsilon>0\) and all sufficiently large \(Y\), contains both signs of size \(X^{1-o(1)}\).

## Parameters at an arbitrary scale

Take any minimizing zero, put \(d=1-\beta, b=\log\gamma, m=du\). Then \(F=m+b=o(u)\), \(d\to0\), \(b\to\infty\). The Vinogradov–Korobov zero-free region gives \(m\gg u^{1/3}/(\log u)^{1/3}\), since \(b\le u\). In particular every fixed polynomial in \(u\) is \(\exp(o(m))\). Put
\[
 H=B F(u)\log(2u/F(u)),\qquad q=\kappa H^2/(m u)
\]
with \(\kappa=10^{-5}\) and an absolute constant \(B\) to be chosen large. Then \(F=o(H)\), \(H=o(u)\), and \(qu\to\infty\). The argument uses this extra width in two different ways.

## Upper bound outside the initial part of the window

For \(u+H\le w\le u^4\), the classical truncated von Mangoldt formula with height \(T\asymp e^{2w}\) gives
\[
 e^{-w}|\vartheta(e^w)-e^w|\ll u^{O(1)}e^{-F(u)}. \tag{1}
\]
As in the companion note one can take a half-integer argument and then return to \(e^w\). Zeros with \(h=1-\beta'\ge h_0\) for any fixed small positive \(h_0\) cost \(O(e^{-h_0 w}w^2)\). Take \(h_0\) small enough that the usual uniform Ingham bound
\(N(1-h,T)\ll T^{c h}(\log T)^c\) for \(0\le h\le h_0\) gives \(N(1-h_0,T)\ll T^{1/4}\). For \(h<h_0\) and \(|\gamma'|>T_0=e^{4F(u)}\), partial summation of the latter bound gives \(\sum1/|\gamma'|\ll T_0^{-3/4}\). For \(|\gamma'|\le T_0\), each summand is bounded by
\[
 e^{-hw}/|\gamma'|\le e^{-F(u)} e^{-hH}.
\]
The sum of the last exponential weights over this range is \(O(u^{O(1)})\), by partial summation of \(N(1-h,T_0)\), since \(H\ge2c\log T_0\) eventually. Conjugate zeros obey the same estimate. The prime-power and truncation errors satisfy (1).

Partial summation of (1) now gives \(|E_2(e^w)|\ll u^{O(1)} e^{-F(u)}\) for \(u+H\le w\le u+8H\). The upper endpoint \(u^4\) in (1) suffices for the partial summation integral, since the PNT remainder for larger logarithmic arguments \(s\) is \(O(e^{-c\sqrt s})\) after division by \(e^s\). Using boundedness of \(E_2\) for the integral below \(e^{u+H}\), we obtain for \(u+2H\le v\le u+8H\)
\[
 e^{-v}\int_2^{e^v} E_2(x)^2\,dx
 \ll e^{-H}+u^{O(1)}e^{-2F(u)}.\tag{2}
\]

## Localization of the arithmetic source

Use \(g\) and its two distributional integrations by parts from the [direct oscillation note](zhao-native-oscillation-nov18.md). For \(u+4H\le\tau\le u+5H\) test the source with
\(k=\chi G_{\tau} e^{-i\gamma v}\), where the Gaussian is centered at \(\tau\) and has variance \(2q\tau\). The cutoff \(\chi\) equals one on \(|v-\tau|\le H/2\), vanishes for \(|v-\tau|\ge H\), and has derivatives of orders \(j=1,2\) bounded by \(O(H^{-j})\). Fix a constant \(L\) large enough that \(\kappa L^2\ge100\), and set \(r=Lm/H=o(1)\). Up to an overall sign and an error \(O(e^{-7m})\) the source integral equals
\[
 \sum_{h\le 10d,\ |\gamma'-\gamma|\le r}
  \exp(\tau(\lambda+q\lambda^2)),\qquad
 \lambda=-h+i(\gamma'-\gamma).\tag{3}
\]
To verify the uniform error, the floor replacement costs \(e^{-u+b}u^{O(1)}\), and the trivial zeros contribute \(O(e^{-u})\). For zeros with \(h>10d\), keep the cutoff. Its Fourier integral in frequency \(t=\gamma'-\gamma\) is \(O(u^{O(1)} e^{-10m}(1+|t|)^{-2})\), by differentiating its amplitude twice on \(v\ge u\), where \(e^{-hv}\le e^{-10m}\). The derivatives have only polynomial costs since \(q\tau\gg1\). The sum of the frequency weights over all zeros is \(O(\log(2+\gamma))\).

For \(h\le10d\) complete the Gaussian on the whole line. Its displaced center is \(\tau-2q\tau h\), within \(O(\kappa H^2/u)=o(H)\) of \(\tau\), and its total mass is \(e^{-h\tau+q\tau h^2}\le1\). On the cutoff tails the integral of the amplitude and its first two derivatives is \(\ll u^{O(1)} e^{-20m}\), from the Gaussian bound at distance at least \(H/3\) and \(q\tau\le 2\kappa H^2/m\). Two integrations by parts and the frequency-weight sum justify completing the cutoff simultaneously over these zeros. The completed terms with \(|t|>r\) cost \(O(u^{O(1)} e^{-90m})\) by \(q\tau r^2\ge100m\) and unit-interval zero counting. This proves (3).

The number \(n\) of retained terms satisfies \(1\le n\ll1+r b\). Indeed \(r\ge10d\) eventually and the positive real-part log-derivative argument at \(1+r+i\gamma\) from the direct note applies with multiplicity. Choose \(M=\lceil(u+4H)n/H\rceil\) and step \(a=(u+4H)/M\). The Kolesnik–Straus theorem supplies an integer \(M<j\le M+n\) for which the sum in (3) at \(\tau=ja\) has absolute value at least
\[
  \exp(-d\tau + q\tau d^2-O(n\log(2u/H))).
\]
Here the target zero supplies the displayed real exponent. This exact power-sum theorem allows repetitions. [Thorner and Zaman, Theorem 5.2](https://arxiv.org/pdf/1604.01750)

The cost is \(O(\log u)+O(Lm/B)\) since \(b\le F(u)\) and \(H\ge F(u)\). Choose \(B\) so the second term is at most \(m/10\). Then \(d\tau=(1+o(1))m\), and the full source integral has magnitude \(\ge e^{-5m/4}\) eventually. Formula (2) of the direct note bounds its magnitude above by
\[
 u^{O(1)}(1+\gamma)^2
 \int_{\tau-H}^{\tau+H}|g(v)|G_\tau(v)\,dv .
\]
This uses the first two derivatives of \(G_\tau\) on the cutoff, divided by \(G_\tau\), which cost at most a polynomial in \(u\). Thus the absolute mass in this window is at least \(e^{-4m/3-2b}\) for large \(u\).

## Extracting both signs at the finer scale

Divide \([\tau-H,\tau+H]\) into at most \(2H+2\) intervals of length at most one. One such interval has ordinary unweighted mass \(\int |g(v)|dv\ge e^{-4m/3-2b}/(2H+2)\), since the adaptive Gaussian is at most one. Center a second Gaussian \(P_t(v)=(4\pi H)^{-1/2}\exp(-(v-t)^2/(4H))\) at the midpoint \(t\) of this interval. It is \(\gg H^{-1/2}\) there. Its absolute mean of \(g\) is therefore at least \(e^{-3m/2-2b}\).

Its signed mean is \(O(e^{-cH})\). In the Laplace inversion from the direct note the weight is now \(\exp(tz+Hz^2)\). Start at \(\Re z=H/(4t)=a\) where \(|\mathcal L(z)|\ll1/a\), discard \(|\Im z|>2\), and move the rest to \(\Re z=-a\). The discarded part and the horizontal edges are \(O(u^{O(1)}e^{-3H})\) and the left edge is \(O(e^{-H/5})\). Holomorphy at zero keeps the transform bounded on the whole compact rectangle. The tails \(|v-t|>H\) also cost \(O(e^{-cH})\) since \(g\) is bounded. As \(H/F\to\infty\), both errors are negligible even when \(b\gg m\). The two parts of \(g\) of opposite signs each attain magnitude at least \(e^{-8m/5-2b}\) within \(|v-t|\le H\). These points belong to \([u+2H,u+7H]\).

The correction between \(g(v)\) and \(-J_1(e^v)/e^v\) is exponentially small in \(u\). The product correction (2), together with the integrated prime-power tail \(O(ve^{-v})\), is smaller than these signed excursions by a factor tending to zero, since \(2F=2m+2b\) and \(\log u=o(m)\). At the two selected points the resulting normalized magnitude exceeds \(e^{-2F}\). Taking \(C=7B\) proves the claim.

## Specified targets in proportional windows

The localization and sign extraction also apply to any specified zero with \(d=o(1)\), \(b=o(u)\), and \(m=du\gg\log u\) with \(m/\log u\to\infty\). For a fixed small \(\alpha>0\) take \(H=\alpha u\), \(q=\kappa H^2/(m u)\). The retained count is \(O(1+Lmb/H)\) and the loss in the power-sum step is \(O_\alpha(1+mb/u)=o(m)\). In this version the displaced center is within \(20\kappa\alpha(1+5\alpha)H <H/6\) of \(\tau\) when \(\alpha\le1/20\), which gives the same tail estimates. The source has mass at least \(\exp(-d\tau-o_\alpha(m))\), with \(\tau\le u+5H\). Both signs of the normalized linear mean attain at least
\[
 \exp(-(1+5\alpha)du-2b-o_\alpha(du))
\]
somewhere in \([u+2H,u+7H]\). This last estimate concerns the linear mean and has no minimization hypothesis. One can choose its center in any desired fixed proportional interior band by shifting the base \(u\) by a fixed factor and then taking \(\alpha\) sufficiently small.
