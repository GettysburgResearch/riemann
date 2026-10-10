# Independent review of the October 10 geometry and height components

**Status:** the new geometric deduction passes this source-level mathematical review, conditional on the imported analytic statements listed in its dependency ledger. The author froze the reviewed geometry file on 2026-10-10. No remaining mathematical must-fix was found in that frozen file.

**Scope:** an independent review by the formalization/Euler audit agent of the geometric adapter, the geometric envelope limit, the causal inverse note, Sections 4–6 of the native height note, and the exact gcd decomposition and conditional norm reduction in Proposition 3.1 of `FOURTH_MOMENT_REDUCTION.md`. The local Euler and tail-criterion note was authored by this reviewer and is therefore listed separately as a contributed component, not as independently reviewed by its author. The broader completed-height and higher-moment extraction arguments in `UPSTREAM_HEIGHT_AND_MOMENTS.md` are not independently reviewed by this report.

**Exact source:** the September 30 manuscript at upstream commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, resident in the October 7 import. Its reviewed local SHA-256 is `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` (766,316 bytes). All source line numbers below refer to this exact file.

**What was actually run:** direct mathematical comparison with the source interfaces; exact rational and sparse-polynomial calculations; independent ordinary and optimized Python runs of the packet's tail/Euler and research-algebra checkers. No fresh Lean kernel build, full independent reconstruction of the upstream analytic proof, zero census, or proof of a new moment estimate was performed.

**Review boundary:** this is a review of the new conditional deduction and its stated mathematical inputs. It does not certify the imported framework independently, establish RH, establish a band tending to the critical line, or verify an unspecified future repository commit. The byte hashes in Section 6 identify the reviewed objects; a later change requires its own comparison or review.

## 1. Geometric theorem: accepted conditional scope

The reviewed statement is that the explicitly listed imported analytic machinery implies

\[
L(s,\eta)\ne0\qquad
\left(\Re s>\frac{139999}{160000}\right)
\]

for finite-order Hecke characters over the Eisenstein field, with the source's transfer to Dirichlet characters. The principal pole is allowed, and the boundary line is not included. This improves the imported constant by exactly `1/160000`, conditionally on the same framework.

The main normalization check is

\[
C(s)=s-\frac{11}{16},\qquad
L_0=\frac3{16}-\frac1{160000}.
\]

Thus the signal exponent is unchanged while the direct physical estimate improves. Merely moving the comparison boundary would not give this gain; the altered low calculation is essential.

The review checked the following load-bearing steps.

### 1.1 The generalized low estimate carries its actual loss

The source's reflected-energy calculation is stated for general bounded lengths (lines 7747–7820). Repeating the row proof at lines 8132–8330 with `M+ell=1`, a rescaled subset length `d`, `M'=M-2d`, and `ell'=ell-d` gives

\[
E_{\rm ref}\le M'+\frac{(5\ell-1+d)_+}{4}+\epsilon.
\]

The change from the published zero-loss specialization is real and has been retained. The actual row-dyad condition `Delta_H >= -o(1)`, the inequality `T_d <= H-3d+o(1)`, the two branches of the hybrid minimum, and the order of extracting the common kernel amplitude agree with the source. The proof does not replace actual row dyads by a hypothetical extremal row.

After Cauchy–Schwarz, tuple counting, the scalar factor in the physical combination, and the rescaled square-root length, the additional exponent is exactly

\[
f_\ell(d)=-d+\frac{(5\ell-1+d)_+}{8}.
\]

Its two slopes are `-1` and `-7/8`; for `ell <= 1/5`, its maximum over `0 <= d <= ell` is zero. This proves the required final low estimate despite the loss in some individual row norms.

For the actual rational tuple, the shortest row length is `19997/40000`, the shortest x length is `44991/240000`, and the Gram domination slack is `19991/240000`. Each is strictly positive. The physical prime windows stay at their original scales in every summand. Equation 2.4 of the frozen file has the correct three-argument source operation, including third argument `Z * Np_(J^c)`.

### 1.2 The row count uses an admissible fixed plain parameter

