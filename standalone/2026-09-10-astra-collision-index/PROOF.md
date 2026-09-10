# Collision index, boundary phase, and an exact-source heat-flow programme

Date: 2026-09-10. Local labels HCI1--HCI7.
**Status: proposed component arguments and a new research direction for this thread;
independent mathematical/code review required. RH and the uniform theta boundary
estimate are NOT proved.** No new upper bound for the de Bruijn--Newman constant
is asserted. This packet contains no actual theta boundary computation.

The intended change of method is from an all-order moment/sign problem to a
noncancelling topological event count. It uses classical de Bruijn--Newman flow,
Hermite collision normal forms, Sturm zero-number ideas and Brouwer degree.
We do not claim priority for these mechanisms or for an RH reformulation.
The contribution proposed here is the explicit all-multiplicity degree formula,
its symmetry/normalization-aware boundary contract, and a tested route for
turning a source-specific phase estimate into a global conclusion.

## 1. Fix the source and the heat normalization

Use the normalization of D.H.J. Polymath, arXiv:1904.12438v2:

\[
 H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                         e^{-\pi n^2e^{4u}}.
\tag{1}
\]

The full source is even by Jacobi inversion, strictly positive, and decreases
faster than every Gaussian in either direction. On compact complex parameter
sets, the integral and all derivatives converge uniformly. Thus H is jointly
analytic in t,z, real on real parameters, even in z, and

\[
 \partial_tH_t=-\partial_z^2H_t,\qquad
 H_0(z)=\tfrac18\xi(\tfrac12+iz/2),\qquad H_t(0)>0.
\tag{2}
\]

Here xi is the entire continuation with xi(0)=xi(1)=1/2. If the other repository
convention is \(\Xi(v)=\int_{\mathbb R}\phi(s)e^{ivs}ds\), with coefficients
4/6 and exponents 9s/2,5s/2, then \(\phi(2u)=2\Phi(u)\) and

\[
 \int_{\mathbb R}\phi(s)e^{(t/4)s^2}e^{i(z/2)s}ds=8H_t(z).
\tag{3}
\]

Time, height and scalar normalizations all matter. This is not a changed
finite theta truncation. Classical facts imported from [P] are identified in
Section 5; no result on the new spectral or Ising branches is a proof input.

## 2. HCI1: all real collisions have the same orientation

For any jointly real-analytic nonzero solution of \(H_t=-H_{xx}\), define

\[
 G(t,x)=(H(t,x),H_x(t,x)),\qquad W(t,x)=H(t,x)+iH_x(t,x).
\tag{4}
\]

The domain orientation is **(t,x)**, in that order. W is not assumed holomorphic
in the artificial variable t+ix; we use real Brouwer degree, not the holomorphic
argument principle in that variable.

At an ordinary double zero,

\[
 DG=\begin{pmatrix}-H_{xx}&0\\-H_{xxx}&H_{xx}\end{pmatrix},
 \qquad\det DG=-H_{xx}^2<0.
\tag{5}
\]

The general Jacobian is \(-H_{xx}^2+H_xH_{xxx}\), which need NOT be negative
away from critical points. No global pointwise Jacobian sign is asserted.

**Theorem HCI1.** Suppose H(t0,.) has a real zero x0 of finite multiplicity
m>=2. The common zero of (H,H_x) is isolated in real (t,x), and its local degree is

\[
                   \operatorname{ind}_{(t_0,x_0)}G=-\lfloor m/2\rfloor.
\tag{6}
\]

In particular an even-multiplicity collision cannot be hidden by some event of
opposite orientation; neither can an odd higher-multiplicity event.

### 2.1 Universal local model and isolation

Let

\[
 P_m(\tau,y)=e^{-\tau\partial_y^2}y^m
 =\sum_{j=0}^{\lfloor m/2\rfloor}
       \frac{m!(-\tau)^j y^{m-2j}}{j!(m-2j)!}.
\tag{7}
\]

It obeys \(\partial_yP_m=mP_{m-1}\), \(\partial_\tau P_m=-\partial_y^2P_m\).
For positive tau it is the scaled monic Hermite polynomial
\((2\tau)^{m/2}\operatorname{He}_m(y/\sqrt{2\tau})\), with m distinct real roots.
For negative tau its roots are the corresponding imaginary multiples; only
the central root in odd degree is real.

