# T-21703 — Final saturation equivalence and complete RH proof chain

Claim ID: `T-21703`  
Title: The Brownian log-variance saturation, the line-zero convolution identity, the completed annihilator, and RH are equivalent  
Status: **PROPOSED PENDING INDEPENDENT REVIEW — equivalence chain proved; the saturation inequality itself is not proved**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Frozen parent head for this continuation: `61c6f1129eb2848ce30750ec51c257945a7351c7`  
Dependencies: `T-21701`, `T-21702`, `L-21703`; Biane--Pitman--Yor's Brownian-range Mellin identity; the centered Hadamard product for `xi`; the rigorous zero verification below the first possible unverified height  
Scope: exact theorem ledger for the proposed full proof, with the sole unresolved arrow isolated

## 1. Normalization

Put

\[
X(w)=\xi\!\left(\frac12+w\right),
\qquad
\Xi(t)=\frac{X(it)}{X(0)}
      =\frac{\xi(\frac12+it)}{\xi(\frac12)}.
\tag{T-21703.1}
\]

Then `X` is real entire, even, of order one, and `Xi` is the characteristic
function of the centered completed-Riemann probability law.

Group the nonzero zeros of `X` as follows.

- Critical-line pairs
  \[
  w=\pm i\gamma,
  \qquad \gamma>0,
  \]
  with multiplicity `m_gamma`.
- Off-line quartets
  \[
  w=\pm\delta\pm i\gamma,
  \qquad \delta>0,
  \quad\gamma>0,
  \]
  with multiplicity `m_(delta,gamma)` for one representative.

The order-one zero count gives

\[
\sum_{X(w)=0}|w|^{-2}<\infty,
\tag{T-21703.2}
\]

so all second-logarithmic-derivative sums below converge absolutely after this
symmetric grouping.

## 2. Brownian representation

Let `b` be a standard Brownian bridge and define its normalized range

\[
Y=\sqrt{\frac2\pi}
\left(
 \max_{0\le u\le1}b_u-
 \min_{0\le u\le1}b_u
\right).
\tag{T-21703.3}
\]

Biane--Pitman--Yor prove

\[
\boxed{\mathbb E[Y^s]=2\xi(s)\qquad(s\in\mathbb C).}
\tag{T-21703.4}
\]

Under the half-size-biased law

\[
\frac{d\mathbb P_{1/2}}{d\mathbb P}
 =\frac{Y^{1/2}}{\mathbb E[Y^{1/2}]},
\qquad
Z=\log Y,
\tag{T-21703.5}
\]

one has

\[
\boxed{
\mathbb E_{1/2}[e^{itZ}]=\Xi(t).}
\tag{T-21703.6}
\]

The functional equation makes this tilted law symmetric. Hence

\[
\boxed{
V:=\operatorname{Var}_{1/2}(Z)
 =-\Xi''(0)
 =\frac{\xi''(1/2)}{\xi(1/2)}.}
\tag{T-21703.7}
\]

## 3. Positive quartet defect

The centered canonical product is

\[
\begin{aligned}
\Xi(t)
={}&\prod_{\gamma\in\Gamma_L}
 \left(1-\frac{t^2}{\gamma^2}\right)^{m_\gamma}\\
&\times
\prod_{(\delta,\gamma)\in\Gamma_O}
 \left(1-\frac{t^2}{(\gamma-i\delta)^2}\right)^{m_{\delta,\gamma}}
 \left(1-\frac{t^2}{(\gamma+i\delta)^2}\right)^{m_{\delta,\gamma}}.
\end{aligned}
\tag{T-21703.8}
\]

Differentiating the logarithm twice at the origin gives

\[
\boxed{
V=
2\sum_{\gamma\in\Gamma_L}\frac{m_\gamma}{\gamma^2}
+
4\sum_{(\delta,\gamma)\in\Gamma_O}
 m_{\delta,\gamma}
 \frac{\gamma^2-\delta^2}{(\gamma^2+\delta^2)^2}.}
\tag{T-21703.9}
\]

