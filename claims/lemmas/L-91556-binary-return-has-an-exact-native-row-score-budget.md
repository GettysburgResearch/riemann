# L-91556 — The binary return has an exact native row-and-score budget

Claim ID: `L-91556`  
Status: **PROVED EXACT ONE-PRIME TARGET/SCORE/ROW NORMALIZATION — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-13  
Depends on: `L-91452/L-91454`, `L-91540`, `L-91545`, `L-91553/L-91554`  
RH status: **unproved**

## 1. Why a new normalization is needed

The binary target and score identities alone do not determine the coefficient
of the physical component row.  This was left explicit in `L-91542`, whose
scope firewall says that the component-row transfer identity remained open.

The full binary score contains a favorable target-null surplus.  Assigning that
surplus to the recursive row packets overstates the native score obligation and
obscures the exact row partition.  The correct normalization keeps the surplus
current-generation and budgets only the score carried by the native parent row.

## 2. Parent and binary scalar atoms

Put

\[
 r=p^{-1/2},
 \qquad
 A=1-r^2,
 \qquad
 d=r(1-r),
 \qquad
 z=\sqrt{x/n}\ge1.
 \tag{L-91556.1}
\]

Suppress the common positive source factor `n^-1/2`.  The native parent target
and score are

\[
 \boxed{
 T_0=4z-3,
 \qquad
 S_0=5z-3.
 }
 \tag{L-91556.2}
\]

The target-exact binary return of `L-91452` has

\[
 \boxed{
 T_s=(1-r)\,[2(r+2)z-(r+3)],
 }
 \tag{L-91556.3}
\]

\[
 \boxed{
 T_h=r\,[(2r+2)z-(r+2)].
 }
 \tag{L-91556.4}
\]

Its exact branch scores are

\[
 S_s=A(5z-3),
 \tag{L-91556.5}
\]

\[
 S_h=r[(4r+1)z-(2r+1)].
 \tag{L-91556.6}
\]

They satisfy

\[
 T_s+T_h=T_0,
 \qquad
 S_s+S_h=S_0+d(z-1).
 \tag{L-91556.7}
\]

## 3. Exact native score allocation

Define the **row-budgeted native scores**

\[
 \boxed{
 \widetilde S_s=A(5z-3),
 \qquad
 \widetilde S_h=r^2(5z-3).
 }
 \tag{L-91556.8}
\]

Then

\[
 \boxed{
 \widetilde S_s+\widetilde S_h=S_0
 }
 \tag{L-91556.9}
\]

because `A+r^2=1`.  The survival allocation is its full binary score, while

\[
 \boxed{
 S_h-\widetilde S_h=d(z-1)\ge0.
 }
 \tag{L-91556.10}
\]

Thus the complete excess binary score is one target-null favorable hazard
surplus.  It is not needed in the inherited score ledger and may remain in the
current generation.

## 4. Exact physical row partition

Let

\[
 \mathcal R_Y(j)=n^{-1/2}Q_Y(j),
 \qquad
 Y=x/n=z^2,
 \tag{L-91556.11}
\]

be the native parent component-row atom.  Assign the branch row coefficients

\[
 \boxed{
 \kappa_s=A,
 \qquad
 \kappa_h=r^2.
 }
 \tag{L-91556.12}
\]

Both are nonnegative and

\[
 \boxed{
 \kappa_s+\kappa_h=1.
 }
 \tag{L-91556.13}
\]

Therefore, coefficientwise in every exact finite row,

\[
 \boxed{
 \mathcal R_Y
 =\kappa_s\mathcal R_Y+
  \kappa_h\mathcal R_Y.
 }
 \tag{L-91556.14}
\]

The same coefficients carry the native score:

\[
 \widetilde S_\tau
 =\kappa_\tau(5z-3).
 \tag{L-91556.15}
\]

This is the missing scalar/row normalization.  Neither branch copies the parent
row, and the branch rows sum exactly to the native parent row.

## 5. Target-Hall compatibility

For survival, target per row-budgeted score is

\[
 q_s(z)
 =\frac{2(r+2)z-(r+3)}
        {(1+r)(5z-3)}.
 \tag{L-91556.16}
\]

For hazard, it is

\[
 \boxed{
 \widetilde q_h(z)
 =\frac{(2r+2)z-(r+2)}
        {r(5z-3)}.
 }
 \tag{L-91556.17}
\]

Direct differentiation gives

