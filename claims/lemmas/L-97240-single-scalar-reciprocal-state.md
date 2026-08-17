# L-97240 - The unique 5:3 scalar is one reciprocal state with a zero-safe Mellin numerator

Claim ID: `L-97240`  
Status: **PROVED EXACT FINITE AND MELLIN ALGEBRA**  
Created: 2026-08-17  
Frozen parent: PR #561 at `db9bdc63c855c6ddf664b763d748f8155a6a2c67`  
RH status: **not assumed**

Put
\[
\mathcal R_X=5c_X(2)+3c_X(3).
\]
Then
\[
\mathcal R_X=\sum_{n\le X}\frac{a_*(n)}{\sqrt n}\log\frac Xn,
\]
where
\[
\boxed{a_*(n)=6\mathbf1_{n=1}-6\mu(n)
 +9\mathbf1_{2\mid n}\mu(n/2)-3\mathbf1_{4\mid n}\mu(n/4).}
\tag{L-97240.1}
\]
Its unsieved dictionary is
\[
q_*(1)=0,\quad q_*(2)=15,\quad q_*(3)=6,\quad q_*(4)=3,
\quad q_*(m)=6\ (m\ge5),
\tag{L-97240.2}
\]
so every nontrivial base coefficient is positive.

Let
\[
b=(\delta_1-\delta_2)*\mu,
\qquad
G(X)=\sum_{n\le X}\frac{b(n)}{\sqrt n}\log\frac Xn.
\]
The exact convolution identity
\[
\boxed{a_*=6\delta_1-3(2\delta_1-\delta_2)*b}
\tag{L-97240.3}
\]
gives
\[
\boxed{\mathcal R_X=6\log X-3\left(2G(X)-2^{-1/2}G(X/2)\right).}
\tag{L-97240.4}
\]

With `z=s+1/2`, termwise Mellin integration in the absolute half-plane gives
\[
\boxed{
\int_1^\infty\mathcal R_X X^{-s-1}\,dX
=\frac6{s^2}-\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}.
}
\tag{L-97240.5}
\]
The finite numerator vanishes only when `2^{-z}=1` or `2^{-z}=2`, impossible
for `Re z>0`.
