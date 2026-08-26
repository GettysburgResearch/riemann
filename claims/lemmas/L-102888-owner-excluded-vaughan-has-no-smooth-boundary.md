# L-102888 — The owner-excluded Vaughan decomposition has no smooth-boundary row

Claim ID: `L-102888`  
Status: **PROVED EXACT SOURCE DECOMPOSITION AND TYPE-I CLOSURE**  
Created: 2026-08-24  
Depends on: `L-102880`; `L-102886--L-102887`  
RH status: **not assumed**

Fix the two distinct owner primes `p,q` supplied by the horizon-safe pair gauge and put

\[
\mathbb N^{(p,q)}=\{n:(n,pq)=1\}.
\]

Let `1^(p,q)` and `mu^(p,q)` be the identity and Möbius functions on this finite-Euler monoid.  On one dyadic block use the fixed cutoff `U_j` of `L-102886`, and define

\[
\mu_U^{(p,q)}=\mu^{(p,q)}\mathbf1_{n\le U_j},
\qquad
a_U^{(p,q)}=\varepsilon-\mu_U^{(p,q)}*1^{(p,q)}.
\]

The exact Vaughan identity is

\[
\boxed{
\mu^{(p,q)}
=2\mu_U^{(p,q)}
-\mu_U^{(p,q)}*\mu_U^{(p,q)}*1^{(p,q)}
+a_U^{(p,q)}*a_U^{(p,q)}*\mu^{(p,q)}.
}
\tag{L-102888.1}

No moving largest-prime threshold occurs.

## 1. Derivative-core decomposition

Define

\[
\mathcal C^K_{p,q}(Y)
=\sum_{(a,pq)=1}{\mu(a)\over a}K_L(Y/a^2).
\]

Then, outside the fixed terminal range,

\[
\boxed{
\mathcal C^K_{p,q}
=\mathcal T^{K,(p,q)}_U
+\mathcal B^{K,(p,q)}_U.
}
\tag{L-102888.2}

where

\[
\mathcal T^{K,(p,q)}_U(Y)
=-\sum_{d,e\le U_j}
{\mu^{(p,q)}(d)\mu^{(p,q)}(e)\over de}
\sum_{(m,pq)=1}{1\over m}
K_L\!\left({Y\over d^2e^2m^2}\right),
\tag{L-102888.3}

and

\[
\boxed{
\mathcal B^{K,(p,q)}_U(Y)
=\sum_{\substack{r,s>U_j\\(rsm,pq)=1}}
{a_U^{(p,q)}(r)a_U^{(p,q)}(s)\mu(m)\over rsm}
K_L\!\left({Y\over r^2s^2m^2}\right).
}
\tag{L-102888.4}

As before,

\[
r,s\gg Y^{1/6},
\qquad m\ll Y^{1/6},
\qquad rsm\asymp\sqrt Y.
\]

## 2. Uniform owner-excluded lattice bound

Let

\[
\mathscr L_K(Z)=\sum_{m\ge1}{1\over m}K_L(Z/m^2).
\]

Inclusion--exclusion of the two owner primes gives the exact operator identity

\[
\boxed{
\mathscr L_K^{(p,q)}
=(I-p^{-1}S_{p^2})(I-q^{-1}S_{q^2})\mathscr L_K.
}
\tag{L-102888.5}

where

\[
\mathscr L_K^{(p,q)}(Z)
=\sum_{(m,pq)=1}{1\over m}K_L(Z/m^2).
\]

By `L-102880`, `mathscr L_K(Z)=O_K(Z^(-1/2))`.  Moreover

\[
p^{-1}\mathscr L_K(Z/p^2)=O_K(Z^{-1/2}),
\]

and similarly for `q` and `pq`.  Hence, uniformly in both owners,

\[
\boxed{
\mathscr L_K^{(p,q)}(Z)=O_K(Z^{-1/2}).
}
\tag{L-102888.6}

Consequently

\[
\boxed{
\mathcal T^{K,(p,q)}_U(Y)=O_K(Y^{-1/6}).
}
\tag{L-102888.7}

uniformly throughout the dyadic block.

## 3. Exact consequence

The smooth-boundary row `KSCB102881` is an artifact of the largest-two coordinate.  In the horizon-safe pair gauge it is absent.  Owner exclusion costs only the two fixed squared-shift factors in (L-102888.5), already inside the polylogarithmic completion ledger.

The only retained arithmetic row is

```text
HBCQDSP102888:
  subpower logarithmic negative mass of the carrier-recombined coherent
  balanced current in (L-102888.4), after exact owner phases and physical
  distinct-product restriction.
```

Together with the power-small Type-I row, `HBCQDSP102888` implies the derivative detector criterion and hence RH.

```text
horizon-safe pair source                 PROVED EXACT
owner-excluded Vaughan                   PROVED EXACT
owner-excluded Type-I                    PROVED POWER-SMALL
smooth-boundary current                  ABSENT IN THIS GAUGE
balanced physical current                OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```
