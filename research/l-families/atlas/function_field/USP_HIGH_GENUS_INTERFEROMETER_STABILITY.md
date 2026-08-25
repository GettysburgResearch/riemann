# High-genus stability of Frobenius interferometers

## Read this first

The three genus-two subgroup selectors are **not ambient-null uniformly in
genus**.  For Haar `USp(2g)`, their means become exactly

\[
 (\mathbb E P,\mathbb E D,\mathbb E S)=(-2,6,-4)
\]

once each packet enters the Hughes--Rudnick Gaussian stable range.  Here

\[
 P=I_{2,2}-I_{4,4},\qquad
 D=-I_{1,1}+2I_{1,5}+I_{4,4},\qquad
 S=-2I_{2,8},
\]

with `I_(r,s)=Tr(U^r)Tr(U^s)-Tr(U^(r+s))`.  The source-locked `USp(4)`
means are all zero.  Thus the old nulling is a real low-rank cancellation,
not a genus-stable background subtraction.

The whole centered covariance stabilizes exactly at `g>=10`:

\[
 \operatorname{Cov}(P,D,S)=
 \begin{pmatrix}
 60&-52&8\\
 -52&104&-12\\
 8&-12&144
 \end{pmatrix}.
\]

Start with this note, inspect `usp_high_genus_interferometer_stability.json`
for the exact thresholds and source ledger, then read
`usp_high_genus_interferometer_stability.py` and
`test_usp_high_genus_interferometer_stability.py` for two independent
integer Wick evaluations.

## Status and scope

**Status:** exact compact-Haar consequences of an imported stable-range
theorem, plus a source-locked replay of the existing `USp(4)` calculations.

**Scope:** Haar `USp(2g)` trace polynomials only.  This packet constructs no
finite field, curve, family, Frobenius class, zero, or random sample.

