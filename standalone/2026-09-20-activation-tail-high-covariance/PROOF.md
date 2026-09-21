# ATC29: activation-tail control and compulsory high-composite cancellation

**Status: proposed component proofs, pending independent mathematical review.**
**No full high-composite upper bound, new zero-free region, or RH proof.**
20 September 2026. Additive continuation of #904, frozen at
`879497b4f11be2618c448efc1fa93f69b4022e4c`.

This pass has two different outcomes. First, the complete nonlocal activation
correction has an upper budget with an EXTRA power saving in the previous native
energy estimate. The remaining high-composite target may therefore be stated
using only the modes at the CURRENT observation cutoff. Second, an actual native
semiprime packet has power-sized energy, and its covariance with the remaining
high-composite modes cancels its leading energy. We prove that covariance
asymptotic, but its absolute remainder is still at the classical prime-number-
theorem scale, not the scale needed for RH.

Do not interpret these results as an extension of NCG28's any-subset estimate to
all high denominators. We prove that an eventual all-subset SUBPOWER estimate is
impossible, even for the actual completed Mobius source. The desired complete
signed sum is a different object.

## 0. Objects, provenance, and the exact current-time target

Use ordinary Dirichlet convolution, with `1*mu=delta`. Let

    m(k)=sum_(n<=k)mu(n)/n, F_Y=sum_(k<=Y)m(k)^2,
    b=Y+1, B=b^2-1.

Preserve the entire native prefix through Y and use PCR26's capped reciprocal
completion c. At each subsequent index subtract the residual with a coefficient
of magnitude at most three, stopping at zero. Then

    sum c(n)/n=0, |c(n)|<=3, L<=Y+ceil(Y/2)<=2Y,
    sum_(k>Y)m_c(k)^2<=F_Y, m_c(k)=0 for k>=L.          (0.1)

These are inherited, source-specific completion statements, not free changes to
the next native prefix. Newton inversion gives

    v=2c-1*c*c,  mu-v=mu*(delta-1*c)*(delta-1*c),
    v(n)=mu(n), n<b^2.                                (0.2)

The strict upper endpoint remains strict. Write

    z=c*c, U_d=sum_(d|n)c(n)/n, B_q=sum_(q|d)z(d)/d,
    T_d(k)=(d-1)/2-(k mod d),
    R_q(k)=sum_(d|q)mu(q/d)T_d(k), q>=2,
    Z_q(k)=sum_(d|q)mu(q/d)H_floor(k/d)+Lambda(q).       (0.3)

All denominator sums stop at L^2. H_0=0 and Lambda is von Mangoldt. The exact
harmonic Newton identity from NCG28 is

    m(k)=2m_c(k)-sum_(q>=2)B_q Z_q(k), 1<=k<=B.        (0.4)

The Lambda(q) constants cannot be omitted from individual prime-power modes.
Only their complete source sum cancels, by
`sum_q B_q Lambda(q)=sum_d z(d)log(d)/d=0`.

Let X_j=b*2^j and set the EXACT integer schedule

    Q_j=min(L^2, floor((Y^4 X_j^6)^(1/11))).            (0.5)

For each composite q define its activation K_q to be the first X_j with q<=Q_j.
Let

    P_low(k)=sum_(q composite, q<=Q_j)B_q R_q(k)
                         for X_j<=k<X_(j+1),
    (TP)(k)=P(k)/(k+1)-sum_(n>k)P(n)/[n(n+1)].

The full tail map, not a finite-window replacement, satisfies

    ||TP||_(ell2,k>=b)^2
      =sum_(n>=b)P(n)^2/[n(n+1)]
       -b (sum_(n>=b)P(n)/[n(n+1)])^2.                (0.6)

For fixed q, T R_q=Z_q. Put W_low=T P_low and define the instantaneous sum

    L_inst(k)=sum_(q composite, q<=Q_j)B_q Z_q(k).

