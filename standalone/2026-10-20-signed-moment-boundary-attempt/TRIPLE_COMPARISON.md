# An eight-point triple comparison with a finite length rank

Research component, 2026-10-20. This proves an exact algebraic comparison,
its fixed-character cancellation, and a finite comparison rank when the
ordinary reflection rule is available. It does **not** prove a sixth
moment or a numerical zero-free boundary below Liu's `B_flat`.

The underlying fixed-character means and ordinary reflection are Liu,
[arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), Lemmas 12.3 and
12.6. The source PDF SHA-256 is
`5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.
The eight-point construction was proposed by the coordinating agent;
the proof below independently checks it and supplies the buffered rank
needed at the seventh comparison term.

## 1. Scales, profiles, and the eight vertices

Fix `Z>1`, `L>0`, and `sigma>0`. Write `B=L+sigma`. The input is a
triple `x=(x1,x2,x3)` with every `xi<=B`. Let `A=x1+x2+x3`.
Negative coordinates are allowed: the actual positive scale is always
`Ti=Z^xi`. No negative coordinate is replaced by zero inside an identity.

Let `y=(x3,x1,x2)`. Choose distinct indices i,j attaining its maximum
and minimum, respectively; when all entries agree, choose any two
distinct indices. Define

```
delta = sigma (e_i-e_j),
t1=3 sigma,   t2=3 sigma+delta2,   t3=3 sigma-delta1,
a=L-x2+t2,    b=L-x3+t3,           c=L-x1+t1,
u=(0,a,-a),   v=(-b,0,b),          w=(c,-c,0).
```

Each `t_i` lies in `[2 sigma,4 sigma]`. Consequently `a,b,c>=sigma`.
For `epsilon in {0,1}^3`, set

```
x_epsilon=x+epsilon1 u+epsilon2 v+epsilon3 w.
```

Every vertex has coordinate sum A. The final vertex is exactly

```
T=x+u+v+w
 =(x3+t1-t3, x1+t2-t1, x2+t3-t2)
 =y+delta.                                             (1)
```

Thus `max(T)>=max(x)+sigma`, so in particular `T!=x`.

Each of the other six noninitial vertices has an explicitly large
coordinate:

| Vertex | Designated coordinate |
|---|---|
| `x+u` | coordinate 2 is `L+t2` |
| `x+v` | coordinate 3 is `L+t3` |
| `x+w` | coordinate 1 is `L+t1` |
| `x+u+v` | coordinate 2 is `L+t2` |
| `x+u+w` | coordinate 1 is `L+t1` |
| `x+v+w` | coordinate 3 is `L+t3` |

These coordinates are at least `L+2 sigma`. Every coordinate of every
vertex is at most `L+4 sigma`. To check the upper bound, the unaffected
or negatively shifted coordinates are at most B; each remaining pair
coordinate is a cyclic input coordinate plus one of the differences
`t1-t3=delta1`, `t2-t1=delta2`, `t3-t2=delta3`, hence at most
`B+sigma=L+2 sigma`. The designated coordinates satisfy the displayed
bound, and (1) handles the last vertex. Positivity of a,b,c, together
with `T!=x`, also shows the eight vertices are distinct.

## 2. An exact comparison for arbitrary three profiles

Let `W1,W2,W3` be any three compact annular profiles. They need not be
equal, nonnegative, or real. On three ideal variables define

```
D_x(l1,l2,l3)
 = sum_{epsilon in {0,1}^3} (-1)^|epsilon|
      product_{i=1}^3 Wi(Nli/Z^(x_epsilon,i)).           (2)
```

This is the operator `(1-T_u)(1-T_v)(1-T_w)` applied to the product of
the profiles as functions of their logarithmic scales. Its coefficient
at the original vertex is one. Every term has the same central
normalization `Z^(-A/2)` because the scale products agree.

For any common multiplicative zero-extended character psi, common
coprimality indicator, and common explicit norm power, let `P(x)` denote
the normalized product of the three corresponding ordinary sums, and
let `C(x)` denote their normalized sum with coefficient (2). Then

```
P(x)=C(x)+sum_{epsilon != 0} (-1)^(|epsilon|+1) P(x_epsilon),
|P(x)|^2 <= 8 ( |C(x)|^2+sum_{epsilon != 0}|P(x_epsilon)|^2 ). (3)
```

The same inequality holds after multiplication by common remaining
prime-polynomial factors and integration against any positive row
measure. Empty rectangles remain their exact zero values in (2)–(3).
No test is transferred from one position to another.

If incoming individual norm modes are present, first absorb them into
the fixed normalized profiles, keeping their scalar factors outside the
comparison. The subsequent whole-product Fourier mode is common to
all three factors. Allowing three different explicit norm powers to
vary with the vertices would invalidate the cancellation below.

## 3. Cancellation of the main and all one-error terms

The signed measure in (2), projected onto any one scale coordinate,
is zero. For coordinate 1, pairing vertices which differ by u proves
this because `u1=0`; for coordinates 2 and 3 use `v2=0` and `w3=0`.
This is exact even if some coordinate values coincide.

On a fixed exceptional inducing character, the common presentation is
`theta(l) 1_{(l,R*)=1}`. By source Lemma 12.3, for one common real norm
twist t,

```
Fi(T)=sum_l theta(l)1_{(l,R*)=1} (Nl)^(it) Wi(Nl/T)
     =ci T^(1+it)+Ei(T),
