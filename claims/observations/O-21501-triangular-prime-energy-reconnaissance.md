# O-21501 — Triangular terminal-prime energy reconnaissance

Claim ID: `O-21501`  
Status: `EMPIRICAL / DISCOVERY ONLY`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215  
Experiment: `X-21502`

## Computation

The complete von Mangoldt manifest through

\[
 10^7
\]

contains

\[
 665134
\]

prime powers. Using the exact piecewise-linear shape of the `L-21501` window,
a deterministic long-double event sweep evaluated every complete unit block

\[
 \mathcal B_G(j)=\int_j^{j+1}|Q_G(x)|^2dx,
 \qquad 2\le j\le16.
\]

The code also accumulated the diagonal Gram contribution separately.

## Observed cancellation

After the short initial transient, the total energy is tiny while the diagonal
grows:

| `j` | total energy | diagonal | off diagonal | total / diagonal |
|---:|---:|---:|---:|---:|
| 5 | 0.00203813 | 6.61923 | -6.61719 | 3.08e-4 |
| 8 | 0.00149011 | 16.57970 | -16.57821 | 8.99e-5 |
| 12 | 0.00126627 | 29.70407 | -29.70280 | 4.26e-5 |
| 16 | 0.00156048 | 42.49387 | -42.49231 | 3.67e-5 |

Across blocks `5` through `16`, the total remains between approximately

\[
 0.00124\quad\text{and}\quad0.00204,
\]

while the diagonal increases by more than a factor six. The off-diagonal term
cancels more than `99.99%` of the diagonal in the later blocks.

This is the arithmetic cancellation that an RH proof must control. An
entrywise absolute-value estimate would replace a quantity near `0.0015` by a
quantity of order `40` at the last retained block.

## Interpretation

Under RH, `T-21501` predicts a bounded/almost-periodic critical-line signal, so
bounded-size block energies are natural. Under a hypothetical off-line zero,
the upper envelope must eventually grow exponentially.

The finite data do not distinguish those alternatives. They do show that:

1. the selected finite window exposes enormous coherent prime-pair
   cancellation;
2. the cancellation is already stable across twelve consecutive complete
   blocks;
3. the correct analytic target is a structured off-diagonal identity or
   dispersion estimate, not a better diagonal majorant;
4. the nonlinear Selberg equation of `L-21503` is a plausible source of the
   cancellation.

## Candidate theorem suggested by the data

A direct full-resolution theorem would be any uniform estimate of the form

\[
 \boxed{
 \mathcal B_G(j)\le\exp(o(j)).}
\]

A stronger bounded or polylogarithmic estimate is consistent with the retained
range but is not claimed.

A productive intermediate target is a scale-recursive inequality

\[
 \mathcal B_G(j)
 \le C(1+j)^A
 +\varepsilon_j
  \max_{k\le j-1}\mathcal B_G(k),
 \qquad
 \varepsilon_j\to0,
\]

obtained by pairing the exact Selberg log-convolution identity with the Gram
kernel before absolute values. Such an inequality would immediately yield the
required subexponential envelope.

## Proof boundary

- The prime-power enumeration is complete through `10^7`.
- Blocks `2,...,16` are complete for that cutoff.
- Arithmetic used long double, not directed intervals.
- No independent compiler/backend replay was performed.
- The values are empirical nominations for an analytic identity, not proof
  evidence for RH.
