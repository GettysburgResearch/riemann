# Moving labels, sixth-power strata and the full A2 norm

This packet strengthens the positive Gauss-family estimate and carries it through the **entire arithmetic A2 correction sum**. At physical arithmetic row height \(H=D^{1/2}\), the normalized full A2 polynomial now satisfies the proposed source-conditional bound

\[
\boxed{\sum_{k\asymp D^{1/2}}|\mathscr Q_{1,1}(D,D;k)|^2
\ll_\epsilon D^{31/19+\epsilon}.}
\]

The preceding packet obtained \(D^{379/228+\epsilon}\) for the all-row raw two-axis family. The new exponent is smaller by \(7/228\), and the improved estimate now includes every correction label in the full normalized A2 polynomial. Moving exclusions and auxiliary twists have explicit uniform costs.

Two complementary deductions are included. An exact graph argument controls overlapping signed fourth-moment cross-gcd events through a larger range and gives a fixed-matching theorem at every fixed even order. Combining the canonical completed blocks with the recent fixed-order large sieve also extends their spectral mean domain from \(\Re u>5/8\) to \(\Re u>4/7\).

**Research status.** These are proposed source-conditional analytic deductions, with complete arguments, scoped AI-agent reviews, exact source pins and finite diagnostics. The imported theta framework is an assumption. The stronger scalar and signed-sector versions retain the additional inputs stated below. No new full inverse-Möbius moment or zero-free boundary is established. The previous proposed source-conditional boundary \(139999/160000\) remains unchanged; \(17/24\), the cofinal higher-moment hierarchy and RH remain open. These results have not been promoted to the integrated record or formalized in Lean.

