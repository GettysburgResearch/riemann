# L-97000 — The unique 5:3 scalar has a positive base dictionary and a zero-safe Mellin numerator

Claim ID: `L-97000`  
Status: **PROVED EXACT FINITE AND MELLIN ALGEBRA**  
Created: 2026-08-17  
Depends on: fixed-row formulas of PR #557

Put
\[
\mathcal R_X=5c_X(2)+3c_X(3).
\]
For the unsieved canonical rows,
\[
q_2(2)=3,\quad q_2(3)=0,\quad q_2(m)=1\ (m\ge4),
\]
\[
q_3(3)=2,\quad q_3(4)=-\frac23,\quad q_3(m)=\frac13\ (m\ge5).
\]
Hence the combined base dictionary is
\[
\boxed{
q_\star(2)=15,\quad q_\star(3)=6,\quad q_\star(4)=3,
\quad q_\star(m)=6\ (m\ge5).
}
\tag{L-97000.1}
\]
Every base coefficient is positive.

Let
\[
F(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}\log\frac xn.
\]
Then
\[
\boxed{
\mathcal R_X
=6\log X-6F(X)+\frac9{\sqrt2}F(X/2)-\frac32F(X/4).
}
\tag{L-97000.2}
\]
Equivalently,
\[
\mathcal R_X=\sum_{n\le X}\frac{a_\star(n)}{\sqrt n}\log\frac Xn,
\]
where
\[
\boxed{
a_\star(n)=6\mathbf1_{n=1}-6\mu(n)
+9\mathbf1_{2\mid n}\mu(n/2)-3\mathbf1_{4\mid n}\mu(n/4).}
\tag{L-97000.3}
\]

With `z=s+1/2`, the Mellin transform is
\[
\boxed{
\int_1^\infty\mathcal R_X X^{-s-1}\,dX
=\frac6{s^2}-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}.
}
\tag{L-97000.4}
\]
The numerator vanishes only when `2^{-z}=1` or `2^{-z}=2`, impossible for
`Re z>0`. Therefore every hypothetical off-line zeta zero survives in this
single transform.
