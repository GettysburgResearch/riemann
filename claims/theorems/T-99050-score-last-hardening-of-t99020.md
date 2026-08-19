# T-99050 — Score-last entropy-isometric hardening of the direct-integral factor-67 candidate

Claim ID: `T-99050`  
Status: **PROPOSED COMPLETE UNCONDITIONAL HARDENING — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-19  
Frozen parent: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
RH status: **not established by publication**

## The new idea

Do not transport or estimate score packet by packet. The exact causal tree has
finite depth, every current and terminal row is nonnegative, and every causal
edge is an exact physical-row identity. Expand the tree first and apply literal
entropy once at the end.

`L-99050` proves that the complete arithmetic recursion is literal-score
isometric. Therefore the terminal score debt of `L-99024` is unnecessary.

## Strengthened physical score

On the frozen endpoint-frame identity, the complete unthinned common-parent row
has score

\[
 \mathcal H(R_X^{\rm eq})=4\sqrt X.
\]

Compact Hall, the residual-only causal tree, endpoint integration, the retained
inner block, and optional exact cubature preserve this score exactly. The Hall
row bonus is current-only and has nonnegative literal score.

`L-99051` proves that, for

\[
 X\ge400160016,
\]

the fixed top omission costs less than `60`, while the unique all-column
thinning costs less than `792`. Hence the same feasible row constructed in
`L-99022/L-99023` satisfies

\[
\boxed{
 \mathcal H(d_X)>4\sqrt X-852.
}
\tag{T-99050.1}

The elementary benchmark comparison gives

\[
\boxed{
 J_\Lambda(X)-\mathcal H(d_X)<4\log X+852
 =o(\log^2X).
}
\tag{T-99050.2}

Ordinary feasibility implies

\[
 F_\Lambda(X)
 =J_\Lambda(X)-P_\Lambda(X)
 \le J_\Lambda(X)-\mathcal H(d_X)
 =o(\log^2X).
\]

The prime-square separation and Mellin--Landau conclusion in `L-99025` then give
the same proposed RH conclusion as `T-99020`.

## Complete chain

```text
compact score-free Hall
 -> positive residual source + current-only row bonus
 -> exact finite causal tree on actual rough primes
 -> one exact physical row, score-isometric before safety operations
 -> direct endpoint integration / optional exact cubature
 -> top omission before realization
 -> one square-root thinning
 -> every q and 4q column, including q<K
 -> literal score >4sqrt(X)-852
 -> J_Lambda-H <4log(X)+852
 -> F_Lambda=o(log^2 X)
 -> prime-square moat
 -> Mellin-Landau
 -> RH candidate.
```

## What is removed

```text
packetwise declared-score loss              removed
terminal score-realization debt             removed
fixed-67 artificial score path              removed
Bellman/leaf-count score estimate           unnecessary
quantization score loss                     absent
finite base score charge                     absent; base is retained
```

## Scientific boundary

This theorem strengthens the score interface of T-99020 but does not turn a
published candidate into an accepted proof. Independent reviewers must still
reconstruct:

1. compact Hall and normalized-row monotonicity;
2. the exact endpoint-frame row identity and its `4sqrt(X)` literal score;
3. direct common-parent integration and source ownership;
4. the all-column finite/continuum discrepancy estimate;
5. the prime-square and Mellin--Landau consumer.

```text
score-last finite-tree theorem           proposed exact
explicit root-owned score loss <852      elementary exact on parent inputs
complete T-99020 composition             materially strengthened candidate
accepted proof of RH                     no
Riemann Hypothesis                       unproved pending review
```
