# A coherent native inverse decomposition and a smaller short-product mean

Status: **proposed source-dependent component theorem**, with a complete
proof below and independent review requested. The estimate applies to an
actual piece of the native Möbius inverse at the detector lengths. It
does not estimate the entire inverse or prove a new zero-free region.

The new positive conclusion is

\[
 \boxed{\quad
 I_R(U,D;Q)\ll (UDNQ)^\epsilon(1+|t|)^A p_J(V)^2
       \frac{UR}{D}\{U+R+(UR)^{2/3}\}.
 \quad}                                                     \tag{1}
\]

Here R is the product of the two short Möbius factors in the exact
ordinary Heath--Brown identity, not a replacement column length. All
sixth-power-free physical rows, including nonsquarefree rows, occur.
Every original character zero and a common growing puncture Q remain.
For the complete contribution with outer product at most sqrt(U), (1)
gives

\[
 \boxed{\quad I_{\rm short}(U,D;Q)
       \ll (UDNQ)^\epsilon(1+|t|)^A p_J(V)^2 U^{5/2}/D.\quad}  \tag{2}
\]

At D=U^(7/5), this is U^(11/10+epsilon), compared with the inherited
full-inverse resource U^(4/3+epsilon). This is a genuine estimate for
the short-product contribution. The complementary product range
R>sqrt(U) remains in the exact identity and is not discarded.

## 1. Pinned premises and conventions

The arithmetic source is `openai/math`, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, file
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Git blob `268c4e3206d460c617d3d2129742a72b831b3def`.
The proof imports its squarefree sextic large sieve, ordinary Hecke
functional equation, primary-ideal conventions, ideal counting, and
fixed-seminorm smooth calculus. No zero-free premise is used in (1)--(2).

The precise full-column sieve needed here is equation (6) of
`standalone/2026-10-23-structured-moment-gains/fifth-pass/SEXTIC_ROW_PHASE_CANCELLATION.md`,
at PR1020 commit
`c690f96fe6876f945398b3e2779810c563a64743`, Git blob
`3a5d7adcc24ec8907be5c8fd6879d81736d44788`. It states, for squarefree
rows w, unrestricted columns r, and a common divisor-bounded sequence,

\[
 \sum_{Nw\asymp A}^{\rm sf}
   \left|\sum_{Nr\asymp R}b_r\chi_r(w)^{\pm1}\right|^2
 \ll (AR)^\epsilon R\{A+R+(AR)^{2/3}\}.                     \tag{3}
\]

This is the divisor-bounded full-column consequence proved there,
not an assertion of a stronger arbitrary-coefficient operator norm.
Its proof splits the column into its squarefree and powerful parts
and uses Minkowski with the actual powerful-ideal count. The bound
remains uniform under common coefficient masks and bounded row
restrictions. Those are exactly its uses below.