Write H(t0,x0+y)=a_m y^m+O(y^{m+1}), a_m!=0. The heat equation identifies its
joint Taylor coefficients: a term \(\tau^p y^q\) has coefficient
\((-1)^p(q+2p)!a_{q+2p}/(p!q!)\). Consequently, locally uniformly on bounded
real tau,y sets, including the y derivative,

\[
 \big(r^{-m}H(t_0+r^2\tau,x_0+ry),\;
      r^{1-m}H_x(t_0+r^2\tau,x_0+ry)\big)
 \longrightarrow a_m(P_m,\partial_yP_m).
\tag{8}
\]

Analyticity justifies the convergent Taylor remainders here; this is not a
finite differentiability assertion. The same Hermite/Rouche argument yields m
simple roots for each sufficiently small nonzero time displacement in a fixed
complex neighborhood of x0. These are all the local roots. Hence no other
common real zero approaches (t0,x0). This is the classical collision normal
form; [P, Proposition 3.1(ii)] supplies its explicit root statement and proof.

The model pair (P_m,partial_y P_m) has no real common zero except (0,0).
For tau>0 this follows from simplicity of Hermite roots. For tau<0, even m
has P_m strictly positive, while odd m has partial_y P_m strictly positive
on the real axis. At tau=0 only y=0 can be common. Uniform convergence on a
fixed rectangle boundary avoiding that point transfers the degree in (8).
Positive parabolic coordinate rescaling preserves orientation; multiplying
both output components by the same nonzero real a_m has determinant a_m^2>0.

### 2.2 Compute the model degree, including every multiplicity

Perturb the target from (0,0) to (epsilon,0), epsilon>0 small.
For tau>0 the critical points have y=sqrt(tau)r, with r a simple real root
of P_(m-1)(1,.), and the critical value equals tau^(m/2) P_m(1,r).
Thus each positive critical value at tau=1 produces exactly one preimage
of the target. Interlacing and the alternating extrema of a monic real-rooted
polynomial give:

- m=2k: k-1 positive critical values for positive tau;
- m=2k+1: k positive critical values for positive tau.

For negative tau, if m is even, the only real critical point is y=0, since
partial_y P_m is y times a polynomial in y^2 with strictly positive coefficients.
Its value is a positive constant times (-tau)^k, giving one further preimage.
If m is odd, partial_y P_m is strictly positive and there is none.
There are no preimages at tau=0. All these finitely many preimages tend to the
origin with epsilon. At every one, partial_y^2 P_m is nonzero and the Jacobian
is -(partial_y^2 P_m)^2. Summing the negative unit signs gives exactly -k.
This proves (6), not merely its double-zero special case.

Equivalently, the forward change in the local real-root count is
2 floor(m/2); the local degree is minus half that increase. This is consistent
with classical Sturm zero-number monotonicity after reversing time [A].

## 3. HCI2: a boundary winding counts collisions without cancellation

Let R be a compact rectangle in a real-analytic heat domain. Assume H(t,.) is
not identically zero at any point of R and G is nonzero on the entire boundary.
The isolated common zeros in R are finite: an infinite set in that compact set
would have an accumulation point, either on a zero-free boundary or at an
isolated interior zero. Brouwer degree additivity and (6) give

\[
 \boxed{\operatorname{wind}_{\partial R}(H+iH_x)
     =-\sum_{(t,x)\in R:\,H=H_x=0}\lfloor m(t,x)/2\rfloor.}
\tag{9}
\]

The boundary is counterclockwise in (t,x). In differential form notation,

\[
 2\pi\operatorname{wind}_{\partial R}W
   =\oint_{\partial R}\frac{H\,dH_x-H_x\,dH}{H^2+H_x^2}.
\tag{10}
\]

**Zero winding excludes EVERY real collision inside R.** A nonzero negative
winding certifies collisions, with the weights in (9); it is not a count of
all complex zeros. An ordinary simple H-zero on the boundary is allowed:
H_x is then nonzero. Only a common zero makes the boundary certificate fail.

### Symmetry makes a one-sided budget enough

