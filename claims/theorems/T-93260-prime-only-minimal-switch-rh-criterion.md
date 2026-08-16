# T-93260 — RH is equivalent to one prime-only minimal-two-switch cubic discrepancy

Claim ID: `T-93260`  
Status: **PROPOSED COMPLETE PRIME-ONLY RH CRITERION — INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Created: 2026-08-16  
Depends on: `R-93260`, `L-93261`, and the complete Q4 source of PR #498  
Scope: removes all prime powers and the four-adic gauge at square-root cost; does not prove the prime discrepancy bound

## 1. Prime and harmless sectors

From the complete source,

\[
\mathcal A_\circ(N)
=
\sum_{n\le N}\Lambda(n)W(n/N)
+
3(\log4)\sum_{4^r\le N}K(4^r/N).
\tag{T-93260.1}
\]

Define the prime-only scalar

\[
\boxed{
\mathcal P_W(N)=\sum_{p\le N}(\log p)W(p/N).
}
\tag{T-93260.2}
\]

On `[0,1]` one has the safe pointwise estimate

\[
|W(x)|\le32x.
\tag{T-93260.3}
\]

Consequently all proper prime powers satisfy

\[
\sum_{\substack{p^k\le N\\k\ge2}}
(\log p)|W(p^k/N)|
\ll \sqrt N\log^2(2N).
\tag{T-93260.4}
\]

The explicit four-adic gauge is `O(log N)`. Therefore

\[
\boxed{
\mathcal A_\circ(N)
=
\mathcal P_W(N)
+O(\sqrt N\log^2(2N)).
}
\tag{T-93260.5}
\]

No estimate for ordinary primes is used here.

## 2. Mellin pole audit after removing prime powers

For `Re s>1`,

\[
\sum_p{\log p\over p^s}
=
-\frac{\zeta'}{\zeta}(s)
-
\sum_{p}\sum_{k\ge2}{\log p\over p^{ks}}.
\tag{T-93260.6}
\]

The double sum is analytic in `Re s>1/2`. Hence the Mellin transform of
`P_W` has, in that half-plane, exactly the same nontrivial zeta poles as

\[
\widehat W(s)\left(-\frac{\zeta'}{\zeta}(s)\right).
\]

By `L-93261`, `What(rho)` is nonzero at every nontrivial zero `rho`.

## 3. Criterion

The standard RH Chebyshev bound and partial summation give

\[
RH\Longrightarrow
\mathcal P_W(N)=O(\sqrt N\log^2(2N)).
\tag{T-93260.7}
\]

Conversely, if for some fixed `B`

\[
\mathcal P_W(N)=O(\sqrt N\log^B(2N)),
\tag{T-93260.8}
\]

then (T-93260.5) gives the same bound for `A_circ`. The reconstructed Mellin
argument of `R-93260` excludes every zero with real part greater than `1/2`.
Functional symmetry then gives RH.

Thus

\[
\boxed{
RH
\quad\Longleftrightarrow\quad
\mathcal P_W(N)=O(\sqrt N\log^B(2N))
\text{ for some fixed }B.
}
\tag{T-93260.9}
\]

This is not `CPBD` under a new name: it is one explicit **linear sum over
ordinary primes only**, with the minimal sign pattern `+,-,+` established in
`L-93261`.

## 4. Boundary

```text
prime-power removal                  UNCONDITIONAL / EXACT-SCALE
four-adic removal                    UNCONDITIONAL / EXPLICIT
prime-only Mellin pole survival      COMPLETE
minimal two-switch geometry          COMPLETE
prime-only sqrt bound                OPEN / RH-BEARING
RH                                   UNPROVED
```
