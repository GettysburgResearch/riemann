# Match two native logarithmic coefficients with a real-root base

Status: proposed source-qualified analytic transport; independent review is
required. This file gives a complete conditional mechanism, not a new native
sector certificate. It preserves all unseen tail zeros and multiplicities.
RH remains unproved. The exact base coefficient ranges and any expanded
complex domain still require directed execution.

Use the complete paired-product convention and authenticated finite census
of `GAUSSIAN_TAIL_TRANSPORT.md` and `TAYLOR_TAIL_BINDING.md`:

    Xi(z)=Xi(0) P_R(z) q_R(z),
    P_R(z)=product_(0<gamma<=R)(1-z^2/gamma^2),
    log q_R(z) = -sum_(k>=1) t_k z^(2k)/k,
    t_k=sum_(Re rho>R) m_rho rho^(-2k).

The complete tail is in |Im rho|<=A, Re rho>R; every nonreal conjugate block
has equal multiplicity. Assume R>3A, and retain a proved bound
S>=sum_tail m_rho/|rho|^2. Put a1=t1 and b2=t2/2. Root sums and logarithms
below converge absolutely on every protected disk of radius less than R.

## QA1. Positive native coefficients and an available real-root base

The complete tail coefficients are real. A real positive root gamma with
multiplicity m contributes

    B=m/gamma^2,       C=m/gamma^4

to t1,t2, with B>0,C>0 and B^2>=C. A nonreal conjugate block gamma±i eta
of multiplicity m contributes

    B=2m(gamma^2-eta^2)/(gamma^2+eta^2)^2,
    C=2m(gamma^4-6gamma^2 eta^2+eta^4)/(gamma^2+eta^2)^4.

Here B>0. Since eta^2/gamma^2<1/9, C>0 as well. The exact identity

    B^2-C = 2m[(2m-1)(gamma^2-eta^2)^2+4gamma^2 eta^2]
               /(gamma^2+eta^2)^4 > 0                         (QA1)

uses integer multiplicity m>=1. Summing finite partial blocks gives
(sum B)^2>=sum C; the cross terms make this strict whenever at least two
blocks occur. Passing to the absolutely convergent complete tail proves

    a1>0, b2>0, a1^2>2b2,
    a1<=S, 2b2<=S/R^2.                                      (QA2)

The strict inequality uses the source's infinitely many tail zeros. The
complete even order-below-two product and the positive imaginary-axis source
growth in `SOURCE_TRANSPORT.md` justify this: a finite complete zero set
would make Xi a polynomial, contradicting that growth. The finite library
count through R and a coarse upper count do not establish this fact. It does
not follow from a fitted finite tail. Thus one additional real pair is available.

## QA2. Match the quartic coefficient; optionally use integer multiplicity

Fix an integer K>=1 satisfying

    a1>=sqrt(2K b2).

For K=1 this follows strictly from QA2. A larger fixed K requires an explicit
native interval or other source bound; QA2 does not prove it for arbitrary K.
Define

    v=sqrt(2b2/K),       a=a1-Kv>=0,
    G_(a,v,K)(z)=Xi(0) exp(-a z^2) P_R(z)(1-v z^2)^K.          (QA3)

Its extra real roots are ±v^(-1/2), each of multiplicity K. The v=0 endpoint
is interpreted by deleting this factor. The base is in the Laguerre–Pólya
class: its polynomial has only real roots, and the nonnegative Gaussian is
a locally uniform limit of real-root polynomials.

The native matching identities are exact, because

    a+Kv=a1,       Kv^2/2=b2.

Consequently Xi=qG, with q nowhere zero on

    |z|<min(R,v^(-1/2)),

and the holomorphic residual logarithm h=log q starts at degree six:

    h(z)=-sum_(k>=3)[t_k-Kv^k] z^(2k)/k.                       (QA4)

Neither b2 nor a1 is replaced by an estimated midpoint. A certificate must
bind their complete native interval and the resulting entire parameter family.

## QA3. Complete residual budgets

Let B<R and v B^2<1. Set u=B^2/R^2 and w=vB^2. For k>=3,

    |t_k-Kv^k| <= S/R^(2k-2)+Kv^k.

Termwise differentiation and geometric summation give

    |h'| <= J1 = 2B^5 [S/(R^4(1-u)) + Kv^3/(1-w)],            (QA5)
    |h''| <= J2 = 2B^4 [S/R^4 * (5-3u)/(1-u)^2
                       + Kv^3 * (5-3w)/(1-w)^2].              (QA6)

