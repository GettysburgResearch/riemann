# L-91320 — The delayed carrier family has exactly one weighted half-line defect

Claim ID: `L-91320`  
Status: **PROVED EXACT DISTRIBUTIONAL FORM-CORE THEOREM**  
Created: 2026-08-13  
Depends on: `R-91008`, `L-91034`  
Upgrades: the proposed half-line closure `L-91034.12`  
RH status: **unproved**

## 1. Abstract theorem

Let `rho>0` and let

\[
 \psi\in C^1([0,\infty))\cap C^\omega((0,\infty))
\]

be nonzero, satisfy `psi(0)=0`, and obey, for some integer `N`,

\[
 |\psi(t)|+|\psi'(t)|
 \le C(1+t)^N e^{-\rho t}
 \qquad(t\ge0).
 \tag{L-91320.1}
\]

Fix

\[
 0<\eta<2\rho
\]

and put

\[
 \mathcal H_{\eta,+}
 =L^2((0,\infty),e^{\eta t}dt).
 \tag{L-91320.2}
\]

For `x in R` and `tau>=0`, define

\[
 g_{x,\tau}(t)
 =e^{ixt}\psi(t-\tau)\mathbf1_{t>\tau},
 \qquad
 f_{x,\tau}=-i\,Dg_{x,\tau}.
 \tag{L-91320.3}
\]

Because `psi(0)=0`, the distributional derivative has no endpoint Dirac mass.
The decay assumption gives `f_(x,tau) in H_(eta,+)`, and

\[
 \int_0^\infty f_{x,\tau}(t)dt=0.
 \tag{L-91320.4}
\]

Then

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_{\eta,+}}
 \{f_{x,\tau}:x\in\mathbb R,\ \tau\ge0\}
 =\ker\ell_+,
 \qquad
 \ell_+(f)=\int_0^\infty f(t)dt.
 }
 \tag{L-91320.5}
\]

Equivalently, the orthogonal complement is exactly

\[
 \boxed{
 \operatorname{span}\{e^{-\eta t}\}.
 }
 \tag{L-91320.6}
\]

The same conclusion holds if, for every carrier `x`, the orthogonality
information is available for almost every delay `tau>0`.  A countable dense
carrier set and continuity in `x` produce one common full-measure set of good
delays.

## 2. The integral defect is bounded

The functional `ell_+` is bounded on `H_(eta,+)` because

\[
 |\ell_+(f)|
 \le \|f\|_{\mathcal H_{\eta,+}}
 \left(\int_0^\infty e^{-\eta t}dt\right)^{1/2}.
 \tag{L-91320.7}
\]

Its Riesz vector is

\[
 q_+(t)=e^{-\eta t},
 \qquad
 \|q_+\|^2=\eta^{-1}.
 \tag{L-91320.8}
\]

Equation (L-91320.4) therefore proves the easy inclusion in (L-91320.5).

## 3. Orthogonality gives a genuine distributional product identity

Let `h in H_(eta,+)` be orthogonal to every `f_(x,tau)` and define the locally
integrable distribution

\[
 H(t)=e^{\eta t}h(t).
 \tag{L-91320.9}
\]

First take the intersection of the full-measure good-delay sets for rational
carriers.  For a fixed surviving delay, the carrier pairing is continuous in
`x` by dominated convergence on compact carrier intervals, so it vanishes for
every real `x`.  Fix such a delay `tau`.  Integration by parts in distributions
gives

\[
 0
 =\langle h,f_{x,\tau}\rangle_{\mathcal H_{\eta,+}}
 =-i\left\langle
  DH,
  e^{-ixt}\overline{\psi(t-\tau)}\mathbf1_{t>\tau}
 \right\rangle.
 \tag{L-91320.10}
\]

Hence the Fourier transform of

\[
 T_\tau
 =\overline{\psi(\,\cdot-\tau)}\mathbf1_{(\tau,\infty)}DH
 \tag{L-91320.11}
\]

vanishes on the real line.

This Fourier statement is legitimate, rather than formal.  Indeed

\[
 T_\tau
 =D\left(
  \overline{\psi(\,\cdot-\tau)}\mathbf1_{(\tau,\infty)}H
 \right)
 -\overline{\psi'(\,\cdot-\tau)}\mathbf1_{(\tau,\infty)}H,
 \tag{L-91320.12}
\]

with no endpoint mass because `psi(0)=0`.  Both functions on the right before
taking `D` belong to `L^1`: Cauchy--Schwarz reduces this to

\[
 \int_\tau^\infty
 e^{\eta t}|\psi(t-\tau)|^2dt<\infty,
 \qquad
 \int_\tau^\infty
 e^{\eta t}|\psi'(t-\tau)|^2dt<\infty,
 \tag{L-91320.13}
\]

which follows from `eta<2rho`.  Thus `T_tau` is tempered.  Injectivity of the
Fourier transform on tempered distributions yields

\[
 \boxed{T_\tau=0.}
 \tag{L-91320.14}
\]

## 4. The delay fibre removes every point-supported obstruction

Fix `t_0>0`.  The zeros of the nonzero analytic function `psi` in `(0,t_0)` are
discrete.  If the good-delay set is all of `(0,infinity)`, choose
`r in (0,t_0)` with `psi(r) != 0` and set `tau=t_0-r`.

If only almost every delay is good, the set of

\[
 r\in(0,t_0)
 \quad\text{such that}\quad
 t_0-r\text{ is good and }\psi(r)\ne0
\]

still has full measure minus a discrete set and is nonempty.  In either case,
there is a good `tau` for which

\[
 \psi(t_0-\tau)\ne0.
\]

The multiplier in (L-91320.11) is then nonzero on a neighborhood of `t_0`.
Multiplying (L-91320.14) there by its smooth reciprocal gives

\[
 DH=0
\]

near `t_0`.  Since `t_0` was arbitrary,

\[
 DH=0\quad\text{on }(0,\infty).
 \tag{L-91320.15}
\]

Therefore `H` is constant and

\[
 h(t)=Ce^{-\eta t}.
 \tag{L-91320.16}
\]

Conversely, this vector is orthogonal to every delayed derivative by
(L-91320.4).  This proves (L-91320.5)--(L-91320.6).

## 5. Application to the Cauchy mother

The causal impulse `psi_a` of `L-91031` is a nonzero exponential polynomial on
the positive half-line.  It is analytic there, satisfies

\[
 \psi_a(0)=\psi_a'(0)=0,
\]

and decays at least at rate `a`.  Thus, for the branch range

\[
 a>\frac12,
 \qquad
 1<\eta<2a,
\]

all hypotheses above hold with `rho=a`.  Consequently the positive-half-line
closure asserted in `L-91034.12` is exact.  Reflection proves the negative
half-line counterpart.

The interior zero found in `R-91008` no longer creates a hidden jump: for any
candidate support point, a full-measure set of translated mothers is locally
invertible there.

## 6. Exact boundary

```text
scalar undelayed half-line core                 FALSE by R-91008
delayed distributional multiplier identity      EXACT
tempered/Fourier injectivity step                EXACT
a.e.-delay local-invertibility argument          EXACT
delayed positive-half-line closure               PROVED
delayed negative-half-line closure               PROVED BY REFLECTION
global bridge normalization                      handled in L-91321
prime-side delayed Gram positivity               OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
