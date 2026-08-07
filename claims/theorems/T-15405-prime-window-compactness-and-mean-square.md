# T-15405 — One prime window is almost periodic exactly on RH

Claim ID: `T-15405`  
Title: Translation compactness and bounded mean square of the pole-free prime window are equivalent to RH  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `T-15404`; elementary Laplace estimates; Bohr almost-periodic Fourier theory  
Scope: robust positive/negative resolution interfaces for the raw single-window statistic  
Related counterexample candidates: none

## Statistic

Let `Q_*` be the raw finite prime-power window of `T-15404`:

\[
 Q_*(x)=
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 G_*(x-\log n),
 \tag{T-15405.1}
\]

where the fixed smooth signed window `G_*` cancels the zeta pole and has a
Laplace transform nonzero at every shifted nontrivial zero in the open
counterexample strip.

## Equivalent criteria

The following are equivalent.

1. The Riemann Hypothesis is true.
2. `Q_*` is bounded on the right.
3. The family of right translates
   \[
    \{Q_*(\cdot+y):y\ge0\}
   \tag{T-15405.2}
   \]
   is relatively compact in uniform convergence on every right half-line after
   discarding one fixed compact initial interval.
4. `Q_*` has uniformly bounded Cesaro mean square: for one, hence every,
   sufficiently large `x_0`,
   \[
   \boxed{
    \sup_{X\ge1}{1\over X}
    \int_{x_0}^{x_0+X}|Q_*(x)|^2dx<\infty.}
   \tag{T-15405.3}
   \]

## RH implies uniform almost periodicity

Under RH, the smoothed explicit formula gives

\[
 Q_*(x)=
 -\sum_\rho
 e^{i\gamma x}\widehat G_{*,L}(i\gamma)
 +E_{triv}(x),
 \tag{T-15405.4}
\]

where `rho=1/2+i gamma`. The zero-counting bound and rapid transform decay make
the series absolutely and uniformly convergent. Its first term is therefore a
uniformly almost-periodic function. The trivial-zero term tends exponentially
to zero and has a relatively compact translate orbit.

This proves criteria 2--4 under RH.

## Mean square implies RH

Assume (T-15405.3), and absorb the fixed initial interval into the constant.
Then

\[
 A(X):=\int_0^X|Q_*(x)|^2dx\le C(1+X).
 \tag{T-15405.5}
\]

For every `sigma>0`, integration by parts gives

\[
 \int_0^\infty e^{-2\sigma x}|Q_*(x)|^2dx<\infty.
 \tag{T-15405.6}
\]

Cauchy--Schwarz then yields

\[
 \int_0^\infty e^{-\sigma x}|Q_*(x)|dx<\infty.
 \tag{T-15405.7}
\]

Hence the Laplace transform of `Q_*` is holomorphic on `Re z>0`. By
`T-15404`, that transform is

\[
 -\widehat G_{*,L}(z)
 {\zeta'\over\zeta}(z+1/2),
 \tag{T-15405.8}
\]

with the zeta pole canceled and no shifted nontrivial pole canceled in the open
strip. Therefore no zero has real part greater than `1/2`, and RH follows by
reflection.

Thus even an **average** failure of growth is sufficient; no pointwise sign or
uniform bound needs to be guessed first.

## Parseval variance under RH

For each distinct positive ordinate `gamma`, let `m_gamma` be the total
multiplicity at that ordinate. The Bohr mean square exists and equals

\[
\boxed{
 \lim_{X\to\infty}{1\over X}
 \int_0^X|Q_*(x)|^2dx
 =2\sum_{\gamma>0}
 m_\gamma^2
 |\widehat G_{*,L}(i\gamma)|^2.}
 \tag{T-15405.9}
\]

The series converges effectively. The factor two accounts for the conjugate
frequency pair. Trivial zeros contribute zero to the limiting mean.

Equation (T-15405.9) supplies a second proof-producing comparison:

1. upper-bound the RH variance using certified zero balls plus shell counts;
2. lower-bound a finite prime-window mean square by directed quadrature or exact
   piecewise integration;
3. a strict reversal disproves RH.

This criterion is robust against phase cancellation at isolated supports.

## False-RH growth

If a right-half-plane pole `z=delta+i gamma` is present, the prime-window signal
contains an exponentially growing mode of scale

\[
 e^{\delta x}.
 \tag{T-15405.10}
\]

Because the filter transform is nonzero there, the exponentially weighted mode
cannot disappear from the Laplace transform. Consequently the Cesaro mean
square cannot satisfy (T-15405.3). In generic isolated-pole situations it grows
on the scale `e^(2 delta X)/X`; the theorem needs only unboundedness.

## Compactness interpretation

`T-15405` is the scalar translation-space analogue of the collective-compactness
hinge in `L-14312`--`L-14315`.

```text
RH true:
  pole-free prime translates form a compact almost-periodic phase orbit.

RH false:
  a shifted pole creates an exponentially escaping translation mode.
```

The escaping-mode phenomenon in the scaled localized Weil packet and the
failure of translation compactness here are two realizations of the same
spectral obstruction.

## Empirical variance control

In the `10^7` run of `O-15401`, the direct pole-free statistic had empirical
mean square approximately

```text
2.90906e-5,
```

while the first-fifty-zero prediction from (T-15405.9) was approximately

```text
2.90403e-5.
```

The corresponding root-mean-square values were `0.00539357` and `0.00538890`.
These are non-directed controls only.

## Proof-producing form

A finite mean-square certificate may use a partition in `x` on which the prime
manifest and spline pieces are fixed. The checker integrates the squared fixed
prime sum exactly or outwardly on every cell. The RH-valid upper side uses:

- certified zero balls and multiplicities;
- transform interval maxima;
- shell-count majorants for the unlisted tail;
- trivial-zero and profile-evaluation budgets.

No oscillatory cancellation is used on either side of a strict comparison.

## Gap audit

- Relative compactness should be formulated in the exact function topology used
  by a final proof; boundedness alone is the simplest equivalent criterion.
- The Parseval identity groups coincident ordinates before squaring.
- A finite empirical average does not establish (T-15405.3).
- A lower mean-square interval must include correlations caused by shared prime
  terms and profile uncertainty.
- The theorem remains an RH-equivalent interface, not a proof of bounded mean
  square.
