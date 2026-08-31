# The native geodesic measure, complete factor allocations and exchange projection

Status: exact finite-source identities and a proposed source-authenticated replay.
Validation: awaiting the parent agent's serialized run.
Scope: the primitive polarized current in L-102707, with its actual integration
measure and root convention. The transport to all post-renewal amplitudes in
T-106140 is not identified here.

## 1. A complete primitive dependency cone

Write the arithmetic coefficients of the L-102707 path as

\[
 a_\tau(n)=[z^n]\prod_p\ell_\tau(z_p),\qquad
 \ell_\tau(z)=\tau\sqrt{1-z}+(1-\tau)\sqrt{1-z^2}.
 \tag{1}
\]

The notation [z^n] means the prime-exponent monomial of n. Thus a_0=lambda^square
and a_1=lambda in the arithmetic normalization of L-102700. The physical field
coefficient is a_tau(n)/sqrt(n), as in L-102707. No second factor 1/sqrt(n)
is inserted when the normalized operator variable p^(-1/2)U_p is used.
Distinct source labels remain distinct before physical collapse; the example
below avoids the duplicated prime 67.

For an ordered factorization nm=K define

\[
 v_K(n)=2\int_0^1 a'_\tau(n)a_\tau(m)\,d\tau.
 \tag{2}
\]

Its physical coefficient is v_K(n)/sqrt(K). The native measure here is
**2 d_tau**, of total mass two, not a probability distribution. Expanding
a'_tau(n) gives one summand for each nonconstant left prime coordinate;
its derivative-site label and coefficient are retained in the replay.
There is no left unit term, since a'_tau(1)=0. The right unit is retained.

Every source exponent is nonnegative. Consequently the coefficient of a fixed
labelled K depends only on its prime labels and on allocations
0<=alpha_p<=v_p(K); an outside prime cannot occur and subsequently disappear.
This proves the finite dependency cone for this primitive. It is not a
statement about ancestral renewal records at a fixed terminal physical pair.

The source identity and its product-kernel observation are

\[
 \sum_{n\mid K}v_K(n)=\beta(K)-\beta^\square(K),\qquad
 H_{\rm def}(X)=(2D-1)\int_0^1 2\int
 \dot G_\tau(Y)G_\tau(X/Y)\,dY/Y\,d\tau.              \tag{3}
\]

All factor pairs with product K have the same observed kernel
(A*_M A)(X/K)/sqrt(K), followed by 2D-1. This is the signed Hankel current
of L-102707. It is not the positive ratio moment introduced below.

## 2. GE-1: the complete zero-chart current

Use the exact U=64 chart in the frozen predecessor diagnostic:

\[
 N=6(71\cdot73\cdot79)^2=1005930209094,\quad
 M=35(401\cdot421)^2=997518551435,\quad K=NM.          \tag{4}
\]

There are four exponent-one labels and five exponent-two labels, hence exactly
2^4 3^5=3888 ordered factorizations. All of them, including the right unit
and every derivative-site term, are used in the replay. Since K has both odd
and square prime exponents, beta(K)=beta^square(K)=0. Therefore the complete
native primitive coefficient in (3) is zero.

This cancellation does not set each factor allocation to zero. Put w=4-3tau.
At the displayed ordered pair,

\[
 a_\tau(N)=-\tau^2w^3/2048=:A(\tau),\qquad
 a_\tau(M)=\tau^2w^2/256=:B(\tau).                   \tag{5}
\]

The two oriented coefficients are 2 int A'B and 2 int B'A, exact nonzero
rationals recorded by the replay. Their sum is

\[
 v_K(N)+v_K(M)=2[A B]_0^1=-1/262144.                 \tag{6}
\]

The right-unit term also equals 2(a_1(K)-a_0(K))=-1/262144;
the left-unit term is zero. The other factor allocations supply the exact
compensating coefficient. No arbitrary weights have been assigned to the
24 Boolean histories of this chart: those histories belong to the later
canonical Boolean/completion map, not to (2).

There is a useful source-defined sector inside the complete factor sum. Require
each physical factor to have exactly two primes at odd exponent. The four odd
labels split two on each side, and each squared label goes wholly to one side.
There are 6*2^5=192 such ordered factorizations. The sector is swap invariant,
so its integrated sum is its endpoint product sum. Each endpoint product is
-1/524288; the sector sum is -3/8192. If both factors must have at least two
squared labels, the sector has 6*(10+10)=120 members and sum -15/65536.
Its complement has the opposite sum. These are physical exponent sectors of
the primitive, not an assertion that every canonical owner mask is this sector.

## 3. GE-2: an actual exchange projector and its preserved observations

On the finite factor space of K let J e_n=e_(K/n), and set
P_+=(I+J)/2, P_-=(I-J)/2. The coefficient identity

\[
 2\dot\Lambda\otimes\Lambda
 =\partial_\tau(\Lambda\otimes\Lambda)
  +(\dot\Lambda\otimes\Lambda-\Lambda\otimes\dot\Lambda)
 \tag{7}
\]

gives exactly

\[
 (P_+v_K)(n)=a_1(n)a_1(K/n)-a_0(n)a_0(K/n),\qquad
 (P_-v_K)(n)=\int_0^1(a'_τ(n)a_τ(K/n)-a_τ(n)a'_τ(K/n))d\tau.
 \tag{8}
\]

