# T-15302 — Cofinal triangular three-block floors imply RH

Claim ID: `T-15302`  
Title: A vanishing radical-row correction and positive visible/ambient Schur block give the required cofinal lower envelope  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-k`  
Created: 2026-07-31  
Dependencies: `L-15306`; cofinal lower-envelope theorem `T-14302`; radical-tail estimates `L-14312/L-15303`; certified-zero visible floor `L-15305`; multiband complement theorem `L-14311/L-14313`  
Scope: final three-block implication for the positive localized-Weil route

## 1. Cofinal packet

Let `A_lambda` be the exact localized Weil form on an unbounded support
sequence. At every retained support, choose a complete orthogonal decomposition

\[
\mathcal H_\lambda
=R_\lambda\oplus V_\lambda\oplus E_\lambda
\]

with exact block matrix

\[
A_\lambda=
\begin{pmatrix}
B_{R,\lambda}&X_\lambda^*&Y_\lambda^*\\
X_\lambda&B_{V,\lambda}&Z_\lambda^*\\
Y_\lambda&Z_\lambda&C_\lambda
\end{pmatrix}.
\tag{T-15302.1}
\]

Let `G_R(lambda),G_V(lambda),M_lambda` be positive metrics. Suppose there are
numbers

\[
e_\lambda,\kappa_\lambda,\delta_\lambda\ge0,
\qquad h_\lambda>0,
\qquad \beta_\lambda>0
\]

such that all hypotheses of `L-15306` hold:

\[
B_{R,\lambda}\succeq-e_\lambda G_{R,\lambda},
\tag{T-15302.2}
\]

\[
C_\lambda\succeq h_\lambda M_\lambda,
\tag{T-15302.3}
\]

\[
B_{V,\lambda}
-h_\lambda^{-1}Z_\lambda^*M_\lambda^{-1}Z_\lambda
\succeq\beta_\lambda G_{V,\lambda},
\tag{T-15302.4}
\]

and, with

\[
\widetilde X_\lambda
=X_\lambda-h_\lambda^{-1}
 Z_\lambda^*M_\lambda^{-1}Y_\lambda,
\tag{T-15302.5}
\]

\[
\begin{aligned}
&h_\lambda^{-1}Y_\lambda^*M_\lambda^{-1}Y_\lambda\\
&\qquad+
\beta_\lambda^{-1}\widetilde X_\lambda^*
G_{V,\lambda}^{-1}\widetilde X_\lambda
\preceq\kappa_\lambda G_{R,\lambda}.
\end{aligned}
\tag{T-15302.6}
\]

All directed assembly and analytic omissions are charged by
`delta_lambda` in the complete block metric.

## 2. Main cofinal theorem

If

\[
\boxed{
e_\lambda\longrightarrow0,
\qquad
\kappa_\lambda\longrightarrow0,
\qquad
\delta_\lambda\longrightarrow0,}
\tag{T-15302.7}
\]

then

\[
\boxed{
\inf\sigma(A_\lambda)
\ge-\varepsilon_\lambda,
\qquad
\varepsilon_\lambda
=e_\lambda+\kappa_\lambda+\delta_\lambda
\longrightarrow0.}
\tag{T-15302.8}
\]

Consequently the Riemann hypothesis is true.

### Proof

`L-15306` gives (T-15302.8) at every retained support. The supports are cofinal,
so the localized lower spectral values have a rigorous lower envelope whose
negative part tends to zero. Apply `T-14302`, which uses support monotonicity to
obtain nonnegativity of every fixed localized Weil form and then Weil's
criterion. QED.

## 3. Scalar norm form of the remaining rates

Equation (T-15302.6) follows from the two scalar conditions

\[
\boxed{
\frac{\|M_\lambda^{-1/2}Y_\lambda
G_{R,\lambda}^{-1/2}\|^2}{h_\lambda}
\longrightarrow0,}
\tag{T-15302.9}
\]

and

\[
\boxed{
\frac{\|G_{V,\lambda}^{-1/2}
\widetilde X_\lambda
G_{R,\lambda}^{-1/2}\|^2}{\beta_\lambda}
\longrightarrow0.}
\tag{T-15302.10}
\]

These are the exact replacements for the looser terms
`||X||^2/beta` and `||(Y,Z)||^2/h`. The visible-complement cross `Z` does not
need to tend to zero. It enters only through the visible Schur floor and the
corrected cross `widetilde X`.

## 4. One-functional radical-tail form

Let

\[
D_{0,\lambda}=
\begin{pmatrix}
\beta_\lambda G_{V,\lambda}
+h_\lambda^{-1}Z_\lambda^*M_\lambda^{-1}Z_\lambda
&Z_\lambda^*\\
Z_\lambda&h_\lambda M_\lambda
\end{pmatrix}.
\tag{T-15302.11}
\]

If the radical row is the localization of exact global radical tails and one
proves the single dual estimate

\[
\left|Q(t_{\lambda,r},v+w)\right|
\le\eta_\lambda\|r\|_{G_R}
\|(v,w)\|_{D_{0,\lambda}},
\tag{T-15302.12}
\]

then

\[
\kappa_\lambda\le\eta_\lambda^2.
\tag{T-15302.13}
\]

Thus the complete `R--V` and `R--E` coupling is one tail functional. A production
proof should contract the complete Weil form against the Schur-lifted test
vector before taking absolute values.

## 5. Gaussian-tail corollary

Suppose a growing exact Hermite/Gaussian packet satisfies a uniform bound

\[
e_\lambda+\eta_\lambda^2
\le
A_\lambda e^{-c\lambda^2}
\tag{T-15302.14}
\]

for one `c>0`, while the metric, visible-floor, complement-floor, packet-rank,
and triangular-lift losses are absorbed in a factor

\[
A_\lambda=\exp(o(\lambda^2)).
\tag{T-15302.15}
\]

Then the first two terms in (T-15302.8) tend to zero. In particular, any
polynomial loss is harmless.

This corollary explains the correct asymptotic target. One does **not** need the
visible or ambient blocks to converge to diagonal blocks. It is enough that:

1. their Schur-corrected floors remain positive;
2. their inverse metrics grow sub-Gaussian relative to the radical-tail decay;
3. the complete tail functional is uniformly controlled over the growing
   radical packet.

## 6. Certified-zero visible split

`L-15305` supplies an unconditional raw visible floor of the form

\[
B_{V,\lambda}\succeq
(\sigma_\lambda^2-B_{T,\lambda})G_{V,\lambda}.
\tag{T-15302.16}
\]

To feed (T-15302.4), it is enough to prove the relative visible-complement
coupling estimate

\[
Z_\lambda^*M_\lambda^{-1}Z_\lambda
\preceq
\theta_\lambda h_\lambda
(\sigma_\lambda^2-B_{T,\lambda})G_{V,\lambda},
\qquad
\limsup\theta_\lambda<1.
\tag{T-15302.17}
\]

Then one may take

\[
\beta_\lambda
=(1-\theta_\lambda)
(\sigma_\lambda^2-B_{T,\lambda}).
\tag{T-15302.18}
\]

This is a relative Schur margin, not a demand that `Z_lambda` vanish.

## 7. Exact frontier after the three-block closure

The finite three-block algebra is complete. The remaining zeta-specific theorem
is the simultaneous cofinal construction of packets satisfying:

1. a source-bound visible floor and (T-15302.17);
2. a uniform growing-packet version of the exact radical-tail estimate
   (T-15302.12);
3. a vanishing assembly radius.

The theorem isolates those analytic rates without a hidden independent-cross
penalty. No finite ladder or midpoint extrapolation substitutes for them.

## 8. Proof boundary

- The implication is exact under its hypotheses.
- No production support sequence satisfying all hypotheses is supplied here.
- `L-15305` still needs a source-bound high-zero tail envelope at each production
  packet.
- Uniformity over a growing Hermite packet remains essential.
- Suzuki/CCM normalization and form-domain gates remain external.
- RH is not claimed without the cofinal packet construction.
