# R-91510 — Prime positive-real completion does not by itself close the completed domain wall

Claim ID: `R-91510`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91510/L-91511`; `L-91411/L-91414`  
RH status: **unproved**

## 1. What the prime theorem proves

The safe normalized prime multiplier

\[
 M_{a,\sigma}
 =\frac{Q_a(\sigma+i\cdot)}{Q_a(\sigma)}
\]

is Schur for `sigma>1`. Its Cayley impedance

\[
 h_{a,\sigma}
 =\frac{1-M_{a,\sigma}}
        {1+M_{a,\sigma}}
\]

is positive real, and its complete dissipation is the ordered positive Julia
detail space.

## 2. The completed multiplier is not the prime multiplier

The completed scattering channel includes

```text
the positive prime impedance;
the positive gamma ladder;
one adverse pole channel;
the radial derivative at three scales;
compressed delay leakage;
both Hardy orientations;
the bridge.
```

A product of a Schur multiplier with an active meromorphic factor need not be
Schur. At the source level the middle Cauchy scale also enters with the
opposite sign. Therefore neither of the implications

\[
 M_{a,\sigma}\text{ Schur}
 \Longrightarrow
 \Theta_a\text{ Schur}
\]

or

\[
 h_{a,\sigma}\text{ positive real}
 \Longrightarrow
 \mathbb K_a^{\rm del}\succeq0
\]

is valid without the completed interconnection.

## 3. Scalar control

Let `m` be any Schur function and let `p` be a scalar meromorphic boundary
factor with `|p|>1` on a set of positive measure. Then `pm` can fail to be
Schur even when `m=1`. Its Cayley transform can have negative real part.

This elementary control has the same logical shape as the pole channel in
`L-91411`: positive prime passivity cannot be used as free budget against an
uncoupled active completion.

## 4. Three-scale firewall

The rank-one formula for one gamma or pole rung is a one-scale tangent
statement. CPPD uses the operator

\[
 \frac{c}{4i}(1-c\partial_c)\partial_x
\]

at `c=a,2a,4a`, with signs

\[
 -1,\quad \frac{17}{16},\quad -\frac1{16}.
\]

The scale derivative creates double-pole ports, and the middle positive ladder
is moved to the adverse side. A one-scale Herglotz realization cannot be
summed with absolute values or treated as three independent passive channels.

## 5. Correct consequence

`L-91510/L-91511` close the **prime component** of the parity transfer. The
remaining theorem must couple its returned state and Clark connection to the
continuous domain wall and the deterministic completed connection before any
norm comparison.

## 6. Exact boundary

```text
safe prime multiplier Schur                    EXACT
safe prime Cayley impedance positive real      EXACT
completed scattering automatically Schur       FALSE
one-scale passivity sums through recurrence     FALSE AS A SHORTCUT
prime Clark connection                         CLOSED
archimedean/domain-wall Redheffer completion    OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
