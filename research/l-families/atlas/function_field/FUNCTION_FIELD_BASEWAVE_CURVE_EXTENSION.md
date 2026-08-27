# The complete base-wave shadow on a curve is controlled by its Frobenius numerator

Status: **exact all-curve Euler factorization and sharp coefficient-growth
consequence from Weil; bounded symbolic replay; no point enumeration,
WAVEPRIMCAR, number-field, GRH, or RH theorem**

Bounded replay:
[function_field_basewave_curve_extension.py](function_field_basewave_curve_extension.py).
Canonical summary:
[function_field_basewave_curve_extension.json](function_field_basewave_curve_extension.json).

This packet extends the frozen genus-zero packet
[FUNCTION_FIELD_BASEWAVE_SHADOW.md](FUNCTION_FIELD_BASEWAVE_SHADOW.md).
The replay pins that frozen predecessor at commit \(e87f2392f\) by its four
commit-object blob hashes.
The frozen ancestry is
\(b870366141fe8d5f43d5b81f6e50a67d2a888070\).

## 0. Outcome

Let \(C/\mathbf F_q\) be a fixed smooth projective geometrically connected
curve.  Let \(\Sigma\) be a finite set of closed points and put
\[
 Z_C(u)={P_C(u)\over(1-u)(1-qu)},\qquad
 P_C(u)=\prod_{\nu=1}^{2g}(1-\alpha_\nu u),
 \qquad |\alpha_\nu|=\sqrt q.
\]
For \(d_v=\deg(v)\), define the complete oriented product
\[
 F_{C,\Sigma}(X,Y)=
 \prod_{v\notin\Sigma}
 \left(1-q^{-d_v/2}X^{d_v}-q^{-d_v/2}Y^{d_v}\right).
\tag{0.1}
\]
Then
\[
 \boxed{
 F_{C,\Sigma}(X,Y)=
 {\mathcal J_{C,\Sigma}(X,Y)\over
  Z_C(X/\sqrt q)\,Z_C(Y/\sqrt q)\,Z_C(XY/q)\,
  D_\Sigma(X,Y)},}
\tag{0.2}
\]
where
\[
 D_\Sigma=
 \prod_{v\in\Sigma}
 (1-q^{-d_v/2}X^{d_v})
 (1-q^{-d_v/2}Y^{d_v})
 (1-q^{-d_v}(XY)^{d_v}).
\tag{0.3}
\]
The residual Euler product \(\mathcal J_{C,\Sigma}\) is analytic on every
closed bidisc \(|X|,|Y|\le r\) with \(r^3<\sqrt q\).

Thus the three genus-zero inverse-zeta zeros persist, but in positive genus
they are divided by the Frobenius numerator channels.  If
\[
 P_C(X/\sqrt q)=\prod_\lambda(1-\lambda X)^{m_\lambda},
 \qquad |\lambda|=1,\qquad m_C=\max_\lambda m_\lambda,
\tag{0.4}
\]
and \(c_{i,j}=[X^iY^j]F_{C,\Sigma}\), then
\[
 \boxed{
 c_{i,j}
 =O_{C,\Sigma}\!\left(
 (i+1)^{m_C-1}(j+1)^{m_C-1}\right).}
\tag{0.5}
\]
This is the sharp general consequence available from Weil plus the pole
multiplicities.  The unconditional all-curve conclusion is a polynomial
bound, not an exponential-decay theorem; particular residue combinations
may still cancel.

For any fixed finite ratio kernel and fixed exceptional orientation, its
degree-\(h\) shell therefore satisfies
\[
 S_h^\alpha=O_{C,\Sigma,\alpha,r}
 \left((1+h)^{2m_C-2}\right).
\tag{0.6}
\]
If the normalized Frobenius roots are simple, this becomes \(O(1)\).
The coarse bound \(m_C\le2g\) gives
\(O((1+h)^{4g-2})\) for \(g\ge1\).  These bounds are subpower in the norm
height \(q^h\), but they neither tend to zero in general nor imply
\(\ell^2\)-summability of the shells.

