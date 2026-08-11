# Terminal Gaussian heat-residue decomposition and finite linear witness completeness

**Status:** `PROPOSED COMPLETE EXACT NORMAL-FORM / RESIDUE THEOREM — INDEPENDENT REVIEW REQUIRED`  
**Date:** 2026-08-11  
**RH status:** **unproved**  
**Depends on:** the Guinand–Weil normalization imported with Zeta23; PR #364 terminal Gaussian isolation; PR #365 Xi-cardinal form/metric capture; PR #367 completed-Chebyshev reduction.

This note continues the terminal Gaussian arithmetic floor of PR #367.  It
identifies its three-Gaussian prime scalar with a parabolic heat transform of
the pole-subtracted logarithmic derivative of zeta, shifts the transform to
the critical line, and obtains an exact residue expansion.

The expansion has three useful features.

1. A target off-line pair contributes **exactly** `-2m`, with no asymptotic
   normalization left.
2. The exponential rate of every nuisance residue is exactly the terminal
   threat exponent of PR #364.
3. False RH therefore has a finite-prime, finite-parameter, strictly negative
   scalar certificate in this one Gaussian family.

The remaining sign is still RH-equivalent.  No unconditional negative
certificate and no proof of RH is claimed.

## 1. The terminal scalar

Fix

\[
 s_x=\frac12+ix,\qquad x\in\mathbb R,\qquad
 0<y<\frac12,\qquad \sigma>0.
\]

Put

\[
 \tau=\sigma^2,\qquad a=\tau y^2,\qquad D=e^{2a}-1
\]

and

\[
 G_\sigma(t)=e^{-t^2/(4\tau)}.
\]

The three-Gaussian shell of PR #367 is

\[
\begin{aligned}
 H_{\sigma,y}(t)
={}&G_\sigma(t)
 -\frac12G_\sigma(t-2\tau y)
 -\frac12G_\sigma(t+2\tau y)\\
={}&G_\sigma(t)\bigl(1-e^{-a}\cosh(yt)\bigr).
\end{aligned}
\tag{HR.1}
\]

Its normalization is

\[
 A_{\sigma,y}
 =\frac{e^a}{\sqrt\pi\,\sigma D^2}.
\tag{HR.2}
\]

Let

\[
 \Theta(t)=\psi(e^t)-e^t+1.
\tag{HR.3}
\]

PR #367 reduces the relevant Weil value to

\[
 \mathfrak A_\sigma(x,y)
 =
 2A_{\sigma,y}\int_0^\infty
 \Theta(t)\frac{d}{dt}
 \left[e^{-t/2}H_{\sigma,y}(t)\cos(xt)\right]dt.
\tag{HR.4}
\]

Since \(\Theta(0)=0\) and the Gaussian kills the boundary at infinity,
Stieltjes integration by parts gives the equivalent form

\[
 \boxed{
 \mathfrak A_\sigma(x,y)
 =
 -2A_{\sigma,y}\int_0^\infty
 e^{-t/2}H_{\sigma,y}(t)\cos(xt)\,d\Theta(t).
 }
\tag{HR.5}
\]

## 2. Gaussian Mellin transform of the completed Chebyshev measure

Define, for every \(s\in\mathbb C\),

\[
 \boxed{
 \mathcal D_\sigma(s)
 =
 \int_0^\infty
 e^{-t^2/(4\tau)}e^{-st}\,d\Theta(t).
 }
\tag{HR.6}
\]

The Gaussian makes this entire.  Directly from

\[
 d\Theta(t)=d\psi(e^t)-e^t\,dt
\]

one has

\[
\boxed{
\begin{aligned}
 \mathcal D_\sigma(s)
={}&
 \sum_{n\ge2}\Lambda(n)n^{-s}
 e^{-(\log n)^2/(4\tau)}\\
 &-\int_0^\infty
 e^{(1-s)t-t^2/(4\tau)}\,dt.
\end{aligned}}
\tag{HR.7}
\]

The continuous term may also be written

\[
 \sqrt\pi\,\sigma\,
 e^{\tau(1-s)^2}
 \operatorname{erfc}\!\bigl(-\sigma(1-s)\bigr).
\tag{HR.8}
\]

