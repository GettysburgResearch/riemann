# Independent full signed compact-witness review

2026-10-10 continuation; reviewer `/root/review_setup/kappa_proof_audit`.
Owner files preserved; independent outputs written only under `/tmp`.

Verdict: **scoped PASS** for C1–C3 and the finite full critical R2 sign.
The same sign persists for the paid genuine Schwartz replacement. No
asymptotic signed-remainder estimate or zero-free improvement follows.

Frozen proof `FULL_SIGNED_COMPACT_WITNESS.md` SHA256
`1c0a1718080e6f763a3531f9f9a8f8fcd31868c48d241290406fe4cef61644ca`;
checker `check_full_signed_compact.py` SHA256
`ace0ec9a10deef974d3cae842590bc46c2d048e65dfa5b14b659cbc7c380dc50`.
The frozen Fourier helper has SHA256
`dddf8f7c12fe022e54e19d9994da6092fd7a3a7e9da1d1d67b6daf6f5c27c598`.

The specially chosen fixed smooth W is legitimate for this finite D=30:
disjoint small bumps at the four specified norm samples can be one there
and zero at every other integer-norm sample. This defines the eight actual
prime columns of the full source family at that scale. It is not an
asymptotic prime-only substitution for the source W.

The exact critical predicate uses actual multiplicities, not merely the
residual exponents. Grouping occurs after classification. The primitive
part has every nonprincipal local character, and the separate principal
mask has every occurring zero-residual prime. They are coprime. A critical
four-slot tuple has at most one principal-mask prime: two balanced
two-occurrence primes would use all four slots and leave no singleton.
The full primitive part cannot be principal because the sector has a
singleton prime.

For every mask divisor d, the substitution u=dv gives the exact factor
`mu(d) chi(d)/Nd` and the dual norm argument `H Nh/(Nd Nq)`.
The radial profile removes the generator rotation from the Fourier
argument, while its phase `chi(d)` remains. The primitive zero-frequency
term is zero. All local exponents 1–5 are evaluated with the literal
source additive character, and their CRT factors retain the exponent e.

The checker correctly enumerates all 4,096 ordered tuples, their 120
product-column diagonals, the 3,696 critical tuples, and all 1,092 critical
character/mask groups. Its exact radial charge projector retains 178
groups with total multiplicity 568 and kills 914. The generic grouped
sharp-ball control independently reconstructs the old values R2=1176
and leading=456. The dual norm box is complete, its cutoff is exact, all
mask divisors are summed, and nonunit zeros are retained in the primitive
dual character.

The two independent replays passed and are byte-identical, SHA256
`46e642fa1c4774f1d31166de547731762fa7f89ac3f0a3ce6b0c500f91571d93`:

* `/tmp/review-full-signed-compact-normal.json`
* `/tmp/review-full-signed-compact-optimized.json`

The directed full value is
`[8852.5068916015827910965314252477411701769971627151 +/- 1.51e-47]`.
The leading subface is
`[3916.7665189976260644009926745000130837431873375545 +/- 2.52e-47]`;
the other critical faces contribute
`[4935.7403726039567266955387507477280864338098251606 +/- 4.02e-47]`.
Deleting principal masks changes the full value to
`[9251.8567576912013130298491628310946723335907643494 +/- 8.36e-48]`.

The whole critical-sector Schwartz replacement is also paid. The combined
mask/conductor norm is at most `(31*19)^2=346921`. Every support denominator
is odd, so the same strict rational gap survives the radius-1e-12 Fourier
mollification. A complete norm box has at most 34693 points. With at most
two divisors per tuple and primitive norm at least seven, the displayed
whole-sector error is directly bounded by
`[0.34894525337247821930000574638437168638594954862192 +/- 3.78e-51]`.
This is below .35, far below the full sign margin. This error bound is an
analytic/independent directed control; the frozen owner replay primarily
authenticates the finite bandlimited sum.

A separate source-normalized principal-mask Poisson oracle was written as
`/tmp/review_masked_poisson_oracle.py`, SHA256
`c2512b833c9232c2668797346db195b49efec4c78a212347d7987e5769730180`.
It reconstructs the two prime fields over seven by discrete logs and uses
the actual prime over thirteen with primary generator 4+3omega as the
principal mask. This is an actual critical configuration: the singleton
norm is 49>H=40. Its primitive generator is seven, primitive norm 49,
local powers are 1 and 5, and its source `chi(d)` equals -1.

For the self-dual Gaussian `exp(-pi*(2/sqrt(3))*Nu/H)`, it compares a direct
primal masked sum with the complete principal-mask Poisson expression.
Both lattice sides are enumerated through norm 1024 (3,696 nonzero rows),
and the whole omitted lattice is bounded by the geometric derivative
using `c_n<=16n`. The absolute difference is below `5.458e-40`, and the
paid combined tail is below `8.137e-36`. Omitting `chi(d)` changes the
answer by more than 3.81, and omitting the `1/Nd` amplitude changes it by
more than 22.90. Thus the phase, norm denominator, and dual dilation are
independently exercised rather than only read from the owner code.

Oracle normal and optimized outputs are byte-identical, SHA256
`aa3fe719858af1ea8fb06ad49fdc8460aaadcf3b3afc82dc3c3fc6c3b0d30cd1`:

* `/tmp/review-masked-poisson-oracle-normal.json`
* `/tmp/review-masked-poisson-oracle-optimized.json`

This oracle authenticates one actual masked Poisson interface with rigorous
tails. The complete compact-window R2 is authenticated by the full code
audit and the two-mode replay; it is not independently recomputed by the
Gaussian oracle. All conclusions concern this fixed finite experiment.
