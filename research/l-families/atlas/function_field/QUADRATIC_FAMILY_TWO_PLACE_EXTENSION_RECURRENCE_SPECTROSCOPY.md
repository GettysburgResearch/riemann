# Two-place cumulant defects have exact signed-Tate extension spectra

Status: **exact all-extension denominator-cleared recurrence theorem through
cumulant order six, exact minimal recurrence ranks, and a falsification of
the proposed rank-two residual beyond order three; no sheaf realization,
new family estimate, zero theorem, RH, or GRH result**

Bounded replay:
[quadratic_family_two_place_extension_recurrence_spectroscopy.py](quadratic_family_two_place_extension_recurrence_spectroscopy.py).
Canonical summary:
[quadratic_family_two_place_extension_recurrence_spectroscopy.json](quadratic_family_two_place_extension_recurrence_spectroscopy.json).

Frozen source: commit
`a91f985329f04e4c3dee9662589980ff7ab8ccf5`, theorem blob
`bf255c1978b7de4a7f6d697b1c40878c50b7a449`, and producer blob
`bd359c41670bbec94fbe79dea096a3cb89bf647d`.

## 0. Outcome

Fix an odd prime \(p\), distinct \(a,b\in\mathbf F_p\), and put

\[
 \alpha=\chi_p(b-a),\qquad \varepsilon=\chi_p(-1).
\tag{0.1}
\]

Over \(\mathbf F_{p^n}\), the lifted squareclasses are

\[
 \chi_{p^n}(b-a)=\alpha^n,
 \qquad
 \chi_{p^n}(-1)=\varepsilon^n.
\tag{0.2}
\]

Let \(\Delta_m(p^n)\), \(2\le m\le6\), be the exact two-place mixed
cumulant defects of the frozen degree-five squarefree family.  Write

\[
 A(q)=q^4(q-1),
 \qquad
 R_m(n)=A(p^n)^{\lfloor m/2\rfloor}\Delta_m(p^n).
\tag{0.3}
\]

The family denominator is load-bearing: the unscaled rational sequences are
not asserted to satisfy finite constant-coefficient recurrences.  After the
natural cumulant denominator is cleared, every residual is an exact finite
sum of signed Tate exponentials.

There are integer polynomials \(P_m,Q_6\) such that, with \(q=p^n\),

\[
\boxed{
\begin{aligned}
 R_2(n)&=P_2(q),\\
 R_3(n)&=\alpha^n(1+\varepsilon^n)P_3(q),\\
 R_4(n)&=P_4(q),\\
 R_5(n)&=\alpha^n(1+\varepsilon^n)P_5(q),\\
 R_6(n)&=P_6(q)+\varepsilon^nQ_6(q).
\end{aligned}}
\tag{0.4}
\]

Their nonzero coefficient vectors, listed from degree zero upward, are

\[
\begin{array}{c|c|c}
 &\text{degrees}&\text{coefficients}\\ \hline
P_2&0,1&(-6,4)\\
P_3&0,1&(-9,6)\\
P_4&0,\ldots,6&(-186,360,-336,312,-276,146,-32)\\
P_5&0,\ldots,6&(-720,1200,-840,600,-555,345,-90)\\
P_6&0,\ldots,11&(-15300,45720,-68040,82200,-90690,81870,\\
&&\qquad -60960,41760,-26196,12766,-3914,544)\\
Q_6&4,\ldots,7&(1620,-3780,2880,-720).
\end{array}
\tag{0.5}
\]

Thus the exact spectral roots are drawn only from

\[
 \{p^j,-p^j:j\ge0\}.
\tag{0.6}
\]

The minimal constant-coefficient recurrence ranks are

\[
\boxed{
\begin{array}{c|cc}
m&\varepsilon=1&\varepsilon=-1\\ \hline
2&2&2\\
3&2&4\\
4&7&7\\
5&7&14\\
6&12&16.
\end{array}}
\tag{0.7}
\]

The value of \(\alpha\) changes signs of roots but not their number.

This settles the rank-two recurrence moonshot for this observable.  It is
true for covariance \(\Delta_2\), and for \(\Delta_3\) when
\(p\equiv1\pmod4\), but it already fails at \(\Delta_4\), whose minimal
rank is seven.  The failure is informative rather than featureless: no
non-Tate recurrence root appears.  The complete residual through order six
is built from boundary/combinatorial signed-Tate channels.

