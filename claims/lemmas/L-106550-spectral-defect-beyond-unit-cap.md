# L-106550 — Spectral defect beyond the unit Frobenius cap

Claim ID: `L-106550`  
Status: **PROVED EXACT FINITE SPECTRAL INEQUALITY**  
Created: 2026-08-25  
Depends on: `L-105210`  
RH status: **not assumed**

Let \(M\succeq0\) be an \(m\times m\) Hermitian matrix with
\(\operatorname{tr}M=m\). Put

\[
E(M)=\operatorname{tr}(M-I)^2
\]

and

\[
\Delta(M)=\operatorname{tr}\Psi(M),
\qquad
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

The earlier seven-gap argument used only

\[
\Delta(M)\ge \min\{E(M),1\}.
\]

The following sharp local refinement crosses that unit cap.

## 1. One-spike lower envelope

Write the eigenvalues of \(M\) as \(1+x_1,\ldots,1+x_m\). Then

\[
x_j\ge-1,\qquad
\sum_jx_j=0,\qquad
\sum_jx_j^2=E.
\]

If \(E<2\), at most one coordinate can exceed \(1\).

If no coordinate exceeds \(1\), then \(\Delta=E\). If exactly one coordinate,
say \(a=x_1>1\), exceeds \(1\), then

\[
\Delta
=
2a-1+\sum_{j\ge2}x_j^2
=
E-(a-1)^2.
\]

Cauchy--Schwarz on the remaining \(m-1\) coordinates gives

\[
E-a^2
\ge
\frac{a^2}{m-1},
\]

so

\[
a\le\sqrt{\frac{m-1}{m}E}.
\]

Consequently, for \(E<2\),

\[
\boxed{
\Delta(M)\ge
\phi_m(E):=
\begin{cases}
E,&0\le E\le \dfrac{m}{m-1},\\[2mm]
2\sqrt{\dfrac{m-1}{m}E}-1+\dfrac Em,
&\dfrac{m}{m-1}\le E<2.
\end{cases}
}
\tag{L-106550.1}
\]

Equality in the second line is attained by the equicorrelation spectrum

\[
1+a,\quad
1-\frac{a}{m-1},\ldots,
1-\frac{a}{m-1}.
\]

Thus (L-106550.1) is the exact spectral lower envelope in the one-spike range.

## 2. Energies above two

If \(E\ge2\), then

\[
\boxed{\Delta(M)\ge2\sqrt2-1.}
\tag{L-106550.2}
\]

Indeed:

- with no coordinate above \(1\), \(\Delta=E\ge2\);
- with at least two coordinates above \(1\), those coordinates alone
  contribute more than \(2\);
- with one coordinate \(a>1\), either \(a\ge\sqrt2\), giving
  \(\Delta\ge2a-1\ge2\sqrt2-1\), or \(1<a<\sqrt2\), giving
  \[
  \Delta
  \ge2a-1+(2-a^2)
  =1+2a-a^2
  \ge2\sqrt2-1.
  \]

## 3. Pressure with a nonnegative span variable

Let \(z\ge0\) and let

\[
\frac{m}{m-1}<q<2.
\]

Assume \(\phi_m(q)\le2\sqrt2-1\). Then

\[
\boxed{
E(M)+z\ge q
\quad\Longrightarrow\quad
\Delta(M)+z\ge\phi_m(q).
}
\tag{L-106550.3}
\]

For \(E\ge q\), use monotonicity of \(\phi_m\), together with
(L-106550.2) when \(E\ge2\). For \(E<q\), use \(z\ge q-E\) and the fact that

\[
\phi_m(E)-E
=
-\left(\sqrt{\frac{m-1}{m}E}-1\right)^2
\]

is nonincreasing after the transition \(m/(m-1)\), while it is zero before
that transition.

Equation (L-106550.3) is the exact mechanism that permits a certified local
pressure slightly larger than one to contribute more than one unit of
spectral defect.