Parent: PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`. All earlier packets remain frozen. [SOURCE_LOCK.json](SOURCE_LOCK.json) binds the inherited foundation and adjacent inputs to exact commit paths, Git blobs, byte counts and SHA-256 hashes.

## 1. What changed

| Object | Previous result or missing step | Result in this packet |
|---|---|---|
| Completed two-axis Gauss norm | Unit labels, or a single auxiliary | Both moving labels, their overlaps, every row valuation and an outer inverse mask; costs \(1,FQ,F^{2/3}Q^{1/3}\) |
| All-row raw energy at \(H=D^{1/2}\) | \(D^{379/228+\epsilon}\) | \(D^{31/19+\epsilon}\) |
| Raw energy at the \(D^2\) scale, unit labels | Through \(H\le D^{114/151}\) | Through \(H\le D^{19/24}\) |
| Full normalized A2 correction sum | Stronger raw bound had not been summed with its moving labels and corrected scales | Inherits the entire improved six-term envelope, including \(D^{31/19+\epsilon}\) |
| Union of four signed fourth-moment cross-gcd events | The earlier sharper range used a disjointness condition | All 15 nonempty intersections handled; at \(b=7/8\), the single-edge cost survives through \(R\le D^{4/5}\) |
| Higher moments | Selected earlier incidence sectors | Every fixed disjoint cross matching at every fixed even order, with explicit loss |
| Canonical all-row spectral mean | Baseline \(\Re u>5/8\) | \(\Re u>4/7\), using the separately credited de Faveri theorem |

The numbers \(19/24\) and \(4/7\) describe an arithmetic row-height range and a spectral mean domain, respectively. Neither is a new boundary for zeros of the Riemann zeta function.

## 2. The two cutoffs that make the norm gain possible

### First cutoff: adapt to the sixth-power part of the row

Keep the exact decomposition

\[
k=\varepsilon v^6k_0,
\]

where \(k_0\) is sixth-power-free. It may share primes with \(v\). The exact character zeros turn \(v\) into a moving exclusion on the physical columns. The exclusion's ideal norm grows by at most \(Nv\), while its row range has shrunk from \(H\) to \(H/(Nv)^6\).

For a cube inverse with parent cutoff \(R\), use

\[
R_v=\min(KB^{1/3},R\,Nv).
\]

The cap is chosen from the fixed physical support. At the cap the long tail is exactly empty. Below it, the stronger sixth-power-free row sieve applies. Summing the energies of these disjoint row classes produces convergent ideal sums. This removes the extra \(H^{1/6}\) factor from the long-tail column term **for this structured family**. The generic all-row sieve still contains that factor.

The exact proof is [SIXTH_POWER_STRATIFIED_INVERSE.md](SIXTH_POWER_STRATIFIED_INVERSE.md); the required moving exclusions are established in [MIXED_LABEL_COMPLETION.md](MIXED_LABEL_COMPLETION.md).

### Second cutoff: adapt to the shortened A2 axis

The full A2 coefficient has correction labels \(c,d,e\). With \(u=Nc,v=Nd,w=Ne\), its normalized forward projection has weight

\[
u^{-1}v^{-1}w^{-3/2},
\]

and child scales

\[
A_t=D u^{-1}v^{-2}w^{-2},\qquad
B_t=D u^{-2}v^{-1}w^{-2}.
\]

Use the separate child cutoff

\[
\boxed{R_t=R(B_t/D)^{1/3}.}
\]

Some children have \(R_t<1\); their short inverse is empty, and the long-tail estimate remains valid. The mixed-label norm, exact A2 weights and shortened lengths now combine into summable correction powers. There is one harmonic correction sum in the angular term and two in the harmless \(H\) term. The complete correction norm costs at most a fixed power of \(\log D\).

The proof, including all six norm-exponent triples and the exact phase/overlap identity, is [ANISOTROPIC_A2_NORM_TRANSFER.md](ANISOTROPIC_A2_NORM_TRANSFER.md). It bounds the whole A2 sum; no correction labels have been omitted.

## 3. Quantitative theorem and assumptions

Let the squarefree starting exclusion and auxiliary be \(q_0,f_0\), with overlap allowed, and set

\[
Q=N\bigl(q_0/(q_0,f_0)\bigr),\qquad F=Nf_0.
\]

Fix a polynomial ceiling \(C_0\): all arithmetic scales and moving-label norms are at most \(D^{C_0}\), with the support-dependent lower-scale conventions in the manuscripts. The implicit constants may depend on \(C_0\) and the fixed smooth tests. The free inverse cutoff \(R\) may be any positive real number. All physical character zeros remain. The normalization is
\(\mathscr Q(D,D)=Q_{\mathrm{unnormalized}}(D,D)/D\).

For a scalar exponent \(1/2<\beta\le1\), every \(R>0\) gives

\[
\begin{aligned}
\sum_{k\asymp H}|\mathscr Q_{q_0,f_0}(D,D;k)|^2
\ll_\epsilon D^\epsilon\bigl[&HD
+FQH^2D^{\beta-1/2}R^{9/2-3\beta}\\
&+F^{2/3}Q^{1/3}H^{4/3}D^{2/3}R^2
+H+D^2R^{-3}+(HD^2)^{2/3}R^{-2}\bigr].
\end{aligned}
\]

Every nonzero element row is included. With the source-conditional angular input, \(\beta=11/12\) denotes the bound with an arbitrarily small final epsilon loss, obtained using a fixed contour strictly to the right of the reciprocal threshold. No endpoint reciprocal estimate is asserted.

Optimizing the two increasing terms against \(D^2R^{-3}\) yields

\[
\boxed{
\sum_{k\asymp H}|\mathscr Q_{q_0,f_0}(D,D;k)|^2
\ll_\epsilon D^\epsilon
\max\left\{
D^{6/5}H^{4/5}F^{2/5}Q^{1/5},
DH^{24/19}(FQ)^{12/19}
\right\},
\quad H^2FQ\le D^{19/12}.
}
\]

In particular, with unit labels, the two regimes are

\[
\begin{cases}
D^{6/5+\epsilon}H^{4/5},&1\le H\le D^{19/44},\\
D^{1+\epsilon}H^{24/19},&D^{19/44}\le H\le D^{19/24}.
\end{cases}
\]

At \(H=D^{1/2}\), moving labels give

\[
D^{31/19+\epsilon}(FQ)^{12/19},\qquad FQ\le D^{7/12}.
\]

The same estimates hold for the normalized raw two-axis polynomial. If the angular reciprocal input is omitted, scalar counting gives \(\beta=1\), the envelope

\[
\max\{D^{6/5}H^{4/5}F^{2/5}Q^{1/5},\ DH^{4/3}(FQ)^{2/3}\},
\quad H^2FQ\le D^{3/2},
\]

and the unit-label exponent \(5/3\) at \(H=D^{1/2}\). This version still uses the explicitly inherited theta and classical sieve foundations.

## 4. Actual signed sectors and the generalized moment direction

The signed argument uses \(H=D^h\), with \(h>1\) fixed, and \(1\le R\le D\). Its native moving-mask second moment is uniform over every shorter nonempty column scale and every polynomially bounded moving mask, all at that same physical row height. A stronger version also assumes a uniform pointwise exponent \(b\in(1/2,1]\); \(b=1\) follows by counting. A bound for one fixed character with unspecified conductor constants does not supply the stronger uniform premise. This signed-sector regime is separate from the Gauss example at \(H=D^{1/2}\) above.

For the fourth moment, let the four cross-gcd events be
\(N(n_i,m_j)\ge D/R\), and retain the original two within-side gcd restrictions. The union is a signed sum. Exact inclusion–exclusion divides its intersections into four single edges, two matchings, four stars, four paths and one cycle. The residual gcd in the cycle is controlled by a new bounded-gcd-selector covariance lemma.

With \(a=2b-1\), the resulting bound is

\[
|\mathcal U_C(D/R)|
\ll_\epsilon HD^\epsilon
\left[D^2R^a+D^{3/2}R^{b+1/2}+DR^2\right].
\]

The sharper single-edge cost \(HD^{2+\epsilon}R^a\) therefore survives through

\[
R\le D^{1/(3-2b)}.
\]

At \(b=7/8\), this is \(R\le D^{4/5}\). A polynomial choice of \(R\) still has the displayed polynomial loss; it does not close the entire fourth moment.

For each fixed \(2k\)-th moment and a fixed set of \(m\) disjoint cross edges, the analogous signed sector satisfies

\[
|\mathcal G_m^\Theta(D/R)|
\ll_\epsilon HD^{k+a(k-1-m)+\epsilon}R^{am},
\qquad 0\le m\le k-1.
\]

For a full \(k\)-edge matching the bound is
\(HD^{k+\epsilon}R^{a(k-1)}\). At \(m=k-1\), a subpower \(R\) gives the diagonal moment scale for that specified sector. The theorem permits the stated one-sided shared-incidence selectors and preserves overlaps between labels belonging to different edges. It does not sum all possible overlapping higher-order matching events automatically.

Complete proofs are in [CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md](CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md).

## 5. A second combination: the spectral line reaches 4/7

[ALL_ROW_SPECTRAL_MEAN.md](ALL_ROW_SPECTRAL_MEAN.md) first supplies the all-row canonical mean at \(a=\Re u>5/8\), using the older sieve and the imported completed block estimate. This baseline is preserved.

[OPTIMAL_SIEVE_SPECTRAL_EXTENSION.md](OPTIMAL_SIEVE_SPECTRAL_EXTENSION.md) adds Alexandre de Faveri's *Optimal large sieve for fixed order characters*, [arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), Theorem 1.1. Its sixth-order operator and exact all-row adapter give the block envelope

\[
H+H^{1/6}X+H^{5/6}X^{1/3}+H^{1/3}X^{5/6}.
\]

Compare each nonconstant term with the completed bound \(H+H^2F/X\), then sum the Mellin-weighted dyadic blocks. The three crossover restrictions are \(a>6/11\), \(a>4/7\) and \(a>11/20\). Thus the canonical series has

\[
\boxed{
\sum_{0<Nk\ll H}|G_{k,d}(a+it)|^2
\ll H^{1+\epsilon}(Nd)^{1-a+\epsilon}(2+|t|)^M,
\qquad 4/7<a<1,
}
\]

uniformly on strict strips, with all row valuations retained. The external large-sieve theorem is imported and explicitly credited, not independently proved here. It is unnecessary for the \(31/19\) A2 theorem.

The exact squarefree-row complete cusp series from PR #922 inherits the expanded mean domain. Its scalar infimum becomes \(11/14\), approached strictly. The note also proves why this scalar improvement by itself does not beat the existing physical envelope.

## 6. The remaining target is concrete

The unsigned A2 correction sum is now controlled in the stated range. The first-Poisson remainder still has two independently corrected columns, the original coupled row kernel, a strict product-column off-diagonal restriction, and a signed auxiliary sum. A sufficient next result must estimate that actual expression and keep those structures through the comparison. The [pinned native sign example](sources/pr921/CENTERED_NATIVE_SIGN.md) shows that its correctly centered completed pieces can have either sign even for genuine source coefficients.

There is also a scale gap: the current gain reaches arithmetic row ranges below \(D\), while the adverse initial dual height is near \(D^{3-\vartheta}\). The next composition needs either a signed contraction which survives that larger range, or a valid height descent for the exact two-column remainder. The enlarged spectral mean domain and the new full A2 norm provide stronger inputs, but no such contraction is claimed here.

For the cofinal moment objective, the fixed-matching theorem gives a reusable all-order sector estimate. What remains is a controlled decomposition of the complementary signed sectors with loss sublinear in the moment order, at the uniformity required by the existing cofinal extraction criterion. Taking a limit of currently unproved full moments would not establish RH.

## 7. Review and reproducibility

[VALIDATION.md](VALIDATION.md) records the scoped proof reviews and the exact arithmetic checks. [MANIFEST.json](MANIFEST.json) covers the packet inventory and binds each review to the exact manuscript bytes. The integrity verifier also checks each retained source against its pinned `commit:path` Git object.

Finite diagnostics exercise literal zero phases, overlapping labels, repeated cube factors, capped tails, exact exponent optimization, signed graph identities and their full intersection classification. They test algebra and bookkeeping; the infinite analytic estimates and their imported premises require mathematical review.
