# Positive reflected Mellin sources: preregistered real-zero firewall

Status: PREREGISTRATION, before any new finite arithmetic.
Base: SC `b0e3b18e690accdee6d77b3b3c4c68850f6cb671`.
This is a synthetic source-axiom countercontrol, NOT the actual modular
theta source, an RH counterexample, or a new automorphic construction.

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
