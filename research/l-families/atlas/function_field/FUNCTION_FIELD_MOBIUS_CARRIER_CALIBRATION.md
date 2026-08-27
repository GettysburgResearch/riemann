# Curve RH is exactly a disjoint Möbius-carrier energy law

Status: **exact all-curve degree-Möbius carrier criterion, exact
orthogonal packet identity, and exact reciprocal-root growth
classification; Weil RH is imported, not reproved, and integer RH/GRH
remain open**

Bounded replay:
[function_field_mobius_carrier_calibration.py](function_field_mobius_carrier_calibration.py).
Canonical summary:
[function_field_mobius_carrier_calibration.json](function_field_mobius_carrier_calibration.json).

Frozen source: the variational probability-carrier optimum at commit
**19f274c9335ecffb357e296b3fd5fefdeba5f3fd**. The producer pins its
four Git blobs and imports no live predecessor module.

## 0. Outcome

Let \(C/\mathbb F_q\) be a smooth projective geometrically connected
curve of genus \(g\), with zeta function

\[
 Z_C(u)
 =\exp\left(\sum_{r\ge1}{\#C(\mathbb F_{q^r})\over r}u^r\right)
 ={P_C(u)\over(1-u)(1-qu)}.
\tag{0.1}
\]

Write

\[
 P_C(u)=\prod_{j=1}^{2g}(1-\alpha_j u).
\tag{0.2}
\]

Let

\[
 M_C(n)
 =\sum_{\substack{D\ge0\\\deg D=n}}\mu_C(D)
 =[u^n]{1\over Z_C(u)}
\tag{0.3}
\]

be the degree-\(n\) divisor-Möbius sum, and normalize it by

\[
 b_C(n)=q^{-n/2}M_C(n).
\tag{0.4}
\]

Choose

\[
 S={\log q\over2},
\tag{0.5}
\]

and let \(J_S\) be the minimum-diagonal parabolic detector from the
frozen packet:

\[
 J_S(x)={6(S-2x)\over S^3}\mathbf1_{(0,S)}(x),
\qquad
 \|J_S\|_2^2={12\over S^3}
 ={96\over(\log q)^3}.
\tag{0.6}
\]

Define the degree-carrier field

\[
 H_{C,N}(t)
 =\sum_{n=0}^N b_C(n)J_S(t-n\log q)
\tag{0.7}
\]

and its energy

\[
 \mathcal E_C(N)
 =\int_{\mathbb R}|H_{C,N}(t)|^2\,dt.
\tag{0.8}
\]

The packets in (0.7) have disjoint interiors because

\[
 S<\log q.
\tag{0.9}
\]

Therefore

\[
\boxed{
 \mathcal E_C(N)
 ={96\over(\log q)^3}
 \sum_{n=0}^N|b_C(n)|^2.}
\tag{0.10}
\]

The complete curve RH is equivalent to the subexponential energy law

\[
\boxed{
 \left[
 |\alpha_j|=\sqrt q\quad(1\le j\le2g)
 \right]
 \Longleftrightarrow
 \mathcal E_C(N)=q^{o(N)}.}
\tag{0.11}
\]

Here \(q^{o(N)}\) means that for every \(\varepsilon>0\),

\[
 \mathcal E_C(N)=O_{C,\varepsilon}(q^{\varepsilon N}).
\tag{0.12}
\]

By the known Weil theorem, every such curve satisfies (0.11). If the
largest normalized reciprocal-root multiplicity is \(r_C\), then more
precisely

\[
 b_C(n)=O_C(n^{r_C-1}),
\qquad
\mathcal E_C(N)=O_C(N^{2r_C-1})
\quad(g\ge1),
\tag{0.13}
\]

In particular, for every genus,

\[
 \mathcal E_C(N)
 =O_C\!\left((1+N)^{\max(0,4g-1)}\right).
\tag{0.14}
\]

For \(g=0\), the reciprocal zeta function is a polynomial and the
energy is bounded.

This packet does not reprove Weil RH. Its value is architectural:
the number-field probability-carrier criterion has an exact
function-field realization in which the energy visibly measures the
reciprocal Frobenius spectrum, with no sampling, curve enumeration, or
random-matrix analogy.

## 1. Divisor Möbius coefficients

The effective-divisor Euler product is

\[
 Z_C(u)
 =\prod_{x\in|C|}
 (1-u^{\deg x})^{-1}.
\tag{1.1}
\]

Its reciprocal expands as

\[
 {1\over Z_C(u)}
 =\prod_{x\in|C|}(1-u^{\deg x})
 =\sum_{D\ge0}\mu_C(D)u^{\deg D}.
\tag{1.2}
\]

Taking degree-\(n\) coefficients proves (0.3). From (0.1),

\[
\boxed{
 \sum_{n\ge0}M_C(n)u^n
 ={(1-u)(1-qu)\over P_C(u)}.}
\tag{1.3}
\]

Substitute

\[
 u={v\over\sqrt q}.
\tag{1.4}
\]

The normalized generating function is

\[
\boxed{
 B_C(v):=
 \sum_{n\ge0}b_C(n)v^n
 =
 {(1-v/\sqrt q)(1-\sqrt q\,v)
 \over
 \prod_{j=1}^{2g}
 (1-(\alpha_j/\sqrt q)v)}.}
\tag{1.5}
\]

For a genuine smooth projective curve, the fraction is reduced at the
two displayed numerator roots. Indeed,

\[
 P_C(1)=\#\operatorname {Jac}(C)(\mathbb F_q)>0,
\tag{1.6}
\]

and the functional equation gives the corresponding nonvanishing at
\(u=1/q\). Thus no Frobenius pole relevant below is hidden by
cancellation with the two trivial reciprocal-zeta factors.

## 2. Orthogonal carrier packets

The support of the \(n\)-th summand in (0.7) is

\[
 [n\log q,\ n\log q+S].
\tag{2.1}
\]

If \(m\ne n\), the distance between their left endpoints is at least
\(\log q\), while \(S=(\log q)/2\). Hence their supports are disjoint.
Finite Fubini gives

\[
\begin{aligned}
 \mathcal E_C(N)
 &=
 \sum_{m,n\le N}
 b_C(m)\overline{b_C(n)}
 \int_{\mathbb R}
 J_S(t-m\log q)J_S(t-n\log q)\,dt\\
 &=
 \|J_S\|_2^2
 \sum_{n=0}^N|b_C(n)|^2.
\end{aligned}
\tag{2.2}
\]

Equation (0.6) now proves (0.10).

The parabolic carrier is not essential for orthogonality. Any nonzero
compact \(L^2\) detector of support shorter than \(\log q\) would give
the same root-growth criterion up to its norm. The parabolic carrier is
distinguished because it has the smallest possible diagonal among
positive normalized probability derivatives at that support.

This exact disjointness is special to the function-field degree lattice.
Integer logarithms are not equally spaced, so no analogous orthogonal
collapse is being inferred for the number-field beta source.

## 3. Energy growth detects the outer reciprocal root

Assume first that \(g\ge1\). The genus-zero reciprocal is a polynomial,
so its coefficient sequence is finitely supported and its energy is
bounded.

The poles of (1.5) occur at

\[
 v={\sqrt q\over\alpha_j}.
\tag{3.1}
\]

Let

\[
 \rho_C=\max_j{|\alpha_j|\over\sqrt q}.
\tag{3.2}
\]

Standard partial fractions for the fixed rational function (1.5) give

\[
 b_C(n)
 =f_C(n)+\sum_{\lambda}
 p_\lambda(n)\lambda^n,
\tag{3.3}
\]

where \(f_C\) is finitely supported and the \(\lambda\)'s are the
distinct normalized reciprocal roots

\[
 \lambda={\alpha_j\over\sqrt q},
\tag{3.4}
\]

and \(\deg p_\lambda\) is one less than the pole multiplicity.

If \(\rho_C\le1\), (3.3) gives

\[
 b_C(n)=O_C(n^{2g-1}),
\qquad
 \mathcal E_C(N)=O_C(N^{4g-1})
\quad(g\ge1).
\tag{3.5}
\]

This is already \(q^{o(N)}\).

Conversely, suppose (0.12) holds. Equation (0.10) gives

\[
 |b_C(n)|=q^{o(n)}.
\tag{3.6}
\]

Therefore the power series \(B_C(v)\) has radius of convergence at
least one. Since (1.5) is reduced, it has no pole in \(|v|<1\). Thus

\[
 \rho_C\le1.
\tag{3.7}
\]

Equivalently,

\[
 |\alpha_j|\le\sqrt q
 \qquad(1\le j\le2g).
\tag{3.8}
\]

This proves the energy/root-radius equivalence before using the
functional equation.

## 4. Functional equation individualizes the circle

The curve functional equation pairs reciprocal roots as

\[
 \alpha\longleftrightarrow {q\over\alpha}.
\tag{4.1}
\]

If every root satisfies (3.8), then its partner also satisfies

\[
 \left|{q\over\alpha}\right|\le\sqrt q.
\tag{4.2}
\]

Multiplication gives

\[
 |\alpha|=\sqrt q.
\tag{4.3}
\]

Thus the one-sided spectral-radius conclusion from the positive energy
becomes the full circle law. This proves the reverse implication in
(0.11).

The forward implication is immediate from the same partial-fraction
formula. Under the circle law, every \(|\lambda|=1\), so only the fixed
polynomial multiplicities in (3.3) remain. This proves (0.13).

In contrast with the integer-zeta problem, no family-to-principal
individualization step appears: \(P_C\) is already one finite
compatible-system numerator and its functional equation pairs its own
roots.

## 5. Genus-one exact control

For a formal genus-one numerator

\[
 P(u)=1-au+qu^2,
\tag{5.1}
\]

the degree-Möbius coefficients obey

\[
 M_n-aM_{n-1}+qM_{n-2}
 =
 \begin{cases}
 1,&n=0,\\
 -(q+1),&n=1,\\
 q,&n=2,\\
 0,&n\ge3.
 \end{cases}
\tag{5.2}
\]

The reciprocal roots are

\[
 \alpha_\pm={a\pm\sqrt{a^2-4q}\over2}.
\tag{5.3}
\]

The bounded replay uses \(q=5\) and three rows:

1. \(a=0\), a Weil-compatible unit-circle control;
2. \(a=4\), a second Weil-compatible near-edge control;
3. \(a=5\), a formal off-circle control.

The third row is not asserted to arise from a curve. It exists only to
verify that the recurrence and energy distinguish an expanding
normalized pole. The tempting choice \(a=q+1\) is deliberately avoided:
then \(P(u)=(1-u)(1-qu)\), and the two trivial reciprocal-zeta factors
cancel completely.

No elliptic curve, finite field, point, or polynomial is enumerated.

## 6. Relation to the integer beta criterion

The architecture now has a precise dictionary:

| integer beta source | curve divisor source |
|---|---|
| \(\beta(n)n^{-1/2}\) | \(M_C(n)q^{-n/2}\) |
| logarithmic source locations \(\log n\) | degree lattice \(n\log q\) |
| overlapping compact ratio packets | exactly disjoint packets when \(S<\log q\) |
| zeta pole obstruction after Abel continuation | rational reciprocal-root pole |
| functional equation reflects a hypothetical zero | curve functional equation pairs \(\alpha\) with \(q/\alpha\) |

The shared mechanism is:

\[
\text{normalized Möbius source}
\longrightarrow
\text{positive derivative-carrier energy}
\longrightarrow
\text{rightmost reciprocal pole}
\longrightarrow
\text{functional-equation circle}.
\tag{6.1}
\]

The difference identifies the integer obstruction sharply. In the curve
degree lattice, support can make the packets orthogonal and reduce the
energy to coefficient squares. In the integer logarithmic lattice,
arbitrarily close source points force an overlapping primitive-pair
problem. The missing theorem is cancellation in those overlaps, not
uncertainty about what the carrier measures.

No number-field estimate is inferred from (0.10).

## 7. Scope and novelty firewall

| statement | grade |
|---|---|
| divisor-Möbius generating function (1.3) | **PROVED EXACT** |
| normalized rational function (1.5) | **PROVED EXACT** |
| disjoint energy identity (0.10) | **PROVED EXACT** |
| energy/root-radius equivalence | **PROVED BY RATIONAL PARTIAL FRACTIONS** |
| functional-equation upgrade to the circle | **PROVED** |
| Weil RH for smooth projective curves | **IMPORTED KNOWN THEOREM; NOT REPROVED** |
| integer beta-energy estimate | **NOT PROVED** |
| integer RH or GRH | **NOT PROVED** |

The criterion (0.11) is a new project adapter and mechanism theorem, not
a claim to have discovered curve RH or a new proof of Weil's theorem.
No external novelty or priority is claimed without a dedicated
literature comparison.

The result is for each fixed curve as \(N\to\infty\). It does not claim
uniformity as genus, field size, conductor, or the curve varies.

## 8. Bounded replay

The producer:

- verifies the frozen variational-carrier quartet by full Git blob ID;
- applies the exact integer recurrence (5.2) through degree 24;
- uses two Weil-compatible formal rows and one explicitly synthetic
  off-circle row;
- computes only quadratic roots and finite coefficient sums;
- performs no curve, point, polynomial, field-element, prime, zero,
  random, or quadrature enumeration.

~~~text
python -B research/l-families/atlas/function_field/function_field_mobius_carrier_calibration.py --check
python -O -B research/l-families/atlas/function_field/function_field_mobius_carrier_calibration.py --check
python -B -m unittest tests.test_function_field_mobius_carrier_calibration
python -O -B -m unittest tests.test_function_field_mobius_carrier_calibration
python -m ruff check research/l-families/atlas/function_field/function_field_mobius_carrier_calibration.py tests/test_function_field_mobius_carrier_calibration.py
python -m ruff format --check research/l-families/atlas/function_field/function_field_mobius_carrier_calibration.py tests/test_function_field_mobius_carrier_calibration.py
~~~