The imported `7/8` conclusion is used as the starting input. Consequently the source's plain fourth moment is admissible at the fixed parameter `kappa=3/4`, and the actual dynamic range has `delta <= 3/4`.

The inverse and plain capacities are then precisely `(1-r)/2` and `2(1-2m)/9`. The source crossing and strict capacity margins can be reused: the inverse capacity is at most `7/37`, the plain capacity at most `2/27`, and zero-capacity neighborhoods use the no-slot bounds. The proof does not substitute a negative value into the published second-stage capacity penalty. In this fixed-parameter use, that penalty is absent for a stated reason.

The total available length, its frequency extension, the mesh, the disjoint underlying prime windows, and the separate centered amplifier pool were checked against the source's order of choices. The new tuple retains the strict supply inequalities.

### 1.3 The principal analytic domain is genuinely extended

The source's shared contour interfaces explicitly assume `sigma0 >= 7/8`; the new proof does not invoke those statements outside their hypotheses without an adapter.

On the enlarged principal rectangle with `Re s >= 437/500`, the exact source local formulas give good-prime decay `Q^(-907/500)`, ramified decay `Q^(-103/125)`, and selected principal relative error `Q^(-437/500)`. The first is summable; the finite ramified product has the source's divisor-product bound. These estimates are uniform in all imaginary parts and unit target phases. They give a fixed excluded cutoff for the shared nonvanishing contraction.

Holomorphy of the full selected correction is obtained from its quotient-free finite expression. Division by a local Euler factor is used only on the principal region where its nonvanishing has been established. The dynamic contour remains in the unchanged first Euler region. The principal contour and its two scalar residues lie in the explicitly enlarged second region.

The principal residue has the same scalar `c_S`, including the factor `1/6` and the squared zeta residue. The fixed-ray prime normalizer is eventually nonzero. Its logarithmic reciprocal cost is subpower, and the same excluded set and normalizer are used for the direct physical estimate and the high identity.

### 1.4 The common exponent and quantifier order close correctly

The source's exact old endpoint certificate has margin `49/440640`. At fixed `b=1/8`, the derivative with respect to `ell` is bounded by `5/2` on the entire old parameter rectangle. Increasing `ell` by `1/40000` therefore leaves the exact positive margin

\[
\frac{1073}{22032000}.
\]

The floor, intermediate, small, principal and extended moderate ranges retain strict margins; the large-row absolute contour can still be moved far enough to provide the required saving.

Under the contradiction assumption `Delta0=beta_* - beta0 > 0`, the real losses, slot system, cutoff, and positive high margin are fixed before the target. The constants and sufficiently large lower thresholds may depend on the target, as permitted by the continuation criterion. Internal height orders are fixed before the external decay order. The auxiliary height exponent may depend on the target and is chosen after those orders; the external order is chosen last.

This provides common positive low and high exponent margins. The resulting physical probe and principal signal are independent of the auxiliary height cutoff. The final use of the continuation criterion does not assume that the supremum of zero real parts is attained. These are the relevant quantifiers in the source criterion at lines 400–507 and in the late-height closure.

## 2. Exact limit of this geometric envelope

The envelope note also passes independent algebraic review. At

\[
x=\frac12,\qquad
\delta=\frac{49-\sqrt{921}}{48},
\]

the displayed balanced row count is exactly `R_*=2/3`. This cancels the imbalance parameter `b` from the high exponent. Strict negativity of the specified envelope requires

\[
\ell<\frac{8\sqrt{921}+33}{1653},\qquad
\beta_0>\frac{1507-2\sqrt{921}}{1653}
=0.874957067\ldots.
\]

The point lies inside the required rectangle. The denominator is positive, and the coefficient of `ell` is positive. The exact algebra and the certified decimal enclosure agree.

This is a limit of the particular uniform sufficient envelope, not a lower bound on the true zero-free constant. The note explicitly allows that actual arithmetic rows might satisfy a stronger joint restriction. That qualification is mathematically necessary and is present.

## 3. Causal inverse, native height, and squarefree-column components

