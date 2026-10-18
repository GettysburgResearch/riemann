# The exact mean mask cost and its sharp order dependence

Status: **PROPOSED deductions from classical ideal counting and the prime
ideal theorem; independent mathematical review required.** No native
cancellation, zero-free boundary, or RH hypothesis is used in this note.

Keep the fixed number field F and fixed finite S of PROOF.md. All indices
are actual ideals, including distinct prime ideals of the same norm.
Write q(p)=Np and, for fixed sigma>0 and real r>0, put

    P_sigma(b) = product_(p|b) (1-q(p)^(-sigma))^(-1),
    C_sigma(r) = product_(p outside S)
                     [1+((1-q(p)^(-sigma))^(-r)-1)/q(p)].    (M1)

PROOF.md §3 proves convergence and the uniform bound
sum_(Nb<=B) P_sigma(b)^r <= C_F B C_sigma(r). This note proves that the
Euler product is the exact limiting mean constant, and identifies its
growth as r tends to infinity. The two limiting variables are kept separate.

## 1. Exact fixed-order mean

Let kappa_F^S be the residue of zeta_F^S at 1. The classical fixed-field
ideal-counting theorem says I_F^S(x)~kappa_F^S x; also I_F^S(x)<=C_F x.
For EVERY FIXED r,sigma>0,

    lim_(B->infinity) B^(-1) sum_(Nb<=B) P_sigma(b)^r
                                    = kappa_F^S C_sigma(r). (M2)

Proof. The nonnegative squarefree function g in PROOF.md §3 has
sum_d g(d)/Nd=C_sigma(r)<infinity. Extend I_F^S(x) as zero for x<1.
The exact divisor expansion gives

    B^(-1) sum_(Nb<=B) P_sigma(b)^r
                = sum_d g(d) I_F^S(B/Nd)/B.

For each fixed d the summand tends to kappa_F^S g(d)/Nd and is bounded
by C_F g(d)/Nd. Dominated convergence for this summable nonnegative
series proves (M2). No error uniform in varying r is asserted. QED.

## 2. Sharp growth of the Euler product

Fix 0<sigma<1. For r>0 let X=X_sigma(r)>1 be the unique real solution of

    X^sigma log X = r.                                    (M3)

As r tends to infinity, the proposed asymptotic is

    log C_sigma(r) ~ [sigma/(1-sigma)] X_sigma(r)
                  ~ [sigma/(1-sigma)]
                                      (sigma r/log r)^(1/sigma). (M4)

The leading coefficient is independent of F and of the finite S. Their
fixed local changes affect the error, and no field-uniform error is claimed.
The classical prime ideal theorem used below is the NATURAL counting
statement pi_F(x)~x/log x, not merely a Dirichlet-density assertion. In
particular it assumes no critical-line conjecture. SOURCES.md gives the
primary reference checked for this classical input.

### 2a. Replace the exact local logarithm on a bounded multiple of X

Put a(q)=-log(1-q^(-sigma)). For q>=2,

    0 <= a(q)-q^(-sigma) <= C_sigma q^(-2sigma).            (M5)

The function l_q(z)=log(1+(exp(z)-1)/q), z>=0, has derivative in [0,1].
Furthermore, for v=z-log q,

    log(1-1/q) <= l_q(z)-max(v,0) <= log 2.               (M6)

Indeed l_q(z)=log(1-1/q+exp(v)). Comparing with max(v,0) proves both
bounds; q>=2 bounds their absolute values by log 2. For any FIXED K>1,
(M5), the Lipschitz property and (M6) imply

    sum_(q(p)<=KX) l_q(r a(q))
      = sum_(q(p)<=KX) max(r q^(-sigma)-log q,0)
        + O_sigma(r sum_(q(p)<=KX) q^(-2sigma)+pi_F(KX)). (M7)

The error is o(X). To check the first part using even ALL ideals and
I_F(x)<=C_F x, partial summation bounds the inner sum by
O(X^(1-2sigma)) if 2sigma<1, O(log X) if 2sigma=1, and O(1) if 2sigma>1.
Since r=X^sigma log X, the resulting errors are respectively
O(X^(1-sigma) log X), O(X^(1/2)(log X)^2), and O(X^sigma log X), each o(X).
The prime ideal theorem gives pi_F(KX)=O(X/log X)=o(X).

