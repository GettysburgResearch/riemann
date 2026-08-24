# Exact coefficient recovery for elliptic `Sym^5` local factors

## The theorem

Let

\[
L_E(T)=1-tT+qT^2=(1-\alpha T)(1-\beta T),
\qquad
\alpha+\beta=t,\quad \alpha\beta=q,
\]

and let \(q\ne0\) and \(x,y,q\in\mathbb Q\). Write

\[
P_5(t,q;T)=\det(1-\operatorname{Sym}^5(\operatorname{Frob})T)
=1+c_1T+c_2T^2+c_3T^3+\cdots .
\]

The scalar character and the next two coefficients are

\[
\begin{aligned}
E_5(t,q)&=t^5-4qt^3+3q^2t
=t(t^2-q)(t^2-3q),\\
c_1(t,q)&=-E_5(t,q),\\
c_2(t,q)&=q(q-t^2)(3q-t^2)(q^2-3qt^2+t^4),\\
c_3(t,q)&=-q^3t(2q-t^2)(3q-t^2)
\mathbin{\cdot}(q^2-3qt^2+t^4).
\end{aligned}
\]

Then the exact recovery classification over \(\mathbb Q\) is

\[
\bigl(E_5(x,q),c_2(x,q)\bigr)
=\bigl(E_5(y,q),c_2(y,q)\bigr)
\]

if and only if one of the following holds:

1. \(x=y\);
2. \(x=-y\) and \(x^2=q\);
3. \(x=-y\) and \(x^2=3q\).

Adding \(c_3\) removes precisely the second alternative:

\[
\bigl(E_5(x,q),c_2(x,q),c_3(x,q)\bigr)
=\bigl(E_5(y,q),c_2(y,q),c_3(y,q)\bigr)
\]

if and only if

\[
x=y
\qquad\text{or}\qquad
x=-y\ \text{and}\ x^2=3q.
\]

The same classification holds for equality of the complete degree-six local
factors. Indeed the coefficient vector is

\[
\bigl(1,c_1,c_2,c_3,q^5c_2,q^{10}c_1,q^{15}\bigr),
\]

so at fixed \(q\) the first three nonconstant coefficients determine all the
others.

This is a local rational theorem. It does not assume that \(q\) is positive, a
prime power, or that either trace is realized by an elliptic curve.

## Difference equations

For \(x\ne y\), scalar equality is equivalent to \(Q=0\), where

\[
\begin{aligned}
Q&=\frac{E_5(x,q)-E_5(y,q)}{x-y}\\
&=K-4qH+3q^2,\\
H&=x^2+xy+y^2,\\
K&=x^4+x^3y+x^2y^2+xy^3+y^4.
\end{aligned}
\]

The second-coefficient difference factors without any division:

\[
c_2(x,q)-c_2(y,q)=q(x^2-y^2)R,
\]

where

\[
\begin{aligned}
R={}&-13q^3+16q^2(x^2+y^2)\\
&-7q(x^4+x^2y^2+y^4)\\
&+(x^6+x^4y^2+x^2y^4+y^6).
\end{aligned}
\]

This already separates the cases in which \(x^2=y^2\). Over
\(\mathbb Q\), that equality means \(x=y\) or \(x=-y\). The first is
diagonal. In the non-diagonal sign case, scalar equality says

\[
0=E_5(x,q)-E_5(-x,q)=2x(x^2-q)(x^2-3q).
\]

Because \(q\ne0\) and \(x\ne-y=y\), one has \(x\ne0\), leaving exactly
\(x^2=q\) and \(x^2=3q\). Since \(c_2\) is even in \(t\), both survive
through \(c_2\).

It remains to rule out a collision with \(x^2\ne y^2\). In that case,
\(q\ne0\) lets us divide the displayed second-coefficient identity, so any
such collision would be a common \(q\)-root of \(Q\) and \(R\).

## Exact resultant, with nothing dropped

Put

\[
\begin{aligned}
S&=x^2+y^2,\\
U&=x^4+x^2y^2+y^4,\\
V&=x^6+x^4y^2+x^2y^4+y^6.
\end{aligned}
\]

Thus \(Q=3q^2-4Hq+K\) and
\(R=-13q^3+16Sq^2-7Uq+V\). Literal polynomial division, after clearing the
single denominator, gives

