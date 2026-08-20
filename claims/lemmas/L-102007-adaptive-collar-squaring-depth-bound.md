# L-102007 — Exact squared-core / unsquared-depth decomposition at the collar threshold

Claim ID: `L-102007`
Status: **PROVED EXACT COMBINATORIAL REDUCTION; FINAL SIGN ESTIMATE OPEN**
Created: 2026-08-21
Audited: 2026-08-21
Depends on: `L-102005--L-102006`; PR #691 `L-100600--L-100603`
RH status: **not assumed**

Fix one double-owner collar with endpoint primes `p_i<p_j` and endpoint `X`.
Put

\[
T=\frac{X}{p_ip_j}.
\]

By `L-102005`, only interval-label products larger than `T` occur in the
centered residual.

Choose a source-side completion cutoff `Z` and square every interior prime
`p<=Z` before physical collapse. Every completed monomial then has a unique
form

\[
\boxed{m=d^2q_1\cdots q_s,}
\tag{L-102007.1}
\]

where

- `d` is a squarefree product of completed primes `p<=Z`;
- `q_1,...,q_s` are distinct unsquared primes larger than `Z`;
- the literal coefficient magnitude is
  \[
  d^{-1}(q_1\cdots q_s)^{-1/2}.
  \]

The centered threshold is exactly

\[
\boxed{d^2q_1\cdots q_s>T.}
\tag{L-102007.2}
\]

## Square-root cutoff

Take

\[
\boxed{Z=T^{1/2}.}
\tag{L-102007.3}
\]

Then every monomial with at least two unsquared labels automatically satisfies
(L-102007.2), because

\[
q_1q_2>Z^2=T.
\]

The exact decomposition is therefore

```text
unsquared depth 0: contributes only when d^2>T;
unsquared depth 1: contributes only when d^2 q>T;
unsquared depth >=2: automatically above the threshold.
```

The earlier depth-three boundary was off by one and is withdrawn.

More generally, if `Z=T^(1/r)` for an integer `r>=1`, then every monomial
with at least `r` unsquared labels automatically exceeds `T`:

\[
q_1\cdots q_r>Z^r=T.
\tag{L-102007.4}
\]

## What this does and does not prove

The depth-zero and depth-one sectors have explicit threshold conditions tied
to the squared core. The depth-at-least-two sector is structurally simpler but
is not absolutely small: the number and total native mass of such monomials
can still be large.

A valid conclusion must recombine

```text
squared-core owner mass;
explicit depth-zero/depth-one collars;
signed depth-at-least-two tail;
joint least/greatest-owner survival;
```

before taking absolute values. This lemma supplies the exact partition only; it
does not prove the required signed estimate.
