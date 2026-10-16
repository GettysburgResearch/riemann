# A radical-preserving geometric lift of the Dedekind reciprocal source

Status: PROPOSED component mathematics, with proofs below. No independent
review, improved native moment exponent, zero-free boundary, or RH proof.
Scope: fixed number field; exact ideal coefficients; uniform physical norm
comparisons; randomized reference moments; signed restoration. New deductions
are not integrated results. Euler manipulations, Rankin counting, and the
Mammen/Peano mechanism are classical or explicitly inherited from #946.

## 1. A second cancellation in the actual local factor

Let F have degree d. Fix an excluded set S containing every prime ideal of
norm below 7. All ideals are nonzero integral ideals prime to S. Put q=Np,
r=1/q, a=1-r, x=q^(-s), y=eta(p)q^2 x^6, with |eta(p)|<=1. The principal
local correction in #948/#949, taken from Cureton--Thorner, is

    H_p=(1-r^2)(1-a*x-y)/[(1-q*y)(1-x)].                 (1)

The first normalization removed 1-q*y. The further normalization here is

    K_p=(1-a*x-y)/[(1-x)(1-y)]
       =1+x(r-y)/[(1-x)(1-y)].                          (2)

Write C_S=product_p(1-q^(-2)). In absolute convergence, Re(s)>1,

    Hhat=C_S product_p K_p
         = H product_p (1-eta(p)q^(3-6s))/(1-eta(p)q^(2-6s)). (3)

When eta is a Hecke character, the extra ratio is
L^S(6s-2,eta)/L^S(6s-3,eta). This notation is NOT needed for the construction:
(3) is initially an Euler identity and the left side has its own continuation.
No finite-order theorem is applied to the generally angular phase eta.

**Theorem 1.** Hhat is holomorphic and nowhere zero on Re(s)>3/7. It and its
inverse are bounded on each closed half-plane strictly inside that region.

Proof. For sigma>=3/7, |x|<=q^(-3/7)<1/2 and |y|<=q^(-4/7)<1/2, since q>=7.
Consequently |a*x+y|<1. Every numerator and denominator in (2) is nonzero.
For fixed sigma0>3/7, their denominators are uniformly separated from zero,
and

    |K_p-1| <= C_sigma0(q^(-1-sigma0)+q^(2-7sigma0)).      (4)

Both prime-ideal series converge: their exponents are greater than one.
Normal convergence gives the holomorphic product. Its logarithmic tail and
inverse converge uniformly; finitely many initial factors have positive
uniform lower bounds. Also C_S>0. This proves the assertions. QED.

Thus the new numerator remains nonzero across the critical line. This is
NOT zero-freeness of the denominator zeta: a pole of 1/zeta still survives.
The number 3/7 is an analytic domain for this correction, not an RH result.

## 2. The surviving coefficients preserve the squarefree radical

Dividing Hhat by the principal zeta factor leaves normalized local source

    F_p(x)=(1-a*x-y)/(1-y)=1-a*x/(1-eta(p)q^2*x^6).       (5)

Its coefficients are

    c_eta(p^(6j+1))=-(1-1/q)eta(p)^j q^(2j),  j>=0,
    c_eta(p^e)=0 for every other e>=1.                    (6)

Every supported ideal has a UNIQUE form n=b*g^6, with b squarefree and
rad(g)|b. In particular rad(n)=b. Its coefficient is

    c_eta(n)=mu_F(b) product_(p|b)(1-1/Np) eta(g)(Ng)^2.   (7)

This is different from #948's 0/1/6 source, where the first and sixth-power
supports were disjoint. Here all lifted powers are attached to primes already
in the squarefree conductor. A sextic row character satisfies chi_n(u)=chi_b(u),
including every nonunit zero. Equal norms never identify distinct ideals.

There is an exact critical mass identity:

    sum_(j>=0) |c_eta(p^(6j+1))| q^(-(6j+1)/2)
          <= q^(-1/2),                                  (8)

with equality for unit eta. Indeed the sum is
(1-1/q)q^(-1/2) sum_j q^(-j). More generally for sigma>=1/2 its positive
majorant is

    rho_p(sigma)=(1-1/q)q^(-sigma)/(1-q^(2-6sigma))
                   <=q^(-sigma).                        (9)

### A literal geometric-probability interpretation

For each p|b independently choose J_p>=0 with probability
(1-1/q)q^(-J_p), and put g=product_(p|b)p^J_p. Then

    Pr(g|b)=product_(p|b)(1-1/q)/(Ng),  rad(g)|b.          (10)

