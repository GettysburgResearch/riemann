# Native \(q\)-adic wavelet square-tower bifurcation

Status: **PROVED** by exact polynomial algebra. No finite field, curve, or
family member is enumerated.

Let

\[
 P(u)=1+au+bu^2+qau^3+q^2u^4,
 \qquad {1\over P(u)}=\sum_{n\geq0}r_nu^n,
\]

and use the native endpoint-three wavelet

\[
 W_3=r_3-(1+\sqrt q)r_2+\sqrt q\,r_1.
\tag{1}
\]

The preceding zero-stratum packet proves that, when \(q\) is a nonsquare odd
prime power,

\[
 W_3=0\iff (a,b)=(0,0).
\tag{2}
\]

This packet proves that the geometry changes discontinuously on the even
levels of a fixed-characteristic tower.

## 1. Exact square-field zero curve

Write \(q=s^2\), where \(s\) is an odd positive integer. The first reciprocal
coefficients are

\[
 r_1=-a,\qquad r_2=a^2-b,\qquad
 r_3=-a(a^2-2b+s^2).
\tag{3}
\]

Substitution into (1) gives

\[
 W_3=-a^3-a^2s-a^2+2ab-as^2-as+bs+b.
\tag{4}
\]

Therefore

\[
 \boxed{
 W_3=0\iff
 (2a+s+1)b=a\bigl(a^2+(s+1)a+s(s+1)\bigr).
 }
\tag{5}
\]

The apparent vertical exceptional value is not a component. At
\(a=-(s+1)/2\), the coefficient of \(b\) vanishes but

\[
 W_3={ (s+1)^2(3s-1)\over8}>0.
\tag{6}
\]

Thus the square-field zero locus is the rational graph

\[
 b={a\bigl(a^2+(s+1)a+s(s+1)\bigr)\over2a+s+1},
 \qquad a\ne-{s+1\over2}.
\tag{7}
\]

This is a coefficient-space statement. Hasse bounds, integrality, principal
polarizability, and realization by a genus-two Jacobian remain separate
filters.

## 2. Exact intersection with the old toy minor

On a square field the toy minor factors:

\[
 K=s^2a^2-b^2=(sa-b)(sa+b).
\tag{8}
\]

On the first line \(b=sa\), equation (4) becomes

\[
 W_3=a^2(s-1-a).
\tag{9}
\]

On the second line \(b=-sa\), it becomes

\[
 W_3=-a(a+2s)(a+s+1).
\tag{10}
\]

Consequently, for every odd \(s\ge3\),

\[
 \boxed{
 \{W_3=0\}\cap\{K=0\}
 =\{(0,0),(s-1,s(s-1)),(-2s,2s^2),(-s-1,s(s+1))\}.
 }
\tag{11}
\]

The four points are distinct. In particular, both implications in the
nonsquare equivalence (2) fail as identities of square-field coefficient
geometry: \(K=0\) is now two lines, while \(W_3=0\) is the different rational
curve (7).

## 3. Compact admissibility of the four crossings

For a reciprocal quartic

\[
 z^4+Az^3+Bz^2+Az+1,
\]

write

\[
 (z^2-xz+1)(z^2-yz+1),\qquad x,y\in[-2,2].
\tag{12}
\]

Then \(x+y=-A\) and \(xy=B-2\). Put

\[
 Q(t)=t^2-(x+y)t+xy.
\]

For the roots \(x,y\) of \(Q\), the four inequalities

\[
 \operatorname{disc}(Q)\ge0,\qquad
 Q(-2)\ge0,\qquad Q(2)\ge0,\qquad |x+y|\le4
\tag{13}
\]

are necessary and sufficient for \(x,y\) to be real and lie in \([-2,2]\).
Indeed, the discriminant first makes the roots real. The two endpoint
products put both roots between the endpoints unless both lie on the same
outer side; the root-sum bound excludes either outer alternative except at
the corresponding double endpoint.

The producer derives all quantities in (13) from each point in (11), rather
than accepting displayed row strings. With \(A=a/s\) and \(B=b/s^2\):

- at \((0,0)\), \((x,y)=(\sqrt2,-\sqrt2)\);
- at \((-2s,2s^2)\), \((x,y)=(2,0)\);
- at \((s-1,s(s-1))\), the discriminant numerator is
  \(5s^2+2s+1\), the endpoint numerators are \(s(s+1)\) and
  \(s(5s-3)\), and the root-sum-bound numerators are \(3s+1\) and
  \(5s-1\);
- at \((-s-1,s(s+1))\), the corresponding numerators are
  \(5s^2-2s+1\), \(s(5s+3)\), \(s(s-1)\), \(5s+1\), and
  \(3s-1\).

Every numerator is certified nonnegative after the exact shift \(s=t+3\).

Hence their reciprocal quartics are compact-admissible \(q\)-Weil
polynomials. This does **not** assert that all four occur as Jacobians over
every square field.

## 4. Tower interpretation

For \(q=p^f\) with \(p\) odd,

\[
 \sqrt q\notin\mathbf Q\quad(f\text{ odd}),
 \qquad
 \sqrt q=p^{f/2}\in\mathbf Z\quad(f\text{ even}).
\]

Thus one fixed characteristic has an exact parity alternation:

| extension degree | endpoint-three zero geometry |
|---|---|
| odd \(f\) | the single point \((a,b)=(0,0)\) |
| even \(f\) | the rational curve (7) |

This is a source-normalization effect, not a monodromy or equidistribution
theorem. It warns that zero incidences of a \(\mathbf Q(\sqrt q)\)-valued
detector need not transport unchanged along prime-power towers even when the
underlying reciprocal formula is identical.

## 5. Replay and boundary

The replay uses a small sparse polynomial engine over
\(\mathbf Z[a,b,s]\). It derives (3)--(5), the exceptional value (6), both
intersection factorizations (9)--(10), and the compact endpoint inequalities.
It source-locks the native wavelet and nonsquare zero-stratum packets. No
floating point, symbolic-algebra package, field table, family histogram, or
database enters.

Run from the repository root:

    python -B research/l-families/atlas/function_field/native_qadic_wavelet_square_tower_bifurcation.py --check
    python -B -O research/l-families/atlas/function_field/native_qadic_wavelet_square_tower_bifurcation.py --check
    python -B -m unittest tests.test_native_qadic_wavelet_square_tower_bifurcation -v
    python -B -O -m unittest tests.test_native_qadic_wavelet_square_tower_bifurcation -v

The theorem makes no all-\(q\) count claim, no Jacobian-realization claim, no
novelty claim, and no RH or GRH implication.
