# NCL29 — every prime power, all-denominator angular control, and what remains

**Proposed component mathematics, requiring independent review.**
**No full high-composite bound or RH proof.**
Continuation of #904 / strategy #902, read at
`879497b4f11be2618c448efc1fa93f69b4022e4c`.

## The result in one paragraph

Large denominators and slowly varying frequencies are different things. A
fraction such as 4999/10000 oscillates rapidly on the integer observation
index, while 1/10000 varies slowly, although their denominators agree.
This packet bounds the combined modes at ALL available denominators away
from a small angular neighborhood of zero, and separately bounds EVERY
pure prime-power denominator at all angles. After exact scale-local native
Newton reconstruction, the controlled contribution has only a fixed power
of logarithmic growth. The unbounded arithmetic problem is concentrated in
the signed near-zero band at denominators with at least two distinct primes.
That remaining band is not proved small and is substantial in the finite data.

The analytic bound is GENERIC for bounded sources. The exact reconstruction
uses Mobius inversion. This is useful localization, not a newly established
Mobius-specific all-mode gain, and not a claim that nearly all of RH is done.

## Read first

[PROOF.md](PROOF.md) gives the statements, complete proofs, exact source and
tail maps, the change from the previous partition, and the remaining estimate.
[SOURCES.md](SOURCES.md) records inherited identities and the literature scope.
[VALIDATION.md](VALIDATION.md) records actual replays and numerical limits.

The principal inequalities are, for |c(n)|<=K, support through L,
B_q=sum_(q|d)(c*c)(d)/d and H the harmonic sums:

```
sum_(q<=L^2) q |B_q|^2 <= 1024 K^4 H_L^4 H_(L^2)^4.
```

For any selected reduced fractions at those denominators with
||a/q||>=eta, and X>=L^2/8, the complete centered harmonic function satisfies

```
whole-future angular-sector energy <= 2^21 K^4 eta^-1 H_L^9.
```

This is a bound on the square of the COMBINED sum, with every covariance
retained. A separate complete bound for all prime powers is

```
whole-future prime-power energy <= 2^12 K^4 H_L^8.
```

With the specified capped native source and dyadic observation blocks,
choose eta=1/[2 ceil(log_2(Y+1))]. Then the full native reciprocal source is

```
m(k) = -G_Y(k) - R_Y(k),          Y<k<(Y+1)^2,
||G_Y||^2 <= C (1+log Y)^11.
```

G includes every pure prime power and the remaining far-from-zero modes at
mixed-prime denominators. R is the exact near-zero mixed-prime remainder.
It includes its full harmonic-tail centering constants. A subquadratic
previous-energy bound for R would complete the existing scale-gain argument;
no such bound is claimed here. The explicit constants are conservative, not
optimized as a practical numerical certificate.

## What changed from NCG28

NCG28 keeps one completed prefix through Y and moves a DENOMINATOR cutoff.
Here each observation block [X,2X) uses a completed prefix only as long as
needed, y=floor(sqrt(last)), with y<=Y. Every source still reconstructs the
actual mu on its assigned block. Its maximum Fourier denominator is then
at most 8X, which makes the angular estimate effective.

These are two different exact decompositions of the SAME full native source.
This packet does not silently assert a termwise bound for the old moving
W_high. We apply the nonlocal tail map to each frozen source BEFORE cutting
out the observation block. Applying it to a stitched source would add
boundary terms and is not what is done.

## Actual finite panels

The accepting defaults cover Y=15 and Y=31, a total of 1,232 observation
cells counting overlap between campaigns, and 2,455 coefficient comparisons
counting overlap of reconstructed prefixes. The largest endpoint is 1,023.
No new large Mertens calculation or zero verification is claimed.

For Y=31 (eta=1/10), descriptive decimals from outward enclosures are:

| Quantity | Value |
|---|---:|
| Actual F_1023-F_31 | 0.0990995899971780... |
| All pure prime-power energy | 0.0077704676653361... |
| Far mixed-prime energy | 0.0109393879927419... |
| Combined controlled G energy | 0.0193154620508891... |
| Remaining near mixed-prime energy | 0.0931762895197677... |
| Twice G/remainder covariance | -0.0133921615734788... |

Every one of the three mixed terms is retained in results.json. The
controlled energy is not the sum of the first two sector energies; their
own covariance matters. Finite native blocks have both signs of the
far/near covariance. These values are not evidence that the remainder is
asymptotically small.

The far-sector evaluations include 32,482 mixed-prime fractions beyond the
local NCG28 denominator-window comparison cut, counting repeated block
experiments. That is a coverage fact, not an estimate of a proportion of RH.
The comparison cut uses the local short source, not NCG28's original fixed Y.

## Reproduce

Python standard library only; no package installation or network is required.
From this directory:

```sh
python -S -B check.py --check results.json
python -S -B test_check.py
python -S -O -B check.py --check results.json
python -S -O -B test_check.py
```

The checker uses exact rational source/divisor algebra and 144-bit outward
integer fixed-point intervals. The Fourier centering constants use proved
cosine and logarithm series, not an unevaluated numerical infinite tail.
Both direct spectral and complementary remainder calculations are labeled
in the report. Same-author implementation agreement is not external review.

## Publication

This session verified GitHub reads but exposed no write action; direct Git
failed DNS. No new commit, PR update, or issue comment was published by this
session. [PUBLISHING.md](PUBLISHING.md) supplies an add-only continuation
procedure and the exact parent. The downloadable patch is intended for the
same #904 branch while preserving any newer work. Prior artifacts and
canonical statuses are not edited.
