# Genus-two `Sym^12`: corrected marked valuation kernel

Status: exact finite invariant theory, corrected by three source-calibration
controls. No point counts, floating-point ranks, or Frobenius interpolation
are used.

Companion replay:
[`genus2_sym12_marked_valuation_kernel.py`](genus2_sym12_marked_valuation_kernel.py).
Canonical output:
[`genus2_sym12_marked_valuation_kernel.json`](genus2_sym12_marked_valuation_kernel.json).

## 1. Corrected result

At covariant bidegree `(d,b)=(9,12)`, hence Siegel weight
`(j,k)=(12,3)`, the natural marked highest-weight source has dimension `66`.
The earlier replay imposed the substitution only on the block containing the
marked sixth root in

\[
\{1,2,6\}\mid\{3,4,5\}.
\]

That was incomplete. After imposing the two-chart minimum on **both**
oriented blocks, the exact matrix is `9902 x 66` and

\[
\boxed{
\operatorname{rank}_{\mathbf Q}J=66,
\qquad \dim\ker J=0.
}
\tag{1}
\]

The ranks modulo `1000003` and `1000033` are also `66`. The former
rank-`51`/nullity-`15` statement is retracted: it was the kernel of only the
orientation containing label `6`, not the regular marked covariant space.

Consequently the finite natural-marked holomorphy problem closes with a zero
kernel. Since the scalar weight is odd, the global Siegel `Phi` target
vanishes, so `M_(12,3)=S_(12,3)` at this level. This supplies an
unconditional finite invariant-theory proof that the natural `S_5`-fixed
holomorphic/cuspidal covariant channel at this bidegree is zero.

This does **not** make the separately source-caveated nonregular Eisenstein
formula unconditional. The primary-source adapter in
[`GENUS2_SYM12_MODULAR_ZERO_GENERAL_CHANNEL_ADAPTER.md`](GENUS2_SYM12_MODULAR_ZERO_GENERAL_CHANNEL_ADAPTER.md)
now shows that this zero closes the positive semisimplified marked
stable/general channel `G`. The actual compact-support Eisenstein Galois class
and the resulting all-`q` Frobenius identity remain open.

## 2. The source and its exact dimension

Put `R=Sym^9(V)`. Permuting the first five roots and distinguishing the
sixth gives

\[
W=\operatorname{Sym}^5(R)\otimes R,
\qquad
H=\operatorname{Hom}_{\mathrm{SL}_2}
   (\operatorname{Sym}^{12}V,W).
\tag{2}
\]

In the monomial basis `e_a=u^(9-a)v^a`, the weight-`12` and weight-`14`
state spaces have dimensions `752` and `686`. The raising map has exact
rank `686`, also certified modulo `1000003`; therefore

\[
\dim H=752-686=66.
\tag{3}
\]

The primitive integral highest-weight basis has digest

```text
6f09eb35f716efab67f717cf55adcde1dab3e9fc11ef73747d41668f95d95c1e
```

The replay basis normalization is independently controlled. For a root
index multiset with multiplicities `m_r`, its symmetric-polynomial basis
vector is `(prod m_r!)` times the distinct labelled-orbit sum. Under this
diagonal normalization, the replay's raising, lowering, and coproduct
coefficients agree with direct labelled-root expansion. The defect was not
a symmetric-power normalization error.

## 3. Primary criterion and the orientation caveat

Clery--van der Geer, Definition 7.1, write

