# FFPS relative boundary trace-tower gate

Status: **exact fixed-divisor trace theorem and exact rational
universal-incidence representation theorem; no native varying-place FFPS
adapter or scalable cohomological estimate**

## 0. Verdict

The observation

\[
 B_D(1)=0
 \qquad
 \text{when every closed place in }D\text{ has degree }>1
\]

has **two different meanings**, depending on whether the selected divisor is
kept fixed or is selected by a Frobenius-cycle projector in a universal
family.

1. **Fixed divisor.**  At the single base field, extension by zero and middle
   extension have exactly the same numerical Frobenius trace.  This is a real
   base-field shadow identity and survives any additive pushforward for which
   the boundary has no rational point in the relevant rational fibres.  It is
   not an equality of sheaves and not an equality over the fixed-divisor
   extension tower.  The full tower recovers the divisor degree profile by
   Möbius inversion, so a Deligne bound applied to the zero-extended sheaf
   still sees `deg(D)`.

2. **Universal irreducible-place selection.**  On the squarefree degree-`d`
   polynomial configuration space there is an exact rational virtual
   selector

   \[
    \mathcal Q_d={1\over d}\Lambda_{-1}(\mathrm{Std}_d)
   \]

   whose Frobenius trace is one exactly on `d`-cycles.  If
   \(\mathcal P_d\) is the universal-root permutation local system, then for
   every \(d>1\)

   \[
    \boxed{[\mathcal P_d\otimes\mathcal Q_d]=0}
    \quad\text{in}\quad
    K_0(\operatorname{Loc})\otimes\mathbf Q.
   \]

   Thus an irreducibility selector annihilates the **universal root-incidence
   boundary** before every additive pushforward.  This is stronger than the
   accidental equality at `m=1`.

The second statement is a genuine formal escape from the root-boundary tax,
but it is not yet an FFPS source theorem.  Irreducibility is a Frobenius
conjugacy condition, not a natural base-change-stable Zariski-open
subfunctor; the displayed selector is signed and virtual; its elementary
exterior-power presentation has absolute
generic-rank mass

\[
 {1\over d}\sum_{k=0}^{d-1}\binom{d-1}{k}
 ={2^{d-1}\over d};
\]

and no universal owner/core/Boolean FFPS pushforward carrying this factor has
been constructed.  The boundary cost can disappear while the
irreducible-place projector cost remains large or worse.

The successor packet `FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md` closes the
rank-optimization question inside the exact full-`S_d`, characteristic-zero
semisimple category.  Character orthogonality and Murnaghan--Nakayama make
the hook expansion unique, so the mass `2^(d-1)/d` is forced, with equal
positive and negative halves for `d>1`.  This does not rule out joint
`K_0` cancellation, a weaker source-specific selector, or different
geometry.

This packet therefore adds a third row to the earlier ledger:

| realization | boundary trace | geometric status | cost verdict |
|---|---|---|---|
| fixed `j_!`, all extensions | `B_D(m)` | honest zero extension | `deg(D)` remains |
| fixed `j_!`, base field only | `B_D(1)=0` if `D(F_q)=empty` | numerical trace shadow | middle trace may be substituted for that one sum |
| universal root incidence times exact cycle selector | identically zero in rational `K_0` | signed virtual family identity | root boundary vanishes; selector/source complexity remains open |

None of these statements proves `CYSEL`, `WCADD`, `WCKUM`, principal
individualization, RH, or GRH.

The sole FFPS input imported from
[`FFPS_RELATIVE_BRANCH_CANCELLATION_LEDGER.md`](FFPS_RELATIVE_BRANCH_CANCELLATION_LEDGER.md)
is the fixed-clean-torsor identity for the **unnormalized** relative object

\[
 C-S=E_U.
\]

The normalized selected average and atom-free covariance have different
local representation classes and are not covered by this packet.

## 1. Fixed reduced divisor

Let \(X/\mathbf F_q\) be a smooth proper curve, let

\[
 i:D\hookrightarrow X,
 \qquad
 j:U=X-D\hookrightarrow X
\]

with \(D\) a nonempty reduced finite divisor, and use the constant
\(\ell\)-adic sheaf \(E\).  The localization triangle is

