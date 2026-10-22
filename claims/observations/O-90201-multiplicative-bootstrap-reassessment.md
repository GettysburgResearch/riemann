# O-90201 — Reassessment of the Multiplicative Bootstrap after exact Liouville and Bernstein rigidity

Claim ID: `O-90201`  
Status: **STRUCTURAL CONSEQUENCES + FINITE RECONNAISSANCE; statuses inherited from `L-90201` and `T-90201`**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Scope: route selection and finite calibration; no RH claim

## 1. What changed

The fifth-dispatch narrative in `T-90008/T-90009` correctly discovered that the
free-sign adversary disappears after imposing multiplicativity. Two exact
identities now explain the phenomenon and sharpen its status.

### The ramp side closes completely

`L-90201` proves pointwise

\[
 ((\mu^2f)*\log)(n)\ge\Lambda(n)
\]

for every real completely multiplicative prime assignment `f(p) in [-1,1]`.
Therefore

\[
 \min_{f\in\mathcal H}\operatorname{Ramp}_f(X)
 =\operatorname{Ramp}_\lambda(X)
\]

at every endpoint. The class search and asymptotic Euler-rigidity sketch are
superseded at this scope by a local positive Bernstein formula.

### The GFEP side is hereditary

`T-90201` proves that every nonempty Boolean coefficient at endpoint `X` is a
positive sum of true GFEP values at endpoints `X/q`, `q>=2`. Consequently:

- if the proper descendants are positive, lambda is automatically the global
  class minimizer at the current endpoint;
- at a first GFEP counterexample, lambda-extremality still holds;
- the only unclassified coefficient is the current lambda value itself.

The correct new object is therefore not bare lambda-extremality. It is the
**empty Bernstein coefficient problem inside a completely classified hereditary
polynomial**.

## 2. Why the exhaustive class sizes were misleading

The WHT decomposition in `X-90008` is exact and valuable as a hostile finite
check. But the reported class sizes `2^95` and `2^669` measure the number of
prime-sign vertices, not the proof complexity after the arithmetic hierarchy is
used.

At depth `K=X/n`, the full class certificate is a linear divisor DAG rather
than an exponential vertex search. At the retained points, direct evaluation
shows that all descendants beyond the ratio cutoff `q>K/20` are positive, so
only the following deep labels remain below that cutoff. Using the existing
certified band as a cofinal theorem at arbitrary real descendants would require
a separate real-endpoint interpolation statement; the table itself is a finite
verified fact.

| `(X,n,p)` | `K` | class size described by prime vertices | labels below the ratio cutoff | minimum nonempty Bernstein coefficient |
|---|---:|---:|---:|---:|
| `(2000,20,20)` | 100 | `2^25` | 4 | `0.0276616` |
| `(3000,25,25)` | 120 | `2^30` | 5 | `0.0153423` |
| `(4000,15,15)` | 266 | `2^56` | 12 | `0.00475530` |
| `(10000,20,20)` | 500 | `2^95` | 24 | `0.000801603` |

These minima occur at large squarefree derivative labels near the support edge,
where the coefficient is already a shallow descendant. No negative mixed
coefficient was found.

The finite conclusion is stronger than “the minimizer happened to be lambda”:
the entire polynomial has nonnegative Bernstein coefficients away from its
constant term.

## 3. Exact line where multiplicativity is consumed

The hostile verifier for `T-90009` located the first obstruction at identities
such as

\[
 f(6)=f(2)f(3).
\]

`T-90201` gives the all-orders version. Multiplicativity is consumed when the
free squarefree coordinates are replaced by one Boolean monomial per prime
set. Expanding around the all-minus point sends the coefficient of every
nonempty monomial to

\[
 2^{\omega(a)}
 \sum_{r:\operatorname{rad}(r)\mid a}
 (ar)^{-1/2}\Sigma_{X/(ar),n}(p).
\]

Thus the parity constraint at `6` is the first member of an infinite descendant
hierarchy, not an isolated finite rescue.

## 4. Correct scope of the Final Deficit Theorem

The exact results do not invalidate the core analytic warning of `T-90009`:
pretentious distances alone do not produce the power saving required at the
Mobius/Liouville slice.

They do refine its interpretation.

```text
comparison of H with lambda on the positive ramp
    CLOSED exactly by local divisor algebra;

comparison of GFEP class directions with lambda
    inherited from proper descendant GFEP values;

power-scale estimate of the current lambda/empty coefficient
    still RH-bearing and untouched.
```

In particular, Hall's optimal constant is not needed to make Form A uniform
over `H`: uniformity is already equivalent to the lambda slice. Hall/Halasz
remain fences on a chosen generic mean-value method for estimating that slice.
They should not be read as an impossibility theorem for every multiplicative
identity, because `L-90201/T-90201` themselves are non-distance multiplicative
identities. They simply leave the empty coefficient unchanged.

## 5. New attack interfaces

The descendant theorem exposes three concrete interfaces not visible in the raw
WHT formulation.

### A. Empty-coefficient renewal

For every exit,

\[
 \Sigma_{X,n}(p)
 =c_p^{X,n}(1)
 -\sum_{q=2}^{\lfloor X/n\rfloor}
 q^{-1/2}\Sigma_{X/q,n}(p).
\]

The forcing is a positive transport packet. Every delay is a smaller endpoint.
The obstacle is exact noncontractive balance, not class extremality.

### B. Sprinkled Liouville interpolation

With independent prime-flip density `t`,

\[
 F_X(2t-1)
 =\Sigma_X+
 \sum_{q\ge2}(2t)^{\omega(q)}q^{-1/2}\Sigma_{X/q}.
\]

This gives a family of exact weighted renewals. A successful proof would need a
scale-dependent choice of `t` and a lower estimate surviving subtraction of the
positive descendant ledger. No such estimate is claimed here.

### C. Sparse producer hierarchy

The same formulas hold after the exact three-site-or-less exit trace of
`L-32301` is applied. This is the preferred structural target: preserve the
bottom/ternary/top recombination and attack the single empty coefficient rather
than every exit separately.

## 6. Honest verdict

The new work pushes beyond the five-dispatch endpoint in two ways:

1. one half of lambda-extremality is now a theorem for all endpoints and all
   real prime parameters;
2. the other half is decompiled into an exact descendant hierarchy, explaining
   why multiplicative adversaries disappear and proving they cannot be the
   first obstruction.

It does not prove the empty coefficient. The Riemann Hypothesis remains
unproved. The live question is now narrower:

> Can the positive forcing in the empty-coefficient renewal be matched to the
> complete smaller-endpoint ledger by an exact dilation-compatible
> construction, especially after the sparse producer trace is retained?

That is a structural problem with every nonempty Boolean direction already
accounted for.