## 1. Frozen two-place law

For one field \(\mathbf F_q\), the frozen packet writes

\[
\begin{aligned}
 V&=q^5-2q^4+2q^3-2q^2+2q-1,\\
 W&=q^5-3q^4+5q^3-7q^2+9q-6,\\
 C&=2q-3,\\
 v&=V/A,\qquad w=W/A,\qquad c=C/A,\\
 u&=s(1+e)c,
\end{aligned}
\tag{1.1}
\]

where \(s=\chi_q(b-a)\), \(e=\chi_q(-1)\), and \(A=q^4(q-1)\).  Its
exact cumulant defects are

\[
\begin{aligned}
 \Delta_2={}&2c,\\
 \Delta_3={}&3u,\\
 \Delta_4={}&8c+6w-6v^2-24vc-12c^2,\\
 \Delta_5={}&15u(1-4(v+c)),\\
 \Delta_6={}&32c+30w-30(v+c)(2v+8c+6w)-90u^2\\
             &\quad+240(v+c)^3+30v^2-60v^3.
\end{aligned}
\tag{1.2}
\]

Nothing in this packet changes that family adapter or recomputes a finite
field census.

## 2. Character lift along one base-prime tower

For \(x\in\mathbf F_p^*\),

\[
 \chi_{p^n}(x)
 =x^{(p^n-1)/2}
 =\left(x^{(p-1)/2}\right)^{1+p+\cdots+p^{n-1}}
 =\chi_p(x)^n,
\tag{2.1}
\]

because \(p\) is odd and \(1+p+\cdots+p^{n-1}\equiv n\pmod2\).  This
proves (0.2).  Hence

\[
 s_n=\alpha^n,
 \qquad
 e_n=\varepsilon^n,
 \qquad
 s_n(1+e_n)=\alpha^n+(\alpha\varepsilon)^n.
\tag{2.2}
\]

Also

\[
 s_n^2(1+e_n)^2=2(1+\varepsilon^n).
\tag{2.3}
\]

The last identity explains why the even sixth cumulant remembers
\(p\bmod4\) but not the oriented squareclass \(\alpha\).

## 3. Exact denominator clearing

Multiply (1.2) by the powers of \(A\) in (0.3).  Direct expansion gives

\[
\begin{aligned}
P_2={}&2C,\\
P_3={}&3C,\\
P_4={}&A(8C+6W)-6V^2-24VC-12C^2,\\
P_5={}&15C\bigl(A-4(V+C)\bigr),\\
P_6={}&A^2(32C+30W)-30A(V+C)(2V+8C+6W)\\
&\quad-180AC^2+240(V+C)^3+30AV^2-60V^3,\\
Q_6={}&-180AC^2.
\end{aligned}
\tag{3.1}
\]

Using (2.2)--(2.3) proves (0.4).  Expanding (3.1) proves the coefficient
table (0.5).  The severe degree cancellations in \(P_4\), from naive degree
ten down to degree six, and in \(P_6\), from naive degree fifteen down to
degree eleven, are the algebraic form of the suppressed leading scales in
the frozen packet.  The polynomial \(P_5\) remains degree six.  None of
these cancellations collapses the recurrence to rank two.

## 4. Minimal recurrence theorem

If

\[
 S_n=\sum_{\rho\in\mathcal R}a_\rho\rho^n
\tag{4.1}
\]

with distinct nonzero \(\rho\) and nonzero \(a_\rho\), then the minimal
constant-coefficient annihilator is

\[
 \prod_{\rho\in\mathcal R}(T-\rho).
\tag{4.2}
\]

Indeed, the Vandermonde matrix on the distinct roots is nonsingular, so no
shorter linear recurrence can annihilate the sequence.

For \(P_m(p^n)\), every nonzero degree \(j\) contributes the root \(p^j\).
For an odd defect, (2.2) replaces it by

\[
 \alpha p^j,\qquad \alpha\varepsilon p^j.
\tag{4.3}
\]

