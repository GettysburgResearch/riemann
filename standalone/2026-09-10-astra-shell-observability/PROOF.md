# Native shell observability: compact derivatives, unbounded transmission, and the critical cost

**PROPOSED component mathematics; independent review pending. RH is not proved.**
This is an addition-only continuation of PR845 at
`be78f076b9abe8d8d6a40c14f71d0df36a4e0407`. It attacks the old-to-new coupling,
not a different arithmetic source. The universal shell estimate Q-AC26 remains
OPEN. In particular, the unbounded transmission theorem below does NOT refute
Q-AC26, whose small old-energy term is essential.

Classical inputs are: finite divisor inversion, the Euler evaluations of
zeta(2) and zeta(4), existence of a critical-line zero (no simplicity or location
required), and, ONLY inside conditional arguments that already imply RH, the
classical RH-to-Mertens bound. Sources and inspection limits are in SOURCES.json.
No novelty claim is made for generic Hankel/Volterra prediction, compactness,
Mellin transforms, or the arithmetic-matrix approach itself.

## 0. The SAME source, endpoints and operator

All integer indices are positive and odd. Define

    M(x)=sum_(n<=x, odd) mu(n), m(x)=sum_(n<=x, odd) mu(n)/n,
    Q(x)=M(x)-x m(x), E(X)=integral_1^X m(t)^2 dt.

Set M,m,Q to zero below 1 and E to zero at X<=1. Q is continuous and Q'=-m
almost everywhere, including the cancellation of its activation jumps.
For odd X>=3 put O_X={1,3,...,X-2}; X itself is EXCLUDED. With v_(-1)=0,

    (B_X v)_n=sum_(d|n)d(v_d-v_(d-2)),
    V_X=B_X^(-1),             V_X(n,d)=m(n/d)/d.             (0.1)

The inverse follows by applying finite Mobius inversion to the differences;
it is not an estimate. If A=3^r, split O_(3A) into O_A and
T_A={A,A+2,...,3A-2}. Keep the parent's exact blocks

    B_(3A)=[B_A,0; C_A,K_A],
    V_(3A)=[V_A,0; D_A,J_A], D_A=L_A V_A, L_A=-J_A C_A,
    J_A(n,k)=1_(k<=n)/k,    ||J_A||^2<=2/3.               (0.2)

Here D_A is an OLD-FORCING-to-new-output matrix, NOT the diagonal integer
matrix in the parent. Explicitly D_A(n,d)=m(n/d)/d for n in T_A,d in O_A.
The complete left-boundary coupling is retained by (0.1)-(0.2).
The proposed parent inequality, equivalently, is

    ||D_A f||^2 <= eta ||V_A f||^2+C_eta ||f||^2,         (Q)

for every eta>0, every r, every complex f, with C_eta independent of r.
Different f components can interfere. Replacing their squared combined output
by the sum of their squared outputs is NOT an upper bound.

## 1. AC27-1: there is an unconditional compact arithmetic derivative

Define the infinite matrix on the odd counting-space l2 by

    T(n,d)=1_(d|n) mu(n/d)/n.                             (1.1)

This infinite matrix is defined directly; a bounded infinite inverse V is
NOT assumed. It is Hilbert--Schmidt, with the EXACT identity

    ||T||_HS^2 = 3/2.                                    (1.2)

Its finite sections equal Delta_X V_X. Consequently, for every finite cutoff,

    ||Delta_X v||^2 <= (3/2)||B_X v||^2.                 (1.3)

Moreover for N>=1 its complete omitted-row Hilbert--Schmidt tail is at most

    sum_(n>N,d) |T(n,d)|^2 <= 2(log N+2)/N.              (1.4)

### Proof

Nonnegative summation, writing n=dk, gives

    sum_(n,d) |T(n,d)|^2
      =(sum_(d odd)d^-2)(sum_(k odd)mu(k)^2 k^-2)
      =Z_o(2)^2/Z_o(4)=3/2,

