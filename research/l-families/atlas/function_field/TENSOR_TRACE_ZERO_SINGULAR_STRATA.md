# Trace-zero pullback of the singular product-tensor coefficient hypersurface

**Status.** Exact symbolic follow-up with a source-locked `q=3,5,7`
histogram census. The reduced affine singular locus, its transverse quadratic
rank drop, and both product-parameter branches are exact. The target
hypersurface/Jacobian statement is over characteristic different from two;
the normalized parameter pullback is over `Q`, or any base where `q` is a
unit. The finite tables are exact for the declared model law only. No field,
curve, or variety is enumerated here.

**Scope.** This is geometry of an ambient hypersurface in normalized
coefficient space that contains the product-tensor image, together with the
pullback of its singular strata. Equality with the full coefficient image is
not proved. A singular ambient coefficient state is not a singular elliptic
curve, genus-two curve, or product variety, and it is not by itself evidence
of extra endomorphisms.

**Exact sources.** The producer reads the payload-hashed
`genus1_cubic_family_laws.json`, `balanced_control_family_scan.json`, and
`product_variety_tensor_family.json`. The last locks the hypersurface and the
sign bridge; the first two alone supply the census weights. Their producers,
the product note, this producer, this note, and the focused test are all
LF-normalized SHA-256 locked in the generated JSON.

## 1. Normalization and exact normal form

The genus-one fixture stores

\[
 t_E=q+1-\#E(\mathbf F_q),\qquad L_E(T)=1-t_ET+qT^2.
\]

The tensor packet instead writes `P_E(T)=1+A*T+q*T^2`, so throughout

\[
                         \boxed{A=-t_E}.                                 \tag{1}
\]

For the genus-two factor use

\[
 P_C(T)=1+aT+bT^2+qaT^3+q^2T^4.
\]

The normalized tensor coefficients `(u,v,w,h)` satisfy

\[
 F=u^2h-u^4+2u^2v+u^2-2uw-w^2=0.                                      \tag{2}
\]

Set

\[
                   r=u+w,\qquad L=h+2v+2.                               \tag{3}
\]

An exact rearrangement gives the useful normal form

\[
                         \boxed{F=Lu^2-u^4-r^2}.                         \tag{4}
\]

The producer reconstructs (2)--(4) as sparse multivariate polynomials over
the integers. No numerical fitting or floating-point algebra occurs.

## 2. The full affine singular locus

In the original coordinates the exact partial derivatives are

\[
\begin{aligned}
 F_u&=2uh-4u^3+4uv+2u-2w,\\
 F_v&=2u^2,\\
 F_w&=-2u-2w,\\
 F_h&=u^2.
\end{aligned}                                                           \tag{5}
\]

Over a field of characteristic different from two, `F_h=0` forces `u=0`
on the reduced singular locus. Then `F_w=0` forces `w=0`. Conversely, all
four derivatives and `F` vanish when `u=w=0`, with `v,h` arbitrary. Hence

\[
             \boxed{\operatorname{Sing}(F)_{\rm red}=V(u,w)\simeq\mathbf A^2_{v,h}.} \tag{6}
\]

Equation (4) also records the nonreduced information cleanly. In coordinates
`(u,r,L,v)`, the Jacobian ideal is

\[
             (r,u^2,uL)=(r,u)\cap(r,L,u^2),                              \tag{7}
\]

whose radical is `(u,r)=(u,w)`. Thus the reduced plane in (6) is the full
affine singular set; the line `u=r=L=0` supports an additional infinitesimal
thickening of the Jacobian scheme.

## 3. Transverse quadratic cone

At a point `(0,v,0,h)` of (6), the quadratic part in the normal variables
`(u,w)` is

\[
 Q=(h+2v+1)u^2-2uw-w^2=Lu^2-r^2.                                      \tag{8}
\]

Its coefficient matrix and determinant are

\[
 \begin{pmatrix}h+2v+1&-1\\-1&-1\end{pmatrix},
 \qquad
 \boxed{\det Q=-(h+2v+2)=-L}.                                          \tag{9}
\]

The normal Hessian determinant is `-4L`. Therefore the transverse quadratic
cone has rank two off, and rank one on, the line

