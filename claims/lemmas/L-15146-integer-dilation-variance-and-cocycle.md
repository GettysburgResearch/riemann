# L-15146 — Integer dilation variance and multiplicative cocycle

Claim ID: `L-15146`  
Title: At every integer scale the Chebyshev dilation energy is an exact discrete weighted variance with a multiplicative cocycle law  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15145`; elementary properties of the step function `psi`  
Scope: exact arithmetic production form and recursive proof interface

## 1. Exact discrete energy

Fix an integer

\[
 a\ge2
\]

and an integer endpoint `N>=3`. On every open unit cell `m<t<m+1`,

\[
 \psi(t)=\psi(m)
\]

and, because `1/a<1`,

\[
 \psi(t/a)=\psi(\lfloor m/a\rfloor).
\]

The endpoint values have measure zero. Therefore (L-15145.11) gives the exact
finite sum

\[
 \boxed{
 \mathcal E_a(N)
 =\sum_{m=2}^{N-1}
 {\left[
   \psi(m)-a\psi(\lfloor m/a\rfloor)
  \right]^2
  \over m(m+1)}.}
 \tag{L-15146.1}
\]

Indeed,

\[
 \int_m^{m+1}{dt\over t^2}
 ={1\over m}-{1\over m+1}
 ={1\over m(m+1)}.
\]

Thus the global energy criterion has a producer using only:

- exact integer von Mangoldt prefix sums;
- multiplication and subtraction;
- rational squares and denominators.

No logarithmic location, transform evaluation, quadrature, or prime-pair matrix
is required.

For scale four,

\[
 \boxed{
 \mathcal E_4(N)
 =\sum_{m=2}^{N-1}
 {\left[
   \psi(m)-4\psi(\lfloor m/4\rfloor)
  \right]^2
  \over m(m+1)}.}
 \tag{L-15146.2}
\]

Combined with `T-15119`, RH is equivalent to

\[
 \boxed{
 \mathcal E_a(N)=N^{o(1)}}
 \tag{L-15146.3}
\]

for any one fixed integer `a>=2`.

## 2. Exact PNT-error increment

Write

\[
 E(t)=\psi(t)-t.
\]

For real `t`, the main terms cancel exactly:

\[
 \boxed{
 \psi(t)-a\psi(t/a)
 =E(t)-aE(t/a).}
 \tag{L-15146.4}
\]

Thus `E_a` is not measuring the size of the main prime mass. It measures one
multiplicative scale increment of the complete prime-number-theorem error.

In normalized form,

\[
 {\psi(t)\over t}-{\psi(t/a)\over t/a}
 ={E(t)\over t}-{E(t/a)\over t/a}.
 \tag{L-15146.5}
\]

The empirical cancellation in PR #216 and `X-15122` is therefore a direct
scale-coherence property of the PNT error.

## 3. Multiplicative cocycle

For `a,b>1`, define

\[
 \Delta_aP(t)=P(t)-P(t/a).
\]

Then

\[
 \boxed{
 \Delta_{ab}P(t)
 =\Delta_aP(t)+\Delta_bP(t/a).}
 \tag{L-15146.6}
\]

Iterating at one scale gives

\[
 \boxed{
 \Delta_{a^k}P(t)
 =\sum_{j=0}^{k-1}\Delta_aP(t/a^j).}
 \tag{L-15146.7}
\]

This is the exact renormalization law for the family of safe filters. In
Laplace coordinates it is the elementary factorization

\[
 1-(ab)^{1/2-z}
 =[1-a^{1/2-z}]
 +a^{1/2-z}[1-b^{1/2-z}].
\]

By Cauchy–Schwarz and a change of variables,

\[
 \boxed{
 \mathcal E_{a^k}(Y)
 \le k\sum_{j=0}^{k-1}
 a^j\mathcal E_a(Y/a^j),}
 \tag{L-15146.8}
\]

where `P(t)=0` below the first prime and harmless lower-end intervals are
included in the convention. Thus a subpolynomial estimate at one fixed scale
propagates to every fixed power of that scale.

## 4. Unit-log block production

For an integer block index `J`, define

\[
 \mathcal B_a(J)
 =\int_{e^J}^{e^{J+1}}
 |P(t)-P(t/a)|^2dt.
 \tag{L-15146.9}
\]

It is exactly the corresponding subrange of (L-15146.1), with at most two
rational endpoint fragments. The cumulative energy is the sum of these
nonnegative blocks.

Consequently the criterion of `T-15119` is equivalently

\[
 \boxed{
 \limsup_{J\to\infty}
 {\log(1+\mathcal B_a(J))\over2J}=0.}
 \tag{L-15146.10}
\]

A sufficient recursive estimate is any inequality of the form

\[
 \boxed{
 \mathcal B_a(J)
 \le C(1+J)^A
 +\varepsilon_J
  \max_{J_0\le k<J}\mathcal B_a(k),
 \qquad \varepsilon_J\to0.}
 \tag{L-15146.11}
\]

Indeed, after increasing `J_0`, the feedback coefficient is below `1/2`; an
induction gives a polynomial block envelope and hence RH through `T-15119`.

Equation (L-15146.11) is the proof-facing form suggested independently by the
PR #216 prime-pair data. The cocycle shows that such a recursion is naturally a
multiplicative-scale statement rather than a relation among unrelated finite
matrices.

## 5. Selberg interface

Selberg's exact coefficient identity may be summed at `x` and `x/a`, then
subtracted before any absolute value is taken. The output contains precisely the
increment (L-15146.4), together with bilinear terms at the two nested scales.
The completion target is to organize those bilinear terms into the energy on
the left of (L-15146.11) plus a lower-scale feedback term.

The crucial restriction is:

```text
retain the signed Selberg quadratic convolution
until after the scale subtraction.
```

Bounding the two scale equations separately or replacing the convolution by its
absolute value loses the cancellation already observed at more than ninety-nine
percent strength.

## 6. Proof boundary

Closed:

- the exact rational discrete-energy formula;
- the exact PNT-error increment;
- the multiplicative cocycle;
- the fixed-power energy transfer;
- the recursive inequality that would suffice for RH.

Open:

- derivation of (L-15146.11) from the Selberg convolution or another arithmetic
  identity.

No recursive bound and no RH proof is claimed here.