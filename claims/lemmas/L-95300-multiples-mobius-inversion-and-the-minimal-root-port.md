# L-95300 — Multiples Möbius inversion gives one exact minimal root port

Claim ID: `L-95300`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `R-95300`; the quarter-balanced signed-span geometry of PR #538

## 1. Carry load to node divergence

Let \(w(q)\) be finitely supported on physical columns \(q\ge2\), and put
\(w(1)=0\). Define

\[
R_w(m)
=
\sum_{d\ge1}\mu(d)w(md),
\tag{L-95300.1}
\]

where the sum is finite, and

\[
r_w(m)=R_w(m)-R_w(m+1).
\tag{L-95300.2}
\]

Then

\[
\boxed{
w(q)=\sum_{n\ge q}r_w(n)\left\lfloor\frac nq\right\rfloor.
}
\tag{L-95300.3}
\]

Indeed, the right side is

\[
\sum_{a\ge1}R_w(aq),
\]

and Möbius inversion on the divisibility poset gives (L-95300.1).

The node source conserves size:

\[
\boxed{
\sum_{n\ge1}n\,r_w(n)=w(1)=0.
}
\tag{L-95300.4}
\]

Its root coordinate is exactly

\[
\boxed{
r_w(1)
=
\sum_{q\ge2}b_2(q)w(q)
=:\rho(w).
}
\tag{L-95300.5}
\]

## 2. Signed interior span, reconstructed

For every \(n\ge4\), the balanced split

\[
n=\lfloor n/2\rfloor+\lceil n/2\rceil
\]

has children at least two and is quarter-balanced. Recursion reduces every
basis vector \(e_n\), modulo interior split divergences, to a combination of
\(e_2,e_3\).

At parent six, compare the two legal trees

\[
6\longrightarrow3+3
\]

and

\[
6\longrightarrow2+4\longrightarrow2+2+2.
\]

Their difference gives the exact relation

\[
3e_2-2e_3
\]

inside the interior split span. Thus the quotient of the node space by
interior split divergences is one-dimensional, measured by total size.
Consequently

\[
\boxed{
r(1)=0,\quad \sum_nnr(n)=0
\Longrightarrow
r\text{ is a signed quarter-balanced interior divergence.}
}
\tag{L-95300.6}
\]

## 3. One root edge spans the missing quotient

Let

\[
\gamma=\chi_{3,1}.
\]

On physical columns,

\[
\boxed{\gamma(q)=\mathbf1_{q=3}.}
\tag{L-95300.7}
\]

Moreover,

\[
\langle b_2,\gamma\rangle=b_2(3)=-1.
\tag{L-95300.8}
\]

For arbitrary \(w\), define

\[
w^\circ=w+\rho(w)\gamma.
\tag{L-95300.9}
\]

Then

\[
\langle b_2,w^\circ\rangle=0.
\]

By (L-95300.4) and (L-95300.6), \(w^\circ\) has a signed interior
realization. Therefore

\[
\boxed{
w=w^\circ-\rho(w)\gamma,
}
\tag{L-95300.10}
\]

where:

```text
w^circ       is signed interior-realizable;
-rho(w)γ     is one boundary root port on 3 -> 1+2.
```

The root-port coefficient is unique, because the interior quotient has
dimension one.

## 4. Positive two-channel realization

Split the signed interior realization into its positive and negative edge
parts. Equation (L-95300.10) then gives a positive two-channel representation
of every physical carry target. The root edge belongs to the positive channel
when \(\rho(w)\le0\), and to the negative channel when \(\rho(w)>0\).

This is an exact positive matrix/two-colour replacement for the false
single-channel PICR statement. It does not prove a one-channel positive
realization.
