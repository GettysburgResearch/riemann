# L-99711 — An adaptive Poisson strip turns point evaluation into a coercive phase square at subpower cost

Claim ID: `L-99711`  
Status: **PROVED EXACT COMPLEX-ANALYTIC REDUCTION**  
Created: 2026-08-20  
Depends on: `L-99710`  
RH status: **not assumed**

Let

\[
F(w)=\sum_{n\le X}c_n n^{-w}
\]

be any finite Dirichlet polynomial.  For `tau>0`, `F` is bounded and analytic
in the half-plane `Re w>-tau`.  Since `|F|^2` is subharmonic, the Poisson
majorant for that half-plane gives

\[
\boxed{
|F(0)|^2
\le
\int_{\mathbb R}
 {\tau\over\pi(\tau^2+\gamma^2)}
 |F(-\tau+i\gamma)|^2\,d\gamma.
}
\tag{L-99711.1}
\]

No limiting Dirichlet-series continuation is used: this is a finite-polynomial
identity/inequality at each endpoint.

For the SHARP Harnack source, put

\[
\mathscr H_x(w)
=
\sum_{n\le x}{\beta(n)\over\sqrt n}
 T(x/n)n^{-w},
\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\tag{L-99711.2}
\]

Then `mathscr H_x(0)=H_67^sharp(x)`, and (L-99711.1) gives

\[
\boxed{
|H_{67}^{\rm sharp}(x)|^2
\le
\int_{\mathbb R}P_\tau(\gamma)
 |\mathscr H_x(-\tau+i\gamma)|^2\,d\gamma.
}
\tag{L-99711.3}
\]

The left shift only multiplies the coefficient of `n` by `n^tau`, and hence by
at most `x^tau`.

## Adaptive width

For `x>=e^e`, choose

\[
\tau_x={1\over\log\log x}.
\tag{L-99711.4}
\]

Then

\[
x^{\tau_x}
=
\exp\!\left({\log x\over\log\log x}\right)
=x^{o(1)},
\tag{L-99711.5}
\]

while `L-99710` gives the owner coercivity

\[
\overline V_{\tau_x}(n)
\ge {1\over\log\log x}|a(n)|^2.
\tag{L-99711.6}
\]

Thus the exact tradeoff is

```text
phase gap loss:       at most one factor loglog(x);
left-strip inflation: exp(log(x)/loglog(x)) = x^(o(1)).
```

This is the first phase regularization in the live owner programme that is both
coercive on the zero-energy parity channel and compatible with the subpower
negative-mass conclusion criterion of PR #653.

## Firewall

A fixed `tau>0` gives a uniform gap but incurs the power cost `x^tau`; it cannot
feed a subpower conclusion.  Sending `tau` to zero faster than
`1/loglog x` is unnecessary and weakens the gap.  The adaptive scale
(L-99711.4) is the natural balance between analytic point evaluation and owner
coercivity.

The remaining question is not complex analysis.  It is a source-specific
Carleson embedding transporting the averaged owner quadratic variation through
the SHARP activation kernel before source indices are collapsed.