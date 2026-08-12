# L-91411 — Nakamura's completion is a gamma ladder minus one pole Hardy channel

Claim ID: `L-91411`  
Status: **PROVED EXACT SOURCE DECOMPOSITION AND HARDY-RANK THEOREM; RECURRENCE SIGN OPEN**  
Created: 2026-08-12  
Depends on: Nakamura 2015 source lock; `L-91306`, `L-91402`, `L-91410`  
RH status: **unproved**

## 1. The plastic-constant split is not the only positive-source split

Fix

\[
 \sigma>1
\]

and retain Nakamura's continuous signed quasi-Lévy density

\[
 q_\sigma(u)
 =\frac{e^{-\sigma u}}u
  \left[
   \frac1{1-e^{-2u}}-(1+e^u)
  \right],
 \qquad u>0.
 \tag{L-91411.1}
\]

The identity

\[
 \frac1{1-e^{-2u}}
 =1+\sum_{m\ge1}e^{-2mu}
\]

gives the exact expansion

\[
 \boxed{
 q_\sigma(u)du
 =\sum_{m\ge1}
   \frac{e^{-(\sigma+2m)u}}u\,du
  -\frac{e^{-(\sigma-1)u}}u\,du.
 }
 \tag{L-91411.2}
\]

Define positive Lévy measures

\[
 d\gamma_{\sigma,m}(u)
 =\frac{e^{-(\sigma+2m)u}}u\,du,
 \qquad m\ge1,
 \tag{L-91411.3}
\]

and the positive pole measure

\[
 d\pi_\sigma(u)
 =\frac{e^{-(\sigma-1)u}}u\,du.
 \tag{L-91411.4}
\]

If

\[
 d\mathsf N_\sigma(u)
 =\sum_{p,r\ge1}
  \frac{p^{-r\sigma}}r
  \delta_{r\log p}(du),
 \tag{L-91411.5}
\]

then Nakamura's full signed quasi-Lévy measure has the exact source-typed form

\[
 \boxed{
 d\nu_\sigma
 =d\mathsf N_\sigma
  +\sum_{m\ge1}d\gamma_{\sigma,m}
  -d\pi_\sigma.
 }
 \tag{L-91411.6}
\]

Thus the continuous archimedean completion is not intrinsically an extended
negative tail.  It is one positive gamma ladder and one negative pole channel.
The plastic-constant Jordan split of `L-91402` and the ladder/pole split here
are two positive-metric realizations of the same signed measure.

## 2. Exact completed phase derivative

Put

\[
 \Theta_\sigma(t)
 =\frac{\xi(\sigma+it)}{\xi(\sigma-it)},
 \qquad t\in\mathbb R,
 \tag{L-91411.7}
\]

and

\[
 r_\alpha(t)
 =\frac1{\alpha-it}-\frac1{\alpha+it}
 =\frac{2it}{\alpha^2+t^2},
 \qquad \alpha>0.
 \tag{L-91411.8}
\]

The prime component is

\[
 \boxed{
 \chi_\sigma^{\rm p}(t)
 =\sum_{n=p^k}
  \Lambda(n)n^{-\sigma}
  \left(e^{it\log n}-e^{-it\log n}\right).
 }
 \tag{L-91411.9}
\]

Using

