# O-5608 — The first unconditional zero count at the PR #71 ordinate

Claim ID: O-5608
Title: `D = 0` over the `40`-unit window around the PR #71 ordinate: `N = 172`
total zeros and `N_0 = 172` certified critical-line zeros, so **no zero off the
critical line**, unconditionally
Status: CERTIFIED-COMPUTATION (all counts are Arb balls isolating single
integers; all signs are Arb balls strictly on one side of zero; no
imported bound, no conjecture, no floating-point sign decision)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: FLINT/Arb (`arb_zeta_nzeros`, Platt/Turing) as an external
implementation; nothing else
Scope: the slab `(a,b)` with `a = 75347258181331/2^4`, `b = 37673629090985/2^3`
Related counterexample candidates: the PR #71 full-complex Pick direction

## Why this exists

Everything this repository had said about the PR #71 ordinate was conditional.
`O-5604`'s census is empirical; its Turing argument imports an unproved bound on
`\int S` and rests on an uncertified `Z`.  An external review pointed out,
correctly, that the decisive object is the **exact slab discrepancy**

\[
 D(a,b) \;=\; N(a,b)\;-\;N_0(a,b),
\]

where `N` counts all zeros of `zeta` in the strip with `a < \Im\rho < b`, with
multiplicity, and `N_0` counts those on the critical line.  `D \ge 0` always,
`D` is even at positive ordinates by the functional equation, and

\[
 D(a,b) > 0 \;\Longrightarrow\; \text{RH is false},
\]

with no conditions whatsoever.  The review's own report stated that no directed
value of `D` had been produced, because a FLINT installation was unavailable to
it.  This claim records the counting half, computed.

## The computation

`python-flint 0.9.0` exposes `arb_zeta_nzeros`, which computes `N(t)` rigorously
by Platt's implementation of Turing's method and returns a **ball**.  A count is
used only when that ball isolates a single integer (`unique_fmpz`); otherwise
the program refuses.  Endpoints are exact dyadic rationals, checked to survive
into Arb without rounding.

```text
a = 75347258181331 / 2^4  = 4709203636333.1875
b = 37673629090985 / 2^3  = 4709203636373.125
target T = 20225875608341108140435 / 2^32 strictly inside: yes

N(a) = [1.9743642385928e+13 +/- 0]      ->  19743642385928
N(b) = [1.9743642386100e+13 +/- 0]      ->  19743642386100
                                    21.0 s at 192 bits

N(a,b) = 172        zeros in the strip, with multiplicity, on or off the line
```

**This is the first unconditional statement this repository has made about the
zeros near the PR #71 ordinate.**

## Two independent confirmations it produced on the way

1. **`N(a)` matches the Turing enumeration exactly.**  `turing.py`, working only
   from `rs_zeta`'s located sign changes and the smooth `theta`, derived
   `N(t_1) = 19743642385928` as its `c_est`.  Arb returns exactly that integer
   at a nearby endpoint.  Two computations sharing no code and no method agree
   on a 14-digit integer.
2. **The `|Z| = 259.78` anomaly is now certified.**  Since `|Z(t)| =
   |\zeta(1/2+it)|` — no `theta`, no branch, no Riemann–Siegel remainder —
   Arb gives, at the exact binary64 point `rs_zeta` and `mpmath` both evaluated,

   ```text
   t = 4822224523626135/2^10 = 4709203636353.6474609375
   |zeta(1/2+it)| = [259.7783878171189 +/- 9.92e-16]
   ```

   against `rs_zeta`'s `259.778388` and `mpmath.siegelz`'s `259.778387817`.
   The central number of `O-5604` is no longer floating.

   A caution recorded because it cost me a false alarm: at the *decimal* point
   `4709203636353.6475`, which differs from that double by `3.90625\times10^{-5}`,
   Arb gives `259.7797555777665` instead.  The fourth digit of `|Z|` is
   sensitive to the last bits of the ordinate, which is the same lesson as the
   serialization defect corrected in `O-5604`.

## The other half: `N_0 = 172`, certified in 81 seconds

Enumerating zeros with `acb.zeta_zeros` at index `1.97\times10^{13}` proved
impractical — it was still running after `18` minutes.  A **certified lower
bound** on `N_0` is all that is needed, though, because `N_0 \le N` is automatic:
if `N_0 \ge N` then `N_0 = N` and `D = 0`.  And a certified *sign change* of `Z`
between two points is a certified critical-line zero between them.

Hardy's `Z` can be evaluated in ball arithmetic with no imported bound at all:

\[
 Z(t)=e^{i\theta(t)}\,\zeta(\tfrac12+it),\qquad
 \theta(t)=\Im\log\Gamma\!\left(\tfrac14+\tfrac{it}{2}\right)-\tfrac{t}{2}\log\pi .
\]

