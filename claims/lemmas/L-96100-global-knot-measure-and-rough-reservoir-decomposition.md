# L-96100 — Exact global knot measure for the initial-prime sieve

Claim ID: `L-96100`  
Status: **EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-16  
Depends on: the canonical row formula in `L-94200`  
RH status: **not assumed**

## 1. Row coefficients

For \(j\ge2\), put

\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}
\]

and

\[
 q_j(m)=
 \begin{cases}
 0,&m<j,\\
 A_j,&m=j,\\
 -B_j,&m=j+1,\\
 C_j,&m\ge j+2.
 \end{cases}
\tag{L-96100.1}
\]

Then

\[
 Q_Y(j)=\sum_{m\ge1}\frac{q_j(m)}{\sqrt m}
 \log\frac Ym\,\mathbf1_{m\le Y}.
\tag{L-96100.2}
\]

Let \(P_r=\prod_{\nu\le r}p_\nu\).  The initial-prime row is

\[
 \mathfrak S_{r,j}(Y)=
 \sum_{d\mid P_r}\frac{\mu(d)}{\sqrt d}Q_{Y/d}(j).
\]

Writing \(Y=e^t\) gives the exact stop-loss potential

\[
 \boxed{
 \mathfrak S_{r,j}(e^t)=
 \int_{\mathbb R}(t-u)_+\,d\nu_{r,j}(u),
 }
\tag{L-96100.3}
\]

where

\[
 \nu_{r,j}=
 \sum_{d\mid P_r}\sum_{m\ge j}
 \frac{\mu(d)q_j(m)}{\sqrt{dm}}\,
 \delta_{\log(dm)}.
\tag{L-96100.4}
\]

This is the correct global object.  Occurrences with the same product may be
combined algebraically, but a positivity certificate is allowed to transport
mass between different products.

## 2. Constant tail plus finite frontier

The coefficient sequence has the exact decomposition

\[
 q_j(m)=C_j+h_j(m),
\]

with

\[
 h_j(m)=
 \begin{cases}
 -C_j,&1\le m<j,\\
 \frac{j+2}{j},&m=j,\\
 -1,&m=j+1,\\
 0,&m\ge j+2.
 \end{cases}
\tag{L-96100.5}
\]

Consequently the coefficient at the physical knot \(n\) is

\[
\boxed{
 \omega_{r,j}(n)=
 C_j\mathbf1_{(n,P_r)=1}
 +
 \sum_{\substack{m\mid n,\ m\le j+1\\ n/m\mid P_r}}
 \mu(n/m)h_j(m).
}
\tag{L-96100.6}
\]

Thus the infinite part is the positive \(P_r\)-rough reservoir and every signed
correction comes from one of the finitely many frontier labels \(m\le j+1\).
Equation (L-96100.6) is also the exact reason that the negative residue at
\((j,P_r,n)=(3,6,24)\) must be paid from other products.

## 3. Kernel order

For fixed \(t\), the function

\[
 u\longmapsto(t-u)_+
\]

is decreasing and convex.  Therefore each of the following measures has
nonnegative potential:

1. a positive atom \(\eta\delta_a\);
2. a monotone pair \(\eta(\delta_a-\delta_b)\), \(a\le b\);
3. a left-curtain butterfly
   \[
   \eta\bigl[\lambda\delta_a+(1-\lambda)\delta_c-\delta_b\bigr],
   \quad a<b<c,
   \quad b=\lambda a+(1-\lambda)c.
   \]

The next theorem constructs precisely such a decomposition of (L-96100.4).
