# L-30403 — The finite Euler boundary source terminates at polylogarithmic Cycle Debt

Claim ID: `L-30403`  
Title: The boundary capacity norm of PR #286 is the atomic divisor-source norm consumed by the adjacent-commutator lift, so boundary sources need not be propagated or matched to positive central edges  
Status: **PROPOSED COMPLETE CROSS-PR COMPOSITION — INDEPENDENT SOURCE-MANIFEST REPLAY REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #286 `L-28401/L-28402`; PR #301 `L-29801/L-29808`; `L-30402`; PR #272 `L-27208`  
Scope: complete finite central-cascade boundary ledger

## 1. Boundary source norm

At cascade depth `a`, let

\[
\sigma_a=(\sigma_a(m))_{m\ge2}
\]

be the complete divisor-source vector emitted by the exact finite
Euler/Peano cutoff ledger, after:

```text
shifted-even / unshifted-odd common-tail recombination;
common arithmetic destinations are combined;
all first-omitted odd terms are retained in the collar;
all zero-extension and endpoint atoms are retained.
```

Use the atomic norm

\[
\boxed{
\|\sigma_a\|_{\rm at}
=\sum_m\sqrt m\,|\sigma_a(m)|.
}
\tag{L-30403.1}
\]

This is the source-side version of the capacity metric.  `L-30402` supplies the
exact flow-side map

\[
\Phi(\sigma_a)=\sum_m\sigma_a(m)E_{m-1}
\]

with

\[
\mathcal N_\omega(\Phi(\sigma_a))
\le24\|\sigma_a\|_{\rm at}.
\tag{L-30403.2}
\]

## 2. The divisor-switch estimate is exactly the required norm

For fixed Euler order, every critical boundary coefficient is a positive
superposition of terms bounded by

\[
C_M n^{-3/2}
\left(1+\log\frac Xn\right)^{A_M}
\tag{L-30403.3}
\]

at a divisor-source node `m` satisfying one of finitely many relations

\[
2m\mid n+b,
\qquad |b|\le B_M.
\tag{L-30403.4}
\]

This is the explicit first-omitted quotient/shift ledger of PR #286.  Therefore

\[
\begin{aligned}
\|\sigma_a\|_{\rm at}
&\le C_M\sum_{|b|\le B_M}
 \sum_n n^{-3/2}
 \left(1+\log\frac Xn\right)^{A_M}
 \sum_{2m\mid n+b}\sqrt m\\
&\le C'_M\sum_{|b|\le B_M}
 \sum_n\frac{\tau(n+b)}n
 \left(1+\log\frac Xn\right)^{A_M}.
\end{aligned}
\tag{L-30403.5}

Here

\[
\sum_{m\mid N}\sqrt m\le\sqrt N\,\tau(N)
\]

and the finitely many small shifted indices are placed in the declared base
table.  The elementary divisor switch gives

\[
\boxed{
\|\sigma_a\|_{\rm at}
\le C_M(1+a)^{C_M}(1+\log X)^{C_M}.
}
\tag{L-30403.6}

This is the norm called the capacity-weighted first-generation jet ledger in
`L-28402.10`; equation (L-30403.5) records its exact source interpretation.

## 3. Summability over the analytic bank

Let `A_a` be the positive stopped-power analytic-bank norm at depth `a`.  PR
#286 proves

\[
A_{a+1}\le\frac67A_a+P_M(a,\log(2X)),
\tag{L-30403.7}

where every source destination is at the strict next half endpoint.  The
boundary export is linear in the current analytic bank and has the fixed-order
bound (L-30403.6).  Hence, through the `O(log X)` support-halving depths,

\[
\boxed{
\sum_a\|\sigma_a\|_{\rm at}
=O((1+\log X)^B)
}
\tag{L-30403.8}

for one absolute `B` once the Euler order is frozen.

The positive stopped-power resolution of PR #301 adds only another finite
logarithmic endpoint layer cake.  Its weights telescope to `log X` and are
already included in the exponent `B`.

## 4. Boundary termination

Instead of sending a residual Hausdorff source to another boundary generation,
replace every emitted source immediately by

\[
\Phi(\sigma_a).
\]

Equation (L-30402.3) verifies every carry column exactly.  No boundary source is
returned to the analytic bank and no incoming central capacity is requested.
Summing (L-30403.2) and using (L-30403.8) gives

\[
\boxed{
\sum_a\mathcal N_\omega(\Phi(\sigma_a))
=O((1+\log X)^B).
}
\tag{L-30403.9]

The closing bracket in the tag is typographical only.

The unmatched odd collar is included in `sigma_a`; it is not estimated by a
common-tail surrogate.  The positive bottom tree contributes no negative debt.
Unit endpoint interpolation is handled by PR #272 `L-27208` and has vanishing
additional debt.

## 5. Consequence for `SFC`

`SFC` demanded that every source coefficient be matched to an actual positive
central edge, up to polylogarithmic defect.  The present construction proves the
strictly weaker statement actually needed by Cycle Debt:

```text
complete boundary source
-> exact balanced signed flow
-> polylogarithmic negative capacity debt.
```

There is no source-flow type conversion and therefore no capacity token to
match or double-spend.  The root-only mutation `c_n=1/n` is irrelevant to the
critical norm because it omits the half-power which makes (L-30403.5)
summable.

## 6. Decisive review hinge

The cross-PR composition is rejected by one production row for which either:

1. the boundary source is not a divisor source of the form consumed by
   (L-30402.3);
2. its declared capacity weight is not the `sqrt(m)` atomic weight in
   (L-30403.1);
3. a first-omitted or endpoint atom is absent from the finite manifest;
4. the divisor-switch estimate (L-30403.5) omits a non-finite family of shifts;
5. the source is counted both in the analytic bank and in `sigma_a`.

These are finite source-map checks, not a new asymptotic arithmetic theorem.

## 7. Proof boundary

Proposed complete, subject to the declared source-manifest replay:

1. identification of the PR #286 capacity norm with the atomic source norm;
2. a polylog bound at every fixed Euler order;
3. summability through the contracted analytic bank;
4. exact termination of every boundary source by adjacent commutators;
5. polylogarithmic total negative capacity debt.

Not independently re-proved here:

1. the frozen finite Euler/Peano source manifest of PR #286;
2. PR #272's prime-ramp and square-screw/Landau consumer;
3. RH.
