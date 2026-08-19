# L-99212 — Direct integration removes the samplewise integral-leaf obligation

Claim ID: `L-99212`  
Status: **PROPOSED COMPLETE EXACT REALIZATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Depends on: `L-99211`, fixed-row positivity consumer `L-96000/L-96001`  
RH status: **not assumed**

At fixed endpoint `X`, the native physical object is a finite real vector

\[
 d_X=(d_X(j))_{2\le j\le X}\in\mathbb R_+^{X-1}.
\]

The random key of `L-99211` is a source coordinate, not an instruction to
select one leaf and discard the rest. Define

\[
 d_X(j)=\int R_j(\omega,u)\,d\mu_X(\omega,u).
\tag{L-99212.1}
\]

The row index set is finite and the integrand is nonnegative, so this is already
one finite-support physical row. No rounding theorem is needed.

Every component coordinate and every fixed-row Mellin input is linear on the
aggregate row. Finite Fubini evaluates them exactly after integration. An
arbitrary score half-space can destroy total unimodularity of an integer flow
polytope, but it cannot obstruct (L-99212.1), because no sampled integer leaf is
the conclusion-producing proof object.

The integral Hall-polymatroid theorem of PR #632 remains correct at network
scope and is stronger than needed here. The expectation-only-rounding firewall
also remains correct but is inapplicable: source ownership is samplewise on the
enlarged source, while the physical row is the deterministic aggregate.

If a finite endpoint-atom proof object is desired, resolve the complete labelled
tree first and apply one positive finite-dimensional cubature to all live row
and provenance coordinates simultaneously.

If the resolved integrated row is the full Möbius component row `c_X`, then
nonnegativity of every source observation gives

\[
 c_X(j)\ge0
\]

for every fixed `j`, with no native score or capacity statement required before
the fixed-row Mellin--Landau consumer.
