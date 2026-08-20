# L-101102 — Largest-label matching closes every short positive-kernel owner block

Claim ID: `L-101102`  
Status: **PROVED EXACT FINITE HALL MATCHING**  
Created: 2026-08-20  
Depends on: `L-101101`; critical Bernstein scaling inequality  
RH status: **not assumed**

Let \(Q\) be a finite ordered set of prime labels contained in one interval
\[
 x<q\le8x,\qquad x\ge67,
\]
with at most one extra labelled copy of \(67\).  Put \(c_q=1/q\).

Let \(w(A)\ge0\), \(A\subseteq Q\), be any family satisfying the critical
child ratio
\[
 w(A\cup\{q\})\le c_q\,w(A)
 \quad(q>\max A).                                  \tag{L-101102.1}
\]
Then
\[
 \boxed{
 \sum_{A\subseteq Q}(-1)^{|A|}w(A)\ge0.
 }                                                   \tag{L-101102.2}
\]

## Exact matching

Every odd subset \(A\) is matched to the even parent
\[
 B=A\setminus\{\max A\}.
\]
For a fixed even \(B\), the complete incoming load is
\[
 \sum_{\substack{q\in Q\\q>\max B}} w(B\cup\{q\})
 \le
 w(B)\sum_{\substack{q\in Q\\q>\max B}}{1\over q}.
\]
By `L-101101`, this is strictly below \(3w(B)/4\).  Hence
\[
 w(B)-\sum_{q>\max B}w(B\cup\{q\})>{1\over4}w(B).
\]
Summing over all even \(B\) gives the exact rearrangement
\[
 \sum_A(-1)^{|A|}w(A)
 =
 \sum_{\substack{B\subseteq Q\\|B|\ {\rm even}}}
 \left[
  w(B)-\sum_{q>\max B}w(B\cup\{q\})
 \right]\ge0.                                      \tag{L-101102.3}
\]

## Arithmetic application

At the final centered-Bernstein critical step, the sharp scaling theorem gives
exactly
\[
 {w(A\cup\{q\};X)\over w(A;X)}\le {1\over q}.
\]
Therefore every double-owner block whose unresolved interior prime labels lie
between endpoint primes \(p_i<p_j\) with
\[
 p_j/p_i\le8
\]
has nonnegative interior parity sum.

The theorem is source-faithful and uses the literal prime labels.  It is a
one-block result: it does not assert that the positive residual belongs to a
cone invariant under a second distant prime band.  That missing cone
preservation is precisely why the long-interval sector remains separate.
