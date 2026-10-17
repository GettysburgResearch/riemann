# A prime-power memory equation for the literal critical source

Status: PROPOSED component mathematics with a complete elementary proof.
Scope: each fixed number field and finite excluded-prime set; the unchanged
ideal Möbius source, all real logarithmic scales, and a fixed ordinary twist.
Dependencies: ideal factorization, the absolutely convergent Euler product,
Gaussian integration, and ordinary ideal counting. No quasi-RH theorem,
unknown covariance estimate, or external new theorem is used in this component.
The equation is a direct logarithmic-derivative identity; no priority claim
is made for that classical operation. Its use here is to replace the
all-pairs energy expansion by an explicitly truncatable prime-memory problem.

## 1. Source and normalization

Fix a number field F of degree d, a finite set S of prime ideals, and a real
number t0. All ideals below are integral, nonzero, and supported outside S.
Write q_a=N a, mu=mu_F, and define the ideal von Mangoldt function by
Lambda_F(p^k)=log(N p) for k>=1 and zero on other ideals. Put

    g(u)=exp(-u^2/4)/(2 sqrt(pi)),
    G(u)=sum_a mu(a) q_a^(-1/2-i t0) g(u-log q_a).             (1.1)

This is the actual Gaussian-smoothed principal source, with an optional
fixed norm twist. There is no randomization, averaging over t0, ideal
identification by equal norm, or alteration of a nonunit mask. The center
t0 stays fixed in every asymptotic statement.

All derivatives converge locally uniformly. Indeed the Gaussian in log q
dominates every fixed power, and ordinary ideal counting is sufficient.
For u<=0 there is the explicit absolute bound

    |G(u)| <= C_F exp(-u^2/4),
    C_F = exp(9/4) zeta_F^S(2)/(2 sqrt(pi)).                  (1.2)

To prove it, factor out exp(-u^2/4), use exp(u log q/2)<=1, and use

    q^(-1/2) exp(-(log q)^2/4) <= exp(9/4) q^(-2).

Analogous bounds with a polynomial factor hold for derivatives. For every
complex r with Re r>1/2, bilateral Laplace integration gives

    integral_R G(u) exp(-r u) du
       = exp(r^2)/zeta_F^S(1/2+i t0+r).                      (1.3)

Absolute convergence at this initial line justifies the exchange. Equation
(1.3) is not an unweighted Fourier representation on Re r=0.

## 2. Exact memory equation

**Theorem 1.** For every real u,

    2 G'(u)+u G(u)
      +sum_b Lambda_F(b) q_b^(-1/2-i t0) G(u-log q_b)=0.     (2.1)

The prime-power series and its derivatives converge locally uniformly.

Proof. The identity 2g'(u-log q)+u g(u-log q)=log q g(u-log q)
reduces the first two terms to the source with coefficient mu(a) log q_a.
Unique factorization gives the exact ideal convolution

    (Lambda_F * mu_F)(a)=-mu_F(a) log q_a.                   (2.2)

At a squarefree ideal, the single surviving contribution for each prime
is minus mu(a) log q_p. At an ideal with one repeated prime, the two possible
prime powers have opposite Möbius values; if other repeats remain, every
term is zero. Equivalently (2.2) is the logarithmic derivative of the Euler
product in its region of absolute convergence. The twist is completely
multiplicative, so it respects this convolution. Substitution proves (2.1).
Gaussian decay and ideal counting justify regrouping on each compact u set.

This equation retains every composite Möbius cofactor inside the delayed
copy of G. The outer memory measure is supported only on prime powers.

## 3. A rigorous uniform truncation rule

**Theorem 2.** Let U>=0, R>=2, and P=ceil(exp(U+R)). Omitting all ideal prime
powers b with q_b>P in (2.1) gives, uniformly for every real u<=U, error at
most

    T_F(U,R)=2 d C_F exp(U/2+1/4)
       *[1+(U+1)/(R-1)] exp(-(R-1)^2/4).                    (3.1)

This is an analytic bound for the complete omitted tail, not a finite scan.

Proof. Since u-log q_b<=-R, use (1.2). For a rational prime p and an exponent
k, the sum of Lambda_F(b) over ideals of norm p^k is at most d log p:
the sum of residue degrees of primes above p is at most d. It is enough
therefore to bound d times

    sum_(n>P) (log n) n^(-1/2) exp(-(log n-u)^2/4).

