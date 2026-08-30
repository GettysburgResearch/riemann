# PFR-T6 — Hardy-flower turning and curvature-defect ledger

Status: **AUTHOR-PROVED EXACT GEOMETRIC THEOREM / REVIEW PENDING**

Scope: fixed-sign angular petals with simple endpoint zeros; Hardy specialization requires `vartheta'>0`. RH remains unproved.

## 1. Angular Hardy petals have a universal turning law

Let

\[
\Gamma(\phi)=r(\phi)e^{-i\phi},
\qquad \alpha\leq \phi\leq\beta,
\tag{1.1}
\]

where

- `r` is real and `C^2` on `(alpha,beta)`;
- `r` has one fixed nonzero sign on `(alpha,beta)`;
- `r(alpha)=r(beta)=0`;
- the endpoint zeros are simple.

Put

\[
L=\beta-\alpha>0.
\tag{1.2}
\]

For a Hardy petal, `phi=vartheta(t)` and

\[
r(\phi)=Z(t(\phi)).
\]

### PFR-T6A — exact regularity and self-intersection threshold

The open petal is regular.  Indeed,

\[
\Gamma'(\phi)=e^{-i\phi}(r'(\phi)-ir(\phi)),
\tag{1.3}
\]

and the two real quantities `r` and `r'` cannot vanish simultaneously in the
open nodal interval.

For two nonzero points of the petal,

\[
\Gamma(\phi_1)=\Gamma(\phi_2)
\]

holds if and only if

\[
\phi_2-\phi_1=2\pi k
\quad\hbox{and}\quad
r(\phi_2)=r(\phi_1)
\tag{1.4}
\]

for a nonzero integer `k`.

Consequently,

\[
\boxed{
\Gamma\text{ is simple away from its common endpoint}
\quad\Longleftrightarrow\quad
L\leq2\pi.
}
\tag{1.5}
\]

More quantitatively, for every positive integer `k` satisfying

\[
2\pi k<L,
\]

there exists a parameter `phi` with

\[
\boxed{
r(\phi)=r(\phi+2\pi k),}
\tag{1.6}
\]

so the petal has a self-intersection in that full-turn lag class.

#### Proof

Because `r(phi_1)/r(phi_2)` is positive, equality of the two complex values in
(1.4) forces `exp(-i(phi_1-phi_2))` to be positive and equal to one.  This gives
(1.4), and no such pair exists when `L<=2 pi`.

For the converse, fix `k` with `2 pi k<L` and consider

\[
F_k(\phi)=r(\phi)-r(\phi+2\pi k)
\]

on `[alpha,beta-2 pi k]`.  If `r>0` in the open interval, then

\[
F_k(\alpha)<0,
\qquad
F_k(\beta-2\pi k)>0.
\]

The signs reverse together when `r<0`.  The intermediate value theorem gives
(1.6).

Thus a visibly simple Hardy petal has a hard angular ceiling of one full turn;
a petal spanning more than one full rotation must cross itself.

---

## 2. The open-arc signed curvature is independent of the radial profile

Write

