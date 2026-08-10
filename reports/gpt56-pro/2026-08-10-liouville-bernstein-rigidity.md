# Liouville–Bernstein rigidity beyond the Multiplicative Bootstrap

Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
Base: PR #351 head `22a94f431d7f4cd87db5f3efdd97b086f8f60183`  
Status: two exact theorem packets, finite hostile replay, revised frontier; **RH remains unproved**

## Executive result

Claude's fifth dispatch found, by exhaustive WHT minimization, that the
Liouville point appears to minimize both the transported prime ramp and every
tested GFEP exit over the full completely multiplicative sign class.

The two appearances have different exact explanations.

1. **Ramp:** Liouville is pointwise minimal before summation. For every real
   prime assignment `x_p in [-1,1]`, the generalized coefficient
   `((mu^2 f_x)*log)(n)` has a manifestly nonnegative Bernstein formula and is
   at least `Lambda(n)`. Therefore the ramp lambda-extremality conjecture is a
   theorem for all endpoints and every nonnegative test weight.
2. **GFEP:** the complete Boolean polynomial around Liouville has an exact
   descendant hierarchy. Every nonempty mixed coefficient is a positive linear
   combination of the same GFEP exit at endpoints `X/q`, `q>=2`. Thus
   lambda-extremality is hereditary from proper-descendant GFEP; at a first
   counterexample it is automatic. The only coefficient not reduced is the
   empty coefficient, namely the current Mobius value.

This changes the campaign map. The exponential class cube is not the remaining
obstruction. The open arithmetic is one constant term in a polynomial whose
entire nonempty coefficient hierarchy is already classified.

## I. Exact pointwise ramp theorem

For prime parameters `x_p in [-1,1]`, define on squarefree divisors

\[
 f_x(d)=\prod_{p\mid d}x_p,
 \qquad b_x(d)=\mu^2(d)f_x(d),
\]

and

\[
 \Lambda_x(n)=(b_x*\log)(n).
\]

Writing `y_p=(1+x_p)/2`, `r=omega(n)`, exact divisor algebra gives

\[
 \Lambda_x(n)
 =2^{r-1}\sum_{q\mid\operatorname{rad}(n)}
   (\log q)\prod_{p\mid n,\ p\ne q}y_p
 +2^r\log\frac{n}{\operatorname{rad}(n)}\prod_{p\mid n}y_p.
\]

The first sum is over prime `q`. Every term is nonnegative. At the all-minus
point, it reduces exactly to the ordinary von Mangoldt function. Hence

\[
 \Lambda_x(n)\ge\Lambda(n)
\]

pointwise.

For the transported ramp of `T-90008`, divisor switching yields

\[
 \operatorname{Ramp}_x(X)
 =\sum_{q\le X}w_X(q)\Lambda_x(q),
\]

so

\[
 \operatorname{Ramp}_x(X)\ge\operatorname{Ramp}_\lambda(X)
\]

for every endpoint. No WHT, Halasz theorem, asymptotic Euler product, or
finite-range hypothesis enters.

### Exact rigidity

At `n=2p`, every prime changed away from Liouville pays at least

\[
 2\log2\,w_X(2p).
\]

Thus

\[
 \operatorname{Ramp}_x(X)-\operatorname{Ramp}_\lambda(X)
 \ge2\log2\sum_{p<X/2}\frac{1+x_p}{2}w_X(2p).
\]

Equality holds exactly when all active primes `p<X/2` remain at `-1`.

### Consequence for Stage 2

The class statement is now exactly free:

\[
 \text{Form A over H}\iff\text{Form A at lambda}.
\]

The Final Deficit Theorem may still fence generic distance technology at the
lambda slice, but class uniformity is no longer a separate analytic demand.

## II. Complete Boolean hierarchy for GFEP

For any finite coefficient sequence `c(k)`, define

\[
 F_c(x)=\sum_{k\le K}\mu^2(k)f_x(k)c(k).
\]

Expanding at `x_p=-1`, with `y_p=(1+x_p)/2`, gives

\[
 F_c(x)=\sum_{a\le K\atop a\ {\rm sf}}B_c(a)y_a,
\]

where

\[
 B_c(a)=2^{\omega(a)}
 \sum_{m\le K/a\atop(m,a)=1}\mu(m)c(am).
\]