\[
 \boxed{
 q_s'(z)
 =\frac{3-r}{(1+r)(5z-3)^2}>0,
 }
 \tag{L-91556.18}
\]

\[
 \boxed{
 \widetilde q_h'(z)
 =\frac{4-r}{r(5z-3)^2}>0.
 }
 \tag{L-91556.19}
\]

Both ratios equal `1/2` at `z=1`; hence

\[
 \boxed{
 q_s(z)\ge\frac12,
 \qquad
 \widetilde q_h(z)\ge\frac12
 \qquad(z\ge1).
 }
 \tag{L-91556.20}
\]

The no-upward target-Hall transports of `L-91454` are unchanged, because their
target atoms are unchanged.  Equations (L-91556.18)--(L-91556.19) show that the
residual positive source is score-superordinate for the **native row-budgeted
score** as well.

The target-normalized branch rows are positive constants times

\[
 \frac{Q_Y(j)}{\alpha_\tau\sqrt Y-1},
 \tag{L-91556.21}
\]

so the existing directed component-row monotonicity gives the exact Hall row
bonus of `L-91545`.  Applying Hall separately to the two branch labels yields

\[
 \boxed{
 T(c_s)+T(c_h)=T_{\rm parent},
 }
 \tag{L-91556.22}
\]

\[
 \boxed{
 \widetilde S(c_s)+
 \widetilde S(c_h)\ge S_{\rm parent},
 }
 \tag{L-91556.23}
\]

and

\[
 \boxed{
 R_{\rm native,parent}
 =R(c_s)+R(c_h)+B_s+B_h,
 \qquad B_s,B_h\ge0.
 }
 \tag{L-91556.24}
\]

Here `R_native,parent` is the literal native component row, not an independently
scaled binary surrogate.

## 6. Fixed-67 entropy compatibility

Let

\[
 \mathcal E(Y)=\sum_jQ_Y(j)G_j
 \tag{L-91556.25}
\]

be the literal component entropy.  The two branch entropies are

\[
 \mathcal E_s(Y)=A\mathcal E(Y),
 \qquad
 \mathcal E_h(Y)=r^2\mathcal E(Y).
 \tag{L-91556.26}
\]

`L-91553` proves, for `Y>=67`,

\[
 \mathcal E(Y)-\mathcal E(Y/67)
 \ge5(\sqrt Y-\sqrt{Y/67}).
 \tag{L-91556.27}
\]

Multiplying by `kappa_tau` gives exactly

\[
 \boxed{
 \mathcal E_\tau(Y)-\mathcal E_\tau(Y/67)
 \ge
 \widetilde S_\tau(Y)-
 \widetilde S_\tau(Y/67).
 }
 \tag{L-91556.28}
\]

Thus the inherited row and score use the same coefficients.  No hidden branch
prefactor remains in `L-91553/L-91554`.

At the terminal quotient `1<=Y<67`, (L-91556.20) gives

\[
 \widetilde S_\tau(Y)\le2T_\tau(Y),
 \tag{L-91556.29}
\]

which is precisely the terminal estimate used by `L-91554`.

## 7. Consequence

The exact one-prime entry now has three simultaneous one-use identities:

```text
target:  survival + hazard = native parent;
score:   row-budgeted survival + hazard = native parent;
row:     A Q + r^2 Q = Q.
```

The additional binary score `d(z-1)` is favorable current-generation slack.
After Hall, the positive residual sources and row bonuses retain these exact
native normalizations.  The fixed-67 score repair and finite-Euler terminal
bound therefore apply with the literal component-row coefficients.

This closes hostile-review item 3 in `T-91555`: the branch row prefactor is no
longer imported or inferred from scalar target/score algebra.

## 8. Scope firewall

The theorem does not by itself prove the native endpoint-measure boundary
inside `J_Lambda`, the one-use continuum-to-finite collar assembly, or final
radix-four feasibility.  It proves the exact local target/score/row
normalization which those global interfaces must consume.

```text
binary target partition                              EXACT
native row-budgeted score partition                  EXACT
favorable excess binary score                        EXACT
literal parent component-row partition               EXACT
row-budgeted target-per-score monotonicity            EXACT
Hall residual native score superordination           EXACT
fixed-67 entropy/score coefficient match              EXACT
native J_Lambda boundary                              SEPARATE / OPEN
Riemann Hypothesis                                    UNPROVEN
```