For the actual even H in (1), H_t(0)>0 excludes axis collisions. On a symmetric
rectangle [a,b] x [-X,X], collisions occur in equal-multiplicity pairs at +/-x.
Therefore its winding is a nonpositive EVEN integer. Consequently

\[
 \operatorname{wind}_{\partial R}W>-2
       \quad\Longrightarrow\quad\operatorname{wind}_{\partial R}W=0.
\tag{11}
\]

Equivalently a strict lower bound greater than -4pi for the circulation in
(10) is sufficient. This is a quantized global boundary budget, NOT an asserted
bound for the actual source. Nested rectangles have nonincreasing winding;
the decrease is precisely the collision weight entering their difference.
Shared boundary contributions cancel exactly when certified rectangles are tiled.

This differs from a signed divisor index with positive and negative events.
The sign restriction in (9) is the reason zero charge is informative here.
It does not repair or reinterpret the different quotient indices in PR #729.

## 4. HCI3: safe normalization and a finite boundary certificate

### 4.1 Remove amplitude without changing the event count

Let A(t,x)>0 be C1 (and sufficiently smooth for any derivatives used below),
and put F=H/A. Then

\[
 \binom F{F_x}=\begin{pmatrix} A^{-1}&0\\-A_xA^{-2}&A^{-1}\end{pmatrix}
 \binom H{H_x}.
\tag{12}
\]

The matrix field is homotopic through positive lower-triangular matrices to
identity. Thus it preserves zero-free boundaries, winding and local indices.
In particular use the derivative of the actual quotient, including A_x;
(H/A,H_x/A) is not (F,F_x), though positive scalar scaling alone also preserves
the index. On the normalized function the equation is

\[
 F_t=-F_{xx}-2(A_x/A)F_x-(A_t+A_{xx})F/A.
\tag{13}
\]

No missing drift or zero-order term may be discarded. Polymath's work explains
why removing the very small gamma envelope is essential at high frequencies.
Its complex B_t normalization is not silently substituted for a positive real
A here; one possible positive real envelope is |B_t| on its zero-free domain,
with its derivative and chosen coordinate domain explicitly accounted for.

### 4.2 A reference phase only needs to work on the boundary

If a continuous real phase theta is defined on all of R, its boundary reference
jet (cos theta,-sin theta) has winding zero. Any actual normalized boundary jet
whose Euclidean error from this reference is strictly below one is homotopic
to it through nonzero vectors. It therefore has zero degree and no collisions.
A general nonzero reference boundary curve with known winding can be used too.

**This does not supply theta for the arithmetic source.** Defining theta by a
logarithm whose existence already requires zero winding is circular. A gamma-only
or fitted cosine reference is not automatically accurate near irregular roots.
The intended research task is a source-derived reference/homotopy or the weaker
one-sided budget (11), uniformly in the exhaustion of Section 5.

### 4.3 Full continuum error, not sampled winding

Let w:[0,1]->C be a twice continuously differentiable boundary segment and let
l be the chord between its exact endpoints. If sup|w''|<=M, the elementary
Dirichlet Green bound gives

\[
             |w(v)-l(v)|\le M v(1-v)/2\le M/8.
\tag{14}
\]

If the distance of the chord from zero is >M/8, the whole segment and its chord
are nonzero and homotopic. With uncertain endpoints, add their uniform chord
error radius to M/8. Every side and corner must be included, in order, without
gaps. Sum the exact polygon winding only after every tube is paid. This chord
bound is classical and already occurs in the repository's L-3104 / PR #33.

The included implementation reconstructs exact rational polynomial heat families.
It restricts their jets to every edge, rescales each dyadic subsegment to [0,1],
and bounds M by the sum of absolute real/imaginary coefficients of the full second
derivative polynomial. That l1 bound dominates the complex modulus. The exact
closest point on a chord uses a clipped rational projection. Polygon winding
uses signed rational ray crossings, with segments through zero forbidden.
The independently checked ordered partitions cover all four sides. An insufficient
budget triggers subdivision or a refusal, never sampled acceptance.

This is a COMPLETE finite algorithm on zero-free polynomial boundaries: if the
boundary jet has positive minimum modulus, sufficiently small subdivisions have
tubes separated from zero. Its bounded depth implementation may return
inconclusive earlier. It supplies no oracle for the actual theta endpoints.

## 5. HCI4: the end-to-end RH implication, with the infinity boundary paid

