# Zero-slack symbol-capacity refutation

Agent: `gpt56-pro-09-f`  
Date: 2026-07-31  
Issue: #156  
Stack: draft PR #163

## Verdict

The requested inequality

\[
 {1\over\pi}\int_{\mathbb R}(\Gamma_j-s_j)_+
 \le d_j(\Gamma_j-\alpha_j)
\]

cannot hold at any nontrivial finite Suzuki level under the same lower-symbol
and low-packet hypotheses. The opposite inequality is strict.

## One-line mechanism

Let

\[
 D_\Gamma=P_I\mathcal F^{-1}(\Gamma-s)_+\mathcal FP_I.
\]

The lower symbol gives

\[
 A\succeq\Gamma I-D_\Gamma.
\]

If `A|L<=alpha I`, `alpha<Gamma`, and `dim L=d`, then

\[
 PD_\Gamma P\succeq(\Gamma-\alpha)P,
\]

so the packet captures trace at least `d(Gamma-alpha)`.

But every nonzero time-frequency localization `D_Gamma` is strictly positive on
all nonzero time-limited vectors: the Fourier transform of a compactly
supported nonzero function is entire and cannot vanish on the positive-measure
set where `(Gamma-s)_+>0`. Therefore `D_Gamma` has strictly positive trace on
`L^perp`.

Hence

\[
 \operatorname{Tr}D_\Gamma
 =\operatorname{Tr}(PD_\Gamma P)
  +\operatorname{Tr}(QD_\Gamma Q)
 >d(\Gamma-\alpha).
\]

On `I=[-1,1]`, the trace is exactly the requested left side.

## Source of the preceding error

The valid Berezin inequality is

\[
 \operatorname{Tr}
 (D_G-(G-\Gamma)I)_+
 \le {1\over\pi}\int(\Gamma-s)_+.
\]

The left side spectrally clips the compressed operator and can have finite
rank. The right side is the full trace of another localization operator and is
infinite-rank whenever nonzero. Spectral functional calculus does not commute
with time-frequency compression.

Thus the Berezin upper bound is valid but too coarse to be saturated.

## Correct continuation targets

The nonvacuous choices are:

1. operator-clipped saturation,
   \[
   \operatorname{Tr}(D_G-(G-\Gamma)I)_+
   \le d(\Gamma-\alpha);
   \]
2. the exact leverage tail,
   \[
   \operatorname{Tr}(QD_\Gamma Q)
   ={1\over2\pi}\int
   (\Gamma-s)_+\|Qe_\xi\|^2d\xi;
   \]
3. a strictly positive but vanishing unweighted excess,
   \[
   \Delta_j
   ={1\over\pi}\int(\Gamma_j-s_j)_+
    -d_j(\Gamma_j-\alpha_j)
   \downarrow0.
   \]

The third condition gives the actual complement floor

\[
 A_j|_{L_j^\perp}
 \succeq(\Gamma_j-\Delta_j)I.
\]

## Repository correction

- Added `R-15603` with the complete proof.
- Rewrote `L-15620` to preserve its convex trace theorem while retiring the
  impossible zero-slack corollary.
- No RH claim is made.
