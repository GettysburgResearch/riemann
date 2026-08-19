# L-99550 — The canonical continuum equality frame is doubly clamped at every activation

Claim ID: `L-99550`  
Status: **PROVED EXACT SOURCE-SPECIFIC VOLTERRA THEOREM**  
Created: 2026-08-19  
Depends on: `L-91106`, `L-91107`, and the distributional operator of `L-99230`  
RH status: **not assumed**

For `0<u<=1`, define

\[
F(u)=4(1-\sqrt u)+2\sqrt u\log u,
\tag{L-99550.1}
\]

and extend `F` by zero for `u>1`.  The canonical continuum equality seed is

\[
\boxed{
\mathscr B^\star(\theta)
 =\sum_{k\le1/\theta}\frac{\mu(k)}k F(k\theta),
 \qquad 0<\theta\le1.
}
\tag{L-99550.2}
\]

This is exactly `L-91106.3`, rewritten so that one activated Möbius colour is
visible.

## 1. Double clamping of one colour

Direct differentiation gives

\[
F(1)=0,
\qquad
F'(1-)=0.
\tag{L-99550.3}
\]

Therefore the colour

\[
\frac{\mu(k)}kF(k\theta)\mathbf1_{\theta\le1/k}
\]

has both zero value and zero first derivative when it enters at
`theta=1/k`.  Hence the complete seed is `C^1` across every reciprocal
activation knot:

\[
\boxed{
\mathscr B^\star(1/k+)=\mathscr B^\star(1/k-),
\qquad
(\mathscr B^\star)'(1/k+)=(\mathscr B^\star)'(1/k-).
}
\tag{L-99550.4}
\]

In particular, every activation atom from `L-99230.4` is exactly zero.

At the endpoint `theta=1`, only the `k=1` colour is active, and (L-99550.3)
gives

\[
\boxed{
\mathscr B^\star(1)=0,
\qquad
(\mathscr B^\star)'(1-)=0.
}
\tag{L-99550.5}
\]

## 2. Exact inverse density

Let

\[
(Vf)(\theta)=
\frac{2\theta^2f''(\theta)-\theta f'(\theta)+f(\theta)}
     {2\sqrt\theta}.
\tag{L-99550.6}
\]

For `0<u<1`, exact differentiation gives

\[
\boxed{VF(u)=\frac2{\sqrt u}-1.}
\tag{L-99550.7}
\]

Scaling `u=k theta` yields

\[
V_\theta\left[\frac1kF(k\theta)\right]
 =\frac1{\sqrt k}
   \left(\frac2{\sqrt{k\theta}}-1\right)
 =\frac2{k\sqrt\theta}-\frac1{\sqrt k}.
\tag{L-99550.8}
\]

Summing the active colours therefore gives

\[
\boxed{
V\mathscr B^\star(\theta)
 =2\theta^{-1/2}\sum_{k\le1/\theta}\frac{\mu(k)}k
  -\sum_{k\le1/\theta}\frac{\mu(k)}{\sqrt k}
 =L(1/\theta).
}
\tag{L-99550.9}
\]

No distributional atom must be added to (L-99550.9), because all derivative
jumps vanish by (L-99550.4).

## 3. Scope

This lemma is source-specific.  The generic nullspace and knot-atom theorem of
PR #638 remains correct for arbitrary piecewise-smooth data.  The present
result proves that the canonical equality frame used by the direct-integral
route lies in the doubly clamped subspace on which those generic boundary
coordinates vanish.
