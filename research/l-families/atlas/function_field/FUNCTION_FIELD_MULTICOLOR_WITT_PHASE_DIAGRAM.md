# Multicolor Frobenius wavelets have a Witt continuation color-square phase diagram

Status: **exact \(c\)-color Euler/Witt factorization, uniform continuation
to radius \(1/c\), and exponential critical-normalized decay when
\(q>c^2\); no claim at or below the color-square boundary, arithmetic
family or sheaf realization, number-field transfer, RH, or GRH result**

Bounded replay:
[function_field_multicolor_witt_phase_diagram.py](function_field_multicolor_witt_phase_diagram.py).
Canonical summary:
[function_field_multicolor_witt_phase_diagram.json](function_field_multicolor_witt_phase_diagram.json).

Frozen source: the binary divisor-wavelet Witt theorem at commit
`02555b216077a3cd3a1309eb530cd29b26c7f6a3`. The producer pins its
Markdown, replay, and canonical JSON blobs.

## 0. Outcome

Let \(q\) be a prime power and \(c\ge2\). At each irreducible polynomial,
allow one absent state and \(c\) mutually exclusive selected colors.
Attach a unit phase \(z_i\) to color \(i\). The complete squarefree color
series is

\[
\boxed{
 F_{q,c}(u;\mathbf z)
 =\prod_P\left(
  1-\sum_{i=1}^c(uz_i)^{\deg P}
 \right),\qquad |z_i|=1.}
\tag{0.1}
\]

For a nonzero content vector

\[
 \mathbf a=(a_1,\ldots,a_c)\in\mathbf Z_{\ge0}^c,
 \qquad |\mathbf a|=\sum_i a_i,
\]

define

\[
\boxed{
 M(\mathbf a)
 ={1\over|\mathbf a|}
 \sum_{d\mid\gcd(a_1,\ldots,a_c)}
 \mu(d)
 {(|\mathbf a|/d)!\over\prod_i(a_i/d)!}.}
\tag{0.2}
\]

This is the nonnegative integer counting primitive \(c\)-letter necklaces
with content \(\mathbf a\). The exact multicolor Witt factorization is

\[
\boxed{
 F_{q,c}(u;\mathbf z)
 =\prod_{\mathbf a\ne0}
 \left(
  1-q\,u^{|\mathbf a|}
  \prod_{i=1}^c z_i^{a_i}
 \right)^{M(\mathbf a)}.}
\tag{0.3}
\]

At total length \(k\), the sum of the exponents is

\[
\boxed{
 L_k(c)
 =\sum_{|\mathbf a|=k}M(\mathbf a)
 ={1\over k}\sum_{d\mid k}\mu(d)c^{k/d}
 \le {c^k\over k}.}
\tag{0.4}
\]

Consequently (0.3) converges normally, uniformly in all unit phases, on
every closed disk

\[
 |u|\le r<\frac1c.
\tag{0.5}
\]

It analytically continues the native Euler series to \(|u|<1/c\). For
every \(0<r<1/c\) and every \(n\ge0\), Cauchy's estimate gives

\[
\boxed{
 \sup_{|z_1|=\cdots=|z_c|=1}
 |[u^n]F_{q,c}(u;\mathbf z)|
 \le C_{q,c,r}r^{-n}.}
\tag{0.6}
\]

After critical normalization, for the same \(r\) and \(n\),

\[
 q^{-n/2}
 \sup_{|z_1|=\cdots=|z_c|=1}|[u^n]F_{q,c}(u;\mathbf z)|
 \le C_{q,c,r}(r\sqrt q)^{-n}.
\tag{0.7}
\]

There exists a radius satisfying

\[
 q^{-1/2}<r<1/c
\tag{0.8}
\]

exactly when

\[
\boxed{q>c^2.}
\tag{0.9}
\]

Thus the complete \(c\)-color shell decays exponentially after
critical normalization throughout the color-square regime \(q>c^2\).
This is the exact phase diagram for when the guaranteed Witt disk supports
this critical Cauchy argument:

| colors \(c\) | Witt radius | proven critical-decay fields |
|---:|---:|---:|
| \(2\) | \(1/2\) | \(q\ge5\) |
| \(3\) | \(1/3\) | \(q\ge11\) |
| \(4\) | \(1/4\) | \(q\ge17\) |
| general \(c\) | \(1/c\) | prime powers \(q>c^2\) |

No decay or failure is inferred when \(q\le c^2\). There the two radii do
not overlap, so this continuation method has no exponential budget.

## 1. Exact color adapter

For one irreducible \(P\), a squarefree colored object has \(c+1\) states:

- absent, contributing \(1\);
- present in color \(i\), contributing
  \(-(uz_i)^{\deg P}\).

The minus sign is the squarefree Möbius sign. Summing those states proves
the local factor in (0.1). The construction is formal and complete: no
positive norm or colorwise triangle inequality is taken.

When \(c=2\), choose

\[
 z_1=z,\qquad z_2=z^{-1}.
\]

Then (0.1) is exactly the binary divisor-orientation wavelet of the
predecessor. The present theorem is not a different normalization of that
case; it is its full color-rank extension.

## 2. Multivariate Witt identity

For formal variables \(X_1,\ldots,X_c\),

\[
\boxed{
 1-\sum_{i=1}^cX_i
 =\prod_{\mathbf a\ne0}
  (1-\mathbf X^{\mathbf a})^{M(\mathbf a)},}
\tag{2.1}
\]

where

