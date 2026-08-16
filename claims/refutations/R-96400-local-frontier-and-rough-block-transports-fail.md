# R-96400 — The submitted local FRONTIER-CHAIN and rough-block shadow arguments do not prove prime-sieved positivity

Claim ID: `R-96400`  
Status: **EXACT REFUTATION OF TWO PROOF MECHANISMS; THE TWO-ROW POSITIVITY STATEMENT IS NOT REFUTED**  
Created: 2026-08-17  
Frozen sources: PR #537 at `2c2d4dd834ee61c54a6f8bdd7ba204a01896d593`; PR #548 at `7c7677e3dda318f8f8ccb813c4ca38f14448a538`; PR #549 at `4ef69785b84b3801627956c3f0c9cf0ce56299aa`  
RH status: **unproved**

## 1. The fixed-product FRONTIER-CHAIN cannot create a cross-knot convex packet

For row \(j=3\),
\[
 A_3=2,\qquad B_3=\frac23,\qquad C_3=\frac13,
\]
and
\[
 q_3(m)=
 \begin{cases}
 0,&m<3,\\
 2,&m=3,\\
 -\frac23,&m=4,\\
 \frac13,&m\ge5.
 \end{cases}
\]

Take the initial prime product \(P=2\cdot3\) and the physical product
\(n=24\).  The divisor-cube vertices are
\[
\begin{array}{c|c|c|c}
d&m=n/d&\mu(d)&\mu(d)q_3(m)\\ \hline
1&24&+1&+\frac13\\
2&12&-1&-\frac13\\
3&8&-1&-\frac13\\
6&4&+1&-\frac23.
\end{array}
\]
The first two bulk vertices cancel and the remaining coefficient is
\[
-\frac13-\frac23=-1.
\tag{R-96400.1}
\]

All four occurrences occupy the same knot \(\log24\).  A proof that first
groups by \(n=dm\) cannot then use those same occurrences as a butterfly at
three distinct knots \(a<b<c\).  Thus the local `FRONTIER-CHAIN` proof in
`L-94200` is invalid.  This is a proof-scope refutation, not a negative value
of the complete row.

## 2. The positive bulk store is \(P\)-rough, not the set of all integers

The exact global coefficient decomposition is
\[
 \omega_{P,j}(n)
 =
 C_j{\bf1}_{(n,P)=1}
 +
 \sum_{\substack{m\mid n,\ m\le j+1\\ n/m\mid P}}
 \mu(n/m)h_j(m).
\tag{R-96400.2}
\]
Hence the positive bulk reservoir used by a global transport contains only
integers coprime to the complete initial-prime product \(P\).

The global-shadow packets in PRs #548 and #549 instead invoke
\[
 \sum_{m=u}^{pu-1}\frac1{\sqrt m}
 \ge \sqrt u\log p
\tag{R-96400.3}
\]
as the capacity of a block cut from that rough reservoir.  The left side of
(R-96400.3) counts every integer.  It is not the mass of the store in
(R-96400.2).

An exact witness is
\[
 P=30,\qquad p=5,\qquad u=2.
\]
In the half-open block \([2,10)\), the only integer coprime to \(30\) is \(7\).
Thus the actual unscaled rough mass is
\[
 \sum_{\substack{2\le m<10\\(m,30)=1}}\frac1{\sqrt m}
 =\frac1{\sqrt7}<\frac12.
\tag{R-96400.4}
\]
On the other hand,
\[
 \sqrt2\log5>2.
\tag{R-96400.5}
\]
For a completely elementary verification, \(\sqrt2>4/3\).  Also
\(e<11/4\), since
\[
 e=1+1+\frac12+\sum_{n\ge3}\frac1{n!}
 <\frac52+\frac14=\frac{11}{4}.
\]
Therefore \(e^3<(11/4)^3<25\), so \(e^{3/2}<5\) and
\(\log5>3/2\).  Multiplying gives (R-96400.5).

After multiplying both sides by \(C_j>0\), the same strict mismatch remains.
Consequently the complete-block capacity used in `L-96101` and `L-96200`
is not a bound for the store those files declare.

## 3. Exact disposition

```text
row-spline formula                                   RETAINED
finite initial-prime algebra                         RETAINED
fixed-product local FRONTIER-CHAIN                   FALSE AS A PROOF
global knot measure                                  RETAINED
all-integer block mass = rough-store capacity        FALSE
GLOBAL-FRONTIER-SHADOW proof in PR #548              UNPROVEN / GAP
two-row global-shadow proof in PR #549               UNPROVEN / GAP
prime-sieved positivity itself                       NOT REFUTED
Riemann Hypothesis                                   UNPROVEN
```

Any future transport must list the actual positive occurrences, preserve their
coprimality restrictions, prove global one-use ownership, and verify both mass
and logarithmic barycentre.  Four scalar inequalities with the unsieved
integer block are insufficient.
