# Three-place elliptic interference in the quadratic genus-two family

Status: **PROVED** for every odd prime power `q`.

The packet computes the first genuinely geometric mixed-place channel in the
squarefree-quintic family. It proves no statement about zeros, RH,
individualization, or a global number-field Euler product.

## Start here

Let

\[
 \mathcal H_5(q)=\{D\in\mathbf F_q[T]:D\text{ monic squarefree},\deg D=5\}
\]

and choose three distinct rational places `a,b,c in F_q`. Put

\[
 X=\chi(D(a)),\qquad Y=\chi(D(b)),\qquad Z=\chi(D(c)),
\]

with `chi(0)=0`, and define the elliptic curve

\[
 E_{a,b,c}: y^2=(a-z)(b-z)(c-z).
\]

Write

\[
 t=t_{a,b,c}=q+1-\#E_{a,b,c}(\mathbf F_q)
 =-\sum_{z\in\mathbf F_q}\chi((a-z)(b-z)(c-z)).
\tag{1}
\]

Then the complete squarefree family satisfies

\[
 \boxed{\sum_{D\in\mathcal H_5(q)}XYZ=3(q-2)t.}
\tag{2}
\]

This is the key transition: the two-place law only contains elementary
polynomials in `q` and squareclass orientations, whereas the first
three-place product already sees the Frobenius trace of an elliptic curve.

Let

\[
 A=q^4(q-1),\qquad C=2q-3,\qquad \epsilon=\chi(-1),
\]

and

\[
 s=\chi(b-a)+\chi(c-a)+\chi(c-b).
\]

For the third-cumulant interaction defect

\[
 \Delta^{(3)}_3
 =\kappa_3(X+Y+Z)-\kappa_3(X)-\kappa_3(Y)-\kappa_3(Z),
\]

the exact answer is

\[
 \boxed{
 \Delta^{(3)}_3
 ={3(1+\epsilon)Cs+18(q-2)t\over A}.}
\tag{3}
\]

When `q = 3 mod 4`, the pair-orientation term vanishes and (3) is a pure
elliptic Frobenius channel. When `q = 1 mod 4`, both the elementary pair term
and the elliptic term survive.

## 1. The triple Euler product

Define the primitive quadratic character

\[
 \psi_{a,b,c}(F)=\chi(F(a)F(b)F(c)).
\]

It has conductor `(T-a)(T-b)(T-c)` and is odd at infinity. Its degree-two
Dirichlet `L`-polynomial is the numerator of the displayed elliptic curve:

\[
 L(u,\psi_{a,b,c})=1-tu+qu^2.
\tag{4}
\]

The sign convention in (4) is fixed directly by the degree-one coefficient:

\[
 \sum_{z\in\mathbf F_q}\psi_{a,b,c}(T-z)
 =\sum_z\chi((a-z)(b-z)(c-z))=-t.
\]

Because `psi^2` is the indicator of coprimality to the three rational
conductor factors,

\[
 L(u^2,\psi^2)={(1-u^2)^3\over1-qu^2}.
\]

Squarefree Euler factorization therefore gives

\[
 \sum_{D\ {\rm monic\ squarefree}}\psi(D)u^{\deg D}
 ={(1-tu+qu^2)(1-qu^2)\over(1-u^2)^3}.
\tag{5}
\]

Now

\[
 (1-u^2)^{-3}=\sum_{j\ge0}\binom{j+2}{2}u^{2j}.
\]

The coefficient of `u^5` in (5) is

\[
 -6t+3qt=3(q-2)t,
\]

which proves (2) for every odd prime power.

## 2. From the triple product to the cumulant defect

Every one-place mean vanishes exactly. Since `X,Y,Z` lie in `{-1,0,1}`, their
individual third moments and third cumulants vanish as well. Expanding the
cube gives

\[
 \Delta^{(3)}_3
 =3\sum_{i\ne j}\mathbb E[X_i^2X_j]+6\mathbb E[XYZ].
\tag{6}
\]

The exact two-place theorem gives, for each unordered pair,

\[
 \mathbb E[X_i^2X_j]+\mathbb E[X_iX_j^2]
 =(1+\epsilon)\chi(a_j-a_i){C\over A}.
\tag{7}
\]

Summing (7) over the three pairs and inserting (2) into (6) proves (3).

## 3. Scale and interpretation

Hasse's bound `|t| <= 2 sqrt(q)` gives

\[
 \left|{18(q-2)t\over A}\right|
 \le {36(q-2)\sqrt q\over q^4(q-1)}.
\tag{8}
\]

Thus the elliptic channel has upper-envelope scale `q^-7/2`, while the
elementary pair correction is of scale `q^-4`. The half-integral scale is not
a universal asymptotic: `t` can vanish for particular triples. It says that a
third place makes a weight-one Frobenius source available, and that source can
dominate the lower-order pair coupling.

This supplies a concrete arithmetic version of Frobenius interferometry. A
phase-coherent three-place observable does not merely detect a compact-group
resonance; it can isolate the `L`-polynomial of the auxiliary elliptic curve
cut out by the three marked places. The next question is whether a
nuisance-quotiented higher detector produces a similarly named geometric
channel rather than only raw local coefficients.

## 4. Controls, provenance, and replay

The formal producer computes the `u^5` coefficient of (5) in a sparse exact
polynomial ring in `(q,t)`. It also exhausts two tiny prime-field controls:

| `q` | places | monic candidates | squarefree members | `t` | `sum XYZ` | third-defect numerator |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | `(0,1,2)` | 243 | 162 | 0 | 0 | 0 |
| 5 | `(0,1,2)` | 3,125 | 2,500 | -2 | -18 | -66 |

Together these visit 3,368 candidates, below the enforced 4,096-atom cap.
No extension field, curve family, zero, or broad parameter sweep is
enumerated. The all-`q` proof is equation (5), not these controls.

The packet hash-locks the exact two-place theorem at commit `a91f98532`, blob
`95f29d89e4eaf953ab5ecf0675e061000d7a9cef`, and payload
`18119e393842cfbe1f3ee7f594466eedf554004f9479f94338675921a3b0f859`.

```text
python -B research/l-families/atlas/function_field/quadratic_family_three_place_elliptic_interference.py --check
python -O -B research/l-families/atlas/function_field/quadratic_family_three_place_elliptic_interference.py --check
python -m pytest -q tests/test_quadratic_family_three_place_elliptic_interference.py
python -O -m pytest -q tests/test_quadratic_family_three_place_elliptic_interference.py
```

No external novelty claim is made.
