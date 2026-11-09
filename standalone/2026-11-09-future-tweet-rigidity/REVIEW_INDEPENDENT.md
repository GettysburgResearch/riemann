# Independent review of the local adapter and coupled kernel

9 November 2026. Reviewer: `/root/future_routes`.

**Decision: the reviewed finite mathematics and source-matching statements pass
within their explicit scope.** No full native inverse estimate, zero-free
improvement, external peer review, or formal verification is certified.

## Authorship and independence

The reviewer authored `inverse/README.md`, `inverse/native_projection.py`, and
their associated artifacts. Those files are **excluded from this independent
review**. Any checks the reviewer performed on them are author self-checks.
The root agent separately reviewed their mathematical statements.

The reviewer did not author the two-channel proofs/checker or the coupled
kernel proofs/checker reviewed here. The agents share a project and exchange
messages; this is an internal author-excluded review, not external peer review.

## Exact reviewed file identities

All paths are relative to this standalone package. SHA-256:

| File | SHA-256 |
|---|---|
| `local_operator/TWO_CHANNEL_LOCAL_ADAPTER.md` | `2dd1894da2ec4e8d4bb89bcdf02998284559217cd65f8e01d1c5c8c035df21de` |
| `local_operator/SCALAR_FILTER_BUDGET.md` | `b8f95808b709160e99d9579b37216a0c962d471503564396504b2c52d50f68dc` |
| `local_operator/check_local_operator.py` | `0e779c09e8a8970bd31a0f6c2d5a28c61f11b3c6d55e7393bb5a625ce2229736` |
| `coupled/LOCAL_KERNEL.md` | `667d61c4994d69d0c3b6e0c39920813c160ba4e9d0dfcf0ca336cf28bc9f2a53` |
| `coupled/verify.py` | `d53793f80b4495ccbb766a05751a524f59be2f1138ab737b340c4bb3e8040267` |
| `transfer/WEIGHTED_ADAPTER.md` | `9c09ea8c786a3da2b9d4eb070b03e792c8b21696013d428eefec83c76cbd1a43` |

These hashes bind the mathematical/code snapshots, rather than a mutable
branch head. Later edits require checking the relevant changed claims.

## 1. Local operator review

Independently checked:

- The product-kernel convention sends a multiplicative character `psi` to its
  conjugate. Its exceptional input mode is `chi`, as the stated Gram formula
  requires; changing to a ratio kernel would change the orientation.
- The zero-extended character sum at zero frequency is -1, and the sum on
  nonzero frequencies is 1. Hence the constant singular value of `B_chi` is
  exactly `1/q`, and centering subtracts exactly `P/q`.
- The Gauss–Jacobi computation gives squared singular values `q^-2`, `q^-1`,
  and 1 in the stated three cases. The one-channel computation itself remains
  valid for a quadratic nontrivial character; nonreality is needed for the
  conjugate-pair repair, not for that computation.
- The two distinct exceptional character projectors are orthogonal. Averaging
  the two centered Grams gives the sharp lower gain `(1+1/q)/2`. The proposed
  decoder has the displayed inverse eigenvalue and norm.
- The distinct-character corollary therefore also permits a quadratic channel
  paired with a genuinely distinct character. Both outputs must be bounded;
  this does not replace an uncontrolled native coefficient.

For tensor products, the `2^r` bank sees only the tensor of local mean-zero
spaces. Adding all local constant outputs gives `3^r` channels and full
reconstruction. Removing just the single all-constant output removes exactly
the globally constant vector, not all mixed sectors. Adding the zero-coordinate
projectors gives the stated full-field `4^r` construction. The sector gains,
channel weights, and decoder identities are consistent.

The conductor assertion is correctly restricted to finite local multiplicative
characters and their original unit masks. In sector S the nontrivial local
character basis has conductor supported on S; the complementary primes remain
as redundant zero masks. Their product divides the original squarefree ideal.
This does not compute a global automorphic conductor. The subpower count proof
is valid for distinct prime ideals of a fixed number field. It does not apply
to arbitrarily many abstract copies of one small finite field. The separate
warning about growing trace-function complexity and composite-modulus analytic
estimates is necessary and present.

