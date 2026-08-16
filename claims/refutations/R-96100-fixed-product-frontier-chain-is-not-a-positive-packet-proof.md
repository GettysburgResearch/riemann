# R-96100 — A fixed-product divisor cube cannot prove the prime-sieved row by local convex packets

Claim ID: `R-96100`  
Status: **EXACT REFUTATION OF THE SUBMITTED PROOF SCOPE; THE POSITIVITY STATEMENT IS NOT REFUTED**  
Created: 2026-08-16  
Frozen source: `L-94200` on PR #537  
RH status: **unproved**

## 1. The submitted local step

The original `FRONTIER-CHAIN` prose groups all divisor-cube occurrences with the
same physical product

\[
 n=dm
\]

and then claims that after bulk cancellation each residual component is a
nonnegative atom or a convex packet supported at distinct logarithmic knots.
That implication is false.

For row \(j=3\),

\[
 A_3=2,\qquad B_3=\frac23,\qquad C_3=\frac13.
\]

Take the initial prime segment \(P=2\cdot3\) and physical product \(n=24\).
The four divisor-cube vertices are

\[
\begin{array}{c|c|c|c}
 d&m=n/d&\mu(d)&\mu(d)q_3(m)\\ \hline
 1&24&+1&+\frac13\\
 2&12&-1&-\frac13\\
 3& 8&-1&-\frac13\\
 6& 4&+1&-\frac23.
\end{array}
\]

The first two bulk vertices cancel.  What remains is

\[
 -\frac13-\frac23=-1.
\tag{R-96100.1}
\]

All four occurrences have the same knot \(\log24\).  A fixed-product packet
cannot manufacture left and right support points from them.  In particular,
the residual is neither a positive atom nor a decreasing-convex butterfly.

## 2. Exact disposition

```text
row-spline formula in L-94200                         retained
finite initial-prime identity                        retained
fixed-product local FRONTIER-CHAIN                   false as a proof
prime-sieved positivity statement                    not refuted
required repair                                      cross-product transport
```

Any successor must expose the transport between different products, assign
every positive reservoir once, and keep the physical knot in the certificate.
A restatement of the four scalar capacity inequalities is not enough.