The causal note's finite convolution inverse and its one-sided Mellin multiplier are correct with the lower cutoff retained. Its absolute weighted estimate preserves a source exponent `a` when `c+a>2/3`; with `c=11/16`, the resulting floor is `-1/48`. The conditional derivative/Abel-summation estimate requires actual angular summatory cancellation and gives threshold `(3+theta)/6`. The note correctly identifies the auxiliary angular character as infinite order and does not apply the imported finite-order theorem to it. It also correctly leaves the physical-probe and initial-data adapter open.

Sections 4–6 of the native height note pass the checked analytic estimates: the Euler truncation remainder, the zero-to-polynomial adapter, the local Sobolev lower mass, and the diagonal/off-diagonal expansion. In particular, at a detected zero the stated local energy lower bound is `1/(6 Omega)`. The derivative term is essential for that lower bound. A small long-interval average alone does not exclude individual zeros.

The shrinking-band arithmetic estimate remains an explicit missing input. The vanishing diagonal estimate does not supply the signed off-diagonal saving. No numerical finite-height control in this pass establishes that missing estimate or an asymptotic zero-free band.

Proposition 3.1 of `FOURTH_MOMENT_REDUCTION.md` was additionally checked for this final packet. The decomposition by `c=gcd(n1,n2)` retains the squarefree and pairwise coprime factors, the common-factor phase, and the nonunit zero extensions. The exterior phase is a contraction on the row norm. Under the explicitly unproved estimate (3.5), Minkowski gives a harmonic common-factor sum for `Nc<=D`; the bounded factor scales for `D<Nc<=bD` contribute only the stated `O(D sqrt(H))`. This proves the conditional reduction, with a squared logarithm absorbed into the arbitrarily small power loss. It does not supply (3.5), remove its uniformity in the moving exclusion, or shorten its stipulated row range.

## 4. Exact computation reproduced

The packet checker `checks/check_tail_euler.py` passes **83 explicit predicates**. These cover exact local polynomial identities and rational affine envelopes, including the instance `alpha=437/500`. The ordinary and `python -O` runs have identical stdout, SHA-256 `ad2c47b0b8af2d5884710f4f3c5829095b15aa08ff18d028c051895abf6e7323`.

The final packet checker `checks/check_research_algebra.py` passes **148 explicit predicates**. These include the original endpoint polynomial identity, the new rational tuple and margins, exact arithmetic in `Q(sqrt(921))`, finite causal convolution controls, conditional extraction-exponent identities, and 90 exact weighted gcd-decomposition panels. Its ordinary and optimized runs have identical stdout, SHA-256 `fb51e01d92b5dc6e94c56f63674bd0276597017d1e36c020bff6c22a1ec64649`. Both checkers also reproduce their recorded `results/*.json` byte for byte.

The 90 added panels use five integer scales and eighteen row labels. Their column phases take values in `{+1,-1}`, are completely multiplicative away from nonunits, and vanish when a column meets the row. The exact rational smooth weights and full finite gcd sums test the source-shaped algebraic identity, including its masks. They do not compute the actual Eisenstein sextic residue symbols, cover all possible phases by enumeration, or authenticate an arithmetic moment estimate. The general identity is justified by the symbolic proof, not by extrapolating these cases.

Acceptance in both checkers uses explicit exception-raising conditions, not Python `assert`. The outputs therefore do not silently lose their gates under optimization. These finite exact checks authenticate the displayed algebra; they do not verify an infinite analytic estimate. The native numerical checker was not independently rerun by this reviewer and is outside this computation-replay statement.

## 5. Remaining dependency and verification boundary

The conditional geometric corollary fails if one of its listed imported analytic statements fails in its actual uniform coefficient class. The source's reflected marked energy, additive Gram bound, buffered detector, inverse/plain moments, dynamic error allocation, and external-tail calculus remain substantive inputs. This review checked their use and the new adapters; it did not rederive their full proofs independently.

No Lean realization of the new rational tuple or its new low-bound lemma was supplied, and no Lean kernel build was run here. The earlier lexical scan and import-closure checks on the vendored implementation are separate provenance results. Absence of lexical placeholders, a complete source import, or matching file hashes is not a replacement for a kernel build or an independent analytic proof review.

