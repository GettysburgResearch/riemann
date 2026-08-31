# Positive reflected Mellin sources: a real-zero firewall

Status: PROPOSED SYNTHETIC SOURCE-EXACT THEOREM; independent review required.
Base: SC `b0e3b18e690accdee6d77b3b3c4c68850f6cb671`.
This is a synthetic source-axiom countercontrol, NOT the actual modular
theta source, an RH counterexample, or a new automorphic construction.
Sections1--3 retain the design frozen before arithmetic at
`67f88c148bb5914897cc13b6cbce61960a277cd1`. The proofs and complete
outcomes follow in sections4--8; no failed bracket is suppressed.

## 1. Exact theorem target

For fixed0<b<=sqrt8 and A>0 take vacuumG=1,alpha1,
C_A(t)=A*1_[1,exp(b)](t) on t>=1, H_A=1+2C_A there, and extend
H_A(t)=t^-1 H_A(1/t) to0<t<1. It is a locally bounded positive source
with compact upper excess. The completed observation and its entire
pole-clearing are

    L_A(s)=1/[2s(s-1)]
        +A[(exp(bs)-1)/s+(exp(b(1-s))-1)/(1-s)],
    Z_A(s)=s(s-1)L_A(s)
        =1/2+A[1+(s-1)exp(bs)-s exp(b(1-s))].

Target: Z_A has exactly two simple real zeros in(0,1) when
A>A_c=1/[2(exp(b/2)-1)], one double zero at1/2 when A=A_c, and no
real zeros when0<A<A_c. The threshold case has no other real zeros.
Reflection and the positive Mellin feature kernel remain valid. No count
of all complex zeros is intended.

Put z=s-1/2, J(z)=integral_0^b exp(x/2)cosh(zx)dx. Then
Z_A=1/2-2A(1/4-z^2)J(z). Prove strict monotonicity of
(1/4-z^2)J(z) on0<z<1/2 from x*tanh(zx)<z*x^2 and b^2<=8.
Prove the local pitchfork by the analytic implicit theorem in u=z^2:
J0=J(0), c_b=2J0-J''(0)/4>0, A_c=1/J0 and

    u'(A_c)=J0^2/(2c_b)>0.

For real A just below threshold the nearby pair is on Re s=1/2; just
above threshold it is the real off-central pair. At threshold multiplicity
is exactly2. These are local statements, not a global complex-zero census.

Also prove existence of globally C-infinity, strictly H(t)>1 synthetic
sources with the same vacuum/reciprocity/rapid tail and a simple off-central
real pair. Smooth the even log-source h0(x)=exp(|x|/2)(1+2A1_|x|<=b)
only near0,+b,-b, preserving h>=exp(|x|/2), then add epsilon exp(-2cosh x).
Put H(t)=t^-1/2 h(log t). Weighted L1 compact-contour convergence and
Rouche must pay persistence; do not assert the full step-family real-zero
count for the smoothed perturbation, or identify it with native MP data.

## 2. Frozen finite panel, with no special-function evaluations

Set b=1 only for finite controls. For EACH
x in{1/8,3/8,1/2,5/8,7/8,1}, use the exact rational Taylor enclosure
with N=16:

    S_N(x)=sum_(j=0)^N x^j/j!,
    S_N(x)<exp(x)<S_N(x)+x^(N+1)/(N+1)!/[1-x/(N+2)].

All endpoints, every rational numerator/denominator, and N are retained.
The inequalities are proved analytically by a geometric majorant; no
floating transcendental library or decimal proxy is accepted.

Use the E=exp(1/2) enclosure to certify3/4<A_c<4/5. Retain all9 enclosed
values Z_A(s) for A in{1/2,1,2} and s in{1/8,3/8,1/2}, plus the exact
endpoint values Z_A(0)=Z_A(1)=1/2. Candidate lower-half brackets
[1/8,3/8] are checked for BOTH supercritical A=1 and A=2. Before
computation, the A=2 candidate is expected to fail because its zero lies
left of1/8; retain that failure, do not shift the panel or label it blinded.
The A=1 candidate is expected to succeed. No bracket is sought for A=1/2.

Retain all9 exact rational monotonicity margins

    2-B/4+B*z^2

