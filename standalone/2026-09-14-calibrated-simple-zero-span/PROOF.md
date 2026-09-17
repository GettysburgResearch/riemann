# Calibrated span charge in the seven-point simple-zero argument

Date: 2026-09-14.

**Status: proposed complete proof of a modest unconditional proportion bound,
subject to independent mathematical and implementation review. Not an RH proof,
not a world-record claim, and not a new abstract theory of zero counting.**

The statement proved here is about zeros with ordinates in `(0,T]`. A new
uniform dyadic-window theorem is not claimed. The original repository's
stronger dyadic-window results imply the corresponding global bounds, so their
numerical constants provide a legitimate global comparison.

Let `N(T)` count nontrivial zeta zeros with `0 < Im rho <= T`, with analytic
multiplicity; let `S(T)` count those that are simple and have `Re rho=1/2`.
The proposed conclusion is

\[
 \liminf_{T\to\infty}\frac{S(T)}{N(T)}\ge C_*>
 \frac{6730129}{10000000},                                      \tag{1}
\]
where
\[
\begin{split}
 H&=\frac32-\frac1{\sqrt2}\cot(1/\sqrt2),\qquad q=\frac{1501}{1250},\\
 c&=2\sqrt{\frac{481821}{402500}}-1+\frac{1501}{402500},\\
 C_*&=\frac{H-\dfrac{1605}{966644}c}{1-c/322}
      =0.673012903898232480616262\ldots.                         \tag{2}
\end{split}
\]
All square roots are the positive ones. Thus the proposed numerical statement
is **67.3012903898... percent simple critical-line zeros**, not a percentage of
RH proved. A distinct-zero corollary is recorded in Section 8.

There are two explicitly imported mathematical inputs. The first is the
published unconditional BGST pair-correlation theorem [BGST], used only in its
actual unconditional scope. The second is the computer-assisted seven-point
inequality of [AINTA], independently implemented in Reviewer A's supplement
[RA]. The exact latter implementation is included and freshly replayed here.
Classical zeta symmetries and Riemann--von Mangoldt are also used. Everything
connecting these inputs to (1) is supplied below; no unknown sign, energy, or
asymptotic estimate is left as a premise.

The new extraction step is Section 2: replace a unit coefficient on the span
penalty by the smaller coefficient `c/q`. The finite rank inequality,
seven-point pressure, Fourier profile, and pair-correlation method are prior
work and are credited. Section 5 gives a direct Hilbert-space realization of
the rank inequality. Section 6 reconstructs the deweighting argument also
used in Lamzouri's Hilbert-space proof [LAM]. This is not a priority claim for
that mechanism, and no novelty claim is made for general spectral convexity.

**Benchmark qualification.** The pinned repository's 280-block extraction gives
`0.673009652279136912...`. The present extraction is strictly larger, by
`0.00000325161909556860...` as a fraction. A publicly posted Michael Devine
preprint [DEV] claims the larger number `0.673399`. Its proof and numerical
certificate were not accessible for full review in this pass. Regardless of
its disposition, (1) is not advertised as a current world record or as an
improvement on [DEV].

## 1. The inherited finite pressure inequality

Put
\[
 K(x)=\int_{-1/2}^{1/2}\cos(\sqrt2 u)\cos(2\pi xu)\,du,
 \quad K_0=\sqrt2\sin(1/\sqrt2),\quad k(x)=K(x)/K_0,
 \quad w(x)=k(x)^2.
\]
The seven-point theorem [AINTA, RA] is the following statement for **all**
nonnegative real gaps `g_1,...,g_6`:
\[
 \frac1{3000}\sum_{i=1}^6g_i+
 \sum_{s=1}^6\frac2{7-s}\sum_{i=1}^{7-s}
 w(g_i+\cdots+g_{i+s-1})\ge\frac{19}{5000}.              \tag{3}
\]
The verification covers a continuum, not only grid points. Section 9 describes
the complete search and its numerical trust boundary. Neither this pass nor
the included code claims to have newly discovered (3).

For ordered real points `y_1 <= ... <= y_m`, let
\[
 G_m=(k(y_i-y_j))_{i,j=1}^m,\quad
 E_m=\|G_m-I\|_F^2=2\sum_{i<j}w(y_j-y_i),\quad
 \ell=y_m-y_1,\quad q_m=\frac{19(m-6)}{5000}.
\]
This is a positive semidefinite matrix with diagonal exactly one: the
nonnegative measure `cos(sqrt(2)u)du/K_0` on `[-1/2,1/2]` gives its Gram
representation. In particular its trace is exactly `m`.