\[
9R=(-39q+48S-52H)Q+aq+b,
\]

with

\[
\begin{aligned}
a={}&-40x^4-185x^3y-264x^2y^2-185xy^3-40y^4,\\
b={}&13x^6+56x^5y+69x^4y^2+60x^3y^3\\
&\quad+69x^2y^4+56xy^5+13y^6.
\end{aligned}
\]

This identity can be checked by multiplying the right side: the quotient
first cancels the \(q^3\) and \(q^2\) terms, and its remaining \(q\) and
constant terms are exactly \(a\) and \(b\).

If \(\rho_1,\rho_2\) are the roots of \(Q\), then

\[
\rho_1+\rho_2=\frac{4H}{3},
\qquad
\rho_1\rho_2=\frac K3.
\]

At either root, \(R(\rho_i)=(a\rho_i+b)/9\). Remembering that the leading
coefficient of \(Q\) is \(3\), the definition of the resultant gives the
elementary norm formula

\[
9\operatorname{Res}_q(Q,R)=Ka^2+4Hab+3b^2.
\]

Direct multiplication of these explicit binary forms now yields

\[
\begin{aligned}
\operatorname{Res}_q(Q,R)
={}&(x^2-3y^2)(3x^2-y^2)(x^2+3xy+y^2)\\
&\mathbin{\cdot}(x^3-3x^2y-4xy^2-y^3)\\
&\mathbin{\cdot}(x^3+4x^2y+3xy^2-y^3).
\end{aligned}
\]

There is no suppressed scalar, no removed \(x\), \(y\), \(x-y\), or
\(x+y\) factor, and every displayed factor has multiplicity one. As an
additional audit, the unfactored coefficient vector from \(x^{12}\) through
\(y^{12}\) is

\[
(3,12,-37,-235,-228,467,1016,467,-228,-235,-37,12,3).
\]

The producer obtains this vector twice: once from a literal \(5\)-by-\(5\)
Sylvester determinant over sparse integer binary polynomials, and once by
multiplying the five displayed factors. It separately verifies the norm
identity above. No symbolic-algebra package is imported.

## Why none of the five factors has a rational projective zero

Suppose first that \(y=0\). Every factor then becomes a nonzero scalar
multiple of \(x^2\) or \(x^3\), so its vanishing forces \(x=0\).

Now take \(y\ne0\) and put \(r=x/y\).

- The first factor would give \(r^2=3\).
- The second would give \(3r^2=1\), hence \((1/r)^2=3\).
- The third gives \(r^2+3r+1=0\), whose discriminant is \(5\).

Neither \(3\) nor \(5\) is a rational square: in a reduced fraction whose
square equals either prime, the prime has odd valuation on one side and even
valuation on the other.

The remaining affine cubics are monic:

\[
r^3-3r^2-4r-1
\qquad\text{and}\qquad
r^3+4r^2+3r-1.
\]

By the rational-root theorem their only possible rational roots are
\(\pm1\). Their values at \(1,-1\) are respectively \((-7,-1)\) and
\((7,-1)\). Neither has a rational root.

Consequently the resultant has no nonzero rational projective zero. A common
root \(Q=R=0\) would therefore force \(x=y=0\), contradicting
\(x^2\ne y^2\). This completes the proof of the \((E_5,c_2)\)
classification.

## The third coefficient and the two sign strata

The formula for \(c_3\) is odd in \(t\). Hence a sign pair survives \(c_3\)
exactly when \(c_3(x,q)=0\). On the two surviving \((E_5,c_2)\) strata:

\[
\begin{array}{c|c}
x^2=q & c_3(x,q)=2q^7x\ne0,\\
x^2=3q & c_3(x,q)=0.
\end{array}
\]

Thus \(c_3\) separates the \(x^2=q\) sign ambiguity, while
\(x^2=3q\) is an unavoidable alias of the entire local factor. On the latter
stratum all of \(c_1,c_2,c_3\) vanish, so the common factor is
\(1+q^{15}T^6\).

The zero cases are also now explicit. The point \(x=y=0\) is diagonal. If
exactly one of \(x,y\) is zero, equality of \(E_5\) forces the other trace
onto \(t^2=q\) or \(t^2=3q\), where \(c_2=0\), while
\(c_2(0,q)=3q^5\ne0\). Such a pair cannot survive \(c_2\).

