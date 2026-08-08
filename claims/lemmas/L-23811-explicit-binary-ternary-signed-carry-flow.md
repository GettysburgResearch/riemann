# L-23811 — Explicit binary–ternary signed carry flow

Claim ID: `L-23811`  
Title: One fixed balanced split kernel saturates the complete carry target algebraically and reduces the prime-ramp problem to a weighted total-variation estimate  
Status: **PROPOSED EXACT CONDITIONAL LEMMA — RECURRENCE ALGEBRA CLOSED; RATE OPEN**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`, `L-23810`  
Scope: one explicit signed producer; no positivity assertion

## 1. A fixed balanced split kernel

For every integer `n>=2`, define

\[
 a_3(n)=\left\lceil{n\over3}\right\rceil,
 \qquad b_3(n)=n-a_3(n),
\tag{L-23811.1}
\]

and

\[
 a_2(n)=\left\lfloor{n\over2}\right\rfloor,
 \qquad b_2(n)=n-a_2(n).
\tag{L-23811.2}
\]

Both splits lie in the fixed balanced window

\[
 {n\over4}\le a_i(n),b_i(n)\le {3n\over4}
\tag{L-23811.3}
\]

for all `n>=2` (with the evident `1+1` case at `n=2`).

At every parent, use one half of the coefficient on the ternary split and one
half on the binary split.  Equal children retain their natural multiplicity.

## 2. Exact descending recurrence

Let `r_X` be the unique target divergence of `L-23810`.  Define the outflow
coefficients `A_X(n)` by descending recursion:

\[
\boxed{
\begin{aligned}
 A_X(n)=r_X(n)+{1\over2}\sum_{m>n}A_X(m)
 \big[&\mathbf1_{a_3(m)=n}+\mathbf1_{b_3(m)=n}\\
      &+\mathbf1_{a_2(m)=n}+\mathbf1_{b_2(m)=n}\big],
\end{aligned}}
}
\tag{L-23811.4}
\]

for `n=X,X-1,...,2`.  The bracket counts a repeated central child twice.
The node `1` equation follows automatically from

\[
\sum_m m r_X(m)=0.
\]

Define the signed split flow

\[
 d_{n,a_3(n)}={1\over2}A_X(n),
 \qquad
 d_{n,a_2(n)}={1\over2}A_X(n),
\tag{L-23811.5}
\]

combining the entries when the two rows coincide.

By construction, its divergence is exactly `r_X`.  Therefore `L-23810` gives

\[
\boxed{
 \sum_{n,j}d_{n,j}\chi_{n,j}(q)
 =w_X(q)
 \qquad(2\le q\le X).
}
\tag{L-23811.6}

This is an algebraic identity for every endpoint `X`; it does not assume any
sign of `A_X(n)`.

## 3. Exact prime and all-integer ledgers

Put

\[
\ell_n={1\over2}\log\binom n{a_3(n)}
       +{1\over2}\log\binom n{a_2(n)},
\tag{L-23811.7}
\]

and

\[
 c_n={1\over2}\sum_{q=2}^{n}\chi_{n,a_3(n)}(q)
     +{1\over2}\sum_{q=2}^{n}\chi_{n,a_2(n)}(q).
\tag{L-23811.8}
\]

The valuation identity and (L-23811.6) give the exact signed formula

\[
\boxed{
 \mathcal P(X)
 :=\sum_{p^k\le X}{\Lambda(p^k)\over\sqrt{p^k}}
       \log{X\over p^k}
 =\sum_{n=2}^{X}A_X(n)\ell_n.
}
\tag{L-23811.9}

Summing (L-23811.6) over all integer columns gives

\[
\boxed{
 \sum_{q=2}^{X}w_X(q)
 =\sum_{n=2}^{X}A_X(n)c_n.
}
\tag{L-23811.10}

Consequently

\[
\boxed{
 \mathcal P(X)-\sum_{q=2}^{X}w_X(q)
 =\sum_{n=2}^{X}A_X(n)(\ell_n-c_n).
}
\tag{L-23811.11}

The right side is independent of how the same divergence is represented by
Pascal four-cycles; the present kernel merely gives one explicit recurrence.

## 4. A single explicit sufficient rate

Dirichlet's hyperbola estimate and Stirling's formula, exactly as in `L-23809`,
give

\[
 |\ell_n-c_n|\le C\sqrt n.
\tag{L-23811.12}
\]

Therefore the explicit weighted total-variation estimate

\[
\boxed{
 \operatorname{BTF}(X)
 :=\sum_{n=2}^{X}|A_X(n)|\sqrt n
 =X^{o(1)}
}
\tag{L-23811.13}
\]

implies

\[
\boxed{
 \mathcal P(X)
 =4\sqrt X+X^{o(1)}
}
\tag{L-23811.14}
\]

and in particular the lower bound consumed by the square-screw route.

An even weaker sufficient statement is the source-specific pairing bound

\[
\boxed{
 \left|\sum_{n=2}^{X}A_X(n)(\ell_n-c_n)\right|=X^{o(1)}.
}
\tag{L-23811.15}
\]

No pointwise positivity is required for either form.

If all `A_X(n)>=0`, then (L-23811.5) is an exact zero-slack BCT certificate.
Finite reconnaissance shows long positive ranges but also demonstrates that
stationary split rules cannot be promoted from finite sign tables alone.  The
review theorem is (L-23811.13) or (L-23811.15), not a numerical positivity
claim.

## 5. Moment identities

For every `0<theta<1`, define the positive split defect

\[
 \delta_\theta(n)
 ={1\over2}\big[a_3(n)^\theta+b_3(n)^\theta-n^\theta\big]
 +{1\over2}\big[a_2(n)^\theta+b_2(n)^\theta-n^\theta\big]>0.
\tag{L-23811.16}
\]

Pairing the divergence equation with `m^theta` yields the exact identity

\[
\boxed{
 -\sum_{m=1}^{X}r_X(m)m^\theta
 =\sum_{n=2}^{X}A_X(n)\delta_\theta(n).
}
\tag{L-23811.17}

Since `delta_theta(n)` is comparable to `n^theta` uniformly in `n`, this gives a
family of Mellin-size probes for the signed producer.  A valid proof of BTF may
use:

- a variation-diminishing theorem for the recurrence;
- a reflected Selberg square for its signed Möbius forcing;
- a blockwise Pascal transport which replaces negative coefficients by an
  equivalent nonnegative flow;
- simultaneous control of the complete moment family (L-23811.17).

Finite moment tables alone do not prove (L-23811.13).

## 6. Review significance

`BCT` is an existential linear program with quadratically many rows.  The
present lemma replaces it by one deterministic `O(X log X)` source computation
and one descending `O(X)` recurrence.  A reviewer can reproduce every
coefficient without solving an LP.

The unresolved assertion remains RH-bearing: an off-line zero can produce a
polynomially large oscillatory contribution to the Möbius tail `r_X`, so no
phase-blind absolute-value proof is permitted.

## 7. Proof boundary

Closed exactly:

- the binary–ternary split kernel is uniformly balanced;
- the recurrence has divergence `r_X`;
- its carry loads equal the complete target `w_X`;
- the exact prime/all-integer ledgers;
- BTF or the weaker pairing estimate implies the sharp prime ramp.

Open:

- BTF (L-23811.13), or the pairing estimate (L-23811.15);
- a cofinal positive Pascal repair of the signed recurrence;
- RH.
