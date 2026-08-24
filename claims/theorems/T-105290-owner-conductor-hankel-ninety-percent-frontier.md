# T-105290 — Source-paid owner-conductor Hankel frontier for ninety percent

Claim ID: `T-105290`  
Status: **EXACT UNCONDITIONAL REDUCTION; COHERENT HANKEL ESTIMATE OPEN**  
Created: 2026-08-24  
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

The diagonal and positive coherent cross ledger are

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

For every \(\varepsilon>0\), put

\[
\boxed{
\mathfrak A_T(\varepsilon)
 =\varepsilon\mathfrak D_T
 +(1+\varepsilon)\mathfrak C_T^+
 +(1+\varepsilon^{-1})\|\mathcal R_T\|_{\mathcal S_2}^2.
}
\tag{T-105290.7}
\]

The Hilbert inequality

\[
\|x+y\|^2\le(1+\varepsilon)\|x\|^2
 +(1+\varepsilon^{-1})\|y\|^2
\]

and deletion only of negative cross terms give the exact bound

\[
\boxed{
\mathfrak H_5(T)
 \le\mathfrak D_T+\mathfrak A_T(\varepsilon).
}
\tag{T-105290.8}
\]

No orthogonality between distinct physical owner packets is assumed.

## 3. What is already paid

`L-105292` applies the exact square-phase owner contraction in the Hilbert
space of Hankel operators. It removes every local phase-cardinality factor and
retains the principal/quadratic root fibre, the two owner quadratic sectors and
all even-character channels.

`L-105293` gives, on the complete five-rung frozen source,

\[
\boxed{
\mathfrak D_T
 \le\left(\frac1{3700}+o(1)\right)N(T,2T).
}
\tag{T-105290.9}
\]

Thus the actual source has paid all but

\[
\boxed{
\frac{97}{1000}-\frac1{3700}
 =\frac{3579}{37000}
 =0.0967297297\ldots
}
\tag{T-105290.10}
\]

of the available ninety-percent defect budget.

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
\tag{T-105290.11}
\]

Then (T-105290.8)--(T-105290.10) imply (T-105290.3), and hence

\[
\boxed{
\mathrm{HOCH}_{105290}
\Longrightarrow
\liminf_{T\to\infty}\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{T-105290.12}
\]

`HOCH105290` is a fixed constant estimate, not an RH-strength subpower
estimate. The subpower principal and nonprincipal owner-conductor moments
`PCM106030/NEM106030` on PR #751 would be far stronger than required here.

## 5. Exact content of the open term

The three terms in (T-105290.7) have distinct ownership:

```text
epsilon * diagonal:
  harmless optimization payment;

positive cross-owner Hankel Gram:
  coherent physical assembly across different owner packets/conductors;

actual-source remainder:
  finite-alpha archimedean freezing, complete contour exhaustion,
  shell/taper limits, and every near-real Blaschke phase slip not represented
  by the frozen owner-conductor packets.
```

The firewall `R-105290` prohibits replacing the coherent term by packetwise
local contraction.

## Boundary

```text
matrix all-pass winding/Hankel payment             PROVED EXACT
finite-alpha oriented-ratio identification         PROVED EXACT
local square-phase contraction in Hankel space     PROVED EXACT
five-rung frozen source cost < 1/3700              PROVED EXACT
fixed remaining allowance 3579/37000               PROVED EXACT
HOCH105290 coherent/transfer estimate               OPEN / RECORD-BEARING
ninety percent for zeta                            UNPROVED
density one / RH                                   UNPROVED
```
