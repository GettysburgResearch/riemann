# T-91302 — Prime Poisson and completed Fisher tangents have explicit compatible Hardy colligations

Claim ID: `T-91302`  
Status: **CORRECTED EXACT PARALLEL COLLIGATIONS; COMMON RENORMALIZED SOURCE MAP OPEN**  
Created: 2026-08-12  
Corrected: 2026-08-12  
Depends on: `T-91301`, `L-91306`, `L-91307`, `L-91312`, `L-91313`, `L-91316`, `L-91401`, `R-91402`  
RH status: **unproved**

## 1. Correction to the first version

The first version asserted one completed source embedding

```text
prime Poisson-Fock output
 -> completed Fisher-Hardy tangent
  + positive auxiliary.
```

That statement merged two distinct positive sources without constructing the
map between them.

`R-91402`, using Nakamura's published theorem, proves that at every safe scale
`a>1/2` the completed xi law

\[
 \frac{\xi(1/2+a-it)}{\xi(1/2+a)}
\]

is quasi-infinitely divisible but not infinitely divisible.  It therefore
cannot itself be the positive Poisson/Levy law of the ordinary-prime source.

The exact retained theorem is a pair of compatible explicit colligations.  The
renormalized common-source map between them remains open.

## 2. Ordinary-prime Poisson colligation

At the fixed safe scale

\[
 a_0=4,
\]

`L-91307/T-91301` give the positive atomic first-chaos measure

\[
 d\beta_4(u)
 =4\sum_{n=p^k}\Lambda(n)n^{-9/2}
  \delta_{\log n}(du),
\tag{T-91302.1}
\]

its exact Hardy tail-Hankel output

\[
 (\mathsf H_{\beta_4}g)(t)
 =\int_{u>t}g(u-t)d\beta_4(u),
\tag{T-91302.2}
\]

and the explicit Julia identity

\[
 \boxed{
 \|g\|^2
 =\|\mathsf H_{\beta_4}g\|^2
 +\|D_0g\|^2+\|D_1g\|^2+\|D_2g\|^2.
 }
\tag{T-91302.3}
\]

Thus the actual ordinary-prime source-linear Poisson component has a complete
positive-metric Hardy dilation.

## 3. Completed Fisher/model-space colligation

For every safe `a>1/2`, let `P_a` be the completed xi probability law of
`L-91309`.  The vector Fisher--Hankel source operator `A_a` and normalized score
observation `C_a` of `L-91316` satisfy

\[
 \boxed{
 \mathcal J_a
 =a\sqrt{2V_a}\,\mathcal C_a\mathcal A_a,
 }
\tag{T-91302.4}
\]

where

\[
 V_a=\operatorname{Var}_{P_a}(Y).
\]

Consequently

\[
 \boxed{
 2a^2V_a\mathcal A_a^*\mathcal A_a
 =\mathcal J_a^*\mathcal J_a
  +2a^2V_a
    \mathcal A_a^*(I-\mathcal C_a^*\mathcal C_a)
    \mathcal A_a.
 }
\tag{T-91302.5}
\]

This is an explicit positive completed Fisher-to-model-space colligation.

## 4. Gamma/pole and delay compatibility

`L-91306` identifies the gamma/pole factor as the skew connection in a moving
unitary factorization of Suzuki's completed multiplier.  It places the
ordinary-prime phase derivative and the completion in the same observed
boundary tangent.

Raw delay does not preserve `K_(Theta_a)`.  The corrected delay colligation of
`L-91401` is

\[
 \boxed{
 S_\tau g=T_\tau g+M_{\Theta_a}R_\tau g,
 }
\tag{T-91302.6}
\]

with

\[
 T_\tau^*T_\tau+R_\tau^*R_\tau=I,
\tag{T-91302.7}
\]

and the exact mixed-delay identity

\[
 \boxed{
 \langle S_{\tau_i}g_i,S_{\tau_j}g_j\rangle
 =\langle T_{\tau_i}g_i,T_{\tau_j}g_j\rangle
  +\langle R_{\tau_i}g_i,R_{\tau_j}g_j\rangle.
 }
\tag{T-91302.8}
\]

Reflection supplies the opposite Hardy orientation.  The two components of
the finite bridge have the same explicit resident/leakage decomposition.

Thus orientation and delay geometry are closed without the false invariance
claim.

## 5. What compatibility does and does not mean

The two colligations recover compatible pieces of the same completed boundary
tangent:

```text
ordinary-prime Poisson source
 -> prime Hardy Hankel output + Julia reserve;

completed xi Fisher source
 -> Suzuki model-space tangent + Fisher reserve.
```

They also use the same gamma/pole covariant connection and the same compressed
delay geometry.

This does **not** yet give an isometry or contraction from the first source to
the second.  Equality of the observed scalar derivative does not identify the
source metrics or their orthogonal complements.

Higher Poisson chaoses remain unused by a source-linear output once the prime
Poisson product system is fixed, as in `L-91036`.  They cannot turn a non-ID
completed law into the same positive Poisson law.

## 6. Correct remaining source theorem

Construct explicitly a renormalized map

\[
 \boxed{
 \mathcal W_a:
 \mathcal H_a^{\rm prime\ Poisson}
 \oplus\mathcal H_a^{\Gamma,\rm pole,\theta}
 \longrightarrow
 L^2(P_a;H^2)
 \oplus\mathcal E_a^{\rm ren}
 }
\tag{T-91302.9}
\]

such that:

1. its visible component is `A_a`;
2. its ordinary-prime visible block is `H_(beta_a)`;
3. its completion block is the covariant gamma/pole connection;
4. it intertwines `(T_tau,R_tau)` for every positive delay;
5. it includes both orientations and the bridge;
6. it is coefficient-one and positive metric.

This is the renormalized Julia/Wick/Green source theorem.

## 7. Final defect theorem after source identification

Only after (T-91302.9) is constructed does the source-minus-output defect have
a legitimate common-source meaning.  The final RH-bearing identity is then

\[
 \boxed{
 \mathcal D_a^{\rm ren}
 =\mathbb K_a^{\rm del},
 }
\tag{T-91302.10}
\]

where `K_a^del` is the corrected delayed zeta screw/Weil Gram, with every
carrier, delay, orientation, bridge and coefficient-one normalization retained.

If (T-91302.9)--(T-91302.10) hold, the delayed Gram is positive and corrected
`T-91008` gives RH.  Neither statement has been established.

## 8. Exact boundary

```text
ordinary-prime Poisson tail-Hankel Julia dilation       EXACT
completed gamma/pole covariant connection               EXACT
completed Fisher/model-space colligation                EXACT
raw-delay model-space invariance                         REFUTED
compressed delays and all mixed cross terms              EXACT
completed xi Fisher law = positive Poisson law           REFUTED
common renormalized Poisson/Julia -> Fisher source map   OPEN
renormalized auxiliary = delayed screw/Weil defect       OPEN / RH-BEARING
Riemann Hypothesis                                       UNPROVED
```
