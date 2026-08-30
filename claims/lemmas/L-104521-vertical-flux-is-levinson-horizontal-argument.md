# L-104521 — The limiting vertical flux is one Levinson horizontal argument

Claim ID: `L-104521`  
Status: **PROVED EXACT AFTER THE L-104519 EXHAUSTION**  
Created: 2026-08-22  
Depends on: `L-104519`; the functional equation and parity of Xi  
RH status: **not assumed**

Fix `k`, `lambda>0` and a regular ordinate `T`.  Put

\[
F_k(z)=\Xi^{(k)}(z),
\qquad
E_k(z)=F_k(z)-i\lambda F_{k+1}(z).
\]

In the `s`-plane, with

\[
s=\frac12+iz,
\]

one has

\[
F_k(z)=i^k\xi^{(k)}(s)
\]

and therefore

\[
\boxed{
E_k(z)
=
i^kG_{k,\lambda}(s),
\qquad
G_{k,\lambda}(s)
=
\xi^{(k)}(s)+\lambda\xi^{(k+1)}(s).
}
\tag{L-104521.1}
\]

Consequently

\[
\boxed{
\frac{E_k(z)}{E_{k+1}(z)}
=
-i\,
\frac{G_{k,\lambda}(s)}
     {G_{k+1,\lambda}(s)}.
}
\tag{L-104521.2}
\]

## 1. Right vertical side is a horizontal safe-line path

The right vertical ray

\[
z=T-iy,
\qquad 0\le y<\infty,
\]

corresponds exactly to

\[
s=\frac12+y+iT,
\qquad
\frac12\le\Re s<\infty.
\]

Let

\[
\Theta_{k,\lambda}(T)
=
\Delta_{\sigma:\,\infty\to1/2}
\arg
\frac{
G_{k,\lambda}(\sigma+iT)
}{
G_{k+1,\lambda}(\sigma+iT)
},
\tag{L-104521.3}
\]

where the argument is continued from the far-right half-plane.  The far-right
Stirling asymptotic fixes the initial branch because

\[
\frac{G_{k,\lambda}(s)}{G_{k+1,\lambda}(s)}
=
\frac1{a(s)}(1+o(1)),
\qquad
a(s)=\frac12\log\frac{s}{2\pi}+o(1),
\]

which is positive real to leading order.

Equation (L-104521.2) gives the exact right-side phase change.

## 2. The left side is the reflected copy

For real-entire Xi and real `lambda`,

\[
E_k(-\overline z)=(-1)^k\overline{E_k(z)}.
\]

Hence

\[
\frac{E_k(-\overline z)}{E_{k+1}(-\overline z)}
=
-\overline{
\frac{E_k(z)}{E_{k+1}(z)}
}.
\tag{L-104521.4}
\]

With the boundary orientations, the left vertical side contributes the same
phase change as the right side.  After `L-104519` removes the lower horizontal
term, the complete limiting vertical charge is therefore

\[
\boxed{
\mathfrak V_{k,\lambda}^{\infty}(T)
=
-\frac1\pi\,
\Theta_{k,\lambda}(T).
}
\tag{L-104521.5}
\]

The sign follows from defining `Theta` from `infinity` toward the critical
line.

## 3. Meaning

The last boundary obstruction is not a new two-dimensional operator.  It is
the horizontal argument variation of one explicit adjacent-derivative quotient

\[
\frac{
\xi^{(k)}+\lambda\xi^{(k+1)}
}{
\xi^{(k+1)}+\lambda\xi^{(k+2)}
}
\]

from the safe half-plane to the critical line.

This is precisely the coordinate in which Levinson-type argument principles
and mollified derivative counts operate.

Define the remaining boundary theorem

```text
HARG104521:
  at the last defective derivative level, the continued horizontal argument
  Theta_(k,lambda)(T) cannot carry the inward unit of companion index.
```

Then

\[
\boxed{
\mathrm{PRES104518}
\wedge
\mathrm{HARG104521}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-104521.6}
\]

Neither exclusion is proved here.  The advance is an exact one-dimensional
identification of the former vertical-flux gate, with its branch fixed in the
far-right Euler/Stirling region.