The named classical inputs are:

1. Every zero of H_t is real for t>=1/2, and reality is preserved as t increases
   [de Bruijn/Polya, as stated in P, Introduction and Theorem 3.2].
2. For every a>0, all zeros at sufficiently large absolute real part are real
   and simple UNIFORMLY for t in [a,1/2]. This follows from [P, Theorem 1.5(i),(ii)]
   after enlarging its absolute constant; its scale is exp(C/a). The theorem's
   displayed C is not an instantiated numerical cutoff in this packet.
3. The zero strip remains bounded for 0<=t<=1/2 by the classical strip-contraction
   theorem, starting from the known critical strip of xi [P, Theorem 3.2].
   No assertion that all zeros were already on the critical line is used.

Consider the explicit nested rectangles

\[
              R_j=[2^{-j},1]\times[-2^j,2^j],\qquad j=1,2,\ldots.
\tag{15}
\]

**Theorem HCI4.** For the actual H in (1), the following are equivalent:

(a) RH;
(b) there is no real common zero H_t(x)=H'_t(x)=0 with t>0;
(c) on every boundary in (15), G is nonzero and its winding is >-2;
(d) on every such boundary G is nonzero and its winding is zero.

Proof. Under RH, reality preservation makes all zeros real at each t>0.
A multiple real zero there would, by (7)--(8), produce nonreal roots at a
slightly earlier still-positive time. Thus all these zeros are simple: (a)->(b).
Equation (9) proves (b)->(d); (d)->(c) is immediate; (11) gives (c)->(d).
Every point with 0<t<1 lies in the interior of some R_j. Hence (d) excludes
all collisions at these times. Times t>1/2 are already simple by applying the
same local splitting argument to the known real-rooted interval. This gives (b).

For completeness, (b)->(a) must address escape through infinity. Fix a>0 with
a<1/2 and let E be the subset of [a,1/2] where all zeros are real. It is closed
by local uniform convergence and Hurwitz (H_t(0)>0 prevents a zero limit function).
It is nonempty at t=1/2. It is also relatively open: use input 2 to dispose of all
sufficiently large real parts, uniformly on this time interval. Input 3 confines
all remaining potentially nonreal zeros to a fixed complex compact. At a time
in E, every remaining zero is simple by (b); a finite family of disjoint small
conjugation-symmetric disks and Rouche give one real zero in each for nearby
times. The rest of the compact is zero-free by a positive minimum modulus.
The compact can be enlarged slightly to have a zero-free vertical boundary at
the chosen time. Thus no nonreal zero can enter this argument from infinity.
Connectedness gives E=[a,1/2]. Since a is arbitrary, every positive-time H is
real-rooted. Taking t down to zero and using Hurwitz proves RH via (2). QED.

Simplicity of H_0 is NOT assumed or concluded. The exact model x^2-2t has a
double zero at t=0 and only simple real roots for every t>0. This route does not
accidentally strengthen RH to the simplicity conjecture. Nor does it require a
rightmost off-line zero or a largest collision height to exist globally.

**Unproved source obligation:** establish the boundary nonvanishing and one-sided
circulation budget (11) for every R_j, or another exhaustive family. A finite set
of successful rectangles is not enough. This criterion is RH-strength, not a
routine final lemma. The proposed gain is a different, one-dimensional and
integer-valued proof/certificate interface, not a logically weaker conjecture.

## 6. HCI5: complete-source bounds for that boundary interface

For q_n=pi n^2 exp(4u), write

\[
 \Phi_n(u)=e^{u-q_n}P_0(q_n),\qquad P_0(q)=2q^2-3q.
\tag{16}
\]

For a polynomial P=P(u,q,t), define the exact source derivative recurrence

\[
 \mathcal L_tP=P_u+4qP_q+(1+2tu-4q)P.
\tag{17}
\]

Then differentiating \(e^{tu^2+u-q_n}P(u,q_n,t)\) gives the same exponential
factor times \(\mathcal L_tP\). At t=0 its first polynomial is
\(-8q^3+30q^2-15q\). The included checker compares six such derivative steps
with a separately expanded formal Taylor series at rational parameters. Those
are algebra controls, not actual theta-value or modular-identity certificates.