\[
                  \boxed{u=w=0,\qquad h+2v+2=0}.                         \tag{10}
\]

The `+2` in (9)--(10) is essential. On this line the quadratic part is
`-(u+w)^2`. More intrinsically, set `lambda=L-u^2`. Then (4) becomes

\[
                         r^2=u^2\lambda.
\]

Thus the total germ along the rank-drop line is a pinch point (Whitney
umbrella) times the free `v`-line. Holding the original `v,h`, hence `L`,
fixed at zero instead leaves `F=-u^4-r^2`, a slice-dependent `A_3`
plane-curve singularity over `C`. Its complex branches are `r=+/-i*u^2`;
the corresponding real slice has only `u=r=0`. Neither description is used
to classify any source curve or product variety.

## 4. Pullback and the two square restrictions

Put

\[
 x={A^2\over q},\qquad y={a^2\over q},\qquad z={b\over q}.
\]

The product map is

\[
\begin{aligned}
 u^2&=xy, & v&=xz+y-2z,\\
 w&=u(x+z-3), & h&=x^2+xy-4x-2y+z^2+2.
\end{aligned}                                                           \tag{11}
\]

With `t=x+z-2`, exact substitution gives

\[
 r=ut,\qquad
 \boxed{L=h+2v+2=(x+z-2)^2+xy=t^2+u^2}.                                \tag{12}
\]

It also gives `F=u^2(xy-u^2)`, which vanishes by (11). On the preimage of
the reduced singular plane, `u=0` and hence `xy=0`. Its two reduced
components are therefore

\[
 x=0\ (A=0),\qquad y=0\ (a=0).                                         \tag{13}
\]

On (13), equation (12) becomes `L=t^2`; the **reduced, set-theoretic**
rank-drop preimage is exactly

\[
       \boxed{\{x=0,z=2\}\ \cup\ \{y=0,z=2-x\}.}                        \tag{14}
\]

The scheme pullback retains the square that (14) suppresses. After clearing
powers of `q` and putting `R=A^2+b-2q`, the singular-plane and rank-line ideals
are

\[
 I_{\rm sing}=(Aa),\qquad I_{\rm rank}=(Aa,R^2),
\]

while

\[
 \sqrt{I_{\rm rank}}
 =(Aa,R)
 =(A,b-2q)\cap(a,A^2+b-2q).
\]

Thus (14) is precisely the reduced support, not an assertion that the
scheme-theoretic inverse image is reduced. It yields two different integral
square restrictions.

### E-trace-zero component

Here `A=0`, so

\[
 q^2L=(b-2q)^2.                                                         \tag{15}
\]

Rank drop means `b=2q`. On that branch

\[
 v={a^2\over q}-4,\qquad h=6-{2a^2\over q},\qquad h=-2v-2,              \tag{16}
\]

and the image obeys the scaled-square restriction

\[
                         \boxed{q(v+4)=a^2}.                             \tag{17}
\]

The specialized genus-two polynomial has the exact formal factorization

\[
 P_C(T)=(1+qT^2)(1+aT+qT^2).
\]

### C-trace-zero component

Here `a=0`, so

\[
 q^2L=(A^2+b-2q)^2.                                                     \tag{18}
\]

Rank drop means

\[
                         \boxed{b=2q-A^2}.                              \tag{19}
\]

The sign in (19) is negative. On this branch

\[
 v=-{b^2\over q^2},\qquad h={2b^2\over q^2}-2,
 \qquad h=-2v-2,                                                        \tag{20}
\]

and the integral restriction is

\[
                         \boxed{2q-b=A^2}.                              \tag{21}
\]

Here the specialized polynomial factors formally as

\[
 P_C(T)=(1+AT+qT^2)(1-AT+qT^2),
\]

which independently confirms the negative sign in (19).

The two source components meet at `A=a=0`. Their rank-drop intersection
requires `b=2q` and maps to

\[
                         (u,v,w,h)=(0,-4,0,6).                           \tag{22}
\]

Equations (15) and (18) combine on the whole singular preimage as

\[
 L=\left({A^2+b-2q\over q}\right)^2.                                   \tag{23}
\]

The producer checks this integer-square identity on every trace-zero source
histogram atom pair.

## 5. Frozen model census

