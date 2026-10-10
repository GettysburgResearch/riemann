# Independent review of the anisotropic full A2 norm transfer

Reviewer: `descent_synthesis`. Date: 2026-10-10.

## Reviewed bytes and verdict

Reviewed file: `ANISOTROPIC_A2_NORM_TRANSFER.md` in the sibling `moving_labels` work directory.

Reviewed SHA-256: **`e671b8b1c8717ed494b3db0ba39fb4c0de374aef56f774bf9a7ca68e01b277cf`**.

**Verdict:** the anisotropic inverse estimate and its transfer to the complete normalized A2 polynomial are supported by the supplied proof, conditional on the explicitly imported completed estimate and sieve. I found no remaining gap in the arbitrary-positive-cutoff argument, the exact A2 projection, the correction-label exponents, or the complete norm summation. In particular the proposed all-row bound at `H = D^(1/2)` transfers to the full A2 coefficient with exponent `31/19 + epsilon`, subject to the named angular input. The counting version transfers with exponent `5/3 + epsilon` without that angular input.

This review is bound to the hash above. It does not certify the imported theta, cusp, sieve or angular theorems afresh, and does not turn the positive norm into the original signed first-Poisson estimate or a zeta zero-free result.

## Sources actually compared

- PR #914, commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`, `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`: Proposition 3.1, Theorem 4.1 and the fixed-auxiliary normalization (5.8). I read the exact git object, including the coefficient and phase proof.
- PR #918, commit `cfa102748b26f840ccc4b963a660711424db0ec3`, `standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md`: the tensor-test convention, masked cube identity, child parameters and normalization.
- Companion `MIXED_LABEL_COMPLETION.md`, inspected at SHA-256 `5e77ec88d6a191ec214bcedebc2b42d37f95735ba2bb18955b2f8a16aedfbcad`: Theorem 2.1 and the exact identities (7.2), (7.5), (7.6). The completed estimate is the analytic hypothesis used for the present review; its proof and source qualifications remain separately recorded.
- Companion `SIXTH_POWER_STRATIFIED_INVERSE.md`, SHA-256 `f98cc20e361ebb99af7dbd4b5ffef83a8a55ca11c4d3f24da238bc24be4cb2e9`: the sixth-power-free sieve, literal row masks and optimization. My separate hash-bound review of that note remains applicable.

## 1. Arbitrary positive cutoff and anisotropic support

Fix one sixth-power stratum `k = u v^6 k0`, with `k0` sixth-power-free; overlap between `v` and `k0` is allowed. For every squarefree physical column, the identity `chi_n(v^6) = 1_(n,v)=1` supplies an actual column mask. It gives `Q_v <= Q Nv` and physical row scale `H_v` comparable to `H/(Nv)^6`. The required nonempty row annuli below one are bounded below by `1/2` and may be enclosed in a fixed-size row ball, as in the companion proof. There is no unbounded small-row-scale extrapolation.

The support condition on the second weight gives `Nt, Nd <= K B^(1/3)` for a fixed `K`; choosing it at least the cube root of the upper support endpoint makes the cap at least one whenever the rectangle is nonempty. Therefore:

- if `R_v = min(K B^(1/3), R Nv) < 1`, the short sum has no ideal index;
- if `R_v = K B^(1/3)`, the long sum is exactly empty;
- otherwise `R_v = R Nv` exactly, which is the equality required for the negative powers in the long-tail estimate.

These statements hold for every `R > 0`, with no analytic constant depending on `R`. Harmonic sums are bounded by the physical support, so an arbitrarily large or small free cutoff does not introduce `log R` into the constant.

For the short sum, the completed middle factor obeys

\[
B_t^{-1}\min(A,\sqrt{B_t})^{2\beta-1}
\le B_t^{\beta-3/2},\qquad B_t=B/(Nt)^3,
\]

because `2 beta - 1 > 0`. The three norm sums with inverse coefficient `1/Nt` are consequently harmonic, of order `R_v^(kappa/2)`, and of order `R_v`, with `kappa = 9/2 - 3 beta`. The small nonempty factor scales are bounded below by fixed support constants, and rescaling their test functions to unit scale has uniformly bounded seminorms and normalization factors. This justifies the displayed use of the original powers of `A` and `B_t` even in that bounded region.

For the long sum, the coefficient is the exact finite divisor sum

\[
c_{R_v}(d)=\sum_{t\mid d,\ Nt>R_v}\mu_K(t).
\]

The regrouped index `d = t b` is unrestricted apart from its original exclusions and support. Neither squarefreeness of `d` nor coprimality of `t,b` is inserted. Its outer mask is `rd`; the inner squarefree index may still overlap `d`. After grouping its raw squarefree product column, the normalized coefficient vector has squared mass `O(D^epsilon)`: the coefficients have only divisor multiplicity, fixed bounded phases and literal masks, and the product length is `O(AB/(Nd)^3)`. The sixth-power-free sieve gives exactly the three terms in (2.9).

The sums of `(Nd)^(-5/2)` and `(Nd)^(-2)` over `Nd > R_v` have bounds `O(R_v^(-3/2))` and `O(R_v^(-1))` for all positive `R_v`. When `R_v < 1`, the full convergent sums suffice, since these negative powers are at least one. Indeed the exact divisor sum in that case vanishes for every `d != 1`, although that additional cancellation is not needed. The first, harmonic, norm sum is physically truncated.

