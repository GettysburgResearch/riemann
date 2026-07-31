# L-15625 — Spectral-deficit normal form isolates the exact extra-low spectrum

Claim ID: `L-15625`  
Title: Choosing the exact spectral positive deficit turns the four-defect gate into one low-spectral tail plus explicit squared-residual charges  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF; COMPUTATION REQUIRES THE UNKNOWN LOW SPECTRUM`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: spectral functional calculus; `L-15621`; `L-15624`  
Scope: canonical normal form for the remaining cofinal inequality  
Related counterexample candidates: none

## 1. Exact spectral lower model

Let `A` be lower-bounded self-adjoint and choose

\[
 0<t<\Gamma<G.                                           \tag{L-15625.1}
\]

Assume the spectral part of `A` below `G` is trace class; compact resolvent is
more than sufficient. Define

\[
 \boxed{D_G^{\rm sp}=(GI-A)_+,}                          \tag{L-15625.2}
\]

\[
 \boxed{\mathcal R_G^{\rm sp}=(A-GI)_+.}                 \tag{L-15625.3}
\]

Then spectral functional calculus gives the exact decomposition

\[
 \boxed{
 A=GI-D_G^{\rm sp}+\mathcal R_G^{\rm sp}.}               \tag{L-15625.4}
\]

The positive and negative spectral pieces are orthogonal:

\[
 D_G^{\rm sp}\mathcal R_G^{\rm sp}=0.                   \tag{L-15625.5}
\]

Thus this lower model has no symbol-to-operator or assembly slack.

## 2. Exact clipping identities

Put

\[
 \theta=G-\Gamma.                                        \tag{L-15625.6}
\]

For every real scalar `x`,

\[
 \bigl((G-x)_+-(G-\Gamma)\bigr)_+
 = (\Gamma-x)_+.                                         \tag{L-15625.7}
\]

Therefore

\[
 \boxed{
 (D_G^{\rm sp}-\theta I)_+
 =(\Gamma I-A)_+.}                                      \tag{L-15625.8}
\]

The packet-clipping operator is

\[
 \boxed{
 (\theta I-D_G^{\rm sp})_+
 =\min\{(A-\Gamma I)_+,\theta I\}}                       \tag{L-15625.9}
\]

in scalar functional calculus.

Hence the first defect in `L-15621` is precisely

\[
 \boxed{
 \operatorname{Tr}
 Q(\Gamma I-A)_+Q,}                                      \tag{L-15625.10}
\]

the true low-spectral mass below `Gamma` that remains outside the packet.

## 3. Squared-residual control of the other two analytic defects

Let `P` be a rank-`d` packet and suppose

\[
 -\alpha P\preceq PAP\preceq\alpha P,
 \qquad
 PA^2P\preceq\rho^2P.                                   \tag{L-15625.11}
\]

The scalar inequalities

\[
 (x-G)_+\le{x^2\over4G},                                 \tag{L-15625.12}
\]

and

\[
 \min\{(x-\Gamma)_+,G-\Gamma\}
 \le{x^2\over4\Gamma}                                   \tag{L-15625.13}
\]

hold for every real `x`. Functional calculus gives

\[
 \boxed{
 \operatorname{Tr}P\mathcal R_G^{\rm sp}P
 \le {d\rho^2\over4G},}                                 \tag{L-15625.14}
\]

and

\[
 \boxed{
 \operatorname{Tr}P(\theta I-D_G^{\rm sp})_+P
 \le {d\rho^2\over4\Gamma}.}                            \tag{L-15625.15}
\]

Moreover,

\[
 \operatorname{Tr}P(\alpha I-A)P\le2d\alpha.            \tag{L-15625.16}
\]

Therefore the complete four-defect sum is bounded by

\[
 \boxed{
 \operatorname{Tr}Q(\Gamma I-A)_+Q
 +2d\alpha
 +{d\rho^2\over4}
  \left({1\over G}+{1\over\Gamma}\right).}              \tag{L-15625.17}
\]

If the packet residual is represented by

\[
 PAQAP\preceq\beta^2P,                                   \tag{L-15625.18}
\]

then

\[
 PA^2P=(PAP)^2+PAQAP
 \preceq(\alpha^2+\beta^2)P,                             \tag{L-15625.19}
\]

so one may take

\[
 \rho^2=\alpha^2+\beta^2.                                \tag{L-15625.20}
\]

## 4. Reduced cofinal condition

The exact sufficient condition becomes

\[
 \boxed{
 \begin{aligned}
 &\operatorname{Tr}Q_j(\Gamma_jI-A_j)_+Q_j\\
 &+2d_j\alpha_j
 +{d_j(\alpha_j^2+\beta_j^2)\over4}
  \left({1\over G_j}+{1\over\Gamma_j}\right)
 <\Gamma_j-t_j.
 \end{aligned}}                                          \tag{L-15625.21}
\]

For packets satisfying the Gevrey/disjoint-bump rates, the last two lines may
be made `o(1)` after choosing the threshold schedule with adequate moat. The
sole non-source term is the exact extra-low spectral trace

\[
 \boxed{
 \operatorname{Tr}Q_j(\Gamma_jI-A_j)_+Q_j.}              \tag{L-15625.22}
\]

## 5. Spectral packet specialization

If `P` reduces `A`, contains every eigenspace below `Gamma`, and its spectrum is
contained in `[-alpha,alpha]`, then

\[
 Q(\Gamma I-A)_+Q=0,
 \qquad
 PAQ=0.                                                   \tag{L-15625.23}
\]

The four-defect condition reduces to

\[
 2d\alpha+{d\alpha^2\over4}
 \left({1\over G}+{1\over\Gamma}\right)<\Gamma-t.        \tag{L-15625.24}
\]

In the exact invariant case the sharper direct calculation makes both
functional-calculus charges vanish whenever the packet eigenvalues lie below
`Gamma`; then only `2d alpha` remains from the deliberately coarse replacement
of the actual compression slack.

Conversely, one additional eigenvalue below `t` contributes more than

\[
 \Gamma-t
\]

to the clipped-excess quantum of `L-15622`. Thus the first term in
(L-15625.21) is exactly where an off-line Xi-cardinal negative direction enters.

## 6. Interaction with exact local Möbius extension

`L-20301` proves that every finite compactly supported localized spectral vector
is the restriction of an exact global arithmetic-radical vector. Consequently
source existence and finite-dimensional provenance are not obstacles to using
a spectral packet in this normal form.

However, the extension tail has the invariant zero signature

\[
 \widehat t(z_\rho)=-\widehat h(z_\rho),
\]

and its Weil matrix equals that of the target. Therefore local Möbius inversion
does not prove that the spectral trace (L-15625.22) vanishes; under false RH it
reproduces the same off-line negative coordinate in the lower tail.

## 7. Meaning of the normal form

The scalar Fourier-symbol condition in the original target mixes four effects:

1. actual extra low spectrum;
2. slack of the lower-symbol majorant;
3. packet leakage across the clipping threshold;
4. finite packet compression error.

The exact spectral model separates them. Three are controlled by squared
packet residuals; the first becomes the literal low-spectral tail. Therefore no
further phase-blind symbol or packet-tail estimate can prove the missing term
without excluding the extra low direction itself.

## 8. Proof boundary

- All functional-calculus identities and inequalities are exact.
- The spectral deficit is finite rank or trace class under the declared compact
  low-spectrum hypothesis.
- It is generally not available from a finite scalar-symbol certificate without
  resolving the low spectrum.
- The theorem proves a canonical reduction, not the vanishing of
  `Tr Q(Gamma-A)_+Q`.
- Cofinal vanishing of that term is the no-extra-low-mode theorem and, under the
  complete cardinal hierarchy, is equivalent to RH.
- No proof of RH is claimed.