|Ei(T)| << Z^epsilon (1+|t|)^J p_J(Wi).                (4)
```

Here theta belongs to the fixed finite coefficient family and R* has
bounded polynomial norm. The same constants and profiles are used at
all vertices. The all-main product is a constant multiple of
`Z^(A(1+it))`, independent of the vertex. A term with only `Ei` as its
error, divided by this common total phase and volume, depends solely on
coordinate i. Both therefore vanish under (2). Every remaining term
has at least two errors.

The estimate (4) also holds for `T<1`. If its annulus is empty, then
`Fi(T)=0` and `Ei(T)=-ci T^(1+it)=O(1)`; on a bounded nonempty subunit
range both terms are bounded. Thus there is no missing lower-scale
case. The two-error terms are bounded by the largest scale, and the
three-error term is bounded independently of the scales. Since
`L+4 sigma>0`, this proves the raw bound

```
|sum_{l1,l2,l3} common_character_and_norm_factors * D_x|
 << Z^(L+4 sigma+epsilon) (1+|t|)^J p_J(W1,W2,W3).      (5)
```

Absolute counting in each original rectangle separately also bounds
the left side by `O(Z^(A+epsilon))`. Indeed, a nonempty annular scale
is bounded below by its fixed support endpoint, so each absolute
ordinary sum is `O(T)` uniformly, including subunit scales. Hence (5)
can be sharpened to `Z^(A-(A-L-4 sigma)_++epsilon)`.

Dividing coordinate i by one fixed extracted ideal at every vertex
translates that entire coordinate by the same removal length. It
preserves equal total products and all three zero coordinate
projections. If the total removal is r, the resulting saving against
its own raw volume is at least `(A-L-4 sigma-r)_+`. This is exactly the
form needed by the exceptional-row last-divisor calculation; no
allocation-dependent positive enlargement is made before cancellation.

## 4. A finite comparison rank with ordinary reflection

The following is an algebraic closure statement under the explicit
reflection rule, not a new estimate for its centered leaves. Suppose
that in absolute product bounds one may reflect any ordinary factor
of length z to a common-measure family of annular factors of actual
length at most

```
z' <= 2L-z+xi,       0<=xi<=sigma/2.                  (6)
```

For the source, take `2L=M` and use Lemma 12.6 with the indicated
fixed length allowance. Conjugating a reflected factor within its own
absolute value restores the original character; the common-measure
version must be applied to the whole triple, with finite profile and
height orders. The three-variable Sobolev variant is the same finite
box argument, retaining all partial derivatives of order at most one
in each of the three scale coordinates.

Use the buffered input range `x_i<=B=L+sigma`, and reflect only
coordinates exceeding B. Every reflected coordinate decreases its
length by more than `2 sigma-xi>=3 sigma/2` and returns below B.
In each of the six designated comparison terms at least one
coordinate is `>=L+2 sigma`; in the seventh term either T remains
inside the box, or it too has a coordinate exceeding B. Thus every
nonempty comparison child has one of two properties:

1. It uses reflection and lowers total length A by at least
   `3 sigma/2`, with all coordinates again at most B.
2. It is the unreflected T, has exactly the same A, and increases the
   maximum coordinate by at least sigma.

The wider box is necessary for this uniform statement. With input
ceiling exactly L, T could cross L by arbitrarily little, so its
reflection need not decrease A by a fixed amount.

For a finite fixed annular support bound and sufficiently large Z,
every nonempty actual scale has logarithmic length at least `-eta`,
where eta is any fixed positive lower-endpoint allowance. Keep these
actual negative lengths; do not round them upward inside a recursion.
Let

```
N=ceil((B+eta)/sigma),
q_A(x)=ceil((A+3 eta)/sigma),
q_max(x)=ceil((B-max_i xi)/sigma),
rank(x)=(N+1)q_A(x)+q_max(x).                          (7)
```

Both q's are nonnegative integers, `0<=q_max<=N`, and
`q_A<=ceil((3B+3eta)/sigma)`. A reflection step decreases q_A by at
least one, even if q_max returns to N; (7) therefore decreases by at
least one. A T-step keeps q_A fixed and decreases q_max by at least
one. This proves finite depth, bounded numerically by

```
(N+1) ceil((3B+3eta)/sigma)+N.                          (8)
```

Any empty child is simply omitted. Functional-equation tails and
profile losses are external analytic data of (6), to be charged at
each of these finitely many edges. The rank proof does not insert a
moment bound for a reflected sum or estimate a product of separately
averaged scale suprema. It only shows that the comparison need not
cycle once a centered-family estimate and the reflection rule are
available with their correct common measures.

## 5. Exact consequence and the remaining analytic issue

The exceptional-row gain is a real component: two errors replace the
single-error term of source Proposition 12.4. The equal-product and
common-character invariants survive every uniform coordinate
extraction, and (7) supplies a finite add-back comparison.

The second Poisson diagonal in source §12.7.3 is a different quantity,
the positive square of the allocated full convolution coefficient.
Its excess remains `A-M+O(sigma)`. The cancellation in (4)–(5) does
not bound that quadratic energy. Therefore neither (3) nor the
comparison rank proves the desired sixth moment `U^(1+epsilon)`.
The separate signed-graph calculation in `SIGNED_SIXTH_POWER_GRAPH.md`
records why the exact Möbius diagonal cancellation also needs a new
width-decreasing estimate before that conclusion would follow.
