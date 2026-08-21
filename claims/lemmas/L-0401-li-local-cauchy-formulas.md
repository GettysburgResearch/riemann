# L-0401 — Local and Cauchy formulas for Li coefficients

Claim ID: L-0401  
Title: Two independent local formulas and a low-height radius audit for Li coefficients  
Status: PROPOSED  
Authoring agent: `gpt56-04`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: standard Laurent expansion of `zeta` at `1`; D-0301 and T-0303 from draft PR #21 for shared normalization and the imported Li criterion; the verified-zero premise is stated explicitly below  
Scope: exact formulas and analytic checks supporting Issue #14  
Related counterexample candidates: none

## Statement

Use the completed zeta function

\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and define

\[
\lambda_n=\frac1{(n-1)!}
 \left.\frac{d^n}{ds^n}\left[s^{n-1}\log\xi(s)\right]\right|_{s=1}
\qquad(n\ge 1),
\]

where the local analytic logarithm is normalized by
`log xi(1)=log(1/2)`.

Write the Laurent expansion

\[
\zeta(1+t)=\frac1t+
 \sum_{m=0}^{\infty}\frac{(-1)^m\gamma_m}{m!}t^m
\]

and put

\[
c_0=1,\qquad
c_k=\frac{(-1)^{k-1}\gamma_{k-1}}{(k-1)!}\quad(k\ge1).
\]

Define `eta_m` exactly by

\[
\eta_0=c_1,
\qquad
\eta_m=(m+1)c_{m+1}-\sum_{j=1}^{m}c_j\eta_{m-j}
\quad(m\ge1).
\]

Then the following three assertions hold.

### A. Finite local recurrence

Let

\[
a_1=1+\frac{\gamma}{2}-\frac12\log(4\pi).
\]

For every `k>=2`, define

\[
B_k=(-1)^{k+1}+\eta_{k-1}
     +(-1)^k(1-2^{-k})\zeta(k).
\]

Then

\[
\boxed{\lambda_n=n a_1+\sum_{k=2}^{n}\binom nk B_k.}
\]

The right side is finite and does not use a truncated sum over nontrivial
zeros.

### B. Independent Cauchy generating function

For `z` near zero set `s=1/(1-z)` and

\[
F(z)=\log\left(2\xi\!\left(\frac1{1-z}\right)\right).
\]

Then

\[
\boxed{F(z)=\sum_{n\ge1}\frac{\lambda_n}{n}z^n}
\]

and hence

\[
\boxed{
F'(z)=s^2\left[
\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi(s/2)+\frac{\zeta'(s)}{\zeta(s)}
\right]
=\sum_{n\ge1}\lambda_n z^{n-1}.}
\]

Whenever `F'` is analytic on `|z|<=r<1`, each coefficient has the Cauchy
representation

\[
\lambda_n=\frac{1}{2\pi r^{n-1}}
\int_0^{2\pi}F'(re^{i\theta})e^{-i(n-1)\theta}\,d\theta.
\]

### C. Low-height audit for a Cauchy radius

For every nontrivial zero `rho=beta+i gamma`, put

\[
z_\rho=1-\frac1\rho.
\]

Fix `0<r<1` and set

\[
H(r)=\frac1{\sqrt{1-r^2}}.
\]

If every nontrivial zero with `|Im rho|<H(r)` lies on the critical line, then
`F'` has no singularity arising from a nontrivial zero in `|z|<=r`.

This is only a radius-reduction lemma.  It does not certify a numerical
quadrature, an FFT, or a coefficient sign.

## Definitions

- `gamma_m` are the Stieltjes constants in the displayed Laurent convention.
- `gamma=gamma_0` is Euler's constant.
- `psi=Gamma'/Gamma` is the digamma function.
- The logarithm in `F` is the analytic branch continued from `F(0)=0` inside
  a zero-free simply connected neighborhood of zero.
- A numerical FFT approximation to the Cauchy integral is called **discovery
  output** until aliasing, function evaluation, and rounding errors are all
  enclosed rigorously.

## Motivation

A strict certified value `lambda_n<0` is a finite unconditional disproof
witness through Li's criterion.  Formula A and Formula B have substantially
different numerical failure modes: the first uses Stieltjes constants and a
triangular formal-power-series recurrence, while the second uses boundary
values of `zeta'/zeta` and Fourier coefficient extraction.  Agreement is a
strong diagnostic, though never a substitute for interval certification.

## Proof

Set

\[
A(t)=t\zeta(1+t)=\sum_{k\ge0}c_k t^k.
\]

By definition `c_0=1`.  Write

