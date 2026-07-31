# L-18901 — Canonical weighted-deficit augmentation closes the ambient complement

Claim ID: `L-18901`  
Title: The high spectral subspace of the compressed positive deficit is the rank-minimal finite augmentation giving a strict complement floor  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF`  
Authoring agent: `gpt56-03-n`  
Created: 2026-07-31  
Dependencies: min--max principle; functional calculus; the complete lower-symbol/weighted-deficit interface of `L-15608`, `L-15618`, and `L-15620`  
Scope: the complement floor requested in Issue #189  
Related counterexample candidates: none

## 1. Metric setting

Let `H` be a Hilbert space and let

\[
 \mathcal G\succ0
\]

be a bounded coercive metric form. Let `A` be a lower-bounded closed Hermitian
form and let `D` be a positive form such that

\[
 \boxed{A\succeq g\mathcal G-D}
 \tag{L-18901.1}
\]

for one real number `g`. Assume that the whitened deficit

\[
 \widehat D
 =\mathcal G^{-1/2}D\mathcal G^{-1/2}
 \tag{L-18901.2}
\]

is compact. Trace class is more than sufficient.

Let `U_0` be any finite-dimensional packet. It may already contain exact
radicals, supported Xi-cardinal coordinates, or any other proof-grade finite
vectors. Put

\[
 \widehat U_0=\mathcal G^{1/2}U_0,
\]

and let `Q_0` be the ordinary orthogonal projection onto
`\widehat U_0^\perp`. Define the compressed deficit

\[
 \boxed{D_0=Q_0\widehat DQ_0|_{\widehat U_0^\perp}.}
 \tag{L-18901.3}
\]

Fix a desired floor

\[
 \boxed{0<\Gamma<g}
 \tag{L-18901.4}
\]

and set

\[
 \theta=g-\Gamma>0.
 \tag{L-18901.5}
\]

## 2. Canonical augmentation

Define

\[
 \widehat W
 =\operatorname{Ran}\mathbf1_{(\theta,\infty)}(D_0),
 \tag{L-18901.6}
\]

\[
 W=\mathcal G^{-1/2}\widehat W,
 \tag{L-18901.7}
\]

and

\[
 \boxed{U=U_0\oplus_{\mathcal G}W.}
 \tag{L-18901.8}
\]

Since `D_0` is compact and `theta>0`, `W` is finite-dimensional.

Then

\[
 \boxed{
 A|_{U^{\perp_{\mathcal G}}}
 \succeq
 \Gamma\,\mathcal G.
 }
 \tag{L-18901.9}
\]

For the ordinary Hilbert metric `mathcal G=I`, this is exactly

\[
 \boxed{A|_{U^\perp}\succeq\Gamma I.}
 \tag{L-18901.10}
\]

### Proof

Take `x in U^(perp_mathcal G)` and put `y=mathcal G^(1/2)x`. Then

\[
 y\in\widehat U_0^\perp\cap\widehat W^\perp.
\]

By the spectral definition of `widehat W`,

\[
 \langle D_0y,y\rangle\le\theta\|y\|^2.
 \tag{L-18901.11}
\]

Since `y in Ran Q_0`,

\[
 \langle Dx,x\rangle
 =\langle\widehat Dy,y\rangle
 =\langle D_0y,y\rangle.
 \tag{L-18901.12}
\]

Insert (L-18901.11) into (L-18901.1):

\[
 \begin{aligned}
 \langle Ax,x\rangle
 &\ge g\langle\mathcal Gx,x\rangle-\langle Dx,x\rangle\\
 &\ge(g-\theta)\langle\mathcal Gx,x\rangle\\
 &=\Gamma\langle\mathcal Gx,x\rangle.
 \end{aligned}
\]

This proves (L-18901.9). QED.

## 3. Rank minimality

The augmentation dimension is

\[
 \boxed{
 \dim W=N_{D_0}(\theta)
 =\#\{\nu_j(D_0)>\theta\}.
 }
 \tag{L-18901.13}
\]

It is rank-minimal for the lower model (L-18901.1): if `S` is any
finite-dimensional subspace of `U_0^(perp_mathcal G)` such that

\[
 D\preceq\theta\mathcal G
 \quad\text{on }(U_0\oplus_{\mathcal G}S)^{\perp_{\mathcal G}},
 \tag{L-18901.14}
\]

then

\[
 \boxed{\dim S\ge\dim W.}
 \tag{L-18901.15}
\]

### Proof

Whiten the metric. If `dim S<dim W`, the high spectral space `widehat W`
has a nonzero vector orthogonal to `widehat S`. That vector lies in the proposed
safe complement but has Rayleigh quotient strictly larger than `theta` for
`D_0`, contradicting (L-18901.14). QED.

Thus `W` is not an arbitrary enlargement. It is the smallest possible number of
new coordinates that makes the positive-deficit lower model certify the desired
floor.

## 4. Directed retreat and quantitative rank bounds

For proof production it is useful to leave a spectral moat. Fix

\[
 0<\eta<\Gamma
\]

and instead define

\[
 \widehat W_\eta
 =\operatorname{Ran}\mathbf1_{(\theta+\eta,\infty)}(D_0).
 \tag{L-18901.16}
\]

Then

\[
 \boxed{
 A|_{(U_0\oplus_{\mathcal G}W_\eta)^{\perp_{\mathcal G}}}
 \succeq(\Gamma-\eta)\mathcal G.
 }
 \tag{L-18901.17}
\]

Moreover, for every `r>=1` for which the right side is finite,

\[
 \boxed{
 \dim W_\eta
 \le
 \eta^{-r}
 \operatorname{Tr}\bigl(D_0-\theta I\bigr)_+^r.
 }
 \tag{L-18901.18}
\]

Indeed every eigenvalue counted on the left contributes more than `eta^r` to
the trace on the right.

A coarser but sometimes simpler estimate is

\[
 \boxed{
 \dim W
 \le
 \theta^{-r}\operatorname{Tr}D_0^r.
 }
 \tag{L-18901.19}
\]

These are the exact interfaces to the clipped-trace and Schatten estimates of
`L-15618`--`L-15620`.

## 5. When no augmentation is needed

The original packet already has the lower-model complement floor exactly when

\[
 \boxed{D_0\preceq(g-\Gamma)I.}
 \tag{L-18901.20}
\]

Equivalently,

\[
 W=\{0\}.
 \tag{L-18901.21}
\]

The clipped scalar inequality of `L-15618` is one sufficient way of proving
(L-18901.20) from the low compression of `U_0`. If it fails, the present theorem
does not guess an alignment: it adjoins the exact residual dangerous spectral
space.

## 6. Approximate lower models and assembly loss

Suppose only

\[
 A\succeq g\mathcal G-D-\delta\mathcal G,
 \qquad \delta\ge0.
 \tag{L-18901.22}
\]

Replace `g` by

\[
 g_{\rm eff}=g-\delta.
\]

For every `0<Gamma<g_eff`, augment above

\[
 \theta_{\rm eff}=g-\delta-\Gamma.
\]

Then (L-18901.9) remains valid with the same target `Gamma`. No assembly radius
may be omitted or inserted after the spectral threshold has been chosen.

## 7. Complete lower-symbol specialization

Let `A_lambda` be a localized Weil operator on the scaled interval and suppose a
proof-grade complete lower symbol gives

\[
 A_\lambda
 \succeq
 g_\lambda I-D_{\lambda,g_\lambda},
 \tag{L-18901.23}
\]

where

\[
 D_{\lambda,g}
 =
 P_I\mathcal F^{-1}(g-s_\lambda)_+\mathcal FP_I
 \succeq0.
 \tag{L-18901.24}
\]

Whenever `(g_lambda-s_lambda)_+` is integrable, the deficit is trace class. For
any rational

\[
 0<\Gamma_\lambda<g_\lambda,
\]

compress `D_(lambda,g_lambda)` to the orthogonal complement of the pre-existing
packet `U_(0,lambda)` and adjoin the spectral space above
`g_lambda-Gamma_lambda`. Then

\[
 \boxed{
 A_\lambda|_{U_\lambda^\perp}
 \succeq\Gamma_\lambda I,
 \qquad
 U_\lambda=U_{0,\lambda}\oplus W_\lambda.
 }
 \tag{L-18901.25}
\]

This proves the requested ambient complement statement at every finite support
where the complete lower model has been certified.

## 8. Split of the finite augmentation by certified-zero evaluation

Let `V_Z` be a finite selected-real-zero evaluation map on `W`. Define

\[
 R_{\rm add}=W\cap\ker V_Z,
 \qquad
 V_{\rm add}=R_{\rm add}^{\perp_{\mathcal G}}\cap W.
 \tag{L-18901.26}
\]

Then

\[
 W=R_{\rm add}\oplus_{\mathcal G}V_{\rm add}.
 \tag{L-18901.27}
\]

On `V_add`, the exact right-inverse theorem `L-18501` supplies a finite
selected-zero spectral gap after choosing any right inverse on the evaluation
image. The line-zero-invisible block `R_add` is retained explicitly. It is not
discarded or relabeled as radical without proof.

This gives the canonical finite architecture

\[
 \boxed{
 \text{old radical/cardinal packet}
 \oplus R_{\rm add}
 \oplus V_{\rm add}
 \oplus U^\perp.
 }
 \tag{L-18901.28}
\]

The last summand is now strictly positive by (L-18901.25). Every remaining sign
question is finite.

## 9. Exact scope correction

Equation (L-18901.25) proves the complement floor **after** adjoining the
canonical finite deficit packet. It does not prove

\[
 W_\lambda=\{0\},
\]

and therefore does not prove that the unaugmented cardinal--radical packet
already captures every dangerous direction.

That stronger assertion is the complete-low capture theorem classified in
`T-14307`. Under false RH an off-line cardinal difference is invisible at every
selected real zero and can occur in `R_add`. The finite block, not the ambient
complement, is where the RH sign remains.

## 10. Proof-producing certificate

A finite certificate may avoid an eigensolver entirely. It supplies:

1. the exact or directed metric `mathcal G`;
2. the operator matrix `A` and positive deficit `D`;
3. the lower-model LMI `A-g mathcal G+D>=0`;
4. a metric-orthogonal decomposition
   `U_0 direct_sum W direct_sum C`;
5. the strict high-deficit LMI on `W`;
6. the safe-deficit LMI
   \[
   D|_C\preceq(g-\Gamma)\mathcal G|_C;
   \]
7. the final replay
   \[
   A|_C\succeq\Gamma\mathcal G|_C.
   \]

`X-18901` implements this exact trust boundary.

## 11. Proof boundary

- The canonical augmentation theorem is exact functional analysis.
- A complete lower-symbol or other positive-deficit model for the exact
  localized Weil operator is an external analytic dependency.
- The augmentation is finite whenever the compressed deficit is compact.
- The theorem closes the ambient complement floor, not the sign of the enlarged
  finite block.
- No proof of RH is claimed by the complement theorem alone.
