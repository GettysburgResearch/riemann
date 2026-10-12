# Directed eighth-moment recovery of a larger count-free census

Status: proposed directed finite source packet; execution and independent
review scope are recorded in its receipt and separate exact-source reviews.
Scope: actual Xi, 278 refined low-zero intervals, the native degree-eight
logarithmic jet, and count-free complete simple census recovery at two fixed
heights. No historical finite zero-count contract or published large
verification is used by this theorem.
Exact dependencies: the complete positive theta/strip/product source in
[THEOREM.md](THEOREM.md), the one-occurrence selection argument in
[COUNT_FREE_CENSUS_RECOVERY.md](COUNT_FREE_CENSUS_RECOVERY.md), the acute
higher-moment theorem (HM1)--(HM9) in
[HIGHER_MOMENT_CENSUS_RECOVERY.md](HIGHER_MOMENT_CENSUS_RECOVERY.md), and
the separately proved [column theorem](CENSUS_FULL_COLUMN_SECTOR.md).
What was actually run: an exploratory directed precursor replayed 556 actual
Hardy-Z signs, evaluated the native degree-eight Gamma/zeta logarithmic jet,
and found the strict eighth-moment exclusion guards. The named checker below
performs the same primitive and whole-source guard checks; accepted machine
receipts identify successful runs, rather than the precursor alone.
Smallest remaining gap: independent frozen-source review and native replay
of this new finite packet. No global real-zero or RH assertion follows.

## 1. Source intervals and exact selection semantics

`produce_eighth_prefix.py` produces 278 candidate intervals of width
`2^-80`, corresponding to the original disjoint intervals below 512.
`check_eighth_moment_census.py` verifies their strict nesting, ordered
geometry, and all 556 strict opposite endpoint signs of the actual Hardy
function (RP1). Candidates supply no root or completeness theorem by
themselves. The refined sign changes each supply a real Xi root, from which
exactly one occurrence is selected. No prior root uniqueness is assumed.

For the remaining 7771 original intervals, retain the original `2^-24`
geometry and import only their already authenticated primitive sign facts
from NATIVE_SLAB_CERTIFICATE.md and its frozen receipt. The earlier count,
uniqueness and complete-census claims are unused here. The producer may use
the library's indexed-root algorithm to suggest candidates; the checker
requires actual strict signs and nesting and calls no complete-count routine.
Thus correctness of the chosen candidate indices is not a load-bearing
completeness assertion.

Each selected `gamma_j` is enclosed by its full interval. Ordered disjoint
intervals identify distinct real zeros. Removing one selected occurrence
and its negative reflection from the complete even source product leaves
every extra multiplicity and every unselected zero in the residual source.

## 2. Native complete moment and positive angular projection

At 224 bits, truncation capacity nine supplies the actual degree-eight jet
through the exact source formula (RP2). The checker verifies its parity and
real-coefficient enclosures and the strict native seed `Xi(0)>99/200`.
The normalized logarithmic jet and all 8049 full selected-root intervals
enclose

\[
 T_4=-4[z^8]\log\frac{\Xi(z)}{\Xi(0)}
         -\sum_{j=1}^{8049}\gamma_j^{-8}.
\tag{EM1}
\]

The complete product interprets (EM1) as the entire remaining inverse-eighth
moment. This uses no assumption that those remaining roots lie beyond 8192.
The positive-theta disk argument (CF1)--(CF5), with its exact rational
seed comparison, gives `|Re rho|>sqrt(30)>27/5` for every actual source zero.
For `A=1/2` and `R0=27/5`, define the positive exact rational constant

\[
 c_4=\frac{\sum_{j=0}^4(-1)^j{8\choose2j}
             R_0^{8-2j}A^{2j}}{(R_0^2+A^2)^4}>0.
\tag{EM2}
\]

The acute bound `8 atan(5/54)<20/27<pi/2` and complete conjugate grouping
give the full remaining-source bound

\[
 T_4\ge c_4\sum_{\text{remaining}\operatorname{Re}\rho>0}
                  m_\rho|\rho|^{-8}\ge0.
\tag{EM3}
\]

No complex pair can cancel this positive real projection. The checker
recomputes (EM1) over every selected-root ball, stores its exact rational
enclosure `[L4,U4]`, and tests for each displayed fixed height

\[
 U_4(H^2+1/4)^4<c_4,\qquad H\in\{3072,3168\}.
\tag{EM4}
\]

Any unselected zero with `|Re rho|<=H` would contribute at least one unit
`c4/(H^2+1/4)^4` to (EM3), contradicting (EM4). Extra multiplicities at a
selected zero below `H` are excluded by the same argument. Both height
boundaries are outside every selected interval, as the checker requires.
Thus each accepted height has a complete **simple** real census. The finite
primitive endpoint signs are used for existence, and the complete native
moment with positive projection is used for absence of any omitted root.

## 3. Resulting full companion columns retain finite scope

The recovered counts are 2539 positive simple zeros through 3072 and 2634
through 3168, if the corresponding native guards pass. These counts are
derived by counting the authenticated intervals below the accepted height;
they are not imported complete zero counts.

Applying the separately reviewed column theorem, for either accepted `H`,
every integer `0<=r<=2H-3` and every real `lambda>0` satisfy

\[
\begin{gathered}
 |T|<H-(r+2)/2,\quad y\ge0,\quad
 E_r=\Xi^{(r)}-i\lambda\Xi^{(r+1)},\\
 E_r(T-iy)\ne0,\quad E_r'(T-iy)\ne0,\quad
 \operatorname{Re}\frac{iE_r(T-iy)}{E_r'(T-iy)}>0.
\tag{EM5}
\end{gathered}
\]

The maximum derivative orders are 6141 and 6333 respectively. Horizontal
range and derivative order remain finite. The complete analytic Xi source
and the imported older primitive sign facts remain dependencies; the
historical zero-count and published verification contracts do not.

## 4. Reproduction and source bindings

The five machine/source files are this document, `produce_eighth_prefix.py`,
`eighth_prefix_candidates.json`, `check_eighth_moment_census.py`, and
`eighth_moment_census.json`. The checker hashes the displayed direct source
list, prior primitive receipt/input, producer/candidate/checker, and native
Arb/acb/series binaries. It checks the direct source hashes in the imported
primitive receipt; it does not claim to hash every transitive mathematical
dependency. No native endpoint, complete product, theta identity, or column
theorem is silently promoted beyond the explicitly stated replay/import
boundary.

```bash
source /workspace/.riemann-tools/activate.sh
python research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_eighth_moment_census.py --output /tmp/eighth-moment-replay.json
```

Every acceptance condition uses an explicit failure branch, so optimized
Python preserves the predicates. `--output` preserves the frozen official
receipt. All modes use the same native arithmetic implementation; no second
arithmetic backend or historical count computation is reproduced.
