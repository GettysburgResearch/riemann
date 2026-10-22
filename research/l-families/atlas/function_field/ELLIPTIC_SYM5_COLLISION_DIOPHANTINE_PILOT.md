# Elliptic `Sym^5` scalar-collision Diophantine pilot

## Result

For

\[
E_5(t,q)=t^5-4qt^3+3q^2t=t(t^2-q)(t^2-3q),
\]

the non-diagonal scalar-collision equation factors as

\[
\frac{E_5(x,q)-E_5(y,q)}{x-y}
=K-4qH+3q^2=0,
\]

where

\[
H=x^2+xy+y^2,
\qquad
K=x^4+x^3y+x^2y^2+xy^3+y^4.
\]

Its discriminant as a quadratic in \(q\) is \(4W\), with

\[
W=x^4+5x^3y+9x^2y^2+5xy^3+y^4,
\]

and the exact elimination identity is

\[
(3q-2H)^2-W=3(K-4qH+3q^2).
\]

This packet produces four substantive project-relative results:

1. A complete discriminant-first census of distinct Hasse-admissible integer
   traces over every odd prime power \(q\le 2000\), without enumerating a curve
   or a finite field.
2. The complete zero-fiber and weighted-scaling laws.
3. An explicit birational bridge from the collision quartic to a positive-rank
   elliptic curve.
4. Three exact non-cyclotomic prime-field collision bases, including a large
   prime certified by a standard-library Lucas/Pocklington certificate.

These are scalar-character results. They are not a classification of full
local factors, integral points, global compatible families, or Euler products.

## Complete frozen census through \(q=2000\)

The largest possible trace has absolute value
\(\lfloor 2\sqrt{2000}\rfloor=89\). Instead of repeating the trace-pair loop
for every \(q\), the producer examines the 15,931 unordered pairs \(x<y\)
once, keeps the 295 pairs for which \(W\) is a square, and tests the 590 signed
values

\[
q=\frac{2H\mathbin{\pm}\sqrt W}{3}.
\]

The exact outcome is 61 collision pairs at 21 prime powers:

- 38 zero/nonzero pairs;
- 19 sign pairs;
- 4 general pairs.

The four general pairs are exactly

\[
(q,x,y)=(31,-7,3),(31,-3,7),
(1021,-40,19),(1021,-19,40).
\]

The two pairs at each \(q\) are simultaneous negations. No completeness is
asserted beyond the frozen bound.

## Zero fibers and the sign issue

If \(q=p^a\) is an odd prime power, then the integral zero fiber of \(E_5\) is

\[
\begin{cases}
\{0,\pm p^{a/2}\}, & a\text{ even},\\
\{0,\pm 3^{(a+1)/2}\}, & p=3,\ a\text{ odd},\\
\{0\}, & \text{otherwise}.
\end{cases}
\]

Thus every nontrivial zero fiber contributes two zero/nonzero pairs and one
sign pair. This extends the earlier \(3^{\text{odd}}\) construction by exposing
the separate \(q=p^{2k}\) family.

The scalar coincidences do not usually imply equality of the full degree-six
factor. Its next two coefficients are

\[
c_2=q(q-t^2)(3q-t^2)(q^2-3qt^2+t^4)
\]

and

\[
c_3=-q^3t(2q-t^2)(3q-t^2)(q^2-3qt^2+t^4).
\]

Consequently, zero/nonzero pairs separate at \(c_2\); sign pairs with
\(t^2=q\) separate at \(c_3\); and the special sign pairs with \(t^2=3q\)
have equal full factors. In the finite census only three of the 61 scalar
collisions have equal full factors.

## Exact scaling theorem

The equation is weighted homogeneous:

\[
Q(dx,dy,d^2q)=d^4Q(x,y,q),
\qquad
E_5(dt,d^2q)=d^5E_5(t,q).
\]

Therefore a primitive collision at a prime \(p\) gives an infinite exact
prime-power tower at

\[
q=p^{2k+1},\qquad (x,y)=(p^kx_0,p^ky_0).
\]

This is an infinite family of scalar collisions, not a claim that infinitely
many primitive prime bases exist. It is also **not** an elliptic-curve
realization tower. For each of the three bases below, \(p>3\). Once \(k\ge1\),
the extension degree \(2k+1\) is odd and each nonzero scaled trace is divisible
by \(p\). In Waterhouse's classification, ordinary case (1) therefore fails;
cases (2) and (3) require even extension degree; case (4) requires
\(p\in\{2,3\}\); and case (5) requires trace zero. Thus only the prime base
\(k=0\) is locally realized for these three towers. The higher levels remain
exact Hasse-lattice/scalar-polynomial identities.

There is a related firewall for the square-\(q\) zero fibers. When
\(q=p^{2k}\), the traces \(\pm\sqrt q\) occur as elliptic traces only when
\(p\not\equiv1\pmod3\), while trace zero occurs only when
\(p\not\equiv1\pmod4\). Hence the algebraic three-point zero fiber is not
automatically a simultaneously realized elliptic zero fiber. By contrast, for
\(q=3^{\text{odd}}\), trace zero and \(\pm\sqrt{3q}\) are precisely covered by
Waterhouse cases (5) and (4).

