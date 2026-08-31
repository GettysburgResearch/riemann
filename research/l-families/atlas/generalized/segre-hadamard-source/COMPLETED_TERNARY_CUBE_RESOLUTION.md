# The completed marked resolution of the ternary-cube Chow module

The accepted degree-seven witness completes an explicit minimal graded free resolution of the same characteristic-zero source used throughout this lane. This note joins the actual matrices to the independently established homological inputs; it does not replace an unfinished older computation by a claim that it ran.

Let

\[
 V=\mathbb Q^3,\qquad W=\operatorname{Sym}^3V,\qquad
 S=\operatorname{Sym}(W),\qquad
 R=\bigoplus_{d\ge0}(\operatorname{Sym}^dV)^{\otimes3}.
\]

The ten degree-one variables of `S` act through the symmetric inclusion `W -> R_1`, in the frozen literal orbit-sum coordinates. Multiplication in `R` is componentwise multiplication in its three symmetric-algebra factors. The diagonal `GL(V)` action and the permutation of the three factors commute. This factor-permutation `S3` is not a new arithmetic monodromy group.

## 1. Completed theorem and actual matrices

The authenticated marked polynomial maps now give an exact sequence in every internal degree:

\[
 0\longrightarrow F_3\xrightarrow{D_3}F_2
 \xrightarrow{D_2}F_1\xrightarrow{D_1}F_0
 \xrightarrow{\epsilon}R\longrightarrow0,
\]

where

\[
\begin{aligned}
 F_0&=S\oplus S(-1)^{17}\oplus S(-2)^{11},\\
 F_1&=S(-2)^{20}\oplus S(-3)^{65},\\
 F_2&=S(-4)^{65}\oplus S(-5)^{20},\\
 F_3&=S(-5)^{11}\oplus S(-6)^{17}\oplus S(-7).
\end{aligned}
\]

All differential entries have positive degree, so the resolution is minimal. In particular `D3` is injective; neither `D1` nor `D2` is asserted to be injective.

The full marked matrices, original coordinate descriptors, lower-map identities and new top column are retained in `single_top_witness.verification.json`, frozen at

`4019ecd9d0b674fa6d9b26eee2c70c2717f33543`,

Git blob `86795a55ffb4751bbcad7a93a0a44b8e62b461ec`, with proof-object digest

`31507a0ebecc931dc2073cd2c81df45c1c25f182cf2da9c6ece483cd8d54ba0a`.

Its executable acceptance contract is `single_top_witness.py` at `596189377cb5d167c95334bfc5ddb74af2d1cc5f`, blob `148a8d9523b30a71b5b49ba92bf957e64a25dbe4`. The new degree-seven column has 379 nonzero integer terms and torus weight `(7,7,7)`. The complete output contains 29 `D3` columns, and its fresh polynomial ledger checks every `D1 D2` and `D2 D3` composition in the original source coordinates.

## 2. Why this proves global exactness

Three ingredients have different roles.

First, the classical finite Chow-module and Cohen--Macaulay theorems give dimension seven and projective dimension three over the ten-variable ring `S`. The canonical-module duality and the actual low-degree Koszul homology determine the complete Tor support. These inputs precede the new marked matrices; a matching Hilbert numerator is not their substitute.

Second, the frozen first presentation is globally exact and minimal. The accepted degree-four and degree-five source kernels make `D2` an exact minimal cover of `ker(D1)`. The accepted degree-five and degree-six `D3` data then give all eleven degree-five generators and all seventeen new degree-six classes. Their actual lower-degree generation identifies the entire degree-seven old subspace as

\[
 (S_{>0}\ker D_2)_7
 =\sum_{i=1}^{11}S_2z_i+\sum_{j=1}^{17}S_1y_j.
\]

The independent Tor theorem says that the only missing minimal class is a single copy of `det(V)^7` in degree seven. Its sole torus weight is `(7,7,7)`. Thus the complete central part of the displayed old space contains every possible old expression for a vector of that weight.

Third, the successful new certificate uses all 592 original central domain columns and all 49 old central multiples. A 49-coordinate minor of the complete old list has determinant 2670 modulo the prime 65521, so it is invertible over `Q`. The accepted nonzero primitive integer vector vanishes on those 49 coordinates and has zero residual in every original target row, including all 2190 rows in the actual support. Therefore it lies in `ker(D2)` and outside the complete old subspace. Modular arithmetic finds the witness and certifies the old minor; acceptance of the new vector itself is exact over the integers.

Its nonzero quotient class fills the independently known one-dimensional top Tor summand. Graded Nakayama now makes `D3` surjective onto `ker(D2)` in every degree. Only after that surjectivity is established, dimension shifting and `Tor_4^S(R,Q)=0` show that `ker(D3)` has zero quotient modulo `S_{>0}`. A second application of graded Nakayama makes this kernel zero. This is the noncircular promotion proved in the frozen `CENTRAL_TOP_CLASS_GLOBAL_EXACTNESS.md`.

The global degree-seven old dimension 775 and kernel dimension 776 follow after exactness. They were not measured by a full 775-column elimination or a 776-vector kernel computation. The old full-kernel and larger replay contracts remain distinct from this completed single-witness contract.

## 3. Equivariant modules and the Hadamard-cube identity

For reference, the independently computed Tor table is recalled below. Write `[abc]` for the polynomial `GL3` Schur module of partition `(a,b,c)`, and `1`, `epsilon`, `sigma` for the trivial, sign and standard factor-permutation representations.

