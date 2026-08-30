# Shared-fibre Wick occupancy spectrum

Status: **exact fixed-fibre source map, arbitrary-occupancy operator identity,
and residue-only forgetting no-go; live occupancy and global signed
recombination remain open**

Scope: distinct odd prime marked conductors in one complete bilateral fibre;
exact rational algebra for every such pair; dependency-free finite controls
at \((3,5),(3,7),(5,7)\) and the held-out pair \((7,11)\). There is no
constructible sheaf, partial-Frobenius descent, trace estimate, principal
binding, RH, or GRH theorem here.

Exact sources or dependencies:
[ffps_shared_fibre_wick_occupancy_spectrum.sources.json](ffps_shared_fibre_wick_occupancy_spectrum.sources.json).

What was actually run:
[ffps_shared_fibre_wick_occupancy_spectrum.py](ffps_shared_fibre_wick_occupancy_spectrum.py)
and its unit tests.

Canonical output:
[ffps_shared_fibre_wick_occupancy_spectrum.json](ffps_shared_fibre_wick_occupancy_spectrum.json).

Smallest remaining gap: determine the actual occupied physical cells,
multiplicities, and coefficients in the complete live source before the
conductor sum. The quotient occupancy remains a finite gate. The aggregate
residue trace alone provably loses literal diagonal energy.
The live occupancy remains open.

## 0. Verdict

The Wick pair in L-106191.5 and T-106140.4 is formed inside one
**shared marked fibre**

\[
 \iota=(g,\ell,\rho,\sigma,\tau),\qquad \ell\ne\rho.
\tag{0.1}
\]

The two atoms have independent owner, cofactor, and all other literal source
labels, but the same marked conductors and owner classes. Across the full
family the correct carrier is

\[
 \boxed{
 \mathscr W^{(2)}
 =
 \left(\Omega\times_{\mathcal I}\Omega\right)
 \setminus\Delta_{\Omega/\mathcal I}.}
\tag{0.2}
\]

It is **not an independent marked-place product**. In particular, a model
with independent pairs \((\ell_0,\rho_0)\) and \((\ell_1,\rho_1)\) cannot
even form the common additive orthogonality kernels modulo one \(\ell\) and
one \(\rho\).

This packet proves the exact replacement:

1. an explicit fixed-fibre owner/cofactor residue envelope and physical map;
2. the exact Wick operator for arbitrary live occupancy;
3. a complete-cell spectrum, used only as a finite algebraic control;
4. an exact no-go showing that residue aggregation alone loses the literal
   diagonal energy required by Wick normal ordering.

The complete-cell operator is full-rank indefinite. That statement does not
promote: a singleton occupancy is zero, and a nontrivial six-cell occupancy
is singular. No noncancellation of the native fibre or globally recombined
source is proved.

## 1. Frozen provenance

The machine source lock authenticates eight exact Git blobs.

| role | commit | blob | exact content used |
|---|---|---|---|
| Gate-0 shared-coordinate firewall | b8cf095e7446583af80cbe4ff5d04257b6901d97 | aad29a0401d0f26c3dceadaaaaf017af6da95ec1 | the two Wick orientations decorate one shared-coordinate graph, not its Cartesian square |
| Gate-0 native source manifest | same | b62cc787177e51bd89ef33307bd08916c16d8d1d | predecessor source identities and blobs |
| trace tensor closure | 3a595dda92ef827a41e50d2395309692a93748ad | 37647db8c43b983dc64bfc71a0c112539119a98a | ONEPLACEWEIL, RELTRACE, signed recombination boundary |
| external-plus-diagonal Adams | same | 884f2fc949bbd5b076df0c0c7afd4711f81ce37e | literal diagonal must remain a separate Adams datum |
| L-106120 | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | a8d829dc10611adb7bfb4853902bdff0ab02a065 | fixed bilateral fibre, owner classes, complete atom phase |
| L-106131 | same | 37722c3f36ec7d1681f34d4329a3795e5028f7ae | Wick before collapse, singleton firewall, centered background |
| L-106191 | same | 85c4ef92ead7d8b235f9c195c3c0acd16d16030f | source-dual normalization and off-atomic centered kernel |
| T-106140 | same | d5be8e376c88b63de0be19e0d9e8791624e99ae2 | complete source labels, WCADD/WCKUM, principal conclusion chain |