## Elliptic-curve bridge

Put \(r=x/y\), \(v=z/y^2\), and then

\[
u=r+r^{-1},\qquad w=v/r.
\]

The quartic becomes the conic \(w^2=u^2+5u+7\). Parametrizing it from
\((-2,1)\) with

\[
m=\frac{w-1}{u+2}
\]

and retaining the square condition needed to recover \(r\) gives

\[
\mathcal E:\quad Y^2=X^3-6X+5,
\qquad
X=2m,\quad Y=(r-r^{-1})(m^2-1).
\]

Away from finitely many exceptional points, the inverse is

\[
r=\frac{-X^2-2X+6+2Y}{X^2-4},
\qquad
w=-\frac{X^2-2X+4}{X^2-4}.
\]

The polynomial discriminant of the quartic is 189 and the Weierstrass
discriminant is \(16\cdot189=3024\). On \(\mathcal E\), let
\(Q=(-2,3)\). Exact group addition gives \(2Q=(5,-10)\). If \(Q\) were torsion,
then \(2Q\) would be torsion; the Lutz--Nagell criterion would require
\((-10)^2\) to divide \(|4(-6)^3+27(5)^2|=189\), which it does not. Hence
\(Q\) is nontorsion and the quartic has infinitely many rational points.
This positive-rank statement does not classify its integral or prime-power
points.

## Six exact multiples and a third prime base

Inverting \(nQ\), clearing the ratio primitively, and selecting the unique
positive integral Hasse-admissible \(q\) gives:

| \(n\) | \((x,y)\) | \(q\) | factorization |
|---:|---:|---:|---:|
| 2 | \((-7,3)\) | 31 | prime |
| 3 | \((-40,19)\) | 1,021 | prime |
| 4 | \((669,91)\) | 547,921 | \(11\cdot49{,}811\) |
| 5 | \((-23{,}541,26{,}440)\) | 626,640,421 | \(11\cdot631\cdot90{,}281\) |
| 6 | \((-370{,}357,3{,}646{,}273)\) | 11,429,428,518,271 | \(131\cdot1171\cdot3301\cdot22571\) |
| 7 | \((-290{,}364{,}080,756{,}187{,}719)\) | 363,804,984,411,209,881 | prime |

For the last row,

\[
q-1=2^3\cdot3\cdot5\cdot7^2\cdot11\cdot4003\cdot5843\cdot240479.
\]

All factors on the right are proved prime by trial division only through 490.
The witness \(a=23\) satisfies

\[
23^{q-1}\equiv1\pmod q,
\qquad
\gcd(23^{(q-1)/\ell}-1,q)=1
\]

for every distinct prime \(\ell\mid q-1\). The full \(q-1\)
Lucas/Pocklington criterion therefore proves that \(q\) is prime. Only six
elliptic additions are used; no large blind scan or factor search is hidden in
the producer.

All three prime rows have \(|x|,|y|<2\sqrt q\) and each trace is coprime to
\(q\). Waterhouse's Theorem 4.1, case (1), therefore shows that each trace is
realized by an ordinary elliptic isogeny class over its corresponding prime
field. This asserts two separate local curves at each prime, not one global
family. Their scalar `Sym^5` traces agree, while \(c_2\) separates their full
local factors.

## Conjectural target

The evidence suggests that primitive prime-power general collisions are sparse
and governed by simultaneous denominator, integrality, Hasse, and prime-power
conditions on this positive-rank elliptic curve. The packet does **not** claim
an integral-point classification, completeness beyond \(q=2000\), or
infinitely many primitive prime values. A natural next step is an exact
descent/S-integral analysis of the maps \(r,w,q\), with the prime-power
condition kept separate from rational-point generation.

## Literature and novelty boundary

- É. Lutz, [*Sur l'équation \(y^2=x^3-Ax-B\) dans les corps
  p-adiques*](https://doi.org/10.1515/crll.1937.177.238) (1937), is used only
  for the classical torsion criterion.
- W. C. Waterhouse, [*Abelian varieties over finite
  fields*](https://numdam.org/articles/10.24033/asens.1183/) (1969), Theorem
  4.1, is used only for the stated local trace realization and nonrealization
  boundaries.

No literature-priority search was performed. “New” here means newly derived
and locked in this project, not a claim of external mathematical priority.

## Replay and resource contract

```powershell
python -B research/l-families/atlas/function_field/elliptic_sym5_collision_diophantine_pilot.py --check
python -B -O research/l-families/atlas/function_field/elliptic_sym5_collision_diophantine_pilot.py --check
python -B -m unittest tests.test_elliptic_sym5_collision_diophantine_pilot
python -B -O -m unittest tests.test_elliptic_sym5_collision_diophantine_pilot
```

The default replay accounts for 16,966 high-level work units under an exclusive
cap of 500,000. Of these, 15,931 are unordered trace pairs. It performs zero
curve or field enumerations. Inputs above the frozen \(q\)-bound and runs that
would meet the exclusive cap are refused.

The prior symmetric-power trace-alias packet is locked at payload
`046f76f43a2af3ac296f5c18c258e61f138e122bee38ec618af489e7e3a9e50e`.
It supplies provenance only; this packet rederives its own algebra and data.
