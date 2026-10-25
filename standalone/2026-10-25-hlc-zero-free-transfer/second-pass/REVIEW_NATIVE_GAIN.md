# Independent review of the twisted Gauss decomposition and ordinary component

Reviewer: the `fractional_native` agent. I did not author the reviewed
identities, ordinary-component refinement, or checker. My investigation of
the separate capped native moment is not used as a premise for this review.

Reviewed local bytes:

- `NATIVE_GAIN.md`, SHA256
  `4127becd461de5a845174203d45ad2f9014cbe67709375db9b1b2046021ce453`;
- `check_native_gain.py`, SHA256
  `643a94ed247a791c9c50f8e6275563ba2b9a7df39f6e96b9f2248c2ff0b9ab26`.

Status: no defect found in the finite identities or the new analytic
deduction at the stated imported-source scope. This is an internal
mathematical review and finite replay, not external peer review, formal
verification, or certification of native Gauss values from first principles.

## Finite identities

The fourth-power twist agrees with the parent's cubic Gauss multiplicativity:
the two squared sextic symbols in the CRT factor multiply to the fourth
power because the reciprocity sign squares to one. This twist is symmetric
and satisfies the stated cocycle identity on coprime factors.

The convolution is associative on squarefree-supported functions, with
identity at the unit ideal. For `f=mu g`, the divisor cancellation gives
`g star f=delta_1`, including the zero extension off squarefree support.
The finite Heath--Brown identity follows by expanding
`g star (delta_1-f star g_y)^(star k)`. Its support is above `y^k`, so the
range restriction in (5) is correct and essential.

At `k=2`, the outer coefficient is the ordered truncated divisor count
`d_y(r)`, and the exact row character becomes `chi_c(u r^4)`. The central
normalizations in (8) multiply to `D^(-1/2)`. All gcd zeros and original
punctures survive in both the outer and inner factors. The common smooth
profile is retained at its shifted scale.

Applying the moving-twist theorem separately to fixed `r` and using
Minkowski gives the four terms of (9) exactly. The long outer-factor branch
`r` comparable to `D` is genuinely present; its deletion would not be a
valid improvement. The positive-majorant cost `(U/D)(D^2/U)=D` in the
native return is also correctly identified as a cost of that method,
rather than a lower bound for the signed expression.

## Cubic/sextic ordinary refinement

I checked the unique decomposition by exact prime valuations,
`k=r s^2 t`, with squarefree `r,s`, pairwise coprimality and cubefull `t`.
Fixing `s,t` leaves a sextic row; fixing `r,t` leaves a cubic row. In both
cases the natural conductor union is at most `R S Nrad(t) FQ`. Phase
cancellation never removes a natural zero.

The reflected common coefficient, nonprincipal restriction, and logarithmic
scale supremum have the same required scope as the parent moving-twist
proof. Both cubic and sextic arbitrary-coefficient bounds are explicit
source premises. Their full-column extensions use the same powerful-column
argument, not a new unproved structured coefficient theorem.

The two slice bounds (13)--(14) were recomputed. Choosing the sextic slice
when `R>=S` and the cubic slice when `R<=S` gives
`Z+Z^(2/3)C^(1/2)+Z C^(1/3)`, where `Z=RS^2`. The cubefull count follows
from the representation `t=a^3 b^4 c^5`, allowing harmless extra overlaps
for an upper bound. Together with `Nrad(t)<=L^(1/3)`, it gives the exact
dyadic exponents `L^(-2/3)`, `L^(-1/6)` and `L^(-5/9)` in (16). All are
summable. The fixed omitted-prime parts and common extra punctures retain
their convergent or subpower costs.

The refined small-`f` term and its subsequent limitation are both correct:
insertion in the full ledger gives `F^(-5/6)M^(-1/3)L^(-1)`. Retaining the
small-width frequency tail and splitting at `F=sqrt(K_0)` costs
`K_0^(1/12)` on each side. Consequently the sharper ordinary component
does not automatically improve the complete parent exponent.

## Independent finite replay and its limits

I ran `python -I check_native_gain.py`. It completed successfully with:

- 3,000 exact twisted-inverse coefficients;
- 289 coefficients for `k=2,y=17` and 343 for `k=3,y=7`;
- 72 complete finite row-transport cases;
- 70 detected substitutions of a third-power row twist for the correct
  fourth power;
- 43 detected substitutions of ordinary multiplication for the cocycle.

I also inspected the checker. Its arithmetic in `Q(zeta_6)` is exact,
and its synthetic symmetric bilinear symbol deliberately realizes the
cocycle and natural-zero identities. The finite test therefore checks the
algebra it claims to check. It does **not** independently derive the actual
Eisenstein cubic Gauss cocycle; that arithmetic remains an imported premise.
No asymptotic cancellation is tested by these finite identities.

The smallest gap to a new zero-free conclusion remains a bound for the
coherently assembled outer factors and signed Fourier kernel. The review
does not convert the separate component estimates into that bound.

## Remote mathematical-commit authentication

I fetched both reviewed files directly from
`GettysburgResearch/riemann@3b47783a7c775bc8133f6601cb9bb97b1b38678a`, under
`standalone/2026-10-25-hlc-zero-free-transfer/second-pass/`.
Their contents are byte-identical to the locally reviewed files. I independently
recomputed their SHA256 hashes and their Git blob identifiers from
`SHA1("blob " + decimal_byte_length + NUL + file_bytes)`:

| File | UTF-8 bytes | Git blob |
| --- | ---: | --- |
| `NATIVE_GAIN.md` | 15,205 | `55e01b86b3ac198951789e5ef03babcff5fd17b7` |
| `check_native_gain.py` | 6,651 | `f0e25e780e49373bc844236c0da78e8387b125f4` |

The SHA256 values equal the two values at the start of this report, and
the recomputed Git blob identifiers equal those returned by GitHub for
the exact commit. This authenticates the reviewed mathematical object and
checker; it does not add an asymptotic claim to their finite validation.

I then fetched both files again at the final corrected mathematical freeze
`5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`. Both contents and Git blob
identifiers are unchanged from the authenticated values above. Thus the
same exact-byte review and finite replay bind to the final freeze as well.
