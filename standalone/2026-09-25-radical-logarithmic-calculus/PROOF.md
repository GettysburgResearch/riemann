# RLC35: a native radical/logarithmic calculus and the exact capped-source defect

Date: 25 September 2026.
Status: PROPOSED component mathematics; independent review required.
Parent: NJV34, PR #907, `4f769249e35d23a9cf955fbab620e70d07117e58`.
Scope: all-cutoff native identities and bounds for an explicit class of complete
composite dilation sums; an all-order quadratic balance; a phase-preserving
finite-source/Hankel adapter with its unresolved defects displayed.
Not claimed: a new asymptotic Mertens-energy bound, the full Newton covariance
estimate, a new zero-free region, or RH.

## 0. What changes, and what is classical

NJV34 controlled a von Mangoldt-weighted first covariance. The construction
below controls complete divisor kernels with arbitrarily many distinct prime
factors whenever their squarefree Möbius transform is a sufficiently regular
function of log n. A bounded logarithmic profile gives a bound linear in the
native energy, with a constant independent of the cutoff and of the number of
primes. There is also an exact positive-term identity for quadratic covariances
of the polynomial members of this class.

The underlying Möbius inversion, divisor product formula, logarithmic
Dirichlet derivation, Abel summation, and Fourier multiplier argument are
classical. In particular the product in (3.1) is DLMF 27.6.2. We make no
external-priority claim for these assembled consequences. The contribution is
the exact native operator realization, its quantitative constants, its
classification boundary, and the explicit attempted transfer to the actual
capped Newton/Hankel source.

That attempted transfer DOES NOT close: it leaves an exact arithmetic defect.
Moreover a coefficient cutoff and an observation-time cutoff cannot be
interchanged after a microscopic frequency mask. This distinction prevents
an otherwise tempting but invalid removal of a quadratic error.

## 1. The coefficient-to-energy representation

Let N>=1, X=N+1, L=log X. Extend any c=(c_1,...,c_N) by zero as necessary and set

    S_c(k)=sum_{n<=k}c_n,
    (U_N c)(u)=exp(-u/2) S_c(floor(exp u)),  0<=u<L.

Thus

    ||U_N c||_2^2 = E_N(c)
                   = sum_{k=1}^N |S_c(k)|^2/[k(k+1)].       (1.1)

All inner products used for energies are Hermitian. The separate arithmetic
kernel pairing in Section 6 is bilinear, as required by the Hankel target.
Let R=R_L be the causal Volterra operator

    (Rg)(u)=integral_0^u exp(-(u-v)/2)g(v)dv,

and T_delta g(u)=1_{u>=delta}g(u-delta), on this same interval. Young's
inequality after zero extension gives ||R||<=2. Integer dilation acts exactly:

    U_N(a*c) = sum_{d<=N} a(d)/sqrt(d) T_{log d}(U_N c),    (1.2)

where the convolution and both sides are truncated coefficientwise through N.
This follows by summing (a*c)(n) and interchanging finite divisor sums.

### Lemma 1: bounded logarithmic source calculus

