# Independent proof review: finite moment ladders and bootstrap limits

**Verdict:** PASS for the stated norm inequalities, synthetic countermodels, and conditional arithmetic consequences. No mathematical correction identified. This review does not validate the imported zero-free exponent or prove a new arithmetic moment estimate.

**File reviewed in full:** `analysis_bootstrap_limits.md`.

**Verified SHA256:** `34af6338d177dbc3295ca96c66109aa8b5f3e768cab181b7ef2a9ae0b60ecff2`.

**Review method:** direct algebraic and logical proof inspection. No numerical testing was needed or performed.

## Checks

1. **Finite-order interpolation.** Bounding the additional `2k-2K` powers by the supremum gives exactly `HD^{K+2(k-K)B+epsilon}`. Input losses can be chosen smaller for each fixed `k`; the endpoint `k=K` is correctly treated separately. The excess identity `(2B-1)(k-K)` and the extraction identity `alpha_k=B+(K/k)(B_K-B)` are correct. Since `0<K/k<=1`, the extracted exponent is a convex combination and cannot improve the better endpoint.

2. **Actual integer row sets.** The condition `E=h-K(2B-1)>0` implies `0<E<h`. For every real `D>=2`, the proposed support count `floor(D^E)` is therefore a positive integer no larger than `floor(D^h)`. Once `D>=2^{1/E}`, its lower bound by `D^E/2` is valid. There is no use of a fractional or eventually empty row count.

3. **Entire finite ladder.** The moment exponent for `j<=K` is exactly `h+j+(K-j)(1-2B)`, so all the asserted smaller moments meet their diagonal upper bounds. For `k>=K`, the same array attains the stated interpolated exponent up to a fixed factor. The explicit condition in the general construction is preserved; it is not silently claimed for parameters making `E<=0`.

4. **Replica capacity.** The equivalence `B<=B_K` if and only if `E>=h/6` is exact. At equality of exponents, the logarithmic denominator still makes the support larger than any fixed multiple of the prime-replica count for sufficiently large `D`. Relabeling permits any prescribed set of that size to receive the large entries. The note explicitly does not claim that these arrays satisfy the arithmetic prime-removal identities.

5. **Endpoint and stronger-cap models.** In the stated range `h<=11/10`, one has `1/2<B_K<1`. Taking `B=min(B_cap,B_K)` preserves `E>=h/6>0` and every finite moment bound, while respecting the additional cap. With `B_cap=7/8`, the separate claims for `K=1` and `K>=2` are correct. The positive limiting slope in the synthetic excess is maintained.

6. **Conditional imported-bound example.** The pointwise input requires uniform reciprocal control, polynomial conductor growth, and deleted-factor control for all rows `Nu<=D^h`, as the note expressly states. Under those hypotheses, `M_4<<HD^{11/4+epsilon}` and `e_k=3(k-1)/4` follow. The extracted boundary is exactly `7/8+(1/24+5theta/12)/k`, hence is weaker than the assumed `7/8`. The conditional wording is accurate.

7. **Tail criterion.** Markov's exponent is correct. A strict power improvement to `o(D^{h/6}/log D)` requires `alpha>B_K` when using that displayed moment bound alone. The equality case is not improperly promoted to a tail theorem. For `alpha<B_K`, the endpoint array gives the claimed violation; when a stronger cap is imposed, the threshold is correctly changed to `min(B_cap,B_K)`.

8. **Varying fixed row exponents.** The replication argument is valid for every fixed positive `h_k`; when its prime norm exceeds the supported column norms, the deleted-multiple terms vanish. Thus no hidden `h_k<6` restriction is needed here. With nonnegative excesses, the displayed gap tends to zero exactly when both `h_k/k` and `e_k/k` tend to zero. The conclusion about long-row theorems with `h_k` proportional to `k` follows.

## Scope conclusion

The note rigorously rules out specified deductions from finite norm data and pointwise caps. Its synthetic arrays are explicitly distinguished from the arithmetic family. It leaves room for a short-row theorem, a stronger tail estimate, or an amplification using additional arithmetic correlations. That boundary is maintained throughout.
