# F1 bounded-detector multiplier correction and spectral repair

Date: 2026-08-26

Durable PR: #730

Base head:

```text
f534df7ad3a180c35a95b57cd7a91b6233702408
```

## Audit verdict

The finite F1 Chow, Boolean/Wick, canonical pair-owner, integer-cell and
bounded Gram theorems survive.

The observation-level identity used to connect the reflection differential
current to the bounded derivative-outer density does not survive. Direct
Mellin integration gives

\[
\widehat K_L(s)=
\frac{4(s-1)(1-2^{-s})^2(1-\sqrt2\,2^{-s})}
{s(s-\tfrac12)},
\]

while the differential analytic square has multiplier
\(P(s)\widehat A(s)^2\). Their exact bridge is

\[
(5s+\tfrac32)(1-\sqrt2\,2^{-s})\widehat K_L(s)
=
4P(s)\widehat A(s)^2.
\]

Thus reflection variation remains a stronger sufficient route through a
stable inverse, but it is not equivalent to the bounded Hardy current.

## Spectral repair

The old weight

\[
|P(\tfrac14+it)|^2r_A(t)^4
\]

is asymptotically constant. Its integral against any nonzero finite Dirichlet
polynomial is infinite. Historical `L-105483.3--L-105483.7` and gates
`F1ASQ2_105483`, `F1FOURTH105483` are withdrawn.

The exact bounded-current weight is

\[
\Omega_K(t)=
\frac{
16|P(\tfrac14+it)|^2r_A(t)^4
}{
((\tfrac{11}{4})^2+25t^2)
(1+\sqrt2-2\,2^{1/4}\cos(t\log2))
}
\asymp(1+t^2)^{-1}.
\]

This yields ordinary Plancherel and the corrected exact packet coordinate

```text
F1KASQ105492 <=> F1GRAM105480 <=> F1HCNC105481.
```

The source-faithful normal-ordered Beta fourth moment

```text
F1KFOURTH105493
```

implies this coordinate but remains open.

## Concurrent quarter-power correction

PR #719 at

```text
426fe1c34a35d21b38a393456a7071c0902170f1
```

correctly leaves coherent owner collapse open:

```text
QPTI103112 <=> BCI102990 -> RH.
```

The fixed-owner quarter-power estimate does not prove either the sharp
one-sided gate or the stronger F1 square gate.

## Status

```text
multiplier correction and stable resolvent       PROVED
old unregularized spectral gate                  REFUTED
correct bounded spectral normal form             PROVED
correct normal-ordered fourth-moment reduction   PROVED
all source-specific estimates                    OPEN
Riemann Hypothesis                               UNPROVED
```
