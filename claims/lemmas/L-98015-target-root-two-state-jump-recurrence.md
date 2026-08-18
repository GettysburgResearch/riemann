# L-98015 — The target root has an exact two-state jump recurrence and integer criterion

Claim ID: `L-98015`  
Status: **PROVED EXACT DISCRETE/REAL-ENDPOINT REDUCTION**  
Created: 2026-08-18  
Depends on: `L-98014`  
RH status: **not assumed**

Define

\[
A_N=\sum_{n\le N}{\mu(n)\over n},
\qquad
B_N=\sum_{n\le N}{\mu(n)\over\sqrt n},
\]

and the inclusive integer target root

\[
F_N=4\sqrt N\,A_N-3B_N.
\tag{L-98015.1}
\]

Then the complete update from `N` to `N+1` is

\[
\boxed{
A_{N+1}=A_N+{\mu(N+1)\over N+1},
}
\tag{L-98015.2}
\]

\[
\boxed{
F_{N+1}
=F_N
+{4A_N\over\sqrt{N+1}+\sqrt N}
+{\mu(N+1)\over\sqrt{N+1}}.
}
\tag{L-98015.3}
\]

Thus the target route is an exact two-state deterministic jump system driven only by the next Möbius value.

## Proof

The first identity is immediate. For the second, use

\[
B_{N+1}=B_N+{\mu(N+1)\over\sqrt{N+1}}
\]

and expand

\[
4\sqrt{N+1}\left(A_N+{\mu(N+1)\over N+1}\right)
-3\left(B_N+{\mu(N+1)\over\sqrt{N+1}}\right).
\]

The coefficient of `mu(N+1)` is exactly `1/sqrt(N+1)`, and

\[
\sqrt{N+1}-\sqrt N
={1\over\sqrt{N+1}+\sqrt N}.
\]

## Exact all-real reduction

On the open cell `N<X<N+1`, no new source index activates, so

\[
\mathcal T_X=4\sqrt X\,A_N-3B_N.
\tag{L-98015.4}
\]

This is affine in `sqrt(X)` with slope `4A_N`. Therefore its cell infimum is

\[
\boxed{
\mathfrak m_N
=F_N+{4\min(A_N,0)\over\sqrt{N+1}+\sqrt N}.
}
\tag{L-98015.5}
\]

If `A_N>=0`, the minimum is the right-hand value at `X=N`. If `A_N<0`, the minimum is the left limit at `X=N+1`. The activation value at `N+1` is then `F_{N+1}` and is checked by the next state.

Consequently

\[
\boxed{
\mathcal T_X\ge0\text{ for every sufficiently large real }X
\iff
\mathfrak m_N\ge0\text{ for every sufficiently large integer }N.
}
\tag{L-98015.6}
\]

No interior optimization and no interpolation error remain.

## Fail-closed computational form

A directed verifier needs to maintain only

```text
exact rational A_N;
directed radical sum B_N or directed F_N;
mu(N+1);
both signs of A_N and the one cell endpoint selected by (L-98015.5).
```

The recurrence also supplies exact mutation tests: changing one `mu(N+1)` must alter `A` by `1/(N+1)` and `F` by `1/sqrt(N+1)` in addition to the deterministic drift.
