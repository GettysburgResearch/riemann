# L-91030 — One fixed safe scale is a form core for the zeta screw kernel

Claim ID: `L-91030`  
Status: **PROPOSED COMPLETE HARDY--WIENER FORM-CORE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91029`; Suzuki's screw criterion  
RH status: **unproved**

## 1. Purpose

`L-91029` produces a two-orientation family of causal rational wavelets.  This
lemma proves that one single fixed scale `a_0>1/2`, together with one bridge
vector, already spans a form core for the complete mean-zero screw space.

Consequently the scale parameter is not part of the logical difficulty.  RH can
be tested by one matrix kernel at one absolutely Eulerian horizontal shift.

## 2. Weighted screw space

Fix

\[
 a_0>\frac12
\]

and choose

\[
 1<\eta<2a_0.
\]

Put

\[
 \mathcal H_\eta
 =L^2(\mathbb R,e^{\eta|t|}dt)
\]

and

\[
 \mathcal H_{\eta,0}
 =\left\{f\in\mathcal H_\eta:
   \int_\mathbb R f(t)dt=0\right\}.
 \tag{L-91030.1}

The integral is a continuous functional on `H_eta`.

Suzuki proves the unconditional growth estimate

\[
 |g_\zeta(t)|\ll e^{|t|/2-c\sqrt{|t|}}
 \tag{L-91030.2}

for some `c>0`.  Therefore

\[
 |g_\zeta(t-u)|\ll e^{|t|/2}e^{|u|/2}.
\]

Cauchy--Schwarz gives the continuous form bound

\[
 \boxed{
 |\mathfrak Q_\zeta(f,h)|
 \le C_\eta\|f\|_{\mathcal H_\eta}
              \|h\|_{\mathcal H_\eta}
 }
 \tag{L-91030.3}

for `f,h in H_(eta,0)`.  Thus the screw form extends continuously from compact
smooth mean-zero tests to the weighted space.

## 3. Physical causal and anti-causal mothers

Let

\[
 \psi^+=(\Psi_{a_0})^\vee,
 \qquad
 \psi^-(\overline{\Psi_{a_0}})^\vee.
\]

By `L-91026`, `psi^+` is supported on `[0,infinity)` and is a nonzero finite
sum of functions

\[
 (A_c+B_ct)e^{-ca_0t},
 \qquad c\in\{1,2,4\}.
\]

The function `psi^-` is its reflected anti-causal partner.  Both are analytic
and nonzero almost everywhere on the interior of their supporting half-lines.

The inverse Fourier transforms of the wavelets in `L-91029.14` are

\[
 \boxed{
 f_x^+(t)=-i\frac d{dt}\left(e^{ixt}\psi^+(t)\right),
 }
 \tag{L-91030.4}

and

\[
 \boxed{
 f_x^-(t)=-i\frac d{dt}\left(e^{ixt}\psi^-(t)\right).
 }
 \tag{L-91030.5}

They belong to `H_eta` because `eta<2a_0`, and each has integral zero.

## 4. Exact half-line Wiener closure

Let

\[
 \mathcal H_{\eta,+}=L^2((0,\infty),e^{\eta t}dt).
\]

Suppose `h in H_(eta,+)` is orthogonal to `f_x^+` for every real `x`.
Set

\[
 H(t)=h(t)e^{\eta t}.
\]

Using (L-91030.4), the orthogonality relation is

\[
 x\,\widehat{H\overline{\psi^+}}(x)
 +i\,\widehat{H\overline{(\psi^+)' }}(x)=0
 \qquad(x\in\mathbb R),
 \tag{L-91030.6}

where the hats are ordinary Fourier transforms on the half-line after zero
extension.  Taking the inverse Fourier transform in the sense of distributions,

\[
 -i(H\overline{\psi^+})'
 +iH\overline{(\psi^+)'}
 =-iH'\overline{\psi^+}=0.
 \tag{L-91030.7}

Since `psi^+` is nonzero almost everywhere, `H` is constant.  Therefore

\[
 h(t)=Ce^{-\eta t}.
 \tag{L-91030.8}

Conversely this vector is orthogonal to every `f_x^+`, because its weighted
inner product with `f_x^+` is `C int_0^infinity f_x^+(t)dt=0`.

Hence

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_{\eta,+}}
 \{f_x^+:x\in\mathbb R\}
 =\left\{f\in\mathcal H_{\eta,+}:
   \int_0^\infty f(t)dt=0\right\}.
 }
 \tag{L-91030.9}

The reflected argument gives

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_{\eta,-}}
 \{f_x^-:x\in\mathbb R\}
 =\left\{f\in\mathcal H_{\eta,-}:
   \int_{-\infty}^0 f(t)dt=0\right\}.
 }
 \tag{L-91030.10}

This is a weighted Wiener theorem with an exact one-dimensional defect on each
half-line.

## 5. One bridge fills the remaining defect

Because `Psi_a(u)` has a simple zero at `u=0`, the quotient

\[
 H_a^+(u)=\frac{\Psi_a(u)}u
\]

has a removable value

\[
 \boxed{
 H_a^+(0)=\frac{\sqrt{378}}{16a}.
 }
 \tag{L-91030.11}

Put

\[
 H_a^-(u)=\frac{\overline{\Psi_a(u)}}u
\]

on the real line, again with its removable value, and define the bridge by

\[
 \boxed{
 \widehat b_a(u)=H_a^+(u)-H_a^-(u).
 }
 \tag{L-91030.12}

Then `b_a` is the difference of a causal and an anti-causal exponential
polynomial.  Its total integral is zero because the two removable values agree,
but

\[
 \int_0^\infty b_a(t)dt
 =\frac{\sqrt{378}}{16a},
 \qquad
 \int_{-\infty}^0b_a(t)dt
 =-\frac{\sqrt{378}}{16a}.
 \tag{L-91030.13}

Therefore `b_(a_0)` spans the one missing direction inside the global
zero-integral hyperplane.

Combining (L-91030.9), (L-91030.10) and (L-91030.13),

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_\eta}
 \left(
 \{f_x^+,f_x^-:x\in\mathbb R\}\cup\{b_{a_0}\}
 \right)
 =\mathcal H_{\eta,0}.
 }
 \tag{L-91030.14
}

Thus one fixed safe scale and two Hardy orientations form a complete screw
form core.

## 6. Consequence for positivity

Let the index set be

\[
 \mathfrak I=(\{+,-\}\times\mathbb R)\sqcup\{\star\},
\]

where `star` denotes the bridge.  For `i,j in mathfrak I`, define

\[
 \mathbb K_{a_0}(i,j)
 =\mathfrak Q_\zeta(F_i,F_j),
 \tag{L-91030.15}

with `F_(epsilon,x)=f_x^epsilon` and `F_star=b_(a_0)`.

If every finite matrix

\[
 (\mathbb K_{a_0}(i_j,i_k))_{j,k}
\]

is positive semidefinite, then the screw form is nonnegative on the algebraic
span.  By (L-91030.3) and (L-91030.14), it is nonnegative on all of
`H_(eta,0)`, in particular on Suzuki's compact smooth mean-zero test space.
Suzuki's criterion then gives RH.

The reverse implication follows from the positive Levy/zero Gram in
`L-91029.18` and continuity.

## 7. No scale limit and no growing prime cutoff

The result holds for **every one fixed choice**

\[
 a_0>\frac12.
\]

At that scale:

- all physical test functions have exponential decay faster than the
  unconditional screw growth;
- every Guinand--Weil prime series converges absolutely;
- all poles used in the rational test remain in a fixed safe half-plane;
- no limit `a -> 0`, `a -> infinity`, `sigma -> infinity` or growing derivative
  order appears.

The full RH-bearing content is moved into matrix positivity across carriers and
Hardy orientations, not into a scale asymptotic.

## 8. Boundary

Closed here, subject to independent review:

```text
continuous weighted screw form at a fixed safe scale;
exact causal and anti-causal half-line closures;
one-dimensional half-line defects identified;
one explicit bridge fills the global mean-zero defect;
one fixed scale is a complete form core;
full fixed-scale Gram positivity implies RH.
```

Still open:

```text
unconditional prime-side proof of the fixed-scale cross-Gram PSD;
conservative Fock/Hardy colligation producing that PSD;
RH.
```
