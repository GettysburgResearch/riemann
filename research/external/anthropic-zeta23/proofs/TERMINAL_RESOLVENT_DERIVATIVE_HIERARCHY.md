# Terminal resolvent-derivative hierarchy: fixed safe Euler data isolate every terminal off-line pair

**Status:** `PROPOSED COMPLETE EXACT RESOLVENT / ALL-ORDER CRITERION — INDEPENDENT REVIEW REQUIRED`  
**Date:** 2026-08-11  
**RH status:** **unproved**  
**Depends on:** PR #375 terminal Gaussian heat-residue decomposition; PR #364 terminal-pair theorem; the standard completed-zeta logarithmic derivative and zero-count estimates.

This note Laplace-transforms the heat time in PR #375 and then takes high
Laplace moments.  The zeroth transform is a rational kernel and a three-point
formula for the completed logarithmic derivative.  Its high derivatives have
a stronger property:

```text
heat time tends to infinity through the derivative order k,
while every zeta/Euler evaluation point remains fixed in Re(s)>1.
```

Consequently a terminal off-line pair is isolated exponentially in `k`, yet
every finite member of the hierarchy is computable from absolutely convergent
prime-power series plus elementary gamma terms.  This yields a countable exact
RH criterion and a finite safe-Euler certificate under false RH.

It does **not** prove the required nonnegativity.  The hierarchy is a new proof
coordinate, not an accepted proof of RH.

## 1. Completed logarithmic derivative

Write

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and define

