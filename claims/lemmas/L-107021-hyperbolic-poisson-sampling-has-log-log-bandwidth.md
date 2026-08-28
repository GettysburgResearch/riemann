# L-107021 — Hyperbolic Poisson sampling has logarithmic-by-logarithmic bandwidth

Claim ID: `L-107021`  
Status: **PROVED UNCONDITIONAL SAMPLING THEOREM**  
Created: 2026-08-27  
Depends on: `L-107020`  
RH status: **not assumed**

Let

\[
H_{\star;X}(u)
=\sum_{n\le X}{\beta(n)\over\sqrt n}B_\star(u-\log n),
\]

so

\[
H_{{\rm hyp};X}=h*H_{\star;X}.
\]

If \(S_\star\) is the fixed support length of \(B_\star\), then

\[
\operatorname{supp}H_{\star;X}\subset[0,L_X],
\qquad
L_X=\log X+S_\star.
\tag{L-107021.1}
\]

Fix \(A>0\). Put

\[
R_A(X)=C_A\log(eX),
\qquad
P_A(X)=L_X+2R_A(X),
\tag{L-107021.2}
\]

and

\[
t_{k,X}={2\pi k\over P_A(X)}.
\tag{L-107021.3}
\]

Then

\[
\boxed{
\mathcal E_{\rm hyp}(X)
={1\over P_A(X)}
\sum_{k\in\mathbb Z}
\left|
 e^{1-\cosh t_{k,X}}
 \widehat B_\star(it_{k,X})
 D_X(t_{k,X})
\right|^2
+O_A(X^{-A}).
}
\tag{L-107021.4}
\]

## 1. Poisson aliases

For a Schwartz function \(F\),

\[
{1\over P}\sum_{k\in\mathbb Z}
 |\widehat F(2\pi k/P)|^2
=\sum_{\ell\in\mathbb Z}
 \langle F,\tau_{\ell P}F\rangle.
\tag{L-107021.5}
\]

The compact-prefix autocorrelation \(\mathcal R_{\star;X}\) is supported in
\([-L_X,L_X]\), and

\[
\|\mathcal R_{\star;X}\|_1
\le\|H_{\star;X}\|_1^2
\ll X.
\tag{L-107021.6}
\]

Since

\[
\mathcal R_{{\rm hyp};X}
=\gamma*\mathcal R_{\star;X}
\]

and \(|\gamma(u)|\ll e^{-|u|}\), every nonzero alias obeys

\[
|\mathcal R_{{\rm hyp};X}(\ell P_A)|
\ll X
 e^{-[2R_A+(|\ell|-1)P_A]}.
\]

Choosing \(C_A\) sufficiently large gives

\[
\boxed{
\sum_{\ell\ne0}
|\mathcal R_{{\rm hyp};X}(\ell P_A)|
=O_A(X^{-A}).
}
\tag{L-107021.7}
\]

This proves (L-107021.4).

## 2. Double-exponential spectral deletion

The Fourier transform is

\[
\widehat H_{{\rm hyp};X}(t)
=e^{1-\cosh t}\widehat B_\star(it)D_X(t).
\tag{L-107021.8}
\]

The fixed compact detector has bounded Fourier transform and
\(|D_X(t)|\le4\sqrt X\). For \(t\ge1\),

\[
\cosh t\ge e^t/3.
\]

Set

\[
\boxed{
T_A(X)=\log\log(e^eX)+C'_A
}
\tag{L-107021.9}
\]

with \(C'_A\) sufficiently large, and

\[
K_A(X)=
\left\lceil{P_A(X)T_A(X)\over2\pi}\right\rceil.
\tag{L-107021.10}
\]

A monotone sum--integral comparison gives

\[
\boxed{
{1\over P_A(X)}
\sum_{|k|>K_A(X)}
\left|
 e^{1-\cosh t_{k,X}}
 \widehat B_\star(it_{k,X})
 D_X(t_{k,X})
\right|^2
=O_A(X^{-A}).
}
\tag{L-107021.11}
\]

Consequently

\[
\boxed{
\mathcal E_{\rm hyp}(X)
={1\over P_A(X)}
\sum_{|k|\le K_A(X)}
\left|
 e^{1-\cosh t_{k,X}}
 \widehat B_\star(it_{k,X})
 D_X(t_{k,X})
\right|^2
+O_A(X^{-A}).
}
\tag{L-107021.12}
\]

Finally,

\[
P_A(X)=O_A(\log X)
\]

and therefore

\[
\boxed{
2K_A(X)+1
=O_A(\log X\,\log\log(e^eX)).
}
\tag{L-107021.13}
\]

The equality is approximate only through an every-power physical-alias and
spectral-tail error. No exact compact-support Nyquist statement is claimed.
