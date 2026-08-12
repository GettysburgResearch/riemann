# T-91546 — The target-Hall residual source and one geometric split form a complete factor-54 reset

Claim ID: `T-91546`  
Status: **CANDIDATE COMPLETE FACTOR-54 COMPOSITION — MERGED REPLAY AND INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-13  
Frozen parent: PR `#399` at `22d7f2f3f3668f664c09708838f6a738e4398eef`  
Integrated producer: `L-91452/L-91454` transplanted from PR `#416` at `23aa9adc48a6c3176b799944dfbac11e665407ef`  
Depends on: `L-91329`, `T-91302`, `L-91452/L-91454`, `L-91540/L-91541/L-91543/L-91545`  
RH status: **unproved pending the audits stated in Section 8**

## 1. Native one-prime input

At one normalized factor-54 reset, the terminal finite source projection supplies
a canonical squarefree/Mobius channel with positive target and score ledgers and
nonnegative exact component rows on the terminal child window.  Let `p>=67` be
the first unabsorbed rough prime.

The integrated one-prime producer `L-91452/L-91454` constructs two disjoint
branch labels:

```text
survival branch s;
hazard branch h.
```

At the state level their target and score satisfy

\[
 \boxed{
 T_s+T_h=T_{\rm parent},
 \qquad
 S_s+S_h=S_{\rm parent}+dR\ge S_{\rm parent},
 }
 \tag{T-91546.1}
\]

where `d=p^(-1/2)(1-p^(-1/2))` and `R>=0` is the reserve coordinate.

Both branch targets admit directed no-upward Hall transports in target units;
their target-per-score and target-normalized component-row profiles are
monotone along every Hall edge.

## 2. Exact Hall residual-source decomposition

Apply `L-91545` separately to the two branch Hall networks.  It yields positive
source measures

\[
 c_s\ge0,
 \qquad
 c_h\ge0,
 \tag{T-91546.2}
\]

in the ordinary paired survival and hazard kernel types, and positive
current-generation row bonuses

\[
 B_s\ge0,
 \qquad
 B_h\ge0.
 \tag{T-91546.3}
\]

The identities are

\[
 \boxed{
 T(c_s)+T(c_h)=T_{\rm parent},
 }
 \tag{T-91546.4}
\]

\[
 \boxed{
 S(c_s)+S(c_h)\ge S_s+S_h\ge S_{\rm parent},
 }
 \tag{T-91546.5}
\]

and, coefficientwise in every finite component row,

\[
 \boxed{
 R_{\rm signed,parent}
 =R(c_s)+R(c_h)+B_s+B_h.
 }
 \tag{T-91546.6}
\]

All recursively inherited target is carried by the genuine positive source
measures `c_s,c_h`.  The matched Hall edges occur only in `B_s,B_h`, which have
zero target source mass and are paid in the current generation.

## 3. Contract both target-bearing outputs

The hazard output is placed by the exact affine functor at endpoint

\[
 Y_h=X/p\le X/67<c_0X.
 \tag{T-91546.7}
\]

For the survival source apply the deterministic split of `L-91543`:

\[
 \theta_s(n)=\mathbf1_{n\le X/67}.
 \tag{T-91546.8}
\]

By `L-91540`, this gives a same-type survival child at

\[
 Y_s=X/67<c_0X
 \tag{T-91546.9}
\]

plus nonnegative current-generation target, score and row residuals.

Normalize the parent target to one and let `omega_s,omega_h` be the target masses
of the two contracted children.  Equations (T-91546.4) and the positive survival
residual give

\[
 \boxed{
 \omega_s\ge0,
 \quad
 \omega_h\ge0,
 \quad
 \omega_s+\omega_h\le1.
 }
 \tag{T-91546.10}
\]

Thus no ordered-prime survival loop remains.

## 4. Positive physical assembly

The complete parent row is the sum of:

1. the terminal finite positive row;
2. the survival and hazard Hall residual-source rows;
3. the target-null Hall bonuses `B_s,B_h`;
4. the positive survival endpoint residual;
5. the affine-lifted hazard child row;
6. arbitrary feasible packings of the two contracted child packets.

Every term is coefficientwise nonnegative.  The affine lift is exact on its
colored rough fiber and score-favorable.  All child colors are first pushed to
the common parent continuum coordinate; `L-91329` sums the total measure and
quantizes once.  The finite collar, top omission and bridge are therefore spent
once per generation, not once per child or Hall edge.

The target-null correction of `L-91452` lies in the single resident innovation
port.  It is charged as one current-generation positive packet before the
children are normalized; it is not duplicated by type.

## 5. Local debt

The one-prime Hall entry is score-superordinate by (T-91546.5), so it creates no
positive score debt.

For a target-normalized paired source, every geometric endpoint residual has
positive score-loss debt at most its target residual by `L-91540`.  Consequently

\[
 \boxed{
 E_X\le C
 }
 \tag{T-91546.11}
\]

for an absolute constant `C` including the bounded terminal collar and common
port.  The stronger polylog-log allowance of `T-91302/T-91541` is therefore not
needed here.

## 6. Branching recurrence

Let `L_X^C` be the worst target-normalized loss over the two paired kernel types.
The actual-packet consumer `T-91541` gives

\[
 \boxed{
 \mathfrak L_X^{\mathcal C}
 \le C+
 \omega_s\mathfrak L_{X/67}^{\mathcal C}
 +\omega_h\mathfrak L_{X/p}^{\mathcal C},
 \qquad
 \omega_s+\omega_h\le1.
 }
 \tag{T-91546.12}
\]

Every branch contracts by at least `67`.  Expanding the substochastic tree gives

\[
 \boxed{
 \mathfrak L_X^{\mathcal C}=O(\log X)=o(\log^2X).
 }
 \tag{T-91546.13}
\]

The native packet enters the typed class through Sections 1--3 with bounded
entry debt, so the native loss obeys the same bound.

## 7. Conditional RH consequence

The factor-54 consumer of PR `#352`, in the branching form `T-91302`, states that

\[
 \mathfrak L_X=o(\log^2X)
 \Longrightarrow
 \mathrm{RH}.
 \tag{T-91546.14}
\]

Therefore the composition of the exact statements cited above would complete
the factor-54 proof route.

This section is a composition theorem, not an independent certification that
every imported producer statement has the identical normalization required by
the current live branch.

## 8. Required hostile audits before promotion

The following joints remain mandatory:

1. **Merged directed replay.** Re-run the survival and hazard target-Hall margins
   and normalized row inequalities after their transplant onto the current
   `P_61/P_79` parent tree.
2. **Affine normalization audit.** Check that the target-unit residual source
   coefficient in `L-91545` is exactly the coefficient lifted by `L-91318`, with
   no extra factor of `p^(+-1/2)`.
3. **Port ledger audit.** Reconstruct the target-null correction and prove that
   the common endpoint port is spent once after the two Hall networks are
   combined.
4. **Loss-definition audit.** Match the target-normalized typed loss of
   `T-91541` term for term to the native score-loss convention consumed by PR
   `#352`.
5. **Independent proof reconstruction.** A reviewer should rebuild
   (T-91546.4)--(T-91546.12) from the definitions, not from this theorem's prose.

A failure at any one of these joints retracts the candidate composition without
affecting the exact abstract lemmas `L-91540/L-91545`.

## 9. Boundary

```text
one-prime target/score binary telescope              EXACT
branch target-Hall positive residual sources          EXACT ABSTRACTLY
matched-edge target-null row bonuses                  EXACT ABSTRACTLY
all target-bearing children contract by 67            EXACT
child target weights sum <=1                          EXACT
actual-packet typed branching consumer                EXACT CONDITIONAL
complete factor-54 reset composition                  CANDIDATE / AUDIT REQUIRED
Riemann Hypothesis                                    UNPROVEN
```