Every nontrivial zero has `gamma>14`, while `0<delta<1/2`. Consequently every
summand in the second sum is strictly positive.

Define

\[
\boxed{
D_{\rm off}
 :=V-2\sum_{\gamma\in\Gamma_L}\frac{m_\gamma}{\gamma^2}.}
\tag{T-21703.10}
\]

Then

\[
\boxed{D_{\rm off}\ge0,}
\qquad
\boxed{D_{\rm off}=0\iff\mathrm{RH}.}
\tag{T-21703.11}
\]

No cancellation between distinct hypothetical off-line packets is possible at
this order.

## 4. The final saturation statement

The final Brownian saturation statement is

\[
\boxed{
\mathrm{SAT}:
\quad
\operatorname{Var}_{1/2}(\log Y)
\le
2\sum_{\gamma\in\Gamma_L}\frac{m_\gamma}{\gamma^2}.}
\tag{T-21703.12}
\]

Equation (T-21703.9) already proves the opposite inequality. Therefore

\[
\boxed{
\mathrm{SAT}
\iff
D_{\rm off}=0
\iff
\mathrm{RH}.}
\tag{T-21703.13}
\]

Thus `SAT` is not a routine auxiliary estimate. An independent proof of `SAT`
is already a complete proof of RH.

## 5. Gamma-convolution form

Let

\[
\Sigma_2=\frac2{\pi^2}
 \sum_{n\ge1}\frac{\Gamma(2)_n}{n^2},
\tag{T-21703.14}
\]

with independent unit-rate gamma variables. Biane--Pitman--Yor prove

\[
\Sigma_2\overset d=\frac2\pi Y^2.
\tag{T-21703.15}
\]

Under the quarter-size-biased law for `Sigma_2`,

\[
\operatorname{Var}^{\Sigma}_{1/4}(\log\Sigma_2)=4V.
\tag{T-21703.16}
\]

Hence `SAT` is equivalently

\[
\boxed{
\operatorname{Var}^{\Sigma}_{1/4}(\log\Sigma_2)
\le
8\sum_{\gamma\in\Gamma_L}\frac{m_\gamma}{\gamma^2}.}
\tag{T-21703.17}
\]

The size-biased perpetuity for `Sigma_2` recorded in `L-21703` supplies a
concrete stochastic operator for an attempted proof, but it does not by itself
imply (T-21703.17).

## 6. Uniform/cosine-bell factorization

For each critical-line ordinate, put

\[
U_\gamma(t)=
 \frac{\sin(\pi t/\gamma)}{\pi t/\gamma},
\tag{T-21703.18}
\]

and

\[
C_\gamma(t)=
 \frac{\sin(\pi t/\gamma)}
 {\left(\pi t/\gamma\right)
  \left(1-t^2/\gamma^2\right)}.
\tag{T-21703.19}
\]

These are characteristic functions of the centered uniform and cosine-bell
laws on `[-pi/gamma,pi/gamma]`, and

\[
\boxed{
U_\gamma(t)=
\left(1-\frac{t^2}{\gamma^2}\right)C_\gamma(t).}
\tag{T-21703.20}
\]

Let `mu_U,mu_C` be the multiplicity-weighted infinite convolution laws. Then

\[
\operatorname{Var}(\mu_U)
 =\frac{\pi^2}{3}
  \sum_\gamma\frac{m_\gamma}{\gamma^2},
\tag{T-21703.21}
\]

\[
\operatorname{Var}(\mu_C)
 =\left(\frac{\pi^2}{3}-2\right)
  \sum_\gamma\frac{m_\gamma}{\gamma^2}.
\tag{T-21703.22}
\]

If `mu_Xi` denotes the law of `Z`, then `T-21702` gives

