# L-102106 — One half-completed Haar field dominates both carrier-free Perron channels

Claim ID: `L-102106`  
Status: **PROVED EXACT FACTORIZATION AND HILBERT BOUND**  
Created: 2026-08-21  
Depends on: `L-102103--L-102105`; PR #702 `L-103100--L-103103`  
RH status: **not assumed**

Let

\[
\widehat\psi(s)={(1-2^{-s})(1-\sqrt2\,2^{-s})\over s}
\]

be the ratio-four half-completed Haar multiplier of PR #702.  Let `B` be the
positive five-box spline of `L-102104`, and let

\[
K_A^\dagger=-{1\over3}D(D-1/2)^2B,
\qquad
K_Q^\dagger={1\over6}(D-1/2)(2D^2+5D+9)B.
\]

Put

\[
C=b_0^{*2}*b_{1/2}\ge0.
\]

Its multiplier is

\[
\widehat C(s)=
\left({1-2^{-s}\over s}\right)^2
{1-\sqrt2\,2^{-s}\over s-1/2}.
\]

Define

\[
R_A=-{1\over3}D(D-1/2)C,
\qquad
R_Q={1\over6}(2D^2+5D+9)C.
\]

Then exact multiplier cancellation gives

\[
\boxed{K_A^\dagger=\psi *_M R_A,
\qquad K_Q^\dagger=\psi *_M R_Q.}
\tag{L-102106.1}
\]

Moreover, on the Fourier line `s=i gamma`,

\[
{\widehat R_A(s)\over\widehat\psi(s)}
=-{1\over3}(1-2^{-s}),
\]

so

\[
\boxed{\|h*_M R_A\|_2\le {2\over3}\|h*_M\psi\|_2.}
\tag{L-102106.2}
\]

For the second channel,

\[
{\widehat R_Q(s)\over\widehat\psi(s)}
={1\over6}(2s^2+5s+9)
{1-2^{-s}\over s(s-1/2)}.
\tag{L-102106.3}
\]

This multiplier is bounded on the imaginary axis.  The elementary estimates

\[
\left|{1-e^{-i\gamma\log2}\over i\gamma}\right|
\le\min\{\log2,2/|\gamma|\}
\]

together with a split at `|gamma|=1` give the safe uniform bound

\[
\boxed{\|h*_M R_Q\|_2\le4\|h*_M\psi\|_2.}
\tag{L-102106.4}
\]

Now let the balanced Vaughan coefficient be `h_U*h_U`, as in PR #696.  By
associativity,

\[
(h_U*h_U)*K_i^\dagger
=(h_U*\psi)*_M(h_U*R_i),
\qquad i\in\{A,Q\}.
\]

Cauchy--Schwarz therefore yields, at every endpoint,

\[
\boxed{|B_A^\dagger(X)|\le {2\over3}\mathcal H_U(X),
\qquad |B_Q^\dagger(X)|\le4\mathcal H_U(X),}
\tag{L-102106.5}
\]

where `mathcal H_U` is the half-completed Haar field energy of PR #702.  The
finite duplicate-67 difference changes only the absolute constant.

Consequently `HCNC103100` controls both coordinates of the carrier-free joint
Perron packet, not merely the original scalar Vaughan coordinate.
