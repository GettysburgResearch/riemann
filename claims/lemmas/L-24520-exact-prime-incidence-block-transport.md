# L-24520 — Constant `b`-blocks give exact prime-incidence transport

Claim ID: `L-24520`  
Status: `PROPOSED — complete finite algebra`  
Scope: ordinary-prime correction after `L-24517`  
Issue: #245

The flow plateau of `L-24518` acts through second differences and transports
endpoint jump vectors. A different operation, performed directly in the
convexified `b`-coordinates, has a simpler exact effect.

For integers `1<=A<B<=X` and a real amount `t`, define

\[
\delta b_m=-t\,\mathbf1_{A<m\le B}.
\tag{L-24520.1}
\]

## 1. Incidence telescoping

For every prime power `q`,

\[
\begin{aligned}
\Delta v_q
&=\sum_{m=A+1}^{B}(-t)
 \left(\mathbf1_{q\mid m}-\mathbf1_{q\mid m-1}\right)\\
&=-t\left(\mathbf1_{q\mid B}-\mathbf1_{q\mid A}\right).
\end{aligned}
\]

Hence

\[
\boxed{
\Delta v_q
=t\mathbf1_{q\mid A}-t\mathbf1_{q\mid B}.
}
\tag{L-24520.2}
\]

This is endpoint incidence transport, not the endpoint-jump transport of a
flow plateau.

## 2. Pure ordinary-prime transfer

If `A=p` and `B=P` are distinct ordinary primes, then no other prime power
divides either endpoint. Therefore

\[
\boxed{
\Delta v_p=+t,
\qquad
\Delta v_P=-t,
\qquad
\Delta v_q=0\quad(q\ne p,P).
}
\tag{L-24520.3}
\]

Thus `t>0` moves residual mass from the larger prime `P` to the smaller prime
`p`, with no third-row leakage. Taking `t<0` moves mass in the opposite
direction.

If `A=1` and `B=P` is prime, equation (L-24520.2) reduces the single `P` row by
`t` and changes no other ordinary-prime row.

## 3. Exact objective change

The full carry objective changes by

\[
\begin{aligned}
\Delta J_X
&=-t\sum_{m=A+1}^{B}\log\frac m{m-1}\\
&=-t\log\frac BA.
\end{aligned}
\]

Therefore

\[
\boxed{J_X(b)-J_X(b+\delta b)=t\log(B/A).}
\tag{L-24520.4}
\]

For the ordinary-prime objective the same formula follows from
`Delta v_p=t`, `Delta v_P=-t`:

\[
\boxed{
J_{\mathbb P,X}(b)-J_{\mathbb P,X}(b+\delta b)
=t\log(P/p).
}
\tag{L-24520.5}
\]

Downward transport costs logarithmic distance. Upward transport has negative
loss, i.e. increases the objective.

## 4. Complete ordinary-prime transport geometry

Let the primes through `X` be `p_1<...<p_N`, and let `r_i` be any residual
vector. The incidence blocks between pairs of primes span every vector of total
mass zero. Adding blocks from endpoint `1` spans the whole prime coordinate
space.

Consequently every ordinary-prime residual can be made nonpositive by an
explicit finite combination of constant `b`-blocks. No primitive-neighbor,
Farey, divisor-chain, or spectral convergence theorem remains at the finite
geometric level.

## 5. Exact scalar firewall

For any correction producing a terminal residual `s_p<=0`, the objective loss
is

\[
\boxed{
\mathcal L
=\sum_{p\le X}(\log p)(r_p-s_p).
}
\tag{L-24520.6}
\]

The maximum possible terminal weighted residual under `s_p<=0` is zero.
Therefore the best correction whose terminal vector is allowed to be zero has
loss exactly

\[
\boxed{
\sum_{p\le X}(\log p)r_p
=J_{\mathbb P,X}(b)-P_X.
}
\tag{L-24520.7}
\]

Thus the two-prime transport theorem removes the graph obstruction completely,
but the optimum scalar is precisely the RH-bearing prime-ramp deficit. A generic
transport-cost argument cannot close it.

## 6. Correct proof boundary

The remaining mathematical question is no longer whether prime constraints can
be transported: they can, exactly. It is whether the specific parabolic
residual has subpower weighted positive deficit, or equivalently whether a
source-specific signed identity forces

\[
J_{\mathbb P,X}(b_X^{(0)})-P_X=X^{o(1)}.
\]

That statement is the prime-only RH criterion itself.

## Status boundary

The incidence transport and objective formulas are complete finite algebra.
They expose, but do not prove, the final scalar arithmetic bound.
