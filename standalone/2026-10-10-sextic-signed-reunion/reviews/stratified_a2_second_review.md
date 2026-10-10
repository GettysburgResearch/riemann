# Independent review: stratified two-scalar A2 theorem and positive-cutoff addendum

## 1. Reviewed bytes and verdict

Reviewer: the higher-balanced/mixed-replication agent. Date: 2026-10-10.

**Contribution disclosure.** The two manuscript authors are other agents,
but I contributed cutoff and scope calculations during development,
including discussion of the child-scale summation and cutoffs below one.
This report records a separate fresh recomputation and adversarial audit
of the final text. It is not a claim that I am independent of every
underlying contribution. Under docs/REVIEWING.md, the packet remains
proposed research: this agent review does not place it in the integrated
accepted mathematics record, and agreement among agents is not a
substitute for the displayed proofs or an integrator's status decision.

The complete files reviewed are:

| File | Bytes | SHA-256 |
|---|---:|---|
| riemann/standalone/2026-10-10-sextic-signed-reunion/STRATIFIED_TWO_SCALAR_A2.md | 22,168 | 9b540fe779b6e0f3c64baba04deed6ee380f1d9746035afc3cf9c7fdb0cf3ad5 |
| pass3_small_w_924_addendum.md | 5,830 | 52a4d27a5f518feabfb8ecb6c87eee5172a6ce3f2cf6a5aa5630c00ff9346461 |

Both paths are relative to /workspace/scratch/6ec6134c1535. The addendum hash
is its final amendment: it explicitly permits the fixed cutoff dilation
used in the combined theorem and references that completed theorem. The
earlier addendum hash ab53e85e is not the object certified here.

**Verdict: PASS, within the explicitly imported analytic premises.**

No defect was found in the sixth-power-free sieve deduction, the use of
both actual scalar cancellations on the row strata, the extension to
either prescribed axis orientation, the exact treatment of cutoffs below
one and of capped strata, the full A2 norm summation, or the optimization.
The positive-cutoff addendum also passes: its calculation is a limitation
of the explicitly displayed positive upper envelopes, with exact
empty-stratum refinements and other analytic strategies expressly left
open. It is not an arithmetic lower bound.

The result certified is a source-qualified estimate for the actual raw
and complete A2 positive Gauss energies. It does not establish the
upstream theta/cusp/angular premises, the signed centered covariance,
a full fourth moment, a cofinal moment hierarchy, or an RH implication.

## 2. Source and premise audit

I read the complete combined theorem, the complete final addendum, and
the relevant arithmetic, scalar, and normalization arguments in their
pinned source files. The following local bytes were independently
checked:

| Source | SHA-256 |
|---|---|
| HYBRID_CUBE_INVERSE.md | d4c5dad1b5c719043ac7118c5f468b3d5c398e2bbd5c4470a1983f64139f066a |
| MOVING_COLUMN_MASKS.md | 068c7c993bdf09e17c2c06182ca8bc631e6ed34d8df6ccf29c46e1f2333ae0ee |
| A2_MOVING_MEAN_SQUARE.md | 6eed5695c672dab92620763f8df5b63f60dc416754367ed541cb854bf06854ba |
| PR #913 REFINED_ALL_ROW_SIEVE.md | 6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8 |
| PR #924 SIXTH_POWER_STRATIFIED_INVERSE.md | f98cc20e361ebb99af7dbd4b5ffef83a8a55ca11c4d3f24da238bc24be4cb2e9 |
| PR #924 ANISOTROPIC_A2_NORM_TRANSFER.md | e671b8b1c8717ed494b3db0ba39fb4c0de374aef56f774bf9a7ca68e01b277cf |

The two #924 files are pinned at commit
725b2d25ab47e57500049d93985560098c7ef3fa, respectively Git blobs
004dd4a8de2237661235a9da460b3caab432ef53 and
1e4e8a9b70fb15ee42bc41abbcdc3b217e07f215. Their byte-exact local copies are
in pass2_root_sources. The #913 source is pinned at commit
6498d6cc2eded03159c7332b25fd224ad07f89c1.

