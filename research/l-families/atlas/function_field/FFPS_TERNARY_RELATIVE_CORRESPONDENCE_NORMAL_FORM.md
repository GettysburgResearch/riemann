# Ternary relative source and Frobenius-correspondence normal form

Status: **exact pre-externalization ternary relative kernel, exact clean-sector
occupancy and native rank theorem, and exact Frobenius-graph shift normal
form; no complete owner/Boolean source complex, independent partial
Frobenius, native closed-point Adams theorem, uniform trace estimate, CYSEL,
RH, or GRH theorem**

Bounded exact replay:
[ffps_ternary_relative_correspondence_normal_form.py](ffps_ternary_relative_correspondence_normal_form.py).
Canonical summary:
[ffps_ternary_relative_correspondence_normal_form.json](ffps_ternary_relative_correspondence_normal_form.json).

Frozen dependencies:

| source | commit | git blob | role |
|---|---|---|---|
| `FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md` | `e39031369` | `19939eb240ca6b2b6d5221954cec76fe0f5c4f9c` | universal native rank and partial-Frobenius obstruction |
| `FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md` | `9ced25bef` | `21645bdb609320cf176893aa589af7a17c741d9a` | ranks 48/32/16 of the clean norm/Kummer package |
| `FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md` | `464c3705f` | `ab16e6c0894e51303119692e67b2f2bf59ba73e4` | honest C − S = Π₀ endomorphism |
| `FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md` | `05da4d170` | `c79e52ebf0099fe416bc2c79dcb041cc21e025fb` | exact separable/partial-Frobenius acceptance criterion |
| `FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md` | `1242951f9` | `9012f96b34a3ffe55b66282ba1e62bc02514b5c6` | physical ternary source and centered identity |
| `FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md` | `271ff4316` | `6c63def72b340f69be9caff41a619f23d2b66fd1` | all-k hard/selected kernels |
| `L-106191` | `98af0db6e` | `85c4ef92ead7d8b235f9c195c3c0acd16d16030f` | native centered double-incidence coordinate |

## 0. Outcome

This packet answers the narrow question left open by the native
partial-Frobenius verdict:

> Does the actual ternary hard-minus-selected cancellation lower the native
> phase/incidence rank if it is performed before externalization?

On the clean complete physical sector, the answer is **no**. The subtraction
does remove the two faithful cubic deck modes, exactly as it should, but it
leaves the principal native phase/incidence kernel coefficientwise.

Let \(Q_1,Q_2\equiv1\pmod6\), put

\[
 m_i={Q_i-1\over2},\qquad M=m_1m_2,
\tag{0.1}
\]

and use the literal physical coordinates

\[
 X=Pc^2,\qquad Y=Qd^2.
\tag{0.2}
\]

The bilateral ternary character \(\Phi(X,Y)\) has three fibres, each of
cardinality \(M/3\). Every rotated two-class hard mask contains \(2M/3\)
cells. Nevertheless, after the three rotations are assembled at covariance
level, the hard, selected, and relative pair kernels are nonzero on all
\(M^2\) ordered cell pairs.

If \(B\) is the native bilateral additive Gram, then the common native lift
of the hard and selected kernels satisfies

\[
 \boxed{B_C-B_S=B.}
\tag{0.3}
\]

Moreover,

\[
 \boxed{
 \operatorname{rank}B_C
 =\operatorname{rank}B_S
 =\operatorname{rank}(B_C-B_S)
 =M.}
\tag{0.4}
\]

Literal Wick deletion does not help. If \((\cdot)^\circ\) deletes the atomic
diagonal, then

\[
 \boxed{B_C^\circ-B_S^\circ=B^\circ,
 \qquad \operatorname{rank}B^\circ=M.}
\tag{0.5}
\]

Thus cancellation before externalization does not create a bounded-rank or
subpower-rank native kernel on the complete clean sector. This is stronger
than the earlier termwise universal no-go and narrower than a no-go for the
complete FFPS source: the live Boolean/owner image may occupy fewer cells,
and no lower bound for that image is proved here.

There is also a positive categorical normal form. The surviving centered
incidence class

