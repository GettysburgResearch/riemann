# T-18901 — Canonical finite augmentation proves the positive ambient complement

Claim ID: `T-18901`  
Title: The cardinal–radical packet plus the residual weighted-deficit eigenspace has an exact strictly positive complement  
Status: `PROPOSED — COMPLETE COMPOSITION RELATIVE TO THE COMPLETE LOWER MODEL`  
Authoring agent: `gpt56-03-n`  
Created: 2026-07-31  
Dependencies: `L-18901`; `L-18501`; `T-14306`; the complete lower-symbol interface of `L-14316/L-15608/L-15620`  
Scope: the boxed complement floor in Issue #189

## 1. Initial structured packet

At support `lambda`, let

\[
 U_{0,\lambda}
\]

be any finite proof-grade structured packet. For the current positive route it
may be the exact finite-section cardinal–radical packet of `T-14306` and
`T-18501`.

No completeness assumption is made about `U_(0,lambda)`.

## 2. Complete positive-deficit lower model

Assume the exact localized Weil operator has a source-bound lower model

\[
 \boxed{
 A_\lambda
 \succeq
 g_\lambda I-D_\lambda,
 \qquad
 D_\lambda\succeq0,
 }
 \tag{T-18901.1}
\]

where `D_lambda` is compact. The weighted lower-symbol construction gives the
canonical example

\[
 D_\lambda
 =
 P_{I_\lambda}\mathcal F^{-1}
 (g_\lambda-s_\lambda)_+
 \mathcal FP_{I_\lambda}.
 \tag{T-18901.2}
\]

Every symbol and assembly loss must be inserted into the lower model before
forming `D_lambda`.

Choose any proof-grade rational floor

\[
 \boxed{0<\Gamma_\lambda<g_\lambda.}
 \tag{T-18901.3}
\]

Let `Q_(0,lambda)` be the orthogonal projection onto
`U_(0,lambda)^perp`, and put

\[
 D_{0,\lambda}
 =
 Q_{0,\lambda}D_\lambda Q_{0,\lambda}
 |_{U_{0,\lambda}^{\perp}}.
 \tag{T-18901.4}
\]

## 3. Exact residual capture packet

Define

\[
 \boxed{
 W_\lambda
 =
 \operatorname{Ran}
 \mathbf1_{(g_\lambda-\Gamma_\lambda,\infty)}
 (D_{0,\lambda})
 }
 \tag{T-18901.5}
\]

and

\[
 \boxed{
 U_\lambda
 =
 U_{0,\lambda}\oplus W_\lambda.
 }
 \tag{T-18901.6}
\]

The augmentation is finite and has exact rank

\[
 \boxed{
 \dim W_\lambda
 =
 N_{D_{0,\lambda}}
 (g_\lambda-\Gamma_\lambda).
 }
 \tag{T-18901.7}
\]

`L-18901` gives immediately

\[
 \boxed{
 A_\lambda|_{U_\lambda^\perp}
 \succeq
 \Gamma_\lambda I,
 \qquad
 \Gamma_\lambda>0.
 }
 \tag{T-18901.8}
\]

This is the requested statement.

## 4. Why no arithmetic asymptotic is needed for existence

The clipped-trace and phase-space inequalities of `L-15618`--`L-15620` are
needed only if one insists that the initial packet already captures the entire
deficit and hence that `W_lambda=0`.

For the existence of a finite complete packet with a positive complement, no
such asymptotic is needed. Compactness of `D_lambda` and positivity of
`g_lambda-Gamma_lambda` make (T-18901.5) finite at each support.

Thus the logically correct alternatives are:

\[
 \begin{array}{ll}
 \text{no-augmentation route:}
 &D_{0,\lambda}\preceq
  (g_\lambda-\Gamma_\lambda)I,\\[1mm]
 \text{canonical-augmentation route:}
 &U_\lambda=U_{0,\lambda}\oplus W_\lambda.
 \end{array}
 \tag{T-18901.9}
\]

The second route always closes the ambient complement under the complete lower
model.

## 5. Metric and directed version

If the finite packet uses a positive metric `mathcal G_lambda`, whiten by that
metric and define `W_lambda` from

\[
 \mathcal G_\lambda^{-1/2}
 Q_{0,\lambda}D_\lambda Q_{0,\lambda}
 \mathcal G_\lambda^{-1/2}.
 \tag{T-18901.10}
\]