The new proof correctly keeps a fixed beta in (1/2,1]. Its beta=11/12
numerics inherit the angular/canonical scalar premise and its epsilon
convention; beta=1 comes from counting. The argument uses both actual
inverse scalar sums, with their finite smooth seminorm and uniformly
polynomial moving-label range. It does not promote a structured theta
estimate to an arbitrary-coefficient assertion.

The reference parameter, physical supports, and polynomial ceilings
remain distinct from the freely chosen inverse cutoff R. In particular,
the assertion for every R>0 does not require scalar estimates on
arbitrarily short nonempty physical supports. Empty supports are zero;
nonempty physical scales below one lie in a fixed compact positive
interval and admit uniformly bounded rescaling.

For q0 and f with overlap, replacing q0 by q0/(q0,f) is an exact use of
the f-character zeros. It is not a contraction argument for a completed
norm. The resulting parameters

\[
J=FQ,\qquad K=F^{2/3}Q^{1/3}\le J^{2/3}
\]

are used consistently below, including after adding the sixth-power
row mask and after the A2 correction.

## 3. The sixth-power-free sieve and the row partition

The deduction in Section 2 is valid from the two cited valuation-block
alternatives. Write P0=product A_j, M=max A_j and P=product A_j^j.
With all A_j at least one,

\[
P_0\le P,\qquad P_0^2/M\le P,\qquad
P_0/M^{1/3}\le P^{2/3}.
\]

For the last two inequalities the positive residual coefficient can
only occur at log A1, where log M absorbs it. Thus

\[
\min(P_0L/M,P_0^2)
\le(P_0L/M)^{2/3}(P_0^2)^{1/3}
\le(UL)^{2/3}.
\]

Taking the minimum of the whole block bounds is legitimate: one first
adds their nonnegative common upper terms, then uses the displayed
minimum for the two remaining terms. The result is
U+L+(UL)^(2/3). This preserves the fixed coefficient masks. I also
checked the cited ordinary-character alternative: it freezes the
sixth-power mask before varying primitive characters, rather than
discarding zeros from imprimitive powers.

The sixth-power-free convention permits valuations 0 through 5. It
retains unit rows and the finitely many bad-prime patterns. The subsequent
representation

\[
k=\varepsilon v^6k_0
\]

is unique in the fixed generator convention. No condition (v,k0)=1 is
present or needed. The literal identity
chi_n(v^6)=1_{(n,v)=1} makes rad(v) an exclusion on every physical
column factor. It also constrains the inverse and regrouped cube indices.
The estimates

\[
Q_v\le QV,\quad J_v\le JV,\quad K_v\le KV^{1/3},
\quad U_v\ll H/V^6
\]

are therefore correct, including overlap of v with f and q0. Its
original bad-prime factors do not introduce a new moving good-prime
label. Unit twists stay in the same finite family.

## 4. Two scalar savings, arbitrary orientation, and exact cutoffs

The orientation extension in Section 3.2 is justified at the physical
block level, rather than inferred by relabelling the already ordered
rectangular corollary. The middle monomial is

\[
\frac{J U^2 A}{B F_1^2}
G^{2\beta-1}Z^{2\beta+1},\qquad
G^2Z^3\ll B.
\]

Since 2 beta-1 is positive, the bound G <= const sqrt(B) Z^(-3/2)
gives

\[
J U^2 A B^{\beta-3/2}Z^{5/2-\beta}.
\]

This remains a valid upper bound when that estimate for G exceeds its
actual outer support; it requires no inequality A<=B. The first and
third block bounds follow from nonpositive G and Z powers at the
positions identified in the proof. All bounded nonempty scales are
covered by fixed constants.

The common-divisor separation retains exactly the scalar norm weights

\[
d_1^{-\beta-1/2}d_2^{-\beta-1/2}\ell^{-2\beta}.
\]