\[
 H_0=[\Delta]-Q^{-1}[J]
\tag{0.6}
\]

does not have independent partial Frobenius. Its successive partial pullbacks
are

\[
 H_n=[\Gamma_n]-Q^{-1}[J],\qquad
 \Gamma_n:\ y=x^{Q^n}.
\tag{0.7}
\]

The \(H_n\) are linearly independent. Hence there is no finite-dimensional
partial-Frobenius closure. But they form one free generator over the shift
ring:

\[
 \boxed{E[T]H_0\simeq E[T],\qquad TH_n=H_{n+1}.}
\tag{0.8}
\]

Bilaterally, the relative incidence is one free
\(E[T_1,T_2]\)-generator. A finite divisor grid is therefore sparse in this
correspondence language even though it has full external separation rank.
This is a viable target category for a successor, not yet a closed-point
Adams formula.

## 1. The literal ternary source kernel before externalization

For the ternary two-point mask, choose \(S\subset\mu_3\) with \(|S|=2\).
For two source atoms write

\[
 g={\Phi(\omega_1)\over\Phi(\omega_2)}\in\mu_3.
\tag{1.1}
\]

The locked cyclic theorem gives

\[
 K_C(g)={3\over4}|S\cap gS|,
 \qquad
 K_S(g)=K_C(g)-1.
\tag{1.2}
\]

Because a two-subset of \(\mu_3\) meets itself in two points and either
nontrivial translate in one point,

\[
 \begin{array}{c|cc}
 &g=1&g\ne1\\ \hline
 K_C(g)&3/2&3/4\\
 K_S(g)&1/2&-1/4.
 \end{array}
\tag{1.3}
\]

Therefore

\[
 \boxed{K_C(g)-K_S(g)=1\quad(g\in\mu_3).}
\tag{1.4}
\]

This is the actual hard-minus-selected covariance kernel, before any
external-product expansion. It is the trace form of
\(\mathsf C-\mathsf S=\Pi_0\). Notice two facts which are easy to miss:

1. \(K_S\) is signed, but it is never zero.
2. \(K_C\) is also never zero, although any one hard amplitude mask deletes
   one of the three classes.

Thus the covariance assembly has already refilled the single-mask holes.
The leverage gain belongs to the individually restricted positive frame; it
does not imply sparse support for the signed relative covariance.

## 2. Exact clean-sector physical occupancy

The sign-pair quotient of \(\mathbf F_{Q_i}^{\times}\) is cyclic of order
\(m_i=(Q_i-1)/2\), divisible by three. An exact-order-three character is a
surjection onto \(\mu_3\), so every fibre has size \(m_i/3\).

For either relative alignment

\[
 \Phi(x,y)=\epsilon_1(x)\epsilon_2(y)^{\pm1},
\tag{2.1}
\]

fixing \(x\) and a target value leaves exactly \(m_2/3\) choices of \(y\).
Hence each \(\Phi\)-class has size

\[
 \boxed{|\Phi^{-1}(a)|={M\over3}.}
\tag{2.2}
\]

Every rotated two-class hard support therefore has

\[
 \boxed{|A_j|={2M\over3}.}
\tag{2.3}
\]

The native additive Gram is positive definite on the complete sign-pair
product, so its restriction to every \(A_j\) has exact rank \(2M/3\).
After covariance assembly, however, (1.3) shows that \(K_C,K_S\), and
\(K_C-K_S\) all have pair support \(M^2\).

This is an occupancy theorem for the **clean complete physical sector** in
the norm/Kummer package. It is not an occupancy theorem for the final live
FFPS image after roughness, Boolean, owner, shell, and renewal restrictions.
If that source occupies only \(s\) distinct physical cells, the corresponding
pullback rank question is an \(s\)-cell question. No lower bound for \(s\) is
imported or inferred here.

## 3. The common native phase lift

On one sign-pair side define

\[
 B_i=Q_iI_{m_i}-J_{m_i}.
\tag{3.1}
\]