\[
 j_!E_U\longrightarrow E_X\longrightarrow i_*E_D\longrightarrow.
\tag{1.1}
\]

Write \(N_d\) for the number of degree-`d` closed places in \(D\).  Applying
compactly supported cohomology and the Grothendieck trace formula gives, for
every \(m\geq1\),

\[
 T_!(m)=T_{\mathrm{mid}}(m)-B_D(m),
 \qquad
 B_D(m)=\#D(\mathbf F_{q^m})
 =\sum_{d\mid m}dN_d.
\tag{1.2}
\]

This is the trace-level form of the exact class

\[
 [j_!E_U]=[E_X]-[i_*E_D].
\]

### The base-field shadow

Equation (1.2) immediately proves

\[
 \boxed{
 N_1=0
 \quad\Longrightarrow\quad
 T_!(1)=T_{\mathrm{mid}}(1).}
\tag{1.3}
\]

For a statistic that literally asks for only this one \(\mathbf F_q\)-trace,
(1.3) permits an exact numerical substitution: prove the estimate for the
middle-extended trace and transfer the resulting number back to the native
zero-extended sum.  One must not first apply a conductor bound to
\(j_!E_U\); that throws away the exact zero in (1.3).

This is a legitimate but very narrow escape.  It says nothing about the
equality of the two sheaves.

### The fixed-tower no-go

The divisor profile is recovered from its trace tower:

\[
 \boxed{
 dN_d=\sum_{e\mid d}\mu(d/e)B_D(e).}
\tag{1.4}
\]

Consequently, for an effective reduced divisor,

\[
 B_D(m)=0\ \text{for every }m
 \quad\Longleftrightarrow\quad
 D=\varnothing.
\tag{1.5}
\]

Equivalently, one degree-`d` place contributes the permutation Frobenius
module

\[
 \operatorname{Ind}_{G_{\mathbf F_{q^d}}}^{G_{\mathbf F_q}}\mathbf 1,
 \qquad
 \det(1-TF)=1-T^d,
\tag{1.6}
\]

whose `m`-th power trace is zero unless `d|m`, and is `d` when `d|m`.
The zero at `m=1` is cancellation among the eigenvalues of a `d`-cycle, not
absence of a `d`-dimensional boundary module.

For a signed virtual divisor, the full tower can vanish through exact
cancellation of equal-degree multiplicities.  Merely knowing `B_D(1)=0`
does not establish such a cancellation.

## 2. What additive pushforward preserves

Let \(f:X\to Y\) be a separated finite-type family map and suppose the
boundary is finite over the relevant base.  Applying \(Rf_!\) to (1.1) gives

\[
 [Rf_!j_!E_U]
 =[Rf_!E_X]-[R(f\circ i)_!E_D].
\tag{2.1}
\]

At \(y\in Y(\mathbf F_{q^m})\), proper base change and the trace formula give

\[
 t_{Rf_!j_!E_U,m}(y)
 =t_{Rf_!E_X,m}(y)
 -\#D_y(\mathbf F_{q^m}).
\tag{2.2}
\]

The same statement holds with Frobenius weights for a constructible boundary
coefficient system; an empty rational fibre contributes no term.

Therefore:

* if every rational fibre \(D_y\), for \(y\in Y(\mathbf F_q)\), has no
  \(\mathbf F_q\)-point, the two trace functions agree pointwise on
  \(Y(\mathbf F_q)\);
* the equality remains true after any further additive pushforward and
  summation over \(Y(\mathbf F_q)\);
* the complexes in (2.1) need not be isomorphic, and the equality generally
  fails on \(Y(\mathbf F_{q^m})\) for a fixed boundary when an extension
  degree meets one of its place degrees.

Thus additive pushforward preserves the **base trace shadow** under an
explicit rational-fibre hypothesis.  It does not turn that shadow into a
geometric equality.

## 3. Universal root incidence and irreducibility

Let \(\operatorname{Conf}_d\) be the squarefree locus in the affine space of
monic degree-`d` polynomials.  Its ordered-root cover is an
\(S_d\)-torsor, and the universal root incidence

\[
 \pi_d:Z_d\longrightarrow\operatorname{Conf}_d
\]

is finite etale of degree `d`.  Let

\[
 \mathcal P_d=(\pi_d)_*E
\]

