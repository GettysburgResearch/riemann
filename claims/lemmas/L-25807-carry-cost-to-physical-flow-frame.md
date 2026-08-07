# L-25807 — Carry-cost to physical-flow frame adapter

Claim ID: `L-25807`  
Title: The exact adjacent displacement scale is dominated by the parabolic carry objective, reducing the analytic PADT bridge to one source-specific generalized-eigenvalue certificate  
Status: **PROPOSED EXACT ADAPTER; SOURCE-SPECIFIC FRAME BOUND OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Dependencies: `L-25804`; PR #254 `L-25301`  
Scope: finite physical flow spaces; no generic diagonal domination claimed

## 1. Exact weight comparison

For `j>=2`, put

\[
h_j=\log\left(1+{1\over j}\right)
\]

and

\[
\omega_j
=\log{j^2\over j^2-1}
=-\log\left(1-{1\over j^2}\right).
\tag{L-25807.1}
\]

The first is the exact logarithmic distance between adjacent multiplicative
indices. The second is the exact objective weight of the parabolic adjacent
flow on PR #254.

Using

\[
\log(1+x)\le x
\]

and

\[
-\log(1-x)\ge x
\qquad(0<x<1),
\]

one obtains

\[
\boxed{
h_j^2\le {1\over j^2}\le\omega_j.}
\tag{L-25807.2}

Thus the scalar carry objective dominates the squared physical displacement of
every individual adjacent edge.

## 2. Incidence and physical Gram

Let `V_J` be the complete finite vector of source fibers in one physical block,
and let `B_J` be the signed adjacent-incidence matrix. A flow vector `F` produces
current

\[
B_JF.
\]

Let `K_J` be the reviewed two-frequency normal Gram of the source fibers. Then
its exact physical energy is

\[
\boxed{
\|B_JF\|_{K_J}^2
=F^*\mathcal G_J^\nabla F,
\qquad
\mathcal G_J^\nabla=B_J^*K_JB_J.}
\tag{L-25807.3}

Let

\[
W_J=\operatorname{diag}(\omega_j)
\tag{L-25807.4}
\]

with the appropriate repetition over source fibers.

## 3. Transport Frame certificate

Let `S_J` be the exact linear subspace licensed by:

- the top and lower-depth source manifests;
- the radix-depletion divergence equations;
- the complete prime-power cluster solves;
- the endpoint flow conditions.

A **Transport Frame** certificate is the source-specific LMI

\[
\boxed{
P_{S_J}^*\mathcal G_J^\nabla P_{S_J}
\preceq
\mathcal C_{K,J}
P_{S_J}^*W_JP_{S_J},}
\tag{L-25807.5}

where

\[
\log\mathcal C_{K,J}=o_K(J).
\tag{L-25807.6}
\]

Equivalently, the largest generalized eigenvalue of the pair

\[
(P_S^*\mathcal G_J^\nabla P_S,
 P_S^*W_JP_S)
\]

is subexponential.

The certificate is required only on the actual flow subspace. It is not a
uniform estimate for arbitrary coefficient vectors.

## 4. Carry transport implication

Suppose a signed source flow satisfies the exact divergence and scale-routing
conditions of `D-25801` and its scalar carry cost obeys

\[
F^*W_JF
\le
\exp\{(\sigma_K+o_K(1))J\}
\left[
1+
\max_{u\le(1-\delta)J+C_K}E_K(u)
\right].
\tag{L-25807.7}

Then the Transport Frame LMI gives

\[
\boxed{
F^*\mathcal G_J^\nabla F
\le
\exp\{(\sigma_K+o_K(1))J\}
\left[
1+
\max_{u\le(1-\delta)J+C_K}E_K(u)
\right],}
\tag{L-25807.8}

where the `o_K(J)` term absorbs `log C_(K,J)`.

Thus a signed constraint-dipole transport theorem with

\[
\sigma_K\to0
\]

plus a Transport Frame certificate supplies the quadratic PADT cost.

## 5. Exact proof object

The finite certificate exports:

```text
source Gram K_J
adjacent incidence B_J
flow-subspace basis P_S
positive diagonal weight W_J
candidate generalized-eigenvalue ceiling C_(K,J)
LDL/SOS/interval proof of
C_(K,J) P_S^*W_JP_S - P_S^*B_J^*K_JB_JP_S >= 0
```

The checker rejects a singular weight direction unless the corresponding
physical current is exactly zero.

## 6. Why a generic proof is unavailable

For arbitrary vectors, a diagonal domination may lose the number of edges or
the full coherent rank of the Möbius hypercube. The known hypercube therefore
rules out claiming (L-25807.5) on the whole ambient space with a uniform small
constant.

The proposed reserve comes from the exact divergence, cluster, and depletion
constraints defining `S_J`. If those constraints do not lower the generalized
eigenvalue, the PADT mechanism fails.

## 7. Proof boundary

Closed exactly:

- the weight inequality `h_j^2<=omega_j`;
- the incidence representation of the physical flow Gram;
- the abstract implication from the Transport Frame LMI and scalar carry cost to
  the PADT quadratic cost.

Open:

- a production subexponential Transport Frame certificate;
- a signed scalar flow of subexponential carry cost on the actual source graph;
- `PADT(K)` or RH.
