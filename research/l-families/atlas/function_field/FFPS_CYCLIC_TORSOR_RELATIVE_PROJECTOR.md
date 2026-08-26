# Cyclic torsor lift of the relative principal projector

Status: **exact endomorphism theorem on every genuine finite cyclic torsor;
the global varying-place FFPS torsor and its uniform trace estimate remain
open**

Scope: finite etale geometry and cyclic Fourier algebra; no finite-field
family, conductor, curve, L-function, or zero enumeration

Exact replay:
[`ffps_cyclic_torsor_relative_projector.py`](ffps_cyclic_torsor_relative_projector.py)

Frozen dependencies:

| source | commit | git blob | role |
|---|---|---|---|
| `FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md` | `271ff4316` | `6c63def72b340f69be9caff41a619f23d2b66fd1` | all-`k` kernels and finite-fibre projector |
| `FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md` | `8b4559a54` | `d531ef36d314549072052cc5b1ae1762c11d00e2` | fixed physical-fibre Kummer adapter |
| `FFPS_PRINCIPAL_ANOMALY_TRANSFER_DICHOTOMY.md` | `806f8c000` | `47c148187db578357035926f8ff12419b0cf3652` | exact principal-channel interpretation |

## 0. Outcome

The relative identity discovered in
[`FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md`](FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md)
does not need to remain a scalar-extended formal `K_0` criterion at a fixed
cyclic fibre.

Let `k` be invertible on a base `U`, assume that `mu_k` is split on `U`
(equivalently, fix the constant cyclic deck group `C_k`), let `E` be a
characteristic-zero coefficient field containing the `k`-th roots of unity,
and let

\[
 \pi:T\longrightarrow U
\]

be a genuine torsor under the split group scheme
`mu_k isomorphic to (C_k)_U`.  (The torsor itself need not be trivial.)  Put

\[
 \mathcal H=\pi_*E_T.
\]

The deck action makes `H` the regular `E[C_k]` local system.  For every
nonempty retained set `S subset mu_k`, there are **honest endomorphisms**

\[
 \mathsf C_S,\mathsf S_S,\Pi_0\in
 \operatorname{End}_E(\mathcal H)
\]

such that

\[
 \boxed{\mathsf C_S-\mathsf S_S=\Pi_0.}
\tag{0.1}
\]

Here `C_S` is the normalized hard autocorrelation operator, `S_S` is its
nonconstant selected-character part, and `Pi_0` is the invariant projector.
Moreover,

\[
 \boxed{\operatorname{im}\Pi_0\simeq E_U.}
\tag{0.2}
\]

Thus the relative cancellation is geometric wherever the physical mask is
actually carried by one cyclic torsor.  It is an equality of endomorphisms,
not merely equality of traces, equality of invariant multiplicities, or a
virtual sheaf with fractional multiplicities.

Every common `E`-linear functorial cleanup preserves (0.1).  In particular,
restriction, extension by zero, derived pushforward with compact supports,
and cones of compatible equivariant maps preserve the relative projector
when they are applied to both terms on the same source object:

\[
 \boxed{
 F(\mathsf C_S)-F(\mathsf S_S)=F(\Pi_0).
 }
\tag{0.3}
\]

This resolves one local categorical question and exposes the global one.
The remaining FFPS burden is to construct a single varying-place physical
torsor/correspondence on which:

1. the actual hard source trace is `C_S`;
2. the actual selected Kummer trace is `S_S`;
3. every diagonal, equal-product, root, incidence, and constant cleanup is
   common and equivariant;
4. the resulting pushed-forward complexes have conductor-uniform complexity.

No such global object or uniform estimate is constructed here.  Even after
(0.1), the remainder is the principal object itself, so no RH-bearing bound
has become formal.

## 1. Exact finite cyclic algebra

Write `G=mu_k`, let `t=|S|`, and define

\[
 c_r={1\over t}\sum_{s\in S}s^{-r},
 \qquad 0\le r<k.
\tag{1.1}
\]

Algebraically, `|c_r|^2` means `c_r c_{-r}`.  It lies in `E` and does not
require an analytic embedding.

For `g in G`, define the hard and selected kernels

\[
 K_C(g)={k\over t^2}|S\cap gS|,
 \qquad
 K_S(g)=K_C(g)-1.
\tag{1.2}
\]

The all-`k` Fourier theorem in the dependency packet gives

\[
 K_C(g)=\sum_{r=0}^{k-1}c_rc_{-r}g^r,
 \qquad
 K_S(g)=\sum_{r=1}^{k-1}c_rc_{-r}g^r.
\tag{1.3}
\]

