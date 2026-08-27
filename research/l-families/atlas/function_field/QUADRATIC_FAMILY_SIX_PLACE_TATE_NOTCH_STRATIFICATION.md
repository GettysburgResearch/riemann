# The six-place Tate notch has one exact geometric alias stratum

Status: **exact all-extension six-place scalar-Tate notch, exact generic
rank-sixteen recurrence, exact memberwise rank formula, and complete
classification of when the notch deletes genuine centered
primitive-wedge modes; both exceptional ranks are realized by explicit
six-rational-branch curves; a sheaf decomposition, RH, and GRH remain open**

Bounded replay:
[quadratic_family_six_place_tate_notch_stratification.py](quadratic_family_six_place_tate_notch_stratification.py).
Canonical summary:
[quadratic_family_six_place_tate_notch_stratification.json](quadratic_family_six_place_tate_notch_stratification.json).

Frozen source: the six-place connected-saturation packet at commit
`b653f272954bf7e1d93d6e54c1883b4cb00b181c`.  Only its exact raw
six-place row and genus-two coefficient convention are used here.

## 0. Outcome

Fix an odd prime \(p\ge7\) and six distinct points
\(A\subset\mathbf F_p\).  For the source-convention genus-two curve

\[
 C_A:y^2=\prod_{a\in A}(a-z),
\tag{0.1}
\]

write the base Frobenius polynomial as

\[
 P(T)=T^4-tT^3+bT^2-ptT+p^2
 =\prod_{i=1}^4(T-\alpha_i).
\tag{0.2}
\]

At extension degree \(n\), put

\[
 t_n=\sum_i\alpha_i^n,
 \qquad
 b_n=\sum_{i<j}(\alpha_i\alpha_j)^n.
\tag{0.3}
\]

The locked six-place theorem gives the raw correlation

\[
\boxed{
 S_n=(p^{2n}-21)t_n+(p^n-6)b_n-p^{2n}+6p^n-21.}
\tag{0.4}
\]

The six pair products contain two universal copies of \(p\).  Define the
centered cross-pair trace

\[
 w_n=b_n-2p^n=\sum_{j=1}^4\gamma_j^n.
\tag{0.5}
\]

Then (0.4) has the exact provenance-separated form

\[
\boxed{
\begin{aligned}
 S_n={}&(p^2)^n-6p^n-21\\
 &+\sum_{i=1}^4\bigl((p^2\alpha_i)^n-21\alpha_i^n\bigr)\\
 &+\sum_{j=1}^4\bigl((p\gamma_j)^n-6\gamma_j^n\bigr).
\end{aligned}}
\tag{0.6}
\]

Let \(E f_n=f_{n+1}\).  The unique monic minimum-degree filter which
annihilates all three scalar Tate modes is

\[
\boxed{
 \mathcal N_{6,p}(E)=(E-1)(E-p)(E-p^2).}
\tag{0.7}
\]

The filtered tower \(Y_n=\mathcal N_{6,p}(E)S_n\) has exact surviving
support

\[
\boxed{
 \{\alpha_i,p^2\alpha_i:1\le i\le4\}
 \cup
 \{\gamma_j,p\gamma_j:\gamma_j\ne p\},}
\tag{0.8}
\]

with multiplicities combined into nonzero amplitudes.  If

\[
 r_P=\#\{\text{distinct roots of }P\},
 \qquad
 r_Q^*=\#\{\text{distinct }\gamma_j\ne p\},
\tag{0.9}
\]

then the exact memberwise minimal recurrence rank is

\[
\boxed{\operatorname{rank}_{\min}(Y)=2r_P+2r_Q^*.}
\tag{0.10}
\]

In particular the generic rank is sixteen.

The scalar notch collides with genuine cross-pair modes if and only if

\[
\boxed{t^2-4b+8p=0.}
\tag{0.11}
\]

On this stratum, \(t=2u\) is even and

\[
\boxed{P(T)=(T^2-uT+p)^2.}
\tag{0.12}
\]

Thus the alias stratum is exactly the square-Frobenius-polynomial stratum.
The notch necessarily deletes two centered cross-pair copies of \(p\) and
their two \(p^2\)-twists.  The surviving rank is

\[
\boxed{
 \operatorname{rank}_{\min}(Y)=
 \begin{cases}
 8,&u\ne0,\\
 6,&u=0.
 \end{cases}}
\tag{0.13}
\]

This is a sharp spectral-aliasing no-go: a scalar polynomial filter cannot
distinguish two contributions carried by the same recurrence root.

## 1. The centered primitive-pair polynomial

Choose reciprocal-pair notation

\[
 \{\alpha_i\}=
 \{a,p/a,c,p/c\}.
\tag{1.1}
\]

After removing the two within-pair products equal to \(p\), the four roots
in (0.5) are