Finally the physical strata are disjoint, so their energies are summed. The short powers of `Nv` are `-6`, `-13/2 - 3 beta`, `-17/3`; the uncapped long powers are `-6`, `-3`, `-6`. All are strictly less than `-1`. Using only uncapped strata for the latter terms is essential and is done correctly in the reviewed note. This proves its anisotropic six-term estimate from the stated inputs.

## 2. Exact full A2 projection and overlapping labels

The source support representation

\[
n_1=a c d^2e^2,\qquad n_2=b c^2d e^2
\]

uses five pairwise-coprime squarefree labels. The source's globally twisted coefficient is exactly

\[
\mathfrak a_\xi(n_1,n_2)=\sqrt{N(cde)}\lambda(cde)^3a_\xi(abe).
\]

I checked that its row symbol supplies `chi_cd(k)^3 chi_e(k)^4`, and that its starting auxiliary supplies the mask `(cde,f0)=1` together with `chi_e(f0)^4`. The exact CRT formula for `a_xi(abe)` changes the raw auxiliary to `e f0`. No principal symbol on nonunits is replaced by the constant one.

With the original normalization `1/sqrt(AB)`, the scalar projection cost is

\[
\sqrt{N(cde)}\sqrt{A_tB_t/(AB)}
=(Nc\,Nd\,(Ne)^{3/2})^{-1}.
\]

This agrees with both pinned source notes. The remaining exterior factor has absolute value at most one for every row, including rows meeting correction primes. It can therefore be discarded only after fixing a correction triple and taking its positive row norm, exactly as in the proof.

For `q_t = q0 cde` and `f_t = f0 e`, the source restrictions imply

\[
Nf_t=FNe,\qquad
N\bigl(q_t/(q_t,f_t)\bigr)=Q Nc Nd,
\quad Q=N\bigl(q0/(q0,f0)\bigr).
\]

This includes every inherited `q0/f0` overlap. In particular the correction prime `e` contributes to the auxiliary cost and is removed from the redundant exclusion cost. Treating it as disjoint from `q_t` would give the wrong estimate.

## 3. Independent exponent calculation and complete summation

I recomputed the correction exponents from the anisotropic theorem, rather than assuming the table. Set `u=Nc`, `v=Nd`, `w=Ne`; the child scales are

\[
A_t=D u^{-1}v^{-2}w^{-2},\qquad
B_t=D u^{-2}v^{-1}w^{-2},\qquad
R_t=R u^{-2/3}v^{-1/3}w^{-2/3}.
\]

Relative to the six parent energy monomials in (4.4), the child energy monomials have powers

| Term | `u` | `v` | `w` |
| --- | ---: | ---: | ---: |
| 1 | -1 | -2 | -2 |
| 2 | 0 | -1 | -1 |
| 3 | -1 | -7/3 | -2 |
| 4 | 0 | 0 | 0 |
| 5 | -1 | -2 | -2 |
| 6 | -2/3 | -4/3 | -4/3 |

The cancellation in term 2 is exact for the symbolic exponent `beta`, using `kappa = 9/2 - 3 beta`. Taking half of each row and adding the projection powers `(-1,-1,-3/2)` gives every entry in the note's norm-level table, including `-13/6` in term 3 and `-13/6` in term 6 at their respective labels.

Every nonempty correction label has norm at most a fixed multiple of `D`. Extending only these positive upper sums to independent ideal labels is valid. Every exponent below `-1` has a convergent ideal sum; term 2 has one harmonic sum, and term 4 has two. Thus the entire correction sum is bounded by `O(log(2D)^2)` times the sum of the six parent square roots. Squaring and assigning smaller preliminary epsilon losses proves the full six-term envelope. No correction labels are left outside the argument.

The child cutoff may be below one. Keeping that exact positive value is legitimate by Section 1 of this review and is necessary for the cancellations above; silently replacing it by one would not prove this table.

## 4. Optimization and exact scope

The resulting envelope is literally the balanced raw envelope already reviewed at the pinned companion hash. Its optimization applies under `H^2 FQ <= D^((5-2 beta)/2)`. Both parent candidate cutoffs lie in `[1,D^(1/3)]`; only child cutoffs may fall below one. The dominance of the remaining `HD`, `H` and mixed-tail terms follows from the same inequalities in that companion proof.

At `beta=11/12`, the transition and terminal row-height exponents remain `19/44` and `19/24`, and the energy exponent at `H=D^(1/2)` is `31/19`. For general labels the corresponding bound is `D^(31/19+epsilon)(FQ)^(12/19)` when `FQ <= D^(7/12)`. The alternative `beta=1` gives `5/3` at unit labels and that same row height. These conclusions concern the complete normalized A2 polynomial in (3.3), with all nonzero element rows, the stated separated weights and literal masks.

The reviewed file correctly keeps the two independently corrected columns, coupled row kernel, strict product-column off-diagonal restriction, signed auxiliary sum and adverse initial dual height outside this theorem. It asserts neither the original Möbius fourth moment nor the `17/24` zero-free goal. The new established step within the source-qualified argument is closure of the entire unsigned A2 correction sum at the improved raw norm.