Then the inherited exact noncommutation identity is

    W_low(k)=L_inst(k)-Acal_j,
    Acal_j=sum_(q composite, q>Q_j)B_q A_q(K_q),
    A_q(K)=sum_(n>=K)R_q(n)/[n(n+1)]
          =R_q(K-1)/K-Z_q(K-1).                      (0.7)

Acal denotes a CORRECTION, not BNR26's balanced energy A. The correction is
constant on each dyadic block and zero after all denominators have activated.
It is not identically zero at earlier times.

The complementary instantaneous high sum is

    H_inst(k)=sum_(q composite, q>Q_j)B_q Z_q(k).

If W_high is NCG28's transformed moving high part, then

    W_high=H_inst+Acal.                               (0.8)

Our first theorem bounds Acal separately. This permits a current-time formulation
of the remaining target WITHOUT pretending that (0.7) commutes.

## 1. ATC29-1: the whole periodic tail gains two inverse powers of its start

For every q>=2 and integer K>=1,

    |A_q(K)| <= q^2/[2 K(K+1)].                       (1.1)

This includes the ENTIRE infinite tail and is independent of the source c.
It is not obtained by separately bounding the two terms in (0.7), which can be
much larger than their difference.

### Proof

R_q has period q, mean zero, and exact period variance

    (1/q)sum_(k=0)^(q-1) R_q(k)^2=J_2(q)/12<=q^2/12,
    J_2(q)=q^2 product_(p|q)(1-p^-2).                  (1.2)

Here is the finite-algebra derivation. T_d has period mean zero and variance
`(d^2-1)/12`. Finite Fourier inversion gives R_q exactly the reduced frequencies
with denominator q. Their coefficient is `1/(1-exp(-2*pi*i*a/q))`. Frequencies
with different reduced denominators are orthogonal over a common finite period.
Since T_d=sum_(q|d,q>=2)R_q, divisor inversion of its period variance gives (1.2).
This is classical finite Fourier/Ramanujan algebra, not a newly assumed spectrum.

A partial period starting at ANY integer has, by Cauchy--Schwarz, absolute sum
at most `sqrt(q)*sqrt(q J_2(q)/12)<=q^2/sqrt(12)<q^2/2`.
Full periods vanish, so the same bound holds for every partial sum starting at K.
Apply summation by parts to the decreasing weights w_n=1/[n(n+1)]. The boundary
at infinity vanishes and the differences telescope. The result is at most
`(q^2/2)w_K`, proving (1.1). No period-length divisibility of K is assumed. QED.

For activation K_q, (0.5) also gives

    K_q >= q^(11/6)Y^(-2/3),
    |A_q(K_q)| <= (1/2)Y^(4/3)q^(-5/3).              (1.3)

The first inequality follows from the admission inequality itself, including at
saturation. Every q here satisfies q<=L^2, so the cap does not invalidate it.

## 2. ATC29-2: a separately paid native activation correction

For the ACTUAL capped native source and every integer Y>=2,

    sum_(k>=b) Acal(k)^2
       <= 2^34 C_0 H_L^3 F_Y^(4/3) Y^(-1/11).         (2.1)

C_0 is the same finite absolute Euler constant as NCG28. This is a proposed
native component theorem using that packet's explicitly stated amplitude input;
it does not independently promote that predecessor to accepted mathematics.
Its elementary input and all new steps are recorded below.

### Source-amplitude input and its scope

NCG28 establishes for this source

    |B_q| <=256(F_Y/Y)^(2/3)q^(-2/3) W(q),
    sum_(q<=T)W(q)^2<=C_0 T H_floor(T)^3.              (2.2)

One explicit choice is

    G(q)=product_(p|q)(1-p^(-2/3))^(-1),
    W(q)=G(q)^2 product_(p^a||q)(a+1+a p^(-2/3)),
    C_0=product_p[1+4(h_p-1)/p],
    h_p=(1+p^(-2/3))^2/(1-p^(-2/3))^4, C_0<=exp(4860).

