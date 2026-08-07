# L-15138 — Exact Ward target transgression and the quartic preservation gate

Claim ID: `L-15138`  
Status: **PROVED EXACT ANALYTIC IDENTITY; RIEMANN DEFECT VANISHING OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15137`; the finite-window Guinand--Weil bookkeeping total in Shimizu v6/v8; regularized determinant calculus  
Scope: redo the classical target calculation after the nonlinear relative-`det_2` Ward amendment  
Related counterexample candidates: none

## 1. Two finite logarithmic-derivative ledgers

Fix a finite window/readout pair `(M,N)`. Let

\[
 g_M^{\rm lin}(w)
 =\sum_{\ell\ge2}(-i)^{\ell-2}
   a_{\ell,M}^{\rm lin}w^{\ell-1}
 \tag{L-15138.1}
\]

be the manuscript's original centered one-contour Guinand--Weil ledger after
its displayed **linear** finite-jet subtraction. Let

\[
 g_{M,N}^{\rm Ward}(w)
 =\sum_{\ell\ge2}(-i)^{\ell-2}
   a_{\ell,M,N}^{\rm Ward}w^{\ell-1}
 =\frac d{dw}\log\det{}_2(I+iwK_{M,N})
 \tag{L-15138.2}
\]

be the nonlinear Ward-amended ledger of `L-15137`, so

\[
 a_{\ell,M,N}^{\rm Ward}
 =\operatorname{Tr}(K_{M,N}^{\ell}).
 \tag{L-15138.3}
\]

Write

\[
 e_{\ell,M,N}
 :=a_{\ell,M}^{\rm lin}
   -a_{\ell,M,N}^{\rm Ward}
 =q_{\ell,M,N}^{\rm Ward}-q_{\ell,M}^{\rm lin}.
 \tag{L-15138.4}
\]

Thus `e_ell` is exactly the target-preservation defect, not merely one contact
subterm.

## 2. Exact transgression formula

Normalize the corresponding centered entire factors by

\[
 F_M^{\rm lin}(0)=F_{M,N}^{\rm Ward}(0)=1
 \tag{L-15138.5}
\]

and remove the common constant and linear exponential factors. Then

\[
 \boxed{
 \frac d{dw}\log
 \frac{F_M^{\rm lin}(w)}{F_{M,N}^{\rm Ward}(w)}
 =\sum_{\ell\ge2}(-i)^{\ell-2}
   e_{\ell,M,N}w^{\ell-1}.}
 \tag{L-15138.6}
\]

Consequently, on every disk where the coefficient series converges,

\[
 \boxed{
 \frac{F_M^{\rm lin}(w)}{F_{M,N}^{\rm Ward}(w)}
 =\exp\!\left(
   \sum_{\ell\ge2}
   \frac{(-i)^{\ell-2}}{\ell}
   e_{\ell,M,N}w^{\ell}
  \right).}
 \tag{L-15138.7}
\]

### Proof

Subtract (L-15138.2) from (L-15138.1), use (L-15138.4), integrate from `0`
to `w`, and apply (L-15138.5). QED.

Equation (L-15138.7) is the exact result of redoing the target calculation with
the nonlinear Ward ledger. The Ward amendment preserves the original target if
and only if the exponent on the right tends locally uniformly to zero (or is
identically zero at the declared finite level).

## 3. The first genuine even discrepancy

Assume centered parity has already killed every odd trace/coefficient and that
the quadratic coefficient agrees. Then

\[
 \boxed{
 \log
 \frac{F_M^{\rm lin}(w)}{F_{M,N}^{\rm Ward}(w)}
 =-\frac14 e_{4,M,N}w^4+O(w^6).}
 \tag{L-15138.8}
\]

Equivalently,

\[
 \boxed{
 \frac{F_{M,N}^{\rm Ward}(w)}{F_M^{\rm lin}(w)}
 =1+\frac14e_{4,M,N}w^4+O(w^6).}
 \tag{L-15138.9}
\]

Here

\[
 \boxed{
 e_{4,M,N}
 =a_{4,M}^{\rm lin}
  -\operatorname{Tr}(K_{M,N}^{4})
 =q_{4,M,N}^{\rm Ward}-q_{4,M}^{\rm lin}.}
 \tag{L-15138.10}
\]

Therefore a nonzero quartic defect cannot be absorbed into the two exponential
normalization constants `a+bw`. It is the first invariant obstruction to target
preservation.

## 4. Exact Riemann quartic target

Put

\[
 E(w)=\frac{\xi(1/2+w)}{\xi(1/2)}.
 \tag{L-15138.11}
\]

If

\[
 \frac{E'(w)}{E(w)}
 =\sum_{\ell\ge2}(-i)^{\ell-2}
   \tau_\ell w^{\ell-1},
 \tag{L-15138.12}
\]

then the first even targets are

\[
 \boxed{\tau_2=\frac{\xi''(1/2)}{\xi(1/2)}}
 \tag{L-15138.13}
\]

and

\[
 \boxed{
 \tau_4
 =-\frac16\left[
  \frac{\xi^{(4)}(1/2)}{\xi(1/2)}
  -3\left(\frac{\xi''(1/2)}{\xi(1/2)}\right)^2
 \right].}
 \tag{L-15138.14}
\]

Thus the first proof-facing production gate is

\[
 \boxed{
 a_{4,M}^{\rm lin}\longrightarrow\tau_4,
 \qquad
 \operatorname{Tr}(K_{M,N}^{4})\longrightarrow\tau_4,}
 \tag{L-15138.15}
\]

or, equivalently,

\[
 \boxed{e_{4,M,N}\longrightarrow0.}
 \tag{L-15138.16}
\]

### Proof of (L-15138.14)

Write `E(w)=1+a w^2+b w^4+O(w^6)`, where

\[
 a=\frac{\xi''(1/2)}{2\xi(1/2)},
 \qquad
 b=\frac{\xi^{(4)}(1/2)}{24\xi(1/2)}.
\]

Then

\[
 \frac{E'}E=2aw+(4b-2a^2)w^3+O(w^5).
\]

Because the coefficient of `w^3` in (L-15138.12) is `-tau_4`, the displayed
formula follows. QED.

## 5. Why no hidden global cancellation remains

Let the finite classical explicit-formula total be

\[
 \mathcal G_M
 =\mathcal G_M^{\rm arch}
  +\mathcal G_M^{\rm arith}
  +\mathcal G_M^{\rm bdry}.
 \tag{L-15138.17}
\]

Every channel is linear in the test source. If the original regularized source
is

\[
 \Psi_M=\widetilde\Psi_M-C_M,
\]

then

\[
 \mathcal G_M(\Psi_M)
 =\mathcal G_M(\widetilde\Psi_M)
  -\mathcal G_M(C_M).
 \tag{L-15138.18}
\]

The complete channel-by-channel cancellation of the linear finite jet is already
contained in

\[
 q_{\ell,M}^{\rm lin}
 =[w^{\ell-1}]\mathcal G_M(C_M(h_{w,M})).
 \tag{L-15138.19}
\]

Replacing this number by `q_ell^Ward` changes the **total** ledger by
`e_ell`. There is no uncounted fourth classical channel in which the nonlinear
relative-determinant term can cancel later. Hence global target preservation is
exactly (L-15138.7), and the quartic global cancellation is exactly
`e_(4,M,N)=0` (or its limiting form).

## 6. Decomposition through the raw determinant ledger

Let

\[
 g_{A,M,N}(w)
 =\frac d{dw}\log\det{}_2(I+iwA_{M,N})
 \tag{L-15138.20}
\]

and define the raw target defect

\[
 \rho_{M,N}(w)
 :=g_M^{\rm lin}(w)-g_{A,M,N}(w).
 \tag{L-15138.21}
\]

Then the exact transgression splits as

\[
 \boxed{
 g_M^{\rm lin}(w)-g_{M,N}^{\rm Ward}(w)
 =\rho_{M,N}(w)
 +g_{A,M,N}(w)-g_{K,M,N}(w).}
 \tag{L-15138.22}
\]

This separates the two target-preservation obligations:

1. the classical one-contour ledger must match the **raw** cyclic determinant;
2. the actual finite-jet comparison map must be small enough, or satisfy an
   exact Ward equality, so that the raw and renormalized determinants agree in
   the limit.

The manuscript's stated convergence of the regularized test source and
pre-determinant continuity of its scalar functional do not, by themselves,
state either estimate in (L-15138.22) in Schatten norm.

## 7. Proof boundary

The target ratio, quartic coefficient, Riemann quartic target, and global-ledger
accounting are exact. This lemma does not prove that `e_(4,M,N)` vanishes for the
actual Riemann finite maps. The quantitative sufficient condition is given in
`T-15116`.
