# L-91861 — Whole-cell restriction and one block realization produce one row from the two-sorted Hall fibre

Claim ID: `L-91861`  
Status: **PROPOSED COMPLETE COMMON-ROW REALIZATION THEOREM ON FROZEN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91860`; frozen `L-91754`, `L-91110`, `L-91658`, `L-91733`; comparison with PR #500 `L-91850--L-91852`  
RH status: **unproved**

## 1. Restrict before Hall

For integer `X`, put

\[
K=\left\lfloor\frac X{67}\right\rfloor+1,
\qquad W=10000.
\]

Use the tagged disjoint endpoint target

\[
\mathcal T_X=\coprod_{n=K+2}^{X-W-3}\{n\}\times[0,1).
\tag{L-91861.1}
\]

Bottom, top, and any declared exceptional cells are removed at this tagged-source level **before** Hall. Therefore the residual-source and row-bonus channels are removed together on exactly the same fibres. No partial-cell boundary atom is created.

## 2. Integrate the two sorts over the same cells

Let `(C_s,B_s)` be the two-sorted fibre of `L-91860`, with `C_s` the target-bearing positive residual source after its rough/causal labels are attached and `B_s` the direct nonnegative Hall-bonus row. Against the positive endpoint density, define

\[
C_X^{\rm bulk}=\int_{\mathcal T_X}C_s\,d\nu_X(s),
\qquad
B_X=\int_{\mathcal T_X}B_s\,d\nu_X(s).
\tag{L-91861.2}
\]

Tonelli gives `C_X^bulk>=0` in the source cone and `B_X>=0` coefficientwise in the row cone. The exact component-row identity is

\[
R_X^{\rm retained}=R(C_X^{\rm bulk})+B_X.
\tag{L-91861.3}
\]

Only `C_X^bulk` is passed through rough ownership, internal same-index child placement, and the endpoint B-spline block. The bonus row has already reached the physical row coordinate. Target exactness of the Hall residual is load-bearing here: at each fibre it carries the complete positive signed target `L(x)`, while the bonus carries target zero. After the stochastic causal split, the aggregate target density entering the bulk quantizer is therefore exactly the frozen equality endpoint density, not an unspecified larger measure.

## 3. Internal child placement

For every residual-source child colour `b`, let `U_b` be its positive same-index physical placement. All children are placed before labels are erased. Let

\[
C_X^{\rm placed}
=C_X^{\rm cur}\oplus\bigoplus_b\alpha_bU_bC_b.
\tag{L-91861.4}
\]

The source identity and every linear row/response observation remain exact. No child is exported for a second Hall operation or a second quantizer.

## 4. One block realization operator

Let `A_X` be the exact anchored finite row sector. Define one realization operator on the direct sum of the three actual domains:

\[
\boxed{
\mathcal Q_X^{(2)}
=I_{\rm anc}\oplus I_{\rm bonus}\oplus Q_{X,\rm bulk}^{\rm lbl}.
}
\tag{L-91861.5}
\]

Here:

```text
I_anc       is the identity on exact finite anchored rows;
I_bonus     is the identity on the integrated Hall-bonus row B_X;
Q_bulk^lbl  is one label-blind positive martingale kernel on the complete
            residual-source/current/child bulk.
```

This is one block operator applied once. It is not a family indexed by Hall edge, rough owner, or child colour.

The unthinned row is

\[
\widetilde d_X
=I_{\rm anc}A_X+I_{\rm bonus}B_X
 +\pi Q_{X,\rm bulk}^{\rm lbl}C_X^{\rm placed}
\ge0.
\tag{L-91861.6}
\]

Apply the single scalar

\[
\tau_K=\frac{\sqrt K}{\sqrt K+130}
\]

to the entire sum:

\[
\boxed{d_X=\tau_K\widetilde d_X\ge0.}
\tag{L-91861.7}
\]

Thus anchored rows, Hall bonuses, causal currents, and internal child rows are all parts of one realized row and share one thinning coefficient.

## 5. Exact discrepancy support

The identity channels have no finite/continuum discrepancy. Therefore

\[
\text{ideal total row}-\text{realized total row}
\]

takes its nontrivial quadrature/collar contribution only from the bulk block. In particular the direct Hall bonus occurs identically on both sides and cancels from the comparison.

The positive collar formula is linear in the bulk endpoint density. By target exactness, the Hall residual carries exactly the frozen positive equality density; the stochastic causal split and same-index placements partition that density without changing its aggregate target marginal. Hence the frozen collar and all-column absolute bounds apply to this bulk with the same constants. No estimate is transferred from an unrelated source measure.

## 6. One row identifier

The construction has one immutable physical identifier

\[
\operatorname{rid}_X=(X,\mathcal T_X,\mathcal Q_X^{(2)},\tau_K).
\]

The following all carry this same identifier:

```text
cell restriction;
Hall residual and bonus;
rough ownership and internal children;
block realization;
common thinning;
finite/continuum comparison;
terminal comparison;
ordinary/detail complements;
Y4 pricing.
```

No theorem below changes the row while retaining an old comparison or slack vector.

## 7. Boundary

```text
restriction before Hall                         exact
residual source and bonus use same retained cells exact
bonus row identity channel                      exact
one bulk quantizer                              exact
one block realization and one thinning          exact
internal child family                           physically inserted / not exported
comparison belongs to same row                  exact by row identifier
all-column capacity                             next lemma
Riemann Hypothesis                              unproved
```
