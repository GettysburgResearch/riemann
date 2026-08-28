# L-107020 — A hyperbolic zero-free smoother preserves the native beta RH criterion

Claim ID: `L-107020`  
Status: **PROVED UNCONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-27  
Base: PR #759 at `d1b8aa57b08db1ba9f2edf3b68238c2a129b7c33`  
RH status: **not assumed**

Use the Fourier convention

\[
\widehat f(t)=\int_{\mathbb R}f(u)e^{-itu}\,du.
\]

Define the fixed even multiplier

\[
\boxed{\widehat h(t)=\exp(1-\cosh t).}
\tag{L-107020.1}
\]

Then \(h\) is a real even Schwartz function, \(\int h=1\), and its
bilateral Laplace transform is

\[
\boxed{
\mathcal Lh(s)
=\int_{\mathbb R}h(u)e^{-su}\,du
=\exp(1-\cos s).
}
\tag{L-107020.2}
\]

The multiplier is entire and zero-free.

Let \(B_\star=B_{1,0}\) be the fixed compact causal native-beta detector from
PR #758, and define

\[
\boxed{B_{\rm hyp}=h*B_\star.}
\tag{L-107020.3}
\]

For

\[
\beta=(\delta_1-\delta_{67})*\mu
\]

put

\[
H_{{\rm hyp};X}(u)
=\sum_{n\le X}{\beta(n)\over\sqrt n}
 B_{\rm hyp}(u-\log n),
\qquad
\mathcal E_{\rm hyp}(X)=\|H_{{\rm hyp};X}\|_2^2.
\tag{L-107020.4}
\]

Then

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathcal E_{\rm hyp}(X)=X^{o(1)}.
}
\tag{L-107020.5}
\]

## 1. Exponential physical tails

Fix \(0<\sigma<\pi/2\). For \(u>0\), shift the Fourier contour from
\(\mathbb R\) to \(\mathbb R+i\sigma\). Since

\[
\Re\cosh(t+i\sigma)=\cosh t\cos\sigma>0,
\]

one obtains

\[
|h^{(j)}(u)|
\le C_{\sigma,j}e^{-\sigma u}.
\]

Shifting downward gives the same estimate for \(u<0\). Thus

\[
\boxed{
|h^{(j)}(u)|\le C_{\sigma,j}e^{-\sigma|u|}
\qquad(0<\sigma<\pi/2).
}
\tag{L-107020.6}
\]

The autocorrelation

\[
\gamma=h*\widetilde h,
\qquad
\widehat\gamma(t)=\exp(2-2\cosh t),
\]

satisfies the same family of exponential bounds.

In particular one may fix once and for all

\[
\boxed{\sigma_0=1>1/2.}
\tag{L-107020.7}
\]

## 2. Exact pole preservation

The fixed detector multiplier is

\[
\boxed{
\widehat B_{\rm hyp}(s)
=\exp(1-\cos s)\widehat B_\star(s).
}
\tag{L-107020.8}
\]

Initially in the absolutely convergent half-plane, the bilateral transform of
the complete field is

\[
\boxed{
\mathcal B H_{\rm hyp}(s)
=\widehat B_{\rm hyp}(s)
 {1-67^{-(s+1/2)}\over\zeta(s+1/2)}.
}
\tag{L-107020.9}
\]

The new multiplier is zero-free, so it cancels no hypothetical open-strip
pole.

Because \(B_{\rm hyp}\) is noncausal, the one-sided transform differs from
(L-107020.9) by the negative-time correction

\[
E_-(s)=\int_{-\infty}^0H_{\rm hyp}(u)e^{-su}\,du.
\]

The exponential bound (L-107020.6), the causal support of \(B_\star\), and
the trivial beta bound show that \(H_{\rm hyp}(u)\ll e^{\sigma_0u}\) as
\(u\to-\infty\). Hence \(E_-\) is holomorphic in the half-plane
\(\Re s<\sigma_0\). Since \(\sigma_0=1\), this contains the complete
detector strip \(0<\Re s<1/2\). Therefore the one-sided transform retains
every hypothetical open-strip pole. This correction is explicit; no causal
identity is silently reused.

## 3. RH implies the energy estimate

Let \(H_{\star;X}\) be the fixed compact-detector prefix field. Then

\[
H_{{\rm hyp};X}=h*H_{\star;X}.
\]

Since \(h\in L^1\), Young's inequality gives

\[
\mathcal E_{\rm hyp}(X)
\le\|h\|_1^2\mathcal E_\star(X).
\]

The source-locked theorem on PR #758 proves
\(\mathcal E_\star(X)=X^{o(1)}\) under RH.

## 4. The energy estimate implies RH

Let \(H_\star\) be the complete causal compact-detector field. Trivially,

\[
|H_\star(v)|\ll e^{v/2}
\qquad(v\ge0).
\tag{L-107020.10}
\]

Fix \(T\) and set

\[
R_T=6T,
\qquad
X_T=e^{T+R_T}=e^{7T}.
\tag{L-107020.11}
\]

For \(0\le u\le T\), the source terms omitted by the \(X_T\)-prefix lie at
physical times \(v\ge T+R_T\). Using \(\sigma_0=1\),

\[
\int_{T+R_T}^{\infty}
 |h(u-v)|\,|H_\star(v)|\,dv
\ll e^{-2T}.
\tag{L-107020.12}
\]

If \(\mathcal E_{\rm hyp}(X)=X^{o(1)}\), then

\[
\int_0^T|H_{\rm hyp}(u)|^2du=e^{o(T)}.
\]

Cauchy--Schwarz gives subexponential negative logarithmic mass. The
source-locked one-sided Mellin--Landau argument applies to the one-sided
transform described in Section 2: its negative part is holomorphic in
\(\Re s>0\), its positive part has finite Laplace abscissa, and every
hypothetical open-strip reciprocal-zeta pole survives. Therefore RH follows.

## Scope

The kernel is fixed, noncompact, real and Schwartz. Its noncausal physical
tail and the negative-time transform correction are both paid explicitly.
The theorem does not use an \(X\)-dependent filter.
