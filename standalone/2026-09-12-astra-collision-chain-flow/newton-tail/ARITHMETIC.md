# A sharp energy price for changing the completion

2026-09-12. **Proposed component proof; independent mathematical review
required. The actual native covariance bound and RH are not proved.**

This works with the original all-integer Möbius source and Dirichlet
convolution. It is not a new positivity theorem obtained by dropping the
completion cost. The strongest new statement here is a sharp optimization
identity: exactly how much full source energy is needed to reduce the
quadratic output on the native annulus.

## 1. Preserve the source, allow the completion to vary

For a fixed integer Y>=1 write

    m(k)=sum_(n<=k)mu(n)/n, F_Y=sum_(k=1)^Y m(k)^2,
    b=Y+1, B=b^2-1, A_Y=F_B-F_Y.                         (1)

Let c be ANY finitely supported real sequence such that

    c_n=mu(n) for every n<=Y,       sum_n c_n/n=0.          (2)

In this note A_Y denotes annular reciprocal energy, not the different
balanced-state variable bearing the same letter in BNR26. Write

    t(k)=sum_(n<=k)c_n/n,
    J(c)=int_1^infinity (sum_(n<=x)c_n)^2 dx/x^2,
    delta(c)=J(c)-F_Y.                                   (3)

Expanding the finite kernel gives

    J(c)=sum_(r,s)c_r c_s/max(r,s)=sum_(k>=0)t(k)^2.       (4)

For the last equality use the zero reciprocal moment in (2) and
1/max(r,s)=min(r,s)/(rs). There is no omission of the physical infinite tail:
if the total ordinary mass is nonzero, its constant cumulative future is
included in the left-hand integral. The reciprocal coordinates nevertheless
vanish beyond the finite support because (2) holds. Hence delta(c)>=0 and

    sum_(k=b)^B t(k)^2 <=delta(c).                        (5)

Put z=c*c, where * is Dirichlet convolution, and define the SAME full
coalesced packets as in XCC26/CJB26:

    K_d(k)=[H_floor(k/d)-H_k+log d]/d,
    Q_c(k)=sum_d z(d)K_d(k),
    S_Y(c)=sum_(k=b)^B Q_c(k)^2=D_Y(c)+C_Y(c).            (6)

C has ordered distinct-product pairs. Both terms in (6) depend on the chosen
completion. One cannot compare a new C with the old diagonal from another c.

## 2. The exact source identity, not a model approximation

Let 1(n)=1 and let delta_1 be the unit for Dirichlet convolution. For
v=2c-1*c*c and e=delta_1-1*c, the classical Newton identity is

    mu-v=mu*e*e.                                        (7)

Since e vanishes below b, (7) makes v(n)=mu(n) for ALL n<=B. It need not hold
at b^2. No values of c after Y can change this reconstructed prefix.

The identities sum z(d)/d=0 and sum z(d)log(d)/d=0 follow from P_c(1)^2
and its derivative. Thus the logarithms and the separated harmonic term
in (6) cancel exactly, giving

    Q_c(k)=sum_d [z(d)/d]H_floor(k/d)=2t(k)-m(k), b<=k<=B. (8)

All sums over d are finite and all terms with d>k are handled by the same
moment cancellation, not silently removed from K_d.

## 3. NJT-A1: completion invariance with its complete cost

The two vectors in (8), over the entire integer annulus, satisfy

    |sqrt(S_Y(c))-sqrt(A_Y)| <=2sqrt(delta(c)).            (9)

Consequently

    (sqrt(A_Y)-2sqrt(delta(c)))_+^2 <= S_Y(c)
        <=(sqrt(A_Y)+2sqrt(delta(c)))^2,                  (10)

and

    |D_Y(c)+C_Y(c)-A_Y|
        <=4sqrt(A_Y delta(c))+4delta(c).                 (11)

**Proof.** On that annulus ||m||_2=sqrt(A_Y), ||t||_2<=sqrt(delta(c)) by
(5), and Q_c=-m+2t by (8). The reverse triangle inequality proves (9);
(10) follows. Expanding ||-m+2t||_2^2 and applying Cauchy--Schwarz gives
(11). All future source cost used in delta(c) has been retained. QED.

This result does not require Y to be a sign crossing, any coefficient cap,
or Liouville-coherent signs. Those additional native conditions are useful
for bounding D, not for the identities (7)--(11).

