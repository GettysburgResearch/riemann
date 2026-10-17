# The hidden functional-equation divisor and its first transverse coefficient

Status: PROPOSED complete component arguments; independent mathematical review required.
Scope: an explicit unramified Euler product, its meromorphic continuation,
nonvanishing on a resonant hyperplane, and an exact principal-source detector.
No improved zero-free half-plane, native moment estimate, or RH proof is claimed.
The classical functional equation is an input; no zero-free hypothesis, S6
large sieve, exceptional-character estimate, or short-support theta bound is used.

## 1. Source and exact normalization

Fix a number field F and a finite set S containing every prime ideal of norm
less than 7. Write q=Np. The actual CT setting containing mu_12 with the usual
bad primes already has this property. All sums/products are over prime IDEALS
outside S, including distinct ideals of equal norm.

The unramified rational factor is the one in #971 RAMIFIED_FACTORS.md (6),
at commit 3f1d2a07631eb6cca1f2716be01f64e874667639. Its earlier OpenAI local
source is credited there. We use that displayed expression as an explicit
definition, so the algebra below can be checked without adopting its theta
proof. Identification with a full physical CT integral retains the upstream
source contract and does not assert a new estimate for that integral.

Let |b_p|<=1 be arbitrary fixed phases, and put

    d=q^(-s), W=q^(-w), v=q^(-6z), E=b_p q^(4-6s-6z).

Complex powers use the real logarithm of q. Define

    F0 = 1/(1-v)+W/(1-W)
         +E/(1-E)*[(1-1/q)/(1-v)+W]
         -d/(1-E)*[1+(q-1)Wv/(1-v)],
    H0 = (1-v)(1-W)F0/(1-d).                         (1)

For the principal frequency there are NO exterior ramified primes. A prime
in S is omitted, not given a fake unit character value. Initially define
H(s,w,z)=product H0 on a right half-space of absolute convergence.

The exact numerator N=(1-E)(1-d)H0 is

    N=1-d+dW
      +v[d W^2(q-1)-dWq+d-W]
      +E[W^2 v-W^2+W/q-1/q].                        (2)

In particular the apparent denominator 1-W in (1) has canceled. At E=v=0,

    H0_base=1+dW/(1-d).

The leading mixed Euler term is PLUS dW=q^(-s-w). It therefore produces
zeta_F^S(s+w), NOT its reciprocal. This sign determines the new divisor.

## 2. Meromorphic continuation across Re(s+w)=1

Write Z_F^S(t)=zeta_F(t) product_(p in S)(1-q^(-t)). Define

    K_p(s,w,z)=(1-dW)H0(s,w,z),   K=product K_p.

### Theorem 1

K is holomorphic, normally convergent, and uniformly bounded in imaginary
parts on every closed real-part compact in

    D={Re s>0, Re w>0, Re z>1, 2 Re s+Re w>1}.        (3)

Consequently the ORIGINAL explicitly defined correction has meromorphic
continuation

    H(s,w,z)=Z_F^S(s+w)K(s,w,z)                      (4)

to D. Its only possible polar hypersurface in D is s+w=1. This is a genuine
continuation through the old absolute-product barrier, not a new zero-free
region for zeta. K is NOT asserted nonzero throughout D.

Proof. At E=v=0, direct subtraction gives

    (1-dW)H0_base-1=d^2 W(1-W)/(1-d).                (5)

This cancellation removes the entire first mixed monomial, not just its
value at one parameter. On a real-part compact in D, |d|,|W|<1 with uniform
margins. Also |E|=q^(4-6 Re s-6 Re z)<q^(-2), so 1-E never vanishes.
Using (2) to estimate the terms with v and E gives

 |K_p-1| <= C [q^(-2 Re s-Re w)
                    +q^(1-6 Re z)+q^(4-6 Re s-6 Re z)]. (6)

