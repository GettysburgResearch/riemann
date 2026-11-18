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

### A local collision under the de Bruijn–Newman heat flow

In the ordinate normalization $F_0(x)=\Xi(x)$, put $F_{-v}=e^{v\partial_x^2}\Xi$ for $v\ge0$. Let $m=(a+b)/2$, $h=(b-a)/2$ and $A=Q'(m)/Q(m)$. As $v$ increases from $0$ to $h^2$, the two indexed zeros in the moving disk $|x-m+2vA|<0.003$ undergo **exactly one collision**. Its backward time satisfies
$$
 .999\,h^2/2<v_*<1.001\,h^2/2,
 \qquad 1.026\cdot10^{-6}<v_*<1.030\cdot10^{-6}.
$$
Before the collision both zeros are simple and real. At $v_*$ there is one real zero of multiplicity two. Afterwards the roots form a simple nonreal conjugate pair. At $v=h^2$ each lies in the disk of radius $.003h$ about $m-2h^2A\pm ih$. In particular their imaginary parts have magnitude between $.997h$ and $1.003h$, where $h$ is about $0.001433907$. The collision ordinate is $3000175351972.082590\pm0.000004$. The final disks have common real center $3000175351972.0825943698701\pm10^{-13}$. This statement follows from the verified pair and the full-strip bound $B$ above, with no assumption on the more distant zeros. For the common normalization with initial function proportional to $\Xi(x/2)$, multiply the ordinates by two and the times by four.

To bound the heat convolution globally, let $E(z)=Q(m+z)e^{-Az}/Q(m)$. The genus-one product at $m$ gives $E(z)=\prod_{w\ne a,b}(1+u_w)e^{-u_w}$, with $u_w=z/(m-w)$ and $\sum |u_w|^2\le B|z|^2$. Each factor has modulus at most $e^{|u_w|^2/2}$ since $|1+u|^2\le e^{2\Re u+|u|^2}$. Integrating the derivative of $(1+u)e^{-u}$ on the segment from zero to $u$ gives $|(1+u)e^{-u}-1|\le |u|^2e^{|u|}/2$. Telescoping the product and using $\sqrt B|z|\le (1+B|z|^2)/2$ yields the global estimate
$$
 |E(z)-1|\le\tfrac12\sqrt e\, B|z|^2e^{B|z|^2}.
$$

Write $x=m+w-2vA$ and use a real Gaussian $U$ of variance $2v$. Completing the square in the Gaussian integral for $F_{-v}(x)$ shows that its zeros in this coordinate equal those of
$$
 G_v(w)=\mathbb E[((w+U)^2-h^2)E(w+U)] .
$$
The omitted factor is $Q(m)e^{A w-vA^2}$, which never vanishes. The Gaussian bounds justify differentiation and give $\partial_v G_v=G_v''$. Equivalently this convolution follows by multiplying each frequency in the Fourier representation of $\Xi$ by $e^{-v\omega^2}$. At $v=0$ the formulas use $U=0$.

For $|w|\le R$ define $D=1-8Bv$, $s^2=2v/D$ and $K=B\exp(1/2+2BR^2)/(2\sqrt D)$. For the times used here $D>0$. Then
$$
 |G_v(w)-(w^2+2v-h^2)|\le C_0+C_1 |w|^2,
 \quad C_0=K(3s^4+h^2s^2),\quad C_1=K(R^2+6s^2+h^2).
$$
Indeed $e^{B|w+U|^2}\le e^{2BR^2}e^{2BU^2}$, and tilting the Gaussian by the second factor changes its variance to $s^2$ and its total mass to $D^{-1/2}$. Its second and fourth absolute moments after translation by $w$ are bounded by $|w|^2+s^2$ and $|w|^4+6|w|^2s^2+3s^4$. The expressions increase with $v$ and $R$.

Take $R=.003$. On $|w|=R$ and $0\le v\le h^2$, the error is less than $R^2-h^2$. Rouché's theorem keeps exactly two zeros in the disk and the function is strictly positive at its real endpoints. Cauchy's inequality on radii $R$ applied to the error on $|w|\le2R$ gives $|G_v''(w)-2|<.1$ for $|w|\le R$. On the real diameter the function is therefore strictly convex and increases with $v$ with derivative greater than $1.9$. The minimum on that fixed diameter is continuous and also increases at least this quickly. At $v=.999h^2/2$ the value at $w=0$ is negative since $C_0<.001 h^2$. At $v=1.001h^2/2$ all real values are positive since $C_0<.001 h^2$ and $C_1<1$. At the unique zero of the minimum the endpoints remain strictly positive, so the minimum occurs in the interior and is a double zero. Strict convexity and the conserved two-zero count give the claimed transition. Finally at $v=h^2$, on $|w\mp ih|=.003h$, the lower bound for the quadratic is $.003(2-.003)h^2$ and exceeds the error bound with $R=1.003h$. Each small disk therefore contains exactly one simple zero. The numerical inequalities use directed ball arithmetic in [the same verifier](check_lehmer_pair.py).

