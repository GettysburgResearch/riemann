# L-102741 — Wick gauge and the exact prime-carrier quotient

Claim ID: `L-102741`  
Status: **PROVED EXACT FINITE-HORIZON SOURCE IDENTITY**  
Created: 2026-08-23  
Depends on: PR #699 `L-101103`; PR #719 `L-102706`, `L-102737`  
RH status: **not assumed**

Let \(\mathcal L\) be a finite labelled prime multiset. The two copies of
\(67\) remain distinct. Put

\[
 x_\ell=p_\ell^{-1/2}e^{-i\vartheta_\ell}U_\ell,
\qquad
 L=\sum_{\ell\in\mathcal L}x_\ell,
\]

and define

\[
 E=\prod_\ell(1-x_\ell),
\qquad
 S=\prod_\ell(1-x_\ell^2),
\]

\[
 R=\prod_\ell\frac{e^{x_\ell}}{1+x_\ell}.
\]

On a finite horizon every shift is nilpotent, so all series below are finite
operator identities. The one-label identity

\[
 (1-x^2)\frac{e^x}{1+x}e^{-x}=1-x
\]

gives

\[
 \boxed{E=SRe^{-L}.}
 \tag{L-102741.1}
\]

## 1. Exact defect decomposition

Subtracting the squared completion gives

\[
 \boxed{
 E-S
 =RS(e^{-L}-1)+(R-1)S.
 }
 \tag{L-102741.2}
\]

The Wick renormalizer starts in degree two:

\[
 \log R
 =\sum_\ell\sum_{m\ge2}\frac{(-1)^m}{m}x_\ell^m.
 \tag{L-102741.3}
\]

Consequently both \(R\) and \(R^{-1}\) have source total-variation norm

\[
 \|R\|_1+\|R^{-1}\|_1
 \ll (\log(2Y))^C
 \tag{L-102741.4}
\]

on every horizon \(Y\). The second labelled \(67\) changes only the constant.
This is the same subcritical gauge already used in `L-102706`.

## 2. Gauge-covariant prime carrier

The exact first-chaos term of \(RS(e^{-L}-1)\) is

\[
 \boxed{\mathcal P_{\rm W}=-RSL.}
 \tag{L-102741.5}
\]

Move this source packet once across any exact regional partition, before an
absolute value, square, radial gauge or physical collapse. The carrier-quotient
remainder is

\[
\begin{aligned}
 \mathcal D_{\ge2}
 &:=(E-S)-\mathcal P_{\rm W}\\
 &=RS(e^{-L}-1+L)+(R-1)S.
\end{aligned}
\tag{L-102741.6}
\]

The literal singleton packet of `L-102737` and the Wick carrier
\(\mathcal P_{\rm W}\) have the same degree-one source coefficient. Their
difference begins at total prime degree at least three and is transported by
the polylogarithmic gauge `R`; replacing one by the other is therefore an exact
source transfer, not an asymptotic subtraction.

## Scope

Equation (L-102741.6) removes the complete first chaos from the
conclusion-facing defect. It does not prove a physical bound for the remaining
second-and-higher chaos. That remainder is factorized in `L-102742`.