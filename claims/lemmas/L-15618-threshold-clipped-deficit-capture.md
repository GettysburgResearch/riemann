# L-15618 — Threshold-clipped deficit capture

Claim ID: `L-15618`  
Title: Only deficit above the desired complement threshold must be captured  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: `L-15612`; scalar Jensen inequality; trace cyclicity; functional calculus  
Scope: sharp scalar saturation gate for Issue #156  
Related counterexample candidates: none

## 1. Motivation

The sufficient condition

\[
 \operatorname{Tr}D-d(G-\alpha)\le G-\Gamma
 \tag{L-15618.1}
\]

charges every eigenvalue of the positive deficit operator `D`, including
arbitrarily many shallow eigenvalues below `G-Gamma`. Such eigenvalues cannot
individually lower the complement below `Gamma`.

The correct scalar object is therefore the deficit clipped at the exact danger
threshold.

## 2. Abstract theorem

Let `A` be lower-bounded self-adjoint on a Hilbert space and let `D>=0` be
trace class. Assume

\[
 \boxed{A\succeq GI-D.}
 \tag{L-15618.2}
\]

Let `L` be a `d`-dimensional subspace with orthogonal projection `P`, put
`Q=I-P`, and suppose

\[
 \boxed{A|_L\preceq\alpha I_L,}
 \qquad \alpha<G.
 \tag{L-15618.3}
\]

Write

\[
 \kappa=G-\alpha.
 \tag{L-15618.4}
\]

For any threshold

\[
 0\le\theta<\kappa,
 \tag{L-15618.5}
\]

define the clipped positive operator

\[
 \boxed{D_\theta=(D-\theta I)_+.}
 \tag{L-15618.6}
\]

Then

\[
 \boxed{
 \operatorname{Tr}(PD_\theta P)
 \ge d(\kappa-\theta),}
 \tag{L-15618.7}
\]

\[
 \boxed{
 \operatorname{Tr}(QD_\theta Q)
 \le
 \operatorname{Tr}D_\theta-d(\kappa-\theta),}
 \tag{L-15618.8}
\]

and

\[
 \boxed{
 A|_{L^\perp}
 \succeq
 \left[
 G-\theta
 -\operatorname{Tr}D_\theta
 +d(\kappa-\theta)
 \right]I.}
 \tag{L-15618.9}
\]

Consequently, if

\[
 \boxed{
 \operatorname{Tr}(D-\theta I)_+
 -d(G-\alpha-\theta)
 \le G-\theta-\Gamma,}
 \tag{L-15618.10}
\]

then

\[
 \boxed{A|_{L^\perp}\succeq\Gamma I.}
 \tag{L-15618.11}
\]

### Proof

Compressing (L-15618.2) to `L` and using (L-15618.3) gives

\[
 PDP|_L\succeq\kappa I_L.
 \tag{L-15618.12}
\]

Let `e_1,...,e_d` be an orthonormal basis of `L`. The scalar function

\[
 f_\theta(x)=(x-\theta)_+
\]

is convex. Applied to the spectral probability measure of `D` associated to
`e_j`, scalar Jensen gives

\[
 \langle D_\theta e_j,e_j\rangle
 \ge
 (\langle De_j,e_j\rangle-\theta)_+
 \ge\kappa-\theta.
 \tag{L-15618.13}
\]

Summing proves (L-15618.7). Trace cyclicity gives

\[
 \operatorname{Tr}(QD_\theta Q)
 =\operatorname{Tr}D_\theta-\operatorname{Tr}(PD_\theta P),
\]

which proves (L-15618.8).

Functional calculus gives the operator inequality

\[
 D\preceq\theta I+D_\theta.
 \tag{L-15618.14}
\]

Therefore, on `L^perp`,

\[
 A\succeq(G-\theta)I-QD_\theta Q.
 \tag{L-15618.15}
\]

The positive operator norm is bounded by its trace:

\[
 \|QD_\theta Q\|
 \le\operatorname{Tr}(QD_\theta Q).
\]

Inserting (L-15618.8) proves (L-15618.9), and (L-15618.10) proves
(L-15618.11). QED.

## 3. Exact danger-threshold form

Set

\[
 \theta=G-\Gamma.
 \tag{L-15618.16}
\]

The admissibility condition `theta<kappa` is exactly `Gamma>alpha`. Equation
(L-15618.10) becomes

\[
 \boxed{
 \operatorname{Tr}\bigl(D-(G-\Gamma)I\bigr)_+
 \le d(\Gamma-\alpha).}
 \tag{L-15618.17}
\]

This proves

\[
 \boxed{A|_{L^\perp}\succeq\Gamma I.}
 \tag{L-15618.18}
\]

Only eigenvalue mass of `D` above the amount `G-Gamma` capable of crossing the
floor is charged. Every shallower deficit direction is discarded exactly.

Moreover, (L-15618.7) and (L-15618.17) force equality:

\[
 \operatorname{Tr}(PD_\theta P)=d(\Gamma-\alpha),
 \qquad
 QD_\theta Q=0.
 \tag{L-15618.19}
\]

