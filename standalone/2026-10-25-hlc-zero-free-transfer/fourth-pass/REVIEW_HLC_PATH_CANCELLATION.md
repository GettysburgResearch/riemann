# Independent internal review: HLC determinant bridges and backtracks

Reviewer: `/root/coherent_identity`, a separate mathematical worker from
the author. This is an internal proof review, not external peer review
or formal verification. The reviewer did not author the mathematical note
or its checker. One wording correction was requested and accepted: the
integer backtrack theorem restores unordered complete lists, not a
particular ordering of their entries.

## Reviewed files

| File | SHA256 | Git blob |
|---|---|---|
| `HLC_PATH_CANCELLATION.md` | `dc806ea8c6b26b6419ae90a3fa8003bd971c7358ed4dba7babb8c82dd8b2fc9b` | `adbe598b517ad5c6c45385b4adc5e5e20eba25f7` |
| `check_hlc_path_cancellation.py` | `92f80b303bf21ebcf60470d85176213b2f76ce36017db3f456b9666ea4b61c58` | `618a293bf2b1c7acb7afd2209d31decc7404dc01` |

**Assessment: pass for the stated finite operator identities, the
conditional projection comparison, the source-qualified integer
backtrack theorem, and the explicitly scoped phase-separation bound.**
No proof of the required integer residue completion, a new native
inverse estimate, a power-saving HLC theorem, or a new zero-free region
is supplied by these statements.

## 1. Complete determinant operator and exact returns

I rederived the two-step kernel by counting the intermediate vector.
When the endpoints are independent there is one solution; when the
final endpoint is a scalar multiple of the initial endpoint, there are
p solutions precisely for the scalar `-d/c`. This gives the displayed
normalization `p^{-1} S_{-d/c}+p^{-2}(J_Sigma-B)`.

The constant, projective-line, and within-line radial subspaces are
orthogonal and invariant. On line-constant mean-zero functions the
operator is `-1/p`. On radial functions its product with the adjoint is
`1/p` times the identity, so the singular value is exactly `p^{-1/2}`.
The distinction between the unnormalized B and J_Sigma sums and the
normalized constant projection is handled correctly.

For an even number of edges, pairing consecutive operators yields the
stated radial permutation and the factor `p^{-m}`. For an odd number,
one remaining nonzero determinant step has zero kernel from a line to
itself. The constant component gives exactly
`q_k=(1+(-1)^k p^{1-k})/(p+1)`. In particular the conditional
three-step kernel is the normalized rank-one constant projection,
whereas the two-step conditional kernel is a permutation with centered
norm one. A zero-determinant step has p-1, not p, available nonzero
targets and annihilates the radial subspace; the note retains that
different normalization.

## 2. Internal projections and their exact probability law

For fixed endpoints on the recorded line, there are exactly p
three-step bridge pairs. Both intermediate vertices are outside that
line, and their marginals under uniform endpoints and uniform bridge
pair selection are uniform on the stated set of size `p(p-1)`.

The restricted kernel, relative to uniform endpoint probability, is
therefore an average of p products of two zero-one projectors and lies
between zero and one. Its deleted mass is at most `delta_1+delta_2`.
The Hilbert--Schmidt argument gives the displayed square-root norm
bound; the same deleted-mass estimate gives the bounded-endpoint pairing
bound. Arbitrary fixed endpoint projectors contract these bounds because
the correctly centered difference is projected as a whole.

The normalization is deliberately the original complete return mass.
The note does not silently renormalize the restricted kernel by an
endpoint-dependent surviving mass. Nor does it substitute a real-phase
exceptional measure for a conditional finite-bridge density. The
comparison estimate for an actual integer operator remains an explicit
additional premise.

For two steps, the source fibres partition the intermediate set. A
nonprincipal multiplicative character on the recorded line is a
mean-zero constant-modulus test, and Jensen's inequality gives the
claimed lower bound `(1-delta)^2`. The distinction between one
uninterrupted even bridge and repeatedly conditioned two-step bridges
is mathematically necessary and correctly retained.

## 3. Source-level integer backtrack check

