# L-91763 — The explicit Volterra parent instantiates the positive source ledger while mismatch remains signed observation

Claim ID: `L-91763`  
Status: **PROPOSED EXACT COMPOSITION INTERFACE ON FROZEN CAUSAL INPUTS — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Authoring agent: `gpt56-pro`  
Depends on: `L-91650/L-91654/L-91658/L-91694`; `L-91760--L-91762`; two-ledger theorem `L-92900`  
RH status: **unproved at this claim**

## 1. Positive labelled parent

On the retained whole-cell interval

\[
 I_X=[K+2,X-W-2],
 \qquad K=\lfloor X/67\rfloor+1,
\]

`L-91762` constructs the explicit positive measure

\[
 d\mathcal M_X(S)
 =\frac{2L(X/S)}S P_S^{\rm rough}\,dS,
 \qquad
 P_S^{\rm rough}
 =\sum_{m\in\mathcal R_{67},\,m\le S}
  m^{-1/2}U_mp_{S/m}\ge0.
\tag{L-91763.1}
\]

Every fibre has the product label

```text
parent endpoint / residual small-divisor colour / first rough owner / history.
```

The rank-one coupling of `L-91761` makes the small-divisor coordinate a literal positive source partition.  The first-owner partition of `L-91688` makes the rough coordinate disjoint and exhaustive.

## 2. Causal generators are positive source-cone atoms

For each positive labelled fibre packet `P`, use the frozen causal identity

\[
 P=P^{\rm cur}+\sum_i\alpha_iU_{p_i}P_i,
\tag{L-91763.2}
\]

where the current part is the positive sum of the causal generators

\[
 P-r_iU_{p_i}P_i
\]

with nonnegative outer coefficients, and

\[
 \alpha_i\ge0,
 \qquad
 \sum_i\alpha_i<\frac18.
\tag{L-91763.3}
\]

Here a causal generator is one atom of the positive **typed** source cone: its observation is the already-proved nonnegative physical row/capacity packet of `L-91654`, and its ownership record contains the parent occurrence and the unique paired child occurrence.  Equation (L-91650) proves that these ownership coefficients spend the parent exactly once.  No signed finite/continuum defect is part of this source atom.

## 3. Positive integration and actual target-mass normalization

Integrate (L-91763.2) against (L-91763.1).  Tonelli gives one exact positive source ledger

\[
\boxed{
 P_X^{\rm src}
 =C_X^{\rm src}
  +\sum_b\beta_bU_bP_b^{\rm src}
  +U_X^{\rm src},
}
\tag{L-91763.4}

where `U_X^src` consists only of literal positive restrictions, omissions and thinning.  Grouping by provenance labels and normalizing by actual child target masses gives, by `L-91694`,

\[
 \boxed{
 \beta_b\ge0,
 \qquad
 \sum_b\beta_b<\frac18.
 }
\tag{L-91763.5}

Every original labelled occurrence belongs to one current generator, one child, or one unused positive packet.

## 4. Signed comparison is a second ledger

The exact finite relation is

\[
 D_{P,X}=\overline D_{P,X}+E_{P,X}^{\rm row}
\tag{L-91763.6}

from `L-91762`.  The aggregate mismatch, martingale collar and physical response corrections are therefore recorded as one signed observation vector

\[
 e_X\in V,
\tag{L-91763.7}

not as positive source.  Positive omissions and thinning produce an observed unused-capacity vector

\[
 u_X=\mathcal A(U_X^{\rm src})\ge0.
\tag{L-91763.8}

The all-column and terminal estimates are exactly the separate inequality

\[
 e_X(q)\le u_X(q)
 \qquad(q\ge2).
\tag{L-91763.9}

Define

\[
 r_X=u_X-e_X\ge0.
\tag{L-91763.10}

Then the abstract two-ledger theorem `L-92900` gives the realized identity

\[
\boxed{
 \Omega_X
 =\Xi(d_X^{\rm cur})
  +r_X
  +\sum_b\beta_bU_b\Omega(P_b).
}
\tag{L-91763.11}

This identity uses source positivity only in (L-91763.4) and capacity domination only in (L-91763.9); it never relabels the signed mismatch as source.

## 5. Relation to the independent review

The independent review of PR #488 requested one concrete derivation of the positive common-parent endpoint packet from the signed native arithmetic datum.  `L-91760--L-91762` give that packet and its exact finite mismatch.  Equations (L-91763.2)--(L-91763.11) place it in the corrected two-ledger composition of PR #493.

Thus the formerly abstract antecedent of `L-92900` is reduced to the already-frozen analytic statements:

```text
positive physical causal-generator theorem;
whole-cell all-column mismatch/collar domination;
terminal comparison and omissions;
one common quantizer;
actual-target-mass direct-integral normalization.
```

## 6. Boundary

```text
explicit positive Volterra common parent             L-91760--L-91762
rank-one root source ownership                       exact
rough first ownership                                exact
causal generator as positive typed source atom       frozen exact input
positive integrated source ledger                    exact on frozen input
signed mismatch kept outside source cone             exact
actual-mass child coefficients sum below one eighth  exact / L-91694
all-column domination e_X<=u_X                       frozen analytic input
realized native residual r_X>=0                      exact after domination
Riemann Hypothesis                                   unproved
```
