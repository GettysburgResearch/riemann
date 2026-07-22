# L-0605 — Exact compression of the finite prime-power matrix

Claim ID: L-0605  
Title: Exact compression of the finite prime-power matrix into two source sequences  
Status: PROPOSED  
Authoring agent: `gpt56-02-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-23  
Dependencies: D-0001 cutoff-free Weil normalization  
Scope: finite prime-power block for fixed `c>1` and a finite Fourier-index set  
Related counterexample candidates: none

## Statement

Let `L=log(c)`. For every prime power `q=p^a<=c`, put

\[
 w_q=\frac{\log p}{\sqrt q},\qquad
 \theta_q=\frac{2\pi\log q}{L}.
\]

Define

\[
 P_S(k)=\sum_{q=p^a\le c}w_q\sin(k\theta_q),
\]

and

\[
 P_D(k)=\sum_{q=p^a\le c}2w_q
 \left(1-\frac{\log q}{L}\right)\cos(k\theta_q).
\]

Extend `P_S` oddly to negative indices. In the D-0001 normalization, the full
prime-power matrix satisfies

\[
 (W_p)_{nn}=P_D(|n|)
\]

and, for `n!=m`,

\[
 (W_p)_{nm}=\frac{P_S(m)-P_S(n)}{\pi(n-m)}.
\]

Consequently, after enumerating the `P` included prime powers, a contiguous
block on `[-N,N]` can be assembled in `O(PN+N^2)` scalar operations instead of
evaluating a `P`-term sum in every one of `O(N^2)` entries. The identity applies
without change to any finite sparse integer index set.

## Motivation

The entry-by-entry implementation made large-band, sparse-carrier, and
continuous-cutoff searches prohibitively expensive. This compression is an
exact finite identity rather than an approximation. It exposes the prime block
as a divided-difference matrix and permits the source sequences to be evaluated
by direct recurrence, a nonuniform transform, or interval arithmetic.

## Proof

For a diagonal entry, X-0001 uses the kernel

\[
 2\left(1-\frac{\log q}{L}\right)
 \cos\left(\frac{2\pi n\log q}{L}\right).
\]

Multiplication by `w_q` and summation gives `P_D(|n|)` because cosine is even.
For `n!=m`, the kernel is

\[
 \frac{\sin(2\pi m\log q/L)-\sin(2\pi n\log q/L)}
 {\pi(n-m)}.
\]

The denominator is independent of `q`; distributing the finite sum gives the
divided difference of `P_S`. Oddness follows from oddness of sine.

## Analytic domain audit

Only finite sums of real elementary functions occur. `L>0`. There is no
complex branch, contour, limiting interchange, pole, or zero computation.

## Dependency audit

The lemma assumes the sign and normalization of the D-0001/X-0001 prime block.
It does not independently verify the Guinand--Weil dictionary.

## Gap audit

- Algebraic compression does not make floating-point evaluation rigorous.
- Phase recurrences can accumulate rounding error.
- Prime-power enumeration must not omit or duplicate terms.
- A sign error inherited from D-0001 would be preserved rather than detected.
- The claim ID was moved from `L-0601` to `L-0605` to avoid collision with the
  independently developed prime-power-edge packet in PR #23.

## Adversarial tests

X-0602 compares both source arrays with independent entry-by-entry sums and
reproduces the original `c=13,N=8` cutoff-free matrix. Its moment-corrected
nonuniform transform is also compared against direct phase recurrence.

## Remaining uncertainty

The finite algebra is complete-looking, but the claim remains PROPOSED pending
independent normalization review.

## Suggested next attack

Evaluate the source arrays with complex balls, propagate their divided-
difference enclosures, and pass a dyadic interval matrix to the exact X-0001
Rayleigh checker.
