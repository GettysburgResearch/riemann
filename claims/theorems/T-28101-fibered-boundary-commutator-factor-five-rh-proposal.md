# T-28101 — Fibered boundary-commutator factor-five proposal for RH

Claim ID: `T-28101`  
Title: One fixed-source boundary-commutator factor-five certificate, lifted through the reciprocal-free top fiber, gives a subexponential top-source bound and proves the Riemann Hypothesis  
Status: **PROPOSED COMPLETE CONDITIONAL COMPOSITION — FIBERED TRANSITION THEOREM OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #281  
Dependencies: `R-28101`, `L-28101`--`L-28103`; PRs #241, #250, #263, #269  
Scope: conditional completion; RH is not claimed proved

## 1. Corrected input

Fix one packet order `K>=4` for which the complete non-top residual-depth and
terminal rows are Euler-small after source-bound partitioning.

For

\[
X=e^{J+O_K(1)},
\qquad
V=\lceil X^{1/K}\rceil,
\]

let

\[
T_{K,V}=\Lambda*r_V^{*(K-1)}
\]

be the complete top source.

By `R-28101`, the fixed-fraction radix of PR #266 produces no shifted top row
and is not used.

By `L-28101`, define instead

\[
S_{K,V}=\omega_2*H_{K,V}.
\]

The fixed dyadic filters give two-sided causal comparisons between the block
energies of `T_(K,V)` and `S_(K,V)` with constants independent of `J`.

## 2. Fibered Boundary-Commutator Factor-Five Transition

A **Fibered Boundary-Commutator Factor-Five Transition Certificate**,
`FBCF5TC(K,J)`, consists of the following exact data for the source
`S_(K,V)`.

### A. Complete source manifest

The object contains:

```text
all omega_2 anchor coordinates;
all H_(K,V) residual-fiber coordinates;
every product collision;
all parity and finite Bezout delays;
every compact-window, output, and ratio cell;
independent frequency variables t,s.
```

No fiber cross term may be discarded.

### B. Exact transverse/boundary split

The certificate emits

\[
\boxed{
I=P_{K,V}^{\rm trans}+B_{K,V}^{\rm fib}
}
\tag{T-28101.1}
\]

on the complete source span.

The transverse part is the pole-canceling carry-window sector. The boundary
part contains:

- the full unit-source fiber `H_(K,V)`;
- every block-cutoff commutator;
- every parity/Bezout endpoint;
- bottom charges `2,3`;
- the dyadic and `2/3` Mertens mutations;
- every noncoprime and small-row correction.

### C. Fibered transverse factor-five certificate

The fixed-source factor-five matrices of PR #269 are lifted through
`H_(K,V)` as full congruences. The object proves the complete physical/carry
transition LMIs and inherits the absolute carry reserve on the represented
transverse span.

The lift must use `L-28102`; rowwise scalar positivity is insufficient.

### D. Physical boundary reserve

Before entering the pure carry-window bank, the independent-frequency boundary
matrix is written as one full block LMI

\[
\mathsf A_{B,K,V,J}
-\kappa_0\mathsf G_{B,K,V,J}
\succeq0,
\qquad
\kappa_0>0,
\tag{T-28101.2}
\]

or as a recurrence-compatible directed enclosure with the same meaning.

The reserve may be obtained by lifting a fixed-source base certificate through
the common fiber. A proof object which first cancels the common zeta factor is
rejected.

### E. Boundary recurrence

The certificate proves

\[
\boxed{
E_{B,K}(J)
\le
C_K(1+J)^{A_K}
+
\sum_{\beta=1}^{R_K}
\vartheta_{K,\beta}
E_{B,K}(J-\delta_{K,\beta}),
}
\tag{T-28101.3}
\]

where

\[
\delta_{K,\beta}\ge\delta_K>0,
\qquad
\vartheta_{K,\beta}\ge0,
\qquad
\sum_\beta\vartheta_{K,\beta}\le1.
\tag{T-28101.4}
\]

A multiplicative strict-scale recurrence is also accepted.

Every delayed row is an exact source map, not merely a support label.

## 3. Why one fixed base certificate is enough

Suppose the fixed-source `omega_2` boundary/transverse theorem is exported as:

