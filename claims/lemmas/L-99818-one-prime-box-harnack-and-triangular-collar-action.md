# L-99818 — One-prime box Harnack positivity and triangular collar action

Claim ID: `L-99818`  
Status: **PROVED EXACT ONE-PRIME / FINITE-STATE THEOREM**  
Created: 2026-08-20  
Depends on: PR #658 `L-99703`  
RH status: **not assumed**

Let `u=log y`, `L=log p`, `p>=67`, and write the normalized box potential as

\[
\Phi(u)=
\begin{cases}
0,&u<0,\\
8+(-8-3u)e^{-u/2},&0<=u<\log67,\\
A-Be^{-u/2},&u>=\log67,
\end{cases}
\]

with

\[
A=8(1-67^{-1/2}),\qquad B=3\log67.
\]

Define the one-prime weighted Harnack operator

\[
\mathcal H_pF(u)=F(u)-e^{-L/2}F(u-L).
\]

Only the regime transitions

```text
0->0,
1->0,
2->0,
2->1,
2->2
```

are possible.

In the first four nontrivial cases direct substitution proves `H_p Phi(u)>0`. In particular, on the only mixed transition `2->1`,

\[
\boxed{
\mathcal H_p\Phi(u)
=a_p+[8-3\log67+3(u-L)]e^{-u/2},
}
\tag{L-99818.1}

where

\[
a_p=8(1-67^{-1/2})-8p^{-1/2}>0.
\]

The derivative of the bracketed expression has one elementary critical point, and endpoint evaluation on

\[
\max(\log67,L)<=u<L+\log67
\]

gives a strictly positive lower bound. On `2->2`, the critical half-order term cancels and

\[
\mathcal H_p\Phi(u)=A(1-p^{-1/2})>0.
\]

More generally, on any interval where

\[
F(u)=a+(b+cu)e^{-u/2}
\]

and both `u,u-L` remain in that same formula, one has the exact triangular action

\[
\boxed{
\mathcal H_pF(u)=a(1-p^{-1/2})+c(\log p)e^{-u/2}.
}
\tag{L-99818.2}

Thus one weighted prime step deletes the entire `b e^{-u/2}` mode, and a second uniform-regime prime step deletes the remaining half-order mode. This explains the global active two-prime positivity of `L-99815`.

The remaining all-prime composition problem is finite-state: it is entirely caused by repeated crossings of the single transition `2->1`. No new functional modes are created.
