# R-100210 — The quadratic envelope is not a subcritical Euler-product route after native conjugation

Claim ID: `R-100210`  
Status: **PROVED EXACT MECHANISM FIREWALL**  
Created: 2026-08-20  
Depends on: PR #672, `L-99980`–`L-99981`  
RH status: **unproved**

PR #672 writes the quadratic-envelope defect in the normalized form

\[
\frac{\mathcal E_2(X)}X
 =\sum_{n\ge1}\frac{\beta(n)}{n^{3/2}}f(X/n),
\]

where

\[
f(y)=
\begin{cases}
16,&0<y<1,\\
24y^{-1/2}-9y^{-1},&y\ge1.
\end{cases}
\]

At first sight the labelled activities `q^{-3/2}` are summable.  That is not
the physical contraction seen by the kernel.

Put `u=log y` and

\[
F(u)=e^{3u/2}f(e^u).
\]

Then

\[
F(u)=
\begin{cases}
16e^{3u/2},&u<0,\\
24e^u-9e^{u/2},&u\ge0.
\end{cases}
\tag{R-100210.1}
\]

For a label `q` and translation

\[
(\tau_qF)(u)=F(u-\log q),
\]

one has the exact conjugation

\[
\boxed{
e^{3u/2}(I-q^{-3/2}U_q)f(e^u)
 =(I-\tau_q)F(u).
}
\tag{R-100210.2}
\]

In the fully active region, the two modes transform as

\[
(I-\tau_q)e^u=(1-q^{-1})e^u,
\]

\[
(I-\tau_q)e^{u/2}=(1-q^{-1/2})e^{u/2}.
\]

Hence the leading physical mode is governed by the critical activity

\[
\boxed{q^{-1},}
\]

not by `q^{-3/2}`.  Equivalently, for fixed large `y`,

\[
\frac{q^{-3/2}f(y/q)}{f(y)}\longrightarrow\frac1q
\qquad(y\to\infty).
\tag{R-100210.3}
\]

Since

\[
\sum_p\frac1p=\infty,
\]

no proof of `FEAG99980` may use the summability of
`sum_p p^{-3/2}` after the source has been observed through `f`.

This does not refute the finite activation inequality itself.  It proves that
the quadratic envelope is another critical parity/cross-core problem, not a
genuinely subcritical alternative to the native box.

```text
quadratic-envelope identities            retained exact
one-/two-prime positivity                retained exact
fully coactive positivity                retained exact
p^(-3/2) source-blind contraction         invalid after observation
critical p^(-1) geometry                  proved exact
FEAG99980                                 open / conclusion-bearing
Riemann Hypothesis                        unproved
```
