# L-15624 — Packet-adapted Schur completion removes three clipped-excess defects

Claim ID: `L-15624`  
Title: Every positive-deficit lower model admits a packet-adapted Schur completion with zero packet majorant slack and residual-controlled clipping leakage  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF; COMPLEMENT TRACE REMAINS RH-BEARING`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15621`; finite-rank block algebra; functional calculus  
Scope: sharpen the cofinal four-defect target in Issue #156  
Related counterexample candidates: none

## 1. Setting

Let `A` be a lower-bounded self-adjoint operator or closed form on a Hilbert
space `H`. Let `P` be a finite-rank orthogonal projection of rank `d`, put

\[
 Q=I-P,
\]

and suppose the relevant block maps are form bounded. Assume one positive
trace-class lower model

\[
 \boxed{A\succeq GI-D,\qquad D\succeq0}                 \tag{L-15624.1}
\]

and define its slack

\[
 \mathcal R=A+D-GI\succeq0.                              \tag{L-15624.2}
\]

Suppose the packet compression and complete cross residual satisfy

\[
 \boxed{-\alpha P\preceq PAP\preceq\alpha P,\qquad
        PAQAP\preceq\beta^2P,}                          \tag{L-15624.3}
\]

with

\[
 0\le\alpha<G.                                           \tag{L-15624.4}
\]

Write

\[
 K=GP-PAP\succeq(G-\alpha)P\succ0                       \tag{L-15624.5}
\]

on `Ran P`, and put

\[
 X=QAP:\operatorname{Ran}P\to\operatorname{Ran}Q.       \tag{L-15624.6}
\]

## 2. Packet-adapted positive deficit

Relative to

\[
 H=\operatorname{Ran}P\oplus\operatorname{Ran}Q,
\]

define

\[
 \boxed{
 D^\sharp=
 \begin{pmatrix}
 K&-X^*\\
 -X&QDQ+XK^{-1}X^*
 \end{pmatrix}.}                                         \tag{L-15624.7}
\]

Then `D^sharp` is positive and trace class. Indeed,

\[
 D^\sharp=
 \begin{pmatrix}K^{1/2}\\-XK^{-1/2}\end{pmatrix}
 \begin{pmatrix}K^{1/2}&-K^{-1/2}X^*\end{pmatrix}
 +\begin{pmatrix}0&0\\0&QDQ\end{pmatrix}.                \tag{L-15624.8}
\]

Moreover,

\[
 \boxed{A\succeq GI-D^\sharp.}                           \tag{L-15624.9}
\]

### Proof of the lower model

The new slack is

\[
 \mathcal R^\sharp=A+D^\sharp-GI.
\]

Its packet diagonal and packet-complement cross blocks cancel exactly:

\[
 P\mathcal R^\sharp P=0,
 \qquad
 P\mathcal R^\sharp Q=Q\mathcal R^\sharp P=0.            \tag{L-15624.10}
\]

The complement block is

\[
 Q\mathcal R^\sharp Q
 =Q\mathcal RQ+XK^{-1}X^*\succeq0.                      \tag{L-15624.11}
\]

Thus `mathcal R^sharp>=0`, proving (L-15624.9). In particular,

\[
 \boxed{P\mathcal R^\sharp P=0}                          \tag{L-15624.12}
\]

identically. The packet-majorant defect in `L-15621` has been removed rather
than estimated.

## 3. Clipping leakage is a squared residual

Choose

\[
 \alpha<t<\Gamma<G,
 \qquad
 \theta=G-\Gamma,
 \qquad
 \kappa=G-\alpha.                                        \tag{L-15624.13}
\]

Then

\[
 \kappa-\theta=\Gamma-\alpha>0.                          \tag{L-15624.14}
\]

For every real scalar `x`,

\[
 (\theta-x)_+
 \le{(x-\kappa)^2\over\kappa-\theta}.                   \tag{L-15624.15}
\]

Functional calculus and compression therefore give

\[
 P(\theta I-D^\sharp)_+P
 \preceq
 {1\over\Gamma-\alpha}
 P(D^\sharp-\kappa I)^2P.                                \tag{L-15624.16}
\]

Now

\[
 P(D^\sharp-\kappa I)^2P
 = (\alpha P-PAP)^2+X^*X.                                \tag{L-15624.17}
\]

Because

\[
 0\preceq\alpha P-PAP\preceq2\alpha P
\]

