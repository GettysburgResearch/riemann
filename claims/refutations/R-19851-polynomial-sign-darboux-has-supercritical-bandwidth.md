# R-19851 — A polynomial which removes all Xi sign changes through height H has supercritical Fourier bandwidth

Claim ID: `R-19851`  
Status: **PROVED ASYMPTOTIC METHOD FIREWALL**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: the unconditional positive-proportion theorem for simple critical-line zeros; the classical critical-line second moment of zeta; Stirling's formula  
Scope: blocks the direct polynomial sign-groundification of `L-19871` at the same bandwidth used to impose positivity  
Nonclaim: nonpolynomial and matrix-valued Darboux mechanisms are not excluded

## 1. Statement

Let

\[
 \Xi(t)=\xi\!\left({1\over2}+it\right).
\]

For `H>0`, let `M_H` be the monic real polynomial whose roots are precisely the
real zeros of `Xi` in `[-H,H]` having odd multiplicity, each repeated once.
Then `M_H(t)Xi(t)` has one constant sign on `[-H,H]` away from its zeros.
Write

\[
 d_H=\deg M_H.
 \tag{R-19851.1}
\]

The unconditional positive proportion of simple critical-line zeros gives a
constant `c_0>0` such that

\[
 \boxed{d_H\ge c_0H\log H}
 \tag{R-19851.2}
\]

for all sufficiently large `H` outside an immaterial bounded initial range.

Put

\[
 F_H(t)=M_H(t)\Xi(t).
 \tag{R-19851.3}
\]

Then

\[
 \boxed{
 {\displaystyle\int_{|t|\le H}|F_H(t)|^2dt
  \over
  \displaystyle\int_{\mathbb R}|F_H(t)|^2dt}
 \longrightarrow0.}
 \tag{R-19851.4}
\]

In fact the energy on `[d_H,2d_H]` divided by the energy on `[-H,H]` tends to
infinity superexponentially in `d_H`.

Consequently the minimal polynomial which makes the rephased Xi samples
one-sign through height `H` moves essentially all of the multiplied target's
Fourier energy beyond that same height.  A finite mode cutoff confined to the
sign-controlled band cannot satisfy the relative approximation required in
`L-19871.20`.

## 2. Degree forced by sign changes

At every simple real zero, `Xi` changes sign.  For `M_H Xi` to keep one sign,
`M_H` must also change sign there, hence must contain that zero with odd
multiplicity.  The same statement applies to every real zero of odd
multiplicity.

The unconditional simple-on-line proportion theorem gives

\[
 N_{0,\mathrm{simple}}(H)\ge c_0H\log H
 \tag{R-19851.5}
\]

with a fixed positive `c_0`, after absorbing the standard `2pi` normalization
into the constant.  This proves (R-19851.2).

The argument only needs a fixed positive proportion.  The optimized numerical
constant is irrelevant.

## 3. Upper bound inside the sign-controlled band

Every root of `M_H` lies in `[-H,H]`.  Hence, for `|t|<=H`,

\[
 |M_H(t)|\le(2H)^{d_H}.
 \tag{R-19851.6}
\]

The gamma factor makes `Xi` square integrable on the real axis.  Therefore one
absolute constant `C` satisfies

\[
 \boxed{
 \int_{|t|\le H}|F_H(t)|^2dt
 \le C(2H)^{2d_H}.}
 \tag{R-19851.7}
\]

## 4. Lower bound beyond H

For large `H`, (R-19851.2) gives `d_H>=2H`.  On
`t in [d_H,2d_H]`, every real root `gamma` of `M_H` obeys

\[
 |t-\gamma|\ge d_H-H\ge d_H/2.
 \tag{R-19851.8}
\]

Thus

\[
 |M_H(t)|\ge(d_H/2)^{d_H}.
 \tag{R-19851.9}
\]

Stirling's formula in the completed zeta factor gives constants `c,C>0` such
that, on this interval,

\[
 |\Xi(t)|^2
 \ge c\,d_H^{7/2}e^{-\pi d_H}
       |\zeta(1/2+it)|^2.
 \tag{R-19851.10}
\]

The deliberately coarse exponential uses `t<=2d_H`; no sharp constant is
needed.  The classical second moment supplies

\[
 \int_{d_H}^{2d_H}|\zeta(1/2+it)|^2dt
 \ge c\,d_H\log d_H
 \tag{R-19851.11}
\]

for all sufficiently large `d_H`.  Combining (R-19851.9)--(R-19851.11),

\[
 \boxed{
 \int_{d_H}^{2d_H}|F_H(t)|^2dt
 \ge c(d_H/2)^{2d_H}
       d_H^{9/2}\log d_H\,e^{-\pi d_H}.}
 \tag{R-19851.12}
\]

## 5. Energy ratio

Divide (R-19851.12) by (R-19851.7).  One obtains

\[
 {\int_{d_H}^{2d_H}|F_H(t)|^2dt
  \over\int_{|t|\le H}|F_H(t)|^2dt}
 \ge
 c\,d_H^{9/2}\log d_H
 \exp\!\left[
  2d_H\log{d_H\over4H}-\pi d_H
 \right].
 \tag{R-19851.13}
\]

By (R-19851.2),

\[
 {d_H\over4H}\ge {c_0\over4}\log H,
 \]

so

\[
 2\log{d_H\over4H}-\pi\longrightarrow+\infty.
 \tag{R-19851.14}
\]

The right side of (R-19851.13) tends to infinity.  This proves
(R-19851.4).

## 6. Finite lattice consequence

Choose a centered Fourier lattice fine enough that between every two
consecutive real zeros of `Xi` in `[-H,H]` there is a sample point on each
side.  Any real polynomial which makes all sampled values one-sign must have at
least one odd real root in every sampled sign-change gap.  Its minimal degree is
therefore at least `d_H`.

`L-19871` then gives an exact real-zero finite CCM vector after multiplication.
But the present theorem shows that the multiplied target cannot be captured by
a Fourier cutoff whose real frequency band ends at `H`: its continuous
`L2` mass is asymptotically outside that band.  The analytic-strip constant in
a target-side cutoff estimate must pay the same derivative-order inflation.

This is the precise circularity:

```text
include enough real zeros to make the coefficients positive
-> degree at least c H log H
-> target bandwidth at least order H log H
-> the sign-controlled band H is no longer a capturing band.
```

Enlarging the band and repeating the same polynomial construction recreates the
same mismatch.

## 7. Proof boundary

- The theorem is unconditional once any fixed positive proportion of simple
  critical-line zeros is imported.
- It rules out the direct minimal polynomial sign correction at its own
  positivity bandwidth.
- It does not rule out a nonpolynomial multiplier with a separately proved
  relative approximation, a matrix-valued colligation, or the anisotropic
  symmetrizer theorem of `L-19869`.
- No assertion about the truth or falsity of RH is made.
