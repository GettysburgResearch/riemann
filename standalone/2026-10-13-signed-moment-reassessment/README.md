# Reassessing the signed moment program

**Status:** proposed standalone mathematics and a source-qualified research
reassessment. The full generalized native moment and RH remain open.
The principal new result is a proof that one proposed sufficient trace
contract is false at every fixed order. The packet also develops an
admissible moving contour, classifies fixed causal replicas, and separates
the random and invariant components of a dense determinant family.

**Scope:** the original Eisenstein Möbius/sextic family, fixed finite-order
Hecke data, literal ideal coefficients, all nonzero physical element rows,
and every principal nonunit zero. The determinant probability model is
explicitly separate from the physical row measure. Its conclusions are
not arithmetic moment estimates for that row measure.

**Source:** stacked on PR #929 at
97bf40329489992e9384c34d7595af6d01a40774.
The historical contracts and comparisons are pinned to 25 exact repository
inputs in [SOURCE_LOCK.json](SOURCE_LOCK.json). This packet changes none
of those historical proof files. In particular, the trace refutation
addresses PR #911 at 2f8b6a3898a722d0602a91dea73bac344a3bb7dd.

**What was actually done:** the relevant September and October reductions
were compared at their stated sources; the new arguments were reconstructed
by separate AI agents; elementary algebra and source identities were checked.
No native asymptotic estimate is inferred from a finite numerical test,
and no external proof-assistant result was replayed.

## 1. The objective and the source of the repeated loss

Write

\[
A_u(D;W)=\sum_{(\mathfrak n,S)=1}
\mu_K(\mathfrak n)\nu(\mathfrak n)\chi_{\mathfrak n}(u)
W(N\mathfrak n/D).
\]

The intended generalized estimate is

\[
\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll_{\epsilon,k,\nu,S,W}H D^{k+\epsilon},
\qquad H=D^h,
\]

for an unbounded hierarchy of fixed orders, with \(h\) near one. The
existing sixth-power extraction prices an extra moment loss \(D^a\) at
the conditional boundary

\[
\Re s>\frac12+\frac{5h}{12k}+\frac{a}{2k}.
\]

This explains both the appeal and the difficulty of the hierarchy.
Sufficient bounds with \(h_k=o(k)\) and \(a_k=o(k)\) would approach
the critical line. A fixed saving on selected collision sectors does
not establish the required complete moment.

The reassessment found a recurring problem with otherwise correct
identities: an affordable transformation preserves a difficult signed
observable, while a later absolute estimate either loses its decisive
correlations or asks for a substantially stronger object. The
[historical note](HISTORICAL_CONNECTIONS.md) makes this precise:

| Route | What the existing source controls | What remains |
|---|---|---|
| Newton covariance compression | Detail energy and an exact reconstruction | The coarse means retain the full difficult energy |
| Balanced completion | Exact finite changes of representation | The later native bulk can be invariant under those changes |
| Mellin bandwidth and phase averages | Specified frequency or phase components | Extraction costs do not yield a contracting exponent |
| Complete CRT averaging | Exact local joint distributions, including zeros | The correlation with the translated short physical row measure |
| All-order collision removal | Reversible finite convolution at polylogarithmic cost | A complete rectangular norm at one common row height |
| Short finite Euler trace | A complete norm-filtered identity and a negligible tube | Its proposed pointwise complement is refuted below |

The collision coefficients, derangement formula, sharp critical kernel
mass, and cycle factorization already occur in PR #916. They are credited
as prior work throughout this packet.

## 2. A pointwise trace target is false for the native family

[SIGNED_TRACE_OBSTRUCTION.md](SIGNED_TRACE_OBSTRUCTION.md) proves the
following statement, with all its constants, masks, and quantifiers.
Fix \(k\ge1\), \(1/3<\sigma<1/2\), the original finite-order datum
\(\nu\), and a nonnegative Schwartz row weight positive at zero.
One fixed admissible cross-pair incidence suffices.

Let \(\mathscr T_{2k,Y}\) be exactly the unfiltered short trace in
PR #911 CT1, and \(\mathcal U_{Y,\kappa}\) its paid common-conjugate
tube. For every fixed polynomial frequency weight \(B\), along an
unbounded sequence of the permitted real cutoffs,

