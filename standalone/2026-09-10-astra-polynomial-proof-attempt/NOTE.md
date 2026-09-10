# Direct attempt at Q-AC28: exact inverse coordinates and the critical boundary

**Status: PROPOSED elementary identities and a refutation of an auxiliary
proof step. Q-AC28 is NOT proved. No RH proof, stronger zero-free region,
or degree-uniform upper bound is claimed.**

This is a direct attempt at the polynomial inequality in PR845, frozen at
`b9ccd03a681a73e91fb7bbfb7a3b97766fe8285e`,
`standalone/2026-09-10-astra-safe-source-kernel/PROOF.md`, Section 7.
The earlier manuscript and its status are unchanged. This note is not an
independent review of that manuscript, and not a proposed complete RH proof.

## 1. The exact target

Write Z(s)=(1-2^{-s}) zeta(s). For a complex odd polynomial p put

    Q_p(t) = sum_(n>=1, odd) p(t/n)/n,
    E_p(t) = Q_p(1) - sum_(n>=3, odd) p(t/n)/n.

The requested assertion is that for every eta>0 some FINITE C_eta works for
EVERY odd polynomial, independently of its degree and coefficients:

    integral_1^3 |E_p(t)|^2 dt
      <= eta integral_0^1 |p(t)|^2 dt
          + 4 C_eta integral_0^1 t^2 |Q_p'(t)|^2 dt.       (Q)

The parent supplies a proposed all-order analytic implication (Q) => RH.
This note does not replace a proof of (Q) by that implication. Fixed-degree
constants, numerical trends, and an unweighted derivative bound do not prove
(Q). The additional term eta ||p||^2 must be retained throughout.

## 2. An exact change of polynomial coordinates

On odd polynomials Q is invertible. If q=Q_p, then

    p(t) = sum_(n>=1, odd) mu(n) q(t/n)/n.                 (1)

For a monomial t^r, r>=1 odd, Q acts by Z(r+1)>0. Its inverse therefore acts
by 1/Z(r+1). The series in (1) acts by the same factor, using the absolutely
convergent Dirichlet inverse for r+1>=2. Finite linear combinations prove the
identity. Alternatively, expanding Q of the right side uses
sum_(d|k) mu(d)=1_(k=1). The double series is absolutely convergent because
q(t/n)=O_t(1/n).

The compensated output has the EXACT inverse expression

    E_p(t) = q(1) + sum_(n>=3, odd) mu(n) q(t/n)/n,
                                                    1<=t<=3. (2)

Indeed E_p=Q_p(1)-Q_p(t)+p(t), and the n=1 term in (1) cancels q(t).
This identity retains all terms. In particular, positivity of the original
Q dilation weights does not turn the output into a positive inverse operator.
No new result about the magnitude of the signed sum follows from (2) alone.

## 3. A native odd-polynomial family at the degenerating boundary

For every integer N>=0 define

    q_N(t)=integral_0^t (1-u^2)^N du
          =sum_(j=0)^N (-1)^j binom(N,j)t^(2j+1)/(2j+1),

    p_N(t)=sum_(j=0)^N
          (-1)^j binom(N,j)t^(2j+1)/[(2j+1)Z(2j+2)].       (3)

These are genuine odd polynomials for the UNCHANGED native Q, and Q_(p_N)=q_N.
They are not finite-Euler controls or unspecified infinite functions.
Let

    a_N=integral_0^1 (1-t^2)^N dt
       =2^(2N)(N!)^2/(2N+1)!.

Then, with unweighted L2 norms on (0,1),

    ||q_N'||^2 = a_(2N),
    ||t q_N'||^2 = a_(2N)/(4N+3).                       (4)

The identity follows by integrating the derivative of
 t(1-t^2)^(2N+1) over [0,1]: its boundary values vanish and

    0 = a_(2N) - (4N+3) integral_0^1 t^2(1-t^2)^(2N)dt.

Thus even on the exact native polynomial domain

    ||Q_(p_N)'||^2 / ||t Q_(p_N)'||^2 = 4N+3.            (5)

No fixed constant can replace the unweighted derivative by the weighted one.

## 4. Adding a fixed multiple of the p norm does not repair that step

Let m(x)=sum_(n<=x, odd) mu(n)/n, zero below 1. The elementary bound
|m(x)|<=2 suffices here; no PNT, RH or zero information is used.

For completeness, for an integer K>=1,

    1=sum_(d<=K) mu(d) floor(K/d)

implies |sum_(d<=K)mu(d)/d|<=1, since the d=1 fractional part is zero and
each other fractional part is less than one. For real cutoffs the sum is
constant between integers. Splitting even indices gives

    m(x)=sum_(j>=0) 2^(-j) sum_(n<=x/2^j)mu(n)/n,

where only finitely many terms are nonzero. This proves the odd bound 2.

Using (1), finite integration followed by an absolutely justified interchange
gives, for 0<t<=1,

    p_N(t)=integral_0^t (1-u^2)^N m(t/u)du.              (6)

The majorant before interchange is
sum_n |mu(n)| q_N(t/n)/n <= t sum_n n^(-2)<infinity.
Consequently

    |p_N(t)| <= 2 q_N(t) <= 2 a_N,
    ||p_N||^2 <= 4 a_N^2 <= 4/(N+1).                    (7)

