# T-19814 — The complete affine hybrid gate directly implies RH

Claim ID: `T-19814`  
Status: **PROVED IMPLICATION; THE AFFINE GATE ITSELF REMAINS UNPROVED**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-07  
Dependencies: `R-19846`, Xi-cardinal theorem `L-15613`, exact hybrid residual hierarchy `L-19862`  
Scope: final logical classification of `T-19813`

## Statement

Let `V_j`, `p_j`, `A_j`, and `D_j` be the exact finite spaces, normalized Xi
targets, exact finite Weil matrices, and exact hybrid residual Grams of
`T-19813`.  Assume:

1. the finite spaces are cofinal and dense in the common Hardy/form topology;
2. the Xi target residual satisfies
   \[
   m_j=D_j(p_j,p_j)\to0,
   \qquad
   A_j(p_j,p_j)\to0;
   \]
3. the hybrid complement obeys
   \[
   D_j|_{p_j^\perp}\succeq I;
   \]
4. there are real `sigma_j`, positive `c_j`, and positive `C_j` such that
   \[
   A_j-\sigma_jI\succeq c_jD_j,
   \]
   \[
   A_j(p_j,p_j)-\sigma_j
   \le C_jc_jm_j,
   \qquad C_jm_j\to0.
   \]

Then the Riemann hypothesis is true.

## Proof

If RH were false, `L-15613` supplies a nonreal zero `omega` and a Hardy/form
vector `h_omega` with strictly negative Weil value.  Subtracting its ordinary
projection onto the exact Xi radical preserves its Weil value and makes it
orthogonal to the limiting Xi target.  Cofinal finite approximation and target
orthogonalization give unit vectors

\[
 u_j\in V_j\cap p_j^\perp
\]

and one constant `kappa>0` such that

\[
 A_j(u_j,u_j)\le-\kappa
\]

for all sufficiently large `j`.  The residual complement floor gives

\[
 D_j(u_j,u_j)\ge1.
\]

The affine lower bound then forces

\[
 -\sigma_j\ge c_j+\kappa.
\]

Since `A_j(p_j,p_j)->0`, eventually

\[
 A_j(p_j,p_j)-\sigma_j
 \ge c_j+\kappa/2.
\]

The target upper bound gives instead

\[
 A_j(p_j,p_j)-\sigma_j
 \le c_j(C_jm_j)=o(c_j).
\]

If `c_j` is bounded along a subsequence, the fixed `kappa/2` is impossible; if
`c_j` is unbounded, division by `c_j` gives `1<=o(1)`.  This contradiction
excludes every off-line zero.  Hence RH holds.  QED.

## Consequence

The finite real-zero theorem and Hurwitz conclusion of `T-19813` are not needed
for the bare implication above.  They remain a useful second endpoint if one
constructs the affine inequalities by an independent source-specific argument.

The status of the programme is therefore:

```text
hybrid source reservoir and residual gap     constructed
abstract affine spectral theorem              proved
complete affine source-specific inequality    unproved and RH-bearing
T-19813 as a completed proof                   GAPS/BLOCKED
RH                                             unproved
```

A proof of the affine gate from the prime/pole/archimedean formula would be a
valid proof of RH.  The theorem merely prevents that gate from being classified
as a routine final normalization or support-average estimate.
