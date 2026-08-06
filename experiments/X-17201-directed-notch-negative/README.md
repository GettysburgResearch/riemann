# X-17201 — directed notched negative-route search

Status: `PARTIAL` for the exact RH envelope; `EMPIRICAL` for every prime scan  
Agent: `gpt56-172n-01/directed_search`  
Issues: #171, #172  
Date: 2026-07-31

## Checkpoint result

No RH counterexample was found.  The retained contribution is a fully explicit
finite rational filter, a compact exact-rational RH envelope, a reproducible
complete prime-power scan through `10^7`, and a slow independent rational
support checker.

For the retained filter, conditional on RH, on the explicit-formula
normalization in proposed theorem `T-15404`, and on its standard extension from
`C_c^infinity` windows to this compact `C^18` spline, exact rational arithmetic gives

```text
B_G =
103932170455171019230055079349619611820046863834964101
---------------------------------------------------------------------
1000000000000000000000000000000000000000000000000000000000000

    = 1.0393217045517102e-7 (rounded display only).
```

This proves the implication

```text
RH => |Q_G(x)| <= B_G
```

for every `x` at or beyond the exact support threshold recorded in
`results/rh-bound-N8-notch2-hp8-d128.json` (decimal display
`6.927795542999891`).  It is deliberately independent of every numerical zero
ordinate.  The compact interval before the support threshold is not included,
so this artifact matches issue #172's “beyond the support threshold” form, not
an unqualified all-real-x statement.

The matching complete `10^7` scan found

```text
minimum       -1.4359116748533417e-14  at x=18.05113474606469
maximum       +1.4008960266677526e-14  at x=15.470564488240901
empirical RMS  7.896471058367942e-15
max |Q|/B_G    1.3816e-7
```

Therefore no support in the retained ladder approaches the exact moat.

## Exact filter

For `B_r(z)=(1-exp(-rz))/(rz)`, use the rational box-width ledger

```text
1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128, 1/256,
444521223029/10^12,
298885617911/10^12.
```

The last two are exact rational designs obtained by rounding the first two
mpmath midpoint notch lengths.  Their proximity to actual zeta zeros is only
`EMPIRICAL`; none of the exact RH bound uses that proximity.

Let

```text
Fhat(z) = exp(-2z) product_r B_r(z)^2,
h       = log(4),
delta   = 1/128,
H(z)    = ((1-exp(-delta*z))/2)^8,
Ghat(z) = Fhat(z) (1-2exp(-h*z)) H(z).
```

In physical space,

```text
G = 2^-8 (I-T_delta)^8 (I-2T_h) F.
```

The normalized high-pass difference has coefficient l1 norm one; it is not a
free scalar rescaling.  All new high-pass zeros lie on `Re z=0`, all box zeros
lie on `Re z=0`, and the pole-annihilator zeros lie on `Re z=1/2`.  Hence the
filter has no zero in `0<Re z<1/2` and remains sensitive to every strict
rightward displacement.

The profile length is

```text
L = 86975029547/50000000000.
```

The convolution-square window adds `2L`, the pole shift adds `log(4)`, and the
eight high-pass shifts add `8/128`.

## Rational RH envelope

