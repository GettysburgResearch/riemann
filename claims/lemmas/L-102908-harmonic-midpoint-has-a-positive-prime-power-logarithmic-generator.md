# L-102908 — The harmonic midpoint has a positive prime-power logarithmic generator

Claim ID: `L-102908`  
Status: **PROVED EXACT POSITIVE-GENERATOR THEOREM**  
Created: 2026-08-25  
Depends on: `L-102906--L-102907`  
RH status: **not assumed**

The local harmonic factor is

\[
M(x)
=1-{x\over2}-{x^2\over2}
=(1-x)(1+x/2).
\]

Its logarithmic Euler generator is

\[
\begin{aligned}
\mathfrak L_M(x)
&=-x{M'(x)\over M(x)}\\
&={x\over1-x}-{x\over2+x}.
\end{aligned}
\]

Expanding both geometric series gives

\[
\boxed{
\mathfrak L_M(x)
=
\sum_{k\ge1}
\left(
1-{(-1)^{k-1}\over2^k}
\right)x^k.
}
\tag{L-102908.1}
\]

Every coefficient is strictly positive. More precisely,

\[
{1\over2}
\le
1-{(-1)^{k-1}\over2^k}
\le
{5\over4}.
\tag{L-102908.2}
\]

For the arithmetic midpoint square, the generator is twice (L-102908.1). Its critical prime coefficient is exactly one:

\[
\boxed{
-\,x{d\over dx}\log M(x)^2
=x+{5\over2}x^2+{7\over4}x^3+\cdots.
}
\tag{L-102908.3}
\]

## 1. Arithmetic meaning

Restoring one logarithmic weight for each labelled prime gives the positive prime-power current

\[
\boxed{
\mathscr L_{\rm harm}(z)
=
2\sum_{p,k\ge1}
\left(
1-{(-1)^{k-1}\over2^k}
\right)
{\log p\over p^{kz}}.
}
\tag{L-102908.4}
\]

The `k=1` part is the native critical prime current. The sum over `k>=2` has polylogarithmic half-order operator mass on every finite horizon.

Thus the Hodge-normalized obstruction has a positive logarithmic intensity. Its sign difficulty does not come from a signed generator; it comes exclusively from transporting that positive intensity through the fixed signed physical observation.

## 2. Exact relation to the temperature connection

The prime coefficient in (L-102908.3) agrees with the invariant of `L-102907` and with the positive-inverse temperature tangent of `L-102900`. Hence

```text
harmonic Hodge charge;
completion-temperature tangent;
stopped prime owner current
```

are the same first-order arithmetic generator.

## Scope

Positivity of the Dirichlet logarithmic generator does not imply positivity of the arithmetic source coefficients or of the fixed outer observation. Exponentiating a positive prime-power intensity reintroduces alternating inclusion-exclusion chaoses. The theorem supplies a canonical positive driving measure, not the missing one-sided physical orientation.
