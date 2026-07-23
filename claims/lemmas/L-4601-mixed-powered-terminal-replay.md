# L-4601 — Exact replay of mixed separate and powered Robin terminals

Claim ID: L-4601  
Title: A mixed terminal stream with exact powered tokens certifies a bounded canonical Robin forest  
Status: PROPOSED  
Authoring agent: `gpt56-03-d`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-2501; L-2502; L-3501; L-3502; exact dyadic Robin lower enclosures  
Scope: finite consecutive-prime, nonincreasing-exponent trees under an exact integer bound  
Related counterexample candidates: Robin finite witnesses

## Statement

Fix an integer bound `B>5040`. For every support size `K` whose primorial does
not exceed `B`, let

\[
 \mathcal F_K(B)=\left\{(a_1,\ldots,a_K):
 a_1\ge\cdots\ge a_K\ge1,
 \quad \prod_{i=1}^K p_i^{a_i}\le B\right\}.
\]

Traverse the prefix tree of `mathcal F_K(B)` in deterministic depth-first order,
with child exponents listed in decreasing order. At a prefix

\[
 \alpha=(a_1,\ldots,a_j),\qquad 0<j<K,
\]

put

\[
 P_\alpha=\prod_{i=1}^j p_i^{a_i},
 \qquad
 N_{\min}(\alpha)=P_\alpha\prod_{i=j+1}^Kp_i.
\]

A **mixed terminal stream** may terminate the subtree at `alpha` with either of
the following tokens.

1. A separate token `P:alpha`, provided the exact L-2502 ceiling
   `U_sep(alpha)` and an outward dyadic lower endpoint `L_alpha` satisfy
   \[
      U_{\rm sep}(\alpha)<L_\alpha
      \le e^\gamma\log\log N_{\min}(\alpha).
   \]
2. A powered token `J:a,d:alpha`, where `a>=0`, `d>=1`, provided the exact
   L-3502 powered ceiling `U_joint^(d)(alpha;a,d)` satisfies
   \[
      U_{\rm joint}^{(d)}(\alpha;a,d)<L_\alpha^d.
   \]

At a full leaf `alpha=(a_1,...,a_K)`, let `n_alpha=prod p_i^{a_i}` and
`I_alpha=sigma(n_alpha)/n_alpha`. The stream must record exactly one of:

- `B:alpha` if `n_alpha<=5040`;
- `S:alpha` if an outward dyadic lower endpoint proves
  `I_alpha<e^gamma log log(n_alpha)`;
- `U:alpha` if the interval comparison is unresolved;
- `V:alpha` if an outward dyadic upper endpoint proves
  `I_alpha>=e^gamma log log(n_alpha)`.

Assume a verifier independently reconstructs:

- the exact support limit and all primes;
- every exact child range in the finite canonical tree;
- every integer, prime-power abundancy, exponent cap, and separate ceiling;
- every powered level weight and backward rational maximum;
- every outward dyadic Robin interval;
- and the identity and order of every terminal token.

Assume further that, for each support, recursive replay consumes the stream
exactly, with no missing or extra token. Then:

1. every element of `mathcal F_K(B)` belongs to exactly one verified terminal
   subtree or verified leaf;
2. a `P` or `J` token proves Robin's strict inequality for every completion of
   its prefix;
3. if no `U` or `V` leaf occurs for any support, every canonical integer
   `n` with `5041<=n<=B` satisfies Robin's strict inequality.

For quantitative tracking, attach to every strict terminal a rational upper
bound `c_tau<1` for

\[
 \frac{\sigma(n)}{e^\gamma n\log\log n}
\]

throughout that terminal. For a powered terminal one may take the outward
dyadic upper endpoint of

\[
 \left(
 \frac{U_{\rm joint}^{(d)}}{L_\alpha^d}
 \right)^{1/d}.
\]

Then

\[
 C=\max_\tau c_\tau<1
\]

is a valid normalized-quotient upper bound for the complete finite canonical
forest.

## Definitions

A terminal stream is **exactly replayed** when the verifier performs the tree
recursion itself. At an internal prefix it may consume a token only if the token
names that exact prefix. If no valid internal token is present, it visits every
licensed child. At a leaf it consumes one token naming that exact leaf. The
stream must be exhausted at the end of the support.

The powered root upper endpoint is computed without a floating root. Given a
positive rational `q<1`, a power `d>=1`, and a dyadic denominator `2^b`, choose
the least integer `m` satisfying

\[
 m^d\operatorname{den}(q)
 \ge
 \operatorname{num}(q)2^{bd}.
\]

Then `m/2^b >= q^(1/d)` exactly.

## Motivation

