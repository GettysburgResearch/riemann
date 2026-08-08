# R-30101 — The recombined common tail is not an alternating Euler tail

Claim ID: `R-30101`  
Title: Pairing the shifted-even and unshifted-odd cutoff legs consumes the alternation; a second alternating Euler transform changes the source  
Status: **EXACT REFUTATION OF THE LOAD-BEARING ADAPTER IN `L-29808.6`–`L-29808.7`**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #301 at `060943ce211f97b59c1ce60e1a74dff8154dceb1`  
Scope: the claimed common-tail Euler compression; the positive Hausdorff typing of each paired difference survives

## 1. The actual common cutoff tail

Fix integers

\[
q\ge1,\qquad K\ge1,
\]

and a real exponent `s>0`. Put

\[
A_k=(2kq-1)^{-s},
\qquad
B_k=((2k+1)q)^{-s},
\qquad
D_k=A_k-B_k.
\tag{R-30101.1}
\]

After the shifted-even and unshifted-odd legs have the same first omitted index, their conditionally paired common tail is

\[
\boxed{
Q_K=
\sum_{k\ge K}\bigl(A_k-B_k\bigr)
=
\sum_{k\ge K}D_k.
}
\tag{R-30101.2}
\]

This is an **ordinary positive sum**. Since `D_k=O(k^{-s-1})`, it is absolutely convergent for every `s>0`.

If the first omitted indices differ by one, there is one unmatched odd collar term and the remaining common tail is still exactly of the form (R-30101.2).

## 2. What the Hausdorff representation actually gives

The first two sections of `L-29808` correctly prove that

\[
D_k=\int_{[0,1]}y^k\,d\sigma(y)
\tag{R-30101.3}
\]

for a finite positive measure `sigma`, and hence

\[
\Delta^mD_k
=
\int_{[0,1]}y^k(1-y)^m\,d\sigma(y)
\ge0.
\tag{R-30101.4}
\]

Tonelli's theorem applied to the actual positive common tail gives

\[
\boxed{
Q_K
=
\int_{[0,1]}
\frac{y^K}{1-y}
\,d\sigma(y).
}
\tag{R-30101.5}
\]

By contrast, the alternating series introduced in `L-29808.6` is

\[
\widetilde Q_K
=
\sum_{k\ge K}(-1)^{k-K}D_k
=
\int_{[0,1]}
\frac{y^K}{1+y}
\,d\sigma(y).
\tag{R-30101.6}
\]

Equations (R-30101.5) and (R-30101.6) are different. For every nonzero positive measure with mass away from zero,

\[
Q_K>\widetilde Q_K.
\]

The identity in `L-29808.7` is therefore a correct identity for an **artificially re-alternated sequence** `D_k`, but it is not an identity for the actual recombined cutoff source.

## 3. Exact elementary control

Take

\[
q=1,\qquad s=1,\qquad K=1.
\]

Then

\[
D_k
=
\frac1{2k-1}-\frac1{2k+1}.
\tag{R-30101.7}
\]

The actual common tail telescopes:

\[
\boxed{
\sum_{k\ge1}D_k=1.
}
\tag{R-30101.8}
\]

The artificially alternating tail is instead

\[
\boxed{
\sum_{k\ge1}(-1)^{k-1}D_k
=rac\pi2-1.
}
\tag{R-30101.9}
\]

A finite rational witness already suffices. The first two paired differences are

\[
D_1=\frac23,
\qquad
D_2=\frac2{15}.
\]

Hence

\[
\boxed{
D_1+D_2=\frac45
\ne
\frac8{15}=D_1-D_2.
}
\tag{R-30101.10}
\]

The exact checker `X-30101` replays this witness and 12,773 additional finite identities.

## 4. Why the two Euler operations cannot both be used

Before recombination, the source can be written as one interleaved alternating sequence

```text
+A_K, -B_K, +A_(K+1), -B_(K+1), ... .
```

An Euler transform may be applied to that alternating sequence if every shifted label and finite difference is retained exactly.

After pairwise recombination, however, the same source is

```text
D_K + D_(K+1) + D_(K+2) + ... .
```

The alternation has been consumed. Applying the alternating Euler transform to the new sequence `D_k` is a second, source-changing operation.

Thus the proof must choose one of two routes:

1. Euler-transform the original interleaved sequence and preserve all mixed shifted/unshifted finite-difference labels; or
2. recombine to the positive ordinary tail and control that ordinary tail without the factor `2^{-M}` from alternating Euler acceleration.

PR #301 does neither: it recombines first and then imports the alternating remainder (R-30101.6).

## 5. Impact on the frozen proposal

The following scopes survive:

1. `D_k>0`;
2. `D_k` is a Hausdorff moment sequence;
3. every finite difference `Delta^m D_k` is nonnegative;
4. the first omitted index mismatch is zero or one;
5. the finite central/sibling carry identity itself.

The following load-bearing deductions do not survive:

1. the statement in `L-29808.6`–`L-29808.7` that the exact alternating remainder represents the recombined common tail;
2. the application in `L-29806.5` of the alternating Euler remainder to the actual common tail;
3. the `2^{-M}` common-tail damping used in the all-generation source budget;
4. the claim in `L-29807/T-29802` that the emitted finite nonnegative Pascal flow is an exact realization of the complete cutoff source;
5. `T-29802` as a proof of RH.

Accordingly,

```text
L-29808 Hausdorff pair typing          RETAINED
L-29808 recombined Euler adapter       REFUTED
L-29806/L-29807 global closure         UNPROVEN
T-29802 as an RH proof                 REJECTED AS WRITTEN
Riemann Hypothesis                     UNPROVED
```

This refutation does not rule out a corrected interleaving-Euler proof or an ordinary-tail transport proof. `L-30102` records the exact ordinary-tail structure available for such a repair.
