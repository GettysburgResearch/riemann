# R-91101 — The factor-54 reset is not only a finite collar: a delayed rough-prime renewal survives

Claim ID: `R-91101` (provisional research range)  
Status: **EXACT SCOPE CORRECTION / METHOD FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-12  
Depends on: `L-91112/L-91113`; PR #399 `T-91101`  
RH status: **unproved**

## 1. Previous label

The first factor-54 handoff described the remaining work as one finite-width collar combining:

```text
target-versus-continuum error;
terminal quotient annulus;
B-spline quantization collar;
33-state parity shadow.
```

That label is no longer exact.

## 2. What is actually closed

`L-91112` proves that using the exact equality rows removes all three listed analytic/discretization objects:

- no target-versus-continuum replacement is made;
- every outer ordinary column is saturated exactly;
- every outer radix-four detail column, including the terminal annulus, is saturated exactly;
- no continuum endpoint density is discretized, so no quantization collar appears.

The three terms combine into the single exact inner row residual

\[
 \mathcal R_{X,K}(q)
 =\sum_{q\le n<K}c_X(n)\beta_{nq}.
\]

## 3. What survives

`L-91113` absorbs every combination of primes at most 53 into a globally positive 65,536-state Boolean forcing. The exact remaining identity is

\[
 \mathbf F^{(53)}
 =\mathbf U+\mathcal K_{59}\mathbf U,
\qquad
 \mathcal K_{59}\ge0,
\]

where every nontrivial delay in `K_59` is at least `log 59` and `U=(L,R)`.

Thus the unresolved operation is not a finite local sign check. It is a **capacity-faithful positive allocation of a delayed rough-prime renewal**:

\[
 \mathbf F^{(53)}
 \rightsquigarrow
 \mathbf U
 +\text{contracted copies of }\mathbf U.
\]

## 4. Positive forcing is not positive inversion

For an abstract positive delay `S`, the scalar model

\[
 F=(I+S)U
\]

may have `F>=0` while `U` changes sign; the causal inverse

\[
 U=(I+S)^{-1}F=F-SF+S^2F-\cdots
\]

alternates.

Therefore none of the following is valid by itself:

```text
positive Boolean forcing -> positive equality state;
all delays exceed one reset window -> positive inverse;
positive 33-state Hall margins -> global cone-preserving recurrence.
```

The arithmetic carry/score geometry must be used to build a shadow, Schur allocation, or martingale coupling for the delayed states.

## 5. Corrected remaining gate

The accurate final interface is:

> Allocate the globally positive small-prime forcing between the current exact inner row residual and the delayed rough-prime copies of the contracted `(L,R)` state, preserving ordinary/radix-four capacity and endpoint-row nonnegativity, with coefficient-one score transfer and bounded additive debt.

This is narrower than a global reciprocal-zeta sign theorem, because the complete finite Euler block and every finite collar have been removed. It is broader than a finite 33-state LP, because the delayed rough-prime renewal is infinite and conclusion-producing.

## 6. Status effect

The conditional implication in `T-91101` remains valid. Its hypothesis should be read as including this rough-prime allocation. Any presentation calling the hypothesis already reduced to a purely finite collar is superseded by this correction.

```text
three analytic/discrete collars                      CLOSED EXACTLY
all primes <=53 / all 65,536 Boolean states          CLOSED EXACTLY
delayed rough-prime renewal identity                  CLOSED EXACTLY
positive inverse / capacity-faithful allocation       OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVEN
```
