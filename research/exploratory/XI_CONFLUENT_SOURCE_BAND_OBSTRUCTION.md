# Xi confluent source-band obstruction

Status: NEW ANALYTIC THEOREM AND EXACT CONTROLS; FROZEN-SOURCE REVIEW REQUIRED.

Scope: one finite confluent denominator cluster, its literal source-Pick jet
metric, and the actual Xi accepted source-frequency envelope at fixed odd order.
No physical inner-weighted band estimate, all-distinct-node theorem, or RH claim.

Exact dependencies: ten Git/blob/LF-SHA-256 bindings in the companion manifest.
The actual-kernel proof is pinned at 3b6972320899a82c6caa3a98e2ada5ff703a605a;
its independent review is pinned at f3d074190e64a97ac935b93c5b628568cde90858.
The original sources and earlier scout remain immutable.

What was actually run: exact rational Laguerre polynomial integrals, differential
identities, finite Gram/jet congruences, and explicit countercontrols. The checker
authenticates the frozen sources; it is not a formal verifier of the analysis.

Smallest remaining gap: the native inner-weighted band Gram and collective
denominator geometry have not been controlled. XICARRIERPICK106710 remains open.

## 1. Literal source, coordinates, and outer retention

Use the reduced finite endpoint pair in the pinned L-106671:
\[
 N=OB_+,\qquad D=OB_-,\qquad R=N-D.
\tag{CB1}
\]
The common outer factor O is holomorphic and nonzero at each retained denominator
node. Common factors are removed before the packet is formed. On a finite set of
denominator jets let E be the injective Hardy-kernel synthesis, G=E^*E, and let
V=J_{B_+} be the triangular multiplication-jet matrix in the convention of
L-106671. The literal regularized determinant is
\[
 {\mathfrak Z}_\tau=\frac{\det(G-\tau V^*GV)}{\det G},\qquad 0<\tau<1.
\tag{CB2}
\]
Stars mean Hermitian adjoints; the theorem permits complex nodes and jets.

At a simple node b, V has entry B_+(b)=R(b)/O(b). At a multiplicity-q
denominator node, R=OB_+ modulo the q-th power of the local parameter.
Consequently, in the same jet convention,
\[
 C=J_O\ \hbox{is invertible},\qquad CV=VC,\qquad J_R=CV=VC.
\tag{CB3}
\]
Commutation is in the finite local multiplication algebra. Neither C nor V
need commute with G or a band Gram.

For a measurable frequency set I, let Pi_I be multiplication by its indicator
on the Hardy Fourier realization L^2(0,infinity), and set G_I=E^*Pi_I E.
Put G_O=C^*GC and G_{O,I}=C^*G_I C. Then
\[
 \boxed{{\mathfrak Z}_\tau
 =\frac{\det(G_O-\tau J_R^*GJ_R)}{\det G_O}.}
\tag{CB4}
\]
Indeed C^*(G-\tau V^*GV)C=G_O-\tau J_R^*GJ_R, and the factors
det(C^*)det(C) cancel. Also, by cyclicity of trace,
\[
 \boxed{\operatorname{tr}(G_O^{-1}G_{O,I})
       =\operatorname{tr}(G^{-1}G_I),}
 \quad
 \boxed{\operatorname{tr}(G_O^{-1}J_R^*G_IJ_R)
       =\operatorname{tr}(G^{-1}V^*G_IV).}
\tag{CB5}
\]
More strongly, G_O^{-1}G_{O,I}=C^{-1}(G^{-1}G_I)C, so the complete
generalized localization spectrum is unchanged.

These are changes of finite frame E -> EC. They are not Fourier commutation
statements for multiplication by O, 1/O, the Riemann--Siegel gauge, or B_+.
In particular, (CB4) does not permit replacing G_O by G while keeping J_R.

