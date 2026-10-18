# Simultaneous growing-order moments of the original native source

**Status: PROPOSED complete source-qualified deduction; independent mathematical
review is required.** The two deep inputs below are adopted at their printed,
fixed-field scope. In particular the common 31/32 zero-free statement is an
INPUT, not a conclusion proved here. No RH, new zero-free fraction, uncapped
critical inverse-moment law, or signed theta-to-native projection is claimed.

The new result is uniformity in an explicitly growing moment order for the
COMPLETE original family. It is not obtained by substituting a moving order
in an earlier fixed-order theorem. All parameter-dependent analytic constants
needed for that change are bounded below. The historical 53-threshold density
certificate and Euler-mask identity are credited, not new discoveries.

## 1. Literal observable, inputs, and statement

Fix a number field F containing mu_6 and the admissible fixed S and UNTWISTED
choice-compatible de Faveri sextic family used in #983. Indices are nonzero
integral exterior ideals, counted by their FULL ideal norms q(a)=Na. Characters
are extended by zero at the original nonunits. Different ideals of equal norm
remain different indices. Fix real c and tau>0 and set

    W(y)=y^(-c) exp[-(log y)^2/(4tau)]/sqrt(4 pi tau),
    A_u(D)=sum_n mu_F(n) chi_u(n) W(q(n)/D),
    M_p(D,H)=sum_(q(u)<=H) |A_u(D)|^p.                         (1)

The Gaussian and both infinite tails are unchanged. There is no norm-twist,
angular, time, or independent-prime average. Only the original row sum occurs.

Use these explicitly named contracts:

* ZF: Cureton--Thorner, Hexagon 2610.00200v2, its printed common zero-free
  half-plane Re s>theta=31/32 for finite-order Hecke L-functions. At the
  principal pole the reciprocal has its removable value zero.
* ZD: de Faveri, arXiv:2610.04045v1, Corollary 1.5, for this exact untwisted
  sixth-power-free ideal family. At any fixed threshold sigma used below and
  any fixed eta>0, choose a sufficiently small fixed rho>0 so the number of
  nonprincipal cores a~U with a zero in Re s>=sigma, |Im s|<=4U^rho is
  O(U^(g_6(sigma)+eta)). One rho suffices for our finite list of thresholds.
* Classical Hecke continuation, functional equation, uniform polynomial
  conductor/height bounds on fixed strips, and the uniformly convergent Euler
  logarithm to the right of one. The field, S, and archimedean types are fixed.
  Also I_F(x)<=C_F x for x>=1.

The source identification, Gaussian Mellin identity, and repeated-row law are
those of #983. The proofs below rederive the transfers that need uniform order
constants. No analytic result from #984 is used. SOURCES.md pins the exact
repository reads and their review limitations.

For sufficiently large D write

    L=log D,   ell=log L,   m=log ell,
    delta_D=100 m/ell.                                        (2)

All logarithms are natural. Increasing the fixed threshold D0 makes m>1 and
0<delta_D<1/1024.

**Theorem T (simultaneous envelope).** There exists ONE D0, depending only on
F,S,c,tau, the fixed family and the adopted analytic contracts, such that for
EVERY real D>=D0, EVERY real p and H satisfying

    1<=p<=ell/m,          2<=H<=D^(p/4),                       (3)

one has

    M_p(D,H) <= H^(1/6)
                  D^(theta*p + 100*p*m/ell + L^(-1/4)).       (4)

There is no unrecorded order-dependent constant on the right of (4). D0 is
not evaluated numerically; the first guaranteed scale can be enormous. This
is an asymptotic uniformity theorem, not a practical numerical certificate.

In particular, for ANY real orders p(D)>=1 with

    p(D) log log log D = o(log log D),                         (5)

and ANY 2<=H(D)<=D^(p(D)/4),

    M_(p(D))(D,H(D)) <= H(D)^(1/6) D^(theta*p(D)+o(1)).        (6)

For the explicit common range 1<=p<=ell/m^2 the o(1) in (6) can be replaced
by 100/m+L^(-1/4). Thus even orders can genuinely tend to infinity with D.
No uniformity over changing fields, exclusions, family constructions or
smoothing parameters is claimed.

## 2. A quantitative reciprocal estimate near the INPUT boundary

This section pays for a line that approaches theta. Merely writing an
unspecified O_(delta,eta)(Q^eta) would not suffice for Theorem T.

