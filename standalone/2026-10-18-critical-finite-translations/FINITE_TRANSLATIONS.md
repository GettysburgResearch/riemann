# Finite translations, complete ideal coefficients, and zero transport

Status: PROPOSED complete component proofs, not independently reviewed.
No new zero-free region or RH proof. The quotient and its Jordan-totient
coefficients are classical. This packet supplies a quantitative, growing-order
finite-translation realization of the existing prime detector, not a new
invention of that detector. The critical signed upper bound remains open.

## 1. Exact source and what changes

Fix a number field F, a finite prime-ideal set S, and real c. All ideals below
are nonzero integral ideals outside S; distinct ideals with equal rational norm
remain distinct. Put Z(s)=zeta_F^S(s), with residue kappa>0 at s=1, and

    W_c(y)=y^(-c) exp[-(log y)^2/4]/(2 sqrt(pi)).

For h>=0 define the COMPLETE ideal coefficients

    a_h(I)=sum_(A B=I) mu_F(A) (NB)^(-h).                 (1)

There is no coprimality condition on A,B. These are not the original Mobius
coefficients: they are an explicitly specified deformation/convolution of them.
The formal identities, absolutely convergent on Re s>1, are

    Q_h(s)=sum_I a_h(I)(NI)^(-s)=Z(s+h)/Z(s),
    a_0(I)=1_(I=1),
    a_h(p^j)=-(1-q^(-h))q^(-(j-1)h), j>=1, q=Np.       (2)

Indeed the local series is (1-q^(-s))/(1-q^(-s-h)). Multiplication proves
(2), including the unit coefficient. The exact cocycle is

    Q_(h+k)(s)=Q_h(s)Q_k(s+h),
    a_(h+k)(I)=sum_(A B=I) a_h(A)a_k(B)(NB)^(-h).        (3)

No root-number or primitive-character replacement enters these identities.
They hold with the same exclusions throughout. Over Q, (1) is the classical
Jordan coefficient of order -h. We claim no priority for (1)-(3).

For h>0 let

    S_h(X)=sum_I a_h(I) W_c(NI/X),
    T_h(X)=[W_c(1/X)-S_h(X)]/h,
    L_F(I)=log q if I=p^j, j>=1, and 0 otherwise,
    P_raw(X)=sum_I L_F(I) W_c(NI/X).                    (4)

All these Gaussian sums converge absolutely. For example |a_h(I)|<=1 for
h>=0, by (2). The unit term MUST be removed before division by h.

## 2. An unconditional bound for every non-prime-power coefficient

For every h>0 and I!=1,

    |-a_h(I)/h-L_F(I)| <= h(log NI)^2.                 (5)

For I=p^j, set l=log q and x=hl. Then

    -a_h(I)/h = l [(1-exp(-x))/x] exp(-(j-1)x).

Here 0<=(1-exp(-x))/x<=1, its deficit from 1 is at most x/2, and
1-exp(-(j-1)x)<=(j-1)x. The difference from l is therefore nonnegative
and at most h(j-1/2)l^2<=h(log NI)^2. If I has at least two DISTINCT prime
IDEAL factors p,r, all remaining local factors in (2) have absolute value
at most one, and the two chosen factors give

    |a_h(I)| <= h^2 (log Np)(log Nr)
              <= (h^2/4)(log NI)^2.

L_F(I)=0 in this case. This proves (5). In particular the whole non-prime-power
sector is controlled, including different split ideals over the same rational
prime. This is not a selected norm-diagonal estimate.

Fixed-field ideal counting and the full Gaussian then give

    |T_h(X)-P_raw(X)| <= C_(F,c) h X(1+log X)^2, X>=2. (6)

One may prove the weighted count by dyadic NI/X annuli: ideal counts are O_F(t),
and the Gaussian and every fixed polynomial logarithmic weight have summable
annular majorants. No Gaussian tail is discarded. The constant in (6) is
independent of h>0 and of S, when S is dropped only in the positive majorant.

## 3. The known pole and its exact continuum subtraction

There is r>0, depending only on F,S, such that

    c(t)=-kappa/[t Z(1-t)]