\[
\boxed{
\sup_{\mathbf t\notin\mathcal U_{Y,\kappa}}
\frac{|\mathscr T_{2k,Y}(\sigma+i\mathbf t)|}
     {\prod_i(1+|t_i|)^B}
\ge
Y^{-C_B}
\exp\!\left(\frac{cY^{1-2\sigma}}{\log Y}\right).
}
\]

Thus CT1 fails even if its proposed \(D^\epsilon\) loss is replaced
by any fixed power of \(D\). This is a native trace theorem, not an
arbitrary-coefficient or unsigned countermodel.

### The mechanism

For two slots at the same complex frequency, the exact collision
factor contains a universal principal factor

\[
F_Y(s)=\prod_{\substack{N\mathfrak p\le Y\\
                       \mathfrak p\notin SP}}
       \left(1-(N\mathfrak p)^{-2s}\right).
\]

The complete trace factors as \(F_Y(s_Y(z))G_Y(z)\), where
\(s_Y(z)=\sigma+iz/\log Y\). Every row-prime correction remains in
\(G_Y\). This residual function is holomorphic on a fixed disk and
has a polynomial bound. At \(z=0\) every one of its native row
summands is nonnegative. The literal coefficient jump at ideal
norm \(p^2\) supplies \(G_Y(0)\gg Y^{-2\sigma}\) along infinitely
many cutoffs, for every fixed allowed \(\nu\).

Elementary complex interpolation then forces \(G_Y\) to have
polynomial size somewhere in \(1\le z\le5/4\). The classical
unconditional prime-ideal theorem gives

\[
\log |F_Y(s_Y(z))|
=\left(-\cos(2z)+o(1)\right)
\frac{Y^{1-2\sigma}}{(1-2\sigma)\log Y}>0
\]

there, with a positive main term. This proves the two-slot lower
bound. Successive right-half-plane maximum principles collapse
every higher-order trace to that two-slot face at only polynomial
cost. The paid tube cannot contain the resulting large supremum.

The physical moment is not contradicted. The pointwise trace is
taken before the physical norm tests. The coefficient identity
and the negligible tube in the original representation remain
valid; its proposed pointwise complement is an impossible premise.

## 3. Two valid ways to retain the physical operation

The finite repair in
[HISTORICAL_CONNECTIONS.md](HISTORICAL_CONNECTIONS.md), HC1--HC6,
applies the existing PR #916 convolution algebra to this exact
SC4 interface. Project the collision series onto the coordinate
norm box before estimating it. Since integral ideal norms can only
increase under multiplication, the whole tested source identity is
unchanged. Its finite collision polynomial satisfies

\[
|\widehat{\mathcal Q}_{Y,Q,u}(\sigma+i\mathbf t)|
\ll_{k,S}
Y^{k(1-2\sigma)}(1+\log Y)^{k(2k-1)},
\qquad 0<\sigma\le\frac12.
\]

This is a polynomial price for an exact finite replacement. It
preserves the original fixed \(S\), every row, and all zero masks.
It does not transfer the old tube estimate to a different
integrand or pay the remaining short-polynomial row trace.

[MOVING_CONTOUR_WINDOW.md](MOVING_CONTOUR_WINDOW.md) gives a different
repair: keep the original rational factor but let the contour
approach \(1/2\) as the cutoff grows. With
\(\sigma_Y=1/2-\delta_Y\) and \(a_Y=2\delta_Y\log Y\), the relevant
prime sum has size at most

\[
O\!\left(\log\log Y+\frac{e^{a_Y}}{1+a_Y}\right).
\]

The subpower window is \(e^{a_Y}/(1+a_Y)=o(\log Y)\).
In that window the estimate makes the collision factor
\(Y^{o(1)}\), uniformly in the row, mask, and all independent
frequencies. The explicit choice

\[
\sigma_Y=\frac12-\frac{\log\log Y}{2\log Y}
\]

is admissible. This removes the fixed-below-half representation
obstruction. It does not prove cancellation in the remaining
literal short polynomials.

## 4. A classification of all fixed causal replicas

[CAUSAL_ORBITS_AND_DENSE_LIFTS.md](CAUSAL_ORBITS_AND_DENSE_LIFTS.md)
first tests whether a more general exact replication operator can
improve the sparse sixth-power count.

