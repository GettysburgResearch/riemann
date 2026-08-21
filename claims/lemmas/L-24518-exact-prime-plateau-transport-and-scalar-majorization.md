# L-24518 — Exact prime plateau transport and scalar majorization

Claim ID: `L-24518`  
Status: `PROPOSED — complete finite transport theorem`  
Scope: ordinary-prime correction after `L-24517`  
Issue: #245

Let

\[
U_p(j)=\mathbf1_{p\mid j}
\qquad(0\le j\le X),
\]

with `U_p(0)=0`. For a flow profile `F` satisfying `F_0=F_X=0`, the ordinary
prime divisor-gradient changes by

\[
\Delta v_p(F)
=\sum_{j=1}^{X-1}F_j
\left(U_p(j+1)-2U_p(j)+U_p(j-1)\right).
\tag{L-24518.1}
\]

## 1. A plateau is a pure endpoint transport

For integers `1<=A<B<=X`, define

\[
F_j=t\,\mathbf1_{A\le j<B}.
\tag{L-24518.2}
\]

A finite telescoping gives

\[
\boxed{
\Delta v_p(F)
=t\left[U_p(B)-U_p(A)ight].
}
\tag{L-24518.3}
\]

Indeed, summing the second difference over `A<=j<B` leaves only the first
difference at the two endpoints.

If `A` and `B` are ordinary primes, then

\[
\boxed{
\Delta v_A(F)=-t,
\qquad
\Delta v_B(F)=+t,
\qquad
\Delta v_p(F)=0\ (p\ne A,B).
}
\tag{L-24518.4}
\]

Thus one plateau transfers an arbitrary real amount of residual mass from one
prime row to another, with no leakage to any third prime.

If one endpoint is `1`, the same plateau creates or removes mass at a single
prime row because no prime divides `1`.

## 2. Exact prime-objective cost

For

\[
J_{\mathbb P,X}(b)=\sum_{p\le X}(\log p)v_p(b),
\]

equation (L-24518.4) gives

\[
\boxed{
\Delta J_{\mathbb P,X}
=t(\log B-\log A).
}
\tag{L-24518.5}
\]

This agrees with the physical plateau cost, since

\[
\sum_{j=A}^{B-1}
\log\frac{j^2}{j^2-1}
=\log\frac{A(B-1)}{(A-1)B}
\]

for the full prime-power objective, while after the prime-only projection the
endpoint potential is exactly `log rad(n)` and equals `log n` at prime
endpoints.

## 3. Complete transport cone

Let the primes through `X` be `p_1<...<p_N`, and let `r_i` be any real residual
vector. By combining prime-to-prime plateaus and prime-to-`1` plateaus, every
vector `s` satisfying

\[
s_i\le0
\]

is reachable from `r`; no sign condition on the flow is needed. If one insists
that prime-to-`1` plateaus only remove residual mass, then the reachable vectors
are exactly those with

\[
\sum_i s_i\le\sum_i r_i.
\tag{L-24518.6}
\]

For maximizing the final prime objective under this one-sided removal rule, the
optimal terminal vector is explicit. Put

\[
R=\sum_i r_i,
\qquad
W=\sum_i(\log p_i)r_i.
\tag{L-24518.7}
\]

- If `R>=0`, transport all positive and negative mass together and remove the
  remaining amount at endpoint `1`; the optimal terminal residual is `s=0`.
- If `R<0`, retain all unavoidable negative mass at the smallest weight,
  namely `p=2`: set `s_2=R` and `s_p=0` for `p>2`.

Therefore the least possible prime-objective loss is

\[
\boxed{
\mathcal L_{\min}(r)
=W-(\log2)\min(R,0).
}
\tag{L-24518.8}
\]

Equivalently, a prime-only correction with objective loss `O(log^2 X)` exists
if and only if

\[
\boxed{
\sum_{p\le X}(\log p)r_p
-(\log2)\min\left(\sum_{p\le X}r_p,0\right)
=O(\log^2X).
}
\tag{L-24518.9}
\]

## 4. Consequence for the carry route

After `L-24517`, no primitive-neighbor convergence theorem is needed to realize
an optimal ordinary-prime correction. The finite transport is exact and
constructive. The sole arithmetic problem is the scalar majorization
(L-24518.9) for the chosen seed residual.

For the parabolic seed, the first term in (L-24518.9) is

\[
J_{\mathbb P,X}(b_X^{(0)})-P_X,
\]

so a generic proof of (L-24518.9) would still prove the RH-bearing prime-ramp
bound. The theorem removes the graph-theoretic obstruction; it does not remove
the scalar arithmetic obstruction.

## 5. Relation to the Lagarias import

Lagarias's harmonic wrapper likewise removes endpoint and small-integer
bookkeeping from Robin's criterion while retaining one global divisor-sum
scalar. Here plateau transport removes every finite prime-constraint geometry
while retaining the weighted residual scalar. Both are elementary
normalizations, not automatic proofs of their arithmetic cores.

## Status boundary

The plateau identity and optimal finite transport are complete. The scalar
majorization (L-24518.9) remains the exact RH-bearing theorem.
