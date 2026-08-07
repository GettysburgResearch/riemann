# D-25801 — Prime-Anchored Digit Transport certificate

Claim ID: `D-25801`  
Title: A fail-closed source-specific transport certificate for the fixed-scale depletion dipole of the top reflected Möbius source  
Status: **PROPOSED EXACT DEFINITION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Corrected: 2026-08-07 after the recovery-wedge audit `R-25802`  
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

and the preferred dyadic radix

\[
L(J)=\left\lfloor{\delta_0J\over\log2}\right\rfloor,
\qquad
Q=2^{L(J)}.
\tag{D-25801.1}
\]

Thus

\[
\log Q=\delta_0J+O(1).
\tag{D-25801.2}
\]

An arithmetic radix satisfying the same scale relation may be substituted, but
the dyadic choice must additionally pass the bit-layer and parity-comb
mutations of `L-25806`.

Let

\[
T_{K,V}=\Lambda*r_V^{*(K-1)}
\]

be the complete top source of `L-25801`. Define the reciprocal-free potential

\[
Z_{K,V,Q}=a_Q*T_{K,V},
\qquad
a_Q=\mathbf1*(\varepsilon-\delta_Q),
\tag{D-25801.3}
\]

and the fixed-scale depletion dipole

\[
\boxed{
D_{K,V,Q}
=(\varepsilon-\delta_Q)*T_{K,V}
=\mu_V*Z_{K,V,Q}.}
\tag{D-25801.4}
\]

The second equality is the source-specific nilpotent identity of `L-25803`.

The physical field therefore satisfies exactly

\[
\boxed{
\mathcal T_J
=Q^{-1/2}\mathcal T_{J-\log Q}
+\mathcal D_J.}
\tag{D-25801.5}
\]

`PADT` estimates `D` directly. It does **not** estimate `Z` at the current block
and recover by an absolute `mu_V` bound; that shortcut is rejected by
`R-25802`.

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

### C. Radix-depletion ledger

The certificate exports:

```text
Q=2^L with log Q=delta_0 J+O(1)
arithmetic a_Q(n)=1-1_(Q|n)
positive kernel C_Q
dyadic bit-layer decomposition
current row
Q-shifted slack row
reciprocal-free potential Z
signed dipole D=mu_V*Z
```

and verifies coefficientwise

\[
(\varepsilon-\delta_Q)T_{K,V}
=\mu_V Z_{K,V,Q}.
\tag{D-25801.6}
\]

The shifted field in (D-25801.5) lies at scale

\[
(1-\delta_0)J+O(1).
\tag{D-25801.7}
\]

The geometric inverse `H_Q` may be exported as an algebraic audit, but it is not
used for an absolute norm recovery.

### D. Reviewed two-frequency block

Every current, slack row, and flow edge is represented in the physical block
Gram of `L-9518`. The object exports independent frequency variables, the block
kernel `Phi_(J,alpha)(t-s)`, and the complete finite arithmetic normal Gram.

A one-frequency global integral is rejected.

### E. Signed `mu_V` transport ledger

The factorization

\[
D=\mu_V*Z
\]

is retained with the Möbius signs. For every represented source fiber the object
gives exact coefficients

\[
c_j=b_j+F_{j-1}-F_j
\]

and endpoint vectors `v_j`, proving

\[
\sum_jc_jv_j
=\sum_jb_jv_j+\sum_jF_j(v_{j+1}-v_j).
\tag{D-25801.8}
\]

Every edge record contains:

```text
flow ID and coefficient
both source tuple projections
truncated Möbius anchor a<=V
marked prime-power/divisor coordinate
induced signs
residual cutoff status
output and ratio cells
destination token
```

The flow may be signed. Positive defect and negative slack must be transported
together before a positive part or total variation is taken.

Taking `sum_(a<=V)|mu(a)|/sqrt(a)` before this ledger is complete is rejected.

### F. Prime-power cluster ledger

All same-scale prime-power children are grouped into complete consecutive
clusters. The certificate verifies the appropriate path inverse or the exact
`{2,3,4,5}` exceptional inverse from `L-25805`.

After the cluster solve, every remaining positive child must have prime-power
endpoint at most half that of its parent or have an explicit lower-scale source
map.

### G. Quadratic dipole-cost certificate

Let `G_J^nabla` be the exact two-frequency Gram of the adjacent currents and let
`D_J` be the complete dipole field after all source siblings are recombined.
The certificate proves

\[
\boxed{
\|\mathcal D_J\|^2
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+
\max_\tau
\max_{u\le(1-\delta_1)J+C_K}
E_{K,\tau}(u)
\right],}
\tag{D-25801.9}
\]

for one `delta_1>0` independent of `J` and with

\[
\eta_K\longrightarrow0
\tag{D-25801.10}
\]

along the proposed order sequence.

The proof object separately authenticates the flow contribution

\[
F^*\mathcal G_J^\nabla F
\]

and every boundary/lower-scale remainder. The bound may be proved by exact LDL,
interval LDL, cellwise SOS, a verified derivative-energy domination, or a
combination. A scalar carry objective is only a scheduler until the physical
quadratic bound is authenticated.

### H. Remainder routes

Every `b_j` row in (D-25801.8) is assigned exactly one destination:

1. source-cancelled internal sibling;
2. complete-lattice Euler row;
3. `Q`-shifted lower-scale slack;
4. factor-two prime-power child;
5. explicit compact-window or residual-cutoff boundary;
6. fixed-ratio Möbius-shell mutation.

No undeclared same-scale remainder is permitted.

### I. Dipole recurrence ledger

The checker verifies (D-25801.5) on the physical block and uses

\[
\|u+v\|^2\le2\|u\|^2+2\|v\|^2
\]

to obtain

\[
E_{\rm top}(J)
\le
2Q^{-1}E_{\rm top}(J-\log Q)
+2E_D(J).
\tag{D-25801.11}
\]

Because `Q=e^(delta_0 J+O(1))`, the first coefficient is exponentially small
and the destination has a fixed logarithmic reserve.

No absolute recovery wedge is present.

### J. Scalar firewalls

The object must reproduce:

1. one fixed-ratio Mertens shell, preferably `c=1/2` or `2/3`;
2. the dyadic bit-layer factorization;
3. the parity-comb three-tap mutation;
4. the exact first-cell Mertens coefficient when the Farey adapter is used.

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
- current-block control of `Z` is substituted for the dipole estimate;
- `mu_V` is paid by total variation before signed transport;
- a reciprocal-zeta inverse is hidden inside the transport theorem;
- the high-rank Möbius hypercube is deleted without its lower-depth siblings;
- the `Q`-shift is not a fixed fraction of `J`;
- the flow is made nonnegative by discarding negative slack;
- a same-scale cluster is solved one row at a time;
- a prime-power child above the declared scale survives;
- cross terms in the physical Gram are discarded;
- the parity or fixed-ratio mutation is absent;
- finitely many orders are promoted to RH.

## 5. Proof boundary

This definition converts the remaining source-specific contraction into one
finite signed dipole-transport and Gram certificate. Corrected `T-25801` proves
that an unbounded `PADT(K)` sequence implies RH. Construction of the production
flow and its subexponential quadratic cost remains the load-bearing arithmetic
theorem.
