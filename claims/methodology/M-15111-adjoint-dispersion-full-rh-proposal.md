# M-15111 — Adjoint-dispersion full RH proposal

Methodology ID: `M-15111`  
Title: Replace the false universal Selberg inverse by an orientation-correct finite prime-dispersion recursion  
Status: **FULL RH PROPOSAL — ONE SOURCE-SPECIFIC BALANCED TYPE-II RECURRENCE OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Review input: PR #158 at `668f10a87eb8b8d0521edf8b5156334e287747f0`; PR #216 frozen at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Dependencies: `L-15151`, `L-15152`, `L-15153`, `T-15120`; PR #216 `T-21502/L-21504`  
Scope: repaired post-review proposal; RH is not claimed proved

## 1. Strategic replacement

The second-pass review establishes that the original Selberg–Mourre completion cannot be repaired by adding one abstract Poincare inequality:

1. the universal block-normalized inverse is false for the number model and for the actual compressed Selberg operator;
2. the second-order `Lambda_2` term is product-dilational;
3. PR #216's positive prime Gram is adjoint/factor-ratio geometry;
4. scalar coefficient positivity does not turn the product channel positive;
5. continuous Hardy averaging is a genuine bulk operator unless separately localized.

`L-15152` now writes the complete product-dilation ledger exactly and exposes its negative bulk masses. This proposal does **not** try to make that indefinite ledger coercive.

Instead it uses the orientation in which positivity is genuine from the start: the finite prime-only block Gram of PR #216.

## 2. Exact front door

Let `H` be the compact prime-only safe window of `T-21502` and define

\[
 Q_H^{\mathbb P}(x)
 =\sum_p{\log p\over\sqrt p}H(x-\log p).
 \tag{M-15111.1}
\]

`L-15151` closes the Hardy interface:

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 {\log\left(1+\int^X|Q_H^{\mathbb P}(x)|^2dx\right)
  \over2X}.}
 \tag{M-15111.2}
\]

Therefore

\[
 \mathrm{RH}
 \iff
 \int^X|Q_H^{\mathbb P}(x)|^2dx=\exp(o(X)).
 \tag{M-15111.3}
\]

For each integer block `J`,

\[
 \mathcal B_J
 =\int_J^{J+1}|Q_H^{\mathbb P}(x)|^2dx
 \tag{M-15111.4}
\]

is one finite positive Gram over ordinary primes only.

## 3. Exact source centering

Let

\[
 d\nu_{\mathbb P}(u)
 =\sum_p{\log p\over\sqrt p}\delta_{\log p}(du)
 -e^{u/2}du.
 \tag{M-15111.5}
\]

`L-15153` proves

\[
 \boxed{
 \mathcal B_J
 =\iint K_J(u,v)
 d\nu_{\mathbb P}(u)d\nu_{\mathbb P}(v),}
 \tag{M-15111.6}
\]

where

\[
 K_J(u,v)=\int_J^{J+1}H(x-u)H(x-v)dx.
\]

The kernel annihilates both

\[
 1
 \quad\text{and}\quad
 e^{u/2}
 \tag{M-15111.7}
\]

in each factor. Thus the continuous main density and every discrete/continuous cross term vanish exactly before estimation.

This is the correct source-specific cancellation. It does not invoke a universal inverse, a zero expansion, or a continuous Hardy remainder.

## 4. Finite balanced semiprime form

Split

\[
 \mathcal B_J=\mathcal D_J+\mathcal O_J.
 \tag{M-15111.8}
\]

The diagonal is polynomial in `J`. PR #216 `L-21504` gives the exact off-diagonal identity

\[
 \boxed{
 \mathcal O_J
 =\sum_{p<q}
 {\Lambda_2(pq)\over\sqrt{pq}}
 K_J(\log p,\log q),
 \qquad
 \Lambda_2(pq)=2\log p\log q.}
 \tag{M-15111.9}
\]

Only primes in one finite interval around `e^J` occur, and `p/q` lies in one fixed compact ratio range. Hence each row is a finite balanced Type-II sum.

Unlike the old product-dilation channel, (M-15111.9) is literally the cross term of a positive adjoint square. No orientation conversion is required.

## 5. Proposed local dispersion mechanism

The compact ratio range is divided into finitely many smooth sectors. In one sector write

\[
 p\asymp P,
 \qquad q\asymp Q,
 \qquad P/Q\asymp1.
\]

The kernel is an explicit piecewise polynomial in `log p-log q`. The proof is to proceed in the following order.

### 5.1 Center before decomposition

