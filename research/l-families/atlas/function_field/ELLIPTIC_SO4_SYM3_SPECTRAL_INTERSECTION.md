# The elliptic \(SO(4)\) / \(\operatorname{Sym}^3\) spectral intersection

Status: **exact compact spectral theorem, exact odd-prime-power arithmetic
obstruction, exact square-\(q\) lattice count, and source-locked replay**

This packet determines exactly where the compact coefficient surface of an
elliptic-pair tensor factor meets the elliptic symmetric-cube coefficient
curve.  The real intersection splits into four Frobenius-angle-doubling
graphs.  Over integral odd-prime-power trace lattices it has a sharp
dichotomy: it is empty when \(q\) is nonsquare, while for
\(q=p^{2k}\) it has an explicit parameterization and exactly
\(16p^{\lfloor k/2\rfloor}-4\) Hasse-lattice points.

Waterhouse's trace classification sharpens the latter result.  Only three
small repeated-root strata are simultaneously realized by the two elliptic
input traces.  That is a local existence statement for separate isogeny
classes, not a correspondence between curves.

The producer authenticates both
`elliptic_pair_rankin_so4_family.json` and
`elliptic_symmetric_cube_family.json` by schema, canonical payload,
LF-normalized fixture hash, and LF-normalized producer hash.  It replays all
645 ordered atom pairs in the five locked nonsquare-prime rows.  It performs
no finite-field, curve, or model enumeration and no random or floating-point
calculation.

## 1. Conventions and the sign bridge

The two tensor inputs are

\[
 P_A(T)=1+AT+qT^2,\qquad P_B(T)=1+BT+qT^2.                 \tag{1}
\]

Put

\[
 u={A\over\sqrt q},\qquad v={B\over\sqrt q},\qquad
 x=uv,\qquad y=u^2+v^2-2.                                 \tag{2}
\]

After \(T=Z/q\), their tensor factor is

\[
 Q_{A,B}(Z)=1-xZ+yZ^2-xZ^3+Z^4.                           \tag{3}
\]

The symmetric-cube source writes an elliptic base factor as
\(1+aT+qT^2\).  Its geometric trace is \(c=-a\).  With
\(t=c/\sqrt q\), the normalized symmetric-cube coordinates are

\[
 X_3(t)=t^3-2t,\qquad Y_3(t)=t^4-3t^2+2.                  \tag{4}
\]

This sign convention is load-bearing.  On
\(u=\varepsilon(v^2-2)\), the matching geometric trace is
\(c=\varepsilon B\), so the symmetric-cube source coefficient is
\(a=-\varepsilon B\).  On the transposed graph, use
\(c=\varepsilon A\).

The two raw factors have different weights.  When \(q=s^2\), the exact
identity is the dilated one

\[
 \boxed{P_{A\otimes B}(sT)=P_{\operatorname{Sym}^3,c}(T).} \tag{5}
\]

It follows from

\[
\begin{aligned}
 c^3-2qc&=sAB,\\
 c^4-3qc^2+2q^2&=q(A^2+B^2-2q),
\end{aligned}                                               \tag{6}
\]

on the relevant graph; reciprocal symmetry supplies the remaining
coefficients.  Equivalently, (5) becomes equality after the respective
normalizations \(T=Z/q\) and \(T=Z/q^{3/2}\).  It is not an assertion that
the two raw polynomials agree in the same unscaled variable.

## 2. Exact pullback of the symmetric-cube curve

The compact symmetric-cube coefficient curve is

\[
 F_3(x,y)=-x^4+x^2y+x^2+y^3-2y^2=0.                       \tag{7}
\]

Exact bivariate expansion gives

\[
\boxed{
 F_3(uv,u^2+v^2-2)=
 (u-v^2+2)(u+v^2-2)(u^2-v-2)(u^2+v-2).}                   \tag{8}
\]

Thus the intersection is precisely the union

\[
\begin{aligned}
 u&=\phantom{-}(v^2-2),&\qquad u&=-(v^2-2),\\
 v&=\phantom{-}(u^2-2),&\qquad v&=-(u^2-2).
\end{aligned}                                               \tag{9}
\]

The polynomial \(r^2-2\) is the trace of the square of an
\(SU(2)\) torus element with trace \(r\).  If
\(v=w+w^{-1}\) and \(u=w^2+w^{-2}\), the tensor spectrum becomes

\[
 \{w^3,w,w^{-1},w^{-3}\},                                  \tag{10}
\]

the symmetric-cube spectrum.  The negative branch applies the central sign,
and exchanging the inputs gives the other orientation.

