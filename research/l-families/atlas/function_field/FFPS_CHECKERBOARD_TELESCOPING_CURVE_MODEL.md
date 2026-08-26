# A telescoping checkerboard sheaf model on the projective line

Status: **exact full-rank quadratic-torsor construction and imported
curve-cohomology bound; not an FFPS source realization or CYSEL theorem**

Exact replay:
[`ffps_checkerboard_telescoping_curve_model.py`](ffps_checkerboard_telescoping_curve_model.py)

## 0. Outcome

There is a genuine one-dimensional function-field model in which the ambient
quadratic torsor rank grows exponentially, while the global checkerboard
character compresses to two endpoint places.

Fix an odd prime power \(q\).  Choose distinct monic irreducibles

\[
 P_0,P_1,\ldots,P_d\in\mathbf F_q[T]
\]

of one common degree \(e\), and put

\[
 f_i={P_{i-1}\over P_i}\qquad(1\le i\le d).
\tag{0.1}
\]

The squareclasses of the \(f_i\) are geometrically independent.  Hence the
product of the quadratic Kummer torsors

\[
 z_i^2=f_i
\]

has geometric deck group \(C_2^d\) on the complement of all \(P_i\).
Nevertheless the top checkerboard character telescopes:

\[
 \boxed{
 \bigotimes_{i=1}^d\mathcal L_\kappa(f_i)
 \simeq
 \mathcal L_\kappa\!\left({P_0\over P_d}\right).}
\tag{0.2}
\]

The selected object is nonconstant, has rank one, and is ramified only at
the \(2e\) geometric endpoint roots after its maximal lisse extension.  Its
compactly supported cohomology on that minimal open is

\[
 \boxed{
 \dim H_c^1=2e-2,\qquad H_c^0=H_c^2=0.}
\tag{0.3}
\]

Consequently, for every \(m\ge1\),

\[
 \boxed{
 \left|
 \sum_{x\in U_{\min}(\mathbf F_{q^m})}
 \kappa_m\!\left({P_0(x)\over P_d(x)}\right)
 \right|
 \le (2e-2)q^{m/2}.}
\tag{0.4}
\]

Here `kappa_m` is the quadratic character of \(\mathbf F_{q^m}^\times\).
If \(e=1\), the right side is zero and the selected complete sum vanishes
exactly for every \(m\).

There is a load-bearing catch.  The full product torsor initially lives on

\[
 U_{\rm all}
 =\mathbf P^1\setminus\bigcup_{i=0}^d V(P_i).
\]

On this common open, the same top line has

\[
 \boxed{\dim H_c^1(U_{\rm all})=(d+1)e-2.}
\tag{0.5}
\]

The \(d-1\) middle places are unramified for the telescoped line but remain
holes in the common source base.  Filling them lowers the Betti cost by the
exact removable-puncture tax

\[
 \boxed{(d-1)e.}
\tag{0.6}
\]

Thus this model identifies a new exact gate:

> Quotient compression becomes geometrically effective only if the selected
> line can be extended across every cancellation puncture without changing
> the native source sum.

At fixed \(q\), take the least \(e=e_q(d)\) for which there are at least
\(d+1\) degree-\(e\) primes.  The exact prime-polynomial formula gives

\[
 e_q(d)=\log_q d+O_q(\log\log(d+2)).
\tag{0.7}
\]

The maximal-extension cost is therefore \(O_q(\log d)\), while the
common-open cost is \(O_q(d\log d)\).  This is a real sheaf-theoretic
separation, not yet a legal FFPS simplification.

## 1. Dependencies and imported theorems

| source | exact lock | role |
|---|---|---|
| `FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md` | commit `a33cf6e6d`, blob `8fb67e8445a40b836703e92cdacc55e680dac500` | one-line top checkerboard projector |
| `FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md` | commit `464c3705f`, blob `ab16e6c0894e51303119692e67b2f2bf59ba73e4` | torsor/Frobenius convention and additive-functor firewall |

The cohomology calculation imports three standard results:

1. Grothendieck--Ogg--Shafarevich for a lisse sheaf on a curve;
2. the Grothendieck trace formula;
3. Deligne's weight bound for compactly supported cohomology of a
   pointwise-pure weight-zero sheaf.

