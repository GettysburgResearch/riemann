# L-3902 — Two-channel value-only pole localizers

Claim ID: L-3902  
Title: Two xi-log-derivative values provide a sign-complete local detector and a pole-displacement estimator  
Status: PROPOSED  
Authoring agent: `gpt56-02-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `D-3201`; `L-3901`; the zero-resolvent interface used by `L-4701`  
Scope: derivative-free finite witnesses in `Re(s)>1/2`  
Related counterexample candidates: none

## Statement

Fix a real ordinate `T`. For `x>0`, at zero-free points define

\[
R_T(x)=\operatorname{Re}\frac{\xi'}{\xi}
 \left(\frac12+x+iT\right).
\]

Write `u=x^2` and define

\[
H_T(u)=\frac{R_T(\sqrt u)}{\sqrt u},
\qquad
J_T(u)=\sqrt u\,R_T(\sqrt u)=uH_T(u).
\]

For `0<u<v`, define the two value-only channels

\[
A_T(u,v)=\frac{H_T(u)-H_T(v)}{v-u},
\]

\[
B_T(u,v)=\frac{J_T(v)-J_T(u)}{v-u}.
\]

If RH holds, then

\[
\boxed{
 A_T(u,v)=
 \sum_\gamma
 \frac1{(u+(T-\gamma)^2)(v+(T-\gamma)^2)}\ge0,
}
\]

and

\[
\boxed{
 B_T(u,v)=
 \sum_\gamma
 \frac{(T-\gamma)^2}
 {(u+(T-\gamma)^2)(v+(T-\gamma)^2)}\ge0.
}
\]

Consequently, a directed negative interval for either channel at exact rational
or dyadic inputs is a finite unconditional counterexample witness to RH.

The two channels satisfy the exact algebraic identities

\[
B_T(u,v)=H_T(v)-uA_T(u,v)=H_T(u)-vA_T(u,v).
\]

For a same-ordinate symmetric off-line pair

\[
\frac12+\delta+i\gamma,
\qquad
\frac12-\delta+i\gamma,
\qquad d=\delta^2>0,
\]

of multiplicity `m`, its exact contributions at `T=gamma` are

\[
A_{\rm pair}(u,v)=
 \frac{2m}{(u-d)(v-d)},
\]

\[
B_{\rm pair}(u,v)=
 -\frac{2md}{(u-d)(v-d)},
\]

and therefore

\[
\boxed{B_{\rm pair}/A_{\rm pair}=-d.}
\]

Thus:

- if `u<d<v`, the bracket channel has `A_pair<0`;
- if `u,v<d` or `d<u,v`, the same-side channel has `B_pair<0`.

Every RH failure creates open exact-input negative basins in both geometries.
Near a pole-dominated pair, the observable estimator

\[
\widehat d=-B_T(u,v)/A_T(u,v)
\]

converges to the squared horizontal displacement `delta^2` whenever the
denominator remains separated from zero.

## Proof under RH

Assume RH and set

\[
a_\gamma=(T-\gamma)^2\ge0.
\]

The horizontal zero-resolvent expansion gives

\[
H_T(u)=\sum_\gamma\frac1{u+a_\gamma},
\qquad
J_T(u)=\sum_\gamma\frac{u}{u+a_\gamma}.
\]

For one `a>=0`,

\[
\frac{(u+a)^{-1}-(v+a)^{-1}}{v-u}
 =\frac1{(u+a)(v+a)},
\]

and

\[
\frac{v/(v+a)-u/(u+a)}{v-u}
 =\frac{a}{(u+a)(v+a)}.
\]

Summing the absolutely convergent series proves both nonnegative formulas. The
algebraic identities follow directly from `J(u)=uH(u)`.

## Off-line pair and completeness

At `T=gamma`, the symmetric pair contributes

\[
H_{\rm pair}(u)=\frac{2m}{u-d},
\qquad
J_{\rm pair}(u)=\frac{2mu}{u-d}.
\]

The displayed formulas follow by direct subtraction. In a sufficiently small
punctured neighborhood of `u=d`, all remaining zeros contribute bounded
secants. Approaching `d` from opposite sides makes `A_pair` tend to negative
infinity; approaching from the right with two nodes makes `B_pair` tend to
negative infinity while both scalar real parts are positive. Hence the pair
term dominates the bounded background in each geometry. Continuity and density
supply exact rational or dyadic inputs. ∎

## Search consequence

One batch of two `F` evaluations provides both channels. A proposal engine may:

1. find a negative same-side `B`;
2. estimate `d` from `-B/A`;
3. move one node across the estimated displacement;
4. demand a negative bracket `A` at the same ordinate;
5. freeze both exact pairs for directed ball evaluation.

The paired signature is not required for the logical implication—one rigorous
negative channel suffices—but it is a stronger reconnaissance filter.

## Analytic domain audit

- Both points lie strictly in `Re(s)>1/2` and must be certified away from zeros.
- `u` and `v` are positive real exact inputs with `u<v`.
- No derivative, contour, branch choice, or limiting matrix is used.
- The ratio estimator is diagnostic only unless `A` is rigorously separated
  from zero.

## Gap audit

- A negative fitted secant or an approximate ratio is not a witness.
- `A` and `B` can be tiny differences of large point values; interval
  propagation must retain their shared inputs and exact coefficients.
- The pole estimator can be meaningless when several zeros contribute
  comparably.
- A two-sign empirical pattern is still not a counterexample without directed
  negative intervals.

## Adversarial tests

1. Verify both RH-side formulas on finite critical-line zero sets.
2. Verify `B_pair/A_pair=-delta^2` exactly on a synthetic off-line pair.
3. Test all three node placements: left-left, straddling, and right-right.
4. Add a bounded on-line background and confirm pole dominance as nodes shrink.
5. Perturb `T` and verify the strict signs persist only inside an open basin.

## Remaining uncertainty

No algebraic gap is known. The practical scale and conditioning of a true
high-height basin are unknown.

## Suggested next attack

Implement a batched Arb evaluator returning both channels and the exact
amplification moat. Use the paired signature to rank high-height anomalies
before any multi-point matrix or jet escalation.