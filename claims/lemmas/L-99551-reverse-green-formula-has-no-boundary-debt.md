# L-99551 — Reverse Volterra reconstruction has no knot or homogeneous debt for the canonical frame

Claim ID: `L-99551`  
Status: **PROVED EXACT GREEN-REPRESENTATION THEOREM**  
Created: 2026-08-19  
Depends on: `L-99230`, `L-99550`  
RH status: **not assumed**

For `0<x<=t<=1`, put

\[
K_-(x,t)=\frac{2(\sqrt{xt}-x)}{t^{3/2}}.
\tag{L-99551.1}
\]

It is nonnegative, vanishes at `x=t`, and its left derivative at the diagonal
is

\[
\partial_xK_-(t-,t)=-t^{-3/2}.
\tag{L-99551.2}
\]

After extending `K_-` by zero for `x>t`, the right-minus-left derivative jump
is `t^{-3/2}`.  Therefore

\[
V_xK_-(x,t)=\delta_t.
\tag{L-99551.3}
\]

## 1. Reverse Green formula

If `f'` has locally bounded variation on `(0,1]`, then

\[
\boxed{
f(x)=A\sqrt x+Bx+
\int_{[x,1)}K_-(x,t)\,d(Vf)(t),
}
\tag{L-99551.4}
\]

where

\[
A=2\bigl(f(1)-f'(1-)\bigr),
\qquad
B=2f'(1-)-f(1).
\tag{L-99551.5}
\]

This is the right-anchored analogue of `L-99230.2`.  It follows either by the
same Green-kernel argument or by applying `L-99230` on each compact reversed
interval and passing through the finite activation partition.

## 2. Application to the equality frame

By `L-99550`, the canonical seed satisfies

\[
f(1)=f'(1-)=0
\]

and has no derivative jumps.  Consequently

\[
A=B=0
\]

and `d(Vf)(t)=L(1/t)dt`.  Hence

\[
\boxed{
\mathscr B^\star(\theta)
 =\int_\theta^1
 \frac{2(\sqrt{\theta t}-\theta)}{t^{3/2}}
 L(1/t)\,dt.
}
\tag{L-99551.6}
\]

The identity is also colourwise exact.  For `k theta<=1`,

\[
\boxed{
\frac1kF(k\theta)
 =\int_\theta^{1/k}
 \frac{2(\sqrt{\theta t}-\theta)}{t^{3/2}}
 \left(\frac2{k\sqrt t}-\frac1{\sqrt k}\right)dt.
}
\tag{L-99551.7}
\]

Expanding the integrand into the powers `t^-2`, `t^-3/2`, and `t^-1`
recovers exactly

\[
\frac1k\left[4-4\sqrt{k\theta}
 +2\sqrt{k\theta}\log(k\theta)\right].
\]

## 3. Consequence for the live calibration ledger

For the canonical continuum equality-frame contribution, the Volterra part of
the signed fixed-row calibration discussed in `L-99240` has

```text
activation-knot contribution = 0;
homogeneous sqrt(theta) mode = 0;
homogeneous theta mode       = 0.
```

Thus the generic two-anchor cone test of PR #638 is not a live obligation for
this particular frame.  Hall-transformed fibres, the explicit anchored finite
block, finite/continuum quadrature, truncation, and ownership interfaces remain
separate unless they are independently identified with the same clamped frame.
