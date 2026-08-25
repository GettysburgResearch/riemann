# Arbitrary signed tensor weights do not improve FFPS principal leverage

Status: **PROVED as an exact finite-dimensional operator theorem** for every
nonempty finite set of distinct odd marked primes.  The result concerns the
formal source-faithful square-phase tensor and does not estimate an arithmetic
varying-conductor family.

Scope: arbitrary real or complex scalar weights on the complete joint tensor
coordinate set, including non-product and cross-prime-entangled weights.
Coefficients may vanish, but the metric remains the complete
\(G_S^{-1}\); deleting coordinates and then re-inverting a restricted Gram is
a different problem.

Exact dependency: the corrected FFPS square-phase Gram

\[
 G_p=pI_{m_p}-J_{m_p},\qquad m_p={p-1\over2},
\]

from `ffps_principal_leverage.json`.  At the live audited PR #751 head
`98af0db6ec7f77d6333a77a3dac53c4698852f43`, this local Gram contract is
unchanged: its source `L-106024` has the same blob as at the dependency
snapshot.  The gate ledger has advanced, however.  `BTPS106121` remains open
and sufficient; the uncentered `BTMS106121` and `BTDS106121` gates are
withdrawn because their nonprincipal atomic diagonals are not paid.  The
preferred live repair is the `T-106140` Wick-centered conjunction of the open
`WCADD106140` and `WCKUM106140` gates.

What was actually run: exact rational Kronecker algebra and
Gaussian-rational complex controls on a tiny declared prime panel, plus a
symbolic spectral proof.  No conductor, character, L-function, polynomial
family, or zero set is enumerated.

## 1. The signed-amplifier question

Let \(S\) be a nonempty finite set of distinct odd marked primes and put

\[
 \mathcal X_S=\prod_{p\in S}\{1,\ldots,m_p\},\qquad
 N_S=|\mathcal X_S|=\prod_{p\in S}m_p.
\]

On the joint tensor packet the phase Gram is

\[
 G_S=\bigotimes_{p\in S}G_p.                                  \tag{1}
\]

The native principal observation is the sum of all \(N_S\) coordinates.
Consider instead an arbitrary scalar signed amplifier

\[
 O_\alpha(w)=\sum_{x\in\mathcal X_S}\overline{\alpha_x}w_x,
 \qquad \alpha\in\mathbf C^{N_S}.                             \tag{2}
\]

This includes every product weight, every non-product cross-prime weight,
and every phase or sign choice.  Preserving the native principal member means

\[
 \langle\alpha,\mathbf1\rangle=N_S.                            \tag{3}
\]

Here \(\langle u,v\rangle=u^*v\), so (3) says
\(\sum_x\overline{\alpha_x}=N_S\); because the right side is real, this is
equivalent to \(\sum_x\alpha_x=N_S\).  This convention exactly matches the
conjugation in (2).

Without (3), a smaller norm can merely be deletion or attenuation of the
target signal.

## 2. Exact optimum and rigidity

The squared dual norm of (2) in the phase metric is

\[
 \|O_\alpha\|_{G_S}^2=\alpha^*G_S^{-1}\alpha.                 \tag{4}
\]

Each local constant vector is an eigenvector:

\[
 G_p\mathbf1=(p-m_p)\mathbf1={p+1\over2}\mathbf1.
\]

Consequently

\[
 G_S\mathbf1=\lambda_S\mathbf1,
 \qquad \lambda_S=\prod_{p\in S}{p+1\over2}.                 \tag{5}
\]

Write \(\alpha=\mathbf1+\beta\).  Condition (3) says
\(\langle\beta,\mathbf1\rangle=0\).  Since
\(G_S^{-1}\mathbf1=\lambda_S^{-1}\mathbf1\), the cross term
vanishes exactly and

\[
\boxed{
 \alpha^*G_S^{-1}\alpha
 =\prod_{p\in S}{p-1\over p+1}
  +\beta^*G_S^{-1}\beta.}                                    \tag{6}
\]

The Gram is positive definite, so the penalty in (6) is nonnegative and is
zero only for \(\beta=0\).  Therefore

\[
\boxed{
 \min_{\langle\alpha,\mathbf1\rangle=N_S}
 \|O_\alpha\|_{G_S}^2
 =\prod_{p\in S}{p-1\over p+1},}                              \tag{7}
\]

and the unique complex extremizer is the unweighted coherent tensor
\(\alpha=\mathbf1\).

This is stronger than optimizing product weights: arbitrary entanglement of
the prime coordinates cannot lower the complete-frame tensor leverage.  It
is complementary to, rather than a derivation of, the earlier masking
theorem.  A zero coefficient inside the complete inverse metric uses a
principal block of \(G_S^{-1}\), whereas physically deleting coordinates and
re-inverting the retained Gram uses the inverse of a principal block of
\(G_S\); those operations need not agree.  The separately source-locked
masking packet proves a local restricted-Gram no-go and its
product-coordinate tensor corollary.  It does not cover arbitrary correlated
subsets of the joint tensor coordinates.

## 3. Mode-resolved penalty

For each \(p\), split the local coordinate space into the constant line and
its sum-zero complement.  A tensor mode indexed by a subset
\(A\subseteq S\), with sum-zero choice at exactly the primes in \(A\), has
Gram eigenvalue

