# L-26204 — Endpoint-scale kernel and its exact Möbius weight state

Claim ID: `L-26204`  
Title: The parabolic endpoint atoms have a positive scale-invariant convolution kernel whose equality weight is a simple Möbius–Riesz state linked by a stable filter to the carry resolvent  
Status: **PROPOSED COMPLETE EXACT TRANSFORM THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue family: `#245/#262`  
Frozen base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
Dependencies: `L-26201`, `L-26202`; PR #252 `L-24501`  
Scope: continuum endpoint-scale convolution and exact transforms; no positivity of the inverse weight state

## 1. Continuum response of the parabolic seed

Retain

\[
 B(u)=2\sqrt u\left[
  \log\frac1u-2(1-\sqrt u)
 \right],
 \qquad
 g(u)=-B'(u)
 =\frac{\log u+4}{\sqrt u}-4.
\tag{L-26204.1}
\]

The continuum carry response of the full parabolic seed is

\[
 \boxed{
 F(\theta)=\sum_{1\le k\le1/\theta}g(k\theta),
 \qquad 0<\theta\le1.}
\tag{L-26204.2}
\]

On the reciprocal cell

\[
 \frac1{N+1}<\theta\le\frac1N,
\]

put

\[
 S_N=\sum_{k=1}^Nk^{-1/2},
 \qquad
 A_N=\sum_{k=1}^Nk^{-1/2}\log k.
\]

Then exactly

\[
 \boxed{
 F(\theta)
 =\theta^{-1/2}
 [A_N+S_N(\log\theta+4)]-4N.}
\tag{L-26204.3}
\]

The function is nonnegative because it is the scaling limit of the positive
carry-row response established in `L-26201`.

## 2. Endpoint derivative kernel

At endpoint fraction `s`, the seed response at final-scale column `theta` is

\[
 R_s(\theta)
 =s^{-1/2}F(\theta/s)
 \qquad(0<\theta<s\le1).
\tag{L-26204.4}
\]

Differentiate with respect to `s`:

\[
 \boxed{
 \partial_sR_s(\theta)
 =s^{-3/2}k(\theta/s),}
\tag{L-26204.5}
\]

where