be its permutation local system and let
\(\mathrm{Std}_d\) be the rank-`d-1` augmentation representation, so that

\[
 \mathcal P_d=E\oplus\mathrm{Std}_d.
\]

At a rational polynomial \(P\), Frobenius permutes the geometric roots.  Its
cycle lengths are exactly the degrees of the irreducible factors of \(P\).
In particular:

* \(P\) is irreducible exactly when Frobenius is a `d`-cycle;
* the trace of \(\mathcal P_d\) is the number of Frobenius-fixed roots, hence
  the number of linear factors.

Irreducibility is therefore not a natural base-change-stable Zariski-open
subfunctor of coefficient space: a polynomial irreducible over one residue
field can split after extension.  It is represented here by a Frobenius
conjugacy-class selector on this finite etale cover.

## 4. Exact exterior-cycle selector

In the rational representation ring of \(S_d\), define

\[
 \boxed{
 \mathcal Q_d
 ={1\over d}\sum_{k=0}^{d-1}(-1)^k
 \bigwedge^k\mathrm{Std}_d
 ={1\over d}\Lambda_{-1}(\mathrm{Std}_d).}
\tag{4.1}
\]

### Theorem 4.1: cycle indicator

For every \(\sigma\in S_d\),

\[
 \operatorname{tr}(\sigma\mid\mathcal Q_d)
 =\begin{cases}
 1,&\sigma\text{ is a }d\text{-cycle},\\
 0,&\text{otherwise}.
 \end{cases}
\tag{4.2}
\]

**Proof.**  The alternating exterior character is

\[
 \sum_k(-1)^k\operatorname{tr}
 (\sigma\mid\bigwedge^k\mathrm{Std}_d)
 =\det(1-\sigma\mid\mathrm{Std}_d).
\tag{4.3}
\]

If \(\sigma\) has `c>1` cycles, its fixed subspace on
\(\mathrm{Std}_d\) has dimension `c-1`, so (4.3) is zero.  If \(\sigma\)
is a `d`-cycle, the eigenvalues on \(\mathrm{Std}_d\) are the nontrivial
`d`-th roots of unity and

\[
 \det(1-\sigma\mid\mathrm{Std}_d)
 =\prod_{\zeta^d=1,\ \zeta\ne1}(1-\zeta)=d.
\]

Dividing by `d` proves (4.2).  \(\square\)

The familiar hook-character expansion of the `d`-cycle indicator is a
consequence of (4.1), but no character table is needed for the proof.

### Theorem 4.2: universal incidence annihilation

For every \(d>1\),

\[
 \boxed{
 [\mathcal P_d\otimes\mathcal Q_d]=0
 \quad\text{in}\quad R(S_d)\otimes\mathbf Q.}
\tag{4.4}
\]

**Proof.**  The character of \(\mathcal P_d\) is the number of fixed letters.
If \(\sigma\) is a `d`-cycle and `d>1`, it has no fixed letter.  If it is not
a `d`-cycle, (4.2) vanishes.  Hence the product character is zero on every
conjugacy class.  Finite-group representations over characteristic zero are
semisimple and their characters inject the rational representation ring into
class functions, proving (4.4).  \(\square\)

This is an identity of rational virtual local-system classes on
\(\operatorname{Conf}_d\), not merely equality of their `F_q` trace sums.
Every additive derived pushforward preserves (4.4).

## 5. Several selected places

For ordered degrees \(d_1,\ldots,d_r>1\), work first on the product of the
squarefree configuration spaces and restrict to any required disjoint-root
locus.  Put

\[
 \mathcal Q=\boxtimes_{a=1}^r\mathcal Q_{d_a},
 \qquad
 \mathcal B=\bigoplus_{a=1}^r\mathcal P_{d_a}.
\]

Distributivity and (4.4) give

\[
 \boxed{[\mathcal B\otimes\mathcal Q]=0.}
\tag{5.1}
\]

Restriction to a collision-free open, quotient pushforward for unordered
blocks, and any subsequent additive pushforward preserve this zero class.
Thus the union of universal geometric root divisors is annihilated by the
product irreducibility selector.