For the native fifth frozen endpoint, L-106620 and L-106671 specify
\[
 N_j=R_{0,j}C_{5,j},\quad D_j=C_{0,j}R_{5,j},\quad
 R_j=2i\lambda_j(h\,DH_5-(Dh)H_5),\quad\lambda_j=\omega(t_j)^{-1}.
\tag{CB6}
\]
All the source values and jets in (CB3)--(CB5) are these actual values.
No freedom to choose their coefficients is assumed. The band quantity in
(CB5) is an explicitly defined source-jet quadratic form; it is not asserted
to equal the Fourier energy of the unnormalized Wronskian in (CB6).

## 2. One confluent denominator cluster: all multiplicities

Let b=a+iy with a real and y>0, and let q be any positive integer. The first q
derivative kernels at b span, in the normalization of L-106673,
\[
 M_{q,a,y}=\{p(\xi)e^{-(y+ia)\xi}:\deg p<q\}\subset L^2(0,\infty).
\tag{CB7}
\]
Harmless nonzero derivative normalizations give the same subspace. Its
orthogonal projection kernel is denoted K_q. For every xi>0,
\[
 \boxed{\xi K_q(\xi,\xi)\le q^2.}
\tag{CB8}
\]
The constant is absolute, independent of a,y,q. This is a coarse bound,
not a sharp-constant claim.