PR #34 used one terminal code for the separate-cap ceiling. PR #40 introduced a
strictly stronger exact shared-budget envelope, but only in a synthetic local
checker. Production integration requires a compact token that licenses the
powered theorem without trusting a supplied dynamic-program table or a
floating optimizer.

The mixed stream preserves the original fail-safe behavior: an unsupported
powered attempt does not remove a node. It merely causes ordinary traversal to
continue.

## Proof

Fix a support `K`. We prove coverage and correctness by structural induction on
the finite prefix tree.

At a leaf, exact token identity gives one and only one classification. A `B`
leaf is outside Robin's domain. For an `S` leaf, the verifier reconstructs
`I_alpha` exactly and a rigorous lower endpoint for the Robin right-hand side,
so the strict inequality holds. The meanings of `U` and `V` are likewise fixed
by the reconstructed interval comparison.

Now consider an internal prefix `alpha`. If the next token names `alpha`, the
replay rules allow only `P` or `J`.

- For `P`, L-2502 bounds the abundancy of every completion by
  `U_sep(alpha)`. Every completion is at least `N_min(alpha)`, while
  `e^gamma log log x` is increasing for `x>1`. Thus
  \[
     \frac{\sigma(n)}n
     \le U_{\rm sep}(\alpha)
     <L_\alpha
     \le e^\gamma\log\log N_{\min}(\alpha)
     \le e^\gamma\log\log n.
  \]

- For `J`, L-3502 gives
  \[
     \left(\frac{\sigma(n)}n\right)^d
     \le U_{\rm joint}^{(d)}(\alpha;a,d)
     <L_\alpha^d.
  \]
  All quantities are positive, so strict monotonicity of `x -> x^d` gives
  `sigma(n)/n<L_alpha`. The same monotonicity in `n` completes the Robin
  inequality.

If no internal token names `alpha`, exact child-range reconstruction partitions
all completions of `alpha` into its children. The induction hypothesis applies
to every child. Hence the subtree is completely covered.

Starting at the root proves that every element of `mathcal F_K(B)` is covered
exactly once. Exhaustion of the stream rules out extra or duplicated terminals.
Repeating over every exact support `1<=K<=K_B` proves the canonical statement.
If no `U` or `V` occurs, every in-domain leaf and every pruned subtree is
strictly safe.

For the quantitative assertion, each completion belongs to one strict terminal
`tau` and its normalized quotient is at most `c_tau`. Taking the maximum over
the finite terminal set proves the bound `C`. The powered dyadic root rule is an
exact ceiling by its defining integer inequality. ∎

## Analytic domain audit

The tree and powered-envelope layers use finite integer and rational arithmetic.
The only analytic quantity is the real function
`e^gamma log log x`, evaluated for integers `x>=3`. Its monotonicity is used on
`x>1`. Every machine comparison must use an outward interval; no complex
branch, contour, zero sum, or analytic continuation occurs.

## Dependency audit

- L-2501 gives the exact finite child ranges and support limit.
- L-2502 gives the separate ceiling.
- L-3501 and L-3502 give the level encoding and exact powered ceiling.
- The dyadic logarithm, Euler-constant, and exponential enclosures provide
  `L_alpha`.
- No assertion about the truth of RH is used in the finite tree proof.

## Gap audit

- A floating ranking of dual pairs cannot authorize a `J` token.
- A supplied dynamic-program value is not trusted; every rational candidate is
  recomputed and compared.
- The prefix named by a terminal must equal the verifier's current prefix.
- Missing, duplicated, reordered, malformed, or extra tokens invalidate
  coverage.
- A powered inequality touching equality does not license a strict prune.
- The dyadic root is used only for a quantitative display; pruning itself is
  checked in exact `d`-th powers.
- The result covers only `n<=B` and says nothing about larger integers.

## Adversarial tests

1. Delete or reorder one terminal and require replay failure.
2. Change the `(a,d)` pair of a powered token and require exact rejection.
3. Change a claimed quantitative summary while refreshing the outer digest and
   require reconstruction to reject it.
4. Replay a strong stream with deliberately weak dyadic parameters and require
   fail-closed behavior.
5. Exhaust small canonical boxes and check that every vector belongs to exactly
   one terminal.
6. Exhaust small shared-budget tails and verify every actual abundancy is below
   the powered bound.

## Remaining uncertainty

No mathematical gap is known in the composition argument. The production
implementation and the common dyadic transcendental kernel still require
independent code review and an independently implemented numerical backend.

## Suggested next attack

Reproduce the mixed terminal stream with a second language and Arb, MPFI, or
another directed library. The second verifier should reconstruct the tree and
the powered recurrence without importing the Python implementation.
