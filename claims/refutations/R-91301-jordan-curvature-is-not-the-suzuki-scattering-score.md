# R-91301 — The normalized Jordan curvature is not the Suzuki scattering score

Claim ID: `R-91301`  
Status: **EXACT SOURCE-TYPE FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91037`, `L-91306`, `L-91307`  
RH status: **unproved**

## 1. Purpose

Several positive prime-power measures occur on the live branch. They must not
be interchanged merely because all are first-chaos Grams. This note records the
exact coefficient mismatch between:

1. the normalized generalized-Jordan curvature of `L-91037`;
2. Suzuki's ordinary-prime logarithmic-radius scattering connection;
3. the normalized ordinary-zeta phase curvature.

Only item 2 feeds the model-space Hankel block in `L-91301/L-91306`.

## 2. Three exact measures

Fix `a>1/2`, put `c=a+1/2`, and write `u=log n` for a prime power
`n=p^k`.

### 2.1 Generalized-Jordan curvature

`L-91037` uses

\[
 \boxed{
 j_a(u,k)
 =\frac{1-(1+2au)e^{-2au}}{ka^2}e^{-cu}.
 }
 \tag{R-91301.1}
\]

### 2.2 Suzuki scattering connection

From `L-91307`, the positive-frequency coefficient of

\[
 \chi_a^{\rm p}=a\partial_a\log
 \frac{\zeta(c+ix)}{\zeta(c-ix)}
\]

is

\[
 \boxed{
 s_a(u,k)=\frac{au}{k}e^{-cu}
 =a\Lambda(n)n^{-c}.
 }
 \tag{R-91301.2}
\]

This is the coefficient of the actual Hardy Hankel block
`P_+M_(chi_a^p)P_-`.

### 2.3 Normalized ordinary-zeta phase curvature

Differentiating

\[
 -i\partial_a\left[
 a^{-1}\log\frac{\zeta(c+ix)}{\zeta(c-ix)}
 \right]
\]

gives sine coefficient

\[
 \boxed{
 r_a(u,k)=
 \frac{2(1+au)}{ka^2}e^{-cu}.
 }
 \tag{R-91301.3}
\]

## 3. The measures are not scalar multiples

The ratios are

\[
 \frac{s_a(u,k)}{j_a(u,k)}
 =\frac{a^3u}{1-(1+2au)e^{-2au}},
 \tag{R-91301.4}
\]

and

\[
 \frac{r_a(u,k)}{s_a(u,k)}
 =\frac{2(1+au)}{a^3u}.
 \tag{R-91301.5}
\]

Both vary nontrivially with `u`. As `u->infinity`,

\[
 \frac{s_a}{j_a}\sim a^3u,
 \qquad
 \frac{r_a}{s_a}\to\frac2{a^2},
\]

whereas the small-`u` behaviours differ again.

Thus no constant renormalization, unitary relabelling of the same atomic basis,
or coefficient-one identification converts one source into another.

## 4. Consequence for the final colligation

The positivity of the Jordan curvature Gram in `L-91037` is genuine, but it
does not by itself dominate Suzuki's model-space shape. A proof must provide an
explicit operator transporting `j_a` to `s_a`, including the gamma/pole
connection and every cross-carrier term, or work with the actual score measure
`s_a` as in `L-91307`.

The following inference is invalid:

```text
positive normalized Jordan first chaos
  + Suzuki amplitude isometry
  => positive scattering tangent Gram.
```

The amplitude isometry is zeroth order, while the two first-chaos measures have
different radial weights.

## 5. What survives

`L-91307` closes the positive-metric Hardy embedding of the actual score measure
`s_a` at one fixed safe scale. `L-91306` places that output inside the completed
gamma/pole connection. The remaining theorem is domination by the **completed**
Fisher curvature of `L-91309`, not a silent identification with
(R-91301.1).

## 6. Exact boundary

```text
Jordan curvature positivity                         RETAINED EXACT
ordinary-prime scattering score                     EXACT
normalized ordinary phase curvature                 EXACT
three measures identical up to scale                FALSE
Jordan positivity alone closes Suzuki tangent       FALSE
actual score tail-Hankel Julia dilation              L-91307
completed Fisher-to-shape domination                 OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