where Z_o(s)=(1-2^-s)zeta(s), Z_o(2)=pi^2/8 and Z_o(4)=pi^4/96.
Only absolutely convergent Euler products and the classical even-zeta values
are used. Differences in (0.1) give the finite identity; operator norm is at
most Hilbert--Schmidt norm. For (1.4), enlarge the number of squarefree divisors
to the ordinary divisor count tau(n). The bound
sum_(n<=t)tau(n)<=t(1+log t), and partial summation with the negative lower
endpoint term dropped, give 2 integral_N^infinity (1+log t)t^-2 dt.
This proves (1.4) for the entire omitted region, not just sampled rows.

There is also a sign-exact positive conjugacy. Write ell(n)=(-1)^Omega(n)
and let S be the diagonal unitary with entries ell(n). Since
mu(k)=ell(k)mu(k)^2 and ell(n/d)=ell(n)ell(d),

    (S T S)(n,d)=1_(d|n)mu(n/d)^2/n >= 0.                (1.5)

This is positivity of entries after a sign conjugation, not positivity of T
or of V as a self-adjoint quadratic form.

### Why this does not finish compactness

Summing differences to recover v is not a uniformly bounded operation on
these growing counting-space intervals. Indeed, the parent's nonnative control
b(3^k)=-2^(k-1), b(1)=1 has an even smaller finite derivative norm:

    ||T_b||_HS^2=Z_o(2)(1+sum_(k>=1)4^(k-1)/9^k)
                 =(6/5)Z_o(2)=3pi^2/20 < 3/2.

The SAME control has E_b(3^r)=6((4/3)^r-1), and violates (Q) for eta<1/3,
as proved in parent AC26-5. Thus compactness of the derivative, even with this
numerical norm bound, does not imply compactness of the integrated response.
This control is not the native Mobius function. Its reuse is credited, not
presented as a new source or an RH counterexample.

## 2. AC27-2: an exact native mean-row probe and unavoidable small-forcing growth

Let u_A be the unit constant vector on the A new-shell rows. Then

    (D_A^* u_A)_d=[Q(A/d)-Q(3A/d)]/(2 sqrt(A)),           (2.1)
    ||D_A^* u_A||^2=(1/(4A)) sum_(d in O_A)
                                  [Q(3A/d)-Q(A/d)]^2.  (2.2)

The identities also hold after restricting to any subset of old columns.
All quantities Q at rational arguments are exactly computable from finite
integer Mobius sums. No zeta zero is used to construct these probes.

### Proof of the EXACT endpoint identity

The jumps of m(t/d), for odd d, occur at odd integer multiples of d.
It is constant on each grid cell [n,n+2), n odd. Therefore

    2 sum_(n in T_A) m(n/d)
       = integral_A^(3A) m(t/d)dt
       =d[Q(A/d)-Q(3A/d)].                              (2.3)

Divide by sqrt(A)d. This includes the last cell and excluded right endpoint.
For any chosen column set I, the RATIONAL vector
b_d=1_I(d)[Q(A/d)-Q(3A/d)] is a concrete lower-norm witness:

    ||D_A b||^2/||b||^2 >= ||b||^2/(4A),                (2.4)

whenever b!=0, by pairing with u_A. In (Q) it yields the finite lower bound
C_eta >= ||b||^2/(4A)-eta ||V_A b||^2/||b||^2. No term is dropped from (Q).

### All-scale native conclusion

For EVERY fixed real q>=1,

    ||D_A 1_(d<A/q)||_op -> infinity as A=3^r -> infinity. (2.5)

In particular, a fixed C in ||D_A f||^2<=C||f||^2 is FALSE even for the
actual native source, and even when the forcing lies below any fixed relative
cutoff. This is stronger than failure for a nonnative control. It still does
not refute (Q), because the old-response term there can absorb this growth.

### Proof using only a classical critical-line zero