extends holomorphically and nonvanishingly to |t|<=4r, with c(0)=1. This follows
from Z(1-t)=-kappa/t+O(1), not from any new global zero-free theorem. Decrease
r below 1/8. On real 0<=t<=r, c(t) is real and positive and

    |c(t)-1|<=C t,    |c^(j)(t)|<=C j! r^(-j).        (7)

The derivative bound follows by Cauchy on radius-r disks, using the fixed
larger disk. Constants here and below may depend on F,S,c and this local r.

Define the exact, one-sided continuum

    J_t(X)=integral_1^infinity y^(-t) W_c(y/X) dy,
    B_t(X)=T_t(X)-c(t)J_t(X), 0<t<=r,
    P(X)=P_raw(X)-J_0(X).                             (8)

Completing the square gives, with b=1-t-c,

    J_t(X)=1/2 X^(1-t) exp(b^2) erfc[-(log X+2b)/2].  (9)

This is NOT replaced by its large-X leading exponential. For Re s>1,
absolute Fubini gives the exact Mellin identity

 integral_0^infinity B_t(X)X^(-s) dX/X
   =exp((s-c)^2) [(1-Q_t(s))/t - c(t)/(s+t-1)].        (10)

The numerator pole of Q_t at s=1-t has residue kappa/Z(1-t)=-t c(t).
Thus (10)'s rational term cancels precisely that known pole. Omitting it
would falsely count the shifted pole as an off-critical zero signal. The
continuum choice also preserves flatness as X tends to zero.

Since |c(t)y^(-t)-1|<=C t+t log y for y>=1, (6) implies

    |B_t(X)-P(X)|<=C t X(1+log X)^2.                  (11)

CRITICAL_TRANSFER strengthens this to a growing-order stencil with subpower
coefficient mass and a power-decaying error after the critical normalization.

## 4. A finite-translation zero test, including cancelled zeros

For any fixed 0<t<=r, the meromorphic function

    D_t(s)=(1-Q_t(s))/t-c(t)/(s+t-1)                  (12)

is holomorphic throughout Re s>1/2 if and only if zeta_F satisfies RH.
This is an elementary criterion, not a proof of its holomorphy.

Under RH the denominator Z has no zeros in that half-plane. Its pole at one
gives a zero of Q_t, not a singularity. The only numerator pole is the one
subtracted in (12). Conversely, suppose (12) is holomorphic and Z(rho)=0 with
Re rho>1/2. Because Z(1-t)!=0, rho is not the subtracted point. Holomorphy
forces Z(rho+t)=0 of at least the same multiplicity; a numerator pole would
worsen rather than cancel the singularity. Repeat this conclusion at each
successive zero. After finitely many steps its real part is at least one,
where classical Euler-product/nonvanishing theory allows no zero. A step
landing at the pole s=1 is not a zero and cannot cancel a denominator zero.
This is a contradiction. The functional equation reflects the conclusion to
all nontrivial zeros. No rightmost-zero, spacing or simplicity assumption is
used. A particular zero may cancel in a ratio, but a finite rightward chain
cannot cancel them all.

## 5. Relation to the original transverse factor -- not a physical estimate

When S and the local data satisfy #975's hypotheses (in particular its small-prime
exclusions), at edbc27b61208ccc7ee1fa99fa3f4e861f5a03452 the principal arithmetic
factor was proved to satisfy, meromorphically,

 A(s,v;z)=Z(1+v) K(s,1-s+v,z) Delta(s-v) Z(s-v)/Z(s).

Putting v=-t and dividing by the displayed meromorphic normalizers gives
exactly Q_t(s). This explains the source choice (1). The identity is asserted
on its valid overlap and then meromorphically, not as pointwise division by a
nonzero bounded normalizer everywhere. The local nonvanishing near v=0 and
its quantitative bounds are credited to #975; no new all-frequency CT norm
estimate is inferred here.

The old first transverse finite part already equals -Z'/Z after compensation.
The new result is a finite, growing-order approximation with quantified ideal
and continuum remainders, proved in the companion note. We do NOT thereby
construct a bounded full physical CT projection: all test-factor derivatives,
other frequencies and contour tails in that different assertion still need
control. Nor do we prove the fixed-center native all-moment estimate.
