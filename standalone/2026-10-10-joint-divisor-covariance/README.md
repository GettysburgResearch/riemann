# Joint divisor cancellation, moving A2 completion, and new moment sectors

**Status:** proposed standalone research, stacked on PR #922 at
f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32. Four new proofs give a
stronger large-divisor tail, close the mixed moving-label interface for
positive theta norms, transfer the short-row saving to the full arithmetic
A2 completion, and control additional sectors of every fixed moment by
published Hecke subconvexity. The full fourth moment, the generalized
moment hierarchy, and RH remain unproved.

**Scope:** the joint-divisor and theta/A2 estimates retain their pinned
imported analytic assumptions. The new residual-conductor sectors use
published Hecke estimates and a complete incidence argument; they do not
assume the imported native Möbius second moment or a zero-free hypothesis.
The separate positive estimates do not bound the remaining signed
covariance.

## 1. The target and what this pass changes

The intended generalized moment is

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad
\sum_{0<Nu\le H}|A_u(D)|^{2k}
\ll_{k,\vartheta,\epsilon,W,\nu,S} HD^{k+\epsilon},
\quad H=D^{1+\vartheta},
\tag{1.1}
\]

for every fixed integer \(k\ge2\), every fixed finite-order character
\(\nu\), fixed bad set S, and fixed \(W\in C_c^\infty((0,\infty))\),
for all sufficiently large real D and arbitrarily small fixed
\(\vartheta>0\), in the inherited Eisenstein normalization. Constants
may depend on all these fixed data and need not be uniform in k.
The test quantifier matters: the fixed test used to exclude a
hypothetical zero may depend on that zero. The exact moment-to-zero-free deduction in
[PR #913's general-moment proof](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/GENERAL_MOMENT_ATTACK.md)
would give the boundary \(1/2+5/(12k)\) from the full order-k hypothesis
and the declared imported machinery. The case k=2 would give \(17/24\);
an unbounded hierarchy would approach \(1/2\). Those implications do not
establish their moment hypotheses.

This pass attacks three concrete losses in the previous work: taking
the divisor norm before recombination, paying uncontrolled costs for
moving A2 labels, and using only the classical complete-character
estimate on residual conductors. The four proof notes have the following
roles.

| Proof | New conclusion | Exact limitation |
|---|---|---|
| [Joint divisor mean](JOINT_DIVISOR_MEAN.md) | A joint block estimate retaining the moving cube reciprocal; a \(Q^{1/4}\) saving in a specified tail norm at \(\Re u=3/4\) | Squarefree rows; large divisors only; the full divisor convergence boundary does not improve |
| [Moving auxiliary adapter](MOVING_AUXILIARY_ADAPTER.md) | Explicit all-row estimates for overlapping moving exclusion q and auxiliary f, full cube inversion, and summable A2 correction operators | The stated theta, sieve, and angular inputs remain assumptions; positive norm only |
| [Optimized A2 transfer](OPTIMIZED_A2_TRANSFER.md) | A correction-dependent cube cutoff transfers the raw short-row saving to the full arithmetic A2 completion with no extra power loss | The raw saving itself was in PR #923; the critical moment's long dual scale is still outside this gain |
| [Signed conductor progress](SIGNED_CONDUCTOR_PROGRESS.md) | Additional diagonal-size incidence sectors at every fixed order, including explicit fourth-moment configurations beyond the old accounting regions | Large separated singleton configurations still require signed cancellation |

## 2. A joint divisor estimate with the literal cube reciprocal

Write \(a=\Re u\), \(b=\Re t\), and let the squarefree row k have
norm comparable to Q. In the canonical reflected series the actual
cube-adjusted local factor is

\[
\Theta_k(d;u,t)=\prod_{p\mid d}
\frac{1-A_p}{1-z_p},
\qquad
z_p=\widetilde c_k(p)(Np)^{1/2-3u},\quad
A_p=\kappa(p)c_k(p)(Np)^{1/2-2t-u}.
\tag{2.1}
\]

All primes dividing kS are omitted. On permitted primes the row part
of these variables is quadratic. Expanding it in that two-dimensional
character basis gives an absolutely summable correction for \(a,b>1/2\).
This retains the exact denominator caused by the moving cube exclusion.

For the normalized joint block \(\mathfrak B_{F,X}\) defined in the
proof, with \(Nd\asymp F\) and completed inner length X, the result is

\[
\sum_{k\asymp Q}^{*}|\mathfrak B_{F,X}(k)|^2
\ll (QFX)^\epsilon
\min\left\{Q+FX+(QFX)^{2/3},
            FQ+\frac{Q^2F^2}{X}\right\}.
\tag{2.2}
\]

Fixed test seminorms are suppressed here. Bounded row-independent
divisor coefficients are allowed. The first branch recombines the
divisor and inner squarefree factor using the exact Gauss CRT; the second
uses the imported completed mean square. Moving masks stay in the actual
coefficients.

For

\[
\frac12<a<\frac56,\qquad
b=\frac{3-a}{2}+\eta,\qquad \eta>0,\qquad R\ge Q^{2/3},
\]

dyadic reconstruction proves

\[
\left\|\operatorname{tail}_{Nd\ge R}\mathcal Z_k\right\|_{\ell^2(k\asymp Q)}
\ll Q^{1-a+\epsilon}R^{-\eta+\epsilon}
(2+|\Im u|)^M.
\tag{2.3}
\]

At \(a=3/4\), this changes the old \(Q^{1/2}\) norm cost to \(Q^{1/4}\)
for that tail. Small divisors are not covered by this comparison. The
full positive majorant still needs \(2b+a>3\); the note proves why the
new block estimate does not remove that condition.

The finite A2 coefficient identification in Section 7 credits its prior
appearance in PR #914. It does not infer a global Weyl functional
equation for the moving angular family.

## 3. Close the moving-label interface and preserve the short-row gain

For squarefree q,f, with overlap allowed, put

\[
r=q/(q,f),\qquad
\ell=N\operatorname{lcm}(q,f),\qquad
m=(Nr)^{1/3}(Nf)^{2/3},\qquad X=\sqrt{AB}.
\]

The [adapter](MOVING_AUXILIARY_ADAPTER.md) computes the excluded-prime
and auxiliary-prime transforms at each physical row valuation, includes
all three cusps and bad-prime tails, and retains every nonunit zero.
This resolves the stronger positive-norm interface left open in
[PR #918](https://github.com/GettysburgResearch/riemann/blob/cfa102748b26f840ccc4b963a660711424db0ec3/standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md).
It preserves the source's distinction between the squarefree inner
index and its unrestricted cube index: there is no extra coprimality
condition between those two indices.

The resulting [optimized theorem](OPTIMIZED_A2_TRANSFER.md) bounds
both the normalized raw polynomial \(\mathcal P_q\) and full arithmetic
A2 completion \(\mathcal Q_q\), for every positive cutoff U:

\[
\begin{aligned}
\|\mathcal P_q\|_H^2+\|\mathcal Q_q\|_H^2
\ll \mathfrak D^\epsilon\big[
&HX+\ell H^2X^{5/12}U^{7/4}
+mH^{4/3}X^{2/3}U^2\\
&+H^{1/6}X^2U^{-3}
+H^{2/3}X^{4/3}U^{-2}\big].
\end{aligned}
\tag{3.1}
\]

The row norm includes every nonzero element of norm at most H.
All moving parameters are bounded by fixed powers of the reference
scale \(\mathfrak D\). The \(11/12\) angular input is explicit in the
proof; it is not replaced by an unstated arbitrary-coefficient estimate.

The new transfer step uses the exact A2 correction labels c,d,e and
assigns each child its own cube cutoff

\[
U_{c,d,e}=U/(Nc\,Nd)^{1/2}.
\tag{3.2}
\]

Every remaining correction norm weight then has a denominator exponent
strictly greater than one. A common cutoff would leave the second
term's exponents at \(13/16\), so absolute convergence would fail.
The proof covers subunit child cutoffs and smaller nonempty rectangles.

At q=f=1 and A=B=D this gives, for the full A2 completion,

\[
\|\mathcal Q_1(D,D;\cdot,1)\|_H^2\ll D^\epsilon
\begin{cases}
D^{6/5}H^{13/15},&1\le H\le D^{38/87},\\
DH^{151/114},&D^{38/87}\le H\le D^{19/22}.
\end{cases}
\tag{3.3}
\]

In particular it is at most \(D^{2+\epsilon}\) for
\(H\le D^{114/151}\). At \(H=D^{1/2}\), the exponent is
\(379/228\), a saving of \(8/19\) over the classical \(25/12\)
exponent. PR #923 already had this numerical saving for the raw
polynomial. The new result is its transfer to the full A2 completion
and the mixed moving family. These short-row estimates are far from the
moment's critical first-Poisson dual length \(D^{3-\vartheta}\).

## 4. New sectors of the actual generalized moment

For a tuple of k unbarred and k barred squarefree columns, let f be
the product of the primes with nonzero residual multiplicity modulo
six. Let \(g_j\) be the product of the nonprincipal primes occurring
in exactly j positions. The actual conductor is
\(Nf=\prod_j Ng_j\). Principal residual primes remain in their
separate zero mask.

Restrict to nonprincipal tuples, so \(f\ne1\). Fix a nonnegative
radial \(\Phi\in C_c^\infty(\mathbb C)\) with \(\Phi\ge1\) on the
unit disk. Set \(L\asymp Ng_1\), \(G\asymp Ng_2\). The positive accounting
\(\mathcal Q_{L,G}^{\Phi}\) sums the absolute values of complete
smooth residual-character row sums, weighted by the tuple coefficients.
It bounds the modulus of any selected signed subcollection.
[The proof](SIGNED_CONDUCTOR_PROGRESS.md) establishes, for every
fixed k and arbitrary bounded coefficient phases,

\[
\mathcal Q_{L,G}^{\Phi}
\ll D^{k+\epsilon}
\min\left\{H\sqrt L,\ L\sqrt G,\
H^{1/2}L^{359/512}G^{103/512}\right\}.
\tag{4.1}
\]

The new branch applies Wu's published Hecke subconvexity theorem with
Blomer–Brumley's \(7/64\), after an exact unit projection and Mellin
integral that retains the principal mask. Higher incidence multiplicities
have strictly convergent sums. These steps do not assume the imported
native Möbius moment.

Söhne's divisor-sensitive bound, in the precise form quoted by Wu,
also proves

\[
\mathcal Q_{L,G;P(f)\le Y}^{\Phi}
\ll D^{k+\epsilon}H^{1/2}Y^{1/6}L^{2/3}G^{1/6}.
\tag{4.2}
\]

Here \(P(f)\) is the largest prime-ideal norm in f. The factor
\(Y^{1/6}\) can be omitted when f has an actual divisor of norm
comparable to \((Nf)^{1/3}\). The proof selects a genuine conductor
divisor; it does not optimize over a fictitious real divisor.

Consequently the following regions, and their literal union with the
previously controlled regions, have total cost \(O(HD^{k+\epsilon})\):

| New region | Additional hypothesis |
|---|---|
| \((Ng_1)^{359/256}(Ng_2)^{103/256}\le H\) | None |
| \(P(f)(Ng_1)^4Ng_2\le H^3\) | None |
| \((Ng_1)^4Ng_2\le H^3\) | An actual divisor of f has norm comparable to \((Nf)^{1/3}\) |

These regions strictly add to the earlier two positive accounting
branches. The proof gives feasible fourth-moment configurations inside
PR #919's small-gcd remainder and with no subpower cross separation.
Their exponent costs, measured relative to \(HD^2\), are:

| Row exponent \(h\), \(H=D^h\) | Old completion branch | New branch | Conductor restriction |
|---|---:|---:|---|
| \(101/100\) | \(+1/400\) | \(-869/204800\) | None |
| \(21/20\) | \(+1/20\) | \(-1/120\) | \(P(f)\ll D^{1/10}\) |

These are comparisons of rigorous upper bounds for entire incidence
collections, not lower bounds on their true contribution.

## 5. The remaining signed estimate

In PR #919's exact fourth-moment reduction, subtract the newly controlled
Hermitian collection from its old signed small-gcd remainder \(U_h(D)\).
The remaining real quantity \(V_h(D)\) satisfies

\[
M_4(D,D^h)\le K D^{h+2+\epsilon}+2V_h(D),
\qquad
V_h(D)\ge-KD^{h+2+\epsilon}.
\tag{5.1}
\]

For \(1<h\le11/10\), the sufficient averaged target, for the source's
fixed universal Mellin-factor test and every positive loss, remains

\[
\int_X^{2X}V_h(D)\,\frac{dD}{D}
\ll X^{h+2+e+\epsilon},\qquad e\ge0.
\tag{5.2}
\]

Together with the pinned detector and source framework this would give
the boundary \(1/2+5h/24+e/4\). This pass narrows the tuple collection
in (5.2), but does not prove (5.2).

For example, pairwise-coprime columns at scale D have
\(Ng_1\asymp D^{2k}\). The present conductor bounds do not reach
\(HD^k\) for those configurations in the near-critical range
\(H=D^{1+\vartheta}\), \(0<\vartheta\le1/10\).
The next needed statement must exploit signed cancellation across
these surviving tuples, or a stronger average across their actual
residual conductors. It must retain both column labels and the
reconstructed original-product diagonal under any A2 or cube inversion.
The positive theta norms alone cannot supply that estimate.

There is no new zero-free half-plane in this packet. The prior numerical
boundary and its imported-source qualifications remain unchanged.

## 6. Review, reproducibility, and source boundaries

The [source lock](SOURCE_LOCK.json) records exact commits, file blobs,
SHA-256 hashes, and the external theorem interfaces. PR #921 and #923
are sibling inputs read at explicit commits; their moving branch tips
are not implicitly adopted.

Independent AI-agent reconstructions are recorded in:

- [Joint divisor review](JOINT_DIVISOR_INDEPENDENT_REVIEW.md).
- [Moving auxiliary review](MOVING_AUXILIARY_INDEPENDENT_REVIEW.md).
- [Optimized transfer review](OPTIMIZED_A2_TRANSFER_REVIEW.md).
- [Signed conductor review](SIGNED_CONDUCTOR_INDEPENDENT_REVIEW.md).
- [Root reconstruction](ROOT_INDEPENDENT_REVIEW.md).
- [Finite checker review](CHECKER_INDEPENDENT_REVIEW.md).

The exact finite diagnostic is
[check_covariance_arithmetic.py](checks/check_covariance_arithmetic.py).
Its [retained report](results/exact_covariance_checks.json) records
22,743 successful predicates including nine negative controls, using
integer, rational, formal-polynomial and exact Eisenstein arithmetic.
It does not evaluate an infinite theta series, prove an external
subconvexity theorem, or certify a moment estimate.

Run it from the repository root:

~~~bash
python -I standalone/2026-10-10-joint-divisor-covariance/checks/check_covariance_arithmetic.py
~~~

The subsequent validation record and frozen-source receipts bind these
scoped reviews to the published source commit. This packet is not
integrated acceptance, external human peer review, or Lean verification.