Sum (3) over every consecutive seven-point window. A pair at index separation
`s <= 6` occurs at most `7-s` times and therefore contributes at most `2w` to
the sum. Every gap occurs at most six times; pairs of larger index separation
in `E_m` are nonnegative. Consequently
\[
             E_m+\ell/500\ge q_m.                       \tag{4}
\]
No lower separation assumption and no upper bound on `ell` are used.

## 2. The calibrated spectral lemma

For a positive semidefinite matrix `G` of size `m` and trace `m`, set
\[
 E=\operatorname{tr}(G-I)^2,\qquad
 \Delta(G)=\operatorname{tr}\Psi(G),\qquad
 \Psi(t)=\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2.\end{cases}
\]
The scalar `Psi` is convex and nonnegative. Fix
\[
             \frac m{m-1}<q<2,
 \qquad c=2\sqrt{\frac{m-1}{m}q}-1+\frac qm.              \tag{5}
\]
Then `0<c<q`.

**Proposition 1.** For every such matrix and every `z>=0`,
\[
 E+z\ge q\quad\Longrightarrow\quad
             \boxed{\Delta(G)+\frac cq z\ge c.}          \tag{6}
\]
This improves the older implication `Delta+z>=c`. It does not claim optimality
for the much smaller class of Gram matrices of the specific kernel.

*Proof.* Write the eigenvalue deviations as `x_i=lambda_i-1`. They sum to zero,
are at least `-1`, and have sum of squares `E`. For `E<2`, at most one `x_i`
can exceed one. If none exceeds one, `Delta=E`. If one is `a>1`, then
\[
 E\ge a^2+a^2/(m-1)=\frac m{m-1}a^2,
 \qquad \Delta=E-(a-1)^2.
\]
It follows that for `0<=E<=q`,
\[
\Delta\ge\phi_m(E):=
\begin{cases}
E,&E\le m/(m-1),\\
2\sqrt{(m-1)E/m}-1+E/m,&m/(m-1)\le E\le q.
\end{cases}                                               \tag{7}
\]
This inherited one-large-eigenvalue estimate is increasing and concave; its
one-sided derivatives agree at the joining point. Since `phi_m(0)=0` and
`phi_m(q)=c`, concavity gives `Delta>=cE/q` when `E<=q`.

If `E>=q`, let `theta=sqrt(q/E)` and replace `G` by
`G_theta=I+theta(G-I)`. This matrix remains positive semidefinite with trace
`m`, and its squared deviation is `q`. For every permitted deviation `x`,
`Psi(1+theta x)<=Psi(1+x)`: for `x<=0` both are on the quadratic branch; for
`x>=0` both branches are increasing in the nonnegative deviation. Therefore
`Delta(G)>=Delta(G_theta)>=c`. We have proved
\[
                  \Delta(G)\ge c\min(E/q,1).              \tag{8}
\]
For `E<=q`, add `(c/q)z` and use `E+z>=q`; for `E>=q` use `z>=0`.
This proves (6). In particular the case `E>=2` is paid, not discarded. QED.

The coefficient in (6) is best possible when the intercept is held at `c`
and only these scalar data are allowed. At `G=I,z=q`, any inequality
`Delta+slope*z>=c` requires `slope>=c/q`. The intercept itself is attained
at `z=0` by an equicorrelation Gram matrix with off-diagonal value
\[
 r=\sqrt{q/[m(m-1)]}.
\]
Its eigenvalues are `1+(m-1)r` and `1-r` repeated `m-1` times. Its energy is
`q` and its defect is exactly `c`. These endpoint examples do not assert that
these matrices arise from actual zeta ordinates.

Applying (6) to (4) gives the block estimate
\[
          \Delta(G_m)\ge c_m-\frac{c_m}{500q_m}\ell,
 \quad c_m=\phi_m(q_m),                                  \tag{9}
\]
whenever `m/(m-1)<q_m<2`.

## 3. Exact block averaging and the endpoint loss

Let `G_p` be the same kernel Gram on `p` ordered real points in an interval of
length `L`. For each of the `m` possible offsets, partition into consecutive
full `m`-blocks and leftover points. Pinching into those principal blocks
cannot increase a convex spectral trace: it is an average of unitary
conjugates, and `tr Psi` is convex. The leftover contribution is nonnegative.
Thus `Delta(G_p)` is at least the sum of (9) over the full blocks of any one
partition.

