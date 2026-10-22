# Q2/Q4 reflected–Selberg, Jordan, curvature, inertia, and full-proof-proposal review

**Review role:** integration-wave reviewer for the complete Q2/Q4 reflected–Selberg / Jordan / curvature / inertia lineage  
**Review cutoff (UTC):** `2026-08-10T22:00:51Z`  
**Base branch:** `main`  
**Base/main SHA:** `d6409319b4041cd09bee85f55a344631508f2501`  
**Review branch:** `review/integration-wave-20260810-q4`  
**Review character:** review only; no source branch was modified, merged, cherry-picked, or rewritten

## 1. Executive verdict

**The Riemann Hypothesis is not established by this lineage.**

The strongest current corrected endpoint is PR #362 at
`31c57c56c00c0a062a49a126d4e5a68ff28e9fe8`. It identifies the
polynomial **Positive Innovation Gate** (PIG) for the compact Q4 current
as the surviving RH-bearing statement. Its exact filtered-Chebyshev
formula, logarithmic delayed gauge, and open-strip pole-preservation
claims survive review. The implication

\[
\mathrm{RH}\Longrightarrow \mathrm{PIG}
\]

is **VERIFIED**. The reverse implication is imported from the incomplete
block assembly on PR #357 and is therefore, at the reviewed SHAs,
**UNPROVEN / GAP** rather than an unconditional theorem. A direct adapter
from the exact Q4 innovation block to the resident vector-valued
pole-energy consumer appears plausible, but is not supplied at the
reviewed head.

PR #359 at
`9ffcb8d3dbc6affd859ea8567a061b71dd0d1e8b` is a
**PROPOSED COMPLETE THEOREM / FALSE** proposal. Its exact aggregate
determinant lemma and its nonnegative-weight inertia estimate are useful,
but its proof composition makes two hypothesis-matching invalid moves:

1. it uses small aggregate negative inertia as though it bounded the
   positive RH-sensitive current, despite the exact #357 refutation that
   the current may be arbitrarily large while the negative spectral mass
   is zero; and
2. it converts a weighted coefficient-energy budget for the finite
   parity synthesis into an operator contraction \(W^*W\le qI\) with
   \(q<2/5\). At the critical-line point \(z=2^{-1/2}\), the submitted
   filters instead satisfy
   \[
   |W_+(z)|^2+|W_-(z)|^2
   =
   \frac{751606691}{24000000}
   -
   \frac{277818163}{18000000}\sqrt2
   \approx 9.4894891256567.
   \]
   The coefficient budget is not a frequencywise synthesis norm.

PR #357 at
`a2843d31649822014219a13ec29c70e4a30932cc` correctly isolates PIG
and correctly refutes the inertia-to-current shortcut, but its claim
that the complete QIDR assembly is closed outside PIG is
**UNPROVEN / GAP**. In particular, its fixed-filter source dictionary
contains a false positive/negative spectral-mass transfer through the
nonconstant multiplier \((1-4^{-s})^{-1}\), while its own all-pass
storage and Q2-cascade files still mark source substitution, final
reservoir negative mass, collars, and the global recurrence as open.

The first load-bearing open arrow is therefore

\[
\boxed{\text{negative-inertia / curvature bookkeeping}
\;\not\Longrightarrow\;
\text{polynomial positive compact-Q4 innovation energy}.}
\]

There is also a pre-PIG assembly obligation: write and prove one exact
global block recurrence in one metric, with the actual source
substitution, final reservoir, pushforward measure, collars, and delayed
states all present.

## 2. Frozen source heads and drift record

The following heads were reviewed as immutable targets. PR titles and
descriptions were used only as navigation; the theorem, lemma,
refutation, report, dependency, checker, and retained-output files were
read at these SHAs.