Each exponent has decay strictly greater than one. The sum over prime ideals
converges by comparison with the ordinary ideal Dirichlet series in its
absolute-convergence half-plane. The same estimates uniformly on compact
sets establish normal convergence, holomorphy, and vertical bounds. On the
original overlap (4) is the exact Euler identity. The region D is convex,
so analytic uniqueness gives the indicated meromorphic continuation. The
classical Dedekind zeta function has only its pole at one; this proves the
polar assertion. QED.

A concrete new point is Re(s,w,z)=(3/5,3/10,2): s+w=9/10<1, but 2s+w=3/2>1.
This point lies outside #971's normal-product domain. No contour of an
inverse L-function is moved through its unknown zeros by Theorem 1.

For a FIXED nonprincipal frequency the same extraction can be made at every
unramified prime: d=theta_p^(-1)q^(-s), W=theta_p q^(-w), hence dW=q^(-s-w).
At each of its finitely many exterior ramified primes replace K_p by
(1-q^(-s-w))H_j using #971's explicit five rational formulas. Their only
local denominator is 1-E, nonzero in (3). Thus the same meromorphic-domain
assertion holds for that fixed frequency under those explicit source
formulas. This extension supplies NO uniform frequency sum or reciprocal
estimate and NO nonvanishing theorem for the ramified K_j.

## 3. The principal residue factor cannot conceal a zeta zero

Let k0(s,z)=K(s,1-s,z). This is defined by Theorem 1 for
0<Re s<1, Re z>1. Here W=1/(qd) and dW=1/q.

### Theorem 2

For arbitrary |b_p|<=1, k0(s,z) is holomorphic and NOWHERE ZERO on

                     0<Re s<1, Re z>1.                (7)

Fix z=2. There is an absolute constant C such that, for degree n_F=[F:Q],
0<delta<=1/2, and delta<=Re s<=1-delta,

 |k0|+|k0|^(-1) <= 2 exp(C n_F/delta^2),
 |(partial_w K)(s,1-s,2)/k0(s,2)| <= C n_F/delta^3.     (8)

The constants are uniform in the imaginary part of s, all allowed phase
profiles b_p and finite exclusions. No discriminant-uniform zeta residue or
functional-equation constant is inferred from these local bounds.

Proof of nonvanishing. On the hyperplane, (2) becomes N=N0+R with

 N0=1-d+1/q,
 R=v(d-1-W/q)+E[-W^2+W/q-1/q+W^2v].                  (9)

Since |d|<1, |N0|>1/q. With x=Re s in (0,1) and Re z>=1, the CORRELATED
sizes |d|=q^-x, |W|=q^(x-1), |E|<=q^(4-6x-6 Re z) give

 |R|/|N0| <= rho_q,
 rho_q=2q^-5+q^-6+2q^-3+q^-2+q^-9
       <=1063987/40353607<1/32, q>=7.                (10)

For example E W^2 costs q^(2-4x-6 Re z), not the bound obtained by treating
E and W as unrelated variables. All seven terms of (9) are retained.
Thus N cannot vanish. The local k0 factor is

          (1-1/q)N/[(1-E)(1-d)],

with nonzero numerator and denominators. Normal convergence from Theorem 1
on (7) now implies global nonvanishing.

For the bounds, the base factor is

 k_base=(1-1/q)(1+1/[q(1-d)]),
 k_base-1=q^-1(d-q^-1)/(1-d).                          (11)

Re(1/(1-d))>1/2 for |d|<1. Hence |k_base|>1-1/q>=6/7.
Also |E|<=q^-2 and (10) imply |k0,p|>3/4. On the indicated strip,
1-q^-delta>=c delta with an absolute c>0, so

 |k0,p-1| <= C delta^-1 q^(-1-delta)+Cq^-2.

At most n_F prime ideals lie above a rational prime; compare with positive
integer sums to obtain sum |k0,p-1|<=C n_F/delta^2. The uniform local lower
bound controls both logarithms of the moduli, proving the first part of (8).
Differentiate the rational formula BEFORE setting w=1-s. Its base part is

 partial_w(K_base-1)=-(log q)d^2 W(1-2W)/(1-d).

