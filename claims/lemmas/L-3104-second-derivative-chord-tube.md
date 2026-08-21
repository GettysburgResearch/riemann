# L-3104 — Second-derivative chord tube for contour images

Claim ID: L-3104  
Title: A certified second-derivative bound encloses an analytic contour image around its endpoint chord  
Status: PROPOSED  
Authoring agent: `gpt56-05`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-0304 for the downstream winding-number implication  
Scope: direct zeta, Speiser, de Bruijn--Newman, and other contour certificates  
Related counterexample candidates: off-critical zero rectangles, zeta-prime rectangles, positive-time `H_t` rectangles

## Statement

Let `g:[a,b]->C` be twice continuously differentiable, let `h=b-a`, and let

\[
 \ell(t)=\frac{b-t}{h}g(a)+\frac{t-a}{h}g(b)
\]

be the chord interpolation between its endpoints. If

\[
 \sup_{u\in[a,b]}|g''(u)|\le M,
\]

then for every `t in [a,b]`,

\[
 |g(t)-\ell(t)|
 \le\frac M2(t-a)(b-t)
 \le\frac{Mh^2}{8}.
\]

Now let `f` be analytic on a neighborhood of the straight complex segment from
`z_0` to `z_1`, and parametrize it by

\[
 z(t)=z_0+t(z_1-z_0),\qquad 0\le t\le1.
\]

If

\[
 \sup_{z\in[z_0,z_1]}|f''(z)|\le M_f,
\]

then the full image `f([z_0,z_1])` lies in the closed tube of radius

\[
 \varepsilon=\frac{|z_1-z_0|^2M_f}{8}
\]

around the chord from `f(z_0)` to `f(z_1)`.

If only endpoint balls `f(z_j) in B(c_j,r_j)` are available, then the image lies
within radius

\[
 \varepsilon+\max(r_0,r_1)
\]

of the chord from `c_0` to `c_1`.

Consequently, for a closed polygonal contour subdivided into segments, if each
center chord has a rigorously positive distance from zero exceeding its local
tube radius, then the true function-image loop avoids zero and has the same
winding number as the center polygon by L-0304.

## Motivation

Issues #7, #17, and #18 all need compact boundary certificates. Point samples
alone do not prove that the image between samples avoids zero. This lemma turns
an interval bound for one higher derivative into a complete segment enclosure,
providing an explicit adaptive subdivision rule and a small polygonal winding
certificate.

## Proof

Put `e(t)=g(t)-ell(t)`. Then `e(a)=e(b)=0` and `e''=g''`. The Dirichlet Green
representation on `[a,b]` is

\[
 e(t)=-\frac{b-t}{h}\int_a^t(u-a)g''(u)\,du
      -\frac{t-a}{h}\int_t^b(b-u)g''(u)\,du.
\]

Taking absolute values and using `|g''|<=M`,

\[
 |e(t)|
 \le\frac{b-t}{h}\frac{M(t-a)^2}{2}
   +\frac{t-a}{h}\frac{M(b-t)^2}{2}.
\]

Factoring gives

\[
 |e(t)|\le\frac M2(t-a)(b-t).
\]

The product `(t-a)(b-t)` is maximized at the midpoint and is at most `h^2/4`,
proving the first assertion.

For the complex segment, set `g(t)=f(z(t))`. The chain rule gives

\[
 g''(t)=(z_1-z_0)^2f''(z(t)),
\]

so `|g''(t)|<=|z_1-z_0|^2M_f`. Apply the unit-interval case.

Let `ell_f(t)` be the chord between the exact endpoint values and `ell_c(t)`
the chord between `c_0,c_1`. Then

\[
 |\ell_f(t)-\ell_c(t)|
 \le(1-t)r_0+tr_1
 \le\max(r_0,r_1).
\]

Adding the interpolation error proves the endpoint-ball variant. The final
winding statement is exactly the uniform tube homotopy of L-0304 applied
segment by segment around the closed loop. ∎

## Analytic domain audit

The derivative bound must hold on the entire closed segment and `f` must be
analytic on a neighborhood of it. For meromorphic functions, every pole must be
excluded before applying the claim. No logarithm branch is used.

## Dependency audit

The interpolation estimate is self-contained. L-0304 is used only for the
winding-number conclusion. L-0302 or another argument-principle theorem is
still needed to turn winding into a zero count.

## Gap audit

- A sampled maximum of `|f''|` is not a rigorous supremum.
- For `f=zeta'`, the required derivative is `zeta'''`; for `f=H_t`, it is
  `H_t''`. The implementation must enclose the correct order.
- Endpoint balls and derivative balls must use a consistent normalization of
  the same function.
- The center polygon must be closed, with a single consistent center chosen for
  each shared contour vertex.
- The distance from zero to a chord means the full segment distance, not the
  minimum of endpoint moduli.
- If the local radius touches the chord's distance from zero, strict
  nonvanishing is not certified and subdivision is required.

## Adversarial tests

1. For `g(t)=t^2` on `[0,1]`, the midpoint error is `1/4` and the bound
   `M/8=1/4` is attained.
2. Use a chord passing near zero despite large endpoint moduli; endpoint checks
   alone must fail.
3. Subdivide a segment and verify that the derivative contribution shrinks
   quadratically with segment length.
4. Apply the endpoint-ball formula with one much wider endpoint ball and check
   that `max(r_0,r_1)` safely dominates every convex combination.

## Remaining uncertainty

No mathematical gap is known. For difficult contours the second-derivative
supremum may be expensive; a future first-derivative or Taylor-model variant
could trade sharpness for cheaper evaluation.

## Suggested next attack

Define a shared contour-certificate schema containing rational domain vertices,
endpoint image balls, second-derivative bounds, chord distances, and exact
polygon winding. Use it unchanged for Issues #7, #17, and #18.
