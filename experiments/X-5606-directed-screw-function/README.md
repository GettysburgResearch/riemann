# X-5606 — Directed evaluation of Suzuki's screw function (PR #98 / issue #95)

Agent: `fable5-01`   Claim: `O-5615`

RH is equivalent to `Psi(t) >= 0` pointwise (D-9501, importing Suzuki
arXiv:2206.03682).  PR #98's reconnaissance found the smallest binary64 value
through cutoff `1e7` at `t = 8.039063759496273` and stated plainly that no
directed certificate existed on the route.

`directed_psi.py` supplies the first ones.  The structural point: for fixed
`t`, D-9501.1 is a FINITE exact expression — at `t ~ 8` the complete prime sum
has 478 terms — so there is no cutoff truncation to control at all; the only
tail is the Lerch series, closed by an exact geometric bound.  Every term is
an Arb ball.

```text
Psi(8.039063759496273)   = [0.0275205733536208048 +/- 2.05e-20]   POSITIVE
Psi(log 3089 + 1e-9)     = [0.0278538460164537321 +/- 3.83e-20]   POSITIVE
Psi(log 3109 - 1e-9)     = [0.0277700092138465624 +/- 2.95e-20]   POSITIVE
```

The directed value agrees with their 80-digit same-derivation replay
(`0.02752057335362080482041457506913...`) to every displayed digit, and shows
their binary64 scan value (`0.0275205733535131`) was off in the 12th digit —
float error, not structure.

With L-9503's strict convexity of `Psi` between knots, positive certified
values at the interior stationary point and both knots certify the cell's
minimum positive.  Conditional only on the imported Suzuki equivalence and
the D-9501 normalization.
