# A connected ferromagnet realizing the original theta law through degree 20

Status: **PROPOSED computer-assisted finite theorem. Independent mathematical
review at the frozen source identity is required. RH is not proved.**

The new result closes the degree-20 finite target left open by the degree-18
models in #981 and #988 and the local positive-loop theorem in #992. The proof
is a complete rational contraction against the original infinite theta source.
It does not infer equality from a numerical residual, a fitted continuation,
moment-interval overlap, or real zeros of an unrelated polynomial.

## 1. Source, normalization and exact statement

For t>=0 let q_n=pi*n^2 and

\[
\Phi(t)=\sum_{n\ge1}
 (4q_n^2e^{9t/2}-6q_ne^{5t/2})e^{-q_ne^{2t}},
\]

extended evenly. Every summand is positive because q_n e^{2t}>3/2. Write

\[
 Z=\int_{\mathbb R}\Phi(t)\,dt,\qquad
 d\rho_\theta(t)=Z^{-1}\Phi(t)\,dt,\qquad
 v=\int t^2d\rho_\theta(t),\qquad T_*=T/\sqrt v.
\]

The classical theta Fourier identity is

\[
 \mathbb E e^{izT}=\frac{\xi(1/2+iz)}{\xi(1/2)}.
 \tag{1}
\]

