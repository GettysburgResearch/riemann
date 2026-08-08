# R-29806 — The interleaved node sequence is not Hausdorff

Claim ID: `R-29806`  
Title: `L-29810` cannot be applied directly to the complete interleaved node sequence; only its smooth Laplace mode is Hausdorff in the node index  
Status: **EXACT SCOPE CORRECTION / DIRECT APPLICATION REFUTED**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-29809`, `L-29810`  
Scope: corrects only the application paragraph of `L-29810`; the abstract Hausdorff matching theorem remains valid

## 1. Hausdorff necessity

A Hausdorff moment sequence is completely monotone. In particular, every
second forward-decrease difference is nonnegative at every starting index.

## 2. Exact interleaved counterexample

For the interleaved source

\[
 a_{2k}=(2kq-1)^{-s},
 \qquad
 a_{2k+1}=((2k+1)q)^{-s},
\]

take `q=2`, `s=1`, and the odd starting index whose consecutive arguments are

\[
 6,7,10.
\]

Then

\[
 \boxed{
 \Delta^2a_n
 ={1\over6}-{2\over7}+{1\over10}
 =-{2\over105}<0.}
\tag{R-29806.1}
\]

Therefore the complete interleaved sequence is not Hausdorff in the node index.

## 3. What remains true

`L-29809` proves two different facts which must not be conflated:

1. from an even start, every scalar Euler jet is positive;
2. as the **paired start index** `K` varies, each emitted scalar jet is a
   Hausdorff sequence in `K`.

Neither statement says that the original node sequence
`a_N,a_(N+1),...` is Hausdorff in the consecutive node index required by the
direct application in `L-29810.6`.

The abstract matching theorem `L-29810` is valid. Its direct application to the
whole interleaved node bank is not.

## 4. Correct repair

The exact two-mode formula of `L-29809` writes

\[
 a_n=\int\left[\alpha z^n+\beta(-z)^n\right]d\mu.
\]

At an even start, multiplication by the Euler sign `(-1)^r` gives:

```text
smooth mode alpha z^(N+r):  alternating binomial Hausdorff source;
parity mode beta (-z)^(N+r): coefficientwise nonnegative source.
```

Thus `L-29810` applies to the smooth mode only, while the parity mode requires
no matching. This repaired vector decomposition is stated separately in
`L-29812`.

## 5. Disposition

```text
abstract Hausdorff matching theorem L-29810       RETAIN
whole interleaved sequence is Hausdorff            FALSE
L-29810 direct application paragraph               SUPERSEDED
mode-separated vector application L-29812          CORRECT REPLACEMENT
DCD / RH                                            UNPROVEN
```
