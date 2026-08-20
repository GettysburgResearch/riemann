# T-100000 — Centered Bernstein carrier cancellation and the critical envelope frontier

Claim ID: `T-100000`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; FINAL CRITICAL SIGN OPEN**  
Created: 2026-08-20  
Base: PR #672 at `2a351548eb7960ff8ae99f193c10e278984c5657`; mathematical input PR #668  
RH status: **unproved**

The new hierarchy starts from globally positive supercritical SHARP boundary
powers and subtracts their exact real Mellin carriers one at a time.

For every integer `m>=3`, the first `m-2` centered remainders are strictly
positive for every real scale:

\[
\boxed{
R_{m,r}(x)>0
\qquad(1\le r\le m-2).
}
\]

Thus every real carrier above the critical prime-harmonic stage can be removed
without losing positivity. The proof is literal in the duplicate-67 Euler
source and uses no Hall flow, physical child promotion, or finite scan.

The final remainder

\[
C_m=R_{m,m-1}
\]

has no positive-real Mellin singularity, while every hypothetical off-line zeta
zero survives as a nonreal pole. Therefore eventual positivity—or subpower
logarithmic negative mass—of any one `C_m` proves RH.

For `m=3`, the final kernel is the explicit positive self-reciprocal Peano
kernel

\[
\Psi(y)=64
\begin{cases}
3y-y^{3/2},&y\le1,\\
3\sqrt y-1,&y\ge1,
\end{cases}
\]

and

\[
C_3(x)=\sum_n{\beta(n)\over\sqrt n}\Psi(x/n).
\]

It also satisfies the exact descent

\[
C_3(x)=6x^{3/2}\int_x^\infty C_2(t)t^{-5/2}\,dt,
\]

where `C_2` is the upper-envelope gap for the positive normalized quadratic
transform of PR #668.

The resulting shortest honest chain is

```text
quadratic/supercritical positivity              PROVED;
all supercritical carrier cancellations         PROVED;
critical quadratic envelope / cubic Peano sign  OPEN;
critical negative mass -> Mellin-Landau          PROVED;
Riemann Hypothesis                               UNPROVED.
```

This packet does not relabel the critical sign as proved. It identifies the
unique step at which the summable labelled mass becomes the divergent prime
harmonic mass.
