# L-24505 — Reciprocal-cell formula for the parabolic seed excess

Claim ID: `L-24505`  
Status: `PROPOSED — explicit calculus reduction; finite rational sign verification still required`  
Scope: elementary continuum sign theorem  
Issue: #245

For fixed integer `N>=1` and

\[
\frac1{N+1}<\theta\le\frac1N,
\]

the number of terms in the continuum excess profile of `L-24504` is exactly `N`.

Define

\[
H_N=\sum_{k=1}^N k^{-1/2},
\qquad
A_N=\sum_{k=1}^N k^{-1/2}\log k.
\]

Then direct collection of the logarithmic terms in `L-24504.4` gives

\[
\boxed{
E(\theta)
=\theta^{-1/2}
\left[A_N+(H_N+1)\log\theta+4H_N\right]-4N.
}
\tag{L-24505.1}
\]

Thus each reciprocal cell is governed by one elementary one-variable function.

Differentiating,

\[
\boxed{
E'(\theta)=\theta^{-3/2}
\left[
(H_N+1)-\frac12\left(A_N+(H_N+1)\log\theta+4H_N\right)
\right].
}
\tag{L-24505.2}
\]

The bracket is affine in `log theta`, so every reciprocal cell has at most one interior critical point. If it exists, it is

\[
\boxed{
\theta_N^*=\exp\left(\frac{2-2H_N-A_N}{H_N+1}\right).
}
\tag{L-24505.3}
\]

Therefore the global sign theorem on `theta>=1/28` reduces to finitely many explicit checks:

- both endpoints of each reciprocal cell `1/(N+1)<theta<=1/N`, `1<=N<=27`;
- the single critical point `theta_N^*` when it lies in that cell.

No oscillatory sum, Farey estimate, or asymptotic number theory remains in this continuum sign check.

## Proposed exact frontier

Floating reconnaissance gives

\[
E(\theta)<0\qquad(1/28\le\theta<1),
\]

with equality only at the trivial endpoint `theta=1`, while the final positive-to-negative transition lies in

\[
1/29<\theta<1/28.
\]

Hence the rational cutoff `1/28` is conservative.

A reviewer can make this rigorous using rational enclosures for the finitely many square roots and logarithms in `H_N`, `A_N`, the endpoints, and the possible critical values. This is a finite elementary sign certificate, not an RH-bearing computation by itself.

## Consequence if certified

Once the finite sign certificate and the uniform Taylor remainder from `L-24504` are supplied, every prime power `q>=X/28` is feasible for the uncorrected parabolic seed for all sufficiently large `X`. The PNC attack may then be restricted to `q<X/28`.

## Status boundary

The reciprocal-cell formula and derivative are exact symbolic calculus. The claimed finite sign pattern is currently reconnaissance until a directed/rational enclosure is committed. RH is not claimed.