\[
q(\phi)=\frac{r'(\phi)}{r(\phi)}.
\]

On the open petal, a continuous tangent angle is

\[
\tau(\phi)=-\phi+\arg(q(\phi)-i),
\tag{2.1}
\]

up to a fixed additive multiple of `pi` when `r<0`.  Since `q-i` remains in the
open lower half-plane,

\[
\frac{d\tau}{d\phi}
=-1+\frac{q'}{1+q^2}.
\tag{2.2}
\]

At the left endpoint `q` tends to `+infinity`; at the right endpoint it tends
to `-infinity`.  The lower-half-plane argument therefore changes by `-pi`.
Hence

\[
\boxed{
\int_{\text{open petal}}\kappa\,ds
=-(L+\pi).
}
\tag{2.3}
\]

This is a universal law: the signed tangent turn depends only on the angular
span, not on the shape or amplitude of `r`.

If the petal is simple, so `0<L<=2 pi`, closing it at the origin contributes
the oriented corner turn

\[
\varepsilon=L-\pi\in(-\pi,\pi].
\tag{2.4}
\]

Therefore the complete simple petal has

\[
\boxed{
\int_{\text{closed petal}}\kappa\,ds=-2\pi.
}
\tag{2.5}
\]

The petal is oriented clockwise, consistently with the negative area in
`PFR-T1`.

---

## 3. Absolute-curvature excess pays for angular excess

Let `K_abs` be the total absolute curvature of a simple closed petal, including
the origin corner.  Split its signed turn into positive mass `P` and negative
magnitude `N`.  Equation (2.5) gives

\[
N-P=2\pi,
\qquad
K_{\rm abs}=N+P=2\pi+2P.
\tag{3.1}
\]

When `L>pi`, the origin corner itself has positive turn `L-pi`; hence

\[
P\geq(L-\pi)_+.
\]

Thus

\[
\boxed{
K_{\rm abs}
\geq
2\pi+2(L-\pi)_+.
}
\tag{3.2}
\]

Equivalently,

\[
\boxed{
L\leq
\pi+\frac{K_{\rm abs}-2\pi}{2}.
}
\tag{3.3}
\]

A convex clockwise petal has the minimal value `K_abs=2 pi`, and (3.3) then
forces

\[
L\leq\pi.
\tag{3.4}
\]

This explains the factor-of-two distinction between mere simplicity and the
stronger visual intuition of a genuinely rounded, convex flower petal:

```text
simple petal  -> angular span at most 2*pi;
convex petal  -> angular span at most pi.
```

The second scale is exactly the mean angular spacing suggested by the
Riemann--von Mangoldt count.

### PFR-T6B — curvature-defect petal-count inequality

Let

\[
\gamma_0<\gamma_1<\cdots<\gamma_M
\]

be consecutive simple critical-line zeros in a region where `vartheta'>0`.
Assume the associated Hardy petals are simple, and let `K_j` be their total
absolute curvatures, including the origin corners.  Then

\[
\boxed{
M
\geq
\frac{\vartheta(\gamma_M)-\vartheta(\gamma_0)}{\pi}
-\frac1{2\pi}
 \sum_{j=0}^{M-1}(K_j-2\pi).
}
\tag{3.5}
\]

#### Proof

Apply (3.3) to every angular span

\[
L_j=\vartheta(\gamma_{j+1})-\vartheta(\gamma_j)
\]

and sum.  Since the spans telescope,

\[
\vartheta(\gamma_M)-\vartheta(\gamma_0)
\leq
\pi M+\frac12\sum_j(K_j-2\pi),
\]

which is (3.5).

### Meaning of the new ledger

This is a precise version of the proposed flower argument:

> enough total phase must be paid either by origin crossings (critical-line
> zeros) or by excess nonconvex turning of the petals.

If the average absolute-curvature excess were `o(1)` per petal, the critical
line would already carry the full main zero density.  To prove RH one would
still need:

- the exact Riemann--von Mangoldt boundary term;
- multiple-zero and endpoint accounting;
- control strong enough to eliminate every sparse off-line pair, not merely a
  density-zero exceptional set.

The theorem does not hide those requirements.

### A completely real local curvature coordinate

In the original height variable, define

\[
\boxed{
\mathfrak C_H(t)=
\vartheta'(t)^2Z(t)^2
+2Z'(t)^2
-Z(t)Z''(t)
+\frac{\vartheta''(t)}{\vartheta'(t)}Z(t)Z'(t).
}
\tag{3.6}
\]

If `r(phi)=Z(t(phi))`, direct differentiation gives

\[
\vartheta'(t)^2
\left(rr''-r^2-2(r')^2\right)
=-\mathfrak C_H(t),
\tag{3.7}
\]

where the primes on `r` are angular derivatives.  Therefore

\[
\mathfrak C_H(t)\geq0
\]

is exactly the local clockwise-curvature condition for the visible Hardy
flower.  The geometry has been reduced to a real differential expression in
`Z`, `vartheta`, and their derivatives.

There is also an exact normalized real curvature ledger.  On an open Hardy
petal put

\[
D_H(t)=\vartheta'(t)^2Z(t)^2+Z'(t)^2.
\]

The derivative of the tangent angle is

\[
\frac{d\tau}{dt}
=-\frac{\vartheta'(t)\mathfrak C_H(t)}{D_H(t)}.
\tag{3.8}
\]

Consequently,

\[
\boxed{
\int_a^b
\frac{\vartheta'(t)\mathfrak C_H(t)}{D_H(t)}\,dt
=L+\pi,
}
\tag{3.9}
\]

and the positive back-turning mass of the open petal is exactly

\[
\boxed{
P_{\rm open}[a,b]
=
\int_a^b
\frac{\vartheta'(t)(\mathfrak C_H(t))_-}{D_H(t)}\,dt.
}
\tag{3.10}
\]

For a simple closed petal,

\[
\boxed{
K_{\rm abs}-2\pi
=2\left(P_{\rm open}+(L-\pi)_+\right).
}
\tag{3.11}
\]

Thus the curvature excess in (3.5) is not an abstract geometric quantity: it
is the sum of an explicit real normalized negative-curvature integral and the
positive origin-corner turn.  Equivalently, defining

\[
\mathcal D_j=P_{{\rm open},j}+(L_j-\pi)_+,
\]

one has the sharpened form

\[
\boxed{
M\ge
\frac{\vartheta(\gamma_M)-\vartheta(\gamma_0)}{\pi}
-\frac1\pi\sum_{j=0}^{M-1}\mathcal D_j.
}
\tag{3.12}
\]

No global bound on this real defect is asserted here.  Establishing one, or
showing that its cumulative size is forced to be small by the arithmetic
source, is the concrete next theorem target.

---
