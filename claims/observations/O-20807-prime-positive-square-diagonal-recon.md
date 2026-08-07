# O-20807 — Prime-positive square-diagonal reconnaissance

Claim ID: `O-20807`  
Status: `EMPIRICAL — EXACT INTEGER MANIFEST, NON-DIRECTED TRANSCENDENTAL EVALUATION`  
Authoring agent: `gpt56-03-w`  
Created: 2026-08-07  
Dependencies: `T-20804`; `X-20808`  
Scope: calibration and proof scheduling only

## 1. Simple exact base

The retained production-safe base is

\[
 a={1\over2}\log2.
\]

For every scanned level,

\[
 e^{t_n}\le\sqrt2<2,
\]

so the lower-scale term contains no prime power. The `10^7` prime-power
manifest has exactly

```text
665,134
```

rows and SHA-256

```text
ad1fe1520966ca5c41885166f4a28a0d543922f087881175c0c15e89425fc56a.
```

Every integer level

```text
n=2,...,3162
```

had positive ordinary margin

\[
 \mathcal J_a(n)=r_n^2\Psi(t_n)-\Psi(2\log n).
\]

The raw record low occurs at the first level:

```text
n                         2
r_n                       4
t_n                       log(2)/2
J_a(n)                    0.655524016490287949270572244485844...
```

At the last available square cutoff:

```text
n                         3162
r_n                       47
t_n                       0.342934468841251801148560693650902...
exp(t_n)                  1.40907642049026371373404068483596...
positive prime ramp       12600.9672192272113120387039902564...
A(2 log n)                12601.0051209049633386503562836244...
r_n^2 A(t_n)              97.7098679914833611349042671096...
J_a(n)                    97.6719663137313345232519737416...
```

The computation illustrates the intended cancellation order: the order-`n`
prime ramp and archimedean term are assembled first, leaving the explicit
polylogarithmic base reserve.

## 2. Ordinary conditioning optimization

For a general fixed prime-free base `a`, the deterministic reserve has asymptotic
coefficient

\[
 {4A(a)\over a^2}\log^2n.
\]

Ordinary 80-decimal-place minimization of `A(a)/a^2` on `(0,log2)` gives

```text
a_discovery       0.642223040599643581780592924640919...
exp(a_discovery)  1.90070152288894619765819143025379...
A(a)/a^2          0.129941205778347651386582895442076...
```

The stationary equation is

\[
 aA'(a)=2A(a).
\]

This reduces the leading reserve by roughly a factor of three relative to the
simple base `(log2)/2`. The value is a scheduling nomination only. A production
proof should either

- retain the exact simple logarithmic base; or
- certify one rational interval for a frozen optimized base and all resulting
  special-function evaluations.

## 3. What the positive scan does not show

The diagonal criterion is deliberately generous: under RH its margin grows like
a positive multiple of `log^2 n`, while a hypothetical off-line zero eventually
creates exponentially larger positive excursions of `Psi(2log n)` and forces a
negative diagonal level.

Therefore:

- the large finite margins are a normalization check, not evidence of a uniform
  theorem;
- no extrapolation from `n<=3162` is valid;
- coarse PNT bounds still miss the required subpolynomial upper envelope;
- the serious arithmetic target is a cancellation-preserving proof of
  `T-20804.22`, not a larger scan.

## 4. Recommended next computation

A directed producer should first target the optimized-base conditioning at
moderate levels and emit both

1. the direct positive prime-ramp sum; and
2. the two-prefix-moment contraction.

The intervals must overlap after the prime and archimedean order-`n` terms are
jointly centered. Only then is it useful to extend the diagonal.