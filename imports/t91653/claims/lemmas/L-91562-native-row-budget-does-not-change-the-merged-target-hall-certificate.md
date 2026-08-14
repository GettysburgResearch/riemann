# L-91562 — The native row budget does not change the merged target-Hall certificate

Claim ID: `L-91562`  
Status: **PROVED EXACT NORMALIZATION-TRANSFER THEOREM — DIRECTED INPUT `L-91550` RETAINED**  
Created: 2026-08-13  
Depends on: `L-91454`, `L-91545`, `L-91550`, `L-91556`, `L-91560`  
RH status: **unproved**

## 1. Question after the row-budget correction

`L-91556` replaces the full binary branch scores in the recursive physical row
by the native row-budgeted scores

\[
 \widetilde S_s=(1-r^2)(5z-3),
 \qquad
 \widetilde S_h=r^2(5z-3).
 \tag{L-91562.1}
\]

The target channels are unchanged.  A hostile review must therefore check that:

1. the no-upward target-Hall transports still exist;
2. the same transports remain score-superordinate for (L-91562.1);
3. the exact component-row lift still has the required monotone normalized
   profile.

No new numerical Hall scan is needed: all directed inequalities depend only on
the unchanged target channels, and the changed row/score coefficients enter as
positive constants.

## 2. Unchanged target channels

Put

\[
 r=p^{-1/2},
 \qquad
 0<r\le67^{-1/2},
 \qquad
 z=\sqrt{x/n}\ge1.
 \tag{L-91562.2}
\]

The survival and hazard targets are

\[
 T_s=g_s(\alpha_s z-1),
 \qquad
 g_s=(1-r)(r+3),
 \qquad
 \alpha_s=\frac{2(r+2)}{r+3},
 \tag{L-91562.3}
\]

\[
 T_h=g_h(\alpha_h z-1),
 \qquad
 g_h=r(r+2),
 \qquad
 \alpha_h=\frac{2(r+1)}{r+2}.
 \tag{L-91562.4}
\]

The parameter corridors are

\[
 \boxed{
 \frac43\le\alpha_s<\frac32,
 \qquad
 1\le\alpha_h<\frac65.
 }
 \tag{L-91562.5}
\]

These are exactly two of the target corridors certified in `L-91550`.
Consequently every active odd target demand admits a no-upward Hall transport
with support

\[
 e\le o
 \tag{L-91562.6}
\]

and directed prefix margin greater than `1/250` on the complete factor-54
window.

The target capacities and demands have not changed by even a scalar factor from
`L-91454/L-91550`; the same transport may be reused verbatim.

## 3. Score superordination with the native budget

The target per native score ratios are

\[
 \boxed{
 q_s(z)
 =\frac{2(r+2)z-(r+3)}
        {(1+r)(5z-3)},
 }
 \tag{L-91562.7}
\]

\[
 \boxed{
 \widetilde q_h(z)
 =\frac{(2r+2)z-(r+2)}
        {r(5z-3)}.
 }
 \tag{L-91562.8}
\]

`L-91556` gives the exact derivatives

\[
 \boxed{
 q_s'(z)
 =\frac{3-r}{(1+r)(5z-3)^2}>0,
 }
 \tag{L-91562.9}
\]

\[
 \boxed{
 \widetilde q_h'(z)
 =\frac{4-r}{r(5z-3)^2}>0.
 }
 \tag{L-91562.10}
\]

Both ratios equal `1/2` at `z=1`.

For a Hall edge `e<=o`, one has `z_e>=z_o`, hence

\[
 q_\tau(z_e)\ge q_\tau(z_o).
 \tag{L-91562.11}
\]

Transport in target-mass units therefore gives

\[
 \boxed{
 \sum_{o,e}t_{o,e}
 \left[
  \frac1{q_\tau(z_o)}-
  \frac1{q_\tau(z_e)}
 \right]
 \ge0.
 }
 \tag{L-91562.12}
\]

Thus the residual positive source measure represents branch target exactly and
has native row-budgeted score at least the signed branch score.  The favorable
full binary surplus is not needed.

## 4. The row profile changes only by a positive constant

The branch row atoms are

\[
 R_s(n;j)=(1-r^2)n^{-1/2}Q_{x/n}(j),
 \tag{L-91562.13}
\]

\[
 R_h(n;j)=r^2n^{-1/2}Q_{x/n}(j).
 \tag{L-91562.14}
\]

Divide by the corresponding target atom.  Using (L-91562.3)--(L-91562.4),

\[
 \boxed{
 \frac{R_s(n;j)}{T_s(n)}
 =\frac{1+r}{r+3}
  \frac{Q_Y(j)}{\alpha_s\sqrt Y-1},
 }
 \tag{L-91562.15}
\]

\[
 \boxed{
 \frac{R_h(n;j)}{T_h(n)}
 =\frac{r}{r+2}
  \frac{Q_Y(j)}{\alpha_h\sqrt Y-1},
 }
 \tag{L-91562.16}
\]

where `Y=x/n`.  The prefactors are positive and independent of `Y` and of the
row coordinate `j`.

`L-91550` certifies that

\[
 \frac{Q_Y(j)}{\alpha\sqrt Y-1}
 \tag{L-91562.17}
\]

is strictly increasing for every target parameter in the corridors
(L-91562.5), with directed derivative-numerator margin greater than `1/25`.
Multiplication by the positive constants in (L-91562.15)--(L-91562.16)
preserves the sign.

Hence every no-upward target-Hall edge contributes a coefficientwise
nonnegative exact row difference under the native row budget.

## 5. Exact Hall residualization

Apply `L-91545` using the unchanged target transport and the row profiles
(L-91562.15)--(L-91562.16).  For both types one obtains a positive residual
source `c_tau` and positive row bonus `B_tau` such that

\[
 T(c_\tau)=T(E_\tau)-T(O_\tau),
 \tag{L-91562.18}
\]

\[
 \widetilde S(c_\tau)
 \ge\widetilde S(E_\tau)-
     \widetilde S(O_\tau),
 \tag{L-91562.19}
\]

\[
 \boxed{
 R(E_\tau)-R(O_\tau)
 =R(c_\tau)+B_\tau,
 \qquad
 B_\tau\ge0.
 }
 \tag{L-91562.20}
\]

Summing survival and hazard and invoking the exact native cocycle `L-91560`
gives the literal parent-row identity required by `L-91559`.

## 6. Replay status

The retained merged certificate already checks a larger parameter box than the
native row budget uses:

```text
survival target: alpha in [4/3,3/2];
hazard target:   alpha in [1,6/5];
component rows:  every alpha in [1,5/3].
```

Its verdict remains

```text
PASS_MERGED_BINARY_HALL_ROW_CORRIDORS
```

with:

```text
Hall-prefix margin >1/250;
normalized row derivative numerator >1/25.
```

Only the exact coefficient transfer in Sections 3--4 was new, and that transfer
is replayed symbolically in `X-91556`.

## 7. Boundary

```text
survival/hazard target Hall graphs                   UNCHANGED
merged directed target margins                       RETAINED / L-91550
native target-per-score monotonicity                  EXACT
native row/target normalization                       EXACT
component-row directed margins                        RETAINED / L-91550
native Hall residual source + row bonus               EXACT
new numerical Hall scan                               NOT REQUIRED
live-parent file transplant                           STILL REQUIRED
Riemann Hypothesis                                   UNPROVEN
```
