# L-91034 — A delay fibre repairs the fixed-scale Hardy form core

Claim ID: `L-91034`  
Status: **PROPOSED COMPLETE VECTOR-HARDY/WIENER FORM-CORE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91031`, `R-91008`, Suzuki's screw-form continuity input  
RH status: **unproved**

## 1. Purpose

`R-91008` proves that one scalar causal mother is not complete: every physical
zero of the impulse supports a hidden jump distribution.  The repair is not to
search for a different scalar spectral phase.  It is to retain an
energy-preserving family of all positive delays.

The resulting output is still one fixed-scale Hardy system.  The additional
coordinate is a passive delay fibre, not a new heat, bandwidth, derivative or
scale limit.

## 2. The delay isometry

Let `w` be any probability density on `(0,infinity)` satisfying

\[
 w(\tau)>0
 \quad\text{for almost every }\tau>0.
 \tag{L-91034.1}
\]

For example one may take

\[
 w_\kappa(\tau)=2\kappa e^{-2\kappa\tau},
 \qquad \kappa>0.
 \tag{L-91034.2}
\]

Define

\[
 \boxed{
 (\mathcal J_wF)(u,\tau)
 =\sqrt{w(\tau)}e^{-iu\tau}F(u).
 }
 \tag{L-91034.3}
\]

Then

\[
 \boxed{
 \|\mathcal J_wF\|_{L^2(du\,d\tau)}^2
 =\|F\|_{L^2(du)}^2.
 }
 \tag{L-91034.4}
\]

Thus `J_w` is an isometry.  It changes no scalar spectral density:

\[
 \int_0^\infty
 |(\mathcal J_wF)(u,\tau)|^2d\tau
 =|F(u)|^2.
 \tag{L-91034.5}
\]

For the Cauchy factor this gives

\[
 \int_0^\infty
 w(\tau)|e^{-iu\tau}\Psi_a(u)|^2d\tau
 =|\Psi_a(u)|^2.
 \tag{L-91034.6}
\]

Hence the sixteenfold residual and every diagonal recurrence identity are
preserved exactly.

## 3. Physical delayed mothers

Let `psi_a` be the causal impulse of `Psi_a`.  The physical direct-integral
mother is

\[
 \boxed{
 \boldsymbol\psi_a(t;\tau)
 =\sqrt{w(\tau)}\,
  \psi_a(t-\tau)\mathbf1_{t>\tau}.
 }
 \tag{L-91034.7}
\]

For every carrier `x` and delay `tau>=0`, define the scalar test

\[
 \boxed{
 f_{a,x,\tau}^{+}(t)
 =-i\frac d{dt}
 \left(e^{ixt}\psi_a(t-\tau)\mathbf1_{t>\tau}\right).
 }
 \tag{L-91034.8}
\]

There is no Dirac mass at `t=tau`, because the relative degree three of the
causal factor gives

\[
 \psi_a(0)=\psi_a'(0)=0.
 \tag{L-91034.9}
\]

Every `f_(a,x,tau)^+` belongs to the positive-half-line weighted space and has
zero integral.  Define the reflected anti-causal family
`f_(a,x,tau)^-` analogously on the negative half-line.

## 4. No common physical zero remains

For fixed `t>0`, the delay-fibre energy is

\[
 \boxed{
 E_{a,w}(t)
 =\int_0^t
 w(\tau)|\psi_a(t-\tau)|^2d\tau>0.
 }
 \tag{L-91034.10}
\]

Indeed, if this integral vanished, then `psi_a(r)=0` for almost every
`0<r<t`; analyticity on the open half-line would force `psi_a` to vanish
identically, contrary to `Psi_a not identically zero`.

Thus the vector-valued physical mother has no common zero at any positive
time, even though every individual scalar delayed copy has isolated zeros.

## 5. Exact positive-half-line closure

Fix

\[
 a>\frac12,
 \qquad
 1<\eta<2a,
\]

and let

\[
 \mathcal H_{\eta,+}
 =L^2((0,\infty),e^{\eta t}dt).
\]

Suppose `h in H_(eta,+)` is orthogonal to

\[
 f_{a,x,\tau}^{+}
 \quad\text{for every }x\in\mathbb R
 \text{ and almost every }\tau>0.
\]

Put `H(t)=h(t)e^(eta t)`.  For each fixed delay, the same Fourier inversion as
in `L-91032` gives distributionally on `(tau,infinity)`

\[
 H'\,\overline{\psi_a(\,\cdot-\tau)}=0.
 \tag{L-91034.11}
\]

Let `T=H'`.  If `T` were nonzero in a neighborhood of a point `t_0>0`, choose
`0<r<t_0` with `psi_a(r) not equal to 0`, possible because the zeros are
discrete.  Taking `tau=t_0-r` makes the multiplier in `(L-91034.11)` nonzero
near `t_0`, forcing `T=0` there, a contradiction.  Hence

