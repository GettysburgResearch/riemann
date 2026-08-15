# L-91821 — Whole-cell integration followed by one anchored labelled quantizer gives one nonnegative common-parent row

Claim ID: `L-91821`  
Status: **PROPOSED COMPLETE PHYSICAL REALIZATION THEOREM ON FROZEN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91820`, `L-91754`, `L-91110`, `L-91733`, frozen finite anchored packets  
RH status: **unproved**

## 1. Retained whole cells

For integer `X` put

\[
 K=\left\lfloor\frac X{67}\right\rfloor+1,
 \qquad W=10000.
\]

Remove the literal positive bottom strip, fixed top strip and the finitely many declared activation collars.  The retained parameter set is a disjoint finite union

\[
 I_X=\bigsqcup_{a=1}^{N_X}I_a
\tag{L-91821.1}
\]

of complete activation cells.  On every `I_a` the active source list and every source, Hall, rough-owner and inner-colour label are fixed.

The positive equality endpoint measure is

\[
 d\nu_X(s)=\frac{2L(X/s)}s\,ds,
 \qquad L(X/s)>0
\tag{L-91821.2}
\]

throughout the factor-67 window.

## 2. Exact labelled direct integral

Let `mathfrak p_s` be the positive labelled fibre of `L-91820`.  Define

\[
\boxed{
 \mathfrak P_X^{\rm cont}
 =
 \bigoplus_{a=1}^{N_X}
 \int_{I_a}\mathfrak p_s\,d\nu_X(s)
 \ge0.
}
\tag{L-91821.3}
\]

Tonelli applies because every summand is nonnegative and the fibre has only finitely many active compact labels at each `s`.  Integration preserves the exact all-coordinate fibre equality and source ownership.

All colours are retained inside the direct integral.  In particular no child is physically quantized in a separate pass.

## 3. Anchored finite block and bulk block

The complete native parent has two disjoint positive sectors.

```text
anchored finite sector:
    exact finite bottom/base packets and any finite source block declared to
    remain discrete;

continuum bulk sector:
    the whole-cell direct integral (L-91821.3).
```

Write

\[
 \mathfrak P_X^{\rm parent}
 =
 \mathfrak P_X^{\rm anc}
 \oplus
 \mathfrak P_X^{\rm cont}.
\tag{L-91821.4}
\]

The anchored sector is already a finite positive endpoint packet in the native normalization.  It must not be continuumized and therefore incurs no finite/continuum discrepancy.

## 4. One labelled quantizer

Let `Q_{X,\rm bulk}^{\rm lbl}` be the positive martingale B-spline quantizer of frozen `L-91110`, applied to the complete labelled bulk measure.  It preserves all labels internally, uses one common barycentric kernel, and moves target, score, every row, ordinary responses and radix-four responses together.

Define the sole physical quantizer by

\[
\boxed{
 Q_X^{\rm lbl}
 =I_{\rm anc}\oplus Q_{X,\rm bulk}^{\rm lbl}.
}
\tag{L-91821.5}
\]

Here `I_anc` is literally the identity on the anchored finite block.  Thus:

1. every anchored packet has exactly its native ordinary and radix-four responses;
2. every finite/continuum and collar comparison belongs to the bulk block;
3. there is one quantizer, not one per Hall edge, rough owner, current colour or child colour.

The output

\[
 \widetilde d_X
 =\pi Q_X^{\rm lbl}\mathfrak P_X^{\rm parent}
\tag{L-91821.6}
\]

is coefficientwise nonnegative.

## 5. One common source thinning

Apply once, before forgetting labels, the scalar

\[
\boxed{
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
}
\tag{L-91821.7}
\]

The final physical row is

\[
\boxed{
 d_X=\tau_K\widetilde d_X\ge0.
}
\tag{L-91821.8}

The removed fraction `1-tau_K` is literal unused positive source.  It is neither signed correction nor recursive child.  Because the same scalar acts once on the complete labelled parent, it preserves every exact source coefficient and the recursive mass bound below `1/8`.

## 6. One aggregate port

All Hall edges, rough owners and inner colours are summed before any root-global port is formed.  In the preferred zero-port specialization the auxiliary port is identically zero.  More generally, only one current-owned aggregate port coordinate is allowed.  Every child-colour port coordinate is zero.

No port is charged per leaf or child.

## 7. Signed comparison is declared after realization

Let `Gamma` denote the ordinary response map and `Xi` the radix-four response map.  The finite/continuum mismatch, B-spline collar, retained-cell interpolation and terminal comparison are recorded only through the differences between the ideal native capacities and

\[
 \Gamma(d_X),
 \qquad
 \Xi(d_X).
\]

They are not stages of (L-91821.3)–(L-91821.8).  `L-91822` proves directly that the resulting complements are nonnegative.

## 8. Source ownership audit

Every original positive source occurrence has exactly one terminal path:

```text
unused bottom/top/collar omission;
anchored finite identity block;
or retained whole cell
 -> one Hall residual/edge
 -> one least rough owner
 -> one inner colour
 -> one common thinning
 -> one labelled bulk endpoint state.
```

The outgoing nonnegative weights sum to the incoming weight at every positive split.  No source mass is copied.

## 9. Boundary

```text
positive whole-cell direct integral               exact
anchored finite identity block                     exact
one labelled global quantizer                      exact
one common source thinning                         exact
nonnegative physical row                           exact
separate child quantizer/correction                 absent
signed comparison in source telescope              forbidden
all-column feasibility and complements             next lemma
Riemann Hypothesis                                 unproved
```