Further large progress requires an additional arithmetic input or a different probe. Neither the small rational geometric gain nor the exact auxiliary factorization supplies a band tending to `1/2` by itself. The native local-energy route and the higher-moment route preserve their stated unresolved source estimates.

## 6. Final packet bindings

All paths below are relative to the final packet `standalone/2026-10-10-quasi-riemann-height-descent`. These hashes were recomputed from the destination files after assembly. `GEOMETRY_PERTURBATION.md` is byte-identical to the author's explicitly frozen proof. The destination `TAIL_AND_EULER.md` was compared against this reviewer's draft: its changes correct the published-import wording, use the local checker path, and record the completed conditional geometry construction. They do not change its mathematics.

**Final editorial normalization:** one extra blank line at EOF was removed from `NATIVE_HEIGHT.md` and `checks/check_native_height.py`, preserving exactly one final newline in each. No mathematical text, executable code, or other theorem content changed. The native note binding below reflects only that whitespace normalization.

The scope column is part of the binding: recording a dependency hash does not imply an independent review of every theorem in that file. In particular, this report does not extend the independent review to the whole upstream-height note or to all sections of the fourth-moment note.

| Final packet file | Scope in this report | Bytes | SHA-256 |
|---|---|---:|---|
| `GEOMETRY_PERTURBATION.md` | Complete new conditional deduction | 35,888 | `6e3befcc15b92536dd80f376a87384d5fa4688a938c11d949be7924d4a4c1e12` |
| `GEOMETRY_ENVELOPE_LIMIT.md` | Exact envelope algebra | 5,853 | `9118bde4dd41557cb155f15304cbd58dd0c0a0852a5ca551f6d59d72aeedde80` |
| `CAUSAL_AUXILIARY_FACTOR.md` | Abstract operator and conditional weighted bounds | 7,410 | `fdd44e2be5ccfd50b073f09aaf4295188f2c534adda6d51120b1b1738e87ce06` |
| `NATIVE_HEIGHT.md` | Sections 4–6 analytic estimates | 24,189 | `75bfb4c03058f7e9a17da08fdb9d83340a40eb376e0c136b91c2b950a14fae7f` |
| `FOURTH_MOMENT_REDUCTION.md` | Proposition 3.1 identity and conditional norm reduction | 12,862 | `8dc1b1377ee3205dd791fac64195513a98ac569f403d4f8b56253e0860355e7f` |
| `TAIL_AND_EULER.md` | Reviewer-authored component; final editorial comparison | 34,444 | `9bc21c039465f14c9125f97718c82b91f3a91be334ab9071ce74dd50a90a81a0` |
| `UPSTREAM_HEIGHT_AND_MOMENTS.md` | Dependency/context binding; not a full independent review here | 43,651 | `17b039afccc1d8bb3b440e1b216e3a94facd2d73493141f17cd50eee193a66b5` |
| `checks/check_tail_euler.py` | Source inspection and exact ordinary/optimized replay | 8,000 | `355a05fd9ea92b7b497fe78e12972d498450e6a5104562a3f762e226c42696f3` |
| `checks/check_research_algebra.py` | Source inspection and exact ordinary/optimized replay | 9,450 | `532ae0038e015f1a4674683c299e783c6b50b3a0ff1bc23589a0161f1a222ef6` |
| `results/check_tail_euler.json` | Byte-identical independently reproduced output | 2,382 | `ad2c47b0b8af2d5884710f4f3c5829095b15aa08ff18d028c051895abf6e7323` |
| `results/check_research_algebra.json` | Byte-identical independently reproduced output | 807 | `fb51e01d92b5dc6e94c56f63674bd0276597017d1e36c020bff6c22a1ec64649` |

The native numerical checker and its recorded output were not independently replayed by this reviewer; their verification, if claimed elsewhere, belongs to that separate stated review. The review report itself is not self-authenticating: publication must bind these bytes and this report in the frozen repository head. No commit, push, or mathematical-content change was performed during this final review update.