| PR | Reviewed head SHA | Principal role in lineage |
|---:|---|---|
| #241 | `3a227e7595e1fe9e38956048297aa97531c80e4e` | independent-frequency bireflected Selberg identity |
| #263 | `6ca2028191d997b6f97118883ec069c1916a69a4` | parity frame and finite Bézout synthesis |
| #268 | `7e614540377cf2b1b3216a33240879ad8daf7b9b` | source typing and RH-sensitive source change |
| #269 | `4c67408f1dd7cd3d6574bafbf51c50a280bc0384` | direct carry-window pole-cancellation firewall |
| #297 | `409e1764fc708f725aae8dcd3fad9b8ae480bea3` | vector local-energy pole consumer |
| #325 | `8036edcd8b42f1fb3bbee605a6fae3b22985238d` | Euler–Blaschke/all-pass family and Q4 reserve |
| #329 | `219cab4496357867018f300936c877967ac0a81b` | complete-jet curvature absorption |
| #337 | `46a4a25ccefbd480d533b03ee5e41d9980f25248` | reflected individual terms and reserve ancestors |
| #339 | `762c9192d9c6505e91e0f3e47f907c9a751b12a5` | exact physical/carry placement and block telescope |
| #341 | `6725c527a1022842b370adb0b5656d2a02827d73` | real-\(X\) placement and exact two-state source ledger |
| #342 | `0ecb814f3f1d376ef28ab77ada6710c07e58f6d9` | critical Q4 reserve increment and compact second current |
| #345 | `36e0b71f27798835e622a0646474ff24064ca62a` | compact innovation recurrence and zero-bare source |
| #346 | `e0cfcf9277eb2c7101e9287e2c5f686780d5610b` | compact parity synthesis and joint jet frame |
| #349 | `1177cbab90c3e948a746afebcc4c2a9198237dcb` | intermediate odd-source correction |
| #350 | `eef62a7260b9c510b5539c13eb8329d6d142acd5` | exact source/carry mismatch refutation and centered repairs |
| #354 | `1541618502d345766a0e0b9758ae04f41c17335d` | mandatory divisor convolution and corrected ordinary-prefix curvature |
| #357 | `a2843d31649822014219a13ec29c70e4a30932cc` | Claude-inspired inertia route and PIG reduction |
| #359 | `9ffcb8d3dbc6affd859ea8567a061b71dd0d1e8b` | aggregate-inertia full RH proposal |
| #362 | `31c57c56c00c0a062a49a126d4e5a68ff28e9fe8` | corrected PIG/RH frontier and pole-preserving multiplier |

At the final drift pass, `main` remained identical to the frozen base
SHA. PRs #357, #359, and #362 remained at the reviewed SHAs above. No
material source drift was observed during this review.

A pre-existing branch-ancestry issue is material and must be preserved:
PR #359 is based on the older #357 snapshot
`1c593a0a29e1f3486f18509995db605c1309533c`, whereas current #357 is
`a2843d31649822014219a13ec29c70e4a30932cc`. The later #357 head contains
the exact inertia-to-current refutation that invalidates the #359
composition. PR #362 is based on the current #357 head.

## 3. Lifecycle and supersession map

The live mathematical lineage is not linear.

```text
#241 independent-frequency bireflected identity
  └─> #263 parity frame / finite Bézout synthesis
       ├─> #268 source typing; positive inverse is RH-blind
       └─> #269 carry-window pole cancellation firewall

#325 Euler–Blaschke / Q4 all-pass / reserve
  ├─> #337 reserve and reflected-individual-term ancestors
  ├─> #339 exact physical/carry placement and all-pass block telescope
  ├─> #341 real-X carry identity and exact two-state ledger
  ├─> #342 critical reserve increment / compact second current
  ├─> #345 compact innovation recurrence / zero-bare relative source
  └─> #346 compact parity synthesis / joint jet frame

#349 intermediate odd-source correction
  └─> #350 exact carry-transform mismatch and centered repairs
       └─> #354 mandatory divisor-convolution repair and matrix-positivity firewall

#357 inertia-tolerant route:
  exact local/aggregate negative-mass bookkeeping
  + exact refutation of "small inertia => small current"
  + proposed global QIDR assembly
       ├─> #359 older-snapshot aggregate-inertia full proposal (FALSE)
       └─> #362 current-head PIG frontier (corrected endpoint)

#297 supplies the resident vector pole-energy consumer, but the exact
Q4-PIG-to-#297 adapter is not written at the reviewed heads.
```

