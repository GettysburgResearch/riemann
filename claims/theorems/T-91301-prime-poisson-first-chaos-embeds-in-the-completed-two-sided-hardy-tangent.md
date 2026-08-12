# T-91301 — The prime Poisson first chaos embeds explicitly in the completed two-sided Hardy tangent

Claim ID: `T-91301`  
Status: **PROVED EXACT PRIME-COMPONENT EMBEDDING; COMPLETED CURVATURE DOMINATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91035`, `L-91036`, `L-91306`, `L-91307`, `R-91301`  
RH status: **unproved**

## 1. Statement

Fix

\[
 a_0=4,
 \qquad c_0=\frac92.
\]

Let

\[
 d\beta_4(u)
 =4\sum_{n=p^k}\Lambda(n)n^{-9/2}\delta_{\log n}(du)
\]

and

\[
 (\mathsf H_{\beta_4}g)(t)
 =\int_{(t,\infty)}g(u-t)d\beta_4(u).
\]

Then:

1. `H_(beta_4)` is, after the standard Hardy Fourier reflection, exactly the
   positive-frequency block of the ordinary-prime Suzuki scattering
   connection;
2. there is an explicit positive-metric isometry
   \[
    \mathcal U_{\beta_4}g
    =(\mathsf H_{\beta_4}g,D_0g,D_1g,D_2g)
   \]
   with `D_0,D_1,D_2` given in `L-91307`;
3. reflection gives the anti-causal orientation, and direct sum gives a fully
   polarized two-sided embedding;
4. the explicit gamma/pole boundary factor acts as the skew covariant
   connection of `L-91306`, placing the two prime outputs inside Suzuki's
   completed model-space normal tangent.

Therefore the source-linear prime Poisson output requested by CJHI is not an
abstract Fock square root: it has one explicit first-chaos/tail-Hankel Julia
realization.

## 2. Exact operator diagram

```text
ordinary-prime Poisson score first chaos
       |
       | exact positive atomic measure beta_4
       v
causal tail-Hankel H_(beta_4) + explicit Julia environment
       |
       | reflection / direct sum / delay unitaries
       v
prime two-sided Hardy tangent
       |
       | gamma/pole moving-unitary connection M_(Gamma_4)
       v
Suzuki completed two-sided model-space normal tangent.
```

At operator level,

\[
 P_-M_{\chi_4^{\rm p}}P_+
 \simeq\mathsf H_{\beta_4},
 \tag{T-91301.1}
\]

and

\[
 \boxed{
 (I-Q_4)a\partial_aM_{\Theta_a}|_{a=4}
 =M_{\Gamma_4}(I-R_4)
 \left[a\partial_aV_a+A_4V_a\right]_{a=4}.
 }
 \tag{T-91301.2}
\]

The prime component inside the bracket is (T-91301.1); `A_4` is the explicit
gamma/pole connection.

## 3. Why higher Fock chaos disappears

`L-91036` proves that a source-linear target annihilates every Poisson chaos of
order at least two. Consequently the full bosonic Fock space contributes only

```text
vacuum/amplitude channel
+ first-chaos tangent channel
+ orthogonal unused environment.
```

The first item is completed by Suzuki's imported amplitude isometry
`L-91035`; the second is completed by `L-91307`. Higher chaos is not a missing
output port.

## 4. What is and is not completed

The following component is now closed:

\[
 \boxed{
 \text{prime Poisson-Fock source-linear output}
 \longrightarrow
 \text{completed two-sided Hardy tangent plus positive auxiliary reserve}.
 }
\]

The word `completed` means that the archimedean/pole amplitude and its radial
motion are retained as the covariant unitary factor of `L-91306`; they are not
discarded or replaced by a scalar remainder.

This theorem does **not** assert

\[
 C_a^{\rm src}\succeq\mathcal J_a^*\mathcal J_a.
\]

That inequality compares the completed Fisher curvature of `L-91309` with the
square of the **sum** of the prime and gamma/pole Hankel connections. Its cross
term is load bearing. Establishing it is corrected `T-91008` and is
RH-equivalent.

## 5. Source-type firewall

The measure used here is the actual scattering-score measure

\[
 a\Lambda(n)n^{-a-1/2}\delta_{\log n}.
\]

It is not the normalized Jordan-curvature measure of `L-91037`. Replacing one
by the other without an explicit transport violates `R-91301`.

## 6. Exact boundary

```text
Suzuki completed amplitude embedding                 IMPORTED PROVED
source-linear reduction to first chaos               EXACT
ordinary-prime score measure                          EXACT
prime score Hardy Hankel block                        EXACT
explicit positive Julia reserve at a0=4              EXACT
two-sided/reflected/delayed prime embedding           EXACT
gamma/pole covariant placement                        EXACT
completed Fisher curvature >= total Hardy shape      OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```