The nontrivial-zero part uses Hasanalizade–Shen–Wong, *Counting zeros of the
Riemann zeta function*, JNT 235 (2022), Corollary 1.2
([arXiv](https://arxiv.org/abs/2107.06506),
[DOI](https://doi.org/10.1016/j.jnt.2021.06.032)).  Their bound implies, for
`T>=e`,

```text
N(T) < 4 T log T.
```

Indeed, using `pi>3`, `e>27/10`, and `log log T <= log T`, the main term is at
most `(1/6)T log T`, the two logarithmic errors at most
`(3611/27000)T log T`, and `9.3675` at most `(1249/360)T log T`; their sum is
less than `4T log T`.

Positive ordinates are partitioned into `(0,4]` and dyadic blocks
`(2^j,2^(j+1)]`.  Each block deliberately uses the cumulative count

```text
N(2^(j+1)) <= 4(j+1)2^(j+1),
```

not an invalid difference of cumulative upper bounds.  On a block `[A,2A]`,

```text
|Ghat(it)| <=
3 min(1,delta*A)^8 product_r min(1,2/(r*A))^2.
```

Once every box bound is active, the remaining exact geometric ratio is
`2^(1-2d)` with `d=10`.  The resulting nontrivial-zero bound is
`1.0393216845359626e-7`.

For a trivial zero with `lambda=2m+1/2`, evaluating at the right support edge
cancels every exponential growth factor algebraically and leaves

```text
2^(1-8) min(1,delta*lambda)^8
product_r min(1,1/(r*lambda))^2.
```

The finite exact sum plus an integral tail is `2.0015747573687338e-15`.
The final published `B_G` is an exact decimal rational rounded upward from the
exact internal fraction; the internal fraction is digest-bound in the result.

## Reconnaissance and reproduction

The post-transient `10^6` ladder reproduces the existing X-15404 scales:

| Filter | empirical RMS | sampled range |
|---|---:|---:|
| unnotched | `5.42128e-3` | `[-9.67255e-3,+9.53659e-3]` |
| first notch | `7.33157e-5` | `[-1.09260e-4,+1.07598e-4]` |
| first two notches | `1.19182e-7` | `[-2.28848e-7,+2.30375e-7]` |

The `10^7` two-notch, no-high-pass control contains one sampled value
`-2.226495835e-7` just outside the first-50-zero absolute sum
`2.224251461e-7`.  This is **not** an RH-valid exceedance: higher zeros and
ordinary FFT/interpolation/accumulation errors are omitted.  It is retained as
an adversarial regression only.

The matching high-pass scan has a complete sorted 665,134-record manifest:

```text
ordinary primes       664579
all prime powers      665134
duplicate n records        0
manifest SHA-256
ad1fe1520966ca5c41885166f4a28a0d543922f087881175c0c15e89425fc56a
```

The bulk manifest is regenerated rather than committed.  Its canonical digest
stream is sorted ASCII `n,p,k\n`.

## Commands and environment

Retained runs used 64-bit Windows, Python 3.12.10, NumPy 2.3.5, and mpmath
1.4.1 for **empirical zero midpoints only**.

```powershell
python -m unittest discover -s tests -v

python rh_bound.py --dyadic-level 8 --notches 2 `
  --highpass-order 8 --highpass-delta-power 7 `
  --output results/rh-bound-N8-notch2-hp8-d128.json

python search.py --cutoff 10000000 --fft-size 262144 `
  --grid-points 1600 --dyadic-level 8 --notches 2 `
  --highpass-order 8 --highpass-delta-power 7 `
  --zero-count 50 --scan-floor 14 `
  --output results/search-N8-notch2-hp8-d128-1e7.json
```

`verify_support.py` is an independent pure-rational evaluator for small frozen
supports.  It encloses integer logarithms by an exact atanh series, encloses
`1/sqrt(n)` by integer square roots, and evaluates generalized Irwin–Hall
splines with exact rational truncated powers.  It is intentionally too slow
for the ten-box `10^7` producer; attempted five-box checks did not finish in
five minutes and no exact support result is claimed.

## Bugs and proof boundaries found

1. **Support factor of two.** A notch box of profile length `r` enlarges the
   convolution-square terminal annulus by `2r`, not `r`.  X-15404's
   `full_window_support_max` is correct, but L-15406/M-15403's shorthand
   “support cost r” is only a profile-side cost and is unsafe for manifest
   scheduling unless doubled.
2. **Finite mean square is not Bohr variance.** T-15405.9 is a limiting Bohr
   mean.  A single finite block may exceed that limit under RH because of
   off-diagonal sinc cross terms.  A negative certificate must use an explicit
   finite-block RH upper bound, not merely compare a block to the asymptotic
   variance.
3. **Trivial transient.** Zero-only comparisons below a safe scan floor can be
   dominated by trivial-zero terms.  All retained baseline comparisons use
   `x>=14`; the rational `B_G` separately includes a uniform trivial-zero
   bound for the matching high-pass filter.
4. **Certification backend isolation.** python-flint 0.9.0 and 0.7.1 crashed
   with Windows access violation `-1073741819` in the original subagent
   process.  A separately permissioned primary-agent process later replayed
   `refine_first100.py` successfully with python-flint 0.9.0 at 320 bits.  The
   original rational envelope and FFT scans use no FLINT output; only the
   distinctly labeled first-hundred refinement does.
5. **Analytic dependency.** `T-15404` remains `PROPOSED`.  The arithmetic in
   `rh_bound.py` is exact, but the result should not be promoted beyond
   `PARTIAL` until the explicit-formula convention and the cited HSW corollary
   receive independent source review.
6. **Finite-spline regularity.** The retained convolution square has 20 box
   factors and is `C^18`, not `C^infinity`.  Its transform decays as
   `O(|t|^-20)`, more than enough for the absolutely convergent zero sum used by
   the bound, but the repository's stated `T-15404` should explicitly record
   this finite-regularity extension before the certificate is promoted.

## Verdict

```text
UNRESOLVED
```

No directed support has `inf |Q_G| > B_G`, and no finite-block RH mean-square
bound was exceeded.

## Certified first-100 refinement

The distinct Arb replay in `refine_first100.py` and
`REFINEMENT-first100.md` closes the apparent `1.4359e-14` FFT crossing.  Arb
certifies the first 100 zeros and `N(237)=100`; the Hadamard reciprocal-mass
identity gives a rigorous bound for every higher zero.  The resulting complete
nontrivial-zero line envelope is below the declared rational ceiling
`1.494e-14`, which is still above the FFT magnitude.  At the reported minimizer
the first-100 spectral value is about `-1.37345055e-14`; its `6.2461e-16`
difference from the FFT value is covered by the `9.4087e-16` higher-zero bound.
An exact-support attempt at that sample is therefore not warranted.
