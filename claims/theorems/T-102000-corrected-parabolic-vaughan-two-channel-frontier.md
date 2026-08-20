# T-102000 — Audited parabolic Vaughan and single-wing owner frontier

Claim ID: `T-102000`
Status: **PROVED CONDITIONAL COMPOSITION; SINGLE-WING ESTIMATE OPEN**
Created: 2026-08-21
Audited: 2026-08-21
Depends on: PR #685 `L-100310--L-100312`; PR #691 `L-100615--L-100616`; `L-102001--L-102008`; `R-102000`
RH status: **unproved**

The positive cubic B-spline and the signed zero-moment Vaughan kernel solve
different analytic tasks. `R-102000` makes the attempted interchange bindingly
invalid.

## Channel A: the conclusion-facing zero-moment kernel

Use the ratio-16 signed kernel `K_1` of `L-100310`. Its half-order continuous
moment vanishes, and `L-100311` gives

\[
\mathcal W_1(X)=\mathcal T_U(X)+\mathcal B_U(X),
\qquad U=\lfloor X^{1/3}\rfloor,
\]

with

\[
\int_2^\infty|\mathcal T_U(X)|\frac{dX}{X}<\infty.
\]

The balanced term has the exact large-divisor form

\[
\mathcal B_U(X)
=\sum_{d,e>U}\frac{\mu(d)\mu(e)}{\sqrt{de}}
\mathcal L_{K_1}(X/de).
\tag{T-102000.1}
\]

`L-102008` further collapses the two apparent Möbius wings to one:

\[
\boxed{
\mathcal B_U(X)
=\sum_{\substack{g,m\ge1\\\mu^2(gm)=1}}
\frac{\mu(m)}{g\sqrt m}
N_{U/g}(m)
\mathcal L_{K_1}\!\left(\frac{X}{g^2m}\right).
}
\tag{T-102000.2}
\]

Here `N_V(m)>=0` is the ordered balanced-divisor multiplicity. If
`m=pc` with the unique owner `p=P^+(m)`, then

\[
\mu(m)N_V(m)
=-2\mu(c)
\sum_{a\mid c}
\mathbf1_{a>V}\mathbf1_{c/a>V/p}.
\tag{T-102000.3}
\]

Thus all signs except one literal cofactor Möbius sign have been removed.

Define `SOW102008` by

\[
\boxed{
\int_2^Y
\left(
\sum_{\substack{g,m\ge1\\\mu^2(gm)=1}}
\frac{\mu(m)}{g\sqrt m}
N_{U_X/g}(m)
\mathcal L_{K_1}\!\left(\frac{X}{g^2m}\right)
\right)_-
\frac{dX}{X}
=Y^{o(1)}.
}
\tag{SOW102008}
\]

By the exact identities above, `SOW102008` is the balanced Vaughan condition
`BVD100310` in a narrower source coordinate. Therefore

\[
\boxed{\mathrm{SOW102008}\Longrightarrow RH.}
\tag{T-102000.4}
\]

This implication is complete; `SOW102008` is not proved.

## Channel B: the positive compact structural probe

`L-102000` supplies a nonnegative compact B-spline built from the critical
cubic. It retains every off-line reciprocal-zeta pole, but

\[
\widehat{\mathcal K}_{a,3}(1/2)>0.
\]

It is therefore a structural positivity/compactness probe only. Any attempt to
insert it into Channel A must explicitly pay its half-order main term and its
source normalization.

## What the implication matrix now contributes

For `U=floor(X^(1/3))`, every active outer divisor pair is exactly parabolic.
The gcd core is sign-free, and the two wing signs collapse to `mu(m)`. Unique
largest-prime ownership then leaves `mu(c)` times a positive oriented divisor
count.

The actual-prime interval theorem `L-100615` proves positivity through every
width `q<=p^A`, `A<exp(3/4)`, but it does not automatically apply to the
composite multiplicity in (T-102000.3). The remaining step is now precisely:

```text
construct a source-faithful positive-renewal or joint-collar estimate for
one unique largest prime p, one cofactor sign mu(c), one sign-free square core
g^2, and one positive balanced-divisor multiplicity.
```

The separate joint min--max collar machinery `L-100616/L-102002` remains a
candidate vehicle. `L-102003` proves that survival weight alone does not remove
supercritical widths, and `L-102004--L-102007` localize the carrier-subtracted
collar without proving its signed tail.

```text
zero-moment Type-I channel                    CLOSED
large-divisor Hankel identity                 PROVED EXACT
exact parabolic geometry                      PROVED EXACT
gcd square-core sign removal                  PROVED EXACT
two Möbius wings -> one Möbius owner           PROVED EXACT
unique-largest-prime multiplicity recurrence  PROVED EXACT
positive B-spline Type-I shortcut             REFUTED
joint survival suppresses wide intervals      REFUTED
SOW102008                                      OPEN / RH-EQUIVALENT
Riemann Hypothesis                             UNPROVED
```
