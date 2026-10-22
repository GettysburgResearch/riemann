# L-3103 — Finite-exponent-capped Robin subtree ceiling

Claim ID: L-3103  
Title: Canonical exponent caps give a strictly sharper exact Robin subtree ceiling  
Status: PROPOSED  
Authoring agent: `gpt56-05`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: T-2002 and L-2004  
Scope: proof-producing branch-and-bound over canonical Robin exponent vectors  
Related counterexample candidates: Robin finite witnesses

## Statement

Let `p_1<...<p_K` be the first `K` primes. Fix `1<=j<K` and a canonical prefix

\[
 a_1\ge\cdots\ge a_j\ge1.
\]

Consider every completion

\[
 n=\prod_{i=1}^Kp_i^{b_i},
 \qquad b_i=a_i\ (i\le j),
 \qquad a_j\ge b_{j+1}\ge\cdots\ge b_K\ge1.
\]

Define the same minimum completion size as in L-2004,

\[
 N_{\min}=\left(\prod_{i\le j}p_i^{a_i}\right)
           \left(\prod_{i>j}p_i\right),
\]

but replace the infinite-geometric abundancy ceiling by

\[
 U_{\mathrm{cap}}=
 \left(\prod_{i\le j}\frac{\sigma(p_i^{a_i})}{p_i^{a_i}}\right)
 \left(\prod_{i>j}\frac{\sigma(p_i^{a_j})}{p_i^{a_j}}\right).
\]

Then every completion satisfies

\[
 n\ge N_{\min},
 \qquad
 \frac{\sigma(n)}n\le U_{\mathrm{cap}}.
\]

Moreover, if `U_infty` denotes the L-2004 ceiling, then

\[
 U_{\mathrm{cap}}
 =U_{\infty}\prod_{i>j}\left(1-p_i^{-(a_j+1)}\right)
 <U_{\infty}.
\]

Therefore, if `N_min>e` and a rigorous comparison proves

\[
 U_{\mathrm{cap}}<e^\gamma\log\log N_{\min},
\]

then every completion satisfies Robin's strict inequality and the entire
subtree may be discarded.

More generally, if safe coordinatewise upper bounds `b_i<=c_i` are known for
`i>j`, then

\[
 U(c)=
 \left(\prod_{i\le j}\frac{\sigma(p_i^{a_i})}{p_i^{a_i}}\right)
 \left(\prod_{i>j}\frac{\sigma(p_i^{c_i})}{p_i^{c_i}}\right)
\]

is a valid exact rational ceiling. The inherited canonical cap corresponds to
`c_i=a_j`.

## Motivation

L-2004 safely replaces every unspecified prime-power factor by the infinite
geometric limit `p/(p-1)`. In the canonical tree of T-2002, however, every
remaining exponent is already bounded above by the last chosen exponent. Using
that finite cap costs essentially nothing and can materially increase the
number of certifiably pruned nodes.

## Proof

For fixed prime `p`, the prime-power abundancy factor is

\[
 A_p(b)=\frac{\sigma(p^b)}{p^b}=\sum_{r=0}^{b}p^{-r}.
\]

It is increasing in the integer exponent `b`. Since every remaining exponent
satisfies `b_i<=a_j`,

\[
 \frac{\sigma(p_i^{b_i})}{p_i^{b_i}}
 \le\frac{\sigma(p_i^{a_j})}{p_i^{a_j}}.
\]

Multiplicativity of `sigma(n)/n` gives the stated ceiling. The size floor is
unchanged from L-2004 because every remaining exponent is at least one.

The finite geometric identity gives

\[
 \frac{\sigma(p^a)}{p^a}
 =\frac{1-p^{-(a+1)}}{1-p^{-1}}
 =\frac{p}{p-1}\left(1-p^{-(a+1)}\right).
\]

Multiplying this identity over `i>j` proves the exact relation to `U_infty` and
its strict improvement.

Finally, `log log x` is increasing for `x>1`. Hence every completion obeys

\[
 \frac{\sigma(n)}n
 \le U_{\mathrm{cap}}
 <e^\gamma\log\log N_{\min}
 \le e^\gamma\log\log n,
\]

which is Robin's strict inequality. The coordinatewise-cap variant is the same
argument with `a_j` replaced by `c_i` for each suffix coordinate. ∎

## Analytic domain audit

All products are positive rationals. The only transcendental comparison uses
the increasing real function `log log x`; the pruning statement assumes
`N_min>e`.

## Dependency audit

T-2002 supplies completeness of the canonical consecutive-prime,
nonincreasing-exponent search domain. L-2004 supplies the existing size-floor
logic and the comparison pattern. This lemma only sharpens its rational upper
bound.

## Gap audit

- The inherited cap is available only after at least one prefix exponent has
  been chosen; a root node needs another proved cap or the L-2004 ceiling.
- Coordinatewise caps must be logically implied by the branch constraints, not
  guessed from empirical exponent patterns.
- Equality in the abundancy ceiling is possible when every remaining exponent
  equals its cap, so the first comparison is non-strict.
- Directed rounding is still required for the final comparison with
  `e^gamma log log N_min`.
- This remains fixed-support pruning; traversal across all support sizes still
  needs a complete strategy.

## Adversarial tests

1. Exhaustively enumerate all completions for small `(K,j,a_j)` and verify that
   none exceeds `U_cap`.
2. Compare `U_cap/U_infty` with the exact product
   `prod_{i>j}(1-p_i^{-(a_j+1)})`.
3. Use a noncanonical completion with some `b_i>a_j`; the lemma must reject its
   application.
4. Check the smallest cap `a_j=1`, where each suffix factor is exactly `1+1/p`
   rather than `p/(p-1)`.

## Remaining uncertainty

No mathematical gap is known. The empirical pruning gain at the support sizes
relevant to Issue #25 has not yet been measured.

## Suggested next attack

Replace the L-2004 ceiling by `min(U_infty,U_cap)` in the proof-producing
branch-and-bound implementation, store the exact finite factors in each prune
certificate, and benchmark the reduction in visited nodes.
