# Retain the source algebra: a diagonal adapter and Adams pushforward firewall

Status: **exact finite Frobenius-set adapter and counterexample; conditional
interface to the native source, not a native Weil realization or trace bound**.

Scope: finite source sets with an invertible Frobenius action and finite
coefficient spaces in characteristic zero.  All universal statements below
have algebraic proofs; bounded rank-one computations are regression controls.

Sources: the shared-fibre occupancy theorem at
`6675c19f20760301d8c91dedc4a7836170003512`, and the external-plus-diagonal
Adams and relative trace-tensor theorems at
`3a595dda92ef827a41e50d2395309692a93748ad`.  Exact paths and Git blobs are
locked in `source_algebra_diagonal_adams_adapter.sources.json`.

Smallest remaining gap: identify the **complete native** source algebra,
coefficient module, and Frobenius action uniformly in horizon, and prove
that the required operations and signed recombination descend.  Assigning
one rational point to every finite atom is not a uniform geometric theorem.

## 1. Outcome and relation to earlier work

The earlier fixed-fibre identity is

\[
 Q(z)=(Rz)^*S(Rz)-d\sum_x|z_x|^2.
\tag{1.1}
\]

The first term uses aggregated cells; the second uses literal source atoms.
This packet gives a canonical finite object that remembers the second term:
the source algebra `A=K^X`, together with the coefficient modules on which
its primitive idempotents act.  The diagonal is then tensoring **over `A`**,
not tensoring the aggregated vector spaces over `K`.

The distinction remains necessary even if one keeps the entire pushed
Frobenius module, rather than merely its first trace: two source objects
below have isomorphic pushed modules and identical traces of every power,
but different literal diagonals and different primitive degree-two data.

This sharpens the interface of #760's already-proved external-plus-diagonal
formalism.  It does not replace that theorem, add a partial-Frobenius
requirement to its diagonal channel, or promote its conditional source
realization to a theorem.

## 2. `DIAGALG-1`: a literal algebraic diagonal

Let `K` be a field of characteristic zero, `X` a finite set, and `sigma` a
permutation of `X`.  Write

\[
 A=K^X=\bigoplus_{x\in X}K e_x,
 \quad e_xe_y=\mathbf1_{x=y}e_x,\quad \sum_xe_x=1.
\]

The algebra automorphism induced by Frobenius sends `e_x` to `e_{sigma x}`.
Let `M=direct_sum_x V_x` and `N=direct_sum_x W_x` be finite `A`-modules,
equipped with invertible maps `F:V_x -> V_{sigma x}` and
`G:W_x -> W_{sigma x}`.  Thus `F(a m)=sigma(a)F(m)` and similarly for `G`.

The element

\[
 e_\Delta=\sum_{x\in X}e_x\otimes e_x\in A\otimes_K A
\tag{2.1}
\]

is an idempotent.  Acting on `M tensor_K N`, it selects the same-source
summands.  Multiplication induces a canonical identification

\[
 \boxed{e_\Delta(M\otimes_K N)
       \simeq M\otimes_A N
       \simeq\bigoplus_x V_x\otimes_K W_x.}
\tag{2.2}
\]

The mixed summands with `x!=y` vanish in the balanced tensor product because
`e_x e_y=0`; on the equal summand the two descriptions coincide.  This
proves (2.2) without choosing bases of the coefficient spaces.  Relabeling
`X` permutes the summands of (2.1), so the construction is source-natural.

Total Frobenius `F tensor G` preserves (2.1).  Its trace on the diagonal is

\[
 D_n=\sum_{\sigma^n x=x}
     \operatorname{tr}(F^n|V_x)\operatorname{tr}(G^n|W_x).
\tag{2.3}
\]

Terms on nonfixed source points move between summands and have zero trace.
In contrast the full tensor trace is

\[
 A_n(M)A_n(N),\qquad A_n(M)=\operatorname{tr}(F^n|M).
\tag{2.4}
\]

The decomposition into (2.2) and its complement is a literal splitting, so
normal ordering is a genuine difference of these trace channels.

