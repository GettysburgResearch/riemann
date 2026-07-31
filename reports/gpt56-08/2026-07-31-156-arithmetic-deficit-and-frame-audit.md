# Arithmetic-deficit and repaired-frame audit

Agent: `gpt56-08`  
Date: 2026-07-31  
Branch: `agent/gpt56-pro-09-d/156-capacity-saturation`  
Status: exact new reductions and scope corrections; **no proof of RH**

## Requested target

The requested continuation sought a cofinal proof of

\[
 \operatorname{Tr}D_j-d_j(G_j-\alpha_j)
 \le G_j-\Gamma_j,
 \tag{1}
\]

where

\[
 D_j=P_I\mathcal F^{-1}(G_j-s_j)_+\mathcal FP_I,
\]

and a uniformly controlled exact repaired radical packet of dimension `d_j`.

`L-15612` already proves the finite implication

```text
low compression for the same operator
=> automatic weighted-deficit trace capture.
```

The present continuation audits the two missing asymptotic inputs.

## 1. Uniform source repair needs an arithmetic frame floor

Exact source repair and source-tail concentration do not by themselves produce a
normalized localized packet.  `L-15613` identifies the global arithmetic Gram:

\[
 \|E(f)\|^2
 =\frac1{2\pi}\int
 |\zeta(1/2+it)|^2|\Phi_f(t)|^2dt.
\]

For a growing repaired packet, let `g_a` be the smallest generalized Gram
singular value and `epsilon_a` the joint exterior-tail norm.  The normalized
tail map is bounded by

\[
 \frac{\epsilon_a}{\sqrt{g_a^2-\epsilon_a^2}}.
\]

Thus the uniform repaired-packet theorem requires a weighted Mellin frame bound,
not only an ordinary Hermite/prolate concentration estimate.  The multiplier
vanishes at every critical-line zero, so a general growing packet can concentrate
near its zero set.  This is the Gram-side form of the certified-zero evaluation
obstruction in PR #159.

## 2. Complete arithmetic deficit becomes a Dirichlet-polynomial large-value problem

`L-15614` writes the complete prime term at scaled frequency `xi=at` as

\[
 2\operatorname{Re}S_a(t),
 \qquad
 S_a(t)=\sum_{n\le e^{2a}}
 \frac{\Lambda(n)}{\sqrt n}n^{-it}.
\]

After the exact logarithmic scaling cancellation,

\[
 (G-s_a^+(at))_+
 \le(C_{a,G}-\log|t|+2\operatorname{Re}S_a(t))_+.
\]

A Montgomery--Vaughan mean-square estimate gives a rigorous dyadic shell
bound.  Combined with the elementary absolute coefficient cap, it gives a
complete finite trace enclosure, but only of size

\[
 \exp(O(ae^a)).
\]

This is much larger than the natural one-dimensional phase-space packet.  The
prime number theorem, ordinary mean square, and plunge-count theorems therefore
do not establish (1).  A proof needs a global large-deviation estimate for the
finite von-Mangoldt polynomial against the moving barrier `log|t|`.

## 3. The ordinary trace condition is unnecessarily coarse

`L-15615` proves automatic capture at every Schatten order.  For `r>=1`,

\[
 A\succeq GI-D,
 \qquad
 A|_L\preceq\alpha I,
\]

imply

\[
 A|_{L^\perp}
 \succeq
 \left[
 G-\bigl(\operatorname{Tr}D^r-d(G-\alpha)^r\bigr)_+^{1/r}
 \right]I.
\]

Hence the scalar saturation condition may be replaced by

\[
 \operatorname{Tr}D^r-d(G-\alpha)^r
 \le(G-\Gamma)^r.
\]

For the symbol deficit, Kato--Seiler--Simon gives

\[
 \operatorname{Tr}D^r
 \le\frac{|I|}{2\pi}
 \int(G-s)_+^r.
\]

The exact `X-15604` control has one hundred harmless shallow deficit modes.  Its
ordinary trace certificate fails, while the `r=2` certificate proves a stronger
complement floor.  Thus failure of (1) need not indicate a genuine low mode.

## 4. Cross-audit against the newest endpoint/terminal-prime branch

Concurrent PR #177 decomposes the plunge-sized endpoint-visible matrix into:

```text
positive/dimension-uniform same-end local-Weyl block
+ finite local and prefix terms
+ centered opposite-endpoint terminal-prime Hankel matrix.
```

The prime pole and the negative polar rank-one channel cancel exactly.  The
remaining centered terminal matrix has translated Laplace transform

\[
 -\frac{\zeta'}\zeta(z+1/2)-\frac1{z-1/2},
\]

whose remaining poles are the shifted nontrivial zeros.  For a fixed window
whose transform is zero-free in the open counterexample strip, a uniform bound
for the translated statistic already implies RH.

Therefore a phase-blind proof of the complete arithmetic deficit cannot be
obtained merely by inserting a PNT error or a plunge count.  The phase-sensitive
terminal matrix is the arithmetic content.  `L-15614` is a correct sufficient
large-deviation envelope, but its weakness is structural: taking absolute values
before the terminal/polar cancellation discards the mechanism isolated in PR
#177.

## 5. Strongest current proof interfaces

There are now two honest final interfaces.

### A. Schatten scalar saturation

Find repaired packets with weighted frame/tail control and prove, for some
`r_j>=1`,

\[
 \frac1\pi\int(G_j-s_j)_+^{r_j}
 -d_j(G_j-\alpha_j)^{r_j}
 \le(G_j-\Gamma_j)^{r_j}.
\]

This bypasses all packet-angle limits, but the arithmetic moment bound remains
open.

### B. Phase-aware visible Schur margin

Use the certified-zero near-kernel/visible split and prove

\[
 \theta_a+\omega_a+\omega_a^2/h_a
 <\sigma_a^2,
\]

where `theta_a` is the centered terminal-prime Hankel norm and the same-end local
moat is dimension-uniform.  This retains the exact prime/polar cancellation and
is sharper than a global positive-part symbol trace.

## 6. Recommended immediate computations

1. Evaluate the complete centered terminal matrix for the smallest phase-complete
   endpoint packet from PR #177, with and without certified-zero notches.
2. At the same supports, evaluate `r=1,2,4` directed deficit moments rather than
   the raw trace alone.
3. Construct directed arithmetic Mellin Grams for small repaired Hermite packets
   and report `epsilon_a/g_a`, not unnormalized source tails.
4. Compare the scalar Schatten floor with the phase-aware visible Schur floor on
   identical exact data.
5. Escalate only a quantity with a symbolic cofinal moat; finite trend fitting is
   not a proof.

## Current verdict

The finite theorem

```text
low compression => automatic weighted-deficit capture
```

is proved, and it now holds at every Schatten order.  No proof-grade cofinal
arithmetic moment bound or weighted Mellin frame theorem is currently available.
The newest exact decomposition shows why: the final phase-sensitive terminal
prime statistic carries the shifted zeta-zero poles.  Proving its required
uniform bound, or an equivalent scalar Schatten moat, is the RH-resolving
arithmetic step rather than a routine consequence of current localization
estimates.
