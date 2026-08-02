# Integrated packet: finite complex Pick controls

**Packet status:** integrated, reviewed finite directed computations  
**Global status:** RH remains unsolved  
**Source A:** PR [#68](https://github.com/gfreund123/riemann/pull/68) at `7b0942a83eede8b57d4f28b14a78d80edc295f2a`  
**Source B:** PR [#71](https://github.com/gfreund123/riemann/pull/71) at `82934cf24ed575e9e554ba4e6c912a447aa1dd4e`  
**Review evidence:** `reports/gpt56-pro-09-i/2026-08-01-pre-public-review-pr64-pr79.md` at review-source commit `7162c2a221fd87e6e7baf4e7245d6f42b5e04de3`  
**Review verdicts:** #68 `VERIFIED`; #71 `VERIFIED`  
**Replay in this integration pass:** none; the exact-SHA review inspected the proof objects without rerunning the expensive primitive evaluations.

## What these results are

At two distinct exact point sets, directed \(\xi'/\xi\) rectangles determine a box of complex Hermitian Pick matrices

\[
K_{ij}
=
\frac{F(s_i)+\overline{F(s_j)}}
{s_i+\overline{s_j}-1},
\qquad
F=\frac{\xi'}{\xi}.
\]

Each source reconstructs an exact rational midpoint matrix, proves a rational lower bound for that midpoint by Hermitian \(LDL^*\), computes a rigorous operator-norm radius for every matrix allowed by the primitive rectangles, and proves the lower bound exceeds the radius.

Therefore every matrix in the finite box is positive definite.

These are strong finite exclusions. They do not prove the Pick kernel positive at any other points or establish RH.

---

## Control A — PR #68

### Exact point set

The common ordinate is

\[
T_A
=
\frac{20225875608343255624083}{2^{32}}.
\]

The eight positive horizontal offsets are

\[
2^{-17},\ 2^{-15},\ 2^{-13},\ 2^{-11},\
2^{-10},\ 2^{-9},\ 2^{-7},\ 2^{-5}.
\]

### Finite theorem

Every Hermitian Pick matrix consistent with the supplied 192-bit directed primitive rectangles has

\[
\lambda_{\min}(K)>2^{-138}.
\]

The retained classification is

```text
ENTIRE_EIGHT_BY_EIGHT_BOX_STRICTLY_POSITIVE_DEFINITE
```

### Proof structure

1. Intersect the supplied complex \(F(s_i)\) rectangles.
2. Construct the exact rational midpoint Hermitian matrix \(M\).
3. Prove

   \[
   M-2^{-137}I\succ0
   \]

   by exact Gaussian-rational unpivoted Hermitian \(LDL^*\).
4. Bound every entry perturbation by exact rectangle arithmetic.
5. Bound the Hermitian operator norm by the maximum exact row sum.
6. Prove the perturbation is smaller than the midpoint moat, leaving a final strict lower bound \(>2^{-138}\).

### Primitive provenance

- backend: FLINT C `acb_dirichlet_zeta_jet_rs`;
- precision: 192 bits;
- historical workflow run: `30009653881`;
- historical artifact ID: `8564591455`;
- artifact zip SHA-256:
  `646ff50e6191d68700bc3bb9a2ad21010241f51ad384d9ee36078a55d6f857a3`;
- certificate SHA-256:
  `bc9bf349864fa65257a195538404e20a9e49891d18e2e55faeb44505b85d618f`.

GitHub Actions retention is not permanent storage. The exact retained result and verification files are the durable source paths below.

### Source files

- `experiments/X-6602-barycentric-nearzero/verify_pick_box_pd.py`
- `experiments/X-6602-barycentric-nearzero/results/pick-j1-192-positive-definite.json`
- `experiments/X-6602-barycentric-nearzero/results/pick-j1-192-positive-definite.verification.json`

The retained result blob for the principal JSON is
`97f722bf2cbdca6ca19ac8134cc718dc7937e9e6` at the source commit.

---

## Control B — PR #71

### Exact point set

The common ordinate is

\[
T_B
=
\frac{20225875608342450317715}{2^{32}}.
\]

The eight horizontal offsets are the same dyadic ladder:

\[
2^{-17},\ 2^{-15},\ 2^{-13},\ 2^{-11},\
2^{-10},\ 2^{-9},\ 2^{-7},\ 2^{-5}.
\]

This is a distinct ordinate and a distinct finite box from Control A.

### Finite theorem

The complete 512-bit complex matrix box is positive definite. The retained exact lower-eigenvalue margin has outward decimal orientation

\[
1.1479437019748901445\times10^{-41},
\]

while the operator-radius upper bound is approximately

\[
5.7573346532278167483\times10^{-147}.
\]

The classification is

```text
ENTIRE_FROZEN_POINT_SET_CERTIFIED_POSITIVE_DEFINITE
```

### Proof structure

The source uses the same midpoint-plus-radius principle:

1. reconstruct the exact complex Hermitian midpoint;
2. certify

   \[
   M-\delta I\succ0,
   \qquad
   \delta=2^{-136},
   \]

   by exact rational Hermitian \(LDL^*\);
3. compute a complete interval-box operator radius;
4. subtract that radius from the exact midpoint moat.

The result strengthens an earlier one-vector positive replay: every complex direction on this point set is excluded.

### Primitive provenance

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

### Source files

- `claims/lemmas/L-7101-rational-midpoint-radius-pick-pd.md`
- `experiments/X-3904-complex-pick-recheck/verify_complex_pick.py`
- `experiments/X-3904-complex-pick-recheck/results/frozen-candidate-full-matrix-summary.json`
- `claims/refutations/R-7101-full-complex-pick-midpoint-ghosts.md`

The retained summary blob is
`d761d78ae6b2c1ac8b8a6ba3624f823ec3290363`.

---

## Shared exact finite lemma

The computations instantiate the following elementary finite principle.

Let \(M\) be an exact Hermitian midpoint, let \(\delta>0\), and suppose exact rational \(LDL^*\) proves

\[
M-\delta I\succ0.
\]

Let every admitted Hermitian perturbation \(E\) satisfy

\[
\|E\|_2<\delta.
\]

Then

\[
M+E\succ0,
\]

because for every nonzero \(v\),

\[
v^*(M+E)v
\ge
\delta\|v\|^2-\|E\|_2\|v\|^2>0.
\]

A maximum row-sum bound supplies a valid operator-norm upper bound for a Hermitian interval box. The checker must construct the exact midpoint and radius from primitive rectangles rather than trust claimed matrix entries.

## Mathematical relationship to RH

Under the reviewed positive-real/Pick theorem, RH implies positive semidefiniteness of every exact finite Pick matrix in the right half-plane. A strict negative finite matrix would therefore be an RH-disproof witness after all source gates are satisfied.

The results here are positive. They establish only:

```text
no real or complex negative direction exists
inside either declared finite matrix box.
```

They do not establish:

- positivity at another ordinate;
- positivity on a larger or adaptive point set;
- positivity of the global Pick kernel;
- RH;
- independent reproduction of the primitive special-function balls.

## Why these controls matter

They show how deceptive midpoint linear algebra can be. Earlier apparent negative modes disappeared when the primitive rectangles and full complex matrix were handled rigorously. These two boxes are useful regression controls for every future Pick producer and checker.

They also close optimization over the exact eight-node point sets: no different vector on the same admitted matrix box can become negative.

## Known exclusions and common misreadings

- The two controls are complementary, not duplicate evidence for a trend.
- A positive matrix box is not statistical evidence for RH.
- Dual precision or a higher precision in one backend is not an independent implementation.
- A successful historical Actions artifact is not permanent storage.
- Exact matrix algebra cannot authenticate a wrong completed-\(\xi\) normalization.
- The finite proof does not cover nearby ordinates or nodes by continuity unless an explicit perturbation theorem and radius are supplied.

## Exact next missing step

Use one of these controls as an end-to-end regression for an independently implemented primitive producer. Then evaluate a newly frozen, condition-aware secant or small Loewner packet. Do not expand the grid until the independent normalization and positive control agree.
