# Tensor/symmetric-power subtorus rigidity

## 1. Result

Fix an integer \(r\geq 1\).  On a formal determinant-one torus, the weights of

\[
 \operatorname{Std}(w^a)\otimes\operatorname{Sym}^r(w^b)
\]

are the multiset

\[
 W_r(a,b)=
 \{\epsilon a+b(r-2j):\epsilon\in\{+1,-1\},\ 0\leq j\leq r\}.
 \tag{1}
\]

The target \(\operatorname{Sym}^{2r+1}(w)\) has the multiplicity-free odd
interval

\[
 O_r=\{-(2r+1),-(2r-1),\ldots,2r-1,2r+1\}.
 \tag{2}
\]

The complete integer classification is

\[
 W_r(a,b)=O_r
 \quad\Longleftrightarrow\quad
 (|a|,|b|)=(r+1,1)\ \text{or}\ (1,2).
 \tag{3}
\]

Thus the signed solutions are exactly

\[
 (a,b)=(\sigma(r+1),\tau)
 \quad\text{or}\quad
 (a,b)=(\sigma,2\tau),
 \qquad \sigma,\tau\in\{+1,-1\}.
 \tag{4}
\]

This turns the two all-\(r\) graph identities in the locked degree-six
predecessor from sufficient examples into an exhaustive classification among
integer monomial one-parameter subtori.

## 2. Elementary proof

The two Weyl involutions are independent.  Changing \(a\) to \(-a\) exchanges
\(\epsilon=+1\) and \(\epsilon=-1\), while changing \(b\) to \(-b\) reverses
\(j\) by \(j\mapsto r-j\).  We may therefore put

\[
 A=|a|,\qquad B=|b|.
\]

If \(A=0\), every weight supplied by one value of \(j\) occurs for both
choices of \(\epsilon\).  If \(B=0\), each of \(+A\) and \(-A\) occurs \(r+1\)
times.  Neither can equal the multiplicity-free target (2), so \(A,B\geq1\).

The largest source weight is \(A+rB\), whereas the largest target weight is
\(2r+1\).  Equality of the multisets forces

\[
 A+rB=2r+1.
 \tag{5}
\]

Since \(A\geq1\), equation (5) gives \(B\leq2\).  If \(B=1\), then
\(A=r+1\).  If \(B=2\), then \(A=1\).  There are no other cases.

Both survivors really work.  For \((A,B)=(r+1,1)\), the \(+A\) translate is

\[
 \{2r+1,2r-1,\ldots,1\},
\]

and the \(-A\) translate is its negative half.  For \((A,B)=(1,2)\), the two
translates are

\[
 \{2r+1-4j:0\leq j\leq r\},\qquad
 \{2r-1-4j:0\leq j\leq r\},
\]

the even- and odd-indexed subsequences of the complete odd interval.  This
proves (3).

## 3. Multiplicity and symmetry audit

For \(A,B>0\), a weight in the \(+A\) translate equals one in the \(-A\)
translate precisely when

\[
 A+B(r-2j)=-A+B(r-2k),
\]

or equivalently

\[
 A/B=j-k\in\{1,\ldots,r\}.
 \tag{6}
\]

Such an overlap has multiplicity at least two and is forbidden by (2).  The
first canonical family has \(A/B=r+1\); the second has \(A/B=1/2\).  Hence
both are overlap-free.  Equation (6) is not needed for the maximum-weight
proof, but closes the possible multiplicity loophole explicitly.

The substitution \(w\mapsto w^{-1}\) changes both exponent signs at once.
The two source Weyl involutions are stronger: they allow the signs of \(a\)
and \(b\) to change independently.  These exponent inversions must not be
confused with multiplying a torus matrix by the central element \(-I\).

At \(r=1\), both source factors are standard two-dimensional factors and

\[
 W_1(a,b)=\{\pm a\pm b\}=W_1(b,a).
\]

Consequently the two canonical classes \((2,1)\) and \((1,2)\) form one orbit
under factor interchange.  There are no extra signed solutions.  For
\(r>1\), the factors have dimensions \(2\) and \(r+1\); interchange is not a
symmetry, and swapping either canonical pair does not give a classified pair.

## 4. Nonprimitive target exponent

There is a useful strengthening.  For every nonzero integer \(c\),

\[
 W_r(a,b)=cO_r
 \quad\Longleftrightarrow\quad
 (|a|,|b|)=|c|(r+1,1)\ \text{or}\ |c|(1,2).
 \tag{7}
\]

Indeed, two successive weights inside either source progression differ by
\(2b\).  Every difference between two elements of \(cO_r\) is divisible by
\(2c\), so \(c\mid b\).  Every source weight belongs to \(cO_r\); subtracting
the now \(c\)-divisible \(b(r-2j)\) term shows that \(c\mid a\).  Divide (1)
by \(|c|\) and apply (3).  Thus (7) classifies all integer one-parameter
subtorus homomorphisms modulo their common nonprimitive reparametrization.

