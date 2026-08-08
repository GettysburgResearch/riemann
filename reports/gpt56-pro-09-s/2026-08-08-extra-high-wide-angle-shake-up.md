# Extra-high wide-angle shake-up: critical-neutral dyadic boundary route

Date: 2026-08-08  
Agent: `gpt56-pro-09-s`  
Base: PR #316 at `c387a48cd6ff07433aafb08b312c0473efef9192`  
Status: **NEW GLOBAL CONDITIONAL PROPOSAL / ONE CRITICAL CAP RECURRENCE OPEN**  
RH: **UNPROVED**

## 1. Why this pass was redone from scratch

The previous quick continuation was not aligned with the live repository frontier. A full refresh changes the answer materially.

Most importantly, the apparently closing PR #304 terminal-atomic route was subsequently refuted: its polylogarithmic boundary claim lost load-bearing `1/(2k)` factors, and the complete stopped boundary has linear ordinary atomic norm. The live route must preserve neighboring dilation cancellation or use a different native coordinate.

The same refresh shows that a strict eta contraction is also the wrong global target. At every critical-line zeta zero the critical eta multiplier is exactly one. Any source-blind norm containing that oscillatory mode must therefore have operator norm at least one.

These are not setbacks to hide. Together they identify the correct critical geometry.

## 2. Three routes were re-audited

### A. Atomized carry / Selberg route

PR #297 supplies a genuine all-zero vector-valued pole frame and exact physical carry Gram. It also closes the complete endpoint source positively. Its remaining `CISR` theorem is a coupled interior Hermitian inequality.

This remains serious, but `R-29002` shows why scalar row positivity cannot simply be lifted through source amplitudes.

### B. Brownian/Nörlund route

PR #296 supplies explicit finite functional-equation approximants converging locally uniformly to xi. Its closing real-zero/Hermite-Biehler theorem remains open. The finite positive gamma mixture does not by itself put the symmetrized approximant in a real-zero class.

This route is genuinely orthogonal, but no new finite stability theorem was found in this pass.

### C. Dyadic carry/cascade route

The newest scope corrections make radix two structurally preferred:

- five-adic residue Fourier modes introduce nonprincipal Dirichlet-L channels;
- the dyadic unit residue has only the principal zeta channel;
- the eta propagation is exactly neutral at zeta-zero modes;
- PR #316 proves fresh boundaries are small in their native first-difference norm;
- PR #272 already shows a coefficient-one fixed-scale descent is sufficient after cycle optimization.

This route therefore received the main attack.

## 3. New exact factorization

At every support-halving depth the fresh boundary profile is

\[
h_{a,X,s}(x)=x^{-s}\log\min\{2^a(x-1)+1,X\}.
\]

The new `L-32401` proves

\[
h_{a,X,s}=u_{a,s}-c_{a,X,s}
\]

with

\[
 u_{a,s}(x)
 =a\log2\,x^{-s}+x^{-s}\log x
 -\sum_{\ell\ge1}{(1-2^{-a})^\ell\over\ell}x^{-s-\ell}.
\]

The faster-power coefficient tail has exact radius-`1/4` norm at most

\[
\log(4/3)
\]

uniformly in depth. Thus the entire uncapped component lies inside PR #286's existing `6/7` Dirichlet–Taylor bank.

The only new boundary species is the explicit cap

\[
 c_{a,X,s}(x)
 =x^{-s}\log{2^a(x-1)+1\over X}
 1_{x\ge1+(X-1)/2^a}.
\]

This is a genuine state-space reduction of `CBVR`: do not propagate the full affine-log boundary after its contracting component has already been identified.

## 4. Criticality means neutrality

The new `L-32402` formalizes the correct spectral threshold. For a Mellin mode

\[
e^{(\rho-1/2)t},
\]

the eta propagation multiplier at a zeta zero is exactly one. Under endpoint doubling the same mode changes by

\[
2^{\rho-1/2}.
\]

Therefore

```text
critical zero      scale modulus 1;
off-line zero      scale modulus >1.
```

A dyadic recurrence with total lower-scale coefficient one is not a weak substitute for contraction. It is the exact critical threshold. Iterated over dyadic scales, a polynomial forcing gives only polynomial growth and therefore the subexponential local-energy bound consumed by the pole criterion.

## 5. New sole theorem — CNCR

The remaining theorem is the **Critical-Neutral Cap Recurrence**:

\[
D_{cap}(2Y)\le D_{cap}(Y)+C\log^A(2Y),
\]

after complete same-destination cap recombination and Pascal-cycle optimization, with every uncapped analytic component removed through `L-32401` before debt is measured.

This is weaker than prior strict-contraction goals and better aligned with the known zero-mode geometry.

A production object must keep:

1. the exact cap profile and cutoff location;
2. every shifted/unshifted sibling;
3. all current-scale cross terms before recombination;
4. the Pascal-cycle affine freedom;
5. integer endpoint perturbations;
6. the dyadic bottom-charge and `2/3` Mertens mutations.

## 6. Why other tempting shake-ups were not promoted

### Entropy dissipation

A generic nonlinear entropy was considered but no exact arithmetic identity ties it to the source-complete carry Gram. Promoting it would simply invent a new unproved bridge. It is not retained.

### Strict eta jet contraction as the full proof

Rejected by the exact zero-mode firewall. The existing strict jet theorem applies to a low-frequency analytic class which excludes the RH-bearing oscillations.

### Five-adic finite automaton

A complete unit-residue contraction simultaneously controls reciprocal Dirichlet-L channels modulo five. This is potentially a GRH theorem, not a harmless finite boundary reduction.

### Brownian positive-mixture stability

Still attractive, but the positive mixture and finite delay representation do not presently imply Hermite-Biehler or Pólya-frequency stability after functional-equation symmetrization.

## 7. Full conditional chain

```text
all-depth finite boundary
-> exact affine-log core/cap split
-> uncapped core through 6/7 analytic bank
-> fresh cap injection polylog in native debt
-> CNCR coefficient-one propagated cap descent
-> polylog Cycle Debt / atomized local energy
-> sharp prime-power ramp or vector-valued pole criterion
-> RH.
```

## 8. Exact status

```text
PR #304 terminal atomic closure             REFUTED / not imported
strict complete eta contraction             IMPOSSIBLE at zero modes
all-depth affine-log factorization          PROPOSED COMPLETE
uncapped core coefficient budget            PROPOSED COMPLETE
critical neutral scale theorem              PROPOSED COMPLETE
fresh boundary native debt                  IMPORTED PROPOSED COMPLETE
CNCR                                         OPEN / RH-BEARING
CNCR -> RH                                   COMPLETE CONDITIONAL
Riemann Hypothesis                           UNPROVED
```

This is the corrected shake-up proposal. It narrows the unknown state without asking for an inequality stronger than RH's actual critical spectral geometry.