Choose the right-regular deck convention
`rho(g)e_h=e_(hg)` on a deck-labelled fibre basis of `H`.  For the character
`chi_r(g)=g^r`, put

\[
 \Pi_r={1\over k}\sum_{g\in G}\chi_r(g)^{-1}\rho(g).
\tag{1.4}
\]

Character orthogonality proves

\[
 \Pi_r\Pi_s=\delta_{r,s}\Pi_r,
 \qquad
 \sum_r\Pi_r=1_{\mathcal H}.
\tag{1.5}
\]

Now define

\[
 \mathsf C_S=\sum_{r=0}^{k-1}c_rc_{-r}\Pi_r,
 \qquad
 \mathsf S_S=\sum_{r=1}^{k-1}c_rc_{-r}\Pi_r.
\tag{1.6}
\]

Since `c_0=1`, subtraction gives (0.1) immediately.  Equivalently,

\[
 \mathsf C_S={1\over k}\sum_{g\in G}K_C(g^{-1})\rho(g),
 \qquad
 \mathsf S_S={1\over k}\sum_{g\in G}K_S(g^{-1})\rho(g).
\tag{1.7}
\]

Equation (1.7) identifies these endomorphisms with the exact hard and
selected pair kernels.  It also shows directly that their difference is

\[
 {1\over k}\sum_{g\in G}\rho(g)=\Pi_0.
\]

The construction uses scalar endomorphisms, not scalar object
multiplicities.  Consequently there is no integrality obstruction from a
coefficient such as `|c_r|^2=1/4`.

## 2. Why the invariant image is the principal local system

The torsor is etale-locally `G x U`, so `H` is etale-locally the regular
representation.  Its invariant line is generated by the sum of the `k`
deck-labelled basis vectors.  Descent identifies that line canonically with
the constant sheaf:

\[
 \mathcal H^G=\operatorname{im}\Pi_0\simeq E_U.
\tag{2.1}
\]

For `r != 0`, `im Pi_r` is, under this right-regular convention, the
rank-one Kummer local system labelled by `chi_r` (using the opposite deck
convention replaces `r` by `-r`).  Thus (1.6) is the abstract torsor Fourier
decomposition sought by the cyclic-mask programme:

\[
 \begin{aligned}
 \mathsf C_S&=\Pi_0+\sum_{r\ne0}|c_r|^2\Pi_r,\\
 \mathsf S_S&=\phantom{\Pi_0+{}}\sum_{r\ne0}|c_r|^2\Pi_r.
 \end{aligned}
\tag{2.2}
\]

After the physical quotient aggregation, source normalization, and common
adapter have been identified with these two abstract operators, every
resonant constant restriction occurs in both rows with the same
endomorphism coefficient.  It then cancels before a trace or absolute value
is taken.  The surviving invariant line is intentional: it is the principal
channel, not a nuisance constituent.  The earlier invariant audit constructs
the selected Kummer lines, not this remaining physical identification.

## 2A. Global Kummer-ratio trace realization

The endomorphisms above are not restricted to a single rational fibre.  Let
`U` be a variety over `F_q` with `k|(q-1)`, let
`f in Gamma(U,O_U^times)`, and form the Kummer torsor

\[
 T_f:\quad z^k=f.
\tag{2A.1}
\]

For a closed point `x`, choose a geometric point of the torsor fibre and
define its Frobenius class `phi_x in C_k` by

\[
 \operatorname{Frob}_x(t)=t\phi_x.
\tag{2A.2}
\]

Changing the chosen point does not change `phi_x` because `C_k` is abelian
and split.  Reversing geometric/arithmetic Frobenius conventions replaces
`phi_x` by its inverse; the hard and selected covariance kernels are
inversion-invariant.

More generally, for any function `w:C_k -> E`, define

\[
 \mathsf A_w={1\over k}\sum_{a\in C_k}w(a^{-1})\rho(a)
 \in\operatorname{End}_E(\pi_*E_{T_f}).
\tag{2A.3}
\]

On the regular torsor fibre, `rho(a)Frob_x` is translation by `a phi_x`.
Its permutation trace is `k` when `a phi_x=1` and zero otherwise.  Hence

\[
 \boxed{
 \operatorname{Tr}
 (\mathsf A_w\operatorname{Frob}_x\mid(\pi_*E)_{\bar x})
 =w(\phi_x).}
\tag{2A.4}
\]

Thus every cyclic hard indicator is an honest trace function with an
endomorphism.  For the rotated normalized mask put