PR #350 has a source/body mismatch worth recording. Its actual head
contains the exact carry-transform mismatch refutation and centered
scale-two/scale-four repairs. Its PR body also narrates an
ordinary-prefix second-current theorem that is not present in that head;
the later actual theorem is on #354. Integration must follow tree
contents, not the #350 narrative.

## 4. Reconstructed strongest current proof DAG

### 4.1 DAG overview

```text
compact arithmetic source
  -> exact physical/carry placement
  -> source, current, and second-current jets
  -> cofinal critical reserve
  -> two-state Hermitian curvature
  -> nonnegative physical aggregation
  -> negative-inertia statistic
  -> finite synthesis / all-pass telescope
  -> delayed normalized recurrence
  -> polynomial positive-innovation energy (PIG)
  -> subexponential pole-current energy
  -> pole exclusion
  -> RH
```

The first seven nodes contain substantial verified infrastructure.
The eighth is only partly assembled and contains two false submitted
transfers. The ninth is exact rowwise but not closed globally. The
tenth is open and RH-bearing.

### 4.2 Claim-by-claim arrows

#### Arrow A — arithmetic source to compact innovation

At #345 and #362, the compact Q4 source has Dirichlet multiplier

\[
B_\circ(s)=\frac{1-4^{1-s}}{\zeta(s)}
\]

and own compact current

\[
i_\circ=q_\circ-(\log4)\,\delta_4*b_4.
\]

The own current has the exact filtered-Chebyshev row formula, for
\(n=j+k\),

\[
\begin{aligned}
L_{(4n,4j)}(q_\circ)
={}&E(4n)-E(4j)-E(4k)\\
&-4\{E(n)-E(j)-E(k)\}-4\log4,
\end{aligned}
\qquad E(x)=\psi(x)-x.
\]

**Type:** equality.  
**Granularity:** rowwise, every nontrivial integer split.  
**Metric/normalization:** unnormalized ordinary prefix/carry row before
the later \(1/\sqrt n\) critical normalization.  
**Scale:** own current at scale \(4n\), with a delayed bare gauge at
scale \(n\).  
**Endpoint/gauge:** the \(-4\log4\) atom and
\((\log4)\delta_4*b_4\) are retained.  
**Verdict:** **VERIFIED**.

#### Arrow B — physical field to exact carry row

#339 `L-33803` and #341 `L-34001` identify the real-\(X\) physical
prefix defect with the carry transform for \(c=1*f\). At an integer
endpoint,

\[
U_c(N,\theta)=c(N)+D_c(N-1,j),
\]

so the physical object is the predecessor carry row plus the explicit
endpoint atom, not a silently shifted present-scale row.

**Type:** equality.  
**Granularity:** pointwise in the physical coordinate, then integrated
rowwise/blockwise.  
**Metric/normalization:** row integration contributes the physical
\(1/n\)-scale; critical square-root normalization contributes the
second \(1/n\)-scale in the final quadratic block, explaining the
compressed \(n^{-2}\) weight used in #359.  
**Scale:** predecessor/delayed carry state.  
**Endpoint/collar:** explicit one-unit floor/endpoint collar.  
**Verdict:** **VERIFIED**.

#### Arrow C — source to Jordan jets

The Jordan deformation is taken along one common path before the finite
source filters are differentiated. #354 repairs the essential typing:
the carry row for a source \(f\) is built from the ordinary prefix of
\(1*f\). The omitted divisor convolution is not optional.

**Type:** exact differentiation and convolution identities.  
**Granularity:** coefficientwise and rowwise.  
**Metric:** common odd-Jordan coefficient/physical block metric.  
**Scale:** current and second-current jets at the declared scale;
delayed gauges remain delayed.  
**Order:** source multiplier/filter, ordinary divisor convolution,
then carry placement; no commutation is assumed without proof.  
**Verdict:** **VERIFIED WITH FIXES**. Earlier odd-source formulas
without the convolution are **FALSE** or **SUPERSEDED**.