\[
 \boxed{
 k(u)=-\frac12F(u)-uF'(u).}
\tag{L-26204.6}
\]

Using (L-26204.3), the cell formula collapses to

\[
 \boxed{
 k(u)=2N-\frac{S_N}{\sqrt u}
 \qquad
 \left(\frac1{N+1}<u\le\frac1N\right).}
\tag{L-26204.7}
\]

This is the continuum response kernel of one positive endpoint atom.

## 3. Positivity and normalization

The elementary integral bound

\[
 S_N\le1+\int_1^Nx^{-1/2}dx=2\sqrt N-1
\tag{L-26204.8}
\]

and

\[
 2\sqrt N-1<\frac{2N}{\sqrt{N+1}}
\tag{L-26204.9}
\]

imply, throughout the cell,

\[
 \frac{S_N}{\sqrt u}
 \le S_N\sqrt{N+1}<2N.
\]

Hence

\[
 \boxed{k(u)>0\qquad(0<u<1).}
\tag{L-26204.10}
\]

Moreover, `F(1)=0`, `uF(u)->0` as `u downarrow0`, and the parabolic objective
identity is

\[
 \int_0^1F(u)du=4.
\]

Integration by parts in (L-26204.6) gives

\[
 \boxed{
 \int_0^1k(u)du=2.}
\tag{L-26204.11}
\]

Thus `k(u)/2` is an explicit probability density on the endpoint ratio
`u=theta/s`.

## 4. Positive endpoint-scale convolution

Let `lambda(s)>=0` be a continuum endpoint weight.  Its column response is

\[
 \boxed{
 \mathcal R_\lambda(\theta)
 =\int_\theta^1
  \lambda(s)s^{-3/2}k(\theta/s)ds.}
\tag{L-26204.12}
\]

Put

\[
 \theta=e^{-t},
 \qquad
 L(t)=\lambda(e^{-t}),
\]

and define the positive causal kernel

\[
 \boxed{
 \varrho(v)=e^{-v/2}k(e^{-v}),
 \qquad v\ge0.}
\tag{L-26204.13}
\]

A change of variables gives

\[
 \boxed{
 e^{-t/2}\mathcal R_\lambda(e^{-t})
 =(L*\varrho)(t).}
\tag{L-26204.14}
\]

The critical target is

\[
 h(e^{-t})=e^{t/2}t.
\]

Therefore exact endpoint-scale saturation is the scalar Volterra equation

\[
 \boxed{(L*\varrho)(t)=t.}
\tag{L-26204.15}
\]

The finite endpoint-scale greedy of `L-26203` is a positive finite-horizon
minorant producer for this equation.

## 5. Mellin and Laplace symbols

For `Re(s)>1/2`, finite dilation switching gives

\[
 \int_0^1F(u)u^{s-1}du
 =\zeta(s)\int_0^1g(u)u^{s-1}du.
\tag{L-26204.16}
\]

The elementary integral is

\[
 \int_0^1g(u)u^{s-1}du
 =\frac{s-1}{s(s-\frac12)^2}.
\tag{L-26204.17}
\]

Hence

\[
 \boxed{
 \int_0^1F(u)u^{s-1}du
 =\zeta(s)\frac{s-1}{s(s-\frac12)^2}.}
\tag{L-26204.18}
\]

Put

\[
 f(t)=e^{-t/2}F(e^{-t}).
\]

Equation (L-26204.6) gives `f'=varrho`, with `f(0)=0`.  Therefore

\[
 \boxed{
 \widehat\varrho(z)
 =\zeta\left(z+\frac12\right)
  \frac{z-\frac12}{z(z+\frac12)}.}
\tag{L-26204.19}
\]

The value at `z=1/2` is removable and equals two, in agreement with
(L-26204.11) after critical weighting.

## 6. Exact equality weight

Taking Laplace transforms in (L-26204.15), the unique causal equality weight
has symbol

\[
 \boxed{
 \widehat L_*(z)
 =\frac{z+\frac12}
 {z(z-\frac12)\zeta(z+\frac12)}.}
\tag{L-26204.20}
\]

The rational factor is

\[
 \frac{z+\frac12}{z(z-\frac12)}
 =\frac2{z-\frac12}-\frac1z.
\tag{L-26204.21}
\]

Thus the physical equality state is the explicit finite Möbius sum

\[
 \boxed{
 L_*(t)
 =\sum_{n\le e^t}\frac{\mu(n)}{\sqrt n}
 \left[
  2e^{(t-\log n)/2}-1
 \right].}
\tag{L-26204.22}
\]

Every hypothetical off-line zeta zero remains an uncancelled pole of
(L-26204.20).  Positivity or boundary-tame approximation of `L_*` is therefore
an RH-bearing theorem, not a routine Volterra fact.

At the critical point,

\[
 \boxed{\widehat L_*(1/2)=2.}
\tag{L-26204.23}
\]

The endpoint entropy score is

\[
 2\int_0^\infty e^{-t/2}L(t)dt.
\]

Hence the equality state has the exact sharp score

\[
 2\widehat L_*(1/2)=4.
\]

## 7. Stable filter connection to the carry resolvent

Let `mathfrak g(t)` be the canonical carry-resolvent state of PR #252:

\[
 \mathfrak g(t)
 =\sum_{n\le e^t}\frac{\mu(n)}{\sqrt n}
 \left[
  8e^{(t-\log n)/2}
  -7-\frac32(t-\log n)
 \right].
\tag{L-26204.24}
\]

Its transform is

\[
 \widehat{\mathfrak g}(z)
 =\frac{(z+\frac12)(z+\frac32)}
 {z^2(z-\frac12)\zeta(z+\frac12)}.
\]

Comparing with (L-26204.20) gives

\[
 \boxed{
 \widehat{\mathfrak g}(z)
 =\frac{z+\frac32}{z}\widehat L_*(z).}
\tag{L-26204.25}
\]

Equivalently, pointwise in causal locally integrable functions,

\[
 \boxed{
 \mathfrak g(t)
 =L_*(t)+\frac32\int_0^tL_*(u)du.}
\tag{L-26204.26}
\]

Conversely,

\[
 \boxed{
 L_*(t)
 =\mathfrak g(t)
 -\frac32\int_0^t
  e^{-\frac32(t-u)}\mathfrak g(u)du.}
\tag{L-26204.27}
\]

Thus the endpoint-scale state and the carry-resolvent state are related by
mutually inverse stable first-order causal filters.  They expose the same
open-strip poles and differ only in the positive producer coordinate.

## 8. Consequence for the finite programme

The exact equality state `L_*` is simpler than the global carry state but still
RH-bearing.  The endpoint-scale proposal does **not** assume `L_*>=0`.
Instead it asks for finite nonnegative weights whose convolution stays below the
target and loses only subpower critical mass.

This is precisely `ESGS`.  In transform language:

```text
exact global equality weight      L_*          reciprocal-zeta / signed;
finite endpoint-scale greedy      L_(X)^+      nonnegative / leaves slack;
closing theorem                   critical mass lost = X^o(1).
```

The stable filter (L-26204.26)--(L-26204.27) gives an exact bridge to DCRS and
FGCM without identifying their finite positive producers term by term.

## 9. Proof boundary

Established here, subject to review:

1. the positive scale-invariant endpoint response kernel;
2. its probability normalization;
3. the endpoint-scale Volterra equation;
4. its exact zeta symbol and equality state;
5. the critical mass two / entropy mass four;
6. the stable causal equivalence with the canonical carry resolvent.

Open:

- positivity of the exact equality state;
- a finite positive endpoint minorant with subpower critical-mass loss;
- `ESBT/ESGS`;
- RH.
