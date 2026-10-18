# A complete cumulative logarithmic mark and its physical principal factor

**PROPOSED, WITH A SPECIFIED EXTERNAL ANALYTIC INPUT.** The new estimate
below is a consequence of Theorem 5 of the primary manuscript
[Structured cubic and sextic means for angular Gauss coefficients,
v3, 17 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/5).
That manuscript depends on the pinned OpenAI recursive inverse framework.
Its site review is not an independent audit by this packet. We state the
precise input and prove the new deduction; we do not claim a new zeta
zero-free region. This section uses the OLD Eisenstein-field interface,
not the general CT interface requiring mu_12.

## 1. The exact analytic input and coefficient class

Let E=Q(omega), q_a=Na, and use the primary generators, zero-extended
sextic symbols and normalized Gauss sums of the pinned original OpenAI
quasi-Riemann manuscript. Fix a finite S and a multiplicative finite ray
character nu supported there. Put

    C_l(c)=alpha(c)^l gamma_2(c),  l a fixed nonzero integer.

The imported input is the following pair of estimates, uniform in every
column length D>=1 and row ball 0<q_m<=K:

    sum_m |sum_(c sf) C_l(c)nu(c)chi_c(m)/sqrt(q_c)
                                  W(q_c/D)|^2 << K(KD)^epsilon;      (I)

    sum_(f~F) w(f) sum_m |sum_(c sf) C_l(c)nu(c)chi_c(m)
                       chi_c(f)^4 W(q_c/D)/sqrt(q_c)|^2
                     << (KDF)^epsilon F(K+KF).                     (II)

Here f is squarefree, 0<=w(f)<=a fixed divisor power, independent of m,c.
All ideals avoid S. A fixed finite combination of nu is allowed. The
test may be one COMMON smooth function of the normalized row, column
and label norms, with its finite seminorm paid. In (II) the puncture is
ONE. The displayed normalization follows by multiplying that source's
normalized label average by F and using its second alternative at Q=1.
No estimate for an arbitrary multiplier of c is being imported.