Put p(x)=integral_1^3 m(xu)du=[Q(x)-Q(3x)]/x. We first prove

    integral_1^infinity p(x)^2 dx=infinity.              (2.6)

Set h(t)=e^(t/2)m(e^t), l=log3 and
psi(t)=e^(t/2)p(e^t)=integral_0^l e^(v/2)h(t+v)dv.
For Re(z)>1/2, absolute convergence gives

    H(z)=Laplace(h)(z)=1/[(z-1/2)Z_o(z+1/2)],
    Laplace(psi)(z)=g(z)H(z)-J(z),
    g(z)=(3^(z+1/2)-1)/(z+1/2),                        (2.7)

where J(z)=integral_0^l e^((z+1/2)v) integral_0^v h(t)e^(-zt)dt dv
is entire. Suppose (2.6) were finite. Then psi belongs to L2(0,infinity),
its Laplace transform is holomorphic for Re(z)>0, and

    |Laplace(psi)(sigma+i t)|<=||psi||_2/sqrt(2sigma).

Multiplying (2.7) by the holomorphic denominator (z-1/2)Z_o(z+1/2) extends
that identity from Re(z)>1/2 to Re(z)>0. At ANY critical-line zero
rho=1/2+i gamma, of multiplicity m>=1, the first term on the right of (2.7)
has a pole of order m at z=i gamma: g(i gamma)!=0 since
|3^(1/2+i gamma)|=sqrt(3)!=1. The entire J cannot cancel it. Along the
right-hand normal its growth is a nonzero constant times sigma^-m,
contradicting the L2 estimate. Thus (2.6) holds. RH and simplicity were not
assumed; no coordinates of a zero were evaluated.

For fixed 1<=q<R, restrict (2.2) to A/R<=d<A/q. Ordinary midpoint-grid
Riemann summation, with spacing 2/A and the continuous function Q, gives

    lim_(A->infinity) (1/(4A)) sum_(A/R<=d<A/q, odd)
                        [Q(3A/d)-Q(A/d)]^2
        =(1/8) integral_q^R p(x)^2 dx.                 (2.8)

The right side increases without bound with R by (2.6); the omitted finite
initial interval has finite integral. Positivity of the summands proves
(2.5), including the full limit rather than only an unbounded subsequence.
Only fixed-R limits were exchanged. No uniform Riemann-sum assertion at d=1
was needed.

## 3. AC27-3: a quantitative full-coupling continuum limit

This result controls the approximation, NOT the limiting norm as the memory
range tends to infinity. For integer q>=2 and A>=q, retain old forcing columns
d>=A/q. Put delta=1/q and define the integral operator on L2(delta,1):

    (K_q F)(s)=(1/2) integral_delta^1 m(s/t)F(t)dt/t,
                           0<s<3.                     (3.1)

m is zero below 1. Its output restrictions to (0,1) and (1,3) will be denoted
V_q and D_q. They retain all cross-band terms.

Use grid cells [d/A,(d+2)/A), length h_A=2/A, and the isometric embedding
f_d -> f_d/sqrt(h_A) on a cell; use the same embedding for output rows.
Let K_(A,q) be the integral-kernel extension of the embedded matrix
V_(3A)(:, d>=A/q,d<A), with cell-averaging on arbitrary inputs. It is zero
on the short initial input sliver before the first retained cell. Then

    ||K_(A,q)-K_q||_HS^2 <= 200 q^6/A.                 (3.2)

This bounds old and new output TOGETHER. It follows in particular that their
operator norms converge for each fixed q. It remains valid for moving integer
q(A) with q(A)^6/A -> 0; this allows an increasing number of forcing bands.
It is not uniform when every old column, including d=1, is restored.

### Proof with a complete boundary estimate

On delta<=t<=1 and 0<s<3 the continuous kernel is the finite sum

    k(s,t)=(1/(2t)) sum_(k<=3q, k odd) (mu(k)/k)1_(s>=kt).

