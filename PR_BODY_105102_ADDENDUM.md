## Checkpoint 3 — paired boundary-coherence flux

Exact checkpoint base:
fd3ef43a6964e502f00ad906482eae5b3c544fba.

This checkpoint adds the first-residue boundary charge

\[
\Phi_{1,F}=\frac1{2\pi i}\int_{\partial\Omega}\frac{F}{F'}\,dz
\]

to the L-105101 second-moment charge. At one regular finite window,

\[
\mathcal M_{1,F}=-\Phi_{1,F}+C_{1,F},
\qquad
\mathcal M_{2,F}=B_F-C_{2,F}-D_{2,F},
\]

so, when \(R_F\mathcal M_{2,F}>0\), the transfer-safe residue-coherence
quotient is

\[
\frac{(-\Phi_{1,F}+C_{1,F})_+^2}
{R_F(B_F-C_{2,F}-D_{2,F})}.
\]

For \(F=\Xi^{(k-1)}\), this is an exact fixed-window reformulation of the
draft PR #720 positive-part coherence gate, conditional on the stated window
hypotheses. The literal RCMV104530 square agrees only after the first moment
is known positive. This checkpoint proves no favorable estimate.

At each fixed regular height, a sufficiently thin strip eliminates
\(C_{1,F}\) and \(C_{2,F}\) exactly. Controlling the boundary charges along a
potentially shrinking strip remains open.

New claims:

- L-105102: paired first/second window flux;
- T-105102: quantitative continuation frontier;
- R-105102: nonreal first-correction carrier firewall;
- M-105102: hostile review contract.

The exact replay uses rational and Gaussian-rational arithmetic only. It
authenticates checkpoint 2, checks both integrated edge formulas, reconstructs
the global \(V_2\) ledger independently, and exercises positive, unit, zero,
and sub-threshold coherence fixtures.

No Xi evaluation, floating-point contour quadrature, broad suite, or heavy
campaign was run. RCMV104530 and RH remain open.