The exact CRT identity is

    C_l(pc')=C_l(p)C_l(c')chi_(c')(p)^4,  p does not divide c'.      (1)

The fourth power in (1) retains zero at p|c'. This fact will remove the
apparently growing puncture in the shared-prime calculation.

## 2. New complete logarithmic-mark estimate

Let V be a fixed smooth test with rapid decay at zero and infinity,
including the logarithmic Gaussian. Let v>=0 be fixed. Define the exact
native completed sum

    L_(m,v)(Z)=sum_(c sf,k)
      C_l(c) alpha(k)^(3l) nu(c k^3) chi_(c k^3)(m)
      log Nrad(c k) V(q_c q_k^3/Z) /[sqrt(q_c) q_k^(1+v)].          (2)

The ideals c,k may share every prime, and every k is included. The
radical is the ideal radical, so log Nrad(c k) counts a shared prime
once. For K,Z>=1,

    sum_(0<q_m<=K) |L_(m,v)(Z)|^2 <<_(v,epsilon) K(KZ)^epsilon.     (3)

This is a cumulative logarithmic mark. It is not an estimate for an
arbitrary annular prime mark, or for growing arbitrary column weights.

Proof. Use the exact identity

    log Nrad(c k)=log q_c+log Nrad(k)
                           -sum_(p|c,p|k)log q_p.                 (4)

For fixed k, the first two terms are an unlabelled core sum at length
Z/q_k^3, with a logarithmic column profile or a cube-only scalar. On
every column annulus log q_c is the sum of the logarithm of its central
length and a smooth normalized logarithm. Apply (I), keeping the complete
row zero chi_k(m)^3 as a contraction. For q_k<=Z^(1/3), Minkowski costs
only sum 1/q_k and logarithms, hence a fixed logarithmic power. When
q_k>Z^(1/3), use annuli q_c~D>=1: every required profile derivative is
O_A((q_k^3/Z)^(-A) D^(-A)), for arbitrary fixed A. Applying (I) on these
annuli makes the complete k and c tails summable. There is no omitted
large-cube sector. The extra q_k^-v only helps.

For the last term of (4), write k=ph and c=pc'. Then p does not divide
c' since c is squarefree, whereas p MAY divide h. Its scalar size is

    (log q_p)/[q_p^(3/2+v) q_h^(1+v)].                            (5)

The row factor is chi_p(m)^4 chi_h(m)^3. It is a contraction even at a
nonunit row, so may be discarded only AFTER Cauchy over p. Formula (1)
gives precisely the fourth-power label chi_(c')(p)^4. This symbol already
enforces p not dividing c'. Therefore use (II) with puncture ONE, not
puncture p. The complete Gaussian profile has exact argument

    q_(c') q_p^4 q_h^3/Z.                                        (6)

For p~P and fixed h, retain this as a common smooth profile in p/P and
the c' norm ratio; do not choose an independent profile for each p.
By (II), the sum over p of the squared row norms is

    << (KPZq_h)^epsilon P(K+KP) << (KPZq_h)^epsilon KP^2.          (7)

This uses the allowed nonnegative label weight supported on primes;
it does not claim a coherent label estimate. Cauchy on (5), together
with the elementary O(P) count of prime ideals in this annulus, gives
the root row norm

    << (KPZq_h)^epsilon sqrt(K)
             (1+log P) P^-v/q_h^(1+v).                          (8)

The label length and its positive average have both been paid. The
effective c' length is Z/(P^4 q_h^3). If it is at least one, sum the
P annuli and h harmonically; there are only logarithmically many P
annuli and h<=Z^(1/3). If it is below one, split c' into D>=1 annuli
and extract the full derivative majorant

    <<_A (P^4 q_h^3/Z)^(-A) D^(-A).

The same Cauchy estimate (8), with this majorant, sums over every large
P,h and D. Choose A after the preliminary epsilon and the finite test
seminorm order. This accounts for the entire joint Gaussian tail. It
also proves local absolute convergence of the original series.
Squaring the resulting root norm proves (3). All phases, common primes,
nonunit zeros and complete cubes were retained before the positive
inequalities. QED.

Exactly the same proof without the mark proves the complete cube-damped
native row bound with q_k^(-1-v), at every K,Z. Thus within input (I),
fixed cube damping v>=1/2 has no scale-power penalty. This is separate
from HYBRID_MOMENT.md, which uses a general-field quadratic sieve instead
of (I), and therefore has a larger proved exponent.

## 3. A finite reviewable realization of the cofinal prime sum

Let I_v(X,Y,Z) be the old physical probe with the sole native change
q_k^-1 -> q_k^(-1-v). Write I_(v;p) for insertion of 1_(p|c k^3).
For a good identity-ray prime p, the original compensated slot is

    I_(v;p)(X,Y,Zq_p)-q_p^(-3/2)I_v(X/q_p,Y/q_p,Z).

To synchronize the completed marked scale, evaluate this operation at
external scale Z/q_p. The resulting ACTUAL physical operation is

    I_(v;p)(X,Y,Z)-q_p^(-3/2)I_v(X/q_p,Y/q_p,Z/q_p).               (9)

A logarithmic prime sum of (9) has a cofinal physical limit. In its first
term the sum of log q_p over prime divisors of c k^3 is at most log(q_c
q_k^3); the Gaussian makes the complete coefficient majorant summable.
The second term has finite prime support at fixed X,Y: its annular s
support q_s approximately Y/q_p is empty for sufficiently large q_p.
There are no hidden physical infinite counterterm tails.

For polynomial row and outer scales, cutting the first prime sum at
q_p<=Z^(1+delta), any fixed delta>0, has an error smaller than any
prescribed negative power of Z, with a suitable full Gaussian tail
bound. Indeed a missing p must divide c or k; then q_c q_k^3>=q_p>Z^(1+delta).
Derivatives introduce only fixed powers of log q_c q_k^3. Thus this is
also a concrete finite family with its complete remainder.

The new operation must use ALL good prime divisors, rather than only the
identity-ray slots of the original seven-eighths construction. This is
legal for the principal target by a direct source calculation. In the
pinned source the local-P and local-P* calculation explicitly imposes no
ray restriction on p; it cancels the entire G/refinement and pair phases
before giving its local series. Inserting 1_(p|A) in the FULL corrected
physical probe replaces precisely P_p by P_p*. Changing only its three
real scales changes no arithmetic index or ray character, and contributes
only the displayed Mellin powers. Thus define (9) before expanding the
fixed finite correction into theta characters, keep all its coefficients,
and use this unrestricted local-P calculation. No assertion that theta(p)
is one is required. In the low proof, the finite theta expansion costs
only a fixed triangle factor; (2)--(8) allow every good prime and every
one of these fixed finite characters. The original identity-ray slot
restriction is not silently retained in the all-prime logarithm.

## 4. Exact principal arithmetic, including its remainder

We calculate for the principal target and all good primes, using the
unrestricted local-P calculation just explained. At the
principal Poisson residues w=1,z=1/6 write

    d=Q^-s,   R_v=kappa(p)Q^(3-6s-2v),
    A_v=1-(1-Q^-1)d-R_v/Q,   Q=q_p.

The exact local series gives

    P_(v,p)^*=(1+Q^-1)(R_v-d)/(1-R_v),
    P_(v,p)=(1+Q^-1)A_v/[(1-Q^-1)(1-R_v)].

Consequently the compensated local factor is

    B_(v,p)=Q^s P_(v,p)^*/P_(v,p)-Q^-1,
    B_(v,p)+1=(1-Q^-1)
        [Q^sR_v-(1-Q^-1)d-R_v/Q]/A_v.                           (10)

These are identities of rational local functions, first in absolute
convergence and then wherever their displayed denominators are nonzero.
For Re s>1/2 and v>=1/2, A_v is nonzero by the elementary local
contraction in CUBE_TILT.md. The principal factor H_v is also nonzero
there, by its complete regular-factor and shifted-L factorization.

The full high Mellin power of the external Gaussian scale is x+z-1.
Thus the extra Z -> Z/Q in (9) changes the standard local slot factor
Q^(z-1)B_(v,p) into Q^-x B_(v,p). At the principal residues x=s this
is Q^-s B_(v,p), not the old positive normalizer Q^-5/6.

For an UNRESTRICTED good-prime family define initially on Re s>1

    T_v(s)=sum_(p notin S)(log Q) Q^-s B_(v,p)(s).

Equation (10) proves

    T_v(s)= (zeta_E^S)'(s)/zeta_E^S(s)+E_v(s),                   (11)

where E_v is normally holomorphic on Re s>1/2 if v>=1/2. Explicitly
it is the sum of Q^-s(B_(v,p)+1)log Q and the positive prime-power tail
sum_(p,r>=2)(log Q)Q^(-rs). On closed substrips the former has complete
absolute prime majorants

    O(log Q)[ Q^(-2 Re s)+Q^(3-6 Re s-2v)
                                  +Q^(2-7 Re s-2v) ].          (12)

All three exponents are strictly below -1 when Re s>1/2,v>=1/2.
For v=0 the same proof gives the region Re s>2/3. No assertion of
absolute prime convergence below these regions is made.

Hence a principal Mellin detector containing H_v/zeta_E^S multiplied
by (11) retains EVERY zero rho of zeta_E^S in that region: at a zero
of order m>=1, the logarithmic derivative has residue m, so the product
has a nonzero pole of order m+1. A holomorphic E_v cannot cancel that
leading pole. Multiplying by the fixed entire auxiliary quadratic L
factor to extract ordinary zeta preserves an order at least two at an
ordinary zeta zero. Extra auxiliary zeros do not invalidate this claim.

Equation (11) uses the full prime set and that exact local correction at
every ray class. For an identity-ray subset alone, the leading prime
Dirichlet series would instead be a ray projection of a logarithmic
derivative, and could not be renamed the full zeta logarithmic derivative.

## 5. What is proved here, and the gate to a boundary improvement

The new deduction is the complete marked norm (3), including its
shared-prime term, conditional on the precisely stated analytic input
(I)--(II). Equations (9)--(12) identify a legal synchronized physical
operation and an exact zero-retaining principal arithmetic expression.
The all-ray local physical identity is justified above. Its complete
nonprincipal Poisson comparison still has to be proved before deriving
any new zero-free boundary.

Even the full valuation mark by itself supplies no automatic power
saving: sum_(p,r>=1)log q_p 1_(p^r|A)=log NA. With the Gaussian
G(log(NA/Z)), multiplication by log NA is exactly

    log Z times the original source + 2 d/d(log Z) of that source,

for the convention G(u)=constant*exp(-u^2/4). It preserves the source's
polynomial exponent and adds only logarithms. A higher principal pole
improves zero detection, but does not by itself improve that exponent.
The complete high comparison, with the actual ray masks, counterterms
and all cofinal tails, remains the test for a new zero-free boundary.

## 6. The available high envelope imposes a definite exponent floor

The cumulative logarithmic family does not reproduce the independent
annular prime amplification used by the original seven-eighths proof.
On nonprincipal rows its leading high correction is the corresponding
L'/L, with a holomorphic local remainder. Buffered Cauchy bounds for the
reciprocal and its derivative cost only an arbitrarily small conductor
power. They supply no new power saving in the count of exceptional rows.

Here is the exact optimization using the original BASE high envelope.
Put X=Z^x,Y=Z^y with x,y>0, and h=1-x>0. There is no independent prime
slot length ell in the cofinal family. From (3), the low separated probe
bound is Z^(max(x,y)/2+epsilon), because the additive row norm is
O(X+Y), the completed-row norm is O(XY), and the outside factor is
(XY)^(-1/2). The physical principal signal exponent is

    C(B)=B-5/6+x/3.

Thus a proposed boundary B requires

    B >= 5/6+max(x,y)/2-x/3.                                    (13)

The original row envelope is R(delta)=1-delta/2 for delta>=2/3.
In its top allowed bin a=beta, at the largest retained row exponent
d=h, the exact central exponent relative to C(beta) is

    -beta*y+(5/6)(1-x).                                       (14)

This follows by inserting R(delta)+delta/2=1, ell=0 and h=1-x
in the source's stage-high-exponent formula. The intermediate z_0
cancels. Therefore an improving application of that AVAILABLE envelope
requires, at its proposed boundary,

    B*y >= (5/6)(1-x),                                       (15)

with strict margin before losses. This is an optimization constraint of
these estimates, not a lower bound for the actual signed arithmetic sum.

Let m=max(x,y). From (13), B>=5/6+m/6, since x<=m, so m<=6B-5.
From (15), Bm>=(5/6)(1-m), so m>=5/(6B+5). Combining gives

    B^2 >= 5/6,  or B>=sqrt(30)/6 = 0.9128709291752768... .      (16)

The relaxed constraints attain equality at x=y=sqrt(30)-5; actual
contours require strict losses, and other row or tail estimates can
increase this floor. It already lies above the imported ordinary-zeta
benchmark near 0.875. Consequently the new cumulative-mark norm does
not, with this high envelope, improve that benchmark. It replaces only
the corresponding direct marked estimate. It does not replace the
prime-slot amplitude and refined high row-count hypotheses of Part II.
Keeping an annular prime weight avoids the logarithm collapse, but its
nonconstant residual column mark is precisely outside (I) and remains
the missing analytic input.
