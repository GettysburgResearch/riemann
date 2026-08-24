# T-105290 — Source-paid owner-conductor Hankel frontier for ninety percent

Claim ID: `T-105290`  
Status: **EXACT UNCONDITIONAL REDUCTION; COHERENT HANKEL ESTIMATE OPEN**  
Created: 2026-08-24  
Corrected: 2026-08-24  
Depends on: `L-105280--L-105293`; PR #726 finite-α folding/bank realization; PR #751 square-phase owner-conductor family  
RH status: **unproved**

## 1. Actual five-rung topological defect

Let

\[
\mathbb U_{5,T}
 =\operatorname{diag}(U_{1,T},\ldots,U_{5,T})
\]

be the block of normalized adjacent Xi companion all-pass quotients on a
regular dyadic window. Put

\[
\mathfrak H_5(T)=\|H_{\mathbb U_{5,T}}\|_{\mathcal S_2}^2.
\tag{T-105290.1}
\]

By `L-105290`, exact reverse Rolle gives

\[
R_0(T,2T)
 \ge R_5(T,2T)-\mathfrak H_5(T)-O(1).
\tag{T-105290.2}
\]

Consequently the unconditional Conrey input

\[
\liminf \frac{R_5(T,2T)}{N(T,2T)}>\frac{997}{1000}
\]

shows that