\[
v_\pi(P_j)=2d-\min\{\deg_t\varphi_\pi(P_j),
                         \deg_t\varphi'_\pi(P_j)\},
\tag{4}
\]

and Criterion 7.4 identifies nonnegative valuations for all `3+3` boundary
components with holomorphy. Their geometric divisor is indexed by an
unordered partition, while the displayed substitutions act on one displayed
block. The cited version does not spell out a block-swap formula.

With a sixth root marked, the substitutions on triples containing label `6`
and on triples avoiding it form two oriented computational orbits under
`S_5`. Transitivity on the ten **unordered** partitions therefore justifies
using one representative partition, but it does not justify dropping one of
its two displayed blocks.

The conservative, source-calibrated implementation is:

1. for `{1,2,6}`, use
   `Sym^5(R) -> Sym^2(R) tensor Sym^3(R)` and retain `R_6` in the selected
   triple;
2. for `{3,4,5}`, use
   `Sym^5(R) -> Sym^3(R) tensor Sym^2(R)` and leave `R_6` unselected;
3. in each orientation and for each coefficient, prove over `Q` that the two
   chart kernels are nested, so the minimum in (4) linearizes;
4. intersect the two resulting oriented kernels.

This packet does not claim that the paper intended an independently oriented
divisor condition. It records the narrower fact forced by exact controls:
one displayed orientation does not reproduce known modular-form dimensions,
whereas the two-orientation implementation does. A future source-level
frame-transition proof could replace this conservative calibration, but it
cannot restore the retracted `15`-dimensional kernel without contradicting
the controls below.

## 4. Exact calibration controls

Three bounded controls localize the defect and fix the convention.

| `(d,b)` | weight `(j,k)` | highest-weight dimension | one-orientation nullity | corrected rank/nullity | external target |
|---:|---:|---:|---:|---:|---|
| `(4,6)` | `(6,1)` | `6` | `1` | `6 / 0` | `M_(6,1)=0` |
| `(7,4)` | `(4,5)` | `18` | `1` | `18 / 0` | natural-`S_5` fixed dimension `0` |
| `(12,2)` | `(2,11)` | `38` | `4` | `36 / 2` | `dim S_(2,11)(Gamma_2[w])=2` |

For `(7,4)`, direct expansion of the false survivor gives chart degrees

\[
\begin{array}{c|ccccc}
j&0&1&2&3&4\\ \hline
\{1,2,6\},\ \varphi&13&13&13&13&13\\
\{1,2,6\},\ \varphi'&13&13&13&13&13\\
\{3,4,5\},\ \varphi&17&16&15&14&13\\
\{3,4,5\},\ \varphi'&13&14&15&16&17
\end{array}
\]

against cap `2d=14`. The omitted orientation fails at `j=2` in both
charts. Stacking the two oriented kernels raises rank `17 -> 18`.

At `(12,2)`, the corrected matrix has `25583` rows, exact rank `36`, and
nullity `2`; its primitive kernel digest is

```text
ce4cbd1e53811943c87c7fad2ffefdf785e19eba084f4c382ef173ccbe809095
```

This matches the paper's exact marked weight-`(2,11)` dimension. The
agreement is a calibration of the boundary implementation, not a fit: the
rank is obtained by exact rational elimination with two independent modular
checks.

## 5. The corrected `(9,12)` matrix

For both orientations, the two chart kernels are nested coefficient by
coefficient. After selecting the larger kernel in each orientation and
stacking them, the coefficient ranks for `j=0,...,12` are

\[
5,9,16,25,39,51,66,51,39,25,16,9,5.
\tag{5}
\]

The middle coefficient alone has rank `66` after the two oriented conditions
are combined. For comparison, at `j=6` the orientation containing the mark
has chart rank `51`, while the orientation avoiding it has chart rank `53`;
their kernels are distinct and have zero intersection. Thus the corrected
full rank is structural, not an accumulation of numerical noise across many
coefficients.

The zero kernel has the canonical empty-basis digest

```text
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
```

## 6. Proof ledger

Proved exactly in the natural split-root convention:

1. the pre-holomorphic source (2) has dimension `66`;
2. the orbit-sum, Lie-action, coproduct, and labelled-root normalizations
   agree;
3. the two-chart minimum linearizes in each of the two oriented blocks by
   exact kernel containment;
4. the three controls in Section 4 match independent primary dimensions;
5. the corrected `(9,12)` matrix has rational and modular rank `66` and
   nullity `0`;
6. the former rank-`51`/nullity-`15` claim is false and is retracted.

Still conditional or source-caveated:

- the nonregular `k=3` official general-space continuation;
- realization of Shmakov's formal Eisenstein associated-graded expression
  as an actual Galois/Frobenius Euler class;
- the equality `epsilon_Eis=L` as an actual trace identity;
- the all-`q` formula for `Hhat_12` obtained by combining those channels.

Closed by the separate primary-source adapter:

- `G=(S_gen,Gamma(2)[12,3])^S5=0` as a positive semisimplified stable/general
  Galois channel.

The finite zero-kernel result removes the previously alleged modular-form
obstruction. Together with the stable adapter it closes `G`; it does not
upgrade any Eisenstein item in the conditional list.

## 7. Replay and resource firewall

Canonical replay:

```text
python research/l-families/atlas/function_field/genus2_sym12_marked_valuation_kernel.py --check
pytest -q tests/test_genus2_sym12_marked_valuation_kernel.py
```

Optional control replay uses `--d D --b B`; for example:

```text
python research/l-families/atlas/function_field/genus2_sym12_marked_valuation_kernel.py --d 7 --b 4
```

The canonical calculation has zero point counts, `752` states in its largest
weight space, `66` source columns, one unordered partition, and two oriented
blocks. The recorded wall-clock budget is `300` seconds on the project
machine. The `(12,2)` calibration is intentionally recorded rather than run
in every unit-test pass because its exact 38-column replay takes about two
minutes; the two smaller controls are replayed in tests.

## 8. Sources and novelty boundary

Primary inputs:

- Clery--van der Geer,
  [*Tautological modular forms of level two and degree two*](https://arxiv.org/abs/2605.13300),
  especially Sections 6, 7, and 9: split-root covariants, Definition 7.1,
  Criterion 7.4, and the exact marked weight-`(2,11)` dimension.
- Bergstrom--Clery,
  [*Dimension formulas for spaces of vector-valued Siegel modular forms of
  degree two and level two*](https://doi.org/10.5565/publmat6922505),
  especially Section 2 and the vector-valued tables: odd scalar weight has
  `M=S`, and the weight-`(4,5)` natural marked fixed space is zero.
- Chenevier's low-weight vanishing quoted in Bergstrom--Clery: the
  weight-`(6,1)` control.

The general valuation criterion and dimension targets are external. The
project contribution is the exact two-orientation implementation, the three
calibrations, and the corrected rank-`66` computation. No claim of external
novelty, Galois realization, or RH consequence is made from this finite
calculation alone.
