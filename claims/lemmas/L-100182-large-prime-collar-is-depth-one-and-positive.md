# L-100182 — The unsquared large-prime collar is depth one and remains positive

Claim ID: `L-100182`  
Status: **PROVED EXACT DEPTH-ONE REDUCTION + POSITIVITY**  
Created: 2026-08-20  
Depends on: `L-100180`; critical Bernstein scaling inequality  
RH status: **not assumed**

Fix a physical endpoint `X` and choose

\[
Z=X^{9/10}
\]

(or any `Z>=X^(9/10)`). After finite Euler squaring of all primes `p<=Z`, the final critical centered-Bernstein source has:

- squared small-prime labels, whose owner cost is `1/p^2`;
- unsquared labels `p>Z`, whose critical owner cost is `1/p`.

## 1. Depth-one geometry

If `p,q>Z`, then

\[
pq>Z^2\ge X^{9/5}>X.
\]

Hence no active source integer `n<=X` contains two unsquared large primes. The large-prime part of the critical Euler expansion is therefore exactly depth one: one positive squared-core parent minus a sum of one-large-prime children. There are no higher large-prime parity layers.

## 2. One-prime child domination

Let `K` denote the positive critical Bernstein kernel on the completed small-prime core. The sharp critical scaling inequality inherited from `L-100000` gives, for every active unsquared prime `p>Z`,

\[
\text{child}_p(X)\le {1\over p}\,\text{parent}(X).
\]

Summing all active large-prime children therefore gives

\[
\sum_{Z<p\le X}\text{child}_p(X)
\le
\left(\sum_{Z<p\le X}{1\over p}\right)\text{parent}(X).
\]

Using the same elementary prime-counting/partial-summation estimate as `L-100020`, with `Z>=X^(9/10)`,

\[
\sum_{Z<p\le X}{1\over p}<1.
\]

Consequently

\[
\boxed{
\text{parent}(X)-\sum_{Z<p\le X}\text{child}_p(X)>0.
}
\]

Thus the entire completed critical observable is positive at `X`, with the small-prime block controlled by `p^-2` owner mass and the unsquared large-prime collar controlled by a depth-one `p^-1` layer of total mass strictly below one.

## 3. Meaning

This removes the last many-prime parity obstruction from the adaptive critical completion. At every scale, choosing `Z>=X^(9/10)` yields pointwise positivity by an entirely finite source-faithful argument:

```text
small primes <=Z: squared, strictly subcritical owner mass;
large primes >Z: at most one active, depth-one child mass < parent.
```

The theorem is local in `X`. It still does not by itself give eventual positivity of one fixed Mellin density, because the completion cutoff varies with the endpoint. That analytic/source-transfer interface remains separate and must not be hidden.
