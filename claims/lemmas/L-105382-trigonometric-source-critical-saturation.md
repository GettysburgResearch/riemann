# L-105382 — Trigonometric models exactly saturate source–critical Stieltjes capacity

Claim ID: `L-105382`  
Status: **PROVED EXACT MODEL THEOREM**  
Created: 2026-08-23  
Depends on: `L-105370`, `L-105372`  
RH status: **not assumed**

## 1. Odd model

Fix `omega>0` and put

\[
F_{\rm odd}(z)=\sin(\omega z).
\]

Then

\[
{F_{\rm odd}(z)\over F_{\rm odd}'(z)}
={\tan(\omega z)\over\omega}.
\tag{L-105382.1}
\]

The classical Mittag--Leffler expansion is

\[
\boxed{
{\tan y\over y}
=
\sum_{j=0}^{\infty}
{8\over\pi^2(2j+1)^2}
{1\over1-{4y^2\over\pi^2(2j+1)^2}}.
}
\tag{L-105382.2}
\]

Hence the origin source sequence is the Stieltjes moment sequence of

\[
\boxed{
\nu_{\rm odd,\omega}
=
\sum_{j=0}^{\infty}
W_j^{\rm odd}\delta_{s_j^{\rm odd}},
}
\tag{L-105382.3}
\]

where

\[
\boxed{
W_j^{\rm odd}={8\over\pi^2(2j+1)^2},
\qquad
s_j^{\rm odd}={4\omega^2\over\pi^2(2j+1)^2}.
}
\tag{L-105382.4}
\]

Indeed,

\[
{F_{\rm odd}(z)\over zF_{\rm odd}'(z)}
=
\int_{[0,\infty)}{d\nu_{\rm odd,\omega}(s)\over1-sz^2}.
\tag{L-105382.5}
\]

The positive critical points are

\[
c_j^{\rm odd}={\pi(2j+1)\over2\omega},
\qquad j\ge0,
\]

and every critical residue is

\[
\rho_j^{\rm odd}
={F(c_j)\over F''(c_j)}
=-{1\over\omega^2}.
\tag{L-105382.6}
\]

Therefore the critical atom attached by `L-105370` is

\[
{1\over(c_j^{\rm odd})^2}=s_j^{\rm odd},
\qquad
{-2\rho_j^{\rm odd}\over(c_j^{\rm odd})^2}
=W_j^{\rm odd}.
\tag{L-105382.7}
\]

Thus the complete odd source measure and the complete positive critical atom
measure are identical.

## 2. Even model

Put

\[
F_{\rm even}(z)=\cos(\omega z).
\]

Then

\[
{F_{\rm even}(z)\over F_{\rm even}'(z)}
=-{\cot(\omega z)\over\omega}.
\]

The central critical residue is `rho_0=-omega^(-2)`. After removing it,

\[
\widehat m_{\rm even}(z)
=-{\cot(\omega z)\over\omega}
+{1\over\omega^2z}.
\tag{L-105382.8}
\]

The classical cotangent expansion gives

\[
\boxed{
{1\over y^2}-{\cot y\over y}
=
\sum_{j=1}^{\infty}
{2\over\pi^2j^2}
{1\over1-{y^2\over\pi^2j^2}}.
}
\tag{L-105382.9}
\]

Hence

\[
{\widehat m_{\rm even}(z)\over z}
=
\int_{[0,\infty)}{d\nu_{\rm even,\omega}(s)\over1-sz^2},
\tag{L-105382.10}
\]

where

\[
\boxed{
\nu_{\rm even,\omega}
=
\sum_{j=1}^{\infty}
W_j^{\rm even}\delta_{s_j^{\rm even}},
}
\tag{L-105382.11}
\]

with

\[
\boxed{
W_j^{\rm even}={2\over\pi^2j^2},
\qquad
s_j^{\rm even}={\omega^2\over\pi^2j^2}.
}
\tag{L-105382.12}
\]

The nonzero positive critical points are

\[
c_j^{\rm even}={\pi j\over\omega},
\qquad j\ge1,
\]

and again `rho_j=-omega^(-2)`. Therefore their critical atoms are exactly
`(W_j^{even},s_j^{even})`.

## 3. Finite-window boundary reserve is a positive tail

Let a parity-symmetric regular window contain precisely the first `N` positive
critical pairs of either model, together with the central pole in the even
case. The exact source–critical split gives

\[
\boxed{
\nu_{\rm boundary,N}
=
\sum_{j>N}W_j\delta_{s_j}\ge0.
}
\tag{L-105382.13}
\]

Consequently every finite-window boundary Stieltjes matrix is positive
semidefinite at every order. Moreover, for every fixed moment order `n`,

\[
\boxed{
\beta_n(N)=\sum_{j>N}W_js_j^n\longrightarrow0.
}
\tag{L-105382.14}
\]

Thus the trigonometric models satisfy `AATR105360` with affine coefficient
`a=0`, and in fact satisfy the stronger exact positive-tail version at every
finite window.

## 4. Strict source positivity

The source measures have infinitely many distinct positive support points.
Therefore both the ordinary and shifted source Hankel matrices are positive
definite at every finite order:

\[
\boxed{
\mathsf A_k^{(0)}\succ0,
\qquad
\mathsf A_k^{(1)}\succ0
\quad(k\ge1).
}
\tag{L-105382.15}
\]

Indeed, the quadratic form is the integral of `q(s)^2`, respectively
`sq(s)^2`, against a positive measure with infinite support; a nonzero finite
polynomial cannot vanish on the entire support.

## 5. Exact saturation

For an exhaustion containing all critical pairs,

\[
\boxed{
\mathsf C_{k,\infty}^{(a)}
=
\mathsf A_k^{(a)},
\qquad
\mathsf S_{k,\infty}^{(a)}=0.
}
\tag{L-105382.16}
\]

Equivalently, the normalized critical-capacity operator is exactly the identity
at every order:

\[
\boxed{
(\mathsf A_k^{(a)})^{-1/2}
\mathsf C_{k,\infty}^{(a)}
(\mathsf A_k^{(a)})^{-1/2}
=I_k.
}
\tag{L-105382.17}
\]

The trigonometric high-derivative model sits on the boundary of the sharp
source–critical capacity cone, with no negative square and no unused terminal
reserve.

## 6. Scope

This theorem is an exact calibration, not an Xi approximation theorem. To use
it for Xi one must prove sufficiently strong convergence of both the origin
source germ and the complete critical atom measure, including their tails.
Relative phase or residue asymptotics alone do not automatically control the
capacity difference. No low-order descent or RH conclusion is claimed.
