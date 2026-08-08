# L-26202 — The parabolic continuum defect is tail-majorized by its slack

Claim ID: `L-26202`  
Title: Every upper tail of the parabolic carry defect is nonpositive, yielding an explicit monotone defect-to-slack transport  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM WITH EXACT FINITE GATES PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue family: `#245/#262`  
Frozen base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
Dependencies: PR #248 `L-24504`, `L-24505`, `L-24514`  
Scope: continuum signed transport; no finite-prime or finite-floor transfer

## 1. The continuum defect

Retain the scale-one parabolic profile

\[
 B(t)=2\sqrt t\left[
  \log\frac1t-2(1-\sqrt t)
 \right],
 \qquad 0<t\le1,
\tag{L-26202.1}
\]

with `B(0)=B(1)=0`, and put

\[
 g(t)=-B'(t)
 =\frac{\log t+4}{\sqrt t}-4.
\tag{L-26202.2}
\]

For `0<theta<=1`, define the finite dilation response

\[
 (\mathcal Tg)(\theta)
 =\sum_{1\le k\le1/\theta}g(k\theta),
\tag{L-26202.3}
\]

and the critical target

\[
 h(\theta)=\theta^{-1/2}\log(1/\theta).
\tag{L-26202.4}
\]

The signed continuum constraint defect is

\[
 \boxed{E(\theta)=(\mathcal Tg)(\theta)-h(\theta).}
\tag{L-26202.5}
\]

`L-24514` proves that its total integral is zero:

\[
 \int_0^1E(\theta)\,d\theta=0,
\tag{L-26202.6}
\]

because the parabolic objective is exactly four.

The new theorem is the one-sided tail inequality

\[
 \boxed{
 H(\theta):=\int_\theta^1E(u)\,du\le0
 \qquad(0<\theta\le1).}
\tag{L-26202.7}
\]

Equality holds at `theta=1` and in the limiting total-mass identity at
`theta downarrow0`; every interior reciprocal endpoint is strictly negative.

## 2. Exact reciprocal-cell formula

Fix `N>=1` and

\[
 \frac1{N+1}\le\theta\le\frac1N.
\]

Put

\[
 S_N=\sum_{k=1}^Nk^{-1/2},
 \qquad
 A_N=\sum_{k=1}^Nk^{-1/2}\log k.
\tag{L-26202.8}
\]

Since `g=-B'` and `B(1)=0`, finite substitution gives

\[
 \int_\theta^1(\mathcal Tg)(u)\,du
 =\sum_{k=1}^N\frac{B(k\theta)}k.
\tag{L-26202.9}
\]

Also

\[
 \int_\theta^1u^{-1/2}\log(1/u)\,du
 =4(1-\sqrt\theta)+2\sqrt\theta\log\theta.
\tag{L-26202.10}
\]

Substituting (L-26202.1) yields the exact cell formula

\[
 \boxed{
 \begin{aligned}
 H_N(\theta)
 ={}&4N\theta-4\\
 &+\sqrt\theta\left[
  4-4S_N-2A_N-2(S_N+1)\log\theta
 \right].
 \end{aligned}}
\tag{L-26202.11}
\]

The entering summand at a reciprocal boundary is `B(1)=0`, so these cell
formulas agree continuously.

## 3. Every reciprocal endpoint is negative

Define

\[
 K_N=(S_N+1)\log N-A_N-2S_N+2.
\tag{L-26202.12}
\]

At the right endpoint of the cell,

\[
 \boxed{H(1/N)=\frac{2K_N}{\sqrt N}.}
\tag{L-26202.13}
\]

The sequence has the exact recurrence

\[
 \boxed{
 K_N-K_{N-1}
 =(S_{N-1}+1)\log\frac N{N-1}-\frac2{\sqrt N}.}
\tag{L-26202.14}
\]

Since `x mapsto x^{-1/2}` is decreasing,

\[
 S_{N-1}+1\le2\sqrt{N-1}.
\tag{L-26202.15}
\]

The logarithmic mean strictly exceeds the geometric mean, so

\[
 \log\frac N{N-1}
 <\frac1{\sqrt{N(N-1)}}.
\tag{L-26202.16}
\]

Equations (L-26202.14)--(L-26202.16) give

\[
 K_N-K_{N-1}<0.
\]

Because `K_1=0`,

\[
 \boxed{K_N<0\qquad(N>=2).}
\tag{L-26202.17}
\]

Thus every nontrivial reciprocal endpoint in (L-26202.13) is strictly
negative.

## 4. Shape on one reciprocal cell

