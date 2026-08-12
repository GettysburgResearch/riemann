# R-19874 — The asserted tail-Hankel Radon–Nikodym lift uses the wrong variable

Claim ID: `R-19874`  
Status: **EXACT OPERATOR-IDENTITY CORRECTION**  
Created: 2026-08-12  
Corrects: `L-19874.20` at PR #202 head `6de0ecba3c0bb0fb4eafd15e0369ff8ae0e4ca69`  
RH status: **unproved**

## 1. What survives

The atomic Radon–Nikodym multiplier of `L-19874` is correct.  If

\[
 d\omega^{\rm J}_{a,c}(u)=m_a(u)^2\,d\beta_{a,c}(u),
\]

then

\[
 \mathcal U_{a,c}:L^2(\omega^{\rm J}_{a,c})
 \longrightarrow L^2(\beta_{a,c}),
 \qquad \mathcal U_{a,c}f=m_af,
\]

is unitary.  Because `m_a` is a function of the carrier `u`, it commutes with
carrier multiplication and with phase multipliers `exp(-i tau u)`.  The
metric-compatible radial connection calculation in `L-19874` also survives.

## 2. The triangular synthesis calculation

Retain the triangular first-chaos synthesis used by the prime tail-Hankel
construction:

\[
 (V_\mu g)(t,u)
 =\mathbf 1_{0<t<u}\,g(u-t).
\tag{R-19874.1}
\]

The fibrewise Radon–Nikodym unitary is

\[
 (\widetilde{\mathcal U}F)(t,u)=m_a(u)F(t,u).
\tag{R-19874.2}
\]

Consequently

\[
 (\widetilde{\mathcal U}V_{\omega^{\rm J}}g)(t,u)
 =\mathbf 1_{0<t<u}\,m_a(u)g(u-t).
\tag{R-19874.3}
\]

By contrast, the right side asserted in `L-19874.20` is

\[
 (V_\beta M_{m_a}g)(t,u)
 =\mathbf 1_{0<t<u}\,m_a(u-t)g(u-t).
\tag{R-19874.4}
\]

The multipliers in (R-19874.3) and (R-19874.4) are evaluated at different
variables.  Since `m_a` is nonconstant, the two operators are not equal.
Indeed `L-19874` itself proves

\[
 -\frac32<a\partial_a\log m_a(u)<-\frac12,
\]

so constancy is impossible.

Thus

\[
 \boxed{
 \widetilde{\mathcal U}V_{\omega^{\rm J}}
 \ne V_\beta M_{m_a}
 }
\tag{R-19874.5}
\]

in the stated triangular model.

## 3. Correct identity

The exact identity is only

\[
 \boxed{
 \widetilde{\mathcal U}V_{\omega^{\rm J}}
 =M_{m_a(u)}V_\beta,
 }
\tag{R-19874.6}
\]

where multiplication acts **after** the triangular lift, on the carrier
coordinate of the two-variable space.

It cannot be pulled back to multiplication by `m_a` on the translated input
variable `u-t`.

Equivalently, the associated tail observations satisfy

\[
 H_{\omega^{\rm J}}g(t)
 =\int_{u>t}m_a(u)^2g(u-t)\,d\beta(u),
\tag{R-19874.7}
\]

whereas

\[
 H_\beta(M_{m_a}g)(t)
 =\int_{u>t}m_a(u-t)g(u-t)\,d\beta(u).
\tag{R-19874.8}
\]

These are different weighted Hankel operators.

## 4. Correct repair target

The atomic source normalization mismatch is still removed, but transferring the
ordinary-prime Julia colligation requires a new weighted triangular observation
operator.  A valid repair must construct its defect explicitly and prove a
row/coisometric identity; it may not identify it silently with the resident
`H_(beta_a)` block.

```text
atomic Radon–Nikodym unitary                    RETAINED EXACT
carrier and phase covariance                    RETAINED EXACT
metric-compatible radial connection             RETAINED EXACT
L-19874.20 triangular intertwiner                FALSE AS WRITTEN
standard H_beta Julia block after RN transport   NOT OBTAINED
weighted triangular Julia repair                 OPEN
Riemann Hypothesis                               UNPROVEN
```
