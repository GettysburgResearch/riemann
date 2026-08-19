# L-99230 — Exact distributional Green formula for the factor-67 endpoint inverse

Claim ID: `L-99230`  
Status: **PROVED EXACT DISTRIBUTIONAL THEOREM**  
Created: 2026-08-19  
Frozen parent: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
RH status: **unproved**

For a function whose derivative has locally bounded variation on `[a,infinity)`,
define the distributional measure

\[
d(Vf)(x)
=
\frac{2x^2\,d f'(x)-xf'(x)\,dx+f(x)\,dx}
     {2\sqrt x}.
\tag{L-99230.1}
\]

Then, for every `x>=a`,

\[
\boxed{
f(x)
=
A_a\sqrt x+B_ax
+
\int_{(a,x]}
\frac{2(x-\sqrt{xt})}{t^{3/2}}\,d(Vf)(t),
}
\tag{L-99230.2}
\]

where

\[
\boxed{
A_a=\frac{2(f(a)-af'(a+))}{\sqrt a},
\qquad
B_a=2f'(a+)-\frac{f(a)}a.
}
\tag{L-99230.3}
\]

## Proof

The homogeneous equation

\[
2x^2f''-xf'+f=0
\]

has basis `sqrt(x),x`. Put

\[
K(x,t)
=
\mathbf 1_{x\ge t}
\frac{2(x-\sqrt{xt})}{t^{3/2}}.
\]

The kernel is continuous at `x=t`, its right-minus-left derivative jump is
`t^{-3/2}`, and therefore

\[
V_xK(x,t)=\delta_t.
\]

The integral in (L-99230.2) is a particular solution. The two boundary
conditions at `a` determine (L-99230.3).

## Activation-knot atoms

If `f'` jumps at an activation knot `t`, then

\[
\boxed{
d(Vf)(\{t\})
=
t^{3/2}\bigl(f'(t+)-f'(t-)\bigr).
}
\tag{L-99230.4}
\]

Thus a smooth-cell density audit omits exactly the derivative-jump atoms unless
they are entered separately.

## Nullspace

\[
\boxed{\ker V=\operatorname{span}\{\sqrt x,x\}.}
\tag{L-99230.5}
\]

Consequently the open-cell inverse density does not determine the complete
equality frame or its score normalization.
