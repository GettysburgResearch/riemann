# T-90201 — The Boolean Bernstein descendant hierarchy: every nonempty lambda derivative is a smaller-scale GFEP value

Claim ID: `T-90201`  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `T-90007` transported coefficient identity; the exact scaling of `w_X`; `T-90005` for the certified band consequence  
Scope: finite Boolean algebra, multiples Möbius inversion, and exact endpoint scaling; no sign theorem for the empty coefficient and no RH conclusion

## 0. Why this theorem is needed

`T-90008` reported an exhaustive and initially surprising phenomenon: over the
entire completely multiplicative sign class `H`, the Liouville point was the
exact minimizer of every tested GFEP exit. It proved single-prime flip
positivity and proposed global **lambda-extremality** as a new open coordinate.

The full higher-order mechanism is exact. The class functional has a Boolean
Bernstein expansion around the Liouville vertex. Every nonempty coefficient in
that expansion is a positive linear combination of the **same GFEP exit at
strictly smaller endpoints**. The exhaustive Walsh searches are therefore the
finite shadow of a hereditary divisor-DAG identity.

The only coefficient not sent to a smaller endpoint is the empty coefficient,
which is the current GFEP value itself.

## 1. General finite class functional

Fix `K>=1` and a real sequence `c(1),...,c(K)`. For prime parameters

\[
 x_p\in[-1,1]
\]

put, on squarefree integers,

\[
 f_x(k)=\prod_{p\mid k}x_p.
\]

Define

\[
 \boxed{
 F_c(x)=\sum_{k\le K}\mu^2(k)f_x(k)c(k).
 }
 \tag{T-90201.1}
\]

Let

\[
 y_p=\frac{1+x_p}{2}\in[0,1],
 \qquad y_a=\prod_{p\mid a}y_p
 \quad(a\text{ squarefree}),
 \qquad y_1=1.
\]

The Liouville vertex is `x_p=-1`, equivalently `y_p=0`.

## 2. Theorem A — exact Boolean Bernstein expansion

For every squarefree `a<=K`, define

\[
 \boxed{
 B_c(a)
 =2^{\omega(a)}
 \sum_{m\le K/a\atop (m,a)=1}
 \mu(m)c(am).
 }
 \tag{T-90201.2}
\]

Then

\[
 \boxed{
 F_c(x)=
 \sum_{a\le K\atop a\ {\rm squarefree}}
 B_c(a)y_a.
 }
 \tag{T-90201.3}
\]

In particular,

\[
 \boxed{
 B_c(1)=\sum_{k\le K}\mu(k)c(k)=F_c(\lambda).
 }
 \tag{T-90201.4}
\]

### Proof

For squarefree `k`, expand at the Liouville vertex:

\[
 \begin{aligned}
 f_x(k)
 &=\prod_{p\mid k}(-1+2y_p)\\
 &=\sum_{a\mid k}(-1)^{\omega(k)-\omega(a)}
   2^{\omega(a)}y_a.
 \end{aligned}
\]

Write `k=am`. Since `k` is squarefree, `(a,m)=1` and

\[
 (-1)^{\omega(k)-\omega(a)}=\mu(m).
\]

Substituting into (T-90201.1) and interchanging finite sums gives
(T-90201.2)--(T-90201.3). ∎

### Complete lambda-monotonicity

If

\[
 B_c(a)\ge0\qquad(a>1),
 \tag{T-90201.5}
\]

then `F_c` is coordinatewise nondecreasing in every `y_p` on the full cube and

\[
 \boxed{
 F_c(x)\ge F_c(\lambda)
 \qquad(x_p\in[-1,1]).
 }
 \tag{T-90201.6}
\]

For a vertex obtained by flipping a prime set `A` from `lambda`,

\[
 \boxed{
 F_c(f_A)-F_c(\lambda)
 =\sum_{a\mid\prod_{p\in A}p\atop a>1}B_c(a).
 }
 \tag{T-90201.7}
\]

Thus the single-flip spectrum of `T-90008` is only the first layer
`B_c(p)`. Formula (T-90201.2) supplies every mixed flip interaction.

Condition (T-90201.5) is a sufficient certificate for global extremality. No
claim that it is necessary for an arbitrary polynomial is made.

## 3. Theorem B — semigroup/primitive form of every derivative

For squarefree `a`, define the multiplicative semigroup

\[
 \mathcal S(a)
 =\{r\ge1:\operatorname{rad}(r)\mid a\}.
 \tag{T-90201.8}
\]

Define the multiples-Möbius primitive of `c` by

\[
 \boxed{
 P_c(q)=\sum_{d\le K/q}\mu(d)c(qd).
 }
 \tag{T-90201.9}
\]

Then

\[
 \boxed{
 \frac{B_c(a)}{2^{\omega(a)}}
 =\sum_{r\in\mathcal S(a)\atop ar\le K}P_c(ar).
 }
 \tag{T-90201.10}
\]

