# L-23827 — Every parabolic endpoint atom is tail-majorized by its critical target increment

Claim ID: `L-23827`  
Title: The positive endpoint-scale carry atom has no continuum transport deficit at any scale  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: the endpoint kernel formula of PR #265 `L-26204`; elementary sum-integral bounds  
Scope: continuum endpoint-scale geometry; no finite prime-sampling estimate and no RH conclusion

## 1. Endpoint response and critical increment

Let

\[
F(u)=\sum_{1\le k\le 1/u}
\left(\frac{\log(ku)+4}{\sqrt{ku}}-4\right),
\qquad 0<u\le1,
\tag{L-23827.1}
\]

be the continuum response of the complete parabolic seed.  Differentiating one
endpoint scale gives the positive endpoint kernel

\[
\boxed{
 k(u)=-\frac12F(u)-uF'(u).
}
\tag{L-23827.2}
\]

On the reciprocal cell

\[
\frac1{N+1}<u\le\frac1N,
\qquad N\ge1,
\]

write

\[
S_N=\sum_{j=1}^Nj^{-1/2}.
\tag{L-23827.3}
\]

The exact cell formula of the endpoint-scale calculation is

\[
\boxed{
 k(u)=2N-\frac{S_N}{\sqrt u}.
}
\tag{L-23827.4}
\]

The critical target response changes with endpoint scale by the density

\[
\boxed{h_\partial(u)=u^{-1/2}.}
\tag{L-23827.5}
\]

Both densities have total mass two:

\[
\int_0^1k(u)\,du
=
\int_0^1u^{-1/2}\,du
=2.
\tag{L-23827.6}
\]

## 2. Exact cumulative discrepancy

Define the upper-tail discrepancy

\[
K(\theta)=\int_\theta^1
\left[k(u)-u^{-1/2}\right]du.
\tag{L-23827.7}
\]

For

\[
\frac1{N+1}<\theta\le\frac1N,
\]

one has the exact formula

\[
\boxed{
K(\theta)
=2\left[(S_N+1)\sqrt\theta-N\theta-1\right].
}
\tag{L-23827.8}
\]

### Proof

Inside one cell,

\[
K'(\theta)
=-k(\theta)+\theta^{-1/2}
=\frac{S_N+1}{\sqrt\theta}-2N.
\]

The right side is the derivative of (L-23827.8).  At `theta=1`, both sides
vanish.  At a reciprocal boundary the entering endpoint term is zero, so the
cell formulas agree continuously.  Induction across the reciprocal cells proves
(L-23827.8).

## 3. Tail majorization

The elementary decreasing-sum estimate gives

\[
S_N
\le1+\int_1^Nx^{-1/2}dx
=2\sqrt N-1.
\tag{L-23827.9}
\]

Hence

\[
\begin{aligned}
\frac12K(\theta)
&\le2\sqrt{N\theta}-N\theta-1\\
&=-(\sqrt{N\theta}-1)^2
\le0.
\end{aligned}
\]

Therefore

\[
\boxed{
K(\theta)\le0
\qquad(0<\theta\le1).
}
\tag{L-23827.10}
\]

The inequality is strict for every `0<theta<1`.  Indeed, equality in the
sum-integral estimate is possible only in the trivial first cell, and there the
square vanishes only at `theta=1`.

Thus the endpoint-atom measure

\[
k(u)du
\]

is stochastically dominated by the critical target-increment measure

\[
u^{-1/2}du.
\]

Equivalently, if

\[
[k(u)-u^{-1/2}]du=d\mu_+-d\mu_-,
\]

then

\[
\mu_+([\theta,1])\le\mu_-([\theta,1])
\qquad(0<\theta<1).
\tag{L-23827.11}
\]

## 4. Explicit positive transport

The two measures in (L-23827.11) have equal total mass.  Their monotone quantile
coupling therefore gives a positive transport measure `pi` supported on

\[
0<u\le v\le1
\tag{L-23827.12}
\]

such that

\[
[k(u)-u^{-1/2}]du
+
\iint(-\delta_u+\delta_v)d\pi(u,v)
=0.
\tag{L-23827.13}
\]

Every transported unit moves from a smaller to a larger endpoint ratio.  In the
carry incidence objective its gain is

\[
\log(v/u)\ge0.
\tag{L-23827.14}
\]

Consequently **each individual endpoint atom**, not merely their complete
parabolic sum, admits a zero-loss continuum deformation into its critical target
increment.

## 5. Consequences for the consolidated proof architecture

The endpoint-scale frame of PR #265 is a positive superposition of these atoms.
Equation (L-23827.13) therefore proves continuum tail majorization before any
greedy elimination, Green inversion, or positive-part operation.  It gives an
independent atomwise explanation of the shell order in `L-23823`.

What remains is not a continuum transport theorem.  It is the finite arithmetic
lifting problem:

```text
continuum ratio pair u<=v
-> integer endpoints A<B
-> complete divisor incidences
-> logarithmically weighted prime shell
-> subpolynomial unmatched boundary charge.
```

The deterministic first-order drift in the unweighted ordinary-prime queue is
not canceled by this theorem.  The review-facing finite consumer must retain the
weighted fixed-ratio shell of `L-23824`--`L-23826`.

## 6. Proof boundary

Closed here:

1. the exact endpoint-kernel tail formula;
2. tail majorization at every ratio;
3. strictness away from the endpoint;
4. a positive ordered transport for every endpoint atom;
5. nonnegative logarithmic transport gain.

Open:

1. a finite integer/divisor lift with subpolynomial weighted shell charge;
2. `WSTS`;
3. RH.