\[
 \boxed{
 \mathscr X(s)=-\frac{\xi'}{\xi}(s).
 }
 \tag{RD.1}
\]

Every nontrivial zero `rho` of multiplicity `m_rho` is a pole of
`mathscr X` with residue `-m_rho`.  In the half-plane `Re(s)>1`,

\[
\boxed{
\begin{aligned}
 \mathscr X(s)
 ={}&\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
 -\frac1s-\frac1{s-1}
 +\frac12\log\pi
 -\frac12\frac{\Gamma'}{\Gamma}(s/2).
\end{aligned}}
\tag{RD.2}
\]

Thus every derivative of `mathscr X` in `Re(s)>1` is an absolutely
convergent prime-power series plus an explicit elementary/archimedean term.

Fix

\[
 s_x=\frac12+ix,
 \qquad x\in\mathbb R,
 \qquad 0<y<\frac12.
 \tag{RD.3}
\]

The heat kernel from PR #375 is

\[
 \mathcal K_{\tau,y}(z)
 =e^{\tau z^2}\bigl[1-\cosh(2\tau yz)\bigr],
 \qquad \tau>0.
 \tag{RD.4}
\]

On the critical line,

\[
 \mathcal K_{\tau,y}(iu)
 =e^{-\tau u^2}\bigl[1-\cos(2\tau yu)\bigr]\ge0,
 \tag{RD.5}
\]

while at the target displacement,

\[
 \mathcal K_{\tau,y}(y)
 =-2e^{\tau y^2}\sinh^2(\tau y^2)<0.
 \tag{RD.6}
\]

## 2. Zeroth Laplace transform: an exact rational zero kernel

For a real parameter `alpha>3y^2`, define

\[
 \mathcal R_{\alpha,y}(z)
 =\int_0^\infty e^{-\alpha\tau}
   \mathcal K_{\tau,y}(z)\,d\tau.
 \tag{RD.7}
\]

Whenever the three elementary Laplace integrals converge,

\[
\boxed{
\begin{aligned}
 \mathcal R_{\alpha,y}(z)
 ={}&\frac1{\alpha-z^2}
 -\frac12\frac1{\alpha-z^2-2yz}
 -\frac12\frac1{\alpha-z^2+2yz}\\
 ={}&-\frac{4y^2z^2}
 {\bigl(\alpha-z^2\bigr)
  \bigl[(\alpha-z^2)^2-4y^2z^2\bigr]}.
\end{aligned}}
\tag{RD.8}
\]

In particular,

\[
 \boxed{
 \mathcal R_{\alpha,y}(iu)
 =\frac{4y^2u^2}
 {\bigl(\alpha+u^2\bigr)
  \bigl[(\alpha+u^2)^2+4y^2u^2\bigr]}
 \ge0,
 }
 \tag{RD.9}
\]

and

\[
 \boxed{
 \mathcal R_{\alpha,y}(y)
 =-\frac{4y^4}
 {\bigl(\alpha-y^2\bigr)
  \bigl(\alpha-3y^2\bigr)
  \bigl(\alpha+y^2\bigr)}<0.
 }
 \tag{RD.10}
\]

The rational kernel decays as `O(|z|^-4)`.  Hence its complete zero sum is
absolutely convergent.

## 3. Exact three-shift formula in the safe Euler half-plane

Put

\[
 q_{\alpha,y}=\sqrt{\alpha+y^2}.
 \tag{RD.11}
\]

Assume

\[
 q_{\alpha,y}-y>\frac12,
 \quad\text{equivalently}\quad
 \boxed{\alpha>y+\frac14.}
 \tag{RD.12}
\]

Then all three points below lie strictly in `Re(s)>1` when `s=s_x`.
Define

\[
\boxed{
\begin{aligned}
 \mathcal F_{\alpha,y}(s)
 ={}&\frac{\mathscr X(s+\sqrt\alpha)}{\sqrt\alpha}\\
 &-\frac{
   \mathscr X(s+q_{\alpha,y}-y)
   +\mathscr X(s+q_{\alpha,y}+y)}
 {2q_{\alpha,y}}.
\end{aligned}}
\tag{RD.13}
\]

### Theorem 3.1 (rational Cauchy representation)

Choose `c` with

\[
 1<c<\Re(s)+q_{\alpha,y}-y.
 \tag{RD.14}
\]

Then

\[
 \boxed{
 \mathcal F_{\alpha,y}(s)
 =\frac1{i\pi}
  \int_{\Re w=c}
  \mathcal R_{\alpha,y}(w-s)\mathscr X(w)\,dw.
 }
 \tag{RD.15}
\]

### Proof

Use the first line of (RD.8).  For example,

\[
 \frac1{\alpha-z^2}
 =\frac1{(\sqrt\alpha-z)(\sqrt\alpha+z)}.
\]

Close the vertical contour to the right.  The kernel is `O(|w|^-2)` term by
term and the complete combination is `O(|w|^-4)`, while
`mathscr X(w)=O(log(2+|w|))` there.  The only enclosed pole of this term is
`w=s+sqrt(alpha)`, with residue
`-mathscr X(s+sqrt(alpha))/(2sqrt(alpha))`.  The clockwise closure converts
it to the first term in (RD.13).  The positive roots of the other two
denominators are `q-y` and `q+y`.  Their residues give the remaining two
terms.  Condition (RD.14) leaves all three kernel poles to the right and all
zeta zeros to the left.  This proves (RD.15).  `square`

The same identity follows by multiplying the PR #375 heat transform by
`tau^(-1/2)e^(-alpha tau)` and using

\[
 \int_0^\infty \tau^{-1/2}
 e^{-\alpha\tau-t^2/(4\tau)}d\tau
 =\sqrt{\frac\pi\alpha}e^{-\sqrt\alpha t}.
 \tag{RD.16}
\]

## 4. The all-order resolvent hierarchy

For every integer `k>=0`, put

\[
\boxed{
 \mathcal R_{k,\alpha,y}(z)
 =(-\partial_\alpha)^k\mathcal R_{\alpha,y}(z)
 =\int_0^\infty \tau^k e^{-\alpha\tau}
   \mathcal K_{\tau,y}(z)d\tau.
 }
\tag{RD.17}
\]

The closed form is

\[
\boxed{
\begin{aligned}
 \mathcal R_{k,\alpha,y}(z)
 =k!\Bigg[&
  \frac1{(\alpha-z^2)^{k+1}}
 -\frac1{2(\alpha-z^2-2yz)^{k+1}}\\
 &-\frac1{2(\alpha-z^2+2yz)^{k+1}}
 \Bigg].
\end{aligned}}
\tag{RD.18}
\]

Likewise define

\[
 \boxed{
 \mathcal F_{k,\alpha,y}(s)
 =(-\partial_\alpha)^k\mathcal F_{\alpha,y}(s).
 }
 \tag{RD.19}
\]

Differentiating (RD.15) under the integral gives

\[
 \boxed{
 \mathcal F_{k,\alpha,y}(s)
 =\frac1{i\pi}
  \int_{\Re w=c}
  \mathcal R_{k,\alpha,y}(w-s)\mathscr X(w)\,dw.
 }
 \tag{RD.20}
\]

At finite `k`, (RD.19) is a finite algebraic linear combination of
`mathscr X^(j)` at the same three safe points in (RD.13), `0<=j<=k`.
No evaluation point moves toward the critical strip as `k` grows.

For the rest of the note freeze

\[
 \boxed{\alpha=1.}
 \tag{RD.21}
\]

This is uniformly safe for every `0<y<1/2`, because

\[
 \sqrt{1+y^2}-y
 >\sqrt{5/4}-\frac12
 >\frac12.
 \tag{RD.22}
\]

Write

\[
 R_{k,y}(z)=\mathcal R_{k,1,y}(z),
 \qquad
 F_{k,y}(s)=\mathcal F_{k,1,y}(s),
 \tag{RD.23}
\]

and

\[
\boxed{
 r_{k,y}=R_{k,y}(y)
 =k!\left[
  \frac1{(1-y^2)^{k+1}}
 -\frac1{2(1-3y^2)^{k+1}}
 -\frac1{2(1+y^2)^{k+1}}
 \right]<0.
 }
\tag{RD.24}
\]

The strict sign follows directly from the integral in (RD.17) and (RD.6).
Similarly,

\[
 \boxed{R_{k,y}(iu)\ge0\quad(u\in\mathbb R).}
 \tag{RD.25}
\]

## 5. Exact zero-side expansion

Shift the contour in (RD.20), with `s=s_x`, from `Re(w)=c` to the critical
line.  The rational kernel makes the horizontal integrals vanish and the
complete residue sum absolutely convergent.

The right boundary value of `mathscr X=-xi'/xi` has

\[
 \Re\mathscr X_+(1/2+it)
 =-\pi\sum_{\xi(1/2+i\gamma)=0}
 m_\gamma\delta(t-\gamma).
 \tag{RD.26}
\]

There is no smooth gamma remainder: it has already been included in the
completed logarithmic derivative.

### Theorem 5.1 (exact rational zero expansion)

For every `k>=0`,

\[
\boxed{
\begin{aligned}
 \Re F_{k,y}(s_x)
 ={}&-\sum_{\xi(1/2+i\gamma)=0}
       m_\gamma R_{k,y}\bigl(i(\gamma-x)\bigr)\\
 &-2\sum_{\substack{\xi(\rho)=0\\\Re\rho>1/2}}
       m_\rho\Re R_{k,y}(\rho-s_x).
\end{aligned}}
\tag{RD.27}
\]

Define the normalized scalar

\[
 \boxed{
 \mathfrak C_k(x,y)
 =\frac{\Re F_{k,y}(s_x)}{r_{k,y}}.
 }
 \tag{RD.28}
\]

Then

\[
\boxed{
\begin{aligned}
 \mathfrak C_k(x,y)
 ={}&-\frac1{r_{k,y}}
 \sum_{\xi(1/2+i\gamma)=0}
 m_\gamma R_{k,y}\bigl(i(\gamma-x)\bigr)\\
 &-\frac2{r_{k,y}}
 \sum_{\substack{\xi(\rho)=0\\\Re\rho>1/2}}
 m_\rho\Re R_{k,y}(\rho-s_x).
\end{aligned}}
\tag{RD.29}
\]

Because `r_(k,y)<0` and every line kernel in (RD.25) is nonnegative,

\[
 \boxed{
 \mathrm{RH}\Longrightarrow
 \mathfrak C_k(x,y)\ge0
 \quad\text{for every }k,x,y.
 }
 \tag{RD.30}
\]

If a right-side zero occurs exactly at `rho=s_x+y` with multiplicity `m`,
its term in (RD.29) is

\[
 \boxed{-2m}
 \tag{RD.31}
\]

for every `k`, with no limiting normalization.

## 6. High derivative order is a large-heat-time amplifier

The dominant target exponential in (RD.6) is `exp(3y^2 tau)`.  After the
fixed Laplace damping `exp(-tau)`, the target moment is governed by

\[
 \tau^k e^{-(1-3y^2)\tau}d\tau.
 \tag{RD.32}
\]

After normalization this is asymptotically a Gamma law with

\[
 \mathbb E\tau\sim\frac{k+1}{1-3y^2}.
 \tag{RD.33}
\]

Thus `k->infinity` sends the effective heat time to infinity although the
three analytic sample points in (RD.13) remain fixed in `Re(s)>1`.

More quantitatively, write a nuisance right-side zero as

\[
 \rho=s_x+d+ir,
 \qquad z=d+ir.
 \tag{RD.34}
\]

The largest heat exponent in its kernel is

\[
 \beta_y(d,r)=d^2-r^2+2yd.
 \tag{RD.35}
\]

The terminal threat condition of PR #364 is precisely

\[
 \boxed{
 \beta_y(d,r)<3y^2.
 }
 \tag{RD.36}
\]

Indeed it is equivalent to

\[
 (d-y)(d+3y)-r^2<0.
\]

For every fixed nuisance satisfying (RD.36), all three denominators in
(RD.18) have modulus strictly larger than

\[
 a_y=1-3y^2.
 \tag{RD.37}
\]

The target denominator is asymptotic to

\[
 r_{k,y}\sim-\frac{k!}{2a_y^{k+1}}.
 \tag{RD.38}
\]

Therefore

\[
 \boxed{
 \frac{R_{k,y}(d+ir)}{r_{k,y}}\longrightarrow0
 \qquad(k\to\infty)
 }
 \tag{RD.39}
\]

exponentially for every fixed terminal nuisance.

The convergence survives the complete zero sum.  On a bounded ordinate
interval there are finitely many zeros and terminality supplies a strict
minimum denominator gap.  Outside that interval the denominators in
(RD.18) are `gg r^2`, while the local zero count is only logarithmic.  The
same argument treats the critical-line sum; a line zero at `gamma=x` has
kernel zero exactly.

### Theorem 6.1 (terminal derivative-order isolation)

Assume false RH and let `rho_0=s_x+y` be a terminal right-side zero of
multiplicity `m`, in the sense of PR #364.  Then

\[
 \boxed{
 \mathfrak C_k(x,y)=-2m+o(1)
 \qquad(k\to\infty).
 }
 \tag{RD.40}
\]

In particular, `mathfrak C_k(x,y)<0` for some finite `k`.

## 7. Countable fixed-Euler RH criterion

Combining (RD.30) and Theorem 6.1 gives:

### Theorem 7.1 (resolvent-derivative criterion)

Subject to the terminal-pair theorem of PR #364,

\[
\boxed{
\begin{aligned}
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 &\mathfrak C_k(x,y)\ge0\\
 &\text{for every }k\in\mathbb Z_{\ge0},
   \ x\in\mathbb R,
   \ 0<y<1/2.
\end{aligned}}
\tag{RD.41}
\]

It is enough to test dyadic `x` and dyadic `y`.  If RH is false,
Theorem 6.1 gives a strict negative value at a finite order.  Continuity in
`x,y` preserves that strict sign at nearby dyadic parameters.

Unlike the large-`sigma` formulation, every member of (RD.41) uses only the
three fixed safe arguments

\[
\boxed{
 s_x+1,
 \qquad
 s_x+\sqrt{1+y^2}-y,
 \qquad
 s_x+\sqrt{1+y^2}+y,
}
\tag{RD.42}
\]

and derivatives of `mathscr X` there.  Their real parts are uniformly greater
than one.

## 8. Complete monotonicity and a moment-Hankel sum-of-squares interface

For general `alpha>y+1/4`, define the safe-Euler real scalar

\[
 \boxed{
 G_{x,y}(\alpha)=-\Re\mathcal F_{\alpha,y}(s_x).
 }
 \tag{RD.43}
\]

Under RH, shifting (RD.15) to the critical line gives

\[
\begin{aligned}
 G_{x,y}(\alpha)
 &=\sum_{\xi(1/2+i\gamma)=0}
   m_\gamma\mathcal R_{\alpha,y}\bigl(i(\gamma-x)\bigr)\\
 &=\int_0^\infty e^{-\alpha\tau}W_{x,y}(\tau)d\tau,
\end{aligned}
\tag{RD.44}
\]

where

\[
 \boxed{
 W_{x,y}(\tau)
 =\sum_\gamma m_\gamma
 e^{-\tau(\gamma-x)^2}
 \bigl[1-\cos(2\tau y(\gamma-x))\bigr]\ge0.
 }
 \tag{RD.45}
\]

Thus RH makes `G_(x,y)` a completely monotone function of `alpha`:

\[
 \boxed{
 (-1)^kG_{x,y}^{(k)}(\alpha)\ge0
 \qquad(k\ge0).
 }
 \tag{RD.46}
\]

At `alpha=1`, put

\[
 A_k(x,y)=(-1)^kG_{x,y}^{(k)}(1)
 =-\Re F_{k,y}(s_x).
 \tag{RD.47}
\]

Under RH this is a Stieltjes moment sequence,

\[
 A_k(x,y)=\int_0^\infty\tau^k e^{-\tau}W_{x,y}(\tau)d\tau.
 \tag{RD.48}
\]

Consequently every Hankel matrix

\[
 \boxed{
 H_d(x,y)=\bigl(A_{i+j}(x,y)\bigr)_{0\le i,j\le d}
 \succeq0.
 }
 \tag{RD.49}
\]

Indeed, for every coefficient vector `c`,

\[
 c^*H_dc
 =\int_0^\infty
 \left|\sum_{j=0}^dc_j\tau^j\right|^2
 e^{-\tau}W_{x,y}(\tau)d\tau\ge0.
 \tag{RD.50}
\]

This is an exact sum-of-squares interface on the **prime side**: every entry
of `H_d` is a finite algebraic combination of derivatives of the three safe
Euler samples (RD.42).

Conversely, for a terminal false-RH pair, Theorem 6.1 gives

\[
 \Re F_{k,y}(s_x)\sim-2m\,r_{k,y}>0,
\]

so

\[
 A_k(x,y)<0
\]

for every sufficiently large `k`.  In particular an even diagonal entry of a
finite Hankel matrix is negative.  Therefore the following are also exact RH
criteria, subject to PR #364:

\[
\boxed{
\begin{aligned}
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 &G_{x,y}\text{ is completely monotone for every }x,y\\
 \quad\Longleftrightarrow\quad
 &H_d(x,y)\succeq0\text{ for every finite }d,x,y.
\end{aligned}}
\tag{RD.51}
\]

The moment-Hankel formulation is stronger structurally than checking one
scalar at a time and is the preferred next target for a source-ordered
sum-of-squares proof.

## 9. Finite safe-Euler certificates

For `Re(w)=sigma>1`, differentiation of (RD.2) gives

\[
 \mathscr X^{(j)}(w)
 =(-1)^j\sum_{n\ge2}
   \frac{\Lambda(n)(\log n)^j}{n^w}
 +E_j(w),
 \tag{RD.52}
\]

where `E_j` is an explicit rational/polygamma expression.

At finite `k`, repeated chain rule in (RD.19) uses only finitely many such
values with `j<=k`.  For a prime cutoff `P`, the omitted prime tail obeys

\[
\boxed{
 \left|
 \sum_{n>P}\frac{\Lambda(n)(\log n)^j}{n^w}
 \right|
 \le
 q_j(P)+\int_P^\infty
  \frac{(\log u)^{j+1}}{u^\sigma}du,
}
\tag{RD.53}
\]

once the summand is decreasing, where

\[
 q_j(P)=\frac{(\log P)^{j+1}}{P^\sigma}.
\]

All coefficients introduced by (RD.19) are explicit algebraic functions of
`y` and can be enclosed outward.

Consequently:

\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
\begin{array}{c}
\text{a finite derivative order }k,\\
\text{finite dyadic }x,y,\\
\text{a finite prime-power cutoff }P,\\
\text{and a strictly negative directed interval}\\
\text{for }\mathfrak C_k(x,y).
\end{array}}
\tag{RD.54}
\]