The native load-bearing locations are L-106120.1--.5,
L-106131.6--.15, L-106191.1--.10, and T-106140.1--.14. The source
lock compares each exact commit:path to its Git blob. A shallow clone that
lacks the sibling objects must fetch, without merging,

    git fetch --no-tags origin b8cf095e7446583af80cbe4ff5d04257b6901d97 3a595dda92ef827a41e50d2395309692a93748ad 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b

The replay fails closed if any object is absent or changed.

## 2. MPD-W2.1 — the source-faithful shared-fibre map

Fix (0.1). A literal atom has

\[
 \omega=(P,Q,c,d;\beta),\qquad
 c=\ell u,\qquad d=\rho v,
\tag{2.1}
\]

where \(\beta\) retains every Boolean, shell, carrier, endpoint-colour,
marked-prime, renewal, and other source label. L-106120.3 gives

\[
 \ell\mid N,\quad\ell\nmid M,\qquad
 \rho\mid M,\quad\rho\nmid N.
\tag{2.2}
\]

Consequently \(Q,v\) are units modulo \(\ell\), and \(P,u\) are units
modulo \(\rho\). Put

\[
 \bar Q=Q\bmod\ell,\quad \bar v=v\bmod\ell,\qquad
 \bar P=P\bmod\rho,\quad \bar u=u\bmod\rho.
\tag{2.3}
\]

The phase in L-106120.5 is

\[
 e_\ell(-hQd^2)e_\rho(kPc^2).
\]

Thus the exact physical residue map is

\[
 \boxed{
 r_\iota(\omega)=(x_\omega,y_\omega),\qquad
 x_\omega=-\rho^2\bar Q\bar v^2\bmod\ell,\quad
 y_\omega=\ell^2\bar P\bar u^2\bmod\rho.}
\tag{2.4}
\]

This agrees with L-106191's convention
\(e_\ell(hx_\omega)e_\rho(ky_\omega)\). If one instead names
\(Y=Qd^2\), then \(x=-Y\); equality is unchanged.

The fixed owner classes are

\[
 \kappa_\ell(\bar Q)=\sigma,\qquad
 \kappa_\rho(\bar P)=\tau.
\]

Hence the ambient cell set is

\[
 \mathcal A_\iota
 =
 \mathcal Q_\ell^{\,\kappa_\ell(-1)\sigma}
 \times
 \mathcal Q_\rho^{\,\tau},
\qquad
 |\mathcal A_\iota|=m_\ell m_\rho,
\qquad
 m_q={q-1\over2},
\tag{2.5}
\]

where \(\mathcal Q_q^\epsilon\) is one raw Legendre class of nonzero
residues. This is not L-106131's sign-pair quotient. The cardinalities agree,
but the sets are not being identified.

### Exact envelope theorem

Let

\[
 \mathcal E_\iota
 =
 \mathcal Q_\ell^\sigma\times\mathbf F_\ell^\times
 \times\mathcal Q_\rho^\tau\times\mathbf F_\rho^\times
\tag{2.6}
\]

carry \((\bar Q,\bar v,\bar P,\bar u)\), and apply (2.4).
Every cell of \(\mathcal A_\iota\) has exactly

\[
 \boxed{(\ell-1)(\rho-1)}
\tag{2.7}
\]

preimages. Indeed, for a fixed \(x\) and each nonzero \(\bar v\), equation
(2.4) determines the unique \(\bar Q\), automatically in class \(\sigma\).
The right coordinate is identical.

Equation (2.7) is an ambient residue-envelope theorem, not live occupancy.
The native horizon, owner arithmetic, least-prime conditions, shell, Boolean,
carrier, endpoint, renewal, and other labels can remove tuples or introduce
different multiplicities. The producer exhausts (2.6) only as a finite
coverage control.

