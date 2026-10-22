# An actual-theta approximate null vector, with the complete Weil source

**PROPOSED component deduction, not a spectral-bottom bound.** The theta
representation and explicit formula are classical. The purpose of the
calculation is to quantify the residual for this packet's exact operator,
including the entire prime-power tail and the singular archimedean term.
No novelty claim is made for the annihilator principle.

## 1. Normalization from the theta formula

For x>=0 define

    Phi(x) = sum_(n>=1) (4pi^2 n^4 exp(9x/2)-6pi n^2 exp(5x/2))
                               * exp(-pi n^2 exp(2x)),

and extend evenly. The classical theta transformation, followed by two
integrations by parts, gives

    Xi(z)=xi(1/2+iz)=integral_R Phi(x) exp(-izx) dx.                (T1)

One way to track the factors is to put
K(x)=exp(x/2) sum_(n>=1) exp(-pi n^2 exp(2x)). For x>=0,
Phi=K''-K/4 and K'(0)=-1/4. The Mellin integral for xi then gives
Xi(z)=2 integral_0^infinity Phi(x)cos(zx)dx. Evenness and smoothness at
zero follow from the same theta transformation. Each displayed summand
is positive for x>=0 since 2pi n^2 exp(2x)>3.

Put phi=Phi/Xi(0), so integral phi=1 and phi_hat=X of CONVERGENCE.md.
For j=0,1 and x>=1, direct differentiation of the absolutely convergent
series gives

    |phi^(j)(x)| <= C_j exp((9/2+2j)x-pi exp(2x)).                 (T2)

For example, factor exp(-pi exp(2x)) out of the n-sum; the remaining
sum of any fixed power of n times exp(-pi(n^2-1)exp(2x)) is uniformly
bounded for x>=1. The same estimate holds at negative x by symmetry.

## 2. Exact whole-line annihilation does not use RH

The full additive Weil distribution K_W acts on this rapidly decreasing
source as

    K_W * phi = 0.                                                (T3)

To justify it without assuming the zeros real, test against an arbitrary
compactly supported smooth h. The Fourier transform of the relevant
convolution is X(z) times H(z) or H*(z), depending on the polarization.
In the classical explicit formula each nontrivial zero contributes at
z=(rho-1/2)/i, where X(z)=0 IDENTICALLY, regardless of Re rho. The spectral
sum is absolutely convergent: X and its fixed-strip translates have
exponential real-frequency decay, while H has arbitrary polynomial decay
on fixed horizontal strips and the unconditional zero count is O(T log T).
The arithmetic side is also absolutely convergent because phi and its
fixed translates decay faster than every exponential. Equivalently the
explicit formula extends to this test by its usual contour argument.
Thus the pairing vanishes for every h. The convolution is continuous by
the explicit expression below, so (T3) holds pointwise.

For a smooth source f with the stated decay, that expression is

    (K_W*f)(x) = 2 integral cosh((x-y)/2) f(y)dy
       -(log(4pi)+gamma)f(x)
       - integral_0^infinity A(t)[f(x+t)+f(x-t)-2exp(-t/2)f(x)]dt
       - sum_(n>=2) Lambda(n)/sqrt(n)[f(x+log n)+f(x-log n)],       (T4)

    A(t)=exp(-t/2)/(1-exp(-2t)).

The cancellation at t=0 is essential. (T4) is the additive form of
[CCM], equations (3.6)--(3.11), with the same signs as PROOF.md (1).
When f is supported on I_a, its restriction to I_a is A_a f. The infinite
prime sum then reduces automatically to n<=exp(2a); it is not truncated
by choice. The positive pole terms have not been removed.

## 3. A super-exponentially small operator residual

Fix a C-infinity cutoff eta on R, equal to one for t<=0, zero for t>=1,
and 0<=eta<=1. For a>=2 put

    chi_a(x)=eta(|x|-(a-1)),
    m_a=integral chi_a(x)phi(x)dx,
    v_a=chi_a phi/m_a.