for B in{1,4,8}, z in{1/8,1/4,3/8}. These are finite controls of the
symbolic proof2-B/4+Bz^2>=Bz^2>0 when0<B<=8, not a sampled proof
of its continuum quantifier.

Finally verify the b=1 formal identities, with E left as an indeterminate:
J0=2E-2, J''(0)=10E-16, c_b=3E/2 and
u'(A_c)=4(E-1)^2/(3E). Verify the exact reflection/endpoints of the
exponential-polynomial expression symbolically, not by sampling zeros.

## 3. Acceptance and provenance

Exactly five new files are intended: this proof, a bounded exact producer,
fixture, source manifest, and tests. The manifest will pin SC's five
frozen scientific files plus this preregistration. Arithmetic is MIXED,
EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE, with no rounding.
The finite checker does not certify an analytic integral, the implicit
theorem, Rouche, a smooth source, or all complex zeros. Full proof and
independent exact-SHA review remain essential. No parent, main or PR edits.

## 4. Completed source and exact count of real zeros

Fix A>0 and0<b<=sqrt8. The field H_A specified in section1 is finite,
measurable, locally bounded, >=1 everywhere, and has the exact reciprocal
law H_A(t)=t^-1 H_A(1/t). The excess C_A=(H_A-1)/2 is nonnegative, is
strictly positive on0<t<1, and vanishes on t>exp(b). Thus it satisfies
the SC bounded-source class with fixed vacuum1 and weight1. SC4 gives
absolute Mellin convergence for Re s>1, meromorphic continuation with
only the nonzero simple poles0,1 and residues-1/2,+1/2, reflection
L_A(s)=L_A(1-s), Schwarz symmetry, and a positive Mellin feature kernel
L_A(z+bar w) on Re z,w>1/2. None of these properties uses a zero claim.

Direct integration on[1,exp(b)] in SC9 gives the two elementary terms
in section1. Their apparent denominators s and1-s have removable
singularities, since (exp(bs)-1)/s is entire. Multiplication by s(s-1)
therefore gives the displayed entire exponential polynomial Z_A.
In particular Z_A(0)=Z_A(1)=1/2, and Z_A(1-s)=Z_A(s). Its explicit
bound O_(A,b)((1+|s|)exp(b|s|)) is not a zero census.

Substitute t=exp(x) in the integral part and put z=s-1/2. The entire even
function J(z)=integral_0^b exp(x/2)cosh(zx)dx satisfies

    Z_A(1/2+z)=1/2-2A Phi(z),
    Phi(z)=(1/4-z^2)J(z),    J0=J(0)=2(exp(b/2)-1).           (ZF1)

For real0<z<1/2, J(z)>0 and

    J'(z)/J(z)
      = weighted_average_(0<=x<=b) [x tanh(zx)] < z b^2.      (ZF2)

The weight is exp(x/2)cosh(zx)>0. The strict inequality follows from
tanh u<u for u>0 and the positive-length set0<x<b. Consequently

    Phi'(z)<z J(z)[-2+b^2(1/4-z^2)]<0,                      (ZF3)

including b^2=8, because z>0. Moreover Phi(0)=J0/4>0 and
Phi(1/2)=0. Thus Z_A is strictly increasing as a function of z on(0,1/2),
has value1/2-AJ0/2 at0, and has value1/2 at1/2. Reflection supplies
the negative-z half. For real |z|>1/2, Phi(z)<0 and hence Z_A>1/2.

It follows that with A_c=1/J0 there are exactly TWO real zeros when
A>A_c, one in each half of(0,1), and no real zeros when0<A<A_c.
Both supercritical zeros are simple because Z_A'=-2A Phi' is strictly
positive at the positive-z zero and strictly negative at its reflection.
There are no real zeros outside(0,1), and the endpoint values are nonzero.
The multiplicity and sole real zero at the threshold are proved next.
Since s(s-1) is nonzero at these interior zeros, they are also genuine
zeros of the meromorphic observation L_A, not artifacts of pole clearing.

## 5. Threshold multiplicity and the local pitchfork

Let J2=J''(0)=integral_0^b x^2 exp(x/2)dx and

    c_b=2J0-J2/4=integral_0^b (2-x^2/4)exp(x/2)dx>0.          (ZF4)

