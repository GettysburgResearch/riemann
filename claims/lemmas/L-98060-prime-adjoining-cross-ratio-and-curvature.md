# L-98060 — Future-prime adjoining is an exact cross-ratio curvature update

Claim ID: `L-98060`  
Status: **PROVED EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98050`; the normalized native Euler recurrence  
RH status: **not assumed**

Let `V:(0,infinity)->R` be a profile, and for a prime `q` put

\[
(\mathcal E_qV)(Y)=V(Y)-{1\over q}V(Y/q).
\tag{L-98060.1}
\]

This is the normalized source-faithful Euler step used in `L-98050`.  For a
prime `p`, define, wherever the denominator is positive,

\[
Q_p[V](Y)={V(Y/p)\over V(Y)}.
\tag{L-98060.2}
\]

Then for distinct primes `p,q`, whenever all displayed denominators are
nonzero,

\[
\boxed{
Q_p[\mathcal E_qV](Y)
=Q_p[V](Y)
 {1-q^{-1}Q_q[V](Y/p)
  \over
  1-q^{-1}Q_q[V](Y)}.
}
\tag{L-98060.3}
\]

Equivalently,

\[
\boxed{
Q_p[\mathcal E_qV](Y)-Q_p[V](Y)
={Q_p[V](Y)\over q}
 {Q_q[V](Y)-Q_q[V](Y/p)
  \over
  1-q^{-1}Q_q[V](Y)}.
}
\tag{L-98060.4}
\]

Thus the effect of adjoining `q` to the future state is not determined by the
single ratio `Q_p`.  It is determined by a multiplicative two-scale curvature.
Put

\[
\mathcal K_{p,q}[V](Y)
=V(Y)V(Y/(pq))-V(Y/p)V(Y/q).
\tag{L-98060.5}
\]

If the four profile values and the Euler denominator in (L-98060.3) are
positive, then

\[
\operatorname{sgn}
\bigl(Q_p[\mathcal E_qV]-Q_p[V]\bigr)
=-\operatorname{sgn}\mathcal K_{p,q}[V].
\tag{L-98060.6}
\]

In particular:

```text
multiplicative TP2, K>=0: adjoining q does not increase the p-ratio;
negative multiplicative curvature, K<0: adjoining q increases the p-ratio.
```

## Proof

Factor the numerator and denominator separately:

\[
\begin{aligned}
(\mathcal E_qV)(Y/p)
&=V(Y/p)
 \left(1-{1\over q}{V(Y/(pq))\over V(Y/p)}\right),\\
(\mathcal E_qV)(Y)
&=V(Y)
 \left(1-{1\over q}{V(Y/q)\over V(Y)}\right).
\end{aligned}
\]

Division gives (L-98060.3), and subtraction gives (L-98060.4).  Moreover

\[
Q_q[V](Y)-Q_q[V](Y/p)
=-{\mathcal K_{p,q}[V](Y)\over V(Y)V(Y/p)},
\]

which proves (L-98060.6).

## Exact accumulated debt

Let `q_1,...,q_m` be future primes, in any fixed adjoining order, and set

\[
V_0=V,
\qquad
V_j=\mathcal E_{q_j}V_{j-1}.
\]

Whenever every ratio and Euler denominator is positive, iterating
(L-98060.3) gives

\[
\boxed{
\log {Q_p[V_m](Y)\over Q_p[V_0](Y)}
=
\sum_{j=1}^m
\log
 {1-q_j^{-1}Q_{q_j}[V_{j-1}](Y/p)
  \over
  1-q_j^{-1}Q_{q_j}[V_{j-1}](Y)}.
}
\tag{L-98060.7}
\]

The native Bellman inequality at `p` is therefore the exact cumulative budget

\[
\boxed{
\sum_{j=1}^m
\log
 {1-q_j^{-1}Q_{q_j}[V_{j-1}](Y/p)
  \over
  1-q_j^{-1}Q_{q_j}[V_{j-1}](Y)}
\le
\log {p\over Q_p[V_0](Y)}.
}
\tag{L-98060.8}
\]

Formula (L-98060.8) is an identity, not a proposed estimate.  It explains why
`PRMP67` cannot be proved by a source-blind monotonicity claim for one ratio:
each future prime contributes a curvature debt at two coupled endpoints.

## Scope

The theorem neither proves nor refutes the final inequality `Q_p<=p`.  Its
purpose is to identify the exact missing state and to provide fail-closed
finite separators.  Any proposed ratio maximum principle must control the
curvatures in (L-98060.5), or an exactly equivalent common-source object, before
it is composed into `GPC67`.