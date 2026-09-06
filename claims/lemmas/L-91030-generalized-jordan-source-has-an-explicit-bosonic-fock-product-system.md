# L-91030 — The generalized-Jordan source is an explicit bosonic Fock product system

Claim ID: `L-91030`  
Status: **PROPOSED COMPLETE EXACT FOCK/POISSON THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014` and the Euler product in `Re(s)>1`  
RH status: **unproved**

## 1. One-particle radial source

Let `P*` be the prime powers.  On

\[
 (0,\infty)\times\mathcal P^*
\]

use the measure

\[
 d\mu(\tau,n)=2\Lambda(n)\,d\tau
\]

and put

\[
 \mathfrak h=L^2((0,\infty)\times\mathcal P^*,d\mu).
\]

For `a>0` and `Re(s)>1/2`, define

\[
 \boxed{
 v_{a,s}(\tau,n)=\mathbf1_{[0,a]}(\tau)n^{-s-\tau}.
 }
 \tag{L-91030.1}
\]

Then, for `Re(s),Re(t)>1/2`,

\[
\begin{aligned}
 \langle v_{a,s},v_{a,t}\rangle
 &=\sum_{n\in\mathcal P^*}
 2\Lambda(n)n^{-s-\bar t}
 \int_0^a n^{-2\tau}d\tau\\
 &=\sum_{n\in\mathcal P^*}
 \frac{\Lambda(n)}{\log n}(1-n^{-2a})n^{-s-\bar t}\\
 &=\boxed{\log Q_a(s+\bar t)},
\end{aligned}
 \tag{L-91030.2}
\]

where

\[
 Q_a(z)=\frac{\zeta(z)}{\zeta(z+2a)}.
\]

The last equality follows because for `n=p^r`,
`Lambda(n)/log(n)=1/r`.

## 2. Symmetric Fock realization

Let `Gamma_s(h)` be symmetric Fock space and

\[
 \operatorname{Exp}(v)=\bigoplus_{m\ge0}\frac{v^{\otimes m}}{\sqrt{m!}}.
\]

Since

\[
 \langle\operatorname{Exp}(v),\operatorname{Exp}(w)\rangle
 =e^{\langle v,w\rangle},
\]

(L-91030.2) gives

\[
 \boxed{
 \langle\operatorname{Exp}(v_{a,s}),
        \operatorname{Exp}(v_{a,t})\rangle
 =Q_a(s+\bar t).
 }
 \tag{L-91030.3}
\]

The coherent vectors of `L-91014` have the same Gram kernel.  Therefore their
closed span is canonically unitary to the closed Fock coherent span, with

\[
 k_{a,s}\longmapsto\operatorname{Exp}(v_{a,s}).
 \tag{L-91030.4}
\]

## 3. Exact radial product system

Decompose

\[
 [0,a+b]=[0,a]\sqcup[a,a+b].
\]

After translating the second interval by `a`,

\[
 \boxed{
 v_{a+b,s}=v_{a,s}\oplus S_av_{b,s+a}.
 }
 \tag{L-91030.5}
\]

The standard Fock factorization then gives

\[
 \boxed{
 \operatorname{Exp}(v_{a+b,s})
 =\operatorname{Exp}(v_{a,s})\otimes
  \operatorname{Exp}(v_{b,s+a}).
 }
 \tag{L-91030.6}
\]

Thus the divisor-splitting isometry and its pentagon law are ordinary interval
factorization and associativity in a bosonic product system.

## 4. Prime powers are independent radial births

The logarithm of the source is

\[
 \boxed{
 \log Q_a(z)=
 \sum_{n\in\mathcal P^*}
 \frac{\Lambda(n)}{\log n}(1-n^{-2a})n^{-z}.
 }
 \tag{L-91030.7}
\]

The identity

\[
 1-n^{-2a}
 =\int_0^a2\log(n)e^{-2\tau\log n}d\tau
\]

shows that the `n`-particle is born at an exponential radial time of rate
`2 log(n)`.  Distinct prime-power species are independent Fock particles.
The shift in the second cocycle factor records survival through the first
radial interval.

## 5. Compound-Poisson boundary multiplier

For `c>1`, put

\[
 M_{a,c}(\theta)=\frac{Q_a(c+i\theta)}{Q_a(c)}
\]

and

\[
 \nu_{a,c}=
 \sum_{n\in\mathcal P^*}
 \frac{\Lambda(n)}{\log n}(1-n^{-2a})n^{-c}
 \delta_{\log n}.
 \tag{L-91030.8}
\]

The measure is finite and positive, and (L-91030.7) gives

\[
 \boxed{
 M_{a,c}(\theta)=
 \exp\left\{
  \int(e^{-i\theta u}-1)d\nu_{a,c}(u)
 \right\}.
 }
 \tag{L-91030.9}
\]

Hence the boundary channel in `L-91020` and the compound-Poisson semigroup in
main's `L-91029` are the boundary representation of this same Fock product
system.

## 6. Finite source jets are finite Poisson chaos

A logarithmic source jet of order `d` lies in the first `d` orthogonal
polynomial/Poisson-chaos levels.  In particular:

```text
second jet: one returned state plus two details;
cubic jet:  one returned state plus three details.
```

This recovers the state counts of `L-91019` and `L-91025` without an ad hoc
matrix polarization.

## 7. Boundary

Closed here, subject to independent review:

```text
explicit prime-power one-particle space;
Jordan kernel = bosonic exponential-vector kernel;
exact radial Fock product system;
coassociative coefficient-one scale propagation;
prime powers as independent exponential radial births;
compound-Poisson boundary multiplier;
finite source jets as finite Poisson chaos.
```

Open:

```text
completed Poisson-Fock to Hardy/scattering isometry;
fixed-scale completed screw Gram positivity;
RH.
```
