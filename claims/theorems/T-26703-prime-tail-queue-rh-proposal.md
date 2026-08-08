# T-26703 — Prime-tail queue proposal for RH

Claim ID: `T-26703`  
Title: A subpower upper-tail charge for the parabolic ordinary-prime residual gives the sharp prime ramp and RH  
Status: **FULL CONDITIONAL PROPOSAL — SHRINKING-RATIO QUEUE ESTIMATE OPEN**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-26704`, `L-26705`; PR #248 `L-24517`, `T-24504`  
Scope: one explicit scalar recurrence target; RH is not claimed proved

## 1. Queue state

For the ordinary-prime residual of the parabolic seed,

\[
r_X(p)
=v_p(b_X^{(0)})-p^{-1/2}\log(X/p),
\]

define

\[
\boxed{
\mathcal Q_X
=
\max_{P\le X}
\left(
\sum_{P\le p\le X}r_X(p)
\right)_+,
}
\tag{T-26703.1}

where the maximum is over ordinary primes `P`.

`L-26704` constructs an explicit nonnegative prime-to-prime incidence flow with one oversupport boundary charge exactly equal to `Q_X`. It proves

\[
\boxed{
P_X
\ge
J_{\mathbb P,X}(b_X^{(0)})
-\mathcal Q_X\log X.
}
\tag{T-26703.2}

The construction is deterministic:

```text
scan primes upward;
carry every positive residual to the next prime;
let negative slack absorb the queue;
export the final unmatched queue to one prime Y in (X,2X).
```

No signed coordinate, negative block, Green solve, or abstract existence theorem appears in the producer.

## 2. Proposed closing theorem

The load-bearing statement is

\[
\boxed{
\mathcal Q_X=X^{o(1)}.
}
\tag{PTQ}

Equivalently, for every `epsilon>0`,

\[
\mathcal Q_X=O_\varepsilon(X^\varepsilon).
\tag{T-26703.3}

This is the **Prime-Tail Queue theorem**.

It is stronger than the scalar prime-ramp inequality, because the latter is only one positive logarithmic average of the tail sums. It is much weaker than:

- total variation of all residuals;
- the full Green-energy theorem;
- DCRS or unsigned Greedy Slack;
- pointwise carry saturation;
- a uniform arbitrary-vector Farey or Type-II estimate.

## 3. Deduction of RH

The parabolic seed satisfies

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X).
\tag{T-26703.4}

Under PTQ, equation (T-26703.2) gives

\[
P_X
\ge4\sqrt X-X^{o(1)}.
\tag{T-26703.5}

By `L-24517`, the higher prime powers differ by only `O(log^2X)`. The equivalence triangle `T-24504` then gives

\[
\boxed{\mathrm{RH}.}
\tag{T-26703.6}

The implication after PTQ is complete.

## 4. Progress already proved toward PTQ

`L-26705` proves the strict fixed-ratio localization

\[
\boxed{
\text{every positive maximizing tail begins at }P_X^{\rm start}=o(X).
}
\tag{T-26703.7}

The input is the exact continuum tail-majorization theorem of PR #265:

\[
\int_\theta^1E(u)\,du<0
\qquad(0<\theta<1),
\]

plus uniform prime Riemann sums and the certified pointwise outer sign of `L-24507`.

Thus the queue has already descended below every fixed output ratio. The remaining issue is quantitative control in the shrinking-ratio regime.

## 5. Preferred completion mechanisms

### 5.1 Dyadic half-scale recurrence

PR #269 proves an exact even-column half-scale isometry and compresses the inverse-zeta source to two carry contacts and two bottom Green charges. The preferred target is an exact signed recurrence

\[
\mathcal Q_X
\le
\mathcal Q_{\lfloor(X+1)/2\rfloor}
+C\log^A(2X),
\tag{T-26703.8}

or a recurrence for the corresponding dyadic signed queue which dominates `Q_X` after the complete three-layer recombination.

### 5.2 Shrinking-ratio prime Riemann sums

Strengthen `L-26705` from fixed `theta` to a range

\[
\theta\ge X^{-\delta_X},
\qquad\delta_X\to0,
\]

with a uniform negative tail margin. The unresolved lower range would then be subpower and could be charged directly.

### 5.3 Contact-cell descent

Use the Green-Skorokhod layer cake of PR #270 to identify each positive queue excursion with one interval contact and route it to a smaller endpoint while preserving the full logarithmic scalar.

Every accepted proof must retain the first fixed-ratio Mertens/dyadic mutation. A phase-blind PNT error estimate is insufficient if it grows like a positive power of `X`.

## 6. Falsifiability

Reject PTQ or any proposed proof upon finding:

1. a sign error in the incidence-block orientation;
2. a missing oversupport boundary charge;
3. a positive complete tail at one fixed output ratio contradicting `L-26705`;
4. use of pointwise continuum convergence where a uniform shrinking-ratio theorem is needed;
5. absolute values taken before defect and slack tails recombine;
6. a lower-scale recurrence that loses the logarithmic/von-Mangoldt ray;
7. promotion of finite queue reconnaissance to PTQ.

## 7. Exact status

```text
prime-tail queue and producer               PROPOSED COMPLETE FINITE
minimal boundary-charge theorem             PROPOSED COMPLETE FINITE
fixed-ratio tail negativity                 PROPOSED COMPLETE ASYMPTOTIC
shrinking-ratio / half-scale queue bound     OPEN
PTQ -> prime ramp -> RH                      COMPLETE CONDITIONAL
Riemann Hypothesis                           UNPROVED
```
