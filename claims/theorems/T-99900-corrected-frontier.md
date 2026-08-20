# T-99900 — Corrected native-box and GPMOC frontier

Claim ID: `T-99900`  
Status: **PROVED HARDENING / FINAL ARITHMETIC ESTIMATE OPEN**  
Created: 2026-08-20  
Base: PR #664 at `14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e`  
RH status: **unproved**

The latest scalar portfolio has two exact conclusion-facing formulations:

1. the source-aligned logarithmic box of PR #653;
2. the compact Poisson packet and `GPMOC99800` of PR #659.

This packet proves that the last window statement in PR #664 is not typed in
the literal normalized box source. The correct normalized prime operator is
`I-p^-1 U_p`, and the native collar coefficient is

\[
-3\sum_{X/67<n\le X}\frac{\beta(n)}{\sqrt n},
\]

equivalently the three-band half-order expression of `L-99900.5`.

It also proves that the GPMOC phase square is exactly the one-dimensional Hardy
tail energy of `L-99901.2` and that the collar window has the exact block Gram
kernel of `L-99902.1`.

The corrected conclusion graph is

```text
native duplicate-67 source
 -> exact normalized box with p^-1 operator
 -> half-order three-band collar correlation
 -> cumulative-tail / cross-core estimate
 -> subpower logarithmic negative mass
 -> zero-free Mellin-Landau consumer
 -> RH.
```

No estimate in this packet proves the cumulative-tail/cross-core line. In
particular:

```text
unweighted ratio-67 Mertens window          not the native normalized source;
half-order three-band window                exact;
Cauchy-Poisson Hardy-tail identity           exact;
GPMOC99800                                   open / RH-bearing;
subpower box negative mass                   open / RH-bearing;
Riemann Hypothesis                           unproved.
```

Thus the requested complete closure cannot be obtained by composing PR #664's
unweighted window theorem. A valid successor must prove the half-order
cross-core estimate at the exact normalization above, or prove `GPMOC99800`
directly.
