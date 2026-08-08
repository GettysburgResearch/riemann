# Centered digital Hardy correction

Date: 2026-08-08  
Agent: `gpt56-pro-22`  
Branch: `agent/gpt56-pro-22/237-greedy-carry-parity`  
Status: **review-hardened conditional proposal; RH remains unproved**

## Executive correction

The first cumulative fifth-shell continuation found the correct arithmetic state but selected two energy scales that were too strong.

```text
uncentered D-energy o(T^2)    false because of the known linear main mode;
centered derivative o(T)      too strong because critical-line zeros carry
                              nonzero boundary Hardy mass.
```

The viable energy is obtained by:

1. subtracting the complete positive linear mode;
2. using the centered **weighted** boundary derivative;
3. asking for a uniform `O(T)` physical energy, equivalently a bounded normalized Hardy norm;
4. combining that bound with the base-five digital Abel recurrence.

This yields a corrected single hinge, `CDHB(5)`.

## Exact arithmetic state

Let

\[
C(y)=
\sum_{n\le y}
{\mu(n)-1_{5\mid n}\mu(n/5)\over\sqrt n}
[4\sqrt{y/n}-4-\log(y/n)].
\]

Its transform is

\[
\widehat C(z)=
{(1-5^{-(z+1/2)})(z+1/2)
 \over z^2(z-1/2)\zeta(z+1/2)}.
\]

Writing

\[
h(z)=
{(z+1/2)(1-5^{-(z+1/2)})
 \over (z-1/2)\zeta(z+1/2)},
\]

one has `widehat C=h/z^2`. The principal coefficient is

\[
a_5=h(0)=-(1-5^{-1/2})/\zeta(1/2)>0.
\]

Thus the arithmetic main term is `a_5 log y`.

## Exact centered forcing

Set

\[
Z(y)=C(y)-a_5\log y.
\]

The base-five digit coefficients

\[
c_5(n)=1-4v_5(n),
\qquad
\sum_{n\le N}c_5(n)=s_5(N)\ge0
\]

produce the exact centered convolution

\[
\sum_{m\le y}{c_5(m)\over\sqrt m}Z(y/m)=F_5(y).
\]

Elementary Abel estimates prove

\[
F_5(y)=F_{5,\infty}+O((1+\log y)^2/\sqrt y),
\]

so the centered forcing is bounded unconditionally.

## Correct digital energy

For

\[
Z_m(y)=m^{-1/2}Z(y/m),
\]

put

\[
\mathcal E_{5,c}(y)=
\sum_{2\le m<\lfloor y\rfloor}
 m^2|Z_m(y)-Z_{m+1}(y)|^2.
\]

The centered Abel identity gives

\[
Z(y)
\ge2^{-1/2}Z(y/2)
-\kappa_5\sqrt{\mathcal E_{5,c}(y)}-O(1).
\]

Therefore

\[
\mathcal E_{5,c}(y)=O(1+\log y)
\]

implies

\[
Z(y)\ge-O(\sqrt{\log y}),
\]

and hence

\[
C(y)\ge a_5\log y-O(\sqrt{\log y})>0
\]

for all sufficiently large `y`.

## Correct continuous Hardy form

Let

\[
\mathcal Z(t)=Z(e^t),
\qquad
V(t)=\mathcal Z'(t)+\frac12\mathcal Z(t).
\]

Then

\[
\mathcal E_{5,c}(e^T)
\le\int_0^{T-\log2}|V(t)|^2dt.
\]

Moreover

\[
\widehat V(z)
={(z+1/2)(h(z)-h(0))\over z^2}.
\]

The corrected sole theorem is

\[
\boxed{
\sup_{0<\sigma\le\sigma_0}
\sigma\int_{-\infty}^{\infty}
\left|
{(z+1/2)(h(z)-h(0))\over z^2}
\right|^2d\tau<\infty,
\quad z=\sigma+i\tau.
}
\]

By Plancherel and Abel--Cesaro this is exactly

\[
\int_0^T|V(t)|^2dt=O(T).
\]

It permits critical-line boundary poles but excludes every interior pole.

## Reflected interface

The fifth-aligned inverse is

\[
B_5(s)={1-5^{-s}\over\zeta(s)},
\qquad
A_5(s)={\zeta(s)\over1-5^{-s}}.
\]

Its inverse coefficients and generalized primes are positive:

\[
a_5(n)=v_5(n)+1,
\qquad
\Lambda_5^\#(n)=\Lambda(n)+(\log5)1_{n=5^k}.
\]

The generalized reflected Selberg identity therefore supplies the correct Hermitian derivative orientation. What it does **not** yet supply is the strict Hardy/Poincare reserve needed to control the anchored rationally weighted difference quotient.

The final production theorem must display that reserve with all cross terms and one constant uniform in `sigma`.

## Conditional completion

`CDHB(5)` gives eventual positivity of `C`. Removing a compact initial segment changes its Mellin transform by an entire function. Landau's theorem then forces its abscissa of convergence to be at most zero, while an off-line zeta zero would give an uncancelled pole in `Re z>0`. Functional-equation symmetry gives RH.

## New files

```text
R-23706  uncentered cumulative energy is false
R-23707  centered little-o energy is too strong
L-23714  first centered derivative normalization (superseded as hinge)
L-23715  bounded centered digital forcing
L-23716  centered digital energy descent
T-23705  corrected centered digital Hardy proposal
M-23702  fail-closed review protocol
```

## Exact status

```text
cumulative source and transform        proposed exact
principal mode                         proposed exact
bounded centered forcing               proposed complete
centered energy descent                proposed complete conditional
CDHB(5)                                open / RH-bearing
CDHB(5) -> eventual positivity -> RH   proposed complete
Riemann Hypothesis                     unproved
```

There is no unconditional RH claim in this report.
