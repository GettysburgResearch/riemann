# Tensor-moment rigidity of an ordered Satake-angle deformation

Status: proposed reviewable mathematics; separate follow-up, not integrated.
Programme: #764 generalized L-objects, prime-deformation/completion axis.
Claims: `GLO764.TENSOR_MOMENT_COMPLETION_RIGIDITY_V1` and
`GLO764.FINITE_MOMENT_PRESERVING_DEFORMATION_V1`.
Source: the unchanged Satake packet at
`b895598abd936a2e42e5b7d14a7e10cc2bf41486`.
Scope: a conditional all-tensor rigidity theorem and explicit finite-moment
countercontrols; no novelty, group-reconstruction, automorphy, or RH claim.

## 1. Source, normalization, and the common parameter interval

The source packet supplies actual Delta prime angles through Deligne's bound
and the exact Delta Sato--Tate theorem of Barnet-Lamb--Geraghty--Harris--Taylor.
It also proves the qualitative Abel lemma and integer-logarithmic-order
obstruction. Those imported arithmetic theorems are not re-proved here.
Their precise primary URLs and locators remain in the source note/manifest.

Fold its circle angle by `phi = arccos(cos(2 theta))` into `[0,pi]`.
The two circle preimages have the same density; hence the probability measure is

\[
 d\mu(\phi)=\frac{1-\cos\phi}{\pi}\,d\phi,\qquad
 F(x)=\mu([0,x])=\frac{x-\sin x}{\pi}.
\]

The corresponding rank-three Satake class and trace are
`A(phi)=diag(e^(i phi),1,e^(-i phi))` and `t(phi)=1+2cos(phi)`.
F is continuous and strictly increasing from zero to one; its derivative may
vanish at zero, which does not impair strict increase. The trace t is a
continuous strictly decreasing bijection from `[0,pi]` to `[-1,3]`.

Let **one common connected interval** `I subset R` contain zero. For every
`epsilon in I`, let `h_epsilon:[0,pi]->[0,pi]` be an increasing homeomorphism,
with `h_0=id`. Assume only that `epsilon -> h_epsilon(phi)` is continuous for
each fixed phi. No differentiability or joint analyticity is assumed.
For each integer `m>=1` define, initially on `Re s>1`,

\[
 L_{m,\epsilon}(s)=\prod_p
 \det\!\left(I_{3^m}-A(h_\epsilon(\phi_p))^{\otimes m}p^{-s}\right)^{-1}.
\]

This is the tensor power of the **deformed local matrix**, not an assertion
that the deformation commutes with tensor functors or comes from a new
automorphic representation.

## 2. The all-tensor theorem

**Theorem.** If, for every `m>=1` and every `epsilon in I`, `L_(m,epsilon)`
has a meromorphic germ at `s=1` agreeing with its Euler product on the right,
then `h_epsilon=id` for every `epsilon in I`.

The meromorphic neighborhoods may depend arbitrarily on both m and epsilon.
There is no uniform germ radius or joint regularity assumption on the completed
objects. Replacing each Euler product by a product with any nonzero meromorphic
multiplier germ at one leaves the theorem unchanged, by local division.

**Proof, step 1: every prime moment is an integer log order.** For each fixed
m the tensor rank is `3^m`. Its eigenvalues are unitary and occur in conjugate
pairs, with real eigenvalues `+1` or `-1` contributing positive factors
`1-X` or `1+X` when `0<X<1`. Thus every local reciprocal determinant is
positive for real `sigma>1`. The Euler logarithm converges absolutely on
`Re s>1`, since every power trace has absolute value at most `3^m`.
It defines a nonzero holomorphic Euler product there with an ordinary real log.

The tensor trace identity gives
`trace(A(h_epsilon(phi))^(tensor m))=t(h_epsilon(phi))^m`. The folded
Sato--Tate theorem applies to this fixed continuous function. Consequently

