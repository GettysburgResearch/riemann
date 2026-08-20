# L-100401 — Every actual activation-zero envelope block through four labels is positive

Claim ID: `L-100401`  
Status: **PROVED EXACT FINITE-ORDER THEOREM; ALL-ORDER GATE OPEN**  
Created: 2026-08-20  
Depends on: `L-100400`  
RH status: **not assumed**

Normalize the envelope kernel by

\[
f_-(y)=\frac{R_-(y)}y=
\begin{cases}
16,&0<y<1,\\
32y^{-1/2}-16y^{-1},&y\ge1.
\end{cases}
\]

A native label \(q\) acts by

\[
D_q=I-q^{-3/2}U_q.
\]

Labels are ordinary primes, with only one repetition permitted: the second
labelled copy of \(67\).

Put \(u=\log y\) and

\[
F(u)=e^{3u/2}f_-(e^u)
=
\begin{cases}
16e^{3u/2},&u<0,\\
32e^u-16e^{u/2},&u\ge0.
\end{cases}
\]

Then

\[
e^{3u/2}D_qf_-(e^u)
=(I-\tau_{\log q})F(u).
\]

## 1. Two-label derivative cone

For \(m=0,1,2\), write

\[
e^{-3u/2}F^{(m)}(u)=
\begin{cases}
A_m,&u<0,\\
32e^{-u/2}-B_me^{-u},&u\ge0,
\end{cases}
\]

with

\[
(A_0,B_0)=(16,16),\qquad
(A_1,B_1)=(24,8),\qquad
(A_2,B_2)=(36,4).
\]

For every actual pair of labels \(p\le q\), including the repeated pair
\((67,67)\),

\[
\boxed{
D_pD_q\!\left(e^{-3u/2}F^{(m)}(u)\right)>0
\qquad(m=0,1,2).
}
\]

The proof is a five-regime calculation at

\[
1,\ p,\ q,\ pq.
\]

In every regime the expression is monotone in the label parameters.  The
ordinary-prime minimum occurs at \((p,q)=(2,3)\); the only repeated case is
\((67,67)\).  Substitution gives strict positive margins for all three
\((A_m,B_m)\).

Equivalently, for

\[
G_{p,q}(u)=(I-\tau_{\log p})(I-\tau_{\log q})F(u),
\]

one has

\[
\boxed{
G_{p,q}(u)>0,\qquad
G_{p,q}'(u)>0,\qquad
G_{p,q}''(u)>0.
}
\]

## 2. Three and four labels

Let \(r\) be a third actual label.  Since \(G_{p,q}\) is increasing,

\[
(I-\tau_{\log r})G_{p,q}>0.
\]

Since \(G_{p,q}'\) is increasing, the three-label block is itself increasing.
Therefore a fourth actual label \(s\) gives

\[
\boxed{
D_pD_qD_rD_sf_-(y)>0
\qquad(y>0).
}
\]

Thus every native block involving at most four labels is strictly positive.

## 3. Sharp scope firewall

This is not an all-order complete-monotonicity theorem.  Repeating the
non-native label \(2\) five times gives the exact mutation

\[
\boxed{
D_2^5f_-(3)<-0.09.
}
\]

Therefore pairwise positivity cannot be iterated without the native
distinct-prime geometry.  Any failure of the actual arithmetic envelope must
begin with at least five interacting labels.

The surviving all-order theorem is:

```text
FAEG100401:
every actual mixed-activation block with at least five labels is nonnegative.
```

It remains open and conclusion-bearing.
