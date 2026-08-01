# L-15629 — Exact completion of a prolate core preserves the sub-square-root frame

Claim ID: `L-15629`  
Title: A power-saving angle to the global-anchor/prolate core plus the exact finite Fourier inverse yields a complete exact source frame  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF; PRODUCTION ANGLE ESTIMATE OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15628`; `L-16218`--`L-16227`; exact linear source/range maps  
Scope: the complete-frame condition in `L-15627`  
Related counterexample candidates: none

## 1. Purpose

The global-anchor/prolate source frame has the desired radial, endpoint, alias,
and zero-side profile structure, including a dimension-uniform omitted-tail Gram
floor. What was missing was proof that it is an exact frame for the actual
complete dangerous complement.

The exact finite Fourier inverse `L-15628` repairs this algebraic defect. The
repair is allowed to be much rougher than the prolate core: it only has to be
small enough not to destroy the already positive tail Gram. Since the exact
inverse costs only `R^(1/4+o(1))`, a quarter-power approximation of the actual
complement by the prolate core is sufficient.

This theorem separates the two jobs:

```text
prolate/global-anchor core:
    supplies the positive tail Gram and support-averaged profile theorem;

finite Fourier source correction:
    supplies exact completeness and source constraints.
```

## 2. Spaces and maps

At radial scale `R`, let

\[
 W_R
\tag{L-15629.1}
\]

be the actual finite dangerous complement, with positive production metric
`G_R`. Let

\[
 J_R:W_R\longrightarrow\mathcal H_R
\tag{L-15629.2}
\]

be its exact localized realization. Assume

\[
 J_R(W_R)\subset E_{N_R}(L_R),
\qquad
 L_R=\log R,
\qquad
 N_R=O(L_R^2).
\tag{L-15629.3}
\]

Let

\[
 \mathcal L_R:\mathcal S_R\longrightarrow E_{N_R}(L_R)
\tag{L-15629.4}
\]

be the exact projected arithmetic source map.

Let

\[
 F_R^0:W_R\longrightarrow\mathcal S_R
\tag{L-15629.5}
\]

be a source synthesis built from the well-conditioned global-anchor/prolate
frame. Its localized image is

\[
 H_R=\mathcal L_RF_R^0.
\tag{L-15629.6}
\]

The approximation defect is

\[
 \Delta_R=J_R-H_R.
\tag{L-15629.7}
\]

Finally let

\[
 \mathcal C_R:E_{N_R}(L_R)\longrightarrow\mathcal S_R
\tag{L-15629.8}
\]

be the exact right inverse of `L-15628`:

\[
 \mathcal L_R\mathcal C_R=I.
\tag{L-15629.9}
\]

All source maps take values in the exact Connes–Consani source space.

## 3. Exact completed frame

Define

\[
 \boxed{
 F_R=F_R^0+\mathcal C_R\Delta_R.
 }
\tag{L-15629.10}
\]

Then

\[
 \begin{aligned}
 \mathcal L_RF_R
 &=H_R+\mathcal L_R\mathcal C_R(J_R-H_R)\\
 &=H_R+(J_R-H_R)\\
 &=J_R.
 \end{aligned}
\tag{L-15629.11}
\]

Therefore

\[
 \boxed{
 \mathcal L_RF_R=J_R
 }
\tag{L-15629.12}
\]

exactly. The completed source frame spans the actual complete dangerous
complement and satisfies every exact source constraint.

No determinant, generic-density argument, or inversion of the projected
prolate image occurs.

## 4. Tail/profile norms

Let

\[
 T_R^0:W_R\to\mathcal X_R
\tag{L-15629.13}
\]

be the omitted-tail/profile synthesis of the prolate core, and let

\[
 U_R:W_R\to\mathcal X_R
\tag{L-15629.14}
\]

be the omitted-tail/profile synthesis of the correction
`C_R Delta_R`. Thus the complete tail is

\[
 T_R=T_R^0+U_R.
\tag{L-15629.15}
\]

Assume the core tail Gram satisfies

\[
 \boxed{
 c_0G_R\preceq (T_R^0)^*T_R^0\preceq C_0G_R
 }
\tag{L-15629.16}
\]

with fixed `0<c_0<=C_0`. This is the production interface of
`L-16227` after metric transport.

Let the exact inverse envelope satisfy

\[
 \|\mathcal C_R\|_{E_N\to\mathcal X_R}
 \le M_R.
\tag{L-15629.17}
\]

`L-15628` supplies

\[
 \boxed{M_R\le R^{1/4+o(1)}.}
\tag{L-15629.18}
\]

Put

\[
 \eta_R
 =\|\Delta_RG_R^{-1/2}\|_{E_N}.
\tag{L-15629.19}
\]

Then

\[
 \boxed{
 \|U_RG_R^{-1/2}\|
 \le M_R\eta_R.
 }
\tag{L-15629.20}
\]

## 5. Preservation of the tail Gram

For every coefficient vector `c`,

\[
 \|T_Rc\|\ge\|T_R^0c\|-\|U_Rc\|.
\]

Hence

\[
 T_R^*T_R
 \succeq
 \left(\sqrt{c_0}-M_R\eta_R\right)^2G_R.
\tag{L-15629.21}
\]

Similarly,

\[
 T_R^*T_R
 \preceq
 \left(\sqrt{C_0}+M_R\eta_R\right)^2G_R.
\tag{L-15629.22}
\]

Therefore, if

\[
 \boxed{M_R\eta_R\longrightarrow0,}
\tag{L-15629.23}
\]

the complete exact frame retains a dimension-uniform positive tail Gram:

\[
 \boxed{
 \frac{c_0}{4}G_R
 \preceq T_R^*T_R
 \preceq 4C_0G_R
 }
\tag{L-15629.24}
\]

for all sufficiently large `R`.

By (L-15629.18), the explicit sufficient approximation rate is

\[
 \boxed{
 \eta_R=o\!\left(R^{-1/4-o(1)}\right).
 }
\tag{L-15629.25}
\]

Any fixed rate

\[
 \eta_R=O(R^{-1/4-\varepsilon})
\tag{L-15629.26}
\]

is more than sufficient.

## 6. Whitened support-derivative envelope

Let the prolate core have whitened amplitude/support-derivative envelope

\[
 \mathfrak B_R^0=R^{o(1)},
\tag{L-15629.27}
\]

as supplied by the global-anchor/radial/endpoint stack. Let the inverse in
`L-15628` satisfy the corresponding block envelope, including the logarithmic
support derivative. If

\[
 \eta_R^{(1)}
 =
 \|\Delta_RG_R^{-1/2}\|
 +R\|\partial_R(\Delta_RG_R^{-1/2})\|
\tag{L-15629.28}
\]

obeys

\[
 M_R\eta_R^{(1)}=o(1),
\tag{L-15629.29}
\]

then the complete exact frame has

\[
 \boxed{
 \mathfrak B_R
 \le
 C\left(\mathfrak B_R^0+M_R\eta_R^{(1)}\right)
 =R^{o(1)}.
 }
\tag{L-15629.30}
\]

The constant includes the uniformly bounded whitening maps from
(L-15629.24). Consequently

\[
 \boxed{
 \mathfrak B_R
 =o\!\left(\sqrt{R/\log R}\right).
 }
\tag{L-15629.31}

This is exactly the missing complete-frame condition of `L-15627`.

## 7. Graph-kernel adapter

The complete selected-real-zero kernel of `L-20302` is the exact graph

\[
 K_R
 =\{r-V_{W,R}^{-1}V_{R,R}r:r\in R_R\}
\tag{L-15629.32}
\]

over the old global-anchor/radical packet. In that setting one may take

\[
 H_Rr=r,
\qquad
 \Delta_Rr=-V_{W,R}^{-1}V_{R,R}r.
\tag{L-15629.33}
\]

If

\[
 V_{W,R}^*V_{W,R}\succeq\sigma_R^2G_W,
\qquad
 V_{R,R}^*V_{R,R}\preceq\epsilon_RG_R,
\tag{L-15629.34}
\]

then `L-20302` gives

\[
 \eta_R\le\frac{\sqrt{\epsilon_R}}{\sigma_R}.
\tag{L-15629.35}
\]

Therefore the exact scalar condition

\[
 \boxed{
 R^{1/4+o(1)}
 \frac{\sqrt{\epsilon_R}}{\sigma_R}
 \longrightarrow0
 }
\tag{L-15629.36}
\]

produces an exact complete kernel frame with positive tail Gram and
sub-square-root support envelope.

This is substantially weaker than demanding that an arbitrary Möbius inverse
be uniformly well conditioned on the complete packet.

## 8. Compatibility with the published prolate error scale

The uniform angular/prolate approximation in `L-16219` has the scale

\[
 O\!\left(R^{-2/3}\operatorname{polylog}R\right)
\tag{L-15629.37}
\]

on the quadratic-log mode window. Since

\[
 R^{1/4}R^{-2/3}=R^{-5/12},
\tag{L-15629.38}
\]

that error is safely below the completion threshold. Thus no stronger PSWF
asymptotic rate is needed.

What remains is not the size of the individual prolate approximation error. It
is the **complete-packet angle theorem** asserting that the actual dangerous
complement is approximated, in the production metric and support derivative,
by the global-anchor/prolate core at one fixed power-saving rate.

## 9. Form-exact variant

If only the Weil/Schur floor is required, the correction need not satisfy the
full profile envelope. Exact radicality gives, by polarization,

\[
 Q_W(T_{\Delta_R c},T_{\Delta_R d})
 =Q_W(\Delta_Rc,\Delta_Rd).
\tag{L-15629.39}
\]

Thus a correction small in the localized form graph norm contributes the same
small matrix in the omitted tail, regardless of the norm of the underlying
source coefficients. This provides a second route when the profile producer is
rough but the localized approximation is form-small.

The ordinary tail-Gram floor, however, still requires (L-15629.23) or another
positive metric argument.

## 10. Proof boundary

- The exact completion formula and Gram perturbation estimates are elementary
  operator algebra.
- `L-15628` supplies the declared inverse bound modulo its normalization audit.
- The global-anchor/prolate tail Gram and core profile estimates are imported
  from `L-16218`--`L-16227`.
- No current theorem proves (L-15629.25) or (L-15629.36) for the **actual
  complete dangerous complement**.
- Under false RH, an off-line Xi-cardinal direction can force precisely this
  angle or frame floor to fail.
- No RH conclusion is claimed without the complete-packet angle estimate.