#### Arrow D — critical reserve

#342 gives the exact radix-four reserve increment

\[
\Delta_4R=8PE+E^2+16S-S_+\ge 8PE
\]

in the balanced range, and derives a cofinal
\(\Theta_\eta(n\log n)\) moat. #325/#337 give the underlying Q4
Selberg–Kummer reserve statements.

**Type:** exact equality followed by inequalities.  
**Granularity:** rowwise on balanced cones, then cofinal/logarithmic
blocks.  
**Metric/normalization:** arithmetic source scale before critical
\(1/n\) or \(1/n^2\) normalization.  
**Sign/coefficient:** positive; the \(8PE\) term is the principal moat.  
**Reserve spending:** it may be charged once in the augmented-curvature
ledger. It cannot also be reused independently to absorb the final
positive innovation mass.  
**Verdict:** **VERIFIED WITH FIXES** because part of the cofinal range
rests on retained finite verification rather than a fully symbolic
all-\(n\) proof.

#### Arrow E — reserve/current jets to Hermitian curvature

For the zero-bare relative source, #357 writes the two-state row
curvature as

\[
K=
\begin{pmatrix}
R & EI-T/2\\
\overline{EI-T/2}&|I|^2
\end{pmatrix}.
\]

Its scalar trace includes the positive current square, but this is a
lower ledger, not an upper bound for \(I\). Completing the determinant
gives a row negative-mass estimate \(O_\eta(n/\log n)\), hence
\(O_\eta(1/\log n)\) after critical normalization.

**Type:** exact matrix identity plus an upper bound for the negative
spectral mass.  
**Granularity:** rowwise.  
**Metric:** common zero-bare two-state Jordan metric.  
**Sign:** only the negative spectral part is controlled.  
**Verdict:** **VERIFIED** at its stated inertia scope.

The stronger assertions “positive scalar curvature implies PSD” and
“positive curvature containing \(|I|^2\) upper-bounds \(I\)” are
**FALSE**.

#### Arrow F — row curvatures to aggregate inertia

#359 `L-90304` proves an exact aggregate determinant theorem. With
nonnegative weights \(w_a\),

\[
\bar K=\sum_aw_aK_a,\qquad
A=\sum_aw_aR_a,\quad F=\sum_aw_a|E_a|^2,\quad
U=\sum_aw_a\Theta_a,
\]

and \(A>F\),

\[
(-\det\bar K)_+
\le\frac{A}{4(A-F)}|U|^2,\qquad
\operatorname{tr}(\bar K)_-
\le\frac{|U|^2}{4(A-F)}.
\]

The unknown positive current energy is optimized out of the negative
determinant defect.

**Type:** exact finite-dimensional inequality.  
**Granularity:** blockwise aggregate.  
**Weights:** nonnegative physical weights.  
**Centering:** one common zero-bare centering; no row-dependent shear.  
**Normalization:** the physical \(n^{-1}\) integration and critical
\(n^{-1}\) quadratic normalization combine to \(n^{-2}\) at an endpoint.  
**Verdict:** algebra **VERIFIED**; the physical application is
**VERIFIED WITH FIXES**.

This theorem controls only negative inertia. It does not control the
positive current energy.

#### Arrow G — negative inertia to synthesis/all-pass statistic

#357 `L-90305`–`L-90306` correctly establish convex lifting of negative
trace mass through nonnegative aggregation/compressions and the sign of
the independent-frequency all-pass curvature telescope. Internal Q2
states cancel in the exact two-stage Q2 realization of Q4.

Two later transfers fail:

1. #357 `L-90308.12` asserts that multiplication by
   \((1-4^{-s})^{-1}\), whose norm is at most \(2\) on the critical
   line, transfers positive and negative spectral masses by a factor
   \(4\). This is false for an indefinite integrated curvature:
   a nonconstant multiplier reweights positive and negative densities
   differently and can destroy their cancellation.
