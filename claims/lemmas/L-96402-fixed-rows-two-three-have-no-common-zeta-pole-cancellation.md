# L-96402 — Fixed rows 2 and 3 have no common reciprocal-zeta pole cancellation

Claim ID: `L-96402`  
Status: **PROVED EXACT MELLIN ALGEBRA**  
Created: 2026-08-17  
RH status: **unproved**

For `j=2,3`, the fixed native row has Mellin transform

\[
\int_1^\infty c_X(j)X^{-s-1}\,dX
=
\frac{C_j}{s^2}
+
\frac{P_j(s+\tfrac12)}
{s^2\zeta(s+\tfrac12)}
\tag{L-96402.1}
\]

in its initial half-plane, followed by meromorphic continuation.

Put `z=s+1/2`, `x=2^{-z}`, and `y=3^{-z}`.  The two finite row numerators are

\[
P_2(z)=2x-1-y,
\tag{L-96402.2}
\]

\[
3P_3(z)=5y-x-1-3x^2.
\tag{L-96402.3}
\]

If both vanish, then `y=2x-1`, and substitution gives

\[
3P_3(z)
=
-3(x-1)(x-2).
\]

For `0<Re z<1`,

\[
\frac12<|x|<1,
\]

so neither `x=1` nor `x=2` is possible.  Therefore

\[
\boxed{
P_2(z)=P_3(z)=0,\quad 0<\Re z<1
\quad\text{has no solution}.
}
\tag{L-96402.4}
\]

Any nontrivial zeta zero off the critical line leaves a nonreal Mellin pole in
at least one of the two fixed rows.