\[
 ac,\qquad {pa\over c},\qquad {pc\over a},\qquad {p^2\over ac}.
\tag{1.2}
\]

Their monic polynomial is

\[
\boxed{
\begin{aligned}
 Q(T)={}&T^4-(b-2p)T^3
 +(pt^2-2pb+2p^2)T^2\\
 &-p^2(b-2p)T+p^4.
\end{aligned}}
\tag{1.3}
\]

This is a centered cross-pair polynomial.  It is not by itself asserted to
be the characteristic polynomial of a constructed four-dimensional sheaf.
Equivalently,

\[
 w_n=p^n\bigl(\chi_{\omega_2}(U^n)-1\bigr),
\tag{1.4}
\]

so the centering removes the zero-weight scalar from the irreducible
\(\operatorname{USp}(4)\) character as well as the symplectic invariant
already separated from \(\wedge^2H^1\).

The two evaluations

\[
\boxed{
 Q(p)=p^3(t^2-4b+8p),
 \qquad
 Q(-p)=p^3t^2}
\tag{1.5}
\]

are useful diagnostics.  The second identifies a separate trace-zero
collision at \(-p\), but \(-p\) and \(-p^2\) are not roots of the scalar
notch and therefore survive.  Only \(Q(p)=0\) is a notch collision.

## 2. Exact filtered root ledger and recurrence

Write the same symbol for the polynomial

\[
 \mathcal N_{6,p}(T)=(T-1)(T-p)(T-p^2).
\tag{2.1}
\]

Applying it to (0.6) gives

\[
\boxed{
\begin{aligned}
 Y_n={}&\sum_i\Bigl[
 \mathcal N_{6,p}(p^2\alpha_i)(p^2\alpha_i)^n
 -21\mathcal N_{6,p}(\alpha_i)\alpha_i^n\Bigr]\\
 &+\sum_j\Bigl[
 \mathcal N_{6,p}(p\gamma_j)(p\gamma_j)^n
 -6\mathcal N_{6,p}(\gamma_j)\gamma_j^n\Bigr].
\end{aligned}}
\tag{2.2}
\]

Every \(\alpha_i\) has modulus \(p^{1/2}\), every \(\gamma_j\) has modulus
\(p\), and their displayed twists have moduli \(p^{5/2}\) and \(p^2\).
Hence different weight rows cannot collide.  The \(H^1\) rows never meet a
notch root.  A cross-pair row meets the notch exactly when
\(\gamma_j=p\), in which case its twist is \(p^2\) and both are deleted.

An all-member annihilator, not always minimal, is

\[
\boxed{
 \mathcal A_{p,t,b}(T)=
 P(T)\,p^8P(T/p^2)\,Q(T)\,p^4Q(T/p).}
\tag{2.3}
\]

It has degree sixteen.  Off the discriminant and collision loci—equivalently
when \(P,Q\) are squarefree and \(Q(p)\ne0\)—all sixteen roots in (0.8)
are distinct with nonzero amplitudes, so (2.3) is the minimal recurrence.

For every member, repeated roots merely add their multiplicity to the
amplitude.  Removing \(p\) from the distinct root support of \(Q\), then
taking one untwisted and one twisted copy of every remaining root, proves
(0.10).

## 3. Complete notch-collision classification

By (1.5), collision is equivalent to (0.11).  Since \(b,p,t\) are
integers and \(p\) is odd, (0.11) forces \(t\) even.  Put \(u=t/2\).  Then

\[
 b=u^2+2p,
\tag{3.1}
\]

and direct coefficient comparison proves (0.12).  Conversely every square
polynomial in (0.12) satisfies (0.11).  There is no second hidden collision
stratum, because the Weil moduli exclude every other meeting with
\(\{1,p,p^2\}\).

On the square stratum,

\[
\boxed{
 Q(T)=(T-p)^2
 \bigl(T^2-(u^2-2p)T+p^2\bigr).}
\tag{3.2}
\]

The notch removes the double \(p\) root and its double \(p^2\) twist.
The quadratic factor has the roots \(\lambda^2,\mu^2\), where
\(\lambda,\mu\) are the distinct roots of \(T^2-uT+p\).

If \(u\ne0\), then \(\lambda^2\ne\mu^2\).  Thus \(r_P=2\) and
\(r_Q^*=2\), proving rank eight.  If \(u=0\), then

\[
 P(T)=(T^2+p)^2,
 \qquad
 Q(T)=(T-p)^2(T+p)^2.
\tag{3.3}
\]

Now \(r_P=2\) and \(r_Q^*=1\), proving rank six.

The equality (0.12) is a spectral square statement.  Identifying it with a
Jacobian isogeny \(E^2\) would use additional Honda--Tate/Tate input, and is
not claimed here.  The exceptional spectral rows themselves do occur in
the source family.  Two exact controls are

