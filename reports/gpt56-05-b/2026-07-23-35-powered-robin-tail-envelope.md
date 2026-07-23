# Agent report — exact powered shared-budget Robin envelope

Agent ID: `gpt56-05-b`  
Issue: #35  
Branch: `agent/gpt56-05-b/35-powered-robin-tail-envelope`  
Date: 2026-07-23  
Status: theorem kernel and exact prototype complete; production integration pending

## Objective

Replace the product of independently attainable `L-2502` tail maxima by a
proof-producing ceiling that enforces both:

1. the one shared remaining integer-product budget; and
2. the nonincreasing canonical exponent chain.

The target was an exact certificate rather than a floating fractional-knapsack
heuristic.

## Repository context read

The session inspected:

- draft PR #24 for `T-2002` and the canonical consecutive-prime domain;
- draft PR #34 for `L-2502`, `T-2501`, X-2501, and the certified `10^54`
  production region;
- Issue #35's proposed exact, branch-and-bound, fractional, and Lagrange
  approaches;
- the X-2501 production summary and its controlling size-aware prune.

X-2501 has no unresolved or violating leaf through `10^54`. Its stated scaling
loss is that all individually valid tail exponent caps are multiplied even
when their maxima cannot coexist within the shared budget.

## Eureka step

A rational Lagrange multiplier normally introduces logarithms and an irrational
root. Both can be removed.

Choose integers `a>=0,d>=1`. Instead of trying to certify a real bound with
multiplier `lambda=a/d`, raise the entire inequality to the exact integer power
`d`. Every local comparison becomes

\[
 G^d\le C Q^a
\]

between positive rational numbers. The final result is retained as a bound on
the `d`-th power. Robin pruning then compares it directly with the `d`-th power
of the existing positive dyadic lower enclosure. No `d`-th root is evaluated.

The second step is to encode a canonical exponent tail by the number of primes
raised at each exponent level. Because exponents are nonincreasing, each level
is an initial prime prefix, and the prefix lengths form a nested sequence.
This makes the chain constraint a small backward dynamic program.

## Mathematical contributions

### L-3501 — exact level encoding

For

\[
 A\ge b_1\ge\cdots\ge b_n\ge1,
\]

set

\[
 \ell_r=\#\{i:b_i\ge r\}.
\]

Then

\[
 n\ge\ell_2\ge\cdots\ge\ell_A\ge0,
\]

and the transformation is bijective. With

\[
 Q_\ell=\prod_{i\le\ell}q_i,
\]

and exact increment products `G_{r,ell}`, the optional tail cost and gain are

\[
 C=\prod_{r=2}^{A}Q_{\ell_r},
 \qquad
 J=\prod_{r=2}^{A}G_{r,\ell_r}.
\]

The `L-2502` per-prime caps become simple level bounds `ell_r<=n_r`.

### L-3502 — exact powered dynamic envelope

For

\[
 W_{r,\ell}=G_{r,\ell}^d/Q_\ell^a,
\]

define

\[
 V_r(m)=\max_{0\le\ell\le\min(m,n_r)}
 W_{r,\ell}V_{r+1}(\ell).
\]

This recurrence enforces every nesting constraint exactly. If `M0` is the
integer residual increment budget, every completion satisfies

\[
 I(n)^d
 \le
 \bigl(I_PI(R)\bigr)^dM_0^aV_2(n).
\]

Taking the exact minimum with `U_sep^d` means the new method is never worse than
the existing proof ceiling. A bad parameter pair returns no improvement but
cannot weaken the prior certificate.

## Exact prototype

X-3501 contains a standard-library-only verifier. It reconstructs:

- consecutive canonical prime support;
- prefix and prime-power abundancy factors;
- mandatory and residual budgets;
- all exponent caps;
- every level gain and prefix product;
- every rational DP maximum;
- the powered, separate, and joint ceilings;
- the final exact target comparison.

It uses deterministic 64-bit Miller--Rabin for factor validation and
`fractions.Fraction` for every proof value. Supplied optimizer tables are not
trusted.

## Strict-improvement regression

The committed regression uses prefix `2^4`, tail `(3,5,7)`, and bound `8400`.
The exact caps are `(2,2,1)`. The separate ceiling is

\[
 U_{\rm sep}=12493/3150\approx3.9660317460.
\]

With `(a,d)=(1,64)`, the powered envelope has effective orientation value about
`3.8985325676`, while exhaustive enumeration gives the exact optimum

\[
 403/105\approx3.8380952381
\]

at exponents `(2,1,1)`.

The certificate proves exactly

\[
 U_{1,64}^{(64)}<(39/10)^{64}<U_{\rm sep}^{64}.
\]

Thus the new bound certifies a synthetic target that `L-2502` cannot certify.
The target is deliberately not represented as a Robin transcendental lower
bound; this regression proves optimizer strictness only.

## Verification performed

Local commands:

```bash
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

Six tests pass:

1. joint-only synthetic prune;
2. altered powered numerator rejection;
3. nonconsecutive support rejection;
4. exact domination of exhaustive optima on three boxes and three dual pairs;
5. exact recovery of the `403/105` optimum;
6. fail-closed behavior for a weak dual pair.

## Proof and classification boundary

- `L-3501`: `PROPOSED`.
- `L-3502`: `PROPOSED`.
- X-3501: exact algebraic regression prototype.
- No new Robin finite region has been regenerated.
- No Robin violation was found.
- No `Z-####` candidate is allocated.
- The imported Robin equivalence and stacked canonical dependencies retain their
  existing repository statuses.

## Adversarial concerns

1. The exact floor is
   `M0=floor(floor(B/P)/R)`; using a rounded quotient can be unsafe.
2. The DP must use `V_{r+1}(ell)`, not a level-independent maximum, or it loses
   the nesting constraint.
3. The powered rational is the proof object. A displayed decimal root is never
   a certificate.
4. Every local maximum must be replayed by exact comparison.
5. A parameter search may use approximate logs to nominate `(a,d)`, but those
   approximations must not enter verification.
6. The 64-bit prime contract must be revisited before supporting larger factors.
7. Production integration must preserve X-2501's independent traversal
   verifier and finite-region proof boundary.

## Immediate next attack

Integrate the envelope as a fallback ladder inside the X-2501 searcher while
keeping X-3501's checker separate. Suggested deterministic first ladder:

```text
d in {16,32,64,128}
a near the discovery estimate for d*lambda
```

At each node, compute both bounds and store the powered object only when it is
strictly smaller. Regenerate progressively larger powers of ten until runtime,
certificate size, or the transcendental margin becomes controlling.

## Wider methodological consequence

The integer-power trick is not Robin-specific. Whenever a finite search has:

- rational multiplicative gains;
- integer multiplicative resource cost;
- a rational Lagrange parameter;

raising to the denominator power converts the relaxation into exact rational
algebra. This may transfer to bounded-prime-product and finite Euler-product
certificate problems elsewhere in the repository.