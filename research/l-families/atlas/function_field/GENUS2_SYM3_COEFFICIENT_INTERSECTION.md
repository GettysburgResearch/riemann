# The elliptic \(\operatorname{Sym}^3\) curve inside a locked genus-two coefficient lattice

Status: exact symbolic packet plus a source-locked finite transform

Scope: all algebraic statements below; exhaustive finite data only for \(q=3,5,7\)

Exact sources: `balanced_control_family_scan.json` and `elliptic_symmetric_cube_family.json`

What was run: 251 pre-enumerated coefficient atoms were transformed with integer arithmetic
Smallest remaining gap: determine whether any analogous incidence law persists in other genus-two families or larger fields

## Result in one paragraph

The normalized elliptic symmetric-cube coefficient curve cuts the 251 locked
genus-two \((a_D,b_D)\)-atoms in only seven atoms.  Four are independently
witnessed arithmetic symmetric-cube *coefficient shapes*, carrying 53 marked
quintics.  Three are copies of the nodal point \((a,b)=(0,0)\), carrying 398
marked quintics; they lie on the compact curve but cannot come from an integral
elliptic trace when \(q\) is odd.  The remaining 244 atoms, carrying 16,617
members, are off the curve.  The pooled totals are an audit only: the three
finite fields do not define one common probability space.

## 1. The scaled integer equation

Write a genus-two local factor as

\[
P_{a,b,q}(T)=1+aT+bT^2+qaT^3+q^2T^4.
\]

After \(Z=\sqrt q\,T\), its compact coefficient coordinates are

\[
(x,y)=\left(-\frac{a}{\sqrt q},\frac bq\right),
\]

because the symmetric-cube convention is
\(1-xZ+yZ^2-xZ^3+Z^4\).  The locked symmetric-cube packet proves that its
rank-one compact image has equation

\[
F(x,y)=-x^4+x^2y+x^2+y^3-2y^2=0.
\]

Clearing exactly \(q^3\) gives the integer equation

\[
\boxed{G_q(a,b)=-qa^4+qa^2b+q^2a^2+b^3-2qb^2=0.}
\]

This is an intersection of independently normalized coefficient shapes.  It
does **not** identify the weight-one genus-two factor with the weight-three
elliptic symmetric-cube factor.

## 2. Generic inverse and its exact certificate

Away from \(d=a^2-b=0\), put

\[
n=a(q-b),\qquad t=\frac nd=\frac{a(q-b)}{a^2-b}.
\]

This is exactly \(t=\sqrt q\,t_0\) under the normalization inverse
\(t_0=x(y-1)/(x^2-y)\).  No appeal to numerical roots is needed.  Direct
expansion gives

\[
n^3-2qn d^2+qa d^3=a(q-a^2)G_q(a,b)
\]

and

\[
\begin{aligned}
n^4-3qn^2d^2+(2q^2-qb)d^4
={}&(a^4b-2qa^4+qa^2b\\
&\quad+q^2a^2-qb^2)G_q(a,b).
\end{aligned}
\]

Consequently, a generic point on \(G_q=0\) obeys

\[
qa=2qt-t^3,\qquad qb=t^4-3qt^2+2q^2.
\]

Thus a generic lattice point is an arithmetic candidate only if the rational
inverse is an integer, \(t^2\le 4q\), and that trace is actually realized by an
elliptic curve over the field in question.  For the frozen fields, the packet
uses the positive-count trace support in the independent elliptic fixture as
the realization witness.  It does not silently replace realization by the
Hasse inequality for arbitrary prime powers.

## 3. The nodal divisor is completely classified

On \(b=a^2\),

\[
G_q(a,a^2)=a^2(a^2-q)^2.
\]

Hence the exceptional lattice points on the curve are exactly

\[
(a,b)=(0,0),\qquad\text{or}\qquad a^2=q,\ b=q.
\]

The first maps to the compact node \((x,y)=(0,0)\), whose normalization
preimages require \(t_0^2=2\).  An integral elliptic trace would therefore
satisfy \(t^2=2q\).  If \(q\) is odd, then \(v_2(2q)=1\), so this is impossible.
This proves, for every odd \(q\), that \((0,0)\) is a coefficient-curve ghost.

The other two nodes can be lattice points only when \(q\) is a square.  Then
\(\sqrt q\) is integral, while their normalization parameters solve
\(t_0^2\pm t_0-1=0\) and are irrational.  They likewise have no integral
elliptic trace.  The generic inverse must not be applied at any of these three
nodes.

## 4. Prime-field arithmetic shapes

For an integer parameter \(t\), the two displayed coefficients are integral
if and only if

\[
q\mid t^3.
\]

