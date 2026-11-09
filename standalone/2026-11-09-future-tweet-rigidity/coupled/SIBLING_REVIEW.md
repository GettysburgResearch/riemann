# Independent review of the local frame and weighted transfer

9 November 2026. Reviewed by the author of the coupled-kernel component,
independently of the authors of the two components below. This review checked
the stated formulas and the checker implementations. It did not replay the
imported analytic theorems or establish a native arithmetic saving.

**Result:** no mathematical blocker found in the reviewed versions. The
coefficient cost, quadratic-character exception, local axes, nonunit sectors,
and prime-versus-composite scope are explicit. The observed receipts report
8,205 local-operator predicates and 2,382 weighted-transfer predicates. These
are read receipts, not a claim of an additional independent execution here.

## 1. Local frame

The Mellin identity (5) follows by first summing the nontrivial additive
Gauss sum in z and then changing the remaining sum to a Jacobi sum. For the
product kernel ht, the weak input character is chi, consistently with the
entrywise Gram in the coupled note. Centering removes exactly the constant
unit vector. Averaging two distinct nontrivial characters gives two
orthogonal exceptional projectors, so the sharp lower eigenvalue is
(1+1/q)/2. The displayed inverse acts by its reciprocal on those two
directions and by one on their orthogonal complement.

The native quadratic case cannot use its identical conjugate as a second
channel. The current note records this and distinguishes introducing a
different auxiliary output from proving a bound for that output. The
distinct-character corollary is a direct consequence of the same Gram
identity and does not replace the native quadratic phase.

For tensor products, the primitive bank sees exactly the tensor of the
locally mean-zero spaces. Adding each local constant projector restores
all other sectors; subtracting only the all-constant output removes just
the global constant. The 3^r count and product lower gain follow from the
orthogonal sector partition. The extra zero-coordinate projectors are
necessary on full residue fields. The proof of subpower channel count uses
distinct prime ideals in a fixed number field; it cannot be replaced by an
arbitrary abstract tensor limit. The note correctly avoids turning this
algebraic reconstruction into an analytic composite-modulus theorem.

The checker constructs the local kernel independently from its definition
and checks its full Gram at q=7,13. Subsequent exact projector/tensor tests
verify the decoder and sector accounting. It shares the coupled component's
cyclotomic arithmetic implementation, so it is not an independent arithmetic
backend. The quadratic extra-channel check uses the proved Gram formula,
not a separate direct quadratic Gauss-sum computation.

## 2. Weighted completion

The normalization in equation (1) is correct: unnormalized Fourier
inversion contributes 1/q, while T(h,t)=sqrt(q) K(ht) away from the axes.
The h=0 term is the complete original nonzero-x diagonal. The t=0 term
on h nonzero has coefficient -1/q. No one axis substitutes for the other.
Affine reindexing requires nonzero A,B; zero extension kills the stated
local character product when either vanishes.

The Moyal identity is exact for arbitrary distinct f and g. Its proof only
uses Plancherel and the bijection (h,x) to (x,x-h). General coupled source
weights retain Fourier inversion but need not inherit the factored norm
bound. The note makes this distinction.

The infimum of sums of products of L2 norms is the matrix nuclear norm,
with the conjugation absorbed into the second vector. Applying FKMS to
each product therefore proves equation (7), and condition (8) is the stated
sufficient condition for a saving relative to Frobenius size. It is not
claimed as necessary or as proved for the native source.

The chirp calculation gives t=2ch exactly. Its unit-domain matrix is a
phase-weighted permutation with q-1 singular values q. The proposed
restricted rectangles contain M distinct support points in distinct rows
and columns, giving the claimed square-root(M) norm ratio. This proves a
coefficient-completion obstruction even for f=g, but says nothing against
a separate estimate along that support curve. The checker compares direct
and completed signed sums, distinct-vector energy, and exact chirp support;
the implementation has the same conventions as the note.

## 3. Versions reviewed

SHA-256 hashes bind this review to the following content. The final two
coupled files specify the shared local normalization and arithmetic dependency.

| Path relative to package root | SHA-256 |
| --- | --- |
| `local_operator/TWO_CHANNEL_LOCAL_ADAPTER.md` | `2dd1894da2ec4e8d4bb89bcdf02998284559217cd65f8e01d1c5c8c035df21de` |
| `local_operator/check_local_operator.py` | `0e779c09e8a8970bd31a0f6c2d5a28c61f11b3c6d55e7393bb5a625ce2229736` |
| `local_operator/CHECKS.json` | `1554f59d6c12607f8b21c8bed9bcfbc92c7837b3808486646eb1a01ee6752b2a` |
| `transfer/WEIGHTED_ADAPTER.md` | `9c09ea8c786a3da2b9d4eb070b03e792c8b21696013d428eefec83c76cbd1a43` |
| `transfer/check_weighted_adapter.py` | `a27e2691601d76f83fdc3a09e98ca30d32bf5657718344853e59611820282748` |
| `transfer/CHECKS.json` | `3f7bd6bfcf23e6d746c6e84ec8ac2c3bc90df93212fe8479bfd55e9212b003af` |
| `coupled/verify.py` | `d53793f80b4495ccbb766a05751a524f59be2f1138ab737b340c4bb3e8040267` |
| `coupled/LOCAL_KERNEL.md` | `667d61c4994d69d0c3b6e0c39920813c160ba4e9d0dfcf0ca336cf28bc9f2a53` |

The review does not certify new global cancellation, loss-free transfer of
the native Möbius/prime weights, or a new zero-free boundary. Those are the
specific next mathematical obligations identified by the reviewed notes.
