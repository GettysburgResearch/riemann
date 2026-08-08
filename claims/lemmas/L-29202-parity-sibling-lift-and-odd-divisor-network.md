# L-29202 — Parity-sibling lift and odd-divisor network

Claim ID: `L-29202`  
Title: Three nonnegative parity siblings preserve every even carry column and turn the odd-column correction into a capacitated divisor-dipole flow  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: atomized carry identity; PR #272 dyadic divergence commutator; PR #285 Mersenne support menu  
Scope: exact factor-two source map and max-flow reduction; positivity of the required network flow is not asserted

## 1. Three parity siblings

Fix a lower split

\[
e=[n,j],
\qquad k=n-j.
\]

Define the three upper splits

\[
\begin{aligned}
e_0&=[2n,2j],\\
e_1&=[2n+1,2j],\\
e_2&=[2n+1,2j+1].
\end{aligned}
\tag{L-29202.1}
\]

The omitted child of `e_1` is `2k+1`; the omitted child of `e_2` is `2k`.
All identities below are orientation independent.

## 2. Exact even-column preservation

For every integer `q>=1`,

\[
\boxed{
\chi_{e_0}(2q)
=\chi_{e_1}(2q)
=\chi_{e_2}(2q)
=\chi_e(q).
}
\tag{L-29202.2}
\]

For example,

\[
\left\lfloor\frac{2n+1}{2q}\right\rfloor
=\left\lfloor\frac nq\right\rfloor,
\qquad
\left\lfloor\frac{2k+1}{2q}\right\rfloor
=\left\lfloor\frac kq\right\rfloor.
\]

Thus replacing a mass `c` on `e_0` by any nonnegative distribution

\[
(c-x-y)e_0+xe_1+ye_2,
\qquad x,y>=0,\quad x+y<=c,
\tag{L-29202.3}
\]

leaves every even carry column unchanged.

## 3. Odd-column divisor dipoles

For every integer `q>=2`, the unit-increment identity

\[
\left\lfloor\frac{a+1}{q}\right\rfloor
 -\left\lfloor\frac aq\right\rfloor
=\mathbf1_{q\mid a+1}
\]

gives

\[
\boxed{
\chi_{e_1}(q)-\chi_{e_0}(q)
=\mathbf1_{q\mid2n+1}-\mathbf1_{q\mid2k+1},
}
\tag{L-29202.4}
\]

and

\[
\boxed{
\chi_{e_2}(q)-\chi_{e_0}(q)
=\mathbf1_{q\mid2n+1}-\mathbf1_{q\mid2j+1}.
}
\tag{L-29202.5}
\]

The right sides vanish automatically for even `q`.  On odd columns, `e_1`
moves one divisor-incidence unit from the odd child `2k+1` to the odd parent
`2n+1`; `e_2` performs the same move from `2j+1`.

No norm, asymptotic estimate, or Möbius cancellation enters these identities.

## 4. A lifted lower flow

Let `Y>=2`, put `X=2Y`, and let `d` be a nonnegative lower flow.  Write

\[
\alpha=2^{-1/2}.
\]

The baseline even lift assigns mass `alpha d_e` to `e_0` for every lower edge.
For every even column `2q`, `q>=2`, its load is

\[
\alpha L_q(d).
\]

If `d` saturates the critical lower target, then

\[
\alpha L_q(d)
=\alpha q^{-1/2}\log(Y/q)
=(2q)^{-1/2}\log(X/(2q))
=w_X(2q).
\tag{L-29202.6}
\]

The separate bottom edge `[2,1]` with coefficient `w_X(2)` supplies column two.
Thus the factor-two lift solves every even column exactly before any odd repair.

## 5. The odd residual

Let `L^0_X(q)` be the carry load of the baseline lift and bottom edge, and put

\[
h_X(q)=w_X(q)-L^0_X(q).
\tag{L-29202.7}
\]

Equation (L-29202.6) gives

\[
h_X(2q)=0.
\tag{L-29202.8}
\]

