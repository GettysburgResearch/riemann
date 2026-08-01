# L-15621 — Clipped-excess rigidity and robust saturation

Claim ID: `L-15621`  
Title: The clipped trace excess is a sum of four positive defects, and only a threshold-gap bound is needed  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF`  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-07-31  
Dependencies: `L-15618`; min--max; functional calculus; trace cyclicity  
Scope: corrected completion gate after `R-15603`  
Related counterexample candidates: none

## 1. Setting

Let `A` be lower-bounded self-adjoint on a Hilbert space and let `D>=0` be
trace class. Assume

\[
 \boxed{A\succeq GI-D.}                                  \tag{L-15621.1}
\]

Let `L` be a nonzero `d`-dimensional subspace, with orthogonal projection `P`,
and put `Q=I-P`. Suppose

\[
 \boxed{PAP\preceq\alpha P,}\qquad \alpha<G.             \tag{L-15621.2}
\]

Write

\[
 \kappa=G-\alpha,                                        \tag{L-15621.3}
\]

choose

\[
 0\le\theta<\kappa,                                      \tag{L-15621.4}
\]

and define

\[
 E_\theta=(D-\theta I)_+,
 \qquad
 c=\kappa-\theta>0,
 \qquad
 \Gamma=G-\theta.                                       \tag{L-15621.5}
\]

The **clipped excess** is

\[
 \boxed{
 \mathfrak e
 =\operatorname{Tr}E_\theta-dc.}                        \tag{L-15621.6}
\]

`L-15618` proves `mathfrak e>=0`.  The point of this lemma is to identify
`mathfrak e` exactly, show that zero excess is a rigid flat-band equality case,
and replace the impossible zero-slack target by the robust condition

\[
 \mathfrak e<\Gamma-t.                                   \tag{L-15621.7}
\]

## 2. Exact four-defect decomposition

Put

\[
 \mathcal R=A+D-GI\succeq0.                              \tag{L-15621.8}
\]

Then

\[
 \boxed{
 \begin{aligned}
 \mathfrak e={}&
 \operatorname{Tr}(QE_\theta Q)\\
 &+\operatorname{Tr}\bigl(P(\alpha I-A)P\bigr)\\
 &+\operatorname{Tr}(P\mathcal RP)\\
 &+\operatorname{Tr}\bigl(P(\theta I-D)_+P\bigr).
 \end{aligned}}                                          \tag{L-15621.9}
\]

Every term on the right is nonnegative.

### Proof

Functional calculus gives the scalar identity

\[
 (x-\theta)_+-c
 =x-\kappa+(\theta-x)_+.
\]

Therefore

\[
 E_\theta-cI
 =D-\kappa I+(\theta I-D)_+.                             \tag{L-15621.10}
\]

Moreover

\[
 D-\kappa I
 =D-GI+\alpha I
 =(A+D-GI)+(\alpha I-A)
 =\mathcal R+(\alpha I-A).                               \tag{L-15621.11}
\]

Taking the trace in an orthonormal basis adapted to
`L direct-sum L^perp` yields

\[
\begin{aligned}
 \operatorname{Tr}E_\theta-dc
 ={}&\operatorname{Tr}(QE_\theta Q)
   +\operatorname{Tr}\bigl(P(E_\theta-cI)P\bigr),
\end{aligned}
\]

and insertion of (L-15621.10)--(L-15621.11) proves
(L-15621.9). Positivity follows from (L-15621.1)--(L-15621.2) and functional
calculus. QED.

### Interpretation

The four terms are logically distinct:

1. `Tr(Q E_theta Q)` is dangerous clipped mass not captured by the packet;
2. `Tr(P(alpha I-A)P)` is finite packet compression slack;
3. `Tr(P R P)` is slack in the chosen lower-symbol/operator majorant;
4. `Tr(P(theta I-D)_+P)` is packet leakage into the shallow side of the
   clipping threshold.

Thus the total clipped trace is not one opaque arithmetic scalar. It is an exact
sum of four positive defects, three of which are source/majorant quality gates.

## 3. Robust complement floor

Since

\[
 D\preceq\theta I+E_\theta,                              \tag{L-15621.12}
\]

for every `q in L^perp`,

\[
 \langle Aq,q\rangle
 \ge\Gamma\|q\|^2-\langle E_\theta q,q\rangle.
\]

A positive operator norm is at most its trace, so

\[
 \boxed{
 A|_{L^\perp}
 \succeq
 \left[
 \Gamma-\operatorname{Tr}(QE_\theta Q)
 \right]I
 \succeq(\Gamma-\mathfrak e)I.}                         \tag{L-15621.13}
\]

Consequently, if

\[
 \boxed{
 \mathfrak e<\Gamma-t}                                   \tag{L-15621.14}
\]

and

\[
 A|_L\prec tI,                                           \tag{L-15621.15}
\]

then

\[
 \boxed{
 A|_{L^\perp}\succ tI,
 \qquad
 N_A(t)=d.}                                              \tag{L-15621.16}
\]

If a second level `Gamma_tilde<=Gamma-mathfrak e` is desired, then

\[
 N_A(t)=N_A(\widetilde\Gamma)=d.                         \tag{L-15621.17}
\]

This is the exact count saturation needed by the inverse-Ritz layer.  The former
zero-slack condition `mathfrak e<=0` is unnecessary.

## 4. One-extra-mode exclusion

Let

\[
 \nu_1(D)\ge\nu_2(D)\ge\cdots\ge0                       \tag{L-15621.18}
\]

be the eigenvalues of `D`, with multiplicity. Compression of
(L-15621.1)--(L-15621.2) gives

\[
 PDP\succeq\kappa P.                                     \tag{L-15621.19}
\]

Min--max therefore gives

\[
 \nu_d(D)\ge\kappa.                                      \tag{L-15621.20}
\]

For `eta>0`, put

\[
 p_\eta=N_D(\theta+\eta)
 =\#\{n:\nu_n(D)>\theta+\eta\}.                         \tag{L-15621.21}
\]

If `p_eta>d`, the first `d` clipped eigenvalues contribute at least `dc`, and
each additional eigenvalue contributes more than `eta`. Hence

\[
 \boxed{
 (p_\eta-d)_+\,\eta<\mathfrak e
 \quad\text{whenever }p_\eta>d.}                         \tag{L-15621.22}
\]

In particular,

\[
 \boxed{
 \mathfrak e<\eta
 \quad\Longrightarrow\quad
 N_D(\theta+\eta)\le d.}                                 \tag{L-15621.23}
\]

On the orthogonal complement of the corresponding `D`-spectral packet,

\[
 A\succeq(G-\theta-\eta)I=(\Gamma-\eta)I.                \tag{L-15621.24}
\]

Thus if

\[
 \mathfrak e<\eta<\Gamma-t,                              \tag{L-15621.25}
\]

min--max gives the same exact count saturation without requiring the trial
packet to align with the `D`-eigenspace.

Equation (L-15621.22) is an integer amplification: once the positive excess is
smaller than one threshold quantum, even one additional dangerous mode is
impossible.

## 5. Zero excess is flat-band rigidity

The following are equivalent:

1. `mathfrak e=0`;
2. every term in (L-15621.9) vanishes;
3. the clipped deficit is exactly
   \[
   \boxed{E_\theta=cP;}                                  \tag{L-15621.26}
   \]
4. `P` reduces `D`,
   \[
   DP=\kappa P,
   \qquad
   D|_{L^\perp}\preceq\theta I,                         \tag{L-15621.27}
   \]
   and both the packet-compression and lower-majorant inequalities are equalities
   on `L`.

### Proof

Because

\[
 E_\theta\succeq D-\theta I,
\]

(L-15621.19) gives

\[
 PE_\theta P\succeq cP.                                 \tag{L-15621.28}
\]

If `mathfrak e=0`, then

\[
 \operatorname{Tr}E_\theta=dc.
\]

The positive operators `QE_theta Q` and `PE_theta P-cP` therefore have zero
trace and vanish. Positivity of `E_theta` also forces the off-diagonal blocks to
vanish. Hence `E_theta=cP`. Functional calculus then gives
(L-15621.27). The converse is immediate. The equivalence with the four zero
defects follows from (L-15621.9). QED.

Therefore the original clipped inequality

\[
 \operatorname{Tr}E_\theta\le dc                         \tag{L-15621.29}
\]

is not a generic asymptotic estimate. Under the low-packet hypotheses it demands
an exact flat dangerous band and exact spectral capture at every finite level.
This explains why it is much stronger than the complement floor it was meant to
certify.

## 6. Squared-residual control of packet clipping leakage

The fourth defect in (L-15621.9) has the general bound

\[
 \boxed{
 P(\theta I-D)_+P
 \preceq
 {1\over\kappa-\theta}
 P(D-\kappa I)^2P.}                                      \tag{L-15621.30}
\]

Indeed, for every scalar `x`,

\[
 (\theta-x)_+
 \le{(x-\kappa)^2\over\kappa-\theta}.                   \tag{L-15621.31}
\]

Thus a squared `D`-residual of the low packet controls spectral leakage below
the clipping threshold. This is the clipped-deficit analogue of the squared
Temple--Schur residual used elsewhere in the positive stack.

## 7. Cofinal RH criterion

At level `j`, define

\[
\begin{aligned}
 \mathfrak e_j={}&
 \operatorname{Tr}
 \left(D_j-(G_j-\Gamma_j)I\right)_+\\
 &-d_j(\Gamma_j-\alpha_j).
\end{aligned}                                            \tag{L-15621.32}
\]

Assume the near-radical packet and residual hypotheses of `T-15602`, and suppose

\[
 \boxed{
 0\le\mathfrak e_j<\Gamma_j-t_j
 \quad\text{eventually}.}                                \tag{L-15621.33}
\]

Then

\[
 A_j|_{L_j^\perp}
 \succeq(\Gamma_j-\mathfrak e_j)I
 \succ t_jI.                                             \tag{L-15621.34}
\]

The low index is exactly saturated. `T-15602` gives

\[
 \inf\sigma(A_j)
 \ge-
 {3t_j\alpha_j+\alpha_j^2+\beta_j^2\over t_j-\alpha_j}
 -\delta_j\longrightarrow0.                              \tag{L-15621.35}
\]

The cofinal localized-Weil lower-envelope theorem then implies RH.

The corrected arithmetic target is therefore **positive clipped excess smaller
than the available spectral gap**, not zero clipped excess.

## 8. Immediate source-side simplification

If the packet compression has the two-sided bound

\[
 -\alpha P\preceq PAP\preceq\alpha P,                   \tag{L-15621.36}
\]

then

\[
 0\le
 \operatorname{Tr}\bigl(P(\alpha I-A)P\bigr)
 \le2d\alpha.                                            \tag{L-15621.37}
\]

For the Gevrey/disjoint-bump packets of `L-15617/L-15619`, `d` grows at most
near-quadratically while `alpha` is smaller than every inverse power. Hence this
second defect is already `o(1)` after choosing the Schwartz/Gevrey order large
enough.

The remaining proof-facing defects are therefore:

\[
 \boxed{
 \operatorname{Tr}(QE_\theta Q),
 \qquad
 \operatorname{Tr}(P\mathcal RP),
 \qquad
 \operatorname{Tr}\bigl(P(\theta I-D)_+P\bigr).}         \tag{L-15621.38}
\]

They respectively encode complete dangerous-index capture, sharpness of the
chosen lower symbol/operator majorant on the packet, and the squared packet
residual relative to the clipping gap.

## 9. Proof boundary

- The decomposition, rigidity theorem, complement floor, and integer exclusion
  are exact.
- The old zero-excess condition is retired as an equality-case certificate.
- The theorem materially weakens the cofinal target to (L-15621.33), but does
  not prove the three remaining zeta-specific defects in (L-15621.38) are small.
- A finite numerical clipped trace does not prove the cofinal condition.
- No proof of RH is claimed without a cofinal bound for the positive excess.
