# T-2001 — Independent certified Robin finite barrier

Claim ID: T-2001  
Title: Independent exact and dyadic reproduction of the finite barrier supporting T-0201  
Status: PROPOSED  
Authoring agent: `gpt56-03-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-0201; L-2001; L-2002; L-2003; X-2001  
Scope: the finite arithmetic and transcendental dependencies of T-0201  
Related counterexample candidates: Robin finite witnesses

## Statement

The following facts hold.

1. The unique maximum of `sigma(n)/n` on `1<=n<=5040` is
   \[
   \frac{\sigma(5040)}{5040}=\frac{403}{105}.
   \]
2. The unique maximum on `5041<=n<=5582` is
   \[
   \frac{\sigma(5460)}{5460}=\frac{224}{65}.
   \]
3. Independent pure-integer dyadic interval arithmetic proves
   \[
   e^\gamma\log\log 5041-\frac{224}{65}>0,
   \]
   \[
   e^\gamma\log\log 5582-\frac{403}{105}<0,
   \]
   and
   \[
   e^\gamma\log\log 5583-\frac{403}{105}>0.
   \]

At the default X-2001 parameters, outward decimal displays of the three difference intervals are respectively

\[
[0.3707648895613142215315093910947055389933,\ 
 0.3707648895632226789909099889961613192659],
\]

\[
[-0.0000055149237443332647249936878115278188,\ 
 -0.0000055149218252903221817095893733053537],
\]

and

\[
[0.0000314656221012828714935658997537077145,\ 
 0.0000314656240203443042912825564500448094].
\]

Consequently:

- no Robin counterexample lies in `[5041,5582]`;
- `5583` is the least integer at which the increasing function
  `e^gamma log log n` exceeds `403/105`;
- every Robin counterexample yields a superabundant Robin counterexample greater than `5040`, as asserted by the finite part of T-0201.

## Definitions

The exact computation and full endpoint integers are stored under
`experiments/X-2001-independent-robin-barrier/`. A **certified strict sign** means that the exact dyadic interval lies wholly on one side of zero; the displayed decimals are outward-rounded summaries only.

## Motivation

T-0201 is the active project's strongest completeness reduction for the Robin path, but its two transcendental signs originally shared the X-0201 Decimal engine. Issue #20 requested a truly independent reproduction. This theorem records that reproduction and strengthens it with the adjacent `5582` sign.

## Proof or construction

### Exact finite maxima

For each integer `n` from `1` through `5582`, X-2001 performs direct trial division. Once

\[
 n=\prod p^{a_p}
\]

is obtained, it computes

\[
 \sigma(n)=\prod_p\frac{p^{a_p+1}-1}{p-1}
\]

using exact integers. Ratios are never divided numerically: candidates
`sigma(n)/n` and `sigma(m)/m` are compared by the sign of the exact integer

\[
 \sigma(n)m-\sigma(m)n.
\]

The factorization loop is exhaustive because it tests every possible prime divisor up to the square root of the current remainder; any final remainder greater than one is prime. The product formula enumerates every divisor by independently choosing a prime-power exponent. Thus the finite loop checks every integer in the two stated ranges without omission.

The unique maxima emitted are

\[
 5040=2^4 3^2 5\,7,
 \qquad
 \sigma(5040)=31\cdot13\cdot6\cdot8=19344,
\]

so `19344/5040=403/105`, and

\[
 5460=2^2 3\,5\,7\,13,
 \qquad
 \sigma(5460)=7\cdot4\cdot6\cdot8\cdot14=18816,
\]

so `18816/5460=224/65`. A separate divisor-addition sieve in the test suite agrees with the factorization result for every `n<=5582`. The exact sequence digest is

```text
4c71bb8b5a918d581f025405a84b026eb07045b0d1560150096616d201bc31a0
```

under the canonical serialization `n:sigma(n)\n`.

### Independent transcendental enclosures

L-2001 encloses every logarithm by a positive atanh series and an explicit rational tail. L-2002 encloses `gamma` between harmonic-number expressions. L-2003 encloses the exponential by a positive Taylor polynomial and a geometric tail. X-2001 implements all operations with integer endpoints over the common denominator `2^B`; no binary floating-point or Decimal transcendental operation is called.

With `B=320`, `96` log and exponential terms, and harmonic cutoff `10^6`, the exact endpoint integers give the three disjoint sign intervals displayed in the statement. The enclosures at `5041` and `5583` are strictly contained in the much wider committed X-0202 intervals after those decimal endpoints are parsed exactly as rational numbers. Three escalating parameter sets reproduce the same signs; a deliberately weak control configuration is rejected rather than accepted with inadequate refinement.

### Logical consequences

For `5041<=n<=5582`, the exact finite maximum and monotonicity give

\[
 \frac{\sigma(n)}n\le\frac{224}{65}
 <e^\gamma\log\log5041
 \le e^\gamma\log\log n.
\]

Hence the entire window satisfies Robin's strict inequality.

The function `e^gamma log log x` is strictly increasing for `x>1`. Its certified difference from `403/105` is negative at `5582` and positive at the adjacent integer `5583`; therefore `5583` is the least integer crossing.

Finally, suppose `n` is a Robin counterexample. The finite window forces `n>=5583`. Let `m<=n` be the least integer attaining the maximum of `sigma(k)/k` on `1<=k<=n`. Then

\[
 \frac{\sigma(m)}m\ge e^\gamma\log\log n
 \ge e^\gamma\log\log5583
 >\frac{403}{105}.
\]

Every `k<=5040` has abundancy at most `403/105`, so `m>5040`. L-0201 proves that this least record maximizer is superabundant and itself violates Robin's inequality. ∎

## Analytic domain audit

All logarithms and exponentials are real. Their arguments are positive, and `log n>0` for every evaluated `n`. No zeta function, analytic continuation, zero, pole, contour, or branch choice occurs.

## Dependency audit

- L-0201 supplies only the elementary least-record-maximizer step.
- L-2001--L-2003 justify every transcendental enclosure.
- X-2001 performs the exact finite enumeration and directed arithmetic.
- Robin's 1984 equivalence is not needed for this finite theorem; it is needed only to turn a Robin violation into falsity of RH.

## Gap audit

- The result verifies the finite dependency of T-0201; it does not independently reconstruct Robin's original equivalence theorem.
- The source code is compact and exact but still requires human or formal code review before repository promotion.
- The hash is a reproduction aid, not a substitute for rerunning or auditing the computation.
- No conclusion about the smaller colossally abundant subsequence follows.

## Adversarial tests

- Recompute all divisor sums by a divisor-addition sieve; the committed tests do this for the whole range.
- Run at 256, 320, and 384 bits with distinct cutoffs and series lengths.
- Confirm the weak 192-bit control is rejected because its interval is not contained in X-0202.
- Check `5040`, `5041`, `5582`, and `5583` separately.
- Parse X-0202 endpoints as exact fractions and prove interval containment by integer cross multiplication.

## Remaining uncertainty

No discrepancy was found. Repository status remains `PROPOSED` until another reviewer audits the proof and code. Full promotion of T-0201 also depends on the project's source-status policy for Robin's theorem.

## Suggested next attack

Adopt the finite barrier, then use T-2002 and L-2004 to build a proof-producing canonical exponent-vector search rather than extending only the empirical colossally abundant spine.