Its eigenvalues are \(Q_i\) on the sum-zero space and
\((Q_i+1)/2\) on the constant line. Thus \(B_i\) is positive definite. The
bilateral native Gram is

\[
 B=B_1\otimes B_2,
\tag{3.2}
\]

and has rank \(M\).

Let \(v=(\Phi(\omega))_{\omega}\). In matrix form the selected ternary
kernel is

\[
 K_S={1\over4}(vv^*+\bar v\bar v^*),
\tag{3.3}
\]

while

\[
 K_C=J+K_S.
\tag{3.4}
\]

For a common native phase/incidence lift, multiplication of pair trace
functions is Hadamard product. Put

\[
 B_S=B\circ K_S,
 \qquad B_C=B\circ K_C.
\tag{3.5}
\]

Equation (1.4) immediately proves (0.3). More explicitly, with
\(D=\operatorname{diag}(v)\),

\[
 B_S={1\over4}(DBD^*+\bar D B\bar D^*).
\tag{3.6}
\]

Both summands are positive definite, so \(B_S\) is positive definite.
Also \(B_C=B+B_S\) is positive definite. This proves (0.4) for every
eligible \(Q_1,Q_2\), not merely for the replayed \((7,7)\) and \((7,13)\)
panels.

This theorem has a precise interpretation. The finite deck ranks

\[
 \operatorname{rank}K_C=3,\qquad
 \operatorname{rank}K_S=2,\qquad
 \operatorname{rank}(K_C-K_S)=1
\tag{3.7}
\]

do not control external separation after native coupling:

\[
 \operatorname{rank}(B\circ K_C)
 =\operatorname{rank}(B\circ K_S)
 =\operatorname{rank}B=M.
\tag{3.8}
\]

The clean torsor ranks \(48/32/16\) remain correct object ranks in their own
finite deck category. Equation (3.8) says that coupling those modes to the
native physical phase variables restores full physical separation rank.
Those are different notions of rank.

There is an exact source-image version. Let a finite atom set map to the
clean physical cells and let \(s\) be the number of distinct occupied cells.
If \(R\) is its zero-one incidence matrix, the pulled-back kernel is
\(R^*B_\bullet R\), where \(\bullet\) is hard, selected, or relative. Each
\(B_\bullet\) is positive definite and \(R\) has row rank \(s\), so

\[
 \boxed{\operatorname{rank}(R^*B_\bullet R)=s.}
\tag{3.9}
\]

Thus, before literal-atom deletion, the native relative rank is **exactly the
physical occupancy**. Ternary signed cancellation supplies no additional rank
saving. This does not estimate \(s\) for the final live Boolean/owner source;
it converts that missing occupancy theorem into the precise remaining
quantity.

## 4. Literal Wick deletion still leaves full rank

Deleting the common literal atomic diagonal is linear, so (0.3) gives

\[
 B_C^\circ-B_S^\circ=B^\circ.
\tag{4.1}
\]

On the clean one-cell-per-label panel, the diagonal of \(B\) is the constant

\[
 d=(Q_1-1)(Q_2-1),
\tag{4.2}
\]

and therefore \(B^\circ=B-dI\). Put \(a=Q_1,b=Q_2\). Its four eigenvalues,
according to constant/sum-zero type on the two factors, are

\[
 \begin{aligned}
 E_{00}&={-3ab+5a+5b-3\over4}
 ={16-(3a-5)(3b-5)\over12},\\
 E_{10}&={-ab+3a+2b-2\over2}
 ={4-(a-2)(b-3)\over2},\\
 E_{01}&={-ab+2a+3b-2\over2}
 ={4-(a-3)(b-2)\over2},\\
 E_{11}&=a+b-1.
 \end{aligned}
\tag{4.3}
\]

For \(a,b\ge7\), the first three are strictly negative and the last is
strictly positive. None vanishes. This proves (0.5).

For a source with several atoms in one physical cell, literal Wick deletion
acts on atom labels rather than cell labels. The present rank proof is not
silently promoted to that arbitrary pullback. However, any two disjoint
labelled copies retaining the full physical cross-block contain \(B\) as a
full-rank off-atomic block. A genuinely sparse or specially weighted live
source remains a separate occupancy problem.

