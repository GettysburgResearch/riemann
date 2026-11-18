# A strong Lehmer-pair inequality above the previous verified height

The consecutive simple zeros with global positive indices $12\,363\,153\,519\,193$ and $12\,363\,153\,519\,194$ have ordinates
$$
 a=3000175351972.0811540487070886\ \pm10^{-15},\qquad
 b=3000175351972.0840218626952641\ \pm10^{-15}.
$$
On this pair Stopple's strong Lehmer differential statistic is **less than $8.057$**, below the threshold $42/5$. The absolute inverse-square statistic summed over *all* the other complex zeros of $\Xi(z)=\xi(1/2+iz)$ is less than $0.00134$. These two bounds hold without assuming RH. Under the customary RH hypothesis in the real-zero definition, this is in particular a strong Lehmer pair. Its normalized spacing is about $0.0123$ of the local mean. No global spacing or de Bruijn–Newman bound record is claimed. [Directed verifier](check_lehmer_pair.py) · [Lehmer criteria and Stopple's differential statistic](https://arxiv.org/abs/1612.08627)

Let $d=b-a$, $r=3/2$, $s=2+it$, and $z=t-ir$ for $a\le t\le b$. Each nontrivial zero $\rho=\beta+i\gamma$ corresponds to $w_\rho=\gamma+i(1/2-\beta)$. The logarithmic derivative of the Hadamard product of $\xi$ and its functional equation give the Poisson mass identity
$$
 P(t)=\Re\frac{\xi'}{\xi}(2+it)=
 \sum_\rho\frac{2-\beta}{(2-\beta)^2+(t-\gamma)^2}.
$$
In particular $\sum_\rho |z-w_\rho|^{-2}\le P(t)$. To evaluate an upper bound, use
$$
 \frac{\xi'}{\xi}(s)=E(s)+\frac{\zeta'}{\zeta}(s),\qquad
 E(s)=1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\psi(s/2).
$$
The Euler product gives $|\zeta'/\zeta(2+it)|\le\sum_{n\ge2}\log n/n^2<2$, by integral comparison (separate $n=2$). The real and imaginary parts of the elementary digamma expression are interval-evaluated for the entire enclosing $t$ interval, giving $P(t)<15.446$ and $|\Re (i\xi'/\xi)(s)|\le|\Im E(s)|+2$.

The verifier takes the twelve certified neighboring indices on either side from [block 0008](blocks/0008.json). It sums the maximum inverse squares of their distances to $[a,b]$. All remaining zeros outside these 26 indices have ordinates separated from $[a,b]$ by at least $R$, using the outermost known neighbors. For those zeros,
$$
 |t-w_\rho|^{-2}\le(1+4/R^2)
 \frac{2-\beta}{(2-\beta)^2+(t-\gamma)^2}.
$$
The full censused prefix ensures there are no additional off-line zeros with intervening ordinates. Negative ordinates and zeros beyond the verified height are covered by this same bound. For every $a\le t\le b$ the resulting total $\sum_{w\ne a,b}|t-w|^{-2}\le B<81.436$ proves the stated absolute statistic $<2d^2B$.

For the strong statistic put $Q(z)=\Xi(z)/((z-a)(z-b))$ and $u=Q'/Q$. The genus-one product gives $|u'(t)|\le B$. At either endpoint $t=a,b$, the known pair terms in $\Re u(t-ir)$ have magnitude in sum at most $d/r^2$, since the contribution directly above its own endpoint has zero real part. The difference of the logarithmic derivatives at $t$ and $z=t-ir$ is an absolutely convergent sum over the other zeros. By Cauchy–Schwarz and reality of $u(t)$,
$$
 |u(t)|\le |\Im E(2+it)|+2+d/r^2+r\sqrt{B P(t)}=:L_t .
$$
Take the uniform upper bound $L$ from this expression. Writing $\mathcal P\Xi'=(\Xi''/\Xi')'$ in the convention of Stopple's criterion, the factorization at a simple root gives
$$
 -\mathcal P\Xi'(a)
 =3\sum_{w\ne a}(a-w)^{-2}+(u(a)-1/d)^2
$$
and similarly at $b$, with $u(b)+1/d$. The cross terms in the two squares sum after scaling to $2d(u(b)-u(a))$, bounded by $2d^2B$. Thus
$$
 -d^2\big(\mathcal P\Xi'(a)+\mathcal P\Xi'(b)\big)
 \le 8+d^2(8B+2L^2)<8.057 .
$$
This controls the contribution from the unverified high ordinates through their entire Poisson mass. Four independent scalar Hardy-sign evaluations certify the two fine enclosures inside their archived globally indexed brackets.

### A nearby simple zero of the derivative of zeta

The pair produces a unique zero of $\zeta'$ in the disk of radius $10^{-4}$ about $m=1/2+i(a+b)/2$. Its location is within $2.3\cdot10^{-15}$ (absolute complex distance) of
$$
 0.500013823730388624+3000175351972.082587159392354416\,i .
$$
This conclusion also holds unconditionally.

Put $h_0=(b-a)/2$, $z=s-m$, $p(z)=z^2+h_0^2$, and write $G(s)=(\log(\zeta(s)/p(s-m)))'$. In the disk $|z|\le R_0=10^{-4}$ the quotient is analytic and nonzero. For $d_0$ the minimum distance to the outer neighboring brackets, the product bound gives
$$
 |G'|\le B/(1-R_0/d_0)^2+1=:D .
$$
The added one bounds $|E'|$ there: in the positive right half-plane $|\psi'(v+iy)|\le 1/y^2+\pi/(2|y|)$ by its series and integral comparison, and the reciprocal-square terms from $1/s$ and $1/(s-1)$ are smaller than $10^{-23}$. At $m$ the logarithmic derivative of the pair-removed completed function is purely imaginary, of magnitude at most $L+dB/2$. Thus $|G|\le G_0=L+dB/2+|E(m)|+R_0D$ in the disk. The roots of $\zeta'$ there solve $2z+p(z)G(m+z)=0$. The verifier gives $G_0(R_0^2+h_0^2)/2<7.19\cdot10^{-5}<R_0$. Rouché's theorem gives exactly one root, hence simplicity. Independently its real offset differs from $h_0^2\Re E(m)/2$ by at most $(D R_1h_0^2+G_0R_1^2)/2$, where $R_1=G_0(R_0^2+h_0^2)/2$.

For the final precision use the fixed-point map $J(z)=-p(z)G(m+z)/2$. Its derivative in the disk has modulus at most $q=R_0G_0+(R_0^2+h_0^2)D/2<0.01$. At an exact scalar trial $s=m+z$ evaluate
$$
 D_\epsilon(s)=\epsilon^{-1}\log\left(\frac{\zeta(s+\epsilon)}{\zeta(s)}
   \left(1+\frac{2z\epsilon+\epsilon^2}{p(z)}\right)^{-1}\right),
 \qquad \epsilon=2^{-38}.
$$
The logarithm is the principal branch because $\epsilon G_0<\pi$. This expression averages $G$ on the short segment and differs from $G(s)$ by at most $\epsilon D/2$. The trial's distance to the unique zero is bounded by $|z-J(z)|/(1-q)$, evaluated with the original uncertain $a,b$. Iterating with enclosure midpoints leaves a residual bound below $2.20\cdot10^{-15}$ before rounding the displayed center. This computation uses only scalar evaluations of $\zeta$ and the proven local derivative bounds.