I checked the supplied PDF text of Lü--Wang--Wu,
[arXiv:2610.20242v1](https://arxiv.org/pdf/2610.20242), particularly:

- the complete-list good-state conditions (4.14)--(4.15), pp. 18--19;
- the Fock transfer, distinct-new-selection rules, and local factors
  (4.37)--(4.38), pp. 26--27;
- the position parametrization (4.40), p. 28;
- the dirty raw determinant and phase condition (4.47), pp. 30--31.

The supplied PDF is the previously recorded 734761-byte source with
SHA256 `32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`.
This source check concerns these exact inputs; it is not a review of the
paper's full proof.

The important extra use of goodness is valid. With I equal to all
groups, the fresh-prime tuple is empty and has mass one. Its only choice
cannot be removed by an exceptional allowance strictly below one.
Thus the full-I separation holds for every pair of distinct D Z products
in the stated finite collection, regardless of whether a particular
edge would have called some lower-group choices fresh.

The reverse of the preceding edge supplies a legitimate comparison
candidate. Its shared product is obtained by omitting the newly incoming
entry in each complete middle list. Its departed lower-group primes are
outside those middle lists, exactly as required by the cross-edge rule.
Both candidates satisfy the same recorded top-prime line and the same
position phase window. Their distance is at most `32/p`, strictly less
than the source's `100 exp(-L^{a_K})` separation. Equality of their D Z
products follows.

Unique factorization separates the current-list primes in D from the
outside primes in Z, and the disjoint group sets recover each incoming
prime value. Hence every unordered complete list is restored. Opposite
integer determinants then give `z_2-z_0=k z_1` with integer k, using
primitivity. The common positive position window bounds k absolutely;
the common recorded projective line and the nonzero determinant modulo p
give `p|k`. For sufficiently large p this forces k=0.

This proves a genuine integer position-and-list backtrack under the
stated raw-edge and good-state hypotheses. The note correctly does not
identify the remaining Fock memory with its initial value, identify the
whole two-edge Fock operator with the identity, or equate such a trace
contraction with the diagonal of the original native Möbius moment.

## 4. New phase-separation and norm statements

Section 5.2 is a direct Haar-measure union bound. For each nonzero integer
x-y, the phase map preserves uniform circle measure. Its bad set has
measure at most `200/P_min`. Counting unordered pairs gives
`100 M(M-1)/P_min`, capped by one. The displayed cardinality bound for M
and the polynomial consequence follow. For the example
`epsilon_i=3^{i-1} epsilon_1`, the geometric sum gives gamma exactly
epsilon_1. These are statements under the specified cardinality and
minimum-prime assumptions; the note does not import the original
prime-list normalization into a changed polynomial band without checking
it.

I also checked the original-list matrix-entry normalization. There are
`(J!)^K` compatible orderings among `((J+1)!)^K` equally weighted
orderings, giving `(J+1)^{-K}`. The equal state masses cancel in the
normalized unordered-list vectors. The resulting operator-norm lower
bound is expressly conditional on a retained good raw edge with the
specified nonnegative cutoff size. No existence of such an integer edge
is inferred from a complete finite-field model.

A further proposed backtrack estimate was rejected during this review:
there is no `1/Y` multiplier in this original matrix entry. The source
kernel has `d_0/D` times `eta(a/Y)`, not `d_0/(DY)`. Copying the `1/Y`
from a separately converted clean auxiliary operator would falsely turn
a row-count estimate into a power saving. The author independently
caught this normalization error; it was withdrawn before publication,
and the final mathematical note explicitly records the distinction.

The final diagonal identity (32) is also correct in this orthonormal
unordered-state basis: its diagonal is the sum of squared raw matrix
entries. Under the explicitly assumed retained-edge hypothesis, one
entry gives the stated positive lower bound. The constant c_0 includes
the full remaining nonnegative multiplier, in particular `d_0/D`.
This does not lower-bound a full signed arithmetic pairing or the native
inverse moment; the note correctly states those limits. Its conclusion
is that identifying a geometric backtrack does not automatically make
that contraction small in the original operator norm.

## 5. Independent execution and limits

I ran `python -O check_hlc_path_cancellation.py` independently. It passed
with, among other checks:

- 1,532,416 two-step matrix entries;
- 2,476 exact line-return entries and 936 zero-step entries;
- 408 bridge marginal counts and 720 projector error checks;
- 110 two-step mask cases and 88 short-return schedules;
- 37,430 integer backtrack cases and five full-I phase cases;
- 12 exact phase-interval union cases and eight polynomial hierarchies;
- 25 list-symmetrization cases and the stated negative controls.

The finite program validates algebra and finite instances. The analytic
source assumptions, source-level uniformity, actual integer residue
completion, and any all-scale arithmetic pairing must be justified in
text; this checker does not establish them. The note preserves those
limits and does not promote a finite centered-bridge identity into an
unproved zero-free consequence.