For odd `m`, define the odd-multiple Möbius transform

\[
\boxed{
z_X(m)
=\sum_{\substack{a\ge1\\a\text{ odd}\\am\le X}}
\mu(a)h_X(am).
}
\tag{L-29202.9}
\]

Then finite Möbius inversion on odd multiples gives

\[
\boxed{
h_X(q)=
\sum_{\substack{m\le X\\m\text{ odd}\\q\mid m}}z_X(m)
\qquad(q\text{ odd}).}
\tag{L-29202.10}
\]

Thus the complete odd-column discrepancy is encoded by one explicit charge on
odd nodes.

## 6. Capacitated odd-node network

For every lower edge `e=[n,j]` of mass `d_e`, introduce two directed arcs

\[
2k+1\longrightarrow2n+1,
\qquad
2j+1\longrightarrow2n+1,
\tag{L-29202.11}
\]

with a **shared** capacity

\[
x_e+y_e\le\alpha d_e.
\tag{L-29202.12}
\]

Let `B_odd` be the node-incidence matrix of these arcs, with `+1` at the head and
`-1` at the tail.  Equations (L-29202.4)--(L-29202.5) prove the exact equivalence

\[
\boxed{
\begin{gathered}
0\le x_e,\quad0\le y_e,\quad x_e+y_e\le\alpha d_e,\\
B_{\rm odd}(x,y)=z_X
\end{gathered}
}
\tag{L-29202.13}
\]

if and only if replacing the baseline masses according to (L-29202.3) corrects
every odd carry column exactly.

This is a finite capacitated transshipment problem.  It contains no hidden
analytic estimate.

## 7. Exact cut alternative

Finite linear-programming duality gives a fail-closed criterion.  The network
system (L-29202.13) is feasible if and only if, for every real potential `phi`
on odd nodes,

\[
\boxed{
\sum_m z_X(m)\phi(m)
\le
\alpha\sum_e d_e
\max\bigl(
0,
\phi(2n+1)-\phi(2j+1),
\phi(2n+1)-\phi(2k+1)
\bigr).
}
\tag{L-29202.14]
\]

The closing bracket in the tag is typographical only.  This is the support
function of the shared-capacity triangle
`{(x,y):x,y>=0,x+y<=alpha d_e}`.

A primal proof emits every sibling allocation.  A dual refutation emits one
potential violating (L-29202.14).

## 8. Compatibility with the Mersenne menu

If the lower parent `n` is not Mersenne and its split lies in the binary central
window, all three upper siblings in (L-29202.1), when their parents do not exceed
`X`, lie in the upper binary central window.

For a lower Mersenne extreme edge, the local even lift need not lie in the upper
MCF menu.  Those edges form the declared boundary state.  By `L-29201`, their
total mass is already `O(log Y)`.  A complete induction must reconstruct their
upper image by a source-bound Pascal/tree ledger; it may not silently use the
forbidden lifted edge.

Thus the factor-two construction splits exactly into:

```text
ordinary central edges  -> finite odd-divisor network;
Mersenne extreme edges  -> logarithmic boundary reconstruction;
endpoint Y              -> one finite top correction.
```

## 9. Relation to the live proof graph

- PR #272's adjacent-tree commutator is the divergence-coordinate form of the
  charge `z_X`.
- PR #269's odd-column leakage is the carry-column form of the same network.
- PR #263's parity frame supplies the physical two-channel interpretation.
- PR #285's Mersenne collar identifies the only support exception.

The present lemma puts those descriptions into one exact positive-allocation
problem.

## 10. Proof boundary

Closed exactly:

- the three sibling identities;
- preservation of every even carry column;
- odd-column correction as divisor dipoles;
- odd Möbius decoding;
- the capacitated network and its exact cut dual;
- support preservation away from the Mersenne boundary.

Open:

- feasibility of the source-specific network at all scales;
- positive reconstruction of the logarithmic Mersenne boundary state;
- support-feasible MCF and RH.
