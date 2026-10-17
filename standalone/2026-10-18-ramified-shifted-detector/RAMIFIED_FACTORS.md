# Exact ramified factors: remove the artificial two-thirds wall

Status: PROPOSED complete component proofs, not independently reviewed.
Scope: local identities, normal convergence of the original correction, and
fixed-field averages of that correction. No new zero-free region is claimed.
The original Poisson identity is imported at its specified scope; the local
summation and bounds below are proved. Nonvanishing of a correction is NOT
asserted from boundedness, and inverse-L estimates remain separate.

## 1. The source and conventions

Use CT v2's Section 11 original frequency series, and its cited OpenAI
primitive-roots local Fourier calculation. Freeze the latter at
1581d4cbdd69a0faf34b2089614fe2a814316a6a,
build/sections/05-poisson.tex, blob c8526f74b281d37fda034c17195c4bb5afd5f79b.
The complete path and inspected lines are in SOURCES.md. We do not invoke
any zero-free conclusion of those papers in this component.

Fix F containing mu_12 and the permissible fixed S, including residue
characteristics 2 and 3. Write Q=Np at an exterior prime. Its residue field
contains mu_12. The specified character chi has order six and chi(-1)=1.
Positive-modulus characters are extended by ZERO at nonunits, even when
their exponent is divisible by six. A modulus p^0 instead has one residue
and character value one. Let psi be the fixed unramified primitive additive
character. Put

    T_v(y)=sum_(r mod p) chi(r)^v psi(yr/p),  tau_v=T_v(1).

For y a unit, T_v(y)=conj(chi(y))^v tau_v. At y divisible by p, its value
is Q-1 if v=0 mod 6 and zero otherwise. In particular tau_0=-1, and
|tau_v|=sqrt(Q) for v not 0 mod 6. Also tau_1 tau_5=Q.
These follow from finite character orthogonality and the Gauss norm identity.
They do not replace the absent-modulus convention.

For u with j=v_p(u) in {0,...,5}, put J=j+6m. The source's stripped sum is

 C_(t,k)(J)=sum_(d mod p^k; p^J=p^t d mod p^k) chi(d)^k
             sum_(v mod p^t) chi(v)^t psi((p^J-p^t d)v/p^(k+t)).       (1)

Its exact evaluations are

 C_(0,0)(J)=1,              C_(0,k)(J)=1_(J=0), k>0;
 C_(t,0)(J)=1_(J>=t-1) Q^(t-1) T_t(p^(J-t+1)), t>0;
 C_(t,1)(J)=1_(J>=t) tau_1 Q^(t-1) T_(t-1)(p^(J-t)), t>0;
 C_(t,k)(J)=0, t>0,k>=2.                                         (2)

For k=0, summing the p-adic lifts of v gives the first positive-t formula.
For k=1, the congruence requires J>=1. Sum over d before v. The sum in d is
tau_1 conj(chi(v)), since chi(-1)=1, and the remaining lifts give the next
formula. For k>=2, translating d by p^(k-1)lambda preserves its unit status,
character and congruence, but gives a nontrivial additive character in
lambda for every unit v. Its sum is zero. Formula (2) follows. This argument
works over the residue field of any size, not just a prime field.

Let theta=chi(u/p^j), so |theta|=1 even when p divides u. Let g=gamma_2(p)
and h=vartheta(p), both unit-modulus. Define the auxiliary variables

 a=g h theta^(-1) Q^(-1/2-xi),    b=h^3 theta^(-3) Q^(-1-3xi),
 r=theta Q^(-w),                 v=Q^(-6z),
 d=-a tau_1,                    e=Q^6 b^2 v.                     (3)

Here d and r are AUXILIARY UNIT-PHASE variables. At p|u they are NOT the
zero-valued local characters of the extracted L-functions. Those L-factors
are absent, whereas theta=chi(u/p^j) in (3) must remain. The source relation
g h tau_1/sqrt(Q)=-eta(p) identifies d=eta(p)theta^(-1)Q^(-xi), with eta=1
for CT's Dedekind target. In particular |d|=Q^(-Re xi).

The exact source local series is

 F_j=sum_(epsilon=0,1; l,k,m>=0)
           a^epsilon b^l r^k v^m C_(epsilon+3l,k)(j+6m).           (4)

This is the original common-prime calculation, not a modified family.
The normalized correction at j>0 is H_j=(1-v)F_j. Initially all identities
are proved on an absolute-convergence right half-space.

## 2. Five rational formulas

**Theorem R1.** For j=1,...,5, H_j=N_j/(1-e), where

 N_1=1-e/Q + d r(1-Qv),
 N_2=1-e/Q -(Q-1)d r +(1-v)Q^2 b tau_3,
 N_3=1-e/Q -(Q-1)d r +(1-v)(Q^2 b tau_1 tau_2 r+Q^3 a b tau_4),
 N_4=1-e/Q -(Q-1)d r +(1-v)Q^3 a b tau_1 tau_3 r,
 N_5=1-e/Q -(Q-1)d r -(1-v)Q^5 b^2.                            (5)