A second atom \(\omega'\) has independent primed versions of every coordinate
in (2.1)--(2.3), but shares (0.1). This is the requested relative
self-product. It introduces independent atom data without inventing
independent marked conductors.

## 3. MPD-W2.2 — exact arbitrary-occupancy pullback

Restrict the centered incidence kernel of L-106191.5 to the raw classes
(2.5). Define

\[
 H_q=I_{m_q}-{1\over q}J_{m_q},\qquad
 S_{\ell,\rho}=H_\ell\otimes H_\rho,
\tag{3.1}
\]

and

\[
 d_{\ell,\rho}
 =
 \left(1-{1\over\ell}\right)
 \left(1-{1\over\rho}\right).
\tag{3.2}
\]

The notation \(H_q\) is deliberate: L-106131 already uses \(C_q\) for a
different principal rank-one operator.

Let \(\Omega_\iota\) be any finite literal atom set actually present in the
fibre, and let

\[
 R_\iota:\mathbf C^{\Omega_\iota}\longrightarrow
 \mathbf C^{\mathcal A_\iota},
\qquad
 (R_\iota z)_a
 =
 \sum_{r_\iota(\omega)=a}z_\omega
\tag{3.3}
\]

be residue aggregation.

The display uses scalar coefficients for spectral clarity. For the
Hilbert-valued coefficients of L-106131, tensor every cell space with the
coefficient Hilbert space and replace scalar products by its inner product;
the same operator identity and diagonal-energy ledger hold.

### Theorem MPD-W2.2

The exact normalized L-106191.5 Wick form on this fibre is

\[
 \boxed{
 B_{R_\iota}
 =
 R_\iota^*S_{\ell,\rho}R_\iota
 -d_{\ell,\rho}I_{\Omega_\iota}.}
\tag{3.4}
\]

Equivalently,

\[
 \boxed{
 z^*B_{R_\iota}z
 =
 (R_\iota z)^*S_{\ell,\rho}(R_\iota z)
 -d_{\ell,\rho}\sum_\omega|z_\omega|^2.}
\tag{3.5}
\]

### Proof

The matrix entry of \(S_{\ell,\rho}\) between physical cells is

\[
 \left(\mathbf1_{x=x'}-{1\over\ell}\right)
 \left(\mathbf1_{y=y'}-{1\over\rho}\right).
\tag{3.6}
\]

Pullback by \(R_\iota\) places (3.6) between every ordered literal atom pair.
Its atom diagonal is the constant (3.2). Subtracting
\(d_{\ell,\rho}I\) removes exactly \(\omega=\omega'\) and nothing else.
This is L-106191.5. \(\square\)

The formula gives the exact occupancy reduction. If \(S\subseteq\mathcal
A_\iota\) is the occupied cell set and \(n_a\) its multiplicity, then

\[
 \ker R_\iota
 =
 \bigoplus_{a\in S}
 \left\{z\text{ on }r^{-1}(a):\sum z_\omega=0\right\},
\tag{3.7}
\]

and

\[
 \boxed{
 B_{R_\iota}|_{\ker R_\iota}
 =-d_{\ell,\rho}I.}
\tag{3.8}
\]

On the orthogonal cell-sum complement, \(B_{R_\iota}\) is unitarily
equivalent to

\[
 M^{1/2}(S_{\ell,\rho})_S M^{1/2}
 -d_{\ell,\rho}I_S,
\qquad M=\operatorname{diag}(n_a).
\tag{3.9}
\]

Thus all remaining finite spectral uncertainty is the actual occupied
principal submatrix and multiplicity matrix. Equation (3.9) is a reduction,
not an evaluation of native occupancy.

## 4. MPD-W2.3 — complete-cell spectrum

As an exact control, retain one atom in every cell of (2.5). Then \(R=I\)
and

\[
 B_{\mathrm{full}}
 =
 H_\ell\otimes H_\rho-d_{\ell,\rho}I.
\tag{4.1}
\]

Put

\[
 a_q=1-{m_q\over q}={q+1\over2q}.
\tag{4.2}
\]

The spectrum over \(\mathbf Q\), and hence over \(\mathbf C\), is

| eigenspace | eigenvalue | multiplicity |
|---|---:|---:|
| mean-zero \(\otimes\) mean-zero | \(1-d\) | \((m_\ell-1)(m_\rho-1)\) |
| mean-zero \(\otimes\) constant | \(a_\rho-d\) | \(m_\ell-1\) |
| constant \(\otimes\) mean-zero | \(a_\ell-d\) | \(m_\rho-1\) |
| constant \(\otimes\) constant | \(a_\ell a_\rho-d\) | \(1\) |

Every eigenvalue with nonzero multiplicity is nonzero for distinct odd
primes. The only possible cross zero satisfies

\[
 a_\rho-d=0
 \Longleftrightarrow
 (\ell-2)(\rho-3)=4,
\tag{4.3}
\]

so the only odd-prime solution is \((3,7)\), where its multiplicity
\(m_\ell-1\) is zero. The other cross term is symmetric. Finally,

\[
 a_\ell a_\rho-d=0
 \Longleftrightarrow
 (3\ell-5)(3\rho-5)=16,
\tag{4.4}
\]

whose only odd-prime solution is \(\ell=\rho=3\), excluded.

The matrix is indefinite. If \(\ell,\rho\ge5\), then \(1-d>0\) is present
and \(a_\ell a_\rho-d<0\). If \(\ell=3<\rho\), then

\[
 a_\ell-d={2\over3\rho}>0,\qquad
 a_\ell a_\rho-d={3-\rho\over3\rho}<0,
\]

and the other orientation is symmetric. Therefore

\[
 \boxed{
 \operatorname{rank}B_{\mathrm{full}}=m_\ell m_\rho,
 \qquad B_{\mathrm{full}}\text{ is indefinite}.}
\tag{4.5}
\]

This proves neither positivity nor cancellation. It authenticates the
centered background and shows that literal Wick deletion is not the zero
operation on a fully occupied cell panel.

If the entire ambient residue envelope (2.6) were retained once, every cell
would have uniform multiplicity \(n=(\ell-1)(\rho-1)\). Formula (3.9)
then gives \(m_\ell m_\rho\) positive cell-sum eigenvalues and
\((n-1)m_\ell m_\rho\) negative within-cell eigenvalues. This is again an
envelope control, not a source-realization theorem. Indeed \(n\ge8\), every
eigenvalue of \(H_\ell\otimes H_\rho\) is greater than \(1/4\), and
\(d<1\), so the cell-sum eigenvalues \(n\lambda-d\) are positive.

## 5. MPD-W2.4 — residue-only forgetting no-go

Equation (3.5) separates two pieces:

\[
 a=R_\iota z,
\qquad
 D=\sum_\omega|z_\omega|^2.
\tag{5.1}
\]

The first is the aggregate physical residue trace. The second is literal
diagonal energy. The first does not determine the second.

Conversely, the two-channel pair

\[
 \boxed{\left(R_\iota z,\ \sum_\omega|z_\omega|^2\right)}
\tag{5.2}
\]

is an exact sufficient statistic for the fixed-fibre Wick scalar, by (3.5).
This is a concrete replacement target for a scalar ONEPLACEWEIL
adapter: one physical aggregate channel plus one literal diagonal-energy
channel.

Take two distinct literal atoms in one physical cell and coefficients
\(z=(1,-1)\). Then

\[
 R_\iota z=0,
 \qquad
 z^*B_{R_\iota}z=-2d_{\ell,\rho}\ne0.
\tag{5.3}
\]

The zero coefficient vector has the same residue aggregate and a different
Wick value. Hence:

> **MPD-W2.4 — residue-only forgetting no-go.** Any scalar adapter which
> retains only \(R_\iota z\) and forgets \(D\) cannot reconstruct native
> literal Wick normal ordering for all source coefficients.

This is a no-go for a residue-only trace pushforward, not for every derived
or correspondence category. PR #760's external-plus-literal-diagonal
formalism retains exactly the extra datum that (5.3) forces.

### Counterfeit controls

Three controls prevent stronger misreadings.

1. **Singleton.** One literal atom has matrix \([0]\), exactly as
   L-106131.9 requires. Thus full rank in (4.5) is not hereditary.
2. **Collision-only deletion.** With one atom per cell, retaining only the
   strict joint collision and deleting the literal diagonal gives the zero
   matrix. The true matrix (4.1) is full rank because the one-coordinate and
   constant centered backgrounds are load-bearing.
3. **Nontrivial singular occupancy.** For \((\ell,\rho)=(5,11)\), occupy
   the \(2\times3\) rectangle

   \[
   T=\{0,1\}\times\{0,1,2\}
   \subset\mathcal Q_5^\epsilon\times\mathcal Q_{11}^{\epsilon'}.
   \]

   In row-major order,

   \[
   55B_T=
   \begin{pmatrix}
   0&-4&-4&-10&1&1\\
   -4&0&-4&1&-10&1\\
   -4&-4&0&1&1&-10\\
   -10&1&1&0&-4&-4\\
   1&-10&1&-4&0&-4\\
   1&1&-10&-4&-4&0
   \end{pmatrix}.
   \tag{5.4}
   \]

   The vector \((-1,-1,-1,1,1,1)\) is null, so
   \(\operatorname{rank}B_T=5\). This is an exact incomplete-occupancy
   obstruction even without duplicate cells.

The live source might occupy a nonsingular panel, a singular panel, or a
weighted combination across fibres. The present sources do not decide which.

## 6. The relative geometry and principal ledger

The Wave-2 theorem changes the required interface but closes no global gate.

| stage | exact status after Wave 2 | remaining burden |
|---|---|---|
| correct Wick carrier | **PROVED** | retain \(\Omega\times_{\mathcal I}\Omega-\Delta\), never independent conductors |
| physical map | **PROVED ON THE RESIDUE ENVELOPE** | classify the actual live image, multiplicities, and coefficients |
| fixed-fibre Wick algebra | **PROVED FOR ARBITRARY OCCUPANCY** | exploit (3.9) without taking fibrewise absolute values |
| residue-only scalar pushforward | **REFUTED AS SUFFICIENT** | retain literal diagonal energy or an equivalent external-plus-diagonal object |
| complete signed pushforward / RELPARTFROB | **OPEN** | construct the complete relative object with all source labels and compatible partial Frobenii |
| ONEPLACEWEIL | **OPEN** | realize complete one-sided amplitudes together with the atom map and diagonal datum, uniformly |
| WCADD / WCCORR | **OPEN** | prove coherent additive conductor recombination before absolute value |
| WCKUM | **OPEN** | control mixed and double nonprincipal Kummer channels with centered backgrounds |
| ONEPLACETRACE / RELTRACE | **OPEN** | prove the required signed Adams--Möbius trace estimate |
| principal binding | **OPEN** | identify the exact T-106140 horizon, endpoint, diagonal, and normalization |
| frozen consumer | conditional only | still requires every preceding open gate |

The exact conclusion-facing identity remains

\[
 \mathfrak A^\circ
 =
 \mathfrak P^\circ+\mathfrak K^\circ.
\tag{6.1}
\]

Consequently the principal chain remains

    WCADD/WCCORR + WCKUM
      -> principal off-atomic moment
      -> exact principal binding
      -> frozen BCI consumer
      -> RH.

Neither input estimate is proved. Indefiniteness in (4.5) is not an estimate,
and the singular control (5.4) rules out inferring one from complete-cell
rank.

## 7. Wave-2 programme boundary map

The programme now has four contrasting mechanisms.

| lane | exact object already available | honest next theorem |
|---|---|---|
| source occupancy | (2.4), (3.4), and the equal/distinct-output split of L-106191 | classify a live dangerous \(u=v=1\) occupancy slice, including multiplicities and coefficient signs |
| relative geometry | Gate-0 support shift and PR #760 external-plus-diagonal Adams | construct or refute a source-faithful atom-and-diagonal ONEPLACEWEIL object with commuting partial Frobenii |
| additive cancellation | bounded centered kernel and WCADD \(=\) WCCORR | prove one signed conductor block estimate that keeps equal and distinct outputs together |
| Kummer/principal route | L-106131 four-channel identity and T-106140 principal recombination | prove a compatible WCKUM or RELTRACE estimate and bind it coefficientwise to the frozen horizon |

Ranked continuation queue:

1. **Live occupancy first.** Freeze the smallest dangerous \(u=v=1\)
   conductor block and determine its exact cell image, multiplicity matrix,
   equal-output partition, and coefficient pattern. Formula (3.9) then gives
   an honest theorem, singularity, or no-go.
2. **Atom-plus-diagonal geometry.** Build the smallest one-place adapter that
   retains both \(Rz\) and \(D\), then test partial Frobenius and closed-point
   Adams. A residue-only adapter should no longer be attempted.
3. **Signed conductor recombination.** Seek cancellation in the assembled
   occupancy forms before an outer absolute value; a source-blind Schur or
   energy bound is excluded by L-106191.
4. **Kummer and principal binding.** Only after a compatible additive or
   relative trace estimate exists, close WCKUM and audit the exact
   T-106140 normalization against the frozen consumer.

These lanes are complementary. The finite occupancy theorem is not a reason
to abandon the geometric, additive, or Kummer programmes.

## 8. Proof and computation ledger

| item | grade |
|---|---|
| exact source commits and blobs | **AUTHENTICATED BY GIT OBJECT LOOKUP** |
| shared-fibre versus independent-product ontology | **PROVED FROM THE NATIVE ORDER OF SUMMATION** |
| owner/cofactor physical map (2.4) | **PROVED FROM L-106120.3--.5** |
| uniform residue-envelope fibres (2.7) | **PROVED AND EXHAUSTIVELY REPLAYED ON THE FINITE CONTROLS** |
| arbitrary-occupancy identity (3.4) | **PROVED EXACTLY** |
| kernel and quotient spectral reduction (3.8)--(3.9) | **PROVED EXACTLY** |
| complete-cell spectrum and full rank | **PROVED FOR ALL DISTINCT ODD PRIMES** |
| finite panels and held-out panel | **EXACT RATIONAL / CERTIFIED INTEGER COVERAGE** |
| residue-only forgetting no-go | **PROVED BY (3.5) AND THE EXACT COUNTEREXAMPLE (5.3)** |
| singleton, collision-only, and singular-subset controls | **REPLAYED EXACTLY** |
| live source occupancy | **NOT PROVED** |
| native fixed-fibre or global noncancellation | **NOT PROVED** |
| ONEPLACEWEIL, RELPARTFROB, RELTRACE, principal binding | **NOT PROVED** |
| RH or GRH | **UNPROVED** |

No external novelty or priority claim is made for fibre products, incidence
matrices, tensor spectra, or Wick pullbacks separately. The project-specific
advance is the source-locked identification of the correct fixed-fibre
occupancy operator and the exact diagonal-energy loss under physical residue
forgetting.

## 9. Replay and resource boundary

Run from the repository root:

    python -B research/l-families/atlas/function_field/ffps_shared_fibre_wick_occupancy_spectrum.py --check
    python -B -O research/l-families/atlas/function_field/ffps_shared_fibre_wick_occupancy_spectrum.py --check
    python -B -m unittest tests.test_ffps_shared_fibre_wick_occupancy_spectrum
    python -B -O -m unittest tests.test_ffps_shared_fibre_wick_occupancy_spectrum

The replay uses only exact integers and rational arithmetic. It enumerates at
most 900 ambient residue-envelope tuples and materializes simple matrices of
dimension at most 15. It enumerates no live source family, curve, sheaf,
closed-place tower, or L-function zero and performs no floating-point
operation.

The Wave-2 statement is therefore:

> The native shared-fibre Wick form admits the exact arbitrary-occupancy
> pullback (3.4), and residue aggregation without literal diagonal energy is
> insufficient. Quotient occupancy remains a finite gate. Complete signed
> noncancellation, descent, ONEPLACEWEIL, RELTRACE, principal binding, RH and
> GRH are not proved. RH and GRH remain unproved.