**Lemma Q.** Let 0<delta<=1/1024 and v=theta+delta. For each primitive
finite-order Hecke member of conductor norm Q, uniformly in t and
v<=x<=2, the analytic contracts and ZF imply

    log^+ |1/L(x+it,chi)|
      <= C delta^(-2) [log(e^2 Q(2+|t|))]^(1-delta/10).       (7)

The constant C is independent of delta, chi, Q and t. The regularized principal
case is included, with a harmless fixed enlargement of C.

**Proof.** For nonprincipal chi put g=L; for the principal member put

    g(s)=(s-1)L(s)/(s+1).

It is holomorphic and nowhere zero on Re s>theta, including at one. Its
analytic logarithm f agrees with the Euler branch (and the displayed rational
factor) on the right. At 2+it that branch is uniformly bounded. Polynomial
strip bounds for g give a uniform upper bound for Re f=log|g| by
C log(e^2 Q(2+|t|)) on each of the following disks.

Center all disks at 2+it and set

    R=2-theta-delta/8,       r_o=2-theta-delta/4,
    r_t=2-theta-delta,       r_i=1-delta/8.                   (8)

They obey R>r_o>r_t>r_i>0. The outer disk is wholly within Re s>theta.
Borel--Caratheodory, with R-r_o=delta/8, bounds |f| on r_o by
C delta^(-1) log(e^2 Q(2+|t|)). On r_i, Re s>=1+delta/8; ideal counting
bounds the absolutely convergent Euler logarithm by C/delta. The principal
rational logarithm costs at most this as well.

Hadamard three circles bounds |f| on r_t by

    C delta^(-1) [log(e^2 Q(2+|t|))]^alpha,
    alpha=log(r_t/r_i)/log(r_o/r_i).

Here r_o<2 and r_o/r_i<2, so log(r_o/r_i)<1. Also

    log(r_o/r_t) >= (r_o-r_t)/r_o >= 3delta/8.

Consequently 1-alpha>=3delta/8>=delta/10. The leftmost target point is
v+it and the disk covers every x+it with v<=x<=2. Exponentiating the real
part of -f proves (7), weakening delta^(-1) to delta^(-2). In the principal
case 1/L=[(s-1)/(s+1)]/g and that rational factor has modulus at most one
for Re s>0. This includes the removable reciprocal zero at s=1. QED.

For completeness, extra imprimitive deletions introduce no uncontrolled
moving-delta constants. Uniformly for v>=3/4,

    log product_(p|a)(1-q(p)^(-v))^(-1)
                               <= C(1+log(2+q(a)))^(1/4).    (9)

To see this, use -log(1-q^-v)<=C q^-3/4 and split at
Y=max(2,log(2+q(a))). Primes below Y cost O(Y^(1/4)) even when summed over
ALL ideals. Primes above Y number at most log q(a)/log Y and cost at most
that number times Y^-3/4. Distinct equal-norm primes and all omissions are
retained. The right side of (9) is absorbed in (7)'s larger logarithmic
power. For the exact sixth-free cores the outside-S conductor is already
the radical of the core; the more general argument (9) is harmless.

Define E_v(a;D)=sup_(0<X<=D) X^(-v)|A_a(X)|. The original Mellin identity is

    Mellin(A_a)(s)=exp[tau(s-c)^2]/L^S(s,chi_a), Re s>1.       (10)

Contour shifting of this very integral, not construction of a replacement
function, gives the following consequence of (7):

    log(1+E_(theta+delta)(a;infinity))
       <= C delta^(-2) {
           (1+log(2+q(a)))^(1-delta/10)
                          +log(2+delta^(-1))}.               (11)

Indeed the conductor satisfies Q<=C q(a). With q=1-delta/10 in (0,1),
(A+B)^q<=A^q+B^q and B^q<=1+B for B>=0. Thus the height part of (7)
is bounded by a factor (2+|t|)^K with K=C delta^-2. Its Gaussian integral
has logarithm O((1+K)log(2+K)): use the maximum of
(2+|t|)^K exp(-tau*t^2/2) and then integrate the remaining Gaussian.
All real parts stay in a fixed strip, so the test's real prefactor is bounded.
This proves (11). The same estimates send both horizontal edges to zero.
The normalization by X^v is uniform for ALL positive X, including X<1;
there are no zero poles to cross under ZF. Constants in (11) do not depend
on delta, p, D, a or H.

## 3. Fixed rectangles suffice above a SUBPOWER core cutoff