Insert the signed measure `nu_P` from (M-15111.5) in both variables. Do not apply total variation. Because of the two exact null modes, the continuous main/main and main/error channels vanish algebraically.

### 5.2 Use an exact finite prime decomposition

Replace the ordinary-prime weights by a source-bound Vaughan or Heath–Brown identity on the finite interval, retaining prime-power correction rows separately. Every term is then a finite Type-I or balanced Type-II form with the original signed kernel.

The decomposition must be exact at the declared endpoint convention; an asymptotic replacement of `Lambda` is insufficient.

### 5.3 Preserve the adjoint square

For each Type-II row, keep the factor variables on opposite sides of the Gram:

\[
 \left\|
  \sum_m a_m\,\tau_{\log m}H_J
 \right\|_2^2
 \quad\text{or its polarized cross form}.
 \tag{M-15111.10}
\]

No product-dilation substitution is permitted. The multiplicative large sieve or dispersion step must act on the factor-ratio phase.

### 5.4 Route cutoff leakage to earlier blocks

The only feedback term is produced by finite block cutoffs and the ends of the compact support. Those rows involve a strictly smaller logarithmic endpoint and are assigned to

\[
 \max_{k<J}\mathcal B_k.
\]

The target is to prove that their total normalized coefficient is eventually below one.

## 6. Load-bearing arithmetic theorem

The exact proposed estimate is

\[
 \boxed{
 [\mathcal O_J]_+
 \le C(1+J)^A
 +\eta_J\max_{J_0\le k<J}\mathcal B_k,
 \qquad
 \limsup_{J\to\infty}\eta_J<1.}
 \tag{M-15111.11}
\]

Every quantity in (M-15111.11) is a finite source-bound prime computation. There is no statement for arbitrary vectors.

`T-15120` proves rigorously that (M-15111.11) gives a polynomial block envelope and hence RH.

## 7. Finite proof object for one row

A production certificate at block `J` should contain:

```text
safe-window SHA-256
complete ordinary-prime manifest
strictly ordered kernel breakpoints
exact/outward block Gram
diagonal ledger
balanced squarefree-semiprime ledger
centered Vaughan/Heath-Brown rows
Type-I and Type-II dual/large-sieve bounds
lower-block leakage coefficients eta_(J,k)
eta_J=sum_k eta_(J,k)
final upper interval for [O_J]_+
```

The checker must reject:

- omitted prime powers in a decomposition of `Lambda`;
- replacement of the centered signed measure by total variation;
- product-dilation/factor-ratio substitution;
- unbound kernel or prime-manifest changes;
- inference from a finite ladder to the cofinal recurrence.

## 8. Relation to the causal Chebyshev/Selberg work

The exact Chebyshev and Selberg files remain useful in two roles:

1. they give an independent RH-equivalent energy and finite integer producer;
2. their multiplicative cocycle nominates the lower-block routing in (M-15111.11).

They are not used to manufacture positivity for (M-15111.9). The causal product-dilation ledger and the compact adjoint Gram are retained as distinct geometries.

A future exact intertwiner may connect them, but the present proposal does not assume one.

## 9. What has been repaired

Closed in this pass:

1. the explicit Hardy `H2` transfer requested by both reviews (`L-15151`);
2. the complete product-dilation and mixed-term algebra (`L-15152`);
3. honest negative bulk accounting in that algebra;
4. exact double centering of the prime-only block (`L-15153`);
5. an orientation-correct finite recurrence theorem (`T-15120`);
6. removal of all universal inverse, boundary-rank, and direct-PR-216-factor-map claims.

## 10. Exact independent-review hinge

The sole remaining proposed theorem in this repaired architecture is the source-specific balanced dispersion recurrence (M-15111.11), including an exact derivation of the leakage coefficient `eta_J` from a finite Vaughan/Heath–Brown decomposition.

A reviewer should either:

1. construct those rows and prove `limsup eta_J<1`;
2. find a finite source-bound row contradicting the proposed routing;
3. prove that standard Type-II estimates necessarily lose too much, thereby rejecting this completion mechanism.

Failure does not affect `L-15151`--`L-15153`, the exact Chebyshev/Selberg front half, or PR #216's finite identities.

## 11. Status boundary

This is a full **proposal**, not a completed proof. RH is not claimed proved.

The repaired chain is

```text
ordinary-prime safe signal
-> exact Hardy exponent
-> finite doubly centered ratio Gram
-> balanced semiprime Type-II recurrence
-> polynomial block energy
-> RH.
```

All arrows except the Type-II recurrence are supplied explicitly.