2. #359 treats the #346 weighted coefficient-energy ratio as
   \(W^*W\le qI\), \(q<2/5\). This is false; the actual frequencywise
   norm already exceeds \(9\) at \(z=2^{-1/2}\).

**Type:** mixed equalities and inequalities.  
**Granularity:** exact independent-frequency block identities, followed
by invalid integrated/operator inequalities.  
**Verdict:** exact telescope **VERIFIED**; the two submitted transfer
arrows **FALSE**.

#### Arrow H — all-pass state to delayed recurrence

The exact scalar recurrence from #345/#357 is

\[
U(4n,4j)=\frac12U(n,j)+\frac{I_\circ(n,j)}{2\sqrt n}
\]

and hence

\[
|U(4n,4j)|^2
\le |U(n,j)|^2+\frac{|I_\circ(n,j)|^2}{3n}.
\]

The coefficient and delayed orientation are correct. #357 also
contains exact state dictionaries and fixed-collar polylogarithmic
bounds.

**Type:** equality and rowwise inequality.  
**Granularity:** rowwise.  
**Metric:** normalized compact current state.  
**Scale:** present \(4n\) state from predecessor \(n\) state plus
current innovation.  
**Coefficient:** \(1/2\) in the state equality and \(1/3\) in the
energy forcing.  
**Collars/terminal terms:** finite fixed-filter collars are polynomial,
but the complete block pushforward and final reservoir term are not
proved in one theorem.  
**Verdict:** row recurrence **VERIFIED**; claimed complete integrated
recurrence **UNPROVEN / GAP**.

#### Arrow I — recurrence to polynomial innovation energy

Define the positive innovation mass on a logarithmic block by

\[
\mathcal I(J)
=
\int \frac{|I_\circ(n,j)|^2}{n}\,d\nu_J.
\]

The required gate is

\[
\mathrm{PIG}:\qquad \mathcal I(J)\le \operatorname{poly}(J).
\]

No preceding inertia estimate yields this: negative inertia can vanish
for arbitrarily large \(I\). The same positive Selberg/Kummer reserve
cannot be spent once in the curvature moat and again to manufacture
this upper bound.

**Type:** desired upper inequality.  
**Granularity:** integrated logarithmic block.  
**Metric:** positive physical innovation Gram, critical \(1/n\)
normalization.  
**Scale:** current-scale innovation.  
**Verdict:** **UNPROVEN / GAP**; relative to a completed exact assembly,
an **RH-EQUIVALENT CRITERION**.

#### Arrow J — PIG to subexponential pole energy

Given the exact block recurrence and PIG, iteration gives polynomial
state energy and hence \(e^{o(J)}\) local energy. This is an elementary
conditional implication; its use requires that the block measure and
source adapter really are the same objects consumed by the pole theorem.

**Type:** conditional inequality/iteration.  
**Granularity:** integrated blockwise.  
**Verdict:** **VERIFIED WITH FIXES** as a conditional implication.

#### Arrow K — pole energy to pole exclusion

#297 supplies an exact vector-valued local-energy criterion: every
off-critical-line zero contributes a nonzero residue norm and forces
exponential block energy. #362 shows that the compact Q4 finite
multiplier

\[
M_4(z)=(4^z-4)(1-2^{1-z})
\]

does not vanish for \(0<\Re z<1\), while the own current has pole order
\(m+1\) and the delayed gauge only order \(m\). Thus the Q4 source does
not hide a hypothetical zeta zero.

**Type:** conditional pole-exclusion implication plus exact
nonvanishing.  
**Granularity:** spectral/local-energy block.  
**Verdict:** pole visibility **VERIFIED**; the exact adapter from the
Q4 PIG block to #297's vector block is **UNPROVEN / GAP**.

#### Arrow L — pole exclusion to RH

Once every open-strip zero off the critical line is excluded and the
functional-equation symmetry is retained, RH follows.

