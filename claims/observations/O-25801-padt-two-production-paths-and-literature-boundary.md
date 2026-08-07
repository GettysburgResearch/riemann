# O-25801 — PADT production paths and literature boundary

Observation ID: `O-25801`  
Title: Two concrete routes may produce the signed dipole certificate: a top-half carry flow with a transport-frame LMI, or a dyadic bit-layer induction with complete source siblings  
Status: **RESEARCH HANDOFF / NO THEOREM CLAIMED**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258

## 1. Path A — top-half signed carry flow

The parabolic carry continuation on PR #254 finds, in floating reconnaissance, a
nonnegative adjacent flow supported in the top half of its finite index range
with exact objective

\[
\sum_jF_j\log{j^2\over j^2-1}
\]

numerically of order `X^-3/2`.

The PADT anchor range is `V=exp(J/K)`, not the full output range. If a common
source-bound flow on `[cV,V]` has cost

\[
V^{-3/2+o_K(1)},
\]

then the exact weight comparison of `L-25807` and a subexponential Transport
Frame constant would make its physical adjacent current exponentially smaller
than the untransported anchor field.

The exact proposed workflow is:

```text
prime-anchor/divisor defect
-> solve complete same-scale prime-power clusters
-> route all positive children below half anchor scale
-> retain shifted dyadic slack
-> solve the remaining top-half adjacent LP
-> rationalize the flow
-> certify the two-frequency generalized eigenvalue
-> PADT.
```

The numerical rate is reconnaissance only. The theorem needed by PADT is merely
subexponential physical cost, not the observed power saving.

## 2. Path B — dyadic bit-layer induction

For

\[
Q=2^L,
\]

`L-25806` gives

\[
a_{2^L}T
=\sum_{j=0}^{L-1}\delta_{2^j}(a_2T).
\]

The large fixed-scale depletion is therefore a finite stack of odd-part
sources. The ordinary odd-part layer contains the positive parity-comb channel
exactly.

A possible induction is:

1. expose the parity layer and the all-integer layer separately;
2. use complete-lattice cancellation on the all-integer principal part;
3. use the parity-comb three-tap identity on the dyadic shell component;
4. retain every lower-depth Möbius sibling generated when a prime crosses `V`;
5. telescope the `L=O(J)` layers before total variation.

A polynomial number of layers does not change an exponential rate. The danger
is that one layer can retain the complete fixed-ratio Mertens mode. The parity
mutation is therefore mandatory at every inductive step.

## 3. Exact source graph versus almost-all Type II

The closest large-scale analytic methodology is the higher-uniformity and
contagion framework of Matomäki, Radziwiłł, Shao, Tao, and Teräväinen,
*Higher uniformity of arithmetic functions in short intervals II. Almost all
intervals*, Inventiones Mathematicae 244 (2026), arXiv:2411.05770.

That theorem is an almost-all short-interval result. PADT needs one of:

1. a deterministic certificate for every sufficiently large physical block; or
2. a separate exact theorem proving that the fixed-ratio Mertens/parity mode
   cannot lie in the exceptional set.

The published almost-all result therefore cannot be inserted directly, but its
contagion and scale-propagation machinery is a serious model for the symbolic
source graph.

## 4. Canonical negative tests

The following finite outcomes would reject the proposed mechanisms.

### Against Path A

- the required flow necessarily leaves the top half;
- the signed flow has fixed positive cost in the carry metric;
- the generalized eigenvalue in `L-25807` grows like `V^c` for one fixed `c>0`;
- a same-scale prime-power cluster has unbounded length or a negative inverse;
- the rationalized flow violates one physical source edge.

### Against Path B

- one dyadic layer loses a lower-depth sibling;
- the parity three-tap mutation fails after source projection;
- layer telescoping requires rowwise absolute values;
- a fixed positive proportion of the Mertens mode remains in every layer;
- the number of live boundary channels grows exponentially in `J`.

## 5. Recommended immediate computation

The next production artifact should not be another synthetic matrix. It should
be the complete `K=4` top-source graph at one manageable block:

```text
all top tuples
all lower-depth divisor-allocation siblings
Q=2^L depletion pairs
marked prime-power anchors
adjacent incidence
same-scale cluster solves
exact two-frequency Gram
fixed-ratio and parity mutations
```

This one object can decide whether PADT is structurally viable before an
all-`K` theorem is attempted.

## 6. Status

```text
exact prime-anchor and depletion algebra       proposed complete
exact dyadic/parity interface                  proposed complete
exact adjacent-flow and weight adapter         proposed complete
Path A production flow and frame               open
Path B bit-layer induction                     open
PADT                                            open
RH                                              unproved
```
