# The source-metric tangent quotient and its nonlinear boundary

This packet uses the complete original finite source with primes2,3,5,
physical horizon25 and all63 ordered factor pairs. It identifies its
two-dimensional tangent quotient in the actual Mellin norm, then compares
shared monotone paths in that norm. It also gives an exact source record
showing why the tangent augmentation is not a nonlinear affine quotient.
Every derivative site, physical inverse square root and cross-product
interference term remains present. No identification with the complete
post-renewal gamma or a conductor-weighted principal moment is claimed.

The primitive and kernel are L-102707 and L-102880 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`. Their full finite source
implementation was frozen at `5d7ea752ee84765a7690bdc36bb2bbcaddb38bb4`.
The earlier global variation certificate is
`7ff5ddbb8f35055085faca7d46fdddb0f12715ae`. These are source inputs,
not newly inferred complete-family identities.

## 1. Complete finite source and its original observed metric

For p in{2,3,5}, let

    u_p(s)=s+epsilon_p eta(s), eta(s)=s(1-s), |epsilon_p|<=1.

The derivative `1+epsilon_p(1-2s)` is nonnegative. Insert these actual
coordinates into

    Lambda_u=product_p[u_p sqrt(1-x_p)+(1-u_p)sqrt(1-x_p^2)].

For every n,m with nm<=25 and prime support in{2,3,5}, retain

\[
 c_{n,m}(\epsilon)=\int_0^1
    [x^n]\frac{d\Lambda_u}{ds}\ [y^m]\Lambda_u\,2\,ds,
 \qquad
 F_\epsilon(t)=\sum_{n,m}\frac{c_{n,m}(\epsilon)}{\sqrt{nm}}
                       e^{it\log(n/m)}.\tag{1}
\]

Here `[x^n]` means the coefficient with the prime exponents of n, not
the degree-n coefficient of one variable. There are63 ordered pairs and45
physical ratios. The empty left derivative contributes zero and is still
included. The norm is the original
`||F||_nu^2=integral |F(t)|^2 |kappahat(t)|^2 dt/(2pi)`.
Its cross terms are the native autocorrelation
`Gamma(log(n/m)-log(n'/m'))`. Equal physical ratios are coalesced only
after retaining the literal coefficient and site records.

Let B_p be the derivative of F at epsilon=0 in coordinate p. The actual
common-time variation satisfies

\[
 B_2+B_3+B_5=0.\tag{2}
\]

At source level, a common variation has `delta Lambda=eta dot Lambda`.
The variation of `2 dot Lambda tensor Lambda` is
`2 d_s(eta dot Lambda tensor Lambda)`. Its integral vanishes because
eta is zero at both endpoints. The physical readout is independent of s,
so (2) holds before and after it.

## 2. Two literal physical coefficients prove the exact rank

The actual record(n,m)=(2,6) contains

\[
 c_{2,6}=-\frac14\int_0^1 u_2u_3\,du_2
        =-\frac1{12}
         -\frac{(\epsilon_3-\epsilon_2)(5+\epsilon_2)}{240}.
 \tag{3}
\]

To check the polynomial, write a=epsilon2,b=epsilon3. Direct integration
gives

    integral u2*u3*du2 = 1/3+(b-a)/12+a(b-a)/60.

The cubic term is zero since `integral eta^2 eta'=0`. The factor-1/4
in (3) follows from the literal half-source coefficients
`[x_2]Lambda=-u2/2`, `[y_2 y_3]Lambda=u2*u3/4`, and the actual2ds.

The only pairs at ratio1/3 under this horizon are(1,3) and(2,6).
The former has a zero left derivative. Consequently the physical ratio1/3
coefficient of `sum_p d_p B_p` is exactly

\[
 \frac{d_2-d_3}{48\sqrt{12}}.\tag{4}
\]

Likewise ratio1/5 is detected by(2,10), after the root-free(1,5), and has
coefficient `(d2-d5)/(48 sqrt20)`. No additional same-ratio record fits
inside the horizon.

The native measure has nonzero absolutely continuous density away from
isolated Fourier zeros. A finite exponential polynomial of distinct
physical ratios cannot vanish in that norm unless all coefficients
vanish. Thus (4) and its ratio1/5 counterpart force d2=d3=d5. Together
with (2), this proves the exact physical tangent kernel and rank:

\[
 \ker(d\mapsto\textstyle\sum_p d_pB_p)=\mathbb R(1,1,1),
 \qquad\operatorname{rank}=2.\tag{5}
\]

