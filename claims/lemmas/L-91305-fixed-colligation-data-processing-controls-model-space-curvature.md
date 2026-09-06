# L-91305 — A fixed source colligation contracts model-space curvature

Claim ID: `L-91305`  
Status: **PROVED ABSTRACT DIFFERENTIAL-COLLIGATION THEOREM; SOURCE LIFT OPEN**  
Created: 2026-08-12  
Depends on: `L-91301`, `L-91035`--`L-91037`  
RH status: **unproved**

## 1. Setup

Let `H0`, `S`, and `H` be Hilbert spaces.  Let

\[
 V_\tau:H_0\to S
\]

be a strongly differentiable family of isometries, and let

\[
 C:S\to H
\]

be one fixed contraction.  Assume

\[
 \boxed{M_\tau=CV_\tau:H_0\to H}
\tag{L-91305.1}
\]

is an isometry for every `tau`.

Put

\[
 R_\tau=V_\tau V_\tau^*,
 \qquad
 Q_\tau=M_\tau M_\tau^*,
 \qquad
 P_\tau=I-Q_\tau.
\]

The range-normal tangent maps are

\[
 N_\tau^S=(I-R_\tau)\dot V_\tau:H_0\to S,
\tag{L-91305.2}
\]

\[
 N_\tau^H=P_\tau\dot M_\tau:H_0\to H.
\tag{L-91305.3}
\]

## 2. Exact tangent factorization

Because `C V_tau=M_tau`, the image under `C` of `Ran V_tau` lies in
`Ran M_tau`.  Hence

\[
 P_\tau C R_\tau=0.
\tag{L-91305.4}
\]

Using `dot M_tau=C dot V_tau`,

\[
\begin{aligned}
 N_\tau^H
 &=P_\tau C\dot V_\tau\\
 &=P_\tau C(I-R_\tau)\dot V_\tau.
\end{aligned}
\]

Therefore

\[
 \boxed{
 N_\tau^H=P_\tau C N_\tau^S.
 }
\tag{L-91305.5}

The Hardy tangent is literally a contracted observation of the source-normal
tangent.

## 3. Data-processing inequalities

For every `f in H0`,

\[
 \boxed{
 \|N_\tau^Hf\|_H
 \le\|N_\tau^Sf\|_S.
 }
\tag{L-91305.6}

Thus, as forms on `H0`,

\[
 \boxed{
 (N_\tau^H)^*N_\tau^H
 \preceq
 (N_\tau^S)^*N_\tau^S.
 }
\tag{L-91305.7}

For every finite-rank packet projection `E` on `H0`,

\[
 \boxed{
 \|N_\tau^HE\|_{\rm HS}^2
 \le
 \|N_\tau^SE\|_{\rm HS}^2.
 }
\tag{L-91305.8}

No dimension factor is lost.

On the output model space, the shape operator of `L-91301` satisfies

\[
 \mathcal B_\tau^*\mathcal B_\tau
 =N_\tau^H(N_\tau^H)^*.
\tag{L-91305.9}

Equation (L-91305.5) therefore gives the explicit source Gram

\[
 \boxed{
 \mathcal B_\tau^*\mathcal B_\tau
 =P_\tau C N_\tau^S(N_\tau^S)^*C^*P_\tau.
 }
\tag{L-91305.10}

In particular, the model-space leakage is not a new independent curvature; it
is the compression of the source normal curvature through the fixed
colligation.

## 4. Equality and auxiliary reserve

Let

\[
 D_C=(I-C^*C)^{1/2}.
\]

For every `f in H0`, (L-91305.5) yields the exact Pythagorean decomposition

\[
\begin{aligned}
 \|N_\tau^Sf\|^2-
 \|N_\tau^Hf\|^2
 ={}&\|D_CN_\tau^Sf\|^2\\
 &+\|Q_\tau C N_\tau^Sf\|^2.
\end{aligned}
\tag{L-91305.11}

Indeed, split `CN_Sf` orthogonally into its `Q_tau` and `P_tau` components, and
use

\[
 \|N_Sf\|^2=\|CN_Sf\|^2+\|D_CN_Sf\|^2.
\]

Hence the source-minus-output tangent defect already has the explicit positive
feature map

\[
 \boxed{
 f\longmapsto
 \binom{D_CN_\tau^Sf}{Q_\tau CN_\tau^Sf}.
 }
\tag{L-91305.12}

No abstract square root is required.

## 5. Application to the zeta completion

Take `H0=H^2(C_+)`, and let

\[
 M_\tau=M_{\Theta_{e^\tau}}
\]

be Suzuki's safe inner multiplication family.  If one constructs a
**fixed-colligation source lift**

\[
 \boxed{
 V_\tau:H^2\to
 \mathcal H_{\Gamma,\mathrm{pole}}^{(1)}
 \oplus L^2(\nu_{e^\tau,\sigma})
 \oplus\mathcal A
 }
\tag{L-91305.13}

such that:

1. `V_tau` is isometric;
2. `C V_tau=M_tau` for one `tau`-independent contraction `C`;
3. the source normal curvature `(N_tau^S)^*N_tau^S` is the completed positive
   first-chaos curvature of `L-91037` plus the explicit gamma/pole channel;

then (L-91305.7) proves

\[
 C_a^{\rm src}\succeq\mathcal J_a^*\mathcal J_a,
\]

and (L-91305.11) produces the complete positive auxiliary defect.  Combined
with the delayed form core, this proves the fixed-scale screw Gram.

Thus the remaining constructive object is not an arbitrary tangent
intertwiner.  It is one fixed Stinespring/first-chaos lifting of Suzuki's entire
safe inner family.

## 6. Why an `a`-dependent output map is insufficient

If `C=C_tau` depends on the radial parameter, then

\[
 \dot M_\tau=\dot C_\tau V_\tau+C_\tau\dot V_\tau.
\]

The first term is an uncontrolled connection curvature and can have either
sign.  Amplitude-level realizations constructed independently at each scale do
not imply (L-91305.7).

The fixed-colligation requirement is therefore load bearing.  It is exactly the
operator version of transporting the whole radial first-chaos family before
taking a norm.

## 7. Proof boundary

```text
fixed-colligation tangent factorization          EXACT
source-to-output curvature data processing       EXACT
explicit positive auxiliary reserve              EXACT
Suzuki amplitude family                          IMPORTED PROVED
fixed first-chaos source lifting of that family  OPEN / RH-BEARING
completed source curvature identification        OPEN
Riemann Hypothesis                               UNPROVED
```