The integrand is nonnegative for b<=sqrt8 and positive on a subinterval,
so strictness holds at the endpoint too. The even power expansion gives

    Z_A(1/2+z)=1/2-AJ0/2+A c_b z^2+O_(A,b)(z^4).            (ZF5)

At A=A_c the quadratic coefficient A_c c_b is nonzero. Hence the sole
real zero at1/2 has multiplicity exactly2. This is not inferred from
numerical coincidence or a sign test at the center.

For completeness the even series defines an entire function of u=z^2:
J_tilde(u)=sum_(n>=0) u^n integral_0^b x^(2n)exp(x/2)dx/(2n)!.
Let F(A,u)=1/2-2A(1/4-u)J_tilde(u). At(A_c,0),
F_u=A_c c_b>0 and F_A=-J0/2. The analytic implicit-function theorem
therefore gives a unique local analytic zero u(A), with

    u(A_c)=0,   u'(A_c)=J0^2/(2c_b)>0.                      (ZF6)

One can obtain the needed local multiplicity statement directly: divide
F(A,u)-F(A,u(A)) by u-u(A), using the integral of F_u along the segment.
The resulting analytic factor is nonzero near(A_c,0). Hence nearby zeros
are precisely z^2=u(A), counting multiplicity. Reality of all coefficients
and uniqueness imply u(A) real for real A. Just below A_c, u(A)<0 and the
two simple nearby zeros are1/2 plus or minus i sqrt(-u(A)); just above
A_c they are1/2 plus or minus sqrt(u(A)), the real pair from section4.
This is a local bifurcation only. Other complex zeros are not enumerated
and are not claimed to lie on any line.

At b=1, writing E=exp(1/2), exact integration by parts yields

    J0=2E-2, J2=10E-16, c_b=3E/2,
    u'(A_c)=4(E-1)^2/(3E)>0.                                 (ZF7)

The producer checks the polynomial antiderivative
exp(x/2)(2x^2-8x+16) and the resulting identities with E formal.
No approximate exponential is substituted for this curvature calculation.

## 6. Globally smooth strictly positive sources retain an off-central pair

The discontinuity of the step density is not essential. Fix ANY one of
the above supercritical pairs, thus fix b and A>A_c. Let
h0(x)=exp(|x|/2)(1+2A1_|x|<=b). For0<epsilon<min(b/4,1/4), choose an
even smooth cutoff chi_epsilon equal1 on |x|<=epsilon and0 on |x|>=2epsilon,
with values in[0,1], and define

    v_epsilon(x)=chi_epsilon(x)exp(sqrt(x^2+epsilon^2)/2)
                 +(1-chi_epsilon(x))exp(|x|/2).               (ZF8)

This is even and C-infinity: the nonsmooth absolute value has zero
coefficient near0. It is >=exp(|x|/2), equals it for |x|>=2epsilon,
and differs from it by O(epsilon) on that small interval. Choose another
even smooth cutoff psi_epsilon in[0,1], equal1 on |x|<=b-epsilon and0
on |x|>=b+epsilon. Such cutoffs can be built explicitly from
rho(u)=exp(-1/u) for u>0 and0 otherwise, using
eta(u)=rho(u)/(rho(u)+rho(1-u)); the absolute value is harmless where
the resulting cutoff is constant near0.

Set

    h_epsilon(x)=v_epsilon(x)(1+2A psi_epsilon(x))
                    +epsilon exp(-2cosh x),
    H_epsilon(t)=t^-1/2 h_epsilon(log t),
    C_epsilon(t)=(H_epsilon(t)-1)/2.                          (ZF9)

Then H_epsilon is globally C-infinity on(0,infinity), satisfies the
EXACT law H_epsilon(t)=t^-1 H_epsilon(1/t), and is strictly greater
than1 for every t>0. Indeed h_epsilon>exp(|x|/2). For t>exp(b+epsilon)
its excess is precisely epsilon t^-1/2 exp[-(t+t^-1)]/2, so all-order
rapid decay is retained. The vacuum stays exactly1; it is not rescaled.
This construction is smooth, not asserted real analytic or modular.

For every fixed M>0,

    integral_1^infinity |C_epsilon(t)-C_A(t)|(t^M+t^-M)dt
       =O_(A,b,M)(epsilon).                                 (ZF10)