Define the pole-subtracted logarithmic derivative

\[
 \boxed{
 \mathcal L(w)
 =
 -\frac{\zeta'}{\zeta}(w)-\frac1{w-1}.
 }
\tag{HR.9}
\]

It is regular at \(w=1\).  At a nontrivial zero \(\rho\) of multiplicity
\(m_\rho\), its residue is \(-m_\rho\).

### Theorem 2.1 (Bromwich–heat representation)

For every \(c>1\),

\[
 \boxed{
 \mathcal D_\sigma(s)
 =
 \frac{\sigma}{i\sqrt\pi}
 \int_{\Re w=c}
 e^{\tau(w-s)^2}\mathcal L(w)\,dw.
 }
\tag{HR.10}
\]

### Proof

The inverse Gaussian identity

\[
 e^{-t^2/(4\tau)}e^{-st}
 =
 \frac{\sigma}{i\sqrt\pi}
 \int_{\Re w=c}
 e^{\tau(w-s)^2}e^{-wt}\,dw
\tag{HR.11}
\]

follows by a one-dimensional Fourier Gaussian integral.  For \(\Re w>1\),

\[
 \int_0^\infty e^{-wt}\,d\Theta(t)
 =
 \sum_{n\ge2}\frac{\Lambda(n)}{n^w}
 -\int_0^\infty e^{(1-w)t}\,dt
 =
 \mathcal L(w).
\tag{HR.12}
\]

Absolute convergence permits interchange, proving (HR.10). \(\square\)

## 3. The parabolic two-point kernel

The shell (HR.1) is the following two-point finite difference of
\(\mathcal D_\sigma\):

\[
\boxed{
\begin{aligned}
 \Delta_{\sigma,y}\mathcal D(s)
={}&
 \mathcal D_\sigma(s)
 -\frac{e^{-a}}2
 \left[
  \mathcal D_\sigma(s-y)+
  \mathcal D_\sigma(s+y)
 \right].
\end{aligned}}
\tag{HR.13}
\]

Indeed,

\[
 \mathfrak A_\sigma(x,y)
 =
 -2A_{\sigma,y}
 \Re\Delta_{\sigma,y}\mathcal D(s_x).
\tag{HR.14}
\]

Put

\[
 \boxed{
 \mathcal K_{\sigma,y}(z)
 =
 e^{\tau z^2}
 \left[1-\cosh(2\tau yz)\right].
 }
\tag{HR.15}
\]

The exact kernel identity is

\[
\begin{aligned}
&e^{\tau z^2}
-\frac{e^{-a}}2
 \left[e^{\tau(z+y)^2}+e^{\tau(z-y)^2}\right]\\
&\hspace{35mm}
=\mathcal K_{\sigma,y}(z).
\end{aligned}
\tag{HR.16}
\]

Consequently

\[
 \Delta_{\sigma,y}\mathcal D(s_x)
 =
 \frac{\sigma}{i\sqrt\pi}
 \int_{\Re w=c}
 \mathcal K_{\sigma,y}(w-s_x)\mathcal L(w)\,dw.
\tag{HR.17}
\]

## 4. Shift to the critical line

The Gaussian in the vertical direction permits the contour in (HR.17) to be
shifted to the critical line.  Critical-line poles are interpreted as the
right boundary value of a tempered distribution.

Let

\[
 \mathcal L_+(t)
 =
 \lim_{\epsilon\downarrow0}
 \mathcal L\!\left(\frac12+\epsilon+it\right)
\tag{HR.18}
\]

in the distributional sense, and put

\[
 \mathcal B_{\sigma,y}(x)
 =
 \frac{\sigma}{\sqrt\pi}
 \left\langle
  \mathcal L_+(t),
  \mathcal K_{\sigma,y}\!\left(i(t-x)\right)
 \right\rangle.
\tag{HR.19}
\]

### Theorem 4.1 (exact heat-residue decomposition)

One has

\[
 \boxed{
\begin{aligned}
 \Delta_{\sigma,y}\mathcal D(s_x)
={}&
 \mathcal B_{\sigma,y}(x)\\
 &-2\sqrt\pi\,\sigma
 \sum_{\substack{\zeta(\rho)=0\\\Re\rho>1/2}}
 m_\rho\,
 \mathcal K_{\sigma,y}(\rho-s_x).
\end{aligned}}
\tag{HR.20}
\]

The residue sum converges absolutely.

### Proof

Shift the line \(\Re w=c\) to \(\Re w=1/2+\epsilon\), close at
imaginary height \(R\), and let \(R\to\infty\).  The horizontal integrals
vanish because

\[
 |e^{\tau(w-s_x)^2}|
 =
 e^{\tau((\Re w-1/2)^2-(\Im w-x)^2)}
\]

and \(\mathcal L(w)\) has at most logarithmic growth away from its poles.
The poles crossed are precisely the nontrivial zeros with real part greater
than \(1/2+\epsilon\).  Since the residue of \(\mathcal L\) is \(-m_\rho\),
multiplication by

\[
 \frac{\sigma}{i\sqrt\pi}\,2\pi i
 =2\sqrt\pi\,\sigma
\]

gives the minus sign in (HR.20).  Letting \(\epsilon\downarrow0\) yields
(HR.19).  Absolute convergence follows from the Gaussian decay in
\(\Im\rho-x\), the bounded width \(0<\Re\rho<1\), and the standard local zero
count. \(\square\)

## 5. The critical-line boundary is explicit

The completed function

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

gives

\[
 \mathcal L(s)
 =
 -\frac{\xi'}{\xi}(s)
 +\frac1s
 -\frac12\log\pi
 +\frac12\frac{\Gamma'}{\Gamma}(s/2).
\tag{HR.21}
\]

Away from its zeros, \(\xi'/\xi\) is purely imaginary on the critical line.
Taking the right boundary value gives the exact distributional identity

\[
\boxed{
\begin{aligned}
 \Re\mathcal L_+(t)
={}&
 \pi\mu(t)
 +\frac{1/2}{1/4+t^2}\\
 &-\pi
 \sum_{\substack{\zeta(1/2+i\gamma)=0}}
 m_\gamma\,\delta(t-\gamma),
\end{aligned}}
\tag{HR.22}
\]

where \(\mu\) is the archimedean density used in the Zeta23 explicit formula.

On the line,

\[
 \mathcal K_{\sigma,y}(iu)
 =
 e^{-\tau u^2}
 \left[1-\cos(2\tau yu)\right]\ge0.
\tag{HR.23}
\]

Moreover the terminal Gaussian of PR #367 satisfies

\[
 \boxed{
 |F_{\sigma,x+iy}(t)|^2
 =
 2A_{\sigma,y}\sqrt\pi\,\sigma\,
 \mathcal K_{\sigma,y}\!\left(i(t-x)\right).
 }
\tag{HR.24}
\]

Substituting (HR.22) into (HR.20) and then (HR.14) gives the exact zero-side
reading of the prime scalar:

\[
\boxed{
\begin{aligned}
 \mathfrak A_\sigma(x,y)
={}&
 \sum_{\substack{\zeta(1/2+i\gamma)=0}}
 m_\gamma |F_{\sigma,x+iy}(\gamma)|^2\\
 &-\mathcal G_\sigma(x,y)\\
 &+4A_{\sigma,y}\sqrt\pi\,\sigma
 \sum_{\substack{\zeta(\rho)=0\\\Re\rho>1/2}}
 m_\rho\,
 \Re\mathcal K_{\sigma,y}(\rho-s_x),
\end{aligned}}
\tag{HR.25}
\]

where the completely explicit smooth boundary term is

\[
\boxed{
\begin{aligned}
 \mathcal G_\sigma(x,y)
 =
 \frac{2A_{\sigma,y}\sigma}{\sqrt\pi}
 \int_{\mathbb R}
 &\mathcal K_{\sigma,y}\!\left(i(t-x)\right)\\
 &\cdot
 \left[
  \pi\mu(t)+\frac{1/2}{1/4+t^2}
 \right]dt.
\end{aligned}}
\tag{HR.26}
\]

For fixed \(x,y\),

\[
 \mathcal G_\sigma(x,y)=o(1)
 \qquad(\sigma\to\infty).
\tag{HR.27}
\]

Indeed the integral has only Gaussian-width growth while
\(A_{\sigma,y}\sigma\ll_y e^{-3\sigma^2y^2}\).

## 6. Exact target normalization

At the target displacement \(z=y\),

\[
\begin{aligned}
 \mathcal K_{\sigma,y}(y)
 &=
 e^a\left[1-\cosh(2a)\right]\\
 &=-2e^a\sinh^2a.
\end{aligned}
\tag{HR.28}
\]

Since

\[
 D^2=(e^{2a}-1)^2=4e^{2a}\sinh^2a,
\]

one obtains the exact identity

\[
 \boxed{
 4A_{\sigma,y}\sqrt\pi\,\sigma\,
 \mathcal K_{\sigma,y}(y)
 =-2.
 }
\tag{HR.29}
\]

Thus a right-side zero at

\[
 \rho=s_x+y
\]

of multiplicity \(m\) contributes exactly

\[
 \boxed{-2m}
\tag{HR.30}
\]

to (HR.25), for every \(\sigma>0\).

This is the hyperbolic pair value, now recovered from the prime-side contour
without invoking an asymptotic normalization.

## 7. The threat exponent is the residue saddle

Let another right-side zero be

\[
 \rho=s_x+d+ir,
 \qquad 0<d<\frac12.
\]

The real part of its kernel is exactly

\[
\boxed{
\begin{aligned}
 \Re\mathcal K_{\sigma,y}(d+ir)
={}&e^{\tau(d^2-r^2)}
 \Bigl\{
 \cos(2\tau dr)
 [1-\cosh(2\tau yd)\cos(2\tau yr)]\\
 &\qquad+
 \sin(2\tau dr)
 \sinh(2\tau yd)\sin(2\tau yr)
 \Bigr\}.
\end{aligned}}
\tag{HR.31}
\]

After multiplication by the normalizing factor in (HR.25), its largest
exponential rate is

\[
\begin{aligned}
 \Phi_y(d,r)
 &=
 d^2-r^2+2yd-3y^2\\
 &=
 \boxed{(d-y)(d+3y)-r^2}.
\end{aligned}
\tag{HR.32}
\]

This is exactly the terminal threat exponent of PR #364.

Therefore:

- the target has \(\Phi_y(y,0)=0\) and value exactly `-2m`;
- every terminal nuisance point has \(\Phi_y(d,r)<0\);
- the complete nuisance residue sum tends to zero by the same zero-count
  argument as the terminal Gaussian theorem.

The critical-line sum in (HR.25) also tends to zero.  Each fixed ordinate
different from \(x\) is Gaussian-suppressed; if an on-line zero occurs at
\(x\), the factor \(1-\cos 0\) vanishes exactly; the far sum is controlled by
the local zero count.

Consequently the terminal theorem becomes the contour statement

\[
 \boxed{
 \mathfrak A_\sigma(x,y)=-2m+o(1)
 }
\tag{HR.33}
\]

for a terminal off-line pair of multiplicity \(m\).

## 8. Depth-resolved criterion

For \(0<\eta<1/2\), consider the gate only for \(y\ge\eta\).

If there is a zero with

\[
 \Re\rho\ge\frac12+\eta,
\]

start the threat chain from that zero.  Threat edges strictly increase depth,
so the terminal pair produced by the PR #364 argument also has depth at least
\(\eta\).  Hence:

\[
\boxed{
\begin{aligned}
&\forall x\in\mathbb R,\ \forall y\in[\eta,1/2):\\
&\qquad
 \liminf_{\sigma\to\infty}\mathfrak A_\sigma(x,y)\ge0
\\[1mm]
&\Longrightarrow
 \zeta(s)\ne0
 \quad\text{for }\Re s\ge\frac12+\eta.
\end{aligned}}
\tag{HR.34}
\]

Letting \(\eta\downarrow0\) recovers the full RH-equivalent gate.

## 9. Finite-prime truncation

Equation (HR.5) is also the exact finite-computation interface

\[
\boxed{
\begin{aligned}
 \mathfrak A_\sigma(x,y)
 =-2A_{\sigma,y}
 \Biggl[
 &\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}
 H_{\sigma,y}(\log n)\cos(x\log n)\\
 &-\int_0^\infty
 e^{t/2}H_{\sigma,y}(t)\cos(xt)\,dt
 \Biggr].
\end{aligned}}
\tag{HR.35}
\]

Let

\[
\begin{aligned}
 E_{\sigma,y}(t)
={}&
 e^{-t^2/(4\tau)}
 +\frac12e^{-(t-2\tau y)^2/(4\tau)}
 +\frac12e^{-(t+2\tau y)^2/(4\tau)}.
\end{aligned}
\tag{HR.36}
\]

Then

\[
 |H_{\sigma,y}(t)|\le E_{\sigma,y}(t).
\tag{HR.37}
\]

If

\[
 \log P\ge\max(2,2\tau y),
\tag{HR.38}
\]

each summand in

\[
 q(u)=\log u\,u^{-1/2}E_{\sigma,y}(\log u)
\]

is decreasing for \(u\ge P\).  Since \(\Lambda(n)\le\log n\), the omitted
prime-power tail obeys the explicit integral-test bound

\[
\boxed{
\begin{aligned}
 &\sum_{n>P}
 \frac{\Lambda(n)}{\sqrt n}
 |H_{\sigma,y}(\log n)|\\
 &\quad\le
 q(P)+
 \int_{\log P}^{\infty}
 t e^{t/2}E_{\sigma,y}(t)\,dt
 =:\mathcal T_{\sigma,y}(P).
\end{aligned}}
\tag{HR.39}
\]

Therefore truncating (HR.35) at \(P\) changes the scalar by at most

\[
 \boxed{
 2A_{\sigma,y}\mathcal T_{\sigma,y}(P),
 }
\tag{HR.40}
\]

which tends to zero super-polynomially in \(P\) for fixed \(\sigma,y\).

## 10. Finite linear witness completeness under false RH

Assume false RH and the terminal isolation theorem of PR #364.  Choose its
terminal pair \((x,y)\) of multiplicity \(m\).  Equation (HR.33) supplies a
finite \(\sigma\) for which

\[
 \mathfrak A_\sigma(x,y)<-m.
\]

The scalar is continuous in \(x,y,\sigma\), so the strict inequality survives
at nearby rational, and hence dyadic, parameters.  Equation (HR.40) then
supplies a finite prime cutoff \(P\) for which the outward upper endpoint of
the truncated scalar remains negative.

Thus:

\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
\begin{array}{c}
\text{there exist finite dyadic }x,y,\sigma,\\
\text{a finite prime-power cutoff }P,\\
\text{and a strictly negative directed interval}\\
\text{for the scalar in (HR.35).}
\end{array}}
\tag{HR.41}
\]

Conversely, any rigorously negative instance of (HR.35) is a finite negative
Weil witness and disproves RH.

This gives a countable semidecision procedure for false RH:

1. enumerate dyadic \(x,y,\sigma\) with \(0<y<1/2\);
2. enumerate finite prime cutoffs;
3. evaluate the finite prime sum and the elementary Gaussian integral with
   outward rounding;
4. subtract the explicit tail bound (HR.40);
5. retain only an upper endpoint strictly below zero.

No negative Riemann-data instance is supplied here.

## 11. What has and has not advanced

Closed in this note, subject to independent review:

```text
completed-Chebyshev scalar
 -> entire Gaussian Mellin transform
 -> pole-subtracted zeta logarithmic derivative
 -> critical-line boundary plus off-line residues

target pair residue                         exactly -2m
nuisance saddle exponent                    exactly PR #364 threat exponent
critical-line boundary                      explicit and o(1)
false RH                                    finite linear prime witness
depth-eta gate                              zero-free strip criterion
```

Still open:

```text
unconditional nonnegativity of the scalar;
the arithmetic corrected-kernel floor;
RH.
```

The surviving theorem is no longer hidden in a matrix, a Gram inverse, a
Schur complement, a pole term, or an unspecified prime remainder.  It is the
assertion that the heat-residue sum (HR.25) has no negative off-line residue,
which is exactly the zero-free assertion it is meant to prove.