The same **pointwise Frobenius-trace annihilation** extends to a coefficient
system on the universal root incidence, provided the selector tensors from
the parameter base: at a `d`-cycle there is no fixed root on which a local
Frobenius weight could be evaluated, while away from the `d`-cycle class the
selector vanishes.  Promoting this observation to a `K_0` identity requires
the corresponding constructible pushforward and factorization to have
actually been built.  What it does **not** cover is a boundary object already
collapsed to one rank-one stalk per closed orbit on the parameter base.  That
object need not have the universal-root permutation character.

This root-incidence versus closed-orbit distinction must be fixed by the
native FFPS source adapter.

## 6. Why this does not contradict the fixed-divisor tower

Fix an irreducible polynomial \(P\) of degree `d` over \(\mathbf F_q\), with
root permutation \(\sigma\) a `d`-cycle.

* Keeping the corresponding closed divisor with constant coefficient one
  gives the power traces

  \[
   \operatorname{tr}(\sigma^m\mid\mathcal P_d)
   =\begin{cases}d,&d\mid m,\\0,&d\nmid m.\end{cases}
  \]

* The universal selected incidence gives

  \[
   \operatorname{tr}(\sigma^m\mid
   \mathcal P_d\otimes\mathcal Q_d)=0
   \qquad\text{for every }m.
  \]

When `d|m`, the roots become fixed but
\(\operatorname{tr}(\sigma^m\mid\mathcal Q_d)=0\); the base-changed selector
is now asking whether the polynomial is irreducible over the enlarged
residue field.  It does not retain weight one on the original
\(\mathbf F_q\)-closed place.

Hence:

\[
 \boxed{
 \text{universal re-selection over residue fields}
 \ne
 \text{the constant-weight tower of a fixed closed place}.}
\tag{6.1}
\]

Any Euler-product or fixed-compatible-system argument must specify which
tower it requires.

## 7. Where Deligne pays

There are now three precise cases.

### 7.1 Apply Deligne directly to fixed `j_!`

The singular boundary has geometric length `deg(D)`.  The
Grothendieck--Ogg--Shafarevich/Euler-characteristic ledger therefore retains
that contribution even if its first Frobenius trace happens to be zero.
Deligne controls eigenvalues on cohomology; it does not delete a nonzero
permutation module because one power sum vanished.

### 7.2 Transfer one base-field number to the middle trace

If (1.3), or its fibrewise version in Section 2, is proved for the literal
source sum, one may apply Deligne to the middle-extended replacement and
transfer the resulting **single numerical estimate** back.  This avoids the
fixed boundary conductor for that one sum.  It supplies no compatible tower
and no varying-place adapter by itself.

### 7.3 Tensor a universal incidence with the cycle selector

Here the boundary alternating-trace/`K_0` contribution vanishes exactly by
(4.4), so it needs no separate bound after the signed class is assembled.
A virtual class itself has no honest positive conductor; applying Deligne
termwise before the exact assembly would reintroduce the constituent mass.
The surviving cost moves into the selection mechanism:

\[
 \sum_{k=0}^{d-1}{1\over d}
 \dim\bigwedge^k\mathrm{Std}_d
 ={2^{d-1}\over d}.
\tag{7.1}
\]

Equation (7.1) is the absolute generic-rank mass of the elementary signed
presentation.  The successor mass no-go proves that it is also optimal among
all exact presentations in `R(S_d) tensor Q`: the `d`-cycle indicator has
unique hook coefficients `(-1)^k/d`.  The discriminant boundary of
\(\operatorname{Conf}_d\), growing base dimension, distinctness conditions,
and every FFPS owner/core cleanup still remain to be costed.  A cheaper
source-specific, approximate, jointly cancelled, or non-semisimple geometric
mechanism is not excluded.

Thus the exact root-boundary cancellation does **not** establish overall
`theta=0` for the varying-place source.

## 8. Source and positivity firewalls

The exact theorems above do not license any of the following substitutions
without a new adapter theorem.

1. **Hard set versus virtual selector.**  \(\mathcal Q_d\) is a rational
   signed class in `K_0`, not an honest positive subfamily.  It is valid for a
   signed trace recombination; it cannot be inserted after an absolute value
   or positivity step.
2. **Irreducibility is arithmetic.**  There is no claimed natural,
   base-change-stable Zariski-open `irreducible polynomial locus`.  The full
   squarefree configuration and its Frobenius class selector are essential.