\[
\frac{A'(t)}{A(t)}=\sum_{m\ge0}\eta_m t^m.
\]

Comparing the coefficient of `t^m` in
`A'=A(A'/A)` gives

\[
(m+1)c_{m+1}=\sum_{j=0}^m c_j\eta_{m-j},
\]

which is exactly the stated triangular recurrence.

Near `t=0`, cancellation of the pole of `zeta` gives

\[
\log\xi(1+t)
=-\log2+\log(1+t)-\frac{1+t}{2}\log\pi
+\log\Gamma\!\left(\frac{1+t}{2}\right)+\log A(t).
\]

Write this as `sum_{k>=0} a_k t^k`.  Since

\[
\frac{d}{dt}\log A(t)=\sum_{m\ge0}\eta_m t^m,
\]

its coefficient of `t^k` is `eta_{k-1}/k` for `k>=1`.  The standard values

\[
\psi(1/2)=-\gamma-2\log2
\]

and, for `k>=2`,

\[
\psi^{(k-1)}(1/2)
=(-1)^k (k-1)!(2^k-1)\zeta(k)
\]

give

\[
a_1=1+\frac\gamma2-\frac12\log(4\pi)
\]

and

\[
k a_k=(-1)^{k+1}+\eta_{k-1}
       +(-1)^k(1-2^{-k})\zeta(k)=B_k
\qquad(k\ge2).
\]

Now

\[
\lambda_n
=n[t^n](1+t)^{n-1}\log\xi(1+t)
=n\sum_{k=1}^n\binom{n-1}{k-1}a_k.
\]

Using
`n binom(n-1,k-1)=k binom(n,k)` proves Formula A.

For Formula B, observe that

\[
s-1=\frac{z}{1-z}.
\]

For every `k>=1`,

\[
[z^n]\left(\frac{z}{1-z}\right)^k
=\binom{n-1}{k-1}.
\]

Therefore

\[
[z^n]\log\xi\!\left(\frac1{1-z}\right)
=\sum_{k=1}^n\binom{n-1}{k-1}a_k
=\frac{\lambda_n}{n}.
\]

The added constant `log 2` makes the constant coefficient zero.  Differentiating
and using `ds/dz=s^2`, followed by logarithmic differentiation of the displayed
normalization of `xi`, proves the formula for `F'`.  Cauchy's coefficient
formula proves the integral identity on every closed disk on which `F'` is
analytic.

Finally, the elementary identity

\[
|z_\rho|^2-1=\frac{1-2\beta}{|\rho|^2}
\]

shows that a zero with `beta<=1/2` cannot map inside `|z|<1`.  If
`|z_rho|<=r<1`, then necessarily `beta>1/2`, and

\[
1-r^2\le 1-|z_\rho|^2
=\frac{2\beta-1}{|\rho|^2}
<\frac1{\gamma^2}.
\]

If `gamma=0`, the stated verified-zero premise already puts the zero on the
critical line, contradicting `|z_rho|<=r<1`.  If `gamma!=0`, the displayed
inequality gives `|gamma|<H(r)`.  The premise again puts the zero on the
critical line, but a critical-line zero has `|z_rho|=1`, a contradiction.  This
proves the radius audit.

## Analytic domain audit

- `xi` is entire and `xi(1)=1/2`, so its local logarithm at `1` is unambiguous
  after fixing the value `log(1/2)`.
- The separate terms `1/(s-1)` and `zeta'/zeta` in the displayed formula have
  cancelling singular parts at `s=1`; the experimental contours do not pass
  through `s=1`.
- `F'` is meromorphic in the transformed plane.  Nontrivial zeros of `xi` map
  to poles at `z_rho`; `z=1` is outside every contour used here.
- The radius audit excludes zero-induced poles only under its explicit
  low-height premise.  It does not assume RH at unverified heights.
- No zero sum or rearrangement of a conditionally convergent series is used.

## Dependency audit

- Formula A uses the standard Laurent expansion at `s=1`, the displayed `xi`
  normalization, and standard polygamma values at `1/2`.
- Formula B is derived directly from the definition of `lambda_n`; Li's
  equivalence theorem is needed only to turn a future strict negative into an
  RH disproof.
- Part C uses only the Möbius-transform identity and an externally certified
  low-height zero-verification premise.  The experiments record the exact
  height required by each radius.

## Gap audit

- The recurrence is exact, but ordinary `mpmath` values of Stieltjes constants
  are not interval enclosures.
- The FFT code in X-0401 has no rigorous aliasing bound for omitted Fourier
  modes and no directed-rounding enclosure.
- Sampling a contour away from observed zeros does not prove the whole contour
  is zero-free; Part C supplies only the analytic reduction, not a machine
  certificate for the imported zero-verification theorem.
- Close agreement between two floating-point methods is evidence, not proof.
- A finite positive search cannot establish RH and does not make later
  coefficients positive.

## Adversarial tests

- Check `lambda_1=1+gamma/2-log(4*pi)/2` independently.
- Compare Formula A with a direct high-precision Cauchy sum for small `n`.
- Change the Cauchy radius and sampling count; reject a candidate whose sign is
  not stable.
- Monitor the imaginary residual of Fourier coefficients that are theoretically
  real.
- Escalate failed binary64 evaluations instead of accepting an exception,
  `NaN`, or silently substituted value.
- For any negative candidate, recompute with an interval backend and a proven
  aliasing/tail estimate before allocating a `Z-####` identifier.

## Remaining uncertainty

The algebraic formulas look complete but have not received independent review.
No certified interval implementation was completed in this session.  In
particular, L-0401 does not promote any output of X-0401 to a theorem or
counterexample.

## Suggested next attack

Implement Formula A in Arb or another ball-arithmetic backend with rigorous
Stieltjes-constant enclosures, and independently certify Formula B using
rectangular contour subdivision plus a geometric aliasing bound.  Use the
binary64 scan only to nominate indices; demand a strict negative ball before
claiming a witness.
