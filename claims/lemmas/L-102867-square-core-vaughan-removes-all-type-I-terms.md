# L-102867 — Square-core Vaughan decomposition removes every Type-I lattice term

Claim ID: `L-102867`  
Status: **PROVED EXACT DECOMPOSITION AND TYPE-I ESTIMATE**  
Created: 2026-08-24  
Depends on: `L-102866`; PR #685 `L-100311`  
RH status: **not assumed**

Fix a semiprime squareclass `Q` and put

\[
Y=\frac XQ.
\]

The carrier-recombined completed core in the fixed outer observation is

\[
\boxed{
\mathcal C_Q(Y)
=\sum_{a\ge1}\frac{\mu(a)}a
R_L\!\left(\frac Y{a^2}\right).
}
\tag{L-102867.1}

The support of `R_L` forces

\[
\sqrt{Y/8}\le a\le\sqrt Y.
\]

Let

\[
U=\lfloor Y^{1/6}\rfloor,
\qquad
\mu_U(n)=\mu(n)\mathbf1_{n\le U},
\qquad
a_U=\varepsilon-\mu_U*\mathbf1.
\]

The exact Vaughan identity is

\[
\boxed{
\mu
=2\mu_U-\mu_U*\mu_U*\mathbf1+a_U*a_U*\mu.
}
\tag{L-102867.2}

Moreover,

\[
a_U(n)=0\qquad(1\le n\le U).
\]

For all sufficiently large `Y`, the support interval in (L-102867.1) lies
above `U`; the finitely many remaining `Y` are a fixed terminal packet.
Therefore the first term in (L-102867.2) vanishes and

\[
\boxed{
\mathcal C_Q(Y)
=\mathcal T_Q(Y)+\mathcal B_Q(Y),
}
\tag{L-102867.3}

where

\[
\mathcal T_Q(Y)
=-\sum_{d,e\le U}\frac{\mu(d)\mu(e)}{de}
\sum_{m\ge1}\frac1m
R_L\!\left(\frac{Y}{d^2e^2m^2}\right),
\tag{L-102867.4}

and

\[
\boxed{
\mathcal B_Q(Y)
=\sum_{\substack{r,s>U\\m\ge1}}
\frac{a_U(r)a_U(s)\mu(m)}{rsm}
R_L\!\left(\frac{Y}{r^2s^2m^2}\right).
}
\tag{L-102867.5}

## 1. Type-I decay

Apply `L-102866` with

\[
Z=Y/(de)^2.
\]

Then

\[
\left|
\sum_{m\ge1}\frac1m
R_L\!\left(\frac{Y}{d^2e^2m^2}\right)
\right|
\le C_R\frac{de}{\sqrt Y}.
\]

The factors `de` cancel those in (L-102867.4), giving

\[
|\mathcal T_Q(Y)|
\le C_R\frac{U^2}{\sqrt Y}.
\]

With `U=Y^(1/6)`,

\[
\boxed{
\mathcal T_Q(Y)=O_R(Y^{-1/6}).
}
\tag{L-102867.6}

This error has finite logarithmic integral and remains so after every fixed
owner, phase, gauge and one-octave partition.

## 2. Exact balanced ranges

The support in (L-102867.5) gives

\[
\sqrt{Y/8}\le rsm\le\sqrt Y.
\]

Since `r,s>U`,

\[
\boxed{
m\le\frac{\sqrt Y}{U^2}\ll Y^{1/6}.}
\tag{L-102867.7}

Thus the sole surviving core packet has

```text
r,s > Y^(1/6),
m   <= Y^(1/6),
r s m asymp sqrt(Y).
```

All classical complete-lattice and Type-I pieces have been removed before any
additive phase or coherent squareclass sum is introduced.

## 3. Owner separation inherited from largest-two gauge

In the clean semiprime-squareclass sector

\[
N=pq\,a^2,
\qquad p>q>P^+(a),
\]

one has `q>P^+(rsm)`. Hence every owner prime is coprime to every balanced
Vaughan variable and

\[
\boxed{q>Y^{1/6}.}
\tag{L-102867.8}

The phase moduli used in `L-102860--L-102865` therefore remain genuinely
external to the balanced core variables.

## Scope

The theorem closes the entire Type-I side of the coherent squareclass problem.
It does not bound the signed balanced packet (L-102867.5). That packet is the
literal arithmetic input of `T-102880`.