The native mechanism behind (2.2) must remain visible. Bounded increments give
`|m(n)|^3<=9F_Y/n`. For squarefree d, exact prime deletion expresses
`sum_(d|n,n<=Y)mu(n)/n` as `mu(d)m_d(Y/d)/d`, and m_d as a finite convolution
of m with d-smooth reciprocals. The entire capped completion then gives
`|U_d|<=16(F_Y/Y)^(1/3)d^(-2/3) G(d)`.
Expanding the local divisibility threshold
`1_(i+j>=a)` as the difference of its two adjacent sums of rectangular indicators
bounds B_q by the first line of (2.2). The second follows from
`W(q)^2<=d_4(q)product_(p|q)h_p` and a convergent nonnegative divisor expansion.
These are the NCG28 Section 1--2 arguments; they are not asserted for arbitrary
ternary sources. The predecessor proof was read and these implications checked,
but its whole numerical campaign was not rerun.

### Sum the full correction before bounding its energy

Cauchy--Schwarz in (2.2) gives

    sum_(q<=T)W(q)<=sqrt(C_0) T H_floor(T)^(3/2).

On consecutive dyadic q-intervals this implies, for integer Q>=1,

    sum_(q>Q)W(q)q^(-7/3)
       <=44 sqrt(C_0) H_Q^(3/2)Q^(-4/3).              (2.3)

For detail, the interval (2^r Q,2^(r+1)Q] costs at most
`2sqrt(C_0)Q^(-4/3)2^(-4r/3)H_(2^(r+1)Q)^(3/2)`.
Use `H_(2^(r+1)Q)<=(r+2)H_Q`, enlarge the geometric weight to 2^-r and the
power to (r+2)^2, and sum `sum_(r>=0)2^-r(r+2)^2=22`.

Combining (1.3), (2.2), and (2.3) gives the blockwise bound

    |Acal_j| <=5632 sqrt(C_0) F_Y^(2/3)Y^(2/3)
                         H_(Q_j)^(3/2) Q_j^(-4/3).     (2.4)

After saturation the correction is zero; before saturation let
`D_j=(Y^4 X_j^6)^(1/11)`. For Y>=2, X_j>=Y+1, D_j>=2, and hence
`Q_j=floor D_j>=D_j/2`. Also `H_(Q_j)<=H_(L^2)<=2H_L`.
Thus, paying every one of the X_j integer cells in the block,

    X_j Acal_j^2
      <=5632^2*8*7 C_0 H_L^3 F_Y^(4/3)
                              Y^(4/11)X_j^(-5/11).

We used `2^(8/3)<7`. The dyadic sum is less than `4b^(-5/11)` because
`2^(-5/11)<3/4`. Finally b>=Y and
`5632^2*8*7*4<2^34` prove (2.1). This is an all-block and all-tail estimate,
not a finite table extrapolation. QED.

The extra factor Y^(-1/11) is independent of whether F_Y is bounded, logarithmic,
or power-sized. It is a saving for THIS correction, not for the entire high part.

## 3. Consequence: the remaining covariance can be measured at the current time

The parent has `||W_low||^2 << H_Y^5 F_Y^(4/3)`. Equations (0.7) and (2.1) give

    ||L_inst||^2 <=2||W_low||^2+2||Acal||^2
                 << H_Y^5 F_Y^(4/3).                  (3.1)

To absorb the smaller term, use H_L<=2H_Y and boundedness of
`H_Y Y^(-1/11)`; for example `1+log Y<=12Y^(1/11)` suffices.
The constants are absolute, coarse, and not fitted to numerical data.

Similarly the two possible high targets satisfy

    ||H_inst||_(b..B) <= ||W_high||_(b..B)+||Acal||,
    ||W_high||_(b..B) <= ||H_inst||_(b..B)+||Acal||.     (3.2)