Both terms retain the whole actual tail; the second terms pay the entire
artificial real factor. The identities used are sum_(j>=0)x^j=1/(1-x) and
sum_(j>=0)(5+2j)x^j=(5-3x)/(1-x)^2. Outward upper parameter bounds may be
substituted, since each nonnegative series is increasing in its parameter.

At fixed b2, the artificial contribution Kv^3=(2b2)^(3/2)/sqrt(K) decreases
with K and the artificial root radius (K/(2b2))^(1/4) increases. This is a
priced improvement subject to the Gaussian constraint in QA3, not permission
to send K to infinity. A sufficient interval guard for a fixed K is

    a1_lower>=sqrt(2K b2_upper).

At a chosen protected B the independent radius guard is
B^2 sqrt(2b2_upper/K)<1. These two guards must both be checked.

## QA4. Native degree-four binding

Write Xi(z)=c0+c2 z^2+c4 z^4+O(z^6), with c0>0. The complete product gives

    b2 = c2^2/(2c0^2) - c4/c0
           - (1/2) sum_(0<gamma<=R) gamma^(-4).                (QA7)

The finite sum uses the authenticated complete real census; no root is
removed because its contribution is small. The coefficients are obtained
from the actual Gamma/zeta series with s=1/2+iz, exactly as in the reviewed
quadratic binding. The complete coefficient identity and the source strip
prove b2 positive independently of a rounded interval. A directed degree-four
jet and every complete census root ball must still enclose the actual value.

Combined outward intervals may overestimate the admissible correlated
coefficient set. It is valid to enclose a larger family, provided it contains
the actual pair and every model parameter used for the LP bounds satisfies
a>=0. Any full-domain acceptance must include every allowed parameter box.

## QA5. Protect the real boundary and the companion quotients

Fix lambda>0 and derivative order zero. For a model G, write

    E0=G-i lambda G',       W0=i E0/E0'.

The LP polynomial-approximation argument in the Gaussian packet proves both
companions nonzero and Re W0>0 in the open lower half-plane. Real multiple
artificial roots do not invalidate this open-half-plane argument. For a
closed protected compact set, require B below every artificial root and
the authenticated census roots in |x|<=B to be simple. Thus all real zeros
of G in that compact set are simple; its strict real Laguerre numerator is

    G'^2-GG'' = G^2[2a + sum_real_roots multiplicity/(x-root)^2]

away from zeros, and is G'^2>0 at a simple root. It gives the boundary sign

    Re(i E0/E0') = lambda(G'^2-GG'')/(G'^2+lambda^2 G''^2)>0.   (QA8)

It also protects the real companion denominators. The nonconstant census
factor is retained even at the a=v=0 model endpoint. No strict real-boundary
claim is made at an artificial multiple root outside the protected compact.

The same LP disk bounds hold in the closed protected lower region:
|G/E0|<=1 and |(G-2i lambda G')/E0|<=2. Suppose a directed finite enclosure
proves on a complete complex/parameter box

    |W0|<=M,       Re W0>=p>0,       tau=p/M.

Using the full multiplier Xi=qG gives exactly

    E_Xi=q[E0-i lambda h'G],
    E_Xi'=q[E0'+h'(G-2i lambda G')-i lambda(h''+h'^2)G].

Therefore set alpha=lambda J1 and
beta=M[2J1+lambda(J1^2+J2)]. The finite acceptance predicate is

    beta<1,       alpha+(1+tau)beta<tau.                        (QA9)

It protects both actual companions and proves

    Re(i E_Xi/E_Xi') >= p-M(alpha+beta)/(1-beta)>0.

This is the order-zero transport only. A higher fixed derivative order needs
the full original-function Leibniz/Bell formulas and new derivative/family
denominator margins. Matching two native coefficients alone does not provide
those higher-order certificates.

## QA6. Claim boundary

The mechanism is exact even when the complete tail contains nonreal zeros.
It absorbs two source coefficients into a permitted real-root base and pays
both the remaining complete tail and the artificial factor. An expanded
native sector requires actual interval binding, complete domain/parameter
coverage and strict QA9 acceptance. No such expanded certificate is proved
by this manuscript alone. It does not extend the real primitive census or
establish a cofinal protected complex domain, an Euler bridge, or RH.
