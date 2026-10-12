# A native sixteenth moment gives a count-free simple census through 5419

Status: proposed directed source packet; the frozen receipt and separate
reviews specify actual executions and acceptance.
Scope: actual Xi, 1561 refined intervals, 3122 actual Hardy-Z signs, a native
degree-sixteen jet, and a complete simple real census through height 5419.
The previous **count-free** complete simple census through 2240 is an explicit
dependency. No historical finite-count contract or published large zero
verification is used. This gives a finite companion column, not RH.
Exact sources: [THEOREM.md](THEOREM.md), the complete even product and
classical strip; [COUNT_FREE_CENSUS_RECOVERY.md](COUNT_FREE_CENSUS_RECOVERY.md)
and its receipt; the complete moment/one-occurrence selection argument in
[HIGHER_MOMENT_CENSUS_RECOVERY.md](HIGHER_MOMENT_CENSUS_RECOVERY.md); and
[CENSUS_FULL_COLUMN_SECTOR.md](CENSUS_FULL_COLUMN_SECTOR.md).
What was actually run: the exploratory precursor computed all new signs,
the native degree-sixteen jet and all 8049 interval inverse-sixteenth terms
at 320 bits. The named checker replays those primitives and exact guards.
Smallest remaining gap: independent frozen-source review and native replay.
Successful receipts and separate reviews identify the accepted runs.

## S16-1. Select source occurrences using the prior count-free census

Retain the 8049 original disjoint positive real sign intervals. The producer
uses indexed native zeros only to suggest 1561 dyadic refinements below
2048, each of width `2^-160`. The checker verifies strict nesting inside the
corresponding old interval and actual strict opposite Hardy-Z signs at all
3122 new endpoints. These prove existence independently of indexing.
The remaining 6488 original strict sign facts are imported from the frozen
native receipt. Its historical count and old uniqueness assertions are
surplus facts and are not used here.

Remove exactly one positive real Xi zero occurrence from every interval,
together with its negative reflection. Import the independently established
count-free **complete simple** census at `H0=2240`, at receipt SHA256
`ce21c175914c1e1d3ad049a8b67e6528ae2f72baed309b4719c1ca8de48a7832`.
That census proves every actual zero through 2240 is the unique simple real
zero in one of the 1739 original intervals below that boundary. Every new
interval is below 2048 and strictly nested inside its corresponding unique
old interval, so its authenticated zero is the same source zero. Other
intervals below 2240 are unchanged. Thus this selection removes every
occurrence through 2240; the **entire remaining source** satisfies
`abs(Re rho)>2240`. Above 2240 no initial uniqueness or completeness is
assumed. Extra integer multiplicities and unknown complex pairs remain.

## S16-2. Complete native moment and joint corner bound

Use the exact completed source

\[
 s=\tfrac12+iz,\qquad
 \Xi(z)=\frac{s(s-1)}2\exp(-s\log\pi/2)\Gamma(s/2)\zeta(s).
\tag{S16-1}
\]

Native `acb_series` at 320 bits, with truncation capacity 17, encloses this
formula through degree 16. The checker verifies `Xi(0)>99/200`, the nonzero
normalizing divisor, and source parity/reality enclosures. Retaining every
selected root's full interval gives a directed enclosure `[L8,U8]` of

\[
 T_8=-8[z^{16}]\log\frac{\Xi(z)}{\Xi(0)}
       -\sum_{j=1}^{8049}\gamma_j^{-16}
     =\sum_{\substack{\text{remaining}\operatorname{Re}\rho>0}}
           m_\rho\rho^{-16}.
\tag{S16-2}
\]

The equality uses the complete paired even order-one product, with no
unaccounted exponential factor. The complete moment converges absolutely.
Reality follows from complete conjugate grouping. Neither midpoint roots
nor a finite subset replaces any selected source term.

Here is the complete corner argument for this remaining source. Let
`R=2240`, `A=1/2`, and put `f(x,y)=Re((x+iy)^(-16))`. If `x>=R` and
`0<=y<=A`, write `theta=atan(y/x)`. Then

\[
 \partial_x f=-16|x+iy|^{-17}\cos(17\theta),\qquad
 \partial_y f=-16|x+iy|^{-17}\sin(17\theta).
\tag{S16-3}
\]

Since `17 atan(A/R)<17/4480<1<pi/2`, the first derivative is strictly
negative and the second is nonpositive. The function is even in y.
Every remaining root has a strictly positive real inverse-sixteenth
projection, since `16 abs(theta)<pi/2`. For `R<x<=H` and `abs(y)<=A`,

\[
 f(x,y)\ge f(H,A)=:
 d_8(H)=\frac{\sum_{j=0}^{8}(-1)^j{16\choose2j}
                        H^{16-2j}A^{2j}}{(H^2+A^2)^{16}}>0.
\tag{S16-4}
\]

If any remaining zero has `abs(Re rho)<=H`, its positive-half-plane
occurrence alone contributes at least `d8(H)`, with integer multiplicity
at least one. All other real projections are nonnegative. Therefore the
strict exact rational guard

\[
 U_8<d_8(5419)
\tag{S16-5}
\]

excludes every omitted zero or extra occurrence through 5419. No selected
interval intersects that boundary. The complete simple positive real root
count is consequently **4968**, derived from the selected list after the
exclusion proof. An extra occurrence at any selected low zero is excluded
by the same complete-source argument, so simplicity is part of the result.

The checker also records `U8>=d8(5420)`: 5420 fails this particular strict
upper-endpoint/corner predicate. Since `d8(H)` is strictly decreasing for
`H>=2240`, 5419 is its largest admitted integer height in this range.
Failure of the predicate is not a claim of an omitted root, a negative
moment, a mathematical barrier, or RH evidence.

## S16-3. Finite full-depth companion consequence

Compose the separately proved finite-census column theorem with this
complete simple census. For every integer `0<=r<=10835`, every real
`lambda>0`, `abs(T)<5419-(r+2)/2`, and every `y>=0`, define

\[
 E_r=\Xi^{(r)}-i\lambda\Xi^{(r+1)}.
\]

Then `E_r(T-iy)` and `E'_r(T-iy)` are nonzero and

\[
 \operatorname{Re}\frac{iE_r(T-iy)}{E'_r(T-iy)}>0.
\tag{S16-6}
\]

Derivative order and horizontal width remain finite; the vertical depth
and positive lambda are unrestricted. The analytic complete product,
classical strip, older primitive sign facts, and prior count-free 2240
census are explicit dependencies. Historical counts, published large
verification, and the separate global real-part-14 bootstrap are absent.

## S16-4. Frozen replay contract

The five owned files are this document, `produce_sixteenth_prefix.py`,
`sixteenth_prefix_candidates.json`, `check_sixteenth_moment_census.py`, and
`sixteenth_moment_census.json`. The checker verifies both imported packets'
direct source hashes, all original interval geometry, all new signs and
nesting, the native logarithmic jet, every full selected inverse-sixteenth
term, the exact lower-census identity and both fixed corner predicates.
The receipt names every import/replay boundary and hashes its displayed
direct source list and native binaries. It does not claim a finite checker
authenticates an infinite analytic source theorem or every transitive file.

```bash
source /workspace/.riemann-tools/activate.sh
python research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_sixteenth_moment_census.py --output /tmp/sixteenth-moment-replay.json
```

All failure branches remain active under optimized Python. The supported
output option preserves the official receipt. Primitive runs use the same
directed native arithmetic implementation; separate source formulations
and exact integer controls do not constitute a different arithmetic backend.
