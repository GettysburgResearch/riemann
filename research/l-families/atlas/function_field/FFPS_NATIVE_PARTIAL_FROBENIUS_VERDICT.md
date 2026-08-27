# Native FFPS phase kernels fail the separable partial-Frobenius gate termwise

Status: **exact separation-rank and partial-Frobenius no-go for the universal
native Artin--Schreier phase/incidence constituent; exact conditional audit of
the relative cleanup; no full native source complex, source-image occupancy
theorem, uniform trace estimate, CYSEL, RH, or GRH theorem**

Bounded exact replay:
[ffps_native_partial_frobenius_verdict.py](ffps_native_partial_frobenius_verdict.py).
Canonical summary:
[ffps_native_partial_frobenius_verdict.json](ffps_native_partial_frobenius_verdict.json).

## 0. Verdict

The clean rank-\(48\) ternary norm/Kummer package belongs to the external-line
category required by closed-point Adams extraction. The native bilateral
Artin--Schreier source does not belong to that category termwise.

Let \(Q\) be the cardinality of one marked-place residue field. The nonzero
additive Fourier block on \(m\) distinct physical residues has exact Gram
matrix

\[
 QI_m-J_m.
\tag{0.1}
\]

Consequently its separation rank is

\[
 \boxed{
 \operatorname {rank}(QI_m-J_m)
 =
 \begin{cases}
 m,&m<Q,\\
 Q-1,&m=Q.
 \end{cases}}
\tag{0.2}
\]

The Wick-centered incidence kernel has the same matrix, up to the scalar
\(Q\). Thus every proper \(m\)-cell physical sector has full rank \(m\), while
the universal all-residue block has rank \(Q-1\). For a degree-\(a\) place
over \(\mathbf F_q\),

\[
 Q=q^a.
\tag{0.3}
\]

Any source-independent external-product presentation valid on a physical
sector containing a positive proportion of the residue cells therefore has
rank exponential, not subpower or polynomial, in \(a\).

There is a second, geometric obstruction. On the universal phase plane,

\[
 \mathcal A=\mathcal L_\psi(hx)
\tag{0.4}
\]

is not invariant under Frobenius in \(h\) alone or \(x\) alone. After the
complete phase square is formed, the diagonal incidence sheaf is likewise
not invariant: partial Frobenius moves its support from \(x=y\) to
\(x^Q=y\).

Therefore the separable two-place Adams formula in
FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md cannot be applied term by term to the
universal native phase/incidence kernel.

This verdict has a strict scope. It does **not** prove that the actual native
source occupies a positive proportion of all residue cells; that image has
not been classified. It also does not rule out a signed relative complex in
which the high-rank incidence constituents cancel before Adams extraction.
No such full relative complex has been constructed.

## 1. Frozen source and exact factor graph

The packet freezes the following source statements.

| source | commit | git blob | role |
|---|---|---|---|
| L-106120 | 98af0db6e | a8d829dc10611adb7bfb4853902bdff0ab02a065 | bilateral two-phase member |
| L-106131 | 98af0db6e | 37722c3f36ec7d1681f34d4329a3795e5028f7ae | Wick-normal additive/Kummer identity |
| L-106191 | 98af0db6e | 85c4ef92ead7d8b235f9c195c3c0acd16d16030f | centered double-incidence kernel |
| T-106140 | 98af0db6e | d5be8e376c88b63de0be19e0d9e8791624e99ae2 | signed global recombination |
| FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md | b87036614 | c79e52ebf0099fe416bc2c79dcb041cc21e025fb | precise separable/partial-Frobenius gate |
| FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md | b87036614 | ab16e6c0894e51303119692e67b2f2bf59ba73e4 | \(C-S=\Pi_0\) on a genuine torsor |
| FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md | b87036614 | d531ef36d314549072052cc5b1ae1762c11d00e2 | resonance and common-complex gate |
| FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md | b87036614 | e7cb9133bb6b57ddbb1c7f1e350f1d2d0af7bd1a | source order and cleanup contract |

After common-square extraction, one native bilateral member is