\[
 \mathbf X^{\mathbf a}=\prod_iX_i^{a_i}.
\]

Taking negative logarithms, the left side becomes

\[
 \sum_{k\ge1}{(X_1+\cdots+X_c)^k\over k}.
\tag{2.2}
\]

The coefficient of a fixed monomial, followed by Möbius inversion on the
gcd of its content, gives exactly (0.2). Summing (0.2) over every content
of size \(k\) gives (0.4).

Apply (2.1) with

\[
 X_i=(uz_i)^{\deg P}
\]

inside each irreducible local factor, then reorder as a formal series:

\[
\begin{aligned}
 F_{q,c}
 &=\prod_{\mathbf a\ne0}
   \left[
    \prod_P
    \left(
     1-
     \left(
      u^{|\mathbf a|}
      \prod_i z_i^{a_i}
     \right)^{\deg P}
    \right)
   \right]^{M(\mathbf a)}.
\end{aligned}
\tag{2.3}
\]

The polynomial zeta identity

\[
 \prod_P(1-v^{\deg P})=1-qv
\tag{2.4}
\]

turns every bracket into the corresponding factor of (0.3).

## 3. Uniform analytic continuation

Group (0.3) by \(k=|\mathbf a|\). For fixed \(r<1/c\) and all sufficiently
large \(k\), \(qr^k\le1/2\). Uniformly for \(|z_i|=1\),

\[
\begin{aligned}
 &\sum_{|\mathbf a|=k}M(\mathbf a)
 \left|
 \log\left(
  1-q\,u^k\prod_i z_i^{a_i}
 \right)
 \right|\\
 &\qquad\ll_q L_k(c)r^k
 \le{(cr)^k\over k}.
\end{aligned}
\tag{3.1}
\]

The last series converges. Finitely many short factors are polynomials, so
their zeros are not singularities. This proves normal convergence on
\(|u|\le r<1/c\), uniformly on the phase torus. Cauchy's formula proves
(0.6), and (0.8)--(0.9) prove the critical phase transition.

The radius \(1/c\) is the guaranteed normal-convergence radius supplied by
the total primitive-word count. No natural-boundary or optimal analytic
continuation claim is needed.

## 4. Detector-design interpretation

The theorem provides a compact-group/family warning and an opportunity.

Adding coherent colors increases the primitive-word entropy from \(2^k\)
to \(c^k\). The polynomial zeta identity still converts every primitive
word into an exact finite factor, but the guaranteed uniform continuation
radius contracts from \(1/2\) to \(1/c\). By this argument, critical
square-root normalization can absorb that entropy exactly when
\(\sqrt q>c\).

This suggests a design constraint for colored family amplifiers:

\[
\boxed{\text{effective coherent color count}<\sqrt q.}
\tag{4.1}
\]

It is a theorem for the complete polynomial color model, not a theorem for
the native FFPS owner/Boolean/Artin--Schreier source. A geometric adapter
must still show that its local states are mutually exclusive and assemble
as (0.1). Tensor colors, overlapping incidences, hard masks, or nontrivial
deck monodromy can change the local polynomial.

No number-field estimate follows. The rational collapse (2.4) is special
to \(\mathbf F_q[T]\).

## 5. Claim ledger

| statement | grade |
|---|---|
| complete \(c\)-color Euler product (0.1) | **PROVED EXACT** |
| content necklace formula (0.2) | **PROVED BY MÖBIUS INVERSION** |
| multicolor Witt product (0.3) | **PROVED EXACT AS A FORMAL SERIES** |
| total Lyndon count (0.4) | **PROVED EXACT** |
| uniform continuation to \(|u|<1/c\) | **PROVED BY NORMAL CONVERGENCE** |
| optimality of \(1/c\) or a natural boundary there | **NOT CLAIMED** |
| coefficient estimate (0.6) | **PROVED BY CAUCHY** |
| critical exponential decay for \(q>c^2\) | **PROVED** |
| behavior for \(q\le c^2\) | **NOT CLAIMED** |
| native arithmetic family or sheaf realization | **NOT INCLUDED** |
| number-field transfer | **NOT INFERRED** |
| RH or GRH | **NOT PROVED** |

No external novelty claim is made without a dedicated literature
comparison.

## 6. Bounded replay

The producer expands the local-color Euler product and the content-refined
Witt product as exact multivariate integer dictionaries:

- \(c=2,q=5\), through total degree seven;
- \(c=3,q=11\), through total degree five.

Both complete coefficient dictionaries agree. It also checks every
content count and its sum \(L_k(c)\), plus controls at and above the
color-square boundary. The replay accepts formal integer \(q\ge2\); the
field-theoretic statement requires \(q\) to be a prime power. It enumerates
no field element, finite-field polynomial, irreducible, curve, point,
floating-point value, or zeta zero.

~~~text
python -B research/l-families/atlas/function_field/function_field_multicolor_witt_phase_diagram.py --check
python -B -O research/l-families/atlas/function_field/function_field_multicolor_witt_phase_diagram.py --check
python -B -m unittest tests.test_function_field_multicolor_witt_phase_diagram
python -B -O -m unittest tests.test_function_field_multicolor_witt_phase_diagram
python -B -m ruff check research/l-families/atlas/function_field/function_field_multicolor_witt_phase_diagram.py tests/test_function_field_multicolor_witt_phase_diagram.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_multicolor_witt_phase_diagram.py tests/test_function_field_multicolor_witt_phase_diagram.py
~~~
