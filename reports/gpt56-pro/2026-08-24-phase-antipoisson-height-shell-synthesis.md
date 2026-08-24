# Phase variance, anti-Poisson descent and height-shell winding

## Executive result

The zero-height/spatial-escape obstruction on PR #729 is now represented in
three exact coordinates which share one reciprocal Xi source:

1. a normalized Herglotz **unit-phase variance**;
2. an exact **backward Poisson** evolution in the descended base height;
3. an integrated **height-shell all-pass winding** paid by negative
   `H^(1/2)` energy.

The frozen arithmetic source is

\[
\sum_n b_L(n)(1+h\log n)n^{-\sigma}e^{ia\log n},
\qquad b_L(n)\ge0.
\]

The frequency `log n` is simultaneously the one-sided Hardy translation,
the anti-Poisson amplification frequency and the all-pass phase frequency.

RH remains unproved.

## Contact rigidity

At the maximal zero-height Pick base, normalize the Herglotz measure into a
probability law with unit phases

\[
\omega_z(t)={t-\bar z\over t-z}.
\]

Then

\[
{y f'(z)\over\Im f(z)}=\mathbb E\omega_z
\]

and

\[
\mathcal C_f(a,y)
=-{\Im f(z)\over4}\mathbb E|\omega_z-1|^2.
\]

After descending the base by `delta`, a nonnegative contact at distance `y`
above the original Pick base forces

\[
\mathbb E|\omega_z-1|^2
\le {2\delta\over y+\delta}.
\]

For shallow contacts this sends the normalized Pick map to the identity and
evacuates the Herglotz measure from every fixed local window.

## Exact backward evolution

The lower-base field has Fourier multiplier

\[
-\frac\pi2(1+h|\xi|)e^{-(h-\delta)|\xi|}.
\]

Since the top-base field has the same multiplier with `e^(-h|xi|)`, and Xi's
affine Herglotz coefficient vanishes,

\[
\mathcal C_h^{[\delta]}
=e^{\delta|D|}\mathcal C_h^{[0]}.
\]

The base-height problem is therefore literally anti-diffusive.

In physical space, every nonnegative contact satisfies

\[
\mu([a-y,a+y])
\le2\delta y
\int_{|t-a|>y}{d\mu(t)\over(t-a)^2}.
\]

This is the exact local source inequality a proof must contradict.

## Finite-model firewall

For a finite positive Herglotz measure of total mass `M`,

\[
\mathcal C_h^{[\delta]}(a)
={\delta M\over2a^2}+O(a^{-3})>0
\]

at large spatial centre. Hence no finite real-rooted polynomial, rational Pick
map or compact truncation can validate global downward-base negativity. The
infinite Xi source and its remote tail are load bearing.

## Height-shell topology

For a real polynomial,

\[
\Theta_{p,h}(x)={p(x+ih)\over p(x-ih)}
\]

has winding minus the number of roots in `|Im rho|<h`. The quotient between two
heights counts one horizontal shell. Along the derivative ladder, adjacent
shell quotients telescope exactly.

Negative winding is paid by negative Hardy energy:

\[
-\deg U
\le
\sum_{n<0}|n||\widehat U(n)|^2.
\]

If a terminal derivative is shell-free, then in a finite rectangle

\[
M_0
\le
\sum_{k<R}\mathcal E_-(U_k)
+\text{one telescoped endpoint correction}.
\]

The shell count is even, so a strict total below two empties the shell.

## Unified producer

In reflected coordinates,

\[
-2\mathcal C_{r,b}(a,h)
=
\Re(q_r-hq_r'),
\qquad q_r={\xi^{(r)}\over\xi^{(r+1)}}.
\]

For the frozen rung-zero reciprocal Dirichlet source,

\[
q_L-hq_L'
=
\sum_n b_L(n)(1+h\log n)n^{-s}.
\]

The existing one-sided Hardy theorem supplies a strict phase gap for these
positive coefficients before physical collapse. The two exact remaining
consumers are:

```text
DMPXFER105603 — preserve the pointwise differential phase reserve through the
physical archimedean/freezing/taper/error ledger;

HSHE105602 — preserve enough negative H^(1/2) shell energy and the single
endpoint difference to remain below two.
```

A mixed proof is plausible: use pointwise phase variance on diffuse regions
and charge only concentrated phase slips to the shell `H^(1/2)` budget.

## Replay

```text
PASS_X_105600_PHASE_BARYCENTER_ANTIPOISSON_SHELL
checks=2187
proof object:
6127ff8f37d767ca34b32a271ae44c10a469d5783a0c31a5f078453ade71b9df
RH_UNPROVEN
```

The replay authenticates finite exact algebra only. It does not prove the Xi
physical transfer, spatial-escape exclusion, moving saddle or RH.