Then

\[
 \boxed{
 A_\lambda|_{U_\lambda^{\perp_{\mathcal G}}}
 \succeq
 \Gamma_\lambda\mathcal G_\lambda.
 }
 \tag{T-18901.11}
\]

With an assembly loss `delta_lambda`, replace `g_lambda` by
`g_lambda-delta_lambda` before choosing the threshold.

A directed finite certificate need not compute a spectral projector. It may
freeze rational bases `U_0,W,C` and prove

\[
 C^*D_\lambda C
 \preceq
 (g_\lambda-\Gamma_\lambda)C^*C.
 \tag{T-18901.12}
\]

This is exactly what `X-18901` checks.

## 6. Canonical finite split after ambient capture

Let `V_(Z,lambda)` be the selected-real-zero evaluation map on the added packet.
Put

\[
 R_{{\rm add},\lambda}
 =
 W_\lambda\cap\ker V_{Z,\lambda},
 \tag{T-18901.13}
\]

\[
 V_{{\rm add},\lambda}
 =
 R_{{\rm add},\lambda}^{\perp}
 \cap W_\lambda.
 \tag{T-18901.14}
\]

Then

\[
 W_\lambda
 =
 R_{{\rm add},\lambda}
 \oplus
 V_{{\rm add},\lambda}.
 \tag{T-18901.15}
\]

The exact right-inverse theorem `L-18501` applies on the evaluation-visible
summand. The selected-zero-invisible summand is retained as a finite block.

Accordingly the complete decomposition is

\[
 \boxed{
 \mathcal H_\lambda
 =
 \bigl[
 R_{{\rm old},\lambda}
 \oplus R_{{\rm add},\lambda}
 \bigr]
 \oplus
 \bigl[
 V_{{\rm old},\lambda}
 \oplus V_{{\rm add},\lambda}
 \bigr]
 \oplus
 U_\lambda^\perp.
 }
 \tag{T-18901.16}
\]

The final summand has the strict floor (T-18901.8).

## 7. Cofinal sequence

Choose any unbounded support sequence on which the complete lower model is
available. At every level choose a positive target
`Gamma_j<g_j`, form the finite augmentation (T-18901.5), and use arbitrarily
strong directed precision to certify its safe complement.

Then

\[
 \boxed{
 A_{\lambda_j}|_{U_{\lambda_j}^\perp}
 \succeq
 \Gamma_jI>0
 }
 \tag{T-18901.17}
\]

at every retained level. No uniform rank bound is required for this statement;
every level is finite.

A retreat version may use `Gamma_j-eta_j` with `eta_j<Gamma_j` and the
quantitative rank bounds of `L-18901.18`.

## 8. What remains for RH

The complement floor is no longer the unresolved theorem once the canonical
finite augmentation is admitted.

The remaining sign is confined to the enlarged finite block. After eliminating
the now-positive ambient complement and the selected-zero-visible coordinates,
the precise unresolved block is the selected-real-zero kernel

\[
 R_{{\rm old},\lambda}
 \oplus R_{{\rm add},\lambda}.
 \tag{T-18901.18}
\]

A sufficient cofinal statement is

\[
 \boxed{
 \lambda_{\min}
 \left(
 B_{{\rm ker},\lambda}
 -
 Z_{{\rm ker},\lambda}^*
 C_\lambda^{-1}
 Z_{{\rm ker},\lambda}
 \right)
 \ge-\varepsilon_\lambda,
 \qquad
 \varepsilon_\lambda\to0.
 }
 \tag{T-18901.19}
\]

For the old exact radical packet this is supplied by the radical-tail theorems.
For the newly added line-zero-invisible packet it is precisely the complete-low
kernel/capture statement classified by `T-14307`.

Under false RH an off-line cardinal difference can occur in this finite kernel
and has strictly negative Weil value. Therefore (T-18901.19), not the ambient
floor (T-18901.8), carries the remaining RH content.

## 9. Proof boundary

- Equations (T-18901.5)--(T-18901.8) are exact.
- The complete lower model and compactness of its positive deficit are external
  source-bound gates already isolated in the symbol stack.
- The theorem permits finite augmentation; it does not prove the stronger claim
  `W_lambda=0`.
- The ambient complement is closed, while the enlarged finite kernel remains
  the final sign problem.
- No proof of RH is claimed without (T-18901.19).