Across all offsets every possible block start `1,...,p-m+1` occurs exactly
once. Each gap appears in at most `m-1` of these block spans. Averaging yields
\[
 \boxed{
 \Delta(G_p)\ge\frac{c_m}{m}(p-m+1)
          -\frac{c_m(m-1)}{500q_m m}L.}                   \tag{10}
\]
When `p<m`, the right side is nonpositive and the statement follows from
`Delta>=0`. This includes the empty set by taking its defect and span as zero.
The `m-1` endpoint count is retained; it is eventually `O(1)`, not initially
set to zero.

The same argument applies to any positive definite normalized profile with
an analogous pressure input. A small perturbation of the profile is handled
explicitly in Section 7.

## 4. The inherited stability rank inequality

This section reconstructs the finite linear-algebra ingredient [AINTA,
Section 2]. Let `V` have `p` columns of norm at most one, let `P=VV*`, and let
`Q` be Hermitian with positive index at most `b`. Set `G=V*V`. Then
\[
 \|P+Q\|_F^2\ge4\operatorname{tr}(P+Q)-3p-4b+\Delta(G).
                                                               \tag{11}
\]
It applies in a finite-dimensional ambient space containing the ranges, so
it also applies to the finite-rank operators below.

For completeness, write `Q=Q_+-Q_-`, with positive parts of orthogonal ranges.
Since `tr(PQ_+)>=0`,
\[
 \|P+Q\|_F^2\ge\|P-Q_-\|_F^2+\|Q_+\|_F^2,
 \qquad \|Q_+\|_F^2\ge4\operatorname{tr}Q_+-4b.
\]
If `p_i` are the eigenvalues of `G` (with zero padding as needed) and `n_i`
those of `Q_-`, von Neumann's trace inequality gives
\[
 \|P-Q_-\|_F^2+4\operatorname{tr}Q_-
 \ge\sum_i\big[(p_i-n_i)^2+4n_i\big].
\]
The minimum of the summand over `n_i>=0` equals
`2p_i-1+Psi(p_i)`. A zero-padded `p_i=0` contributes zero to this expression,
so the different dimensions cause no omitted term. Thus
\[
 \|P-Q_-\|_F^2\ge2\operatorname{tr}P-p+\Delta(G)
                         -4\operatorname{tr}Q_-.
\]
Combine the inequalities and use `tr P<=p` to obtain (11). The spectral
stability term, not a new positive-prime assumption, is the source of the
improvement over the scalar rank bound.

## 5. An exact finite-multiset Hilbert realization

Choose a real, even, nonnegative `p` in `C_c^infty(-1/2,1/2)` with integral
one, and write
\[
 k_p(z)=\int p(t)e^{2\pi izt}\,dt.
\]
Let `Z` be any finite conjugation-invariant multiset, with positive integer
multiplicities equal at conjugate points. Denote total multiplicity by `M`
and the number of simple real points by `S`. On complex `L^2(dt)` put
\[
 v_z(t)=\sqrt{p(t)}e^{2\pi izt},\qquad
 A=\sum_{z\in Z_{\rm distinct}}m_z\,v_zv_{\bar z}^{*}.       \tag{12}
\]
Our inner product is conjugate-linear in the first argument, and `uv*` maps
`f` to `u <v,f>`. Conjugation of the multiset proves `A=A*`. Direct finite
calculation gives
\[
 \operatorname{tr}A=M,\qquad
 \|A\|_{HS}^2=\operatorname{tr}A^2
   =\sum_{z,w}m_zm_w k_p(z-w)^2=:\mathcal E_p.             \tag{13}
\]
The norm of an individual nonreal vector need not be one. The trace identity
instead uses `<v_barz,v_z>=1`. The simple-real vectors do have norm one.
The double sum is real and nonnegative as a whole; its individual terms need
not be nonnegative or even real.

Take `P` to be the sum of the unit rank-one contributions from simple real
points. In `Q=A-P`, each distinct multiple real point contributes positive
index at most one. A nonreal conjugate pair contributes positive index at
most one because it is the difference of two positive rank-one operators.
Hence
\[
             n_+(Q)\le b\le(M-S)/2.
\]
Applying (11), with `G_S` the exact Gram of the simple-real vectors, yields
\[
             \boxed{S\ge2M-\mathcal E_p+\Delta(G_S).}     \tag{14}
\]
This is the stability-refined form of the finite Hilbert-space mechanism in
[LAM]. Equation (12) is a direct realization, not a finite Gabor compression;
there is no approximate diagonal normalization or unproved transfer between
different source matrices.

