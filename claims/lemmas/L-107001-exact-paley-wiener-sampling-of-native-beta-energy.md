# L-107001 — The native beta energy has an exact Nyquist lattice

Claim ID: `L-107001`  
Status: **PROVED EXACT PALEY--WIENER SAMPLING THEOREM**  
Created: 2026-08-27  
Depends on: `L-107000`  
RH status: **not assumed**

Let \(B=B_{r,\log}\) and let \(S_B\) be its fixed causal support length. Put

\[
H_X(u)
=
\sum_{n\le X}
\frac{\beta(n)}{\sqrt n}
B(u-\log n).
\tag{L-107001.1}
\]

Then

\[
\operatorname{supp}H_X
\subset[0,\log X+S_B].
\]

Choose

\[
P_X=\log X+S_B+1
\]

and define the deterministic frequency lattice

\[
t_{k,X}=\frac{2\pi k}{P_X},
\qquad k\in\mathbf Z.
\tag{L-107001.2}
\]

The Fourier transform is

\[
\widehat H_X(t)
=
\widehat B(it)D_X(t).
\tag{L-107001.3}
\]

Extend \(H_X\) by zero to an interval of length \(P_X\). Its Fourier-series
coefficient at \(k\) is \(P_X^{-1}\widehat H_X(t_{k,X})\). Parseval therefore
gives the exact identity

\[
\boxed{
\mathcal E_{r,\log}(X)
=
\frac1{P_X}
\sum_{k\in\mathbf Z}
\left|
\widehat B(it_{k,X})
D_X(t_{k,X})
\right|^2.
}
\tag{L-107001.4}
\]

There is no discretization error and no random sampling.

## 1. Every-power truncation

For \(A>0\), let \(T_A(X)\) be as in `L-107000` and put

\[
K_A(X)
=
\left\lceil
\frac{P_XT_A(X)}{2\pi}
\right\rceil.
\tag{L-107001.5}
\]

The same monotone tail bound used in `L-107000`, together with
\(P_X^{-1}=(2\pi/P_X)/(2\pi)\), gives

\[
\boxed{
\frac1{P_X}
\sum_{|k|>K_A(X)}
\left|
\widehat B(it_{k,X})
D_X(t_{k,X})
\right|^2
=
O_A(X^{-A}).
}
\tag{L-107001.6}
\]

Consequently

\[
\boxed{
\mathcal E_{r,\log}(X)
=
\frac1{P_X}
\sum_{|k|\le K_A(X)}
\left|
\widehat B(it_{k,X})
D_X(t_{k,X})
\right|^2
+
O_A(X^{-A}).
}
\tag{L-107001.7}
\]

The number of retained samples is

\[
\boxed{
2K_A(X)+1
=
O_A\!\left(
(\log X)^2
[\log\log(e^eX)]^2
\right).
}
\tag{L-107001.8}
\]

## 2. Explicit finite-rank Gram

Define

\[
\mathbf v_X(n)
=
\frac1{\sqrt{P_X}}
\left(
\widehat B(it_{k,X})n^{-it_{k,X}}
\right)_{|k|\le K_A(X)}.
\tag{L-107001.9}
\]

Then the truncated energy is exactly

\[
\boxed{
\left\|
\sum_{n\le X}
\frac{\beta(n)}{\sqrt n}
\mathbf v_X(n)
\right\|_{\mathbf C^{2K_A(X)+1}}^2.
}
\tag{L-107001.10}
\]

Equivalently, it is a positive Gram form of rank at most

\[
O_A((\log X)^2(\log\log X)^2).
\]

Every source coefficient remains the literal individual-zeta beta
coefficient. No family average, positive completion, owner surrogate, or
principal-member extraction is used.

## 3. Exact multiplicative phase coordinate

The components have the explicit form

\[
n^{-it_{k,X}}
=
\exp\left(
-\frac{2\pi ik\log n}{P_X}
\right).
\tag{L-107001.11}
\]

Thus the conclusion-facing arithmetic object is one deterministic
almost-quadratic-dimensional Fourier feature vector of the native beta
measure on logarithmic scale.