Here is a native proof, including the classical polynomial identities used.
Define
\[
 L_j(x)=\sum_{\ell=0}^j(-1)^\ell {j\choose\ell}\frac{x^\ell}{\ell!}
       =\frac{e^x}{j!}\frac{d^j}{dx^j}(e^{-x}x^j).
\tag{CB9}
\]
Repeated integration by parts gives integral e^{-x}L_j(x)x^k dx=0 for k<j.
All boundary terms vanish: at infinity they are polynomial times e^{-x};
at zero the derivatives of e^{-x}x^j of order below j vanish. For k=j
the integral is (-1)^j j!. The leading coefficient of L_j is (-1)^j/j!,
so
\[
 \int_0^\infty e^{-x}L_jL_\ell\,dx=\delta_{j\ell}.
\tag{CB10}
\]
Direct comparison of the finite coefficients in (CB9) gives, with L_{-1}=0,
\[
 xL_j=(2j+1)L_j-(j+1)L_{j+1}-jL_{j-1},\qquad
 xL_j''+(1-x)L_j'+jL_j=0.
\tag{CB11}
\]
Thus, for phi_j=e^{-x/2}L_j,
\[
 \int\phi_j^2=1,\qquad \int x\phi_j^2=2j+1,\qquad
 -(x\phi_j')'+\frac{x}{4}\phi_j=(j+\tfrac12)\phi_j.
\]
Multiplying the last identity by phi_j and integrating by parts (the same
endpoint control applies) proves
\[
 \int_0^\infty x(\phi_j')^2dx=\frac{2j+1}{4}.
\tag{CB12}
\]
For every x>0,
\[
 \begin{split}
 x\phi_j(x)^2
 &=-\int_x^\infty\{\phi_j(t)^2+2t\phi_j(t)\phi_j'(t)\}\,dt\\
 &\le2\left(\int_0^\infty t\phi_j(t)^2dt\right)^{1/2}
        \left(\int_0^\infty t\phi_j'(t)^2dt\right)^{1/2}
 =2j+1.
 \end{split}
\tag{CB13}
\]
The functions
\[
 \psi_j(\xi)=\sqrt{2y}\,e^{-(y+ia)\xi}L_j(2y\xi),\quad 0\le j<q,
\]
are an orthonormal basis of (CB7). Therefore
xi K_q(xi,xi)=sum_{j<q}(2y xi)phi_j(2y xi)^2<=sum_{j<q}(2j+1)=q^2,
which proves (CB8).

These identities are classical Laguerre analysis, also recorded in
[DLMF 18.3](https://dlmf.nist.gov/18.3),
[DLMF 18.9, Table 18.9.2](https://dlmf.nist.gov/18.9.T2), and
[DLMF 18.8](https://dlmf.nist.gov/18.8). No novelty is asserted for them.
The application and explicit source boundaries are the contribution here.

## 3. Exact nonlocal band and source-jet inequalities

For 0<A<B, integration of (CB8) gives
\[
 \boxed{\operatorname{tr}(P_M\Pi_{[A,B]}P_M)
 \le\min\{q,q^2\log(B/A)\}.}
\tag{CB14}
\]
The trace here is on the q-dimensional subspace M. Positivity and the
operator bound Pi_I<=1 give, with epsilon=min(1,q^2 log(B/A)),
\[
 \boxed{G_{[A,B]}\le\epsilon G.}
\tag{CB15}
\]
Equivalently every unit vector f in M has integral_A^B |f|^2<=epsilon.
This holds for every vector, hence also for the actual constrained source
jets; it does not require any ability to vary their coefficients.

Congruencing (CB15) by J_R and contracting with the positive matrix G_O^{-1},
\[
 \boxed{\operatorname{tr}(G_O^{-1}J_R^*G_{[A,B]}J_R)
 \le\epsilon\,\operatorname{tr}(G_O^{-1}J_R^*GJ_R).}
\tag{CB16}
\]
Thus the common outer values and all their required jets remain in the exact
denominator metric. The statement covers ill-conditioned derivative frames:
no frame-condition-number estimate replaces the Gram whitening.

For a general measurable I with finite integral_I dxi/xi, the same proof gives
trace<=q^2 integral_I dxi/xi. For the Xi application it suffices to enclose
the accepted set by one positive interval.

## 4. Uniform actual-Xi accepted-frequency envelope

Fix a positive odd integer K and M>0. They do not grow with X. Set lambda=2/X
and, exactly as in the earlier scout, restrict xi to [X/2,2X]. Use the literal
Xi g_K,p_K,rho of XL6--XL7 in the reviewed concentration source. That source
proves as xi tends to infinity
\[
 g_K(\xi)\sim\frac{\pi}{K}\xi^2e^\xi,\qquad
 p_K(\xi)\to\frac1{2K},\qquad
 \rho-p_K=(\eta-1)\{p_K-g_K(1+1/\eta)\},\quad\eta=\xi/X.
\tag{CB17}
\]
No growing-K assertion is imported. Define
\[
 S_X=\{\xi\in[X/2,2X]:|\rho_{K,2/X}(\xi)|\le M\}.
\]
There exists a nonnegative r_X tending to zero such that, for all sufficiently
large X,
\[
 \boxed{S_X\subset[A_X,B_X],\quad
 A_X=X+(c_--r_X)\frac{e^{-X}}X,\quad
 B_X=X+(c_++r_X)\frac{e^{-X}}X,}
\]
\[
 c_\pm=\frac1{4\pi}\mathbin{\pm}\frac{KM}{2\pi},\qquad
 \boxed{\log(B_X/A_X)=
        \left(\frac{KM}{\pi}+o(1)\right)\frac{e^{-X}}{X^2}.}
\tag{CB18}
\]
This asserts only containment, not that S_X is an interval or that rho is
monotone in xi. Monotonicity in eta with xi held fixed is not substituted for
monotonicity along the physical line eta=xi/X.

Proof of uniformity: the limits in (CB17), by their definition, hold uniformly
on the tail xi>=X/2. In particular p_K is uniformly bounded, g_K is bounded
below by a positive fixed multiple of xi^2 e^xi, and eta lies in [1/2,2].
For xi in S_X the exact identity first gives
\[
 |\eta-1|\le\frac{M+|p_K|}{g_K(1+1/\eta)-p_K}
          =O_{K,M}(e^{-\xi}/\xi^2).
\tag{CB19}
\]
Its denominator is positive for all sufficiently large X. Initially
|xi-X|=O_{K,M}(e^{-X/2}/X)=o(1), uniformly on S_X. It follows that
xi/X->1 and e^{xi-X}->1 uniformly there. Substitution back in (CB19)
improves this to |xi-X|=O_{K,M}(e^{-X}/X). Finally (CB17) gives uniformly
on the same possibly disconnected set
\[
 \boxed{\xi-X=
 \left(\frac{1-2K\rho_{K,2/X}(\xi)}{4\pi}+o(1)\right)\frac{e^{-X}}X.}
\tag{CB20}
\]
This follows by solving the exact linear expression for eta-1; the bounded
rho and the uniform asymptotics control the error. Taking a uniform error
majorant (and zero if S_X is empty) proves (CB18). The logarithm expansion
uses A_X/X,B_X/X->1. There is no inversion of a merely pointwise limit.

For one confluent packet, allow a=a(X), y=y(X)>0 and positive integer q=q(X)
arbitrarily. Equations (CB14)--(CB18) give
\[
 \operatorname{tr}(P_M\Pi_{S_X}P_M)
 \le q(X)^2\left(\frac{KM}{\pi}+o(1)\right)\frac{e^{-X}}{X^2}.
\tag{CB21}
\]
The o(1) depends only on fixed K,M, not on q,a,y. In particular, if
\[
 \boxed{q(X)=o(Xe^{X/2}),}
\tag{CB22}
\]
every unit-vector band mass, and the relative source-jet band energy in
(CB16) when its total is nonzero, tends to zero. If the total is zero,
(CB16) says the band energy is also zero. No division by a zero charge occurs.

This obstructs a strategy requiring these denominator/source-jet vectors to
concentrate in the accepted scalar band. It does not identify scalar Xi
source energies with the physical Pick defect or prove any free-energy bound.
For M=0 one can get a zero-width leading envelope with an o(e^{-X}/X) error,
but no positive-width asymptotic or singleton assertion is made here.

## 5. Why multiplicity and the physical inner factor cannot be suppressed

### Unbounded multiplicity: a countercontrol at fixed height

For every fixed real a and y>0,
\[
 \overline{\bigcup_{q\ge1}M_{q,a,y}}=L^2(0,\infty).
\tag{CB23}
\]
If f is orthogonal to this union, its Laplace transform
F(z)=integral_0^infinity f(xi)e^{-z xi}dxi is analytic on Re z>0 by
Cauchy--Schwarz and locally dominated differentiation. Orthogonality means
all derivatives of F vanish at z=y-ia. The identity theorem makes F zero
on the right half-plane. For any sigma>0, F(sigma+it) is the Fourier
transform of the L^1 function e^{-sigma xi}f(xi), extended by zero to the
negative line. Fourier uniqueness gives f=0.

Hence for any nonempty positive interval and any epsilon>0 some finite q
and some unit vector in M_q have interval mass greater than 1-epsilon:
approximate a unit interval-supported function and normalize. There can be
no localization bound vanishing with interval width uniformly over all q.
This is an abstract model-space statement, not a claim about actual Xi
multiplicities, coefficient freedom, or a quantitative converse to (CB22).

### Physical inner multiplication: an exact noncommutator

In the Fourier convention F(t)=(2pi)^(-1/2)integral f(xi)e^{it xi}dxi, let
B(t)=(t-i)/(t+i), a finite Blaschke factor. Physical multiplication is
\[
 (\mathcal B f)(s)=f(s)-2\int_0^s e^{-(s-u)}f(u)\,du.
\tag{CB24}
\]
For f(s)=e^{-s} and I=[A,B_0] with 0<=A<B_0, at s>B_0,
\[
 ((\Pi_I\mathcal B-\mathcal B\Pi_I)f)(s)
 =2(B_0-A)e^{-s}.
\tag{CB25}
\]
Thus the squared tail norm is exactly
2(B_0-A)^2 exp(-2B_0)>0. For A=1,B_0=2 the coefficient is 2 and the
tail exponent is -4. These are symbolic exact constants, not a floating
transcendental evaluation. This toy is not Xi data.

For the native numerator inner factor the physical band Gram instead is
\[
 G_{I,B_+}=E^*M_{B_+}^*\Pi_I M_{B_+}E.
\tag{CB26}
\]
Nothing above replaces (CB26) by G_I or commutes its factors. Orthogonalizing
multiple denominator clusters can also introduce inner multipliers, so
(CB8) is not silently promoted to arbitrary distinct-node configurations.

## 6. Bounded exact controls and provenance

The companion producer uses only integer/rational arithmetic, with e^{-2},
pi, and exponential asymptotic scales treated as symbolic labels. It proves
finite polynomial identities and authenticates sources, not analytic limits.

- Laguerre orders j=0,...,7: all 64 cross-orthogonality integrals, recurrence,
  differential equation, first moment, derivative energy, and q^2 summation.
  The public polynomial control allows j<=8; larger inputs fail closed.
- Two actual rational Hardy model controls, q=2,3, in the basis
  e_j(xi)=xi^j e^{-xi}/j!. Their G entries are
  (i+j)!/(i!j!2^{i+j+1}). For I=[0,1],
  G_I=G-zH, z=exp(-2), with
  H_ij=G_ij sum_{m=0}^{i+j}2^m/m!.
- Take the zero-free outer function O(t)=4/(1-it) and
  B_+(t)=(t-i/2)/(t+i/2), while B_- has its q-fold zero at i.
  In the adjoint-kernel jet convention C_ij=4/2^{j-i+1} for j>=i;
  V_ii=1/3 and V_ij=-(2/3)^{j-i+1} for j>i.
  The negative upper entries follow by applying the adjoint of (CB24)
  with height 1/2 to e_j. The matrices C,V commute with each other but
  neither commutes with G or H (hence not formally with G_I).
- The checker verifies the determinant congruence at tau=1/2, all characteristic
  coefficients of the generalized band-metric pencil, both source-band trace
  coefficients, and strict disagreement when the outer metric is dropped.
  It also checks G positive definite and G-V^*GV positive semidefinite by
  every principal minor. These controls are rational real specializations of
  the complex theorem; actual Xi jets are not sampled.
- A held-out q=4 test uses the same native model formulas. The physical
  inner/projection noncommutator is checked from its exact Volterra tail.
- Fixed odd K=1,3,...,15 and M=1/2,1,2 check the rational coefficients of the
  center, endpoints, and logarithmic width, with 1/pi symbolic. These finite
  constants do not establish the unbounded asymptotic theorem.

Hard caps: q<=8 for polynomial panels, matrix size<=4, at most 20 polynomial
coefficients, and 128-bit rational inputs. Public functions reject booleans,
floating point, noninteger orders, malformed matrices, and oversized input
before expansion. The complete fixed report has 64 orthogonality cells,
8 Laguerre energy rows, 8 multiplicity rows, 2 matrix controls and 24 phase
rows; no unbounded search or numerical Xi computation runs.

The manifest contains exact commit, Git blob and LF-normalized SHA-256 for
each of ten frozen sources, including the independent concentration review.
External DLMF formula contracts are authenticated as declared metadata only;
remote page bytes and formal analytic proofs are not machine-authenticated.
The fixture binds note, producer, tests, and manifest by LF-normalized hashes,
plus a canonical-JSON manifest hash. Acceptance is exact typed canonical-JSON
equality to a complete source-authenticated rebuild, not subset agreement.
Changing a source or any bound file requires a new artifact identity.

Replay completed: all 23 new tests and the new producer pass in normal Python
and under -O. The 15 actual-kernel and 23 earlier-scout tests, and both adjacent
producers, also pass in both modes. Ruff lint/format and whitespace checks pass.
These are source/algebra replays, not independent analytic verification.

Replay commands:
```text
python research/exploratory/xi_confluent_source_band_obstruction.py --check
python -O research/exploratory/xi_confluent_source_band_obstruction.py --check
python -m unittest discover -s tests -p test_xi_confluent_source_band_obstruction.py
python -O -m unittest discover -s tests -p test_xi_confluent_source_band_obstruction.py
```

The new packet requires independent exact-SHA review. Its load-bearing new
analytic statements are (CB13), the uniform bootstrapping in (CB19)--(CB20),
and faithful separation of (CB5) from (CB26). A finite replay cannot replace
those proofs. No topological-index charge is removed, no percentage of
critical-line zeros is inferred, and RH remains unsolved.
