# Closed-point Adams compression for the ternary place selector

Status: **exact one-place and separable two-place closed-point trace
theorems; exact bounded-character application to the clean ternary
norm/Kummer package; no native owner/Boolean/Artin--Schreier adapter,
uniform pushed-forward Betti estimate, CYSEL, RH, or GRH theorem**

Bounded exact replay:
[ffps_closed_point_adams_compression.py](ffps_closed_point_adams_compression.py).
Canonical summary:
[ffps_closed_point_adams_compression.json](ffps_closed_point_adams_compression.json).

Frozen dependencies:

| source | commit | git blob | role |
|---|---|---|---|
| FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md | 464c3705f | ab16e6c0894e51303119692e67b2f2bf59ba73e4 | ternary relative-projector normalization |
| FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md | 961603fd0 | cc8b649848a2e7425989a553628d9c830f56f6d1 | fixed closed-point tower and coefficient-space cycle selector |
| FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md | 691166b8c | d136159ea9f0fa41600e673dc2c6ef1a2ad2f10f | forced full-\(S_d\) selector mass |
| FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md | c81e69db1 | 1cb3c9613308474e9ad80de4d8d18e86a18a1b97 | rank-48 varying-place physical package |

## 0. Verdict

There is an exact escape from the exponential hook mass of the
coefficient-space irreducibility selector, but it changes the geometric
question.

For a Frobenius-compatible constructible class \(V\) on a fixed
\(\mathbf F_q\)-scheme \(X\), put

\[
 A_n(V)=\sum_{u\in X(\mathbf F_{q^n})}
 \operatorname{Tr}(F_{q^n,u}\mid V_{\bar u})
\]

and

\[
 P_d(V)=\sum_{\substack{x\in|X|\\ \deg x=d}}
 \operatorname{Tr}(F_x\mid V_{\bar x}).
\]

Then Adams operations give the exact closed-point extractor

\[
 \boxed{
 dP_d(V)=\sum_{e\mid d}\mu(e)
 A_{d/e}(\psi^eV).}
\tag{0.1}
\]

For a two-place trace kernel carrying two independent Frobenius actions,
the corresponding formula is

\[
 \boxed{
 abP_{a,b}(K)=
 \sum_{e\mid a}\sum_{f\mid b}
 \mu(e)\mu(f)
 A_{a/e,b/f}^{\rm sep}(\psi_1^e\psi_2^fK).}
\tag{0.2}
\]

Thus exact place degrees cost \(\tau(a)\tau(b)\) extension-field trace
evaluations, rather than the coefficient-space selector mass

\[
 {2^{a+b-2}\over ab}.
\tag{0.3}
\]

The clean ternary norm/Kummer package is a finite sum of external character
lines. After independent additive pushforward on its two physical sides,
the resulting place kernel is therefore separable and (0.2) applies. Every
partial Adams transform still has physical deck-character rank \(48\); the
selected and relative pieces still have underlying ranks 32 and 16. The
exponential exact-cycle mass is therefore absent from this **signed
extension-field recombination**. This rank statement is about the finite
deck package, not the total cohomology created by a source pushforward.

This does not contradict the exact full-\(S_d\) selector no-go. That theorem
asks for the characteristic function of a \(d\)-cycle as one semisimple
class on the degree-\(d\) coefficient space. Formula (0.1) instead compares
trace sums over several extension fields of one fixed place space. It is not
a cheaper presentation of the same \(S_d\)-class.

There is also a precise obstruction. An arbitrary sheaf on \(X\times Y\)
has one diagonal Frobenius structure, not two independent partial Frobenius
structures. Formula (0.2) is valid for a separable trace kernel--in
particular a finite rational sum of external products--or for a stronger
bivariate Weil object supplied with commuting partial Frobenii. It cannot
be applied merely because a coupled source happens to mention two places.
The full FFPS owner/core/Boolean/Artin--Schreier complex has not been shown
to lie in this separable trace category.

## 1. One-place closed-point theorem

Let \(X/\mathbf F_q\) be separated of finite type. Work in the rational
Grothendieck group of constructible Weil complexes with coefficients of
characteristic zero. It is enough to stratify \(X\) so that every
cohomology sheaf is lisse. The \(e\)-th Adams operation is characterized at
every closed point by

