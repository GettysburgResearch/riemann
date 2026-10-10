# Exact-commit receipt for the independent Möbius overlap review

**Reviewer:** theta_closure, a nonauthor of the overlap proof.

**Status:** the existing scoped mathematical PASS is carried onto the exact published source commit below. The published proof is byte-for-byte identical to the proof previously reviewed. No mathematical premise or covered sector is strengthened by this receipt.

## 1. Published source and prior full review

Repository: GettysburgResearch/riemann.

Draft publication: [PR #926](https://github.com/GettysburgResearch/riemann/pull/926).

Exact source commit:
[a0a31c4f9775c5516a78d5c9eb69088b9c83595a](https://github.com/GettysburgResearch/riemann/commit/a0a31c4f9775c5516a78d5c9eb69088b9c83595a).

Publication tree identifier supplied with this release:
5082fe79296a9d701bef4e8e88691b80e818cb33.
The independent checks recorded here authenticate the commit-specific file contents; the complete tree was not reconstructed.

The exact repository directory is:

    standalone/2026-10-10-mobius-overlaps-and-sampled-moments/

The reviewed source is [MOBIUS_OVERLAP_TAILS.md at the exact commit](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/MOBIUS_OVERLAP_TAILS.md).

The preceding complete nonauthor review is [reviews/overlap_review.md at the same commit](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/overlap_review.md).
Its SHA256 is
b4578527422bfeca44d1f2ff2aa5accaa9a144f82632d0b60defcb550ea1cc80.
It is itself byte-for-byte identical to the previously written review of the frozen local overlap note.

## 2. Independently recomputed file identities

All paths in this table are relative to the exact repository directory above. Each file was fetched through the GitHub connector with the full source commit specified. The SHA256 and Git blob ID were recomputed from the fetched UTF-8 bytes, preserving all bytes and the final newline. Every recomputed Git blob matched the connector's returned blob ID.

| Exact relative path | Bytes | SHA256 | Git blob ID |
|---|---:|---|---|
| MOBIUS_OVERLAP_TAILS.md | 43009 | 980c0e5d4e82e4c6105a21db37aeeb84ff19da9c985be571002fe4f3e9bfba04 | 15d6694e748b6e6bca3a7dad1e37045f98cbcde8 |
| checks/check_mobius_overlaps.py | 18756 | 3baada57f5ae301e8d4d374e086fd85b03c03b99f85c01ac7c5d5c8205b8c838 | b3911f4b6dc3055a8f34c8cb89c1b0e7be18de55 |
| results/mobius_overlaps.json | 9002 | 65457f1cf57581604cc8bda4ac93e8792e7fcd9f664cf3c2b684d3322758f013 | 2fc871b6806d3134ba0309d88caad677f38401c3 |
| reviews/overlap_review.md | 12084 | b4578527422bfeca44d1f2ff2aa5accaa9a144f82632d0b60defcb550ea1cc80 | 3281fb37e0f04c7f241182ea6f3e001563277606 |

The source commit identity was also checked through the GitHub commit endpoint. The file blob calculation used the standard Git object bytes: the ASCII prefix consisting of the word blob, a space, the decimal byte length, and one zero byte, followed by the exact file bytes.

The proof was compared directly with the previously reviewed local note, whose frozen SHA256 was

    980c0e5d4e82e4c6105a21db37aeeb84ff19da9c985be571002fe4f3e9bfba04.

Both its hash and its complete bytes agree. The published full-review bytes also agree with the preceding review. Thus this receipt does not rely on a filename match or an unauthenticated status field in a derived JSON result.

## 3. Mathematical verdict carried to this commit

I carry the preceding review's PASS for the native component deductions in Sections 3--7 of MOBIUS_OVERLAP_TAILS.md onto commit a0a31c4f9775c5516a78d5c9eb69088b9c83595a.

The proof scope is exactly that of the preceding full review:

- The exact designated-incidence local correction, including its ordinary-subset-gcd variant, character zeros, and weighted absolute-convergence conditions.
- The sharp common-factor tail obtained by leaving the sharp common-factor dyad inside the classical sieve while Mellin-separating the original smooth residual tests.
- The mixed positive/inverse correction at critical finite-horizon weights, retaining all frozen-mask and pairwise-disjointness conditions.
- The entire physical cubic-product estimate, including every shared-prime incidence in the independent products.
- The grouped double-triangle signed-sector estimate, its cutoff \(r=19/55\) at \(h=21/20\) under the stated \(b=7/8\) premise, and its specified embedding into every higher fixed moment.

The full review reconstructed the formulas, normalizers and numerical fractions. This receipt adds a binding to their exact published source bytes.

## 4. Preserved premises and sector limitations

The classical squarefree and all-row character-sieve interfaces remain identified external inputs. This receipt does not independently reprove their source theorems.

At \(b<1\), the inverse pointwise estimate PW_b^sm remains an explicit analytic premise, uniform in the required physical row range, smaller scales, exclusions and fixed finite test seminorms. A bound with uncontrolled conductor constants or only a scale-linked row range does not replace it.

The sharper quadratic common-factor use additionally retains the reciprocal premise R_b, or the alternative uniform interval-test hypothesis stated in the proof. A smooth pointwise estimate alone is not promoted to the sharp common-factor test. The optional NM2 input remains confined to the selected bounds and comparisons that expressly invoke it; the two new numerical main examples do not acquire an unstated NM2 premise.

The numerical use of \(b=7/8\) does not constitute independent validation of the imported 7/8 zero-free assertion. The grouped estimate bounds the complete specified signed Hermitian sector, including its literal masks. It is not a bound for every individual tuple after absolute values, for every low-gcd sector, or for the full \(2k\)-th moment. The fully singleton sextic core and its signed long-conductor average remain outside the proved improvement.

No full generalized moment hierarchy, new zero-free half-plane, or RH result is certified by this receipt.

## 5. Checker scope and blocker status

The [published overlap checker](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/checks/check_mobius_overlaps.py) and [published result JSON](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/results/mobius_overlaps.json) were fetched and identified by their exact bytes.

I did not execute or independently audit that checker for this receipt. Its result JSON is not treated as an independent replay or as analytic verification. The prior full review likewise did not claim a moment-checker replay. My separately recorded theta diagnostic concerns a different theorem and does not change that boundary.

**Blocker status:** no file-identity mismatch or change to the reviewed overlap proof was found. The existing scoped mathematical PASS applies to the published proof at the exact commit above. It is not blanket approval of every claim or checker in the surrounding packet.
