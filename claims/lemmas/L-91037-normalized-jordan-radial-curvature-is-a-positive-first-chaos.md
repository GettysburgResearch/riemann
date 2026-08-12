# L-91037 — The normalized Jordan radial curvature is an explicit positive first chaos

Claim ID: `L-91037`  
Status: **PROPOSED COMPLETE EXACT POSITIVE-CURVATURE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: main `L-91029`, branch `L-91030`, `L-91036`  
RH status: **unproved**

## 1. The normalized source curvature

For `a>0` and `Re(z)>1`, put

\[
 Q_a(z)=\frac{\zeta(z)}{\zeta(z+2a)}
 \tag{L-91037.1}
\]

and define

\[
 \boxed{
 \mathscr C_a^{\rm J}(z)
 =-\partial_a\left[\frac1a\log Q_a(z)\right].
 }
 \tag{L-91037.2}
\]

The Euler logarithm gives

\[
 \boxed{
 \mathscr C_a^{\rm J}(z)
 =\sum_{n=p^k}
 \frac{1-(1+2a\log n)n^{-2a}}{k a^2}
 n^{-z}.
 }
 \tag{L-91037.3}
\]

Every coefficient is nonnegative because

\[
 e^x\ge1+x
 \quad(x\ge0).
\]

It is strictly positive for every prime-power coefficient.

## 2. Exact radial integral

For `L=log n`,

\[
 \boxed{
 1-(1+2aL)e^{-2aL}
 =\int_0^a4rL^2e^{-2rL}dr.
 }
 \tag{L-91037.4}

\]

Since `Lambda(n)/log(n)=1/k` on prime powers, `(L-91037.3)` becomes

\[
 \boxed{
 \mathscr C_a^{\rm J}(z)
 =\frac4{a^2}
  \sum_{n=p^k}\Lambda(n)\log n
  \int_0^a r\,n^{-z-2r}dr.
 }
 \tag{L-91037.5}
\]

Thus the curvature is the radial second moment of the prime-power birth
process, with no signed coefficient.

## 3. One-particle Gram factorization

On

\[
 (0,a)\times\mathcal P^*
\]

with counting measure in the prime-power variable and Lebesgue measure in `r`,
define

\[
 \boxed{
 w_{a,s}(r,n)
 =\frac2a
  \sqrt{r\Lambda(n)\log n}\,
  n^{-s-r}.
 }
 \tag{L-91037.6}
\]

For `Re(s),Re(t)>1/2`,

\[
\begin{aligned}
 \langle w_{a,s},w_{a,t}\rangle
 &=\frac4{a^2}
  \sum_{n=p^k}\Lambda(n)\log n
  \int_0^a r\,n^{-s-\bar t-2r}dr\\
 &=\boxed{
  \mathscr C_a^{\rm J}(s+\bar t).
 }
\end{aligned}
 \tag{L-91037.7}
\]

Hence

\[
 \boxed{
 \left(
 \mathscr C_a^{\rm J}(s_j+\overline{s_k})
 \right)_{j,k}\succeq0
 }
 \tag{L-91037.8}
\]

for every finite safe packet.

The missing normalized-curvature source is therefore not hidden in higher
Poisson chaos.  It is one explicit weighted first-chaos vector.

## 4. Positive boundary spectral measure

For `c>1`, define

\[
 \boxed{
 d\omega_{a,c}(u)
 =\sum_{n=p^k}
 \frac{1-(1+2a\log n)n^{-2a}}{ka^2}
 n^{-c}\delta_{\log n}(u).
 }
 \tag{L-91037.9}

\]

Then

\[
 \boxed{
 \mathscr C_a^{\rm J}(c+i\theta)
 =\int_0^\infty e^{-i\theta u}d\omega_{a,c}(u).
 }
 \tag{L-91037.10}
\]

Thus `mathscr C_a^J` is a positive-definite carrier kernel on every safe
vertical line.  Its increment Gram is

\[
 \int
 (e^{-ixu}-1)(e^{iyu}-1)d\omega_{a,c}(u)\succeq0.
 \tag{L-91037.11}
\]

All carrier polarizations are retained before aggregation.

## 5. Relation to the completed scattering curvature

Main `L-91023` writes the completed scattering amplitude as

\[
 \Theta_a=\Gamma_aQ_a.
\]

The Cauchy soft count and its normalized sixteenfold recurrence are radial
curvatures of the Wigner--Smith delay of `Theta_a`.  Equations
`(L-91037.2)`--`(L-91037.11)` close the complete generalized-prime part of that
curvature on the safe side.

The remaining completed tangent problem is now exactly:

```text
transport the positive first-chaos curvature omega_(a,c)
through Suzuki's gamma/pole Hankel scattering completion,
including its derivative with respect to radial scale,
without creating a negative second-fundamental-form remainder.
```

Suzuki's amplitude isometry `L-91035` performs the zeroth-order transport.  It
does not by itself perform this normalized derivative lift.

## 6. Monotonicity interpretation

Coefficientwise,

\[
 \boxed{
 a\longmapsto
 \frac{1-n^{-2a}}a
 \quad\text{is decreasing.}
 }
 \tag{L-91037.12
}

Therefore

\[
 a\longmapsto\frac1a\log Q_a(z)
\]

is decreasing on every positive real safe argument, and its complete
safe-kernel derivative is negative semidefinite.

This is the source-side analogue of the desired monotonicity of the normalized
completed Clark/Wigner--Smith measure.  The failure to continue this Loewner
order through the completed boundary is the RH-bearing joint.

## 7. Exact boundary

```text
normalized Jordan radial curvature coefficients    EXACT POSITIVE
radial first-chaos Gram factor                      EXACT
full safe cross-carrier polarization                EXACT
safe normalized Jordan Loewner order                EXACT
Suzuki amplitude completion                         IMPORTED CLOSED
completed tangent/Clark-measure order                OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```