**Type:** conditional implication.  
**Verdict:** **VERIFIED** as logic, but its antecedent is not proved.

## 5. Source typing and convolution order

The repository now contains a clear correction chain.

1. The RH-sensitive arithmetic source is the von-Mangoldt source, not
   the positive inverse primitive. The latter is RH-blind because it
   cancels the reciprocal-zeta pole (#268).
2. A carry row for \(f\) uses the ordinary prefix of \(1*f\). #354
   supplies an exact smallest counterexample to the omitted-convolution
   formula: at the row \((2,1)\), the discrepancy is \((\log3)^2\).
3. A pure Selberg carry window has an extra zeta factor and may cancel
   the pole before the RH consumer sees it (#269). It cannot be used
   as a direct coercive pole-energy source.
4. The centered compact Q4 innovation avoids that cancellation: its
   finite numerator is nonzero at every open-strip zero and its gauge
   has lower pole order (#362).
5. Finite radix-two/radix-four filters must be applied to the common
   source path before the Jordan derivatives are compared. There is no
   license to swap “filter”, “ordinary divisor convolution”, and
   “carry transform” merely because all are linear.

## 6. Physical versus carry placement

The exact physical statements are stronger than approximation but more
delicate than several PR summaries suggest.

- The real-\(X\) field is exactly the carry transform only for the
  correctly typed coefficient \(c=1*f\).
- At integer endpoints it is the predecessor row plus an explicit
  endpoint coefficient. Returning that term at current scale changes
  the recurrence.
- The floor/borrow collar is one unit and must remain in the global
  block theorem.
- Physical aggregation uses nonnegative weights. Synthesis commutes
  with aggregation only for one common parameter-independent finite
  operator in one common metric.
- The apparently different \(n^{-1}\) and \(n^{-2}\) weights in #357
  and #359 are compatible when the physical integration factor and
  critical square-root normalization are written separately.

## 7. Independent frequencies

The foundational #241 identity is

\[
C_{(t,-s)}-C_t-C_{-s}
=
2\,\Lambda_t*\Lambda_{-s}.
\]

The physical Gram is a genuine double \((t,s)\)-integral with kernel
\(\Phi_J(t-s)\). #339/#341 preserve this in the product block and in
the all-pass block-state telescope. No reviewed theorem licenses
replacement by a one-frequency modulus square. Every integrated
product, reflected cross term, and individual term must retain both
frequencies until an exact Gram factorization is written.

## 8. Scalar positivity, matrix positivity, and inertia

Four different statements must not be conflated.

1. **Positive scalar trace:** a lower ledger; it can contain
   \(+|I|^2\).
2. **Positive curvature:** still scalar unless a polarized matrix is
   named.
3. **Positive semidefinite polarized matrix:** a much stronger Schur
   inequality.
4. **Small negative spectral mass:** controls only the bad eigenvalue.

The #354 matrix firewall is correct: a fixed synthesis upper bound is a
polarized matrix/operator statement, not a consequence of scalar
curvature positivity. The #357/#359 inertia estimates are useful
because they relax PSD to control of the actually consumed negative
part. They do not furnish the missing upper bound for the positive
innovation current.

## 9. Aggregate inertia audit

The valid aggregate theorem has all of the following features:

- the matrix aggregated is the centered two-state Hermitian curvature;
- all weights are nonnegative;
- the zero-bare relative source supplies one common centering;
- no row-dependent shear is allowed;
- the controlled quantity is
  \(\operatorname{tr}(\bar K)_-\);
- the final scalar current recurrence consumes
  \(\int |I_\circ|^2/n\), not this negative mass.

Consequently, a large positive current can coexist with zero aggregate
negative inertia. The current #357 exact determinant formula already
exhibits this: the determinant is a quadratic with positive leading
coefficient in \(I\), so the matrix becomes PSD for sufficiently large
\(|I|\). #359's aggregate theorem does not remove this problem; it
removes the current only from the **negative determinant defect**.

## 10. Delayed states, collars, and reserve accounting

The safe scale ledger is:

```text
current-scale compact innovation:
    I_circ(n,j)

predecessor normalized state:
    U(n,j)

next state:
    U(4n,4j) = U(n,j)/2 + I_circ(n,j)/(2 sqrt(n))

delayed gauge:
    L_(n,j)(b4), one radix-four step behind

integer endpoint:
    predecessor carry row + explicit endpoint atom

fixed filter/cut collars:
    polynomial, but must be included in the global block statement
```

No reviewed exact identity returns the delayed gauge as a new
current-scale reserve. The deterministic Q4 reserve is already charged
in the local augmented-curvature/inertia estimate. Reusing it as an
independent payment for PIG would be double spending. The terminal
terms are plausibly polynomial and several fixed-collar estimates are
proved, but the final theorem must state one measure, one pushforward,
one state orientation, and all terminal terms simultaneously.

## 11. Pole preservation

The pole firewall has two sides.

**Rejected:** direct pure carry-window transference. Its extra zeta
factor cancels the reciprocal-zeta pole (#269).

**Surviving:** compact Q4 innovation. For a hypothetical zero
\(\rho\), \(0<\Re\rho<1\),

\[
(4^\rho-4)(1-2^{1-\rho})\ne0.
\]

The own compact current has pole order \(m+1\); the delayed gauge has
order \(m\). No finite source multiplier used in the corrected compact
path cancels the leading pole. This establishes visibility, not an
energy upper bound.

## 12. Exact new review counterexamples

### 12.1 Coefficient budget is not an operator contraction

At \(z=2^{-1/2}\), direct exact evaluation of the submitted #346
filters gives

\[
S=
\frac{751606691}{24000000}
-
\frac{277818163}{18000000}\sqrt2.
\]

Moreover,

\[
S-\frac25
=
\frac{2226020073-1111272652\sqrt2}{72000000}>0
\]

because

\[
2226020073^2-2(1111272652)^2
=
2485311551232699121>0.
\]

Thus the frequencywise synthesis norm is not \(<2/5\). The retained
checker certifies a weighted coefficient sum and the true joint
jet-frame inequality; it does not certify #359's operator hypothesis.

### 12.2 Bounded nonconstant multipliers do not transfer inertia masses

On the critical line let

\[
M(t)=\frac1{1-\frac12e^{-it\log4}},
\qquad
|M(t)|^2=\frac1{5/4-\cos(t\log4)}.
\]

Choose identical disjoint bumps \(a\) near \(t=0\) and
\(b(t)=a(t-\pi/\log4)\). Put

\[
d_\tau=(a+b)+\frac{\tau^2}{2}(-a+b).
\]

At \(\tau=0\), the first derivative vanishes and the integrated scalar
curvature is

\[
\|a\|_2^2-\|b\|_2^2=0.
\]

After multiplying the whole path by \(M\), the curvature is weighted by
\(|M|^2\). On corresponding support points near zero,

\[
|M(t)|^2>|M(t+\pi/\log4)|^2,
\]

so the integrated curvature becomes strictly positive. Reversing the
signs makes it strictly negative. Hence neither positive nor negative
spectral mass of the integrated indefinite curvature is bounded by
four times the corresponding mass before multiplication. The
hypothesis \(\|M\|_\infty\le2\) is insufficient.

## 13. Retained experiments inspected but not rerun

No heavy experiment, endpoint campaign, exhaustive transform search,
large interval computation, optimization sweep, or large formal build
was rerun.

The following retained artifacts were inspected for scope, outputs, and
hashes:

| Artifact | Retained scope | Proof-object/output hash |
|---|---|---|
| `X-9515` | independent-frequency bireflected identity regression | `c194c7cdcc5a13cf69baaed6cdf798666656b925ddfd07f614106c7a1a591165` |
| `X-32402` | Q4 reserve finite range; 2,803,709 rows | `570d1302e47ad299f0854b407c1aa8cf477aca76ad3629e0e8838d9a3073feeb` |
| `X-34401` | compact parity finite synthesis | `05fbc3e49a729957d3253593d566e131f100964d1ac80144b4ae423c47ffd65e` |
| `X-34401` jet frame | joint parity/current jet-frame regression | `4a4c3cffc2b803827776066aaab27bb8d058a31ad0bac3fe41e1f3b8654982b` |
| `X-90301` | all-pass, Wronskian, relative, and zero-bare finite identities | `9d0aa825298a48412cf9b856ca57dea096231eb07d6aab5bc1c51a4ae419cee5` |
| `X-90302` | 32,268 exact finite Hermitian aggregate cases | `11dd103d5c25fe22dc9dfbe81bd9e85a85f200ad1e066a2b02b2e0868aec171a` |
| `X-90402` | 384 coefficient/prefix identities and 4,560 filtered-Chebyshev/gauge rows | retained PASS record; no claim of RH |
| `X-29002` | vector pole-energy frame regression | `aaccceaed2de644025ce6a7e97bfb8ca25ae9da213da2987eee0d0dff1e12d29` |

These artifacts certify only their finite algebraic or enumerated
scope. None certifies PIG, the global Q4 recurrence, pole exclusion
from PIG, or RH.

A lightweight exact symbolic reconstruction was performed only for the
two counterexamples in Section 12.

## 14. Recommended integration actions

1. Integrate the exact independent-frequency identities, source-typing
   corrections, physical/carry placement, reserve identities,
   zero-bare source, all-pass state identities, inertia lemmas, and
   refutations while preserving their historical supersession chain.
2. Mark #359's full proposed theorem **FALSE** and **SUPERSEDED**. Its
   aggregate determinant lemma may survive independently.
3. Demote #357's “complete assembly outside PIG” claim to
   **UNPROVEN / GAP** until:
   - `L-90308.12` is removed or replaced;
   - the actual fixed-filter source substitution is proved in one
     metric;
   - the final reservoir negative mass and collars are bounded;
   - one exact block pushforward recurrence is stated and proved.
4. Retain #362 as the corrected frontier, but label the full PIG
   equivalence conditional until a direct Q4-PIG-to-pole-energy adapter
   is written.
5. Never infer an operator contraction from a coefficient budget.
   Use the actual joint jet-frame inequality or prove a genuine
   frequencywise matrix inequality.
6. Keep ordinary prefix, divisor convolution, Selberg carry, and
   physical endpoint placement as distinct typed operations.
7. Use negative inertia only as bad-spectrum bookkeeping; do not market
   it as positive-current control.
8. Do not spend the critical Selberg/Kummer reserve twice.
9. Preserve the #269 pole-cancellation firewall and require explicit
   nonvanishing for every final finite source multiplier.
10. Do not integrate or advertise any unconditional RH conclusion.

## 15. Final classification

| Object | Mathematical type | Review verdict |
|---|---|---|
| Reflected-Selberg independent-frequency identities | ROUTE INFRASTRUCTURE / UNCONDITIONAL THEOREM | VERIFIED |
| Corrected source/carry and physical-placement identities | ROUTE INFRASTRUCTURE / UNCONDITIONAL THEOREM | VERIFIED WITH FIXES |
| Q4 reserve and compact zero-bare infrastructure | ROUTE INFRASTRUCTURE | VERIFIED WITH FIXES |
| Local and aggregate inertia lemmas | UNCONDITIONAL THEOREM | VERIFIED at negative-mass scope |
| #359 full RH composition | PROPOSED COMPLETE THEOREM | FALSE; SUPERSEDED |
| #357 complete assembly outside PIG | PROPOSED COMPLETE THEOREM | UNPROVEN / GAP |
| #362 RH implies PIG | CONDITIONAL IMPLICATION | VERIFIED |
| #362 full PIG equivalence | RH-EQUIVALENT CRITERION | UNPROVEN / GAP at reviewed SHA |
| Unconditional PIG | RH-EQUIVALENT CRITERION | UNPROVEN / GAP |
| Riemann Hypothesis | — | **NOT ESTABLISHED** |