The summand, viewed on positive real x>=P, is decreasing: its logarithmic
derivative with respect to log x is

    1/log x - 1/2 -(log x-u)/2 < 0.

It is bounded by its integral from P to infinity. Set v=log x-u and
a=log P-u>=R. The integral becomes

    exp(u/2+1/4) integral_a^infinity (u+v) exp(-(v-1)^2/4) dv.

Use u+v <= (U+1)+(v-1), exp(u/2)<=exp(U/2), and

    integral_a^infinity exp(-(v-1)^2/4) dv
        <= 2 exp(-(a-1)^2/4)/(a-1),
    integral_a^infinity (v-1)exp(-(v-1)^2/4) dv
        =2 exp(-(a-1)^2/4).

This proves (3.1). In particular, a logarithmic padding R of order sqrt(U)
plus the requested accuracy margin makes the discarded memory small. The
rule does not omit the composite cofactors in the retained terms.

## 4. Exact energy law and a one-sided prime-memory target

For U>=0 set

    E(U)=integral_0^U |G(u)|^2 du,
    C(U)=Re sum_b Lambda_F(b) q_b^(-1/2-i t0)
                    integral_0^U conjugate(G(u))G(u-log q_b) du.

Multiplying (2.1) by conjugate(G), taking real parts, and integrating gives

    |G(U)|^2 + integral_0^U u|G(u)|^2 du + C(U)=|G(0)|^2.    (4.1)

Equivalently the middle integral is U E(U)-integral_0^U E(v)dv.
The convergence already proved justifies integrating the full memory.

**Corollary 3 (conditional RH implication).** If t0 is fixed and

    for every epsilon>0, C(U)>=-C_epsilon exp(epsilon U)
    for every U>=0,                                         (OPEN-PM)

then zeta_F has no nontrivial zero to the right of the critical line and
hence satisfies its Riemann hypothesis.

Proof. Dropping the nonnegative endpoint term in (4.1) bounds
integral_1^U |G(u)|^2 du by |G(0)|^2+C_epsilon exp(epsilon U).
Thus E(U) is subexponential in U. Cauchy--Schwarz on successive unit
intervals now makes the Laplace integral in (1.3) holomorphic for Re r>0:
choose epsilon<2 Re r on each compact subset. The negative half-line is
controlled by (1.2). Uniqueness of analytic continuation identifies this
holomorphic function with exp(r^2)/zeta_F^S(1/2+i t0+r). The Gaussian never
vanishes, so a zero in that half-plane is impossible. A fixed vertical
translation still covers all imaginary parts. Finite omitted Euler factors
do not affect nontrivial zeros; the functional equation gives the conclusion.

OPEN-PM IS NOT PROVED. The memory identity provides a different arithmetic
object to estimate, with explicit truncation, rather than the estimate
itself. Its exterior coefficients are positive at t0=0, but its correlations
can have either sign. Dropping those signs does not establish the corollary.

## 5. Why a simple dissipativity argument does not close the problem

The formal completion

    2 Re(conjugate(G(u))G(u-v))
       = |G(u)|^2+|G(u-v)|^2-|G(u)-G(u-v)|^2

cannot be summed term by term over the complete prime memory. The positive
measure has infinite total mass, sum_b Lambda_F(b)/sqrt(q_b)=infinity.
The original delayed series converges because G(u-log q_b) is Gaussian
small in the far past; the isolated |G(u)|^2 term has lost that decay.

At a finite prime cutoff P, the total prime-power memory mass is finite,
but it grows on a square-root scale in P under the usual prime ideal
theorem. A uniform-coefficient positivity estimate requiring u to dominate
that mass is incompatible with the native horizon log P about u. No claim
that this particular failure rules out a more precise signed estimate is made.

The substantive next step is to bound the negative part of the weighted
prime-memory correlation itself, retaining the common source and all
delays. The scattering and free-parameter constructions in the companion
notes give alternative coordinates for that work. None presently supplies
OPEN-PM.

## 6. Relation to earlier repository work

The native Gaussian and subpower energy target were already present in
#952; the full equal-norm block and long-twist energies in #954--#955 are
not new here. This note contributes the explicit prime-power evolution,
the all-past uniform tail estimate (3.1), and its direct one-sided energy
adapter. It changes neither the source nor the existing open covariance
status. Standard log-derivative algebra is credited as such.