\[
 w_j(g)={k\over t}\mathbf1_{g\in\zeta_k^jS}.
\tag{2A.5}
\]

Then the exact pair identity is

\[
 {1\over k}\sum_{j=0}^{k-1}w_j(g_1)w_j(g_2)
 =K_C(g_1g_2^{-1}).
\tag{2A.6}
\]

On `U x U`, take the contracted quotient torsor

\[
 T_\Delta=\operatorname{pr}_1^*T_f
 \mathbin{\times^{C_k}}
 (\operatorname{pr}_2^*T_f)^{-1}.
\tag{2A.7}
\]

For an `F_(q^m)`-valued pair `(x_1,x_2)`, its Frobenius class is exactly
`phi_(x_1) phi_(x_2)^(-1)`, with both classes measured using `Frob_(q^m)`.
More intrinsically, at a closed point `y` of `U x U`, use the two pullback
classes along its projections, both measured for `Frob_y`; this automatically
includes the residue-degree powers.  Applying (2A.4) with `w=K_C` and
`w=K_S` therefore realizes the hard covariance and selected covariance on
one common global torsor, and their endomorphism difference is the constant
trace-one summand `Pi_0`.

This is a genuine global construction for one Kummer function `f` and all
closed points of its clean base.  It still does not identify the complete
FFPS source with that construction.  The physical programme has owner
sectors, two native sums, Artin--Schreier phases, irreducible-place
selection, Boolean/incidence operations, and several exceptional cleanups.
Each must be transported to the same Kummer-ratio object before (2A.7) can
be called the FFPS `C-S` complex.

## 3. Functorial survival through common cleanup

Let `F` be an additive `E`-linear functor defined on the object `H` with its
endomorphisms.  Applying `F` to (0.1) gives (0.3) because

\[
 F(a\alpha+b\beta)=aF(\alpha)+bF(\beta).
\tag{3.1}
\]

This applies, in the usual derived settings, to:

- pullback and restriction to a `G`-stable open or closed stratum;
- extension by zero from a `G`-stable open;
- `Rf_*` and `Rf_!` for one common equivariant map `f`;
- tensoring by the same source local system;
- taking a cone in a fixed stable/dg enhancement when the source and target
  carry compatible endomorphisms and the cleanup arrow intertwines them;
- taking compactly supported cohomology and then Frobenius traces, provided
  the coefficients and endomorphisms descend and commute with Frobenius.

Idempotent completeness splits `F(Pi_0)` as the image of the transported
projector.  When `F` is applied to the invariant summand itself,

\[
 F(\operatorname{im}\Pi_0)\simeq F(E_U).
\tag{3.2}
\]

This statement is stronger and narrower than a numerical cancellation:

- stronger, because it is functorial at the endomorphism level;
- narrower, because it requires one object, one group action, and one common
  cleanup functor.

It fails to apply if the hard and selected terms are built on different
bases, if only one side deletes a stratum, if a source weight breaks the deck
action, or if the physical quotient has not been promoted to a torsor.  If
`mu_k` is not split over the base, arithmetic Galois can permute the
characters; then only Galois-orbit sums of the `Pi_r` necessarily descend.
One must either base-change and descend the full identity or formulate it
with those orbit projectors.  The individually labelled formula (1.4) is not
silently asserted in that nonsplit setting.

## 4. Finite products and the growing-place boundary

For finitely many cyclic torsors, external tensor product gives a torsor for

\[
 G=\prod_{i=1}^m\mu_{k_i}.
\]

Writing `C_i=Pi_(0,i)+S_i`, exact distributivity gives

\[
 \bigotimes_{i=1}^m\mathsf C_i
 =
 \sum_{J\subseteq\{1,\ldots,m\}}
 \left(\bigotimes_{i\in J}\mathsf S_i\right)
 \otimes
 \left(\bigotimes_{i\notin J}\Pi_{0,i}\right).
\tag{4.1}
\]

Therefore, if the total selected operator is the sum of every nonempty
`J`-term,

\[
 \boxed{
 \bigotimes_i\mathsf C_i-\mathsf S_{\rm total}
 =\bigotimes_i\Pi_{0,i}.}
\tag{4.2}
\]

So no new algebraic obstruction appears at any finite tensor stage.  What
does grow is the number of nonprincipal character sectors and the geometric
complexity of their pushforwards.  Equation (4.2) gives no uniform Betti,
conductor, or cancellation bound as `m` grows.

This separates two questions that were previously easy to conflate:

1. **Does exact relative cancellation exist?** Yes, on every constructed
   finite product torsor.
2. **Is the resulting family uniformly estimable?** Open; this is the
   varying-place analytic-geometric gate.

