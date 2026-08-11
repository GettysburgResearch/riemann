# L-90703 — The Q4 compact innovation is a singular cosine-antiderivative energy and a weighted Goldbach correlation

Claim ID: `L-90703`  
Status: **PROPOSED COMPLETE EXACT FINITE NORMAL FORM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `T-90404` exact filtered-Chebyshev innovation formula  
Scope: the own compact current and its uniform row energy; the delayed gauge remains `O(log n)`, and no PIG/RH estimate is proved

## 1. The radix-four block-prime source

For integers \(x\ge0\), put

\[
\mathcal B(x)=\psi(4x)-4\psi(x),
\qquad \mathcal B(0)=0,
\tag{L-90703.1}
\]

where \(\psi(x)=\sum_{m\le x}\Lambda(m)\). Define its increment

\[
b(m)=\mathcal B(m)-\mathcal B(m-1)
=\sum_{r=0}^{3}\Lambda(4m-r)-4\Lambda(m).
\tag{L-90703.2}
\]

Thus \(b(m)\) is the discrepancy between one complete block of four consecutive von-Mangoldt coefficients and four copies of the coefficient at the contracted endpoint. Exactly,

\[
\mathcal B(x)=\sum_{m=1}^{x}b(m).
\tag{L-90703.3}
\]

For \(n=j+k\), `T-90404` gives the own compact-current row

\[
\boxed{
Q_n(j)=\mathcal B(n)-\mathcal B(j)-\mathcal B(n-j)-c,
\qquad c=4\log4,
}
\tag{L-90703.4}
\]

for \(1\le j\le n-1\). The actual innovation is this row minus the delayed bare gauge

\[
(\log4)\,\mathcal L_{n,j}(b_4)=O(\log n).
\tag{L-90703.5}
\]

The hard positive mass is therefore already present in the row energy of (L-90703.4).

## 2. Exact cyclic cosine decomposition

Put

\[
C_n=\mathcal B(n)-c,
\qquad
S_n=\sum_{j=0}^{n-1}\mathcal B(j).
\tag{L-90703.6}
\]

On the cyclic group \(\mathbb Z/n\mathbb Z\), define the artificial endpoint completion

\[
\widetilde Q_n(j)=C_n-\mathcal B(j)-\mathcal B((-j)\bmod n),
\qquad0\le j<n,
\tag{L-90703.7}
\]

where the cyclic sequence has value \(\mathcal B(0)=0\). Then

\[
\widetilde Q_n(0)=C_n,
\qquad
\widetilde Q_n(j)=Q_n(j)\quad(1\le j<n).
\tag{L-90703.8}
\]

Use the discrete Fourier convention

\[
\widehat{\mathcal B}_n(\ell)
=\sum_{j=0}^{n-1}\mathcal B(j)e^{-2\pi i\ell j/n},
\qquad
\widehat{\widetilde Q}_n(\ell)
=\sum_{j=0}^{n-1}\widetilde Q_n(j)e^{-2\pi i\ell j/n}.
\tag{L-90703.9}
\]

Reflection on the cyclic group gives the exact spectrum

\[
\boxed{
\widehat{\widetilde Q}_n(0)=nC_n-2S_n,
}
\tag{L-90703.10}
\]

and, for \(1\le\ell<n\),

\[
\boxed{
\widehat{\widetilde Q}_n(\ell)
=-2\operatorname{Re}\widehat{\mathcal B}_n(\ell).
}
\tag{L-90703.11}
\]

Hence only the cosine projection of the cumulative prime-block discrepancy survives. Parseval yields

\[
\boxed{
\begin{aligned}
\sum_{j=1}^{n-1}|Q_n(j)|^2
={}&\frac1n\left[
  (nC_n-2S_n)^2
  +4\sum_{\ell=1}^{n-1}
    \bigl(\operatorname{Re}\widehat{\mathcal B}_n(\ell)\bigr)^2
  \right]
  -C_n^2.
\end{aligned}}
\tag{L-90703.12}
\]

This is an exact diagonalisation of the full uniform row energy, with no prime estimate and no discarded cross term.

## 3. The singular discrete antiderivative

Let

\[
q_\ell=e^{-2\pi i\ell/n}.
\]

For \(\ell\ne0\), summing (L-90703.3) in the opposite order gives

