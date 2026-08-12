# L-91521 — Annular log mass is an explicit Green potential with a quantitative zero moat

Claim ID: `L-91521`  
Status: **PROVED EXACT ZERO-BY-ZERO GREEN FORMULA AND LOWER BOUND**  
Created: 2026-08-12  
Depends on: `L-91520`  
RH status: **unproved**

## 1. One right-half-plane Blaschke zero

Let

\[
 \zeta=x+iy,
 \qquad x>0,
\]

be a zero coordinate of a right-half-plane Blaschke product, with
multiplicity `m`. Use the canonical factor

\[
 b_\zeta(z)=\frac{z-\zeta}{z+\overline\zeta}
\]

up to an irrelevant unimodular constant. At a real interior node `eta>0`,

\[
\boxed{
 |b_\zeta(\eta)|^{-2}
 =\frac{(\eta+x)^2+y^2}
        {(\eta-x)^2+y^2}.
}
\tag{L-91521.1}

\]

Its logarithmic Green mass is

\[
\boxed{
 g_\eta(\zeta)
 =\log\frac{(\eta+x)^2+y^2}
             {(\eta-x)^2+y^2}>0.
}
\tag{L-91521.2}

\]

## 2. Exact zero-by-zero formula

Let `C_(a,b)` be the annular Blaschke product, with distinct zero coordinates
`zeta` and multiplicities `m_zeta`. The Blaschke condition gives absolute
convergence at every fixed interior node, and

\[
\boxed{
 \Lambda_{a,b}^{\rm ann}(\eta)
 =\sum_{\zeta\in Z_{a,b}}
  m_\zeta\,g_\eta(\zeta).
}
\tag{L-91521.3}

\]

Thus the additive annular innovation is a sum of strictly positive individual
zero charges. No cancellation between crossed zeros is possible in this
coordinate.

## 3. Green–Laplace representation

Assume `eta>x`, which holds for the fixed node `eta=1` in the horizontal
zeta-zero coordinates used by the one-node route. The elementary logarithm
identity gives

\[
\boxed{
 g_\eta(x+iy)
 =4\int_0^\infty
  e^{-\eta t}
  \frac{\sinh(xt)\cos(yt)}{t}\,dt.
}
\tag{L-91521.4}

\]

Indeed, apply

\[
 \log\frac BA
 =\int_0^\infty\frac{e^{-At}-e^{-Bt}}t\,dt
\]

to

\[
 A=\eta-x-iy,
 \qquad
 B=\eta+x-iy,
\]

and take twice the real part.

Equation (L-91521.4) places the model annular defect in the same one-node
Laplace coordinates as the Cauchy and one-Green arithmetic sources.

## 4. Quantitative moat

Write

\[
 t_\zeta
 =\frac{4\eta x}
        {(\eta-x)^2+y^2}>0.
\]

Then `g_eta(zeta)=log(1+t_zeta)`. Since

\[
 \log(1+t)\ge\frac{t}{1+t},
\]

we obtain

\[
\boxed{
 g_\eta(\zeta)
 \ge
 \frac{4\eta x}
      {(\eta+x)^2+y^2}.
}
\tag{L-91521.5}

\]

Consequently

\[
\boxed{
 \Lambda_{a,b}^{\rm ann}(\eta)
 \ge
 \sum_{\zeta\in Z_{a,b}}
 m_\zeta
 \frac{4\eta\Re\zeta}
      {|\eta+\overline\zeta|^2},
}
\tag{L-91521.6}

\]

and, because `e^Lambda-1>=Lambda`,

\[
\boxed{
 H_{a,b}^{\rm ann}(\eta)
 \ge
 \sum_{\zeta\in Z_{a,b}}
 m_\zeta
 \frac{2\Re\zeta}
      {|\eta+\overline\zeta|^2}.
}
\tag{L-91521.7}

\]

Thus any crossed zero creates an explicit positive moat at the fixed node.
For a zero with `Re zeta>=x0` and `|Im zeta|<=Y`,

\[
 H_{a,b}^{\rm ann}(\eta)
 \ge
 \frac{2x_0}{(\eta+x_{\max})^2+Y^2}
\]

with the evident annular upper bound on `x`.

## 5. Upper control

The converse elementary inequality `log(1+t)<=t` gives

\[
\boxed{
 \Lambda_{a,b}^{\rm ann}(\eta)
 \le
 \sum_{\zeta\in Z_{a,b}}
 m_\zeta
 \frac{4\eta\Re\zeta}
      {|\eta-\zeta|^2},
}
\tag{L-91521.8}

\]

whenever the node is not itself a zero. Hence the logarithmic innovation is
quantitatively equivalent to the one-node Green potential of the annular zero
measure.

## 6. Strategic consequence

The remaining one-node arithmetic theorem can now be targeted at one linear
Green quantity:

\[
 \Lambda_{a_j,a_{j-1}}^{\rm ann}(1).
\]

A source identity forcing this scalar to zero automatically deletes every
crossed zero in the annulus. The nonlinear hyperbolic mass and its inherited
multiplicative weight no longer need to be tracked.

## 7. Exact boundary

```text
one-zero Blaschke mass                         EXACT
annular log mass = sum of positive zero charges EXACT
Green-Laplace representation                   EXACT
quantitative one-node moat                     EXACT
arithmetic identification of the Green mass    OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
