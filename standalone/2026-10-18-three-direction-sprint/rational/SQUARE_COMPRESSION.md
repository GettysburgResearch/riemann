# A one-dimensional square-source alternative with an explicit error floor

Status: **PROPOSED source reduction. The complete signed one-dimensional
estimate remains OPEN. No improved zero-free boundary is proved.**

The zero-loss balanced-pair reduction is `MASKED_COMPRESSION.md`.
This alternative deliberately accepts a larger, fully quantified error
in exchange for a one-dimensional reference source. It is still adequate
for the illustrative intermediate boundary 5/6 if its remaining estimate
can be proved. By itself its error floor cannot reach RH.

## 1. Full masked source and exact new coefficients

Use ALL definitions and exact annular fixed masks of
`MASKED_COMPRESSION.md` Sections 1--2, including

    V_(Y,omega)(k)=sum_(q>=2)omega_j(q)C_Y(q)S_q(k), k in I_j,
    alpha_(j,d)=sum_(q:d|q)mu(q/d)omega_j(q)C_Y(q),
    V_(Y,omega)(k)=sum_d alpha_(j,d)R(k/d),
    |alpha_(j,d)|<<_epsilon Y^epsilon/d.                       (1)

The masks may be the exact native large-denominator and arbitrary
prefix-dependent original core cutoff, with no subpower restriction.
They are fixed within each complete annulus; arbitrary cellwise weights
are not claimed.

For any requested epsilon>0, there is an explicit real diagonal
old-input amplitude

    D_(Y,omega)(k)=sum_(r<=Y,mu(r)^2=1)t_j(r)R(k/r^2),
                                      k in I_j,                (2)
    |t_j(r)|<<_epsilon Y^epsilon/r,

such that on EVERY strict native cell Y+1<=k<(Y+1)^2,

    ||V_(Y,omega)-D_(Y,omega)||_2^2
                      <<_epsilon Y^(2/3+epsilon).             (3)

Every reference is the actual old pair (r,r), whose Mobius product
is mu(r)^2=1. Its input weight is r^2 t_j(r). This is NOT a claim
that square products have only square reduced denominators. The full
R(k/r^2) in (2), including every lower divisor and its centering, is
retained. There is no new reference core projection.

## 2. Legal references from one squarefree root interval

Discard d<=L=floor(sqrt Y) at the already proved COMPLETE discrete
energy cost O_epsilon(Y^epsilon), by `MASKED_COMPRESSION.md` (11)--(12).
Partition ALL remaining d into integer dyadic blocks D<=d<2D,
D a power of two, write X=sqrt D, and fix a small eta>0.
Put H=ceil(X^(1/5+eta)). For each target d let n=floor(sqrt d),
and use every squarefree root in the interval

    G_d={r:n-H+1<=r<=n, mu(r)^2=1}, g_d=|G_d|.                (4)

Tolev's uniform primary squarefree density theorem, precisely cited
and checked in `SOURCES.md`, gives g_d>=H/2 for all sufficiently
large Y. Only its ONE-INTERVAL density is needed here. Uniformity
holds because n is comparable to X and X>=cY^(1/4) tends to infinity.
Every root is positive, squarefree, and <=floor(sqrt d)<=Y. Thus
there is NO upper-corner exclusion or large-product endpoint loss.

Every reference product M=r^2 satisfies

    M is comparable with X^2,
    0<=d-M<=C X H<<X^(6/5+eta).                              (5)

Define the explicit probability transport and diagonal coefficient

    D_(j,X)(x)=sum_(d in block,d>L)alpha_(j,d)/g_d
                                      sum_(r in G_d)R(x/r^2),
    t_(j,X)(r)=sum_(d:r in G_d)alpha_(j,d)/g_d.                (6)

This is finite and signed. Shared prime powers in the original
coefficients remain encoded by (1), with no sign dropped. For a fixed
r, membership implies n in [r,r+H-1], so the targets lie in an
interval of O(XH) integers. Since g_d>=H/2 and
alpha_(j,d)<<X^epsilon/X^2 on these blocks,

    |t_(j,X)(r)|<<_epsilon X^(-1+epsilon).                    (7)