Product collapse C_K v=sum_n v(n) satisfies C_K P_+=C_K and C_K P_-=0.
The same is true of every kernel depending only on K. This is a source-defined
exchange action, not an identification of core-degree parity, colour Walsh
characters, or residue-cell mean/primitive decomposition.

For the original real outer kernel kappa, put
dnu(t)=|kappahat(t)|^2 dt/(2pi), and define the physical ratio observation

\[
 (R_Kv)(t)=K^{-1/2}\sum_{n\mid K}v(n)e^{it\log(n^2/K)}.
 \tag{9}
\]

Let T f(t)=f(-t) and E_+=(I+T)/2, E_-=(I-T)/2. Then

\[
 R_KJ=TR_K,\qquad R_KP_\pm=E_\pm R_K.               \tag{10}
\]

The measure nu is even because kappa is real. Thus E_+ and E_- are orthogonal
Hilbert projections, and

\[
 \|R_Kv\|_{L^2(\nu)}^2
 =\|R_KP_+v\|^2+\|R_KP_-v\|^2.                     \tag{11}
\]

For real coefficients the two fields are respectively real-even and
imaginary-odd. Their linear integral has no odd contribution, while the odd
square is generally positive. Exchange may swap owner/conductor fibres;
(10) is asserted on the primitive factor space, or on the doubled exchanged
fibre, not on one arbitrarily oriented fixed iota.

Derivative-site provenance needs a separate statement. In a doubled tensor
ledger, swapping both slots and the derivative mark preserves counting measure
on the marks and the measure 2 d_tau. Summing site marks into v_tau is an
additional map, not an isometry. In particular the primitive diagonal,

\[
 D_{\rm site}=K^{-1}\sum_{n,j}2\int_0^1|b_{n,j}(\tau)|^2d\tau,
 \tag{12}
\]

and the separately integrated-site diagonal
K^(-1) sum_(n,j)|2 int b_(n,j)|^2 are distinct. Neither is replaced by
K^(-1) sum_n|v_K(n)|^2 without its explicit cross terms. The replay records
all three resolutions and the endpoint and exchange identities before any
Wick centering. No full principal diagonal claim is inferred from (11).

Even the symmetric quotient is not the whole product quotient: for (4),
P_+v is nonzero and its sum is zero. Cancellation among symmetric factor
allocations remains. Exchange alone therefore cannot supply the proposed
universal primitive/mean projector for every later source construction.

## 4. GE-3: a constructive endpoint-preserving deformation

Allow an explicitly specified continuously differentiable primewise schedule
u_p(s), with u_p(0)=0,u_p(1)=1, and replace ell_tau by ell_(u_p(s)). Use the
full chain-rule derivative in (2) and the measure 2 ds. This is a constructed
deformation of the authenticated primitive, not a claim that its schedules
were silently present in L-102707. The endpoint defect and (3) are unchanged.
Equation (8) shows that the symmetric tensor is also unchanged; only the
antisymmetric integral can vary.

This effect occurs already at two distinct primes p,q. Take u_p(s)=s and
u_q(s)=s^k, k a positive integer. In the K=pq factor space,

\[
 v(p)=1/[2(k+1)],\quad v(q)=k/[2(k+1)],\quad
 v(pq)=1/2,\quad v(1)=0.                            \tag{13}
\]

The full sum is one, as required by beta(pq)-beta^square(pq). On the swapped
pair p,q, P_+v has the two coefficients 1/4, whereas P_-v has opposite
coefficients (1-k)/[4(k+1)]. Relative to the uniform schedule k=1, the entire
ratio-field change is

\[
 \Delta F_k(t)=\frac{i(1-k)}{2(k+1)\sqrt{pq}}
             \sin(t\log(p/q)).                    \tag{14}
\]

For k!=1 its L2(nu) norm is strictly positive: p!=q, and nu is a nonzero
absolutely continuous measure, so it cannot be supported on the discrete
zeros of this sine. Its squared L2 norm is at most
Gamma(0)/(4pq). Meanwhile its product and signed Hankel observations are
exactly zero. Piecewise differentiable monotone schedules that move one prime
first and the other second attain the two extreme antisymmetric coefficients
plus/minus1/4; no arbitrary signed history weights are needed.

The held-out positive canonical tuple is not used to fit this deformation.
Its primitive product has one prime at exponent four, two at exponent two and
four at exponent one, so its complete factor cone has 5*3^2*2^4=720 members. Its beta-beta^square
coefficient is also zero. The same endpoint, site and exchange replay is
applied there without changing a formula or omitting its contractions.

## 5. Replay and boundary

The bounded producer authenticates the exact Git blobs of L-102700/701/707,
the real compact kernel, the predecessor zero chart and the frozen positive
fixture. It streams the 3888 and 720 factor allocations, coalesces identical
local exponent patterns, and evaluates rational polynomials of bounded degree.
It retains all derivative-site weights, checks their sum independently against
the derivative of the full coefficient, and compares endpoint, swap, sector
and right-unit identities. No prime search, numerical integration or large
matrix computation is required.

This supplies a complete finite dependency cone and actual source measure at
the primitive homotopy level. It also proves which exchange projector preserves
which observation, and exhibits a genuine source deformation that changes a
ratio norm while preserving the original current. A decoder from these
primitive records, including carrier, renewal and completion transport, to the
full amplified principal member remains a separate task.