\[
\boxed{
\limsup_{T\to\infty}
\frac{\mathfrak H_5(T)}{N(T,2T)}
<\frac{97}{1000}
\quad\Longrightarrow\quad
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{T-105290.3}
\]

This is a multiplicity-aware critical-line count; the standard adjacent
zero-count comparison contributes only \(o(N)\).

## 2. Prescribed source packets and exact coherent ledger

Use the finite-α oriented ratio of `L-105291`, the two-boundary realization of
PR #726 and the degree-five source bank of `L-105293`. Before physical owner
labels are forgotten, let

\[
\{\mathcal H_{i,T}:i\in\mathcal I_T\}
\subset\mathcal S_2
\]

be the finite source-owned Hankel packets indexed by

```text
derivative rung;
owner pair and opposite owner conductor;
quadratic owner sector sigma;
nonzero square phase / even character;
physical shell and frozen Vaughan block;
orientation and taper label.
```

They are fixed by the source construction, not chosen after the zero signs are
known. Define the exact remainder

\[
\mathcal R_T
 =H_{\mathbb U_{5,T}}-
  \sum_{i\in\mathcal I_T}\mathcal H_{i,T}.
\tag{T-105290.4}
\]

The phase-family diagonal and positive coherent cross ledger are

\[
\mathfrak D_T=\sum_i\|\mathcal H_{i,T}\|_{\mathcal S_2}^2,
\tag{T-105290.5}
\]

\[
\mathfrak C_T^+
 =2\sum_{i<j}
 \left(
 \operatorname{Re}\operatorname{tr}
 (\mathcal H_{i,T}^*\mathcal H_{j,T})
 \right)_+.
\tag{T-105290.6}
\]

Let \(\mathfrak S_T\) denote the complete five-rung **unphased frozen Wick
source energy**. By `L-105293`,

\[
\boxed{
\mathfrak S_T
 \le\left(\frac1{3700}+o(1)\right)N(T,2T).
}
\tag{T-105290.7}
\]

The exact phase-family diagonal excess is

\[
\boxed{
\mathfrak P_T=(\mathfrak D_T-\mathfrak S_T)_+.
}
\tag{T-105290.8}
\]

Thus \(\mathfrak D_T\le\mathfrak S_T+\mathfrak P_T\). The local contraction
of `L-105292` removes phase-cardinality loss packetwise, but does **not** by
itself prove \(\mathfrak P_T=o(N)\); the owner-character family energy remains
in the ledger.

For every \(\varepsilon>0\), put

\[
\boxed{
\begin{aligned}
\mathfrak A_T(\varepsilon)
={}&\varepsilon\mathfrak S_T
 +(1+\varepsilon)(\mathfrak P_T+\mathfrak C_T^+)\\
&+(1+\varepsilon^{-1})\|\mathcal R_T\|_{\mathcal S_2}^2.
\end{aligned}
}
\tag{T-105290.9}
\]

The Hilbert inequality

\[
\|x+y\|^2\le(1+\varepsilon)\|x\|^2
 +(1+\varepsilon^{-1})\|y\|^2
\]

and deletion only of negative cross terms give

\[
\begin{aligned}
\mathfrak H_5(T)
&\le(1+\varepsilon)(\mathfrak D_T+\mathfrak C_T^+)
 +(1+\varepsilon^{-1})\|\mathcal R_T\|_{\mathcal S_2}^2\\
&\le\boxed{\mathfrak S_T+\mathfrak A_T(\varepsilon).}
\end{aligned}
\tag{T-105290.10}
\]

No orthogonality between distinct physical owner packets is assumed.

## 3. What is already paid

`L-105292` applies the exact square-phase owner contraction in the Hilbert
space of Hankel operators. It removes every local phase-cardinality factor and
retains the principal/quadratic root fibre, the two owner quadratic sectors and
all even-character channels.

`L-105293` pays the unphased five-rung source energy (T-105290.7). Therefore
the remaining allowance above a ninety-percent target is

\[
\boxed{
\frac{997}{1000}-\frac9{10}-\frac1{3700}
 =\frac{3579}{37000}
 =0.0967297297\ldots .
}
\tag{T-105290.11}
\]

The owner-character diagonal excess, coherent cross terms and actual-Xi
transfer are **not** included in the paid \(1/3700\); all three occur in
\(\mathfrak A_T\).

## 4. Single fixed-constant frontier

Define

\[
\boxed{
\mathrm{HOCH}_{105290}:\quad
\text{there exist }\varepsilon_T>0\text{ such that }
\limsup_{T\to\infty}
\frac{\mathfrak A_T(\varepsilon_T)}{N(T,2T)}
<\frac{3579}{37000}.
}
\tag{T-105290.12}
\]

Then (T-105290.7), (T-105290.10) and (T-105290.11) imply
(T-105290.3), and hence

\[
\boxed{
\mathrm{HOCH}_{105290}
\Longrightarrow
\liminf_{T\to\infty}\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{T-105290.13}
\]

`HOCH105290` is a fixed constant estimate, not an RH-strength subpower
estimate. The subpower principal and nonprincipal owner-conductor moments
`PCM106030/NEM106030` on PR #751 would be far stronger than required here.

## 5. Exact content of the open term

The four terms in (T-105290.9) have distinct ownership:

```text
epsilon * unphased frozen source:
  harmless Hilbert-inequality payment;

phase-family diagonal excess:
  the exact cost of resolving the unphased source into its complete
  owner-conductor square-phase/even-character family;

positive cross-owner Hankel Gram:
  coherent physical assembly across different owner packets/conductors;

actual-source remainder:
  finite-alpha archimedean freezing, complete contour exhaustion,
  shell/taper limits, and every near-real Blaschke phase slip not represented
  by the frozen owner-conductor packets.
```

The firewall `R-105290` prohibits replacing the last three terms by packetwise
local contraction.

## Hostile correction

An earlier version of this checkpoint identified \(\mathfrak D_T\) itself
with the \(1/3700\) frozen source bound. That was too strong: `L-105293` proves
the unphased frozen energy, while the complete phase-family diagonal is an
additional positive owner-conductor moment. Equations (T-105290.8)--
(T-105290.12) are the controlling corrected formulation.

## Boundary

```text
matrix all-pass winding/Hankel payment             PROVED EXACT
finite-alpha oriented-ratio identification         PROVED EXACT
local square-phase contraction in Hankel space     PROVED EXACT
unphased five-rung frozen cost < 1/3700             PROVED EXACT
phase-family diagonal excess                       OPEN / EXPLICIT
fixed remaining allowance 3579/37000               PROVED EXACT
HOCH105290 coherent/transfer estimate               OPEN / RECORD-BEARING
ninety percent for zeta                            UNPROVED
density one / RH                                   UNPROVED
```