\[
\boxed{
\mathrm{RH}
\iff
\mu_\Xi*\mu_C=\mu_U.}
\tag{T-21703.23}
\]

Taking variances in (T-21703.23) recovers the equality case of `SAT`.
Conversely, (T-21703.9) shows that variance equality alone already forces RH.
Therefore

\[
\boxed{
\mathrm{SAT}
\iff
\mu_\Xi*\mu_C=\mu_U
\iff
\mathrm{RH}.}
\tag{T-21703.24}
\]

## 7. Convex-order and martingale forms

Let `Z,C,U` have laws `mu_Xi,mu_C,mu_U`, respectively, with `Z` independent of
`C`. Since all laws are centered and square-integrable, the proposed stronger
statement

\[
\boxed{Z+C\preceq_{\rm cx}U}
\tag{T-21703.25}
\]

implies `SAT` by testing the convex function `x -> x^2`. Equation
(T-21703.9) then forces equality and RH. Under RH, the laws are equal, so the
converse holds. Thus

\[
\boxed{
\mathrm{RH}
\iff
Z+C\preceq_{\rm cx}U.}
\tag{T-21703.26}
\]

By Strassen's theorem, (T-21703.25) is equivalent to the existence of a
martingale coupling satisfying

\[
\boxed{
\mathbb E[U\mid Z+C]=Z+C.}
\tag{T-21703.27}
\]

This is the most concrete nonanalytic target presently available: construct the
martingale coupling from Brownian-bridge or gamma-perpetuity data and the
explicit line-zero uniform/cosine factors.

## 8. Completed prime-annihilator form

Let `R_infty` denote the corrected, two-sided completed residual of `T-21701`.
Subject to independent review of that full Guinand--Weil normalization,

\[
\boxed{
R_\infty\equiv0\iff\mathrm{RH}.}
\tag{T-21703.28}
\]

Consequently the full proposed chain is

\[
\boxed{
\begin{aligned}
\mathrm{SAT}
&\iff D_{\rm off}=0\\
&\iff E_{\rm off}\equiv1\\
&\iff \mu_\Xi*\mu_C=\mu_U\\
&\iff R_\infty\equiv0\\
&\iff \mathrm{RH}.
\end{aligned}}
\tag{T-21703.29}
\]

The scalar first, second, third, and final equivalences do not require the
prime-side normalization. The `R_infty` equivalence remains a separate proposed
analytic realization of the same obstruction.

## 9. Exact proof ledger

The proposed full proof has the following status.

1. **Brownian Mellin identity.** Imported theorem of Biane--Pitman--Yor.
2. **Half-tilted characteristic function and variance.** Exact consequence.
3. **Centered Hadamard grouping.** Standard order-one entire-function algebra.
4. **Positive quartet defect.** Exact and sign-definite.
5. **Uniform/cosine-bell factorization.** Exact finite transforms plus `L2`
   infinite convolution.
6. **Corrected completed annihilator.** Proposed, with two-sided prime and full
   archimedean ledger required.
7. **SAT / martingale coupling.** **OPEN.** This is the sole independent step
   needed by the short scalar proof.
8. **RH conclusion.** Immediate from Steps 4 and 7.

## 10. Proof boundary

No claim is made here that `SAT`, (T-21703.25), or (T-21703.27) has been proved.
They are equivalent RH-bearing statements. A verification report must reject any
argument that derives them by assuming one of the following under another name:

- Laguerre--Polya or `PF_infinity` membership of `Xi`;
- the complete central Hausdorff hierarchy;
- innerness or zero-free continuation of the xi scattering ratio;
- the centered GGC/Thorin representation of the reciprocal xi function;
- annihilator vanishing or the absence of an off-line pole packet;
- a finite verified-height limit promoted to exact equality.

The theorem's contribution is the exact, noncancelling chain and the isolation
of one reviewable final statement. It is not a completed proof of that final
statement.