Let xi_u be completely multiplicative with |xi_u|<=1, preserving its original
zeros, and let z_p be a prime-support profile. For bounded compactly supported W,
set

    C_z,u(X)=sum_n c_eta(n)xi_u(n)W(Nn/X) product_(p|n)z_p.

With V(t)=sqrt(t)W(t), the exact normalized identity is

    X^(-1/2) C_z,u(X)
      =sum_(b squarefree) mu_F(b)xi_u(b)/sqrt(Nb) product_(p|b)z_p
          * E_(g|b)[eta(g)xi_u(g)^6 V(Nb*(Ng)^6/X)].      (11)

The probability is positive; its angular phase need not be. Equation (11)
therefore does not assert positivity or cancellation of the completed source.
The factor is sqrt(t)W(t), NOT W(t)/sqrt(t). Compact support makes the actual
coefficient sum finite even though the geometric representation is infinite.

## 3. Constant-cost comparison with the native source, including random profiles

Define

    A_z,u(X)=sum_n mu_F(n)xi_u(n)W(Nn/X) product_(p|n)z_p.

The weight W has support in [a0,b0] inside (0,infinity). Let w be ANY finite
nonnegative row measure, and pi ANY probability law on profiles with
|z_p|<=5/3. Neither independence nor a Hecke interpretation is needed here.
For 1<=p<infinity define the SAME-ROW-MEASURE envelopes

    E_A,p(D)=sup_(0<X<=D) X^(-1/2)||A_z(X)||_(Lp(w x pi)),
    E_C,p(D)=sup_(0<X<=D) X^(-1/2)||C_z(X)||_(Lp(w x pi)).

**Theorem 2.** For every D>0 and p>=1,

    E_C,p(D)<=exp(10d) E_A,p(D),
    E_A,p(D)<=exp(10d) E_C,p(D).                          (12)

For the deterministic native profile z=1, exp(4d) suffices in both directions.
These are scale-independent ROOT-NORM constants, not log(D) losses. At order
2k their moment costs are exp(20dk), or exp(8dk) at z=1.

Proof. The local convolution ratio is

    K_z,p(x)=[1-z*a*x/(1-y)]/(1-z*x)
            =1+z*x(r-y)/[(1-z*x)(1-y)].                 (13)

The actual inverse is

    K_z,p^(-1)=1-z*x(r-y)/(1-y-z*a*x).                   (14)

For R=5/3, the following formal series are coefficientwise nonnegative
majorants independent of every permitted profile:

    V_+(x)=1+R*x(r+q^2*x^6)/[(1-R*x)(1-q^2*x^6)],
    V_-(x)=1+R*x(r+q^2*x^6)/(1-q^2*x^6-R*a*x).

At t=q^(-1/2) both have mass

    1+2R q^(-3/2)/[(1-r)(1-R*t)] <=1+(35/3)q^(-3/2).    (15)

Here t<2/5 and 1-r>=6/7. Each integer norm has at most d prime ideals, so
sum_p q^(-3/2)<=d sum_(n>=7)n^(-3/2)<=2d/sqrt(6)<5d/6.
Multiplying (15) gives two profile-independent ideal majorants v_+,v_- with
critical masses at most exp(175d/18)<exp(10d). They need not be the same
majorant. For R=1 replace 35/3 by 35/9, giving exp(175d/54)<exp(4d).

Let j_z and h_z be the signed kernels defined by (13) and (14). Literal
finite convolution, evaluated with the SAME profile on both factors, gives

    C_z,u(X)=sum_n j_z(n)xi_u(n) A_z,u(X/Nn),
    A_z,u(X)=sum_n h_z(n)xi_u(n) C_z,u(X/Nn).             (16)

Shared factors between n and the residual ideal are REQUIRED. No extra
coprimality is inserted. Bound j_z,h_z by v_+,v_-; multiply by xi_u(n), an
Lp contraction; apply Minkowski and their critical masses. This proves (12).
QED.

The same-height and shorter-scale requirements are essential. This is not a
comparison of the two moments at one fixed X, and a bound only on H=X^h is
not automatically a bound for these envelopes. Random kernels and source
values in (16) are not replaced by independent copies.

## 4. Positive reference moments survive without an extra exponent cost

Use the classical Mammen law: Z takes (1+sqrt(5))/2 with probability
(1-1/sqrt(5))/2, and (1-sqrt(5))/2 with the complementary probability.
Its moments satisfy m0=1,m1=0,mj=m_(j-1)+m_(j-2); mj>=0 for j>=2.
Its absolute support is below 5/3. The law and its use in this project are
credited to #946; neither is claimed as a new discovery.

