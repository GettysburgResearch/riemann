# A physical-row obstruction to extending prime freezing uniformly

Status: PROPOSED component refutation with a complete proof. It concerns
partially randomized moments, not the full native moment conjecture. It
improves the scope of the earlier arbitrary-phase obstruction; it does not
improve a zero-free exponent. No independent review is claimed.

Dependencies: the definitions and projection of #936 at
`eb8d23decc003d36ded287dc98868308192cc889`, Sections 1 and 5 of its PROOF.md;
the newly proved smooth-sum Theorems 3.1--3.2 in the companion note; and the
classical prime number theorem for split rational primes, stated explicitly
in SOURCES.md. The fixed-field sixth-power replication mechanism is credited
to the preceding moment program, not claimed as new. No theta foundation,
large sieve, subconvexity, GRH, or improved native moment is an input.

## 1. The original coefficients and the actual row box

Work over K=Q(omega), with the same fixed excluded set S and one fixed
nonzero nonnegative W in C_c^infinity((0,infinity)) as the companion note.
Take the trivial finite-order twist; this one allowed twist suffices to
refute a statement purporting to cover the full family. Keep the literal
sextic values chi_p(u), including zero when p divides u, and multiply them
on squarefree ideals as in #936. Set H=D^h for a fixed h>0.

For each good prime p with Np>y, let Z_p be an independent uniform sixth
root. Define

    F_(u,D,y)(Z) = sum_(n squarefree, (n,S)=1)
       mu_K(n) W(Nn/D) chi_n(u) product_(p|n, Np>y) Z_p,
    J_(k,y)(u;D) = E_Z |F_(u,D,y)(Z)|^(2k),
    Q_(k,y)(D,H) = sum_(0<Nu<=H) J_(k,y)(u;D).               (1.1)

Only primes occurring in the finite column support are randomized. This is
exactly the mask-preserving conditional moment from #936 with
B=B_y. All small-prime phases are native; no nonunit zero is resampled.

The uniform extension under investigation would say, for some fixed A>2,

    Q_(k,y)(D,D^h) <<_(k,h,W,S,epsilon,A) D^h D^(k+epsilon)
            for EVERY 2<=y<=(log D)^A, and every epsilon>0.  (1.2: TESTED)

The constant cannot depend on the moving cutoff y. A fixed, predetermined
curve y=(log D)^A is a weaker premise and is not refuted by the theorem
below. Nor does the theorem assert failure at every scale D.

## 2. An exact native mean on many physical sixth-power rows

Write M_y(D)=sum_(d|P_y) mu_K(d) W(Nd/D), as in the companion note.
For every element b with (b,P_y)=1, u=b^6 satisfies

    E_Z F_(b^6,D,y)(Z) = M_y(D),
    J_(k,y)(b^6;D) >= |M_y(D)|^(2k).                         (2.1)

Indeed, every smooth column has chi_n(b^6)=1. Every column containing a
rough prime has zero expectation: either its original character value is
already zero or the corresponding independent Z_p has mean zero. No
coprimality between b and the rough part is needed. Jensen's inequality
for the convex function |z|^(2k) then proves the second assertion.

### Lemma 2.2 (copies inside the actual box)

For fixed h>0 and A>1, uniformly in y<=(log D)^A, for all sufficiently
large D,

    Q_(k,y)(D,D^h)
       >= c_(h,S) D^(h/6)/log D * |M_y(D)|^(2k).             (2.2)

Proof. Let T=D^(h/6). Use split rational primes p in [T/2,T], avoiding S.
There are at least c T/log T of them, by the classical PNT in 1 modulo 3.
For each choose one prime ideal of norm p and its fixed generator b. For
large D, p>y uniformly in the allowed range, so (b,P_y)=1. The elements
b^6 have norms p^6<=D^h and are distinct: equality of two elements would
imply equality of their sixth-power principal ideals, hence of the chosen
prime ideals. They are an actual subset of the physical rows, not rows
realized by a CRT construction of uncontrolled height. Summing (2.1) over
this subset proves (2.2). The logarithm absorbs the fixed factor h/6. QED.

For u=1 alone, (2.1) is valid with no prime-distribution input. The stronger
D^(h/6) factor in (2.2) uses the standard replica mechanism and PNT.

## 3. The fixed-order barrier with its exact exponent

Set

    beta_(k,h) = 1/2 + 5h/(12k).

### Theorem 3.1 (native-coefficient partial-moment obstruction)

Let k>=1 be fixed, 0<h<6k/5, and

    A > 1/(1-beta_(k,h)) = 12k/(6k-5h).                     (3.1)

For every fixed alpha with beta_(k,h)<alpha<1-1/A, there are unbounded
pairs (D,y), with 2<=y<=(log D)^A, for which

    Q_(k,y)(D,D^h)
       >= c D^h D^(k+delta)/log D,
    delta = 2k(alpha-beta_(k,h)) > 0.                        (3.2)

The same W and true mu_K coefficients occur in every witness. The cutoff
is the complete initial segment B_y, not a specially selected prime band.
Consequently (1.2) is false for any epsilon<delta.

Proof. Apply companion Theorem 3.1 with this A and alpha. It supplies, for
every sufficiently large y, a D>=exp(y^(1/A)) with |M_y(D)|>D^alpha.
Apply Lemma 2.2. Its exponent is

    h/6 + 2k alpha = h + k + 2k(alpha-beta_(k,h)),

which is (3.2). Since D tends to infinity and delta>epsilon, the ratio
D^(delta-epsilon)/log D is unbounded. This contradicts any constant in
(1.2). No premise about the full native moment has been used. QED.

