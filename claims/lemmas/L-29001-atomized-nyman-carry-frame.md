# L-29001 — Atomized Nyman–carry frame and exact physical/carry normal Gram

Claim ID: `L-29001`  
Title: Retaining the full carry-position variable gives a balanced Nyman–Beurling filter bank whose pole-preserving prime energy is exactly a finite carry Gram  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Dependencies: PR #241 `L-9518`; PR #269 `L-26901`--`L-26904`; PR #289 `L-27601`--`L-27603`; the classical Nyman–Beurling generators  
Scope: exact filter-bank, pole, and physical-to-carry identities; no cofinal energy estimate or RH claim

## 1. Carry windows are symmetric Nyman–Beurling generators

For real `x>=1` and `0<=theta<=1`, put

\[
 C(x,\theta)
 =\lfloor x\rfloor
  -\lfloor\theta x\rfloor
  -\lfloor(1-\theta)x\rfloor
 \in\{0,1\}.
\tag{L-29001.1}
\]

For `0<y<=1`, define the usual Nyman function

\[
 \rho_\theta(y)
 =\left\{\frac\theta y\right\}
  -\theta\left\{\frac1y\right\}.
\tag{L-29001.2}
\]

Using `theta+(1-theta)=1` and `t=floor(t)+{t}` gives the termwise identity

\[
\boxed{
 C(1/y,\theta)
 =\rho_\theta(y)+\rho_{1-\theta}(y).
}
\tag{L-29001.3}
\]

Let

\[
 (\mathcal Uf)(u)=e^{-u/2}f(e^{-u}),
 \qquad u\ge0.
\tag{L-29001.4}
\]

Then `mathcal U` is unitary from `L^2((0,1),dy)` to `L^2((0,infinity),du)`, and the atomized carry window

\[
\boxed{
 H_\theta(u)
 =e^{-u/2}C(e^u,\theta)\mathbf1_{u\ge0}
 =\mathcal U(\rho_\theta+\rho_{1-\theta})(u)
}
\tag{L-29001.5}
\]

is literally a symmetric Nyman–Beurling generator in logarithmic coordinates.

## 2. Exact transform

Write

\[
 s=z+\frac12,
 \qquad
 N_\theta(s)
 =\frac{1-\theta^s-(1-\theta)^s}{s}.
\tag{L-29001.6}
\]

The standard floor integral, initially for `Re(s)>1`, gives

\[
\boxed{
 \widehat H_\theta(z)=\zeta(s)N_\theta(s).
}
\tag{L-29001.7}
\]

Thus a zeroth-order carry window has the expected zeta factor.  Averaging over
`theta` recovers the canonical carry kernel of PR #289, but averaging before
squaring discards the transverse carry-position frame.

## 3. The pole-preserving atomized prime field

Retain the opposite-parity coefficient

\[
 \omega_2(n)
 =\mu(n)
  -\frac32\mathbf1_{2\mid n}\mu(n/2)
  +\frac12\mathbf1_{4\mid n}\mu(n/4),
\tag{L-29001.8}
\]

and put

\[
 E(s)=(1-2^{-s})(1-2^{-s-1}),
 \qquad
 \Omega(s)=\frac{E(s)}{\zeta(s)}.
\tag{L-29001.9}
\]

Let `beta_omega` be the normalized atomic measure with coefficient
`omega_2(n)/sqrt(n)`, and define

\[
 z_{\theta,\omega}=\beta_\omega*H_\theta.
\tag{L-29001.10}
\]

Then

\[
\boxed{
 \widehat z_{\theta,\omega}(z)
 =E(s)N_\theta(s).
}
\tag{L-29001.11}
\]

The zeta factor cancels only at this zeroth source order.

Let

\[
 \lambda=\sum_{q\ge1}\frac{\Lambda(q)}{\sqrt q}\delta_{\log q}
\]

and define the ordinary-prime commutator field

\[
\boxed{
 \mathfrak P_\theta=\lambda*z_{\theta,\omega}.
}
\tag{L-29001.12}
\]

Its transform is

