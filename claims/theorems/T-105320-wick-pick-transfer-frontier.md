# T-105320 — Wick-preconditioned low-order Pick frontier

Claim ID: `T-105320`  
Status: **UNCONDITIONAL MODEL THEOREM + CONDITIONAL XI RECORD THEOREM**  
Created: 2026-08-23  
Depends on: `T-105310`; `L-105320--L-105323`  
RH status: **unproved**

## 1. What is now unconditional

The low-order reciprocal coefficient family is exactly the frozen-parameter
derivative of the formal xi-prime coefficient source. A finite entire,
zero-free congruence cancels its complete degree-one von Mangoldt packet.
The resulting normalized coefficient energy satisfies

\[
\mathcal D_W<7/320
\]

per one-sided safe-line source, and the Hermitian frozen model has normalized
effective rank exceeding `160/167`.

This repairs the false premise that the raw reciprocal matrix was already a
one-percent perturbation of its archimedean carrier.

## 2. Actual-Xi transfer theorem

Let `H_T^Xi` be a source-owned finite compression of the affine-centered Pick
kernel of `Xi/Xi'`, obtained by multiplying the observation family by the
finite Wick factor `W_(L,X)` before the contour is collapsed. Assume:

1. the dimension is `(1-o(1))N_1(T)`;
2. the frozen-parameter coefficient bridge of `L-105320` passes through the
   xi-prime explicit formula with entry-dependent error `o(N_1)`;
3. horizontal, endpoint, pole and canonical-product tail terms have trace and
   positive-index cost `o(N_1)`;
4. after these terms are included,
   \[
   tr H_T^Xi >=0.99 tr K_T,
   \qquad
   ||H_T^Xi||_HS<=1.01||K_T||_HS,
   \]
   where `K_T` is the frozen Wick model of `L-105322`;
5. the common-zero/multiple-parent correction is retained explicitly.

Call this conjunction `WXFER105320`.

Then `L-105322`, the confluent inertia budget of `T-105310`, and exact reverse
Rolle give

\[
\boxed{
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}
\ge {5765136493\over8517835000}
=0.676831\ldots .}
\tag{T-105320.1}

This conclusion counts critical-line zeros with multiplicity. If the
common-zero and multiple-parent terms are `o(N)`, the corresponding simple
version follows from the same ledger.

## 3. Remaining arithmetic rows

The coefficient-level part of `FREEZE105320` is closed by `L-105323`. The remaining transfer has been reduced to three typed estimates:

```text
GRAMFREEZE105320:
  pass the already-controlled differentiated coefficient re-expansion through
  the complete zero/prime Gram bridge and the finite Wick congruence;

BOUND105320:
  control the two horizontal contour edges and the finite Wick factor without
  paying an exponential-type loss;

TAIL105320:
  show the canonical-product, multiplicity and omitted-prime positive-index
  tail is o(N_1(T)).
```

Together these are `WXFER105320`.

## 4. Boundary

```text
raw one-percent Cauchy comparison          refuted
coefficient derivative bridge             proved exact
entry-dependent coefficient freezing       proved in H1/H2/H3 norms
zero-free first-chaos cancellation         proved exact
Wick diagonal constant <7/320              proved
frozen model effective rank >160/167       proved
WXFER105320                                open / record-bearing
0.676831 zero proportion                   unproved
Riemann Hypothesis                         unproved
```