1. exact source maps which are linear over a common fiber;
2. full independent-frequency matrices;
3. full PSD or Schur LMIs;
4. explicit block commutator rows.

Then `L-28102` lifts every matrix inequality through `H_(K,V)` with the same
coercivity constant. The packet order introduces no new generalized-eigenvalue
loss.

Thus a proof-producing base `BCF5TC` object automatically supplies the
corresponding fibered object, provided the module-linearity and boundary
commutators are verified.

This is stronger than checking finitely many packet orders and weaker than an
ambient arbitrary-vector theorem.

## 4. Subexponential top-source energy

Equations (T-28101.3)--(T-28101.4) and elementary renewal induction give

\[
E_{B,K}(J)=e^{o_K(J)}.
\tag{T-28101.5}
\]

The transverse factor-five estimate and exact decomposition
(T-28101.1) then give

\[
E_{S,K}(J)=e^{o_K(J)}.
\tag{T-28101.6}
\]

The fixed stable filters of `L-28101` imply

\[
\boxed{
E_{T,K}(J)=e^{o_K(J)}.
}
\tag{T-28101.7}
\]

No `1/K` endpoint count or moving-order limit is used.

## 5. Complete source

The corrected finite inverse packet is

\[
Q_K=Q_K^{\rm top}+Q_K^{\rm non-top}.
\]

The source-bound higher-order Euler theorem gives

\[
E_K^{\rm non-top}(J)\le e^{-c_KJ}
\]

after retaining all cutoff and first-crossing rows. Combining with
(T-28101.7),

\[
\boxed{
E_K^{\rm complete}(J)=e^{o_K(J)}.
}
\tag{T-28101.8}
\]

The top source carries the same rightmost-zero exponent as the complete
fixed-logarithm Möbius signal. Therefore the safe-window Hardy/Mellin transfer
gives

\[
\Theta_\zeta=0.
\]

Functional-equation symmetry yields

\[
\boxed{\mathrm{RH}.}
\tag{T-28101.9}
\]

## 6. Scalar audit

The fixed dyadic filter retains the exact dyadic Mertens shell. The all-ratio
causal transfer then gives the `2/3` first Farey-cell increment.

Thus an accepted production object also yields

\[
M(x)-M(cx)=O_\varepsilon(x^{1/2+\varepsilon})
\]

for every fixed `0<c<1`, and hence the classical Mertens formulation of RH.

This is a mutation of the same source, not an additional assumption.

## 7. What has and has not been reduced

The previous `PADT` front line required, for every packet order:

```text
construct a signed top-source flow;
prove its two-frequency Transport Frame;
obtain eta_K -> 0.
```

The corrected front line is one fixed theorem:

```text
construct the independent-frequency
boundary-commutator factor-five certificate
for the fixed omega_2 source,
in a matrix form stable under common fibers.
```

If produced, it lifts to every top source automatically and proves RH already at
one fixed packet order.

The theorem remains RH-bearing and open. The reduction is credible because its
matrix, source, and boundary obligations are fixed rather than growing with
`K`.

## 8. Automatic rejection

Reject a claimed `FBCF5TC` if it:

- uses the vacuous fixed-fraction radix;
- omits a fiber collision or `h != h'` cross term;
- applies a scalar carry sign after multiplying by a signed fiber;
- uses pure carry-window coercivity as the RH-sensitive reserve;
- omits the unit-source fiber;
- treats a block cutoff as commuting without its commutator;
- lifts a Schur complement without lifting the full block LMI;
- loses the parity, dyadic shell, or `2/3` first-cell mutation;
- promotes finitely many numerical matrices to the cofinal theorem.

## 9. Proof boundary

Complete conditionally:

\[
\mathrm{FBCF5TC}(K)
\Longrightarrow
E_{\rm top}(J)=e^{o(J)}
\Longrightarrow
E_{\rm complete}(J)=e^{o(J)}
\Longrightarrow
\mathrm{RH}.
\]

Open:

- the fixed-source independent-frequency boundary/transverse decomposition;
- the physical boundary Schur reserve;
- the recurrence (T-28101.3);
- an unconditional proof of RH.
