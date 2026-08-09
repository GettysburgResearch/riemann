# L-34405 — Odd-prime Jordan deformation commutes with the compact parity synthesis

Claim ID: `L-34405`  
Title: Freezing the dyadic filters and deforming only the odd Euler core makes the compact Q=4/parity synthesis parameter-independent at every Jordan order; the full compact current is the odd Jordan first jet plus one finite bare-source gauge  
Status: **PROPOSED COMPLETE EXACT ALL-ORDER DIRICHLET/FILTER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #346 `L-34401`; PR #329 `L-32306`; elementary Euler algebra  
Scope: exact all-order odd-prime deformation and fixed synthesis; no relative curvature upper bound or RH claim

## 1. Common odd Euler core

Put

\[
 z=2^{-s},
 \qquad
 \mathcal O(s)=\prod_{p\ {m odd}}(1-p^{-s}),
 \qquad
 A_{\rm odd}(s)=\mathcal O(s)^{-1}.
\]

Retain the parity polynomials

\[
 p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2,
\]

and the compact polynomial

\[
 T(z)=(1-z)(1-4z^2).
\]

Then

\[
 B_+(s)=p(z)\mathcal O(s),
 \qquad
 B_-(s)=p(-z)\mathcal O(s),
\tag{L-34405.1}
\]

and

\[
 B_\circ(s)=T(z)\mathcal O(s)
 ={1-4^{1-s}\over\zeta(s)}.
\tag{L-34405.2}
\]

PR #346 `L-34401` supplies fixed polynomials `W_+,W_-` such that

\[
\boxed{
 W_+(z)p(z)+W_-(z)p(-z)=T(z).
}
\tag{L-34405.3}
\]

The critical squared synthesis charge is strictly below `2/5` of the declared parity analysis reserve.

## 2. Odd-prime Jordan deformation

For `tau>=0` define

\[
\boxed{
 J_{{\rm odd},\tau}(s)
 ={A_{\rm odd}(s-\tau)\over A_{\rm odd}(s)}
 ={\mathcal O(s)\over\mathcal O(s-\tau)}.
}
\tag{L-34405.4}
\]

At an odd prime `p`, with `a=p^tau>=1`, the local factor is

\[
 {1-p^{-s}\over1-p^{\tau-s}}
 =1+{(a-1)p^{-s}\over1-ap^{-s}}.
\]

Hence

\[
\boxed{
 J_{{\rm odd},\tau}(p^k)
 =(p^\tau-1)p^{\tau(k-1)}\ge0
 \qquad(k\ge1),
}
\tag{L-34405.5}
\]

while the prime-two local factor is identically one. Multiplicativity gives

\[
\boxed{
 J_{{\rm odd},\tau}(n)\ge0
 \qquad(n\ge1,\tau\ge0),
}
\tag{L-34405.6}
\]

with support on odd integers.

Coefficientwise differentiation at zero gives

\[
\boxed{
 J_{{\rm odd},0}=\varepsilon,
 \qquad
 \partial_\tau J_{{\rm odd},\tau}|_0=\Lambda_{\rm odd},
 \qquad
 \partial_\tau^2J_{{\rm odd},\tau}|_0=C_{\rm odd},
}
\tag{L-34405.7}
\]

where

\[
 C_{\rm odd}
 =\Lambda_{\rm odd}\log
  +\Lambda_{\rm odd}*\Lambda_{\rm odd}.
\]

These are exactly the ordinary odd-prime Kummer/Selberg first two moments used in PR #337/#346.

## 3. Deformed source paths

Define

\[
\boxed{
 \mathcal B_{+,\tau}=B_+J_{{\rm odd},\tau},
 \qquad
 \mathcal B_{-,\tau}=B_-J_{{\rm odd},\tau},
 \qquad
 \mathcal B_{\circ,\tau}=B_\circ J_{{\rm odd},\tau}.
}
\tag{L-34405.8}
\]

The crucial point is that the dyadic polynomials `p(+-z),T(z),W_+-,` are **not** deformed. Multiplying (L-34405.3) by the common factor `O J_(odd,tau)` gives, for every `tau>=0`,

\[
\boxed{
 \mathcal B_{\circ,\tau}
 =W_+(z)\mathcal B_{+,\tau}
  +W_-(z)\mathcal B_{-,\tau}.
}
\tag{L-34405.9}
\]

This is an all-order source identity, not a first-jet approximation.

## 4. Every Jordan jet synthesizes with the same filter

Because `W_+,W_-` are independent of `tau`, coefficientwise differentiation of (L-34405.9) gives for every integer `r>=0`

\[
\boxed{
 \partial_\tau^r\mathcal B_{\circ,\tau}|_0
 =W_+(z)\,
   \partial_\tau^r\mathcal B_{+,\tau}|_0
 +W_-(z)\,
   \partial_\tau^r\mathcal B_{-,\tau}|_0.
}
\tag{L-34405.10}
\]

There is **no derivative gauge at any order**.

In particular, the odd-prime first-current jets satisfy

\[
\boxed{
 B_\circ\Lambda_{\rm odd}
 =W_+(z)B_+\Lambda_{\rm odd}
  +W_-(z)B_-\Lambda_{\rm odd},
}
\tag{L-34405.11}
\]