Thus a subquadratic-in-F budget for either one, with fixed logarithmic losses,
transfers to the other after adding the already controlled 4/3-power correction.
The complete actual update may now be written exactly as

    m(k)=2m_c(k)-W_prime(k)-L_inst(k)-H_inst(k),
                                               b<=k<=B.    (3.3)

The correction cancels between the two instantaneous components; it has not
been set to zero in either transformed component. One must still pay (2.1)
when transporting an estimate between versions.

This result simplifies the analytic and computational target. It does not bound
the main instantaneous high-composite norm. Nor is it a new RH criterion counted
as a separate proof route.

## 4. A generic ceiling useful for comparing large native components

For ANY reciprocal-balanced source supported through L<=2Y with |c|<=K,

    |B_q|<=K^2 H_L^2 tau(q)/q.                         (4.1)

If q|rs, at least one d|q has d|r and (q/d)|s. Enlarge by the sum of these
nonnegative rectangular indicators, then bound the two reciprocal sums by
`K H_L/d` and `K H_L/(q/d)`. This proves (4.1), including prime powers.
It uses no native divisor-inverse identities and no false multiplicative law.

We claim the two full-future bounds

    ||P_low||_physical^2 <=32 K^4 H_L^8 Y^(8/11),
    ||Acal||_ell2^2 <=2^13 K^4 H_L^6 Y^(7/11).         (4.2)

Consequently

    ||L_inst||^2 <=2^15 K^4 H_L^8 Y^(8/11).            (4.3)

These estimates are WEAKER than the native bound when F is small, but have a
fixed exponent less than one in Y. They will keep the already controlled low
modes out of the leading power-sized compensation calculation below.

### Proof of the first ceiling

Reduced fractions with denominators <=Q are separated by Q^-2. Finite geometric
summation and the Schur row bound give, on X consecutive integers,

    sum |sum_(q in A)B_q R_q(k)|^2
      <=[X+Q^2 H_(Q^2)] sum_(q in A)B_q^2 J_2(q)/12.

This elementary logarithmic-loss additive large sieve is proved in NCG28:
sort neighboring frequencies on each side of one frequency, use distance at
least j/Q^2, and sum the reciprocal-distance row. It does not assume quadratic
sample orthogonality, complete periods, or favorable covariance signs.

The elementary inequality `tau(q)^2<=d_4(q)` gives
`sum_(q<=Q)tau(q)^2<=QH_Q^3`. Thus the coefficient mass is at most
`K^4 H_L^4 QH_Q^3/12`. On the weighted block [X_j,2X_j), using H_Q<=2H_L,
the resulting bound is at most

    (2/3)K^4 H_L^7 Q_j/X_j
     +(8/3)K^4 H_L^8 Q_j^3/X_j^2.

Always `Q_j<=Y^(4/11)X_j^(6/11)`, even after saturation. Sum the two geometric
bounds with ratios 2^-5/11 and 2^-4/11, whose sums are less than four and five.
Using b>=Y gives (4.2)'s first statement (with room in 32).

### Proof of the second ceiling

Since `sum_(q<=T)tau(q)<=TH_T`, dyadic summation gives

    sum_(q>Q)tau(q)q^(-8/3)<=12H_Q Q^(-5/3).

Use (1.3) and (4.1) to obtain
`|Acal_j|<=6K^2 H_L^2 Y^(4/3)H_Q Q^(-5/3)`.
Before saturation, floor D_j>=D_j/2; after saturation Acal is zero. Use
H_Q<=2H_L, `2^(10/3)<11`, and
`sum_(j>=0)2^(-9j/11)<3`. The total is at most
`12^2*11*3 K^4 H_L^6 Y^(7/11)<2^13 K^4 H_L^6 Y^(7/11)`.
This proves the second statement. Contractivity of T and (0.7) prove (4.3).

