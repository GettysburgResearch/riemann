# Prime-only continuation of the global Hardy-energy attack

Agent: `gpt56-pro-17`  
Date: 2026-08-07  
Issue: #215  
PR: #216

## Result

The initial `10^7` prime-power reconnaissance showed a cancellation above
`99.99%` between the diagonal and off-diagonal Gram contributions. A layer
replay reveals that most of the first cancellation is not mysterious:
ordinary primes and prime squares carry two order-one signals with opposite
cross term.

Möbius inversion explains this exactly. If

\[
 P_1(s)=\sum_p\log p\,p^{-s},
 \qquad
 D(s)=-\zeta'(s)/\zeta(s),
\]

then

\[
 P_1(s)=\sum_{r\ge1}\mu(r)D(rs).
\]

At `s=1/2+z`, the `r=2` term creates one boundary pole at `z=0`. The square
layer in the full von Mangoldt series cancels the same channel.

`T-21502` adds one exact boundary difference

\[
 H(u)=G(u)-G(u-1)
\]

and proves that the ordinary-prime-only signal

\[
 Q_H^{\mathbb P}(x)
 =\sum_p{\log p\over\sqrt p}H(x-\log p)
\]

has cumulative-energy exponent exactly

\[
 \Theta_\zeta=\sup_\rho(\Re\rho-1/2).
\]

Therefore

\[
 \mathrm{RH}
 \iff
 \int^X|Q_H^{\mathbb P}(x)|^2dx=\exp(o(X)).
\]

Every prime power of exponent at least two has been removed from the global
criterion.

## Exact semiprime collapse

`L-21504` rewrites the complete off-diagonal ordinary-prime Gram as one linear
sum over balanced squarefree semiprimes:

\[
 \mathcal O_H^{\mathbb P}(X)
 =\sum_{n=pq,\,p<q}
 {\Lambda_2(n)\over\sqrt n}
 K_X^H(\log p,\log q),
\]

where

\[
 \Lambda_2(pq)=2\log p\log q.
\]

The fixed compact support forces `p/q` into one bounded interval. The final
arithmetic theorem is therefore a balanced Type-II semiprime estimate, not an
all-prime-power matrix limit.

## Empirical calibration

At block `j=16`, the complete pushed prime-power signal decomposes roughly as

```text
prime energy                  +0.29916866
square energy                 +0.23823574
twice prime/square cross      -0.53258697
all remaining terms           -0.00325795
final energy                  +0.00156048
```

For the new prime-only boundary-difference signal, the block energies decrease
to the `0.003`--`0.005` scale over the retained final blocks even while the
diagonal grows to about `89`. This remains long-double reconnaissance only.

## Attempted closure and why it stops

Three direct closure mechanisms were tested conceptually:

1. **entrywise semiprime upper bounds:** exponentially too large because they
   destroy the signed cubic kernel;
2. **classical PNT/zero-free-region error:** leaves an `exp(X/2-o(X))`
   envelope after the square-root normalization;
3. **standard short-interval mean squares:** a bound at the strength needed here
   is itself equivalent to excluding off-critical zero modes.

The semiprime rewrite is valuable because it exposes the exact arithmetic
interface for dispersion or a nonlinear Selberg identity. It does not make the
remaining estimate automatic.

## SERIOUS RESOLUTION PATH

The sharpened path is

```text
ordinary primes only
-> one fixed boundary-safe compact window
-> prime Hardy exponent = rightmost zero
-> exact balanced squarefree-semiprime forcing
-> subexponential signed Type-II estimate
-> RH.
```

The first four arrows are now explicit. The smallest exact blocker is

\[
 \boxed{
 [\mathcal O_H^{\mathbb P}(X)]_+=\exp(o(X)).}
\]

for the single fixed piecewise-polynomial balanced kernel of `L-21504`.

No proof of this final estimate, and hence no proof of RH, is claimed.
