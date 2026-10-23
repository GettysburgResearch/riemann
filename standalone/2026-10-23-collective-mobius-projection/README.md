# A growing Gauss projection with a power saving

23 October 2026. Proposed, source-dependent research; component reviews are included. **This packet does not lower the fixed zero-free boundary and does not prove RH.** Its main advance controls an actual growing projection of the specific Möbius inverse vector, including both its residue and its continuous remainder. The complementary space is still open.

The numerical checks here authenticate finite algebra only. The analytic proofs retain the imported inverse theorem, completed functional equations, local inversion, and Gram conditioning. These external and earlier standalone inputs are not turned into independently established theorems by this packet.

## Main statement and a concrete comparison

Use the pure Möbius column coefficient, fixed ray data, smooth annuli, and literal nonunit zeros specified in `LABEL_UNIFORM_MOBIUS_RESIDUES.md`. Let `A_U` be the inverse matrix with row scale `U` and column scale `D`; let `P_K` be orthogonal projection onto the actual Gauss vectors indexed by good sixth-power-free labels of norm at most `K`. The proposed bound is

\[
 \|P_K A_U\overline b\|^2
 \ll (UDKNQ)^\epsilon
 \{KU+D^{11/12}K^{13/12}+U^{1/3}D^{2/3}\},
\]

for `K <= D^(1/7)` and the stated conditioned-Gram range `K <= U^(1/2-delta)`, with fixed positive margin and the inherited puncture uniformity. This is a bound for the actual coefficient, not an arbitrary-coefficient operator estimate.

At `U=D^(6/7)` and `K=D^(1/32)`, it gives `D^(20/21+epsilon)`. The inherited nonvolume resource is `D^(41/42+epsilon)`: the projection gains the fixed exponent `1/42` on a growing label family. It does not follow that the entire inverse vector has that saving.

Under the additional ordinary good-ideal Mertens premise `sum_(Na<=X) mu(a) << X^(beta+epsilon)`, `2/3<beta<1`, the continuous term improves to

\[
 D^{(13-2\beta)/12}U^{-(1-\beta)/3}K^{(15-2\beta)/12}.
\]

For the explicit conditional example `beta=7/8`, the same `1/42` saving holds with the larger family `K=D^(1/24)`. This premise is not a conclusion of the finite checker.

## Selected proof chain

1. `LABEL_UNIFORM_MOBIUS_RESIDUES.md`: uniform fixed-label residue bound; read `SOURCE_PIN_ERRATUM.md` for the corrected source hash.
2. `SHORT_LABEL_RESIDUE_VECTOR.md`: simultaneous squarefree-label finite norm and residue estimate.
3. `SIXTH_FREE_LABEL_EXTENSION.md`: all good sixth-power-free labels, including every principal local branch; optimized full-residue reference scale.
4. `PRIMITIVE_LABEL_CONTINUATION.md`: complete primitive remainder with a fixed label, retaining the moving-coprimality inversion and every reciprocal completion scale.
5. `ACTUAL_PROJECTION_BENCHMARK.md`: exact projection, Gram interface, and the rational power-saving example. The projected vector is `A_U conjugate(b)`, not the adjoint applied to a column vector.
6. `SIGNED_COMPLETION_PRIMITIVE_PROJECTION.md`: separate conditional refinement from cancellation in the global reciprocal-completion ideal.

The component reviews bind exact SHA256 identities. Some frozen author headers still say “review pending”; the subsequently dated review files record the completed review. Frozen source prose has not been rewritten to change its identity. In the signed-completion note, the workspace-relative predecessor path resolves to the same-named file at this packet's root; its printed SHA256 is the binding identity.

## Other results and unsuccessful approaches

The quartic chain is `QUARTIC_PHYSICAL_ORIENTATION.md`, `QUARTIC_CUBIC_NUMERATOR_TAIL.md`, then `QUARTIC_OPTIMAL_SIEVE_TAIL.md`. The physical inverse Fourier family is the cubic-numerator family `g4(k^3,c)`, with its specified angular factor. The older native numerator-`k` transfer is not licensed. An exact cyclotomic check rejects that incorrect identification. The stronger physical tail uses the newer fourth-power-free sieve and retains its principal branches.

`PHYSICAL_QUARTIC_CUBIC_ROW_MEAN.md` gives a source-dependent, orientation-correct completed mean. Its optimized raw annular consumer is only `D^(17/12+epsilon)`, too large for the required inverse bound. A useful completed mean is not automatically a useful physical annular mean.

`REFLECTED_VECTOR_COMPLETION_SCOPE.md` retains the full completion variable and identifies the lost gain in a tempting reflected-vector estimate. `SIGNED_LEVEL_CUSP_OBSTRUCTION.md`, `FINITE_CUBE_FREQUENCY_TRACE.md`, and `ALL_PRIME_LOG_MARK_INTERFACE.md` record three further precise obstacles. They do not refute all possible centered projectors, trace identities, or redesigned detectors.

## Evidence and exact scope

Run `python replay.py`. It verifies the component manifest and runs four finite checkers in isolated temporary copies, both normally and with `python -O`, comparing outputs. No third-party Python package is required. `REPLAY_RESULTS.json` records the replay. The tests cover local exponent bookkeeping, affine parameter ranges, the exact projection benchmark, and a prime-5 quartic Fourier countercheck. They do not verify analytic continuation, functional equations, infinite sums, or a zero-free theorem.

`COMPONENT_MANIFEST.json` pins the unchanged new components and selected earlier repository files. The complete selected PR1013, PR1015, and PR1016 directories are preserved under `imports/`, with exact Git commit and original path. **Their inclusion preserves provenance; it does not endorse every historical claim in their READMEs.** The source chain selected above and the quartic orientation correction govern this proposal. External papers are linked and version-pinned in `EXTERNAL_SOURCES.json`; the rstation snapshots are hash-identified but not republished.

The smallest missing statement for a boundary improvement is a power saving for `(I-P_K)A_U conjugate(b)` in the binding range, or a signed first-Poisson identity that bounds the complete physical inverse norm using the controlled projection. A scalar large-sieve inequality does not supply that spectral statement. No such complement theorem is claimed here.