\[
 \operatorname{Tr}(F_x\mid\psi^eV_{\bar x})
 =\operatorname{Tr}(F_x^e\mid V_{\bar x}).
\tag{1.1}
\]

This convention includes alternating signs from a complex in its
Grothendieck class.

### Theorem 1.1

For every \(n\ge1\),

\[
 \boxed{
 A_n(V)=\sum_{d\mid n}dP_d(\psi^{n/d}V).}
\tag{1.2}
\]

Consequently (0.1) holds for every \(d\ge1\).

**Proof.** A degree-\(d\) closed point with \(d\mid n\) gives exactly \(d\)
points of \(X(\mathbf F_{q^n})\). At each one, \(F_{q^n}\) acts as
\(F_x^{n/d}\). Summing its contribution proves (1.2).

Now expand the right side of (0.1):

\[
 \begin{aligned}
 \sum_{e\mid d}\mu(e)A_{d/e}(\psi^eV)
 &=\sum_{e\mid d}\mu(e)
   \sum_{r\mid d/e}rP_r
   (\psi^{e(d/e)/r}V)\\
 &=\sum_{r\mid d}rP_r(\psi^{d/r}V)
   \sum_{e\mid d/r}\mu(e).
 \end{aligned}
\]

The inner sum is zero unless \(r=d\), when it is one. The result is
\(dP_d(V)\). \(\square\)

No purity, smoothness, irreducibility, or RH hypothesis enters this
identity. Those hypotheses matter only when one tries to bound the
extension-field sums on the right.

## 2. Two independent place degrees

Let \(X,Y/\mathbf F_q\) be separated of finite type and define the separable
trace group

\[
 \mathscr E(X,Y)=
 K_0^{\rm Weil}(X)_{\mathbf Q}
 \otimes_{\mathbf Q}
 K_0^{\rm Weil}(Y)_{\mathbf Q}.
\tag{2.1}
\]

Write an element as \(K=\sum_jc_jV_j\boxtimes W_j\). Define

\[
 \begin{aligned}
 A_{m,n}^{\rm sep}(K)
   &=\sum_jc_jA_m(V_j)A_n(W_j),\\
 P_{a,b}(K)
   &=\sum_jc_jP_a(V_j)P_b(W_j),\\
 \psi_1^e\psi_2^fK
   &=\sum_jc_j\psi^eV_j\boxtimes\psi^fW_j.
 \end{aligned}
\tag{2.2}
\]

These definitions are independent of the chosen tensor presentation. They
also apply verbatim to a bivariate trace object with commuting partial
Frobenii; (2.1) is the minimal category needed here.

### Theorem 2.1

For all \(a,b\ge1\), formula (0.2) holds.

**Proof.** Apply (1.2) to each tensor factor:

\[
 A_{m,n}^{\rm sep}(K)=
 \sum_{r\mid m}\sum_{s\mid n}
 rsP_{r,s}(\psi_1^{m/r}\psi_2^{n/s}K).
\tag{2.3}
\]

Double Möbius inversion, using
\(\psi_i^u\psi_i^v=\psi_i^{uv}\), leaves only \(r=a,s=b\).
\(\square\)

### Removing the equal-place diagonal

If \(X=Y\), \(a=b\), and the two places must be distinct, define

\[
 \delta(V\boxtimes W)=V\otimes W.
\tag{2.4}
\]

Then

\[
 \boxed{
 P_{a,a}^{\ne}(K)=P_{a,a}(K)-P_a(\delta K).}
\tag{2.5}
\]

The first term uses \(\tau(a)^2\) evaluations from (0.2), and the diagonal
uses another \(\tau(a)\) evaluations from (0.1). If \(a\ne b\), equality of
the two closed places is impossible and no correction occurs. Symmetric
unordered pairs require the usual final factor of two and fixed-point
check; this packet keeps the ordered convention.

### Why an ordinary product sheaf is not enough

For a general \(M\in K_0^{\rm Weil}(X\times Y)\), the ordinary trace formula
supplies sums over \((X\times Y)(\mathbf F_{q^n})\), with the same Frobenius
power on both coordinates. It does not supply \(A_{m,n}\) for independent
\(m,n\), nor operations \(\psi_1,\psi_2\). Consequently the diagonal tower
cannot distinguish every ordered degree pair. One needs an external-product
decomposition, commuting partial Frobenii, or an equivalent relative trace
adapter. This is a structural condition, not a technicality in the proof.

