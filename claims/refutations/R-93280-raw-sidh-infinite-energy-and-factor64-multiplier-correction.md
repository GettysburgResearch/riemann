# R-93280 - Raw SID_H has infinite scale energy, and the factor-64 multiplier is multiplicative

Claim ID: `R-93280`  
Status: **EXACT CORRECTION AND REFUTATION**  
Created: 2026-08-16  
Depends on: PR #539 at `9c124705600603914ee9fe2678360b759780a1e0`; PR #531 at `e1b3b03d97d47c5046aa84f31e51c925d92baabd`  
Scope: the carrier interface and the displayed factor-64 Mellin multiplier; no RH conclusion

## 1. Mechanical correction to `L-93270.17`

Let

\[
\Phi_{64}=(64-T)(16-T)(4-T)\Phi_P,
\qquad (Tf)(x)=f(4x),
\]

and let `W_64=D^2 Phi_64/x`. Since

\[
\frac{D^2(Tf)(x)}x=4T\left(\frac{D^2f}x\right)(x),
\]

the curvature multiplier is a product, not a sum:

\[
\boxed{
\widehat W_{64}(s)=
\frac{2(s-1)^2
(4-4^{1-s})(16-4^{1-s})(64-4^{1-s})}
{s(s+1)(s+2)}.
}
\tag{R-93280.1}
\]

The plus sign printed between the Peano numerator and the scale factors in
`L-93270.17` is a typographical error. The physical definition, the positive
convolution factorization, and the zero-line discussion all use the product.
PR #539 remains frozen; this successor is the normative correction.

## 2. The raw carrier field

Let `W_C` be the centered-cubic kernel and, for `X=e^r`, define

\[
\mathcal F_C(r,t)
=e^{-r/2}
\sum_{n\le e^r}\Lambda(n)n^{it}W_C(ne^{-r}).
\tag{R-93280.2}
\]

The continuous-prime model is

\[
\mathcal F_C^{\rm cont}(r,t)
=e^{-r/2}\int_1^{e^r}x^{it}W_C(xe^{-r})\,dx.
\tag{R-93280.3}
\]

Changing variables `x=e^r u` gives

\[
\mathcal F_C^{\rm cont}(r,t)
=e^{(1/2+it)r}
\int_{e^{-r}}^1u^{it}W_C(u)\,du.
\tag{R-93280.4}
\]

Hence, for fixed real `t`,

\[
\mathcal F_C^{\rm cont}(r,t)
=e^{(1/2+it)r}\widehat W_C(1+it)+O_t(e^{-r/2}).
\tag{R-93280.5}
\]

The prime number theorem changes this only by a lower-order relative term.
At `t=1`,

\[
\widehat W_C(1+i)
=
\frac{(1-4^{-i})i}{3(2+i)(3+i)(4+i)}\ne0.
\tag{R-93280.6}
\]

Indeed `0<log 4<2<2 pi`, so `4^{-i}=e^{-i log 4}` is not one.
Consequently

\[
\int_0^\infty|\mathcal F_C(r,1)|^2\,dr=\infty.
\tag{R-93280.7}
\]

Thus the raw, unweighted `L2(dr)` statement called `SID_H` in `L-93273.6`
cannot hold uniformly in the carrier. This is a genuine interface failure, not
merely a weak bound.

## 3. Correct replacement

The continuous mode must be removed and one extra factor `e^{-r/2}` must be
inserted before taking scale energy. `L-93280` constructs that centered safe-line
field exactly. `L-93281` then uses the phase-locked Q4 adjoint to cancel the
critical-boundary poles in the cubic synthesis kernel.

```text
factor-64 physical bank                  retained
factor-64 printed Mellin plus sign       corrected to multiplication
raw SID_H scale L2 norm                  false
centered safe-line scale field           constructed in L-93280
Riemann Hypothesis                       unproved
```
