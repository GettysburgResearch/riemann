# Review of the natural-length primitive projection

23 October 2026. Reviewer: type_i_gain. Reviewed final file:
`../two-hour-boundary-20261023/NATURAL_LABEL_PRIMITIVE_PROJECTION.md`,
SHA256 `623253614f939fd071a131499eed8fd401429dcc6e4f6ad6a8561b121e7ce0a1`.
The fixed-progression input is bound to
`50681c59e39a1e86bb63ab792cc252e39d35b11f17576d1df5475f69de874f43`.
The volume input is bound to
`5c94ecba69197b8f129d47b5891d7a2d0adcd1835dd39778b3f03ed68e03f5ed`.

I read the final assembly, its fixed-progression input and its inherited
selected-prime residue identity. No additional defect was found under
the stated analytic inputs and coefficient conventions. Some local
regroupings and the volume proof were co-derived with this reviewer;
this receipt independently checks the resulting assembly, not every
ingredient's authorship.

The new partial-pole interface is essential. The numerator expansion
classifies the shared subset only at the selected label primes. It
does not impose an exact gcd at the remaining label. After fixing d,k,
their exclusion from the remaining label is a subset of label rows;
the free original coefficient may still share unselected label primes.
At a selected squarefree label the two possible numerator digits are
1 and 2. The inherited local residue relation makes its selected term
minus q^(-1) times the original full residue, including the phase.
The analogous n-prime identity reconstructs the original numerator nR.
Thus N2 has the fixed progression and fixed punctures required by F3,
without the moving free-column/remaining-label mask of the old scalar
exact-gcd block. Multiplying by the common reciprocal-tail bound gives
N3 with exactly the powers (DK)^(1/12) P^(-1/2) d^(-1/2) k^(-1).

The fixed-progression translation is injective on sixth-free labels
because multiplication by fixed b translates each prime exponent
modulo six. This is used only for residues. The whole-b split and all
three resulting powers in N4 check; each is bounded by D^(5/6)K in
the claimed range. No continuous sixth-power periodicity is needed.

The q0^(1/12) in the improved plateau is load-bearing. Here is the
physical-support detail implicit in the imported convention: a column
with common multiplier q0 has inverse-row norm L>=q0. In a completed
block of scale C, the constant-weight b contribution is therefore
supported through b <= (C/q0)^(1/6). Before that sum, its q0 factor
is q0^(1/4); the support count changes it to q0^(1/12). The reflected
tail uses the same minimum row and kernel decay. This gives the stated
lambda*X^(5/12)*sqrt(B)*q0^(1/12) plateau, rather than discarding its
physical support. Substitution yields N5. The worst ordinary selected
outside-modulus amplitude is p^(-5/6); the inside-modulus amplitude is
at most p^(-1). Their squared weights converge. The original-only
w=e*d0 grouping retains a decaying dyadic w weight and finite k support.

I checked the small-U expansion term by term: its eight monomials and
the whole pole are bounded by D^(11/12)K^(1/12)+D^(5/6)K for
1<=U<=sqrt(DK), K<=D^(1/7). The explicitly retained negative-pole
subunit tail makes restoration of the label denominator legitimate.

The reviewed result is therefore the squarefree-label continuous bound

    U + D^(11/12)K^(1/12) + D^(5/6)K,

and, within the conditioned Gram range, the actual projection bound
with the additional whole-pole term U^(1/3)D^(2/3). At K=D/U and
U=D^h, the four exponents are h, 1-h/12, 11/6-h, and 2/3+h/3.
Each is strictly below 5/6+h/6 for 6/7<h<1. The example h=7/8
has maximum 23/24 versus the inherited resource 47/48. This is a
projection estimate only; the complementary inverse vector is not
controlled. No smaller B_flat or proof of RH follows from this review.