Differentiating (L-26202.11) gives

\[
 H_N'(\theta)
 =4N-\theta^{-1/2}
 \left[A_N+4S_N+(S_N+1)\log\theta\right],
\tag{L-26202.18}
\]

and

\[
 \boxed{
 H_N''(\theta)
 =\theta^{-3/2}\left\{
  \frac12\left[A_N+4S_N+(S_N+1)\log\theta\right]
  -(S_N+1)
 \right\}.}
\tag{L-26202.19}
\]

The expression in braces increases with `theta`.

### 4.1 Cells `N>=15`

Exact rational interval arithmetic gives

\[
 \boxed{K_{16}< -\frac12.}
\tag{L-26202.20}
\]

This is replayed independently in `X-26201`; no floating assertion is used.
Since `K_N` decreases, for `N>=15` the brace in (L-26202.19) at the left
endpoint is

\[
 -\frac12K_{N+1}-\frac1{\sqrt{N+1}}\ge0.
\tag{L-26202.21}
\]

Hence `H_N` is convex on the whole cell.  A convex function lies below the
maximum of its endpoint values, and both endpoint values are nonpositive by
Section 3.  Therefore `H_N<=0`.

### 4.2 The first fourteen cells

For `N=1`, equation (L-26202.18) reduces, after putting
`t=sqrt(theta)`, to

\[
 H_1'(\theta)
 =4\left[1-\frac{1+\log t}{t}\right]\ge0
\]

by `log t<=t-1`.

For `2<=N<=14`, the exact rational interval checker in `X-26201` subdivides the
closed reciprocal cell and proves the uniform directed lower bound

\[
 \boxed{H_N'(\theta)>\frac7{25}.}
\tag{L-26202.22}
\]

The checker evaluates logarithms by an exact rational `atanh` series with a
rigorous remainder and square roots by integer-square enclosures.  Thus each of
these cells is increasing and is bounded above by its negative right endpoint.

Sections 3--4 prove (L-26202.7).

## 5. Explicit transport interpretation

Put

\[
 C(\theta)=-H(\theta)\ge0.
\tag{L-26202.23}
\]

Since `H'=-E` away from the harmless reciprocal knots and both sides are
locally integrable,

\[
 \boxed{E=C'}
\tag{L-26202.24}
\]

in distributions, with

\[
 C(0+)=C(1)=0.
\]

Thus `C` is an explicit nonnegative flux transporting the positive part of the
constraint defect toward larger scale, where the negative slack lies.

Equivalently, write

\[
 E\,d\theta=\mu_+-\mu_-.
\]

Equation (L-26202.6) gives equal total masses, and (L-26202.7) gives

\[
 \mu_+([\theta,1])\le\mu_-([\theta,1])
 \qquad(0<\theta<1).
\tag{L-26202.25}
\]

The monotone quantile coupling therefore supplies a positive measure `pi` with
first marginal `mu_+`, second marginal `mu_-`, and support

\[
 \boxed{0<u\le v\le1.}
\tag{L-26202.26}
\]

At the continuum level every positive parabolic defect can be paid by slack at
a larger multiplicative scale.

For the incidence-block objective of `L-24520`, moving one residual unit from
`u` to `v>=u` has loss

\[
 -\log(v/u)\le0.
\tag{L-26202.27}
\]

Hence the complete continuum transport has nonpositive logarithmic cost.  The
macroscopic positive and negative defect masses found in PR #254 are not an
obstruction once their order is retained; the obstruction is the finite
arithmetic/floor transfer of this monotone coupling.

## 6. What this changes

The previous parabolic programme knew:

```text
positive defect mass  ~ sqrt(X),
negative slack mass   ~ sqrt(X),
signed difference     = lower order.
```

The present theorem adds an order statement:

```text
on every upper scale tail,
negative slack mass >= positive defect mass.
```

This is materially stronger than equality of total signed mass.  It suggests a
positive transport rather than a positive-part deletion and explains why the
monotone Divisibility Cover lost the sharp constant: that cover ignored where
the compensating slack was located.

## 7. Proof boundary

Established here, subject to independent review:

1. the exact reciprocal-cell formula for the cumulative defect;
2. strict negativity at every reciprocal endpoint;
3. nonpositivity throughout every cell;
4. the nonnegative flux and monotone defect-to-slack coupling;
5. nonpositive continuum logarithmic transport cost.

Not established:

- a proof-grade transfer to primes or finite carry columns at subpower error;
- preservation of finite carry-row positivity under the transported correction;
- a finite near-optimal packing or RH.