## 1. Local-to-global proof

At a point of degree \(d\), set
\[
 a=q^{-d/2}X^d,\qquad b=q^{-d/2}Y^d.
\]
The exact local identity
\[
 (1-a)(1-b)(1-ab)-(1-a-b)=ab(a+b-ab)
\tag{1.1}
\]
gives
\[
 1-a-b=(1-a)(1-b)(1-ab)\mathcal J_d(a,b),
\qquad
 \mathcal J_d=1+O(a^2b+ab^2).
\tag{1.2}
\]
For any parameter \(u\),
\[
 \prod_{v\notin\Sigma}(1-u^{d_v})
 ={1\over Z_C(u)\prod_{v\in\Sigma}(1-u^{d_v})}.
\tag{1.3}
\]
Applying (1.3) to \(X/\sqrt q\), \(Y/\sqrt q\), and \(XY/q\)
proves (0.2)--(0.3).  Notice the direction of the deletion factor:
deleting a place divides the complete inverse-zeta product by its local
factor, so \(D_\Sigma\) belongs in the denominator.
Here, explicitly,
\[
 \mathcal J_{C,\Sigma}(X,Y)=
 \prod_{v\notin\Sigma}
 \mathcal J_{d_v}\!\left(
 q^{-d_v/2}X^{d_v},q^{-d_v/2}Y^{d_v}\right).
\tag{1.4}
\]

If a modulus is \(\mathfrak m=\prod_vv^{e_v}\), squarefree avoidance depends
only on \(\operatorname{supp}\mathfrak m\).  The exponents \(e_v\) do not
enter (0.3).  Distinct deleted points of the same degree contribute repeated
factors; their degrees must not be deduplicated.

For \(C=\mathbf P^1\), deleting the point at infinity gives
\[
 {1\over Z_{\mathbf P^1}(u)(1-u)}=1-qu.
\tag{1.5}
\]
Consequently (0.2) specializes exactly to the affine genus-zero factors
\((1-\sqrt qX)(1-\sqrt qY)(1-XY)\) in the shadow packet.

## 2. Residual convergence

Write \(N_C(d)\) for the number of closed points of degree \(d\).  Weil gives
\[
 N_C(d)=O_C(q^d/d).
\tag{2.1}
\]
On \(|X|,|Y|\le r\), the first nonconstant residual terms have total local
degree three, so
\[
 |\mathcal J_d-1|
 \ll_{C,r}\left({r^3\over q^{3/2}}\right)^d.
\tag{2.2}
\]
Therefore
\[
 \sum_{d\ge1}N_C(d)|\mathcal J_d-1|
 \ll_C\sum_{d\ge1}{1\over d}
 \left({r^3\over\sqrt q}\right)^d<\infty
\tag{2.3}
\]
whenever \(r^3<\sqrt q\).  Removing finitely many places does not change
this domain.

## 3. Frobenius residues and coefficient growth

The mixed reciprocal factor
\(1/P_C(XY/q)\) can become singular only when
\(|XY|=\sqrt q\).  Deleted axis factors first become singular at
\(|X|=\sqrt q\) or \(|Y|=\sqrt q\), and deleted mixed factors at
\(|XY|=q\).  Hence
\[
 G_{C,\Sigma}(X,Y)=
 P_C(X/\sqrt q)P_C(Y/\sqrt q)F_{C,\Sigma}(X,Y)
\tag{3.1}
\]
is analytic on a bidisc of radius \(R>1\), for example any
\(1<R<q^{1/6}\).