### Proof

Let

\[
 h_a(r)=\mathbf1_{\operatorname{rad}(r)\mid a}.
\]

The finite coefficient identity

\[
 \boxed{
 \mu(m)\mathbf1_{(m,a)=1}=(\mu*h_a)(m)
 }
 \tag{T-90201.11}
\]

is immediate prime by prime. At a prime not dividing `a`, the local series is
`1-z`; at a prime dividing `a`, the product `(1-z)(1+z+z^2+...)` is `1`,
which exactly deletes every coefficient divisible by that prime.

Apply (T-90201.11) in (T-90201.2):

\[
 \begin{aligned}
 2^{-\omega(a)}B_c(a)
 &=\sum_m(\mu*h_a)(m)c(am)\\
 &=\sum_{r\in\mathcal S(a)}\sum_d\mu(d)c(ard)\\
 &=\sum_{r\in\mathcal S(a)}P_c(ar).
 \end{aligned}
\]

All sums are finite by the support bound `K`. ∎

This form is the crucial structural statement: every higher Boolean derivative
is assembled from ordinary Möbius primitives on the descendant multiples
`a, ap, ap^2, ...` supported on the primes of `a`.

## 4. Theorem C — specialization to a GFEP exit

Fix the GFEP data `(X,n,p)` and write

\[
 K=\left\lfloor\frac Xn\right\rfloor.
\]

Let `c_p^{X,n}(k)` be the transported coefficient of `T-90007`, so

\[
 \Sigma^f_{X,n}(p)
 =\sum_{k\le K\atop k\ {\rm squarefree}}
 f(k)c_p^{X,n}(k).
 \tag{T-90201.12}
\]

The critical weight scales exactly:

\[
 w_X(mqd)=q^{-1/2}w_{X/q}(md).
\]

The first-entrance path kernel is independent of the endpoint. Therefore

\[
 c_p^{X,n}(qd)
 =q^{-1/2}c_p^{X/q,n}(d),
 \tag{T-90201.13}
\]

and the primitive (T-90201.9) is

\[
 \boxed{
 P_c(q)
 =q^{-1/2}\Sigma_{X/q,n}(p).
 }
 \tag{T-90201.14}
\]

Use the convention `Sigma_{Y,n}(p)=0` when `p>Y`; this is exactly what the
coefficient formula gives because the exit is outside the endpoint.

Combining Theorems A and B gives the complete descendant formula

\[
 \boxed{
 B_{X,n,p}(a)
 =2^{\omega(a)}
 \sum_{r\in\mathcal S(a)\atop ar\le K}
 \frac{\Sigma_{X/(ar),n}(p)}{\sqrt{ar}}.
 }
 \tag{T-90201.15}
\]

Every term on the right has endpoint at most `X/a`. For `a>1` this is a strict
proper descendant of `X`.

### Hereditary lambda-rigidity

If

\[
 \Sigma_{X/q,n}(p)\ge0
 \qquad(2\le q\le K),
 \tag{T-90201.16}
\]

then every nonempty Bernstein coefficient is nonnegative, and hence

\[
 \boxed{
 \min_{f\in\mathcal H}\Sigma^f_{X,n}(p)
 =\Sigma^{\lambda}_{X,n}(p)
 =\Sigma_{X,n}(p).
 }
 \tag{T-90201.17}
\]

The same minimum holds over the larger real cube `x_p in [-1,1]`.

This proves the following first-failure principle:

> On any divisor-closed endpoint DAG, at a node whose every proper descendant
> GFEP value is nonnegative, the Liouville/Mobius point is automatically the
> global class minimizer, regardless of the sign of the current value.

Thus a first GFEP failure, if one exists, cannot be preceded by a multiplicative
adversary. Lambda-extremality is hereditary from GFEP; it is not an independent
source of positivity.

## 5. Collapse of the exponential class search to a descendant certificate

Formula (T-90201.15) gives a deterministic certificate with at most `K-1`
proper descendant values:

\[
 \boxed{
 \Sigma_{X/q,n}(p)\ge0
 \quad(2\le q\le K)
 \quad\Longrightarrow\quad
 B_{X,n,p}(a)\ge0\ \text{for every }a>1.
 }
 \tag{T-90201.18}
\]

Thus a class described by `2^{pi(K)}` prime-sign vertices never needs vertex
enumeration. One checks a divisor DAG of linear size and obtains every higher
mixed flip coefficient formally.

The ratio is even smaller wherever the certified `K<20` GFEP theorem is
available at the descendant endpoint. At descendant `q`, the depth is `K/q`,
so descendants with `q>K/20` are in the certified proportional band. For a
strictly integer endpoint formulation this applies immediately when `q` divides
`X`; a uniform extension to arbitrary real descendants `X/q` requires the
corresponding real-endpoint interpolation theorem and is not silently assumed
here.

At the retained finite points, direct evaluation of the real descendant DAG
leaves only the following deep labels below the ratio cutoff:

```text
K = 100:   4 labels below K/20 instead of a 2^25 class;
K = 120:   5 labels below K/20 instead of a 2^30 class;
K = 266:  12 labels below K/20 instead of a 2^56 class;
K = 500:  24 labels below K/20 instead of a 2^95 class.
```

These counts are a finite certification fact, not a claimed new cofinal
real-endpoint theorem. For the ramp searches described as classes up to
`2^669`, `L-90201` removes the search entirely.

This is not merely an algorithmic speedup. It explains why multiplicativity
consumed the free-sign adversary so abruptly: every nonempty class direction
was already a weighted descendant of the true arithmetic problem.

## 6. Nonnegative traces and the sparse producer

Let `a(p)>=0` be any endpoint-independent nonnegative exit trace and define

\[
 F_a^X=\sum_p a(p)\Sigma_{X,n}(p),
 \qquad
 c_a^X(k)=\sum_p a(p)c_p^{X,n}(k).
 \tag{T-90201.20}
\]

All previous identities are linear in the exit trace. Therefore

\[
 \boxed{
 B_a^{X}(u)
 =2^{\omega(u)}
 \sum_{r\in\mathcal S(u)\atop ur\le K}
 \frac{F_a^{X/(ur)}}{\sqrt{ur}}.
 }
 \tag{T-90201.21}
\]

For the true hitting trace of `L-32301`,

\[
 F_a^X=nA_X(n),
\]

and the trace is supported only at the bottom exit, one or two ternary contacts,
and the top binary contact. Hence every nonempty Boolean derivative of the
**actual sparse producer** is a positive combination of strictly smaller
producer coefficients.

At a first producer failure in the descendant DAG, Liouville is therefore also
the exact global minimizer of the transported sparse class.

## 7. Theorem D — empty-coefficient renewal and the real remaining object

Multiples Möbius inversion of (T-90201.9) gives

\[
 c(q)=\sum_{d\le K/q}P_c(qd).
 \tag{T-90201.22}
\]

At `q=1`, using (T-90201.14),

\[
 \boxed{
 c_p^{X,n}(1)
 =\sum_{q\le K}\frac{\Sigma_{X/q,n}(p)}{\sqrt q}.
 }
 \tag{T-90201.23}
\]

Equivalently,

\[
 \boxed{
 \Sigma_{X,n}(p)
 =c_p^{X,n}(1)
 -\sum_{2\le q\le K}
  \frac{\Sigma_{X/q,n}(p)}{\sqrt q}.
 }
 \tag{T-90201.24}
\]

The forcing `c_p(1)` is positive in the Stieltjes/path coordinate of the Exact
Flow Gambit, while every delayed term is the same exit at a smaller endpoint.
The delay mass is not contractive; no sign is inferred here.

A useful one-parameter form follows by setting every `y_p=t`. From Theorems A
and B, every integer `q>=2` occurs uniquely with `a=rad(q)`, so

\[
 \boxed{
 F_c(2t-1)
 =B_c(1)+
  \sum_{2\le q\le K}(2t)^{\omega(q)}P_c(q).
 }
 \tag{T-90201.25}
\]

At `t=1/2`, this is exactly (T-90201.23), because random independent prime
signs annihilate every nonconstant squarefree monomial and leave `c(1)`.

This identifies the true frontier:

```text
all nonempty Boolean coefficients     descendant arithmetic, classified;
empty Boolean coefficient             current GFEP / producer value, open.
```

## 8. Consequences for T-90008 and T-90009

1. The one-scalar lambda-extremality conjecture is a theorem by `L-90201`.
2. Per-exit lambda-extremality is implied by GFEP on proper descendants and is
   automatic at a first counterexample. It should be recorded as
   **hereditary lambda-rigidity**, not as an independent conjectural escape from
   the GFEP wall.
3. The WHT certificates remain valid finite evidence, but the exponential class
   size is not the mathematical difficulty. A linear divisor-DAG certificate
   suffices; at the retained points only the labels below the `K/20` ratio
   cutoff require deep evaluation.
4. The Final Deficit Theorem remains a fence on distance-only estimates of the
   empty Mobius coefficient. It does not govern the now-closed nonempty class
   directions.

## 9. Proof boundary

Proved exactly:

1. the complete Boolean Bernstein expansion;
2. every mixed flip coefficient, not only single flips;
3. the semigroup/primitive formula;
4. the scaled-descendant identity for every GFEP exit;
5. hereditary lambda-rigidity and the first-failure principle;
6. collapse of finite class certification from an exponential cube to a linear descendant DAG;
7. the same hierarchy for every nonnegative trace and the sparse producer;
8. the empty-coefficient and sprinkled renewal identities.

Still open:

1. the sign of the empty coefficient at unbounded depth;
2. GFEP and sparse producer positivity;
3. a contractive or exact combinatorial solution of (T-90201.24);
4. RH.