\[
 \mathcal W_{\ell,\rho;h,k}
 =
 \sum_{P,Q,c,d}
 \overline {A_{P,c}}B_{Q,d}\,
 e_\ell(-hQd^2)e_\rho(kPc^2),
\tag{1.1}
\]

with

\[
 \ell=P^-(c),\qquad \rho=P^-(d),
\tag{1.2}
\]

and physical coordinates

\[
 X=Pc^2\pmod\rho,\qquad
 Y=Qd^2\pmod\ell.
\tag{1.3}
\]

The exact factor graph is a crossed square:

~~~text
left source (P,c)  --selects--> ell
      |                            |
      | X=Pc^2                     | e_ell(-hY)
      v                            v
rho phase side <-------------- right source (Q,d)

right source (Q,d) --selects--> rho
      |                            |
      | Y=Qd^2                     | e_rho(kX)
      v                            v
ell phase side  <--------------- left source (P,c)
~~~

Coprimality, common-core extraction, Boolean labels, physical shells, owner
sectors, and later cleanups remain attached to this graph. For fixed
\((\ell,\rho)\) and fixed source support, the two displayed phase factors
tensor. That pointwise tensorization is not a conductor-uniform external
decomposition: each Fourier edge already has the growing rank (0.2).

## 2. Exact Fourier-rank theorem

Let \(\psi\) be a nontrivial additive character of \(\mathbf F_Q\), let
\(S=\{x_1,\ldots,x_m\}\) be \(m\) distinct residues, and form

\[
 F_{h,j}=\psi(hx_j),
 \qquad h\in\mathbf F_Q^\times.
\tag{2.1}
\]

Additive orthogonality gives

\[
 (F^*F)_{i,j}
 =\sum_{h\neq0}\psi(h(x_j-x_i))
 =
 \begin{cases}
 Q-1,&i=j,\\
 -1,&i\neq j.
 \end{cases}
\tag{2.2}
\]

Hence

\[
 F^*F=QI_m-J_m.
\tag{2.3}
\]

The eigenvalue on the constant vector is \(Q-m\), and every orthogonal vector
has eigenvalue \(Q\). This proves (0.2). In particular:

- on all \(Q\) residues, the rank is \(Q-1\);
- on the \(Q-1\) nonzero residues, the rank is \(Q-1\);
- on a sign-pair or quadratic-sector set of \(m<Q\) distinct residues, the
  rank is exactly \(m\).

Equation (2.3) proves the raw-residue statement. Independently, frozen
L-106131.1 proves that the native sign-pair aggregation has the same operator
\(QI-J\) on its \((Q-1)/2\) coordinates, so its rank conclusion does not
depend on choosing representatives of the sign pairs.

The theorem does not assume that the live source fills any one of those
sets. It says that a universal adapter cannot compress the Fourier block:
every occupied set of \(m<Q\) distinct physical cells costs \(m\) external
coordinates.

For two marked places of cardinalities \(Q_1,Q_2\), the tensor phase block has
rank

\[
 \operatorname {rank}F_1\,
 \operatorname {rank}F_2.
\tag{2.4}
\]

On complete nonzero sectors this is

\[
 (Q_1-1)(Q_2-1).
\tag{2.5}
\]

The replay verifies (0.2) by exact rational elimination for
\(Q=3,5,7,11\), and verifies (2.4) directly on the \((3,5)\) and \((5,7)\)
blocks. It enumerates no finite-field element: only the orthogonality Gram is
formed.

## 3. Wick centering does not lower separation rank

L-106191 rewrites the normalized additive square as