For the Gaussian-smoothed native row \(A_r\), allow any fixed
complex measure on causal dilations:

\[
A_u(D)=\int_{[1,\infty)}A_r(D/t)\,d\lambda(t),
\qquad
\int t^{-\sigma_0}\,d|\lambda|(t)<\infty
\]

for some \(0<\sigma_0\le1\). This includes continuous measures.
The theorem proves that such an identity is possible exactly when
the primitive characters satisfy

\[
\boxed{\psi_u=\psi_r\quad\text{or}\quad\psi_u=\psi_r^c.}
\]

Field conjugation is required because radial norm smoothing
identifies a character with its field conjugate.

The proof combines Mellin-transform uniqueness with induced
finite-group characters. A different primitive character produces
nonzero prime coefficients in the Euler ratio on a positive-density
Chebotarev set. Their weighted absolute sum diverges already at
exponent one. No continuous measure can avoid this coefficient
obstruction.

Kummer theory consequently restricts this orbit to at most two
fixed sixth-power classes, or four if complex conjugation of the
sum is also allowed. Their physical row count remains
\(O_{\nu,r}(H^{1/6})\). The exponent-one threshold is sharp:
arbitrary fixed rows can be connected at absolute weights
\(\sigma_0>1\).

This classifies the stated weighted-total-variation method. It
does not classify operators controlled through cancellation,
nonstationary identities, or signed interactions between distinct
primitive characters.

## 5. A finite-group connection separates randomness from the target

The same note investigates a more radical enlargement. Multiplying
the six power twists puts a fixed target reciprocal in every member
of a dense family:

\[
\mathcal D_u(s)=
\prod_{\substack{\mathfrak p\notin S\\\mathfrak p\nmid u}}
\prod_{j=0}^{5}
\left(1-\nu_0(\mathfrak p)\chi_{\mathfrak p}(u)^j
                     (N\mathfrak p)^{-s}\right).
\]

Even the \(j=0\) factor retains its principal nonunit zero. A
nontrivial zero of \(L_K(s,\nu_0)\) is a pole of every member.
Thus this enlargement really does escape the sparse causal orbit.

For a general finite group representation \(\rho\) on \(V\), put
\(m_0=\dim V^{\mathcal G}\). The exact determinant average is

\[
\frac1{|\mathcal G|}\sum_{g\in\mathcal G}\det(I-x\rho(g))
=\sum_j(-x)^j\dim(\wedge^jV)^{\mathcal G}
=(1-x)^{m_0}Q_\rho(x),
\qquad Q_\rho'(0)=0.
\]

On the independent local Haar model, with the true nonunit
probability \(1/N\mathfrak p\), this yields

\[
\mathbb E\mathcal D_\omega(s)
=\frac{\mathcal H_{\rho,S,\nu_0}(s)}
       {L_K(s,\nu_0)^{m_0}},
\qquad \Re s>1,
\]

where \(\mathcal H\) is holomorphic and nonzero for
\(\Re s>1/2\), after a stated fixed small-prime deletion.
The quotient supplies a meromorphic continuation of the mean;
its holomorphy below one is not assumed.

Normalize each local determinant by its mean. Independence and
the cancellation of the linear terms in its mixed moments produce
an \(L^{2k}\)-valued holomorphic Euler product for every fixed
\(k\) and every \(\sigma>1/2\).
This identifies the model's decisive distinction:

- If \(m_0=0\), the Gaussian determinant sum has the desired
  \(D^{k+\epsilon}\) moment of order \(2k\), for every fixed \(k\),
  unconditionally in this model.
- If \(m_0>0\), even one such fixed-order model moment is equivalent
  to the fixed target's zero exclusion in \(\Re s>1/2\).
  That zero exclusion gives the entire hierarchy. Jensen and
  Mellin continuation prove one direction; normalized \(L^{2k}\)
  convergence and a Gaussian contour shift prove the other.

