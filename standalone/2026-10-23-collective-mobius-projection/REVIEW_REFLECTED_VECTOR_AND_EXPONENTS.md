# Review of the reflected completion scope and structural bookkeeping

23 October 2026. Reviewed frozen files:

- `../two-hour-boundary-20261023/REFLECTED_VECTOR_COMPLETION_SCOPE.md`,
  SHA256 `39850353a97e596a8e0ebabfecaf41b954cceed2026612a91ae0716eb62cb040`.
- `../two-hour-root-20261023/verify_structural_exponents.py`,
  SHA256 `c251b32fd7ad9104f3e301a8d35c6782277e6fb59d4fed958816759f9f197325`.

No reviewed source was changed. I independently derived the reflection
orientation and the completion plateau before reading the final scope
note. The prior V4/sixth-free vector estimate and the primitive-label
continuation theorem are explicit dependencies, not reproved here.

## Analytic scope review

I read the exact PR1015 source at commit
`e87c5f669f81fe6371af926917d1c5b21023bce8`,
`standalone/2026-10-22-residue-remainder-followup/COMPLETED_FE_KERNEL.md`.
Its equation (9) preserves the numerator nR and Gauss orientation.
The finite matrix is resolved by a fixed local-class partition. Its
kernel argument contains the common norm coordinates n/D, R/K and
c/L; their Mellin separation preserves the original Mobius coefficient.
Thus the finite vector estimate is applicable after reflection.

The three regimes in R1 follow by separating L at K and K squared.
In the intermediate range the weighted nonvolume term decreases as
L^(-1/2), making L near K the peak. This proves the additional
K^(3/2) C^(-1/3) term with the displayed D factor. The small losses
in the kernel exponent are absorbed by choosing internal epsilons.

The exact reflected completion includes all integral ideals b with
weight 1/Nb, not merely bad-prime ideals. The effective scale is
C/(Nb)^6. On the peak range its square-root bound times 1/Nb is
constant in Nb. Ideal counting therefore gives precisely the plateau
D^(5/6)K^(7/6). The other ranges have convergent power sums, except
for the harmless intermediate volume logarithm. This verifies R2.
When C is below one, use the large-argument kernel estimate on every
actual modulus dyad; no nonexistent fractional row ball is introduced.

The concluding warning is correct. Regularity of the completed vector
at the central point forces the raw series to vanish there after
continuation. It does not authorize subtracting a constant from finite
modulus blocks and discarding the complementary tail. R2 is an upper
bound for the stated method; the plateau is not asserted to be a lower
bound for the actual arithmetic vector.

## Exact finite replay

I read the checker and independently ran an unchanged copy normally
and with Python `-O` in `structural-replay/`. Both generated exactly
the same certificate bytes, SHA256
`22f638fcaccd8fc97dc9fd05adabe93bf08860e926b273288b3918fb6ac31ae0`.
Acceptance uses explicit arithmetic checks and remains active under
optimization. All scalar arithmetic uses `fractions.Fraction`.

I checked the origin of the local exponents against the sixth-free
branch table: both exceptional Ramanujan valuations and the valuation
seven branch are included. The Rankin comparisons have the correct
label-norm powers. The optimized residue-reference comparisons are
affine in the logarithmic label exponent, so the two endpoint checks
cover the stated interval. The chosen projection example gives terms
199/224, 365/384 and 20/21, against 41/42, with saving exactly 1/42.
The quartic cutoff calculation is 11/75 and is smaller than 4/27.

The deliberately false projection target is rejected by an explicit
predicate. These are finite local and exponent checks only. They do
not prove the imported analytic inequalities, the full complementary
operator bound, a new fixed zero-free half-plane, or RH.

Verdict: no defect found in either reviewed object within this scope.