They are summable in ideal norms for every fixed beta>1/2. In particular,
the remaining positive factor is allowed to meet ell. Forcing an extra
coprimality there would change the inverse identity; the new proof does
not do so. The moving exclusions are those already proved for both
actual scalar coefficients.

The chosen cutoff has omega=1 on [0,1/2] and omega=0 on [1,infinity).
Consequently:

* If r<=1, every inverse ideal has Nh/r>=1, so the short part is
  exactly empty.
* At r=2 C B^(1/3), every actual inverse index has Nh/r<=1/2, so
  the long part is exactly empty.
* On a nonempty smooth inverse dyad Nh comparable to Z, rescaled
  derivatives of omega((Z/r)(Nh/Z)) are uniformly bounded, since Z/r
  is bounded on support. Common-divisor shifts preserve that ratio.

These statements justify use of the smooth scalar premise without a
new r-dependent seminorm loss. The stratum-dependent choice
r_v=min(2 C B^(1/3),R V) is legitimate because it is made after an
exact partition of the physical rows.

For the long inverse, d=hb need not be squarefree and (h,b)=1 must not
be imposed. The coefficient

\[
c_r(d)=\sum_{h\mid d}\mu(h)[1-\omega(Nh/r)]
\]

vanishes when Nd<=r/2. Every divisor h of a permitted physical d already
has the required inherited exclusions. The outer mask (a,d)=1 remains,
while the inner squarefree column can meet d. The child normalization
and coefficient mass give its sixth-power-free energy

\[
D^\epsilon[U+AB/(Nd)^3+(UAB)^{2/3}/(Nd)^2].
\]

The exterior coefficient has norm 1/Nd. Minkowski therefore invokes
the ideal sums of powers -1, -5/2 and -2. The first is finite harmonic;
the latter two give r^(-3/2) and r^(-1) at norm level. Their stated
upper bounds also hold when r<1, since the actual sums then start at
norm one. Capped strata are omitted exactly, rather than charged a
fictitious positive long tail.

After squaring and adding disjoint v strata, the six V powers are

\[
-6,\quad-17/2-\beta,\quad-23/3+2\beta,\quad
-6,\quad-3,\quad-6.
\]

Each is less than -1 throughout the fixed beta range. Hence the
six-term raw estimate holds for every positive R, with all rows and
moving exclusions retained. This is the valid mechanism removing the
earlier H^(1/6) repetition factor from the long tail.

## 5. Complete A2 transfer and independent norm arithmetic

For the five-label local support
n1=a c d^2 e^2 and n2=b c^2 d e^2, I checked the exact projection
normalization and child parameters. With x=Nc, y=Nd, z=Ne,

\[
A_t=Dx^{-1}y^{-2}z^{-2},\quad
B_t=Dx^{-2}y^{-1}z^{-2},\quad
\sqrt{N(cde)}\sqrt{A_tB_t/D^2}=(xyz^{3/2})^{-1}.
\]

The exterior phase has modulus at most one only after retaining its
nonunit zeros. Since correction primes avoid q0 f S,

\[
F_t=Fz,\quad Q_t=Qxy,\quad
J_t=Jxyz,\quad K_t=K(xy)^{1/3}z^{2/3}.
\]

This accounts for the overlap at e exactly once. It does not replace
the completed polynomial by a conductor-independent column contraction.

Set p=5/2-beta and

\[
\tau=\frac{3-2\beta}{5-2\beta},\qquad
R_t=R(B_t/D)^\tau.
\]

Then 1/3<=tau<1/2 and p tau=(3-2 beta)/2. The arbitrary-orientation
argument above is essential here, since the relative sizes of A_t and
B_t depend on c and d.

I recomputed the entire six-by-three norm table by substituting the
child A_t,B_t,J_t,K_t and R_t into each energy monomial, taking its
square root, and only then inserting the exterior weight. This yields
exactly the displayed table. In particular the critical second energy
row has pre-normalization powers (0,-1,-1), and thus norm powers
(-1,-3/2,-2). The first coordinate costs only a finite harmonic sum.