3. **Root incidence versus orbit atom.**  The annihilated boundary is the
   universal geometric-root cover.  A source that records one closed place
   as one already-descended atom may carry a different trace module.
4. **Normalization.**  The exact indicator requires the factor `1/d`.
   Multiplying by `d` gives an integral virtual representation but also
   multiplies the source trace.  Owner and automorphism normalizations must
   be checked explicitly.
5. **Factorization through cleanup.**  The proof needs the cycle selector to
   tensor with the boundary incidence before diagonal, owner, Wick, and
   conductor recombinations.  It is open whether the native FFPS pipeline
   has this common equivariant factorization.
6. **Bounds for the surviving main object.**  Killing the boundary does not
   bound the middle object twisted by all selectors, nor does it remove
   geometrically constant constituents of that object.

## 9. Proof ledger

| statement | grade |
|---|---|
| fixed-divisor formula (1.2) | **PROVED EXACT** from localization and the trace formula |
| base-field shadow (1.3) | **PROVED EXACT FOR A FIXED REDUCED DIVISOR** |
| Möbius tower recovery (1.4) | **PROVED EXACT** |
| fibrewise pushforward criterion (2.2) | **PROVED EXACT UNDER THE STATED FINITENESS/RATIONAL-FIBRE HYPOTHESIS** |
| exterior `d`-cycle selector (4.2) | **PROVED EXACT FINITE REPRESENTATION ALGEBRA** |
| universal-root annihilation (4.4) | **PROVED EXACT IN RATIONAL `K_0`** |
| multi-place universal boundary cancellation (5.1) | **PROVED EXACT ON THE ORDERED PRODUCT/DISJOINT LOCUS** |
| cancellation after arbitrary additive pushforward | **PROVED FORMALLY FOR THE SAME RATIONAL `K_0` CLASS** |
| identification of the native FFPS boundary with that universal root-incidence class | **OPEN / NOT CONSTRUCTED** |
| cheaper exact full-`S_d` semisimple selector | **RULED OUT BY THE SUCCESSOR MASS NO-GO; (7.1) IS OPTIMAL** |
| source-specific, approximate, or jointly cancelled selector | **OPEN** |
| uniform Betti/conductor bound for the surviving FFPS complex | **OPEN** |
| `CYSEL`, `WCADD`, `WCKUM`, principal individualization, RH, or GRH | **NOT PROVED** |

## 10. Source and novelty boundary

The localization/trace formalism used in Sections 1--2 is standard; a
primary source is SGA 4 1/2, Expose II,
[Trace formula and L-functions](https://grothendiecksga.com/read/sga4.5/en/II_3.html).
Finite etale pushforward preserving local constancy is also recorded in the
[Stacks Project, Tag 095B](https://stacks.math.columbia.edu/tag/095B).
The weight bounds relevant after an actual complex is constructed are
Deligne's
[Weil II](https://publications.ias.edu/book/export/html/386).

No external novelty is claimed for the elementary identity
\(d^{-1}\Lambda_{-1}(\mathrm{Std}_d)=1_{(d)}\) or its zero product with the
permutation character.  The project-specific contribution is the audit:
it separates the fixed-divisor base shadow, the fixed-tower no-go, and the
universal irreducibility-selector cancellation, then identifies exactly
which source and complexity gates still prevent an FFPS theorem.

## 11. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_relative_boundary_trace_tower_gate.py --check
python -B -O research/l-families/atlas/function_field/ffps_relative_boundary_trace_tower_gate.py --check
python -B -m unittest tests.test_ffps_relative_boundary_trace_tower_gate
python -B -O -m unittest tests.test_ffps_relative_boundary_trace_tower_gate
python -B -m ruff check research/l-families/atlas/function_field/ffps_relative_boundary_trace_tower_gate.py tests/test_ffps_relative_boundary_trace_tower_gate.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_relative_boundary_trace_tower_gate.py tests/test_ffps_relative_boundary_trace_tower_gate.py
```

The replay checks all 66 integer cycle types through degree eight, the exact
exterior selector, universal-incidence annihilation, one fixed-divisor trace
tower, Möbius recovery, and the raw selector rank mass.  It enumerates no
finite-field point, closed place, polynomial, curve, sheaf, source atom,
`L`-function, or zero.
