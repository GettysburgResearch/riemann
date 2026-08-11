# L-91032 — One fixed safe scale is a form core for the zeta screw kernel

Claim ID: `L-91032`  
Status: **PROPOSED COMPLETE HARDY–WIENER FORM-CORE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91031`; Suzuki's screw criterion  
RH status: **unproved**

## 1. Weighted screw space

Fix one scale

\[
 a_0>\frac12
\]

and choose

\[
 1<\eta<2a_0.
\]

Put

\[
 \mathcal H_\eta=L^2(\mathbb R,e^{\eta|t|}dt),
 \qquad
 \mathcal H_{\eta,0}=
 \left\{f\in\mathcal H_\eta:\int_\mathbb R f(t)dt=0\right\}.
 \tag{L-91032.1}
\]

Suzuki's unconditional growth bound has the form

\[
 |g_\zeta(t)|\ll e^{|t|/2-c\sqrt{|t|}}.
\]

Therefore

\[
 \boxed{
 |\mathfrak Q_\zeta(f,h)|
 \le C_\eta\|f\|_{\mathcal H_\eta}
              \|h\|_{\mathcal H_\eta}
 }
 \tag{L-91032.2}
\]

for `f,h in H_(eta,0)`.  The screw form is continuous in this weighted norm.

## 2. Causal and anti-causal physical mothers

Let

\[
 \psi^+=(\Psi_{a_0})^\vee,
 \qquad
 \psi^-=(\overline{\Psi_{a_0}})^\vee.
\]

By `L-91026/L-91031`, `psi^+` is supported on `[0,infinity)` and is a nonzero
finite sum of

\[
 (A_c+B_ct)e^{-ca_0t},
 \qquad c\in\{1,2,4\},
\]

while `psi^-` is its reflected anti-causal partner.

The wavelets of `L-91031` are

\[
 \boxed{
 f_x^+(t)=-i\frac d{dt}\left(e^{ixt}\psi^+(t)\right),
 }
 \tag{L-91032.3}
\]

and

\[
 \boxed{
 f_x^-(t)=-i\frac d{dt}\left(e^{ixt}\psi^-(t)\right).
 }
 \tag{L-91032.4}
\]

They belong to `H_eta` because `eta<2a_0`, and each has integral zero.

## 3. Exact positive-half-line closure

Let

\[
 \mathcal H_{\eta,+}=L^2((0,\infty),e^{\eta t}dt).
\]

Suppose `h in H_(eta,+)` is orthogonal to every `f_x^+`.  Put

\[
 H(t)=h(t)e^{\eta t}.
\]

Using (L-91032.3), orthogonality gives

\[
 x\widehat{H\overline{\psi^+}}(x)
 +i\widehat{H\overline{(\psi^+)'}}(x)=0
 \qquad(x\in\mathbb R).
 \tag{L-91032.5}
\]

Taking inverse Fourier transforms distributionally,

\[
 -i(H\overline{\psi^+})'
 +iH\overline{(\psi^+)'}
 =-iH'\overline{\psi^+}=0.
 \tag{L-91032.6}
\]

The causal mother is analytic and nonzero almost everywhere on `(0,infinity)`,
so `H` is constant.  Thus

\[
 h(t)=Ce^{-\eta t}.
\]

Conversely this vector is orthogonal to every `f_x^+`, because the weighted
inner product is `C int_0^infinity f_x^+`.

Therefore

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_{\eta,+}}
 \{f_x^+:x\in\mathbb R\}
 =\left\{f:\int_0^\infty f(t)dt=0\right\}.
 }
 \tag{L-91032.7}
\]

Reflection gives

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_{\eta,-}}
 \{f_x^-:x\in\mathbb R\}
 =\left\{f:\int_{-\infty}^0 f(t)dt=0\right\}.
 }
 \tag{L-91032.8}
\]

Thus each Hardy orientation has exactly one half-line defect.

## 4. One bridge fills the global defect

Because `Psi_a` has a simple zero at zero,

\[
 H_a^+(u)=\frac{\Psi_a(u)}u,
 \qquad
 H_a^-(u)=\frac{\overline{\Psi_a(u)}}u
\]

have removable values, with

\[
 \boxed{
 H_a^+(0)=H_a^-(0)=\frac{\sqrt{378}}{16a}.
 }
 \tag{L-91032.9}
\]

Define the bridge by

\[
 \boxed{
 \widehat b_a(u)=H_a^+(u)-H_a^-(u).
 }
 \tag{L-91032.10}
\]

It is a causal-minus-anti-causal exponential polynomial.  Its total integral
is zero, while its two half-line integrals are opposite and nonzero:

\[
 \int_0^\infty b_a(t)dt=rac{\sqrt{378}}{16a},
 \qquad
 \int_{-\infty}^0b_a(t)dt=-\frac{\sqrt{378}}{16a}.
 \tag{L-91032.11}
\]

Hence the bridge fills the remaining direction inside the global mean-zero
hyperplane.

Combining (L-91032.7), (L-91032.8), and (L-91032.11),

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_\eta}
 \left(
 \{f_x^+,f_x^-:x\in\mathbb R\}\cup\{b_{a_0}\}
 \right)
 =\mathcal H_{\eta,0}.
 }
 \tag{L-91032.12}
\]

## 5. Positivity consequence

Let

\[
 \mathfrak I=(\{+,-\}\times\mathbb R)\sqcup\{\star\},
\]

where `star` denotes the bridge.  For indexed tests `F_i`, define

\[
 \mathbb K_{a_0}(i,j)=\mathfrak Q_\zeta(F_i,F_j).
 \tag{L-91032.13}
\]

If every finite matrix from this kernel is positive semidefinite, then the
screw form is nonnegative on the algebraic span.  By continuity and
(L-91032.12), it is nonnegative on all of `H_(eta,0)`, hence on Suzuki's compact
smooth mean-zero test space.  Suzuki's theorem then gives RH.

The reverse implication follows from the Lévy Gram under RH.

## 6. No scale limit remains

The result holds for every one fixed choice `a_0>1/2`.  At that scale:

```text
all tests decay faster than the unconditional screw growth;
all prime series converge absolutely;
all rational poles remain in one fixed safe half-plane;
no a->0, a->infinity, heat, support or derivative-order limit appears.
```

The full difficulty has moved into cross-carrier, two-orientation matrix
positivity.

## 7. Review warning

The load-bearing joints are:

```text
the distributional inversion in (L-91032.6);
boundary terms at t=0;
nonvanishing of the causal mother almost everywhere;
the signs and half-line integrals in the bridge;
continuity of the screw form in H_eta.
```

They require cold independent review.

## 8. Boundary

Closed here, subject to independent review:

```text
continuous weighted screw form at one safe scale;
exact causal and anti-causal half-line closures;
one-dimensional half-line defects;
one bridge fills the global mean-zero defect;
one fixed scale is a complete screw form core.
```

Open:

```text
unconditional fixed-scale cross-Gram positivity;
conservative completed Fock/Hardy colligation;
RH.
```
