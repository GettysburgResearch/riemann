# L-91401 — Positive delays have an explicit model-space Julia colligation

Claim ID: `L-91401`  
Status: **PROVED EXACT COMPRESSED-DELAY/MODEL-SPACE COLLIGATION; ARITHMETIC DEFECT IDENTIFICATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91301`, `L-91316`, `R-91011`  
RH status: **unproved**

## 1. Purpose

`R-91011` correctly observes that a raw Hardy delay need not preserve Suzuki's
model space:

\[
 S_\tau K_\Theta\not\subseteq K_\Theta
\]

in general.  This does not destroy the delayed programme.  The correct object
is the canonical compression of the delay together with its orthogonal Julia
leakage into `Theta H^2`.

This lemma writes that colligation explicitly and retains every mixed-delay
cross term.

## 2. Hardy and model-space notation

Let

\[
 H=H^2(\mathbb C_+),
 \qquad
 M=M_\Theta:H\to H
\]

for an inner function `Theta`. Put

\[
 Q=MM^*,
 \qquad
 P=I-Q,
 \qquad
 K_\Theta=PH.
\tag{L-91401.1}
\]

For `tau>=0`, let

\[
 \boxed{
 S_\tau=M_{e^{i\tau z}}.
 }
\tag{L-91401.2}
\]

Then `S_tau` is an isometry on `H`,

\[
 S_{\tau+\sigma}=S_\tau S_\sigma,
\]

and it commutes with `M`.  Therefore `Theta H` is invariant under every
`S_tau`:

\[
 S_\tau QH\subseteq QH.
\tag{L-91401.3}
\]

The sign in (L-91401.2) is the upper-half-plane convention.  On the reflected
lower Hardy orientation one uses `e^{-i tau z}`.  These are the two standard
representatives of positive physical translation after the repository's
Fourier reflection.

## 3. Resident delay and Julia leakage

Define

\[
 \boxed{
 T_\tau=PS_\tau|_{K_\Theta}:
 K_\Theta\to K_\Theta,
 }
\tag{L-91401.4}
\]

and

\[
 \boxed{
 R_\tau=M^*S_\tau|_{K_\Theta}:
 K_\Theta\to H.
 }
\tag{L-91401.5}
\]

For every `g in K_Theta`, orthogonal projection gives

\[
\begin{aligned}
 S_\tau g
 &=PS_\tau g+QS_\tau g\\
 &=T_\tau g+MM^*S_\tau g.
\end{aligned}
\]

Hence

\[
 \boxed{
 S_\tau g=T_\tau g+MR_\tau g,
 \qquad
 T_\tau g\perp MR_\tau g.
 }
\tag{L-91401.6}
\]

This is the canonical model-space Julia decomposition of a raw delay.

In particular,

\[
 \boxed{
 T_\tau^*T_\tau+R_\tau^*R_\tau=I_{K_\Theta}.
 }
\tag{L-91401.7}
\]

Thus

\[
 \boxed{
 \mathfrak U_\tau g=
 \binom{T_\tau g}{R_\tau g}
 }
\tag{L-91401.8}
\]

is an explicit positive-metric isometry

\[
 K_\Theta\longrightarrow K_\Theta\oplus H.
\]

No invariance of `K_Theta` is assumed.

## 4. Fully polarized mixed-delay identity

For arbitrary delays `tau_i,tau_j>=0` and vectors `g_i,g_j in K_Theta`,
(L-91401.6) gives

\[
 \boxed{
 \langle S_{\tau_i}g_i,S_{\tau_j}g_j\rangle_H
 =\langle T_{\tau_i}g_i,T_{\tau_j}g_j\rangle_{K_\Theta}
 +\langle R_{\tau_i}g_i,R_{\tau_j}g_j\rangle_H.
 }
\tag{L-91401.9}

Equivalently, as an operator-valued kernel on the delay semigroup,

\[
 \boxed{
 P S_{\tau_i}^*S_{\tau_j}P
 =T_{\tau_i}^*T_{\tau_j}
  +R_{\tau_i}^*R_{\tau_j}
 }
\tag{L-91401.10}
\]

on `K_Theta`.

Therefore every finite carrier/delay polarization is preserved exactly once
the leakage coordinate is retained.  The correction to the old statement is
not a scalar loss; it is one explicit positive auxiliary Gram.

## 5. Semigroup and leakage cocycle

Since `QH` is invariant under `S_tau`,

\[
 PS_\tau Q=0,
 \qquad
 PS_\tau=PS_\tau P.
\tag{L-91401.11}
\]

Consequently

\[
 \boxed{
 T_{\tau+\sigma}=T_\tau T_\sigma.
 }
\tag{L-91401.12}
\]

The leakage obeys the exact cocycle

\[
\begin{aligned}
 R_{\tau+\sigma}
 &=M^*S_\tau(P+Q)S_\sigma P\\
 &=R_\tau T_\sigma+S_\tau R_\sigma,
\end{aligned}
\]

so

\[
 \boxed{
 R_{\tau+\sigma}
 =R_\tau T_\sigma+S_\tau R_\sigma.
 }
\tag{L-91401.13}
\]

Thus repeated physical delays are represented by a genuine conservative
cascade, not by unrelated projections at each delay.

## 6. Compatibility with Suzuki's tangent reserve

Let

\[
 \widetilde{\mathcal J}_a
 =\sqrt2\,M_{a\partial_a\Theta_a}^*P
\tag{L-91401.14}
\]

be the ambient form of the canonical tangent map, whose restriction to
`K_(Theta_a)` is `mathcal J_a` of `L-91301/L-91316`.

For `g in K_(Theta_a)`,

\[
 \boxed{
 \widetilde{\mathcal J}_aS_\tau g
 =\mathcal J_aT_\tau g.
 }
\tag{L-91401.15}
\]

The delayed tangent therefore depends on the raw delay only through its
resident model-space component.  The discarded component is not lost: it is
exactly `R_tau g` in the Julia reserve.

Combining with `L-91316`,

\[
 \boxed{
 \widetilde{\mathcal J}_aS_\tau
 =a\sqrt{2V_a}\,
  \mathcal C_a\mathcal A_aT_\tau
 }
\tag{L-91401.16}
\]

on `K_(Theta_a)`.  Hence every resident delayed packet has the same completed
Fisher score observation and the mixed-delay Gram is controlled before taking
norms.

## 7. Two Hardy orientations

Apply the preceding construction to `H^2(C_+)` with `S_tau^+` and to the
reflected `H^2(C_-)` with `S_tau^-`.  Their orthogonal direct sum gives

\[
 \boxed{
 \mathfrak U_\tau^{\rm two}
 =\mathfrak U_\tau^+\oplus\mathfrak U_\tau^-.
 }
\tag{L-91401.17}
\]

It preserves all same-orientation and opposite-orientation cross terms in the
ambient two-sided boundary space.  No raw-delay invariance of either model
space is required.

## 8. The finite bridge coordinate

The bridge inherited by `L-91034` has boundary decomposition

\[
 \widehat b_a=H_a^+-H_a^-,
 \qquad
 H_a^+=\Psi_a/u,
 \qquad
 H_a^-=\overline{\Psi_a}/u.
\tag{L-91401.18}
\]

Treat each Hardy component by the same orthogonal split:

\[
 H_a^\epsilon
 =P_a^\epsilon H_a^\epsilon
  +M_{\Theta_a^\epsilon}
   (M_{\Theta_a^\epsilon})^*H_a^\epsilon.
\tag{L-91401.19}
\]

Thus the bridge has explicit resident vectors

\[
 g_{a,\star}^\epsilon=P_a^\epsilon H_a^\epsilon
\]

and explicit leakage vectors

\[
 r_{a,\star}^\epsilon
 =(M_{\Theta_a^\epsilon})^*H_a^\epsilon.
\]

This closes the **geometric boundary placement** of the bridge.  It does not
identify its source norm with the arithmetic gamma/pole/prime first chaos, nor
does it prove its screw Gram positive.

## 9. What remains

The raw-delay obstruction of `R-91011` is now repaired exactly:

```text
raw delay
 -> compressed resident model-space delay T_tau
  + explicit Julia leakage R_tau.
```

The remaining theorem is source-specific.  One must prove that the arithmetic
Poisson/Jordan plus gamma/pole source dominates the joint Fisher--Hankel norm
of all resident delayed vectors and supplies the leakage/bridge reserves with
coefficient one.

Because of `R-91402`, this cannot be reduced to identifying the completed
Fisher probability law with a positive Poisson Levy law.

## 10. Exact boundary

```text
raw delay preserves K_Theta                         FALSE in general
compressed delay semigroup T_tau                    EXACT
Julia leakage R_tau                                 EXACT
same-delay isometry                                 EXACT
all mixed-delay cross terms                        EXACT
leakage cocycle                                    EXACT
two reflected Hardy orientations                   EXACT
bridge geometric Hardy/model-space placement        EXACT
arithmetic source norm of delayed/bridge packet     OPEN
renormalized Poisson/Jordan -> Fisher-Hankel map     OPEN / RH-BEARING
full delayed screw/Weil Gram                        OPEN
Riemann Hypothesis                                  UNPROVED
```
