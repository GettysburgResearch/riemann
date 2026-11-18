# A direct lower bound at the selected zero in the third Mertens mean problem

This proof supplies the oscillation step in the [resolution of Zhao's §8(1)](zhao-third-mertens-nov18.md) without importing Zhao's Lemma 10 or an assertion about all scales for an arbitrary specified zero. Only the particular minimizing ordinates and scales from (2) of that note are needed. The ingredients below are the ordinary explicit formula, the classical local zero count, and the power-sum inequality. All constants in this note may depend on the fixed widths $\eta,q$.

Use $F,u,\rho=1-d+i\gamma,b=\log\gamma$ as in that note, so $F=du+b=o(u)$, $du\ge0.45F$, and $F\gg\sqrt u$. Take $\eta=1/100$ and any fixed sufficiently small $q>0$, for example $q=10^{-6}$. Let
$$
 A(v)=\Pi(e^v)-\mathrm{lg}(e^v),\quad
 g(v)=\int_v^\infty A(w)e^{-w}dw,\quad
 \mathrm{lg}(x)=\sum_{2\le n\le x}1/\log n,
 \quad \Pi(x)=\sum_{p^k\le x}1/k
$$
for $v\ge0$. Thus $g'(v)=-e^{-v}A(v)$ almost everywhere. The classical PNT with its zero-free-region remainder gives bounded $g$ tending to zero and absolute convergence of its tail integral. Euler summation gives $\mathrm{lg}(x)-\mathrm{li}(x)=O(1)$, and $\Pi(x)-\pi(x)=O(\sqrt x\log x)$. Consequently Zhao's elementary partial summation identity (18) gives
$$
 J_1(e^v)/e^v=-g(v)+O((1+v)e^{-v/2}).
 \tag{1}
$$
Let $G_\tau(v)=(4\pi q\tau)^{-1/2}\exp(-(v-\tau)^2/(4q\tau))$.

## The signed Gaussian mean is exponentially small

Write $\mathcal L(z)=\int_0^\infty g(v)e^{-zv}dv$ for $\Re z>0$. For every smooth compactly supported $k$ on $(0,\infty)$ ordinary distributional integration by parts twice gives
$$
 \int k(v)e^{-v}\,d(\psi(e^v)-\lfloor e^v\rfloor)
   =-\int ((vk)''-(vk)')g(v)dv.
 \tag{2}
$$
Indeed $d(\psi(e^v)-\lfloor e^v\rfloor)=v\,dA(v)$ there, and $A=-e^v g'$. At $k(v)=e^{-zv}$ the endpoint calculation yields
$$
 [z(z+1)\mathcal L(z)]'=g(0)+1-\zeta(1+z)-\zeta'(1+z)/\zeta(1+z).
 \tag{3}
$$
Here the arithmetic sum starts at 2, $A=0$ near zero, and the second integration by parts contributes $-g(0)$ on the arithmetic side. The pole terms at $z=0$ cancel on the right. In $-1/4\le\Re z\le1/4$, $|\Im z|\le2$, there are no nontrivial zeros to cause another singularity. Since $z\mathcal L(z)\to0$ down the positive real axis, (3) gives holomorphic continuation throughout this rectangle, including zero.

Fourier inversion of the Gaussian expresses $\int_0^\infty g(v)G_\tau(v)dv$ by the vertical integral of $\mathcal L(z)\exp(\tau(z+qz^2))$ at $a=q/4$. The original transform is bounded on this line. Outside $|\Im z|\le2$ the Gaussian gives $O(e^{-c_q\tau})$. Move the bounded segment to $\Re z=-a$, using (3); the horizontal and left edges also give $O(e^{-c_q\tau})$ with some fixed $c_q>0$. Thus the signed mean is exponentially small uniformly for large $\tau$.

## The modulated source cannot cancel throughout the chosen interval

In this paragraph $\tau\in[(1+2\eta)u,(1+3\eta)u]$. Choose a smooth cutoff equal to one on $|v-\tau|\le\eta u/2$ and zero on $|v-\tau|\ge\eta u$, with first two derivatives $O_\eta(1/u)$ and $O_\eta(1/u^2)$. Denote it by $\chi_\tau$. Apply the distributional von Mangoldt formula away from the origin to $k(v)=\chi_\tau(v)G_\tau(v)e^{-i\gamma v}$ in (2). Up to sign the resulting arithmetic integral equals
$$
 \sum_{\rho'}\exp\{\tau(\lambda_{\rho'}+q\lambda_{\rho'}^2)\}
       +O(e^{-c u}),\qquad
 \lambda_{\rho'}=\Re\rho'-1+i(\Im\rho'-\gamma),
 \tag{4}
$$
where the sum includes multiplicities. To verify the uniform error, first replace the floor measure by the continuous $d(e^v)$: integration by parts against their bounded cumulative difference costs $O((1+\gamma)(1+u)^C e^{-u})$ on the support. The trivial zeros give $O(e^{-u})$ there. For each nontrivial zero, restore the discarded Gaussian tails on the entire real line. Their Fourier integral is $O(e^{-c u}(1+|\Im\rho'-\gamma|)^{-2})$, uniformly in $d'=1-\Re\rho'\in[0,1]$. Indeed multiplication by $e^{-d'v}$ shifts the Gaussian center to $\tau-2q\tau d'$ and multiplies its mass by $e^{-d'\tau+q\tau(d')^2}\le1$. The discarded region is still at distance $\gg\eta u$ from that center. The same Gaussian estimate holds for two derivatives of the discarded amplitude up to polynomial factors, so integrate by parts twice for frequency separation greater than one. Summing with the unit-interval zero count costs $O(\log(2+\gamma))$, absorbed since $b=o(u)$. Full-line Gaussian integration gives (4). The error exponent $c$ may shrink at successive occurrences.

Put $r=K\sqrt{F(u)/u}$ with a fixed $K$ large enough that $qK^2>100$. This tends to zero, while $r\ge d$ eventually. Retain the multiset with $|\Im\rho'-\gamma|\le r$ and $d'\le r$. All other terms in (4) have total absolute value $O(e^{-10F(u)})$. For the nearby ordinates with $d'>r$ use $-d'+q(d')^2\le-(1-q)r$ and $u r/F(u)\to\infty$. For $|\Im\rho'-\gamma|>r$ use the Gaussian $e^{-q\tau|\Im\rho'-\gamma|^2}$, first on the two adjacent unit intervals and then on the successive unit intervals, with their $O(\log(2+\gamma+j))$ zero counts. This also proves absolute convergence.

The retained number $n$ of terms satisfies $1\le n\ll 1+r\log(2+\gamma)=o(F(u))$. To see this, evaluate the real part of the completed logarithmic derivative at $1+r+i\gamma$. By the Euler series and Stirling the positive Poisson sum over all zeros is $O(1/r+\log(2+\gamma))$. Each retained term contributes $\gg1/r$, since its horizontal distance lies in $[r,2r]$ and its vertical distance is at most $r$. The target itself is retained.

For completeness choose $M=\lceil(1+2\eta)n/\eta\rceil$, $h=(1+2\eta)u/M$ and apply the Kolesnik–Straus power-sum inequality to the $n$ numbers $z_j=\exp(h(\lambda_j+q\lambda_j^2))$. It gives some $M<k\le M+n$ with
$$
 |\sum_j z_j^k|\ge e^{-C_\eta n}\max_j|z_j|^k .
$$
The discrete form is stated in [Thorner and Zaman, Theorem 5.2](https://arxiv.org/pdf/1604.01750). The exact factor in the Kolesnik–Straus theorem is $1.007(n/[4e(M+n)])^n$. It allows repeated terms and arbitrary separations. [Thorner and Zaman, Theorem 5.2](https://arxiv.org/pdf/1604.01750) Equivalently one can use the continuous power-sum form in Pintz, Acta Arith. 36 (1980), Appendix, Theorem 2, equation (18.9). The target has $\lambda=-d$, so at $\tau=kh$ the full arithmetic integral has magnitude at least $\exp(-(1+3\eta)du-o(F(u)))$. The omitted terms and (4)'s absolute error are negligible. [Pintz, On the remainder term of the prime number formula, I](https://matwbn.icm.edu.pl/ksiazki/aa/aa36/aa3644.pdf)

## Two signs on the original arithmetic mean

On the support of $k$, differentiating in (2) gives $|((vk)''-(vk)')|\ll_{q,\eta}u(1+\gamma)^2G_\tau(v)$. This uses $G_\tau'/G_\tau=-(v-\tau)/(2q\tau)$ bounded there, with the analogous bound for the second derivative. Thus the Gaussian mean of $|g|$ on $|v-\tau|\le\eta u$ is at least
$$
 \exp(-(1+3\eta)du-2b-o(F(u))).
$$
Here $\log u=o(F(u))$. The signed Gaussian mean on the same window is exponentially small by (3), since $g$ is bounded and the truncated tails cost $O(e^{-c u})$. Both positive and negative parts have at least half the absolute mean up to that negligible error. The interval therefore contains ordinary points of each sign at this scale, with $u\le v\le(1+4\eta)u$. Returning to (1), the same conclusion holds for $J_1(e^v)/e^v$ with its corresponding signs. By (2) of the companion note, the exponent spent is at most
$$
 (1+3\eta)du+2b+o(F(u))\le (2-0.97\cdot0.45+o(1))F(u)<1.57F(u).
$$
The quadratic term costs $O(e^v\exp(-1.96F(u))/v^2)$ by (4) of the companion proof, more than enough separation. This yields the claimed two signs of the *actual* product integral directly. It also explains why a possible small spacing or multiple zero cannot obstruct the selection: only the number of local terms enters the power-sum lower bound.
