# L-91850 — A Hall–causal physical coupling compiles source ownership into one output row

Claim ID: `L-91850`  
Status: **PROVED EXACT ABSTRACT COUPLING THEOREM**  
Created: 2026-08-15  
Corrects: the output-marginal/source-marginal type gap isolated by `R-91850`  
RH status: **unproved**

## 1. Fiber data

Let `(S,lambda)` be a finite positive endpoint-parameter space. On each fiber `s`, let `E_s` and `O_s` be positive measures in target-mass units on finite even and odd source labels. Let `pi_s(do,de)>=0` be a measurable Hall coupling with

\[
 (\pi_s)_O=O_s,\qquad (\pi_s)_E\le E_s.
\tag{L-91850.1}
\]

Put

\[
 R_s=E_s-(\pi_s)_E\ge0.
\tag{L-91850.2}
\]

Thus every odd demand is used exactly once and every even capacity is split exactly between one Hall edge and residual source.

For each declared physical row coordinate `j`, let `rho_(s,j)` be the target-normalized row profile. Assume

\[
 \pi_s(o,e)>0\Longrightarrow
 \rho_{s,j}(e)\ge\rho_{s,j}(o)
\tag{L-91850.3}
\]

for every `j`.

## 2. Positive Hall output

Define the residual and edge-bonus rows

\[
 H_s^{\rm res}(j)=\int\rho_{s,j}(e)dR_s(e),
\]

\[
 H_s^{\rm bon}(j)=
 \iint[\rho_{s,j}(e)-\rho_{s,j}(o)]d\pi_s(o,e)\ge0.
\]

The two marginal identities give

\[
 \boxed{
 H_s^{\rm res}(j)+H_s^{\rm bon}(j)
 =\int\rho_{s,j}(e)dE_s(e)-
  \int\rho_{s,j}(o)dO_s(o).
 }
\tag{L-91850.4}
\]

This is the signed arithmetic row represented by positive physical outputs, while retaining both source marginals.

## 3. Causal and child placement kernel

Let the residual source carry a positive stochastic kernel `C_s(da|e)` into current and child labels `a`. For every child label let `P_(a,s)(dt)` be a positive same-index physical placement kernel. Hall bonuses have the distinguished current label and use their own positive placement.

Put

\[
 K_s(da,dt|e)=C_s(da|e)P_{a,s}(dt),
\tag{L-91850.5}
\]

and require

\[
 \sum_a C_s(a|e)=1,
 \qquad
 \int P_{a,s}(dt)=1.
\tag{L-91850.6}
\]

A first-owner restriction is part of `C_s`, not merely metadata. Hence one rough monomial cannot enter two child labels.

## 4. One label-blind quantizer

Let `Q_X(dj|t)` be one positive Markov kernel from the common physical target to finite row indices. It may depend on `t`, but not on the source label, Hall edge, current/child label or rough owner:

\[
 \sum_jQ_X(j|t)=1.
\tag{L-91850.7}
\]

The retained physical coupling is obtained by composing `pi_s`, `R_s`, `C_s`, `P_(a,s)` and `Q_X`, and then integrating in `s`. Its output marginal is one nonnegative row `d_X`.

## 5. Exact ownership identities

Before scalar thinning, the coupling has the exact input marginal laws

\[
 \boxed{
 \text{odd edge marginal}=O_s,
 \qquad
 \text{even edge marginal}+R_s=E_s.
 }
\tag{L-91850.8}
\]

After a common factor `tau in [0,1]`, introduce explicit discard measures

\[
 D_s^E=(1-\tau)E_s,
 \qquad
 D_s^O=(1-\tau)O_s.
\tag{L-91850.9}
\]

Then retained plus discarded input mass equals the original input mass in both marginals. No source occurrence disappears and no discarded mass is assigned to a child.

## 6. Linear observations

For every nonnegative linear observation `L` on finite rows, Tonelli gives

\[
 L(d_X)=
 \tau\int_S L\bigl(\text{quantized Hall residual + bonus}\bigr)d\lambda(s).
\tag{L-91850.10}
\]

Ordinary response is evaluated at `q` and `4q` separately; radix-four detail is formed only afterward. Label erasure therefore commutes with all declared linear observations.

## 7. Signed finite comparison is a second ledger

A finite/continuum comparison vector `e_X` belongs to the observation space and may be signed. It is not promoted to positive source. If positive unused native capacity `u_X` from thinning and omission satisfies

\[
 e_X(q)\le u_X(q)\quad(q\ge2),
\]

then

\[
 r_X=u_X-e_X\ge0
\]

is the physical capacity slack. Equality comes from the source/output identity; positivity comes from the all-column comparison. These are separate statements.

## 8. Boundary

```text
odd Hall demand used once                  exact marginal
matched plus residual even capacity        exact marginal
rough child first owner                    part of the kernel
child physical placement                   positive / explicit
one global quantizer                       label-blind Markov kernel
output row                                 one positive marginal
signed finite comparison                   separate observation ledger
source positivity of comparison            not asserted
Riemann Hypothesis                         unproved
```