On a retained grid cell the discrete kernel evaluates it at its left endpoints
(s_n,t_d). The normalization 1/2 is forced by the odd mesh, not optional.
Both coordinates change by at most h_A. The contribution from variation of
1/t has L2 norm at most

    (sqrt3/2)q^2 h_A sum_(k<=3q)1/k <3q^3 h_A.

An indicator can change only in the strip |s-kt|<=(1+k)h_A, whose area
in the full rectangle is at most 2(1+k)h_A. Its k-th norm contribution is
at most q sqrt(h_A)/sqrt(k). Sum_k k^-1/2<=2sqrt(3q), giving a total below
4q^(3/2)sqrt(h_A). The input sliver has width less than h_A and the kernel
has magnitude at most q, using |m|<=2; its contribution is below
2q sqrt(h_A). The absent initial output interval (0,1/A) contributes zero,
because s<t there when A>=q. By the triangle inequality the total error is
at most 9q^3 sqrt(h_A). Squaring gives 162q^6/A <200q^6/A. This treats
EVERY activation strip and the whole boundary sliver. QED.

## 4. AC27-4: future/past prediction and an unavoidable cost at critical zeros

The continuum limit makes one necessary part of the remaining problem exact.
It is not a converse adapter from continuum control to every lattice column.
For compactly supported G on [0,infinity), define

    (P_h G)(u)=integral_u^infinity h(v-u)G(v)dv, u>=0,
    (F_h G)(r)=integral_0^infinity h(r+v)G(v)dv, 0<=r<=l.
                                                               (4.1)

Here h(t)=e^(t/2)m(e^t) is the LITERAL native function. On compact inputs
both operators have finite output norms, without RH. P_h has output zero
past the input support. The variable r is future logarithmic time and u is
past logarithmic time, not a zero ordinate.

If the DISCRETE inequality (Q) holds with C_eta, then

    ||F_h G||^2 <= eta ||P_h G||^2+4C_eta||G||^2        (4.2)

for every such G. Indeed apply (Q) to cell averages of F supported in
[1/q,1], use (3.2), and let A grow. Set t=e^-v,
G(v)=e^(-v/2)F(e^-v), old s=e^-u and new s=e^r. These unitary changes of
variables turn V_q into P_h/2 and D_q into F_h/2. Let q include the fixed
support of G. This proves (4.2), including its factor four.

Thus a proof of (Q) must control the new logarithmic window using the entire
old response AND the forcing. Boundedness of the future operator alone is
excluded by Section 2. Compactness of Delta V is not that prediction estimate.

### Conditional necessary lower bound on the constants

Assume (Q) for every eta>0. This assumption implies RH by parent AC26-4.
The classical RH-to-Mertens theorem, explicitly used only under this
assumption, gives h(t)=O_epsilon(e^(epsilon t)). Hence (4.2) extends to
G(v)=e^-zv for Re(z)=sigma>0 by truncation and dominated L2 convergence.
Precisely,

    P_h G(u)=e^-zu H(z),
    F_h G(r)=e^(zr)[H(z)-H_r(z)],
    H_r(z)=integral_0^r h(t)e^-zt dt.

For every sigma>0 this forces

    4C_eta >= 2sigma integral_0^l e^(2sigma r)
                      |H(z)-H_r(z)|^2 dr -eta|H(z)|^2. (4.3)

Let rho=1/2+i gamma be any critical-line zero of multiplicity m. Put

    a_rho=lim_(sigma down0) sigma^m H(sigma+i gamma) !=0.

The finite-interval functions H_r stay bounded near i gamma, while
H(sigma+i gamma)~a_rho sigma^-m. For every fixed k>1, insert
sigma=k eta/(2l) into (4.3). Let eta decrease to zero, then maximize over k.
The maximum is at k=2m/(2m-1), giving the exact necessary lower bound

    liminf_(eta down0) eta^(2m-1) C_eta
      >= (|a_rho|^2/4)(2l)^(2m)
                      (2m-1)^(2m-1)/(2m)^(2m) >0.     (4.4)

