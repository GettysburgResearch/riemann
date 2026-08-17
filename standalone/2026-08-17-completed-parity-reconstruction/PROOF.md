# Completed parity, terminal row ratios, and the exact scalar Lorenz frontier

**Scientific status:** exact reconstruction and downgrade.  The uniform producer
remains open.  The Riemann Hypothesis is unproved.

## 1. The source ledger must finish parity before observation

For a squarefree native index

\[
k=d p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad 67\le p_1<\cdots<p_t,
\]

rough placement preserves both the activation `X/k` and coefficient magnitude
`k^{-1/2}`.  It swaps the even and odd source channels once per rough prime.
The correct terminal owner is therefore

\[
\omega_\ell S^{|h_\ell|}\mathscr P_\ell,
\]

not a parity-blind canonical packet.  At each fixed `X` the full expansion is
finite.  Complete colour grouping and every fixed row scalar commute with the
swap and preserve `(-1)^|h|`.

This validates the order “complete history, then observe,” but it does not
supply a positive realization of a swapped leaf.

## 2. The odd terminal remains fatal to leafwise gluing

At

\[
X=67\cdot71\cdot13,
\qquad h=(67),
\qquad(p,y)=(71,13),
\]

PR #561 certifies

\[
E_T-O_T>17.
\]

The incoming history is odd, so exact target realization requires the reversed
orientation `O_T>=E_T`.  It is impossible.  No component-row inequality can
alter this target-coordinate failure.

## 3. A new exact terminal ratio theorem

The canonical rows satisfy

\[
Q_Y(2)=3h_2+\sum_{m\ge4}h_m,
\qquad
Q_Y(3)=2h_3-\frac23h_4+rac13\sum_{m\ge5}h_m,
\]

where `h_m(Y)=m^{-1/2} log(Y/m)_+`.  Hence

\[
3Q_Y(3)-Q_Y(2)=3(2h_3-h_4-h_2).
\]

For `Y>=4`, the right side is affine in `log Y`.  On each activation cell,
writing `Q_Y(2)=S_N log Y-T_N`, direct differentiation gives

\[
\frac{d}{dY}\frac{Q_Y(3)}{Q_Y(2)}
=\frac{B S_N-A T_N}{YQ_Y(2)^2}>0,
\]

with `A<0<B`.  The ratio is zero on `(2,3]`, increases on `(3,4)`, and is
continuous at every knot.  Therefore

\[
\rho(Y)=Q_Y(3)/Q_Y(2)
\]

is globally nondecreasing.

This proves that a row-2-exact edge to a later endpoint is automatically
row-3 superordinate.

## 4. Why the previous scalar lift was still wrong

The `5:3` scalar is

\[
R_*(Y)=Q_Y(2)(5+3\rho(Y)).
\]

For a scalar-exact edge from `Y_o` to `Y_e>=Y_o`, the row changes are

\[
\Delta_2=-\frac{3bQ_{Y_o}(2)(\rho_e-\rho_o)}{5+3\rho_e},
\qquad
\Delta_3=\frac{5bQ_{Y_o}(2)(\rho_e-\rho_o)}{5+3\rho_e}.
\]

Thus the scalar exact edge has a negative row-2 change and a positive row-3
change whenever the endpoints are distinct above `3`.  The former response
inserted the coefficient for row-2 exactness while describing it as scalar
exactness.  The terminal ratio lemma survives; the scalar-to-two-row promotion
does not.

## 5. Exact finite global replacement

Once all histories and parities are retained, let even source atom `i` have
capacity `a_i`, target `t_i>0`, and scalar row `r_i`.  Let the complete odd
source demand target `T_O` and scalar `R_O`.  The common-source scalar producer
at this endpoint asks for

\[
0\le u_i\le a_i,
\qquad
\sum t_i u_i=T_O,
\qquad
\sum r_i u_i\ge R_O.
\]

This is an exact finite LP.  Sort atoms by `r_i/t_i` in decreasing order and
fill target capacity in that order.  The resulting fractional-knapsack value
`Phi_X(T_O)` is the maximum possible scalar response.  Equivalently,

\[
\Phi_X(T)=\min_\lambda
\left[\lambda T+\sum_i a_i(r_i-\lambda t_i)_+\right].
\]

Thus the all-depth problem has one precise finite Lorenz gate at every endpoint
and one explicit separating threshold when it fails.

## 6. Conditional analytic finish

The scalar Mellin transform is

\[
\int_1^\infty \mathcal R_X X^{-s-1}\,dX
=
\frac6{s^2}-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)},
\qquad z=s+\frac12.
\]

The numerator is `-3(1-2^{-z})(2-2^{-z})`, zero-free for `Re z>0`.
Therefore uniform completed-parity scalar Lorenz feasibility implies
`mathcal R_X>=0`, and the fixed-sign Mellin-Landau consumer implies RH.

The uniform Lorenz inequality is not proved.  It is the exact remaining
RH-bearing producer `CPSL67`, synonymous at this scope with `GPHT*` and
`ASHP67`.

## 7. Final status

\[
\boxed{
\text{completed parity and finite LP reduction: proved};\qquad
\text{uniform scalar producer: open};\qquad
\text{RH: unproved}.}
\]
