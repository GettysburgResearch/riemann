# Fixed-source prime deletion removes the replica error floor

Status: proposed conditional analytic adapter; independent review requested.
Scope: precisely the ideal Mobius/sextic family and fixed-height OPEN-RMS
contract in [REPLICA_TRADEOFF.md](REPLICA_TRADEOFF.md). The moment remains
unproved, and RH remains open. No growing conductor or profile is introduced.
What ran: exact rational recurrence and finite squarefree divisor controls
in `check_prime_deletion_bootstrap.py`.
Smallest remaining gap: the same source-faithful below-diagonal moment.

## 1. Exact deletion uses the same character and smoothing profile

Keep nu,W,S fixed. For a prime ideal p outside S let P=Np and write
B_p(D) for A_1(D) restricted to columns coprime to p. The exact squarefree
Euler decomposition, including every norm scale, is

    A_1(D)=B_p(D)-nu(p) B_p(D/P).

The compact support of W makes the following iterated identity finite:

    B_p(D)=sum_(j>=0) nu(p)^j A_1(D/P^j),
    A_1(D)-A_(p^6)(D)=-sum_(j>=1)nu(p)^j A_1(D/P^j).             (B1)

Indeed A_(p^6)=B_p by the actual sextic identity. Iteration stops because
there are no nonzero integral ideals in the sufficiently small norm support.
Neither the character nor W changes as p varies. In particular a hypothesis
for one fixed excluded set S is enough; it need not be strengthened to a
uniform bound over the additional prime p.

If for every epsilon>0 and this fixed nu,W one has

    A_1(X)<<_{nu,W,epsilon} X^(theta_0+epsilon), theta_0>0,        (B2)

for X>=2, extend the bound to all X>0 by compact support and a larger
constant. The exact vanishing below a positive X makes this legitimate.
Since |nu(p)|=1 and P>=2, the geometric sum in B1 gives, uniformly in p,

    |A_1(D)-A_(p^6)(D)|
       << (D/P)^(theta_0+epsilon)/(1-P^(-theta_0-epsilon))
       << (D/P)^(theta_0+epsilon).                              (B3)

This is stronger than the trivial O(D/P) count whenever theta_0<1.
All constants retain the original fixed data; no ideal/element multiplicity
or source coefficient has been swapped.

## 2. A fixed-height moment can be reused at every bootstrap step

Assume OPEN-RMS(kappa,h) for one fixed 0<=kappa<=1/2 and 0<h<1.
Set

    A=(1+kappa+h*(5/6-kappa))/2,  c=1-h/6,  0<c<1.               (B4)

Apply B3 to the same prime-sixth family, with Y=D^(h/6) and P in (Y/2,Y].
The moment branch of the replica extraction is unchanged. Its error branch
now has exponent c*theta_0. Thus B2 implies

    A_1(D)<<D^(max(A,c*theta_0)+epsilon)                         (B5)

for every epsilon>0. Distribute the input exponent loss, moment loss and
prime logarithm loss below the requested final epsilon. The height remains
H=D^h and the moment is always used in its originally assumed range.

The elementary ideal count gives the starting exponent theta_0=1.
Repeated B5 therefore gives

    theta_j=max(A,c^j).                                        (B6)

Because c<1 and A>0, some finite j satisfies c^j<=A. For each requested
epsilon choose the losses at the finitely many steps sufficiently small.
Consequently the single fixed-height moment implies

    A_1(D)<<D^(A+epsilon) for every epsilon>0,
    L_K(s,nu) is zero-free for Re(s)>A.                          (B7)

The smooth Mellin proof is R6 in the preceding packet. It retains all finite
zero heights and multiplicities, with no height-uniform moment assumption.

For example kappa=2/5, h=1/2 gives A=97/120=0.8083333..., c=11/12;
three bootstrap steps suffice since (11/12)^3<97/120. This is an exact
conditional deduction from that fixed-height moment, not a proof of it.
The preceding target kappa=2/5,h=18/23 still gives A=20/23; at that height
the first moment branch was already the limiting cost.

## 3. Quantifiers determine the critical implication

For one fixed h, B7 proves only its displayed fixed bound. If RMS were
proved for every fixed arbitrarily small positive h, with one fixed kappa,
then choosing h below each requested exponent loss would give the strict
half-plane Re(s)>(1+kappa)/2. Constants may depend on h; no exchange of an
infinite uniform limit is needed. In particular kappa=0 for all such h
would imply RH (and the stated finite-order quasi-RH class) by symmetry.
Already the u=1 term of this all-height moment contract has that limiting
implication, so the contract must not be portrayed as a routine source
extension.

The 6/7 floor in R5 is the floor of the **one-step extraction with a trivial
prime-deletion error**. B1--B7 show why that specific floor does not apply
to a repeated fixed-source bootstrap. The new unpaid moment is still the
essential obstacle; scalar optimization and source deletion cannot prove it.
