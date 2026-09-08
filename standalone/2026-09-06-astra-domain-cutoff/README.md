# Explicit domain cutoff construction and the unresolved global cost

Status: PROPOSED COMPONENT PROOFS; independent review pending. RH is not proved.
Scope: continuation of PR804 from 4a88ee5ed8be897ed88c85e69e7650ab7e3ddd01.
Author: Astra, 2026-09-06. This is not a Reviewer D acceptance verdict.

## What this pass contributes

The new pole-neutral test has Laplace transform (z-1/2)^2/(z+1)^4.
Its only right-half-plane zero is the removable real pole-point, not a
nontrivial zeta zero. An explicit stable cubic kernel and ordinary Mobius
coefficients construct y_T in the ORIGINAL factorial-source domain with

    y_T(t)=f(t) on [0,T], for every T>0.

The full future tail is retained. Any hypothetical off-line zero forces its
energy to grow exponentially; repeated zeros introduce an exact polynomial
factor. An unconditional nearby-damping family does fill the ambient space,
but its obvious damped-output assignment is proved noncontractive on the
ACTUAL sources. The correct Xi assignment has an explicit signed commutator.

Separately, every finite parent Gram has a proved explicit exponentially
small spectral floor. This pays inverse-conditioning uncertainty at a large
specified source cutoff; it does not evaluate the limiting domain defect.

The remaining signed energy upper bound is written completely in ordinary
Mobius coefficients and a cubic-exponential correlation kernel. Its diagonal
is O(T). The required subexponential cross-term/future-energy bound remains
UNPROVED and is RH-equivalent. No component or finite check silently supplies
that estimate.

## Reading path

1. CONSTRUCTION.md — fixed coefficients, pole cancellation, full energy and
   conditional RH consequence.
2. TAIL_AND_DAMPING.md — complete tail/multiplicity cost, true density and the
   failed corresponding transfer.
3. GRAM_FLOOR.md — unconditional finite-rank conditioning and its cost.
4. ATTEMPT.md — the precise unsuccessful closure and surviving results.
5. CLAIMS.tsv, EDGES.tsv, SOURCES.tsv, EXTERNAL_INPUTS.md, VALIDATION.md.

## Run

    python checks.py --check checks.normal.json
    python -O checks.py --check checks.optimized.json
    python validate.py

The directed finite-source check covers every one of 63 logarithmic cells
through time log64. It proves 1/2 < ||h 1_[0,log64]||_2^2 < 13/25 and
h(log2)<-4/5, using integer intervals. This is not a global growth result.

No Lean, remote CI, high-ordinate zero evaluation, full critical-map norm
computation, or independent referee acceptance is claimed. The construction
is in the classical Nyman--Beurling/Mobius approximation lineage. External
novelty has not been established.