and the odd-prime second-current jets satisfy the identical synthesis with `C_odd`.

Thus the same strict finite filter of PR #346 acts on the complete odd-prime Jordan curvature, not merely on its first current derivative.

## 5. Odd Jordan row reserve is exactly the critical-scale arithmetic reserve

For one carry row `e=(n,j)`, put

\[
 F_{{\rm odd},e}(\tau)
 =1+\mathcal L_e(J_{{\rm odd},\tau}).
\tag{L-34405.12}
\]

Then

\[
\boxed{
 F_{{\rm odd},e}'(0)
 =O(n,j)
 =\log\operatorname{odd}{n\choose j},
}
\tag{L-34405.13}
\]

and

\[
\boxed{
 F_{{\rm odd},e}''(0)=S_{\rm odd}(n,j).
}
\tag{L-34405.14}
\]

Hence

\[
\boxed{
 -\bigl(\log F_{{\rm odd},e}\bigr)''(0)
 =R_{\rm odd}(n,j)
 :=O(n,j)^2-S_{\rm odd}(n,j).
}
\tag{L-34405.15}
\]

For the aligned scale ratio

\[
 H_{{\rm odd},e}(\tau)
 ={F_{{\rm odd},4e}(\tau)
   \over F_{{\rm odd},e}(4\tau)},
\]

one has exactly

\[
\boxed{
 -\bigl(\log H_{{\rm odd},e}\bigr)''(0)
 =\Delta_4R_{\rm odd}(e).
}
\tag{L-34405.16}
\]

PR #346 proves on every fixed balanced cone, cofinally,

\[
\boxed{
 \Delta_4R_{\rm odd}(e)=\Theta_\eta(n\log n),
}
\tag{L-34405.17}
\]

with an explicit positive lower constant. Therefore the all-order gauge-free deformation is aligned with the already-established **critical-scale** reserve rather than the oversized full parity reserve.

## 6. Relation to the full compact `s`-current

The physical compact source is

\[
 B_\circ(s)=T(z)\mathcal O(s).
\]

Differentiate with respect to `s`. Since

\[
 \mathcal O'(s)
 =\mathcal O(s)\Lambda_{\rm odd}(s),
\]

one gets the exact decomposition

\[
\boxed{
 q_\circ(s)=B_\circ'(s)
 =B_\circ(s)\Lambda_{\rm odd}(s)
  +T'(s)\mathcal O(s).
}
\tag{L-34405.18}
\]

The first term is precisely the first odd-Jordan jet in (L-34405.11). The second is a **fixed finite dyadic polynomial times the bare odd Euler source**:

\[
 T'(s)
 =(\log2)z(1+8z-12z^2).
\tag{L-34405.19}
\]

Thus every RH-sensitive logarithmic derivative has been separated into

```text
odd-prime Jordan current:
    all-order gauge-free fixed parity synthesis;

finite dyadic gauge:
    one fixed polynomial acting on the bare odd source.
```

The matching augmented parity curvature of PR #329 `L-32306` already contains both parity current and parity bare-source coordinates with coefficient one. Therefore the finite gauge in (L-34405.18) introduces no new source species.

## 7. Why this is stronger than differentiating the original synthesis

PR #346 `L-34401` differentiates the full source identity in `s`; because `z=2^-s` moves, derivative gauges appear and must be factored into delayed Möbius states.

The odd-prime Jordan parameter `tau` does not move `z`. Consequently (L-34405.10) commutes with **every** Jordan derivative and has no gauge at all. The critical odd-prime reserve increment, current jet, second-current jet, and all higher source moments therefore live in one fixed finite analysis/synthesis geometry.

This is the natural deformation for any future curvature-level frame theorem.

## 8. What remains

The theorem removes the all-order source-typing/gauge problem. It does not by itself imply that a first-derivative frame bound controls a second-order curvature.

The remaining conclusion-producing theorem can now be stated sharply:

> **Odd-core relative curvature frame.**  Apply the fixed parity synthesis (L-34405.9) to the relative odd-Jordan source-convolved paths at scales `e` and `4e`, retaining the matching bare-source coordinate. Prove that the compact output relative curvature is bounded by a fixed multiple of the input matching parity relative curvature plus finite delayed collars.

Because the scalar reserve of that relative input is already `Theta(n log n)`, such a curvature-frame theorem would give the required critical innovation bound and the coefficient-one recurrence.

No source-dependent derivative gauge remains to be estimated inside that theorem.

## 9. Proof boundary

Closed exactly here:

1. positive odd-prime Jordan deformation;
2. exact all-order compact/parity synthesis with parameter-independent filters;
3. gauge-free synthesis of every odd Jordan jet;
4. identification of the odd reserve and its radix-four relative curvature;
5. exact decomposition of the full compact `s`-current into the odd first jet plus one finite bare-source gauge;
6. compatibility with the matching augmented parity source state.

Still open:

1. the relative curvature-frame / Hermitian Schur inequality;
2. critical innovation energy recurrence;
3. global subpower pole energy;
4. RH.