**Proof.** The allowed t=epsilon+3l residues modulo six are 0,1,3,4.
For t>0, (2) has the following exhaustive possibilities:

|t mod 6|k=0|k=1|
|---|---|---|
|0|J=t-1: -Q^(t-1); J>=t: Q^(t-1)(Q-1)|J=t: Q^t|
|1|J=t-1: Q^(t-1)tau_1|J=t: -Q^(t-1)tau_1; J>t: Q^(t-1)tau_1(Q-1)|
|3|J=t-1: Q^(t-1)tau_3|J=t: Q^(t-1)tau_1 tau_2|
|4|J=t-1: Q^(t-1)tau_4|J=t: Q^(t-1)tau_1 tau_3|

All omitted cases vanish. For j>0 the t=0 contribution is 1/(1-v).
The t=6n, n>=1, J>=t terms contribute
(1-Q^-1)e/((1-e)(1-v)). There is an additional J=t-1 shell only for j=5:
its sum is -Q^5 b^2/(1-e). The k=1 shell at t=6n occurs only at j=0 and
therefore does not enter (5).

For t=6n+1, n>=0, only k=1 occurs for j>0. At j=1, its boundary and tail
sum to d r(1-Qv)/((1-e)(1-v)); at j>=2 the sum is
-(Q-1)d r/((1-e)(1-v)). The t=6n+3 boundary occurs at j=2 for k=0 and j=3
for k=1. It gives Q^2 b tau_3/(1-e) or Q^2 b tau_1 tau_2 r/(1-e).
The t=6n+4 boundary occurs at j=3 or 4 and gives Q^3 a b tau_4/(1-e) or
Q^3 a b tau_1 tau_3 r/(1-e). Adding these contributions and multiplying by
1-v proves all five formulas. No shell is discarded. In particular l and
m were summed subject to their support, not as unrelated geometric series.
The same calculation proves local absolute convergence when |v|,|e|<1,
regardless of whether |Q^3 b| is less than one. QED.

For reference, when j=0 put W=theta Q^-w and D=d. The unramified formula is

 F_0=1/(1-v)+W/(1-W)
       +e/(1-e)[(1-Q^-1)/(1-v)+W]
       -D/(1-e)[1+(Q-1)Wv/(1-v)],
 H_0=(1-v)(1-W)F_0/(1-D).                                  (6)

This is already explicitly summed in the OpenAI source, not a new formula
claimed here. Equations (5), the complete ramified case, sharpen the crude
ramified shell estimate subsequently used there and in CT.

## 3. Holomorphic domain and a critical uniform bound

Let x=Re xi, y=Re w, z0=Re z. Define the OPEN convex domain Omega by

 x,y,z0>0;
 6z0+y>1, x+6z0>1, x+y>1, x+y+6z0>2, 6x+6z0>5.             (7)

**Theorem R2.** For each actual frequency u the ORIGINAL H_u is holomorphic
on Omega. On every bounded real-part compact subset of Omega intersected
with x>=1/2, and uniformly in imaginary parts,

                         |H_u| <= C_epsilon q_u^epsilon.    (8)

The compact may touch x=1/2 provided all margins in (7) remain positive.
It need not obey 3x>2 or 3x+y>5/2. The conclusion asserts holomorphy and an
upper bound, NOT nonvanishing of H_u or its L-function denominator.

**Proof.** The unramified formula (6) gives, with compact-dependent constants,

 |H_0-1| << Q^(-6z0-y)+Q^(-x-6z0)+Q^(-x-y)
             +Q^(1-x-y-6z0)+Q^(4-6x-6z0).                  (9)

For sufficiently large Q its denominators are uniformly bounded away from
zero; the finitely many smaller Q also have nonzero denominators since
x,y,z0>0 and x+z0>5/6. All terms in (9) have exponent strictly below -1,
so the product over p not dividing u converges normally, uniformly in u
and phases. The bounds hold over arbitrary fixed F by ideal counting.

There are only finitely many p|u. Their (5) denominators 1-e never vanish
on Omega because |e|<Q^-1. Thus their product is holomorphic. This proves
the first assertion, including points x<1/2. Analytic continuation is from
the original right half-space inside the convex domain (7).

For (8), the common errors e and (Q-1)dr have sizes
O(Q^(4-6x-6z0)) and O(Q^(1-x-y)). The other ramified sizes are

 j=1: Q^(-x-y) and Q^(1-x-y-6z0);
 j=2: Q^(3/2-3x);
 j=3: Q^(2-3x-y) and Q^(2-4x);
 j=4: Q^(5/2-4x-y);
 j=5: Q^(3-6x).                                           (10)

