# A native tenth moment enlarges the count-free simple census

Status: proposed directed source packet; exact receipt and separate reviews
record execution and acceptance scope.
Scope: actual Xi, 668 refined low-zero intervals, a native degree-ten jet,
and count-free complete simple census recovery at heights 4064 and 4072.
The previously proved count-free census at 2240 is an explicit dependency.
No historical finite zero-count contract or published large verification
is used by this theorem.
Exact dependencies: [THEOREM.md](THEOREM.md),
[COUNT_FREE_CENSUS_RECOVERY.md](COUNT_FREE_CENSUS_RECOVERY.md), the complete
moment extraction and selection argument in
[HIGHER_MOMENT_CENSUS_RECOVERY.md](HIGHER_MOMENT_CENSUS_RECOVERY.md), and
[CENSUS_FULL_COLUMN_SECTOR.md](CENSUS_FULL_COLUMN_SECTOR.md).
What was actually run: the exploratory precursor replayed all 1336 new
actual Hardy-Z signs, computed the native degree-ten logarithmic jet and
full finite inverse-tenth sum at 256 bits. The named checker replays these
primitives and exact whole-source guards. Successful receipts, rather than
the exploratory precursor alone, identify accepted runs.
Smallest remaining gap: independent frozen-source review and native replay.
No unbounded real-zero or RH conclusion follows.

## 1. Refined source existence and explicit prior census import

The original 8049 disjoint positive real sign intervals are retained.
`produce_tenth_prefix.py` suggests candidate refinements for the 668 original
intervals wholly below 1024, each with width `2^-112`.
`check_tenth_moment_census.py` verifies strict nesting and all 1336 actual
Hardy-Z endpoint signs. These establish a real Xi zero in each new interval;
candidate indices alone establish neither existence nor completeness.
For the other 7381 original intervals, only their previously authenticated
primitive sign facts are imported from the frozen native packet. Its
historical complete-count and full-census assertions are not used here.

Select exactly one positive real zero occurrence from each interval and
remove its reflected negative occurrence too. The previously proved
**count-free** complete simple census through `H0=2240` is imported at exact
receipt SHA `ce21c175914c1e1d3ad049a8b67e6528ae2f72baed309b4719c1ca8de48a7832`.
It identifies every zero below that height with its unique original
interval. All 668 refined intervals lie strictly inside those original
intervals and below 1024, so each selects the same unique actual zero.
The remaining intervals below 2240 are unchanged. Consequently the new
selection removes **every occurrence** below 2240. Any extra multiplicity
or omitted zero in the remaining source has `|Re rho|>2240`.
Initial full completeness or uniqueness of the 8049 intervals is not
assumed; the lower count-free completeness just proved is used explicitly.

## 2. Exact native moment and complete remaining-source projection

The exact source formula (RP2), evaluated by native `acb_series` through
degree ten at 256 bits, gives a logarithmic jet normalized by `Xi(0)`.
The checker verifies the strict constant seed and parity/reality enclosures,
then encloses every selected inverse tenth power over its full interval:

\[
 T_5=-5[z^{10}]\log\frac{\Xi(z)}{\Xi(0)}
       -\sum_{j=1}^{8049}\gamma_j^{-10}.
\tag{TN1}
\]

The complete product identifies (TN1) with the entire remaining paired
inverse-tenth source moment. Nonreal conjugates and all unselected integer
multiplicities remain present. With `A=1/2` and `R0=2240`,

\[
 c_5=\frac{\sum_{j=0}^{5}(-1)^j{10\choose2j}
                 R_0^{10-2j}A^{2j}}{(R_0^2+A^2)^5}>0,\qquad
 T_5\ge c_5\sum_{\text{remaining}\operatorname{Re}\rho>0}
                  m_\rho|\rho|^{-10}\ge0.
\tag{TN2}
\]

The acute-angle hypothesis holds because
`10 atan((1/2)/2240)<5/2240<pi/2`. This projection uses the **remaining**
source support after the explicit lower census import; it does not claim
that every actual Xi zero lies beyond 2240. No unknown complex pair can
cancel another positive real source contribution.

Let `[L5,U5]` be the full directed enclosure of (TN1). For both fixed heights
the checker requires

\[
 U_5(H^2+1/4)^5<c_5,\qquad H\in\{4064,4072\}.
\tag{TN3}
\]

Any remaining zero with `|Re rho|<=H` would have remaining multiplicity
at least one and norm at most `sqrt(H^2+1/4)`, so its positive-half-plane
occurrence alone contradicts (TN3). All other source contributions remain
nonnegative. The same argument excludes an extra occurrence at a selected
low zero, forcing simplicity. No selected interval meets either boundary.
Thus the recovered complete simple positive root counts are 3540 and 3548,
derived from the interval lists only after the exclusion proof.

## 3. Full companion columns and finite scope

The separately proved column theorem gives for either accepted H,

\[
\begin{gathered}
 0\le r\le2H-3,\quad \lambda>0,\quad |T|<H-(r+2)/2,\quad y\ge0,\\
 E_r=\Xi^{(r)}-i\lambda\Xi^{(r+1)},\qquad
 E_r(T-iy)\ne0,\quad E'_r(T-iy)\ne0,\quad
 \operatorname{Re}\frac{iE_r(T-iy)}{E'_r(T-iy)}>0.
\tag{TN4}
\end{gathered}
\]

The maximum derivative orders are 8125 and 8141. Horizontal range and
derivative order remain finite. The historical Gram/Rosser and published
verification contracts are absent; the complete analytic source, imported
older primitive signs and explicitly imported lower count-free census
remain load-bearing dependencies. The separate global moment bootstrap
at real part 14 is not required by this composition.

## 4. Replay and frozen source identities

The five files are this document, `produce_tenth_prefix.py`,
`tenth_prefix_candidates.json`, `check_tenth_moment_census.py`, and
`tenth_moment_census.json`. The checker binds the exact lower census receipt,
checks the direct source identities in both imported packets, replays the
new signs and native jet, and evaluates exact rational exclusion predicates.
Its receipt records each import/replay boundary and hashes the displayed
direct source list and native binaries. It does not claim to authenticate
an infinite theta/product theorem or every transitive dependency by finite
checking. No point root or midpoint coefficient replaces a source interval.

```bash
source /workspace/.riemann-tools/activate.sh
python research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_tenth_moment_census.py --output /tmp/tenth-moment-replay.json
```

Optimized Python retains every explicit failure branch. The supported
output argument preserves the official receipt. All primitive runs use the
same directed native arithmetic implementation; no independent arithmetic
backend or historical count computation is reproduced.
