# T-30601 — Corrected cycle-optimized band-transference frontier

Claim ID: `T-30601`  
Title: The PR #304 terminal-atomic proof is false; a source-complete completion must optimize the recombined dyadic band before measuring Cycle Debt  
Status: **CORRECTED CONDITIONAL FRONTIER — NOT A FULL PROOF; RH UNPROVED**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #306  
Dependencies: `R-30601`--`R-30603`, `L-30601`; PR #272 Cycle-Debt consumer  
Scope: exact disposition of PR #304 and the smallest surviving construction theorem

## 1. Disposition of the frozen full proposal

PR #304's proposed completion relies on two load-bearing assertions:

1. a quotient-index source lift which retains an outer arithmetic-fiber factor `q_0^(-1/2)`;
2. a polylogarithmic square-root atomic norm for every finite stopped-power boundary source.

`R-30601` proves that the first erases the arithmetic fiber. The correct source nodes are

\[
2kq_0,
\qquad
(2k+1)q_0,
\]

not `2k,2k+1`. The corrected adjacent-tree capacity loses the asserted outer factor.

`R-30602` proves that one stopped critical power already forces

\[
\|\sigma\|_{\rm at}\ge\frac N{240}
\]

at the declared half endpoint. Thus the second assertion is false at layerwise source scope.

Therefore

\[
\boxed{
T\text{-30401 is GAP/BLOCKED and its claimed full proof is rejected.}
}
\tag{T-30601.1}

This does not prove RH false and does not refute optimized Cycle Debt.

## 2. What the linear atomic lower bound misses

The atomic lift pays separately for every top-band divisor node. The balanced carry cone can amortize them.

`L-30601` proves that on

\[
H<q\le2H
\]

the central rows are exactly the step basis

\[
\chi_{[n,\lfloor n/2\rfloor]}(q)=\mathbf1_{q\le n}.
\]

Hence an arbitrary recombined top-band profile `g` is realized exactly by

\[
d_g
=\sum_{n=H+1}^{2H}
[g(n)-g(n+1)]
[n,\lfloor n/2\rfloor].
\]

Its debt is controlled by weighted one-sided variation rather than atomic mass:

\[
\mathcal N_\omega(d_g)
\le
2\sum_{n=H+1}^{2H}
\sqrt n\,[g(n+1)-g(n)]_+.
\tag{T-30601.2}
\]

For a monotone critical-size negative profile this is `O(polylog X)`.

Every uncorrected load is routed to `q<=H`, so this is a strict half-scale transference.

## 3. Why central steps alone do not finish the proof

`R-30603` gives a source-specific capacity mutation. A single top-band profile of size `n^(-1/2)` has bounded initial central debt, but its lower leakage is one central carry row with weighted downward variation

\[
\Omega(n^{3/4}).
\]

A second central-step repair therefore costs

\[
\Omega(n^{1/4}).
\]

Thus the recurrence

```text
apply L-30601;
repeat at half scale;
```

is false as a uniform critical contraction.

The remaining freedom is exactly the complete Pascal-cycle space: different balanced splits have the same top-band step but different lower-band leakage.

## 4. Smallest surviving theorem

The corrected construction theorem is **Cycle-Optimized Band Transference** (`COBT`).

For every source-bound recombined boundary profile on one band, construct a balanced split mixture which:

1. realizes the entire top-band profile exactly;
2. retains every arithmetic fiber and common destination;
3. minimizes over the complete Pascal fundamental-cycle coordinates before taking a negative part;
4. exports an exact carry source supported at the strict half endpoint;
5. satisfies
   \[
   \mathcal N_{\omega,\rm current}
   +\mathcal V_{\rm lower}
   \le
   \theta\mathcal V_{\rm incoming}
   +C\log^A(2X),
   \qquad\theta<1,
   \tag{T-30601.3}
   \]
   in a declared source variation norm.

If COBT is proved for the complete finite Euler/Peano manifest, fixed-scale iteration gives polylogarithmic Cycle Debt, then the inherited prime-ramp and square-screw/Landau consumer yields RH.

No proof of COBT is claimed here. It is not assigned to reviewers; this PR exists to remove a false full proof and establish the exact finite lemmas a future construction must use.

## 5. Automatic rejection conditions

Reject a claimed replacement if it:

1. indexes the flow by `k` while retaining `q_0` only in the coefficient;
2. uses the `q_0^(-1/2)` capacity gain after physical dilation;
3. asserts a polylog atomic norm for a stopped power despite `R-30602`;
4. recursively uses only central steps despite `R-30603`;
5. takes negative parts before common-fiber and common-destination recombination;
6. omits Pascal-cycle coordinates or lower-band leakage;
7. promotes a finite LP trend to (T-30601.3).

## 6. Exact status

```text
PR #304 source-fiber map                    REFUTED
PR #304 layerwise polylog atomic norm       REFUTED
correct dilated adjacent-tree source        PROPOSED COMPLETE EXACT
top-half band step basis                    PROPOSED COMPLETE EXACT
naive central-step recursion                REFUTED
cycle-optimized band transference COBT      OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVED
```
