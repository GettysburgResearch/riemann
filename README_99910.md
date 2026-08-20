# T99910 — Minimal ratio-eight ordinary-Möbius wavelet

This packet continues the corrected native-box route from PR #665 at exact head

```text
a771772682a2c09c026348b176618c302c49c223
```

**The Riemann Hypothesis remains unproved.**

## New exact reduction

Let

\[
W(y)=
\begin{cases}
0,&y<1,\\
8\sqrt y-8-3\log y,&1\le y<67,\\
8(1-67^{-1/2})\sqrt y-3\log67,&y\ge67.
\end{cases}
\]

The minimal causal dyadic annihilator of the three local modes
\(\sqrt y,1,\log y\) is

\[
\mathscr D=(I-\sqrt2\,S_2)(I-S_2)^2.
\]

Its box image has two transition shells and exact anti-symmetry:

\[
\mathscr DW=K_0-S_{67}K_0,\qquad \operatorname{supp}K_0\subset[1,8].
\]

Two exact positive resolvents then give

\[
\mathscr DB=(I-S_{67})G_\beta,\qquad
G_\beta=(I-67^{-1/2}S_{67})G_\mu,
\]

where

\[
G_\mu(X)=\sum_{n\le X}\frac{\mu(n)}{\sqrt n}K_0(X/n).
\]

Thus the seven-band decorated-\(\beta\) shell reduces, without changing any
native coefficient, to one ordinary-Möbius wavelet on the minimal ratio-eight
shell.

## Analytic contract

\[
\int_1^\infty G_\mu(X)X^{-s-1}\,dX
=
\frac{(s+\tfrac32)(1-\sqrt2\,2^{-s})(1-2^{-s})^2}
{s^2(s-\tfrac12)\zeta(s+\tfrac12)}.
\]

The added zeros lie only on `Re s=0` and `Re s=1/2`. Therefore

```text
subpower logarithmic negative mass of G_mu  -> RH.
```

Conversely RH gives the same subpower bound, so this is an RH-equivalent
minimal wavelet criterion.

Pointwise positivity is false already at `X=4`; the remaining theorem is a
signed ratio-eight Hardy/Carleson estimate, not a sign claim.

## Replay

```bash
python3 experiments/X-99910-minimal-mobius-wavelet/verify.py \
  --output experiments/X-99910-minimal-mobius-wavelet/results/verification.json
sha256sum -c T99910_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99910_MINIMAL_MOBIUS_WAVELET
```
