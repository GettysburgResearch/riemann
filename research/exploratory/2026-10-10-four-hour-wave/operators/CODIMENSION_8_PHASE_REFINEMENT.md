# Phase-aware codimension-eight coercivity at L=1

Date: 2026-10-10. This theorem uses the literal whole source and the inherited
operator/source-domain hypotheses O1--O4. Its directed transcendental coverage
uses python-flint0.8.0 (Arb), unlike the prior rational-only codimension14
coverage. Independent review is requested. It does not establish effective
Schur positivity or RH.

Set \(b=3/2,c=1/2\) and

\[
E_8=\operatorname{span}\{e^{ct},e^{-ct},\cosh(bt),
                         \sin(j\pi t):1\le j\le5\},\qquad V_8=E_8^\perp.
\]

**Claim.** Every \(h\in V_8\) satisfies

\[
q(h,h)\ge\frac16\|\phi_h'\|_2^2
          +\tau_2|\langle\sinh(bt),h\rangle|^2,
\quad\phi_h''-c^2\phi_h=h,
\quad\tau_2=\sum_{n\ge3}\Lambda(n)/n^2.
\tag{1}
\]

Thus the audited positive sector has an eight-dimensional exact complement.
The lower residual enclosure for any exact trials in this sector is

\[
U-\frac{27}{2}R\preceq S\preceq U.
\tag{2}
\]

The larger coefficient in (2) reflects the smaller primitive gap; it is not a
claim that dimension8 automatically gives a better numerical Schur enclosure.

## All-frequency line retaining the prime phase

Reuse the exact X=2 source-tail decomposition and Fourier/primitive identity
in `CODIMENSION_18_COERCIVITY.md`. With \(x=\omega^2\),

\[
P(x)=\frac{(x+1/4)^2}{x+9/4},\quad
V_2(\omega)=\Omega(\omega)-2q_2\cos(\omega\log2),\quad
\Omega(\omega)=\Re\psi(1/4+i\omega/2)-\log\pi.
\]

The new coverage proves the literal supporting line

\[
P(x)V_2(\sqrt x)\ge\frac45x-244\quad(x\ge0).
\tag{3}
\]

As before, \(\Omega(0)>-43/8\), \(q_2<491/1000\), and

\[
\Omega(\sqrt x)-\Omega(0)=
\sum_{k\ge0}\frac{16x}{(4k+1)((4k+1)^2+4x)}.
\]

The exact elementary bounds are replayed using Fraction arithmetic and Machin
arctangent/logarithm series. On each integer cell \([a,a+1]\), retain
\(k=0,\ldots,256\) at \(x=a\), rounding its positive sum down at scale
\(2^{100}\). Compute the complete phase interval

\[
\sqrt a\log2\le\theta\le\sqrt{a+1}\log2
\]

with directed Arb endpoints and an enclosing union ball. Arb cosine encloses
\(\cos\theta\) on the entire interval, including any extremum inside it.
The exact positive \(q_2=\log2/\sqrt2\) is enclosed by outward balls, so
\(-2q_2\cos\theta\) is bounded in the correct direction for **both signs**
of the cosine. In particular, the negative-cosine region is not treated by
multiplying its sign by an upper bound for \(q_2\).

Let \(v_a\) be the resulting directed lower endpoint for \(V_2\). The
function \(P\) is positive and increasing. When \(v_a<0\), bound its product
using \(P(a+1)v_a\); otherwise use \(P(a)v_a\). Subtract
\((4/5)(a+1)\), add244, and check strict positivity. Every one of4096 cells
passes. The minimum certified margin exceeds4.8455, at cell331.

On the unbounded tail, discard the phase again and use the same positive
partial gamma sum at4096. Its rational lower value is

\[
v_\infty=
\frac{210504802984478740971221621778721}
 {158456325028528675187087900672000}>\frac45.
\]

Since \(P(x)\ge x-7/4\),
\(P(x)V_2\ge v_\infty x-(7/4)v_\infty\), which implies (3) because
\(244>(7/4)v_\infty\). Therefore the unbounded frequency tail is covered,
not sampled.

## Primitive gap and exact complement

The inherited clamped inverse and Fourier identity imply from (3)

\[
q_2(h,h)\ge\frac32\left(\frac45\|\phi_h'\|_2^2
                                -244\|\phi_h\|_2^2\right).
\]

The first five sine moments of \(h=\phi''-c^2\phi\) transfer to those of
\(\phi\) by integrating twice. The clamped endpoint conditions remove both
boundary terms. Poincare on the remaining sine modes gives

\[
\|\phi\|_2^2\le\frac1{36\pi^2}\|\phi'\|_2^2.
\]

Using \(\pi>3.1415\), the directed lower gap is

\[
\frac32\left(\frac45-\frac{244}{36(3.1415)^2}\right)
=\frac{1648682}{9707235}>\frac16.
\]

The exact whole-source tail adds the nonnegative sinh moment because the
cosh moment is zero. This proves (1). The five sines and three exponential
functions are linearly independent, so the complement dimension is eight.
The audited source coupling and the gap \(1/6\) give
\(b^2/(1/6)=27/2\), proving (2).

This argument uses a global supporting line plus Poincare; it does not infer
Fourier support from finitely many sine moments. Ordinary numerical LP scans
suggested the line, but every accepted frequency cell and the infinite tail
are enclosed independently by the directed checker.

## Replay

Install `python-flint==0.8.0`, or use the environment's isolated installation
at `/tmp/riemann-wave-python`. Run:

```sh
PYTHONPATH=/tmp/riemann-wave-python python -B check_codimension8_phase.py
PYTHONPATH=/tmp/riemann-wave-python python -O -B check_codimension8_phase.py
```

`codimension8_phase_certificate.json` records the outward receipt;
`codimension8_phase_replay_receipt.json` records normal/optimized replay
identity and all helper hashes. Acceptance checks use explicit exceptions and
remain active under Python optimization. Arb's outward transcendental
operations are part of this proof's computational trust base.