Primary proof sources are Deligne's
[`Weil II`](https://eudml.org/doc/103970) and Katz's
[`Gauss Sums, Kloosterman Sums, and Monodromy Groups`](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf),
especially Katz's chapters on breaks and curve cohomology.  These theorems
are imported, not reproved by the finite replay.

## 2. Full geometric \(C_2^d\)-monodromy

Work first in \(\overline{\mathbf F}_q(T)^\times/
\overline{\mathbf F}_q(T)^{\times2}\).  Suppose

\[
 \prod_{i=1}^d f_i^{\epsilon_i}
\]

is a square, with \(\epsilon_i\in\mathbf F_2\).  At a geometric root of
\(P_0\), its valuation parity is \(\epsilon_1\), so
\(\epsilon_1=0\).  At a root of \(P_1\), the parity is
\(\epsilon_1+\epsilon_2\), hence \(\epsilon_2=0\).  Continuing along the
path forces every \(\epsilon_i=0\).

Thus the \(d\) squareclasses are geometrically independent.  The compositum
has degree \(2^d\) and deck group \(C_2^d\).  This rules out a cheap
explanation in which the ambient torsor had secretly collapsed before the
top character was taken.

Multiplying (0.1) cancels every middle polynomial and proves

\[
 \prod_{i=1}^d f_i={P_0\over P_d},
\]

which gives (0.2).  The endpoint ratio is not a geometric square: it has odd
valuation at each root of \(P_0\) and \(P_d\).  Therefore the top selected
line has no geometric invariant vector.

## 3. Branch-parity criterion

More generally, for rational functions \(g_1,\ldots,g_d\), put
\(G=\prod_i g_i\).  On \(\mathbf P^1_{\overline{\mathbf F}_q}\), define

\[
 B(G)=\{x:v_x(G)\equiv1\pmod2\},\qquad b(G)=|B(G)|.
\tag{3.1}
\]

Because constants are squares over the algebraic closure and
\(\operatorname{Pic}^0(\mathbf P^1)=0\),

\[
 \boxed{
 \mathcal L_\kappa(G)\text{ is geometrically constant}
 \iff b(G)=0.}
\tag{3.2}
\]

When \(b(G)>0\), it is a geometrically nontrivial, tame, rank-one sheaf on
\(U=\mathbf P^1\setminus B(G)\).  Divisor degree zero makes \(b(G)\) even.
Grothendieck--Ogg--Shafarevich gives

\[
 \chi_c(U,\mathcal L_\kappa(G))=2-b(G).
\]

Compact support kills \(H_c^0\), and geometric nontriviality kills \(H_c^2\)
by duality.  Hence

\[
 \boxed{\dim H_c^1=b(G)-2.}
\tag{3.3}
\]

The trace formula and the weight bound prove

\[
 \left|\sum_{x\in U(\mathbf F_{q^m})}
 \operatorname{Tr}(\operatorname{Frob}_x\mid\mathcal L_\kappa(G))\right|
 \le (b(G)-2)q^{m/2}.
\tag{3.4}
\]

This is a complete fixed-sheaf estimate, uniform in the extension degree
\(m\).  It is not uniform in a changing FFPS conductor/source until an exact
adapter bounds \(b(G)\) and every removed stratum.

## 4. The removable-puncture tax

For the path construction, let

\[
 \Sigma_{\rm all}=\bigcup_{i=0}^dV(P_i),\qquad
 \Sigma_{\min}=V(P_0)\cup V(P_d).
\]

Over the algebraic closure,

\[
 |\Sigma_{\rm all}|=(d+1)e,\qquad |\Sigma_{\min}|=2e.
\]

The top line is lisse on both corresponding opens and is nontrivial.  It is
unramified at every middle root, but restricting it to `U_all` still removes
those points from the space.  Applying (3.3) twice proves

\[
 \begin{aligned}
 \dim H_c^1(U_{\rm all})&=(d+1)e-2,\\
 \dim H_c^1(U_{\min})&=2e-2,
 \end{aligned}
\]

and subtraction proves (0.6).

Equivalently, extending the top line across the middle points adds their
trace values back to the complete sum.  The extension is canonical as a
sheaf because local monodromy is trivial there.  It is not automatically
legal for the arithmetic source: if the native sum excludes those atoms,
adding them back changes the statistic.  One must prove either exact
source-zero contributions at the filled points or a compensating boundary
identity.

This is why an endomorphism identity surviving on one common open is weaker
than a conductor-compressed trace theorem on the maximal extension.

## 5. Closed-place scaling at fixed \(q\)

The number of monic irreducibles of degree \(e\) is

\[
 I_q(e)={1\over e}\sum_{r\mid e}\mu(r)q^{e/r}.
\tag{5.1}
\]

Define

\[
 e_q(d)=\min\{e\ge1:I_q(e)\ge d+1\}.
\tag{5.2}
\]

Then the path construction exists with common degree \(e_q(d)\).  The
standard estimate \(I_q(e)=q^e/e+O(q^{e/2})\) gives (0.7).  Therefore

\[
 \begin{array}{c|c}
 \text{object}&\dim H_c^1\\ \hline
 \text{maximally extended top line}&2e_q(d)-2=O_q(\log d),\\
 \text{top line on common product-torsor open}
 &(d+1)e_q(d)-2=O_q(d\log d).
 \end{array}
\tag{5.3}
\]

The top selected rank remains one in both rows.  The difference is entirely
topological: whether removable holes are filled.

When \(q\ge d+1\), one may take \(e=1\).  On the minimal two-puncture open,
\(H_c^\bullet\) vanishes and the selected complete character sum is exactly
zero.  On the common open, the cost remains \(d-1\).  This finite row is a
sharp control for the extension gate, not a fixed-\(q\), \(d\to\infty\)
asymptotic.

## 6. Relation to the formal leverage gain

The frozen checkerboard Gram theorem has one selected top line and formal
leverage ratio

\[
 {L_{\rm cb}\over L_{\rm full}}={4Q\over Q+P}.
\]

The present path construction proves that a one-line tensor character can
have maximally extended Betti cost only \(O_q(\log d)\), even with full
\(C_2^d\) geometric torsor monodromy.  This makes an exponential-leverage /
subexponential-sheaf-cost regime algebraically possible.

It does not place the Gram panel and the path torsor inside the same native
FFPS source.  In particular, no conclusion may multiply the formal leverage
ratio by (0.4) and call the result WCADD, WCKUM, CYSEL, or an RH estimate.
The missing work is precisely:

1. construct the many-place physical orientation in the native source;
2. identify its selected top line with a path-like tensor;
3. justify extension across every canceled source stratum;
4. retain the signed Wick recombination and principal anomaly;
5. pay varying-owner, carrier, roughness, and conductor sums.

## 7. Proof ledger

| statement | grade |
|---|---|
| independence of the path squareclasses | **PROVED EXACT ALL \(d,e\)** |
| top-character telescoping (0.2) | **PROVED EXACT ALL \(d,e\)** |
| geometric invariant criterion (3.2) | **PROVED ON \(\mathbf P^1\)** |
| cohomology dimensions (0.3), (0.5) | **PROVED FROM IMPORTED GOS + DUALITY** |
| trace bound (0.4) | **PROVED FROM IMPORTED TRACE FORMULA + WEIL II** |
| exact removable-puncture tax (0.6) | **PROVED EXACT** |
| fixed-\(q\) degree law (0.7) | **PROVED FROM THE PRIME-POLYNOMIAL FORMULA** |
| full many-place FFPS adapter | **OPEN** |
| legal source extension across middle punctures | **OPEN / CENTRAL GATE** |
| CYSEL, WCADD, WCKUM, RH, or GRH | **OPEN / UNPROVED** |

No external novelty or priority claim is made.

## 8. Reproduction

The replay uses the exact irreducible-count formula and bit-vector path
incidence.  It checks \(q=3,5,7,9\) and \(1\le d\le128\), with no finite
field, polynomial, curve, character family, cohomology, or zero enumeration.
The geometric and weight theorems remain visibly imported.

~~~powershell
python research/l-families/atlas/function_field/ffps_checkerboard_telescoping_curve_model.py --check
python -O research/l-families/atlas/function_field/ffps_checkerboard_telescoping_curve_model.py --check
python -m unittest tests.test_ffps_checkerboard_telescoping_curve_model
python -O -m unittest tests.test_ffps_checkerboard_telescoping_curve_model
python -m ruff check research/l-families/atlas/function_field/ffps_checkerboard_telescoping_curve_model.py tests/test_ffps_checkerboard_telescoping_curve_model.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_checkerboard_telescoping_curve_model.py tests/test_ffps_checkerboard_telescoping_curve_model.py
~~~