\[
\boxed{
\widehat{\mathcal B}_n(\ell)
=-\sum_{m=1}^{n}b(m)\frac{1-q_\ell^m}{1-q_\ell}
=\frac{T_n(\ell)-\mathcal B(n)}{1-q_\ell},
}
\tag{L-90703.13}
\]

where

\[
T_n(\ell)=\sum_{m=1}^{n}b(m)q_\ell^m.
\tag{L-90703.14}
\]

The term \(m=n\) is harmless in the first expression because \(q_\ell^n=1\). The zero mode can likewise be written

\[
\boxed{
nC_n-2S_n
=\sum_{m=1}^{n}(2m-n)b(m)-nc.
}
\tag{L-90703.15}
\]

Equations (L-90703.12)--(L-90703.15) show precisely where the generic \(L^2\) route loses a factor of \(n\):

\[
|1-q_\ell|^{-1}
=\frac1{2|\sin(\pi\ell/n)|}
\asymp\frac n\ell
\qquad(1\le\ell\ll n).
\tag{L-90703.16}
\]

PIG therefore asks for arithmetic cancellation of the low-frequency block-prime exponential sums \(T_n(\ell)-\mathcal B(n)\) in the singular cosine-antiderivative metric. Parseval for \(b\) alone cannot provide it.

## 4. Exact physical/additive-correlation expansion

The same row energy has a second exact form. Let

\[
C=C_n,
\qquad
R_1(n)=\sum_{m=1}^{n-1}(n-m)b(m),
\tag{L-90703.17}
\]

\[
R_{\max}(n)
=\sum_{a,b<n}(n-\max(a,b))b(a)b(b),
\tag{L-90703.18}
\]

and

\[
R_+(n)
=\sum_{\substack{a,b\ge1\\a+b\le n}}
(n+1-a-b)b(a)b(b).
\tag{L-90703.19}
\]

Direct expansion of the square gives

\[
\boxed{
\sum_{j=1}^{n-1}|Q_n(j)|^2
=(n-1)C^2-4CR_1(n)+2R_{\max}(n)+2R_+(n).
}
\tag{L-90703.20}
\]

Here

\[
R_+(n)=\sum_{r=2}^{n}(n+1-r)(b*b)(r)
\tag{L-90703.21}
\]

is a weighted additive convolution. Substituting (L-90703.2) expands it into an explicit finite linear combination of Goldbach-type correlations between von-Mangoldt coefficients in the four residue classes of the blocks \(4m-r\), together with the contracted \(\Lambda(a)\Lambda(b)\) terms.

Thus the exact arithmetic price of PIG is visible in two equivalent coordinates:

```text
frequency side:
    singular low-frequency cosine energy of T_n(ell)-B(n);

physical side:
    max-kernel quadratic energy
    + weighted radix-four Goldbach convolution.
```

## 5. A concrete sufficient gate

A source-specific theorem of the following form would imply a uniform-row version of PIG:

\[
\boxed{
\begin{aligned}
&\left|\sum_{m=1}^{n}(2m-n)b(m)-nc\right|^2\\
&\quad+
4\sum_{\ell=1}^{n-1}
\left[
\operatorname{Re}
\frac{T_n(\ell)-\mathcal B(n)}{1-q_\ell}
\right]^2
\ll n^2(\log n)^A.
\end{aligned}}
\tag{L-90703.22}
\]

Indeed (L-90703.12) would then give

\[
\frac1{n-1}\sum_{j=1}^{n-1}\frac{|Q_n(j)|^2}{n}
\ll(\log n)^A.
\tag{L-90703.23}
\]

The delayed gauge changes the left side by only polylogarithmic terms after Cauchy--Schwarz. A transfer from normalized counting measure to the exact positive block measure \(d\nu_J\) of `T-90302` is still required; it is not asserted here.

## 6. Proof boundary

Closed exactly, subject to review:

```text
radix-four block-prime increment                    exact
cyclic cosine diagonalisation                       exact
singular antiderivative multiplier                  exact
weighted Goldbach/max-kernel expansion              exact
uniform-row Fourier gate -> uniform-row PIG          exact
```

Open:

```text
arithmetic bound (L-90703.22)                       RH-bearing
transfer to the exact QIDR block measure            open
PIG and RH                                            unproved
```