| Tor degree `i` | Internal degree `j` | `GL3 x S3` module | Dimension |
|---|---|---|---:|
| 0 | 0 | `[000] tensor 1` | 1 |
| 0 | 1 | `[210] tensor sigma + [111] tensor epsilon` | 17 |
| 0 | 2 | `[222] tensor 1 + [330] tensor epsilon` | 11 |
| 1 | 2 | `[411] tensor sigma` | 20 |
| 1 | 3 | `[522] tensor (1+sigma) + ([531]+[432]) tensor epsilon` | 65 |
| 2 | 4 | `[552] tensor (1+sigma) + ([642]+[543]) tensor epsilon` | 65 |
| 2 | 5 | `[663] tensor sigma` | 20 |
| 3 | 5 | `[555] tensor 1 + [744] tensor epsilon` | 11 |
| 3 | 6 | `[765] tensor sigma + [666] tensor epsilon` | 17 |
| 3 | 7 | `[777] tensor 1` | 1 |

All omitted entries vanish. This table identifies the abstract equivariant free modules `sum_j S(-j) tensor Tor_(i,j)`. The concrete marked lifts in the artifact are not claimed to be a preferred equivariant splitting or to carry the displayed irreducible actions in their printed bases. Their torus weights and the full character comparisons are retained separately.

For `g in GL(V)`, put `h_d(g)=Tr(g | Sym^d V)`. The diagonal action on the actual graded source gives

\[
 \operatorname{Tr}_R(g,T)=\sum_{d\ge0}h_d(g)^3T^d.
\]

Thus this is the coefficientwise Hadamard cube of the symmetric-power trace series. Equivariant Euler additivity, or equivalently the equivariant Koszul identity, gives the precise bridge

\[
 \boxed{\quad
 \det(1-T\operatorname{Sym}^3g)
 \sum_{d\ge0}h_d(g)^3T^d
 =\sum_{i,j}(-1)^i\operatorname{Tr}
       \bigl(g\mid\operatorname{Tor}_{i,j}^S(R,\mathbb Q)\bigr)T^j.
 \quad}
\]

This identity is in formal power series, with a polynomial right side. Its denominator is the ten-dimensional Chow-base denominator. Replacing it by the denominator for `Sym(V tensor V tensor V)`, or by a canceled scalar recurrence denominator, would change the base or its Euler polynomial.

At `g=1`, the numerator is

\[
\begin{aligned}
 N(T)&=1+17T-9T^2-65T^3+65T^4+9T^5-17T^6-T^7\\
     &=(1-T)^3(1+20T+48T^2+20T^3+T^4),
\end{aligned}
\]

and consequently

\[
 \sum_{d\ge0}\binom{d+2}{2}^{\!3}T^d
 =\frac{1+20T+48T^2+20T^3+T^4}{(1-T)^7}.
\]

The negative degree-two coefficient is `11-20`, not a claim of nine relations with no degree-two generators. The finite numerator is an equivariant Euler character, also called the `K`-polynomial. Neither this identity nor the completed marked resolution supplies an additional finite superdeterminant identity, a pure resolution, or an arithmetic purity or Frobenius theorem.

## 4. Frozen dependencies, attribution and validation

All following paths are in this directory. The accepted artifact authenticates the consumed executable and data chain before use.

| Role | Freeze | File |
|---|---|---|
| Classical source conventions and Cohen--Macaulay input | `a895f47628b0bc7c7ee5e0392df2f79c24166f92` | `MATHEMATICS.md` |
| Actual low-degree homology and duality-completed characters | `08147ccecfe684af76a8417861fcccda61abe601` | `TERNARY_CUBE_TOR_CHARACTERS.md`, `tor_characters.verification.json` |
| Globally exact first presentation | `4c635b2ee8d7cf6caa41efde2d2e0c7baea1b787` | `TERNARY_CUBE_PRESENTATION.md` |
| Accepted degree-five maps | `742d68b6d3c37191589b0e6463bc122af6d90f76` | `resolution_stage5.cache.json` |
| Accepted complete degree-six source data | `d3bda0446a379ce0bd8dfe4024f0184451adb1d5` | `row_restricted_grade6.discovery.json` |
| Authenticated fresh polynomial prefix and top-class promotion | `ed8c7251719a381abf6d55f57d768d69e76b776d` | `composed_grade7_prefix.discovery.json`, `CENTRAL_TOP_CLASS_GLOBAL_EXACTNESS.md` |
| New complete marked resolution artifact | `4019ecd9d0b674fa6d9b26eee2c70c2717f33543` | `single_top_witness.verification.json` |

The classical Chow-module structure and duality are credited in those sources to Raicu--Sam--Weyman, *On some modules supported in the Chow variety*, especially Proposition 2.7, equations (3.2)–(3.5), and Example 4.5. The abstract existence and the previously known invariant normalization component are not new claims here. The added result is the source-bound construction and exact acceptance of the complete marked matrices, including the formerly missing top column, together with the established source character table.

The coordinator reports successful write/check/optimized-check and all 26 ordinary plus 26 optimized tests for the new single-witness contract. Its first reconstruction attempt failed honestly and was retained; the second lift supplied the exact accepted witness. Earlier source eliminations and character computations are imported as separately proved frozen inputs, not reported as newly rerun work. The independent contract/artifact review is `REVIEW_4019ecd9.md`; the independent promotion-proof review is `REVIEW_ed8c7251.md`.

No new computation is required for this synthesis. It does not claim completion of every older test suite, an equivariant marking of the printed matrices, a retained-gamma identification, or an RH consequence.
