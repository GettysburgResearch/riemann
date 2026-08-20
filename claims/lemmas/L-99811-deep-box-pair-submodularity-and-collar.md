# L-99811 — Deep box pair-submodularity and activation-collar localization

Claim ID: `L-99811`  
Status: **PROVED EXACT DEEP-REGION THEOREM + EXACT COLLAR LOCALIZATION**  
Created: 2026-08-20  
Depends on: PR #658 `L-99703`; PR #652 native first-owner source  
RH status: **unproved**

Let `Phi(y)=phi(y)` be the normalized factor-67 box potential of `L-99703`, with zero extension below one. For primes `p,q>=67`, define

\[
 \Delta_{p,q}\Phi(y)
 =\Phi(y)-\Phi(y/p)-\Phi(y/q)+\Phi(y/(pq)).
\]

## 1. Exact deep-region sign

If all four arguments lie in the flat tail, equivalently `y/(pq)>=67`, then

\[
 \Phi(t)=8(1-67^{-1/2})-\frac{3\log67}{\sqrt t}.
\]

Therefore

\[
 \boxed{
 \Delta_{p,q}\Phi(y)
 =-\frac{3\log67}{\sqrt y}(\sqrt p-1)(\sqrt q-1)<0.
 }
\tag{L-99811.1}
\]

Thus the conclusion-complete box potential is strictly pair-submodular on every two-prime cube wholly contained in the deep region.

## 2. Exact localization of every failure

If (L-99811.1) is not applicable, then at least one of

```text
y,
y/p,
y/q,
y/(pq)
```

lies below `67`. Hence every possible sign failure is contained in the multiplicative collar

\[
 \boxed{1\le y<67pq.}
\tag{L-99811.2}
\]

For ordered primes `p<q`, the genuinely mixed transition is more sharply contained in the union of the finite ratio intervals determined by

\[
1,\;67,\;p,\;q,\;67p,\;67q,\;pq,\;67pq.
\]

On each such interval the potential is an explicit linear combination of `1`, `y^{-1/2}`, and `y^{-1/2}\log y`, so the sign of the mixed difference reduces to elementary one-variable inequalities and endpoint checks.

## 3. Consequence for the native Euler source

Pair future primes before taking absolute values. Every two-prime block whose smallest child scale remains in the deep region has a fixed favorable mixed sign. The only unresolved two-prime contributions are activation-collar blocks satisfying (L-99811.2).

This is strictly narrower than the full owner-Carleson or min-cut problem. It suggests the repaired closure target `APCL99810`: prove that the total logarithmic negative mass of activation-collar blocks is subpower, using the existing compact factor-67 certificate, mesoscopic Dickman corridor, and exact first-owner ledger.

The theorem does **not** claim global pair-submodularity: finite stress tests show positive mixed differences across activation transitions, so any proof that ignores the collar is invalid.