The elementary inequalities

    1/sqrt(2N+1) <= a_N <= 1/sqrt(N+1)                   (8)

follow by induction from a_0=1 and
 a_(N+1)/a_N=(2N+2)/(2N+3).
Squaring reduces their induction steps respectively to
4(N+1)^2 >= (2N+1)(2N+3) and
4(N+1)(N+2) <= (2N+3)^2.

Normalize by setting p_hat_N=p_N/sqrt(a_(2N)). Equations (4), (7), and (8)
prove

    ||Q_(p_hat_N)'||^2 = 1,
    ||t Q_(p_hat_N)'||^2 = 1/(4N+3) -> 0,
    ||p_hat_N||^2 <= 4 sqrt(4N+1)/(N+1) -> 0.           (9)

Therefore the following AUXILIARY assertion is false for EVERY pair of fixed
finite nonnegative constants A,B:

    ||Q_p'||^2 <= A||p||^2+B||t Q_p'||^2
                            for all odd polynomials p. (FALSE)

This rules out a proof which tries to turn the parent's unweighted derivative
estimate into the required weighted estimate, EVEN if it adds a bounded
multiple of the original input norm. It is not a refutation of (Q), whose
left side is ||E_p||^2, not ||Q_p'||^2.

## 5. The same family exposes the actual endpoint cancellation

For 1<=t<=3, (2) yields exactly

    E_(p_N)(t)
       =integral_0^(t/3) (1-u^2)^N m(t/u)du
          +integral_(t/3)^1 (1-u^2)^N du.                (10)

To verify this, integrate the sum over n>=3 in (2). Its summatory factor is
m(t/u)-1 on 0<u<=t/3. The subtracted 1 cancels the corresponding part of
q_N(1)=a_N. The remaining integral is the second term in (10).
All arguments of (1-u^2)^N are in [0,1]; the same absolute majorant justifies
the interchange. Both endpoints t=1,3 are included.

The second term satisfies

    0 <= integral_(t/3)^1 (1-u^2)^N du <= (8/9)^N.       (11)

The first term still contains the literal signed harmonic Mobius sum.
The bound |m|<=2 gives only

    |E_(p_N)(t)|<=2 a_N,
    ||E_(p_N)||_(1,3)^2 <=8 a_N^2 <=8/(N+1).            (12)

In particular ||E_(p_hat_N)||^2 tends to zero, so the sequence (9) is NOT a
counterexample to the original target. Estimate (12) does not prove (Q) on
this family: its bound has scale N^(-1), whereas the weighted forcing in
(4) has scale N^(-3/2); the eta||p_N||^2 term cannot simply be removed or
assumed to dominate the signed output. No comparison of the required form
with degree-independent C_eta was obtained.

Bounding q_N(1) separately is also too crude. Its exact cost obeys

    |q_N(1)|^2 / ||t q_N'||^2
      =(4N+3)a_N^2/a_(2N)
      >=(4N+3)/sqrt(2N+1) -> infinity.                  (13)

Thus the cancellation in (10), rather than separate endpoint and tail bounds,
is indispensable to any proposed completion based on these coordinates.

## 6. Relation to a classical arithmetic sequence, not a novelty claim

Termwise differentiation of (1) is absolutely valid on compact t sets for a
fixed N and gives

    p_N'(t)=sum_(n>=1, odd) mu(n)n^(-2)(1-t^2/n^2)^N.   (14)

At t=1 this is

    sum_(j=0)^N (-1)^j binom(N,j)/Z(2j+2).              (15)

It is the odd-integer version of the reciprocal-even-zeta binomial sums in
Luis Baez-Duarte, *A sequential Riesz-like criterion for the Riemann hypothesis*,
International Journal of Mathematics and Mathematical Sciences (2005),
3527-3537, DOI 10.1155/IJMMS.2005.3527.

For the all-integer version b_N(t), and its odd version b_N^o(t), the exact
relation is

    b_N(t)=b_N^o(t)-(1/4)b_N^o(t/2).

It follows directly from mu(2n)=-mu(n) for n odd and mu(4n)=0. The cited paper
proves an RH criterion for its all-integer sequence. That published theorem
is cited as comparison, not silently asserted for a new normalization or
used as a proof of (Q). Its publisher abstract/metadata were consulted; no
external proof or numerical dataset was independently replayed here.

## 7. Result of this attempt

A proof of (Q) has NOT been found. The exact direct transformation, the
normalized native boundary family, and the failure of the auxiliary graph
estimate are the completed calculations. They identify a concrete invalid
way to finish the previous argument; they do not supply a new global bound
on the compensated output or on the Mobius source energy.

In particular, an argument that replaces ||tQ_p'|| by ||Q_p'|| has a provable
unbounded loss, even after a fixed input-norm correction. An argument that
bounds the endpoint and tail separately also loses the required uniformity.
The remaining assertion is still (Q) with its exact all-degree quantifiers.
It has not been delegated to an unnamed compactness lemma, to a numerical
matrix census, or to an independent reviewer.