## 3. Closed-point form of the clean ternary package

Assume \(q\equiv1\pmod6\). Let \(C\) be the clean curve whose closed points
index the allowed function-field places. Over one side, retain the sector
anchor \(u\), two physical coordinates \(X_1,X_2\), and the orientation
equations

\[
 h_1^2=X_1/u,\qquad h_2^2=X_2/u.
\tag{3.1}
\]

At a degree-\(d\) closed point \(x\), the trace convention for a Kummer sheaf
automatically evaluates the base character on a norm:

\[
 t_{\mathcal L_\chi}(z)
 =\chi(N_{k_x/\mathbf F_q}z).
\tag{3.2}
\]

Hence (3.1) is trace-equivalent, on the irreducible degree-\(d\) row, to the
scalar norm-orientation cover in the frozen universal packet. Indeed,
\(X/u\) is a square in \(k_x\) exactly when its norm is a square in
\(\mathbf F_q\), and if \(h^2=X/u\), then \(N(h)\) is a square root of
\(N(X/u)\). The cubic character is unchanged by \(h\mapsto-h\).

Let \(R_{2,X}\) and \(R_{2,Y}\) denote the regular character sums of the two
orientation groups \(C_2^2\), and let \(\kappa_X,\kappa_Y\) denote the two
cubic Kummer characters. For alignment
\(\varepsilon\in\{1,-1\}\), the rank-48 regular physical trace kernel is

\[
 \boxed{
 \mathcal H_\varepsilon=
 \sum_{\alpha\in\widehat{C_2^2}}
 \sum_{\beta\in\widehat{C_2^2}}
 \sum_{r=0}^2
 (\mathcal L_{X,\alpha}\otimes\kappa_X^r)
 \boxtimes
 (\mathcal L_{Y,\beta}\otimes\kappa_Y^{\varepsilon r}).}
\tag{3.3}
\]

This is the external-line form of the direct-product monodromy theorem in
the frozen norm-torsor packet. The selected, relative, and hard trace
classes are

\[
 \begin{aligned}
 \mathcal S_\varepsilon
   &=\frac14\sum_{\alpha,\beta}
     \sum_{r=1}^2
     (\mathcal L_{X,\alpha}\otimes\kappa_X^r)
     \boxtimes
     (\mathcal L_{Y,\beta}\otimes\kappa_Y^{\varepsilon r}),\\
 \mathcal R
   &=\sum_{\alpha,\beta}
     \mathcal L_{X,\alpha}\boxtimes\mathcal L_{Y,\beta},\\
 \mathcal C_\varepsilon&=\mathcal R+\mathcal S_\varepsilon.
 \end{aligned}
\tag{3.4}
\]

Thus \(\mathcal C_\varepsilon-\mathcal S_\varepsilon=\mathcal R\) before
any absolute value. More precisely, let
\(\pi_X:Z_X\to C\) and \(\pi_Y:Z_Y\to C\) be the two physical parameter
maps carrying the anchor, coordinate, and orientation variables. Formula
(3.3) is a sum of external lines on \(Z_X\times Z_Y\). Künneth and
additivity show that

\[
 R(\pi_X\times\pi_Y)_!\mathcal H_\varepsilon
 =\sum_{\alpha,\beta,r}
   R\pi_{X,!}(\mathcal L_{X,\alpha}\otimes\kappa_X^r)
   \boxtimes
   R\pi_{Y,!}(\mathcal L_{Y,\beta}\otimes
                    \kappa_Y^{\varepsilon r})
\tag{3.5}
\]

belongs to \(\mathscr E(C,C)\), whenever these are the actual independent
additive pushforwards used by the trace problem. Theorem 2.1 then extracts
its two place degrees without an \(S_a\times S_b\) cycle projector.

Equation (3.5) does not say that Adams operations commute with pushforward.
The extractor applies Adams to each resulting class \(R\pi_!\mathcal L\).
Its stalk Frobenius eigenvalues, as well as its deck character, are raised
to the required power. The deck-character bookkeeping remains bounded, but
the presentation and Betti complexity of these Adams classes must still be
controlled.

