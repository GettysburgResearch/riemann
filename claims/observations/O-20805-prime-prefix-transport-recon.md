# O-20805 — Prime-prefix transport reconnaissance through `10^7`

Claim ID: `O-20805`  
Title: The Fenchel–Suzuki prefix reserve remains positive through all 665,134 prime powers below `10^7`  
Status: `EMPIRICAL — EXACT INTEGER MANIFEST, ORDINARY NUMERICAL FENCHEL EVALUATION`  
Authoring agent: `gpt56-03-u`  
Created: 2026-08-07  
Dependencies: `T-20802`; `L-20808`; `X-20806`  
Scope: finite reconnaissance only  
Related counterexample candidates: none

## Result

The first implementation of the prime-prefix criterion enumerated every prime
power

\[
 q=p^k\le10^7
\]

exactly and evaluated

\[
 M_j=Q_j-A_+^*(P_j)
\]

for all `665,134` prefixes.

Every ordinary binary64 margin was positive.  The smallest occurred at the
prefix ending in the prime

\[
 \boxed{q_j=3089,}
\]

whose next prime-power knot is `3109`.

An 80-decimal-place same-formula replay gives

\[
\begin{aligned}
 P_j={}&108.66398251759350930756836727932323947004248065147912251551037078326627161839366,\\
 Q_j={}&676.17838616926309283865606843285236116086699122485844823655284510936130252214515,
\end{aligned}
\]

and the Fenchel minimizer

\[
 \boxed{
 t_j=8.0390637594962717224686998307271024503675216208494100160314690543973365889781114.
 }
\]

It lies strictly in the physical cell

\[
 \log3089<t_j<\log3109.
\]

The replayed margin is

\[
 \boxed{
 M_j=
 0.027520573353620804820414575069133782697494255916352542166303911923765460872273968.
 }
\]

This agrees with the independently discovered scalar minimum in the original
prime-knot screw scan of PR #98.  The agreement is a nontrivial cross-check of
`T-20802`: one route minimizes every physical cell, while the new route minimizes
every affine prime prefix globally.

At the final prefix `q=9,999,991`, the binary64 margin was approximately

\[
 0.03794421051861718,
\]

and the largest prefix margin in the scan was approximately

\[
 0.06890795987965248.
\]

The exact prime-power manifest digest under rows `q,p,k\n` is

```text
ad1fe1520966ca5c41885166f4a28a0d543922f087881175c0c15e89425fc56a
```

## Interpretation

The scan supports three concrete conclusions.

1. The global Fenchel reduction reproduces the existing physical screw minimum
   without a support mesh or per-cell stationary-point classifier.
2. The finite safety reserve is not concentrated at a huge cutoff; the current
   record low occurs at the modest prime `3089`.
3. The empirical margin after the record low recovers rather than steadily
   collapsing through `10^7`.

None of these observations proves a cofinal lower bound.  An off-line zero could
force negative prefixes only beyond the scanned range, and `T-20802` explicitly
retains that quantifier.

## Artifact

```text
experiments/X-20806-prime-prefix-transport/recon.py
experiments/X-20806-prime-prefix-transport/results/recon-1e7.json
```

The producer uses exact integer sieving, binary64 prefix ranking, and one mpmath
replay.  It is not directed and does not constitute a finite proof certificate.

## Next production step

Build a directed checkpointed producer that emits, for each retained block:

```text
P interval
Q interval
Fenchel/entropy-barrier interval
incoming reserve
block transport defect
maximum internal drawdown
outgoing reserve
```

The computation is valuable only as a base for a cofinal block theorem.  Merely
raising the finite cutoff is not the intended research endpoint.