## 6. The unconditional analytic input and exact removal of its weight

For actual zeta zeros `rho=beta+i gamma` with `0<gamma<=T`, counted with
multiplicity, set
\[
 z_\rho=\frac{(\rho-1/2)\log T}{2\pi i},\qquad
 N_*(T)=\frac{T\log T}{2\pi},\qquad W(u)=\frac4{4-u^2}.
\]
Functional-equation reflection makes the `z_rho` multiset conjugation invariant.
Its real points are precisely the critical-line zeros. Its real-point span is
at most `N_*(T)`. The classical Riemann--von Mangoldt formula gives
`N(T)/N_*(T)->1`.

The exact imported statement is [BGST, Theorem 1 / Lemma 5]: for each fixed
real even integrable `r` supported in `[-1,1]`, Lipschitz at zero,
\[
 \frac1{N_*}\sum_{\rho,\rho'}
 \widehat r\!\left(\frac{i(\rho-\rho')\log T}{2\pi}\right)
 W(\rho-\rho')
 \longrightarrow r(0)+2\int_0^1 u r(u)\,du,               \tag{15}
\]
where `hat r(z)=int r(u)exp(-2pi iuz)du`. Both sums are ordered and retain all
multiplicities. This is their unconditional theorem, not their separate
simple-zero corollary with a thin-box hypothesis. The imported proof and all
its prime/archimedean terms are not rerun by our finite code.

Put `g=p*p`. The test
\[
                  r_T=g-\frac{g''}{4(\log T)^2}
\]
has the exact Fourier identity
\[
 \widehat r_T\!\left(\frac{i(\rho-\rho')\log T}{2\pi}\right)
 W(\rho-\rho')
 =k_p(z_\rho-z_{\rho'})^2.                               \tag{16}
\]
Indeed `hat g=k_p^2` by evenness, and Fourier differentiation contributes
`-4pi^2 z^2`; the factor on the left before multiplication by `W` is exactly
`1-(rho-rho')^2/4`. No denominator vanishes for two zeros in the critical strip.

There is no appeal to (15) uniformly over unspecified changing tests. Apply
(15) separately to the two **fixed** smooth tests `g` and `g''`, then multiply
the second answer by `-1/[4(log T)^2]`. It follows that
\[
 \frac{\mathcal E_p(T)}{N(T)}\longrightarrow C(p),\qquad
 C(p)=\int p(u)^2du+\iint|u-v|p(u)p(v)\,du\,dv.            \tag{17}
\]
This reconstructs the deweighting mechanism recorded in [LAM]. In particular,
there is no remaining RH-strength analytic estimate behind (17).

## 7. Passing to the Montgomery--Taylor profile and completing (1)

The nonsmooth limiting density is
\[
 p_0(u)=\frac{\cos(\sqrt2u)}{K_0}\mathbf1_{[-1/2,1/2]}(u).
\]
Take even nonnegative smooth cutoffs `chi_j`, supported strictly in that
interval, with `chi_j -> 1` pointwise in its interior. Normalize
`chi_j^2 cos(sqrt(2)u)` to integral one, obtaining smooth densities `p_j`.
They converge to `p_0` in both `L^1` and `L^2`. Equivalently each density is a
square of a smooth compactly supported even function, as in [LAM].

Let `epsilon_j=||p_j-p_0||_1`. For all real `x`,
\[
 |k_{p_j}(x)-k(x)|\le\epsilon_j,\qquad
 |k_{p_j}(x)^2-k(x)^2|\le2\epsilon_j.                     \tag{18}
\]
Both transforms have absolute value at most one on the real axis. Consequently
for each fixed block size `m`, its squared deviation satisfies
\[
 E_{m,j}+\ell/500\ge q_{m,j}:=q_m-2m(m-1)\epsilon_j.      \tag{19}
\]
Eventually `m/(m-1)<q_{m,j}<2`, so all of Sections 2--3 apply with
`c_{m,j}=phi_m(q_{m,j})`. This pays the entire finite-profile perturbation
before the zero-height limit; it does not use uniformity in a growing block.

Write
\[
 \alpha_j=c_{m,j}/m,\qquad
 \beta_j=\frac{c_{m,j}(m-1)}{500q_{m,j}m}.
\]
Equations (10), (14) and the real span bound give for every sufficiently large
`j`, fixed before `T` tends to infinity,
\[
 (1-\alpha_j)S(T)
 \ge2N(T)-\mathcal E_{p_j}(T)-\beta_j N_*(T)-O_m(1).
\]
The constants are positive with `alpha_j<1`. Therefore
\[
 \liminf_{T\to\infty}\frac{S(T)}{N(T)}
 \ge\frac{2-C(p_j)-\beta_j}{1-\alpha_j}.                 \tag{20}
\]
Now let `j` tend to infinity. Continuity of (17) in these `L^1,L^2` norms gives
`C(p_j)->C(p_0)`; the support is fixed and the distance kernel is bounded.

For clarity the value of `C(p_0)` can be evaluated without importing an
optimized numerical constant. On the interval set
\[
 Lp_0(u)=p_0(u)+\int_{-1/2}^{1/2}|u-v|p_0(v)\,dv.
\]
Its second derivative in the interior is `p_0''+2p_0=0`. It is even, hence
constant. Its continuous boundary value at `u=1/2` is
\[
 C(p_0)=\frac12+\frac{\cos(1/\sqrt2)}{\sqrt2\sin(1/\sqrt2)}
        =2-H.                                           \tag{21}
\]
The integral of `p_0 Lp_0` equals `C(p_0)`, because `int p_0=1`.
Choose the single fixed block size `m=322`. Then `q_m=1501/1250`, and
\[
 c_m=2\sqrt{481821/402500}-1+1501/402500,
 \quad\alpha=c_m/322,
 \quad\beta=(1605/966644)c_m.
\]
Taking `j->infinity` in (20) proves (1)--(2). No limit uniform in `m` or in
an unknown high zero is used. All actual off-line zeros remain in the finite
Hermitian operator and the full ordered BGST sum. QED.

The exact-rational verifier brackets the value in (2) between
`0.673012903898232480616262` and
`0.673012903898232480616263`. It also brackets the old 280-block constant
between `0.673009652279136912013711` and
`0.673009652279136912013712`. The inequality between them is certified without
floating transcendental inputs. The choice 322 was found by noncertifying
exploration; the proof only needs this prescribed integer and makes no claim
that it is globally optimal over other inequalities, profiles, or block sizes.

## 8. Distinct zeros: optional corollary, with multiplicities retained

Let `D(T)` count distinct nontrivial zeros in `(0,T]`, whether on or off the
critical line. In Section 5 one also has `b<=D-S`, hence (11) gives
\[
             D\ge M+S/4+\Delta/4-\mathcal E_p/4.           \tag{22}
\]
Combine with (14) to get `D>=3M/2-E_p/2+Delta/2`. The same block lower bound,
and (20) for the simple fraction, then imply
\[
 \liminf_{T\to\infty}\frac{D(T)}{N(T)}
       \ge\frac{1+C_*}{2}
       =0.836506451949116240308131\ldots.                 \tag{23}
\]
For the algebra, at a fixed smooth profile put `H_j=2-C(p_j)` and
`C_j=(H_j-beta_j)/(1-alpha_j)`. Then
`alpha_j C_j-beta_j=C_j-H_j`, giving `(1+C_j)/2` in (22).
Letting `j->infinity` proves (23). This is a lower bound for distinct zeros,
not for simple off-line zeros separately, and not a claimed record.

## 9. Computer-assisted input and fresh verification boundary

The code in `pressure/` is copied byte-for-byte from the Reviewer A supplement,
not a newly independent implementation in this pass. It proves (3) with a
complete branch-and-bound exhaustion and returns no unresolved terminal cell.
Its primitive kernel is
\[
 K(x)=\tfrac12[\operatorname{sinc}(\pi x-1/\sqrt2)
                   +\operatorname{sinc}(\pi x+1/\sqrt2)].
\]
Machin arctangent series supply pi enclosures; integer square roots supply
radicals; degree-49 sine/degree-48 cosine polynomials with full remainders,
range reduction and Lipschitz widening supply trigonometric enclosures.
All these primitives use outward 128-bit dyadics. The range-minimum and some
accumulation operations use outward binary64 arithmetic with `nextafter`.
This is **not** an integer-only full pressure verification. Ordinary floating
LDL is only a rejection screen; every accepted Hessian floor is checked using
the dyadic LDL routine. The supplied implementation assumes correctly rounded
CPython/IEEE-754 operations as described in the inherited review.

If `sum g_i>=57/5`, the linear term alone proves (3). Otherwise the search
starts from closed gap cells of width `1/4000`. The independently rebuilt
one-gap filter retains exactly the three cell ranges
`[3809,4778]`, `[7221,9364]`, `[10571,44827]`. Their sixth Cartesian power is
covered by 729 initial boxes. Span sums use the extra `s-1` cells required by
endpoint addition. Every unaccepted box is split into its two closed children;
a final unproved single cell raises an error, not an accepting verdict.

A Hessian floor is a sum of signed incidence outer products. Each difference
from the actual Hessian is a **nonnegative scalar times a positive rank-one
matrix**. Thus it is a valid Loewner lower bound, not an arbitrary entrywise
matrix comparison. The tangent test pays every gradient-radius contribution.
Table queries beyond the computed range use only `w>=0`, not an extrapolated
curvature value.

Fresh normal and optimized replay details are recorded in VALIDATION.md.
The certified tree has 713315 nodes: 3072 linear-pressure leaves, 259807
interval leaves, 94143 convex-tangent leaves, and 356293 splits. The identities
`nodes=729+2*splits` and `leaves=729+splits` hold. It is a different implementation
and transcript from the ainta Arb implementation's 707901-node record. The
old independent-replay provenance is retained rather than silently conflated.

`check_constants.py` separately uses exact fractions, alternating series for
cos(u) and sinc(u) at `u^2=1/2`, and rational square-root brackets. It rebuilds
(2), the strict improvement, and bounded offset-count fixtures. It does not
prove BGST or replace the written spectral argument.

## 10. Dependencies, novelty boundary, and review questions

[BGST] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh,
*An unconditional Montgomery theorem for pair correlation of zeros of the
Riemann zeta function*, Acta Arithmetica 214 (2024), 357--376;
arXiv:2306.04799v1, Theorem 1 and Lemma 5. The theorem statement, exact
normalizations and its test-function deduction were read in the primary PDF,
including page images. The entire external analytic proof was not independently
reproved. URL: https://arxiv.org/abs/2306.04799

[AINTA] ainta/zeta-simple-zeros at commit
`040c5e899e658aed7b56a2a87f501798fe10761d`, especially `paper/riemann.tex`,
Sections 2--4; seven-point finite pressure and stability-refined rank inequality.
The proposed 269-block result is not a new result of this pass. URL:
https://github.com/ainta/zeta-simple-zeros/tree/040c5e899e658aed7b56a2a87f501798fe10761d

[RA] GettysburgResearch/riemann, frozen main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`,
`reviews/A/supplement/REPORT.md`, Sections S01--S02 and the exact two-file
independent pressure implementation supplied with that supplement. The
spectral function (7) and the 280-block extraction were already present.
This pass's change is (6), with its improved span coefficient, and its use in
(10), not a claim that the prior core inequality or finite pressure is new.

[LAM] Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the
Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1.
The repository import at `a9c7b44f908c90f63d2f49a5fde58face5921e42`,
`research/exploratory/lamzouri-zeta-zeros-2026-09-02/PAPER_DIGEST.md`, and the
primary abstract were read. The original PDF could not be freshly opened in
this pass. No formal Lean/Comparator replay is claimed. Sections 5--6 above
are written out independently, using only BGST as their analytic input.
URL: https://arxiv.org/abs/2609.02882

[AF] Claude, *More Than Two Thirds of the Zeros of the Riemann Zeta Function
Lie on the Critical Line*, version dated August 10, 2026, communicated and
verified by Levent Alpoge and Alex Furman. Its Theorem D is the optimized
rank--trace background used by AINTA. The present global argument instead
uses (12)--(17), so it does not introduce an unproved finite-grid adapter.
The read primary PDF is at
https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf

[DEV] Michael Devine, *An Unconditional 67.3399% Bound and Conditional Advances
Beyond 67.92% for Simple Critical Zeros of the Riemann Zeta Function*, Zenodo
22066689, version 1.0.3. Its author-posted description claims `0.673399` and
uses several profiles and a finite verified subaction. Only the primary
metadata/abstract was retrieved; the paper and certificate were NOT audited.
It is a benchmark warning, not a theorem imported into this proof.
URL: https://zenodo.org/records/22066689

Review should concentrate on (6)'s case `E>=q`, the exact coefficient of the
span in (10), the conjugate rank-one convention in (12), the sign/factor four
in (16), and the order of the fixed-profile and large-height limits. The
pressure backend needs its own implementation review. No proof assistant,
repository-wide scientific audit, new high-zero computation, RH completion,
record claim, or exhaustive novelty search is represented by this packet.
