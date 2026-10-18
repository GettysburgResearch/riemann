# Independent internal audit of the complete mixed-witness consumer

Reviewed source: `../eisenstein/MIXED_CONSUMER.md`, actual-byte SHA256
`6ba26a3b23ed38a4337b78d2a7eb92330ef668e3158c4f780c7adfd4e3302468`.
Reviewer: parallel theta track. This is scoped internal reconstruction,
not external review or a proof of the arithmetic mixed mean.

**Outcome:** no blocking error found in the stated conditional consumer
after its boundary-robustness hypothesis(2a) was added. The uniform
row-size mean remains OPEN. No unconditional zeta boundary is approved.

## Witness scope and the repair made during review

I checked the pinned original source's `prop:detector-witness` at t=3/2.
It gives r>=1-O(preliminary epsilon), m<=1/2+O(preliminary epsilon),
r<=3/2+O(1/log U), and r+m>=3/2-O(1/log U), with the same arithmetic
row character in the inverse and plain factors. These are not literally
restricted to the closed polygon displayed in(2).

The initial consumer stated only that limiting polygon. I requested
the robust eta-neighborhood input with a fixed O(eta) power cost, or an
explicit legal boundary reduction. The reviewed version adds(2a),
retains the original common smooth-profile and nonunit masks, and
chooses eta after the strict numerical margins. The extra U^(C eta)
is understood as the leading right-hand power cost in the mixed mean,
with the actual row scale U and lengths D,N unchanged. Markov then
gives the advertised count exponent with an additional O(eta), which
fits the reserved strict gaps. A theorem only on the closed polygon
would not activate this consumer without such a repair.

## Source-based low geometry

I reconstructed the source's reflected-energy proof around
`old-eq:5.3` and its tuple summation `old-eq:5.5`.
For M=1-ell, M'=M-2d and ell'=ell-d, its second energy branch has

    1+3ell'-2M'=5ell-1+d.

The first branch and the second are nonincreasing in the physical
row-shortfall parameter Delta_H, after retaining the actual row/kernel
scale and its tiny boundary allowance. This gives the stated energy
`M'+((5ell-1+d)/4)_+`. The powerful/principal row counts are already
inside that reflected-energy bound and are not counted again.

In the physical triangle, tuple count Z^d, coefficient Z^(-3d/2),
and X' square-root scaling Z^(-d/2) give exactly -d. The additional
square-root energy loss is `(5ell-1+d)_+/8`; monotonicity of the
positive-part function gives the aggregate bound(8), without needing
every individual tuple energy to meet the unmodified exponent.

At b=0, the fixed choice Y=q_(b_*)X makes P_a=Y'^2/Q exactly1 for all
rescaled tuples. This respects the original Gram hypothesis P_a>=1.
At ell=3/16, x=y=13/32 all rescaled X',Y' and row lengths remain in
strict positive ranges. The resulting low exponent is13/64 and the
principal Mellin exponent is C(s)=s-2/3.

## Complete high-frequency and amplitude accounting

From the robust mixed mean and the saturated product spike, the
limiting count exponent is `max(0,1-3delta/2)`. This uses the whole
witness polygon, not one corner. I reconstructed the central exponent
from the source's `bin-contour-accounting` formula and its physical
Mellin powers. It is affine in row-frequency d_row, so checking0 andh
is sufficient with no assumed slope sign.

At d_row=h, q<=delta/2 reduces it to(15).
`delta+max(0,1-3delta/2)` has maximum99/100 on the full nonfloor
interval[1/50,3/4]. At d_row=0, the correct ceiling is the imported
a<=7/8, rather than the contradiction boundary B. This gives(16).
The floor a=51/100 has no zero witness: using R=1 produces exactly
B_*-B and is the binding constraint. I checked these identities directly.

I also reconstructed the source-only small-row interface and the
principal local H factor in the old Eisenstein field. Its angular
factor is the actual old source's kappa=bar alpha^6, and its regular
local numerator has the advertised nonvanishing estimate for Re s>1/2.
The remaining angular L-function is in absolute nonzero convergence
for Re s>2/3. Thus the needed principal half-plane below7/8 does not
silently import a different field's finite phase convention.

The complete source framework, including its detector, reflected-energy
theorem, original high identity and continuation criterion, remains an
explicit import. This review did not re-prove those original theorems
or their entire recursive moment proof.

## Fresh exact checker replay

I read and replayed `mixed_consumer_check.py` under Python -O. Its
actual-byte source SHA256 was
`6d99e17fa6d2d968a1ce2283917bbb9f781de76c5bcd53550dabcd3ae144b952`.
The only replay adaptation redirected `__file__` to the theta
`adversarial/` directory so the output receipt stayed in the reviewer's
write scope; the compiled checker source and all arithmetic were
unchanged. No write occurred in the sibling track.

PASS: all20,301 aggregate tuple inequalities,151 full-polygon candidate
envelopes, and the exact rational final margins:

    nonfloor d=h:       -1883/80000;
    floor d=h:          -1/10000;
    d=0:                -38141/160000;
    small-row:          -6613/120000;
    prime-supply:        47/925;
    low/signal margin:   1/10000.

The fresh replay checks finite rational arithmetic. The analytic
piecewise-affine proofs, not the meshes, cover the continua. Its
104387/120000 boundary is conditional on the robust OPEN mean and all
named source interfaces. The limiting167/192 is a conditional
sufficient threshold, not a result established by the sprint.