Indeed, integrality of \(a=2t-t^3/q\) forces this divisibility, and it then also
implies \(q\mid t^4\), so \(b\) is integral.

Now let \(q=p\) be an odd prime.  Then \(p\mid t\).  Write \(t=kp\).  The
Hasse inequality becomes \(k^2p\le4\).  Therefore

\[
\begin{cases}
t=0, & p\ge5,\\
t\in\{-3,0,3\}, & p=3.
\end{cases}
\]

The resulting coefficient shapes are

\[
(a,b)=(0,2p)\quad(p\ge5),
\]

and, at \(p=3\),

\[
t=-3,0,3\quad\longmapsto\quad(3,6),(0,6),(-3,6).
\]

This theorem classifies possible integral shapes arising from an elliptic
trace; it does not say that every shape occurs in the marked quintic family.
That distinction is visible already at \(q=3\): the locked genus-two support
contains the two \(t=\pm3\) shapes but omits the \(t=0\) shape \((0,6)\).
For \(q=5,7\), it contains the unique possible shape \((0,2q)\).

## 5. Complete frozen intersection

| \(q\) | locked atoms | curve-hit atoms | curve-hit members | source-witnessed shapes | witnessed members | ghost members |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 32 | 3 | 18 | 2 | 6 | 12 |
| 5 | 81 | 2 | 55 | 1 | 5 | 50 |
| 7 | 138 | 2 | 378 | 1 | 42 | 336 |

The seven atoms are:

| \(q\) | \((a,b)\) | genus-two members | classification | recovered \(t\) | independent elliptic-source witnesses |
|---:|:---:|---:|:---|:---:|---:|
| 3 | \((-3,6)\) | 3 | source-witnessed arithmetic shape | \(3\) | 1 |
| 3 | \((0,0)\) | 12 | nodal ghost | undefined | -- |
| 3 | \((3,6)\) | 3 | source-witnessed arithmetic shape | \(-3\) | 1 |
| 5 | \((0,0)\) | 50 | nodal ghost | undefined | -- |
| 5 | \((0,10)\) | 5 | source-witnessed arithmetic shape | \(0\) | 20 |
| 7 | \((0,0)\) | 336 | nodal ghost | undefined | -- |
| 7 | \((0,14)\) | 42 | source-witnessed arithmetic shape | \(0\) | 42 |

The exact family fractions are:

- \(q=3\): curve hit \(1/9\), witnessed \(1/27\), ghost \(2/27\);
- \(q=5\): curve hit \(11/500\), witnessed \(1/500\), ghost \(1/50\);
- \(q=7\): curve hit \(9/343\), witnessed \(1/343\), ghost \(8/343\).

The machine-readable fixture retains all 251 transformed atoms, including
every exact member count and every nonzero residual.

## 6. Negative controls

The normalized USp(4) boundary point \((x,y)=(0,-2)\) corresponds to
\((a,b)=(0,-2q)\), and

\[
G_q(0,-2q)=-16q^3\ne0.
\]

So the curve is a proper rank-one subset of the compact genus-two coefficient
region.  Conversely, \((0,0)\) is the essential false positive: it satisfies
the curve equation exactly but fails the odd-\(q\) arithmetic trace test.  The
fixture also freezes one positive-count off-curve atom in each field.

## 7. Scope and literature boundary

Exact here:

- the scaled equation, inverse identities, nodal classification, divisibility
  criterion, and odd-prime candidate theorem;
- the complete source-locked transform of 251 atoms.

Frozen only:

- all \(q=3,5,7\) incidence and member counts;
- the positive-count elliptic trace witnesses used to call four atoms genuine.

Not claimed:

- equidistribution, an all-family density, or persistence at larger \(q\);
- arithmetic symmetric-cube origin from the curve equation alone;
- an identity of local factors of different weights;
- a new automorphy theorem, a literature-priority result, or any RH/GRH
  consequence.

The symmetric-cube representation and automorphic lift are classical; the
upstream packet points to Kim--Shahidi
([1999](https://arxiv.org/abs/math/9909198),
[2004](https://arxiv.org/abs/math/0409607)).  “Project-specific” here means
only that this exact locked-lattice calculation was made for the atlas.  It is
not a claim that the observation is absent from the literature.

## Replay

```powershell
python research/l-families/atlas/function_field/genus2_sym3_coefficient_intersection.py --check
python -m unittest tests.test_genus2_sym3_coefficient_intersection
python -O -m unittest tests.test_genus2_sym3_coefficient_intersection
```

The producer refuses source hash, schema, payload, normalization, field-set,
atom-cap, or member-cap drift before it performs the 251 residual evaluations.