The witnesses can also be localized as in companion Theorem 3.2. That
localization does not convert the varying-cutoff theorem into a theorem
on the single exact curve y=(log D)^A.

### Corollary 3.2 (sharpness already at the fixed row u=1)

For every fixed k>=1 and A>2,

    limsup_(D->infinity)
      log(1 + sup_(2<=y<=(log D)^A) J_(k,y)(1;D)) / log D
       = 2k(1-1/A).                                         (3.4)

The lower bound follows from (2.1) and companion Corollary 3.3. For the
upper bound use #936's absolute Rankin estimate with X=max(3,bD), choosing
any sigma>1-1/A. Its small-prime product is D^o(1), and 2sigma>1 makes the
remaining Euler majorant a fixed constant at this k and sigma. Let sigma
decrease to 1-1/A. The fixed support multiplier b changes no exponent.
Thus the previous uniform-phase upper exponent is sharp even for the
unchanged native coefficients, the same fixed smooth test, and the bounded
physical row u=1. This is still a statement about J, not about |A_1|^(2k).

### Concrete fourth-order instance

Take k=2, h=21/20, and A=4. Then

    beta_(2,21/20) = 23/32,
    alpha = 47/64 < 3/4 = 1-1/A,
    delta = 1/16.

There are unbounded native-coefficient witnesses with H=D^(21/20) and
y<=(log D)^4 such that

    Q_(2,y)(D,H) >= c H D^(2+1/16)/log D.                    (3.3)

For example sigma=95/128 is permitted in the Mellin proof: alpha<sigma<3/4
and 1-sigma=33/128>1/4. The displayed fractions are bookkeeping for a proved
asymptotic implication; finite tests of them are not the proof of (3.3).
More generally every delta<1/8 is achievable here by choosing alpha closer
to 3/4. The endpoint delta=1/8 is not asserted.

At h=1 the critical A values from (3.1) are 24/7 for k=2, 36/13 for k=3,
48/19 for k=4, and 96/43 for k=8; they decrease to 2.

## 4. The log-power-two boundary is sharp for a cofinal hierarchy

Suppose one seeks, at an unbounded collection of fixed orders k,

    Q_(k,y)(D,D^(h_k))
       << D^(h_k) D^(k+e_k+epsilon)
       for every 2<=y<=(log D)^A,                           (4.1)

with fixed A>2, h_k>0, h_k=o(k), and e_k>=0, e_k=o(k). Each k is fixed
before D tends to infinity; this is not a growing-k uniformity claim.

### Corollary 4.1

The cofinal collection of assertions (4.1) is impossible.

Proof. Choose a fixed alpha with 1/2<alpha<1-1/A. For sufficiently large
orders,

    alpha > 1/2 + 5h_k/(12k) + e_k/(2k).

The same proof as Theorem 3.1 gives an exponent strictly larger than
h_k+k+e_k. Choose epsilon smaller than that positive difference and let
D run through the witnesses. This contradicts (4.1) at that fixed order.
QED.

Combined with #936's upper theorem at A=2 (indeed at 2+o(1)), this identifies
the sharp LOGARITHMIC POWER boundary for this uniform-cutoff cofinal
partially randomized hierarchy, now with native coefficients and actual
short rows. It does not claim sharp log-log refinements, fixed-curve
sharpness, or a sharp threshold at every fixed small k.

## 5. What a successful native argument would have to cancel

The actual moment is

    M_(2k)(D,H)=sum_(0<Nu<=H)|F_(u,D,y)(1)|^(2k),

which is independent of y. In the notation of #936 it satisfies exactly

    M_(2k)(D,H)=Q_(k,y)(D,H)+R_(k,y)(D,H),                   (5.1)

where R is the real signed interference between unequal rough charge
blocks. Equation (5.1) is inherited and not presented as new cancellation.

If the desired native upper bound holds at an exponent loss epsilon<delta
along witnesses from (3.2), then necessarily

    R_(k,y)/Q_(k,y) = -1 + O(D^(epsilon-delta) log D).        (5.2)

Proof: divide (5.1) by the lower bound for Q and use the assumed native
upper bound and M_(2k)>=0. Thus (5.2) is a conditional necessity, not an
unconditional estimate on R.

The reference can be much larger than the conjectured answer even when all
coefficients are genuinely Mobius. A successful continuation therefore
cannot require every intermediate prime-freezing stage to have diagonal
size. It must preserve compensating signed interference. This rules out a
particular continuation strategy; it does not rule out the native target.

Subtracting just the smooth mean is not automatically enough. The same
smooth-Mobius profiles occur as coefficients of nonzero rough monomials at
shorter scales. No theorem controlling all their physical recouplings is
proved here. The open one-sided upper estimate for R at the safe log-square
cutoff in #936 remains the smallest RH-bearing arithmetic gap of this path.

## 6. Physical-scale localization, not an off-diagonal bound

There is also a physical-scale localization statement in the proof,
which must not be confused with cancellation of the rough interference. For a fixed y, the Mellin mass from scales
D<exp(y^(1/A)) is exponentially too small to account for E_y at t_y. In
companion Theorem 3.2 the far tail D>exp(y^(1/A+eta)) is also negligible.
The large smooth component is therefore forced into the intervening
PHYSICAL norm window. It is not an unfiltered Euler artifact that can be
removed merely by reapplying the original column support. This is why the
norm-filtered obstruction differs from the earlier CT1 objection.

This window localization is not an estimate for the physical rough-prime
interference. No full fourth/sixth moment, 17/24 boundary, shrinking zeta
band, or RH conclusion is promoted.