## Plethystic explanation

Let

\[
E_m(t,q)=\sum_{j=0}^{m}\alpha^{m-j}\beta^j.
\]

The second coefficient is the trace on
\(\Lambda^2\operatorname{Sym}^5V\). The exact decomposition is

\[
\Lambda^2\operatorname{Sym}^5V
\simeq
(\operatorname{Sym}^8V\otimes\det V)
\oplus(\operatorname{Sym}^4V\otimes(\det V)^3)
\oplus(\det V)^5,
\]

and therefore

\[
c_2=qE_8+q^3E_4+q^5.
\]

The normalization is visible directly in the weights. The six
\(\operatorname{Sym}^5\) weights are
\(\alpha^{5-i}\beta^i\), \(0\le i\le5\). A wedge pair \(i<j\) has weight
\(\alpha^{10-i-j}\beta^{i+j}\). Its multiplicities as \(i+j\) runs from
1 through 9 are

\[
(1,1,2,2,3,2,2,1,1).
\]

The summand \(qE_8\) contributes one copy at every index \(1,\ldots,9\);
\(q^3E_4\) adds one at \(3,\ldots,7\); and \(q^5\) adds the final copy at
index \(5\). This is the complete 15-weight multiset, not only a character
specialization. Expanding the trace identity gives

\[
c_2=qt^8-7q^2t^6+16q^3t^4-13q^4t^2+3q^5,
\]

which is the factored formula used above.

For an independent check on the next coefficient, the producer also verifies
the 20 weights in

\[
\Lambda^3\operatorname{Sym}^5V
\simeq
(\operatorname{Sym}^9V\otimes(\det V)^3)
\oplus(\operatorname{Sym}^5V\otimes(\det V)^5)
\oplus(\operatorname{Sym}^3V\otimes(\det V)^6).
\]

Since \(c_3\) carries the determinant-polynomial sign,

\[
-c_3=q^3E_9+q^5E_5+q^6E_3.
\]

The three summands contribute beta-exponent intervals \(3\) through \(12\),
\(5\) through \(10\), and \(6\) through \(9\), exactly matching all
\(\binom63=20\) triple weights.

## Frozen collision replay and minimality

The preceding theorem is all-\(\mathbb Q\); it is not inferred from a finite
search. The packet nevertheless replays every one of the 61 scalar-collision
rows frozen in the source packet:

| source collision class | first separated at \(T^2\) | first separated at \(T^3\) | complete-factor alias |
|---|---:|---:|---:|
| general | 4 | 0 | 0 |
| zero/nonzero | 38 | 0 | 0 |
| sign | 0 | 16 | 3 |
| **total** | **42** | **16** | **3** |

Three small witnesses show that each depth is real:

- \((q,x,y)=(31,-7,3)\): the scalar aliases, but \(c_2\) separates;
- \((q,x,y)=(9,-3,3)\): \(E_5,c_2\) alias, but \(c_3\) separates;
- \((q,x,y)=(3,-3,3)\): the complete factors are equal.

The replay reads and validates the locked rows. It does not enumerate a finite
field, a curve, or even a new trace range.

## Replay, resources, and firewall

```powershell
python -B research/l-families/atlas/function_field/elliptic_sym5_coefficient_recovery.py --check
python -B -O research/l-families/atlas/function_field/elliptic_sym5_coefficient_recovery.py --check
python -B -m unittest tests.test_elliptic_sym5_coefficient_recovery
python -B -O -m unittest tests.test_elliptic_sym5_coefficient_recovery
```

The producer has an exclusive cap of 25,000 high-level work units. Its work
consists only of 120 determinant permutations, five factor multiplications,
35 exterior-power weight combinations, three exact plethystic
specializations, one source load, one norm check, and 61 locked-row replays.
Runs that would meet the cap are refused.

The source is locked simultaneously by path, schema, canonical payload hash,
and LF-normalized file hash. The theorem asserts only a local algebraic
classification over \(\mathbb Q\). It makes no claim about elliptic-curve
realization, automorphy, modularity, global compatible families, Euler
products, zero distributions, RH, or external literature priority.