## 5. Exact relation to the physical FFPS source

The physical cyclic source uses root orientations to turn squareclass data
into an exact-order-`k` character.  On one clean fixed fibre, the prior audit
constructs the corresponding selected Kummer systems.  Equation (0.1)
supplies the abstract cyclic relative operator on a torsor.  It becomes the
physical `C-S` projector only after quotient aggregation,
normalization/source weights, and the common adapter are matched exactly.

It does **not** yet globalize for free.  A valid FFPS lift must exhibit:

\[
 \boxed{
 \text{one physical orientation torsor}
 +\text{ one source object}
 +\text{ one equivariant cleanup pipeline}.}
\tag{5.1}
\]

The following checks are binding.

1. `P c^2` and `Q d^2`, not owner labels alone, define the torsor map.
2. The two native source sums and their phases must be present before the
   quadratic operator is formed.
3. Literal atoms, equal products, root pieces, shared incidence, and
   geometrically constant pieces must be removed by common equivariant maps.
4. Different closed-place residue fields must be related by an explicitly
   constructed group scheme or correspondence; an abstract identification
   of two cyclic value groups is insufficient.
5. Frobenius structures and Tate/source weights must agree on the two
   endomorphisms, not only their geometric ranks.

If these checks close, the relative identity itself survives every finite
stage automatically.  The remaining trace is the principal object, so a
subpower estimate for it would still be the open producer theorem feeding
the frozen Mellin-Landau consumer.

## 6. What this changes about `CYSEL`

The general resonance theorem proves that a separate selected-mode sheaf has
unavoidable constant restrictions.  The present theorem shows that the same
restrictions cancel exactly inside the relative endomorphism.

Hence there are now two sharply different research targets.

### Separate route

Prove `CYSEL` after explicitly accounting for every selected invariant,
boundary term, and conductor-growing Betti cost.

### Relative route

Construct (5.1), transport (0.1) through the common cleanup, and estimate the
principal relative trace directly.

The relative route avoids proving an unnecessarily strong absolute estimate
for each selected summand.  It does not make the remaining estimate easier
by algebra alone: (0.1) says that the remainder is exactly principal.

## 7. Proof ledger

| statement | grade |
|---|---|
| cyclic idempotents (1.4)--(1.5) | **PROVED EXACT ALL-`k`** |
| honest endomorphisms (1.6)--(1.7) | **PROVED EXACT ALL-`k`** |
| relative projector (0.1) | **PROVED EXACT ON EVERY TORSOR UNDER SPLIT `mu_k`** |
| invariant image (0.2) | **PROVED BY FINITE-ETALE DESCENT** |
| arbitrary trace selector (2A.3)--(2A.4) | **PROVED EXACT ON A SPLIT CYCLIC TORSOR** |
| global Kummer-ratio realization (2A.7) | **PROVED FOR ONE CLEAN KUMMER FUNCTION** |
| preservation by common `E`-linear functors | **PROVED FORMALLY** |
| finite-product projector (4.2) | **PROVED EXACT** |
| identification with the fixed clean cyclic fibre | **CONDITIONAL ON THE LOCKED PHYSICAL ADAPTER** |
| one varying-closed-place physical torsor | **NOT CONSTRUCTED** |
| equivariance of the full FFPS cleanup | **OPEN** |
| uniform Betti/conductor control | **OPEN** |
| `CYSEL`, `WCADD106140`, `WCKUM106140` | **OPEN / RH-BEARING** |
| RH or GRH | **UNPROVED** |

No external novelty or priority claim is made.  The theorem is elementary
Fourier descent; the project contribution is its exact placement in the
physical-mask obstruction and the resulting reduction of the categorical
gap.

## 8. Reproduction

The companion replay uses rational circulant matrices.  It audits all 494
nonempty proper subsets for `2<=k<=8` and a small tensor control; it performs
no arithmetic-family enumeration.

~~~powershell
python research/l-families/atlas/function_field/ffps_cyclic_torsor_relative_projector.py --check
python -O research/l-families/atlas/function_field/ffps_cyclic_torsor_relative_projector.py --check
python -m unittest tests.test_ffps_cyclic_torsor_relative_projector
python -O -m unittest tests.test_ffps_cyclic_torsor_relative_projector
python -m ruff check research/l-families/atlas/function_field/ffps_cyclic_torsor_relative_projector.py tests/test_ffps_cyclic_torsor_relative_projector.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_cyclic_torsor_relative_projector.py tests/test_ffps_cyclic_torsor_relative_projector.py
~~~
