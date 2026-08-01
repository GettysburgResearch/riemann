# Arithmetic-deficit and repaired-frame audit

Agent: `gpt56-08`  
Date: 2026-07-31  
Branch: `agent/gpt56-pro-09-d/156-capacity-saturation`  
Status: exact new reductions and one constructive source-packet theorem; **no proof of RH**

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

`L-15612` proves the finite implication

```text
low compression for the same operator
=> automatic weighted-deficit trace capture.
```

This continuation audits and advances both missing asymptotic inputs.

## 1. General normalization gate

Exact source repair and source-tail concentration do not automatically produce a
normalized localized packet. `L-15613` identifies the global arithmetic Gram:

\[
 \|E(f)\|^2
 =\frac1{2\pi}\int
 |\zeta(1/2+it)|^2|\Phi_f(t)|^2dt.
\]

For a general growing repaired packet, let `g_a` be the smallest generalized
Gram singular value and `epsilon_a` the joint exterior-tail norm. The normalized
tail map is bounded by

\[
 \frac{\epsilon_a}{\sqrt{g_a^2-\epsilon_a^2}}.
\]

Thus a generic Hermite/prolate construction needs a weighted Mellin frame bound.
The multiplier vanishes at every critical-line zero, so rank and ordinary
concentration alone do not provide one. This is the Gram-side form of the
certified-zero evaluation obstruction in PR #159.

## 2. Constructive uniformly controlled repaired packet

`L-15616` bypasses the Mellin small-denominator problem with an explicit packet.

Choose one smooth compact zero-mean atom and place disjoint scaled copies in cells
of width

\[
 \ell_\lambda=\lambda^{\delta-1}
\]

inside `(5 lambda/8,7 lambda/8)`, together with their even reflections. Every
source is smooth, even, supported away from zero, and satisfies exactly

\[
 f(0)=0,
 \qquad
 \int f=0.
\]

The packet has rank

\[
 d_\lambda\gg_\delta\lambda^{2-\delta}.
\]

For `u` in the positive source interval, all arithmetic summands with `n>=2`
vanish, so

\[
 E(f)(u)=\sqrt u\,f(u).
\]

Therefore the complete arithmetic Gram has the exact dimension-free floor

\[
 E^*E\succeq\frac12I.
\]

The upper localized tail is identically zero. Poisson summation and Schwartz
decay give, uniformly over the entire packet,

\[
 \|T_\lambda\|_{X_{\lambda,\tau}}
 \le C_{N,\tau}
 \lambda^{1+\tau-\delta N}
\]

for every integer `N`. Hence every fixed finite polynomial graph/form norm is
smaller than every prescribed inverse power of `lambda` after increasing `N`.
The packet compression and residual inherit the same rapid decay whenever the
complete Weil-form continuity budget has polynomial support growth.

Thus the uniformly controlled repaired-source side of (1) is constructively
closed at rank `lambda^(2-delta)`. The packet lies in the exact radical
near-kernel and is not claimed to replace the evaluation-visible block.

## 3. Complete arithmetic deficit becomes a Dirichlet-polynomial large-value problem

`L-15614` writes the complete prime term at scaled frequency `xi=at` as

\[
 2\operatorname{Re}S_a(t),
 \qquad
 S_a(t)=\sum_{n\le e^{2a}}
 \frac{\Lambda(n)}{\sqrt n}n^{-it}.
\]

After exact logarithmic scaling cancellation,

\[
 (G-s_a^+(at))_+
 \le(C_{a,G}-\log|t|+2\operatorname{Re}S_a(t))_+.
\]

A Montgomery--Vaughan mean-square estimate gives a rigorous dyadic shell
bound. Combined with the elementary absolute coefficient cap, it gives a
complete finite trace enclosure, but only of size

\[
 \exp(O(ae^a)).
\]

This is far larger than the new source rank

\[
 d_\lambda\asymp e^{(2-\delta)a}.
\]