A fixed r belongs to only a bounded number of adjacent product blocks,
so summing the blocks gives (2). Every coefficient in (6) retains
the complete original Q/core masks through alpha_(j,d).

## 3. Complete global transport error and its exact exponent

The full block difference

    W_(j,X)(x)=sum_(d in block,d>L)alpha_(j,d)
                     [R(x/d)-g_d^-1 sum_(r in G_d)R(x/r^2)]   (8)

has exactly zero total R coefficient and integer dilations. It is
therefore constant on every complete integer cell. The compact-flux
theorem `FLUX_COMPRESSION.md` (2), with D=X^2,
G<<X^(6/5+eta), gives for fixed 1/6<theta<1/2

    ||W_(j,X)||_L2(0,infinity)^2
       <<_epsilon X^(-2+4theta+(2-2theta)(6/5+eta)+epsilon).   (9)

At theta=1/6 the exponent would be

    2/3+(5/3)eta.                                           (10)

For every requested final loss choose fixed eta>0, theta>1/6 and
the divisor losses sufficiently small. The exponent in (9) is then
at most 2/3 plus that requested loss. All X<=Y, so summing the
O(log Y) block root norms and O(log Y) disjoint native annuli gives
O_epsilon(Y^(2/3+epsilon)) complete error energy. The already paid
low-d part has smaller subpower energy. All cross terms are paid
by the root triangle inequality. This proves (3), with no time tail,
new Fourier window, or missing native output interval.

## 4. The one-dimensional signed arithmetic left to estimate

The coefficients have an exact square-shell description. Within one
product block H is fixed. Define

    A_(j,X)(n)=sum_(n^2<=d<(n+1)^2, d in block,d>L)alpha_(j,d),
    g_X(n)=sum_(n-H<r<=n)mu(r)^2.

Then the ACTUAL reference coefficient is

    t_(j,X)(r)=mu(r)^2 sum_(r<=n<r+H) A_(j,X)(n)/g_X(n).      (11)

The sum includes partial shells at product-block boundaries. Each
shell coefficient is a complete signed sum, not an arbitrary new
variable. Trivially |A_(j,X)(n)|<<Y^epsilon/n and g_X(n)>=H/2,
which recovers (7) but does not yield cancellation. The factor
mu(r)^2 supplies squarefree support only; no free Mobius sign remains
at the reference roots.

The kernel R(k/r^2) has reciprocal-square dilation and exact jumps
at r=floor(sqrt(k/jump_index)). A square-root-phase estimate cannot
simply be substituted without deriving its exact phase, coefficient
class, all root ranges and complete remainders. In particular generic
bounded coefficients in (11) can still produce large full energy.
No such external phase adapter is asserted here.

### A complete small-root sector bound

For every u>0, |R(u)|<=1/u. For u<1 this follows directly from
R(u)=-log u-gamma and -log u<=1/u-1; for u>=1 it is the harmonic
remainder estimate. Thus the actual coefficients in (2) give, for
any 1<=T<=Y and every native k,

    |sum_(r<=T)t_j(r)R(k/r^2)|
         <=k^-1 sum_(r<=T)|t_j(r)|r^2
         <<_epsilon Y^epsilon T^2/k.

The entire coherent small-root energy, including all annuli, is

    <<_epsilon Y^epsilon T^4/Y.                              (11a)

In particular roots r<=Y^(5/12) can be removed within the existing
Y^(2/3+epsilon) square-compression error budget. For an exact
prefix-dependent budget G_Y one may instead use the COMPUTABLE
old-source quantity

    M_Y(T)=max_j sum_(r<=T)|t_j(r)|r^2.

Whenever M_Y(T)<=sqrt(Y G_Y)/4, the removed complete root norm
is <=sqrt(G_Y)/4, since sum_(k>=Y+1)k^-2<=1/Y. This statement
uses the actual coefficients, without an unknown asymptotic constant.
It is an optional removal of a paid source sector, not a new estimate
for the larger roots. They retain every signed square-shell term.

