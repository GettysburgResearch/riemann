# R-93900 — One rank-one Volterra channel cannot simultaneously carry the SHARP target and score

Claim ID: `R-93900`  
Status: **PROVED EXACT TWO-POINT TYPE SEPARATOR**  
Created: 2026-08-16  
Frozen comparison: PR #509 at `e01daee9cdfea35d2a7d2591f1df6c8080084119`  
RH status: **unproved**

## 1. The row-first scalar

For `1<=k<=x`, put

\[
e_x(k)=\frac1{\sqrt k}\left(2\sqrt{\frac xk}-1\right)
      =\frac{2\sqrt x}{k}-\frac1{\sqrt k}.
\]

The Volterra order swap correctly proves that the component-row colour at a
fixed endpoint is `e_x(k)` times one common positive infinitesimal row packet.
That is an exact **row** factorization.

A complete typed source compiler would additionally need constants independent
of `k` carrying the SHARP target and declared score

\[
T_x(k)=\frac{4\sqrt{x/k}-3}{\sqrt k},
\qquad
S_x(k)=\frac{5\sqrt{x/k}-3}{\sqrt k}.
\]

## 2. Exact target separator at `x=2`

At `k=2`,

\[
e_2(2)=T_2(2)=\frac1{\sqrt2}.
\]

Thus a common scalar target feature `tau` satisfying

\[
T_2(k)=\tau e_2(k)
\]

for both active colours would have to satisfy `tau=1`.  At `k=1`, however,

\[
T_2(1)-e_2(1)
=(4\sqrt2-3)-(2\sqrt2-1)
=2(\sqrt2-1)>0.
\]

Therefore no such common target feature exists.

## 3. Exact score separator

At `k=2`,

\[
S_2(2)=2e_2(2),
\]

so a common score feature would have to equal two.  At `k=1`,

\[
S_2(1)-2e_2(1)
=(5\sqrt2-3)-(4\sqrt2-2)
=\sqrt2-1>0.
\]

Thus one common rank-one source channel cannot carry the score either.

## 4. Disposition

This does **not** refute the Volterra component-row identity, the positive
infinitesimal row, or PR #509's finite/continuum split.  It refutes only the
promotion

```text
common row scalar e_x(k)
        ->
one complete target/score/row source feature independent of k.
```

It also explains the score obstruction reconstructed in review PR #501: an
edge coupling between source atoms with different score-per-target ratios cannot
be treated as a target-null positive complete packet with exact score.

The exact repair is the unique two-channel factorization of `L-93900`.

```text
rank-one component-row factorization       retained
single-channel SHARP target factorization  false
single-channel SHARP score factorization   false
exact separator domain                     x=2, k=1,2
repair                                     equality/reserve two channels
Riemann Hypothesis                         unproved
```