\[
\begin{array}{c|c|c|c|c|c}
p&A&t&b&t_2&\operatorname{rank}_{\min}(Y)\\ \hline
11&\{0,1,2,3,5,9\}&0&22&-44&6\\
13&\{0,1,2,3,5,11\}&-4&30&-44&8.
\end{array}
\tag{3.4}
\]

For each row the replay counts the curve over \(\mathbf F_p\) and
\(\mathbf F_{p^2}\), derives \(t\), \(t_2\), and
\(b=(t^2-t_2)/2\), and then checks the square factorization.  Thus the
scalar-notch loss is not merely conditional on an abstract Weil
polynomial: both exceptional ranks are realized by explicit members with
six distinct rational branch points.

## 4. The sharp no-go

The three scalar roots \(1,p,p^2\) have nonzero amplitudes in (0.6).
Therefore every configuration-independent polynomial filter which removes
them termwise is divisible by

\[
 (T-1)(T-p)(T-p^2).
\tag{4.1}
\]

The cubic notch is consequently the unique monic minimum-degree scalar
filter.  On (0.11), however, centered geometric cross-pair modes occupy the
same roots \(p,p^2\).  Any scalar filter removing the nuisance must remove
those modes too.  Coefficients, positivity, more extension rows, or a
different polynomial degree cannot recover provenance after the roots have
aliased.

Avoiding this loss requires extra structure not present in the scalar tower,
for example a representation-valued projector which separates the scalar
and cross-pair channels before taking traces.  No such sheaf or projector is
built here.

## 5. Scope and interpretation

The tower fixes one six-place configuration over \(\mathbf F_p\) and extends
scalars to \(\mathbf F_{p^n}\).  It does not choose unrelated configurations
at successive \(n\).  The exact generic rank is sixteen, but memberwise rank
must use (0.10); quoting sixteen on a square, trace-zero, repeated-root, CM,
or decomposable stratum without checking the support would be false.

The term "Tate" describes recurrence roots \(p^j\).  The packet constructs
no cohomology object realizing the decomposition.  The raw correlation is a
family sum, not an individual \(L\)-function.  No family cancellation,
principal-member amplifier, zero-free region, number-field transfer, RH,
or GRH result follows.

## 6. Claim ledger

| statement | grade |
|---|---|
| six-place tower identity (0.4) | **IMPORTED EXACT** |
| centered cross-pair polynomial (1.3) | **PROVED EXACT** |
| unique minimal cubic scalar notch (0.7) | **PROVED EXACT** |
| filtered root ledger (0.8), memberwise rank (0.10) | **PROVED EXACT** |
| generic rank-sixteen recurrence (2.3) | **PROVED EXACT OFF THE STATED LOCI** |
| complete notch-collision equation (0.11) | **PROVED EXACT** |
| square-stratum ranks eight and six (0.13) | **PROVED EXACT** |
| provenance-preserving scalar notch on every member | **REFUTED BY EXPLICIT FAMILY MEMBERS** |
| realization of ranks eight and six in the six-rational-branch family | **PROVED BY TWO EXACT BOUNDED CONTROLS** |
| sheaf realization, RH, or GRH | **NOT PROVED** |

## 7. Bounded replay

The replay uses exact integer polynomial arithmetic through degree sixteen,
two formal generic split-Weil controls, and the two realized square-stratum
controls in (3.4).  It verifies (1.3), (1.5), (2.3), the generic rank
counts, the exact factorizations (3.2)--(3.3), and recurrence rows at three
starting indices.  Its largest polynomial degree is sixteen and its largest
raw extension index is twenty-two; the corresponding Newton power-sum
exponent is at most forty-four.  It constructs no matrix.

The only finite-field work is the exact point count for the two displayed
curves over \(\mathbf F_{11}\), \(\mathbf F_{13}\),
\(\mathbf F_{11^2}\), and \(\mathbf F_{13^2}\): 290 quadratic-extension
elements plus 24 base-field elements, with largest field size 169. There is no
polynomial-family, branch-set, prime, or zero enumeration and no
floating-point arithmetic.

~~~text
python -B research/l-families/atlas/function_field/quadratic_family_six_place_tate_notch_stratification.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_six_place_tate_notch_stratification.py --check
python -B -m unittest tests.test_quadratic_family_six_place_tate_notch_stratification
python -B -O -m unittest tests.test_quadratic_family_six_place_tate_notch_stratification
python -B -m ruff check research/l-families/atlas/function_field/quadratic_family_six_place_tate_notch_stratification.py tests/test_quadratic_family_six_place_tate_notch_stratification.py
python -B -m ruff format --check research/l-families/atlas/function_field/quadratic_family_six_place_tate_notch_stratification.py tests/test_quadratic_family_six_place_tate_notch_stratification.py
~~~