The remaining differentiated E,v terms have the same summable bounds with
an extra log q. Therefore sum |partial_w K_p|<=C n_F/delta^3 on z=2.
Use |k0,p|>3/4 to sum partial_w log K_p normally. This is the second part
of (8). The derivative is transverse (s,z fixed), NOT d/ds of k0. QED.

## 4. A residue that loses the zeros; a finite part that retains every one

Write Z=Z_F^S. Its Laurent expansion at one is

                  Z(1+t)=kappa/t+gamma+O(t), kappa>0.

Let Delta(s) be the classical incomplete functional-equation multiplier:

                  Z(1-s)=Delta(s)Z(s).                (12)

For completeness, with G_F(s)=|Disc F|^(s/2)Gamma_R(s)^r1 Gamma_C(s)^r2,
Gamma_R(s)=pi^(-s/2)Gamma(s/2), Gamma_C(s)=(2pi)^(-s)Gamma(s),

 Delta(s)=G_F(s)/G_F(1-s)
             *product_(p in S)(1-q^(s-1))/(1-q^-s).    (13)

It is holomorphic and nonzero on 0<Re s<1. The choice of a constant factor
2 in Gamma_C does not change this ratio. Every finite-S factor remains.

Define the PRINCIPAL arithmetic ratio, with an oblique Mellin coordinate t,

 A(s,t;z)=Z(1-s+t)/Z(s) * H(s,1-s+t,z).                (14)

The additional CT factors Z(6z)q_u^-z are independent of t; for the principal
row q_u=1. They can be retained by multiplying both residue and finite part
by Z(6z), and cancel in the normalized expressions below. Archimedean test
factors, if included, add their own explicit t derivatives; they are not
silently differentiated away. Equations (14)-(17) concern the arithmetic
factor itself, NOT a claimed extraction of its physical integral.

Put k1(s,z)=(partial_w K)(s,1-s,z).

### Theorem 3 (meromorphic Laurent coefficients)

The coefficient of t^-1 and the finite part of (14) are respectively

 R(s,z)=kappa Delta(s)k0(s,z),                          (15)
 V(s,z)=Delta(s)[gamma k0+kappa k1]
             -kappa Delta'(s)k0
             -kappa Delta(s)k0 Z'(s)/Z(s).             (16)

R is holomorphic and nowhere zero throughout (7). V has a SIMPLE pole at
EVERY zero rho of Z in that strip, regardless of its multiplicity m_rho:

             Res_(s=rho) V(s,z)=-m_rho R(rho,z) != 0.  (17)

Thus the residue alone detects no zeta zeros. The first transverse finite
part retains ALL of them and replaces arbitrary reciprocal pole order by
one simple pole with explicit nonzero multiplicity weight.

Proof. Use (4), (12) to write exactly, initially away from zeros of Z,

 A(s,t;z)=Z(1+t)K(s,1-s+t,z)Delta(s-t) Z(s-t)/Z(s).

Expand at t=0: the last three factors are respectively k0+t k1+O(t^2),
Delta-t Delta'+O(t^2), and 1-t Z'/Z+O(t^2). Multiplying gives (15)-(16).
These identities then extend meromorphically in s. They are Laurent
coefficients in t with meromorphic s dependence: they do NOT assert joint
holomorphy at a crossing (s,t)=(rho,0), nor assign a value to 0/0 there.
If Z(s)=(s-rho)^m h(s), h(rho)!=0, then Z'/Z=m/(s-rho)+h'/h.
Every other factor in (16) is holomorphic, and R(rho,z)!=0 by Theorem 2
and (13). This proves (17). QED.

For any fixed finite-order Hecke frequency, replace Z(1-s+t)/Z(s) by
L^S(1-s+t,chi)/L^S(s,bar chi). Its functional equation gives the same
residue formula with its explicit Delta_chi and K_u. All reciprocal poles
cancel from that residue as a MEROMORPHIC identity. For ramified u we have
not proved k0,u nonzero, so the all-zero visibility in (17) is claimed only
for the principal source. No uncontrolled infinite family sum is taken.

