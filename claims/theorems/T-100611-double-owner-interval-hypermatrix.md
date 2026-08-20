# T-100611 — Double-owner interval hypermatrix after hostile source audit

Claim ID: `T-100611`  
Status: **EXACT INDEXING/ASSIGNMENT FRAMEWORK; REGIONAL ESTIMATES OPEN EXCEPT WHERE CITED**  
Created: 2026-08-20  
Audited: 2026-08-21  
Depends on: `L-100605`; `L-100610--L-100616`; PR #695 balanced coboundary identities  
RH status: **unproved**

The exact double-owner block is

\[
\mathcal D_{i,i}=-r_iU_i,
\qquad
\mathcal D_{i,j}
=r_ir_jU_iU_j
\prod_{i<h<j}(I-r_hU_h),
\quad i<j.
\tag{T-100611.1}
\]

For the cubic endpoint kernel, the equivalent positive-hazard block is

\[
H_{i,j}=\Delta_i\Delta_jE_{i+1:j-1}\Psi.
\tag{T-100611.2}
\]

The two presentations are opposite signed/positive coordinate systems on the
same finite prime interval. The matrix is indexed by actual labelled
coordinates, including the duplicated `67` occurrence.

## Region I — diagonal/singleton terms

The diagonal contains no interior Euler product. In the positive-hazard
coordinates, root and singleton packets are nonnegative by cubic monotonicity.
These terms are therefore not part of the terminal signed estimate.

## Region II — ratio-eight endpoint intervals

For endpoint prime values satisfying

\[
67\le p_i<p_j\le8p_i,
\]

`L-100613`, with its duplicated-67 audit, proves the complete interior Euler
packet nonnegative. Equal-value duplicated-67 endpoints have empty interior and
are covered by `L-100612`.

Thus the short labelled interval region is closed unconditionally.

## Region III — wider endpoint intervals

For `p_j/p_i>8`, no theorem in the repository permits the completed core and
its desquaring transitions to be estimated separately. PR #695 proves the
inverse-free identity

\[
E_{a:b}
=Q_{a:b}-\sum_{t=a}^{b}Q_{a:t-1}R_tE_{t+1:b}
\tag{T-100611.3}
\]

and the double-owner rectangle telescope. These identities preserve the
power-sized carrier cancellation only when the completed and transition terms
remain in one oriented state.

Finite interior squaring may be used as an **exact coordinate change** in this
balanced expression. It is not a positive inverse and does not independently
bound the native block.

## Region IV — genuine divisor restrictions only

The positive divisor-renewal theorem `L-99961` applies when a term has first
been proved to be the literal restriction

\[
\sum_m\beta(dm)m^{-z}.
\]

It does not apply merely because a scale dilation `U_d` occurs in an operator
expansion. The earlier arrows `L-100603` and `L-100604` are withdrawn at that
statement-to-use interface and are not inputs to this theorem.

If a future argument derives a genuine divisor restriction inside one oriented
block, `L-99961` may then transport it positively with subpower Mellin mass.
Until that typing theorem is supplied, no positive-renewal credit is assigned.

## Two complementary implication gates

The exact matrix now has two honest conclusion-facing formulations:

1. **Two-ended energy gate.** Prove both `FOCR100610` and `LOCR100610`; then
   `T-100610` gives subpower negative mass and RH.
2. **Activation gate.** Prove `AEP100612` and `DNT100612` for the actual
   labelled source; then `T-100612` gives positivity of the critical envelope
   and RH.

These are useful AND-gates, not claims that one gate follows from the other.
The row/column and activation coordinates can be mixed region by region, but
every transition must retain one common source ledger.

## Audited regional table

| matrix region | exact tool | status |
|---|---|---|
| root / singleton | cubic monotonicity | proved positive |
| duplicated-67 pair | endpoint convexity | proved positive |
| distinct endpoint ratio `<=8` | `L-100613` labelled budget | proved positive |
| long interval | rectangle telescope + balanced first-transition identity | exact reduction; estimate open |
| finite squared interior | source-faithful coordinate identity | exact; no positive desmoothing |
| genuine divisor restriction | `L-99961` | positive only after literal restriction is proved |
| carrier / transition split | PR #695 firewall | must remain balanced |

## Exact frontier

After the audit, the shared terminal object is not a sum of separately positive
regional estimates. It is the oriented long-interval boundary state left after
short intervals and singletons are removed while completed/transition carriers
remain paired.

A subpower logarithmic bound for that balanced state feeds either the
critical-negative-mass detector or the compact-wavelet detector and yields RH.
It remains open.

```text
double-owner indexing                      proved exact
short intervals including duplicate 67     proved positive
long-interval balanced reduction            proved exact
positive renewal for generic dilations      withdrawn / invalid
FOCR+LOCR AND-gate                          conditional exact
AEP+DNT AND-gate                            conditional exact
balanced long-interval estimate             open / RH-bearing
Riemann Hypothesis                          unproved
```