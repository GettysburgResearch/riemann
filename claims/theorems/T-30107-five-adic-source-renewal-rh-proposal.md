# T-30107 — Five-adic source renewal proposal toward RH

Status: FULL RESEARCH PROPOSAL — LOAD-BEARING CLOSING THEOREM OPEN

## Motivation

The previous atomic boundary closures failed because they destroyed cancellation before measuring cost. The correct object is the finite signed source itself.

The surviving structure is not an eta tail estimate but a renewal equation.

## Five-adic decomposition

Let

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

For X=5Y, the Möbius-resolved source satisfies the exact scaling relation

\[
 u_X(5a)=5^{-1/2}u_Y(a).
\]

Therefore the divergence blocks obey

\[
\sum_{j=0}^4 r_X(5a+j)=5^{-1/2}r_Y(a).
\]

Every block decomposes as

\[
5^{-1/2}r_Y(a)e_{5a}
+
\sum_{j=1}^4 c_{a,j}(e_{5a+j}-e_{5a+j-1}),
\]

where

\[
c_{a,j}=\sum_{\ell=j}^4r_X(5a+\ell).
\]

## Source renewal theorem

The desired theorem is:

> There exists a finite admissible Pascal-cycle operator R such that the complete inner five-adic commutator source satisfies
>
> \[
> D_X\le \frac15D_{X/5}+O(\log^A X).
> \]

Here D_X is the optimized Cycle Debt in the source-native coordinate.

## Why this is the correct final target

The old approach attempted:

\[
\text{boundary}
\rightarrow\text{atoms}
\rightarrow\text{absolute norm}
\rightarrow\text{debt}.
\]

That route is false.

The correct order is:

\[
\text{signed source}
\rightarrow\text{five-adic recombination}
\rightarrow\text{legal cycles}
\rightarrow\text{debt}.
\]

## Proposed closing mechanism

The remaining inner block should be attacked by a finite five-state automaton:

1. retain residues modulo 5;
2. solve the local commutator transport exactly;
3. push all residual charge to the 5-divisible channel;
4. iterate.

The expected contraction is the exact scaling reserve

\[
5^{-1}
\]

rather than a heuristic analytic factor.

## Conditional completion

If the five-adic source renewal theorem holds, then:

\[
D_X=X^{o(1)}.
\]

Combined with the existing Cycle Debt consumer, this gives the sharp prime ramp and the RH deduction.

## Proof boundary

Closed:

- finite five-block identity;
- outer commutator confinement;
- exact lower-scale scaling.

Open:

- inner five-state transport certificate;
- RH.
