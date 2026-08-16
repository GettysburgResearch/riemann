# L-93303 — Vaughan decomposition closes every unbalanced cubic range and leaves one explicit near-hyperbola bilinear form

Claim ID: `L-93303`  
Status: **UNCONDITIONAL EXACT DECOMPOSITION AND SAFE-RANGE THEOREM**  
Created: 2026-08-16  
Depends on: `L-93301`, `L-93302`; elementary divisor estimates  
RH status: **unproved**

## 1. The weighted von Mangoldt sum

Put

\[
 S_F(N)=\sum_{n\le N}\Lambda(n)F(n/N),
\]

with \(F\) extended by zero outside \(0<x\le1\).

Let

\[
 U=V=\lfloor N^{1/3}\rfloor
\]

and write \(f_{\le U}(n)=f(n)\mathbf1_{n\le U}\).  The exact Vaughan identity is

\[
 \boxed{
 \Lambda
 =
 \Lambda_{\le V}
 +\mu_{\le U}*\log
 -\mu_{\le U}*\Lambda_{\le V}*1
 +\mu_{>U}*\Lambda_{>V}*1.
 }
 \tag{L-93303.1}
\]

It follows from \(\Lambda=\mu*\log\), \(\log=\Lambda*1\), and
\(\mu*1=\varepsilon\).  No analytic estimate enters.

## 2. The three Type-I terms

Apply (L-93303.1) to \(S_F(N)\).  Denote the first three weighted terms by
\(T_1,T_2,T_3\).

Because \(|F(x)|\le5x\),

\[
 |T_1|
 \le\frac5N\sum_{n\le V}n\Lambda(n)
 \ll\frac{V^2\log(2V)}N.
 \tag{L-93303.2}
\]

For \(y=N/d\), `L-93302.11` gives

\[
 \sum_{r\le y}\log r\,F(r/y)
 =O\!\left(\frac{\log(2y)}y\right).
\]

Hence

\[
 |T_2|
 \ll
 \sum_{d\le U}\frac{d\log(2N)}N
 \ll\frac{U^2\log(2N)}N.
 \tag{L-93303.3}
\]

Similarly, `L-93302.9` gives

\[
 \begin{aligned}
 |T_3|
 &\ll
 \frac1N
 \left(\sum_{d\le U}d\right)
 \left(\sum_{\ell\le V}\ell\Lambda(\ell)\right)
 \\
 &\ll
 \frac{U^2V^2\log(2V)}N.
 \end{aligned}
 \tag{L-93303.4}
\]

With \(U=V=N^{1/3}+O(1)\),

\[
 \boxed{
 T_1+T_2-T_3
 =O(N^{1/3}\log(2N)).
 }
 \tag{L-93303.5}
\]

Thus all Type-I contributions are far below the required square-root scale.

## 3. Exact Type-II coefficient

For \(m\ge1\), define the truncated Möbius divisor coefficient

\[
 \boxed{
 a_U(m)=\sum_{\substack{d\mid m\\d>U}}\mu(d).
 }
 \tag{L-93303.6}
\]

Grouping \(m=dr\) in the last term of (L-93303.1) gives the exact Type-II form

\[
 \boxed{
 \mathcal T_N
 =
 \sum_{\substack{m>U,\ \ell>V\\m\ell\le N}}
 a_U(m)\Lambda(\ell)F(m\ell/N).
 }
 \tag{L-93303.7}
\]

Every variable is automatically bounded by

\[
 U<m\le N/V,
 \qquad
 V<\ell\le N/U.
 \tag{L-93303.8}
\]

Consequently both variables lie between the one-third and two-thirds scales.

The complete cubic scalar is

\[
 \boxed{
 \mathcal A_\circ(N)
 =
 \mathcal T_N
 +O(N^{1/3}\log(2N))
 +O(\log N),
 }
 \tag{L-93303.9}
\]

where the final term is the explicit four-adic gauge.

## 4. The low-product part is square-root safe

Put

\[
 Y=N^{3/4}
\]

and split \(\mathcal T_N=\mathcal T_N^{\rm low}+\mathcal B_N\) according as
\(m\ell\le Y\) or \(m\ell>Y\).

Since \(|a_U(m)|\le\tau(m)\), \(|F(x)|\le5x\), and

