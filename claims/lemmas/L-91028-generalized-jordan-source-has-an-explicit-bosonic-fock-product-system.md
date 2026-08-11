# L-91028 — The generalized-Jordan source has an explicit bosonic Fock product system

Claim ID: `L-91028`  
Status: **PROPOSED COMPLETE EXACT FOCK/POISSON THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014`, the Euler product in `Re(s)>1`  
RH status: **unproved**

## 1. Purpose

`L-91014` constructs a coefficient-one divisor-splitting isometry for

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)},
 \qquad a>0.
\]

The present lemma identifies the complete positive source behind that isometry:
it is a bosonic Fock product system over a radial prime-power birth process.
The construction is explicit, scale-local and coassociative.  It replaces the
abstract Stinespring environment of `L-91020` by a concrete Poisson/Fock space.

## 2. The one-particle radial source

Let

\[
 \mathcal P^*=\{p^r:p\text{ prime},\ r\ge1\}
\]

be the prime powers.  On

\[
 (0,\infty)\times\mathcal P^*
\]

use the measure

\[
 d\mu(\tau,n)=2\Lambda(n)\,d\tau,
\]

where the second coordinate carries counting measure.  Put

\[
 \mathfrak h=L^2((0,\infty)\times\mathcal P^*,d\mu).
\]

For `a>0` and `Re(s)>1/2`, define

\[
 \boxed{
 v_{a,s}(\tau,n)
 =\mathbf1_{[0,a]}(\tau)n^{-s-\tau}.
 }
 \tag{L-91028.1}
\]

Then, for `Re(s),Re(t)>1/2`,

\[
\begin{aligned}
 \langle v_{a,s},v_{a,t}\rangle_{\mathfrak h}
 &=\sum_{n\in\mathcal P^*}
 2\Lambda(n)n^{-s-\overline t}
 \int_0^a n^{-2\tau}d\tau\\
 &=\sum_{n\in\mathcal P^*}
 \frac{\Lambda(n)}{\log n}
 (1-n^{-2a})n^{-s-\overline t}.
\end{aligned}
 \tag{L-91028.2}

For `n=p^r`, `Lambda(n)/log(n)=1/r`, and the Euler product gives

\[
 \boxed{
 \langle v_{a,s},v_{a,t}\rangle
 =\log Q_a(s+\overline t).
 }
 \tag{L-91028.3}

The series converges absolutely because `Re(s+conj(t))>1`.

## 3. Symmetric Fock realization

Let

\[
 \Gamma_s(\mathfrak h)
 =\bigoplus_{m\ge0}\mathfrak h^{\widehat\otimes m}
\]

be symmetric Fock space, and use the unnormalised exponential vectors

\[
 \operatorname{Exp}(v)
 =\bigoplus_{m\ge0}\frac{v^{\otimes m}}{\sqrt{m!}}.
\]

Their inner product is

\[
 \langle\operatorname{Exp}(v),\operatorname{Exp}(w)\rangle
 =e^{\langle v,w\rangle}.
\]

Therefore (L-91028.3) yields

\[
 \boxed{
 \langle\operatorname{Exp}(v_{a,s}),
        \operatorname{Exp}(v_{a,t})\rangle
 =Q_a(s+\overline t).
 }
 \tag{L-91028.4}

The coherent vectors `k_(a,s)` of `L-91014` have the same Gram kernel.  Hence
there is a canonical unitary between their closed coherent spans,

\[
 \boxed{
 U_a:\overline{\operatorname{span}}\{k_{a,s}:\Re s>1/2\}
 \longrightarrow
 \overline{\operatorname{span}}\{\operatorname{Exp}(v_{a,s}):\Re s>1/2\},
 }
 \tag{L-91028.5}

with

\[
 U_ak_{a,s}=\operatorname{Exp}(v_{a,s}).
\]

Thus the positive Jordan kernel is literally a bosonic coherent-state kernel.

## 4. Exact radial product system

Split the one-particle interval as

\[
 [0,a+b]=[0,a]\sqcup[a,a+b].
\]

After translating the second interval by `a`,

\[
 v_{a+b,s}|_{[0,a]}=v_{a,s},
\]

and

\[
 v_{a+b,s}(a+u,n)
 =n^{-s-a-u}=v_{b,s+a}(u,n).
\]

Hence

\[
 \boxed{
 v_{a+b,s}=v_{a,s}\oplus S_av_{b,s+a},
 }
 \tag{L-91028.6}

where `S_a` is the interval-translation unitary.  The standard Fock
factorisation

\[
 \Gamma_s(\mathfrak h_{[0,a+b]})
 \simeq
 \Gamma_s(\mathfrak h_{[0,a]})\otimes
 \Gamma_s(\mathfrak h_{[a,a+b]})
\]

then gives

\[
 \boxed{
 \operatorname{Exp}(v_{a+b,s})
 =\operatorname{Exp}(v_{a,s})\otimes
  \operatorname{Exp}(v_{b,s+a}).
 }
 \tag{L-91028.7}

Equation (L-91028.7) is the Fock realization of both the analytic cocycle

\[
 Q_{a+b}(s+\overline t)
 =Q_a(s+\overline t)Q_b(s+\overline t+2a)
\]

and the divisor isometry of `L-91014`.  Associativity is now ordinary
associativity of interval decomposition, so the pentagon identity is automatic.

## 5. Prime powers as independent radial births

The logarithm of the source is

\[
 \boxed{
 \log Q_a(z)
 =\sum_{n\in\mathcal P^*}
 \frac{\Lambda(n)}{\log n}
 (1-n^{-2a})n^{-z}.
 }
 \tag{L-91028.8}

The factor

\[
 1-n^{-2a}
 =\int_0^a2\log(n)e^{-2\tau\log n}d\tau
\]

is the distribution function of an exponential radial birth time of rate
`2 log(n)`.  Thus each prime-power species is born independently along the
radial coordinate, and the shift `z -> z+2a` in the second cocycle factor is
exactly survival through the first interval.

This gives a probabilistic interpretation of the coefficient-one rule:

```text
old prime-power particles survive into the delayed state;
new births occupy an independent Fock interval;
no particle and no norm is spent twice.
```

## 6. Boundary multiplier is compound Poisson

For `c>1`, define

\[
 M_{a,c}(\theta)=\frac{Q_a(c+i\theta)}{Q_a(c)}.
\]

Put

\[
 \boxed{
 \nu_{a,c}
 =\sum_{n\in\mathcal P^*}
 \frac{\Lambda(n)}{\log n}
 (1-n^{-2a})n^{-c}\,\delta_{\log n}.
 }
 \tag{L-91028.9}

This is a finite positive measure.  Equation (L-91028.8) gives

\[
 \boxed{
 M_{a,c}(\theta)
 =\exp\left\{
  \int_0^\infty(e^{-i\theta u}-1)d\nu_{a,c}(u)
 \right\}.
 }
 \tag{L-91028.10}

Hence the anchor variable `T=log(n)` of `L-91019/L-91020` is exactly compound
Poisson, not merely an abstract probability law.  The random-unitary
Stinespring representation of the Schur channel is the boundary representation
of the same Poisson Fock space.

At the resident boundary `c=1+2a`, (L-91028.10) is precisely the multiplier
`M_a(theta)` of `L-91020`.

## 7. Wiener--Itô chaos and finite source jets

Every polynomial logarithmic jet of order `d` lives in the first `d` orthogonal
polynomial/Poisson-chaos levels of this Fock environment.  In particular:

```text
second source jet: one returned state plus two details;
cubic source jet:  one returned state plus three details.
```

This recovers the state counts of `L-91019` and `L-91025` as finite-chaos
statements.  It also identifies the correct environment in which the missing
source/physical intertwiner must live.

## 8. Boundary

Closed here, subject to independent review:

```text
explicit one-particle prime-power space;
Jordan kernel = bosonic exponential-vector kernel;
exact radial Fock product system;
coassociative coefficient-one scale propagation;
prime powers as independent exponential radial births;
compound-Poisson boundary multiplier;
Poisson-chaos interpretation of finite source jets.
```

Still open:

```text
unitary identification of the Poisson-Fock complement with the completed
  causal Hardy/scattering output;
positivity of the completed fixed-scale screw Gram;
RH.
```
