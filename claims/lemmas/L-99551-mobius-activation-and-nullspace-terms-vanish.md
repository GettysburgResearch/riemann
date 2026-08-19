# L-99551 — Every Möbius activation knot and both Volterra boundary modes vanish

Claim ID: `L-99551`  
Status: **PROVED EXACT DISTRIBUTIONAL CONSEQUENCE**  
Created: 2026-08-19  
Depends on: `L-99230`, `L-99550`  
RH status: **unproved**

Let

\[
f_\mu(x)=\sum_{n\le x}\mu(n)\Phi(x/n),
\tag{L-99551.1}
\]

where \(\Phi\) is the zero-extended atom of `L-99550`.

## 1. Scaling of the inverse

For \(y=x/n\),

\[
V_x[\Phi(x/n)]
=
\frac1{\sqrt n}V_y\Phi(y).
\tag{L-99551.2}
\]

Hence, away from activation knots,

\[
\begin{aligned}
V_xf_\mu(x)
&=
\sum_{n\le x}
\frac{\mu(n)}{\sqrt n}
\left(2\sqrt{x/n}-1\right)\\
&=
\boxed{
2\sqrt x\sum_{n\le x}\frac{\mu(n)}n
-
\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
}
\end{aligned}
\tag{L-99551.3}
\]

Denote the last expression by \(L(x)\).

## 2. Activation atoms are zero

At \(x=n\), the entering colour is \(\mu(n)\Phi(x/n)\). Since

\[
\Phi(1)=0,
\qquad
\Phi'(1+)=0,
\tag{L-99551.4}
\]

the one-sided values satisfy

\[
f_\mu(n+)=f_\mu(n-),
\qquad
f_\mu'(n+)=f_\mu'(n-).
\tag{L-99551.5}
\]

PR #638 identifies the distributional activation mass as

\[
n^{3/2}\bigl(f_\mu'(n+)-f_\mu'(n-)\bigr).
\tag{L-99551.6}
\]

Therefore

\[
\boxed{
d(Vf_\mu)(\{n\})=0
\qquad(n\ge1).
}
\tag{L-99551.7}
\]

No separate knot ledger is required for this frame.

## 3. Lower boundary modes are zero

At the lower endpoint,

\[
f_\mu(1)=0,
\qquad
f_\mu'(1+)=0.
\tag{L-99551.8}
\]

The exact coefficients in `L-99230` are therefore

\[
A_1
=
2\bigl(f_\mu(1)-f_\mu'(1+)\bigr)
=
0,
\tag{L-99551.9}
\]

and

\[
B_1
=
2f_\mu'(1+)-f_\mu(1)
=
0.
\tag{L-99551.10}
\]

Thus the complete distributional Green formula is

\[
\boxed{
f_\mu(X)
=
\int_1^X
\frac{2(X-\sqrt{Xt})}{t^{3/2}}
L(t)\,dt.
}
\tag{L-99551.11}
\]

There is no hidden \(\sqrt X\) term, no hidden \(X\) term, and no atomic
activation correction.

## 4. Physical endpoint compatibility

The parabolic endpoint packet used in the direct-integral route is

\[
b_X(t)
=
2\sqrt t\log(X/t)-4\sqrt t+\frac{4t}{\sqrt X}.
\tag{L-99551.12}
\]

At its activation point \(X=t\),

\[
b_t(t)=0,
\tag{L-99551.13}
\]

and

\[
\left.\partial_Xb_X(t)\right|_{X=t}
=
\frac{2}{\sqrt t}-\frac{2}{\sqrt t}
=
0.
\tag{L-99551.14}
\]

The same double-clamping convention is therefore present in the physical
endpoint packet itself.

## Boundary

This lemma proves the distributional boundary cancellation for the explicit
frame (L-99551.1). It does not independently replay the downstream Hall,
capacity, terminal, or Mellin campaigns.