\[
 \frac{\xi'}{\xi}(s)
 =\frac1s+\frac1{s-1}
  -\frac12\log\pi
  +\frac12\frac{\Gamma'}{\Gamma}(s/2)
  +\frac{\zeta'}{\zeta}(s),
 \tag{L-91411.10}
\]

and the digamma series

\[
 \frac12\left[
  \psi\!\left(\frac{\sigma+it}{2}\right)
  -\psi\!\left(\frac{\sigma-it}{2}\right)
 \right]
 =\sum_{m\ge0}r_{\sigma+2m}(t),
 \tag{L-91411.11}
\]

the `m=0` term cancels the factor `1/s`.  Hence

\[
 \boxed{
 \partial_\sigma\log\Theta_\sigma(t)
 =\chi_\sigma^{\rm p}(t)
  +\sum_{m\ge1}r_{\sigma+2m}(t)
  -r_{\sigma-1}(t).
 }
 \tag{L-91411.12}
\]

This is the transform-side version of (L-91411.6).  It contains no arbitrary
Lévy compensation threshold and no unevaluated drift: the deterministic terms
have recombined into the one pole channel.

## 3. One positive Hilbert source with one negative observation sign

Define

\[
 \mathcal S_\sigma^{\rm lad}
 =L^2(\mathsf N_\sigma)
  \oplus\bigoplus_{m\ge1}L^2(\gamma_{\sigma,m})
  \oplus L^2(\pi_\sigma).
 \tag{L-91411.13}
\]

Every summand has a positive metric.  The completed phase tangent is obtained
by observing the first two families with sign `+` and the final pole family
with sign `-`.

The ordinary-prime Poisson first chaos remains an orthogonal direct summand.
The gamma ladder is the completed positive archimedean environment.  All
indefiniteness of the one-scale tangent source is concentrated in one pole
channel.

## 4. Every ladder rung has rank-one Hardy compression

Let `H2_plus` and `H2_minus` be the two Hardy boundary spaces, with norm

\[
 \|f\|^2=\frac1{2\pi}\int_\mathbb R|f(t)|^2dt.
\]

For `alpha>0`, define on the common rational Hardy core

\[
 \mathsf H_{\sigma,\alpha}
 =P_-M_{\Theta_\sigma r_\alpha}P_+.
 \tag{L-91411.14}
\]

The factor `1/(alpha-it)` is analytic in the upper half-plane and contributes
no Hankel block.  The other term has one upper-half-plane pole.  For
`f in H2_plus`, partial fractions give

\[
 \boxed{
 (\mathsf H_{\sigma,\alpha}f)(t)
 =i\,\Theta_\sigma(i\alpha)
   \frac{f(i\alpha)}{t-i\alpha}.
 }
 \tag{L-91411.15}
\]

Therefore

\[
 \boxed{
 \operatorname{rank}\mathsf H_{\sigma,\alpha}=1
 }
 \tag{L-91411.16}
\]

unless the displayed scalar vanishes, and

\[
 \boxed{
 \|\mathsf H_{\sigma,\alpha}f\|^2
 =\frac{|\Theta_\sigma(i\alpha)|^2}{2\alpha}
  |f(i\alpha)|^2.
 }
 \tag{L-91411.17}
\]

No RH input is used.  The denominator of `Theta_sigma` is zero-free in the
upper half-plane because `sigma>1`.

## 5. Exact arithmetic values of the observation weights

For the pole channel

\[
 \alpha_0=\sigma-1,
\]

one has

\[
 \boxed{
 \Theta_\sigma(i\alpha_0)
 =\frac{\xi(1)}{\xi(2\sigma-1)}.
 }
 \tag{L-91411.18}
\]

For the gamma ladder

\[
 \alpha_m=\sigma+2m,
 \qquad m\ge1,
\]

functional symmetry gives

\[
 \boxed{
 \Theta_\sigma(i\alpha_m)
 =\frac{\xi(-2m)}{\xi(2\sigma+2m)}
 =\frac{\xi(1+2m)}{\xi(2\sigma+2m)}.
 }
 \tag{L-91411.19}
\]

Thus every rank-one rung has an explicit safe arithmetic weight.

## 6. Relation to the completed Fisher and Julia pictures

The quasi-Lévy source of `L-91402` stores the sign by a two-channel score
vector.  The present realization stores the same sign as

```text
prime atoms             positive;
gamma ladder            positive;
one pole channel        negative.
```

After the Hardy projection, the pole channel is one evaluation functional and
each gamma rung is another evaluation functional.  This turns the
archimedean part of the source problem into a concrete Hardy sampling and
Schur-complement problem.

## 7. Scope firewall for the coefficient-one Cauchy recurrence

Equation (L-91411.12) is a **one-scale tangent** statement.  The Cauchy
recurrence of `L-91404` applies

\[
 \frac{c}{4i}(1-c\partial_c)\partial_x
\]

at the three scales `c=a,2a,4a`.  The scale derivative turns a simple rung into
at most a double-pole/rank-two Hardy port.  Moreover the middle recurrence
coefficient is negative, so its entire positive gamma ladder enters the
negative side before the three scales are recombined.

Consequently the exact rank-one pole theorem must not be promoted to a
rank-one theorem for the complete recurrence or delayed screw form.  It is a
new source normal form and a sharper local port dictionary, not an RH proof.

## 8. Exact boundary

```text
Nakamura continuous density = gamma ladder - pole     EXACT
gamma and pole measures positive individually         EXACT
completed phase derivative ladder formula             EXACT
prime first chaos retained as direct summand           EXACT
each ladder/pole Hardy compression rank one            EXACT
explicit xi values of all rung weights                 EXACT
one-scale negative source dimension                    ONE POLE CHANNEL
three-scale recurrence negative source                 STILL NONTRIVIAL
completed delayed source domination                    OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVED
```