\[
\boxed{
 \widehat{\mathfrak P_\theta}(z)
 =-E(s)N_\theta(s)\frac{\zeta'}{\zeta}(s).
}
\tag{L-29001.13}
\]

If `rho` is a nontrivial zero of multiplicity `m_rho`, the residue at
`z=rho-1/2` is

\[
\boxed{
 -m_\rho E(\rho)N_\theta(\rho).
}
\tag{L-29001.14}
\]

## 4. The balanced frame sees every nontrivial zero

Fix once and for all

\[
 0<\eta<\frac12.
\]

Define the carry-position frame factor

\[
\boxed{
 \mathfrak A_\eta(s)
 =\int_\eta^{1-\eta}|N_\theta(s)|^2\,d\theta.
}
\tag{L-29001.15}
\]

For every `s!=1` with `Re(s)>0`,

\[
\boxed{\mathfrak A_\eta(s)>0.}
\tag{L-29001.16}
\]

Indeed, if `N_theta(s)` vanished on an interval, analyticity in `theta` would
make

\[
 1-\theta^s-(1-\theta)^s
\]

identically zero.  Differentiation would give
`theta^(s-1)=(1-theta)^(s-1)` on an interval, which is possible only for
`s=1`.  Nontrivial zeta zeros are not equal to one.

On the full interval one has the explicit control

\[
\begin{aligned}
 |s|^2\mathfrak A_0(s)
 ={}&1+\frac{2}{2\operatorname{Re}s+1}
   +2\operatorname{Re}B(s+1,\overline s+1)
   -4\operatorname{Re}\frac1{s+1}.
\end{aligned}
\tag{L-29001.17}
\]

The balanced restriction avoids every degenerating endpoint window while
retaining a strictly positive residue norm at every zero.

## 5. Exact finite carry representation

For real `X>=1`, define

\[
 Z_{X,m}(\theta)
 =\sum_{k\le X/m}\omega_2(k)
   C\!\left(\frac{X}{mk},\theta\right).
\tag{L-29001.18}
\]

The coefficient identity `Lambda*omega_2=-omega_2 log` gives

\[
\boxed{
\begin{aligned}
 \mathfrak P_\theta(\log X)
 &=\frac1{\sqrt X}
   \sum_{r\le X}(\Lambda*\omega_2)(r)
   C\!\left(\frac Xr,\theta\right)\\
 &=\frac1{\sqrt X}
   \sum_{m\le X}\Lambda(m)Z_{X,m}(\theta)\\
 &=-\frac1{\sqrt X}
   \sum_{r\le X}\omega_2(r)\log r
   C\!\left(\frac Xr,\theta\right).
\end{aligned}}
\tag{L-29001.19}
\]

No limit or approximation enters this formula.

Let

\[
 g_m(y)=\mathbf1_{m\le y<2m}
        -\frac12\mathbf1_{2m\le y<4m}.
\tag{L-29001.20}
\]

The real-variable version of the divisor-prefix collapse on PR #269 gives

\[
\boxed{
 Z_{X,m}(\theta)
 =g_m(X)-g_m(\theta X)-g_m((1-\theta)X).
}
\tag{L-29001.21}
\]

Thus the exact physical source is one fixed-ratio carry wavelet for every
balanced position.  For `theta in [eta,1-eta]`, only scales

\[
 m>\frac{\eta X}{4}
\]

can contribute.

## 6. The physical normal energy is exactly a carry Gram

Define the balanced atomized block energy

\[
\boxed{
 \mathscr E_\eta(J)
 =\int_J^{J+1}\int_\eta^{1-\eta}
  |\mathfrak P_\theta(t)|^2\,d\theta\,dt.
}
\tag{L-29001.22}
\]

At each fixed `X=e^t`, equation (L-29001.19) gives

\[
\boxed{
\begin{aligned}
 \int_\eta^{1-\eta}|\mathfrak P_\theta(\log X)|^2d\theta
 =\frac1X\sum_{m,n\le X}
 \Lambda(m)\Lambda(n)\,
 \mathcal K_{\eta,X}(m,n),
\end{aligned}}
\tag{L-29001.23}
\]

where

\[
\boxed{
 \mathcal K_{\eta,X}(m,n)
 =\int_\eta^{1-\eta}
   Z_{X,m}(\theta)Z_{X,n}(\theta)\,d\theta
 \succeq0.
}
\tag{L-29001.24}
\]

The kernel is a finite piecewise-rational object: every breakpoint belongs to
one of the explicit sets

\[
 \left\{\frac{am}{X},1-\frac{am}{X}:a=1,2,4\right\}
\]

for an active scale `m`.  Consequently a production proof can emit the exact
carry Gram without a numerical Fourier inversion or an unproved
physical-to-carry map.

Equations (L-29001.22)--(L-29001.24) are the independent-frequency normal
orientation: the carry-position variable is retained until after the square.

## 7. Vector-valued RH criterion

The following statements are equivalent:

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathscr E_\eta(J)=e^{o(J)}.
}
\tag{L-29001.25}

Under RH, the standard bound

\[
 \psi(x)=x+O_\varepsilon(x^{1/2+\varepsilon})
\]

and the exact cancellation of the linear density in (L-29001.19) give the
subexponential estimate uniformly for balanced `theta`.

Conversely, `mathscr E_eta(J)=e^{o(J)}` puts the vector-valued signal
`theta mapsto mathfrak P_theta(t)` in every exponentially weighted `L^2`
half-plane.  Its vector-valued Laplace transform is therefore holomorphic in
`Re(z)>0`.  A zero `rho` with `Re(rho)>1/2` would create the pole vector

\[
 -m_\rho E(\rho)N_\theta(\rho),
\]

whose squared norm is the strictly positive number
`m_rho^2|E(rho)|^2 mathfrak A_eta(rho)`.  This is impossible.  Functional-equation symmetry gives RH.

## 8. What this changes in the proof graph

The missing interface on the reflected/carry branches was previously phrased as

```text
physical independent-frequency block
 -> unknown bounded source map
 -> carry transition Gram.
```

For the complete atomized bank, that map is the identity (L-29001.19), and the
normal Gram is exactly (L-29001.24).  The remaining problem is no longer
transference.  It is a source-specific estimate for one explicit finite-ratio
carry Gram.

## 9. Proof boundary

Closed exactly or by standard Hilbert-space continuation, subject to review:

- symmetric Nyman/carry identity;
- unitary logarithmic realization;
- balanced carry-frame transform and nonvanishing residue norm;
- exact finite pole-preserving source field;
- exact factor-four wavelet formula;
- equality of physical energy and the finite carry Gram;
- vector-valued energy criterion for RH.

Open:

- a subexponential estimate for `mathscr E_eta`;
- the endpoint/collar recurrence proposed in `T-29001`;
- RH.