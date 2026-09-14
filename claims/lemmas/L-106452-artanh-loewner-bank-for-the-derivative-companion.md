# L-106452 — The derivative companion has a positive artanh–Loewner source bank

Claim ID: `L-106452`  
Status: **PROVED EXACT OPERATOR-MONOTONE SOURCE THEOREM**  
Created: 2026-08-25  
Depends on: elementary Loewner theory and the truncated Xi Fourier source  
RH status: **not assumed**

Fix `lambda,L>0` with

\[
c=\lambda L<1
\]

and put

\[
\phi_\lambda(u)=\operatorname{artanh}(\lambda u),
\qquad |u|\le L.
\]

## 1. Exact hyperbolic factorization

For every `|lambda u|<1`,

\[
\boxed{
1\pm\lambda u
 =\sqrt{1-\lambda^2u^2}\,
  e^{\pm\phi_\lambda(u)}.
}
\tag{L-106452.1}
\]

Thus the two derivative-companion multipliers have one common positive carrier
and opposite values of one real spectral generator.  This identity is
nonperturbative; it retains the complete odd Taylor hierarchy.

## 2. Positive Loewner kernel

Define

\[
\mathscr L_\lambda(u,v)
 ={\phi_\lambda(u)-\phi_\lambda(v)\over u-v}
\]

with the diagonal value

\[
\mathscr L_\lambda(u,u)
 ={\lambda\over1-\lambda^2u^2}.
\]

The exact integral representation is

\[
\boxed{
\begin{aligned}
\mathscr L_\lambda(u,v)
={\lambda\over2}\int_0^1\Bigg[&
 {1\over(1-t\lambda u)(1-t\lambda v)}\\
&+{1\over(1+t\lambda u)(1+t\lambda v)}
\Bigg]dt.
\end{aligned}
}
\tag{L-106452.2}

Indeed,

\[
\operatorname{artanh}x
 =\int_0^1{x\over1-t^2x^2}\,dt
 ={1\over2}\int_0^1
 \left({x\over1-tx}+{x\over1+tx}\right)dt,
\]

and the divided difference of `x/(1-ax)` is

\[
{1\over(1-ax)(1-ay)}.
\]

Equation (L-106452.2) is a Gram representation. Consequently, for every finite
real packet `u_1,...,u_n in [-L,L]`,

\[
\boxed{
[\mathscr L_\lambda(u_j,u_k)]_{j,k=1}^n\succeq0.
}
\tag{L-106452.3}

Equivalently, `artanh(lambda x)` is operator monotone on the declared band.

## 3. Positive continuum derivative bank

Let `a(u)>=0` be any integrable source supported in `[-L,L]`. Define

\[
\boxed{
\mathcal Q_{\lambda,a}(x)
 =\iint
 \mathscr L_\lambda(u,v)
 a(u)a(v)e^{ix(u-v)}\,du\,dv.
}
\tag{L-106452.4

Using (L-106452.2),

\[
\boxed{
\begin{aligned}
\mathcal Q_{\lambda,a}(x)
={\lambda\over2}\int_0^1\Bigg(
&\left|\int{a(u)e^{ixu}\over1-t\lambda u}\,du\right|^2\\
+&\left|\int{a(u)e^{ixu}\over1+t\lambda u}\,du\right|^2
\Bigg)dt\ge0.
\end{aligned}
}
\tag{L-106452.5

The continuum features

\[
(1\mp t\lambda u)^{-1},
\qquad -1\le t\le1,
\]

are source-owned resolvent coordinates. Their power-series closure contains
every polynomial in `u`; hence they are complete in the cyclic polynomial
subspace of the truncated source measure.

Expanding the generator gives

\[
\phi_\lambda(u)
 =\sum_{r\ge0}{\lambda^{2r+1}u^{2r+1}\over2r+1}.
\]

Therefore (L-106452.4) is the positive recombination of the complete odd
Hermitian derivative hierarchy.  No finite derivative truncation has been
selected after observing a zero.

## 4. Connection with endpoint exterior-square sources

For every odd monomial, the divided difference is

\[
{u^{2r+1}-v^{2r+1}\over u-v}=Q_{2r}(u,v).
\]

Thus `L-106450` supplies the analytic-square, sum-frequency endpoint currents,
while (L-106452.4) supplies their Hermitian, difference-frequency positive
completion.  The two are the two boundary polarizations of the same odd source
hierarchy.

This is the natural positive bank for a future proof of `SIGNEDTAIL106430` or
`SIGNEDTAIL5-106450`: it retains all scales of the derivative companion rather
than using one hard Paley--Wiener cutoff.

## 5. Boundary

The physical all-pass quotient is a ratio of **observed transforms**, not the
observation of the spectral multiplier ratio in (L-106452.1).  Therefore the
Loewner positivity does not by itself imply that the companion is inner or
that its signed complement is nonpositive.  A source-to-companion realization
or a quantitative resolvent sampling theorem is still required.