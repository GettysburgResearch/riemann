# O-90209 — Ordered quarter-balanced hinge reconnaissance: zero negatives through large depth, while generic step targets fail exactly

Claim ID: `O-90209`  
Status: **FINITE RECONNAISSANCE + ONE EXACT MUTATION; NO COFINAL CLAIM**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90209`, `T-90205`  
Scope: discovery evidence and review tests only

## 1. Why this scan was run

`T-90204` refutes the frozen half-binary/half-ternary producer by a deterministic
near-critical resonance.  The ordered policy of `L-90209` uses a broad interval
of balanced splits and has a nonlattice continuum spectral gap.  The remaining
question is arithmetic: does its Green occupation stay nonnegative for the
square-root hinge source?

The scan deliberately tests both the desired hinge family and nearby target
classes which **should not** be automatically positive.

## 2. Exhaustive square-root hinge sweep

For each integer

\[
 3\le T\le2000,
\]

the verifier forms

\[
 h_T(q)=q^{-1/2}-T^{-1/2}
\]

on `2<=q<=T`, computes the exact Möbius-divergence formula in floating
high-accuracy arithmetic, and propagates the ordered-policy occupation by the
linear-time sliding-band recurrence `L-90209.5`.

Result:

```text
endpoints tested                         1,998
negative occupation coordinates              0
```

The terminal coordinate `M_T=0` is forced because `h_T(T)=0`.  Excluding that
zero, the smallest observed positive occupation in the exhaustive sweep is

```text
T = 2000,
n = 1999,
M_n = 0.011178941995514106...
```

No finite sign theorem is inferred.

## 3. Large hinge spot checks

The same recurrence was checked at

```text
T = 10^3,
    10^4,
    10^5,
    10^6,
```

with zero negative coordinates.  The bottom occupations were respectively
approximately

```text
M_2 = 0.8288315027101476
      0.8538543363170702
      0.8658401374973990
      0.8707995547582963.
```

A separate discovery run extended the hinge check to `T=5,000,000`, again with
zero negative coordinates.  That last large run is reconnaissance only and is
not part of the default replay budget.

## 4. Direct critical-target checks

The ordered policy was also applied directly to

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

At

```text
X = 10^3, 10^4, 10^5, 10^6
```

there were again zero negative occupations.  The bottom values were

```text
M_2 = 5.831487393863583
      7.835150453992188
      9.835517264827760
      11.829944372525508.
```

These values are consistent with the positive hinge superposition of
`T-90205.9`; they are not an independent asymptotic theorem.

## 5. Exact proves-too-much mutation

The same policy is **not** positive on generic decreasing or convex-looking
targets.

Take endpoint `X=9` and the prefix step target

\[
 w(q)=\mathbf1_{2\le q\le8}.
\tag{O-90209.1}
\]

Exact `Fraction` arithmetic gives the node divergence / occupation table

```text
n   r_n       M_n
2   -1        62/45
3    0        38/15
4   -1        -4/3
5    0         2
6    0        12/5
7    0         0
8    1         8
9    0         0
```

so

\[
 \boxed{M_4=-\frac43<0.}
\tag{O-90209.2}
\]

This is the mandatory mutation for any proposed OBH proof.  An argument which
uses only monotonicity, convexity, target nonnegativity, or the broad Markov
kernel cannot work.

The square-root structure and its Möbius recombination are load-bearing.

## 6. A useful empirical lower envelope — not a theorem

For all hinge points inspected,

\[
 M_n^{(T)}
 \ge
 n\left(n^{-1/2}-(n+1)^{-1/2}\right)
\tag{O-90209.3}
\]

for `n<T`, with equality throughout the top no-parent region beginning near
`3T/4`.

However this simple lower envelope is **not** itself a global subsolution of the
occupation recurrence: substituting it into `L-90209.5` produces negative
residuals at small inner nodes.  It is retained only as a clue that the actual
Green reserve accumulated at larger parents is essential.

## 7. Interpretation

The data distinguish the new route from both neighboring failures:

```text
frozen two-split critical producer     long finite positivity, but now proved false cofinally;
ordered broad step target              fails already at X=9;
ordered broad square-root hinges       positive in every retained test through very large depth.
```

Thus the broad policy is neither generically positive nor obviously another
finite-range mirage of the exact same type: its deterministic continuum
resonances have a strict gap by `L-90209`.

The arithmetic theorem `OBH` remains completely open and must be proved without
extrapolating these scans.