When \(c=0\), the target consists only of zero with multiplicity \(2r+2\).
Then successive source weights force \(b=0\), and the two signs force \(a=0\).
This unique collapsed map is not a subtorus; the producer's scaled theorem
API deliberately refuses \(c=0\).

## 5. Dickson/Chebyshev graph equations

Let \(z=w+w^{-1}\), and define the integral Dickson trace polynomials by

\[
 D_0(z)=2,\qquad D_1(z)=z,\qquad
 D_{n+1}(z)=zD_n(z)-D_{n-1}(z).
 \tag{8}
\]

Then

\[
 D_n(w+w^{-1})=w^n+w^{-n}.
 \tag{9}
\]

Writing \(x=u+u^{-1}\) and \(y=v+v^{-1}\), the two canonical graph equations
are therefore

\[
 x=D_{r+1}(z),\quad y=z,
 \tag{10}
\]

and

\[
 x=z,\quad y=D_2(z)=z^2-2.
 \tag{11}
\]

Negative cocharacter exponents give the same equations because
\(D_{-n}=D_n\).  Central scalar signs are different.  With the target \(w\)
fixed, write source central signs as
\(u\mapsto(-1)^{\delta_u}u\) and
\(v\mapsto(-1)^{\delta_v}v\).  The tensor spectrum is unchanged exactly when

\[
 \delta_u+r\delta_v\equiv0\pmod2.
 \tag{12}
\]

For \(r=2\), (12) forces \(\delta_u=0\) and leaves \(\delta_v\) free.  This is
exactly why the locked degree-six equations have the two \(y\)-sign branches
\(y=\pm z\) and \(y=\pm(z^2-2)\).

## 6. Raw weight bookkeeping

The normalized torus theorem compares spectra of absolute value one.  The raw
source
\(\operatorname{Std}(E_A)\otimes\operatorname{Sym}^r(E_B)\) has motivic
weight \(r+1\), whereas \(\operatorname{Sym}^{2r+1}(E_C)\) has weight
\(2r+1\).  The typed raw comparison is therefore

\[
 P_{\operatorname{Std}(A)\otimes\operatorname{Sym}^r(B)}
 \bigl(q^{r/2}T\bigr)
 =P_{\operatorname{Sym}^{2r+1}(C)}(T).
 \tag{13}
\]

For even \(r\), the dilation is an integral power of \(q\).  For odd \(r\), a
raw formula requires a chosen square root of \(q\), just as in the earlier
\(SO(4)/\operatorname{Sym}^3\) comparison.  The formal normalized result
(3) has no square-root choice.

## 7. Exact bounded replay and source lock

The producer exhausts every signed pair

\[
 |a|,|b|\leq2r+1
\]

for $1\leq r\leq16$.  This box is forced by (5), not chosen heuristically.
It checks $27{,}344$ signed pairs and emits $720{,}816$ small integer weight
atoms, below a hard $800{,}000$-atom cap.  Separate rows check only the eight
predicted signed solutions at $r=32$ and $r=64$, without enumerating either
surrounding box.  The proof is the five-line maximum-weight argument; the
finite replay is regression only.

The packet locks both the producer and the canonical fixture of
`elliptic_tensor_sym2_sym5_spectral_intersection`.  In particular it binds
predecessor payload
`e2c9c7ac3d1329b7b911a5214d36935d2694436cbe6d9cce551b94f8486b01ba`
before sharpening its two universal graph identities.

Replay with:

```text
python -B research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_subtorus_rigidity.py --check
python -B -O research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_subtorus_rigidity.py --check
python -B -m pytest -q tests/test_elliptic_tensor_symmetric_power_subtorus_rigidity.py
python -B -O -m pytest -q tests/test_elliptic_tensor_symmetric_power_subtorus_rigidity.py
```

All arithmetic is exact standard-library integer arithmetic.  There are no
floats, random samples, symbolic packages, curve searches, field enumerations,
or trace-range enumerations.

## 8. Scope firewalls

The theorem is generic and monomial.  It is equality of Laurent-character
multisets for a formal \(w\), or equivalently for a generic characteristic-zero
torus parameter.  It does **not** say the following.

- At a root of unity, exponents are compared modulo the torsion order.  Extra
  cyclotomic coincidences and new multiplicities can occur.  The order
  (7,12,14) residuals in the degree-six predecessor are not removed by this
  theorem.
- A nonmonomial rational or algebraic curve in trace space need not come from
  an integer cocharacter.  Such components, and isolated rational points, are
  outside (3) and (7).
- Except for the locked \(r=2\) predecessor, this packet does not classify the
  full rational coefficient intersection.
- Equality along a subtorus is not an isomorphism of the ambient
  representations.
- No Hasse-lattice point is promoted to a linked triple of elliptic curves, a
  variety, a motive, or a compatible family.
- No Euler product, automorphy, modularity, global family, analytic
  continuation, zero-free region, RH, or GRH consequence is asserted.
- The elementary identity is recorded without a literature-priority or
  novelty claim.

The next mathematical boundary is now sharper: classify the torsion residuals
for general \(r\), and determine whether any nonmonomial positive-dimensional
components survive the full coefficient equations.