This is the original source, with no heat deformation. The Fourier identity
and the weighted finite ferromagnetic Lee--Yang theorem are imported classical
inputs; [Newman--Wu, arXiv:1901.06596v2](https://arxiv.org/html/1901.06596v2),
Sections 2.1 and 2.5, supplies precise statements. The source has all exponential moments, by its superexponential
decay on the real axis. The directed reconstruction verifies 1/25<v<1/20
in the inherited source protocol; its full variance interval is also retained.

Let c_j be the cumulants of a fair sign and set

\[
 s_r=\kappa_{2r}(T_*)/c_{2r},\qquad1\le r\le10.
\]

The nonzero c_2r are computed by the exact cumulant recurrence. In particular
c_20=-29088885112832. Cumulants here mean formal Taylor coefficients of a
logarithm at a generating series with constant term 1; no logarithm is taken
across unknown zeros of xi.

### Theorem T20D

There exists a zero-field ferromagnetic Ising measure on a **connected tree
with 305 vertices and 304 edges**, and a nonnegative weighted spin observable Y,
such that

\[
 \mathbb E Y^{2r}=\mathbb E T_*^{2r}\quad(1\le r\le10),
 \qquad \mathbb E Y^{2r+1}=0\quad(r\ge0).
 \tag{2}
\]

All 304 observed spins have strictly positive weights. The remaining vertex is
an auxiliary hub with observable weight 0. Every edge coupling is finite and
satisfies

\[
 10^{-11}<J_e<3.
 \tag{3}
\]

The support of Y is contained in (-11,11), its variance equals 1, and its entire
characteristic function has only real zeros. The root is unique in the
specified 10-coordinate cube of radius 10^-30 about the terminating-rational
center in `parameters20.json`, with all other coordinates fixed. This is
uniqueness in that cube, not uniqueness among all graphs or parameter choices.

Consequently X=sqrt(v)*Y realizes every original unstandardized theta moment
through 20 and also has a real-zero characteristic function. This last scaling
changes only the observable weights; all Ising couplings stay fixed.

No order beyond 20 is claimed matched, and no unbounded-order feasibility or
full RH conclusion is claimed.

## 2. A small component formula for the complete 305-spin Gibbs law

The 48 coordinates are triples z_i=(A_i,B_i,p_i), 0<=i<=15. Their multiplicities
are

\[
 (m_0,m_1,m_2,\ldots,m_{15})=(256,10,1,\ldots,1).
\]

The first type is a single observed spin of weight A_0. Its unused entries
are fixed exactly at B_0=0 and p_0=1. Every other type is a two-spin component
with positive weights

\[
 u_i=(A_i+B_i)/2,\qquad w_i=(A_i-B_i)/2
 \quad(1\le i\le15),
\]

and internal correlation q_i=2p_i-1. Thus each copy has spins sigma_i,tau_i
and observable u_i sigma_i+w_i tau_i. On the entire certified cube,
0<B_i<A_i and 1/2<p_i<1.

Add one fair, zero-weight hub epsilon. Join the hub to the single spin in each
type 0 copy and to sigma_i in each dimer copy. Every such hub edge has the exact
correlation

\[
 \eta=\tanh J_{hub}=10^{-10}.
\]

There are 256 single spins and 10+14=24 dimers, hence 304 observed spins. The
280 component roots give 280 hub edges; the 24 dimer edges give 304 edges in all.
The graph is a tree. No spin is discarded, and no correlation is replaced by an
independence approximation in the accepted model.

For every full configuration s in {−1,+1}^305, the probability is

\[
 \mathbb P(s)=2^{-305}\prod_{e=ab}(1+q_e s_a s_b).
 \tag{4}
\]

To see that (4) is normalized, choose the hub uniformly and choose each edge
product independently with its specified mean q_e. A tree gives a bijection
from those independent signs to the full spin configuration. This also shows
that (4) is exactly the usual zero-field Gibbs law with J_e=atanh(q_e), because
exp(J_e s_as_b)=cosh(J_e)(1+q_e s_as_b).

Conditional on epsilon=+1, component roots are independent signs of mean eta.
The internal dimer edge product is independent of its root and equals +1 with
probability p_i. Conditional on root +1 the dimer observable is therefore A_i
with probability p_i and B_i with probability 1-p_i. Define its conditional
raw moments by M_i,0=1 and

\[
 M_{i,n}=\bigl[p_iA_i^n+(1-p_i)B_i^n\bigr]
 \begin{cases}1,&n\text{ even},\\\eta,&n\text{ odd},\end{cases}
 \qquad i\ge1.
 \tag{5}
\]

For i=0 the bracket in (5) is A_0^n. In particular B_i has its stated positive
orientation in the odd conditional moments; changing its sign changes the
joint law through the shared hub. Conditional independence applies only after
conditioning on that hub.

For any raw sequence M_0=1 the cumulant recurrence and its inverse are

\[
 K_n=M_n-\sum_{j=1}^{n-1}\binom{n-1}{j-1}K_jM_{n-j},
 \qquad
 M_n=\sum_{j=1}^{n}\binom{n-1}{j-1}K_jM_{n-j}.
 \tag{6}
\]

Apply the first recurrence to each (5), add the conditional cumulants with
the integer multiplicities m_i, and apply the inverse recurrence. Averaging
the two hub signs keeps the resulting even moments and sets all odd moments
to 0. A final application of (6) gives the unconditional cumulants.
`connected_blocks.py` implements exactly these polynomial operations over
rationals. Denote its normalized even outputs by B_r(z), 1<=r<=10.

Every statement above holds for the complete finite graph, not for a truncated
configuration list or a selected spin sector.

### Positivity and size bounds

The checker verifies 1e-11<q_e<.99 for every edge type on the whole cube. For
0<q<1, atanh(q)>q. Also (1+q)/(1-q)<199 when q<.99, while the rational lower
sum of exp(6) through degree 6 exceeds 199. Hence atanh(q)<3, proving (3).
The support bound is the whole-box inequality

\[
 256A_0+10A_1+\sum_{i=2}^{15}A_i<11.
 \tag{7}
\]

At the rational center this sum is approximately 9.76214231. The approximations
in this prose are explanatory only; no decimal tolerance is an acceptance gate.

## 3. Exact source equations and a whole-cube contraction

The equations are

\[
 F_r(z)=B_r(z)-s_r=0,\qquad1\le r\le10.
 \tag{8}
\]

The active flattened-coordinate list is exactly

\[
 (6,0,15,21,3,27,9,12,4,42).
\]

All other 38 coordinates are fixed by the rational parameter file. Let c be
that center and let C be the closed cube of radius r_0=10^-30 in the active
coordinates. Every weight/coupling/size inequality in Section 2 is checked on C,
not merely at c.

The checker computes the exact rational center Jacobian J_0=DB(c), forms its
exact rational inverse R, and verifies both R J_0=I and J_0 R=I entry by entry.
Using fresh intervals for the actual theta constants and outward polynomial
differentiation, it computes rational upper bounds

\[
 \beta\ge\|RF(c)\|_\infty,\qquad
 L\ge\sup_{z\in C}\|I-RDB(z)\|_\infty.
 \tag{9}
\]

The strict acceptance predicates are

\[
 L<10^{-3},\quad\beta<r_0/1000,\quad
 r_0-\beta-Lr_0>99r_0/100.
 \tag{10}
\]

The accepted full-source calculation gives

\[
 \beta<1.561\,10^{-39},\qquad L<1.371\,10^{-10}.
\]

`certificate20.json` records the complete exact rational bounds; its values are
not inputs to a new accepting run. Equations (9)--(10) show that z↦z-RF(z) maps
C strictly into itself and is a strict contraction. Banach's theorem gives a
unique fixed point there. Since R is invertible, it solves (8). The triangular
moment-cumulant identities prove every equality in (2).

The direct interval check that each raw-moment box overlaps its source box is
only a diagnostic. It does not prove an equality or existence. The exact
source-bound contraction is the existence proof.

## 4. Complete infinite-theta reconstruction

The implementation `theta_source.py` is byte-identical to #988 at
86c156baa3f10296a26e066f5f4d276776b79c27, Git blob
fc51d49fe2bdbbde3fcb3928f1d82fd8baffbf53. It reconstructs all normalized
moments through 20 in 320-bit outward integer arithmetic. This source capability
is inherited; the degree 20 graph/root and its certification are new.

For n=1,...,6 integrate its summand to

\[
 U_n=(2,3/2,1,3/4,1/2,3/8)_n.
\]

Use 98 cells of width 1/16, with counts (32,24,16,12,8,6). On each cell centered
at c, let h=1/32 and expand the density in(t-c)/h through degree D=120. Multiply
the polynomial by the exact polynomial t^j and integrate it, keeping the
full-line factor2, for every j=0,2,...,20. The following remainders are all paid.

**Taylor tail.** On the complex circle |t-c|=1/8, Re exp(2t)>0, and the density
prefactor is bounded by 10^11 for all six indices and all centers below 2. Indeed
q_n<144 and Re t<17/8 give
4*144^2*3^10+6*144*3^6<10^11. Cauchy's coefficient estimate, the radius ratio1/4,
the real bound t^j<=2^j, and total full-line integration length 49/4<16 give

\[
 E_j=\frac{16\,10^{11}2^j}{4^{121}(3/4)}.
 \tag{11}
\]

This tail is subtracted from the lower polynomial integral and added to its
upper endpoint.

**Six time tails.** For t=U+u put q=pi*n^2, E=exp(2U) and
lambda=2qE-9/2>0. Dropping the negative prefactor term and using
exp(2u)>=1+2u gives the full-line tail bound

\[
 T_{n,j}=8q^2e^{9U/2-qE}
 \sum_{k=0}^{j}\binom jk U^{j-k}\frac{k!}{\lambda^{k+1}}.
 \tag{12}
\]

Every n=1,...,6 tail is included.

**All indices n>=7.** At U=0 the analogous bound is
8*pi^2*n^4*exp(-pi*n^2)*j!/(2*pi*n^2-9/2)^(j+1). Consecutive numerators have
ratio at most(8/7)^4*exp(-15*pi)<1/2, while the denominator increases. Hence
the entire omitted-index tail is bounded by

\[
 N_j=\frac{16\pi^2 7^4e^{-49\pi}j!}{(98\pi-9/2)^{j+1}}.
 \tag{13}
\]

By positivity, (12) and (13) are added to the upper endpoint only. None is set
to 0. Normalize by the enclosed positive mass, enclose the variance v and
standardize by v^r, then use (6) to produce all ten s_r intervals.

The inherited primitive has interval endpoints in 2^-320 times the integers.
Multiplication, reciprocal and squaring round outward using integer floor and
ceiling. Pi uses Machin's identity with 96-term alternating arctangent series
and their first omitted terms. Exponentials use argument scaling to [0,1/8],
96 positive Taylor terms, a bound beginning with term 97, and outward squaring;
negative arguments use outward reciprocals. This is inherited directed
arithmetic, not a separately developed transcendental implementation.

`pr886_primitive.py` has SHA256
2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55,
authenticated before use. It is the #988 file, 6534 bytes, Git blob
c32015f110d10186538ffabcb4689ba5bbc060d0. Compared with original #886's
6533-byte primitive at d998605c0718e332ac503baf078704b862f8250e, it has exactly
one extra final newline. Removing that newline gives original Git blob
712bb0f0114cbba85e8082c3130ebf09b53e8936. No backend algorithm changed.

## 5. Real zeros and the zero-weight hub

The classical finite ferromagnetic Lee--Yang theorem applies to every finite
zero-field Ising model with nonnegative pair couplings and nonnegative real
observable weights. Unequal and irrational positive weights are allowed. It
states that the moment generating function has only imaginary zeros, or
equivalently that the characteristic function has only real zeros.

If using the strictly-positive-weight formulation, temporarily give the hub
weight delta > 0 while holding all edges fixed. Every resulting characteristic
function is zero-free off the real axis. As delta decreases to 0, the finite
configuration sums converge locally uniformly to the actual characteristic
function. Its value at 0 is 1, so Hurwitz's theorem preserves zero-freeness in
both open half-planes. The zero-weight hub therefore causes no gap.

This conclusion concerns the finite model just constructed. Its first 20
moments coincide with theta's; the entire functions have not been identified.

## 6. Independent finite assembly and executed controls

`check_connected.py` independently enumerates all 128 configurations of a
seven-vertex fixture: the hub, two fair leaves and two unequal dimers. It
forms (4) directly, verifies normalization and all odd moments, and compares
every raw moment of orders 0 through 20 against the conditional recurrence.
A separate deletion of a positive internal edge changes the variance.

The same script independently builds the complete 305-spin generating function
at the rational center by multiplying component Taylor polynomials and taking
integer powers for all multiplicities. It compares all raw orders 0 through 20
exactly, with Fraction arithmetic, against the cumulant implementation. This
checks the complete 305-spin finite assembly, while the root itself is supplied
by Section 3. It is not a 2^305-state enumeration or a second theta backend.

The replay executes four distinct optimized corrupted subprocesses. Removing
the hub correlations, reversing an inner-amplitude orientation, or reducing
the fair-leaf multiplicity must fail the complete finite-assembly equality.
Omitting order 20 must fail the explicit complete-order predicate. The executed
replay receipt records every return code and required failure message.

The ordinary and optimized full-source checkers must reproduce the identical
certificate, and the ordinary and optimized finite-assembly scripts must
reproduce their identical receipt. Assertions are not used as acceptance
predicates; failed requirements raise exceptions even under optimized Python.

## 7. Why the numerical search could escape the old boundary

The initial #988 chart had one substantial unequal dimer and many nearly
independent signs. Weak positive-edge insertions in that chart did not reach
the next target. The successful exploration instead split observed signs into
almost-aligned unequal dimers. Algebraically, the symmetric two-spin law is

\[
 \frac p2(\delta_A+\delta_{-A})+
 \frac{1-p}{2}(\delta_B+\delta_{-B}).
 \tag{14}
\]

At p=1 it is exactly a fair sign of amplitude A; at p=1/2 it is exactly the
sum of two independent fair signs of amplitudes (A+B)/2 and (A-B)/2. Those are
exact distributional identities. The first endpoint is only a limiting
infinite-coupling description when represented as two observed spins; it is
treated as a single spin in that boundary chart.

When a component reached p=1/2 during exploration, it was decomposed into those
two independent signs. Splitting them again created additional graph freedom
while preserving the old boundary law exactly. After the degree 20 scout was
found, a positive hub was added, ten coordinates were refined, and the entirely
separate directed checker proved the stated interior finite model.

The published theorem does not rely on continuity of the exploratory path, on
the accuracy of its intermediate projections, or on any unbounded repetition
of this operation. No global path was interval-certified. The two boundary
identities are elementary; the contribution is the actual theta-target root
obtained and checked after this change of architecture.

## 8. Remaining full-proof requirement

The #981 compactness consumer correctly observes that bounded variance already
gives common analytic bounds for real-zero finite spin laws. For a sequence
whose theta moments agree through unbounded orders, local uniform convergence
and Hurwitz would therefore give RH; separate bounds on graph size, support,
couplings or inverse Jacobians are not required. Approximation of every fixed
moment would also suffice.

T20D supplies one additional finite order. It does not show that sign splitting
always reaches the next theta target, that a usable chart survives every
extension, or that this finite success repeats without bound. That global
feasibility problem remains open.