The cutoff is smooth at zero because it is constant there. It vanishes
smoothly at +/-a. Thus v_a is in the operator domain of A_a, and
v_a_hat(0)=1. There exist constants C,a0, depending only on eta, such that
for a>=a0,

    ||A_a v_a||_2 <= R_a,
    sup_(|Im z|<=1) |v_a_hat(z)-X(z)| <= R_a,
    R_a = C(1+a) exp(12a-pi exp(2(a-1))).                          (T5)

The exponent 12a is a generous elementary majorant, not an optimized
constant. This is an actual-source residual theorem; it is not a
numerical eigenvalue assertion.

*Proof.* Write r_a=(1-chi_a)phi. By (T2) and its differentiated cutoff,

    |r_a(y)|+|r_a'(y)| <= B_a exp(-2|y|),
    B_a = C exp(9a-pi exp(2(a-1))).                                (T6)

For |y|>=a-1, multiply (T2) by exp(2|y|); the resulting exponent has
negative derivative once |y|>=1. Its maximum is at a-1. The cutoff
and its first derivative have fixed bounds. Elsewhere r_a is zero.
This proves (T6), including the transition layer.

Apply (T4) to r_a for |x|<=a. The pole part is bounded by C B_a exp(a/2).
For 0<t<=1, rewrite the archimedean bracket as

    (r_a(x+t)-r_a(x))+(r_a(x-t)-r_a(x))
                       +2(1-exp(-t/2))r_a(x).

Its absolute value is at most C B_a t, canceling A(t)=O(1/t).
For t>=1, A(t)=O(exp(-t/2)) and the bracket is bounded by C B_a.
Thus the complete archimedean part is O(B_a).
For the primes, use Lambda(n)<=log n and

    exp(-2|x+/-log n|)<=exp(2a)n^(-2).

EVERY prime power, including all beyond exp(2a), is therefore bounded in
absolute value by the convergent resource

    B_a exp(2a) sum_(n>=2) (log n)n^(-5/2) <= C B_a exp(2a).

By (T3), A_a(chi_a phi)=-(K_W*r_a)|_(I_a). Its sup norm is at most
C B_a exp(2a); its L2 norm gains only sqrt(2a). Since m_a tends to one,
it is at least 1/2 for large a. This proves the first inequality (T5),
with the stated generous R_a. The weighted L1 tail bound from (T6),
plus normalization by m_a, proves the second inequality uniformly on
|Im z|<=1. QED.

## 4. Why this does not prove RH

Equation (T5) locates an eigenvalue CLOSE TO ZERO, not necessarily the
lowest eigenvalue. A negative spectral subspace can coexist with an
arbitrarily accurate approximate null vector. The exact family
A_epsilon=diag(-1,epsilon), v=(0,1), is a minimal counterexample to the
invalid inference ||A v|| small => lambda_min(A) near zero.

Combined with CONVERGENCE.md (14), (T5) gives the sufficient estimate

    |F_(a,kappa,0)(z)-X(z)|
      <= R_a + sqrt(2a)exp(a|Im z|)(R_a+C|kappa|)/gamma_a.          (T7)

Here gamma_a is coercivity of q_kappa on zero-mean vectors and kappa must
be below the TRUE spectral minimum. The denominator and the legal shift
are not supplied by the residual theorem. Claiming legal kappa_a->0
along expanding intervals would itself establish unshifted Weil positivity
(by domain nesting), hence would already contain the missing RH step.
This packet does not assume or prove such a sequence.

An improved proof should estimate the exact projected residual rather than
the crude |kappa| term, or control the negative spectral sector directly.
The near-null calculation and real-zero resolvent construction supply
separate ingredients, but neither licenses their identification. Their
composition remains OPEN. In particular the nonreal zeros of X, if any,
would still vanish in (T3); the annihilator identity does not filter them out.