The prime number theorem, ordinary mean square, and plunge-count theorems do not
therefore establish (1). A proof needs a global large-deviation estimate for the
finite von-Mangoldt polynomial against the moving barrier `log|t|`, or a
phase-aware replacement.

## 4. The ordinary trace condition is unnecessarily coarse

`L-15615` proves automatic capture at every Schatten order. For `r>=1`,

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

Hence (1) may be replaced by

\[
 \operatorname{Tr}D^r-d(G-\alpha)^r
 \le(G-\Gamma)^r.
\]

For the symbol deficit, Kato--Seiler--Simon gives

\[
 \operatorname{Tr}D^r
 \le\frac{|I|}{2\pi}\int(G-s)_+^r.
\]

The exact `X-15604` model has one hundred harmless shallow deficit modes. Its
ordinary trace certificate fails, while the `r=2` certificate proves a stronger
complement floor. Thus failure of (1) need not indicate a genuine low mode.

## 5. Cross-audit against the endpoint/terminal-prime branch

Concurrent PR #177 decomposes the plunge-sized endpoint-visible matrix into:

```text
positive/dimension-uniform same-end local-Weyl block
+ finite local and prefix terms
+ centered opposite-endpoint terminal-prime Hankel matrix.
```

The prime pole and negative polar rank-one channel cancel exactly. The remaining
centered terminal matrix has translated Laplace transform

\[
 -\frac{\zeta'}\zeta(z+1/2)-\frac1{z-1/2},
\]

whose remaining poles are the shifted nontrivial zeros. For a fixed window whose
transform is zero-free in the open counterexample strip, a uniform bound for the
translated statistic already implies RH.

Therefore a phase-blind proof of the complete arithmetic deficit cannot be
obtained merely by inserting a PNT error or plunge count. `L-15614` is a correct
sufficient envelope, but taking absolute values before terminal/polar
cancellation discards the phase mechanism isolated in PR #177.

## 6. Strongest current proof interfaces

### A. Schatten scalar saturation

For the explicit packet of `L-15616`, prove for some `r_j>=1`

\[
 \frac1\pi\int(G_j-s_j)_+^{r_j}
 -d_j(G_j-\alpha_j)^{r_j}
 \le(G_j-\Gamma_j)^{r_j}.
\]

The packet rank and compression/residual rates are now available. The arithmetic
moment bound remains open.

### B. Phase-aware visible Schur margin

Use the certified-zero near-kernel/visible split and prove

\[
 \theta_a+\omega_a+\omega_a^2/h_a
 <\sigma_a^2,
\]

where `theta_a` is the centered terminal-prime Hankel norm and the same-end local
moat is dimension-uniform. This retains exact prime/polar cancellation and is
sharper than a global positive-part trace.

## 7. Recommended immediate computations

1. Evaluate the complete centered terminal matrix for the smallest phase-complete
   endpoint packet from PR #177, with and without certified-zero notches.
2. Evaluate `r=1,2,4` directed deficit moments on the same exact supports.
3. Instantiate the disjoint-bump packet at small support and verify its arithmetic
   Gram and tail through an independent Poisson implementation.
4. Compare the scalar Schatten floor with the phase-aware visible Schur floor on
   identical data.
5. Escalate only a quantity with a symbolic cofinal moat; finite trend fitting is
   not a proof.

## Current verdict

The finite theorem

```text
low compression => automatic weighted-deficit capture
```

is proved at every Schatten order. A uniformly normalized exact repaired packet
of rank `lambda^(2-delta)` with rapidly vanishing whole-packet tails is now also
constructed. The remaining unresolved theorem is the complete arithmetic
Schatten/terminal-prime bound. The newest exact decomposition shows why: the
phase-sensitive terminal statistic carries the shifted zeta-zero poles. Proving
its required uniform bound, or an equivalent scalar Schatten moat, is the
RH-resolving arithmetic step rather than a routine consequence of current
localization estimates.