For a simple zero this is |a_rho|^2(log3)^2/4. The theorem does not assume
simplicity; higher multiplicity forces a higher cost. No zero location or
zeta derivative was numerically computed. This is a restriction ON any
successful compactness constants, not an upper bound proving their existence.
In particular a constant uniform BOTH in eta and in cutoff is impossible.

## 5. AC27-5: complete finite-band certificates do not add without cross terms

This is a finite exact native counterexample to a proof shortcut, not to (Q).
Take A=81, eta=1/100 and

    G_A=D_A^*D_A-eta V_A^*V_A.

Split the odd columns into the four bands [27,81),[9,27),[3,9),[1,3).
Every diagonal band block satisfies

    (3/5) I - (G_A)_(band,band) > 0.                   (5.1)

Nevertheless for the vector f consisting of forty ones,

    f^*G_A f / ||f||^2 > 94/100 > 9/10.                (5.2)

The sum of its four diagonal-band contributions divided by ||f||^2 is
less than 44/100; the remaining off-diagonal contribution is greater than
1/2. These are exact rational comparisons. Each (5.1) is an ALL-VECTOR band
inequality, not a test only on the bandwise constant vectors.

The checker reconstructs V and D from the native divisor matrix and from
independent Mobius sums. Rational LDL pivots and separate fraction-free
principal determinants prove every (5.1). It also proves I-G_A>0, consistent
with the parent's finite C=1 certificate. Formula (5.2) is the exact rational
witness; decimal scouting is not certificate input. The finite theorem does
not claim a bandwise constant 3/5 at arbitrary larger cutoffs.

## 6. The direct closure attempt, and a less restrictive sufficient target

The attempted proof was to combine compact derivative control with bounded
new forcing, split the old forcing into bands, and pass to compactness.
This does NOT prove (Q): cumulative integration loses uniform control, actual
small-forcing transmission grows without bound, and independent band energies
miss substantial cross terms. Sections 1-5 keep those failures in the SAME
native normalization, rather than swapping in a positive model.

The positive output of the pass is a global compact derivative theorem with
an explicit infinite tail, an exact native variational probe, a quantitative
whole-coupling limit on growing controlled ranges, and the necessary prediction
estimate with its critical-zero cost. These provide tools and constraints,
not the desired upper bound on the true integrated response.

Uniform C_eta is sufficient but need not be the easiest closing theorem.
A weaker sufficient statement is: for every eta>0 and delta>0 there is a
finite C_(eta,delta), independent of A, such that

    ||D_A f||^2 <= eta||V_A f||^2
                      +C_(eta,delta) A^delta ||f||^2.   (Qweak)

This allows a subpower cutoff-dependent defect. If true, (0.2) gives

    kappa(3A)<=max((1+2eta)kappa(A)+2C_(eta,delta)A^delta,4/3).

Given a desired exponent epsilon>0, choose eta and delta with
log_3(1+2eta)<epsilon/2 and delta<epsilon/2. Iterating the scalar recurrence,
including its possible equal-exponent factor r, yields kappa(A)=O(A^epsilon).
The parent's exact energy/trace bridge then gives RH. Conversely RH implies
(Qweak), simply from subpower kappa(3A) and the nonnegative eta term. This is
an elementary equivalence, NOT counted as an obtained arithmetic bound.

Neither (Q), (Qweak), nor a native global upper bound in (4.2) has been proved.
The fixed-q approximation does not justify interchanging q->infinity with
A->infinity; its explicit error shows the limitation. A successful next step
must retain the old-response penalty while controlling the complete polarized
small-divisor coupling, with uniform or genuinely subpower defects. A uniform
bound on transmission alone, a fixed finite list of bands, compactness of the
derivative, or the finite positive tests cannot be substituted for it.
