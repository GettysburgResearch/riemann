# R-106700 — Positive source, a real-rooted fifth derivative, and vanishing pole height do not imply MESOTRANS

Claim ID: `R-106700`  
Status: **PROVED EXACT COUNTERMODEL**  
Created: 2026-08-27  
RH status: **unproved**

Fix `c>1` and an integer `n>=1`, and put

\[
F_n(t)=c+\cos(nt).
\]

Its Fourier source is the positive even measure

\[
c\,\delta_0+\frac12\delta_n+\frac12\delta_{-n}.
\]

Moreover,

\[
F_n^{(5)}(t)=-n^5\sin(nt)
\]

has only simple real zeros, while `F_n` has no real zero.

Choose

\[
\lambda_n=\frac1n.
\]

Writing `z=e^{int}`, the fifth-endpoint quotient is

\[
\begin{aligned}
U_n(t)
&=\frac{(F_n-i\lambda_nF_n')(F_n^{(5)}+i\lambda_nF_n^{(6)})}
        {(F_n+i\lambda_nF_n')(F_n^{(5)}-i\lambda_nF_n^{(6)})}\\
&=-\frac{z+c}{z(cz+1)}
=-\frac1{z\,b_{-1/c}(z)},
\end{aligned}
\]

where

\[
b_{-1/c}(z)=\frac{z+1/c}{1+z/c}.
\]

Thus, on each period, the reduced numerator inner factor is constant and the denominator inner factor has degree two. Hence

\[
\boxed{-\operatorname{wind}U_n=2,\qquad\|H_{U_n}\|_{\mathcal S_2}^2=2.}
\tag{R-106700.1}
\]

The exact primal transport has no numerator model direction available, so

\[
\boxed{\inf_X\mathcal R_n(X)=2}
\tag{R-106700.2}
\]

per period.

The nontrivial finite Blaschke zero has height

\[
\frac{\log c}{n}\longrightarrow0.
\]

Also the fifth Wronskian has positive Fourier source:

\[
F_n'F_n^{(5)}-F_nF_n^{(6)}=n^6(1+c\cos nt),
\]

whose Fourier coefficients are nonnegative. Nevertheless the transport cost has density one relative to the fifth-derivative zero count.

Therefore the following collection does not imply `MESOTRANS106630`:

```text
positive even Fourier source;
positive fifth-Wronskian Fourier source;
all fifth-derivative zeros real and simple;
carrier-matched companion scale;
vanishing finite pole height;
exact endpoint all-pass algebra.
```

A proof for Xi must use a genuinely arithmetic microscopic correlation statement. None of the source-positive or macroscopic-height inputs can supply it by formal composition alone.