\[
 \lambda_A=\prod_{p\in A}p
             \prod_{p\in S\setminus A}{p+1\over2}.            \tag{8}
\]

Its multiplicity is

\[
 d_A=\prod_{p\in A}(m_p-1).
\]

In particular, a putative mode with \(3\in A\) has multiplicity zero because
the \(p=3\) coordinate space is already the constant line.

The normalization (3) removes only the all-constant perturbation.  If
\(\beta=\sum_{A\ne\varnothing}\beta_A\) is its orthogonal spectral
decomposition, then (6) refines to

\[
 \boxed{
 \|O_\alpha\|_{G_S}^2-L(S)
 =\sum_{A\ne\varnothing}{\|\beta_A\|_2^2\over\lambda_A},
 \qquad L(S)=\prod_{p\in S}{p-1\over p+1}.}                  \tag{9}
\]

Thus the failure of a nonuniform complete-frame reweighting is not merely
qualitative: every nonconstant tensor mode carries an explicit positive cost.
Complex phases cannot create destructive cross terms between these
orthogonal modes.

## 4. Consequence for the RH-facing programme

Within the complete corrected local phase metric, none of the following can
beat the coherent product leverage while retaining the native principal
amplitude:

- signed or complex scalar reweighting;
- weights correlating several marked primes;
- non-separable tensor weights;
- zero-coordinate weights evaluated in the complete tensor metric.

The separate conditioned-mask packet rules out local physical deletion and
product-coordinate tensor masks followed by restricted-Gram inversion.  It
does **not** rule out correlated non-product deletion of joint coordinates.
There is already a small exact warning at \(S=\{5,7\}\).  In zero-based
lexicographic order on the \(2\times3\) joint coordinates, retain

\[
 A=\{0,2,3,4\}
 =\{(0,0),(0,2),(1,0),(1,1)\}.
\]

For the retained principal block \(H=(G_5\otimes G_7)_{A,A}\),

\[
 \mathbf1^TH\mathbf1=74.
\]

After restoring the native amplitude \(N_S=6\), its exact restricted-metric
optimum is

\[
 {N_S^2\over\mathbf1^TH\mathbf1}={36\over74}={18\over37}
 <{1\over2}=L(\{5,7\}),
\]

attained at the retained weights

\[
 \alpha={1\over37}(45,66,45,66).
\]

The same weights extended by zero to all six coordinates have complete-metric
energy \(8181/13690>1/2\), exactly as theorem (7) requires.  Thus correlated
physical deletion is a genuinely different formal amplifier direction.
Whether such a subset is source-faithful or arithmetically realizable remains
open; the present theorem neither proves nor suggests a no-go for that
restricted problem.

This closes the complete-frame scalar-reweighting loophole in the formal
model.  It is not a global no-go theorem.  An improvement may still come from
an arithmetic condition that changes the Gram, a new incidence operator, a
nonlinear or indefinite identity not controlled by positive phase energy,
exceptional-ledger cancellation, or a genuine varying-core moment theorem.
In particular, (7) does not prove the open `BTPS106121`, `WCADD106140`, or
`WCKUM106140` gates, RH, or GRH, and it does not turn the tensor packet into a
realized conductor family.

## 5. Frozen provenance and replay

The producer first closes the self-contained Kronecker and spectral algebra,
then reads the frozen dependencies.  Thus the dependency files certify the
FFPS interpretation but are not numerical inputs to the operator identity.
The local principal dependency is locked to corrected PR #751 snapshot
`37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2` and LF-normalized SHA-256
`cdf514d8f8b76b7d2569ea6852c8f4dcc8590c0ad72822d3bee711711cfd3ee3`.
The complementary conditioned-mask and conductor-frontier JSON locks are,
respectively,
`fe6024020775e977e3dfe31822137b579c9cef438f9e94666714179ed43d469b`
and
`f6b65bb4a8cdaaa7c91464d8fba86b7691350bf14cdcc8a68c90848be6f89d51`.
The live-status audit is separately pinned to head `98af0db6e`: current blobs
are `9111983ae` for `T-106121`, `8dde14dd3` for `R-106131`, `37722c3f3` for
`L-106131`, and `d5be8e376` for `T-106140`.  These later ledger repairs do not
alter `L-106024` or the operator theorem proved here.

The canonical JSON, bounded producer, and tests accompanying this note check
the Kronecker spectrum, the exact Pythagorean identity (6), the mode penalty
(9), genuinely non-product complex Gaussian-rational controls, and uniqueness
under normal and optimized Python.  They also certify the correlated
restricted-Gram counterexample above, so the metric distinction fails closed
rather than being merely verbal.  The finite controls use only the panels
\((5,7)\) and \((3,5,7)\), of tensor dimension six; the proof is the displayed
all-finite-\(S\) algebra, not interpolation from those panels.

```text
python -B research/l-families/atlas/function_field/ffps_tensor_signed_amplifier_no_go.py --check
python -B -O research/l-families/atlas/function_field/ffps_tensor_signed_amplifier_no_go.py --check
python -B -m unittest tests.test_ffps_tensor_signed_amplifier_no_go
python -B -O -m unittest tests.test_ffps_tensor_signed_amplifier_no_go
```
