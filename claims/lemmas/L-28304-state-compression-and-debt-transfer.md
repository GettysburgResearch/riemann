# L-28304 — State compression transfers Gamma transport to Pascal debt

Claim ID: `L-28304`
Title: A sufficient finite bridge for SAPC: compressing the Markov Gamma–carry state to a half-scale Pascal debt process
Status: **PROPOSED REDUCTION — LOAD-BEARING CONTRACTION STEP OPEN**
Authoring agent: `gpt56-pro-22`
Created: 2026-08-08
Issue: #283
Dependencies: `L-28301`, `L-28302`, PR #272 `L-27204/L-27205`

## 1. The observation

The remaining SAPC theorem should not attempt to discretize the entire Gamma residual. The exact Markov coupling has too much state. The finite Pascal system only sees two projections:

1. the carry-column image;
2. the weighted negative capacity debt.

For a state cell `C` in the Gamma–carry partition, define its projected debt atom

\[
\delta(C)=\inf_d \sum_e \omega_e(-d_e)_+
\]

where the infimum is over all balanced Pascal corrections preserving the exact carry image of that cell.

The key compression target is:

\[
\boxed{\delta(C)\text{ depends only on the half-scale divisor source }\sigma_C(h).}
\]

This replaces the full continuous state by the finite divisor transport state of `L-28302`.

## 2. Why this projection is natural

The Markov coupling supplies

\[
g=p\mathcal K.
\]

The finite central cascade supplies

\[
\mathcal T_X=\mathcal T+\mathcal E.
\]

The only non-positive part of the finite realization is therefore the commutator

\[
(\mathcal E r)(q)=\sum_{q\mid h}\sigma(h).
\]

The state variable that survives both maps is exactly the divisor source `sigma`.

Any proposed SAPC certificate should therefore export:

```text
Markov cell
 -> divisor source sigma
 -> Pascal cycle coordinates
 -> capacity debt
```

rather than

```text
Markov cell
 -> individual split edge
```

which is unnecessarily large.

## 3. Candidate contraction theorem

Define `D_j` as the optimized debt after this compression at cascade stage `j`.

A sufficient theorem is:

\[
\boxed{
D_{j+1}
\le
(1-\log 2+o(1))D_j
+O(\log^A X).
}
\]

The coefficient is suggested by the exact continuum residual mass identity

\[
\|\mathcal T f\|_1=(1-\log2)\|f\|_1.
\]

The finite correction is entirely concentrated in the adjacent divisor transport
of `L-28302`.

## 4. New proof route

Instead of proving SAPC directly:

```text
all Markov cells
 -> all split edges
 -> all cycle coefficients
 -> debt recurrence
```

prove the shorter chain:

```text
Markov coupling
 -> divisor-source compression
 -> half-scale transport recurrence
 -> Pascal debt recurrence
```

The first arrow is exact algebra. The last two arrows are the sole open arithmetic estimates.

## 5. Proof boundary

Closed:

- the Gamma carry state;
- the exact lattice divisor source;
- sibling-switch realization;
- the Pascal debt metric.

Open:

- proving that compression loses at most a contracting fraction of debt;
- SAPC;
- RH.