## 2. Coupled kernel and source match

The reviewer directly fetched the immutable source

`GettysburgResearch/riemann`, commit
`8b2c6d50ad2d729c681745717c615095bd8f1d9d`,
`standalone/2026-10-25-hlc-zero-free-transfer/fourth-pass/OFF_DIAGONAL_TRANSFER.md`,
Git blob `3ead6e25fdb589ae49b65cc98e8f3eb09d77be25`.

Its equations (15)–(18) give the asserted affine relation and character phase.
The four Möbius factors, prime restriction, `(d,p)=1`, smooth weights, affine
outer parameters, and the original aggregate normalization must remain in the
joint coefficient. The coupled note retains these obligations and does not
identify the collected coefficient `lambda` with Möbius.

The finite proofs checked directly are:

- `T(h,t)=S(ht)` for nonzero h, with the separate h=0 and t=0 axes and the
  reducible principal-character case;
- the complete hypergeometric double-sum identity, including the denominator
  character orientation and the unit-modulus normalization;
- the exact dilation Gram identity, particularly the removed y=0 term in its
  Möbius substitution, which produces the exceptional character term;
- the complete local singular spectrum and the distinction between sheaf rank
  two and finite matrix rank q-1;
- Fourier completion for arbitrary signed joint W, with its exact q factors.

At a local prime dividing an affine coefficient, the original phase vanishes;
division is not performed there. Local h=0 can occur for a nonzero global
shift, and it is not discarded as if it were only the global pair diagonal.
These distinctions are correctly retained.

The sheaf local data, infinite gallant monodromy, FKMS analytic estimate, and
the appended difference-of-ratios theorem are attributed external inputs.
This review does not independently reprove their geometry or duplicate the
other reviewer's full external-source audit. The finite adapter does not
establish their hypotheses for a composite/inert/global arithmetic block.
The text explicitly preserves that limitation.

## 3. Scalar budget and weighted bridge

The scalar note's finite local-valuation classification follows from the
finite support of the local Möbius tensor. Its pole statement has the required
nonvanishing local denominator in the right half-plane and an explicit
continuation hypothesis. The dual affine function proves the sharp total
variation lower bound also for complex coefficients. The product equality is
properly limited to collision-free support; equal-norm ideal shifts are not
silently treated as distinct scalar scales.

The weighted bridge was also read. Its axis-separated Fourier identity,
Moyal identity for factored blocks, projective/nuclear-norm extension, and
chirp counterexample have consistent conjugations and normalizations. The
chirp rectangle lies in the displayed interval regime when its side length
is a suitable fixed fraction of q. The example excludes a generic cheap
separation inference; it is neither a native Möbius counterexample nor a
counterexample to direct cancellation on a curve. The bridge explicitly
does not claim that a general native joint weight is one factored block.

## 4. Independent finite replays

The reviewer inspected the finite-field and cyclotomic arithmetic and ran
the frozen coupled checker independently in isolated Python:

```bash
python -I -S -B coupled/verify.py --output /tmp/review_coupled_checks.json
python -I -S -B local_operator/check_local_operator.py --output /tmp/review_local_operator_checks_final.json
```

Results: **9,816 coupled predicates PASS** and **8,205 local/operator/scalar
predicates PASS**. The final local run records the exact checker hash above
and the same imported coupled-arithmetic hash. The coupled run records its
own exact source hash above. The fields, negative controls and count scope are
described in the corresponding checked-in reports.

Both checkers share the sibling cyclotomic arithmetic implementation, so these
are not independent software implementations. The local checker independently
constructs its kernels and exact Gram entries using that common arithmetic.
The review of the general finite proofs is separate from these small-field
replays. Passing them does not certify monodromy, an infinite operator bound,
or the remaining source-specific estimate.

## Remaining mathematical boundary

The completed native joint coefficient must still receive a genuine estimate
that survives all outer sums, axes, masks, and source normalization. The
two-channel frame gives stable reconstruction; it gives no upper bound on
those particular transformed outputs. The nuclear-norm criterion is a useful
sufficient condition, not a verified property of the native source. Nothing
in this review changes that boundary.