and `X^*X=PAQAP<=beta^2P`, one obtains

\[
 \boxed{
 P(\theta I-D^\sharp)_+P
 \preceq
 {4\alpha^2+\beta^2\over\Gamma-\alpha}P.}               \tag{L-15624.18}
\]

Consequently,

\[
 \boxed{
 \operatorname{Tr}P(\theta I-D^\sharp)_+P
 \le
 d\,{4\alpha^2+\beta^2\over\Gamma-\alpha}.}             \tag{L-15624.19}
\]

## 4. Reduced four-defect inequality

Put

\[
 E^\sharp=(D^\sharp-\theta I)_+.                         \tag{L-15624.20}
\]

Apply the exact four-defect identity of `L-15621` to the lower model
`A>=GI-D^sharp`. Since (L-15624.12) annihilates the packet majorant slack and

\[
 \operatorname{Tr}P(\alpha I-A)P\le2d\alpha,             \tag{L-15624.21}
\]

we obtain

\[
 \boxed{
 \begin{aligned}
 &\operatorname{Tr}(QE^\sharp Q)
 +\operatorname{Tr}(P\mathcal R^\sharp P)\\
 &\quad+
 \operatorname{Tr}P(\theta I-D^\sharp)_+P
 +2d\alpha\\
 &\le
 \operatorname{Tr}(QE^\sharp Q)
 +2d\alpha
 +d{4\alpha^2+\beta^2\over\Gamma-\alpha}.
 \end{aligned}}                                          \tag{L-15624.22}
\]

Therefore the single reduced condition

\[
 \boxed{
 \operatorname{Tr}(QE^\sharp Q)
 +2d\alpha
 +d{4\alpha^2+\beta^2\over\Gamma-\alpha}
 <\Gamma-t}                                              \tag{L-15624.23}
\]

implies the original four-defect gate for the packet-adapted lower model. It
follows that

\[
 A|_{P^\perp}\succ tI,
 \qquad
 N_A(t)=d.                                                \tag{L-15624.24}
\]

## 5. Cofinal consequence

For a sequence with

\[
 d_j\alpha_j\to0,
 \qquad
 {d_j(4\alpha_j^2+\beta_j^2)\over
  \Gamma_j-\alpha_j}	o0,                                \tag{L-15624.25}
\]

the complete source-side contribution to the four-defect sum vanishes. The
only remaining term is

\[
 \boxed{
 \operatorname{Tr}
 \left[
 Q_j(D_j^\sharp-(G_j-\Gamma_j)I)_+Q_j
 \right].}                                               \tag{L-15624.26}
\]

Thus the positive path no longer needs separate asymptotic estimates for the
packet lower-symbol slack and clipping leakage. Both are eliminated or reduced
to the already available low-compression/residual rates.

## 6. Relation to the requested symbol deficit

`D^sharp` is a packet-adapted positive trace-class lower model constructed from
the exact operator, the original positive deficit `D`, and finite packet
blocks. It need not be a scalar Fourier multiplier. Therefore this lemma does
not prove the stronger statement with the unmodified Suzuki multiplier

\[
 P_I\mathcal F^{-1}(G-s)_+\mathcal FP_I.
\]

It proves that the scalar-symbol majorant slack is not intrinsically part of
the RH obstruction. Once packet-adapted completion is allowed, the sole
remaining quantity is the dangerous clipped mass on the true complement.

## 7. Exact obstruction

If there is one additional `(d+1)`-st direction below `t`, `L-15622` applied to
`D^sharp` forces

\[
 \operatorname{Tr}(QE^\sharp Q)
 +2d\alpha
 +d{4\alpha^2+\beta^2\over\Gamma-\alpha}
 >\Gamma-t
\]

up to the nonnegative slack terms retained in the exact identity. Thus the
remaining complement trace is still the no-extra-low-mode theorem; the Schur
completion does not assume it away.

## 8. Proof boundary

- Positivity of `D^sharp`, the lower model, and the clipping estimate are exact.
- The theorem closes three of the four requested positive defects.
- It changes the deficit from the scalar Fourier localization operator to a
  packet-adapted trace-class operator.
- No cofinal bound for (L-15624.26) is proved.
- Under the complete-kernel hypothesis, an off-line Xi-cardinal direction makes
  such a bound impossible.
- No proof of RH is claimed.