**Exact sources or dependencies:** the project packet
`FROBENIUS_INTERFEROMETRY_SUBGROUP_SELECTORS.md`, its producer, and its tests
are locked by LF-normalized SHA-256.  The external theorem is quoted from
Entin--Pirani, [*Moments of traces of random symplectic matrices and
hyperelliptic L-functions*](https://arxiv.org/abs/2409.04844), equation
(1.4), equation (1.6), and the following paragraph, which records the
Hughes--Rudnick extension.

**What was actually run:** exact integer trace-polynomial algebra and cached
Wick contractions.  The producer refuses more than 4,096 accounted
contraction branches.  It performs no floating-point arithmetic, numerical
integration, or enumeration.

**Smallest remaining gap:** before these observables can be compared across
an arithmetic increasing-genus family, one needs a source-faithful family
and an equidistribution theorem uniform enough for the growing frequencies.
Neither is supplied here.

No external novelty claim is made for these compact-group consequences.

## 1. Imported stable-range theorem

Put

\[
 p_j(U)=\operatorname{Tr}(U^j),\qquad
 \eta_j=\mathbf 1_{2\mid j}.
\]

The imported theorem says that for independent standard real Gaussians
`X_1,X_2,...`, every trace monomial of weighted degree

\[
 \sum_j j a_j\le 2g+1
\]

has the exact Haar moment

\[
 \int_{USp(2g)}\prod_j p_j(U)^{a_j}\,dU
 =\mathbb E\prod_j\left(\sqrt j X_j-\eta_j\right)^{a_j}. \tag{1}
\]

This is an exact finite-`g` stable range, not a `g`-asymptotic approximation.
The theorem itself is imported and is not reproved by this packet.

Independence immediately gives

\[
 \mathbb E[p_rp_s]=r\mathbf 1_{r=s}+\eta_r\eta_s,
 \qquad
 \mathbb E[p_{r+s}]=-\eta_{r+s}.
\]

Therefore, whenever `r+s<=2g+1`,

\[
 \boxed{
 \mathbb E I_{r,s}
 =r\mathbf1_{r=s}+\eta_r\eta_s+\eta_{r+s}.} \tag{2}
\]

Equation (2) is the basic `g`-axis interferometer law.  It distinguishes
eventual exact stability from the special small-rank constant terms in the
genus-two packet.

## 2. The three selectors acquire universal ambient backgrounds

The exact comparison is:

| selector | source-locked `USp(4)` mean | stable mean | exact from genus |
|---|---:|---:|---:|
| `P=I_(2,2)-I_(4,4)` | `0` | `-2` | `g>=4` |
| `D=-I_(1,1)+2I_(1,5)+I_(4,4)` | `0` | `6` | `g>=4` |
| `S=-2I_(2,8)` | `0` | `-4` | `g>=5` |

The thresholds follow from the largest weighted degrees: eight for `P,D`
and ten for `S`.  For example, equation (2) gives

\[
 \mathbb E I_{2,2}=4,\qquad
 \mathbb E I_{4,4}=6,
\]

so `E[P]=-2`.  Likewise

\[
 \mathbb E I_{1,1}=2,\quad
 \mathbb E I_{1,5}=1,\quad
 \mathbb E I_{2,8}=2,
\]

which yields the other two entries.

This does not invalidate the genus-two subgroup signatures.  It changes how
they must be used across rank: a detector centered at zero for `USp(4)` must
be recentered by its rank-appropriate ambient expectation before a subgroup
contrast is interpreted.

## 3. Exact stable covariance

The producer expands each trace factor as

\[
 Z_j=\sqrt j X_j-\eta_j
\]

and applies integer Wick contractions.  Odd Gaussian multiplicities vanish;
an even multiplicity `2k` contributes `(2k-1)!! j^k`.  Frequencies are
independent.  No radicals remain in a nonzero term.

The stable second-moment matrix is

\[
 \mathbb E
 \begin{pmatrix}P\\D\\S\end{pmatrix}
 \begin{pmatrix}P&D&S\end{pmatrix}
 =
 \begin{pmatrix}
 64&-64&16\\
 -64&140&-36\\
 16&-36&160
 \end{pmatrix}.
\]

The complete displayed second-moment matrix is exact for `g>=10`; its
individual entries have the same thresholds as the covariance entries below.

After subtracting the mean outer product, the covariance is

\[
 \boxed{
 \begin{pmatrix}
 60&-52&8\\
 -52&104&-12\\
 8&-12&144
 \end{pmatrix}.} \tag{3}
\]

The entrywise least stable genera are

\[
 \begin{pmatrix}
 8&8&9\\
 8&8&9\\
 9&9&10
 \end{pmatrix}.
\]

Hence all of (3) is exact for `g>=10`.  Its leading principal minors are
`60`, `3536`, and `503872`, so it is positive definite.  The locked
genus-two covariance was

\[
 \begin{pmatrix}
 24&-20&4\\
 -20&48&0\\
 4&0&40
 \end{pmatrix};
\]

both the bias and the noise geometry therefore change between genus two and
the stable high-genus regime.

## 4. The inverse-design pool exposes the same drift

For the raw pool

\[
 (I_{1,7},I_{1,9},I_{2,4},I_{2,8}),
\]

the source-locked `USp(4)` mean vector is `(0,0,0,0)`, while the stable mean
vector is

\[
 (1,1,2,2). \tag{4}
\]

All four entries of (4) are exact simultaneously for `g>=5`.  The previous
inverse-design winner

\[
 F_*=2I_{1,7}+4I_{1,9}-I_{2,4}+I_{2,8}
\]

therefore has stable ambient mean `6`, despite having zero `USp(4)` mean.

Because every pool coordinate is already `USp(4)`-mean-null, the simultaneous
`USp(4)` and stable mean-null lattice is exactly

\[
 \boxed{c_1+c_2+2c_3+2c_4=0}. \tag{5}
\]

One primitive integral basis is

\[
 (-1,1,0,0),\qquad(-2,0,1,0),\qquad(-2,0,0,1).
\]

Equation (5) is only a statement about Haar means.  It gives neither
pointwise vanishing nor an `L^2` nullspace.

## 5. Interpretation and firewalls

The exact project lesson is methodological: a low-genus ambient-null filter
need not remain null as genus grows, even before any arithmetic corrections
enter.  The stable-range theorem supplies the universal recentering and the
correct covariance scale at essentially no computational cost.

Nothing here proves:

- equidistribution of a named arithmetic family as `g` grows;
- that a finite-family anomaly identifies a subgroup, split Jacobian,
  endomorphism, correspondence, or motive;
- that the compact transition survives a coupled `(q,g)` limit;
- a low-lying-zero or central-rank law; or
- any RH or GRH consequence.

The phrase “high genus” in this packet refers only to the exact compact Haar
stable range.  It does not name an arithmetic limiting process.

## 6. Replay

From the repository root:

```text
python research/l-families/atlas/function_field/usp_high_genus_interferometer_stability.py --check
python -O research/l-families/atlas/function_field/usp_high_genus_interferometer_stability.py --check
python tests/test_usp_high_genus_interferometer_stability.py
python -O tests/test_usp_high_genus_interferometer_stability.py
```

The stored JSON also records the exact source hashes, stable thresholds,
second moments, covariance, null lattice, contraction ledger, and canonical
payload hash.
