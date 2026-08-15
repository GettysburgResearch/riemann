# Handoff — Centered-Q4 cubic closure successor to PR #483

## Publication identity

```text
intended base PR:
#483

base branch:
agent/first-hermite-q4-prime-coherence

base SHA:
87bd7ad2127f98b6141b4c03355556f2b95f6404

successor branch:
research/gpt56-pro/93250-centered-q4-cubic-closure
```

RH remains unproved.

## What changed

The packet proves, subject to independent review, that the complete Q4 endpoint **variance** is already RH-equivalent. The endpoint mean used by earlier consumers is not necessary.

One fixed weight

\[
w(\theta)=\theta(1-\theta)-1/6
\]

extracts the exact cubic scalar

\[
\mathcal A_\circ(N)
=\sum_{m\le N}c_\circ(m)
 {m\over N}\left(1-{m\over N}\right)
 {2m/N-1\over3}.
\]

Its Mellin multiplier is

\[
\frac{s-1}{3(s+1)(s+2)(s+3)},
\]

which is zero-free in the open critical strip.

The centered Cauchy bridge is

\[
|\mathcal A_\circ(N)|^2
\le{N\over180}\mathscr V_\circ(N).
\]

Therefore

\[
\mathrm{RH}
\iff
\mathscr V_\circ(N)\ll\log^A N.
\]

## Q4 major-arc effect

Centering removes the zero frequency. With the exact PR #474 estimates,

\[
\left|
\mathscr V_\circ(N)
-\mathfrak C_{\ne p}^{\mathrm{maj},0}(N)
\right|
\le1464\log(2N).
\]

Hence RH is equivalent to a polylogarithmic bound for fewer than
\(2\sqrt N+O(1)\) **nonzero** distinct-prime major modes. No mean or same-prime term remains.

## Common First-Hermite/Q4 endpoint

The cubic scalar decomposes as

\[
\mathcal A_\circ(N)=\sum_pZ_{p,N},
\qquad
\sum_p|Z_{p,N}|^2
\le{20\over243}N\log(2N).
\]

The frozen First-Hermite scalar has

\[
S_{q,a}(t)=\sum_pY_{p,q,a}(t),
\qquad
\sum_p|Y_{p,q,a}(t)|^2\ll q+1.
\]

Both final obstructions are one-dimensional prime-block coherence ratios.

## Review order

```text
1. L-93250
2. T-93251
3. L-93252
4. T-93253
5. R-93254
6. T-93255
7. M-93250
8. X-93250
9. report
```

## Exact frozen dependencies

```text
PR #483
87bd7ad2127f98b6141b4c03355556f2b95f6404

PR #474
0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b

PR #392
d2387cd21eb891a8801fd122bc8d0ddd7c1c0fc4

PR #390
ea20af8867c3119c23efc27738d343aac2f79362

PR #383
d764be15bd8ea902ad260484eab44d19a9e82175
```

`R-90412` is normative. Do not import `L-90419` as an unconditional macroscopic Selberg theorem.

## Replay

```bash
cd experiments/X-93250-centered-q4-cubic
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_X_93250_CENTERED_Q4_CUBIC
```

## Smallest next theorem

The preferred producer is Cubic Prime-Block Decorrelation:

\[
\left|\sum_pZ_{p,N}\right|^2
\ll N\log^B N.
\]

Equivalent targets are the mean-free nonzero Q4 major arc or the independent First-Hermite one-carrier exclusion.

## Exact boundary

```text
all source/normalization/Mellin interfaces  proposed complete
mean removal                               proposed complete
same-prime cubic diagonal                  proposed complete
minor-arc removal                          imported exact
deterministic distinct-prime decorrelation open / RH-bearing
RH                                         unproved
```