This is an identity of spectra along four one-dimensional maximal-torus
loci.  The angle-doubling relation does **not** construct a claimed
\(SU(2)\to SU(2)\times SU(2)\) representation homomorphism.  In particular,
the two-dimensional weight pair \(\{2,-2\}\) is not being promoted to a
two-dimensional \(SU(2)\) representation.

The fixture retains 25 symbolic residuals: the global bivariate
factorization and, on each signed orientation, the two coefficient
identities, curve equation, fold discriminant, endpoint factor, and full
root discriminant.  Every residual is the zero polynomial.

## 3. The integral nonsquare obstruction

Substituting (2) into (7) and clearing \(q^4\) gives the integral identity

\[
\boxed{
 q^4F_3=
 \bigl[qA^2-(B^2-2q)^2\bigr]
 \bigl[(A^2-2q)^2-qB^2\bigr].}                             \tag{11}
\]

Let \(q=p^e\) with \(p\) odd and \(e\) odd.  If the first factor vanishes
with \(A\ne0\), then

\[
 e+2v_p(A)=2v_p(B^2-2q),                                   \tag{12}
\]

whose left side is odd and right side even.  If \(A=0\), vanishing would
force \(B^2=2q\), again impossible because its \(p\)-adic valuation is odd.
The second factor is symmetric in \(A,B\).  Therefore

\[
\boxed{\text{nonsquare odd prime-power }q
 \Longrightarrow F_3(x,y)\ne0\text{ for every }A,B\in\mathbb Z.} \tag{13}
\]

No Hasse bound is needed for this obstruction.

## 4. Square-\(q\) parameterization and exact counts

Let \(q=p^{2k}\), \(s=p^k\), and
\(M=p^{\lfloor k/2\rfloor}\).  Equation (11) splits over the integers as

\[
 sA=\varepsilon(B^2-2q)
 \quad\text{or}\quad
 sB=\varepsilon(A^2-2q),\qquad \varepsilon\in\{-1,1\}.      \tag{14}
\]

On the first orientation, integrality is equivalent to
\(s\mid B^2\).  Write

\[
\boxed{
 B=p^{\lceil k/2\rceil}m,\qquad
 A=\varepsilon\bigl(p^{\,k\bmod2}m^2-2p^k\bigr),\qquad
 |m|\le2M.}                                                 \tag{15}
\]

The bound on \(m\) is exactly the Hasse bound on \(B\); (14) then puts
\(A/s\) in \([-2,2]\) automatically.  Each signed orientation has
\(4M+1\) parameters, so the four graphs have \(16M+4\) incidences.

Their only integral (equivalently rational) pairwise overlaps are four endpoint pairs
\((u,v)\in\{\pm2\}^2\) and four unit pairs
\((u,v)\in\{\pm1\}^2\), each counted twice.  Hence

