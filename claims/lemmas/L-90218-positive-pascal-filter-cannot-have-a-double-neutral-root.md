# L-90218 — A positive uniform-Pascal dyadic filter cannot have a double neutral root

Claim ID: `L-90218`  
Status: **PROPOSED COMPLETE EXACT GLOBAL NO-GO LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: exact dyadic filter cone `L-90216`; elementary summation by parts  
Scope: every finite dyadic source polynomial represented by a nonnegative uniform-Pascal reward; no arithmetic sign theorem and no RH conclusion

## 1. Setup

Let

\[
 Q(t)=\sum_{j=0}^{J}q_jt^j,
 \qquad q_0=1,
 \qquad Q(1)=0,
 \tag{L-90218.1}
\]

and construct its normalized uniform-Pascal node potential and reward as in `L-90216`.

Put

\[
 S_j=\sum_{\ell=0}^{j}q_\ell,
 \qquad
 A_j=2\sum_{\ell=0}^{j-1}2^\ell S_\ell.
 \tag{L-90218.2}
\]

Suppose the complete reward is nonnegative. By `L-90216`, in particular,

\[
 \boxed{A_j\ge0\qquad(1\le j\le J).}
 \tag{L-90218.3}
\]

The stronger left-end block inequalities are not needed for the present theorem.

## 2. Root slope as cumulative block mass

Since `Q(1)=0`, finite summation by parts gives

\[
 \boxed{
 Q'(1)=\sum_{j=1}^{J}jq_j
 =-\sum_{j=0}^{J-1}S_j.
 }
 \tag{L-90218.4}
\]

The weighted coordinates obey

\[
 \boxed{
 A_{j+1}=A_j+2^{j+1}S_j,
 \qquad A_1=2.
 }
 \tag{L-90218.5}
\]

For `J>=2`, substitute

\[
 S_j=\frac{A_{j+1}-A_j}{2^{j+1}}
 \qquad(j\ge1)
 \tag{L-90218.6}
\]

into (L-90218.4). Weighted telescoping yields

\[
\boxed{
\begin{aligned}
 -Q'(1)
 &=\sum_{j=0}^{J-1}S_j\\
 &=\frac12
 +\sum_{j=2}^{J-1}\frac{A_j}{2^{j+1}}
 +\frac{A_J}{2^J}.
\end{aligned}}
 \tag{L-90218.7}
\]

For `J=1`, the only normalized polynomial is `Q(t)=1-t`, so `-Q'(1)=1`.

## 3. Sharp slope theorem

Every term after `1/2` in (L-90218.7) is nonnegative. Therefore

\[
 \boxed{
 Q'(1)\le-\frac12<0.
 }
 \tag{L-90218.8}
\]

In particular, the neutral root `t=1` is always simple. No nonzero filter in the positive uniform-Pascal reward cone can satisfy

\[
 Q(1)=Q'(1)=0.
 \tag{L-90218.9}
\]

### Equality rigidity

Equality in (L-90218.8) forces

\[
 A_j=0\qquad(j\ge2).
 \tag{L-90218.10}
\]

From `A_2=A_1+4S_1=0` one obtains `S_1=-1/2`. The recurrence then gives

\[
 S_j=0\qquad(j\ge2).
 \tag{L-90218.11}
\]

Consequently

\[
 \boxed{
 Q(t)=1-\frac32t+\frac12t^2
 =(1-t)(1-t/2).
 }
 \tag{L-90218.12}
\]

Thus the canonical `15:4` filter is also the unique positive Pascal filter whose neutral-root slope is closest to zero.

## 4. Annularization no-go

A compact endpoint annular filter which removes both the constant and logarithmic neutral modes necessarily contains

\[
 (1-t)^2,
 \tag{L-90218.13}
\]

and hence satisfies `Q(1)=Q'(1)=0`. Equation (L-90218.8) proves:

\[
 \boxed{
 \text{No finite double-neutral dyadic annular filter has a coordinatewise}
 \text{ nonnegative uniform-Pascal reward.}
 }
 \tag{L-90218.14}
\]

This includes every factor-`2^J` polynomial in the annular hierarchy of PR #352, not only the improved factor-64 member. The explicit state-15 witness of `L-90216` is one finite manifestation of this global obstruction.

The theorem does not refute annular criteria. It proves that annular moment cancellation and coordinatewise-positive uniform-Pascal geometry are incompatible at the neutral root. A bridge between them must use signed reward, separate positive channels, a different policy, or a nonlocal state.

## 5. Quantitative gap

Equation (L-90218.7) records the exact distance from the forbidden double root:

\[
 \boxed{
 -Q'(1)-\frac12
 =\sum_{j=2}^{J-1}\frac{A_j}{2^{j+1}}
 +\frac{A_J}{2^J}.
 }
 \tag{L-90218.15}
\]

Every positive reward placed beyond the canonical two-row extremizer contributes a nonnegative slope tax. The filter can become more complicated, but it necessarily moves the neutral-root derivative farther from zero.

This gives a useful design duality:

```text
annular cancellation seeks Q'(1)=0;
positive Pascal reward forces Q'(1)<=-1/2;
canonical 15:4 uniquely minimizes the gap.
```

## 6. Proof boundary

Proved exactly:

- the cumulative formula for `Q'(1)`;
- the reward-cone telescoping identity;
- the sharp bound `Q'(1)<=-1/2`;
- uniqueness of equality;
- impossibility of every finite positive-reward double-neutral annular filter;
- the exact slope-tax formula.

Not proved:

- any signed annular/Pascal payment theorem;
- factor-64 sign, SHARP, or RH.