For the displayed real coordinates the scalar logarithmic derivative enclosure in the preceding section gives $A=-\Im(G(m_s)+E(m_s))=-1.55979826\pm3\cdot10^{-9}$, writing $m_s=1/2+im$ and using $G,E$ there in their logarithmic-derivative notation. To enclose the collision ordinate, Cauchy on $|w|=R$ bounds $|G_v'(0)|$ by $(C_0+C_1R^2)/R$ since the quadratic has derivative zero at the origin. Dividing by the proved lower curvature bounds the distance from the origin to the collision minimum. The physical ordinate adds $m-2vA$.


The same estimates give a local criterion for any real entire function of Hadamard genus at most one with two simple real zeros $m\pm h$: if the sum $B$ of absolute inverse-square distances from $m$ to the other zeros, counted with multiplicity, satisfies $Bh^2\le1/4000$, these two zeros have a unique collision in the moving disk of radius $2h$ at $.999h^2/2<v<1.001h^2/2$ and lie within $.003h$ of the stated conjugate centers at $v=h^2$. Indeed rescale $h$ to one, replace $B$ by $1/4000$ in the same monotone error bounds, and use $R=2$. The error on the outer circle is below $.017$, the uniform curvature error is below $.050$, and at $v=1.001/2$ the constant and quadratic error coefficients are below $.000830$ and $.00228$. On the final two small circles the error is below $.00582$, while the quadratic has modulus at least $.005991$. The real Gaussian convolution exists because the global product bound has quadratic type small enough at all the stated times.

### An independently enclosed double root

A second calculation, evaluating the completed zeta function on a complex circle, encloses the unique collision more tightly:
$$
 \begin{aligned}
 v_* &=1.0281241341155220688976\cdot10^{-6}\ \pm10^{-28},\\
 x_* &=3000175351972.0825911632211648425075631\ \pm10^{-25}.
 \end{aligned}
$$
Here $x_*$ is the common real ordinate at heat time $-v_*$ in the $\Xi$ normalization. [Independent scalar heat replay](check_heat_collision.py)

Set $x_0=3000175351972.08258795570117635$, $d_0=.001434$ and $f(z)=-\Xi(x_0+d_0z)/\Xi(x_0)$. The preceding root enclosures give $|x_0-m|<2\cdot10^{-15}$ and $.999<h/d_0<1.001$. The pair-removed estimates give $|A|<1.57$ and $B<81.436$. Substitution in the quadratic factor and the bound $|E(z)|\le e^{B|z|^2/2}$ yields
$$
 |f(z)|\le 2(2+r)^2e^{.003r+.0001r^2}\le 10000e^{.001r^2},\qquad r=|z|.
$$
For the denominator use $|E(x_0-m)-1|<.01$. For the final inequality use $.003r\le.0225+.0001r^2$ and $(2+r)^2\le8+2r^2\le(8+2/(.0008e))e^{.0008r^2}$.

Write $f(z)=\sum c_n z^n$. The checker evaluates $f$ at the 48 equally spaced points of $|z|=8$, using conjugation symmetry and interval evaluations of $\zeta$ and $\log\Gamma$. The discrete Fourier coefficient divided by $8^n$ equals $c_n+\sum_{j\ge1}c_{n+48j}8^{48j}$. By the outer circle $|z|=128$ the error is at most $10000e^{.001(128)^2}16^{-48}/(8^n(1-16^{-48}))$.

Put $C(\nu,z)=\mathbb E[f(z+\sqrt{2\nu}N)]$, with $N$ standard real normal, so the physical coordinates are $v=d_0^2\nu$ and $x=x_0+d_0z$. For $|z|\le2$ and $0<\nu<.51$ the Gaussian absolute-moment norm $\|z+\sqrt{2\nu}N\|_n\le 2+\sqrt{1.02n}\le1.30\sqrt n$ for $n\ge48$. Cauchy optimized at $r=\sqrt{n/.002}$ gives $|c_n|\le10000(.002e/n)^{n/2}$. Consequently the discarded terms of $C$ have modulus at most $10000(.097)^{48}/(1-.097)$, uniformly in that disk. For $|z|<.1$ the $j$th $z$ derivative of the tail is bounded by $j!$ times the same number by Cauchy on radius one. The retained terms use the exact heat moments $p_0=1$, $p_1=z$, $p_{k+1}=zp_k+2\nu k p_{k-1}$.

After ordinary Newton iteration chooses a numerical center, the checker applies the contraction $(\nu,z)\mapsto(\nu-C/2,z-C_z/2)$ on the closed real square of radius $10^{-23}$ about that center. Since $C_\nu=C_{zz}$, its two Jacobian row sums are bounded explicitly by $|1-C_{zz}/2|+|C_z|/2$ and $|C_{zzz}|/2+|1-C_{zz}/2|$. Both are below $.007$. The center residual plus this Lipschitz bound times the radius is less than the radius. The resulting common zero of $C,C_z$ lies inside the previously proved disk and time interval and hence is the unique collision already identified.
