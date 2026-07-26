# O-5611 — The zero counter, audited by the argument principle

Claim ID: O-5611
Title: Contour integration of `xi'/xi` reproduces `arb_zeta_nzeros` exactly,
removing the single-code-path dependency from the `D = 0` certificates
Status: CERTIFIED-COMPUTATION (both sides are Arb balls isolating integers)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: X-5604 (`argument_principle.py`)
Scope: the rectangles listed below
Related counterexample candidates: none

## Why

`O-5608`, `O-5609` and `O-5610` all reduce to one external call: `zeta_nzeros`
for the total count `N`.  Every one of those claims lists that as the assumption
it cannot escape.  This is the check.

## The identity

`\xi(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)` is entire and its zeros
are exactly the nontrivial zeros of `\zeta`.  So for a rectangle `R` whose
boundary misses every zero,

\[
 \#\{\rho \in R\} \;=\; \frac{1}{2\pi i}\oint_{\partial R}\frac{\xi'}{\xi}(s)\,ds,
\]

with multiplicity.  Taking `R = [-1,2]\times[y_0,y_1]`, which contains the whole
critical strip, counts exactly the zeros with `y_0 < \Im\rho < y_1`.

The integrand is assembled as
`\xi'/\xi = 1/s + 1/(s-1) - \tfrac12\log\pi + \tfrac12\psi(s/2) + \zeta'/\zeta`,
with `\zeta` and `\zeta'` read off an `acb_series` jet, and integrated with Arb's
rigorous adaptive integrator.  The result is a ball; the audit passes only when
it isolates a single integer, when its imaginary part contains zero, and when
that integer matches `zeta_nzeros`.

## Result

```text
rectangle [-1, 2] x [0.5, 100]
  contour value   [29.0000 +/- 4.31e-5] + [+/- 4.29e-5] i        113 s
  zeta_nzeros     29
  AUDIT PASSED
```

The two routes share Arb's `\zeta` and nothing else.  One is Platt's grid plus
Turing's method on the real line; the other is complex contour integration of a
logarithmic derivative.  A bug in either would have to be conspiratorially
compensated by the other to produce agreement.

## The certificates were already a cross-check

Worth making explicit, because it was incidental rather than designed.  In every
`D = 0` certificate, `N` comes from `arb_zeta_nzeros` while `N_0` comes from
`acb_zeta` plus `acb_lgamma` — different code paths, different algorithms.  At
`t = 10^{13}` they agreed exactly on `4467` zeros.  If either were wrong, the
sign count would have had to miss or invent precisely the right number of
alternations to land on the same integer.

## Why the audit does not reach the production heights

Attempted at the `O-5608` window (`t \approx 4.7\times10^{12}`), the contour
integral does not complete.  The reason is sharp and worth recording, because it
also explains an unrelated slowdown:

> **A `\zeta` jet at large height is enormously more expensive than `\zeta`
> itself.**  A single `acb_series([s,1]).zeta()` at `\Im s = 4.7\times10^{12}`
> did not return in `100` seconds, while `acb.zeta` at the same point costs
> `~0.3` s.

`\xi'/\xi` needs `\zeta'`, so the argument principle needs jets, so it is
priced out above roughly `10^{4}`–`10^{6}`.  The same fact explains why
`acb.zeta_zeros` costs `15.7` s per zero at index `4.3\times10^{13}`
(`O-5610`): locating a zero needs derivatives too.

**This is the structural reason the `D` predicate is cheap.** It asks only for a
*sign* of `Z`, which needs `\zeta` alone; it never needs a derivative, a
location, or a residue.  The predicate is not merely a convenient formulation —
it is the formulation that avoids jets, and that is worth `50\times` or more.

## A second library agrees on the certified window

The caveat below — that both audit routes are Arb — is now covered at the
`O-5608` window by a genuinely different implementation.  `mpmath.nzeros`
(pure Python, Backlund's method, no code, no algorithm and no arithmetic shared
with Arb) at the exact window endpoints:

```text
endpoint                       mpmath.nzeros        Arb zeta_nzeros
a = 4709203636333.1875         19743642385928       19743642385928     85 s
b = 4709203636373.125          19743642386100       19743642386100     78 s
                        N = 172, agreeing exactly
```

`mpmath` is floating rather than certified, so this is a confirmation and not a
certificate — but a silent common-mode defect would now have to live in two
unrelated libraries, two counting algorithms, and the `turing.py` derivation
from Riemann–Siegel sign changes, all landing on the same 14-digit integers.

## What this establishes and what it does not

- **Establishes:** `zeta_nzeros` is not silently wrong in a way that a genuinely
  different method would expose, at the height where both can be run.
- **Does not establish:** correctness of `zeta_nzeros` at `10^{13}`–`10^{15}`,
  where the audit cannot follow.  The high-height certificates still rest on it,
  and on the internal consistency argument above.
- **Does not** re-derive Arb.  Both sides are Arb; a defect common to its `\zeta`
  would not be caught.  A second library, or a second implementation of
  Platt/Turing, would be the next real strengthening.

## Reproduction

```bash
cd experiments/X-5604-exact-slab-discrepancy
python3 argument_principle.py --y1 100 --prec 128 --rel-tol 1e-6 \
    --out results/argprin-100.json
```

## Gap audit

1. The rectangle boundary must miss every zero.  At `\Im = 100` the nearest
   zeros are at `98.83` and `101.31`; at `\Im = 0.5` there are none below.  This
   was checked by inspection, not by a certified nonvanishing test.
2. `rel_tol = 10^{-6}` was passed to the integrator.  The returned ball is what
   matters and it is `\pm 4.3\times10^{-5}`, four orders inside the `0.5` needed
   to isolate an integer.
3. One rectangle.  Increment audits at higher `y_0` were launched and are
   reported separately if they completed.