## 5. Why partial Frobenius is still absent

On one residue-incidence plane, write

\[
 H_0=[\Delta]-Q^{-1}[J],
 \qquad \Delta:\ y=x.
\tag{5.1}
\]

The cyclic relative subtraction leaves precisely the principal deck line
tensor this native class. Pulling in the \(x\)-coordinate by the \(n\)-th
power of \(Q\)-Frobenius gives

\[
 H_n=[\Gamma_n]-Q^{-1}[J],
 \qquad \Gamma_n:\ y=x^{Q^n}.
\tag{5.2}
\]

For \(n>0\), \(\Gamma_n\ne\Delta\). Hence \(H_0\) is not isomorphic to its
partial Frobenius pullback. The projector \(\Pi_0\) cannot repair this:
its image is the constant deck line, so it contributes no compensating
support.

The same conclusion holds for the Artin--Schreier line before squaring by
the locked coboundary-degree argument. Relative cyclic cancellation removes
the cubic Kummer obstruction; it does not create independent Frobenius on
the remaining native source.

## 6. Exact Frobenius-graph shift module

The lack of an isomorphism does not force a \(Q\)-term external expansion.
Keep the graphs as correspondences.

The curves \(\Gamma_n\) are distinct irreducible closed supports. For any
finite linear relation among \(H_0,\ldots,H_N\), first take the generic stalk
off every graph and then at the generic point of each \(\Gamma_n\). The
resulting triangular system forces every coefficient to vanish. Therefore

\[
 \boxed{\dim_E\langle H_0,\ldots,H_N\rangle=N+1.}
\tag{6.1}
\]

If \(T\) denotes partial Frobenius pullback on support classes, then
\(TH_n=H_{n+1}\). Consequently

\[
 \boxed{E[T]H_0\text{ is free of rank one over }E[T].}
\tag{6.2}
\]

This has two complementary consequences.

1. No finite-dimensional \(E\)-space containing \(H_0\) is stable under all
   partial Frobenius powers. A bounded finite list of graph correspondences
   cannot restore the separable Adams hypothesis.
2. The whole tower has one generator over the shift semigroup. It is a
   compressed exact correspondence representation, not a \(Q\)-rank Fourier
   decomposition.

Bilaterally, the unique top support of
\(T_1^rT_2^s(H_0\boxtimes H_0)\) is
\(\Gamma_r\times\Gamma_s\). The same generic-support argument gives

\[
 \boxed{
 E[T_1,T_2](H_0\boxtimes H_0)
 \simeq E[T_1,T_2].}
\tag{6.3}
\]

This is the promised correspondence-level normal form.

Here \(Q^{-1}\) is the fixed-residue-field scalar in the trace kernel. In a
varying-degree Weil realization it must be represented by the appropriate
Tate eigenvalue. Adams powering then also powers that eigenvalue. The support
module above deliberately records the graph geometry only; it does not erase
the separate Tate/Frobenius-scalar ledger.

## 7. Sparse formal divisor grids, and the exact firewall

For a positive integer \(a\), form the sparse shift polynomial

\[
 M_a(T)=\sum_{e\mid a}\mu(e)T^e.
\tag{7.1}
\]

It has exactly \(2^{\omega(a)}\) nonzero terms. Therefore

\[
 M_a(T_1)M_b(T_2)(H_0\boxtimes H_0)
\tag{7.2}
\]

has \(2^{\omega(a)+\omega(b)}\) distinct top graph products. If \(a,b>1\),
then \(M_a(1)=M_b(1)=0\), so every constant-background and one-axis support
term cancels formally; only the top graph products remain.

This looks like the divisor tax in closed-point Adams compression, but it is
not yet that theorem. Formula (7.2) records how a **hypothetical** independent
power request would act in the graph-shift module. The actual Adams formula
also changes extension-field trace level and applies Adams operations to
stalk eigenvalues. No functor identifying those operations with (7.2) for the
native owner/Boolean complex is constructed here.

The safe conclusion is:

\[
 \boxed{
 \text{full separation rank }M
 \quad\text{coexists with}\quad
 \text{one-generator, divisor-sparse correspondence bookkeeping}.}
\tag{7.3}
\]

The next categorical target is a trace functor on this shift module which
realizes independent closed-point degree extraction and retains uniform
complexity after the native pushforwards. A proof would reopen Adams
compression in a new category. A proof that no such trace functor can obey
the required source compatibilities would close this escape.

## 8. What is closed and what remains open

This packet closes three tempting shortcuts.

1. **Single hard-mask sparsity does not survive covariance assembly.** The
   three rotated hard covariances and the selected covariance all have full
   pair support.
2. **Relative subtraction does not lower native phase/incidence rank.** It
   leaves the native principal kernel exactly.
3. **A finite graph list cannot supply partial Frobenius.** The graph orbit is
   linearly independent at every depth.

It does not close the following possibilities.

- The actual owner/Boolean source may occupy subpower-many physical cells.
- Source coefficients and cleanup cones may impose relations absent on the
  clean complete sector.
- The shift module may admit a useful correspondence trace theory despite
  its infinite coefficient-space dimension.
- Signed Möbius recombination across graph powers may cancel after the full
  source pushforward.
- A prime-polynomial explicit formula may bypass both separability and the
  coefficient-space cycle selector.

Most importantly, the complete common source stack carrying both hard and
selected native terms is still not constructed. Equations (0.3)--(0.5) are
the exact verdict for the natural **common native lift on the clean physical
sector**, not a declaration that every owner/core/Boolean cleanup has already
been transported.

## 9. Proof ledger

| statement | grade |
|---|---|
| ternary pre-externalization kernels (1.3)--(1.4) | **PROVED EXACT** |
| clean-sector class occupancy (2.2)--(2.3) | **PROVED EXACT ALL ELIGIBLE (Q_1,Q_2)** |
| full pair support of hard, selected, and relative covariances | **PROVED EXACT TERNARY** |
| common native identity (B_C-B_S=B) | **PROVED EXACT** |
| native ranks (0.4) | **PROVED BY POSITIVE-DEFINITE CONJUGATION** |
| source-image pullback rank (3.9) | **PROVED EXACT BEFORE LITERAL-ATOM DELETION** |
| Wick-relative rank (0.5) | **PROVED BY THE FOUR EIGENVALUE CHANNELS** |
| absence of partial Frobenius after relative subtraction | **PROVED BY DISTINCT GRAPH SUPPORT** |
| graph-orbit independence (6.1) | **PROVED BY GENERIC STALKS** |
| one-generator shift modules (6.2)--(6.3) | **CONSTRUCTED EXACTLY** |
| divisor-sparse formal shift ledger | **PROVED EXACT** |
| native closed-point Adams formula on the shift module | **NOT CONSTRUCTED** |
| live owner/Boolean physical occupancy lower bound | **OPEN / NOT CLAIMED** |
| complete native relative complex | **NOT CONSTRUCTED** |
| uniform Betti/conductor or trace estimate | **NOT PROVED** |
| `CYSEL`, `WCADD`, `WCKUM`, RH, or GRH | **NOT PROVED** |

## 10. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_ternary_relative_correspondence_normal_form.py --check
python -B -O research/l-families/atlas/function_field/ffps_ternary_relative_correspondence_normal_form.py --check
python -B -m unittest tests.test_ffps_ternary_relative_correspondence_normal_form
python -B -O -m unittest tests.test_ffps_ternary_relative_correspondence_normal_form
python -B -m ruff check research/l-families/atlas/function_field/ffps_ternary_relative_correspondence_normal_form.py tests/test_ffps_ternary_relative_correspondence_normal_form.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_ternary_relative_correspondence_normal_form.py tests/test_ffps_ternary_relative_correspondence_normal_form.py
```

The largest exact matrix has dimension \(18\). The replay checks only the
\((7,7)\) and \((7,13)\) rational Gram panels, graph signatures through depth
five, and three small divisor ledgers. It enumerates no finite-field element,
source atom, polynomial, closed place, point, curve, \(L\)-function, or zero.