## 5. ATC29-3: an explicitly large ACTUAL high-semiprime packet

Set

    P_Y={p prime: 3(Y+1)/4 < p <=Y},
    I_Y={Y+1,...,floor(5Y/4)},
    a_Y=(sum_(p in P_Y)1/p)^2-sum_(p in P_Y)1/p^2,
    S_Y(k)=sum_(p<r in P_Y)B_(pr)Z_(pr)(k).            (5.1)

For all sufficiently large Y (and for the declared finite test cases),

    B_(pr)=2/(pr),
    S_Y(k)=a_Y(H_k-2), k in I_Y.                      (5.2)

These are ACTUAL capped-native amplitudes, not independently chosen weights.
The capped completion ends by Y+ceil(Y/2), which is smaller than 2p for every
p in P_Y. Thus the only supported index divisible by p is p itself, with
coefficient -1. The only two ordered source pairs whose product is divisible
by pr are (p,r) and (r,p). This proves the first identity.

For k in I_Y, p,r<=k<2p,2r and k<pr. Since Lambda(pr)=0,
`Z_(pr)(k)=H_k-H_floor(k/p)-H_floor(k/r)+H_floor(k/(pr))=H_k-2`.
The distinct-prime restriction is essential: prime squares have a log p term.
Summing 2/(pr) proves the second identity. The denominator band lies above Q_0
for all sufficiently large Y, since its lower endpoint is a constant times Y^2
whereas Q_0 is of order Y^(10/11).

Let lambda=log(4/3). The classical prime number theorem and partial summation give

    sum_(p in P_Y)1/p ~ lambda/log Y,
    sum_(p in P_Y)1/p^2=O(1/(Y log Y)).

Also H_k-2~log Y uniformly on I_Y, which has Y/4+O(1) cells. Therefore

    E_sem(Y):=sum_(k in I_Y)S_Y(k)^2
        ~ (lambda^4/4) Y/(log Y)^2.                   (5.3)

This is an unconditional lower/asymptotic theorem using the classical PNT.
It is not a new prime-distribution theorem, and no effective first Y is claimed.

### What this rules out

There is no Y^o(1) bound for EVERY subset of actual denominators through Y^2:
(5.1) is an explicit counterexample subset. In particular a plan that both
proves F_Y=Y^o(1) and extends NCG28's fixed-power-in-F, any-subset inequality to
all denominators through Y^2 is inconsistent with (5.3).

This does NOT refute the specific complete signed high-component target. It
also does not unconditionally refute a bound in F alone, whose growth is unknown.
Under RH, however, F is subpower and any such all-subset, fixed-power-F extension
would fail. The distinction between the complete sum and arbitrary subpackets
is mathematically necessary, not just cautious wording.

## 6. ATC29-4: the remaining HIGH composites cancel this large packet

On I_Y, let G_Y=H_inst from (3.3), and define

    R_Y=G_Y-S_Y,
    C_sem,rest(Y)=2 sum_(k in I_Y)S_Y(k)R_Y(k).         (6.1)

R_Y contains ALL other high composite denominators, with their signs. It is
not the low sector, prime sector, a freely chosen counterterm, or a fake source.
For every fixed A>0,

    ||G_Y||_I^2=O_A(Y/(log Y)^A),
    ||R_Y||_I^2=E_sem(Y)+O_A(Y/(log Y)^A),
    C_sem,rest(Y)=-2E_sem(Y)+O_A(Y/(log Y)^A).          (6.2)

In particular the leading signed high/high covariance is

    C_sem,rest(Y) ~ -(lambda^4/2)Y/(log Y)^2.          (6.3)

### Proof, and exactly which external theorem enters

The classical zero-free-region estimates for M imply
`M(x)=O_A(x/(log x)^A)` for every A. Together with m(infinity)=0, partial
summation gives `m(x)=O_A((log x)^-A)` for every A. For example use the M bound
with exponent A+2 in

    m(x)=M(x)/x-integral_x^infinity M(t)dt/t^2.

