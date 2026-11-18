# A single degree detects the rightmost zero exponent

**Status.** Proposed unconditional exponent identity and finite arithmetic reduction for the complete odd Möbius source. The bound needed on an unbounded sequence of actual columns remains open.

Let $m(x)=\sum_{n\le x,\ n\text{ odd}}\mu(n)/n$, zero below one, $Z(s)=(1-2^{-s})\zeta(s)$, $\phi_j=\sqrt{4j+3}P_{2j+1}$, and
$$
 u_j(t)=\int_0^1 m(t/v)\phi_j(v)\,dv/v,\qquad t>0.
$$
The output restricted to $(1,3)$ is precisely $K\phi_j$ from [#866, DG26](https://github.com/GettysburgResearch/riemann/blob/a27285abe428835ac0171fe9eb8cbbc97a64a33a/standalone/2026-09-12-astra-polynomial-degree-growth/PROOF.md). Put $\Theta=\sup_\rho\Re\rho$, counting all nontrivial zeta zeros. The prefix trace and operator exponents were obtained in [#869, arithmetic §4](https://github.com/GettysburgResearch/riemann/blob/5e559c9cbf5aee84ff7ed78dc91b55df744aef56/standalone/2026-09-12-three-route-completion/arithmetic/PROOF.md). Here the energy uses one individual degree.

For **every** fixed interval of positive length $I\subset(1,3)$,
$$
 \lim_{j\to\infty}\frac{\log(1+j\int_I|u_j(t)|^2dt)}{\log j}
        =2\Theta-1.
\tag{1}
$$
The result also holds when $I=I_j\subset(1,3)$ may move with $j$, provided its logarithmic width $h_j=\log(\sup I_j/\inf I_j)$ satisfies $\log^+(1/h_j)=o(\log\log j)$. For example one can use width $1/\log\log j$. In particular an upper bound $j\int_{I_j}|u_j|^2\le j^{o(1)}$ on *any one* unbounded sequence of degrees suffices to prove RH, and under RH it holds at every large degree. No sum over a growing family of other columns is required.

## A sharp input multiplier upper bound

Write $J=j+3/4$ and
$$
 c_j(z)=\int_0^1\phi_j(v)v^{z-1}dv
  =(-1)^j A(z)\sqrt J
    \frac{\Gamma(j+1-z/2)}{\Gamma(j+(z+3)/2)},\qquad
 A(z)=\frac{\Gamma((1+z)/2)}{\Gamma(1-z/2)} .
\tag{2}
$$
This is the rational DG26 formula (3.2) written in gamma notation, valid away from removable presentation singularities for $\Re z>-1$. For $0\le q\le1/2$,
$$
 \sup_{v\in\mathbb R}|c_j(q+iv)|=|c_j(q)|\asymp_q (j+1)^{-q}.
\tag{3}
$$
In fact for $0<a\le b$ the modulus of $\Gamma(a+it)/\Gamma(b+it)$ is nonincreasing for $t\ge0$, as seen by taking the logarithmic derivative of the Weierstrass product (the derivative terms are $-t/((n+a)^2+t^2)+t/((n+b)^2+t^2)\le0$). Both ratios in (2) have this ordering of real parts, and conjugation handles the opposite imaginary signs. The value at zero frequency follows by Stirling, uniformly for $q$ in compact subintervals of $[0,1/2]$.

Thus Mellin Plancherel for the convolution with $\phi_j(v)\mathbf 1_{(0,1)}(v)$ gives the unconditional norm implication
$$
 \int_0^\infty |u_j(t)|^2t^{2q-1}dt
 \le |c_j(q)|^2\int_1^\infty |m(t)|^2t^{2q-1}dt,
\tag{4}
$$
whenever the right side is finite. It is finite at $q=0$ by the classical quantitative PNT. If $\Theta<1$, the generalized Littlewood estimate for the ordinary Möbius sum and partial summation as in #869 give $m(x)\ll_\delta x^{\Theta-1+\delta}$ for each $0<\delta<1-\Theta$. This pays (4) at every $q<1-\Theta$. Since $t^{2q-1}$ is bounded away from zero on $[1,3]$, (4) gives the upper half of (1) for all $\Theta$, including $\Theta=1$. Under the weak Mertens hypothesis [the continuous energy adapter](trace-weak-mertens-nov18.md) gives $\int_1^X m^2\ll\log(2X)$. Integration by parts then pays (4) at $q=1/2-1/\log j$ with right-hand input energy $O(\log j)$. Hence $\int_1^3 |u_j|^2\ll (\log j)/j$ at each sufficiently large degree.

## Isolating a pole using only the output coordinate

Suppose $\rho=\beta+i\gamma$ with $\beta>1/2$ is a zero of multiplicity $m_\rho$. Choose $1/2<\alpha_0<\alpha<\beta$, taking $\alpha$ a positive distance at least $c(1+|\Im\rho'|)^{-3}$ from the real part of every nontrivial zero $\rho'$. Such a choice in any prescribed interior subinterval follows by excluding intervals of that radius with sufficiently small $c$, using the classical global zero count. Put $s_0=\rho-1$. By Ingham's density theorem the zeros with $\Re\rho'>\alpha_0$ up to height $T$ number $O(T^k)$ for some $k<1$ counting multiplicities: any $k>3(1-\alpha_0)/(2-\alpha_0)$ suffices. Build the genus-zero product
$$
 P(s)=\prod_{\substack{\Re\rho'>\alpha_0\\\rho'\ne\rho}}
 \left(1-\frac{s}{\rho'-1}\right)^{m_{\rho'}},
$$
where the product is over distinct zeros and includes the target's conjugate. Its convergence is absolute on compact sets, $P(s_0)\ne0$, and $|P(s)|\le \exp(C(1+|s|)^k)$, by integrating the count against the derivative of $\log(1+|s|/u)$. Complex output tests are allowed, so the target need not be paired with its conjugate. This use of sparse-spectrum isolation is related to [the detector construction](detector-positive-isolation-nov18.md).

Choose $k<d<1$ and $a_n=c_d n^{-1/d}$ with $\sum a_n=1$. The entire transform $J_0(z)=\prod_{n\ge1}\sinh(a_nz)/(a_nz)$ has exponential type at most one and $J_0(0)=1$. On each bounded real strip its modulus is $O(e^{-c|\Im z|^d})$: each factor is bounded by $e^{a_n|\Re z|}\min(1,1/(a_n|z|))$ and the first $\gg |z|^d$ factors have the latter term at most $1/2$. Let $0<h\le1$ and choose the center $v_0$ so $[v_0-h,v_0+h]\subset \log I$. Then
$$
 H_h(s)=e^{v_0s} P(s) J_0(h(s-s_0))
       =\int_I \eta_h(t)t^s\,dt
\tag{5}
$$
for a smooth complex $\eta_h$ supported in $I$. Indeed the shifted transform without $e^{v_0s}$ has exponential type at most $h$, since $P$ has order less than one. It decays faster than any inverse power on the imaginary axis. The classical $L^2$ Paley–Wiener theorem and Fourier inversion give a smooth inverse supported on $[-h,h]$ in the log variable, and translation and $dt/t$ give (5). Uniformly for bounded $v_0$,
$$
 \|\eta_h\|_2+\int_{\Re s=\alpha-1}
 |H_h(s)|\exp(C_1\log^2(2+|\Im s|))\,|ds|
     \le \exp(C_2(1+h^{-dk/(d-k)})).
\tag{6}
$$
For any fixed $C_1$ this follows by bounding the transform with $\exp(C'(1+|\Im s|)^k-c h^d|\Im s|^d)$ and absorbing the squared logarithm; integration or Fourier inversion leaves the displayed dependence. The value $H_h(s_0)=e^{v_0s_0}P(s_0)$ stays bounded away from zero, and its fixed-order derivatives there stay bounded for $0<h\le1$.

For $0<c<1$ one has the exact equality
$$
 \int_I \eta_h(t)u_j(t)\,dt
 =\frac1{2\pi i}\int_{\Re s=c}
     \frac{H_h(s)c_j(-s)}{sZ(1+s)}\,ds .
\tag{7}
$$
To check interchanges, the primitive $p(w)=\int_w^\infty\eta_h(t)dt$ has Mellin transform $H_h(s)/s$ in $\Re s>0$. Inserting its inverse for $p(nv)$ in the original arithmetic sum uses $\sum n^{-1-c}<\infty$ and $\int_0^1 |\phi_j(v)|v^{-c-1}dv<\infty$ since $\phi_j$ vanishes linearly at the origin. The smooth Mellin transform pays absolute integration in ordinate.

Shift (7) to $\Re s=\alpha-1$. All competing poles are removed by (5), $s=0$ is removable, and the zeros of $1-2^{-1-s}$ lie strictly left of this strip. On the selected vertical line the reciprocal $1/\zeta(1+s)$ is at most $\exp(C\log^2(2+|\Im s|))$. This follows by integrating the classical local partial-fraction formula for $\zeta'/\zeta$ horizontally from $\Re(1+s)=2$, with the local singular logarithms first subtracted, and using the defining polynomial separation of $\alpha$ from all zero real parts. Cofinal horizontal lines separated by $\gg1/\log(2+T)$ from all zero ordinates have the same bound across the strip. See the cited detector construction §3 for the full argument. On those horizontals $c_j(-s)$ is a rational function of $s$ at fixed $j$. For the remaining vertical line use (3) at $q=1-\alpha$. Thus the shifted integral is $O(j^{\alpha-1}\exp(C(1+h^{-dk/(d-k)})))$ by (6).

Near fixed $s_0$, (2) gives $c_j(-s)=(-1)^j j^s(A(-s)+O(1/j))$ locally uniformly, with derivative control for the coefficient in parentheses by Cauchy's formula. The pole contributes
$$
 (-1)^j j^{s_0}(\log j)^{m_\rho-1}
 \left[\frac{H_h(s_0)A(-s_0)m_\rho!}
 {(m_\rho-1)!s_0 Z^{(m_\rho)}(\rho)}+o(1)\right],
$$
uniformly over these $h,v_0$; the leading coefficient has modulus bounded below. For fixed $I,h$ this gives
$$
 \int_I |u_j|^2\,dt\gg_{\rho,I}
       j^{2\beta-2}(\log j)^{2m_\rho-2}
 \quad\text{at every sufficiently large }j .
$$
For the moving intervals use $h=\min(h_j/3,1/4)$ with center at the logarithmic midpoint. Then $\exp(C(1+h^{-dk/(d-k)}))=j^{o(1)}$. The error stays smaller than the residue, and Cauchy–Schwarz costs only $j^{o(1)}$, giving $j\int_{I_j}|u_j|^2\ge j^{2\beta-1-o(1)}$. Taking the supremum over all right-of-line zeros proves the lower half of (1), with nonnegativity sufficient if $\Theta=1/2$. For widths $h_j\asymp(\log j)^{-a}$ with fixed $a>0$ the same proof detects every $\beta>(1+3a)/(2+3a)$: take $\alpha_0$ close to $\beta$, then $k$ close to the Ingham exponent and $d$ close to one, so $a<1/k-1/d$.

## An unconditional approximation at finer than the critical scale

Define $\operatorname{Si}(v)=\int_0^v\sin u\,du/u$ and
$$
 V(X)=\frac2{\sqrt\pi}\sum_{n\ge1,\,n\text{ odd}}
                      \frac{\mu(n)}n\operatorname{Si}(2X/n).
$$
The series converges absolutely at each $X>0$. Then uniformly in degree,
$$
 \left(\int_0^\infty
  |u_j(t)-(-1)^j V(Jt)|^2\,\frac{dt}{t}\right)^{1/2}
      \ll (j+1)^{-2/3}\log(2+j).
\tag{8}
$$
Thus the approximation preserves even a critical $j^{-1/2}$ column norm on any output subinterval of $[1,3]$.

For the positive-exponent Mellin convention, the multiplier of convolution with $(2/\sqrt\pi)\sin(2v)$ is
$$
 (2^{1-z}/\sqrt\pi)\Gamma(z)\sin(\pi z/2)=A(z)
$$
on $\Re z=0$, by reflection and duplication. For a precise $L^2$ realization first insert $e^{-\delta v}$ with $0<\delta<1$. The multiplier is $\Gamma(z)((\delta-2i)^{-z}-(\delta+2i)^{-z})/(i\sqrt\pi)$ by analytic continuation from $\Re z>0$. On $z=i\tau$ it is $O((1+|\tau|)^{-1/2})$ uniformly by Stirling and the removable limit near zero. The regularized convolution with $m$ tends pointwise to $V(X)$, since $m(X/v)$ vanishes at $v>X$ and Fubini near zero is justified by the convergent sum $\sum n^{-2}$ after integrating the small arguments. Mellin Plancherel and dominated convergence give $\widehat V(\tau)=A(i\tau)\widehat m(\tau)$. On the same axis, the quantitative PNT and the Euler product continued from the right give
$$
 |\widehat m(\tau)|=|1/[(-i\tau)Z(1-i\tau)]|
       \ll \log(2+|\tau|)/(1+|\tau|)
$$
by the classical bound $1/\zeta(1+it)\ll\log(2+|t|)$ at large $|t|$. At zero the expression is removable.

The centered gamma ratio in (2) has arguments $J+a,J+1-a$ where $a=1/4-z/2$. For $|\tau|\le c J^{2/3}$, integrate $\psi(J+w)=\log J+(w-1/2)/J+O((1+|w|)^2/J^2)$ along the segment between $1-a$ and $a$. This digamma expansion is uniform by Stirling since $|w|\ll J^{2/3}$, and the integral of the linear term vanishes by symmetry. Exponentiation gives relative error $O((1+|\tau|)^3/J^2)$ against $J^{2a-1}$ for sufficiently small absolute $c$. At any $\tau$, the large-$J$ gamma ratio in (2) has modulus bounded by its value at zero frequency, and $|A(i\tau)|\ll(1+|\tau|)^{-1/2}$. Consequently
$$
 |c_j(i\tau)-(-1)^j J^{-i\tau} A(i\tau)|
 \ll (1+|\tau|)^{-1/2}\min(1,(1+|\tau|)^3/J^2).
$$
Square, multiply by $|\widehat m(\tau)|^2$, split at $|\tau|=J^{2/3}$ and integrate. Both parts cost $O(J^{-4/3}\log^2(2J))$. This proves (8).

## A finite arithmetic band on selected degrees

For $M=\lfloor j^{2/3}\rfloor$, $K=\lceil j^{3/2}\rceil$ and $x\in[J,3J]$, define
$$
 V_{M,K}(x)=\frac2{\sqrt\pi}
          \sum_{M<n\le K,\,n\text{ odd}}\frac{\mu(n)}n\operatorname{Si}(2x/n).
$$
At every degree where $|m(M)|\le1/M$,
$$
 \|V-V_{M,K}\|_{L^2(J,3J)}=O(1)
\tag{9}
$$
with an absolute constant. Such degrees form an unbounded set. Consequently RH is equivalent to a subpower bound $\int_J^{3J}|V_{M,K}(x)|^2dx\le j^{o(1)}$ on any one unbounded sequence *from this stated set*. Under RH it holds on all such degrees. For general degrees retain the explicit constant $(\pi/\sqrt\pi)m(M)$ in the band approximation.

To prove (9), first center the small terms by subtracting $\pi/2$ from $\operatorname{Si}$. Uniformly for $x\in[J,3J]$, integration by parts in the sine tail gives
$$
 \sum_{n\le M,\,n\text{ odd}}\frac{\mu(n)}n
      [\operatorname{Si}(2x/n)-\pi/2]
   =-\frac1{2x}\sum_{n\le M,\,n\text{ odd}}\mu(n)\cos(2x/n)
       +O(M^2/J^2).
$$
For arbitrary coefficients $a_n$ at $n\le M$, a fixed nonnegative smooth majorant of the interval $[1,3]$ and its Fourier decay show
$$
 \int_J^{3J}\left|\sum_{n\le M}a_n e^{2ix/n}\right|^2dx
        \ll (J+M^2)\sum_{n\le M}|a_n|^2.
$$
Indeed the weighted Gram entries are bounded by $C J(1+J|n-m|/M^2)^{-2}$, whose row sums have the displayed bound. Applying this to both cosine directions shows that the centered small sector has squared norm $O(M/J+M^3/J^2+M^4/J^3)=O(1)$. Its constant piece costs $O(\sqrt J|m(M)|)$ in norm. The large terms $n>K$ cost $O(J/K)$ pointwise by $|\operatorname{Si}(2x/n)|\ll x/n$, so their squared norm is $O(J^3/K^2)=O(1)$.

Finally $m(M)$ changes sign infinitely often. If it were eventually of one sign, its nonnegative signed tail would have a real singularity of its Laplace transform at the abscissa of convergence by Landau's theorem. Its transform in the variable $\log x$ is $1/[s Z(1+s)]$ up to a harmless entire finite prefix and sign. It has a pole at a shifted critical zero, so that abscissa would be at least $-1/2$; the PNT gives at most zero. Yet the transform is holomorphic at every real $s\in[-1/2,0]$ (including the removable value at zero). This contradiction proves the sign changes. At their integer crossings the jump has modulus at most $1/M$, yielding unbounded $M$ with $|m(M)|\le1/M$. Every sufficiently large integer $M$ occurs as $\lfloor j^{2/3}\rfloor$ because consecutive values of $j^{2/3}$ differ by less than one. Combining (8), (9) and (1) proves the criterion.

**Remaining estimate.** The comparisons bound the discarded sectors and the approximation error for the complete arithmetic source. They leave the signed middle-band energy on an unbounded sequence open. A finite small band energy is only one instance of the required sequence.

## Removing both outer sectors at every degree

Fix an interval $I$ of positive length in $(1,3)$ and $0\le a<1$. Take $K=\lfloor J/(\log J)^a\rfloor$, $M=\lfloor j^{2/3}\rfloor$, and take $D$ the nearest larger odd integer to $2\log J/((1-a)\log\log J)$. Let $\Pi_D$ be the orthogonal projection in $L^2(I,dt)$ onto the orthogonal complement of $1,t,t^3,\ldots,t^D$. Set
$$
 B_j(t)=\frac2{\sqrt\pi}\sum_{M<n\le K,\ n\text{ odd}}
   \frac{\mu(n)}n\operatorname{Si}(2Jt/n).
$$
Then the exponent identity holds on this finite projected band:
$$
 \lim_{j\to\infty}\frac{\log(1+j\|\Pi_D B_j\|_2^2)}{\log j}
     =2\Theta-1 .
\tag{10}
$$
In particular a subpower bound on $j\|B_j\|_2^2$ on any unbounded sequence suffices for RH. The two-way criterion uses $\Pi_D B_j$. The degrees may be chosen without knowledge of sign changes of $m$.

Indeed the constant small-sector term disappears under projection. The rest of the small sector costs $O(J^{-1/2})$ in $L^2(I,dt)$ by the previous Gram estimate. For $n>K$ subtract the odd Taylor polynomial of $\operatorname{Si}(2Jt/n)$ of degree $D$. Taylor's theorem for the sine and integration bound its error by $(6J/n)^{D+2}/(D+2)!$ on $I$. Summing with the factor $1/n$ costs at most $(6J/K)^{D+2}/(D+2)!$, by integral comparison. This is $J^{-2+o(1)}$ by Stirling. The subtracted series of polynomials converges coefficientwise. Consequently (8) gives
$$
 \|\Pi_D B_j-(-1)^j\Pi_D u_j\|_2\ll J^{-1/2}.
$$
This proves the upper exponent by contraction and (4).

For the lower exponent fix an off-line zero as in (5), keep $h>0$ fixed, and multiply its $H_h(s)$ by
$$
 F_D(s)=\frac{s}{s_0}\prod_{1\le b\le D,\ b\text{ odd}}
                 \frac{1-s/b}{1-s_0/b}.
$$
This preserves the value at $s_0$, annihilates every subtracted monomial (including the constant), and preserves the support by Paley–Wiener. The test at each $j$ therefore pairs equally with $u_j$ and $\Pi_D u_j$. Fixed derivatives of $F_D$ at $s_0$ are $O_r((1+\log D)^r)$ by logarithmic differentiation. Thus the lower Laurent terms in the contour shift are still relatively $o(1)$ against the highest power of $\log j$.

Write $L=(D+1)/2$. For $s$ in a fixed vertical strip and $T=2+|\Im s|$, the product obeys
$$
 |F_D(s)|\le C T \exp(O(L))(1+T/L)^L .
$$
Here the normalizing denominator contributes at most a fixed power of $D$ by the harmonic sum, and the numerator is bounded by $(C(T+L))^L/L!$. Multiplying this estimate by $\exp(-cT^d)$ from (5) shows that the norm of the modified test and its weighted shifted-contour integral in (6) are both at most
$$
 \exp\big((1/d-1)L\log L+O_d(L)\big).
$$
For $T\le L$ the bound follows directly, and for $T>L$ maximize $L\log(T/L)-c'T^d$. The remaining fraction of $cT^d$ absorbs the order-$k$ product, squared logarithm and integration. Since $L\log L\sim \log J/(1-a)$, for every prescribed $\varepsilon>0$ we can choose $k<d<1$ sufficiently close to one that both costs are $O(j^\varepsilon)$. With $\varepsilon<\beta-\alpha$ the shifted integral remains negligible. Cauchy–Schwarz now gives $\|\Pi_D u_j\|_2\gg j^{\beta-1-\varepsilon}$ at every sufficiently large $j$. Also taking $\varepsilon<\beta-1/2$ absorbs the comparison error. Letting $\varepsilon$ decrease to zero and taking the supremum over off-line zeros proves (10).

## Both signs of the actual columns

Suppose $1/2<b<\beta_0=\Re\rho_0$. Put $S_b^*=\sum_{\Re\rho>b,\Im\rho>0}\pi/\Im\rho$, now **with multiplicity**, finite by Ingham. If the log width of any positive output interval $I$ exceeds $S_b^*$, then at every sufficiently large $j$ the positive and negative parts of $u_j$ both have $L^1(I,dt)$ norm $\gg j^{\beta_0-1}$. The implicit constant and starting index depend on $I$ and the zero. For an unattained $\Theta$, $S_b^*\to0$ as $b\uparrow\Theta$; in that case for every fixed interval $I$ of positive length in $(1,3)$ and every $1/2<c<\Theta$, both signs have mass $\gg j^{c-1}$ at every large degree.

Indeed take the compact positive probability measure $\mu$ of the [LCM annihilator](robin-lcm-positive-kernel-nov18.md), using one factor per multiplicity. Its transform $\int e^{zs}\mu(ds)$ vanishes to the required multiplicity at every $z=\rho-1$ with $\Re\rho>b$. Convolve this measure with a nonnegative smooth compact Gevrey density on the log-output axis with transform decaying as $\exp(-c_1|\Im z|^r)$ for some $0<r<1$. Choose the latter density supported in an interval of length less than $\operatorname{width}(\log I)-S_b^*$ and translate so its convolution is supported in $\log I$. The resulting test $\eta(t)dt$ is positive, smooth, and positive bounded below on some subinterval $I'$ of positive length. Shift (7) to $\Re s=\alpha-1$ with $b<\alpha<\beta_0$ chosen as before. All residues vanish, so $|\int_I\eta u_j|\ll j^{\alpha-1}$. The complex isolated-pole test (5) supported on $I'$ gives $\int_{I'}|u_j|dt\gg j^{\beta_0-1}$ by dividing its pairing by its fixed sup norm. Thus $\int_I\eta |u_j|$ dominates the signed integral. Since $\eta$ has fixed finite sup norm, the asserted lower bound applies to each unweighted sign separately.
