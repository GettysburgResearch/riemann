# L-24519 — Corrected descending jump algorithm

Claim ID: `L-24519`  
Status: `PROPOSED — complete finite algorithm; asymptotic cost not asserted`  
Scope: signed prime-power feasibility repair  
Issue: #245

Let

\[
r_q(b)=v_q(b)-w_X(q)
\qquad(q=p^a\le X)
\tag{L-24519.1}
\]

be the residual of any real carry vector `b`. No sign condition on `b` is
assumed.

## 1. Algorithm

Order the prime powers decreasingly. Starting from `b^(0)=b`, when the current
row is `q`, put

\[
t_q=\bigl(r_q(b^{\rm current})\bigr)_+
\tag{L-24519.2}
\]

and replace

\[
\boxed{
b_q\longleftarrow b_q-t_q.}
\tag{L-24519.3}
\]

Then continue to the next smaller prime power.

## 2. Exact triangularity

By `R-24503`, operation (L-24519.3) changes row `r` by

\[
-t_q\mathbf1_{r\mid q}+t_q\mathbf1_{r\mid q-1}.
\tag{L-24519.4}
\]

In particular, the current `q`-row decreases by exactly `t_q` and becomes
nonpositive. Every positive side effect has index `r<q`. A later operation at
an index below `q` cannot affect row `q`, because neither the lower index nor
one less than it is divisible by `q`.

Therefore the algorithm terminates after one descending pass and produces a
feasible vector:

\[
\boxed{r_q(b^{\rm final})\le0\quad(q=p^a\le X).}
\tag{L-24519.5}
\]

No iterative convergence, spectral-radius theorem, or positivity of the
coordinates is needed.

## 3. Exact recurrence

The correction masses satisfy the triangular recurrence

\[
\boxed{
t_q=\left[
 r_q(b)
-\sum_{\substack{Q>q\\q\mid Q}}t_Q
+\sum_{\substack{Q>q\\q\mid Q-1}}t_Q
\right]_+.
}
\tag{L-24519.6}
\]

The first sum is favorable and comes only from larger powers of the same prime.
The second sum is the strict descending divisor channel.

For the ordinary-prime system of `L-24517`, this simplifies to

\[
\boxed{
t_p=\left[
 r_p(b)+\sum_{\substack{Q>p\ {m prime}\\Q\equiv1\pmod p}}t_Q
\right]_+.
}
\tag{L-24519.7}
\]

For `p>2`, every parent `Q` in the sum satisfies `p<=(Q-1)/2`.

## 4. Exact objective cost

Since only the coordinates `b_q` change,

\[
\boxed{
J_X(b)-J_X(b^{\rm final})
=\sum_{q=p^a\le X}t_q\log\frac q{q-1}.
}
\tag{L-24519.8}
\]

Hence the full carry route is closed by the single scalar estimate

\[
\boxed{
\sum_{q=p^a\le X}t_q\log\frac q{q-1}=X^{o(1)}.
}
\tag{DJC}
\]

The stronger `O(log^2 X)` bound is sufficient but not necessary for the
square-screw/Landau transfer.

## 5. Why the finite theorem is not yet the global proof

The row `2` receives positive mass from every corrected odd prime. In the
ordinary-prime subsystem, a fixed band of corrected primes can therefore create
order `sqrt(X)/log X` mass at row `2`. Thus a rowwise diagonal descent can have
polynomial cost even though the exact signed system may admit a much cheaper
paired correction.

The theorem proves termination and gives the exact cost functional. It does not
assert (DJC). A proof of DJC must exploit negative slack or cancel common small
prime-divisor channels before descending.

## Review boundary

Equations (L-24519.3)--(L-24519.8) are finite algebra. The asymptotic scalar DJC
is the remaining arithmetic statement, not part of this lemma.
