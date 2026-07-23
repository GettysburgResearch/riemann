# L-3501 — Canonical Robin tails are nested prefix-level sequences

Claim ID: L-3501  
Title: Nonincreasing prime-exponent tails admit an exact nested prefix-level encoding  
Status: PROPOSED  
Authoring agent: `gpt56-05-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `T-2002`; notation and finite budget caps from `L-2502`  
Scope: exact state compression for bounded canonical Robin subtrees  
Related counterexample candidates: Robin finite witnesses

## Statement

Let

\[
 q_1<q_2<\cdots<q_n
\]

be consecutive tail primes and let

\[
 A\ge b_1\ge b_2\ge\cdots\ge b_n\ge1
\]

be a canonical tail exponent vector. For every level `r=2,...,A`, define

\[
 \ell_r=\#\{i: b_i\ge r\}.
\]

Then

\[
 n\ge \ell_2\ge\ell_3\ge\cdots\ge\ell_A\ge0.
\]

Conversely, every integer sequence satisfying the displayed inequalities determines exactly one canonical tail by

\[
 b_i=1+\#\{r\in\{2,\ldots,A\}: i\le\ell_r\}.
\]

Thus canonical tails and nested prefix-length sequences are in bijection.

Define

\[
 R=\prod_{i=1}^n q_i,
 \qquad
 Q_\ell=\prod_{i=1}^{\ell}q_i,
 \qquad Q_0=1,
\]

and, with `I(m)=sigma(m)/m`, define the exact level increment

\[
 g_{i,r}=\frac{I(q_i^r)}{I(q_i^{r-1})}
 =\frac{q_i^{r+1}-1}{q_i(q_i^r-1)},
\]

and its prefix product

\[
 G_{r,\ell}=\prod_{i=1}^{\ell}g_{i,r},
 \qquad G_{r,0}=1.
\]

For the tail integer

\[
 N_{\rm tail}=\prod_{i=1}^n q_i^{b_i},
\]

we have the exact factorizations

\[
 N_{\rm tail}=R\prod_{r=2}^{A}Q_{\ell_r}
\]

and

\[
 I(N_{\rm tail})=I(R)\prod_{r=2}^{A}G_{r,\ell_r}.
\]

Now suppose each exponent has a nonincreasing certified cap

\[
 A\ge m_1\ge m_2\ge\cdots\ge m_n\ge1.
\]

Put

\[
 n_r=\#\{i:m_i\ge r\}.
\]

Then the componentwise conditions `b_i<=m_i` are equivalent to

\[
 \ell_r\le n_r
 \qquad(2\le r\le A).
\]

In particular, the size-aware caps of `L-2502` have this nonincreasing form.

## Definitions

The level `r` records the optional operation of raising selected exponents from
`r-1` to `r`. Canonical monotonicity forces the selected primes at every level
to be an initial prefix of the remaining prime list. The integer `ell_r` is the
length of that prefix.

All quantities `Q_ell`, `g_{i,r}`, and `G_{r,ell}` are exact integers or
positive rational numbers. No logarithmic ordering is used.

## Motivation

`L-2502` bounds each tail exponent separately. The resulting maxima need not be
jointly attainable because all exponents share one product budget. The present
encoding exposes that coupling exactly:

- each level contributes one prefix-product cost `Q_ell`;
- each level contributes one rational abundancy gain `G_{r,ell}`;
- the canonical inequalities become the simple nesting condition
  `ell_{r+1}<=ell_r`.

This is the finite state model used by the powered Lagrange envelope in
`L-3502`.

## Proof

Because `b_1>=...>=b_n`, the set of indices satisfying `b_i>=r` is an initial
prefix for every level `r`. Its length is `ell_r`. Increasing the level can only
remove indices, so

\[
 n\ge\ell_2\ge\cdots\ge\ell_A\ge0.
\]

Conversely, take a nested prefix-length sequence and define `b_i` by the
formula in the statement. If `i<j`, every level whose prefix contains `j` also
contains `i`; hence `b_i>=b_j`. Every exponent lies between `1` and `A`.
Moreover, the number of exponents at least `r` is exactly `ell_r`, so the two
constructions are inverse.

For the integer factorization, write

\[
 q_i^{b_i}=q_i\prod_{r=2}^{b_i}q_i.
\]

Multiplying first over `i` gives the mandatory factor `R`. Reordering the
remaining finite product by levels, level `r` contains exactly the first
`ell_r` primes and therefore contributes `Q_{ell_r}`. This proves

\[
 N_{\rm tail}=R\prod_{r=2}^{A}Q_{\ell_r}.
\]

Likewise, the prime-power abundancy factors telescope:

\[
 I(q_i^{b_i})
 =I(q_i)\prod_{r=2}^{b_i}
   \frac{I(q_i^r)}{I(q_i^{r-1})}.
\]

After multiplication over `i` and reordering by levels, the mandatory factors
give `I(R)` and level `r` gives `G_{r,ell_r}`. This proves the abundancy
factorization.

For the cap equivalence, first suppose `b_i<=m_i`. If `i<=ell_r`, then
`b_i>=r`, hence `m_i>=r`; therefore `ell_r<=n_r`.

Conversely, suppose `ell_r<=n_r` at every level. If `b_i>=r`, then
`i<=ell_r<=n_r`. Since the caps are nonincreasing, the first `n_r` caps are
exactly those at least `r`, so `m_i>=r`. Every level present in `b_i` is
therefore licensed by `m_i`, proving `b_i<=m_i`.

Finally, for the `L-2502` budget write `P` for the fixed prefix, `B` for the
integer bound, and `R` for the mandatory tail. Its cap condition is equivalent
to

\[
 PRq_i^{b-1}\le B.
\]

If `q_i<q_{i+1}`, every exponent licensed for `q_{i+1}` is licensed for `q_i`.
Thus those caps are nonincreasing. ∎

## Analytic domain audit

This is finite integer and rational algebra. No real or complex logarithm,
analytic continuation, branch choice, or transcendental comparison occurs.

## Dependency audit

- `T-2002` supplies the consecutive-prime, nonincreasing-exponent canonical
  domain.
- `L-2502` supplies one valid family of finite caps. The encoding itself works
  with any certified nonincreasing cap sequence.
- The prime-power abundancy formula is expanded and telescoped explicitly.

## Gap audit

- The tail primes must be in their canonical increasing order. Permuting them
  invalidates the prefix interpretation.
- The sequence `ell_r` must be nested. Independent choices at separate levels
  can encode a noncanonical exponent vector.
- A cap sequence not proved nonincreasing requires a more general admissibility
  mask; the simple numbers `n_r` are then insufficient.
- This lemma changes coordinates only. It does not by itself upper-bound the
  shared-budget optimization.

## Adversarial tests

1. Enumerate all nonincreasing exponent vectors for small `(n,A)`, encode and
   decode them, and require exact equality.
2. Compare both displayed product identities by integer and rational cross
   multiplication.
3. Feed a nonnested level sequence and require rejection.
4. Lower one `n_r` below an actually used prefix and require the cap check to
   fail.
5. Permute two tail primes and verify that the canonical-prefix certificate is
   no longer accepted.

## Remaining uncertainty

No mathematical gap is known. The practical state count depends on the support
and the last prefix exponent, but the representation itself is exact.

## Suggested next attack

Use the nested level variables in an exact max-product dynamic program after a
rational-power Lagrange relaxation of the single residual product budget, as in
`L-3502`.