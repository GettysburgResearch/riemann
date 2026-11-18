# Signed prime cancellation for a pole-free contour witness

**Status.** Proposed consequence of the [cluster witness](weil-contour-nov18.md), with an assumed actual off-line zero. This determines the sign and quantitative precision of the arithmetic comparison for a nearby test. The argument uses the zero-side interpolation to evaluate the residual. A prime-side proof of positivity remains open.

## The signed arithmetic comparison

Use $T,\delta,H,L$ and the tilted contour construction from the companion. Write $F(z)=e^{\theta z}\Xi(z)$, $\eta=\pi/4-\theta$, with its specified optimized tilt. All constants below are absolute. For sufficiently large $T$ there is a smooth test $g$ of support radius at most $L+O(\log T/T)$ such that
\[
 \widehat g(i/2)=\widehat g(-i/2)=0,\qquad
 c m\le P(g)-G(g)\le C m,
 \qquad G(g)\ge \exp(2\eta T-C\log^2 T).
\]
Here $m$ counts the zeros in the disk around the given defect with multiplicity, $1\le m\ll\log T$. The two real quantities, in the convention $\widehat g(z)=\int g(u)e^{izu}du$, are
\[
 G(g)=\frac1{2\pi}\int_{\mathbb R}|\widehat g(t)|^2
   [\Re\psi(1/4+it/2)-\log\pi]dt,
 \qquad
 P(g)=2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\Re
    \int_{\mathbb R}g(u+\log n)\overline{g(u)}\,du .
\]
The sum is finite by support. These retain the signed prime-power phases and the full gamma density. The Guinand–Weil formula gives $W(g)=G(g)-P(g)$ after the two pole evaluations vanish. In particular the relative excess of the actual prime sum above the positive gamma integral is at most $Cm\exp(-2\eta T+C\log^2T)$. For the optimized tilt $\eta\gg(\log T/T)^{1/3}$, so the exponent is eventually negative. This conditioning statement is specific to this construction and normalization. It does not impose a complexity lower bound on other tests or arithmetic proofs.

## Why the exact projector is large away from its chosen cluster

Let $f_\infty$ denote the untruncated tilted projector and $f$ its smooth truncation, as in the companion. We may impose any fixed small absolute error, simultaneously in the uniform Fourier error $\ll(1+|z|^2)^{-1}$ on $|\Im z|\le1/2$ and the sample $\ell^2(\Gamma)$ error, by increasing the absolute constant in $L$. Let $D$ be the monic polynomial whose roots are the enclosed zeros in both disks with multiplicity. Its degree $d=2m$ is $O(\log T)$. There is a polynomial $B$ of degree less than $d$ such that
\[
                \widehat f_\infty(z)=F(z) B(z)/D(z).
\]
Indeed for $z$ exterior to the two contours the signed contour formula, after division by $F(z)$, is the difference of the two contour integrals of $1/[F(v)(z-v)]$ with the common $1/(2\pi i)$ factor. Residues give a rational function vanishing at infinity, with poles only at the roots of $D$ of at most their designated orders. Analytic continuation gives the assertion everywhere.

On the circle $|z-T|=2$, all roots of $D$ are at distance at least one, and Stirling and fixed-strip zeta growth give $|F(z)|\le\exp(-\eta T+C\log T)$. The maximum principle bounds $|F/D|$ by the same expression inside. The projector is $+1$ at the specified enclosed root $w$, whence
\[
                    |B(w)|\ge\exp(\eta T-C\log T).
\]
Fix any compact interval $J$ of positive length on which $\Xi$ has no zeros. Polynomial extrapolation gives
\[
 |B(w)|\le (C_J(1+T))^d\,\|B\|_{L^2(J)}.
\]
For instance expand in the orthonormal Legendre polynomials on $J$, use the three-term recurrence to bound each degree-$j$ polynomial at $w$ by $\sqrt{2j+1}(C_J(1+T))^j$, and apply Cauchy–Schwarz. On $J$, $|D|\le(C_J T)^d$ and $|F|$ is bounded below independently of the tilt. Consequently
\[
 \|\widehat f_\infty\|_{L^2(J)}
       \ge \exp(\eta T-C_J\log^2 T).
\]
The cutoff changes this norm by at most an absolute constant depending on $J$. It is negligible for the optimized tilt. Thus the projector has large Fourier amplitude even on a fixed interval disjoint from the chosen high zeros.

## Suppressing the negative gamma density and eliminating the poles

Let $\mu(t)=\Re\psi(1/4+it/2)-\log\pi$. Stirling gives fixed $R>1$ such that $\mu(t)\ge1$ for $|t|>R$. Put $I=[-R,R]$ and fix $J\subset[3R,4R]$ of positive length avoiding all real zeros, possible by discreteness. Polynomial extrapolation between these two fixed intervals yields $\|B\|_{L^2(I)}\le C_0^d\|B\|_{L^2(J)}$ by the same Legendre argument. Also $\sup_{J}|D|/\inf_I|D|\le ((T+5R)/(T-5R))^d$ for $T$ large, and $F$ is bounded on $I$ and bounded below on $J$. Using the absolute cutoff error and the previous lower bound on $J$ gives
\[
             \|\widehat f\|_{L^2(I)}\le C_1^{d+1}\|\widehat f\|_{L^2(J)} .
\]

Take $\tau=\pi/(2T)$, $k=\lceil C_2(d+1)\rceil$, and define
\[
 \widehat g(z)=b(z)\widehat f(z),\qquad
 b(z)=\sin(\tau z)^k[\cos(\tau z)-\cosh(\tau/2)].
\]
This finite sum of translations increases the support radius by at most $(k+1)\tau$ and annihilates both pole arguments. On $I$ and $J$ the absolute cosine difference is comparable to $\tau^2(t^2+1/4)$ with absolute constants for large $T$. In particular its maximum on $I$ divided by its minimum on $J$ stays bounded. The corresponding ratio for the absolute sine is at most $1/2$. Therefore
\[
 \|\widehat g\|_{L^2(I)}\le C_3 2^{-k}C_1^{d+1}\|\widehat g\|_{L^2(J)}.
\]
Choose $C_2$ sufficiently large compared to these fixed constants and $\sup_I|\mu|$. The full signed gamma integral then obeys $G(g)\ge (4\pi)^{-1}\|\widehat g\|_{L^2(J)}^2$. Since $\inf_J|b|\ge(c_J/T)^k c_J/T^2$ for large $T$, the lower bound on $J$ proves the stated bound for $G$.

On the full zero strip, $|b(z)|\le 4\cosh(\tau/2)^k\le5$ for large $T$. On the two disks $|z-T|<1$ one has $b(z)=-1+O(1/T+k/T^2)$ by Taylor expansion around $\tau T=\pi/2$. Thus the samples of $g$ equal minus the signed indicator of the clusters, up to an $\ell^2$ error at most $o(1)\sqrt{2m}+5\varepsilon$, where $\varepsilon$ is the chosen cutoff sample error. With $\varepsilon$ sufficiently small and $T$ large this is at most $\sqrt{2m}/8$. Conjugation permutes the zeros and changes the sign of the indicator. Expanding the Weil form and applying Cauchy–Schwarz gives $|W(g)+2m|\le 2m(2/8+1/64)$. This proves both sides of the signed comparison.
