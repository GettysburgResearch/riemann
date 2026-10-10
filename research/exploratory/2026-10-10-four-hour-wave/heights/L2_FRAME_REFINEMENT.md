# A sharp Legendre frame and half-width annuli certify global order 6000

Status: proposed quantitative refinement; independent review required.
RH remains unproved. This file preserves and strengthens the independently
reviewed [L2_ANNULAR_PICK.md](L2_ANNULAR_PICK.md) deduction using the same
classical source and published argument/verified-height inputs.

## 1. Result

For the complete xi Pick kernel `K(x,y)=(F(x)+F(y))/(x+y)`, every packet of at
most **6000 positive nodes** is positive semidefinite, conditional on the
explicit classical and published inputs of the preceding packet. Distinct
nodes give positive definiteness. The deduction uses the classical strip
`a<=A=1/2`; it requires no new quasi-RH input.

For even `256<=n<=6000`, the new sufficient ratio is

\[
 \boxed{\mathcal R_*(n,A,H)=
 \frac{43659}{4096}\frac{n^3}{H}
 +\frac{1287495}{131072}A^2\frac{n^6}{H^2}
 +\frac{99}{20}A^2\frac{n^3+3n}{H^2}.}
 \tag{R1}
\]

The auxiliary guards below hold in this full range. At `n=6000`, `A=1/2`,
`H=3*10^12`,

\[
 \mathcal R_*=
 \frac{31206948706055875500099}{40000000000000000000000}
 <4/5.
 \tag{R2}
\]

Together with `mathcal R_*<1`, the guards prove global positivity as in the
preceding packet. Its moment congruence and complete-source summation are
unchanged; no node-size restriction is introduced.

## 2. Sharp elementary L2 and two-endpoint bounds

With `m=d+1` and Legendre degree bound `d`, the derivative matrix's exact
squared Frobenius norm is

\[
 \sum_{k=1}^d\sum_{j<k,\,j+k\text{ odd}}(2k+1)(2j+1)
 =\frac{d(d+1)^2(d+2)}4\le\frac{m^4}4.
\]

Thus the L2 derivative inequality improves to

\[
 \|R^{(j)}\|_2\le(m^2/2)^j\|R\|_2.
 \tag{R3}
\]

The two endpoint evaluation vectors in the orthonormal basis have squared
norm `m^2/2` and inner product `(-1)^d m/2`. The two nonzero eigenvalues of
their combined evaluation operator are `(m^2 +/- m)/2`. Hence

\[
 |R(-1)|^2+|R(1)|^2\le\frac{m^2+m}{2}Q,
 \quad Q=\int_{-1}^1R^2.
 \tag{R4}
\]

These bounds include the correlation between endpoint evaluations. The
preceding packet bounded them individually and used a larger Frobenius
constant. Both sharper identities are elementary exact finite formulas.

## 3. Half-width annuli and the weighted variation bound

Take now

\[
 r=1+1/(2n),\quad J=[1,r^2],\quad
 h=|J|/2=1/(2n)+1/(8n^2).
 \tag{R5}
\]

Use the same normalized source weights `phi,psi_j` and polynomial `R(t)`.
The complete count discrepancy gives the same factor `(9/16)log L` in
Stieltjes integration by parts. The main density remains between
`LhlogL/9` and `LhlogL/6`.

For real `v in J`, `phi(v)<=1`, `psi_j(v)<=r^2`, and
`|d psi_j/dv|<=r^2(n+1)`. Equations (R3)--(R4) show that the endpoint-plus-
variation norm of `psi_j R^2` is bounded by

\[
 r^2\left[\frac{3m^2+m}{2}+h(n+1)\right]Q
 =r^2\left[\frac{3n^2}{8}+\frac n4+h(n+1)\right]Q
 \le\frac{49}{128}n^2Q.
 \tag{R6}
\]

The last rational inequality holds for every even `n>=256` in the stated
range and is checked for every such order by the replay. For the unweighted
square, its endpoint-plus-variation bound is smaller than the same right
side.

Also

\[
 \phi(v)\ge r^{-2n}>4/11,\qquad \psi_j(v)>4/11,
 \tag{R7}
\]

because `(1+1/(2n))^(2n)<e<11/4` and `v>=1`.
The main reference reserve is therefore `4LhlogL Q/99`.

## 4. Sampling and variable-shift guards

The unweighted discrete sampling bound becomes

\[
 \sum w|P(v)|^2
 \le Lh\log L\left[\frac16+\frac{441}{1024}\frac{n^3}{L}\right]Q
 \le\frac15 Lh\log L\,Q.
 \tag{R8}
\]

Here `1/h<=2n`. This is the principal auxiliary guard, and at `n=6000` its
bracket is about `0.19767448<1/5`.

The sharper derivative operator gives

\[
 D_P=m^2/(2h)\le n^3/4.
\]

The preceding packet's variable-complex-shift Taylor/Minkowski argument thus
retains the same `kappa=17/16` and the same rational bounds
`|psi|<=2, |psi'|<=3n, |psi''|<=4n^2`, provided

\[
 5n^3/(16H)<=1/32,\qquad nA^2/H^2<1/17,
\]

and the same elementary segment/derivative guards. Every guard holds at
`n=6000` and is checked throughout the declared even-order range.
The real horizontal displacement `-a^2/L^2` remains included.

## 5. Revised domination coefficients

The complete-count quadrature loss is at most
`(9/16)logL*(49/128)n^2Q`. Divide by the main reserve `4LhlogLQ/99` and use
`1/h<=2n`: the relative loss is at most

\[
 (43659/4096)n^3/L.
\]

The previous integrated strip error (L16) still holds, since the sampling
constant and upper derivative scale are unchanged. Divide that error by the
new main reserve. Its quadratic coefficient is

\[
 (99/4)(45/128)(17/16)^2=1287495/131072,
\]

and its linear real-shift coefficient is `(99/4)/5=99/20`.
Thus the complete relative loss is exactly bounded by (R1), with `H`
replaced by `L`. This decreases on the annuli `L=H r^k`.

All normalized moment quadratic forms are strictly positive. The exact
arbitrary-node congruence, the verified low critical source, and complete
source convergence prove section 1 exactly as in the preceding packet.

The finite order and finite verified height are essential. This remains a
large fixed hierarchy, not an all-order statement or a proof of RH.

## 6. Replay boundary

[verify_l2_refinement.py](verify_l2_refinement.py) checks (R2), every declared
auxiliary order, the sharp Frobenius and two-endpoint identities, and inherited
proof hashes. Normal and optimized outputs are compared. The complete source,
published `S(T)` estimate, and published verified height remain imported;
finite arithmetic does not independently establish those analytic inputs.
