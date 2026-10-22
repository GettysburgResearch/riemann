# Carry Green phase-frame proposal — full research report

Agent: `gpt56-pro-22`  
Date: 2026-08-07  
Status: `FULL PROPOSAL / RH NOT PROVED`

## Repository-wide conclusion

The newest arithmetic branches agree that every route which preserves the true
Möbius source ends at a balanced signed core. The reflected endpoint-count
shortcut does not remove that source, and the first Farey cell is already an
RH-equivalent Mertens increment.

The elementary carry route remains attractive because the prime side is
positive after Legendre's formula. The previous formulation, however, asked for
the full pointwise positivity of one exact triangular inverse. This pass found a
strictly weaker target and an exact factorization that makes it visible.

## New exact algebra

The carry matrix satisfies

\[
(n+1)\beta_{nq}
 =(n+1)\lfloor n/q\rfloor-2\sum_{j\le n}\lfloor j/q\rfloor.
\]

After Möbius transformation,

\[
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
 =\frac{2m-n-1}{n+1}.
\]

Thus the floor matrix becomes an affine Green kernel. If

\[
s_m=\sum_{n\ge m}\frac{c(n)}{n+1},
\]

then

\[
s_m=\frac{m u_m+\sum_{\ell>m}u_\ell}{m(m-1)},
\qquad
c(m)=(m+1)(s_m-s_{m+1}).
\]

Full Carry Saturation is only monotonicity of this one profile.

## Stronger conceptual simplification

The cumulative carry derivative is

\[
\Delta_{mq}=m\mathbf1_{q|m}-\lfloor m/q\rfloor.
\]

The cumulative logarithmic-binomial increment is

\[
L_m=\log\frac{m^{m-1}}{(m-1)!}>0.
\]

Therefore any nonnegative cumulative profile `sigma_m` with

\[
\sum_m\sigma_m\Delta_{mq}\le w_X(q)
\]

gives the positive prime-ramp lower bound

\[
P_X\ge\sigma_2\log2+\sum_{m\ge3}\sigma_mL_m.
\]

The profile need not be decreasing. Exact coefficient positivity is genuinely
stronger than the RH-facing certificate.

## Unconditional atom dictionary

For every endpoint `T`, the exact inverse coefficients are nonnegative whenever
`5n>T`. This outer region splits into four quotient bands. Each band is an
explicit nonnegative carry atom with a positive binomial-entropy score.

The new global target is to combine these already-proved atoms over many
endpoints without exceeding `w_X`, while retaining entropy
`4sqrt(X)-X^{o(1)}`.

## Why phase and four bands

A single geometric endpoint ladder leaves a fixed continuum deficit. Splitting
the four quotient bands gives activation phases `0,log2,log3,log4` modulo
`log5`.

In the continuum scaling limit the four log kernels `k_r` satisfy

\[
\sum_rk_r(v)=v\quad(0\le v<\log5)
\]

and

\[
\int e^{-v/2}k_r(v)dv=h_r,
\]

where `h_r` is the entropy mass of the band. Consequently any positive renewal
that fills the target has total critical mass exactly

\[
\int_0^\infty ve^{-v/2}dv=4.
\]

The constant four is therefore structural, not numerically fitted.

## Exact remaining theorem

Prove a four-input positive Volterra renewal on logarithmic phase, with residual
critical mass tending to zero, and transfer it to finite floors with
`X^{o(1)}` absolute loss.

This theorem is sharply falsifiable by a fixed-gap dual phase functional or a
phase cell requiring a negative band weight.

## Reconnaissance

A nondirected SciPy/HiGHS implementation used only the positive outer atoms.
Representative sparse log-phase runs gave:

```text
X=500,  H=32: restricted objective / finite P_X = 0.9998792934
X=1000, H=64: restricted objective / finite P_X = 0.9997761433
X=2000, H=64: restricted objective / finite P_X = 0.9997349652
X=5000, H=16: restricted objective / finite P_X = 0.9992505541
```

Using every integer endpoint gave:

```text
X=500:  ratio = 0.9999967809
X=1000: ratio = 0.9999902833
```

Solver tolerances were ordinary floating point. These values do not certify
feasibility exactly and do not establish the asymptotic constant four. They show
only that the four-band cone does not display an obvious fixed finite-scale
loss.

## Proposed proof spine

```text
exact carry-floor identity
-> Möbius affine Green kernel
-> cumulative positive entropy basis
-> unconditional outer four-band atoms
-> four-band positive phase renewal
-> finite floor/BV transfer
-> prime ramp >= 4 sqrt(X)-X^o(1)
-> subpolynomial upper square-screw envelope
-> one-sign Landau continuation
-> RH.
```

## Honest boundary

The first four arrows are supplied as proposed complete elementary mathematics.
The positive phase renewal and its finite-floor transfer are open. They are not
routine details and are the exact review hinge. RH is not proved.