Thus the low packet captures the complete dangerous spectral part of `D`.

## 4. Layer-cake and threshold-index form

For positive trace-class `D`,

\[
 \boxed{
 \operatorname{Tr}(D-\theta I)_+
 =\int_\theta^\infty N_D(u)\,du,}
 \tag{L-15618.20}
\]

where

\[
 N_D(u)=\#\{n:\lambda_n(D)>u\}
\]

counts eigenvalues with multiplicity. Hence (L-15618.17) is an integrated
threshold-index condition:

\[
 \boxed{
 \int_{G-\Gamma}^\infty N_D(u)\,du
 \le d(\Gamma-\alpha).}
 \tag{L-15618.21}
\]

This is directly aligned with plunge-region and singular-value estimates.
Unlike the full trace, it does not charge the infinite shallow spectral tail.

## 5. Schatten corollary

For `r>1`, `theta>0`, scalar optimization gives

\[
 (x-\theta)_+
 \le
 \frac{(r-1)^{r-1}}{r^r\theta^{r-1}}x^r
 \qquad(x\ge0).
 \tag{L-15618.22}
\]

Therefore

\[
 \boxed{
 \operatorname{Tr}(D-\theta I)_+
 \le
 \frac{(r-1)^{r-1}}{r^r\theta^{r-1}}
 \operatorname{Tr}D^r.}
 \tag{L-15618.23}
\]

At `theta=G-Gamma`, the proof-facing sufficient condition

\[
 \boxed{
 \frac{(r-1)^{r-1}}
      {r^r(G-\Gamma)^{r-1}}
 \operatorname{Tr}D^r
 \le d(\Gamma-\alpha)}
 \tag{L-15618.24}
\]

implies exact saturation. This converts modern Schatten estimates into the
sharp clipped-trace gate without routing shallow modes through the `r=1` trace.

## 6. Symbol localization corollary

For

\[
 D=P_I\mathcal F^{-1}w\mathcal FP_I,
 \qquad w\ge0,
\]

Kato--Seiler--Simon gives

\[
 \operatorname{Tr}D^r
 \le\frac{|I|}{2\pi}\int_\mathbb Rw(\xi)^r\,d\xi.
 \tag{L-15618.25}
\]

Thus, on the scaled Suzuki interval `I=[-1,1]`, it is sufficient that

\[
 \boxed{
 \frac{(r-1)^{r-1}}
      {\pi r^r(G-\Gamma)^{r-1}}
 \int_\mathbb R(G-s(\xi))_+^r\,d\xi
 \le d(\Gamma-\alpha).}
 \tag{L-15618.26}
\]

This is weaker and better localized than the un-clipped ordinary-trace target.

## 7. Exact finite separation from the full-trace condition

Let

\[
 G=2,\qquad\alpha=0,\qquad\Gamma=1,
\]

and on `R^(N+2)` put

\[
 D=\operatorname{diag}(2,2,
 \underbrace{\varepsilon,\ldots,\varepsilon}_{N\text{ times}}),
 \qquad0<\varepsilon<1,
 \tag{L-15618.27}
\]

\[
 A=2I-D,
 \qquad
 L=\operatorname{span}\{e_1,e_2\}.
 \tag{L-15618.28}
\]

Then `A=GI-D`, `A|L=0`, and

\[
 A|_{L^\perp}=(2-\varepsilon)I\succeq\Gamma I.
 \tag{L-15618.29}
\]

The clipped condition is exact:

\[
 \operatorname{Tr}(D-I)_+=2=d(\Gamma-\alpha).
 \tag{L-15618.30}
\]

But the full-trace condition reads

\[
 \operatorname{Tr}D-d(G-\alpha)
 =N\varepsilon\le1.
 \tag{L-15618.31}
\]

It fails whenever `N epsilon>1`, despite the strict complement floor. Thus the
full-trace inequality is sufficient but not necessary and can be destroyed by
arbitrarily many harmless shallow modes.

## 8. Cofinal application

At level `j`, put

\[
 \theta_j=G_j-\Gamma_j.
\]

If

\[
 \boxed{
 \operatorname{Tr}(D_j-\theta_jI)_+
 \le d_j(\Gamma_j-\alpha_j),}
 \tag{L-15618.32}
\]

then `A_j|_(L_j^perp)>=Gamma_j`. Combining this with the uniform near-radical
rates of `L-15617` and the inverse-Ritz theorem `T-15602` gives a cofinal lower
floor tending to zero.

The remaining arithmetic statement is therefore a threshold-clipped
large-values/Schatten estimate, not the ordinary complete trace of every
shallow symbol deficit.

## 9. Proof boundary

- The abstract theorem, layer-cake identity, and finite separation are exact.
- The Suzuki specialization still requires a cofinal bound for the complete
  clipped deficit or one of its Schatten majorants.
- The theorem does not infer a source packet from dimension alone; the packet
  must satisfy the same-operator low-compression gate.
- No cofinal arithmetic clipped-deficit estimate is proved here.
- No proof of RH is claimed.