\[
 a_m(\epsilon)=\int_0^\pi t(h_\epsilon(\phi))^m\,d\mu(\phi),\qquad
 \sum_{p\leq x}\left(t(h_\epsilon(\phi_p))^m-a_m(\epsilon)\right)=o(\pi(x)).
\]

The source Abel lemma proves that the centered prime Dirichlet sum is
`o(log(1/(sigma-1)))`. The `k>=2` Euler-log terms are bounded by
`2*3^m sum_(n>=2)n^(-2)`, for this fixed m. It follows that

\[
 \lim_{\sigma\downarrow1}
 \frac{\log L_{m,\epsilon}(\sigma)}{\log(1/(\sigma-1))}=a_m(\epsilon).
\]

For clarity, the imported elementary Abel argument needs no PNT: if
`B(x)=o(pi(x))`, partial summation and `|B(x)|<=delta pi(x)` after a fixed
cutoff bound the centered sum by `O_delta(1)+delta sum_p p^(-sigma)`.
The zeta Euler logarithm and its elementary pole give
`sum_p p^(-sigma)=log(1/(sigma-1))+O(1)`. Let delta decrease to zero.

A nonzero meromorphic germ is `(s-1)^k u(s)` for an integer k with
`u(1)!=0`. Its real log absolute value has the preceding limit `-k`.
The assumed meromorphy therefore forces `a_m(epsilon) in Z`.

**Step 2: connectedness freezes every moment.** Pointwise parameter continuity
and the fixed bound `|t(h_epsilon(phi))^m|<=3^m` imply continuity of
`a_m(epsilon)` by dominated convergence. A continuous integer-valued function
on the connected interval I is constant. Hence, simultaneously for all m,

\[
 \int t(h_\epsilon(\phi))^m\,d\mu(\phi)
       =\int t(\phi)^m\,d\mu(\phi).
\]

Moment zero also agrees because both measures have total mass one. This step
uses the **same I for every m**. Tensor-dependent neighborhoods shrinking with m
do not give equality of all moments at any one nonzero parameter and are not
covered by the theorem.

**Step 3: compact moments and the ordered angle force identity.** Let
`nu_epsilon=(t circ h_epsilon)_*mu` and `nu_0=t_*mu`, both supported on `[-1,3]`.
Equal moments give equal integrals of polynomials. To recall why this determines
the measure, rescale to `[0,1]` and approximate any continuous function f by its
Bernstein polynomials. If `K~Binomial(N,x)`, their error is bounded by
`omega_f(delta)+2||f||_infinity/(4N delta^2)`, using the variance bound
`Var(K/N)<=1/(4N)`. First choose delta small and then N large: convergence is
uniform. Thus all continuous integrals agree. Continuous upper/lower ramps at
each point recover the CDFs: both measures are atomless, since mu is atomless
and t and h are homeomorphisms. Hence `nu_epsilon=nu_0`.

Because t is injective with continuous inverse, `h_epsilon_*mu=mu`. Monotonicity
now implies for every y that
`F(h_epsilon^(-1)(y))=F(y)`. Strict increase of F yields
`h_epsilon^(-1)(y)=y`, and therefore `h_epsilon=id`. QED.

If the ordered-homeomorphism setting is enlarged to arbitrary measure-preserving
rearrangements, equality of laws need not force identity. Without the common
connected parameter interval, continuity does not freeze
all moments together. The theorem does not classify arbitrary local matrix
deformations, prime-dependent maps, or disconnected parameter families.

## 3. Explicit finite-moment-preserving deformations

For every integer `j>=1`, use the standard Dirichlet-kernel polynomial

\[
 q_j(\phi)=1+2\sum_{r=1}^j\cos(r\phi),\qquad
 I_j=\left(-\frac1{2j+1},\frac1{2j+1}\right).
\]

The triangle inequality gives `|q_j|<=2j+1`. For `epsilon in I_j`, therefore,
`1+epsilon q_j>0`. The telescoping product identity is

