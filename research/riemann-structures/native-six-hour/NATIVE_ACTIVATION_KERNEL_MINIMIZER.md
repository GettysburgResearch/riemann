# The original kernel selects a nonuniform native activation path

Status: exact source reduction and interval-certified finite variational result;
final producer/test replay pending. The three prime sets were fixed in
ACTIVATION_KERNEL_PREREGISTRATION.md before the first parent-run discovery.

The primary conclusion is about genuine primewise deformations of the
L-102707 primitive. For primes 3,5,7, the uniform path does not minimize the
positive ratio energy measured with the original K_L kernel. The source
endpoint and its signed Hankel current are unchanged by the improved path.
This is not a claim about the post-renewal amplified principal moment.

## 1. The optimization variable comes from the source

Fix K=p_1 p_2 p_3, and let u_j(s) be nondecreasing primewise schedules from
zero to one. The full chain-rule derivative, with the actual measure 2 ds,
gives activation numbers

\[
 q_j=\int_0^1u'_j(s)\prod_{i\ne j}u_i(s)ds,\qquad
 q_j\ge0,\quad \sum_jq_j=1.
 \tag{1}
\]

For a left prime subset S, the complete factor coefficient is
v(S)=2(-1/2)^3 sum_(j in S) q_j. All eight factor allocations are retained,
including the root-free left unit and the native right unit. With

\[
 C(t)=\prod_j\cos(t\log p_j),\qquad
 S_j(t)=\sin(t\log p_j)\prod_{i\ne j}\cos(t\log p_i),
\]

the physical ratio field is exactly

\[
 F_q(t)=-K^{-1/2}\left(C(t)+i\sum_jq_jS_j(t)\right).              \tag{2}
\]

Every point of the simplex is realizable. In its interior choose
u_j(s)=s^(c q_j), with c large enough that every exponent is at least one.
For rational q, positive integer exponents suffice. On a face, first
activate the zero-q primes while at least one positive-q coordinate remains
zero, then use the power path on the positive coordinates. The first stage
contributes no activation mass. These are actual paths with their chain rule,
not an arbitrary coefficient substitution or a probability measure on s.

The mean-only field is not such a path: its coefficient at the left unit
would be (-1/2)^3 instead of zero. The root-free boundary enforces sum q=1,
so the odd field cannot simply be discarded within this source family.

## 2. The exact original-kernel Gram matrix

Freeze L-102880, and set kappa(u)=K_L(exp u),
nu=|kappahat(t)|^2dt/(2pi). The real kernel has the three literal pieces

\[
 K_L(y)=\begin{cases}
 8-4\sqrt y,&1\le y<2,\\
 -8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
 8\sqrt2-2\sqrt y,&4\le y<8.
 \end{cases}                                                     \tag{3}
\]

It is zero elsewhere. The even autocorrelation is
Gamma(v)=int kappa(u)kappa(u-v)du. Plancherel gives its exact role as the
Gram entry between two exponential modes. Since nu is even, C is orthogonal
to every S_j. Define

\[
 M=\int C^2d\nu,\qquad G_{ij}=\int S_iS_jd\nu.
\]

Then the complete physical energy is

\[
 E(q)=\|F_q\|^2=K^{-1}(M+q^TGq).                                \tag{4}
\]

The factor 1/K is retained throughout; displayed scout energies and energy
differences were multiplied by K.

There is an exact finite formula. For signs epsilon in {+1,-1}^3 put
n_epsilon=prod_(epsilon_j=1)p_j. Then

\[
 G_{ij}=\frac1{64}\sum_{\epsilon,\delta}
 \epsilon_i\delta_j\,
 \Gamma\left(2\log\frac{n_\epsilon}{n_\delta}\right),\qquad
 M=\frac1{64}\sum_{\epsilon,\delta}
 \Gamma\left(2\log\frac{n_\epsilon}{n_\delta}\right).             \tag{5}
\]

No field, diagonal or factor allocation is omitted from these sums.

For rational r>=1, Gamma(log r) is obtained by intersecting the nine pairs
of intervals in (3). On [L,H], if the two pieces are a+b sqrt(y) and
c+d sqrt(y/r), the integral is

\[
 ac\log(H/L)+2(ad/\sqrt r+bc)(\sqrt H-\sqrt L)
                   +(bd/\sqrt r)(H-L).                          \tag{6}
\]

In (5), r is a rational square. Thus every entry belongs to the real span
of Q(sqrt2) and Q(sqrt2) times logarithms of positive rationals. Independent
closed-form checks are

\[
 \Gamma(0)=(384+128\sqrt2)\log2-288,\qquad
 \Gamma(\log4)=64\sqrt2\log2-48.                                 \tag{7}
\]