The function r q^(-sigma)-log q decreases strictly with q and is zero at
X. Thus the main sum in (M7) is EXACTLY

    r sum_(q(p)<=X) q(p)^(-sigma) - sum_(q(p)<=X) log q(p). (M8)

Primes in S are omitted in these sums. Their finitely many contributions
are O_(F,S,sigma)(r+1)=o(X), so either convention has the same leading term.

### 2b. The entire infinite prime tail is smaller than X

Fix K>1 and choose a fixed delta>0 so that beta=(1+delta)K^(-sigma)<1.
For all sufficiently large r and EVERY q>KX, (M5) gives

    r a(q) <= (1+delta) r q^(-sigma) <= beta log X.

Using log(1+t)<=t and exp(v)-1<=v exp(v) for nonnegative arguments,

    sum_(q(p)>KX) l_q(r a(q))
      <= C_sigma r X^beta sum_(q(p)>KX) q(p)^(-1-sigma)
      <= C_(F,sigma,K) r X^(beta-sigma)
       = O(X^beta log X) = o(X).                         (M9)

The second inequality uses the complete IDEAL tail from I_F(x)<=C_F x.
There is no omitted infinite product, conditional rearrangement, or use
of a finite prime grid as a substitute for this error bound.

### 2c. Evaluate the main term

Partial summation of the classical prime ideal theorem gives, for fixed
0<sigma<1,

    sum_(q(p)<=X) q(p)^(-sigma)
                          ~ X^(1-sigma)/[(1-sigma) log X],
    sum_(q(p)<=X) log q(p) ~ X.                           (M10)

For the first relation, the endpoint contributes X^(1-sigma)/log X and
the partial-summation integral contributes sigma/(1-sigma) times that
quantity. The second follows from the same counting theorem. Insert
r=X^sigma log X in (M8), then use (M7) and (M9). The main difference is
[1/(1-sigma)-1]X, proving the first equivalence in (M4).
Finally log X~(log r)/sigma in (M3), so
X~(sigma r/log r)^(1/sigma). This proves all of (M4). QED.

## 3. A stronger growing-order transfer, with the native premise retained

By (M4), for each FIXED F,S and 0<sigma<1 there is a finite C>0 such that

    log C_sigma(2k)
           <= C [k/log(2+k)]^(1/sigma)       (all integers k>=1). (M11)

It follows from the exact convolution and average-mask bound that,
simultaneously for all integers k>=1 and B,D>=1,

    sum_(Nb<=B) |A_(a b^6)(D)|^(2k)
      <= C_F B [D^sigma E_sigma(a;D)]^(2k)
                       exp(C [k/log(2+k)]^(1/sigma)).     (M12)

This improves the exp(O(k^(1/sigma))) mask cost in PROOF.md §3a by the
displayed logarithmic factor. At sigma=1/2, (M4) states specifically

    log C_(1/2)(2k) ~ k^2/[log(2k)]^2.                   (M13)

Thus an order-independent mask constant is impossible in the complete
fixed-order mean (M2). This does NOT assert a matching lower bound for
the actual signed/complex Gaussian row moments; the mask majorant can
overestimate those rows.

Suppose, as a SEPARATE hypothesis, that the one fixed source satisfies
E_sigma(a;infinity)<infinity. For every sequence of integer orders k(D)
such that

    [k(D)/log(2+k(D))]^(1/sigma) = o(log D),              (M14)

(M12) implies, uniformly for ALL B>=1,

    sum_(Nb<=B) |A_(a b^6)(D)|^(2k(D))
                           <= B D^(2k(D)sigma+o(1)).     (M15)

If the envelope is zero the result is trivial. Otherwise the extra
logarithm of its 2k-th power is O_a(k), which is
O_(sigma)(1+[k/log(2+k)]^(1/sigma)) because sigma<1. All prefactors in
(M12) are therefore exp(o(log D)), proving (M15).

