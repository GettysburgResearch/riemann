# T-15603 — Positive-defect trace saturation gives the cofinal Weil floor

Claim ID: `T-15603`  
Title: Exact E-radicals plus certified line-cardinal radicals reduce the final positive path to one residual trace-tail inequality  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-o`  
Created: 2026-07-31  
Dependencies: `L-15613`, `L-15614`, `L-15607/L-15608`, `L-14308`, `T-14302`  
Scope: the corrected sufficient theorem for the requested `F_j -> 0^-` conclusion

## Setup

At support `a_j`, let `A_j` be the exact localized Weil operator.  Choose a
finite set `Z_j` of independently certified critical-line zeros and let

\[
 A_j^{[Z_j]}=A_j-Q_{Z_j,j}.
 \tag{T-15603.1}
\]

Assume a proof-grade symbol comparison

\[
 A_j\succeq G_jI-D_{j,G_j},
 \qquad
 D_{j,G_j}\succeq0,
 \tag{T-15603.2}
\]

and put

\[
 \widetilde D_j
 =
 D_{j,G_j}+Q_{Z_j,j}.
 \tag{T-15603.3}
\]

Let `L_j` be the localized truncation of a finite global packet contained in

\[
 \mathscr R_E+
 \operatorname{span}\{k_\gamma:\gamma\in Z_j\},
 \tag{T-15603.4}
\]

so that its ideal global form is radical for `Q_W^[Z_j]`.

Let `P_j` be the orthogonal projection onto `L_j`.  Suppose

\[
 \eta_j
 =
 \operatorname{Tr}\bigl((I-P_j)\widetilde D_j\bigr)
 <G_j,
 \tag{T-15603.5}
\]

and define

\[
 \Gamma_j=G_j-\eta_j>0.
 \tag{T-15603.6}
\]

Finally assume directed packet bounds

\[
 -\alpha_j H_j
 \preceq B_j^{[Z_j]}
 \preceq\alpha_jH_j,
 \tag{T-15603.7}
\]

\[
 R_j^{[Z_j]}\preceq\beta_j^2H_j.
 \tag{T-15603.8}
\]

## Conclusion

Then

\[
 A_j^{[Z_j]}|_{L_j^\perp}\succeq\Gamma_jI
 \tag{T-15603.9}
\]

and the block Schur theorem gives

\[
 \boxed{
 A_j^{[Z_j]}
 \succeq
 -\left(
   \alpha_j+\frac{\beta_j^2}{\Gamma_j}
  \right)I.
 }
 \tag{T-15603.10}
\]

Since `Q_(Z_j,j)` is positive,

\[
 \boxed{
 A_j
 \succeq
 -\left(
   \alpha_j+\frac{\beta_j^2}{\Gamma_j}
  \right)I.
 }
 \tag{T-15603.11}
\]

Therefore, if

\[
 \boxed{
 \alpha_j+
 \frac{\beta_j^2}{G_j-\eta_j}
 \longrightarrow0,
 }
 \tag{T-15603.12}
\]

then the whole-operator floors satisfy

\[
 \boxed{
 F_j\ge-\varepsilon_j,
 \qquad
 \varepsilon_j\longrightarrow0.
 }
 \tag{T-15603.13}
\]

The cofinal lower-envelope theorem `T-14302` then implies RH.

## Clean sufficient schedule

It is enough to prove

\[
 \boxed{
 \eta_j\le\frac{G_j}{2},
 \qquad
 \alpha_j\to0,
 \qquad
 \frac{\beta_j^2}{G_j}\to0.
 }
 \tag{T-15603.14}
\]

Indeed, `Gamma_j>=G_j/2` and

\[
 \boxed{
 F_j
 \ge
 -\alpha_j
 -2\frac{\beta_j^2}{G_j}.
 }
 \tag{T-15603.15}
\]

## What this theorem resolves

The finite evaluation-visible block arising from already certified line zeros
is no longer an independent positivity obligation.  Its exact cardinal
correctors are residual radicals after positive zero deflation, and their
localization errors enter only through `alpha_j` and `beta_j`.

The unresolved trace packet is therefore the **positive defect packet**

```text
exact E-range radicals
+ certified critical-line cardinal radicals.
```

## Exact remaining statement

A full proof still requires a cofinal sequence for which this positive defect
packet captures the weighted deficit:

\[
 \boxed{
 \operatorname{Tr}
 \bigl((I-P_{L_j})\widetilde D_j\bigr)
 \le\frac{G_j}{2},
 }
 \tag{T-15603.16}
\]

while its growing tail-synthesis bounds satisfy the last two limits in
(T-15603.14).

`R-15602` proves that a generic `L2` density theorem cannot establish
(T-15603.16) together with the tail limits in the presence of an off-line
cardinal defect.  Thus (T-15603.16) is the exact remaining RH-bearing
statement, not a missing finite-dimensional algebra identity.

## Proof boundary

- All listed zeros and multiplicities must be independently proof-grade.
- The complete symbol comparison and every trace endpoint must be directed.
- Growing-packet tail control must be an operator/synthesis bound, not
  entrywise convergence.
- The theorem is conditional on (T-15603.12) or (T-15603.14); those cofinal
  estimates are not proved here.
- No proof of RH is claimed by this theorem card alone.
