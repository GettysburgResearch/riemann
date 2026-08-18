# T-97900 — After Dickman localization, only the subpower least-prime critical core remains

Claim ID: `T-97900`  
Status: **UNCONDITIONAL REDUCTION; SUBPOWER CORE OPEN / RH-BEARING**  
Created: 2026-08-18  
Depends on: PR #593, PR #594, `L-97900`--`L-97902`  
RH status: **unproved**

The factor-67 state portfolio now has three exact regions.

1. Every threshold split retains the full native coefficient and the
   `(R-A)F` residual (PR #593).
2. Every subcritical count-depth stopping current is eventually negative
   (PRs #593/#594).
3. Every state whose least allowed rough prime satisfies

\[
p_0\ge Y^\theta
\]

for one fixed `theta>0` is eventually positive, with the uniform asymptotic

\[
\mathcal F(Y,p_0)
=a\sqrt Y\,
\mathfrak D\!\left(\frac{\log Y}{\log p_0}\right)
+o_\theta(\sqrt Y).
\tag{T-97900.1}
\]

Consequently, if state-wise RBLPTE fails along a sequence `(Y_n,p_n)`, then

\[
\boxed{
\frac{\log p_n}{\log Y_n}\longrightarrow0.
}
\tag{T-97900.2}
\]

In words: every counterexample must lie in the **subpower least-prime core**.
Combining this with the subcritical-depth no-go places the unresolved source in
the genuine rough harmonic saddle, not in a terminal power-scale sector and not
on a shallow stopping line.

The same localization applies to `CSHT67`: all fixed power-scale states are
already closed at the conclusion-producing scalar coordinate, so a full
all-coordinate transport is needed only, if at all, in the subpower critical
core. It remains stronger than the minimal root obligation.

Define `SPCC67` (Subpower Critical Core, factor 67) to be eventual
nonnegativity of the native scalar restricted to state sequences satisfying

\[
\log p_0=o(\log Y)
\]

with rough depth in the harmonic-saddle range. Then the exact implication is

\[
\boxed{
\mathrm{SPCC}_{67}\Longrightarrow
\mathrm{RBLPTE}_{67}\Longrightarrow
\text{eventual annular }5{:}3\text{ positivity}\Longrightarrow\mathrm{RH}.
}
\tag{T-97900.3}
\]

`SPCC67`, `RBLPTE67`, and full `CSHT67` are not proved here. The new theorem is
that no fixed-power terminal state can carry the obstruction.

```text
Dickman simplex identity                     PROVED EXACT
all fixed power-scale states                 PROVED POSITIVE
state-wise RBLPTE on those states            PROVED
scalar one-use transport on those states     PROVED
full target-preserving CSHT on those states  NOT CLAIMED
subpower critical core SPCC67                OPEN / RH-BEARING
root RBLPTE67                                OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
