# R-90703 — The Q4 row operator has an exact linear norm loss on a sine mode

Claim ID: `R-90703`  
Status: **EXACT OPERATOR-CLASS REFUTATION**  
Created: 2026-08-11  
Depends on: `L-90703`  
Scope: refutes source-blind `ell^2`/Parseval control of the Q4 innovation; it is not a counterexample for the von-Mangoldt block source

## 1. The test source

Fix \(n\ge3\), set \(\theta=2\pi/n\), and take the real increment sequence

\[
b(m)=\sin(m\theta),
\qquad1\le m\le n.
\tag{R-90703.1}
\]

Let

\[
\mathcal B(j)=\sum_{m=1}^{j}b(m),
\qquad
Q_n(j)=\mathcal B(n)-\mathcal B(j)-\mathcal B(n-j)
\quad(1\le j<n).
\tag{R-90703.2}
\]

Here \(\mathcal B(n)=0\), so the constant mode and the genuine arithmetic source play no role.

## 2. Exact Fourier calculation

For \(q=e^{-2\pi i/n}\),

\[
T_n(1)=\sum_{m=1}^{n}b(m)q^m=-\frac{in}{2},
\qquad
T_n(n-1)=\frac{in}{2},
\tag{R-90703.3}
\]

and every other nonzero Fourier coefficient of \(b\) vanishes. Since

\[
\frac1{1-e^{-i\theta}}
=\frac12-\frac i2\cot\frac\theta2,
\tag{R-90703.4}
\]

`L-90703` gives

\[
\operatorname{Re}\widehat{\mathcal B}_n(1)
=\operatorname{Re}\widehat{\mathcal B}_n(n-1)
=-\frac n4\cot\frac\pi n.
\tag{R-90703.5}
\]

Moreover

\[
\sum_{j=0}^{n-1}\mathcal B(j)
=\frac n2\cot\frac\pi n,
\tag{R-90703.6}
\]

so the zero mode in (L-90703.10) is \(-n\cot(\pi/n)\). Parseval therefore yields the exact row energy

\[
\boxed{
\sum_{j=1}^{n-1}|Q_n(j)|^2
=\frac32 n\cot^2\frac\pi n.
}
\tag{R-90703.7}
\]

On the other hand

\[
\sum_{m=1}^{n}|b(m)|^2=\frac n2.
\tag{R-90703.8}
\]

Hence the operator taking increments to the reflected cumulative row satisfies

\[
\boxed{
\frac{\|Q_n\|_2}{\|b\|_2}
=\sqrt3\cot\frac\pi n
\sim\frac{\sqrt3}{\pi}n.
}
\tag{R-90703.9}
\]

## 3. Consequence

Any argument which first forgets the arithmetic structure of

\[
b(m)=\sum_{r=0}^3\Lambda(4m-r)-4\Lambda(m)
\]

and uses only an unweighted bound for \(\sum|b(m)|^2\) necessarily loses one complete factor of \(n\) in norm. This is the exact spectral source of the generic firewall `R-90406`.

Therefore none of the following can prove PIG by itself:

```text
Parseval for the block-prime coefficients;
the ordinary von-Mangoldt second moment;
a source-blind discrete Sobolev inequality;
Cauchy--Schwarz before radix-four prime cancellation.
```

The remaining theorem must suppress the sine-like low modes of the **specific** block-prime source, or equivalently control the weighted Goldbach correlation of `L-90703.20` with its exact signs intact.

This result does not assert that the actual von-Mangoldt source contains the sine adversary. It is an operator-class no-go only.
