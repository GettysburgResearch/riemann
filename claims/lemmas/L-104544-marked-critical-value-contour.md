# L-104544 — Marked critical-value moments as thin-strip contour integrals

Claim ID: `L-104544`  
Status: **PROVED EXACT**  
Created: 2026-08-23  
RH status: **not assumed**

Let `f` be real entire. Fix a regular `T>0`. For sufficiently small
`epsilon>0`, suppose the thin rectangle

\[
\Omega_{T,\epsilon}
=
\{z:|\Re z|<T,\ |\Im z|<\epsilon\}
\]

has no zero of `f'` on its boundary and contains no nonreal zero of `f'`.
Thus its zeros of `f'` are exactly the real critical points of `f` in
`(-T,T)`.

Let `m` be holomorphic on a neighbourhood of the closed rectangle and real on
the real axis.

## 1. Exact marked second moment

At a simple zero `c` of `f'`, the logarithmic derivative `f''/f'` has residue
one. Therefore

\[
\boxed{
\sum_{\substack{f'(c)=0\\c\in(-T,T)}}
m(c)^2f(c)^2
=
\frac{1}{2\pi i}
\int_{\partial\Omega_{T,\epsilon}}
m(z)^2f(z)^2\frac{f''(z)}{f'(z)}\,dz.
}
\tag{L-104544.1}
\]

The left side is exactly the marked second moment `B_w` of `L-104543` when
`w(t)=|m(t)|`.

More generally, for every integer `r>=1`,

\[
\boxed{
\sum_{f'(c)=0}
m(c)^r f(c)^r
=
\frac{1}{2\pi i}
\int_{\partial\Omega}
m(z)^r f(z)^r\frac{f''(z)}{f'(z)}\,dz.
}
\tag{L-104544.2}
\]

## 2. Xi specialization

For

\[
f(t)=\Xi''(t),
\qquad
f'(t)=\Xi'''(t),
\]

the second moment becomes

\[
\boxed{
B_m(T)
=
\frac{1}{2\pi i}
\int_{\partial\Omega_{T,\epsilon}}
m(z)^2\Xi''(z)^2
\frac{\Xi''''(z)}{\Xi'''(z)}\,dz.
}
\tag{L-104544.3}
\]

In the `s`-plane this is a mixed adjacent-derivative moment of `xi`, with the
complete gamma factor retained.

A height-dependent holomorphic normalizer `m_T` may remove the deterministic
gamma envelope before the contour is estimated. The normalizer is fixed before
the real critical points are observed.

## 3. Analytic route

Equation (L-104544.3) is designed for the same Dirichlet-polynomial machinery
as Levinson--Conrey:

```text
thin-strip logarithmic derivative
+ marked adjacent-derivative square
+ fixed mollifier
+ horizontal gamma normalization.
```

The theorem does not evaluate the contour asymptotically. It proves that the
only new second moment needed by `CM2X104590` is a standard marked
logarithmic-derivative contour, not an unknown nonlinear sampling measure.
