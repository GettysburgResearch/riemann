# L-19876 — The Jordan tail-Hankel block is an exact radial carrier-anticommutator mixture

Claim ID: `L-19876`  
Status: **PROVED EXACT POSITIVE RADIAL-MIXTURE / TWO-CARRIER SOURCE THEOREM**  
Created: 2026-08-13  
Depends on: corrected scope of `L-19874`, `L-91307`  
RH status: **no RH input**

## 1. Measures

For `a>0`, `c>1`, and a prime-power carrier `u=log(p^k)`, retain

\[
 d\omega^J_{a,c}(u)
 =\frac{1-(1+2au)e^{-2au}}{ka^2}e^{-cu}\,\delta_u,
\tag{L-19876.1}
\]
and introduce the two-parameter ordinary-prime score measure

\[
 d\beta_{b,c+2b}(u)
 =b\frac uk e^{-(c+2b)u}\,\delta_u,
 \qquad0<b<a.
\tag{L-19876.2}
\]

This is a positive scalar multiple of a genuine safe scattering-score measure.
With

\[
 a_b=c+2b-\frac12>\frac12,
\]

the measure `beta_(a_b)` of `L-91307` is supported on the same safe line and

\[
 \boxed{
 \beta_{b,c+2b}=\frac{b}{a_b}\,\beta_{a_b}.
 }
\tag{L-19876.2a}
\]

Thus the radial mixture below uses positive scalar multiples of actual
ordinary-prime scattering chaoses, not an invented signed source.

## 2. Exact positive radial mixture

The elementary integral

\[
 \int_0^ab e^{-2bu}db
 =\frac{1-(1+2au)e^{-2au}}{4u^2}
\tag{L-19876.3}
\]
gives the measure identity

\[
\boxed{
 d\omega^J_{a,c}(u)
 =\frac4{a^2}\int_0^a u\,d\beta_{b,c+2b}(u)\,db.
}
\tag{L-19876.4}
\]

Every measure in the integrand is positive.  Thus the Jordan source is not one
ordinary-prime score source multiplied on the input; it is a continuum of safe
ordinary-prime sources with one carrier derivative.

## 3. Exact first-chaos embedding

Let

\[
 \mathcal K_{a,c}
 =\int_0^a{}^\oplus L^2(\beta_{b,c+2b})\,db.
\]
Define

\[
\boxed{
 (\mathcal J_{a,c}f)(b,u)=\frac2a\sqrt u\,f(u).
}
\tag{L-19876.5}
\]

By (L-19876.4),

\[
 \|\mathcal J_{a,c}f\|_{\mathcal K_{a,c}}^2
 =\int|f(u)|^2d\omega^J_{a,c}(u).
\tag{L-19876.6}
\]
Hence `mathcal J_(a,c)` is an explicit isometric embedding.  It commutes with
carrier multiplication and every delay phase `exp(-itau u)`.

The range is the closed radial-diagonal subspace consisting of fields whose
`b` dependence is fixed by (L-19876.5).  Surjectivity onto the full direct
integral is neither needed nor claimed.

## 4. Triangular two-carrier lift

On the triangular domain `0<t<u`, put `s=u-t`.  Lift (L-19876.5) fibrewise and
use the pointwise identity

\[
 u=t+s.
\]
The scalar source amplitude has the exact two-port isometry

\[
\boxed{
 \frac2a\sqrt u\,F(t,u)
 \longmapsto
 \frac2a
 \begin{pmatrix}
  \sqrt t\,F(t,u)\\
  \sqrt{u-t}\,F(t,u)
 \end{pmatrix},
}
\tag{L-19876.7}
\]
because the squared norms add to `4u|F|^2/a^2`.

Applied to the triangular synthesis, the Jordan source becomes the direct
integral of two ordinary-prime triangular ports

```text
output-carrier port: sqrt(t) g(u-t);
input-carrier port:  sqrt(u-t) g(u-t).
```

This is the correct source-level replacement for the false single input
multiplier in `L-19874.20`.

## 5. Tail-Hankel anticommutator formula

Let `M` denote multiplication by the positive half-line variable, on the input
or output space as indicated.  From (L-19876.4),

\[
\begin{aligned}
 (H_{\omega^J_{a,c}}g)(t)
 &=\frac4{a^2}\int_0^a
   \int_{u>t}u\,g(u-t)d\beta_{b,c+2b}(u)db\\
 &=\frac4{a^2}\int_0^a
   \left[
    tH_{\beta_{b,c+2b}}g(t)
    +H_{\beta_{b,c+2b}}(Mg)(t)
   \right]db.
\end{aligned}
\]
Therefore, on the finite-cylinder/core domain,

\[
\boxed{
 H_{\omega^J_{a,c}}
 =\frac4{a^2}\int_0^a
 \bigl(MH_{\beta_{b,c+2b}}
       +H_{\beta_{b,c+2b}}M\bigr)\,db.
}
\tag{L-19876.8}
\]

This is an exact carrier anticommutator, not an estimate.  It retains every
carrier cross term and displays explicitly the extra derivative port that the
single-multiplier argument omitted.

## 6. Consequence for the completed source programme

At a fixed safe base line, each `beta_(b,c+2b)` can be supplied with the
conditional-variance/Julia environment of `L-91307` whenever its tail mass is
contractive.  The Jordan block must then be assembled as the radial coherent
mixture (L-19876.8), retaining both carrier ports and their radial cross terms.

The theorem does not identify the resulting direct-integral environment with
the completed Fisher, theta, bridge or delayed Weil environment.  It converts
the previously false source arrow into a precise constructive problem.

```text
Jordan measure as positive radial prime mixture        EXACT
explicit first-chaos isometric embedding               EXACT
two carrier ports from u=t+(u-t)                       EXACT
Jordan tail-Hankel anticommutator formula               EXACT
single ordinary-prime Julia block                       INSUFFICIENT
radial Julia/Fisher/bridge source lock                  OPEN / RH-BEARING
Riemann Hypothesis                                      UNPROVEN
```