\[
 H'=0
 \quad\text{on }(0,\infty).
\]

Therefore `H` is constant and

\[
 h(t)=Ce^{-\eta t}.
\]

Conversely this vector is orthogonal to every delayed derivative because each
has zero integral.  Thus

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_{\eta,+}}
 \{f_{a,x,\tau}^{+}:x\in\mathbb R,\ \tau\ge0\}
 =
 \left\{f\in\mathcal H_{\eta,+}:
  \int_0^\infty f(t)dt=0
 \right\}.
 }
 \tag{L-91034.12}
\]

The reflected argument gives the corresponding negative-half-line identity.

## 6. Global mean-zero core

Retain one bridge `b_a` with total integral zero and unequal, opposite
half-line integrals, as in `L-91032`.  Then

\[
 \boxed{
 \overline{\operatorname{span}}^{\mathcal H_\eta}
 \left(
 \{f_{a,x,\tau}^{+},f_{a,x,\tau}^{-}:
    x\in\mathbb R,\tau\ge0\}
 \cup\{b_a\}
 \right)
 =\mathcal H_{\eta,0}.
 }
 \tag{L-91034.13}
\]

The proof is now dimensionally exact:

```text
causal delayed family      -> one positive-half-line integral defect;
anti-causal delayed family -> one negative-half-line integral defect;
one bridge                 -> fills their difference inside global mean zero.
```

No hidden jump defect remains.

## 7. Corrected fixed-scale screw criterion

Let

\[
 \mathfrak I_a^{\rm del}
 =
 (\{+,-\}\times\mathbb R\times[0,\infty))
 \sqcup\{\star\}.
 \tag{L-91034.14}
\]

For the delayed tests and bridge define

\[
 \mathbb K_a^{\rm del}(i,j)
 =\mathfrak Q_\zeta(F_i,F_j).
 \tag{L-91034.15}
\]

Subject to the standard screw-form continuity already used in the branch,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathbb K_a^{\rm del}\succeq0
 \text{ on every finite packet of }\mathfrak I_a^{\rm del}
 }
 \tag{L-91034.16}
\]

for any one fixed `a>1/2`.

The forward implication is the zero-side Lévy Gram.  The reverse implication
uses `(L-91034.13)`, continuity and Suzuki's full screw criterion.

This repairs the logical role intended for `L-91032`; it does not prove the
prime-side matrix sign.

## 8. Arithmetic availability

Delaying a physical test multiplies its Fourier transform by a phase and does
not change its exponential decay.  At fixed `a>1/2`, every delayed matrix
entry still has an absolutely convergent prime-power expansion and an explicit
gamma/pole term.  Rational carriers and rational delays form a countable
uniqueness set.

False RH therefore still implies one finite rational
carrier/orientation/delay packet with a strict negative directed eigenvalue,
provided the analytic normalizations in the screw formula are retained.

## 9. Scope and review joints

The load-bearing joints are now:

```text
Fubini/distributional passage for almost every delay;
local invertibility of a nonzero analytic delayed mother;
weighted screw-form continuity;
bridge normalization and Fourier orientation.
```

Unlike `L-91032`, the proof does not replace “nonzero almost everywhere” by
“invertible against every point-supported distribution.”

## 10. Exact boundary

```text
scalar fixed-scale core                            REFUTED by R-91008
delay isometry and unchanged residual density      EXACT
delay-fibre no-common-zero property                EXACT
delayed half-line closure                          PROPOSED COMPLETE
delayed two-sided-plus-bridge form core             PROPOSED COMPLETE
corrected fixed-scale Gram criterion               PROPOSED COMPLETE
unconditional delayed cross-Gram PSD               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```