\[
\boxed{\#\{\text{integral Hasse intersection points}\}=16M-4.} \tag{16}
\]

The complete grids at \(q=9\) and \(q=25\) independently give 20 graph
incidences and 12 distinct points in each case.  Formula (16) predicts
44 points at \(q=81\) and 76 at \(q=625\), without scanning either grid.

The lattice is genuinely larger for \(k\ge2\).  At \(q=p^4\),

\[
 (A,B)=(1-2p^2,p)                                          \tag{17}
\]

is a Hasse-admissible graph point.  Its first trace is ordinary, while the
second is divisible by \(p\) and is not one of Waterhouse's special
supersingular traces.  It is therefore an explicit arithmetic ghost in the
compact intersection.

## 5. Exact Waterhouse-realized strata

Specializing Waterhouse's Theorem 4.1 to \(q=p^{2k}\), a trace divisible by
\(p\) can occur here only as \(0,\pm s,\pm2s\).  Since every free trace in
(15) is divisible by \(p\), simultaneous realization of both tensor inputs
collapses to:

| normalized coefficient pair \((A/s,B/s)\) | points | condition |
|---|---:|---|
| \((\pm2,\pm2)\) | 4 | always |
| \((\pm1,\pm1)\) | 4 | \(p\not\equiv1\pmod3\) |
| \((\pm2,0),(0,\pm2)\) | 4 | \(p\not\equiv1\pmod4\) |

Thus the realized union has \(4,8,8,12\) points for primes congruent to
\(1,5,7,11\pmod {12}\), respectively; \(p=3\) has all 12.  In the two
synthetic checks, all 12 points at \(q=9\) are realized, while \(q=25\)
has the four endpoint and four unit points, but not the four mixed points.
Here Waterhouse case (3) includes \(p=3\), not merely primes congruent to
2 modulo 3.  At odd powers of 3, the separate exceptional case (4) cannot
create an intersection: the valuation theorem (13) has already ruled out
every integral pair at nonsquare \(q=3^{\text{odd}}\).

The input coefficients \(A,B\) correspond to geometric traces \(-A,-B\);
the sign-symmetric Waterhouse cases make the table unchanged.  Each branch's
symmetric-cube trace is a sign of one input trace, so it too is locally
realized whenever that input is.

This theorem says that separate elliptic isogeny classes with the prescribed
traces exist over \(\mathbb F_q\).  It neither puts all three factors on one
curve nor constructs an isogeny, shared cover, compatible system, or global
Euler product.

Primary boundary: W. C. Waterhouse,
[*Abelian varieties over finite fields*](https://numdam.org/articles/10.24033/asens.1183/),
Annales scientifiques de l'École Normale Supérieure 2 (1969), Theorem 4.1,
cases (2), (3), and (5)(ii).

## 6. Discriminants restricted to the intersection

Use the symmetric-cube parameter \(t=\varepsilon v\) or
\(t=\varepsilon u\) on the relevant graph.  The two factors of the
reciprocal-quartic root discriminant restrict to

\[
\begin{aligned}
 D&=(y+2)^2-4x^2=(t^2-1)^2(t^2-4)^2,\\
 E&=x^2-4(y-2)=t^2(t^2-4)^2.
\end{aligned}                                               \tag{18}
\]

Consequently

\[
\boxed{\operatorname{Disc}_Z(Q)=D E^2
 =t^4(t^2-1)^2(t^2-4)^6.}                                  \tag{19}
\]

For \(q=s^2\) and \(c=st\), this is

\[
\begin{aligned}
 D&={(c^2-q)^2(c^2-4q)^2\over q^4},\\
 E&={c^2(c^2-4q)^2\over q^3},\\
 \operatorname{Disc}_Z(Q)
  &={c^4(c^2-q)^2(c^2-4q)^6\over q^{10}}.
\end{aligned}                                               \tag{20}
\]

Thus \(D=0\) at \(t^2=1,4\), \(E=0\) at \(t=0\) or \(t^2=4\),
and the full quartic has a repeated root precisely at
\(t=0,\pm1,\pm2\).  The Waterhouse-realized intersection is therefore
entirely contained in the repeated-root locus:

- endpoints have \(D=E=0\);
- unit pairs have \(D=0\) and \(E=9\);
- mixed endpoint-zero pairs have \(D=16\) and \(E=0\).

The producer checks (19) independently with the \(7\times7\) Sylvester
resultant for every incident graph parameter in the complete \(q=9,25\)
grids.

## 7. Frozen replay

The locked \(SO(4)\) source rows have 7, 9, 11, 13, and 15 trace atoms at
\(q=3,5,7,11,13\).  Their ordered Cartesian products contain

\[
 7^2+9^2+11^2+13^2+15^2=645                               \tag{21}
\]

atom pairs.  For each pair the producer:

1. reconstructs the raw tensor polynomial and its normalized \(Z\)-factor;
2. evaluates \(q^4F_3\) directly and by the product in (11);
3. applies the all-\(q\) nonsquare valuation theorem.

Every row has exactly zero hits, as (13) predicts.  The represented
marked-model pair masses are retained, but no individual model is visited.
The symmetric-cube source's 55 raw local factors are also independently
reconstructed to pin the geometric-trace/source-coefficient sign bridge.

The declared work ledger is 3,334 high-level units under an exclusive cap of
4,000: 645 source atom pairs, 610 tiny synthetic Hasse-lattice points, 55
locked symmetric-cube factors, 25 symbolic certificates, and their associated
exact checks.

## 8. Replay and firewalls

From the repository root:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python research/l-families/atlas/function_field/elliptic_so4_sym3_spectral_intersection.py --check
python -O research/l-families/atlas/function_field/elliptic_so4_sym3_spectral_intersection.py --check
python -m unittest tests.test_elliptic_so4_sym3_spectral_intersection
python -O -m unittest tests.test_elliptic_so4_sym3_spectral_intersection
```

What this packet does **not** prove:

- The torus doubling locus is not promoted to an \(SU(2)\) representation
  homomorphism.
- The dilation identity is not equality of raw factors in one unscaled
  variable.
- Waterhouse realization supplies separate local isogeny classes, not a
  curve-pair correspondence.
- Five frozen rows are not used to infer a probability, rate, or
  equidistribution law; their vanishing is explained by the uniform
  nonsquare theorem.
- No automorphy, analytic continuation, zero-free region, RH, or GRH result
  follows.
- No literature-priority claim is made for this coefficient-geometric
  packaging.

The most concrete next questions are scheme-theoretic intersection
multiplicities at \(t=0,\pm1,\pm2\), and whether any geometric family can
enforce one signed doubling orientation coherently across primes.
