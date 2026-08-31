# Fixed finite controls for the cusp spectral and period arguments

Status: PREREGISTRATION before running the new producer.
Arithmetic: Arb directed real balls, initially 256 bits; independent replay
at 512 bits. No midpoint sign is an acceptance criterion.

The purpose is to instantiate analytic inequalities for the actual source,
not to fit a spectral law or evaluate a surrogate period matrix.

## Operator bounds

Weights: 96, 192, 384, 768, 1536, 3072, 6144, 12288.
At each weight test the distinct positive indices among
`1, 2, floor(sqrt(k)/4), floor(k/96), floor(k/48), floor(k/24)`.
Record delta, Gamma Q, L, and both eigenvalue bounds in Theorem K.
Keep invalid lower-bound hypotheses as UNRESOLVED, never as false statements.

## Exact period inertia bounds

Weights: 384, 1536, 6144, 24576, 98304.
Endpoint parameters: 1/16, 1/32, 1/64, 1/128, 1/256.
Relative margins: 1/4, 1/8, 1/16.

At each cell compute the exact-symbol turning height Y from (P1), then
use Jminus=floor((1-margin)*(k-1)/(4*pi*Y)),
Jplus=ceil((1+margin)*(k-1)/(4*pi*Y)),
and H=(1+margin/2)*Y. A floor/ceiling is accepted only when the entire
directed ball determines the same integer; otherwise record UNRESOLVED.
If Jminus=0, record the trivial lower bound zero separately. Evaluate
the complete strict upper and lower criteria (P4),(P8), without tuning.

All cells, successful and unresolved, must be retained. Every completed
upper/lower result is a certificate via the proved analytic source bounds.
It is not a zero census, numerical matrix integration, or proof of an
infinite asymptotic. The producer must include Gaussian/Gamma identity
controls and mutation rejection; proof review is separate from replay.

Additional held-out families require a new written declaration before their
producer run. They must not silently replace failures in this panel.
