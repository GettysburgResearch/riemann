# L-97904 — Owner primes above `exp((log log X)^4)` are negligible

Claim ID: `L-97904`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-97901`--`L-97902`; the classical upper-bound sieve; Vinogradov--Korobov PNT  
RH status: **not assumed**

Put

\[
 \ell=\log\log X,
 \qquad
 H_X=\exp(\ell^4),
 \qquad
 K_X=\left\lfloor\frac{\log X}{\log H_X}\right\rfloor,
 \tag{L-97904.1}
\]

and

\[
 L_X=\exp(\ell^2).
 \tag{L-97904.2}
\]

Start from any complete lower-prime cube `U_Z` with `Z<H_X`. Let
`U_(Z,<p)` be the exact state immediately before adjoining owner prime `p`, and
define

\[
 \mathfrak H_Z(X)=
 \sum_{H_X\le p\le X/2}\frac1pU_{Z,<p}(X/p).
 \tag{L-97904.3}
\]

Then

\[
 \boxed{
 |\mathfrak H_Z(X)|\ll\ell^{-2}.
 }
 \tag{L-97904.4}
\]

The implied constant is uniform for the lower cube used in `L-97903`.
Since that cube has size `asymp 1/ell`, the complete high-owner range is lower
order.

## 1. Exact conversion to rough products

Apply the top-history completion of `L-97901`. The pair consisting of the owner
`p` and its selected top set `S` is one squarefree integer

\[
 n=p\prod_{q\in S}q
 \tag{L-97904.5}
\]

whose least prime is the owner. Every squarefree `H_X`-rough integer
`2<=n<=X/2` occurs exactly once. The corresponding term is

\[
 \frac1nU^{\widehat A}(X/n),
 \tag{L-97904.6}
\]

where `A` is the set of prime factors of `n`. Since every factor is at least
`H_X`, one has

\[
 |A|\le K_X.
 \tag{L-97904.7}
\]

Therefore

\[
 \boxed{
 \mathfrak H_Z(X)=
 \sum_{2\le n\le X/2\atop P^-(n)\ge H_X}
 \frac{\mu^2(n)}nU^{\widehat{\operatorname{rad}(n)}}(X/n).
 }
 \tag{L-97904.8}
\]

This is an exact source partition, not an upper-bound sieve identity.

## 2. Interior endpoints

For `n<=X/L_X`, the terminal endpoint `Y=X/n` is at least `L_X`.
The omitted-state estimate of `L-97902` gives

\[
 |U^{\widehat A}(Y)|
 \ll L_X^{-1/4}+\mathcal E(\sqrt{L_X})+K_X/H_X.
 \tag{L-97904.9}
\]

The complete reciprocal mass is

\[
 \sum_{P^-(n)\ge H_X\atop n\le X}\frac{\mu^2(n)}n
 \le\prod_{H_X\le q\le X}(1+q^{-1})
 \ll\frac{\log X}{\log H_X}\ll K_X.
 \tag{L-97904.10}
\]

Now

\[
 \log K_X=\ell+O(\log\ell),
 \qquad
 \log L_X=\ell^2,
 \qquad
 \log H_X=\ell^4.
\]

The Vinogradov--Korobov exponent at `sqrt(L_X)` is
`gg ell^(6/5)/(log ell)^(1/5)`, so multiplication by `K_X` still tends to zero
faster than every fixed negative power of `ell`. Likewise

\[
 K_XL_X^{-1/4}=o(\ell^{-A}),
 \qquad
 K_X^2/H_X=o(\ell^{-A})
 \tag{L-97904.11}
\]

for every fixed `A`. Thus the interior part of (L-97904.8) is
`o(ell^(-A))`.

## 3. Activation boundary

For `X/L_X<n<=X/2`, use the uniform bound
`U^(hat A)(X/n)=O(1)` from `L-97902`.
The classical upper-bound sieve gives, uniformly for
`H_X=X^o(1)`,

\[
 \#\{m\le t:P^-(m)\ge H_X\}
 \ll\frac{t}{\log H_X}.
 \tag{L-97904.12}
\]

Partial summation on the interval `(X/L_X,X/2]` yields

\[
 \sum_{X/L_X<n\le X/2\atop P^-(n)\ge H_X}
 \frac{\mu^2(n)}n
 \ll\frac{1+\log L_X}{\log H_X}
 \ll\ell^{-2}.
 \tag{L-97904.13}
\]

Combining the interior and boundary estimates proves (L-97904.4).

## Consequence

Every fixed-power prime range, and much more, is now removed. The only possible
conclusion-producing owner primes lie below

\[
 \exp((\log\log X)^4),
\]

a quasipolylogarithmic scale. The exact lower edge is sharpened separately by
`L-97903`.