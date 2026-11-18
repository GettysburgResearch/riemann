# Local heat collisions and zeros of the derivative in the indexed high-zero census

**Status.** Proposed finite theorem. In the [2,000,000-index checkpoint](checkpoint-0200.json) there are at least 83 distinct neighboring pairs of simple zeta zeros that each undergo a unique real double collision as the ordinate-normalized de Bruijn–Newman time decreases from zero to \(-1/5000\). At the common final time each pair consists of two simple nonreal conjugate zeros. In the same strip of ordinates there are at least 526 distinct simple zeros of \(\zeta'\) strictly to the right of the critical line, including 9 within distance 0.001. The assertions are unconditional given the published Platt–Trudgian anchor and the indexed finite arithmetic. [Arb verifier](heat_pair_census.py) · [Counted witnesses](heat-pair-census-0200.json)

## Entire-product bounds from the surrounding census

Use \(\Xi(x)=\xi(1/2+ix)\) and its complex zeros \(w=\gamma+ib\), with \(|b|<1/2\). Let real simple consecutive zeros be \(m-h,m+h\), let \(Q(x)=\Xi(x)/((x-m)^2-h^2)\) and put \(A=Q'(m)/Q(m)\). The checker uses outer dyadic enclosures to bound \(h\) from above and \(m\) on both sides. For \(r=3/2\),
\[
 P=\Re(\xi'/\xi)(2+im)=\sum_w\frac{r+b}{(r+b)^2+(m-\gamma)^2}<16 .
\]
The Euler product gives \(|\zeta'/\zeta(2+im)|<2\) and the elementary gamma factor is interval-evaluated. Subtract the pair's Poisson mass and rigorous lower bounds on the contributions of the nearest twenty indexed zeros on each side. Denote the resulting upper bound for the remaining mass by \(P_f\), and write \(F\) for a lower bound on every remaining ordinate distance from \(m\). The uniform full-strip estimate is
\[
 B=\sum_{w\ne m\pm h}|m-w|^{-2}
 \le \sum_{\rm near}|m-w|^{-2}+(1+4/F^2)P_f .
\]

A signed comparison also bounds \(A\) without multiplying the entire near mass by a common absolute constant. At \(m-ir\) the pair contributions to the real part of \(\Xi'/\Xi\) sum to zero by symmetry. Its real part has absolute value below 3 by the elementary gamma factor and the Euler-product estimate. For a known real zero with signed distance \(d=m-\gamma\), moving the point from \(m-ir\) to \(m\) adds \(r^2/[d(d^2+r^2)]\) to its real logarithmic derivative. For arbitrary other zeros the absolute difference, divided by that zero's Poisson mass, is
\[
 \left|\frac{d(r^2+2rb)}{(d^2+b^2)(r+b)}\right|\le\frac{15}{4|d|}.
\]
Consequently
\[
 |A|\le 3+
 \left|\sum_{\rm near}\frac{r^2}{d(d^2+r^2)}\right|+\frac{15 P_f}{4F}.
\]
The sums of differences converge absolutely by the Hadamard product. All near-zero terms retain their signs and use interval endpoints.

## The heat criterion and uniqueness of collision

In the coordinate \(x=m+w-2uA\), the zeros at backward time \(u\) are those of
\[
 G_u(w)=\mathbb E\left[((w+U)^2-h^2)E(w+U)\right],
 \quad U\sim N(0,2u),\quad E(z)=Q(m+z)e^{-Az}/Q(m).
\]
From the [Gaussian product estimate](lehmer-pair.md), for \(|w|\le R\), \(0\le u\le v\), and \(8Bv<1\),
\[
 |G_u(w)-(w^2+2u-h^2)|\le C_0+C_1|w|^2 .
\]
Put \(D=1-8Bv\), \(s^2=2v/D\) and \(K=B\exp(1/2+2BR^2)/(2\sqrt D)\). Then \(C_0=K(3s^4+h^2s^2)\) and \(C_1=K(R^2+6s^2+h^2)\). Each certificate at \(v=1/5000\) verifies
\[
 C_0<2v-h^2,\qquad C_1<1,\qquad C_0+C_1R^2<R^2-2v .
\]
Since \(h^2<2v\), the last inequality preserves exactly two zeros by Rouché on the circle for **every** \(0\le u\le v\). The first two make the real diameter strictly positive at the final time. Thus the initial simple real pair becomes a simple nonreal conjugate pair. There is exactly one collision in between: at a real double root the conserved count gives multiplicity two, and \(\partial_uG_u=\partial_w^2G_u\ne0\) there. Locally the two roots are \(w_*\pm\sqrt{-2(u-u_*)}+O(|u-u_*|)\), by the analytic quadratic preparation theorem. Every collision therefore has the same orientation as \(u\) increases. The real-part intervals enlarged by \(R+2v|A|\) are checked disjoint across witnesses throughout the deformation. For the normalization with initial function proportional to \(\Xi(x/2)\), double the ordinates and multiply all times by four.

## Locating simple zeros of the ordinary zeta derivative

Let \(s_0=1/2+im\) and \(z=s-s_0\). Write \(E_0(s)=1/s+1/(s-1)-\log(\pi)/2+\psi(s/2)/2\) and remove the pair from \(\zeta'/\zeta\) by defining
\[
 L(z)=\frac{\zeta'}{\zeta}(s_0+z)-\frac{2z}{z^2+h^2}.
\]
At the center \(L(0)=-iA-E_0(s_0)\), with \(13<\Re E_0(s_0)<14\) and \(|E_0(s_0)|<15\). For a circle of radius \(R\) below the distance \(d_*\) to every other zero, \(|L'|\le M'=B/(1-R/d_*)^2+1\) throughout the disk. The unit allowance covers \(E_0'\): in the tested disks the imaginary part exceeds \(3\cdot10^{12}-1\) and the real part is positive. The trigamma series and integral comparison give \(|\psi'(s/2)|\le (\Im(s)/2)^{-2}+\pi/|\Im(s)|\). Therefore \(|L|\le M=15+|A|+RM'\). The checker tries small radii for which
\[
 q=M(R^2+h^2)/2<R.
\]
By Rouché there is one simple zero of \(2z+(z^2+h^2)L(z)\) inside, necessarily a zero of \(\zeta'\) because the analytic pair-removed zeta is nonvanishing. It satisfies \(|z|\le q\). For \(MR<2\), it also satisfies \(|z|\le M h^2/(2-MR)\). From the equation for \(z\),
\[
 \left|\Re z-\tfrac12 h^2\Re E_0(s_0)\right|\le
 \tfrac12(M'q h^2+Mq^2).
\]
A relative error bound is \(\tfrac12[M'q+M(M/(2-MR))^2 h^2]\) after division by \(h^2\). An upper bound for the half-gap suffices in both tests, including when its rigorous lower bound is zero. The relative error below \(13/2\) locates the derivative zero strictly to the right. The absolute error bounds its distance. Distinctness follows from the disjoint imaginary-part projections of the proved disks. The checkpoint records lower counts by several distances.

## Reproduction and scope

From this directory run the two checkers against the counted checkpoint.

```sh
python heat_pair_census.py checkpoint-0200.json
python spacing_census.py checkpoint-0200.json
```

The [spacing counts](spacing-census-0200.json) compare successive pairs of **new** indices using outward-rounded endpoints on a \(2^{-32}\) lattice. Uncertain comparisons count in neither strict category. The heat and derivative scan skips block joins and tests only pairs whose initial upper bound for the gap is at most 0.09. Each report includes the ordered source digest. The heat report hashes the accepted left indices in increasing order with one ASCII decimal index and newline per row. Replaying the underlying zero isolation requires the separate [native verification procedure](README.md).