This is a trace-level replacement of the irreducible-polynomial coefficient
space by the closed-point space. It does not yet identify the native FFPS
source variables with the coordinates in (3.1).

## 4. Exact Adams behavior of \(C_2^4\times C_3\)

For \(R_2=\sum_{\alpha\in\widehat{C_2^2}}\alpha\),

\[
 \boxed{
 \psi^eR_2=
 \begin{cases}
 R_2,&e\text{ odd},\\
 4\mathbf1,&e\text{ even}.
 \end{cases}}
\tag{4.1}
\]

Put

\[
 D_\varepsilon=
 \sum_{r=0}^2\kappa_X^r\boxtimes\kappa_Y^{\varepsilon r}.
\]

Then

\[
 \boxed{
 \psi_1^e\psi_2^fD_\varepsilon
 =\sum_{r=0}^2
 \kappa_X^{er}\boxtimes\kappa_Y^{\varepsilon fr}.}
\tag{4.2}
\]

The right side is always an honest rank-three character sum:

| divisibility by \(3\) | cubic image |
|---|---|
| \(3\nmid e,\ 3\nmid f\) | graph of slope \(\varepsilon f/e\) in \(\mathbf F_3\) |
| \(3\mid e,\ 3\nmid f\) | \(\mathbf1\boxtimes R_3\) |
| \(3\nmid e,\ 3\mid f\) | \(R_3\boxtimes\mathbf1\) |
| \(3\mid e,\ 3\mid f\) | \(3(\mathbf1\boxtimes\mathbf1)\) |

The two selected cubic lines behave the same way with the \(r=0\) term
removed before applying Adams; they remain an honest rank-two sum, although
the two lines can merge into two copies of the trivial line. Combining
(4.1)--(4.2) gives

\[
 \begin{array}{c|c|c}
 \text{class}&\text{underlying character rank per divisor pair}
   &\text{absolute weighted line mass}\\ \hline
 \mathcal H_\varepsilon&48&48\\
 \mathcal S_\varepsilon&32&8\\
 \mathcal R&16&16\\
 \mathcal C_\varepsilon&48&24.
 \end{array}
\tag{4.3}
\]

These finite deck-character quantities are unchanged by every partial
Adams transform. In particular, no Schur-functor expansion is needed to
describe the \(C_2^4\times C_3\) quotient: the abelian character powers in
(4.1)--(4.2) are explicit honest sums. This does not assert that the entire
pushed-forward cohomology is an honest rank-48 sheaf after Adams; its
non-deck eigenvalues are also powered, and its virtual presentation is part
of the open Betti gate.

For the regular package, the raw character-line evaluation ledger is

\[
 \boxed{
 48\tau(a)\tau(b)
 +\mathbf1_{a=b}\,48\tau(a),}
\tag{4.4}
\]

where the second term is needed only when equal places are excluded. This
is to be compared with the termwise coefficient-space rank mass

\[
 48{2^{a+b-2}\over ab}.
\tag{4.5}
\]

Equation (4.4) counts character-line trace evaluations, not the total Betti
number of a pushed-forward source complex. It therefore proves a selector
compression theorem, not a Deligne estimate.

## 5. Exact validity criterion and source obstruction

The closed-point replacement is valid when all of the following are true.

1. The varying place is represented as a closed point of one fixed
   finite-type \(\mathbf F_q\)-space.
2. The local weight is the Frobenius trace of one compatible constructible
   class on that space; degree dependence enters through Frobenius power,
   not by changing the geometric object.
3. For two independently prescribed degrees, the joint weight lies in the
   separable trace group (2.1), or a genuine bivariate object supplies two
   commuting partial Frobenii.
4. All hard-sector, diagonal, and signed recombinations are made linearly
   before a triangle inequality or absolute value.
5. If the same place is forbidden, the diagonal class in (2.4) is defined
   and its one-place correction is retained.

It fails, or remains unproved, in any of the following situations.

* A degree-\(d\) coefficient-space complex is supplied separately for every
  \(d\), with no descent to one fixed closed-point space.
* A Boolean cutoff, owner/core incidence condition, or source truncation
  depends on polynomial representatives rather than only on the resulting
  compatible closed-point trace.