For fixed angular type the ordinary functional equation was also read
directly in `openai/math` at the same commit, file
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex`,
Git blob `e93fbddf626ab532b7e8fbfac830f1b45370b0e3`, specifically
`lem:angular-hecke`, `eq:angular-hecke-fe`, and the smooth-duality
subsection. Only the ordinary primitive equation and its common-test
calculus are used. No cubic exceptional-moment or cubic metaplectic
equation is transferred to the sextic family.

Work over E=Q(omega), with primary ideal representatives outside the
same fixed omitted set S. The set S contains the primes above 6 and
the conductor of the fixed finite ray data. For a physical row u, put

\[
 \psi_u(n)=\nu(n)\chi_n(u)^{\varsigma}1_{(n,Q)=1},
 \qquad \varsigma\in\{1,-1\}.                              \tag{4}
\]

All powers in (4) are evaluated on units and then extended by zero.
The finite ray character, orientation, and any fixed angular order
are fixed before taking the mean. A common norm height is placed in
the profile. Bounded common row restrictions and a fixed finite
family of presentations are permitted.

Rows have Nu comparable to U and are sixth-power-free as ideals.
The theorem below concerns their nonprincipal inducing characters.
With the fixed finite-order data and good rows, all sufficiently large
U have this property: an exterior prime of a sixth-power-free u has a
nonzero valuation modulo six, so its Kummer ramification cannot be
canceled by the fixed S-supported character. For nonzero angular
order the inducing character is automatically nonprincipal.
No principally induced row is removed from an assertion that included it.
Bounded exceptional principal presentations must be treated on the
complete inverse, before this nonprincipal decomposition.

The puncture Q is fixed within each row mean. It may grow polynomially
in UD; more generally the displayed loss (NQ)^epsilon is retained.
No conductor of Q is inserted into the primitive reflection scale.
Its zeros are removed and restored by an exact finite Euler-factor
identity instead.

## 2. An exact full-convolution identity

For y>=1, let m_y(n)=mu(n)1_(Nn<=y), with the same original good-ideal
support. Ordinary Dirichlet convolution satisfies

\[
 \mu=2m_y-m_y*m_y*1\qquad\text{at }Nn\le y^2.                \tag{5}
\]

Indeed, delta_1-m_y*1=(mu-m_y)*1 is supported above y. Its convolution
square vanishes at norm at most y^2. Multiply that square by mu and
expand, using mu*1=delta_1. This proves (5) with no limiting operation.

Take D>=3, y=sqrt(2D), and V supported in (1,2). The 2m_y term is
zero throughout the support. Define

\[
 a_y(r)=\sum_{ab=r\atop Na,Nb\le y}\mu(a)\mu(b),
 \qquad |a_y(r)|\le d_E(r).                                \tag{6}
\]

The ideals a,b are not required to be coprime. In particular r may
have squared prime factors, and those terms are essential to (5).
For a dyadic window eta_R on Nr comparable to R, set

\[
 M_{u,R}=-D^{-1/2}\sum_{r,c}
       a_y(r)\eta_R(Nr)\psi_u(r)\psi_u(c)V(NrNc/D).
                                                               \tag{7}
\]

The windows form one common partition of the actual finite r range
1<=Nr<=2D. Then the exact native inverse is

\[
 M_u(D;V)=D^{-1/2}\sum_n\mu(n)\psi_u(n)V(Nn/D)
                    =\sum_R M_{u,R}.                       \tag{8}
\]

Precisely, for a bounded nonnegative physical row weight w_U supported
on Nu comparable to U, define

\[
 I_R(U,D;Q)=\sum_{u\ {m sixth\!\!\!-free}\atop\psi_u^*\ne1}
                       w_U(u)|M_{u,R}|^2.
\]

Let M_(u,<=R_0) be (7) with eta_R replaced by 1_(Nr<=R_0), and let
I_(<=R_0) be its squared physical row norm with the same weight and
row set. Thus I_short in (2) means I_(<=sqrt(U)), the norm of the
coherent sum, not the sum of the individual dyadic norms. Common
bounded physical row restrictions may be included in w_U.

Every natural zero survives because psi_u is completely multiplicative
with its zero extension. The common profile in (7) is the original V
at the displayed product scale. The entire small-product contribution
may also be defined with the literal cutoff Nr<=R_0; subdividing that
cutoff into dyads leaves (6) divisor-bounded, including its last partial
dyad.

This ordinary identity is useful after the exact twisted Gauss identity
from `second-pass/NATIVE_GAIN.md`: on a coprime genuine column, a second
Gauss transformation sends g(n)mu(c) to mu(r)mu(c)^2 times its fixed
ray/angular factor. The Möbius signs move to the two short factors.
They do not disappear. The full and unitary convolutions agree only on
their coprime squarefree factorizations. Formula (7) is independently
derived from (5); its repeated-prime terms must be kept, rather than
identified term by term with the unitary Gauss decomposition.

## 3. The signed reflected identity, with punctures still present

Let psi_u^* be the primitive inducing Hecke character and q_u its
conductor norm, including the fixed bad-place factor. After a fixed
finite division into bad-place sectors, the redundant zeros of the
original natural presentation outside Q are supported in S. Write
Q_s for the union of these fixed redundant primes and rad(Q).

For every positive C, exact removal of the additional zeros gives

\[
 T_u(C):=C^{-1/2}\sum_c\psi_u(c)V(Nc/C)
   =\sum_{e\mid Q_s}\frac{\mu(e)\psi_u^*(e)}{\sqrt{Ne}}
                        T_u^*(C/Ne).                       \tag{9}
\]

There is no new coprimality condition between the quotient c and e.
The coefficient in (9) is the primitive psi_u^*(e); using the original
zero-extended psi_u(e) at a deleted prime would incorrectly make that
summand zero. If e meets the primitive conductor, its actual coefficient
is zero automatically.

The ordinary functional equation, with the nonprincipal hypothesis
above, gives

\[
 T_u^*(C/Ne)=\varepsilon_u\sqrt{C/(q_uNe)}
       \sum_n\overline{\psi_u^*(n)}
                    \Phi\!\left(\frac{NnC}{q_uNe}\right).
                                                               \tag{10}
\]

Fixed field and archimedean constants are included in q_u or Phi.
Phi is the corresponding common smooth transform. It and the required
Euler derivatives are bounded at zero and rapidly decreasing at
infinity, with a fixed finite-seminorm bound. Placing a common height t
in V costs a fixed polynomial in 1+|t|. Equations (9)--(10) can
equivalently be obtained by ordinary Hecke lattice Poisson summation.
They cross no zeros of an L function: a full L function, not its
reciprocal, is reflected.

Substituting C=D/Nr into (7) gives the exact coherent return

\[
\boxed{
\begin{split}
 M_{u,R}={}&-\varepsilon_u\sqrt{D/q_u}
  \sum_r\frac{a_y(r)\eta_R(Nr)\psi_u(r)}{Nr}
  \sum_{e\mid Q_s}\frac{\mu(e)\psi_u^*(e)}{Ne}\\
 &\hspace{10mm}\times\sum_n\overline{\psi_u^*(n)}
       \Phi\!\left(\frac{NnD}{q_uNrNe}\right).
\end{split}}                                                \tag{11}
\]

The r,e sums are finite. The dual n sum converges absolutely with its
rapid tail. Formula (11) retains a_y(r), hence both original Möbius
signs in (6), the same root number, the original row, and the full
coupled profile. It is not a formula with an independently chosen
test for each row.

## 4. Proof of the component estimate

### 4.1 The actual nonsquarefree physical rows

Split a sixth-power-free row uniquely, after fixing its unit and its
finitely many S-valuations, as

\[
                    u=v w,
\]

where w is squarefree and v is powerful, with (v,w)=1 and every
valuation of v between two and five. Fix v of norm comparable to V_0
and put P=Nrad(v). Then

\[
 A\asymp U/V_0,\qquad Nw\asymp A,\qquad
 P\le V_0^{1/2},\qquad q_u=c_s P Nw\asymp q_v:=AP.           \tag{12}
\]

The equality for the good conductor follows because every positive
good valuation is nonzero modulo six; its tame conductor exponent is
one. The finite constant c_s is fixed in the chosen bad-place sector.
Nonempty row annuli have A bounded below by a fixed positive constant.
The condition (v,w)=1 and every original physical restriction are kept
until a positive row estimate is applied.

### 4.2 Fix a puncture divisor before reflection is estimated

Fix e in (11), write E=Ne, and define its actual nominal dual scale

\[
                         L_0=q_vRE/D.                       \tag{13}
\]

On a dual dyad Nn comparable to L>=1, separate the single smooth
profile in the normalized variables Nw/A, Nr/R, and Nn/L. The factor
sqrt(q_v/q_u) is part of that same smooth profile. The separation uses
one common Fourier/Mellin density. Its required weighted norm is
bounded by a fixed seminorm times

\[
                         (1+L/L_0)^{-J_0}                  \tag{14}
\]

for any prescribed fixed J_0. Height and profile costs are retained.
This is uniform in v,e; only their displayed scales have changed.

For a fixed dual n and a fixed separation mode, its row multiplier
overline(psi_u^*(n)), the root number, and psi_u^*(e) have modulus at
most one. The r polynomial has common coefficients
a_y(r) times the fixed v-phase, the original zero masks, fixed ray
data, and a unit norm twist. They are divisor-bounded uniformly in n
and w. Thus (3), in the actual residual row annulus A, bounds its row
norm by

\[
 (AR)^\epsilon
       \{R[A+R+(AR)^{2/3}]\}^{1/2}.                         \tag{15}
\]

Every prime of v stays as an original zero in this common coefficient.
The remaining w-zero is precisely that of the sextic sieve kernel.
No arbitrary pair-dependent mask is introduced into that kernel.

Ideal counting gives O(L) possible n in a dyad. Minkowski over those
actual n, followed by the convergent dyadic tail, uses the elementary
bound

\[
 \sum_{L\ge1}^{\rm dyadic}L(1+L/L_0)^{-J_0}\ll L_0
               \qquad(L_0>0,\ J_0>1).                      \tag{16}
\]

For L_0<1 the left side is O(L_0^J_0)<=O(L_0). Thus no empty short
dual range is replaced by a constant row or column count.

The complete norm of the fixed-e term in (11) is consequently at most

\[
\begin{split}
 &(UDNQ)^\epsilon(1+|t|)^{A_1}p_{J_1}(V)
 \frac{\sqrt{D/q_v}}{RE}\,L_0
       \{R[A+R+(AR)^{2/3}]\}^{1/2}\\
 &\qquad=(UDNQ)^\epsilon(1+|t|)^{A_1}p_{J_1}(V)
       \left\{\frac{q_vR}{D}
                       [A+R+(AR)^{2/3}]\right\}^{1/2}.
\end{split}                                                 \tag{17}
\]

In particular **E cancels exactly** from this bound. Summing over the
actual finite divisors e costs only tau(Q_s), which is at most
(NQ)^epsilon after the preliminary losses are chosen. This proves
the fixed-v squared bound

\[
 I_{R,v}\ll(UDNQ)^\epsilon(1+|t|)^A p_J(V)^2
       \frac{APR}{D}\{A+R+(AR)^{2/3}\}.                    \tag{18}
\]

The primitive dual n may meet S. This is harmless: it was estimated
as a bounded row multiplier and counted as an ideal, not incorrectly
placed into a good squarefree-column sieve.

### 4.3 Sum all powerful physical parts

There are O_epsilon(V_0^(1/2+epsilon)) powerful ideals in a V_0 dyad.
Together with P<=sqrt(V_0), this gives
sum_(Nv comparable V_0) P << V_0^(1+epsilon).
Substitute A comparable to U/V_0 into (18) and sum over that dyad.
The three resulting costs are

\[
 (UDNQ)^\epsilon\left\{
 \frac{U^2R}{DV_0}
 +\frac{UR^2}{D}
 +\frac{U^{5/3}R^{5/3}}{DV_0^{2/3}}\right\}.               \tag{19}
\]

The first and third sums over dyadic V_0 converge; the second costs
only a logarithm. Units and the fixed S-valuations have already been
split into finitely many sectors. This proves (1), including every
nonsquarefree sixth-power-free row.

All small powers in (3), ideal counting, divisor bounds, and common
profile separation are chosen before the final epsilon. The orders
J,A depend only on that epsilon, the fixed arithmetic data, and the
fixed bounded length range. They do not depend on u,v,e,Q, or on a
row-selected coefficient sequence.

## 5. Native length consequence and the exact remaining range

For R<=sqrt(U), both R and (UR)^(2/3) are at most U. Hence

\[
                         I_R\ll U^2R/D                    \tag{20}
\]

with the same small-power, height and seminorm factors. Sum the row
norms over dyadic R<=R_0<=sqrt(U); their geometric sqrt(R) growth is
dominated by the last range. Therefore

\[
             I_{\le R_0}\ll U^2R_0/D.                     \tag{21}
\]

This proves (2). At D=U^r its exponent is 5/2-r. It is strictly below
the inherited full-inverse exponent (1+5r)/6 whenever r>14/11.
For example:

| Native r | New exponent for R<=sqrt(U) | Inherited full exponent |
| --- | --- | --- |
| 13/10 | 6/5 | 5/4 |
| 7/5 | 11/10 | 4/3 |
| 10/7 | 15/14 | 19/14 |

These compare a proved component with the full resource. They are
not a replacement for the full-resource exponent in the detector.
For the natural shorter cutoff R_0=D/U<=sqrt(U), (21) is just U.
The range D/U<R<=sqrt(U), which is present when 1<r<3/2, is included
with its displayed nonvolume cost rather than being dismissed as
an empty Type I range.

A shorter cutoff supplies an actual component gain at the current
global critical length as well. Taking R_0=U^(1/4) in (21) gives
the exponent 9/4-r, whose saving over (1+5r)/6 is exactly

\[
                         (22r-25)/12.                     \tag{21a}
\]

It is positive for every r>25/22. The source critical class and its
detector crossing, defined in Liu's
[Lemma 14.9 and Proposition 2.7](https://arxiv.org/html/2610.26835v1)
and evaluated in `SHORT_INVERSE.md`, Section 5, have
r=t_c=1.1639535765090109563... . At that length the component exponent
is 1.0860464234909890437..., with saving 0.0505815569331867532...
over the inherited full resource. The `fractional_native` reviewer
pointed out this specialization. It uses no new analytic premise in
(1); only the identification of the source's critical length is
imported. Its complementary range is R>U^(1/4), so it is still not
a full critical-class improvement.

The remaining coherent sum is exactly (11) with Nr>sqrt(U). Its
coefficient is the two-sign sum (6), with the original product profile.
Applying (1) all the way to R comparable to D does not improve the
full inverse. There is no subtraction of component upper bounds from
a total upper bound here.

## 6. The actual signed first-Poisson diagonal

There are two separate cancellations, which should not be conflated.

First, the complete first-Poisson frequency sum runs over the full
Eisenstein lattice k, with the factor e_0(k/3). Every good prime in a
column or a natural coprimality mask is prime to 3. For a good ideal P,
CRT gives

\[
 \sum_{k\bmod 3P} e_0(k/3)1_{(k,P)=1}=0.                  \tag{22}
\]

The additive character on O/3O is nontrivial. Multiplication by any
good primary divisor preserves this fact. Thus the complete local
diagonal class sum vanishes, including the actual coprimality mask.
It does not vanish after an arbitrary restriction to one k residue
class; in particular one may not retain only primary k and still use
(22).

For a smooth lattice weight at norm scale K, expand its coprimality
mask by divisors of P and apply lattice Poisson. All resulting shifted
frequencies stay a fixed distance from zero after the mod-3 scaling.
For every fixed J one obtains, for K>=NP,

\[
 \left|\sum_k e_0(k/3)W(k/\sqrt K)1_{(k,P)=1}\right|
 \ll_J \tau(P)(K/NP)^{-J}.                               \tag{23}
\]

One chooses the Schwartz decay order larger than J+1 to absorb the
Jacobian. With the complete effective column of norm comparable to
D, its diagonal mask radical has norm O(D), so (23) makes that
fixed-block diagonal rapidly small when K exceeds D by a fixed power.
This statement preserves the full class sum and all masks.

Second, before coprimality inversion the genuine first-Poisson pair
has coprime residual columns p_1,p_2 and excludes the pair (1,1).
Consequently it has no equal-column pair. The later l expansion adds
such pairs only formally. Summing the complete signed l divisor sum
restores exactly

\[
               \sum_{l\mid(p_1,p_2)}\mu(l)
                        =1_{(p_1,p_2)=1}.                  \tag{24}
\]

Thus all artificial equal-column pairs other than the separately
subtracted unit pair cancel algebraically. This is true with their
full outside coefficients and kernel **on one common formal extension,
with the complete l inversion undone before any l-dependent scale
truncation or separated absolute integral**. The formal extension is
only required to agree with the genuine expression on the coprime
locus; its other values cancel in the complete divisor sum. This is
not an estimate obtained by subtracting an upper bound for a diagonal.
If such a formal extension was introduced inside a previously positive
majorant, undoing its inversion returns that same majorant's expression,
not the original signed native block. In particular the source's
second transformed positive-majorant identity cannot be promoted to
a signed identity for the original block by this observation.

Neither (22) nor (24) controls cross terms between different outer
Heath--Brown factors. In particular a centered estimate for each
individual factor is not a Hilbert norm to which Minkowski can be
applied. The improved component (1) uses the full coherent identity
(11), not that invalid step.

## 7. The unbalanced coefficient-interval attempt

For squarefree columns of norm comparable to B, let

\[
 P(z)_k=B^{-1/2}\sum_n\mu(n)\gamma_2(n)\theta(n)
                   z^{\omega(n)}\chi_n(k)V(Nn/B).          \tag{25}
\]

The value z=-1 has the missing coefficient gamma_2. The degree is
at most m(B)=O(log B/log log B): order distinct prime ideals by norm,
use ideal counting to get q_j>=c j, and then
B>=c^m m! for the product of m distinct primes.

This small degree gives a useful precise interpolation fact. If a
uniform bound holds on any fixed real interval [a,a+delta], delta>0,
then its value at any fixed z_0 has at most exp(O_delta(m(B))) extra
cost. Indeed, use the m+1 equally spaced nodes in the interval. The
denominator of the j-th Lagrange coefficient is
(delta/m)^m j!(m-j)!; bounding its numerator by a fixed constant to
the power m and summing gives at most C_delta^m, by m!>=(m/e)^m.
The same argument holds for a Hilbert-space valued polynomial.

For a signed or centered quadratic form of (25), with all outside
coefficients fixed, its restriction to real z is a polynomial of
degree at most 2m(B). Scalar interpolation applies to that exact
signed polynomial as well. Thus a constant-width interval theorem
for the **complete signed return** would transfer to z=-1 with only
B^o(1) loss. A theorem at the single point z=1 supplies no such
interval.

After the known Gauss cancellation, the coefficient at general z is
mu(n)^2 z^omega(n). Its ordinary Dirichlet series has the form

\[
                 L(s,\psi)^z H_z(s,\psi),                  \tag{26}
\]

where the Euler correction is absolutely convergent for Re(s)>1/2
on compact z sets away from the finitely treated small local factors.
For nonintegral z, zeros of L create branch cuts. Even for positive
z near one, these are not poles, but their Hankel contributions cannot
be silently omitted during reflection. Their coefficient vanishes
at z=1; a fixed small |z-1| is not a saving by a power of B.

For the finite-order ordinary orientation of the scalar native case,
the actual unit-divisor Poisson block of the Gauss moment at
A=K=D^2/U, B=D has ordinary row length B^2/A=U. Thus the available
buffered zero-cut budget is

\[
                  U^{\max_a\{R(a)+r(2a-1)\}+\epsilon},
                   \qquad D=U^r.                          \tag{27a}
\]

The Gauss-moment prefactor A/B=D/U and the outer signed-return
prefactor U/D cancel. They do not change (27a) into a budget at the
larger row scale K. This reproduces the already available capped
envelope. At r=7/5 its endpoint value is 187/140, exceeding the
inherited 4/3 by 1/420; its first contact with that inherited line
is r=10/7.

I also tested the more optimistic one-level budget that would result
from an ordinary sum at row A=K and column B=D. It is not a licensed
substitution for the actual row U in (27a). Put
s=log B/log A=r/(2r-1). For 1<=r<=10/7, one has 10/13<=s<=1.
That budget's individual zero contribution has candidate exponent

\[
 R(a)+s(2a-1),\qquad
 R(a)=\frac{31-32a}{21-12a},\qquad a\le7/8.                 \tag{27}
\]

This is a budget calculation, not a proof of a new branch-cut theorem.
Even that budget does not reach row-volume exponent one. Its interior
maximum is

\[
        \frac83+\frac52s-\frac{10}{\sqrt6}\sqrt{s}.         \tag{28}
\]

At r=7/5, s=7/9, (28) is approximately 1.01069961199; the fixed
0.51 floor also costs 1+s/50 approximately 1.01555555556. At r=10/7,
s=10/13, these are approximately 1.00916921955 and 1.01538461538.
Thus even these optimistic positive zero-cut bounds do not reach
row volume at the larger unbalanced row scale. The actual signed
return still has the unit-block budget (27a).
To bound the signed polynomial one would additionally have to retain
coherence among those zero contributions and the complete frequency
kernel. No such estimate has been obtained here.

This is not an impossibility claim for the interval route. In
particular no lower bound for an arbitrary-coefficient sextic sieve
is being used as a lower bound for the present gamma_2/angular family.
The coefficient orientation and exact signed weight would have to be
verified before any such lower-bound comparison.

For completeness I checked the actual witness in
[Xu--Sang v2, (3.1) and Corollary 4.3](https://arxiv.org/html/2610.17675v2).
On squarefree columns it uses G(n,-m)=gamma_1(n) overline(chi_n(-m)).
Whole-sum conjugation and the pinned Gauss identity turn its coefficient
into

\[
 \overline{\gamma_1(n)}\chi_n(-1)
   =\mu(n)\gamma_2(n)\alpha(n)^{-1}\overline{G(n)}\chi_n(-1).
                                                               \tag{28a}
\]

This is the resonant angular -1 mu gamma_2 class, with its specified
finite-ray sector. Converting their 1/B normalization to the present
1/sqrt(B) makes the lower-bound scale A^(5/6)B^(1/3), precisely the
resonant term of PR1020. It prevents discarding that term uniformly
over the finite-ray family in a positive moment. It is not a lower
bound for the native gamma_2 coefficient missing mu, or for the
complete signed return. A positive A+B interval across every such
resonant ray sector therefore cannot be the proposed continuation
input; the useful interval target must keep the complete signed form.

## 8. A two-sign Stieltjes estimate for the radial reflected kernel

This additional estimate was suggested and its prefactors checked by
the `two_sign_hlc` research agent. Its analytic premise is separate
from (1): assume the pinned all-finite-order Hecke zero-free cap at
beta_0=7/8, with the reciprocal growth consequence on every fixed
line to its right. Fix beta>beta_0. This paragraph does not assert an
extension of that cap to nonzero angular types.

For the finite-order presentations, the cap supplies the uniform
prefix estimate

\[
 \left|\sum_{Na\le X}\mu(a)\psi_u(a)\right|
          \ll (UNQX)^\epsilon X^\beta.                     \tag{29}
\]

One way to obtain its needed scope is the Euler-log and
three-circles argument of `second-pass/CAPPED_NATIVE_MOMENT.md`, now
on the globally zero-free strip Re(s)>beta_0, followed by finite
Perron inversion. On Re(s)>=beta the primitive reciprocal is bounded
by (q_u(3+|t|))^epsilon; the natural deleted Euler factors cost
(NQ)^epsilon. Choose the Perron height as a fixed sufficiently large
power of UX and choose its preliminary epsilon afterwards. Taking
a half-integer between successive integer norms bounds the truncation
error using the ordinary ideal-divisor count. This proves (29) for
sharp prefixes, with every natural zero retained. It imports the
cap rather than proving it.

Dyadically separate the two factors a,b in (6), with Na comparable
to A_1, Nb comparable to B_1 and R=A_1 B_1. Their actual upper
endpoints Na,Nb<=y remain. For fixed dual n and e, the dependence
on a,b in (11) is radial through

\[
 \frac{\eta_R(NaNb)}{NaNb}
     \Phi\!\left(\frac{NnD}{q_uNaNbNe}\right).              \tag{30}
\]

Each mixed Stieltjes derivative of (30) is bounded by
R^(-1) A_1^(-i) B_1^(-j), i,j in {0,1}, times a fixed finite sum
of Euler derivatives of the same Phi. Sharp endpoints contribute
the corresponding controlled boundary terms. Apply (29) on both
variables before taking the row norm. Their two signed prefix factors
contribute R^beta; the normalized product kernel contributes R^(-1).

In a conductor dyad q_u comparable to q, the ordinary full-character
mean from PR1020 Section 3, with principally induced rows removed,
bounds the normalized dual plain polynomial by U^(1/2+epsilon) in
row norm. Its smooth dyadic restoration uses
sum_(L>=1) sqrt(L)(1+L/L_0)^(-J) << sqrt(L_0), including L_0<1.
Here L_0=qRNe/D. Combining this with the exact outside factor
sqrt(D/q)/Ne in (11) gives

\[
 U^{1/2+\epsilon}R^{\beta-1}
  \frac{\sqrt{D/q}}{Ne}\sqrt{qRNe/D}
       =U^{1/2+\epsilon}R^{\beta-1/2}(Ne)^{-1/2}.            \tag{31}
\]

The puncture-divisor mass sum_(e|Q_s)(Ne)^(-1/2) is subpower.
All conductor dyads, a,b dyads, common norm heights, and their finite
derivative orders are priced as before. Hence this route gives

\[
                  I_R\ll (UDNQ)^\epsilon
                             U R^{2\beta-1}.                \tag{32}
\]

This exploits both Möbius signs for the exact radial product kernel.
It is not an application of the rational fixed-shift HLC theorem to
Eisenstein characters. At beta=7/8 with arbitrarily small losses,
(32) improves the old resource only when

\[
        \log_U R<\frac{10}{9}(r-1),\qquad D=U^r.             \tag{33}
\]

At r=7/5, this stops at 4/9, strictly below 1/2, already inside
the stronger short-product result (2). In the larger R range where
(32) beats the generic component estimate (1), it is still above the
inherited full inverse resource. Thus this direct use of the two
signs does not complete the missing Type II estimate.

## 9. The logarithmic prime identity on the genuine physical slots

I checked the actual Q_i definitions in the pinned arithmetic source,
Section `sec:amplitudes`, and the following witness-character matching
paragraph. They are

\[
 Q_i(u;z)=P_i^{-1/2}\sum_{p\in1_T\cap\mathcal P_i(Z)}
       \overline{\chi_p(u)}W_i(Np/P_i)(Np/P_i)^{z-1}.          \tag{34}
\]

For the inverse witness character psi=nu times the same negative
sextic orientation, the relative prime coefficient is

\[
 \overline{\nu(p)}1_{p\in1_T}
   =|T|^{-1}\sum_{\theta\in\widehat T}
                          (\overline\nu\theta)(p).         \tag{35}
\]

The natural zero at p|u is retained. The allowed prime sets and the
independent W_i are part of (34), not disposable notation.

The unrestricted identity mu*Lambda=-mu log N is exact. With one
common multiplicative character psi its Dirichlet series is

\[
 \frac1{L(s,\psi)}\frac{-L'(s,\psi)}{L(s,\psi)}
                           =\left(\frac1{L(s,\psi)}\right)'.
                                                               \tag{36}
\]

After completing a ray term of (35) to its usual Hecke von Mangoldt
series, the second factor instead belongs to psi times
overline(nu)theta. It is a derivative of the same inverse only in
the matching theta=nu sector. The other ray terms are not canceled
by differentiating 1/L(s,psi).

There is a coefficient-faithful prime-only identity for every fixed
prime weight b_i(p):

\[
 \sum_{ap=n\atop p\ {m prime},\ (a,p)=1}
       \mu(a)\psi(a)\psi(p)b_i(p)
   =-\mu(n)\psi(n)\sum_{p\mid n}b_i(p).                    \tag{37}
\]

This includes nonsquarefree n: both sides vanish. It preserves the
actual ray restriction and prime weights, but its multiplier is the
weighted prime-divisor mark, not log Nn. For the source's disjoint
prime lists, repeated applications on the genuine coprime locus give
the corresponding product-form marked coefficient already present
in its marked-moment class.

The actual product of the inverse and Q_i does not impose (a,p)=1.
Its overlap terms must therefore also be retained or separately
priced. At n=p^2 the prime-only unrestricted convolution is
-b_i(p), while the right side of (37) is zero; the p^2 von Mangoldt
term is exactly what repairs this for the full Lambda identity.
Likewise the separate profile W(Na/D) in the inverse depends on
n/p after merging the variables, so it is not one fixed profile in
Nn multiplying log Nn. Common Mellin separation preserves this
dependence as prime-dependent mark weights.

Consequently the logarithmic identity gives a precise same-character
full-factor simplification, and the genuine restricted slots give
the existing weighted marked class plus its exact overlap terms.
It does not supply a smaller estimate for the broad physical marked
polynomial or for the R>sqrt(U) kernel in (11).

## 10. What remains

The file proves a smaller native component at relevant detector
lengths and gives an exact signed formula for the remaining one.
The open range is the complete coherent R>sqrt(U) sum in (11), with
the two Möbius signs, physical conductor, masks, and dual kernel
retained. A scalar fixed-shift Hardy--Littlewood--Chowla statement
does not control that Eisenstein character-weighted kernel.

The arithmetic source theorems and their entire global framework have
not been independently certified by this note. `check_signed_native.py`
passes 1,352 full-convolution coefficients, 108 masked finite row
identities, 10,000 complete gcd inversions, 1,500 weighted prime-mark
identities, six exact Eisenstein additive class sums, 16 rational
polynomial interpolations, and 286 exponent predicates. Its negative
controls reject the wrong support,
coprime-only outer factors, deleted nonsquarefree outer terms, and
restriction to primary frequencies before the class cancellation,
discarded prime overlaps, and replacement of a restricted mark by a
full logarithmic mark.
The factorization checks use an explicitly labeled integer free-prime
model. They cannot certify (3), the functional equation, or an
asymptotic mean estimate. No RH or zero-free-boundary claim follows
from the present component theorem.