\[
 \sum_{\ell\le z}\ell\Lambda(\ell)
 \le\sum_{\ell\le z}\ell\log(2\ell)
 \ll z^2\log(2z),
\]

one obtains

\[
 \begin{aligned}
 |\mathcal T_N^{\rm low}|
 &\ll
 \frac1N
 \sum_{U<m\le Y/V}
 \tau(m)m
 \left(\frac Ym\right)^2
 \log(2N)
 \\
 &\ll
 \frac{Y^2\log(2N)}N
 \sum_{m\le Y/V}\frac{\tau(m)}m.
 \end{aligned}
\]

The elementary divisor identity gives

\[
 \sum_{m\le M}\frac{\tau(m)}m
 =
 \sum_{ab\le M}\frac1{ab}
 \ll(1+\log M)^2.
\]

Therefore

\[
 \boxed{
 \mathcal T_N^{\rm low}
 =O\!\left(\sqrt N\,(\log(2N))^3\right).
 }
 \tag{L-93303.10}
\]

## 5. The sole remaining bilinear form

The hard form is now

\[
 \boxed{
 \mathcal B_N
 =
 \sum_{\substack{
 N^{1/3}<m,\ell\le N^{2/3}\\
 N^{3/4}<m\ell\le N
 }}
 a_U(m)\Lambda(\ell)F(m\ell/N),
 \qquad U=\lfloor N^{1/3}\rfloor.
 }
 \tag{L-93303.11}
\]

Combining the previous sections,

\[
 \boxed{
 \mathcal A_\circ(N)
 =
 \mathcal B_N
 +O\!\left(\sqrt N(\log(2N))^3\right).
 }
 \tag{L-93303.12}
\]

This is a strict reduction of CPBD:

```text
no endpoint row;
no mean coordinate;
no prime-block count;
no same-prime tower estimate;
no small prime base;
no Type-I range;
no product below N^(3/4).
```

Only the arithmetic covariance of the explicit truncated Möbius coefficient
\(a_U(m)\) with \(\Lambda(\ell)\) remains.

## 6. Additive dispersion coordinate

By `L-93302.13`, the full Type-II form has the exact absolutely convergent
expansion

\[
 \boxed{
 \mathcal T_N
 =
 \sum_{h\ne0}\widehat F_{\mathbb T}(h)
 \mathcal D_h(N),
 }
 \tag{L-93303.13}
\]

where

\[
 \mathcal D_h(N)
 =
 \sum_{\substack{m>U,\ \ell>V\\m\ell\le N}}
 a_U(m)\Lambda(\ell)e(hm\ell/N).
 \tag{L-93303.14}
\]

The zero additive mode is absent.  The low-product contribution is already
paid by (L-93303.10), so a proof may work with either
\(\mathcal B_N\) or the Fourier family \(\mathcal D_h(N)\).

A generic large sieve is not sufficient; `R-93300` explains why the actual
Möbius--prime covariance is load bearing.

## 7. Mellin band-pass coordinate

For any \(c>0\) avoiding the negative poles of \(\widehat F\), Mellin inversion
also gives

\[
 \boxed{
 \mathcal T_N
 =
 \frac1{2\pi}
 \int_{-\infty}^{\infty}
 \widehat F(c+it)N^{c+it}
 A_U(c+it)L_V(c+it)\,dt,
 }
 \tag{L-93303.15}
\]

with finite Dirichlet polynomials

\[
 A_U(s)=\sum_{U<m\le N/V}\frac{a_U(m)}{m^s},
 \qquad
 L_V(s)=\sum_{V<\ell\le N/U}\frac{\Lambda(\ell)}{\ell^s}.
\]

At \(c=1\), the multiplier has a double zero at \(t=0\) and decays like
\(|t|^{-2}\).  This is a genuine band-pass identity.  A bound for the product
of the two finite polynomials at the required strength is still arithmetic,
not a contour-shift consequence.

## 8. Boundary

```text
Vaughan identity                                  exact
Type-I terms                                      O(N^(1/3) log N)
low-product Type-II                               O(sqrt(N) log^3 N)
balanced near-hyperbola form                      exact remaining object
additive dispersion representation                exact
Mellin band-pass representation                   exact
balanced square-root estimate                     open / RH-bearing
Riemann Hypothesis                                unproved
```