The empty coefficient is the Liouville value `B_c(1)`.

Now let

\[
 P_c(q)=\sum_d\mu(d)c(qd),
 \qquad
 \mathcal S(a)=\{r:\operatorname{rad}(r)\mid a\}.
\]

The coefficient identity

\[
 \mu(m)1_{(m,a)=1}=(\mu*1_{\mathcal S(a)})(m)
\]

gives

\[
 \frac{B_c(a)}{2^{\omega(a)}}
 =\sum_{r\in\mathcal S(a)}P_c(ar).
\]

For a GFEP exit coefficient, endpoint scaling identifies

\[
 P_c(q)=q^{-1/2}\Sigma_{X/q,n}(p).
\]

Therefore

\[
 B_{X,n,p}(a)
 =2^{\omega(a)}
 \sum_{r\in\mathcal S(a)}
 (ar)^{-1/2}\Sigma_{X/(ar),n}(p).
\]

Every nonempty coefficient is a proper-descendant sum.

### First-counterexample theorem

If all proper descendant values are nonnegative, all nonempty Bernstein
coefficients are nonnegative. The Liouville point is then the global class
minimum on the entire real prime cube, even if the current empty coefficient
were negative.

Thus:

```text
multiplicative adversary before the truth fails     impossible;
first truth failure with lambda still minimizing    structurally allowed.
```

Claude's Stage-1 surprise is explained. The WHT calculation was detecting a
hereditary theorem.

### Sparse producer

The same identity survives every nonnegative exit trace. For the actual
three-site-or-less hitting trace,

\[
 nA_X(n)=\sum_p h_n(p)\Sigma_{X,n}(p),
\]

every nonempty class derivative is a positive sum of smaller producer
coefficients. The preferred exact-flow target remains the sparse empty
coefficient, not coordinatewise GFEP.

## III. Empty-coefficient renewal

Multiples Möbius inversion gives

\[
 c_p^{X,n}(1)
 =\sum_{q\le X/n}q^{-1/2}\Sigma_{X/q,n}(p),
\]

or

\[
 \Sigma_{X,n}(p)
 =c_p^{X,n}(1)
 -\sum_{q\ge2}q^{-1/2}\Sigma_{X/q,n}(p).
\]

This is the exact current frontier. The forcing is a positive transport packet;
every delay is a smaller endpoint; the delay mass is noncontractive.

Setting every Bernstein variable to the same `t` gives the sprinkled renewal

\[
 F_X(2t-1)
 =\Sigma_X+
 \sum_{q\ge2}(2t)^{\omega(q)}q^{-1/2}\Sigma_{X/q}.
\]

This is an unfenced exact coordinate, but no lower estimate surviving the
subtraction is presently proved.

## IV. Verification

`X-90201` retains five assurance layers.

```text
local generalized-Lambda cases        3,546
exact Boolean class vertices           1,024
exact primitive/semigroup checks           19
actual scaled descendants                 109
actual mixed derivatives                   70
small actual exhaustive minima              4
ramp class vertices                      1,088
```

Large finite reconnaissance at depths `100,120,266,500` finds no negative
nonempty Bernstein coefficient. The minimum coefficients are respectively

```text
0.0276616, 0.0153423, 0.00475530, 0.000801603.
```

The high-precision identity errors are below `2e-70`.

## V. Revised route map

### Closed

- positive-kernel conjecture for the transported packet: PR #355;
- one-scalar lambda-extremality: `L-90201`;
- all mixed class derivatives: `T-90201`;
- exact reason multiplicative adversaries disappear;
- exponential WHT search replaced by a linear descendant DAG.

### Still open

- the empty GFEP coefficient;
- the sparse producer empty coefficient;
- a contractive or bijective solution of the empty-coefficient renewal;
- Form A at lambda;
- RH.

### Correct strategic statement

The multiplicative bootstrap did not leave a free class adversary, but neither
did it leave a mysterious global minimizer conjecture. It left one exact
constant-term problem:

> Prove the empty coefficient of a hereditary Boolean polynomial whose every
> nonempty coefficient is a positive combination of proper descendants.

That formulation is narrower than Claude's final class statement and preserves
the only place where new exact combinatorics can still enter.