The all-scale decay is an IMPORTED classical analytic input. Lee--Leong's
explicit Mertens estimates are more than sufficient; no particular numerical
constant or zero-verification receipt from their work is consumed here.
Tao's account supplies the standard PNT/m(infinity)=0 relationship. These
sources are recorded in SOURCES.md.

For the capped completion, |m_c(k)|<=|m(Y)| after Y. Hence (0.4) gives on I_Y

    ||sum_(q>=2)B_q Z_q||_I^2=O_A(Y/(log Y)^A).

The whole prime sector has full-future norm at most `K^4 H_L^6/(4b)` by DSE27
and the contractive tail map. The instantaneous low sector satisfies (4.3),
which is `O(Y^(8/11)(log Y)^8)`, hence `O_A(Y/(log Y)^A)` for every fixed A.
Subtract these two fully specified components using a valid three-term Cauchy
bound. This proves the first assertion of (6.2) for K=3.

Finally R=G-S gives exactly

    C_sem,rest=-2E_sem+2<S,G>,
    ||R||^2=E_sem-2<S,G>+||G||^2.                      (6.4)

Use Cauchy--Schwarz, (5.3), and the first assertion with a sufficiently large
logarithmic exponent to obtain each asserted O_A error. QED.

### Why this is NOT the missing RH estimate

We have proved a signed covariance asymptotic for a real high-composite
subpacket and its actual high-composite complement. But `Y/(log Y)^A`, even for
every fixed A, is not Y^o(1). It can still have logarithmic growth exponent one.
Subtracting the two large leading energies requires an ABSOLUTE residual bound
at the RH-sensitive scale, not merely arbitrarily good logarithmic relative
cancellation. This pass supplies no such new absolute bound for G or for the
full high contribution on b..B.

The leading covariance is eventually negative. It is NOT negative at every
finite Y: our complete native Y=95 panel has positive C_sem,rest. No onset or
monotone improvement is extrapolated from the finite cases.

## 7. Finite execution and the next experiment actually enabled

The checker retains the complete correction (0.7) on every dyadic block until
saturation and sums `X_j Acal_j^2` exactly with outward enclosures. It also
computes a source-dependent finite whole-tail envelope from (1.1), without
using exp(4860) as a numerical certificate.

Small complete panels Y=31,63,95,127 retain every local observation cell in I_Y,
all native source coefficients, all B_q identities, centering constants, the
high/semiprime/other-high energy ledger, and full direct high spectral checks at
three declared points per panel. Every other point's high component is evaluated
by exact complementary algebra, not a falsely claimed independent exhaustive
spectral summation. The largest harmonic tail argument is 4,194,303; this is NOT
a Mobius computation to that height.

Separate larger panels Y=4095,16383,65535 compare the semiprime packet with ALL
other spectral modes, not just the high ones. A short-source integer Newton
calculation generates the relevant local output and two finite Mobius methods
check it. The largest native endpoint is 81,918, NOT the end of a square stage.
No new Mertens or zero-computation record is claimed.

At Y=65535, descriptive decimals from directed enclosures are about

    semiprime energy       0.7410439745561518
    all-other-mode energy  0.8268642831292799
    twice covariance      -1.5638782740995609
    combined Q energy      0.0040299835858708.

This is a FINITE demonstration of substantial signed cancellation. It is not a
fit used to prove (6.2), an unbounded energy estimate, or a fraction of RH solved.

The analytic next target is H_inst itself on the full new native annulus, keeping
its internal high/high signs. Thanks to Section 2, this target can now be
investigated without evaluating future activation tails. Any proposed splitting
into independently small high-denominator types must pass the native semiprime
control (5.3). We do not replace that target by the much stronger and false goal
of making every high packet small.
