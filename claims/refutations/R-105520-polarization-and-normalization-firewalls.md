# R-105520 — Polarization and normalization firewalls for a false 90% proof

Claim ID: `R-105520`  
Status: **PROVED EXACT FIREWALLS**  
Created: 2026-08-24  
RH status: **unproved**

## 1. The missing half order

For a Dirichlet polynomial

\[
D(t)=\sum_n c_n n^{-it},
\]

Montgomery--Vaughan gives diagonal energy \(\sum|c_n|^2\).  Therefore the
formula

\[
1+2\Re\sum a(n)n^{-it}
\]

cannot have diagonal energy \(\sum a(n)^2/n\).  The latter belongs to

\[
1+2\Re\sum a(n)n^{-1/2-it}.
\]

The old display in `L-105322` omitted this factor.  `L-105520` repairs it.

## 2. Physical cutoff scaling cannot be suppressed

At cutoff \(e^{\alpha L}\), the simplex is
\(\sum u_j\le\alpha\), and degree \(m\) gains
\(\alpha^{2m}\).  Using \(\mathcal D_K(1)\) at \(\alpha\ne1\) is invalid.
The corrected degree-four estimate at \(\alpha=2\) remains strong, but this
must be proved rather than assumed.

## 3. Pointwise Hermitian polarization is not the formal square

For a holomorphic scalar \(p\), define

\[
p^\#(z)=\overline{p(\bar z)}.
\]

A Hermitian analytic compression formed from \(p\phi_j\) contains
\(p(z)p^\#(z)\) on an off-real contour, not \(p(z)^2\).

For example, with

\[
p(z)=1+\varepsilon e^{-iaz},
\]

\[
p(z)^2
=
1+2\varepsilon e^{-iaz}
+\varepsilon^2e^{-2iaz},
\]

whereas

\[
p(z)p^\#(z)
=
1+\varepsilon(e^{-iaz}+e^{iaz})+\varepsilon^2.
\]

On \(z=t-i\eta\), the two linear terms have relative size \(e^{2a\eta}\).
Thus the positive formal identity
\(P_K(x)^2/(1-x)\) cannot be inserted into the off-real Hermitian Xi contour
without a proved Hardy/strip intertwiner.

## 4. Safe-line positivity is not the conclusion

For a contraction \(X\), `L-105522` proves

\[
2\Re(I-X)^{-1}\succeq I.
\]

If this positive safe-line operator could be identified with the complete
residue form up to an automatically negligible error, the zero problem would
already be solved.  The left-edge, vertical, taper, and analytic-polarization
remainder is therefore conclusion-bearing.  Treating it as a routine
\(o(N)\) term is circular.

These firewalls refute a false unconditional ninety-percent proof while
preserving the model and full-signature advances.