The branch is not an obstacle: `\Re(1/4+it/2) = 1/4 > 0`, and on the right
half-plane `\log\Gamma` is the analytic continuation from `\log\Gamma(1)=0`,
which is what Arb's `lgamma` computes.  Checked against the independent Stirling
expansion `\theta = (t/2)\log(t/2\pi) - t/2 - \pi/8 + 1/(48t) + 7/(5760t^3)`, the
two agree to `5\times10^{-63}` — so no branch correction and no asymptotic
remainder bound enters.

`certified_sign_changes.py` samples `Z` at exact dyadic points between
consecutive approximate zeros and counts alternations, accepting a sign **only**
when the Arb ball lies strictly on one side of zero:

```text
slab (4709203636333.1875, 4709203636373.125)
173 sample points, 0 undecided
certified sign changes                     172        81 s at 192 bits
```

The approximate zero list from `rs_zeta` is used *only* to place the sample
points.  It cannot manufacture a sign change: a wrong guide zero costs one, it
never creates one.  So `N_0 \ge 172`.

## `D = 0`

\[
 172 \;=\; N_0 \;\le\; N \;=\; 172
 \qquad\Longrightarrow\qquad
 D \;=\; N-N_0 \;=\; 0 .
\]

**There is no zero off the critical line in the `40`-unit window containing the
PR #71 ordinate.  This is unconditional**: no bound on `\int S`, no conjecture,
no floating-point sign decision, no Riemann–Siegel remainder estimate.  Total
cost `102` seconds.

It also settles multiplicity: `N` counts with multiplicity and `172` simple
sign changes account for all of it, so every zero in the window is **simple**
and on the line.

This retires the conditional Turing argument of `O-5604` for this window.  That
argument is still worth keeping as an independent route — it reaches the same
verdict from entirely different ingredients — but it is no longer what the
conclusion rests on.

## A cost anomaly worth knowing about

The tighter slab straddling `T` itself was not needed in the end, and is just
as well: `N` at an endpoint inside the anomalous gap had not returned after
`13` minutes, against `21` seconds for **both** window endpoints together.

That cost asymmetry looks structural rather than incidental, and is worth
stating as an observation in its own right: **Turing's method is dramatically
more expensive exactly where the local zero configuration is anomalous**,
because the region over which `\int S` must be controlled has to extend until
the fluctuation settles, and a `4.33`-spacing gap is precisely a place where it
does not settle quickly.  The ordinate that is hardest to certify is the one a
gap-hunting screen nominates.  This is an observation from two data points and a
plausible mechanism, not a measurement.

## What may and may not be concluded

- **May:** the window contains exactly `172` zeros of `zeta` in the strip, all
  on the critical line, all simple.  The PR #71 candidate ordinate is closed
  unconditionally: whatever its eighth-order Pick determinant evaluates to, the
  zeros that determine it are all where RH says they should be.
- **May not:** anything about RH itself.  `D > 0` would refute RH; `D = 0` on
  one `40`-unit window at height `4.7\times10^{12}` is one local ledger entry
  and no more.  RH is a statement about infinitely many such windows.
- **May not:** that the method scales.  See the cost anomaly above.

## Limitations

1. `arb_zeta_nzeros` is an **external implementation**.  Its correctness is
   assumed, exactly as a compiler's is.  Nothing in this repository proves it,
   and a second implementation would be worth having before any `D > 0` were
   ever believed.
2. `172` is the count for the *dyadic* window, which is narrower than the
   `[T-20, T+20]` of `O-5604` by `0.0255` on the left and `0.036` on the right.
   `rs_zeta` found `173` sign changes in the wider one; the two are consistent
   if exactly one located zero lies in the trimmed edges, which has not been
   separately verified.
3. The `|Z|` certification is at a single point.

## Reproduction

```bash
pip install python-flint
cd experiments/X-5604-exact-slab-discrepancy
python3 slab_discrepancy.py --a 75347258181331/16 --b 37673629090985/8 \
    --target 20225875608341108140435/4294967296 --prec 192 \
    --out results/window-pr71.json
```

Add `--list-zeros` to attempt `N_0` and hence `D`; expect it to be slow at this
height.

## Suggested next attack

Get `N_0`, and prefer the cheap route.  `acb.zeta` costs `0.49 s` at this height
and `|Z| = |\zeta(1/2+it)|` needs no `theta`, so `173` certified evaluations
would cost about `90` seconds — except that certifying a *sign change* needs the
sign of `Z`, not its modulus, and therefore needs `theta` to a certified branch.
Either obtain `theta` rigorously (Arb's `lgamma` is principal-branch and must be
reconciled), or let `acb.zeta_zeros` finish.  Once `N_0 = 172` is certified,
`D = 0` closes the PR #71 ordinate unconditionally and retires every conditional
argument in `O-5604`.
