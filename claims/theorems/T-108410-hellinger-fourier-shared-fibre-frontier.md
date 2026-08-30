# T-108410 — Hellinger–Fourier shared-fibre frontier

Claim ID: `T-108410`  
Status: **EXACT NONLINEAR-TO-SPECTRAL REDUCTION; LIVE ARITHMETIC ESTIMATE AND RH OPEN**  
Created: 2026-08-31  
Base: PR #778 at `f690b8f921e4c53e203dbd3aa7e9bd76d36cc0b5`  
Sibling inputs: PR #771 at `bffe68cec24fd785f7b16087d6ce8fea4561eece`; PR #774 at `abe712bdeca0968167f6decc2fbc0651fdd73592`  
RH/GRH status: **unproved**

PR #778 reduced the complete positive fixed-fibre Wick trace to the Hellinger
distance between the live occupancy and an orbitwise Frobenius comparator.
`L-108410--L-108412` now convert that nonlinear distance into literal
nonprincipal character energies.

For each grouped source-authorized rectangular fibre `iota`, let

\[
\mathcal V_{L,\iota}
={1\over L_\iota^2}
\sum_{\chi\ne1}
|\widehat l_\iota(\chi)|^2,
\qquad
\mathcal V_{R,\iota}
={1\over R_\iota^2}
\sum_{\psi\ne1}
|\widehat r_\iota(\psi)|^2.
\]

Let `B_mask(X)` be the positive-trace payment obtained from
`L-108410.6` for the exact live-mask completion boundary. Define

\[
\boxed{
\mathfrak V_{\rm occ}(X)
=
2\sum_\iota
N_\iota
\sqrt{
\mathcal V_{L,\iota}+
\mathcal V_{R,\iota}}
+
\mathfrak B_{\rm mask}(X).
}
\tag{T-108410.1}
\]

Then

\[
\boxed{
\mathfrak V_{\rm occ}(X)=X^{o(1)}
\Longrightarrow
\mathrm{FROBHELL}_{108400}.
}
\tag{T-108410.2}
\]

Name the premise in (T-108410.2)

```text
FROBSPEC108410.
```

## Exact character ledger

For the physical squareclass map `(x,y)->x*y^2`, every output coefficient is

\[
\widehat A(\chi)\widehat B(\chi^2).
\]

Thus the complete character energy splits exactly into:

```text
nonresonant reduced-Kummer modes;
the at-most-three quadratic/constant resonance rows;
principal and endpoint binding;
exact live-mask boundary.
```

The complete deep nonresonant function-field sector remains closed by PR
#771 at its stated normalized source scope. No family-size or atom-multiplicity
factor is introduced by the new bridge.

The number-field conclusion-facing chain is now

\[
\boxed{
\mathrm{FROBSPEC}_{108410}
\wedge
\mathrm{QRESBIND}_{107300}
\Longrightarrow
\mathrm{FROBHELL}_{108400}
\wedge
\mathrm{QRESBIND}_{107300}
\Longrightarrow
\mathrm{LIVEBOUND}_{107301}
\Longrightarrow
\mathrm{CBKM}_{106130}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-108410.3}
\]

## What has changed

The first live theorem is no longer phrased as an abstract Hellinger estimate.
It is the weighted sum of two one-sided multiplicative-character variances,
plus an explicit `L^1` mask boundary and finitely many resonance rows.

`R-108410` shows that a max-character estimate alone is insufficient: many
small modes can retain a positive Hellinger debt. The complete spectral sum or
a source `L^2` theorem is load-bearing.

```text
Hellinger chi-square/Fourier majorant     PROVED EXACT
twisted squareclass character ledger     PROVED EXACT
rectangular one-sided spectral reduction PROVED EXACT
live-mask L1 transfer                     PROVED EXACT
FROBSPEC108410                            OPEN
QRESBIND107300                            OPEN
RH / GRH                                  UNPROVED
```
