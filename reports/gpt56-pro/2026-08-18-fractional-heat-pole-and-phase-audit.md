# Hostile audit of the fractional Julia–Tao–Hermite candidate

Agent: `gpt56-pro`  
Date: 2026-08-18  
Frozen head: PR #613 at `f28aa51a6d6740067202611d8ebda4be2ef0a1c9`

## Verdict

The candidate does not prove RH. Two independent load-bearing interfaces fail.

### A. The energy theorem is analytically false

The fractional power has the local branch

\[
B_\diamond(s)^\theta=(3/8)^\theta(s-1)^\theta(1+O(s-1)).
\]

The exact heat packet therefore has center-zero energy

\[
\mathcal E_{\theta,T}(0)
\sim
\frac{4\pi(3/8)^{2\theta}}
     {\sqrt3\,\Gamma(-\theta)^2}
 e^{T/2}T^{-2\theta-1}.
\]

For `theta<1/192`, this contradicts the claimed upper exponential rate
`96 theta`. This effect exists regardless of RH.

### B. The Tao port is not phase-ready

The positive complementary-semigroup identity is specific to phase zero. At
`P={3}`, `x=3`, and `tau=pi/log 3`, the phased off-diagonal is `4/3` while the
Tao diagonal is `8/9`; the Schur determinant is `-80/81`. Thus the local atoms
do not automatically pay the logarithmic carrier used by the Fock heat packet.

## Surviving material

The following PR #613 results remain useful:

```text
fractional positive even/odd coefficient channels       retained;
native defect factorization at theta=1/2               retained;
unphased atomwise Tao decomposition                     retained;
local off-line branch growth after a valid contour      potentially retainable.
```

The uniform energy theorem, the direct-limit proof, and the claimed RH
composition are rejected in their current forms.

## Connection to PR #615

PR #615 independently records that every nonzero fractional positive channel
retains the real zeta pole and that trace-free extraction remains open. The
explicit asymptotic here quantifies that firewall: the unremoved carrier has
energy exponent exactly `1/2`.

## Corrected frontier

A possible successor must use a genuinely pole-subtracted observable and a
new phase-covariant completion. Proving its upper heat rate remains an open,
RH-bearing theorem. No remaining object is relabelled as proved.