For D>=2 let Y=(log(3+D))^2. Freeze primes of norm <=Y at z_p=1 and give
the others independent Mammen variables. Let G_k(X;w)=E||C_Z(X)||_(L^(2k)(w))^(2k).

**Theorem 3.** At each fixed k>=1 and epsilon>0, uniformly for 0<X<=D,

    G_k(X;w) <= C_(F,k,W,epsilon) w(total) X^k D^epsilon. (17)

This is a randomized reference theorem, NOT the native completed moment.

Proof. Expand the finite moment. The random variable occurs ONCE per prime
support in each column, regardless of the exponent 6j+1. A prime with a
single occurrence has expectation zero. Apply the Rankin factor
(b0 X)^(2k sigma), sigma>1/2, and absolute values after taking expectations.
Equation (9) bounds the local column mass by q^(-sigma). Hence the entire
positive majorant is at most

    ||W||_infinity^(2k)(b0 X)^(2k sigma)
      product_(q<=Y)(1+q^(-sigma))^(2k)
      product_(q>Y) [sum_(j=0)^(2k) binom(2k,j)mj q^(-j sigma)]. (18)

All masks only delete terms in this positive count. For fixed k the rough
factor is 1+O_k(q^(-2sigma)), whose product converges. For fixed
sigma=1/2+delta<1 the small-prime logarithm is O_(F,k,delta)(Y^(1/2-delta)),
using at most d prime ideals of each integer norm. This is o(log D).
Choose delta small relative to epsilon/k; use X<=D and enlarge the constant
on a bounded interval. Equation (17) follows. No prime ideal theorem or
new large sieve is used. QED.

No k-uniform error constant is asserted in (17). The comparison (12), by
contrast, explicitly retains its order dependence.

## 5. The signed restoration has the same critical cofactor budget

Fix a prime p not yet restored, condition on all other multipliers, and
exclude p from the residual source. Equations (5)-(7) give EXACTLY

    C=U+Z_p V,
    U=C^(p excluded)(X),
    V=-(1-1/q) sum_(j>=0) eta(p)^j q^(2j) xi_u(p)^(6j+1)
                    C^(p excluded)(X/q^(6j+1)).          (19)

The sum is finite at a fixed compact test. If p divides the physical row,
V=0. No other zero is changed. The same physical row, original exclusions,
all composite cofactors, and all shorter scales are retained.

The normalized absolute cofactor budget is EXACTLY the native one:

    (1-1/q) sum_(j>=0) q^(2j)q^(-(6j+1)/2)=q^(-1/2).    (20)

Thus any common-height bound ||C^(p excluded)(T)||<=B sqrt(T) gives
||V||<=B sqrt(X/q). This does not supply B or bound the signed injection.

For completeness the inherited #946 local functional is

    R_k(U,V)=E|U+ZV|^(2k)-|U+V|^(2k)
                       +2k|U|^(2k-2) Re(U conjugate(V)).

That packet proves
R_k>=((2k)_4/24)(8/75)^(k-2)|V|^(2k)>=0 for k>=2, and R_2=|V|^4.
Its proof uses the Peano kernel of Eg(Z)-g(1)+g'(0): it is nonnegative,
has mass 1/24, and the probability measure 24K(t)dt has variance 8/75.
For g(t)=|U+tV|^(2k), its fourth derivative is at least
(2k)_4 |V|^(2k)(Re(U/V)+t)^(2k-4). Jensen proves the quoted constant.
This local theorem is inherited, not reproved or strengthened by lifting.

Restore the remaining primes in any fixed order. Sum the local identity
with conditional expectation over the still-random coordinates and w over
rows. Then the exact all-order identity is

    M_C,2k = G_k + I_C,k - D_C,k,
    I_C,k=2k sum_(steps,u) w(u) E[|U|^(2k-2)Re(U conjugate(V))],
    D_C,k=sum_(steps,u) w(u) E R_k(U,V)>=0.                (21)

At order four D_C,2=sum w E|V|^4. The theorem applies because our lift is
MULTIAFFINE IN PRIME SUPPORT. Replacing Z_p by Z_p^(6j+1) would destroy
this identity and the zero-singleton reference.

The remaining specific inequality is

    I_C,k <= D_C,k + C_epsilon H D^(k+e_k+epsilon).       (OPEN-LIFT)

For the original tests, twists, row heights, and same-height scale envelopes,
(12), (17), and (21) transfer this to the native hierarchy. With e_k=o(k)
and admissible h_k=o(k), the inherited replica/Mellin implication approaches
1/2. OPEN-LIFT is NOT proved here and is equivalent up to the controlled
reference to the needed completed moment bound. Neither (8), positivity of
D_C,k, nor the probability in (10) establishes it.
