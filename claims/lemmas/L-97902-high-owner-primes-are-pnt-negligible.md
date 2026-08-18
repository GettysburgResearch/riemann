# L-97902 — Owner primes above `X^{o(1)}` are negligible by finite top completion and PNT

Claim ID: `L-97902`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-97900`--`L-97901`; the native coefficient formula; classical Vinogradov--Korobov PNT  
RH status: **not assumed**

Let `U_full(Y)` be the normalized native annular `5:3` scalar at endpoint
`Y`. For a finite set `A` of rough primes, let `U^(hat A)` be the same full
state with exactly the Euler factors in `A` omitted, as in `L-97901`.

Define

\[
 \mathcal E(Y)=
 \exp\!\left[-c(\log Y)^{3/5}(\log\log Y)^{-1/5}\right]
 \qquad(Y\ge Y_0),
 \tag{L-97902.1}
\]

for a suitable absolute `c>0`.

## 1. Full-state PNT bound

One has

\[
 \boxed{
 |U_{\rm full}(Y)|
 \ll Y^{-1/4}+\mathcal E(\sqrt Y).
 }
 \tag{L-97902.2}
\]

In particular `U_full(Y)` tends to zero faster than every negative power of
`log Y`. There is also the global crude bound

\[
 |U_{\rm full}(Y)|\ll1.
 \tag{L-97902.3}
\]

### Proof

The native coefficient dictionary is a fixed linear combination of

\[
 \mu(n),\qquad \mathbf1_{2\mid n}\mu(n/2),
 \qquad \mathbf1_{4\mid n}\mu(n/4),
\]

against the bounded factor-four logarithmic hinge. It is therefore enough to
bound

\[
 Y^{-1/2}\sum_{n\le Y}\frac{\mu(n)}{\sqrt n}
 \min(\log4,\log(Y/n))_+.
 \tag{L-97902.4}
\]

On `n<=sqrt(Y)`, absolute summation gives `O(Y^(-1/4))`. On the
remaining interval, partial summation with

\[
 M(t)=\sum_{n\le t}\mu(n)
 \ll t\mathcal E(t)
\]

and the derivative bound `O(t^(-3/2))` for the hinge weight gives
`O(mathcal E(sqrt(Y)))`. The fixed shifts by two and four obey the same
estimate. The unsigned calculation gives (L-97902.3).

## 2. Omitted-factor stability

The omitted factors have the exact finite inverse expansion

\[
 \boxed{
 U^{\widehat A}
 =\prod_{q\in A}(I-q^{-1}\mathsf T_q)^{-1}U_{\rm full}
 =\prod_{q\in A}\left(\sum_{j\ge0}q^{-j}\mathsf T_q^j\right)
 U_{\rm full}.
 }
 \tag{L-97902.5}
\]

The sums terminate at each endpoint. Suppose

\[
 |A|\le K+1,
 \qquad
 \min A\ge H,
 \qquad
 K/H\longrightarrow0.
\]

For `Y>=L`, (L-97902.2)--(L-97902.5) give

\[
 \boxed{
 |U^{\widehat A}(Y)|
 \ll L^{-1/4}+\mathcal E(\sqrt L)+K/H.
 }
 \tag{L-97902.6}
\]

Indeed the zero multi-index is bounded by (L-97902.2), while the total
coefficient of all nonzero multi-indices is

\[
 \prod_{q\in A}(1-q^{-1})^{-1}-1
 \ll K/H.
\]

For arbitrary `Y`, the same argument and (L-97902.3) give the uniform bound
`U^(hat A)(Y)=O(1)`.

## 3. High-owner budget

Use the growing parameters

\[
 K=K_X=\lfloor(\log\log X)^{1/4}\rfloor,
 \qquad
 H=H_X=X^{1/(K+2)},
 \qquad
 L=(\log X)^{20}.
 \tag{L-97902.7}
\]

After the complete logarithmic cube of `L-97900`, define

\[
 \mathfrak H_X=
 \sum_{H\le p\le X/2}\frac1pU_{P_X,<p}(X/p).
 \tag{L-97902.8}
\]

Then, for every fixed `A>0`,

\[
 \boxed{
 |\mathfrak H_X|\ll_A(\log\log X)^{-A}.
 }
 \tag{L-97902.9}
\]

### Proof

Insert the exact top-history expansion (L-97901.4). Every active term is
indexed by a nonempty squarefree set of primes at least `H`; its smallest prime
is the owner. By (L-97901.7), the omitted set has at most `K+1` primes. The
total reciprocal coefficient mass is bounded by

\[
 \prod_{H\le q\le X}(1+q^{-1})-1
 \ll\frac{\log X}{\log H}\asymp K.
 \tag{L-97902.10}
\]

For terms whose terminal endpoint `X/q_S` is at least `L`, use
(L-97902.6). Their total is

\[
 \ll K\{L^{-1/4}+\mathcal E(\sqrt L)+K/H\}.
 \tag{L-97902.11}
\]

For the activation-boundary terms `X/L<q_S<=X/2`, choose the largest prime
last. Conditional on the preceding product, that prime lies in a multiplicative
interval of ratio at most `L` and is at least `H`. The standard reciprocal-prime
interval estimate gives mass

\[
 \ll\frac{\log L}{\log H}.
\]

Summing the preceding products with (L-97902.10), the complete boundary mass is

\[
 \ll K\frac{\log L}{\log H}
 \ll\frac{K^2\log L}{\log X}.
 \tag{L-97902.12}
\]

The omitted states are uniformly bounded there. Equations
(L-97902.11)--(L-97902.12), with (L-97902.7), decay faster than every fixed
negative power of `log log X`, proving (L-97902.9).

## Interpretation

No fixed-power owner range is conclusion-producing. The top-history identity
turns every owner `p>=X^{1/(K_X+2)}=X^{o(1)}` into a bounded collection of
fully completed states. Classical PNT cancellation then pays the entire range,
including all activation-boundary terms.