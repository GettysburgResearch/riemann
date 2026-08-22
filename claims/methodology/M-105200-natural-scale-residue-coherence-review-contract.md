# M-105200 — Hostile review contract for the natural-scale Xi residue programme

Claim ID: `M-105200`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

Review the packet in the following order:

1. `L-105200`: complex Gaussian saddle law;
2. `L-105201`: natural-height Rouché theorem;
3. `L-105202`: critical-residue asymptotics;
4. `L-105203`: exact coherence-defect budget;
5. `R-105200`: quantifier and boundary firewalls;
6. exact finite replay;
7. `T-105200`: conclusion graph and remaining gate.

## Mandatory analytic checks

Reject `L-105200` unless the proof supplies:

- one uniform dominant saddle for the positive Xi kernel;
- curvature and third/fourth derivative estimates on the standardized scale;
- exponentially negligible tails after bounded complex exponential tilting;
- relative, not merely additive, control of the one-sided Fourier transform on
  the full natural box;
- derivative control obtained on a strictly larger complex parameter disk.

Reject `L-105201` unless:

- the Gaussian multiplier is retained and shown nonzero;
- Rouché is applied cellwise with a uniform complement lower bound;
- the common box is uniform over every `m>=M`;
- reality follows from conjugation plus multiplicity one, not from a numerical
  scan.

Reject `L-105202` upon any:

- replacement of a zero of `Xi^(m+1)` by a model critical point without a
  `C^2` localization argument;
- use of the same real-box boundary for the approximation and residue sum
  without an explicit buffer;
- hidden exchange of the limits `m->infinity` and height `T->infinity`;
- claim that the global PR #723 second-moment ledger directly localizes in
  height.

## Mandatory logical checks

- `mathfrak C` controls wrong extrema only through
  `E<=R(1-mathfrak C)`.
- The Xi rectangle ledger must retain every `B_j+W_j-1` term.
- A fixed transfer constant `c<1` may not be iterated through
  `O(T^2 log T)` steps as though it were lossless.
- High-tail coherence is not fixed-order coherence.
- Finite polynomial identities are not entire-function limit theorems.

## Replay boundary

The exact replay authenticates only rational polynomial fixtures, Sturm root
counts, the Gaussian-model residue formula, and transfer algebra. It does not
authenticate the Xi saddle analysis or RH.

The smallest failure invalidating the new analytic advance is failure of the
uniform complex Gaussian limit (L-105200.4) at fixed standardized frequency.
The smallest conclusion-facing open statement is `CRDB105200`.