When \(\varepsilon=1\) these coincide and their amplitudes add; when
\(\varepsilon=-1\) they are distinct.  For \(R_6\), the base roots are
\(p^j\), \(0\le j\le11\), while the orientation roots are
\(\varepsilon p^j\), \(4\le j\le7\).  If \(\varepsilon=1\), the four
overlapping coefficients remain nonzero after addition.  If
\(\varepsilon=-1\), four distinct negative roots are added.  This proves
(0.7) and minimality.

The corresponding characteristic polynomials are therefore explicit.  For
example,

\[
 \mathcal P_4(T)=\prod_{j=0}^6(T-p^j),
\tag{4.4}
\]

and

\[
 \mathcal P_6(T)=
 \begin{cases}
 \prod_{j=0}^{11}(T-p^j),&\varepsilon=1,\\
 \displaystyle
 \prod_{j=0}^{11}(T-p^j)
 \prod_{j=4}^{7}(T+p^j),&\varepsilon=-1.
 \end{cases}
\tag{4.5}
\]

## 5. What the spectroscopy does and does not say

This is a guarded cohomological inference, not a cohomology computation.
The exact tower sequence has only signed powers of \(p\), so it has a
Tate-shaped spectrum.  No sheaf, stack, weight filtration, or Tate class is
constructed here.  The safe conclusion is:

> after natural denominator clearing, the exact two-place cumulant residual
> has no non-Tate recurrence eigenvalue through order six.

The result supplies a useful null calibration.  A nuisance-quotiented
detector whose cleared extension tower exhibits an eigenvalue not of the
form \(\pm p^j\) would contain arithmetic information absent from this raw
two-place evaluation packet.  Conversely, fitting two or three extension
rows to a rank-two recurrence would be misleading: \(\Delta_4\) requires
seven exact modes even though all of them are elementary.

The denominator-cleared sequence is the one governed by (0.4).  Expanding
\(1/A(p^n)^k\) as a geometric series would create an infinite collection of
decaying powers, so no finite-recurrence claim is made for raw
\(\Delta_m(p^n)\).

Nothing here supplies a family estimate, principal-member amplifier,
individualization theorem, zero-free region, RH implication, or GRH
implication.

## 6. Claim ledger

| statement | grade |
|---|---|
| base-field character lift (0.2) | **PROVED EXACT** |
| cleared polynomial identities (0.4)--(0.5) | **PROVED BY EXACT EXPANSION** |
| signed-Tate root classification (0.6) | **PROVED EXACT** |
| minimal ranks (0.7) | **PROVED BY VANDERMONDE MINIMALITY** |
| rank-two residual beyond order three | **REFUTED BY THE EXACT \(m=4\) RANK-SEVEN THEOREM** |
| Tate-class or sheaf realization | **NOT CLAIMED** |
| raw unscaled finite recurrence | **NOT CLAIMED** |
| RH or GRH | **NOT PROVED** |

## 7. Bounded replay

The replay uses exact symbolic \(q\)-polynomial arithmetic through degree
fifteen and recurrence polynomials through degree sixteen, the primes
\(p=3,5\), both values of \(\alpha\), and the actual values
\(\varepsilon=(-1\mid p)\).  The producer checks extension degrees through
thirty-four; tests reach thirty-six and also exercise both formal signs
algebraically.  It verifies the frozen rational cumulants against every
cleared polynomial, constructs every minimal root ledger, and checks each
recurrence well beyond twice its order.
It performs no finite-field enumeration, curve count, point count, prime
search, floating-point fit, zero computation, or large matrix calculation.

~~~text
python -B research/l-families/atlas/function_field/quadratic_family_two_place_extension_recurrence_spectroscopy.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_two_place_extension_recurrence_spectroscopy.py --check
python -B -m unittest tests.test_quadratic_family_two_place_extension_recurrence_spectroscopy
python -B -O -m unittest tests.test_quadratic_family_two_place_extension_recurrence_spectroscopy
python -B -m ruff check research/l-families/atlas/function_field/quadratic_family_two_place_extension_recurrence_spectroscopy.py tests/test_quadratic_family_two_place_extension_recurrence_spectroscopy.py
python -B -m ruff format --check research/l-families/atlas/function_field/quadratic_family_two_place_extension_recurrence_spectroscopy.py tests/test_quadratic_family_two_place_extension_recurrence_spectroscopy.py
~~~
