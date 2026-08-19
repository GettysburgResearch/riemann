# L-99121 — Score, capacity and provenance commute with the resolved tree

Claim ID: `L-99121`  
Status: **PROVED EXACT COROLLARY; APPLICATION INPUTS REQUIRE REVIEW**  
Created: 2026-08-19  
Depends on: `L-99120`; local identities of PR #620

Assume the compact Hall and causal identities of PR #620 hold in every physical
component row before endpoint integration. Integrate the labelled fields and
form the nilpotent operator `T_X` and current map `J_X` of `L-99120`.

Then the complete all-depth ideal row satisfies

\[
D_X^{\rm ideal}=E_X^{\rm eq}
\]

in every physical row coordinate. In particular, if the equality endpoint
frame has

\[
\mathcal H(E_X^{\rm eq})=4\sqrt X,
\]

then

\[
\boxed{
\mathcal H(D_X^{\rm ideal})=4\sqrt X.
}
\tag{L-99121.1}
\]

This equality uses only the physical row identity. It does not require:

- assigning a declared score to the Hall bonus;
- charging one score debt per generation;
- comparing a signed source score with an unsigned source mass;
- an infinite convergence argument.

Let `O_X` be one positive top/anchored omission and apply one common scalar
thinning

\[
\tau_K=\frac{\sqrt K}{\sqrt K+24},
\qquad K=\lfloor X/67\rfloor+1.
\]

For

\[
d_X=\tau_K(D_X^{\rm ideal}-O_X),
\]

linearity gives

\[
\mathcal H(d_X)
=\tau_K[4\sqrt X-\mathcal H(O_X)].
\]

Since `K>X/67`,

\[
4\sqrt X(1-\tau_K)<96\sqrt{67}.
\]

Thus any absolute top-score bound `C_top` gives

\[
\boxed{
\mathcal H(d_X)
\ge4\sqrt X-(96\sqrt{67}+C_{\rm top}).
}
\tag{L-99121.2}
\]

All ordinary and detail capacities are evaluated on this same final row. A
common positive restriction, omission or cubature applied after resolution
commutes with the exact identities. Source provenance is retained because every
child label occurs in one direct-sum summand and the row-only Hall sort never
enters `T_X`.

The local Hall, profile-monotonicity, direct-integral and all-column estimates
remain the load-bearing application inputs. This corollary removes only the
all-depth score/composition interface.