This is a finite certificate made entirely from absolutely convergent Euler
series and standard gamma/polygamma evaluations.  No zeta value inside the
critical strip is an input.

## 10. Sharp zeroth-resolvent firewall and how the hierarchy bypasses it

The zeroth Laplace transform has two distinct convergence boundaries.

A target heat residue grows like `exp(3y^2 tau)`, so its Abel transform requires

\[
 \alpha>3y^2.
 \tag{RD.55}
\]

On the separated prime side, the slowest exponential in (RD.16) is

\[
 e^{-(\sqrt{\alpha+y^2}-y)t}.
\]

Against the critical factor `e^{t/2}`, absolute Euler/Stieltjes interchange
requires

\[
 \alpha>y+\frac14.
 \tag{RD.56}
\]

The two boundaries are separated throughout the open strip by the exact gap

\[
\boxed{
 y+\frac14-3y^2
 =3\left(\frac12-y\right)\left(y+\frac16\right)>0.
}
\tag{RD.57}
\]

This is precisely the phase-blind saddle exponent found in PR #367.
Therefore a zeroth-order Abel limit cannot simultaneously approach terminal
isolation and justify termwise absolute Euler summation.

The derivative hierarchy bypasses this obstruction without crossing either
boundary:

```text
freeze alpha=1 in the absolute Euler region;
raise k;
the Gamma/Erlang moment moves the effective heat time to infinity;
terminal nuisances lose an exponential denominator ratio;
the zeta sample points never move.
```

This is the main constructive advance of the note.

## 11. Exact proof boundary

Closed here, subject to independent review:

```text
heat-time Laplace transform              exact rational kernel
critical-line sign                       nonnegative at every order
target sign                              negative at every order
target normalized contribution           exactly -2m
safe Euler representation                three fixed points in Re(s)>1
high derivative order                    large-heat-time amplifier
complete monotonicity under RH            exact Laplace representation
moment-Hankel matrices under RH            exact sum-of-squares
terminal nuisance contribution           exponentially vanishing
false RH                                 finite negative safe-Euler witness
all-order nonnegativity                   exact RH criterion
zeroth Abel/Euler convergence gap         exact and sharp
```

Still open:

```text
an unconditional proof that every mathfrak C_k(x,y) is nonnegative;
a prime-side proof of complete monotonicity / Hankel positivity;
a sum-of-squares or total-positivity theorem for the safe-Euler hierarchy;
the arithmetic corrected-kernel floor;
RH.
```

The remaining sign has moved from a large Gaussian parameter and a huge moving
prime cutoff to an all-order hierarchy at three fixed points of absolute Euler
convergence.  That is a narrower and more algebraic target, but it remains the
Riemann Hypothesis rather than a solved estimate.
