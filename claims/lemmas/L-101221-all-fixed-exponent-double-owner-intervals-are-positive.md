# L-101221 — Every fixed prime-power double-owner interval is eventually positive

Claim ID: `L-101221`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC INTERVAL THEOREM**  
Created: 2026-08-21  
Depends on: `L-101220`; PR #701 `L-100721`  
RH status: **not assumed**

Use the endpoint-compensated prefix of PR #701:

\[
\mathcal B_{p,q}(x)=
A_{p,q}(x)-p^{-1/2}A_{p,q}(x/p)
-q^{-1/2}A_{p,q}(x/q)
+(pq)^{-1/2}A_{p,q}(x/(pq)).
\tag{L-101221.1}
\]

Fix `A>1`. Suppose, contrary to the claim, that there are primes

\[
p_j<q_j\le p_j^A,\qquad p_j\to\infty,
\]

and `x_j>=1` with `B_(p_j,q_j)(x_j)<=0`. Pass to a subsequence with

\[
a_j=\log q_j/\log p_j\to a\in[1,A].
\]

The absolute variation of every prefix `A_(p_j,q_j)` is bounded by

\[
\prod_{p_j<\ell<q_j}(1+\ell^{-1})=O_A(1).
\tag{L-101221.2}
\]

If `u_j=log x_j/log p_j` is bounded, pass again to `u_j->u`. By `L-101220`,

\[
A_{p_j,q_j}(x_j)\to F_a(u)>0,
\]

while all three endpoint-compensation terms tend to zero by (L-101221.2).
This contradicts `B<=0`.

If `u_j->infinity`, `L-101220.12` gives

\[
A_{p_j,q_j}(x_j)\to1/a>0,
\]

and the compensated terms again vanish. This is the same contradiction.

Therefore, for every fixed `A>1`, there is `p_1(A)` such that

\[
\boxed{
\mathcal B_{p,q}(x)>0
\qquad
(p_1(A)\le p<q\le p^A,\ x\ge1).
}
\tag{L-101221.3}
\]

PR #701 proves the exact coarea identity

\[
H'_{p,q;\mathcal P}(t)
=384\int_0^1(1-s)
\mathcal B_{p,q}((t/s)^2)\,ds.
\]

Since `H(0)=0`, (L-101221.3) yields

\[
\boxed{
H_{p,q;\mathcal P}(t)\ge0
\qquad(t\ge0)
}
\tag{L-101221.4}
\]

for every sufficiently large endpoint interval with `q<=p^A`.

This replaces the former fixed corridor `A<e` by **every finite exponent**.
