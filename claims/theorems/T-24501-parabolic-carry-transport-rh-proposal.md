# T-24501 — Parabolic carry transport full RH proposal

Claim ID: `T-24501`  
Status: `FULL PROPOSAL — one primitive-neighbor contraction theorem open`  
Scope: full Riemann Hypothesis conditional on PNC  
Issue: #245

## 1. Prime ramp

Define

\[
S_X=\sum_{q=p^a\le X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\]

By `L-24501`, every feasible point `b` of the prime-power divisor-gradient LP satisfies

\[
S_X\ge J_X(b),
\qquad
J_X(b)=\sum_{m=2}^Xb_m\log\frac m{m-1}.
\]

By `L-24502`, the explicit parabolic seed satisfies

\[
J_X(b_X^{(0)})\ge4\sqrt X-6\log X+O(1).
\]

Thus the only task is to repair its positive prime-power constraint excess at polylogarithmic objective cost while preserving `b_m>=0`.

## 2. Primitive-Neighbor Contraction (PNC)

Fix rational `0<alpha<beta<1` and an unbounded sequence of taper orders `R`. Define `phi_{X,R}`, `C_{X,R}(q,d)`, and

\[
A_d=-C_{X,R}(d,d)>0
\]

on the active divisor-comb coordinates.

Let

\[
r_q^{(s)}=v_q(b^{(s)})-w_X(q),
\qquad
e_q^{(s)}=(r_q^{(s)})_+.
\]

Starting with `T_d^(0)=0`, iterate

\[
\boxed{
T_d^{(s+1)}=T_d^{(s)}+\frac12\frac{e_d^{(s)}}{A_d}
}
\tag{T-24501.1}
\]

for prime powers `d` with `A_d>0`, define

\[
F^{(s)}(j)=\phi_{X,R}(j)\sum_{d\mid j}T_d^{(s)},
\]

and

\[
b_m^{(s)}=b_X^{(0)}(m)+F^{(s)}_{m-1}-F^{(s)}_m.
\]

The proposed Primitive-Neighbor Contraction theorem is:

\[
\boxed{
\begin{aligned}
&b_m^{(s)}\ge0\quad\text{for all }m,s,\\
&e_q^{(s)}\to0\quad\text{for every prime power }q,\\
&\sum_{j=2}^{X-1}F_j^{(\infty)}\log\frac{j^2}{j^2-1}=O(\log^2X),\\
&\text{prime powers with }A_q=0\text{ retain nonpositive residual.}
\end{aligned}}
\tag{PNC}
\]

By `L-24503`, all noncoprime interactions are favorable and all harmful cross-interactions are balanced primitive determinant-one equations `ad-bq=+-1`.

## 3. PNC implies the sharp prime-ramp lower bound

If PNC holds, the limiting vector `b^(infinity)` is feasible and `L-24502` gives

\[
\begin{aligned}
J_X(b^{(\infty)})
&=J_X(b_X^{(0)})
-\sum_{j=2}^{X-1}F_j^{(\infty)}\log\frac{j^2}{j^2-1}\\
&\ge4\sqrt X-O(\log^2X).
\end{aligned}
\]

Therefore

\[
\boxed{S_X\ge4\sqrt X-O(\log^2X).}
\tag{T-24501.2}
\]

## 4. Transfer to RH

The repository's square-screw / prime-ramp transfer identifies the exact archimedean main term `4 sqrt(X)` and shows that the lower bound

\[
S_X\ge4\sqrt X-O(\log^2X)
\]

forces a subpower negative square-screw envelope. The Landau continuation argument then excludes nontrivial zeta zeros with real part greater than `1/2`; functional-equation symmetry gives RH.

Thus

\[
\boxed{\mathrm{PNC}\Longrightarrow\mathrm{RH}.}
\tag{T-24501.3}
\]

## 5. Mandatory Mertens firewall

Convexification does not erase the arithmetic difficulty. For the exact carry inverse, the first integrated coordinate is

\[
\boxed{
b_{X,2}=-\sum_{2\le n\le X}\frac{\mu(n)}{\sqrt n}\log\frac Xn.}
\tag{T-24501.4}
\]

Any proof of PNC must therefore reproduce the coherent smoothed-Mertens channel. A generic unsigned norm or rowwise absolute-value estimate is not acceptable.

## 6. Review protocol

Review in this order:

1. `L-24501` finite second-difference identities and LP duality;
2. `L-24502` seed and exact objective/correction identities;
3. `L-24503` gcd ledger and primitive-neighbor reduction;
4. high-order elimination of `qd<<X` cells;
5. PNC itself, including preservation of `b>=0`, terminal coordinates, and total objective cost;
6. the first-coordinate Mertens firewall;
7. the existing square-screw/Landau transfer.

One reachable primitive-neighbor cycle with gain at least one, one terminal positive residual, one forced negative `b_m`, or a correction cost of polynomial size rejects this proposal.

## Status boundary

This is an unmistakable full architecture, not a claim that RH has been proved. The sole new load-bearing theorem is PNC (or the stronger Divisibility Cover Theorem of `L-24502`).