For phi in W^{1,infinity}(0,L), with its continuous representative at zero,
put c_phi(n)=c(n)phi(log n), and define the bounded operator

    T_phi = M_phi - R M_{phi'}.

Then

    U_N c_phi = T_phi U_N c,                              (1.3)
    ||T_phi f-M_phi f|| <= 2||phi' f||,                   (1.4)
    ||T_phi|| <= ||phi||_infinity+2||phi'||_infinity.       (1.5)

Proof. Finite Abel summation says

    sum_{n<=exp u} c(n)phi(log n)
      = phi(u)S_c(floor(exp u))
        - integral_0^u phi'(v)S_c(floor(exp v))dv.

Multiplication by exp(-u/2) proves (1.3); the R bound proves the estimates.
Endpoint values on a null set do not affect the energy. The same argument
works for any absolutely continuous phi whose displayed multiplication
operators are bounded. No analytic continuation is used. QED.

These operators form a unital algebra: T_phi T_psi=T_{phi psi}. One direct
proof uses

    M_phi R - R M_phi = R M_{phi'} R,

whose kernel identity follows by integrating phi' from v to u. Expansion then
proves the product law, including for arbitrary L2 functions, not just the
finite arithmetic subspace.

If phi and phi' vanish outside a subinterval I, the preceding bound depends
only on ||f||_{L2(I)}. The output may extend past I, but its entire extension is
the one-dimensional exponential memory of R, not an omitted tail.

## 2. Complete composite kernels and their exact classification

Define

    a_phi(n)=sum_{d|n} mu(d)phi(log d).                    (2.1)

Here mu is the actual Möbius function. Then a_phi=1*(mu phi), so

    a_phi*mu = mu phi.                                   (2.2)

For f=U_N mu, introduce the COMPLETE finite divisor operator

    C_{a_phi,N}=sum_{d<=N} a_phi(d)/sqrt(d) T_{log d}.

Every denominator through N is included; no independent amplitudes replace
those in (2.1). Equations (1.2)--(2.2) give

    C_{a_phi,N} f = phi f - R(phi' f),                    (2.3)

and consequently

    ||C_{a_phi,N}f-phi f||^2 <=4 integral_0^L |phi'|^2|f|^2,
    ||C_{a_phi,N}f|| <= (||phi||_infinity
                         +2||phi'||_infinity) sqrt(E_N). (2.4)

This is source-specific: C_a and T_phi agree on the native vector in (2.3),
not as operators on all vectors. In particular the C_a do NOT inherit the
multiplication law of the T_phi. For phi(u)=exp(-u), a_phi(2)=1/2 and
(a_phi*a_phi)(2)=1, whereas a_{phi^2}(2)=3/4. This exact counterexample is tested.

Expanding the square in (2.4) gives a bound for the complete d,e covariance,
including every cross term. The constant has no prime-count or support loss.
It does not control arbitrary replacements of the arithmetic weights a_phi.

### Theorem 2: radical invariance is precisely the algebraic compatibility

For an arithmetic sequence a, the following are equivalent:

(i) a*mu vanishes on all nonsquarefree integers;
(ii) a(n)=a(rad n) for every n;
(iii) a=1*b for some squarefree-supported sequence b.

Proof. If b=a*mu is squarefree-supported then a=1*b, and its divisor sum
depends only on rad n. Conversely, if a is radical invariant, then in
(a*mu)(n)=sum_{d|n}mu(d)a(n/d), any prime dividing n to exponent at least two
pairs the d with and without that prime; their a-values agree and their signs
oppose. The result vanishes. The equivalence with (iii) is Möbius inversion.
QED.

On squarefree n one can write b(n)=mu(n)w(n), uniquely. Thus (i)--(iii)
classify scalar native coefficient multipliers, without a regularity bound.
They do NOT assert that an arbitrary such w admits a globally bounded,
low-derivative interpolation phi(log n). A finite interpolation can have a
very large derivative, and then (2.4) is correspondingly expensive.

If n has distinct prime factors p_1,...,p_r, (2.1) is a prime-cube difference:

    a_phi(n)=(-1)^r integral_0^{log p_1} ... integral_0^{log p_r}
                  phi^{(r)}(t_1+...+t_r) dt_1...dt_r.      (2.5)

The identity follows by applying the fundamental theorem of calculus r times.
It requires phi in C^r on the indicated interval (or the corresponding weak
regularity). For a polynomial of degree k it vanishes when r>k. For a general
bounded smooth profile there is no bound on the number of distinct primes
appearing, while (2.4) still involves only phi and its FIRST derivative.

## 3. A sharp, cutoff-uniform phase comparison

Take phi_tau(u)=exp(i tau u), tau real. The elementary divisor product gives

    a_tau(n)=product_{p|n}(1-p^{i tau}),  a_tau(1)=1.       (3.1)

For f=U_N mu, its complete composite sum is exactly U_N(mu(n)n^{i tau}).
Let

    kappa(tau)=sqrt(1+tau^2)+|tau|.

Then for EVERY f in L2(0,L),

    kappa(tau)^(-1)||f|| <= ||T_{phi_tau}f||
                                <= kappa(tau)||f||.      (3.2)

In particular

    kappa(tau)^(-2) E_N
       <= ||C_{a_tau,N}U_N mu||^2 <= kappa(tau)^2 E_N.     (3.3)

Proof. T_phi_tau=(I-i tau R)M_phi_tau. The full-line causal R has Fourier
multiplier 1/(1/2+i xi). The modulus squared of I-i tau R is

    [(1/4)+(xi-tau)^2]/[(1/4)+xi^2].

Its supremum over real xi is kappa(tau)^2, by elementary maximization.
Zero extension and projection back to (0,L) prove the upper bound. The
operator product law gives T_phi_tau^{-1}=T_phi_{-tau}; its upper bound proves
the lower bound. The upper constant is sharp uniformly over interval lengths:
long, smoothly cut-off monochromatic functions approach the maximizing
Fourier frequency, and the relative endpoint error tends to zero. This is
sharpness for the universal operator family, not a claim that mu attains it.
QED.

For example tau=3/4 gives kappa=2. The maximizing frequency xi=-1/4 makes the
multiplier ratio exactly 4; this algebraic normalization is checked rationally.

An all-denominator covariance can therefore have complicated products of
prime phases and still be within an explicit constant factor of the native
energy. This does not give an absolute bound for that energy. General
Dirichlet-character twists are not being bounded by the principal energy:
they need not arise from a profile with controlled logarithmic derivative.

Real damping phi(u)=exp(-sigma u) also gives an exact product
product_{p|n}(1-p^{-sigma}) and (2.4), but it has no cutoff-uniform inverse
comparison when sigma>0. A source supported at a single large n already has
its energy multiplied by n^{-2sigma}. Bounds after damping cannot be
transferred back by silently inverting it.

## 4. All-order native quadratic covariance with positive correction terms

Let k>=1 and let a_k=1*(mu(log n)^k). Write C_k=C_{a_k,N}, f=U_N mu, and

    y_k=R(u^{k-1}f).

Then (2.3) gives C_k f=u^k f-k y_k. An integration by parts produces the
stronger exact identity

    ||C_k f||^2 + k integral_0^L u|y_k(u)|^2 du
                  + k L |y_k(L)|^2
       = integral_0^L u^{2k}|f(u)|^2 du
                  + k(k+1)||y_k||^2.                    (4.1)

In particular,

    ||C_k f||^2 <= integral u^{2k}|f|^2
                    +4k(k+1) integral u^{2k-2}|f|^2.    (4.2)

There is no discarded endpoint and no term of order integral u^{2k-1}|f|^2
on the right side of this bound.

Proof. Put g=u^{k-1}f and y=Rg. Then y'+y/2=g almost everywhere, y(0)=0,
and y is absolutely continuous. Hence

    2 Re integral_0^L u g conjugate(y) du
       = L|y(L)|^2 -||y||^2 + integral_0^L u|y|^2 du.

Expand ||ug-ky||^2 and substitute this equality. The R norm bound yields
(4.2). All terms are finite on the fixed interval; the proof also works for
complex f. QED.

The arithmetic logarithmic derivation D a(n)=a(n)log n obeys

    a_0=delta_1,  a_{k+1}=D a_k-Lambda*a_k.

Thus

    a_1=-Lambda,
    a_2=Lambda*Lambda-D Lambda,
    a_3=-Lambda*Lambda*Lambda+3Lambda*(D Lambda)-D^2 Lambda.

For a_2 the coefficient is -(log p)^2 at every prime power p^a,
2log p log q at every p^a q^b with p!=q, and zero at numbers with at least
three distinct primes. The covariance in (4.1) includes ALL pairings of
these denominators, including mixed-prime/mixed-prime terms. The subtraction
of the prime-power contribution is part of the theorem and cannot be removed.
These logarithmic derivative identities belong to classical Dirichlet
calculus; the stated covariance identity is proved here rather than inferred
from a numerical fit.

## 5. The exact defect for a capped native source

Let c be any finite source with c(n)=mu(n) for 1<=n<=Y, Y>=1. Values after Y
are arbitrary; they can be a reciprocal-balancing completion. Let

    nu=1*c,  so c=mu*nu,

where all identities can be interpreted coefficientwise up to any finite B.
Then nu(1)=1 and nu(n)=0 for 2<=n<=Y. For any completely multiplicative chi
with chi(1)=1, use subscripts chi for pointwise multiplication by chi and put

    a_chi=1*mu_chi,
    r_chi=a_chi*c-c_chi=mu_chi*(nu-nu_chi).                (5.1)

The last equality follows because c_chi=mu_chi*nu_chi. It is an exact,
primitive-source formula for the failure of the native comparison after
changing the source. In particular

    r_chi(n)=0 for n<=Y.                                 (5.2)

For chi(n)=n^{i tau}, a_chi is (3.1); the same algebra works for rational
damping chi(n)=n^{-j}, which is used in the exact tests. The norm constants
from Section 3 concern real tau, not arbitrary chi.

Tensoring (5.1) gives

    (a_chi*a_chi)*(c*c)
       =(c*c)_chi +2 c_chi*r_chi+r_chi*r_chi.              (5.3)

For coefficient indices n<(Y+1)^2, the final convolution vanishes. At the
endpoint it need not: take Y=2 and the balanced source

    c(1)=1, c(2)=-1, c(3)=-3/2,

with chi(n)=1/n. Then r_chi(3)=-1/3 and

    (r_chi*r_chi)(9)=1/9.                                (5.4)

This is tested from independently generated divisor convolutions. The linear
term is already nonzero at n=3. Thus even below the square threshold one
cannot replace the capped source by the native source without a defect.

## 6. A phase-preserving finite Hankel adapter -- with both errors retained

For any cutoff B and any complex product kernel Phi on {1,...,B}, define

    (A_a^vee Phi)(m)=sum_{d<=B/m}a(d)Phi(dm).

This is a BILINEAR transpose, not a Hermitian adjoint. Write z=c*c. Reordering
finite sums in (5.3) yields

    sum_{n<=B} z(n) [(A_{a_chi}^vee)^2 Phi(n)-chi(n)Phi(n)]
       =2 sum_{n<=B}(c_chi*r_chi)(n)Phi(n)
          +sum_{n<=B}(r_chi*r_chi)(n)Phi(n).               (6.1)

No conjugation or absolute square has been introduced. This is an exact
kernel relation for the finite product source, valid for complex phases.
The last term may be removed if B<(Y+1)^2, or if Phi annihilates its entire
support. An observation variable being smaller than that threshold is NOT
such a condition.

### Relation to the current repository target

MHB32, at `8c506696d8ad7772ccaf48fbb8678fcd889e8beb`, equations (2.1)--(2.2),
unreduces its microscopic covariance as

    U(k)=sum_{r,s<=L_c} c(r)c(s)/(rs) f_{X,k}(rs),
    f_{X,k}(d)=sum_{j>=1}g_{X,k}(jX/d).

Accordingly its EXACT product kernel is Phi_k(n)=f_{X,k}(n)/n, and
B=L_c^2. Substituting that Phi into (6.1) gives the stated adapter for the
same capped source and the same complex-square/Hankel phase. This is not a
claim that it has the norm of a positive Fourier multiplier.

The microscopic mask does not force Phi_k(n)=0 when n>k. For L_c up to 2Y,
B can exceed (Y+1)^2 even if the observation k is below that threshold.
Consequently BOTH residual terms in (6.1) must in general be retained. Full
Newton cancellation after complete divisor closure does not authorize their
removal from a frequency-selected piece.

An exact rational control illustrates the distinction within the same
unreduced-product construction. Let g(t)=(1-t)^4 for 0<t<1, zero for t>=1,
and X=8. Then Phi(9)=1/9^5 despite 9>X. In the source (5.4), restricted to
B=9, the quadratic residual contributes exactly 1/9^6. This g is a structural
control, NOT the actual centered harmonic g of MHB32, and is not evidence
about the sign or size of that harmonic target. It disproves only an
argument that tries to discard the residual from the observation cutoff
alone for this class of product kernels.

Equation (6.1) provides an exact adapter identity, NOT a bounded inversion of
the kernel operator (A_a^vee)^2-M_chi. Neither a uniform source-specific bound
for its residual pairings nor a suitable controlled inverse is proved here.
Those are explicit remaining mathematical obligations, not assumed steps.

## 7. Why the reciprocal balance cannot be silently transported either

MHB32's metric for a reciprocally balanced source is

    J(c)=sum_{j=1}^{L_c-1}|sum_{n<=j}c(n)/n|^2.

NJV34 instead gives, for a prefix through N,

    F_N(c)=E_N(c)+(N+1)|bar s_N|^2,
    bar s_N=s_N-S_c(N)/(N+1).                            (7.1)

Multiplying coefficients by chi changes the reciprocal balance. Preserving
all the modulated coefficients through N and adding a balancing coefficient
at N+1 costs the actual uncentered energy F_N(c_chi), including the scalar
in (7.1). Section 3 bounds E_N(c_chi), not that scalar.

This distinction has an exact unbounded control. Start with c=delta_1-2delta_2
and preserve its zero coefficients through N>=2. Its original balanced
energy is J(c)=1. For chi(n)=n^{i tau}, repair balance at N+1. The new energy is

    J_repaired=1+(N-1)|1-2^{i tau}|^2.                   (7.2)

For the rational damping chi(n)=1/n it is exactly 1+(N-1)/4. Moving the repair
to the coefficient at 1 instead would avoid this long constant primitive,
but would change the literal source at 1. It is not an allowed silent repair.

This is a generic counterexample to a proposed uniform transfer of metrics,
not a claim that the actual native completion attains this growth. Its role
is to identify precisely what an adapter must prove rather than infer.

## 8. Research consequence

The controlled class now includes full mixed-prime kernels of unbounded
prime complexity, with first-derivative rather than prime-count constants.
The radical classification identifies its exact arithmetic range. The
polynomial members have a complete quadratic identity with positive bulk and
boundary terms. The source-preserving transfer to a capped tensor source is
also explicit, and it exposes rather than erases the residual.

None of these statements bounds E_N independently. Some members, such as
phi supported below log 2, reduce to mu*1=delta_1; others damp high coefficients.
Their bounded outputs do not imply a bounded inverse. Source-specific small
output and source-independent coercivity must not be conflated.

A useful next theorem would bound the actual pairings with r_chi in (6.1),
including the part surviving the microscopic mask, or exploit a different
logarithmic profile for which a controlled inverse and a separately estimated
image coexist. Merely solving the finite arithmetic identities exactly does
not give either estimate. This pass supplies no new native asymptotic upper
bound and does not close the full composite covariance or RH.

## 9. Validation boundary

The standard-library checker regenerates Möbius data by a sieve and checks
it by independent Dirichlet inversion; it verifies complete rational divisor
and covariance sums, formal prime-log polynomial identities, the all-order
quadratic identity at specified finite panels, exact tensor defects and
endpoints, and genuine rejected shortcuts. See VALIDATION.md for exact
ranges and the executed commands.

Universal analytic statements depend on the written Abel, Volterra, and
Fourier proofs above. Finite tests do not constitute their proof or an
independent mathematical review. No repository-wide validator, remote CI,
proof-assistant verification, or new validation of inherited packets is
claimed. Parent directories and canonical statuses are unchanged.