As an independent exact-arithmetic check, beta=11/12 gives tau=7/19
and the following norm table:

| Row | x | y | z |
|---|---:|---:|---:|
| First short | -3/2 | -2 | -5/2 |
| Second short | -1 | -3/2 | -2 |
| Third short | -86/57 | -165/76 | -143/57 |
| First long | -1 | -1 | -3/2 |
| Second long | -53/38 | -37/19 | -91/38 |
| Third long | -24/19 | -31/19 | -239/114 |

For general fixed beta the inequalities follow from tau<1/2 and
2 beta tau>1/3. Every non-harmonic power is strictly less than -1.
The possible constant blowup as beta approaches one half is explicitly
allowed. The harmonic sums have polynomially bounded physical support,
so their fixed logarithmic powers enter D^epsilon.

Only in these positive coefficient sums may correction coprimalities
be dropped. Minkowski then transfers the same six-term envelope to the
complete A2 polynomial. Child R_t below one is used literally; replacing
it everywhere by one would invalidate the displayed table.

The proof appropriately describes tau as one successful choice. The
source cube-root choice gives second-row x exponent -17/18 at beta=11/12,
which obstructs that naive independent-coordinate summation. It does
not obstruct every ordered or coupled use of the original support.

## 6. Optimization and numerical consequences

Under J H^2<=D^p, the two balancing cutoffs R2 and R3 in Section 5
are at least one. The second follows from
K H^(4/3)<=(JH^2)^(2/3)<=D^(2p/3)<=D^(4/3).
Moreover R3<=D^(1/3); the proof correctly does not require that of
R2 separately. Thus R=min(R2,R3) is in the declared range.

Both increasing terms are at most E*=D^2 R^(-3). I checked the
comparisons controlling HD and the mixed long tail:

\[
\frac{D^2R_3^{-3}}{HD}
=(D/H)^{(2\beta-1)/(2\beta+3)}
K^{3/(2\beta+3)}\ge1,
\]

\[
\frac{H^{2/3}D^{4/3}R^{-2}}{D^2R^{-3}}
\le(H/D)^{\,2/3-4/[3(2\beta+3)]}
K^{-1/(2\beta+3)}\le1.
\]

Here H<=D follows from the same feasibility condition. The optimized
maximum in (5.3) follows exactly; no infeasible branch is inserted.

At beta=11/12 it is

\[
D^\epsilon\max\{
D^{34/29}H^{24/29}K^{18/29},
D^{53/55}H^{72/55}J^{36/55}\},
\qquad JH^2\le D^{19/12}.
\]

For unit labels and H=D^(1/2), the choice R=D^(7/55) produces the
six exact exponents

\[
3/2,\quad89/55,\quad47/30,\quad1/2,\quad89/55,\quad233/165.
\]

An exact Fraction calculation independently confirms these fractions,
all 18 specialized table entries, and the gains
31/19-89/55=14/1045 and 1087/660-89/55=19/660.
The largest exponent is 89/55. This numerical check supplements the
symbolic proof; it is not treated as evidence for a general moment.

At beta=1 the formula agrees with the existing counting bound, as
the text states. The beta=11/12 sufficient positive row range
H<=D^(19/24) J^(-1/2) remains the same; the improved energy exponent
does not by itself enlarge that range or a zeta zero-free region.

## 7. Profiles and retained quantifiers

Fixed smooth two-variable tests admit the stated finite-seminorm
Mellin separation on their physical supports. It does not introduce an
arbitrary arithmetic theta vector.

For inward annuli the same parent R can be used, with row powers
1,2,4/3,1,0,2/3. The zero row power contributes a finite logarithmic
factor. For outward Schwartz annuli, keeping the physical axes,
labels, parent R and arithmetic child choices fixed is legitimate.
One enlarges only the common reference parameter and applies the
unoptimized six-term bound. The largest row power is two and fixed
rapid decay absorbs it and the preliminary epsilon losses. The proof
does not incorrectly maintain the optimized feasibility condition on
arbitrarily large annuli.

