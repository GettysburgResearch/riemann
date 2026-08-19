# L-99702 — The factor-67 scalar obeys an exact tilted owner flow and a positive renewal at every tilt

Claim ID: `L-99702`  
Status: **PROVED EXACT TWO-PARAMETER SOURCE IDENTITY**  
Created: 2026-08-20  
Depends on: `L-99271`; `L-99601`  
RH status: **not assumed**

Let `beta`, `g`, `T`, and `h` be as in `L-99700`. Thus

\[
g(n)=v_{67}(n)+1,
\qquad
\beta*g=\varepsilon.
\]

For every real `tau>=0`, define

\[
\beta_\tau(n)=\beta(n)n^{-\tau},
\qquad
g_\tau(n)=g(n)n^{-\tau},
\]

and

\[
\boxed{
h_\tau(x)=
\sum_{n\le x}\frac{\beta(n)}{n^{\tau+1/2}}T(x/n).
}
\tag{L-99702.1}
\]

Since `(beta_tau*g_tau)(n)=n^(-tau)(beta*g)(n)`,

\[
\boxed{\beta_\tau*g_\tau=\varepsilon.}
\tag{L-99702.2}
\]

## 1. Positive inverse renewal at every tilt

Finite divisor switching in (L-99702.2) gives

\[
\boxed{
T(x)=
\sum_{d\le x}
\frac{g(d)}{d^{\tau+1/2}}
 h_\tau(x/d)
\qquad(\tau\ge0).
}
\tag{L-99702.3}
\]

Every inverse-renewal weight is positive. At `tau=0` this is the renewal of PR
#653. Increasing `tau` damps every nonunit source while preserving the same
positive inverse.

For each fixed `x`,

\[
\lim_{\tau\to\infty}h_\tau(x)=T(x),
\tag{L-99702.4}
\]

because only `n=1` survives.

## 2. Logarithmic owner and the tilt evolution

Define

\[
\Lambda_g(q)=
\begin{cases}
2\log67,&q=67^a,\ a\ge1,\\
\log p,&q=p^a,\ p\ne67,\ a\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]

The logarithmic derivative of

\[
G(z)=\frac{\zeta(z)}{1-67^{-z}}
\]

gives

\[
\boxed{
\beta(n)\log n
=-\sum_{q\mid n}\Lambda_g(q)\beta(n/q).
}
\tag{L-99702.5}
\]

Differentiate the finite sum (L-99702.1), substitute (L-99702.5), and switch
finite divisors. This yields the exact positive-owner evolution

\[
\boxed{
\partial_\tau h_\tau(x)
=
\sum_{2\le q\le x}
\frac{\Lambda_g(q)}{q^{\tau+1/2}}
 h_\tau(x/q).
}
\tag{L-99702.6}
\]

Integrating from `tau=0` to infinity and using (L-99702.4),

\[
\boxed{
T(x)-h(x)
=
\int_0^\infty
\sum_{2\le q\le x}
\frac{\Lambda_g(q)}{q^{\tau+1/2}}
 h_\tau(x/q)
\,d\tau.
}
\tag{L-99702.7}
\]

Equations (L-99702.3) and (L-99702.6) are two independent exact descriptions
of the same native source: one is a positive inverse renewal in scale, the
other is a positive prime-power owner flow in tilt.

## 3. Exact positive-work domination of the negative part

Write `h_tau=(h_tau)_+-(h_tau)_-` and set

\[
\mathcal W_+(x)=
\int_0^\infty
\sum_{q\le x}
\frac{\Lambda_g(q)}{q^{\tau+1/2}}
(h_\tau(x/q))_+
\,d\tau.
\tag{L-99702.8}
\]

Equation (L-99702.7) gives

\[
h(x)=T(x)-\mathcal W_+(x)+\mathcal W_-(x)
\]

with `mathcal W_- >=0`. Therefore

\[
\boxed{
h_-(x)
\le
[\mathcal W_+(x)-T(x)]_+.
}
\tag{L-99702.9}
\]

This isolates a source-faithful sufficient producer:

```text
TOCE67:
    integral_1^X [mathcal W_+(x)-T(x)]_+ dx/x
    = X^o(1).
```

By `L-99700`, `TOCE67` implies RH.

Unlike an absolute Möbius estimate, `mathcal W_+` retains the exact tilt, the
actual positive prime-power owner, the doubled local 67 channel, and the live
smaller-scale scalar. The theorem does not assert `TOCE67`; it supplies its
complete primitive formula.
