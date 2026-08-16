# L-93303 — The surviving Q4 obstruction is one explicit mollified carrier Fourier coefficient

Claim ID: `L-93303`  
Status: **PROVED EXACT NORMAL FORM / OPEN ESTIMATE**  
Created: 2026-08-16  
Depends on: `L-93302`; Mellin inversion  
RH status: **unproved**

For fixed `r`, define

\[
P_{V,N}(t)=\sum_{V<m\le N}\frac{\Lambda(m)}{m^{1/2+it}},
\]

\[
M_{U,N}(t)=\sum_{U<q\le N}\frac{a_U(q)}{q^{1/2+it}}.
\]

Then Mellin inversion gives

\[
\boxed{
B_r(N)=\frac{\sqrt N}{2\pi}
\int_{-\infty}^{\infty}
\widehat W_r(1/2+it)
N^{it}P_{V,N}(t)M_{U,N}(t)dt.
}
\tag{L-93303.1}
\]

The product cutoff `mq<=N` is supplied by the support of `W_r`.

## 1. Safe coefficient energies

Elementary estimates give

\[
\sum_{m\le N}\frac{\Lambda(m)^2}{m}\ll\log^2(2N),
\tag{L-93303.2}
\]

and, since `|a_U(q)|<=tau(q)` and `tau(q)^2<=d_4(q)`,

\[
\sum_{q\le N}\frac{|a_U(q)|^2}{q}\ll\log^4(2N).
\tag{L-93303.3}
\]

Also

\[
\widehat W_r(1/2+it)\ll_r(1+|t|)^{-r-1}.
\tag{L-93303.4}
\]

These are diagonal inputs only. `R-93301` shows that they do not imply the required pointwise Fourier coefficient.

## 2. Actual remaining estimate

By `L-93302`, RH would follow from

\[
\boxed{
\left|
\int_{-\infty}^{\infty}
\widehat W_r(1/2+it)N^{it}
P_{V,N}(t)M_{U,N}(t)dt
\right|
\ll_r(\log(2N))^A
}
\tag{L-93303.5}
\]

for one fixed `r` and `A`.

This is not CPBD with a new name. Complete prime towers, all Type-I terms, the two-adic gauge, and every product `mq<=N^(eta_r)` have already been removed. The surviving object is one specified Fourier coefficient—at frequency `log N`—of a prime carrier multiplied by an explicit truncated-Mobius mollifier.

## 3. First-Hermite carrier interface

The First-Hermite polynomial uses the same critical-weight prime carrier

\[
\sum_n\frac{\Lambda(n)}{\sqrt n}h_q(\log n)n^{it}.
\]

Q4 uses a sharp log window, a mollifier, and a resolvent weight; First-Hermite uses a Gaussian-Hermite log window. A genuine shared theorem must exploit these carrier phases and source coefficients, not merely count aligned prime blocks.