Proof: on the bounded interval t<=exp(b+epsilon), the only transition
regions have O(epsilon) length in log t and uniformly bounded height;
the change near log t=0 is even O(epsilon) in height. Outside that
interval the difference is the displayed epsilon times a fixed rapidly
decreasing function. These bounds are uniform for sufficiently small
epsilon. SC9 and the common vacuum now imply uniform convergence of the
entire Z_epsilon(s)=s(s-1)L_epsilon(s) to Z_A on EACH fixed compact s-set.
This is paid by weighted L1, not by pointwise source convergence alone.

Let r and1-r be the real simple zeros,0<r<1/2. Take two small disjoint
closed disks centered there, lying in0<Re s<1 and away from Re s=1/2,
whose boundaries have no zero of Z_A and whose interiors each contain
just the designated simple zero. Their boundary minimum |Z_A| is positive.
For sufficiently small epsilon, ZF10 makes |Z_epsilon-Z_A| smaller than
that minimum. [Rouche's theorem](https://dlmf.nist.gov/1.10#iv) gives exactly
one zero COUNTING multiplicity in each disk. Schwarz symmetry makes each
zero real, since otherwise its distinct conjugate would lie in the same
disk. Each zero is therefore simple, real, off-central, and reflected
to the other one. The positive source/kernel, continuation, endpoint
residues and reflection survive. No full real-zero count is claimed for
the smooth perturbation; only this rigorously retained pair is needed.

## 7. Complete exact finite outcomes and acceptance

For0<x<=1, the positive exponential Taylor series has lower sum S_N(x).
Its tail begins with x^(N+1)/(N+1)! and each subsequent ratio is at most
x/(N+2)<1, with later ratios strictly smaller. Hence the displayed
geometric upper bound is strict. This proves that the rational endpoints
computed at N16 genuinely enclose exp(x); no floating rounding enters.

All six exponential enclosures and all nine sign enclosures from the
frozen design are retained. The threshold enclosure lies strictly inside
(3/4,4/5), so A=1/2 is subcritical and A=1,2 are supercritical. In the
declared point order s=1/8,3/8,1/2, the signs are

    A=1/2: +,+,+;     A=1: +,-,-;     A=2: -,-,-.

Thus the proposed bracket[1/8,3/8] succeeds for A=1 and FAILS for A=2.
The latter failure is preserved, not silently replaced by another grid.
The proof's exact monotonicity and the endpoint value1/2 locate A=2's
left zero to the left of1/8; no new numerical bracket is claimed. All
nine rational monotonicity margins are positive, including B=8. They
check finite algebra but do not replace ZF2--ZF4's all-b argument.

The fixture binds the complete scientific source, all five SC files and
the pre-computation design using literal Git identities and LF hashes.
Its final proof/producer/manifest/tests are bound by artifact hashes and
a canonical payload digest. MIXED arithmetic means EXACT_RATIONAL plus
CERTIFIED_INTEGER_COVERAGE, with rounding NONE. Acceptance requires a
fresh source-authenticated reconstruction, not a self-consistent checksum.
Strict bool/int/rational separation, finite order/work/bit/JSON caps,
source tampering, artifact tampering and resealed scope/coverage mutations
are tested in both normal and optimized Python. The proof of the infinite
source and all analytic quantifiers remains a written obligation.

## 8. What this refutes, and what it does not

The countercontrol has a fixed positive vacuum, a positive source, exact
reflection, an entire pole-cleared completion, positive real observations
in their convergence half-plane, and a positive Mellin feature kernel.
These source axioms do NOT force critical-line zeros. The smooth version
shows that this is not merely a jump-discontinuity artifact.

The actual MP theta source is not substituted, perturbed or contradicted.
No arithmetic identity, Euler product, modular transformation in z,
Hecke structure or genuine automorphic origin is claimed for this scalar
source. In particular this is not an RH/GRH counterexample. Its role is
to identify exactly what the new positive-source completion axioms alone
cannot supply; an additional native zero-location mechanism remains needed.
The Mellin completion, analytic implicit theorem and Rouche theorem are
classical. No new abstract bifurcation theory or exhaustive novelty claim
is asserted. The smallest critical arguments are the strict all-b
monotonicity and the weighted-L1-to-compact-contour persistence, not the
finite sign table.