\[
 (1-\cos\phi)q_j(\phi)=\cos(j\phi)-\cos((j+1)\phi).
\]

It follows that `int q_j dmu=0`, and
`dmu_(epsilon,j)=(1+epsilon q_j)dmu` is a probability measure with strictly
increasing CDF

\[
 F_{\epsilon,j}(x)=\frac1\pi\left[x-\sin x+
   \epsilon\left(\frac{\sin(jx)}j-
                      \frac{\sin((j+1)x)}{j+1}\right)\right].
\]

Its endpoints are zero and one. Define the exact transport, without numerical
inversion, by

\[
 h_{\epsilon,j}=F_{\epsilon,j}^{-1}\circ F.
\]

It is an increasing homeomorphism, `h_(0,j)=id`, and pushes mu to
`mu_(epsilon,j)`: its inverse is `F^(-1) circ F_(epsilon,j)`, so the image CDF
at y is `F(h_(epsilon,j)^(-1)(y))=F_(epsilon,j)(y)`.
It is pointwise continuous in epsilon. Indeed the CDFs converge uniformly as
epsilon varies continuously; every convergent subsequence of inverse images
must solve the limiting strictly monotone CDF equation, whose solution is
unique. Compactness supplies such subsequences, proving convergence.

**Proposition.** These maps preserve the trace moments `0..j-1` exactly, while
their j-th moment equals its undeformed value plus epsilon.

**Proof.** Write `z=e^(i phi)` and
`t=1+z+z^(-1)`. The integrands are even trigonometric polynomials, so their
uniform average on `[0,pi]` equals the circle constant term. If
`C_(m,k)=[z^k](1+z+z^(-1))^m`, symmetry gives `C_(m,-k)=C_(m,k)`, and

\[
 b_m=\int t^m\,d\mu=C_{m,0}-C_{m,1}\in\mathbb Z,
 \quad
 c_{m,j}=\int t^m q_j\,d\mu=C_{m,j}-C_{m,j+1}.
\]

For `m<j` both latter coefficients vanish; for `m=j` they are one and zero,
respectively. Transport of measure now gives

\[
 \int t(h_{\epsilon,j}(\phi))^m\,d\mu
       = b_m+\epsilon c_{m,j},\qquad
 c_{m,j}=0\ (m<j),\quad c_{j,j}=1.
\]

The integer coefficients can independently be written, for `0<=k<=m`, as
`C_(m,k)=sum_(r=0)^floor((m-k)/2) binomial(m,r) binomial(m-r,r+k)`.
This also proves the asserted integrality of b without importing invariant
theory. QED.

For every fixed nonzero `epsilon in I_j`, the j-th tensor Euler product formed
from this transport has log order `b_j+epsilon`, which is not an integer since
`0<|epsilon|<1`. It is therefore not meromorphic at one. Nonzero meromorphic
multiplier germs cannot repair it. The lower moment equalities **do not prove
that any of the lower tensor Euler products is meromorphic**; they only pass
this necessary moment test. Nor does the result describe the analytic branch
type or give a constant-times asymptotic.

The especially useful `j=2` control has `q_2=t^2-t-1`, `b_1=0`, and `b_2=1`.
For every `0<|epsilon|<1/5` its first trace mean remains zero but its second
moment is `1+epsilon`, so the tensor-square completion fails. For arbitrary
finite cutoff M, choosing `j=M+1` preserves all moments through M while failing
the next one. This is a finite-moment insufficiency statement inside the broad
space of transported probability laws, not inside the narrower space of
genuine compact-group Sato--Tate measures.

## 4. What the exact checker establishes