If x>1/2 and x+y>1, every exponent in (10) is strictly negative.
Hence H_j=1+O(Q^-delta) uniformly on interior compacts. At x=1/2 they are
nonpositive, and |H_j| is still at most a fixed constant C. Consequently
product_(p|u)|H_j| <= C^omega(u) <<_epsilon q_u^epsilon; enlarge the fixed
threshold so C<=Q^epsilon for large primes and absorb the finitely many
others once each. This also proves uniformity on compacts meeting x=1/2.
Together with the uniformly bounded unramified product, it gives (8). QED.

A concrete newly allowed interior point is (x,y,z0)=(3/5,1/2,2/5).
All five margins in (7) are positive, while the old conditions 3x>2 and
3x+y>5/2 both fail. Thus this is a strict enlargement, not a different
notation for CT's old domain. At the critical face use, for example,
(1/2,3/4,1/2). This does NOT license a contour through actual L-function zeros.

## 4. Weighted averages beyond the critical face

Put delta=max(0,1/2-x). Uniformly on a real-part compact in Omega, (10) gives

 |H_u| <= C_epsilon q_u^epsilon
       product_(v_p(u)=2) Q^(3delta)
       product_(v_p(u)=3) Q^(4delta)
       product_(v_p(u)=4) Q^(3delta)
       product_(v_p(u)=5) Q^(6delta).                       (11)

Indeed x+y>1 bounds the first j=3 exponent by 2delta and the j=4 exponent
by 3delta. At j=1 the errors decay. Absorb the bounded factor per ramified
prime as in Theorem R2. The finite S-unit class multiplicity is fixed.

**Theorem R3.** For every fixed real p>=1 and compact subset of Omega on
which x>1/2-1/(3p), for U>=2,

             sum_(u: q_u<=U) |H_u(xi,w,z)|^p << U^(1+epsilon).     (12)

These are the complete sixth-power-free frequencies, with full ideal-norm
ordering and the original finite unit classes. Constants are fixed-field,
compact- and p-dependent. No growing-p uniformity is asserted.
In particular the second correction moment is bounded for x>1/3.

**Proof.** Raise (11) to p, using epsilon/p for its preliminary loss. Let
w_j=Q^(p c_j delta) with c_1=0,c_2=3,c_3=4,c_4=3,c_5=6. Majorize the
multiplicative weight on a sixth-free ideal a by

 sum_(d|a) h(d),  h(p)=0, h(p^j)=w_j-1>=0 for 2<=j<=5,
 h(p^j)=0 for j>=6.

This is a majorant, not a claimed equality: for v_p(a)=j it includes w_j
and the other nonnegative terms. If delta<1/(3p), every exponent
p c_j delta-j is strictly below -1. The j=2 inequality is the binding one;
the others are weaker. Hence sum_d h(d)/Nd is bounded by its convergent
nonnegative Euler product. Fixed-field ideal counting yields

 sum_(Na<=U) sum_(d|a)h(d) <= C_F U sum_d h(d)/Nd.

Dropping the sixth-free restriction in this last positive count is legitimate.
Multiply by the fixed number of unit classes and the preliminary U^epsilon.
This proves (12). This is a correction-factor moment, not a numerator-L or
native-Mobius moment, and not a claim that inverse denominators have this mean.

## 5. Why subcritical uniform suprema really fail

The critical threshold for the uniform subpower claim cannot simply be
removed. Fix 0<x<1/2, y=2,z0=1. For a prime-frequency u=p^2, the j=2 term
in (5) has a unique growing term Q^2 b tau_3 of modulus Q^(3/2-3x), while
all other terms remain bounded or decay. Thus

                    |H_2| asymp Q^(3/2-3x).                (13)

For a FULL H_u lower example, enlarge fixed S to include the finite set of
primes for which the uniform bound (9) is not smaller than 1/2. This is an
allowed choice of source data, made once. The product of the other local
factors is then bounded above and away from zero uniformly in their phases.
Along unbounded allowed prime ideals, (13) gives

                  |H_(p^2)| asymp q_u^(3/4-3x/2).

Therefore a uniform q_u^epsilon estimate for every epsilon>0 is false below
x=1/2 at this scope. No zero distribution, RH, or prime number theorem is
used: infinitely many prime ideals suffice. This is not a lower bound on
the original signed Poisson sum.

## 6. What the new domain does not finish

The frequency sum and the inverse L-function remain. A correction bound on
Omega does not grant a zero-free contour for those denominators. The old
principal specialization H(s)=H_1(s,1,1/6) still has its stated convergence
threshold Re s>2/3; (7) specializes to the same restriction. Nor does this
local argument improve the physical theta norm. It removes an artificial
ramified convergence wall and supplies (11)-(12) for future summed-contour
arguments. No global zero-free fraction is deduced in this file.
