# D-25801 — Prime-Anchored Digit Transport certificate

Claim ID: `D-25801`  
Title: A fail-closed source-specific transport certificate for the reciprocal-free depletion of the top reflected Möbius source  
Status: **PROPOSED EXACT DEFINITION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Frozen base: PR #250 at `f179ab93e7e0dc748e0e9fb9e5a6800b80b6d224`  
Scope: one packet order and one logarithmic block; no claim that production certificates exist

## 1. Parameters and sources

Fix

\[
K\ge8,
\qquad
X=e^{J+O_K(1)},
\qquad
V=\lceil X^{1/K}\rceil.
\]

Choose one fixed

\[
0<\delta_0<\frac13
\]

and put

\[
m_K=\lfloor\delta_0K\rfloor,
\qquad
Q=V^{m_K}.
\tag{D-25801.1}
\]

Let

\[
T_{K,V}=\Lambda*r_V^{*(K-1)}
\]

be the complete top source of `L-25801`, and define its depletion

\[
Z_{K,V,Q}=a_Q*T_{K,V},
\qquad
a_Q=\mathbf1*(\varepsilon-\delta_Q).
\tag{D-25801.2}
\]

The certificate uses the exact recovery

\[
T_{K,V}=H_Q*\mu_V*Z_{K,V,Q},
\qquad
H_Q=(\varepsilon-\delta_Q)^{-1},
\tag{D-25801.3}
\]

on the complete active coefficient range.

## 2. Definition of a `PADT(K,J)` object

A Prime-Anchored Digit Transport certificate contains the following exact data.

### A. Top-source manifest

A duplicate-free manifest for

\[
T_{K,V}=g_{K-1}*\mu_{>V}^{*(K-1)},
\qquad
g_{K-1}=\Lambda*d_{K-1},
\]

including:

```text
source tuple ID
marked prime-power anchor q
remaining positive divisor coordinates
large Möbius coordinates d_i>V
exact coefficient and square-root normalization
window and physical block hashes
output, ratio, and cutoff cells
```

The manifest must reconstruct the complete coefficient before any estimate.

### B. Lower-depth sibling manifest

Every divisor-allocation sibling required to move a prime or divisor coordinate
through the cutoff `d_i=V` is retained. The high-rank Möbius hypercube may not
be isolated from the lower-depth vertices that complete its signed allocation
cube.

A sibling already proved Euler-small may be consumed only after its source
incidence has been used in the transport identity.

### C. Radix depletion ledger

The certificate exports:

```text
Q=V^m_K
arithmetic a_Q(n)=1-1_(Q|n)
positive kernel C_Q
current row
Q-shifted slack row
stable inverse H_Q
```

and verifies coefficientwise

\[
(\varepsilon-\delta_Q)T_{K,V}
=\mu_V Z_{K,V,Q}.
\tag{D-25801.4}
\]

The `Q`-shifted row must be routed to scale

\[
\le(1-\delta_0+O(1/K))J+O_K(1).
\tag{D-25801.5}
\]

### D. Reviewed two-frequency block

Every current and flow edge is represented in the physical block Gram of
`L-9518`. The object exports independent frequency variables, the block kernel
`Phi_(J,alpha)(t-s)`, and the complete finite arithmetic normal Gram.

A one-frequency global integral is rejected.

### E. Signed adjacent-flow ledger

For each source fiber, the object gives exact coefficients

\[
c_j=b_j+F_{j-1}-F_j
\]

and endpoint source vectors `v_j`, proving

\[
\sum_jc_jv_j
=\sum_jb_jv_j+\sum_jF_j(v_{j+1}-v_j).
\tag{D-25801.6}
\]

Every edge record contains:

```text
flow ID and coefficient
both source tuple projections
marked anchor and prime-power coordinates
induced signs
residual cutoff status
output and ratio cells
destination token
```

The flow may be signed. Positive defect and negative slack must be transported
together before a positive part or total variation is taken.

### F. Prime-power cluster ledger

All same-scale prime-power children are grouped into complete consecutive
clusters. The certificate verifies the appropriate path inverse or the exact
`{2,3,4,5}` exceptional inverse from `L-25805`.

After the cluster solve, every remaining positive child must have prime-power
endpoint at most half that of its parent or have an explicit lower-scale source
map.

### G. Quadratic transport-cost certificate

Let `G_J^nabla` be the exact two-frequency Gram of the adjacent currents. The
certificate proves

\[
\boxed{
F^*\mathcal G_J^\nabla F
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+
\max_\tau
\max_{u\le(1-\delta_1)J+C_K}
E_{K,\tau}(u)
\right],}
\tag{D-25801.7}
\]

for one `delta_1>0` independent of `J` and with

\[
\eta_K\longrightarrow0
\tag{D-25801.8}
\]

along the proposed order sequence.

The bound may be proved by exact LDL, interval LDL, cellwise SOS, a verified
derivative-energy domination, or a combination. A scalar transport objective
is only a scheduler until (D-25801.7) is authenticated.

### H. Remainder routes

Every `b_j` row in (D-25801.6) is assigned exactly one destination:

1. source-cancelled internal sibling;
2. complete-lattice Euler row;
3. `Q`-shifted lower-scale slack;
4. factor-two prime-power child;
5. explicit compact-window or residual-cutoff boundary;
6. fixed-ratio Möbius-shell mutation.

No undeclared same-scale remainder is permitted.

### I. Recovery ledger

The checker applies

\[
T=H_Q*\mu_V*Z
\]

only after the depleted estimate. It verifies

\[
\|H_Q^\#\|_{\rm TV}
\le(1-Q^{-1/2})^{-1}
\]

and charges `mu_V` once:

\[
\left(\sum_{a\le V}{|\mu(a)|\over\sqrt a}\right)^2
\le
\exp\left[\left({1\over K}+o_K(1)\right)J\right].
\tag{D-25801.9}
\]

A second hidden truncated-coordinate charge is rejected.

### J. Scalar firewalls

The object must reproduce:

1. one fixed-ratio Mertens shell, preferably `c=1/2` or `2/3`;
2. the dyadic parity-comb three-tap mutation;
3. the exact first-cell Mertens coefficient when the Farey adapter is used.

These are source mutations, not additional assumptions.

## 3. The `PADT(K)` assertion

`PADT(K)` means that for every sufficiently large block there is a
`PADT(K,J)` certificate with constants

\[
\delta_0,\delta_1>0
\]

uniform along an unbounded sequence of `K`, and with `eta_K->0`.

The certificate is finite and proof-producing. It is not a generic coercivity
theorem for `C_Q`, not an arbitrary-vector Type-II estimate, and not an
almost-all short-interval theorem.

## 4. Automatic rejection conditions

Reject a purported certificate if any of the following occurs:

- the aggregate zero Schur reserve of PR #250 is reused;
- a reciprocal-zeta inverse is hidden inside the transport theorem;
- the high-rank Möbius hypercube is deleted without its lower-depth siblings;
- the `Q`-shift is not a fixed fraction of `J`;
- the flow is made nonnegative by discarding negative slack;
- a same-scale cluster is solved one row at a time;
- a prime-power child above the declared scale survives;
- cross terms in `G_J^nabla` are discarded;
- the recovery pays more than one `mu_V` coordinate;
- the parity or fixed-ratio mutation is absent;
- finitely many orders are promoted to RH.

## 5. Proof boundary

This definition converts the remaining source-specific contraction into one
finite signed transport and Gram certificate. `T-25801` proves that an unbounded
`PADT(K)` sequence implies RH. Construction of the production flow and its
subexponential quadratic cost remains the load-bearing arithmetic theorem.