The independent standard-library producer uses rational Laurent algebra and
binomial sums. Its default rectangle is `1<=j<=8`, `0<=m<=12`; the supported
maximum is `j<=12`, `m<=24`. Every cell in the declared rectangle is replayed.
It checks tensor-weight multiplicities, total dimension `3^m`, inverse-pair
symmetry and zero total weight, integer b_m, telescoping densities, both
independent c_(m,j) constructions, the polynomial `q_2=t^2-t-1`, CDF derivative
coefficients, positive density margins, signed rational epsilon controls, and
first-failing-moment controls. Tests include held-out j/epsilon values.

No floating trigonometry, numerical inverse CDF, prime sample, or Delta tau
table is used. The computer does not verify the infinite Sato--Tate theorem,
dominated convergence, compact moment determinacy, or meromorphic continuation.
Those are separated into imported theorems and native written arguments above.

Arithmetic class is `MIXED`, with components `EXACT_RATIONAL` and
`CERTIFIED_INTEGER_COVERAGE`, and no rounding. Integer/rational public inputs
reject bool, floats, strings, excessive bit sizes, and out-of-range indices.
The declared algebra-work budget score must be strictly below the selected
cap before source authentication or corpus loops. It is a deterministic
resource preflight contract, not a certified wall-time prediction.

The source manifest authenticates three parent files at the frozen Git commit
and their LF-normalized hashes, verifies unchanged current bytes, and pins the
prior-art declarations. Parent arithmetic source URLs remain source-qualified
imports; no PDF theorem is machine-proved. Note, producer, tests, and manifest
have LF artifact hashes. The fixture is accepted only after full regenerated
typed canonical-JSON equality, including the payload digest. Duplicate keys,
nonfinite JSON, over-size data, altered source/artifact bytes, and type confusion
fail closed; validation does not depend on Python assertions.

```text
python -B research/l-families/atlas/generalized/tensor_moment_completion_rigidity.py --check
python -B -O research/l-families/atlas/generalized/tensor_moment_completion_rigidity.py --check
python -B -m unittest discover -s tests -p test_tensor_moment_completion_rigidity.py
python -B -O -m unittest discover -s tests -p test_tensor_moment_completion_rigidity.py
```

`--write` regenerates only this packet's fixed fixture after authenticating its
sources. Author-run and independent-review results are reported at frozen SHA;
the file itself does not confer review status. The smallest mathematical
failure invalidating the rigidity conclusion would be a failure of moment
continuity on the common interval or of the ordered CDF implication. Both have
explicit proofs above. Finite algebra replay cannot substitute for those proofs.

## 5. Primary prior art and the research boundary

Michael Larsen, *Rigidity in the Invariant Theory of Compact Groups*,
[arXiv:math/0212193v1](https://arxiv.org/pdf/math/0212193), introduction and
Theorem 3.3 (PDF p.8), explicitly relates compact-group Sato--Tate moments to
dimensions of mixed-tensor invariant spaces and proves an isolation theorem
under its stated semisimplicity condition. That is substantial prior art for
moment-based rigidity. Its finite-determinacy conclusion ranges over genuine
compact-group Sato--Tate measures, not arbitrary positive perturbations such as
those above; this packet neither contradicts nor strengthens it.

Michael Larsen and Richard Pink, *Determining Representations from Invariant
Dimensions*, [author-hosted primary paper](https://people.math.ethz.ch/~pink/ftp/LP1.pdf),
introduction, Theorems 1--3, and §1, studies which group/representation data can
be recovered from invariant dimensions, with both uniqueness results and
counterexamples. This packet does not reconstruct a group and does not import
those reconstruction theorems. Its elementary compact-real-moment argument is
written explicitly rather than presented as a new invariant-theory principle.

The useful programme distinction is now precise: preserving the first mean
alone leaves explicit tensor-square counterexamples; every finite list of
moment constraints still permits explicit higher-moment failures; preserving
meromorphic completion of all tensor powers along a common connected ordered
angle deformation forces the deformation to be trivial. None of this supplies
a new generalized L-function, an automorphy theorem, or an RH route.