The mean-removal operator `P=I-(1/3)11^T` therefore satisfies `B P=B`.
It is a source-parameter projector for this derivative. It is not being
identified with a Boolean coefficient projector, a quadratic-residue
augmentation, or an orthogonal projector on an arbitrary physical field.

## 3. The actual source-metric descent direction

Use parameter coordinates epsilon=(a,b,-a-b), with tangent basis
`V1=B2-B5,V2=B3-B5`. Define

\[
 M_{ij}=\operatorname{Re}\langle V_i,V_j\rangle_\nu,
 \qquad g_i=2\operatorname{Re}\langle F_0,V_i\rangle_\nu.\tag{6}
\]

Equation (5) makes M positive definite. For a unit tangent in this actual
metric, the unique steepest descent direction is

\[
 d_*=-\frac{M^{-1}g}{\sqrt{g^TM^{-1}g}},\tag{7}
\]

provided g is nonzero, with first variation
`-sqrt(g^T M^{-1}g)`. This is Cauchy--Schwarz in the positive metric M.
The substance of the construction is that M and g come from the complete
physical source in (1), including cross-product interference, rather
than an unweighted coefficient metric.

The finite scout evaluates the exact radical/logarithm expressions for
M and g, certifies a positive determinant, and uses the declared rational
rounding rule on `-adj(M)g`. It checks that the resulting direction still
has strictly negative original first variation. This rational direction
and the fixed hexagon controls yield actual monotone paths, not just
unrealized formal tangents. Their finite energies are evaluated directly
from (1); first-order descent alone is not used to assert a finite gain.

## 4. A nonlinear affine quotient fails in the same actual source

When all epsilon_p are one common constant c, the path is simply the
common reparameterization `s -> s+c eta(s)`. The complete integrated
current in (1) is unchanged, including endpoint cases c=+-1.

It does not follow that arbitrary parameter triples differing by c1
have the same current. Formula (3) gives the exact change

\[
 c_{2,6}(\epsilon+c1)-c_{2,6}(\epsilon)
       =-\frac{c(\epsilon_3-\epsilon_2)}{240}.\tag{8}
\]

Take epsilon=(1/2,0,-1/2) and c=1/4. Both triples are admissible,
and their literal coefficient difference is1/1920. By the unique
nonzero ratio1/3 record, their complete physically coalesced current
difference has coefficient

\[
 \frac1{1920\sqrt{12}}=\frac1{3840\sqrt3}\ne0.\tag{9}
\]

Thus it also has nonzero original Mellin norm. This is not cancellation
hidden by a changed diagonal: the same complete63-record readout was
used on both sides. The map `epsilon -> P epsilon` is not a nonlinear
current quotient, even though it is the exact quotient of the tangent
map at zero.

The reason is explicit. A true common reparameterization of already
different schedules is `u_p(s) -> u_p(v(s))`; its variation is
`delta u_p=eta u_p'`. Adding c eta to every schedule instead uses
`delta u_p=eta`, which agrees only at the common baseline. The missing
mixed source term is measured by (8).

## 5. Replay and remaining boundaries

The declared experiment is frozen at
`b3a8a85021cedefae034aaef7c14a6976429142b`. Its simple joint path

    u2=2s-s^2, u3=s, u5=s^2

improves the original energy by more than6.16 over the baseline and by
more than2.74 over the best frozen one-coordinate path. The respective
rounded gains are6.166962 and2.747716. These comparisons use every one
of the63 original ordered records and all cross-product terms.

The declared metric rounding rule selects
`epsilon=(69/125,56/125,-1)`. Its first variation is less than-5.84,
and its finite energy improves on the best frozen one-coordinate path
by more than1.70. The simple hexagon vertex gives the better finite gain;
the metric direction solves an infinitesimal unit-metric problem and is
not claimed to optimize a finite coordinate step. Every worse path from
the fixed panel is retained in the discovery and final replay.

The preregistered experiment retains all fixed paths, including any that
raise the energy. It keeps four distinct diagonal resolutions: primitive
2ds site squares, integrated site squares, integrated pair squares, and
physical ratio-coalesced squares. The observation still uses the full
Gram form; no one of these diagonals is substituted for it or declared
equal to the native T106140 Wick ledger.

This yields a positive, original-metric tangent quotient and a precise
nonlinear projector obstruction in one explicit native finite source.
It does not prove global optimality among all monotone schedules,
identify the all-path curvature span, or control the full retained-gamma
family. The separate curvature-span investigation addresses a different
question from the rank of this two-dimensional tangent.
