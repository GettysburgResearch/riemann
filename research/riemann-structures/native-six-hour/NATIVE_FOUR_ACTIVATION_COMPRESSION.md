# Four actual activations preserve the full H25 source

This proof-only corollary uses the actual occupation identity frozen at
`a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc`, specifically
`NATIVE_OCCUPATION_MOMENTS.md`. It introduces no numerical optimization or
new source. The convex-geometric reduction below is classical; the
conclusion about all63 native records uses that fixed source identity.

Let `(u,v,w)` be any continuous coordinatewise nondecreasing path from
`(0,0,0)` to `(1,1,1)`. Retain its oriented planar path `(u,v)`, including
vertical segments, and the six occupation moments

\[
 A=\int v\,du,\quad B=\int uv\,du,\quad C=\int v^2\,du,
 \quad D=\int w\,du,\quad E=\int uw\,du,\quad F=\int w\,dv.
\]

There is another continuous monotone three-coordinate path with exactly
the same oriented planar path, up to insertion of pauses, on which `w`
increases at at most four planar points and is constant elsewhere. This
new path has exactly the same six moments, all63 original H25 source
records, every physical coefficient formed from those records, and the
original H25 physical quadratic energy.

## 1. The three moments carried by the activation measure

Continuous bounded-variation integration by parts gives

\[
 D=1-\int u\,dw,\qquad
 E=\frac12-\frac12\int u^2\,dw,\qquad
 F=1-\int v\,dw.                                      \tag{1}
\]

The Stieltjes measure `dw` is a probability measure. Thus the vector

\[
 m=\left(\int u\,dw,\int u^2\,dw,\int v\,dw\right)
\]

belongs to the convex hull of the compact subset

\[
 K=\{(u(t),u(t)^2,v(t)):0\le t\le1\}\subset\mathbb R^3.
                                                               \tag{2}
\]

For completeness, membership in the convex hull, rather than just its
closure, follows without a measure-theoretic shortcut. Approximate the
continuous map in(2) uniformly by finitely many sample values on a
partition, weighted by the corresponding `dw` masses. Each finite convex
combination can be reduced to at most four terms: if more than four
positive weights remain, the augmented vectors `(1,k_i)` are linearly
dependent. Move the weights in that dependence until one first becomes
zero; positivity, their sum and the barycentre are unchanged. Repetition
leaves four terms. The set of all four-term combinations is the image of
the compact set `K^4` times the closed four-weight simplex, so is closed.
The limiting integral therefore also has such a representation.

Consequently there are planar points visited at times `t_1,...,t_r`,
`r<=4`, and nonnegative weights `lambda_i` with sum1 such that

\[
 m=\sum_{i=1}^r\lambda_i
       (u(t_i),u(t_i)^2,v(t_i)).                         \tag{3}
\]

Zero weights may be dropped, repeated planar points combined, and the
remaining points put in their original path order. No uniqueness is
asserted, and no smaller bound is needed here.

## 2. Realize the atomic measure by one actual continuous path

Traverse the original planar path in order. At its `i`th selected point,
pause `(u,v)` and increase `w` continuously by `lambda_i`; between these
pauses leave `w` constant. The pauses are genuine vertical segments of
the new path, not discontinuities of a coordinate and not a convex
mixture of different source fields. The construction also permits an
activation at the initial or final planar point. A reparameterization
places all original subpaths and these finitely many segments in a
compact parameter interval.

The new path is continuous and coordinatewise nondecreasing with the
same endpoints. Its activation measure has the barycentre(3), so(1)
proves that `D,E,F` are unchanged. Its oriented planar projection is
unchanged, so `A,B,C` are unchanged as well. Planar pauses contribute
nothing to the integrals against `du` and `dv`.

The frozen occupation theorem identifies the complete actual source
vector as an affine function of `(A,B,C/2,D,E,F)`. Applying that identity
to the old and new actual paths proves equality of all63 records. The
physical collection sums, weights and energy are then identical because
they are the same fixed operations on identical source records.

## 3. Scope

This is an exact source compression theorem for the H25 continuous
monotone category. The planar path can retain arbitrary bounded-variation
complexity; the theorem bounds only the number of `w` activations. It
does not bound the total number of planar segments by seven, the cap used
in the separate finite replay, and does not claim a finite rational
algorithm for an arbitrary nonpolygonal input.

The single-activation linear-support theorem and this four-activation
source-preserving theorem serve different purposes. A signed linear
functional can be improved by putting all activation mass at a suitable
point. Preserving the entire native source generally requires preserving
three activation moments at once. There is no claim that one activation
attains the physical quadratic minimum, or that an arbitrary point in
the convex hull of different planar paths is realized by this argument.

No all-height or full retained-gamma source identification is supplied.
No new replay or scientific computation is required for this corollary.