[COMPACT_TEST_HAAR_MOMENTS.md](COMPACT_TEST_HAAR_MOMENTS.md) proves
the same sufficient moment hierarchy for every fixed
\(W\in C_c^\infty((0,\infty))\), using its rapid Mellin decay.
When \(m_0>0\), a fixed-order moment assertion for the entire
compact-test class is also equivalent to the target's zero exclusion.
The converse can use only nonnegative tests: for any hypothetical
zero, one fixed small log-bump has a Mellin transform that does not
vanish there. No uniformity over the test class is assumed.
A converse for a single arbitrary compact test is not claimed.

Only the normalized random product is continued by this convergence.
The original random Dirichlet series is continued as the meromorphic
mean times that normalized limit, matched first on \(\Re s>1\).
This continuation is holomorphic under the stated zero-exclusion
hypothesis, or unconditionally when \(m_0=0\).
Convergence of its unnormalized finite Euler products below one
is neither required nor asserted.

For the regular sextic representation,

\[
P_{C_6}(x)=1-x+2x^2-4x^3+3x^4-x^5
         =(1-x)(1+2x^2-2x^3+x^4),
\]

so \(m_0=1\). The dense family moves the fixed target into its
invariant mean. Generic local randomness controls the normalized
fluctuations, while that mean still carries the zero problem.
These are theorems about the stated probability model; no
physical-to-Haar comparison has been proved.

The original one-dimensional sextic representation has \(m_0=0\).
Its independent model therefore already has every desired fixed
Gaussian or smooth compact-test moment. The complete-residue identities in PR #911 explain
why that benchmark cannot distinguish Möbius signs from their CRT
translation. The missing information is how the actual short
physical row measure correlates with that translation.

## 6. The surviving arithmetic target

The source-faithful rectangular target already isolated by PR #916
remains a concrete route:

\[
\sum_{0<Nu\le H}
|B_{k,u}(X_1,\ldots,X_k)|^2
\ll H\!\prod_iX_i\,D^{a_k+\epsilon},
\qquad 1/b\le X_i\le D,
\]

at one common \(H=D^{h_k}\). Here \(B_{k,u}\) is the exact
fixed-\(S\), pairwise-coprime product polynomial with all its
divisor allocations. Sufficient sublinear defects
\(h_k=o(k)\), \(a_k=o(k)\) would feed the existing extraction.
No such hierarchy is proved here.

A continuation should therefore preserve the physical norm
filters and the signed correlation between distinct Kummer
classes through the estimate. The new results rule out a fixed
subcritical pointwise trace and a broader class of cheap causal
replicas. They also identify exactly where a dense Haar model
retains the target arithmetic. They do not replace the needed
physical correlation theorem.

For the original compact-test family this can also be expressed as
an exact comparison with the proved Haar benchmark, with the same
fixed \(W\) as the physical moment. Put
\(Z_H=\sum_{u\ne0}\Phi(u/\sqrt H)\) and define

\[
\Delta_{2k}(D,H;W)=
\sum_{u\ne0}\Phi(u/\sqrt H)|A_u(D;W)|^{2k}
-Z_H\,\mathbb E_\Omega|A_\omega(D;W)|^{2k}.
\]

The second term is \(O(H D^{k+\epsilon})\). For this same smoothed
row measure, the desired physical moment is therefore equivalent
to \(|\Delta_{2k}(D,H;W)|\ll H D^{k+\epsilon}\).
If the nonnegative \(\Phi\) majorizes the unit norm ball, this
smoothed physical bound implies the hard row bound. No converse
from one hard cutoff to the Schwartz measure is assumed.
This is a precise description of the remaining correlation;
no bound for the discrepancy is proved. The compact-test note
supplies the norm-test adapter, so this comparison no longer
requires a change to Gaussian smoothing.

## 7. Review and publication boundaries

The proof notes distinguish unconditional elementary deductions,
classical imported theorems, conditional statements, and the
independent Haar model. Source and review records are collected in
[VALIDATION.md](VALIDATION.md), including the frozen mathematical
commit and the later receipts that do not change its proof bytes.

The [signed-trace content review](SIGNED_TRACE_INDEPENDENT_REVIEW.md)
reconstructs the complete native trace, prime-square jump,
interpolation, half-plane reduction, and the exact historical
contract. Further scoped reviews cover the moving contour and the
causal/determinant theorems. All reviewers are AI agents; this is
not external human acceptance, integration, or Lean certification.