The entire theorem keeps all nonzero element rows, actual finite ray
families, original exclusions and their overlaps. It uses no native
higher moment beyond the stated source machinery.

## 8. Review of the final positive-cutoff addendum

The addendum qualifies the old small-w audit, whose hash is
c0d07ccc7ed2fc1490a631c73db47044df256b7ca6f946ecacd5c735e457f9d9.
My separate completed review of that old audit is
pass2_small_w_core_independent_review.md, SHA-256
a7d6f5b23b52d235274981955ecf86828826de87415043885aad11f05b8b132a.
Its R>=1 discussion was explicitly restricted to the old pinned route.

The final addendum now distinguishes the two smooth cutoff
normalizations precisely. A cutoff supported below 2 with plateau
through 1 has the stated sufficient empty threshold R<1/2. Its
fixed dilation, with plateau through 1/2 and support below 1, has
empty short part for R<=1 and a doubled physical cap. They yield
the same power estimates with different fixed constants. There is no
conflict between the addendum and the combined proof.

For the displayed balanced residual block,

\[
Z=D^2/B,\quad m=M=\sqrt Z,\quad Y=Z^2/H,\quad
J=B,\quad K=B^{1/3},
\]

I independently substituted these quantities into the second short
energy monomial and multiplied by the explicitly optimistic H/Z
conversion. After division by the target H, the two relevant costs
are exactly

\[
\mathcal A R^p,\quad R^{-3},\qquad
\mathcal A=D^2H^{-2}Z^{7/4+\kappa/2}.
\]

The two values of p are 9/2-3 kappa for #924 and 5/2-kappa for the
completed two-scalar theorem. Both are positive. Minimization over
all R>0, including R<1, gives

\[
\inf_{R>0}\max(\mathcal A R^p,R^{-3})
=\mathcal A^{3/(p+3)}.
\]

This follows by comparing each side of the balancing point
R=A^(-1/(p+3)); it imposes no artificial lower cutoff.

Nonempty compact dual support implies Y bounded below by a positive
support constant. Consequently Z is at least a constant times sqrt(H),
and

\[
\mathcal A\gg D^2H^{-9/8+\kappa/4}.
\]

For fixed 1<h<2, H=D^h and 1/2<kappa<=1, its D exponent is positive:
9/8-kappa/4<1, so it is greater than 2-h. At kappa=11/12 this
gives -43/48 as the H exponent, and the two optimized powers are
12/19 and 36/55, respectively. All fractions check exactly.

The addendum accurately describes this as a lower bound on the value
of a specified upper envelope after optimizing its parameter. It is
not a lower bound on the arithmetic energy. The primitive-pair/Cauchy
conversion is explicitly granted for a benchmark rather than asserted
as an unsigned replacement of the original covariance.

Finally, at the leading rectangle the classical positive envelope
Y+Y^(1/6)D^2+(YD^2)^(2/3), after multiplication by H/D^2, has
exponents 2,(5h+4)/6,2+h/3. The last is the largest for 1<h<2
and is greater than h. The separate D^3 first-short-term benchmark
is also arithmetically correct.

These observations do not force an actual short stratum to be
nonempty. The addendum expressly permits exact empty-stratum omission,
new support pruning, other positive methods, averaged labels, and
signed cancellation. It also exempts bounded-Y and eventually empty
dual endpoints from its growing-scale diagnosis. This scope is
necessary in light of #924 and is present in the final reviewed bytes.

## 9. Certification boundary

The new theorem and the final cutoff addendum can be included as
source-qualified component results with the stated hashes. Their
analytic distinction is clear: the theorem proves a stronger positive
energy bound for the actual coefficient family; the addendum records
why its displayed envelope still does not settle a particular
remaining balanced covariance problem.

This review made no edits to either target or to any repository file.
It certifies the deductions and scope above, while retaining the
upstream analytic premises and the open signed moment problem.
