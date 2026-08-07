# Agent report — cofinal Finsler completion audit

Agent: `gpt56-04-f`  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Date: 2026-07-31  
Status: **the requested unconditional cofinal inequality was not proved**

## Objective

The requested final step was

\[
 x^{\mathsf T}A_{p_j}x>0
 \quad
 (0\ne x\perp p_j,
  \ x^{\mathsf T}B_{p_j}x=0)
\]

cofinally, equivalently strict separation of all simple-root Bézoutian
thresholds. Together with target-transform convergence this would prove RH.

I audited the newest positive-path branches and attempted to replace the
condition by consequences of:

- the exact Hermite global radical;
- the mode-8 prolate gap;
- the Rayleigh-floor bypass;
- the localized-Weil/prolate trace-form comparison;
- definite-slope target completion;
- total-positivity and Jensen/hyperbolicity results.

No existing theorem supplies the required actual localized-Weil comparison.
The strongest current mode-8 theorem is exact only for the pure prolate defect
model; its transfer to the complete arithmetic form remains an explicit open
hypothesis.

## Exact positive contribution — L-15110

For arbitrary `mu,c` define

\[
 r=Qp-\mu p-c\eta.
\]

Then

\[
 T_p(c)=Q-\mu I-c\eta\eta^{\mathsf T}
       -\operatorname{diag}(r_i/p_i).
\]

If one positive diagonal metric `M=diag(m_i)` satisfies

\[
 Q-\mu I-c\eta\eta^{\mathsf T}
 \succeq gM
 \quad\text{on }p^\perp
\]

and

\[
 |r_i|\le\rho |p_i|m_i,
 \qquad \rho<g,
\]

then

\[
 T_p(c)\succeq0,
 \qquad
 \ker T_p(c)=Rp.
\]

This is an exact quantitative route to the desired cofinal condition. It
isolates the two missing zeta-specific estimates:

1. an actual arithmetic complement floor;
2. a coordinate-relative radical-tail residual, uniform over the growing band.

Ordinary transform convergence or an ordinary residual norm does not imply the
second estimate when target coefficients become small.

## Exact negative contribution — R-15102

For every `N>=1`, define

\[
 R_N(z)=\sum_{n=-N}^{N}\frac{(-1)^n}{z-n},
 \qquad
 P_N(z)=\prod_{m=-N}^{N}(z-m)R_N(z).
\]

An exact alternating-series argument proves that `P_N` has no real root.
Nevertheless

\[
 \sin(\pi z)R_N(z)\to\pi
\]

locally uniformly on `C`.

Thus a sequence of finite cardinal transforms may converge locally uniformly to
a nonzero zero-free entire function while every finite numerator has only
nonreal roots. By the special-completion converse, no positive special matrix
with the prescribed kernel exists at any finite level.

This refutes the inference

```text
target convergence + vanishing tail
=> eventual Finsler completion.
```

It also proves that fixed-band expanding-support Fourier targets eventually
remain in a non-real-rooted cardinal neighborhood. Any viable diagonal must use
a genuinely growing global-root control, not merely a tail estimate.

## Exact software

`X-15104` reconstructs the cardinal numerator with Python integers and
`fractions.Fraction`, then counts distinct real roots using an exact Sturm chain.

Retained result:

```text
N=1,...,24
exact real-root count at every level = 0
proof digest = dbb89c2554290c9e3231a080262de4a8bcae4626f1df4a8562a00ed74f6bec65
```

Seven adversarial tests pass, including an all-positive-residue control with all
numerator roots real.

## Empirical reconnaissance

Ordinary high-precision scouts of the canonical Fourier-projection target and
cutoff-free Weil matrices did not locate a passing scalar completion at the
modest levels tested. Those computations are not directed and are not retained
as mathematical conclusions.

Their only strategic use is consistent with the exact obstruction: spurious
cardinal roots and negative complement minima are not automatically removed by
increasing ordinary precision.

## Literature boundary

The available primary literature gives:

- finite special-matrix real-zero transfer;
- exact finite Guinand--Weil dictionaries;
- localized Weil/screw operators;
- pure prolate concentration asymptotics;
- eventual fixed-degree Jensen hyperbolicity;
- low-order total positivity and partial Toeplitz-minor wedges.

It does not prove:

- growing-degree Jensen hyperbolicity in the approximation regime;
- total positivity of all orders for the Riemann kernel;
- an actual mode-8-scale localized-Weil/prolate sandwich;
- the cofinal Finsler isotropic-cone inequality.

## PDF decision

The user requested a final proof PDF only after the unconditional step was
completed. Since that step did not survive the gap audit, I did not create or
publish a document labeled as a proof of RH. Producing such a PDF would
misrepresent the mathematics.

A separate audit/nonproof note can be prepared if explicitly requested.

## Exact point reached

The target-pinned program now has:

1. a complete finite Finsler/Bézoutian decision;
2. exact positive and negative finite certificates;
3. a quantitative residual/coercivity sufficient theorem;
4. an exact obstruction showing convergence alone is inadequate.

The unresolved theorem remains genuinely arithmetic:

\[
 \rho_j<g_j
\]

cofinally in `L-15110`, or an alternative theorem directly separating every
Bézoutian threshold. No current repository result establishes it.