The finite-height adapter in the pending density packet used U>=D^kappa.
Here a weaker cutoff is necessary to avoid an order-dependent small-core loss.

Fix b=1/100000. For any one of our fixed density thresholds sigma, consider
cores a~U whose L-functions have no zero with Re s>=sigma and
|Im s|<=4U^rho. For U sufficiently large, the logarithm/disc argument with
fixed buffer b gives, uniformly for sigma+b<=x<=2 and |t|<=2U^rho,

    log^+ |1/L^S(x+it,chi_a)| <= C(1+log U)^omega,
                                      some fixed omega<1.   (12)

The maximum of the finitely many omega can be used. It can be chosen at
least 1/4 to absorb (9). All constants are independent of p. Nonprincipal
cores only enter these rectangles; the unit core is handled globally.

Truncate the ORIGINAL Gaussian Mellin integral at T=U^rho and move only its
central segment. For every 0<X<=D, after division by X^(sigma+b), the two
horizontal pieces and original vertical tails are bounded by

    C(1+D^2) U^C(1+T)^C exp(-tau*T^2/2).                    (13)

The central vertical piece has bound exp(C(1+log U)^omega). These estimates
retain the parts above the known zero-free rectangle on their ORIGINAL
right-hand line; no untruncated contour shift is asserted.

Suppose now

    log U >= (1/2) sqrt(log D).                              (14)

Then log D<=4(log U)^2. The negative exponential in (13) dominates this
entire quadratic expression in log U, and all fixed polynomial factors.
Thus, throughout (14),

    log(1+E_(sigma+b)(a;D)) <= C(1+log U)^omega.             (15)

A bounded initial interval is irrelevant after the D0 in Theorem T is fixed.
This proves a maximal estimate at the SAME core height for every smaller
column scale, not an estimate at one X silently turned into a supremum.

## 4. Uniform cost of EVERY repeated row, for real growing p

The exact source identity, including shared primes, is

    chi_(a b0^6)(n)=chi_a(n) 1_((b0,n)=1),
    A_(a b0^6)(D)
       =sum_(d supported on primes(b0)) chi_a(d) A_a(D/q(d)). (16)

The sum contains all powers and converges absolutely by Gaussian flatness.
Its finite Euler inverse is unchanged. For v>0 it follows that

    |A_(a b0^6)(D)| <= D^v E_v(a;D) P_v(b0),
    P_v(b0)=product_(p|b0)(1-q(p)^(-v))^(-1).               (17)