The *infinite* source has vanishing odd derivatives at u=0 by evenness.
Individual terms and raw finite n truncations do not. A multiplier or integration-
by-parts argument must keep the full boundary cancellation and both omitted tails;
it cannot import a termwise positive shape or silently drop n>N.

Here are explicit elementary tail bounds usable for a real boundary oracle.
For 0<=t<=1, 0<=k<=5, U>=1 and m=N+1>=2, put

\[
 T_k(U)=\sum_{n\ge1}\int_U^\infty u^k e^{tu^2}\Phi_n(u)\,du,
 \quad A_U=(\pi/2)e^{4U}.
\]

Then

\[
 T_k(U)\le\frac{\pi}{e^{4U}}
                     \frac{e^{-A_U}}{1-4e^{-A_U}},
\tag{18}
\]

and the omitted indices on the finite interval satisfy

\[
 \sum_{n\ge m}\int_0^U u^ke^{tu^2}\Phi_n(u)\,du
 \le 2\pi^2U^{k+1}e^{U^2+9U}
        \frac{m^4e^{-\pi m^2}}{1-16e^{-\pi(2m+1)}}.
\tag{19}
\]

Proof. Positivity and \(\Phi_n\le2\pi^2n^4e^{9u-\pi n^2e^{4u}}\) reduce this
to a positive tail. For u>=1,

\[
 u^2+9u+k\log u\le u^2+14u<16u^3\le(\pi/2)e^{4u}.
\]

The middle inequality follows from
\(16u^3-u^2-14u=u[16(u-1)^2+31(u-1)+1]>0\); the last uses pi>3 and the cubic
term of exp(4u). Thus the nth integrand is at most
\(2\pi^2n^4\exp[-(\pi/2)n^2e^{4u}]\). Linearizing e^{4u} below at U and
integrating bounds its tail by
\(\pi n^2e^{-4U}e^{-A_Un^2}\). Since n^2<=4^(n-1) and n^2>=n, a geometric
series proves (18). On [0,U] bound the positive prefactors by their endpoint
ceilings; for n=m+j use (m+j)^4<=m^4 16^j and
(m+j)^2>=m^2+(2m+1)j. This proves (19). Both denominators are positive.

Every real x derivative through order five is bounded in absolute value by the
corresponding complete moment \(M_k(t)=\int_0^\infty u^ke^{tu^2}\Phi(u)du\).
On a straight edge (t,x)=(t0+a v,x0+b v), v in [0,1], the full second derivative
of W is

\[
 W_{vv}=a^2(H_{xxxx}+iH_{xxxxx})
       -2ab(H_{xxx}+iH_{xxxx})+b^2(H_{xx}+iH_{xxx}).
\tag{20}
\]

The M_k therefore give a paid bound in (14). Finite n/u parts can be enclosed by
convergent interval quadrature with (17), directed pi/exponential/trigonometric
primitives, and (18)--(19) for both omitted tails. Refining those finite parts
and precision yields arbitrary endpoint accuracy at every fixed real parameter.
The mathematical interface is effective; this packet has NOT implemented or run
that full theta oracle. High-frequency cancellation and useful relative error
remain a computational and analytic burden, not something these absolute bounds
make inexpensive. The fixed degree of the derivative bounds is not a fixed
precision/complexity claim as j grows.

A concrete next experiment is a collision-free collar containing a moving low
real zero over a positive time interval, certifying W on its four edges rather
than presuming H stays nonzero inside. A decisive theorem would control a
source-derived normalized boundary phase or (11) uniformly as j grows. Exact
modular endpoint cancellations and the integer-square source in (16) are the
specific structure not preserved by the following adversarial family.

## 7. HCI6: positive, strongly log-concave, fast-decaying sources can collide

Let g_2 be the centered Gaussian probability density of variance 2 and put

\[
 c=\frac e{1+e},\qquad
 w_0(u)=c g_2(u)+\frac{1-c}{2}\{g_2(u-1)+g_2(u+1)\}.
\tag{21}
\]

This is strictly positive, even and smooth. For t<1/4, d=1-4t, completing the
Gaussian square gives its exact Fourier heat transform

\[
 F_t(z)=d^{-1/2}e^{-z^2/d}
       [c+(1-c)e^{t/d}\cos(z/d)].
\tag{22}
\]

