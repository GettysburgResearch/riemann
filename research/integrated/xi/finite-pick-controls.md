# Integrated packet: finite complex Pick controls

**Packet status:** integrated reviewed finite directed computations  
**Scope:** two exact finite complex matrix boxes only; no statement at other points and no global Pick positivity  
**Global status:** RH remains unsolved  
**Source A:** PR [#68](https://github.com/gfreund123/riemann/pull/68) at `7b0942a83eede8b57d4f28b14a78d80edc295f2a`  
**Source B:** PR [#71](https://github.com/gfreund123/riemann/pull/71) at `82934cf24ed575e9e554ba4e6c912a447aa1dd4e`  
**Review evidence:** `reports/gpt56-pro-09-i/2026-08-01-pre-public-review-pr64-pr79.md` at `7162c2a221fd87e6e7baf4e7245d6f42b5e04de3`  
**Review verdict:** #68 `VERIFIED`; #71 `VERIFIED`  
**Replay in this integration:** none.

> **Assurance boundary.** These are reviewed finite directed matrix computations, not independently regenerated special-function computations. The exact rational \(LDL^*\) and interval-box deductions are exact **conditional on the supplied directed primitive rectangles containing the intended \(\xi'/\xi\) values in the stated normalization**. This integration did not regenerate those primitive rectangles or replay the production backends.

## Shared finite setup

At two distinct exact point sets, supplied directed rectangles for

\[
F(s)=\frac{\xi'(s)}{\xi(s)}
\]

determine boxes of complex Hermitian Pick matrices

\[
K_{ij}
=
\frac{F(s_i)+\overline{F(s_j)}}
{s_i+\overline{s_j}-1}.
\]

Each source:

1. reconstructs an exact rational midpoint Hermitian matrix \(M\);
2. proves \(M-\delta I\succ0\) by exact rational Hermitian \(LDL^*\);
3. derives a rigorous operator-norm radius for every matrix admitted by the primitive rectangles;
4. proves the radius is smaller than the midpoint moat.

Therefore every matrix in the declared finite box is positive definite.

“Exact box” refers to the exact downstream matrix enclosure and rational proof. It does not mean that this integration independently regenerated the upstream special-function primitives.

---

## Control A — PR #68

### Exact point set

The common ordinate is

\[
T_A
=
\frac{20225875608343255624083}{2^{32}}.
\]

The positive horizontal offsets are

\[
2^{-17},\ 2^{-15},\ 2^{-13},\ 2^{-11},
\ 2^{-10},\ 2^{-9},\ 2^{-7},\ 2^{-5}.
\]

### Finite theorem

Every Hermitian Pick matrix consistent with the supplied 192-bit directed primitive rectangles satisfies

\[
\lambda_{\min}(K)>2^{-138}.
\]

The retained classification is

```text
ENTIRE_EIGHT_BY_EIGHT_BOX_STRICTLY_POSITIVE_DEFINITE
```

### Exact proof structure

1. Intersect the supplied complex \(F(s_i)\) rectangles.
2. Construct the exact rational midpoint matrix \(M\).
3. Prove
   \[
   M-2^{-137}I\succ0
   \]
   by exact Gaussian-rational unpivoted Hermitian \(LDL^*\).
4. Bound every entry perturbation by exact rectangle arithmetic.
5. Bound the Hermitian operator norm by a maximum exact row sum.
6. Prove that perturbation is smaller than the midpoint moat, leaving the strict lower bound \(>2^{-138}\).

### Primitive provenance and storage boundary

- backend: FLINT C `acb_dirichlet_zeta_jet_rs`;
- precision: 192 bits;
- historical workflow run: `30009653881`;
- historical artifact ID: `8564591455`;
- historical artifact zip SHA-256:
  `646ff50e6191d68700bc3bb9a2ad21010241f51ad384d9ee36078a55d6f857a3`;
- certificate SHA-256:
  `bc9bf349864fa65257a195538404e20a9e49891d18e2e55faeb44505b85d618f`.

GitHub Actions artifacts are temporary transport, not permanent immutable storage. The durable source paths retained at the reviewed commit are:

- `experiments/X-6602-barycentric-nearzero/verify_pick_box_pd.py`
- `experiments/X-6602-barycentric-nearzero/results/pick-j1-192-positive-definite.json`
- `experiments/X-6602-barycentric-nearzero/results/pick-j1-192-positive-definite.verification.json`

The principal retained JSON blob is
`97f722bf2cbdca6ca19ac8134cc718dc7937e9e6`.

### Exact boundary

This excludes every real and complex direction inside this one admitted finite box. It does not independently authenticate the primitive producer, cover another ordinate, or imply global Pick positivity.

---

## Control B — PR #71

### Exact point set

The common ordinate is

\[
T_B
=
\frac{20225875608342450317715}{2^{32}}.
\]

The horizontal offsets are the same dyadic ladder:

\[
2^{-17},\ 2^{-15},\ 2^{-13},\ 2^{-11},
\ 2^{-10},\ 2^{-9},\ 2^{-7},\ 2^{-5}.
\]

This is a distinct ordinate and a distinct finite box.

### Finite theorem

The complete 512-bit complex matrix box is positive definite. The retained exact lower-eigenvalue margin has outward decimal orientation approximately

\[
1.1479437019748901445\times10^{-41},
\]

while the operator-radius upper bound is approximately

\[
5.7573346532278167483\times10^{-147}.
\]

The retained classification is

```text
ENTIRE_FROZEN_POINT_SET_CERTIFIED_POSITIVE_DEFINITE
```

### Exact proof structure

1. Reconstruct the exact complex Hermitian midpoint.
2. Prove
   \[
   M-\delta I\succ0,
   \qquad
   \delta=2^{-136},
   \]
   by exact rational Hermitian \(LDL^*\).
3. Compute a complete interval-box operator radius.
4. Subtract the radius from the exact midpoint moat.

The result strengthens an earlier one-vector positive replay: every complex direction on this point set is excluded.

### Primitive provenance and storage boundary

- precision: 512 bits;
- historical artifact name: `arb-xi-frozen-pick-candidate`;
- historical artifact ID: `8564247721`;
- artifact digest:
  `sha256:b959095a7da656a18b8fd55b399613a220abd224ed7e522fc749119603606710`;
- audit input SHA-256:
  `7c79099e07b30d0f6502542ca729db1a17126a6aae6171d607687b016695a1bd`;
- audit verification SHA-256:
  `65d94d511c7fe52da62ba2a74268f43aa4ddf4d496a225b1c4837ef311f62613`;
- internal verification SHA-256:
  `e1f15d38ca18610fbe79bfbb5d66bf9b47ee5364da3f5c831682a9e4bf1bb809`.

Again, the historical Actions artifact is not durable storage. The reviewed source commit retains:

- `claims/lemmas/L-7101-rational-midpoint-radius-pick-pd.md`
- `experiments/X-3904-complex-pick-recheck/verify_complex_pick.py`
- `experiments/X-3904-complex-pick-recheck/results/frozen-candidate-full-matrix-summary.json`
- `claims/refutations/R-7101-full-complex-pick-midpoint-ghosts.md`

The retained summary blob is
`d761d78ae6b2c1ac8b8a6ba3624f823ec3290363`.

### Exact boundary

This closes every complex direction only on this declared finite box. It does not independently regenerate the primitive values, prove a neighborhood result, or establish RH.

---

## Shared finite lemma

Let \(M\) be an exact Hermitian midpoint, \(\delta>0\), and suppose exact rational \(LDL^*\) proves

\[
M-\delta I\succ0.
\]

If every admitted Hermitian perturbation \(E\) satisfies

\[
\|E\|_2<\delta,
\]

then

\[
M+E\succ0,
\]

because for every nonzero \(v\),

\[
v^*(M+E)v
\ge
\delta\|v\|^2-\|E\|_2\|v\|^2
>0.
\]

A maximum row-sum bound gives a valid operator-norm upper bound for a Hermitian interval box. The checker must construct the exact midpoint and radius from the primitive rectangles rather than trust declared matrix entries.

## Relationship to RH

Under the source-qualified Lagarias positive-real/Pick theorem, RH implies positive semidefiniteness of every exact finite Pick matrix in the right half-plane. A strict negative finite matrix would therefore contradict RH after all source and primitive gates were satisfied.

The results here are positive. They establish only:

```text
no negative real or complex direction exists
inside either declared finite matrix box
```

They do not establish:

- positivity at another ordinate;
- positivity on a larger or adaptive point set;
- global Pick positivity;
- RH;
- independent reproduction of the special-function primitives.

## Why the controls matter

Earlier apparent negative modes disappeared when full primitive rectangles and the complete complex matrix were handled rigorously. These boxes are valuable regression controls for future producers and checkers.

They also close vector optimization on the exact admitted boxes: choosing another vector cannot create a negative direction there.

## Common misreadings

- The two controls are complementary finite exclusions, not evidence for a trend.
- A positive finite box is not statistical evidence for RH.
- Two precisions in one implementation are not an independent backend.
- A successful historical Actions artifact is not permanent storage.
- Exact downstream matrix algebra cannot authenticate a wrong completed-\(\xi\) normalization.
- No nearby-point theorem follows without an explicit perturbation radius in the point coordinates.

## Exact next missing step

Regenerate one control’s primitive \(\xi'/\xi\) values with a separately structured implementation and compare normalization and enclosures. Only after that control passes should a new condition-aware secant or small Loewner packet be evaluated.