The latter uses just y in [4,8], hence only the first and third kernel
pieces. Correlations vanish when |v|>=log8, including the support endpoint.

## 3. AK-1: strict convexity and the unique source activation

The three odd functions are linearly independent. If sum_j a_jS_j vanishes,
its exponential coefficients are proportional to sum_j a_j epsilon_j for
each epsilon. Unique factorization makes the eight exponential frequencies
distinct, and the sign characters are independent, so every a_j=0.
A nonzero finite exponential polynomial cannot vanish on a set of positive
Lebesgue measure. Since nu is nonzero and absolutely continuous, G is positive
definite. Consequently (4) has a unique minimizing activation vector on the
simplex, though generally many paths realize that vector.

When the following vector is positive, it is the unique simplex minimizer:

\[
 q_* =\frac{\operatorname{adj}(G)\mathbf1}
               {\mathbf1^T\operatorname{adj}(G)\mathbf1},\qquad
 q_*^TGq_* =\frac{\det G}{\mathbf1^T\operatorname{adj}(G)\mathbf1}.
 \tag{8}
\]

This is the exact definition of the reported minimizers; decimal values are
only a readable rendering. The interval replay verifies interior positivity
and hence all KKT conditions. It never treats an exterior stationary point
as a source minimum.

## 4. AK-2: a nonuniform minimizer and a short explicit improved path

For the preregistered primary set (3,5,7), the exact matrix has the approximate
display

\[
 G\simeq\begin{pmatrix}
 10.011276&-2.197720&0.911536\\
 -2.197720&18.785049&-3.475351\\
 0.911536&-3.475351&14.076042
 \end{pmatrix},\qquad M\simeq8.193660.
\]

Certified rational enclosures of (8) imply

\[
 .3992<q_{*,3}<.3993,\quad
 .2960<q_{*,5}<.2961,\quad
 .3047<q_{*,7}<.3048.                                             \tag{9}
\]

The uniform gradient components are unequal, so the uniform activation is
not stationary. The initially discovered integer powers were (399,296,305).
After that discovery, the simpler path

\[
 u_3(s)=s^4,\qquad u_5(s)=s^3,\qquad u_7(s)=s^3                 \tag{10}
\]

was selected for an additional exact test. Its activation is (2/5,3/10,3/10),
and the replay certifies

\[
 E(1/3,1/3,1/3)-E(2/5,3/10,3/10)>\frac{2}{25K}
                                      =\frac2{2625}.             \tag{11}
\]

Both paths have precisely the same source endpoint and signed product/Hankel
current. Equation (11) concerns their full eight-factor ratio fields in the
original nu, without a different metric or a chosen subset of allocations.
The absolute improvement is small, as its physical normalization shows.

The independent crowded control (2,3,5) also has an interior nonuniform
activation, enclosed respectively by (.3959,.3961), (.2904,.2906),
(.3135,.3136). The same exponent pattern (4,3,3), assigned in that listed
prime order, improves the uniform energy by more than 9/(100K). These are
two distinct primewise schedules on two declared three-prime models; no
single global schedule optimizing both overlapping panels is asserted.

For the separated control (3,11,101), every nonzero frequency difference
exceeds log8. Therefore G=Gamma(0)I/8 and M=Gamma(0)/8 exactly. Its minimizing
activation is uniform, as predicted before the run. Thus nonuniformity is a
property of the actual kernel correlations in the crowded models, rather
than an artifact of the source parameterization.

## 5. The certificate uses rational inequalities

For a positive rational x, binary range reduction puts its logarithm in
[1,2]. With z=(x-1)/(x+1), the producer uses

\[
 \log x=2\sum_{j=0}^{n-1}\frac{z^{2j+1}}{2j+1}+R_n,
 \quad 0\le R_n\le
 \frac{2z^{2n+1}}{(2n+1)(1-z^2)}.                                \tag{12}
\]

There are 48 terms and |z|<=1/3 after reduction. An integer-square-root
bracket with denominator 10^40 encloses sqrt2. Every arithmetic operation,
determinant, cofactor, probability bound and energy comparison is then
performed using rational intervals. The full exact expressions and interval
endpoints are preserved in the fixture. Floating-point values only display
the discovery and suggest candidate integer powers; they are not an
acceptance condition for any theorem.

The source locks include the actual K_L formula and L-102707 primitive. The
tests check independent anchors (7), the support boundary and symmetry,
all eight factor modes, exact native activation coefficients, positive
definiteness certificates, the separated control, and hostile numeric types.

The result is a finite source-owned variational theorem. It neither chooses
new weights independently in different tuples of a full source nor supplies
the missing post-renewal decoder. The next test is one common schedule on a
complete finite product horizon, retaining cross-product interference.
