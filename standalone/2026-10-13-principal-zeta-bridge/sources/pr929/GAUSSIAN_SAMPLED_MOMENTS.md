# Entire scale interpolation for a fixed Gaussian Mellin detector

**Status:** new proved sampling, maximal-moment, finite-truncation and
moment-to-zero implications. The arithmetic sampled moment estimate remains
open. No full fourth moment, generalized moment, improved zero-free
half-plane, or RH theorem is asserted.

**Main result.** A single fixed log-Gaussian test permits recovery of the
full moving-height moment from only
\(O(\log X/\log\log X)\) predetermined scales per dyadic interval, without a
power loss. Alternatively, it suffices to control its integral on **any**
measurable aperture of an admissible total measure. That aperture can be
concentrated in one shrinking interval; no local distribution condition is
needed. The recovered estimate bounds the sum over rows of the maximum over
the preceding dyadic interval.

**Scope.** The literal zero-extended Möbius/sextic family over
\(K=\mathbb Q(\sqrt{-3})\), every nonzero element row, each fixed moment
order, and all sufficiently large real column scales. The detector is
fixed before the column scale, row, and observations vary. Its noncompact
tails and exact sixth-power replicas are treated explicitly.

**Exact comparison sources.**

1. PR #926, commit 086bf0560c0c2679a1fe41418f583d2c5ca743c3,
   [SAMPLED_MOMENT_CRITERION.md](https://github.com/GettysburgResearch/riemann/blob/086bf0560c0c2679a1fe41418f583d2c5ca743c3/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/SAMPLED_MOMENT_CRITERION.md),
   Sections 2--7. That result uses compactly supported detectors and
   quantitative derivative growth. It recovers a fixed-lower-height
   integrated moment from locally distributed data. The present entire
   detector, global aperture geometry, smaller grid, and maximal recovery
   are new. No estimate for one detector is silently transferred to another.
2. PR #917, commit 6b4723042b3d250024eef45cb1924f88f28e902c,
   [SCALE_AVERAGED_CRITERION.md](https://github.com/GettysburgResearch/riemann/blob/6b4723042b3d250024eef45cb1924f88f28e902c/standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/SCALE_AVERAGED_CRITERION.md),
   Sections 1--4, and
   [AVERAGED_MASK_OPERATORS.md](https://github.com/GettysburgResearch/riemann/blob/6b4723042b3d250024eef45cb1924f88f28e902c/standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/AVERAGED_MASK_OPERATORS.md),
   Sections 2--5 and 7. The exact replica normalization and causal mean
   operator are retained. Section 6 supplies the extension from positive
   lower support to an integrable low-scale tail.
3. The inverse family and fixed primitive inducing characters are those of
   PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1,
   [GENERAL_MOMENT_ATTACK.md](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/GENERAL_MOMENT_ATTACK.md),
   Section 6. Its pinned upstream source is OpenAI/math commit
   adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 5 manuscript.

The interpolation statements use no character large sieve, angular
estimate, native inverse second moment, or zero-free premise. The final
conditional extraction uses the exact arithmetic replicas and the usual
meromorphic continuation of the fixed inducing Hecke \(L\)-function.

**Smallest remaining gap:** the sampled upper bound (4.4) or (4.5) for the
actual Gaussian sums at the intended order and excess. The new theorems
reduce the number and placement of scale observations required; they do not
establish signed arithmetic cancellation at those scales.

## 1. One fixed detector and its entire scale family

Fix a finite excluded-prime set \(S\) and finite-order coefficient datum
\(\nu\). Keep the source's primary ideal generators and literal sextic
symbols, including their zero value at nonunits. Define

\[
G(y)=\frac1{\sqrt{2\pi}}
      \exp\!\left(-\frac{(\log y)^2}{2}\right),\qquad y>0,
\tag{1.1}
\]

\[
A_u(D;G)=
\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)G(Nn/D),
\qquad
M_p(D,H;G)=\sum_{0<Nu\le H}|A_u(D;G)|^p.
\tag{1.2}
\]

The sum includes all good ideals; its Möbius coefficient imposes
squarefreeness. It converges absolutely at every \(D>0\).

### Lemma 1.1. Uniform Gaussian counting and low-scale tails

There is a constant \(C_K\) such that

\[
\sum_n G(Nn/D)\le C_KD\qquad(D>0).
\tag{1.3}
\]

For every fixed \(v>0\), the same bound holds for
\(\exp(-(\log(Nn/D))^2/(2v))\), with a constant depending on \(v\).
Uniformly in the row, for every \(B>0\),

\[
A_u(D;G)=O_{K,B}(D^B)\qquad(0<D\le1).
\tag{1.4}
\]

**Proof.** Let \(J(T)\) count integral ideals of norm at most \(T\), with
\(J(T)=0\) for \(T<1\). Elementary planar lattice counting gives
\(J(T)\le C_KT\) for all \(T>0\). Stieltjes integration by parts gives

\[
\sum_n G(Nn/D)
=-\int_0^\infty J(Dy)G'(y)\,dy
\le C_KD\int_0^\infty y|G'(y)|\,dy.
\tag{1.5}
\]

The boundary terms vanish at both ends and the final integral is finite.
The same argument handles every fixed variance.
For (1.4), choose \(B'>\max(B,1)\). For \(y\ge1\),
\(G(y)\le C_{B'}y^{-B'}\). At \(D\le1\) all arguments satisfy
\(Nn/D\ge1\), so the absolute sum is at most
\(C_{B'}D^{B'}\sum_n(Nn)^{-B'}=O_B(D^B)\).
Every arithmetic multiplier has modulus at most one. \(\square\)

### Proposition 1.2. Entire scale dependence and a nonvanishing detector

For \(X>0\), define the complex scale function by the unambiguous series

\[
F_{u,X}(z)=\frac1{\sqrt{2\pi}}
\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)
\exp\!\left[-\frac12(\log(Nn/X)-z)^2\right].
\tag{1.6}
\]

It is entire and, for every \(z=x+iy\),

\[
|F_{u,X}(x+iy)|\le C_KX e^x e^{y^2/2}.
\tag{1.7}
\]

For real \(t\), \(F_{u,X}(t)=A_u(Xe^t;G)\). The Mellin transform is

\[
\widehat G(s)=\int_0^\infty G(y)y^{s-1}\,dy=e^{s^2/2},
\qquad s\in\mathbb C,
\tag{1.8}
\]

and is never zero.

**Proof.** The absolute value of each term in (1.6) is
\(e^{y^2/2}G(Nn/(Xe^x))\). Lemma 1.1 gives (1.7). On each compact
complex set, Gaussian decay supplies a summable majorant, so the series
of entire summands converges normally. Substituting \(t=\log y\) in the
Mellin integral gives the Gaussian moment-generating function (1.8),
first for real \(s\), then for all complex \(s\) by entire continuation.
The exponential has no zero. \(\square\)

This detector is noncompact. Its Mellin transform decays in each fixed
vertical strip and remains nonzero, while its logarithmic scale
dependence is entire. Neither property is inferred for a compact test.

### Corollary 1.3. An all-order derivative bound

Fix \(a=\log2\) and \(I=[-a,a]\). There are fixed \(B,C>0\), independent
of \(u,X,m\), such that for every integer \(m\ge1\),

\[
\frac{\|F_{u,X}^{(m)}\|_{L^\infty(I)}}{m!}
\le CX\left(\frac B{\sqrt m}\right)^m.
\tag{1.9}
\]

**Proof.** Center Cauchy's formula at real \(t\in I\), with radius
\(R=\sqrt m\). Equation (1.7) gives the bound
\(CX\exp(R+R^2/2)\) on that circle. The derivative divided by \(m!\)
is consequently at most \(CXe^{\sqrt m+m/2}m^{-m/2}\).
Use \(\sqrt m\le m\) and enlarge the fixed \(B\). \(\square\)

The explicit factor \(m^{-m/2}\) makes the smaller observation set
possible. An unspecified smoothness constant would not suffice.

## 2. Interpolation from an aperture anywhere in the interval

### Lemma 2.1. Supremum recovery from integrated observations

Let \(I_0\) have length \(\ell>0\), let \(E\subset I_0\) be measurable
with \(|E|\ge\gamma\ell>0\), and let
\(f\in C^m(I_0;\mathbb C)\). For \(p\ge1\) and integer \(m\ge1\),

\[
\sup_{I_0}|f|
\le \ell^{-1/p}\left(\frac C\gamma\right)^m
       \|f\|_{L^p(E)}
   +\frac{\ell^m}{m!}\|f^{(m)}\|_\infty,
\tag{2.1}
\]

where \(C>1\) is absolute.

**Proof.** Chebyshev's inequality leaves \(E_0\subset E\) of measure at
least \(\gamma\ell/2\) on which
\[
|f(t)|\le(2/(\gamma\ell))^{1/p}\|f\|_{L^p(E)}.
\]
Choose \(m\) ordered points in \(E_0\), separated by at least
\(d=\gamma\ell/(4m)\). A greedy choice works because fewer than \(m\)
excluded neighborhoods have total measure less than \(\gamma\ell/2\).
Their interpolation polynomial \(P\), of degree at most \(m-1\), has
Lagrange basis satisfying
\[
\sup_{I_0}\sum_{j=1}^m|L_j(t)|
\le\left(\frac{\ell}{d}\right)^{m-1}
\sum_{j=1}^m\frac1{(j-1)!(m-j)!}
\le(C/\gamma)^{m-1}.
\tag{2.2}
\]
Here the factorial sum is \(2^{m-1}/(m-1)!\); the case \(m=1\)
is immediate. Combine (2.2) with the bound on \(E_0\), using
\(\gamma^{-1/p}\le\gamma^{-1}\).
The divided-difference integral formula gives
\[
|f(t)-P(t)|
\le\frac{\|f^{(m)}\|_\infty}{m!}\prod_{j=1}^m|t-t_j|
\le\frac{\ell^m}{m!}\|f^{(m)}\|_\infty.
\]
For complex functions the formula follows by iterating the fundamental
theorem of calculus over the interpolation simplex; it is
complex-linear and does not require a real mean-value point.
This proves (2.1). \(\square\)

The set \(E\) need not occupy a fixed fraction of smaller intervals.
It may be disconnected, irregular, or concentrated at one endpoint.

## 3. A maximal moment with the correct moving row budget

Let \(h>0\), \(p\ge1\), and \(X\ge2\). Define

\[
\mathfrak M_{p,h}(X)=
\sum_{0<Nu\le X^h}
\sup_{X/2\le D\le X}|A_u(D;G)|^p.
\tag{3.1}
\]

For measurable \(E_X\subset[0,a]\), put

\[
\gamma_X=|E_X|/a,\qquad
Q^{E}_{p,h}(X)=
\int_{E_X}M_p(Xe^t,(Xe^t)^h;G)\,dt.
\tag{3.2}
\]

### Theorem 3.1. Global-aperture maximal recovery

For \(0<\gamma_X\le1\) and every integer \(m\ge1\),

\[
\boxed{
\mathfrak M_{p,h}(X)^{1/p}
\le \left(\frac C{\gamma_X}\right)^m
        Q^{E}_{p,h}(X)^{1/p}
   +C_{K,p,h}X^{1+h/p}
       \left(\frac B{\sqrt m}\right)^m.
}
\tag{3.3}
\]

The constants are independent of \(X,m,E_X\), and the row.

**Proof.** Apply Lemma 2.1 on \(I=[-a,a]\) to each \(F_{u,X}\).
The observation set \(E_X\subset[0,a]\) has proportion
\(\gamma_X/2\) in \(I\); all fixed interval factors are absorbed into
\(B,C\). Corollary 1.3 bounds the remainder. Take the \(\ell^p\)
triangle inequality over the fixed set \(0<Nu\le X^h\), with
cardinality \(O_K(X^h)\). Every observed scale has
\((Xe^t)^h\ge X^h\), so its moment includes every interpolated row.

The target is the **preceding** interval \([X/2,X]\). For \(D\) there,
\(D^h\le X^h\), so
\[
M_p(D,D^h;G)\le\mathfrak M_{p,h}(X).
\tag{3.4}
\]
No row at a moving-height endpoint is omitted. \(\square\)

This is extrapolation over a bounded logarithmic distance, justified
by (1.9). It is not a change of row height inside an integral.

### Theorem 3.2. A predetermined finite grid

For \(N\ge2\), set

\[
t_j=\frac{ja}{N-1},\quad 0\le j<N,\qquad
Q^{\rm grid}_{p,h}(X;N)=
\frac1N\sum_{j=0}^{N-1}
M_p(Xe^{t_j},(Xe^{t_j})^h;G).
\tag{3.5}
\]

Then

\[
\boxed{
\mathfrak M_{p,h}(X)^{1/p}
\le C^NQ^{\rm grid}_{p,h}(X;N)^{1/p}
   +C_{K,p,h}X^{1+h/p}
      \left(\frac B{\sqrt N}\right)^N.
}
\tag{3.6}
\]

**Proof.** Interpolate \(F_{u,X}\) at all these nodes. For output
\(t\in[-a,a]\), numerator distances are at most \(2a\); the
denominator for node \(j\) has absolute value
\[
\left(\frac a{N-1}\right)^{N-1}j!(N-1-j)!.
\]
The sum of absolute Lagrange basis values is at most
\[
\frac{[4(N-1)]^{N-1}}{(N-1)!}\le(4e)^{N-1}.
\tag{3.7}
\]
Thus the interpolant is bounded by \(C^N\max_j|F_{u,X}(t_j)|\), then
by \(C^NN^{1/p}(N^{-1}\sum_j|F_{u,X}(t_j)|^p)^{1/p}\).
Absorb \(N^{1/p}\le2^N\) into \(C^N\).
The remainder is at most
\((2a)^N\|F_{u,X}^{(N)}\|_\infty/N!\); apply (1.9).
Take the fixed-row \(\ell^p\) triangle inequality as above. \(\square\)

The nodes depend only on \(X,N\), not on the row or on arithmetic
values.

## 4. No power loss and the exact arithmetic hypotheses

Put \(L_X=\log(e^eX)\), and choose

\[
n_X=\left\lceil\frac{8L_X}{\log L_X}\right\rceil.
\tag{4.1}
\]

Then
\[
n_X=O(\log X/\log\log X),\quad n_X=o(\log X),\qquad
X\left(\frac B{\sqrt{n_X}}\right)^{n_X}=X^{-3+o(1)}
\tag{4.2}
\]
for every fixed \(B>0\). Indeed
\(n_X\log n_X/(2\log X)\to4\) and
\(n_X\log B/\log X\to0\).

### Theorem 4.1. Sampled bounds recover the full moment

Fix \(p\ge1\), \(h>0\), and \(b\ge0\). Assume either of the following
on every sufficiently large dyadic \(X=2^j\).

**Aperture version.** There is a measurable
\(E_X\subset[0,\log2]\), with \(\gamma_X=|E_X|/\log2>0\), such that

\[
\log(1/\gamma_X)=o(\log\log X),
\tag{4.3}
\]

\[
Q^{E}_{p,h}(X)\ll_\epsilon X^{h+b+\epsilon}
\quad\text{for every }\epsilon>0.
\tag{4.4}
\]

**Grid version.** With the prescribed \(N=n_X\),

\[
\boxed{
Q^{\rm grid}_{p,h}(X;n_X)
\ll_\epsilon X^{h+b+\epsilon}
\quad\text{for every }\epsilon>0.
}
\tag{4.5}
\]

Either version implies

\[
\boxed{
\mathfrak M_{p,h}(X)\ll_\epsilon X^{h+b+\epsilon},
\qquad
M_p(D,D^h;G)\ll_\epsilon D^{h+b+\epsilon}
\quad\text{for every real }D\ge2.
}
\tag{4.6}
\]

Constants and sets may depend on the fixed \(p,h\). The same \(E_X\)
is used for the complete row moment, rather than separate arithmetic
selections for different rows.

**Proof.** In (3.3) take \(m=n_X\). Equation (4.3) gives
\(n_X\log(C/\gamma_X)=o(\log X)\), hence observational multiplier
\(X^{o(1)}\). By (4.2), the row-norm error is
\(O(X^{h/p-1})\), smaller than \(X^{(h+b)/p}\).
Allocate arbitrarily small exponents in (4.4) and raise to the fixed
power \(p\). For the grid \(C^{n_X}=X^{o(1)}\), so (3.6) gives the
same conclusion. Absorb bounded initial scales.
For real \(D\ge2\), choose dyadic \(X\) with \(D\in[X/2,X]\).
Use (3.4) and \(X\le2D\). \(\square\)

### Apertures without local distribution

One may take
\[
E_X=[t_X,t_X+a\gamma_X]\subset[0,a],\qquad
\gamma_X=\exp[-\sqrt{\log\log(e^eX)}],
\tag{4.7}
\]
at any permitted location \(t_X\). All observations then lie in one
shrinking interval, whose measure tends to zero. Fixed positive
measure and \(\gamma_X=(\log\log(e^eX))^{-A}\), for any fixed \(A>0\),
also work.

A fixed power \(\gamma_X=(\log X)^{-A}\) does not meet (4.3).
The resulting interpolation power cost is not discarded.
The finite-grid theorem is separate: it uses discrete values with
explicit nonnegative weights.

For the target, set \(p=2k\), \(b=k+e\), \(e\ge0\). The missing
arithmetic estimate is precisely

\[
\frac1{n_X}\sum_{j=0}^{n_X-1}
\sum_{0<Nu\le(Xe^{t_j})^h}
|A_u(Xe^{t_j};G)|^{2k}
\ll_\epsilon X^{h+k+e+\epsilon},
\tag{4.8}
\]

or the aperture counterpart. It concerns one fixed detector and the
actual signed coefficients. The sampling theorem supplies no bound
for its left side. Conversely, a full moment estimate trivially
implies these sampled estimates because all observations lie in
\([X,2X]\). Thus the new result simplifies sufficient scale
observations and adds maximal recovery; it does not make the
remaining arithmetic assertion true by itself.

## 5. Explicit finite sums suffice at each observed scale

### Proposition 5.1. Uniform finite-truncation error

For \(R\ge0\) define

\[
A_u^{[R]}(D;G)=
\sum_{\substack{(n,S)=1\\De^{-R}\le Nn\le De^R}}
\mu_K(n)\nu(n)\chi_n(u)G(Nn/D).
\tag{5.1}
\]

For all \(D>0\) and every row,

\[
\boxed{
|A_u(D;G)-A_u^{[R]}(D;G)|
\le C_KD e^{-R^2/4}.
}
\tag{5.2}
\]

For fixed \(A>0\), take
\[
R_A(D)=2\sqrt{(A+1)\log D},\qquad D\ge2.
\tag{5.3}
\]
The error is \(O_K(D^{-A})\), and retained norms lie in
\[
\left[D\exp(-O_A(\sqrt{\log D})),
      D\exp(O_A(\sqrt{\log D}))\right]=D^{1+o(1)}.
\tag{5.4}
\]

**Proof.** On omitted terms \(t=\log(Nn/D)\) has \(|t|\ge R\), and
\(e^{-t^2/2}\le e^{-R^2/4}e^{-t^2/4}\).
Sum the Gaussian of variance two using Lemma 1.1. \(\square\)

The interval is literal, with no ideals below norm one. On the rows
\(0<Nu\le D^h\), the error has \(\ell^p\) norm
\[
O_{K,p}(D^{h/p-A}).
\tag{5.5}
\]
Thus any fixed \(A>0\), for example \(A=1\), allows the full sums in
(4.4), (4.5), or (4.8) to be replaced by these finite truncations
without changing Theorem 4.1 for \(b\ge0\). Use the integrated or
finite weighted \(\ell^p\) triangle inequality; all observation
scales are within a fixed factor of \(X\).

The derivative and interpolation arguments apply to the complete
entire Gaussian family. They are **not** applied to truncated sums,
whose moving endpoints need not be smooth. Equation (5.5) is the
separate adapter from finite arithmetic data. No earlier compact-test
bound is automatically a bound for these Gaussian-weighted finite
sums.

## 6. Exact replicas and causal extraction with a low-scale tail

Fix nonzero \(r\), put \(\eta(n)=\nu(n)\chi_n(r)\) outside \(S\), and
extend it completely multiplicatively by zero at excluded primes.
For an ideal \(v\), with its chosen generator, define

\[
(T_vf)(x)=
\sum_{d:\,\operatorname{rad}d\mid v}\eta(d)f(x/Nd).
\tag{6.1}
\]

### Lemma 6.1. Absolutely convergent Gaussian replicas

For \(f(x)=A_r(x;G)\),
\[
T_vf(x)=A_{rv^6}(x;G)
\tag{6.2}
\]
for all \(x>0\), with absolute convergence of all regrouping used.

**Proof.** Lemma 1.1 gives
\[
\sum_{\operatorname{rad}d\mid v}
\sum_n|\mu(n)\eta(n)\eta(d)|G(Nn\,Nd/x)
\le C_Kx\prod_{p\mid v}(1-(Np)^{-1})^{-1}<\infty.
\tag{6.3}
\]
At a prime of \(v\), its geometric local series cancels the inverse
local factor \(1-\eta(p)z\). This deletes exactly the columns divisible
by that prime, as required by
\(\chi_n(v^6)=\mathbf1_{(n,v)=1}\).
The identity also holds when \(\eta(p)=0\), where the local operation
is the identity. There is no condition \((r,v)=1\). \(\square\)

### Lemma 6.2. Moving-cutoff inversion with an integrable low part

Let \(p\ge1\), \(\sigma>0\), and let \(f\) be measurable with
\[
\int_0^T|f(x)|^px^{-p\sigma}\frac{dx}{x}<\infty
\qquad\text{for every finite }T>0.
\tag{6.4}
\]
Let \(Y\) be measurable with \(Y(x)\ge c x^\rho\) eventually,
\(c,\rho>0\), and define
\[
Pf(x)=\frac1{J(Y(x))}\sum_{Nv\le Y(x)}T_vf(x)
\tag{6.5}
\]
where \(Y(x)\ge1\). If \(Pf\) has finite weighted \(L^p\) norm above
some sufficiently large fixed scale, then \(f\) has finite weighted
\(L^p\) norm on \((0,\infty)\).

**Proof.** Write \(R_d=N\operatorname{rad}d\). The exact coefficient
of the mean is \(w_Y(d)=J(Y/R_d)/J(Y)\). The elementary ideal count
with error \(O(\sqrt Y)\) gives
\[
w_Y(d)\ll R_d^{-1},\qquad
|w_Y(d)-R_d^{-1}|
\ll_\delta Y^{-\delta}R_d^{-1+\delta},\quad 0<\delta<1/2.
\tag{6.6}
\]
This includes \(R_d>Y\), when \(w_Y(d)=0\).

A dilation by \(Nd\) costs at most \((Nd)^{-\sigma}\) in the
weighted \(L^p\) norm on \((0,T)\). The operator
\[
Mf(x)=\sum_d\eta(d)R_d^{-1}f(x/Nd)
\tag{6.7}
\]
is bounded there and has a bounded causal inverse. At \(q=Np\), with
\(z=\eta(p)S_p\), \(S_pf(x)=f(x/q)\), its factor and inverse are
\[
\frac{1-(1-q^{-1})z}{1-z},\qquad
1-q^{-1}\sum_{j\ge1}(1-q^{-1})^{j-1}z^j.
\tag{6.8}
\]
Both Euler products converge in the coefficient norm
\(\sum_d|c_d|(Nd)^{-\sigma}\), since their nonconstant local norms
are \(O_\sigma(q^{-1-\sigma})\).

Choose \(0<\delta<\min(\sigma,1/2)\). The positive majorant
\[
\sum_d R_d^{-1+\delta}(Nd)^{-\sigma}
=\prod_p\left(1+
 \frac{(Np)^{-1+\delta-\sigma}}{1-(Np)^{-\sigma}}\right)
\tag{6.9}
\]
converges. On functions supported in \([X_0,\infty)\), equations
(6.6)--(6.9) give \(\|P-M\|\ll X_0^{-\rho\delta}\), uniformly on
every finite \([X_0,T]\). Choose \(X_0\) so large that
\(\|M^{-1}(P-M)\|<1/2\). A Neumann series gives a causal inverse of
\(P\) there, uniformly in \(T\).

Split \(f=f_0+f_1\), with \(f_0=f\,\mathbf1_{(0,X_0)}\).
Hypothesis (6.4) gives a finite global weighted norm for \(f_0\).
The first bound in (6.6) majorizes \(Pf_0\) by the positive dilation
operator with coefficients \(C_KR_d^{-1}\), so it too has finite
global weighted norm. Apply the finite-interval inverse to
\(Pf_1=Pf-Pf_0\), then let \(T\to\infty\).
No integrability at infinity of \(f_1\) was assumed in advance.
\(\square\)

For the Gaussian family, (6.4) holds for every \(\sigma>0\), by
Lemma 1.1. This replaces the exact positive lower support assumed in
the original compact-test formulation.

### Theorem 6.3. Sampled generalized moments and zero extraction

Fix \(k\ge1\), \(h>0\), \(e\ge0\). Suppose either arithmetic sampling
hypothesis of Theorem 4.1 holds with
\(p=2k\), \(b=k+e\), using full Gaussian sums or the finite
truncations of Section 5. Then each fixed primitive Hecke twist
induced by \(n\mapsto\nu(n)\chi_n(r)\) is zero-free in

\[
\boxed{\Re s>\frac12+\frac{5h}{12k}+\frac e{2k}.}
\tag{6.10}
\]

**Proof.** Theorem 4.1 gives
\[
M_{2k}(D,D^h;G)\ll_\epsilon D^{h+k+e+\epsilon}
\quad(D\ge2)
\tag{6.11}
\]
for every \(\epsilon>0\).
For fixed \(r\) and large \(D\), put
\(Y_r(D)=(D^h/Nr)^{1/6}\).
Ideals \(Nv\le Y_r(D)\) give distinct rows \(rv^6\) in the original
ball. Jensen, (6.2), and \(J(Y)\asymp_KY\) give
\[
|M_{Y_r(D)}A_r(D;G)|^{2k}
\ll_{K,r}D^{-h/6}M_{2k}(D,D^h;G).
\tag{6.12}
\]
Fix \(\sigma\) above (6.10). Integration against
\(D^{-2k\sigma}dD/D\) gives a convergent dyadic series with exponent
\[
k+5h/6+e-2k\sigma+\epsilon<0
\]
after a small enough choice of \(\epsilon\). Lemma 6.2 applies with
\(\rho=h/6\), proving
\[
\int_0^\infty |A_r(D;G)|^{2k}D^{-2k\sigma}\frac{dD}{D}<\infty.
\tag{6.13}
\]

Hölder above scale one and (1.4) below it make
\[
\mathcal F_r(s)=\int_0^\infty A_r(D;G)D^{-s}\frac{dD}{D}
\]
holomorphic for \(\Re s>\sigma\), with locally uniform convergence
on every strictly smaller half-plane. For \(\Re s>1\), absolute
convergence and (1.8) give
\[
\mathcal F_r(s)=e^{s^2/2}\frac{E_r(s)}{L_K(s,\psi_r)}.
\tag{6.14}
\]
Here \(\psi_r\) is the fixed primitive inducing character and \(E_r\)
is the finite correction for deleted Euler factors. Those factors
and their reciprocals are holomorphic and nonzero for \(\Re s>0\),
as is \(e^{s^2/2}\). By the identity theorem, a zero of
\(L_K(s,\psi_r)\) in \(\Re s>\sigma\) would produce a pole in the
holomorphic \(\mathcal F_r\). This is impossible. A principal pole
produces a zero of the reciprocal and causes no exception.
Let \(\sigma\) approach (6.10). \(\square\)

For \(k=2\), \(h=1+\theta\), \(e=0\), the conditional boundary is
\(17/24+5\theta/24\). Along unbounded fixed orders with
\(h_k=o(k)\) and \(e_k=o(k)\), the conditional boundaries approach
\(1/2\). The arithmetic estimates at those orders are still required.
The order and target character stay fixed while each scale theorem
is applied; uniform-in-\(k\) constants are neither claimed nor needed.
Coverage of reflected characters is still required for the
corresponding critical-line conclusion.

## 7. What the argument advances

The entire detector and row-uniform growth bound prove maximal
recovery from an arbitrarily located admissible aperture, the
\(O(\log X/\log\log X)\) predetermined grid, the explicit finite-sum
adapter, and the unchanged exact moment-to-zero implication.

They do not cancel the long singleton coefficients in the sampled
moment. Finitely many scales at each \(X\) are not a finite
verification of the all-\(X\) bound. The signed Möbius arithmetic
remains the missing infinite assertion.

No numerical moment experiment, finite zero census, proof-assistant
check, or independent replay of the imported quasi-Riemann theorem
is used or claimed in this note.
