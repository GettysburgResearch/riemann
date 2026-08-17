# R-97300 — A 5:3-scalar-exact edge does not lift to two nonnegative rows

Claim ID: `R-97300`  
Status: **PROVED EXACT REFUTATION OF THE RECONSTRUCTED SCALAR-LIFT STEP**  
Created: 2026-08-17  
Depends on: `L-97301`  
RH status: **unproved**

Let

\[
q_i=Q_{Y_i}(2)>0,
\qquad
\rho_i=\frac{Q_{Y_i}(3)}{Q_{Y_i}(2)},
\qquad i\in\{o,e\},
\]

and suppose `Y_e>=Y_o>2`, so `rho_e>=rho_o` by `L-97301`.  The unique scalar
from PR #559 is

\[
R_*(Y)=5Q_Y(2)+3Q_Y(3)=Q_Y(2)(5+3\rho(Y)).
\]

Take odd demand coefficient `b>=0` and choose the even coefficient `u` by
**scalar exactness**

\[
uR_*(Y_e)=bR_*(Y_o).
\tag{R-97300.1}
\]

Then

\[
u=\frac{bq_o(5+3\rho_o)}{q_e(5+3\rho_e)}.
\]

The two row changes are exactly

\[
\boxed{
\Delta_2
=uQ_{Y_e}(2)-bQ_{Y_o}(2)
=-\frac{3bq_o(\rho_e-\rho_o)}{5+3\rho_e}\le0,
}
\tag{R-97300.2}
\]

\[
\boxed{
\Delta_3
=uQ_{Y_e}(3)-bQ_{Y_o}(3)
=\frac{5bq_o(\rho_e-\rho_o)}{5+3\rho_e}\ge0.
}
\tag{R-97300.3}
\]

Moreover

\[
5\Delta_2+3\Delta_3=0.
\tag{R-97300.4}
\]

If `Y_e>Y_o>3`, the ratio is strictly increasing and `Delta_2<0<Delta_3`.
Thus scalar exactness produces a row tradeoff, not simultaneous row
nonnegativity.

The formula quoted in the former completed-parity response,

\[
Q_{Y_e}(3)-\frac{Q_{Y_e}(2)}{Q_{Y_o}(2)}Q_{Y_o}(3)\ge0,
\]

is the row-2-exact formula of `L-97301.7` after rescaling.  Calling its
coefficient scalar-exact was the precise normalization error.

This refutation does not harm the scalar Mellin consumer: proving the scalar
`5c_X(2)+3c_X(3)` nonnegative would still be sufficient for RH.  It only
withdraws the claimed route from one scalar coupling to two positive rows.