## 5. A bounded analytic compensation and exact prime detector

For the principal source at z=2 define

 J(s)=V(s,2)/R(s,2)-gamma/kappa
                -k1(s,2)/k0(s,2)+Delta'(s)/Delta(s).

Then the exact identity is

                         J(s)=-Z'(s)/Z(s).             (18)

In particular the dependence on every auxiliary theta phase b_p disappears
AFTER the explicit compensation. The correction k1/k0 is bounded by (8);
it contains no hidden target zero poles. The remaining gamma and finite-S
terms are explicit. By unique meromorphic continuation, on Re s>1,

              J(s)=sum_(p notin S) sum_(j>=1) log(q)q^(-js). (19)

This is the CLASSICAL prime log-derivative series, not a claimed discovery
of it or a new RH criterion. The new source-specific point is its exact
realization as the compensated FIRST TRANSVERSE COEFFICIENT of (14), with
nonvanishing and quantitative control of the normalizer already proved.

All nontrivial zeros have multiplicity >=1, so J has residue -m_rho at each.
Its holomorphy on Re s>1/2 within the critical strip would exclude all
right-of-line zeros and, with the functional equation, imply the relevant
RH statement. That holomorphy / an adequate physical growth bound is NOT
proved. Identity (18) is not an upper bound for J.

## 6. Why this is not another numerical zero-free improvement

The previous positive moment/zero-density route estimates independent
Mellin lines and retains a difficult reciprocal denominator. The proposed
alternative was to place numerator and denominator on functional-equation
partners and use their exact cancellation. Equations (15)-(17) settle its
first ambiguity: simply bounding the hyperplane residue loses the target
zeros completely; its transverse finite part is the zero-sensitive source.

What is now proved: a normally convergent correction beyond the mixed
Euler barrier; a zero-free residue normalizer on the ENTIRE critical strip;
a simple-pole, phase-independent exact detector; and bounds for its analytic
compensation. What remains: a legal full physical transverse projection,
including derivatives of test factors and every contour remainder, followed
by a genuinely new signed estimate. No derivative bound is inferred from
an estimate of the restriction t=0. No old short-support bound is applied
on a newly continued contour without proof. No new all-field exponent or
native higher-moment conclusion is promoted.

This also connects to #962's separately constructed prime detector and
scattering warnings. The classical log derivative and the general warning
that a canceled pole is no longer detected are credited; this is an explicit
adapter at the original Poisson correction, not two independent RH advances.

## Sources and review boundary

- #971, 3f1d2a07631eb6cca1f2716be01f64e874667639,
  standalone/2026-10-18-ramified-shifted-detector/RAMIFIED_FACTORS.md,
  especially (3), (5), (6). Read live in this pass. The unramified formula
  is inherited; the global extraction, resonant nonvanishing, and jet
  calculation here are new deductions relative to that inspected text.
- #969, 6542781188469e8a23dadf9d419b3d5cf4d11de7, and the delivered full
  packet were inspected for the previous boundary and its declared gaps.
  Its S6/AFE/theta composition is NOT an analytic premise of Theorems 1-3.
- #962, b2032c663736ecd1e3872559d160ce069664ea06: PR description inspected,
  not its complete proof. Prime detector and multiplicity cautions credited
  at that scope only.
- Classical completed Dedekind functional equation, meromorphic continuation
  and pole at one, ideal Euler products, normal-product and Laurent calculus.
  In the rational/Dirichlet specialization the functional-equation and
  finite-Euler conventions are NIST DLMF 25.4 and 25.15.4-5.
- Fresh attempts to retrieve CT v2 and DF 2610.04045 primary bodies failed.
  They are not presented as freshly checked or needed as deep estimates in
  this packet. No upstream theta construction, independent mathematical
  referee, Lean build, or global literature-priority audit was performed.