For EVERY real p>=1, uniformly for v>=3/4 and B>=1,

    sum_(q(b0)<=B) P_v(b0)^p <= C_F B exp[C_F'(1+p^2)].      (18)

Here and subsequently fixed F,S dependencies can be absorbed in C.
Proof: it is enough to use v=3/4. Expand P_v(b0)^p into its nonnegative
squarefree divisor convolution. Its average is at most C_F B times

    C_v(p)=product_q [1+((1-q^-v)^(-p)-1)/q].               (19)

Put c_v=(1-2^-v)^(-1), X=(c_v p)^(1/v). For q<=X, the logarithm of the
local factor is at most c_v p q^-v; summing over all ideals is
O((c_v p)^(1/v)). For q>X, use exp(t)-1<=2t for 0<=t<=1 to bound the
COMPLETE infinite tail by O(c_v p X^-v)=O(1). Thus
log C_(3/4)(p)<=C(1+p^(4/3))<=C'(1+p^2). No prime ideal theorem or
independence of masks is used. This rederives the explicit uniform bound
already available for fixed-core transfer in #983; it is not a new Euler
mask theorem.

For ANY collection C of sixth-free cores, with respective exponents v_a>=3/4,
(17)--(18) give

    sum_(u=a b0^6, a in C, q(u)<=H) |A_u(D)|^p
      <= C H^(1/6) exp[C(1+p^2)]
            sum_(a in C, q(a)<=H) q(a)^(-1/6)
                               D^(p v_a) E_(v_a)(a;D)^p.   (20)

Every u occurs exactly once. There is no imposed (a,b0)=1. Formula (20)
is valid for real orders, not only even integer powers. No moving-order
constant is left hidden in it.

## 5. One FIXED density partition, not a changing theorem parameter

The file DENSITY_CERTIFICATE.json copies, with attribution and an original
hash, the 53 rational thresholds from the historical pending packet.
Their g values are recomputed directly from de Faveri's displayed formulas:

 g(s)=1-(2s-1)[36(2s-1)-6(6s-2)+3]
                   /[36(2s-1)(3-2s)-24s+2],  s<=11/12;
 g(s)=1-(8s^2-10s+3)/[1-24(1-s)^2],          s>=11/12.       (21)

Only thresholds in [3/4,121/125] are used. They agree at 11/12. Write
sigma_0=3/4,...,sigma_J=121/125, J=52; let g_j=g(sigma_j), f=1/6,
and gamma=1/400. The exact certificate gives

    f+4theta-(1+4sigma_0)=1/24>gamma;
    f+4theta-max(g_j,f)-4sigma_(j+1)>gamma, j=0,...,51;
    f-g_J=313/91446>gamma.                                 (22)

Its minimum middle margin is 9387546301/3528153375000. This old rational
certificate is REUSED, not claimed as the new contribution.

Fix eta0=1/100000, independently of D,p,H, and choose rho ONCE so ZD gives
counts C U^(g_j+eta0) at all 53 thresholds. Any strict/non-strict endpoint
convention is handled first by a fixed tiny left buffer within this loss.
This choice never depends on p. Denote the nested exceptional sets E_j(U).
There are 54 disjoint classes: the good complement, 52 differences, and
E_J. A difference is COUNTED at j and bounded on the zero-free line
sigma_(j+1)+b; it is not assigned its upper threshold's smaller count.

The main new uniformity is supplied by (11), (15), and (18), NOT by asking
a zero-density theorem for a loss eta0/p with an uncontrolled constant.

## 6. All large-core envelopes can be raised to the moving order

Set

    U0=exp(sqrt L),       delta=100m/ell.                     (23)

Group core ideals in dyads; boundary dyads intersecting U0 have
log U >= sqrt L-log 2 >= (1/2)sqrt L. Fixed factors two in norms have
no effect on the estimates below. Cores q(a)<U0 are handled separately.

For large U and a nonterminal good or middle class, (15) gives

    p log(1+E_(sigma+b)(a;D))/log U
       <= C (ell/m)(log U)^(omega-1) = o(1)                 (24)

UNIFORMLY for (3) and U>=U0/2. Its maximum is bounded by
C(ell/m) exp[-(1-omega)ell/2+O(1)], which tends to zero.

For the terminal class use the global bound (11) on the MOVING line
v=theta+delta. Write t=log U; t>=sqrt L/2. Then

 p log(1+E_v(a;infinity))/t
   <= C p delta^-2 [t^(-delta/10)+log(2+delta^-1)/t].        (25)

The constants are uniform in the entire relevant core range, even if
H is as large as D^(p/4). Directly from (2)--(3),

    p delta^-2 <= ell^3/(10000m^3),
    t^(-delta/10) <= exp[-5m+O(m/ell)],
    log(2+delta^-1)=O(m).

The first term of (25) is therefore O(ell^-2/m^3); the other is
O(ell^3/(m^2 sqrt L)). Both tend to zero. Unlike a fixed-order big-O,
these bounds actually control the growth of its constant as delta tends
to zero and p tends to infinity.

Increasing ONE D0, (24)--(25) imply, on every respective class,

    E_v(a;D)^p <= U^eta0.                                  (26)

The finite small-U cases no longer occur here. This uses the fixed
eta0 already chosen, not a redefinition of the exceptional sets.

## 7. Complete moment estimate: small, good, middle, and terminal cores

### Small cores

Use the global v=theta+delta on ALL q(a)<U0, including principal and any
bounded initial cores. From (11), since 1+log(2+q(a))<=C sqrt L,

 p log(1+E_v(a;infinity))
   <= C p delta^-2 [sqrt L+log(2+delta^-1)].                 (27)

Weighted ideal counting gives sum_(q(a)<=U0)q(a)^(-1/6)<=C U0^(5/6).
Using the smaller cap min(H,U0) only improves this upper bound. By (20),

    M_small <= H^(1/6) D^(p(theta+delta)) exp[B_D],
    B_D <= C {sqrt L+p delta^-2(sqrt L+log(2+delta^-1))
                                                   +1+p^2}.

Uniformly for p<=ell/m, B_D=o(L^(3/4)). All Gaussian scales, all repeated
rows, and all small nonprincipal cores remain; none is assumed to be a
new random character.

### Good and middle cores

Apply (20), the appropriate fixed v=sigma+b, fixed density counts, and
(26). For a middle class the dyadic weight is

    U^(g_j-1/6+2eta0).

The good class has the same upper formula with g=1 and sigma=sigma_0.
Summing all dyads U<=H gives at most a factor C(1+log H) times
H^max(g-1/6+2eta0,0). Because H<=D^(p/4), (22) proves

    p(sigma+b)+(p/4)max(g-1/6+2eta0,0)
       <= p theta-p gamma/4+p b+p eta0/2
       <= p theta-p gamma/8.                              (28)

The last inequality uses b+eta0/2<gamma/8, exactly checked. With the fixed
number of classes and the mask cost, this entire sector is bounded by

    H^(1/6) D^(p theta-p gamma/8)
                         exp[C(1+p^2)] C(1+log H).

The logarithm of the extra factor is o(L^(3/4)) uniformly in (3).
There is no deleted terminal class or scalar-convexity substitution.

### Terminal large cores

Use v=theta+delta and E_J's count, retaining every exceptional member.
Since g_J-1/6+2eta0<-gamma/2, the dyadic sum from U0/2 upward is bounded,
in fact decays like exp(-c sqrt L). Hence

    M_terminal <= C H^(1/6) D^(p(theta+delta)) exp[C(1+p^2)]. (29)

The estimate of its values comes from the explicitly named ZF input,
not from the zero-density theorem or from an omitted exceptional set.

### Combine

Each logarithmic prefactor in these three sectors is o(L^(3/4)), uniformly
for (3). There are only finitely many sectors. Choose D0 so their combined
prefactor is at most exp(L^(3/4)). Since p delta=100p m/ell, the sum of
(27)--(29) is exactly (4). This proves Theorem T from its two named inputs.
The choice of D0 is common to all p,H in the displayed ranges. QED.

**Useful localization.** For every fixed kappa>0, increasing D0 in terms of
kappa, the same proof gives, simultaneously for 1<=p<=ell/m^2 and
2<=H<=D^(p/4),

 sum_(u=a b0^6, q(u)<=H, q(a)>=D^kappa) |A_u(D)|^p
    <= H^(1/6) D^(theta*p-min(kappa,1)/20000).              (30)

An empty range has sum zero. For these cores no small-core sector occurs.
The good/middle sector saves p gamma/8 before negligible prefactors. The
terminal weighted count saves kappa gamma/2, whereas p delta<=100/m tends
to zero. Mask, dyadic and finite-class prefactors have logarithm o(L).
Spending less than one quarter of the smaller fixed margin gives the
weaker advertised 1/20000 constant. This is a uniform growing-order version
of earlier fixed-order localization, not evidence that the remaining small
cores have been controlled at square-root strength.

## 8. What was proved beyond the previous packets, and what was not

The pending density packet establishes the same main exponent for EACH
fixed p, with arbitrary order-dependent constants. Updated #983 supplies a
fixed-core growing-order mask transfer only AFTER a native envelope is
provided, and a two-class density-native bound with fixed k,h and losses.
Here quantitative moving-line reciprocity, a subpower core cutoff, and
one fixed density partition control ALL growing cores and ALL repetitions
with ONE asymptotic order range. The exponent table itself and the mask
algebra are inherited and credited.

A nonquantitative diagonal argument can extract SOME sufficiently slow
unbounded order schedule from earlier fixed-order bounds. It does not give
our explicit rate, the common envelope (4), or uniformity on the entire order
range (3). The contribution is that specified uniformity, not mere existence
of an unspecified moving subsequence.

There is no general rule that a collection of fixed-order inequalities
implies (6) for the explicit schedules stated here. For a simple scalar countermodel, C_p=exp(exp(p^2)) is finite
for every fixed p. A statement F_p(D)<=C_p D^(theta*p) is then a valid
fixed-p estimate. At p=sqrt(log log D), however, C_p=D. This order obeys
(5), but it creates a FULL extra power of D, not D^o(1). The new quantitative
lemmas are necessary; this countermodel says nothing about actual Mobius
values.

The source-qualified improvement is real uniformity, not a new memberwise
zero-free result. At H=D^h, the gap between (6)'s exponent and the desired
critical H D^(p/2) scale is

    p(theta-1/2)-5h/6+o(1)=15p/32-5h/6+o(1).

This does NOT vanish by increasing p. The principal fixed source may still
be the hard core. A new bound for it, or a source-faithful signed projection
that improves its exponent, remains a distinct unsupplied step. No criterion
is being labelled as a proof of its open premise, and no practical zero
census or numerical RH evidence is supplied by this theorem.