Partial fractions on the unit circle give
\[
 [X^n]{1\over P_C(X/\sqrt q)}
 =\sum_\lambda Q_\lambda(n)\lambda^n,
 \qquad \deg Q_\lambda\le m_\lambda-1.
\tag{3.2}
\]
Convolving (3.2) twice with the exponentially decaying coefficients of
\(G_{C,\Sigma}\) proves (0.5).  More sharply, for every two fixed integer
offsets \(a,b\), there are polynomials \(Q_{\lambda,\mu}^{a,b}\) such that
\[
 c_{h+a,h+b}
 =\sum_{\lambda,\mu}
 Q_{\lambda,\mu}^{a,b}(h)(\lambda\mu)^h+O(R^{-h}),
 \qquad
 \deg Q_{\lambda,\mu}^{a,b}
 \le m_\lambda+m_\mu-2
\tag{3.3}
\]
for some \(R>1\).  Indeed, extend the exponentially convergent convolution
to all coefficients of \(G_{C,\Sigma}\); the omitted tails are exponential,
and the infinite polynomial moments are derivatives of \(G_{C,\Sigma}\) at
unit-modulus points.  Thus every fixed-ratio shell is a finite
unit-circle exponential-polynomial plus an exponentially decaying error.
The formula permits complete residue cancellation, but does not assert it.

A repeated normalized root of multiplicity \(m\) already produces
\[
 [X^n](1-X)^{-m}={n+m-1\choose m-1},
\tag{3.4}
\]
so Weil alone cannot improve the exponent attached to that multiplicity.

Equation (0.6) follows because a fixed ratio support leaves only \(O(1)\)
bidegrees on the height shell, with \(i,j=h+O(1)\).

## 4. What this does and does not say

The theorem cleanly answers the positive-genus question posed by the shadow
packet:

- the exact three-zeta factorization extends to every fixed curve;
- a finite deleted-place modulus is tracked exactly by (0.3);
- positive genus can introduce unit-circle Frobenius residues, so only at
  most polynomial degree growth follows uniformly from Weil;
- simple Frobenius roots yield bounded complete shells.

It does **not** prove cancellation among the oscillatory terms in (3.2).
Special curves, repeated roots, or aligned shell phases can prevent decay.
It also omits nontrivial cores, the harmonic \(d\)-average, incomplete
owner/Boolean restrictions, and nonzero incidence modes.  Consequently it
does not prove WAVEPRIMCAR, PRIMCAR, RH, or GRH, and it supplies no
number-field estimate.

## 5. Proof ledger

| statement | grade |
|---|---|
| local cubic identity (1.1) | **PROVED EXACT** |
| all-curve factorization (0.2) | **PROVED EXACT FROM THE CURVE EULER PRODUCT** |
| finite deleted-place factor (0.3) | **PROVED EXACT; SUPPORT ONLY** |
| residual convergence for \(r^3<\sqrt q\) | **PROVED FROM WEIL** |
| coefficient bound (0.5) | **PROVED BY PARTIAL FRACTIONS AND CAUCHY** |
| unit-circle residue expansion (3.3) | **PROVED FOR FIXED JOINT OFFSETS** |
| fixed-ratio shell bound (0.6) | **PROVED** |
| repeated-pole coefficients through degree 16 | **REPLAYED EXACT SYMBOLICALLY** |
| curve or point examples | **NOT ENUMERATED** |
| exponential decay in positive genus | **NOT CLAIMED** |
| WAVEPRIMCAR, PRIMCAR, RH, or GRH | **NOT PROVED** |

## 6. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/function_field_basewave_curve_extension.py --check
python -B -O research/l-families/atlas/function_field/function_field_basewave_curve_extension.py --check
python -B -m unittest tests.test_function_field_basewave_curve_extension
python -B -O -m unittest tests.test_function_field_basewave_curve_extension
python -B -m ruff check research/l-families/atlas/function_field/function_field_basewave_curve_extension.py tests/test_function_field_basewave_curve_extension.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_basewave_curve_extension.py tests/test_function_field_basewave_curve_extension.py
~~~

The replay uses rational arithmetic, a nine-row local identity check, and
formal reciprocal-series recurrences only.  It enumerates no point, closed
point, curve, zero, or \(L\)-function.
