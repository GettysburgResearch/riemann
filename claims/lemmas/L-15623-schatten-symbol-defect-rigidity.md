# L-15623 — Schatten symbol-defect rigidity and the extra-low-mode quantum

Claim ID: `L-15623`  
Title: The proposed Schatten symbol inequality is a sum of three positive defects, and one additional low direction forces its strict failure  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF; ZETA-SPECIFIC POSITIVE ESTIMATE OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15615`, `L-15621`, `L-15622`; min--max; Kato--Seiler--Simon/Berezin--Lieb upper moment bound  
Scope: exact logical content of the proposed cofinal symbol/Schatten condition  
Related counterexample candidates: none

## 1. Setting

Let `A` be a lower-bounded self-adjoint operator on a Hilbert space. Let
`D>=0` belong to `S_r` for some real `r>=1`, and suppose

\[
 \boxed{A\succeq GI-D.}                                      \tag{L-15623.1}
\]

Let `L` be a `d`-dimensional subspace with orthogonal projection `P`, put
`Q=I-P`, and assume

\[
 \boxed{PAP\preceq\alpha P,}\qquad \alpha<G.                 \tag{L-15623.2}
\]

Set

\[
 \kappa=G-\alpha>0.                                           \tag{L-15623.3}
\]

Let `mathcal I_r` be any proof-grade scalar upper bound for the complete
Schatten moment:

\[
 \boxed{\operatorname{Tr}D^r\le\mathcal I_r.}                 \tag{L-15623.4}
\]

For a Fourier localization deficit

\[
 D=P_I\mathcal F^{-1}w\mathcal FP_I,
 \qquad w=(G-s)_+,
\]

one may take

\[
 \mathcal I_r={|I|\over2\pi}\int_{\mathbb R}w(\xi)^r\,d\xi.  \tag{L-15623.5}
\]

On the scaled interval `I=[-1,1]`, this is the scalar appearing in the
question:

\[
 \mathcal I_r={1\over\pi}\int_{\mathbb R}(G-s(\xi))_+^r\,d\xi.
 \tag{L-15623.6}
\]

## 2. Exact three-defect decomposition

Define the symbol moment excess

\[
 \mathcal E_r=\mathcal I_r-d\kappa^r.                         \tag{L-15623.7}
\]

Then exactly

\[
 \boxed{
 \begin{aligned}
 \mathcal E_r={}&
 \underbrace{\bigl(\mathcal I_r-\operatorname{Tr}D^r\bigr)}_
 {\text{symbol-to-operator Schatten slack}}\\
 &+\underbrace{\bigl(\operatorname{Tr}(PD^rP)-d\kappa^r\bigr)}_
 {\text{packet flat-band/Jensen slack}}\\
 &+\underbrace{\operatorname{Tr}(QD^rQ)}_
 {\text{uncaptured Schatten tail}}.
 \end{aligned}}                                             \tag{L-15623.8}
\]

Every term on the right is nonnegative.

### Proof

Compression of (L-15623.1) and (L-15623.2) gives

\[
 PDP\succeq\kappa P.                                         \tag{L-15623.9}
\]

For an orthonormal basis `e_1,...,e_d` of `L`, scalar Jensen applied to the
spectral measure of `D` gives

\[
 \langle D^re_j,e_j\rangle
 \ge\langle De_j,e_j\rangle^r
 \ge\kappa^r.
\]

Hence

\[
 \operatorname{Tr}(PD^rP)-d\kappa^r\ge0.                    \tag{L-15623.10}
\]

The first term is nonnegative by (L-15623.4), and the third because `D^r>=0`.
Finally,

\[
 \operatorname{Tr}D^r
 =\operatorname{Tr}(PD^rP)+\operatorname{Tr}(QD^rQ),
\]

which proves (L-15623.8). QED.

### Special role of `r=1`

For the exact Fourier localization operator,

\[
 \operatorname{Tr}D={|I|\over2\pi}\int w,
\]

so the first defect in (L-15623.8) vanishes identically when `r=1`. For
`r>1`, the Kato--Seiler--Simon/Berezin upper bound can have positive slack.
Thus increasing `r` suppresses shallow eigenvalues but introduces a separate
phase-space quantization defect that must also fit inside the same moat.

## 3. The proposed inequality closes the low count

Fix

\[
 t<\Gamma<G,
 \qquad
 \theta=G-\Gamma>0.                                        \tag{L-15623.11}
\]

If

\[
 \boxed{
 \mathcal E_r
 =\mathcal I_r-d(G-\alpha)^r
 \le(G-\Gamma)^r=\theta^r,}                                \tag{L-15623.12}
\]

then

\[
 \boxed{A|_{L^\perp}\succeq\Gamma I}                       \tag{L-15623.13}
\]

by `L-15615`. In particular, if

\[
 A|_L\prec tI,                                              \tag{L-15623.14}
\]

then

\[
 \boxed{N_A(t)=N_A(\Gamma)=d.}                              \tag{L-15623.15}
\]

No principal-angle or packet-alignment hypothesis is present.

A slightly weaker count-only proof follows directly from eigenvalues. If
`nu_1(D)>=nu_2(D)>=...`, then (L-15623.9) and min--max give

\[
 \nu_d(D)\ge\kappa.
\]

Equation (L-15623.12) forces

\[
 \sum_{n>d}\nu_n(D)^r\le\theta^r,
\]

and hence `nu_(d+1)(D)<=theta`. Therefore `A` has at most `d` eigenvalues below
`Gamma`; (L-15623.14) supplies at least `d` below `t`.

## 4. One additional low mode forces strict failure

Suppose there is a subspace `W` of dimension `d+q`, `q>=1`, on which

\[
 \boxed{A|_W\prec tI.}                                     \tag{L-15623.16}
\]

Then

\[
 \boxed{
 \mathcal E_r
 >q(G-t)^r.}                                               \tag{L-15623.17}
\]

Since `t<Gamma`, this implies

\[
 \boxed{
 \mathcal E_r>(G-\Gamma)^r,}                               \tag{L-15623.18}
\]

so the proposed inequality fails strictly.

### Proof

On `W`, (L-15623.1) and (L-15623.16) give

\[
 \langle Du,u\rangle>(G-t)\|u\|^2
 \qquad(0\ne u\in W).
\]

Min--max yields

\[
 \nu_{d+q}(D)>G-t.                                         \tag{L-15623.19}
\]

The first `d` eigenvalues contribute at least `d\kappa^r`; the next `q`
contribute strictly more than `q(G-t)^r`. Therefore

\[
 \operatorname{Tr}D^r-d\kappa^r>q(G-t)^r.
\]

Since `mathcal I_r>=Tr D^r`, (L-15623.17) follows. QED.

This is the Schatten-moment analogue of the clipped-excess quantum in
`L-15622`.

## 5. False RH produces the forbidden extra direction

Under the cardinal-localization interfaces of `T-14306/T-14307` and
`L-15622`, a nonreal centered zeta zero `rho` supplies the exact global
cardinal difference

\[
 h_\rho=\ell_\rho-\ell_{\bar\rho},
 \qquad
 Q_W(h_\rho,h_\rho)=-2m_\rho.                              \tag{L-15623.20}
\]

It is Weil-orthogonal to every exact global `E`-range radical. After fixing a
finite radical packet and localizing at sufficiently large support, its
negative block retains a fixed moat while every radical/cardinal cross term is
a vanishing tail term. Thus it supplies at least one additional direction
below `t_j` at all sufficiently large diagonal levels.

Consequently false RH forces

\[
 \boxed{
 {1\over\pi}\int(G_j-s_j)_+^{r_j}
 -d_j(G_j-\alpha_j)^{r_j}
 >(G_j-t_j)^{r_j}
 >(G_j-\Gamma_j)^{r_j}}                                    \tag{L-15623.21}
\]

for every proof stack satisfying the imported localization gates.

Therefore a cofinal proof of the displayed inequality is already an
RH-resolving theorem. It cannot follow from packet dimension, plunge estimates,
or fixed-mode tail decay alone; those inputs do not exclude the cardinal
extra-low direction.

## 6. Rigidity of zero excess

Let `mathcal I_r=Tr D^r`. If

\[
 \operatorname{Tr}D^r=d\kappa^r,                           \tag{L-15623.22}
\]

then `D` has exactly `d` nonzero eigenvalues, all equal to `kappa`, and

\[
 \boxed{D=\kappa P.}                                       \tag{L-15623.23}
\]

Indeed, the first `d` eigenvalues are at least `kappa`, while their complete
`r`-moment plus the tail equals `d kappa^r`; equality forces
`nu_1=...=nu_d=kappa` and `nu_(d+1)=0`.  Equation (L-15623.9) then forces `L`
to equal the nonzero spectral range of `D`.

For the symbol version, zero total excess additionally requires equality in
the Schatten phase-space bound. Thus the zero-slack target is a rigid flat-band
and exact-quantization equality case, not a generic asymptotic estimate.

## 7. Corrected proof target

The displayed inequality is valid as a sufficient RH criterion but is stronger
than necessary.  The exact robust clipped condition of `L-15621` is

\[
 \operatorname{Tr}
 \bigl(D_j-(G_j-\Gamma_j)I\bigr)_+
 -d_j(\Gamma_j-\alpha_j)
 <\Gamma_j-t_j.                                           \tag{L-15623.24}
\]

It ignores every shallow deficit eigenvalue below the danger threshold and has
no Kato--Seiler--Simon quantization slack. `L-15622` shows that false RH still
violates it by one full threshold quantum.

Alternatively, `L-18901` gives the canonical finite augmentation by the actual
high-deficit spectral packet. This always closes the infinite complement and
moves the remaining RH-bearing sign into a finite selected-zero-kernel block.

## 8. Proof boundary

- The three-defect identity, rigidity, saturation, and extra-mode quantum are
  exact operator theory.
- The Fourier symbol moment in (L-15623.6) is only an upper bound for
  `Tr D^r` when `r>1`; its slack is load-bearing.
- The false-RH implication imports the existing exact cardinal decomposition
  and fixed-finite-packet localization estimates.
- No positive zeta-specific estimate proving (L-15623.12) is supplied here.
- A claim that standard PNT, mean-square, or plunge bounds prove the displayed
  inequality would leave the extra-low cardinal direction unaddressed.
- No proof of RH is claimed.