For a split fibre at the trace level, set `z_x=tr(F|V_x)` and
`w_x=tr(G|W_x)`.  A cell map `r:X -> C` gives aggregate traces
`z_c=sum_{r(x)=c}z_x`.  Pulling back any prescribed scalar cell kernel
`S(c,c')` and subtracting `d e_Delta` gives exactly

\[
 \sum_{c,c'} S(c,c')z_cw_{c'}-d\sum_xz_xw_x.
\tag{2.5}
\]

This recovers (1.1) when the second coefficients are complex conjugates of
the first, with the factors put in the matching order.  An abstract dual
Weil module has inverse eigenvalues, **not automatically conjugate traces**;
no purity or unitarity premise is silently supplied.  A conjugate partner
must be separately specified if the Hermitian energy is intended.

For finite etale schemes over a finite field the underlying finite
Frobenius-set description is standard
([Stacks Project, Tag 04JI](https://stacks.math.columbia.edu/tag/04JI)).
Equations (2.1)--(2.3) are its explicit coefficient algebra.  No assertion
about a positive-dimensional native source space follows from this example.

## 3. `DIAGALG-2`: forgetting `A` loses more than a first moment

Consider two source objects over a point, with one-dimensional coefficients.

**Cycle source.** `X={0,1}`, `sigma` exchanges the points, and both transition
weights are one.  Take the same object for `M` and `N`.  The pushed map is

\[
 F_c=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

**Split source.** `X'={0,1}`, both points fixed, and the coefficient weights
are `+1,-1`.  Again use the same coefficients for `M` and `N`.  The pushed
map is

\[
 F_s=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

The matrix `P=[[1,1],[1,-1]]` has determinant `-2` and satisfies
`F_c P=P F_s`.  Thus the pushed Frobenius modules are isomorphic over `K`,
and for **every** `n>=1` their common trace is zero for odd `n` and two for
even `n`.  Their tensor-over-source-algebra diagonals are nevertheless

\[
 D_{c,n}=\begin{cases}0,&n\text{ odd},\\2,&n\text{ even},\end{cases}
 \qquad D_{s,n}=2\quad\text{for every }n.
\tag{3.1}
\]

Consequently no construction from the isomorphism class of the pair of
pushed modules alone can universally recover this source diagonal.  For a
single residue cell with `S(c,c)=d`, the two normal-ordered values at `n=1`
are `0` and `-2d`, despite identical aggregate modules and every-order
aggregate traces.  The counterexample is specified upstream by finite
source points and coefficient maps; no zero set or target `L`-function was
inserted.

The difference is in the retained algebras and their actions.  Frobenius on
`A_c` exchanges its idempotents; Frobenius on `A_s` fixes them.  The
intertwiner `P` does not identify these source-algebra structures.

## 4. `DIAGALG-3`: Adams must be applied before forgetting source orbits

For an orbit `O` of `sigma`, put `d_O=|O|` and let `T_O` denote `F^{d_O}`
on any one of its coefficient fibres, defined up to conjugacy.  Then

\[
 A_n(M)=\sum_{d_O\mid n}d_O\operatorname{tr}(T_O^{n/d_O}).
\tag{4.1}
\]

The source Adams class `psi_X^e` raises the eigenvalues of each local
monodromy `T_O` to their `e`-th powers.  At the trace level this gives

\[
 A_n(f_*\psi_X^e V)
 =\sum_{d_O\mid n}d_O\operatorname{tr}(T_O^{en/d_O}).
\tag{4.2}
\]

In contrast, applying Adams to the **already pushed** module gives

\[
 A_n(\psi^e(f_*V))
 =A_{ne}(M)
 =\sum_{d_O\mid ne}d_O\operatorname{tr}(T_O^{ne/d_O}).
\tag{4.3}
\]

The extra terms with `d_O|ne` but `d_O` not dividing `n` are an exact
orbit-creation defect.  Thus Adams does not in general commute with this
pushforward.  For the cycle source, `n=1,e=2` gives `0` in (4.2) and `2`
in (4.3).  The difference need not be nonzero for every coefficient object;
cancellation can occur.  The universal commutation assertion is what fails.

Define the primitive degree trace

\[
 P_d(V)=\sum_{d_O=d}\operatorname{tr}(T_O).
\]

The exact source-aware extraction is

\[
 \boxed{dP_d(V)=\sum_{e\mid d}\mu(e)
 A_{d/e}(f_*\psi_X^e V).}
\tag{4.4}
\]

Substitute (4.2); the coefficient for an orbit length `l|d` becomes
`l sum_{e|d/l} mu(e)`, leaving exactly the `l=d` term.  This is the
one-variable extractor used in #760, now with its source-before-pushforward
typing displayed.  No new Adams theorem is claimed.

If one incorrectly substitutes (4.3) into (4.4), every summand has the same
trace `A_d(M)` and the result is zero for every `d>1`.  This would erase all
nontrivial closed-point degrees.  In the counterfeit pair of Section 3,
`P_2` equals one for the cycle source and zero for the split source, while
the complete pushed trace sequences are identical.

The same source-aware extraction applies to the literal diagonal object
`V tensor W` on `X`.  Its local monodromy is `T_O tensor U_O`, not a
diagonal guessed after aggregation.  Combining it with the existing
two-place extractor yields the external-plus-diagonal normal-ordering
formula in the frozen #760 packet.

## 5. Partial Frobenius and the honest complexity boundary

The source diagonal is invariant under simultaneous source Frobenius.  If
all `V_x,W_x` are nonzero, it is invariant under `F tensor identity` only
when `sigma` fixes every source point: a same-point summand `(x,x)` moves
to `(sigma x,x)`.  The same holds for the other partial action.

This is **not a new obstruction to #760**.  That packet explicitly gives
the literal diagonal one ordinary Frobenius and one-variable Adams, beside
an external channel with its own partial-Frobenius requirements.  Demanding
partial Frobenii on their entire direct sum would reintroduce an already
avoided artificial requirement.  Nor are these two source-copy actions
automatically the native marked-place actions: their identification would
require a separate geometric theorem.

There is a precise rank cost to the proposed source-algebra carrier.  If a
cell contains `m` source points, its algebra is `K^m`.  Any faithful finite
module over this algebra has dimension at least `m`, since its `m`
orthogonal idempotents must each act on a nonzero summand.  Rank-one source
fibres attain equality.  Thus a uniform bound on the rank of this faithful
pushforward requires a uniform bound on cell multiplicity.

This is a bound on **faithful algebra-action carriers**, not on arbitrary
nonlinear sufficient statistics such as the scalar `D`.  Unbounded live
native multiplicity is not proved here.  Likewise a rank-one sheaf upstairs
can have growing pushforward rank; that observation alone supplies no
uniform conductor, Betti, or signed trace estimate.

## 6. What has and has not been advanced

Exact outputs are the canonical algebra-retained diagonal, the two-point
all-traces counterfeit, the explicit Adams/pushforward defect, and the
conditional faithful-module rank tax.  They give a more precise candidate
input for `DIAGREL` and a test that any claimed adapter must pass.

Still open are native atom-space realization, compatible marked-place
partial Frobenii on the external channel, all source cleanup/gluing,
uniform signed conductor recombination and trace bounds, and the required
principal-source estimates.  The earlier labeled identity `P=A-K=C-S`
remains a valid extraction route if its bounds are proved; no new
family-binding axiom is imposed on it.

The finite algebra is classical.  Its application here is a source-typing
clarification, not a novelty or arithmetic-realization claim.  RH and GRH
remain unproved.

## 7. Bounded replay

```text
python -B research/riemann-structures/source_algebra_diagonal_adams_adapter.py --check
python -B -O research/riemann-structures/source_algebra_diagonal_adams_adapter.py --check
python -B -m unittest tests.test_source_algebra_diagonal_adams_adapter
python -B -O -m unittest tests.test_source_algebra_diagonal_adams_adapter
```

The producer enumerates permutations on at most four atoms, transition
weights in `{-1,1}`, and trace/extraction orders at most six.  It also checks
a five-cycle with nonintegral rational transition weights, the explicit
two-point intertwiner, the differing diagonals, and source-aware versus
incorrect extraction.  It authenticates frozen Git sources and hashes the
current note, producer, tests, and manifest with LF normalization.  All
checks use exact integers or `Fraction`; there is no finite-field sweep,
floating-point computation, native Frobenius construction, or analytic
certification.  Finite controls do not prove the universal statements.