## 5. Adaptive original core cutoff and the honest consumer floor

Use the actual old-energy budget of #1002 at its pin in `SOURCES.md`:

    G_Y=Y^a(1+F_Y)^p, a>=0,1<=p<2,
    S_Y=min(Y^2,floor(G_Y/[2304 H_Y^2 H_(Y^2)^6])).            (12)

The removed ORIGINAL small-core amplitude has root at most sqrt(G_Y)/4.
Apply (3) to the actual mask
omega_j(q)=1_(q>floor(K_j^rho),core(q)>S_Y), and call its full
diagonal reference source D_(Y,G). At the source-qualified native
crossings, the exact native comparison gives

    sqrt(F_((Y+1)^2-1)-F_Y)
       <=||D_(Y,G)||_2+sqrt(G_Y)/4
                              +O_epsilon(Y^(1/3+epsilon))+o(1). (13)

A PROVED full-source bound

    ||D_(Y,G)||_2^2<<_epsilon Y^epsilon G_Y                   (14)

on an unbounded crossing subsequence would, by the pinned #848
ALL-PREFIX exponent theorem, imply

    2kappa<=max(a+p kappa,2/3),
    kappa<=max(a/(2-p),1/3),
    every nontrivial zero satisfies
       Re s<=[1+max(a/(2-p),1/3)]/2.                         (15)

The coefficient estimate (14) is OPEN. For the illustrative a=1/3,
p=3/2, the conditional boundary in (15) is 5/6, unchanged by the
square-compression error. With a=0 and any p<2 this alternative
would reach only 2/3, because its error floor remains. RH would
require a genuinely stronger error estimate or the zero-loss balanced
construction; it does not follow from (3).

The value of this alternative is the exact, fully masked, single-index
coefficient array (11), with a tolerable intermediate-error budget.
It is not a claim that changing the source dimension has already
proved its missing signed cancellation estimate.

## 6. Why a fresh high-core projection would invalidate the estimate

If r is squarefree and q|r^2, its squarefree core divides r. Hence
EVERY canonical denominator in R(k/r^2) has core<=r<=Y. When the
original adaptive S_Y exceeds Y, a fresh core>S_Y projection would
annihilate the diagonal source (2). This does NOT imply that the
original high-core source is small. The small error (3) is not stable
under that fresh projection.

There is a quantitative actual-source witness. In the full original
C_Y choose the fixed mask retaining only q=pl for distinct primes
p,l in (Y/2,Y]. Their coefficients are exactly 2/(pl), so the
complete masked amplitude is

    P_Y(k)=sum_(p<l)2/(pl)S_(pl)(k).                          (16)

The already proved witness window and ordinary PNT give
||P_Y||_2>>Y/log(Y)^2. Apply the current square compression to this
legal mask. It gives a full diagonal amplitude D_Y,prime with

    ||P_Y-D_Y,prime||_2<<_epsilon Y^(1/3+epsilon).             (17)

Let Pi retain the canonical q>Q_j, core(q)>S_Y modes, where
Y<S_Y<Y^2/4 for large Y. Then Pi P_Y=P_Y and Pi D_Y,prime=0
EXACTLY. Thus Pi applied to the small deformation in (17) has
root norm >>Y/log(Y)^2. Any source-space stability inequality

    ||Pi E||_2<=K_Y||E||_2

covering these legal deformations would require

    K_Y>>_epsilon Y^(2/3-epsilon)/log(Y)^2.                   (18)

If a deformation had zero physical norm, no such finite stability
constant would exist at all; (18) is the necessary lower bound when
one exists. This concerns the source's exact canonical expansion,
not an assumed orthogonal projection of its finitely many output
values. The high-core and low-core sources can be very close on
the native window even though their canonical supports are disjoint.
The FULL diagonal kernel in (2), including all of its low-core modes,
must therefore remain in the genuine completion target (14).
