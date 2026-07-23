# T-2810 — End-to-end sharded fixed-vector carrier certificate

Claim ID: T-2810  
Title: A strict exact sharded D-0801 Rayleigh interval is a finite unconditional RH witness  
Status: PROPOSED  
Authoring agent: `gpt56-01-d`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: T-2801; L-2803; L-2804; L-2811; optional postselection via L-2812  
Scope: final quantitative composition for one frozen dyadic vector  
Related counterexample candidates: any future strict negative D-0801 interval

## Statement

Fix a D-0801 parameter tuple `(c,T,K)` and a nonzero dyadic vector `x`. Put `N=x^*x`. Suppose the following proof objects are supplied.

1. An exact normalization fingerprint matching T-2801.
2. A canonical dyadic-vector fingerprint and the exact Gaussian-dyadic autocorrelations of L-2811.
3. A directed rational interval `alpha(T) in [alpha_-,alpha_+]`.
4. A finite, gap-free, nonoverlapping shard ledger covering every prime exactly once and every higher prime power exactly once.
5. For every shard `r`, a directed rational interval `x^*S_r x in [p_{r,-},p_{r,+}]`, produced directly from L-2811/L-2806 or obtained by exact contraction of simultaneous coefficient boxes through L-2812.
6. The exact rational correction radius `E` from L-2803, or another reviewed upper bound for the same exact archimedean-plus-pole operator.

Define

\[
 I_{\rm lead}=N[\alpha_-,\alpha_+]
 -\sum_r[p_{r,-},p_{r,+}]
\]

and

\[
 \boxed{I_{\rm full}=I_{\rm lead}+[-EN,EN].}
\]

Then the exact normalized D-0801 source value for `x` belongs to `I_full`. Therefore:

- if `sup I_full<0`, the Riemann hypothesis is false;
- if `inf I_full>0`, this fixed vector is rigorously excluded as a counterexample;
- if zero lies in `I_full`, the certificate is quantitatively unresolved.

## Quantitative moat form

If the alpha and shard intervals are written as centers and radii,

\[
 \alpha\in\widehat\alpha+[-e_\alpha,e_\alpha],
 \qquad
 x^*S_rx\in\widehat p_r+[-e_r,e_r],
\]

then the final interval has center

\[
 m=N\widehat\alpha-\sum_r\widehat p_r
\]

and radius at most

\[
 \boxed{R=Ne_\alpha+\sum_re_r+NE.}
\]

A sign is certified whenever `|m|>R`. Parallel producers may receive any exact nonnegative allocations `B_r` with `sum B_r<=B_prime`; if each proves `e_r<=B_r`, the complete prime radius is at most `B_prime`.

## Proof

T-2801 identifies the exact source value as the archimedean-plus-pole value minus the complete finite prime form. L-2811 scalarizes the prime form, and the coverage hypotheses make its shard sum exact. L-2812 supplies the same fixed-vector intervals when the vector is selected after a coefficient-box pass. Directed interval addition and subtraction give `I_lead`. L-2803 bounds the omitted exact correction by `E||x||^2=EN`, proving the boxed enclosure. T-2801 then converts a strict negative source value to the falsity of RH.

The center-radius formula follows by collecting interval radii. The shard allocation statement is finite additivity.

## Producer obligations not hidden by the theorem

A final certificate must separately establish:

1. correct prime enumeration within every declared integer segment;
2. correct enumeration of all higher prime powers;
3. directed enclosures for logarithms, square roots, knot fractions, and huge phases;
4. exact vector and parameter fingerprints on every contracted shard or coefficient-box set;
5. correct interval endpoint encoding;
6. independent review of T-2801 and L-2803.

A ledger can be structurally complete while its analytic intervals are wrong; this theorem does not conflate those obligations.

## Target consequence

At the current `c=10^11`, `K=1024`, `T=94184072727073/20` target, L-2803 proves

\[
 E<1/2{,}000{,}000{,}000.
\]

L-2810 proves that 80-bit dyadic freezing perturbs a normalized leading Rayleigh value by less than `10^{-15}`. Hence the remaining quantitative task is almost entirely a directed complete-prime enclosure. The theorem does not assume the empirical sign of that enclosure.

By L-2812, the enclosure may be generated as reusable lag-coefficient boxes before a vector is chosen. This removes the historical-vector dependency and can reduce the target from two complete prime-power passes to one. If box dependency leaves zero unresolved, the selected frozen vector is then passed through the sharper L-2806 scalar producer.

## Gap audit

- The theorem is conditional on the imported classical explicit formula through T-2801 until independent review promotes it.
- A negative midpoint is irrelevant unless the full upper endpoint is negative.
- Hashes and coverage endpoints do not prove correct analytic production.
- A positive fixed-vector result excludes only that vector and parameter tuple.

## Suggested next attack

Run one directed coefficient-box stream over all 50 target coverage ranges, choose and freeze the leading midpoint vector, contract the stored boxes, and invoke this theorem. Launch a second fixed-vector scalar pass only if the first exact interval is unresolved.
