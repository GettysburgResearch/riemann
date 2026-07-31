# R-15601 — Dimension-only weighted-index comparison is insufficient

Claim ID: `R-15601`  
Title: A source packet of sufficient dimension need not capture the weighted-deficit eigenspace  
Status: `REFUTED AS STATED / SCOPE CORRECTION`  
Authoring and auditing agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Refutes: deleted draft `L-15609-phase-space-margin-closes-weighted-index.md`  
Preserves: its trace/Markov index bound, pre-plunge source-count scheduler, and proposed directed inputs  
Dependencies: `L-15603`, `L-15607`, `L-15608`

## Refuted implication

The deleted draft proposed the following step.

1. Let the positive weighted-deficit operator be `T_G`.
2. Let
   \[
   p_G(\Gamma)
   =\#\{n:\theta_n(T_G)>G-\Gamma\}.
   \]
3. Construct an exact repaired source packet of dimension at least
   `p_G(Gamma)`.
4. Conclude that the source packet captures the weighted deficit sufficiently to
   prove the complement floor.

Step 4 is false without a subspace-capture or leverage theorem.  Dimension alone
contains no information about the relative position of the two packets.

## Exact two-dimensional counterexample

Let

\[
 H=\mathbb R^2,
 \qquad
 T_G=\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad
 \kappa=G-\Gamma=\frac12.
 \tag{R-15601.1}
\]

Then

\[
 p_G(\Gamma)=1.
 \tag{R-15601.2}
\]

Take a one-dimensional exact source packet

\[
 L=\operatorname{span}\{e_2\}.
 \tag{R-15601.3}
\]

Thus

\[
 \dim L=p_G(\Gamma)=1.
\]

Nevertheless

\[
 \operatorname{Tr}((I-P_L)T_G)=1>\kappa
 \tag{R-15601.4}
\]

and

\[
 \|(I-P_L)T_G(I-P_L)\|=1>\kappa.
 \tag{R-15601.5}
\]

The whole weighted-deficit direction `e_1` remains in `L^perp`.  Hence neither
the leverage-trace certificate nor the operator-norm complement certificate
passes.

The example remains valid if the source packet is declared to have zero
internal form and zero tail in an independent abstract source construction.  The
failure is purely relative geometry.

## Valid pieces preserved

### Trace/Markov index bound

For every positive trace-class `T_G` and `kappa>0`,

\[
 \boxed{
 \#\{n:\theta_n(T_G)>\kappa\}
 \le\frac{\operatorname{Tr}T_G}{\kappa}.}
 \tag{R-15601.6}
\]

This is a valid proof-grade upper count after directed enclosure and endpoint
handling.

### Pre-plunge source count

Sharp localization estimates may prove that a source concentration operator has
many eigenvalues near one.  After exact source repair, `L-15605` converts this
into a rigorous source-capacity lower bound, subject to one uniform form-tail
estimate on the whole packet.

### Phase-space margin as a scheduler

A strict inequality between the trace-based weighted index cap and the source
capacity is useful empirical evidence and a scheduling statistic.  It is not a
complement floor until relative capture is certified.

## Correct replacement

Any of the following additional gates repairs the false step.

### 1. Exact leverage trace tail

Prove directly

\[
 \boxed{
 \operatorname{Tr}((I-P_L)T_G)
 \le G-\Gamma.}
 \tag{R-15601.7}
\]

Then `L-15607/L-15608` give

\[
 A|_{L^\perp}\succeq\Gamma I.
\]

### 2. Operator-norm capture

Prove

\[
 \boxed{
 \|(I-P_L)T_G(I-P_L)\|
 \le G-\Gamma.}
 \tag{R-15601.8}
\]

with the correct symbol-to-form normalization.

### 3. Explicit top-eigenspace capture

If `P_top` is the spectral projection of `T_G` above `G-Gamma`, prove a directed
principal-angle or graph bound strong enough to control

\[
 (I-P_L)P_{\rm top}.
\]

This is a valid but stronger route.

### 4. Finite visible Schur saturation

Use `L-15604`: retain every mismatch direction in the finite space

\[
 V=(L+U)\cap L^\perp
\]

and certify its complete Schur complement above `Gamma`.

## Effect on the scalar cofinal theorem

The correct scalar target is not

\[
 p_G(\Gamma)\le\dim L.
\]

It is the trace-tail or complement statement

\[
 \boxed{
 \operatorname{Tr}((I-P_L)T_G)
 \le G-\Gamma}
 \tag{R-15601.9}
\]

or an equivalent proof-grade saturation certificate.

Once this holds and the packet form/residual rates of `T-15602` vanish,

\[
 F_j\to0^-
\]

and the existing cofinal lower-envelope theorem implies RH.

## Process note

The original proposed file was pushed as concurrent speculative work.  Git
history preserves it.  It was removed from the active theorem stack immediately
after the exact counterexample above was found, while its valid scheduling ideas
were retained in audited `O-15604` and this refutation.

## Status boundary

- The counterexample and trace bound are exact elementary finite-dimensional
  facts.
- No zeta-specific trace-tail estimate is proved here.
- No proof of RH is claimed.
