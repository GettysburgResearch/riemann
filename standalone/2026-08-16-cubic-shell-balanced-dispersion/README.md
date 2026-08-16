# Cubic-shell balanced-dispersion packet

Frozen predecessor:

```text
PR #498
6cc0da2fa5711017e260ebdcea4ba8c22e453288
```

This packet independently reconstructs the centered cubic Q4 analytic spine and then replaces the open prime-block statement by an explicit arithmetic reduction.

## Main result

Unconditionally,

\[
\mathcal A_\circ(N)
=
\operatorname{BCD}(N)
+O\!\left(\sqrt N(\log(2N))^3\right),
\]

where

\[
\operatorname{BCD}(N)=
\sum_{\substack{N^{1/3}<m,\ell\le N^{2/3}\\N^{3/4}<m\ell\le N}}
\left(\sum_{\substack{d\mid m\\d>\lfloor N^{1/3}\rfloor}}\mu(d)\right)
\Lambda(\ell)F(m\ell/N)
\]

and the scale-four cubic wavelet is

\[
F(x)=K(x)-4K(4x)\mathbf1_{x\le1/4},
\qquad
K(x)=\frac{x(1-x)(2x-1)}3.
\]

The packet proves:

- the centered cubic identity, interpolation and Mellin pole audit;
- reduction to a large-prime shell;
- two vanishing Mellin moments;
- exact mod-four grid cancellation;
- every Vaughan Type-I estimate;
- the Type-II range \(m\ell\le N^{3/4}\) at square-root scale;
- an exact First-Hermite Calderón frame for the cubic wavelet.

The final balanced covariance estimate is stated openly and is not proved here.

## Review order

```text
L-93300
R-93300
L-93301
L-93302
L-93303
L-93304
T-93305
O-93300
M-93300
X-93300
```

## Replay

```bash
cd experiments/X-93300-cubic-shell-dispersion
python3 verify.py --output results/verification.json
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
cd ../..
sha256sum -c standalone/2026-08-16-cubic-shell-balanced-dispersion/CONTENT_SHA256SUMS
```

Expected:

```text
PASS_CUBIC_SHELL_BALANCED_DISPERSION_REDUCTION
283634ae3674d2a5059c79528c1b02a37bdb7d43b8b3210fd20f3aeb2e5835dd
```

## Status

```text
unconditional finite/analytic reductions   PROVED / REVIEW
balanced cubic dispersion                  OPEN / RH-EQUIVALENT
Riemann Hypothesis                         UNPROVED
```