At t*=1/5, x*=pi/5, we have d=1/5, t*/d=1. The bracket is c(1+cos(5x)), so
F=F_x=0 while \(F_{xx}=25c\,d^{-1/2}e^{-x_*^2/d}>0\). Its Jacobian (5) is
strictly negative. This is an ACTUAL positive-time double collision of a changed
source, not a zeta zero or an approximate root plot.

For this equal-variance mixture,
\((\log w_0)''=-1/2+\operatorname{Var}(\mu\mid u)/4\le-1/4\), since its component
means mu belong to [-1,1]. Thus the source is already strongly log-concave.
To give it double-exponential tails and an entire heat parameter, set

\[
 w_\epsilon(u)=Z_\epsilon^{-1}w_0(u)e^{-\epsilon\cosh(2u)},\qquad\epsilon>0.
\tag{23}
\]

Positivity/evenness persist and the log-concavity only strengthens. Every
Gaussian tilt is now integrable. On a small closed parameter rectangle about
(t*,x*) with t<1/4, all required heat derivatives converge uniformly to the
unmodified Gaussian-mixture derivatives as epsilon down to zero, by Gaussian
domination. Choose its boundary with G nonzero and local degree -1. Degree
stability then forces a collision inside for every sufficiently small positive
epsilon. C1 convergence near the original point keeps H_xx bounded away from
zero, so those collisions are double. A continuous-parameter local uniqueness
argument can additionally isolate one; existence and multiplicity suffice here.

No extension to negative epsilon is used (the integral would fail), and no
numerical epsilon threshold is certified. This is a rigorous one-sided stability
argument, not a two-sided parameter IFT applied outside its domain.

Therefore positivity, evenness, strong log-concavity, all exponential moments
and double-exponential decay do NOT imply the proposed no-collision theorem.
The countermodel does not retain the exact modular/integer-square identity.
The route must use that missing structure; an anonymous source-shape argument
would incorrectly prove (23) collision-free.

## 8. HCI7: what was tested, and what has not been achieved

The written all-multiplicity result is not inferred from the finite tests.
`check.py` reconstructs 22 exact polynomial-heat controls, including multiplicities
2--12, shifted collisions, two distinct collision times, an even off-axis pair,
its two half-rectangles, the harmless zero-time double, and a forward-heat sign
control. Every accepted edge segment has its entire interpolation remainder
paid. `test_check.py` exercises missing/overlapping/reordered coverage, unbudgeted
curvature, boundary common zeros, orientation, scalar normalization, strict
receipt types, symlinks, and changed numerical/claim outputs.

There is no actual theta collar certificate, new Newman bound, finite-height zero
census, new all-order positive moment theorem, or RH proof in this packet. The
uniform source boundary budget is OPEN. Prior integration and research results
keep their own scopes. Publishing this research does not promote its proofs to
independently accepted mathematics.

## Sources and reading boundaries

[P] D.H.J. Polymath, *Effective approximation of heat flow evolution of the
Riemann xi function, and a new upper bound for the de Bruijn--Newman constant*,
arXiv:1904.12438v2 (2019), https://arxiv.org/abs/1904.12438v2 . Read the source
normalization, Introduction, Theorem 1.5 and Proposition 3.1, including page
images for the high-height statement and collision proof. The external global
asymptotic and real-root-preservation theorems are imported; their full proofs
and numerical campaigns are not independently reverified here.

[A] S. Angenent, *The zero set of a solution of a parabolic equation*, J. reine
angew. Math. 390 (1988), 79--96, DOI 10.1515/crll.1988.390.79;
https://authors.library.caltech.edu/records/tdcs5-h8b80 . Author/repository metadata
and abstract read for the Sturm-theory attribution. This is contextual, not a
substitute for the local proof in Sections 2--3.

Repository context: current main and AGENTS; PR #842's README/current description
for avoiding duplicate ferromagnetic synthesis; PRs #839--#841 descriptions for
trace/metric and feedback context; PR #33 description for the inherited chord
bound; PR #729 description for the different signed-index obstacle. Those PRs
are not imported as accepted theorem dependencies. The earlier local trace-Hankel
manuscript supplied motivation, not a theorem needed here. Exact sources and
inspection limits are in SOURCES.json.