\[
 \sum_{\omega\neq\omega'}
 \widetilde z_\omega\overline{\widetilde z_{\omega'}}
 \left(\mathbf1_{x_\omega=x_{\omega'}}-{1\over Q_1}\right)
 \left(\mathbf1_{y_\omega=y_{\omega'}}-{1\over Q_2}\right).
\tag{3.1}
\]

On \(m\) distinct residue labels, one centered factor has matrix

\[
 H_{Q,m}=I_m-{1\over Q}J_m.
\tag{3.2}
\]

Multiplying by \(Q\) gives (0.1), so

\[
 \operatorname {rank}H_{Q,m}
 =
 \begin{cases}
 m,&m<Q,\\
 Q-1,&m=Q.
 \end{cases}
\tag{3.3}
\]

Literal Wick ordering deletes the source-atom pairs
\(\omega=\omega'\). It does not delete different atoms in the same physical
residue cell. Equivalently, two labelled copies of the residue set realize
the full off-atomic matrix (3.2) between the copies. The universal cleanup
kernel therefore retains the same separation obstruction.

This is not a lower bound for the rank of the **actual** native source image.
Such a bound would require an occupancy theorem showing how many distinct
physical cells survive every owner/Boolean restriction. No such theorem is
imported here.

## 4. The natural Artin--Schreier line has no partial Frobenius

Work in characteristic \(p\), put \(Q=p^r\), and consider (0.4) on
\(\mathbf A_h^1\times\mathbf A_x^1\). Pullback by Frobenius in the \(h\)
coordinate alone changes the Artin--Schreier function by

\[
 (h^Q-h)x.
\tag{4.1}
\]

Two Artin--Schreier lines are geometrically isomorphic only if their
difference is

\[
 G^p-G+c
\tag{4.2}
\]

for a rational function \(G\) and constant \(c\). If (4.2) is polynomial,
then \(G\) has no pole: at a pole, the \(G^p\) term has strictly larger pole
order and cannot cancel. Thus \(G\) is polynomial.

If \(\deg_xG=d>0\), then

\[
 \deg_x(G^p-G)=pd>1,
\tag{4.3}
\]

whereas (4.1) has \(x\)-degree one. If \(G\) is independent of \(x\), it
cannot produce (4.1). Hence the partial-\(h\) isomorphism does not exist.
Interchanging \(h,x\) proves the same for partial Frobenius in \(x\).

Total Frobenius is different: it raises both coordinates and is the ordinary
Weil structure. The obstruction is exactly to **independent** partial
Frobenii.

## 5. The centered diagonal also fails partial Frobenius

The sheaf-theoretic support of the equality term in (3.2) is the diagonal

\[
 \Delta:\quad x=y.
\tag{5.1}
\]

Pullback under Frobenius in \(x\) alone has support

\[
 \Gamma_Q:\quad x^Q=y.
\tag{5.2}
\]

Over the geometric product these are distinct irreducible graphs: their
defining monomial supports are respectively

\[
 \{(0,1),(1,0)\},
 \qquad
 \{(0,1),(Q,0)\}.
\tag{5.3}
\]

Subtracting the constant background \(Q^{-1}\mathbf1\) does not identify
those supports. Therefore the natural centered-incidence class also lacks a
partial-Frobenius structure.

On \(\mathbf F_Q\)-rational points, \(x^Q=x\), so the two graphs have the same
rational row. This is why a base-field trace table alone cannot detect the
geometric obstruction. The exact support comparison is load-bearing.

## 6. Consequence for closed-point Adams extraction

The clean ternary norm/Kummer class is a finite sum of \(48\) external
character lines; partial Adams operations preserve its finite deck rank. The
native phase factor changes the category:

~~~text
clean rank-48 Kummer package
  tensor native Artin--Schreier phase
    -> universal external rank comparable with Q
    -> no independent partial Frobenius on the natural phase line
  square and sum phases
    -> centered diagonal incidence
    -> the same growing rank
    -> diagonal moves under partial Frobenius.
~~~

Thus the clean Adams compression cannot simply be quoted after tensoring the
full native source. Formula (0.2) of the closed-point Adams packet remains
valid for separable kernels or genuine bivariate objects with commuting
partial Frobenii; the native universal phase/incidence constituent satisfies
neither condition.

This is a termwise/category no-go, not a trace-estimate no-go. Four escapes
remain logically open:

1. Prove that the actual native source occupies only subpower-many physical
   residue cells, and use a source-specific presentation.
2. Keep the connected signed incidence/Kummer--Möbius combination intact and
   prove that the high-rank diagonal correspondences cancel before any
   absolute value.
3. Construct the common relative \(C-S\) complex and transport all cleanups
   as common equivariant functors.
4. Develop a correspondence-level closed-point formula that retains diagonal
   and graph terms instead of requiring separability.

The first has no current occupancy theorem. The second is the open
WCCORR/WCADD/WCKUM analytic route. The third is the open relative-complex
route. The fourth would be a new category, not an application of the present
Adams theorem.

## 7. Relative \(C-S\) cleanup audit

The exact cyclic identity

\[
 C-S=\Pi_0
\tag{7.1}
\]

holds as an identity of endomorphisms on every constructed split cyclic
torsor. Every genuinely common \(E\)-linear pullback, pushforward, extension,
or cone preserves it.

The native audit is:

| operation | verdict | reason |
|---|---|---|
| clean cyclic hard-selected difference | **PROVED EXACT** | (7.1) on the constructed torsor |
| common \(E\)-linear functor | **PROVED FORMALLY** | functoriality preserves one existing identity |
| literal atom diagonal and equal physical-product strata | **CONDITIONALLY EQUIVARIANT** | the relations are base-defined and deck-stable, but the common native source maps are unbuilt |
| owner/core overlap and shared incidence | **CONDITIONALLY EQUIVARIANT** | likewise base-defined only after one common adapter exists |
| constant/resonant subquotient removal | **NOT AUDITED GLOBALLY** | multiplicity, Tate shift, arithmetic Frobenius scalar, and source coefficient must all match |
| signed conductor recombination | **FORMALLY LINEAR** | preserves an existing common identity but cannot construct it |

Accordingly:

\[
 \boxed{\text{the full native relative }C-S\text{ complex remains unbuilt}.}
\tag{7.2}
\]

It would be incorrect to report that the rank obstruction disproves that
relative route. Common high-rank pieces can cancel in a virtual difference.
It would be equally incorrect to assume they cancel merely because the clean
torsor identity exists.

## 8. Proof ledger

| statement | grade |
|---|---|
| frozen bilateral factor graph (1.1)--(1.3) | **IMPORTED EXACT** |
| Fourier Gram (2.2)--(2.3) | **PROVED EXACT** |
| rank formula (0.2) | **PROVED EXACT ALL \(Q,m\)** |
| bilateral rank multiplication | **PROVED EXACT** |
| Wick-centered rank (3.2)--(3.3) | **PROVED EXACT** |
| Artin--Schreier partial-Frobenius obstruction | **PROVED BY THE COBBOUNDARY DEGREE TEST** |
| diagonal partial-Frobenius obstruction | **PROVED BY DISTINCT GEOMETRIC SUPPORT** |
| clean torsor \(C-S=\Pi_0\) | **IMPORTED PROVED EXACT** |
| common-functor preservation | **IMPORTED PROVED FORMALLY** |
| source-independent bounded/subpower externalization | **REFUTED FOR THE UNIVERSAL PHASE/INCIDENCE KERNEL** |
| subpower occupancy of the actual native residue image | **OPEN / NOT CLAIMED** |
| common full native relative complex | **NOT CONSTRUCTED** |
| uniform Betti or signed trace estimate | **NOT PROVED** |
| CYSEL, WCADD, WCKUM, RH, or GRH | **NOT PROVED** |

## 9. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_native_partial_frobenius_verdict.py --check
python -B -O research/l-families/atlas/function_field/ffps_native_partial_frobenius_verdict.py --check
python -B -m unittest tests.test_ffps_native_partial_frobenius_verdict
python -B -O -m unittest tests.test_ffps_native_partial_frobenius_verdict
python -B -m ruff check research/l-families/atlas/function_field/ffps_native_partial_frobenius_verdict.py tests/test_ffps_native_partial_frobenius_verdict.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_native_partial_frobenius_verdict.py tests/test_ffps_native_partial_frobenius_verdict.py
~~~

The largest replayed matrix has dimension \(24\). No finite-field elements,
places, polynomials, point counts, curves, \(L\)-functions, or zeros are
enumerated.