For each `q`, the producer negates every locked genus-one trace key according
to (1), takes the Cartesian product with the locked genus-two `(a,b)` atoms,
and uses the product of the two member counts as weight. The exclusive
categories are `A=0,a!=0`, `A!=0,a=0`, `A=a=0`, and neither. The first three
are precisely the product-parameter preimage of the singular plane.

| `q` | all product pairs | E zero only | C zero only | both zero | singular total | transverse rank drop |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2,916 | 528 | 420 | 120 | 1,068 | 66 |
| 5 | 250,000 | 41,880 | 32,480 | 8,120 | 82,480 | 5,000 |
| 7 | 4,235,364 | 513,324 | 550,368 | 91,728 | 1,155,420 | 72,324 |

The component counts include their intersection, unlike the exclusive table:

| `q` | E-zero component | C-zero component | intersection | E rank drop | C rank drop | rank-drop intersection |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 648 | 540 | 120 | 48 | 18 | 0 |
| 5 | 50,000 | 40,600 | 8,120 | 2,900 | 2,200 | 100 |
| 7 | 605,052 | 642,096 | 91,728 | 37,044 | 37,044 | 1,764 |

Here are the conditional first moments of the three normalized coordinates;
`L=h+2v+2` is the transverse rank-drop detector. The JSON additionally stores
support sizes, exact ranges, conditional second moments, and each zeroth,
first, and second moment's share of the full product law. Because the
rank-drop support is tiny, its complete joint `(v,h,L)` distribution is also
retained.

| `q` | stratum | `E[v]` | `E[h]` | `E[L]` |
|---:|:---|:---|:---|:---|
| 3 | E zero only | `-28/33` | `142/99` | `172/99` |
| 3 | C zero only | `-4/35` | `2/35` | `64/35` |
| 3 | both zero | `-4/15` | `38/15` | `4` |
| 3 | singular total | `-44/89` | `814/801` | `1624/801` |
| 3 | rank drop | `-16/11` | `10/11` | `0` |
| 5 | E zero only | `-956/1047` | `8546/5235` | `3152/1745` |
| 5 | C zero only | `-24/145` | `1651/10150` | `18591/10150` |
| 5 | both zero | `-12/29` | `2662/1015` | `3852/1015` |
| 5 | singular total | `-2936/5155` | `29671/25775` | `51861/25775` |
| 5 | rank drop | `-1088/625` | `926/625` | `0` |
| 7 | E zero only | `-1868/2037` | `23762/14259` | `26128/14259` |
| 7 | C zero only | `-174/637` | `1136/1911` | `3914/1911` |
| 7 | both zero | `-58/91` | `1852/637` | `178/49` |
| 7 | singular total | `-18876/32095` | `40258/32095` | `9528/4585` |
| 7 | rank drop | `-488/287` | `402/287` | `0` |

Every row obeys `E[L]=E[h]+2E[v]+2`. These are exact finite model-law facts,
not coarse-isomorphism-class probabilities.

## 6. Replay boundary and firewall

The complete run visits

\[
 7\cdot32+9\cdot81+11\cdot138=2{,}471
\]

histogram atom pairs, strictly below the hard `20,000` cap. It uses integer,
`Fraction`, and sparse integer-polynomial arithmetic only, with no random
sampling and no field or curve enumeration. The payload hash authenticates
the generated JSON; the JSON in turn locks the producer, this note, the test,
and every direct dependency.

The census does **not** identify the mechanism producing any trace-zero or
rank-drop atom. The two displayed factorizations are polynomial identities
only in this packet: no Honda--Tate or Tate isogeny theorem is imported, and
no Jacobian splitting, isogeny, or extra-endomorphism conclusion is asserted.
Nor does the packet prove a supersingular classification, special
correspondence, monodromy enhancement, or singularity of `E`, `C`, or
`E x C`. It also gives no asymptotic law, equidistribution theorem,
number-field transfer, RH statement, or GRH statement.

Replay with either the default fixture path or an explicit path:

```text
python research/l-families/atlas/function_field/tensor_trace_zero_singular_strata.py --check
python -m unittest tests.test_tensor_trace_zero_singular_strata
python -O -m unittest tests.test_tensor_trace_zero_singular_strata
```
