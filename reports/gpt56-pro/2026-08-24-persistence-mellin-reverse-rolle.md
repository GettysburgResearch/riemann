# Research report — Persistence–Mellin reverse Rolle for Xi

Date: 2026-08-24  
Branch: `research/gpt56-pro/104510-hermite-biehler-last-defect`

## Result

The unit-amplitude phase identity is exact but not an independent producer: its
phase drift is the parent real-zero count up to bounded endpoints.

The replacement is a source-side excursion theory.

For every positive amplitude threshold, the difference between good and wrong
critical points of `Xi''` above that threshold is exactly half the number of
level crossings. Equivalently, wrong extrema inject into larger good extrema.

For every `p>0`, the signed p-th critical amplitude moment is the positive
coarea integral

\[
{p\over2}\int |\Xi''|^{p-1}|\Xi'''|.
\]

After normalizing by the maximum amplitude, these moments form a completely
monotone Laplace transform of the level-crossing function.

## Two conclusion-facing routes

### Excursion route

A positive density follows from one threshold retaining enough derivative
criticals and enough excursion components:

\[
\delta_y(1+\kappa_y)>1.
\]

### Mellin-variation route

On height windows, the signed p-moment numerator is exactly a positive
p-variation plus endpoints. One marked `2p` critical moment then gives the
count by Cauchy--Schwarz.

Both routes use Conrey's `alpha_3` input linearly and do not import the
independent `alpha_2` theorem.

## Boundary

The exact persistence and Mellin theorems are unconditional. Their
asymptotic Xi estimates remain open. RH is unproved.
