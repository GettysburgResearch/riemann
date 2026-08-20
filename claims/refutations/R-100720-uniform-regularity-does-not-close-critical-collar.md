# R-100720 — Uniform Lipschitz and third-variation bounds do not close the critical collar

Claim ID: `R-100720`  
Status: **PROVED EXACT METHOD FIREWALL**  
Created: 2026-08-21  
Depends on: `L-100722`  
RH status: **not assumed**

The unconditional estimates

```text
uniform derivative bound;
uniform L1 third-variation bound;
compact collar support at every finite cutoff;
```

are substantial but do not by themselves imply subpower logarithmic negative
mass.

Let

\[
\eta(s)=s^3(1-s)^3\mathbf1_{0\le s\le1}
\]

and for `T>=1` define

\[
f_T(t)=-T\eta(t/T).
\tag{R-100720.1}
\]

Because `eta` and its first two derivatives vanish at both endpoints, `f_T` is
a compact `C^2` cubic-spline-type packet. Moreover

\[
\|f_T'\|_\infty=\|\eta'\|_\infty,
\]

and

\[
\|f_T'''\|_{L^1(dt)}
=T^{-1}\|\eta'''\|_{L^1(ds)}
\le\|\eta'''\|_1.
\tag{R-100720.2}
\]

Thus the two regularity quantities are uniformly bounded, in fact the third
variation tends to zero.

On the other hand,

\[
\int_0^\infty(f_T(t))_-{dt\over t}
=T\int_0^1\eta(s){ds\over s}
\asymp T.
\tag{R-100720.3}
\]

In the physical variable `X=t^2`, this is of order `sqrt(X)`, not `X^o(1)`.

Consequently neither the Tao prefix bound nor the summable third derivative
may be promoted directly to the conclusion-facing estimate.  A successful
proof must preserve the arithmetic sign/phase information in the compensated
prefix, or prove both source-owned Taylor certificates of `L-100723`.

This countermodel does not refute `LPCC100723` or `FPCC100723`; it refutes only
the source-blind inference from regularity to critical one-sided mass.
