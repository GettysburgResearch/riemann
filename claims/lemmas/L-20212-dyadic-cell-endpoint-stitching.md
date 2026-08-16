# L-20212 — Dyadic-cell endpoint stitching

Claim ID: `L-20212`  
Title: Adjacent all-positive dyadic prime blocks differ at their common endpoint by one explicit polynomial-size archimedean edge term  
Status: `PROPOSED — COMPLETE IDENTITY AND ASYMPTOTIC`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20208`; `L-20210`  
Scope: every integer `r>=2`

## 1. Shared physical endpoint

Put

\[
 a=\log2.
\]

For the corrected dyadic defect, define

\[
 L_r=\widetilde{\mathcal D}_r(a)
\]

at the left endpoint of block `r` and

\[
 R_r=\widetilde{\mathcal D}_r\left(a+{a\over r}\right)
\]

at its right endpoint.

Both `R_r` and `L_(r+1)` evaluate the same large physical screw value

\[
 \Psi((r+1)a),
\]

but use adjacent dilation normalizations.

## 2. Exact stitching identity

On the small interval `[a,a+a/r]`, the only prime ramp is `q=2`:

\[
 \Psi(t)=F(t)-a_2(t-a),
 \qquad
 a_2={a\over\sqrt2}.
\]

The correction in `T-20208` cancels that ramp. Therefore

\[
\boxed{
 R_r-L_{r+1}
 =r^2F\left(a+{a\over r}\right)
  -(r+1)^2F(a).}
 \tag{1}

No prime sum, zero sum, or large-scale special-function value remains on the right side.

## 3. Uniform edge asymptotic

Taylor expansion at `a` gives

\[
\boxed{
\begin{aligned}
 R_r-L_{r+1}
 ={}&r\,[aF'(a)-2F(a)]\\
 &+\left[{a^2\over2}F''(a)-F(a)\right]\\
 &+{a^3\over6r}F'''(a)
 +O_a(r^{-2}).
\end{aligned}}
 \tag{2}

In particular,

\[
\boxed{|R_r-L_{r+1}|=O(r).}
 \tag{3}

This is automatically `e^(o(r))`.

## 4. Endpoint burden collapses

The relaxed criterion of `T-20208` permits a subexponential negative part. Equation (3) implies that controlling one endpoint orientation controls the other at the required scale:

\[
 (-L_{r+1})_+
 \le(-R_r)_+ +O(r),
\]

and conversely.

Hence a proof-producing cofinal ledger need not establish two unrelated endpoint estimates per block. It may:

1. carry one outgoing endpoint margin from block `r`;
2. apply the explicit edge correction (1);
3. use the result as the incoming margin for block `r+1`.

Since `2^r` and `2^(r+1)` are themselves prime powers, the endpoints also belong to the global prime-knot stream. The complete dyadic hierarchy is therefore one stitched scalar recurrence, not a collection of independent finite problems.

## 5. Critical base-point observation

For a general base `a` before the first prime knot, the coefficient of the linear edge drift is

\[
 aF'(a)-2F(a)
 =a^3{d\over da}\left({F(a)\over a^2}\right).
 \tag{4}

A base point satisfying

\[
 aF'(a)=2F(a)
\]

would reduce the edge mismatch from `O(r)` to `O(1)`. The dyadic choice `a=log2` is preferred for exact support and needs no such cancellation because `O(r)` is already harmless for the subexponential criterion.

This observation is a scheduling tool, not an asserted existence or uniqueness theorem for a critical base point.

## 6. Proof boundary

- The stitching identity and expansion are exact.
- Polynomial endpoint transfer does not control the interior prime-knot minima.
- The cofinal transport/square inequality inside each block remains the load-bearing arithmetic theorem.