* An Artin--Schreier phase or cleanup couples the two residues in a way that
  has only diagonal Frobenius and no external-product decomposition.
* A positivity step is taken before the signed Möbius sums in (0.1)--(0.2).
* The required extension-field towers change the source normalization or
  the physical hard mask.

The current FFPS source has unresolved instances of the second and third
bullets. In particular, the native owner labels, both Boolean sums, the
actual \(Pc^2,Qd^2\) maps, the source-selected Artin--Schreier phases, shared
incidence, Wick subtraction, and the varying-conductor signed recombination
have not been assembled as one separable bivariate Weil class. It would be
incorrect to apply (0.2) to that full source before this adapter is proved.

## 6. What the compression does and does not buy

The theorem changes the most economical next target. For the clean local
mask, there is no reason to tensor with the exact full-cycle selector and
pay (0.3). Instead one should:

~~~text
construct one fixed closed-point trace kernel
  -> prove external/partial-Frobenius factorization
  -> retain all divisor-indexed Adams transforms
  -> simplify the signed double Möbius sum
  -> only then estimate compactly supported traces.
~~~

If the native source adapter has this form, the exact degree tax is only a
divisor-count tax. What remains load-bearing is the size of the compactly
supported cohomology of every transformed source class and the cancellation
in their signed recombination. Rank \(48\) of the physical deck package is
not a uniform Betti bound after owner/Boolean/source pushforward.

The theorem does **not** prove:

* a fixed closed-point model for the complete FFPS owner/Boolean source;
* compatibility of its Artin--Schreier phases with partial Frobenius;
* a uniform Betti/conductor bound for the pushed-forward classes;
* cancellation of resonant or geometrically constant constituents;
* CYSEL, WCADD106140, WCKUM106140, or principal individualization;
* RH or GRH.

## 7. Proof ledger

| statement | grade |
|---|---|
| one-place orbit formula (1.2) and Adams--Möbius inversion (0.1) | **PROVED EXACT** |
| separable two-place formula (0.2) | **PROVED EXACT** |
| equal-degree distinct-place correction (2.5) | **PROVED EXACT** |
| absence of partial Frobenius for a general product sheaf | **EXACT SCOPE OBSTRUCTION** |
| trace equivalence of local orientation and norm orientation | **PROVED EXACT FOR THE CLEAN KUMMER PACKAGE** |
| external character decomposition (3.3)--(3.4) | **PROVED FROM THE LOCKED DIRECT-PRODUCT NORMAL FORM** |
| Adams laws (4.1)--(4.2) and bounded ranks | **PROVED EXACT FINITE-ABELIAN CHARACTER ALGEBRA** |
| replacement of exponential selector mass by \(\tau(a)\tau(b)\) trace terms | **PROVED FOR THE CLEAN SEPARABLE PACKAGE** |
| native owner/Boolean/Artin--Schreier separable adapter | **NOT CONSTRUCTED** |
| uniform pushed-forward Betti or signed trace estimate | **OPEN** |
| CYSEL, WCADD106140, WCKUM106140, RH, or GRH | **NOT PROVED** |

The orbit formula and Adams operations are standard. No external novelty or
priority is claimed for them. The project contribution is the
source-sensitive composition: it identifies an exact non-exponential
closed-point route for the rank-48 ternary mask, proves its finite-abelian
stability under both partial Adams operations, and states the exact
factorization gate that the native FFPS source must pass.

## 8. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_closed_point_adams_compression.py --check
python -B -O research/l-families/atlas/function_field/ffps_closed_point_adams_compression.py --check
python -B -m unittest tests.test_ffps_closed_point_adams_compression
python -B -O -m unittest tests.test_ffps_closed_point_adams_compression
python -B -m ruff check research/l-families/atlas/function_field/ffps_closed_point_adams_compression.py tests/test_ffps_closed_point_adams_compression.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_closed_point_adams_compression.py tests/test_ffps_closed_point_adams_compression.py
~~~

The replay checks the one- and two-variable Möbius identities on exact
synthetic Frobenius eigenvalue packets, all \(C_2^4\times C_3\) partial
Adams profiles for \(1\le e,f\le12\), and divisor-term ledgers through
\(a,b\le12\). It enumerates no finite field, polynomial, closed place,
curve, source atom, \(L\)-function, or zero.
