# Extend the frozen eighth-moment census by the global moment bootstrap

Status: proposed analytic composition with exact rational finite guards.
Scope: the two explicitly imported frozen native packets below, the actual
complete Xi source, and a finite complete simple census through 3272. The
composition itself replays no native Gamma/zeta jet or Hardy-Z endpoint.
Exact dependencies: [EIGHTH_MOMENT_CENSUS_RECOVERY.md](EIGHTH_MOMENT_CENSUS_RECOVERY.md),
the separately reviewed
[global moment bootstrap](../../heights/final-review/COMPLETE_MOMENT_ZERO_FREE_BOOTSTRAP.md),
and [CENSUS_FULL_COLUMN_SECTOR.md](CENSUS_FULL_COLUMN_SECTOR.md).
What was actually run: the imported eighth-moment packet replayed its 556
new endpoints and degree-eight jet; the imported bootstrap replayed a
degree-twelve unsubtracted jet. This composition only checks exact rational
projection/exclusion arithmetic, input/source bindings and boundary geometry.
Smallest remaining gap: independent source/math review and exact replay of
this new composition. It gives no global real-zero assertion or RH proof.

The frozen eighth-moment packet encloses the exact complete residual

\[
 T_4=-4[z^8]\log\frac{\Xi(z)}{\Xi(0)}-\sum_{j=1}^{8049}\gamma_j^{-8}
 \le U_4.
\tag{EC1}
\]

It selects one occurrence from each authenticated real sign interval and
retains every other source zero or multiplicity. The native upper bound is
valid over the full selected-root intervals and assumes no initial finite
completeness or simplicity. Its exact receipt SHA is
`e224616d2497c0477146ccd0c712e3888c55a279e55c5fa27115310b7710a47f`.

The frozen complete-moment bootstrap proves `|Re rho|>14` for every actual
Xi zero, using the positive theta source, classical strip, native seed and
five successive **unsubtracted** complete moment guards. Its exact receipt
SHA is `b1074698a2529e98637ad8dc4554f4d89f55e063dbe44c1841e93ba5e620cec3`.
That packet uses no finite sign list, root index or zero-count routine.

The same remaining-source selection from (EC1) therefore has the stronger
complete projection

\[
 T_4\ge c_4(14,1/2)\sum_{\text{remaining}\operatorname{Re}\rho>0}
                m_\rho|\rho|^{-8},\qquad
 c_4(14,1/2)=
 \frac{\sum_{j=0}^4(-1)^j{8\choose2j}14^{8-2j}(1/2)^{2j}}
      {(14^2+1/4)^4}>0.
\tag{EC2}
\]

The angular hypothesis is strict because `8 atan(1/28)<2/7<pi/2`.
Complete conjugate grouping and nonnegative remaining integer multiplicity
make every real part positive. No native moment or finite root interval is
changed in moving from the older projection to (EC2).

For the two fixed heights `H=3264,3272`, the exact rational checker requires

\[
 U_4(H^2+1/4)^4<c_4(14,1/2).
\tag{EC3}
\]

No selected interval meets either boundary. The one-occurrence exclusion
argument in (HM4)--(HM5) then proves complete simple real censuses of 2730
and 2737 positive roots at those heights. These counts are obtained from
the interval lists after completeness is proved; they are not imported
complete zero counts. The exact accepted guard ratios are about 0.962736
and 0.981776, respectively, with rounded values supplied only for reading.

Applying the separately reviewed full-column theorem gives, for either H,

\[
\begin{gathered}
 0\le r\le2H-3,\qquad\lambda>0,\qquad |T|<H-(r+2)/2,\qquad y\ge0,\\
 E_r=\Xi^{(r)}-i\lambda\Xi^{(r+1)},\quad
 E_r(T-iy)\ne0,\quad E'_r(T-iy)\ne0,\quad
 \operatorname{Re}\frac{iE_r(T-iy)}{E'_r(T-iy)}>0.
\tag{EC4}
\end{gathered}
\]

The strongest displayed range has `H=3272` and `0<=r<=6541`. Both the
horizontal range and derivative order remain finite. The historical
Gram/Rosser count and published large verification are absent; the complete
analytic Xi source and the explicitly imported primitive facts remain.

`check_eighth_bootstrap_composition.py` binds both imported receipt SHAs,
checks their direct source bindings, reads their stated native facts,
recomputes the exact positive projection and both exclusion predicates,
and checks the selected interval boundaries and list sizes. The generated
`eighth_bootstrap_composition.json` labels these imports and records that no
native primitive is replayed by this composition checker. It does not treat
an internally consistent derived JSON as an authenticated native calculation.

```bash
python research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_eighth_bootstrap_composition.py --output /tmp/eighth-bootstrap-composition.json
```

Optimized Python preserves every explicit acceptance branch. No further
arithmetic implementation, native endpoint replay or higher jet is claimed.