## 4. NJT-A2: the lower tradeoff is exactly attained

The lower bound in (10) is not just a rough safety estimate. For 0<=u<=1/2
make the following finite completion:

    c_n=mu(n), n<=Y,
    c_b=u mu(b)+(u-1)b m(Y),
    c_n=u mu(n), b<n<=B,
    c_(B+1)=-u(B+1)m(B),
    c_n=0 otherwise.                                    (12)

Exactly,

    t(k)=m(k), 1<=k<=Y;
    t(k)=u m(k), b<=k<=B;
    t(k)=0, k>=B+1.

Thus (2) holds and

    delta(c)=u^2 A_Y,
    S_Y(c)=(1-2u)^2 A_Y.                                (13)

This saturates the lower norm tradeoff. At u=1/2 the ENTIRE quadratic
annular output Q_c vanishes, but its full additional source energy is
exactly A_Y/4. Conversely Q_c=0 in (8) forces t=m/2 on the entire annulus,
so (5) forces delta(c)>=A_Y/4. Therefore

    inf {delta(c): c satisfies (2), Q_c|_[b,B]=0}=A_Y/4.  (14)

More generally for any budget d>=0,

    inf_{c satisfies (2), delta(c)<=d} S_Y(c)
        =(sqrt(A_Y)-2sqrt(d))_+^2.                      (15)

For d<=A_Y/4 choose u=sqrt(d/A_Y), and for d>=A_Y/4 choose u=1/2.
The case A_Y=0 is immediate, using u=0. Negative u similarly saturates the
upper bound at the corresponding delta; this is only an algebraic check,
not a positive-coefficient claim.

**Essential limitation.** Formula (12) uses mu through B, not just through Y.
It is an extended-prefix ("oracle") completion, exhibited to prove sharpness
and to test energy accounting. The extended coefficients are of course
computable, for example by the existing Newton reconstruction; the obstacle
is NOT access to those numbers. Their annular energy is the very quantity
whose upper bound is missing. Formula (12) is not that upper estimate, not
the bounded native crossing collar, and not a claim that these new coefficients
retain a cap or multiplicative sign coherence.

## 5. Why a free completion optimization cannot close the arithmetic route

For the native crossing source in #848, the single late coefficient at 2Y
costs delta=(Y-1)m(Y)^2<=1/Y. CJB26 already gives the still sharper identity

    A_Y=D_Y+C_Y+4m(Y)P_Y, |4m(Y)P_Y|<2,
    P_Y=sum_(n=Y+1)^(2Y-1)(2Y-n)mu(n)/n.                 (16)

This manuscript does not replace that bound by the weaker (11). Its new
purpose is to quantify the situation for ARBITRARY competing completions.

For example, suppose along a sequence of cutoffs some collection of admissible
completions has delta(c)<=d_Y and D_Y(c)<=L_Y, where

    d_Y=o(A_Y),       L_Y=o(A_Y).

Then (11), uniformly over this entire collection, gives

    C_Y(c)/A_Y ->1.                                     (17)

Thus a large actual annular energy cannot be removed by changing to any cheap
completion whose diagonal is small. Under the explicitly inherited XCC26
common-exponent theorem, a hypothetical off-line zero makes
A_Y=Y^(2kappa+o(1)), kappa=2Theta-1>0. Any subpower d_Y,L_Y meet these smallness
conditions, so (17) applies to every such admissible completion.

Conversely, making C negative through the oracle construction (12) pays a
fraction of the very annular energy that needed an upper bound. Dropping
that payment would manufacture an apparent proof. Equations (14)--(15)
identify the exact price rather than leaving the problem as a vague warning.

The native C_Y<=K D_Y on unbounded crossings, or another genuine native
subpower/subquadratic gain, remains OPEN. The joint Newton-tail route in
PROOF.md offers an alternative analytic ending; it does not supply this
arithmetic estimate by analogy.

## 6. Finite verification scope

check.py constructs actual finite Möbius arrays by trial factorization and
checks the Newton output by a separate divisor-convolution loop. It verifies
the sharp family (12), full physical kernel energy (4), the reciprocal norm,
and the annular output for specified bounded Y and rational u. Additional
zero-reciprocal perturbations test (9)--(11) away from equality. All work uses
integers and fractions. These tests do not prove an unbounded cancellation,
count as a second author's review, or certify the XCC26 analytic exponent.