For example, at sigma=1/2 a sufficient order range is
k(D)=o(sqrt(log D) log log D); the critical native envelope needed to
use that example is UNKNOWN. Under field RH the principal row has the
needed envelope at every fixed sigma>1/2, and (M14) then gives the stated
conditional replica transfer at that same sigma. No sigma(D)->1/2 claim,
varying-core envelope, critical cancellation, or theta-to-native projection
is proved. No interchange of the B->infinity limit in (M2) with r->infinity
is used anywhere in this argument.

## 4. Sharp large-mask tails over complete finite ideal families

The same positive mask has a much lighter tail than the ramified correction
observable treated in #982. No assertion about that distinct observable,
or the distribution of the actual Gaussian values, is made here.

For fixed 0<sigma<1 and t>1 put

    Y(t) = (t log t)^(1/(1-sigma)),
    T_sigma(B,t) = #{b: Nb<=B, log P_sigma(b)>=t}.

For every fixed epsilon in (0,1), all sufficiently large t, and EVERY B>=1,

    T_sigma(B,t) <= C_F B exp[-(1-epsilon)Y(t)].          (M16)

There is a fixed B_0>=1 such that, for the same sufficiently large t and
EVERY B>=B_0 exp[(1+epsilon)Y(t)],

    T_sigma(B,t) >= (kappa_F^S/2) B exp[-(1+epsilon)Y(t)]. (M17)

The lower estimate states its necessary family-size range explicitly;
there need not be a large-mask ideal in a shorter complete cap. These
two inequalities give the sharp logarithmic tail scale without assuming
that any limiting distribution has already been constructed.

Proof of the upper bound. Markov's inequality and PROOF.md (7) give,
for EVERY real r>0,

    T_sigma(B,t) <= C_F B exp(log C_sigma(r)-r t).

Choose r=Y(t)^sigma log Y(t), so X_sigma(r)=Y(t) exactly. By (M4),
log C_sigma(r)=[sigma/(1-sigma)+o(1)]Y(t). Also the defining Y gives

    r t = Y(t) log Y(t)/log t
        = [1/(1-sigma)+o(1)]Y(t).

Their difference is -(1+o(1))Y(t), proving (M16) uniformly in B. The
asymptotic variable in this argument is r(t), never B. QED.

For the lower bound, fix a small delta>0 with 1+delta<1+epsilon and let
y=(1+delta)Y(t). Let m_y be the squarefree product of EVERY prime ideal
outside S with norm <=y. The prime ideal theorem and (M5),(M10) give

    log Nm_y ~ y,
    log P_sigma(m_y)
            ~ y^(1-sigma)/[(1-sigma)log y]
             = [(1+delta)^(1-sigma)+o(1)]t > t.          (M18)

Here the sum of q^(-2sigma) errors is lower order than the main sum,
by the same three cases as in §2a. Taking t sufficiently large also gives
Nm_y<=exp[(1+epsilon)Y(t)]. Classical ideal counting supplies a FIXED
B_0 such that I_F^S(x)>=(kappa_F^S/2)x for x>=B_0. If
B>=B_0 exp[(1+epsilon)Y(t)], then B/Nm_y>=B_0. Every ideal b=m_y d
with Nd<=B/Nm_y lies in the required cap and has
P_sigma(b)>=P_sigma(m_y)>exp(t), without any coprimality condition on d.
There are at least (kappa_F^S/2)B/Nm_y such ideals. This proves (M17).
No ideals of equal norm are identified and no shared primes are discarded.
QED.

For example, uniformly over B>=B_0 exp(2Y(t)), (M16)--(M17) imply
log(T_sigma(B,t)/B)=-(1+o(1))Y(t) as t tends to infinity, with sigma fixed.
At sigma=1/2 the rate is exp[-(1+o(1))(t log t)^2]. No assertion at the
shorter cap exp((1+o(1))Y(t)) is implicit in this example. If a fixed
native envelope is supplied, (6) further shows that all
but at most the count in (M16) satisfy

    |A_(a b^6)(D)| <= D^sigma E_sigma(a;D) exp(t).

This last statement is a deterministic consequence for those replicas,
with the unknown native envelope still displayed. It is not a new
zero-free estimate or an unconditional critical native bound.
