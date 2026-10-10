# Averaged conductor criteria for fourth and higher inverse moments

**Status:** proposed, independently reviewed combinations of exact source-pinned results. This packet makes the sufficient fourth-moment remainder smaller and permits a signed average over scales. It also proves a cofinal higher-order criterion with explicit nonzero moment losses. It does not bound the remaining arithmetic average, establish \(17/24\), improve the earlier source-conditional boundary \(139999/160000\), or prove RH.

The immediate parent is [PR #918](https://github.com/GettysburgResearch/riemann/pull/918), frozen at `cfa102748b26f840ccc4b963a660711424db0ec3`. New adjacent inputs are [PR #917](https://github.com/GettysburgResearch/riemann/pull/917), at `6b4723042b3d250024eef45cb1924f88f28e902c`, and the separately audited [PR #916](https://github.com/GettysburgResearch/riemann/pull/916), at `dabd6da99fb92eead7c99f941331ed9cbd2ec4ad`. All prior packets remain unchanged. Their source and review limitations are retained.

## 1. A smaller sufficient fourth-moment remainder

For the literal inverse polynomial

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad H=D^h,\quad1<h\le11/10,
\]

PR #917 proves a stronger estimate for the exact portion of \(A_u(D)^2\) with common-factor norm at least \(C\):

\[
\|T_{\ge C}\|_2^2
\ll(DH)^\epsilon D^4
\left[HC^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}\right].
\]

Its proof keeps the cubic character of the common factor inside an all-row cubic sieve. This reaches the desired \(HD^{2+\epsilon}\) scale at

\[
C=D^{(6-h)/7},
\]

improving the earlier \(D^{(4-h)/4}\) cutoff. Near \(h=1\), these are \(D^{5/7}\) and \(D^{3/4}\), respectively. Equivalently, after removing the common factor, the equal singleton lengths can extend to \(D^{(1+h)/7}\), instead of \(D^{h/4}\); their limiting exponents are \(2/7\) and \(1/4\). This gain belongs to PR #917 and was independently audited here.

The new combination splits off that complete polynomial portion before using PR #914's Hermitian conductor accounting on the remaining square. The sole signed remainder \(\mathcal S_h(D)\) then has all of these restrictions:

- Both side gcds are smaller than \(D^{(6-h)/7}\).
- There is a prime appearing exactly once in the full four-factor tuple; \(g_1\) is the product of these primes.
- \(Ng_1\sqrt{Ng_2}>D^h\), where \(g_2\) is the product of nonprincipal primes appearing exactly twice.

The proved reduction retains the signs:

\[
M_4(D,D^h)\le C_\epsilon D^{h+2+\epsilon}
 +2\mathcal S_h(D),\qquad
\mathcal S_h(D)\ge-C_\epsilon D^{h+2+\epsilon}.
\]

Explicit feasible incidence patterns show that this remaining domain is strictly smaller than the old small-gcd/conductor domain. This is a valid norm reduction, not an assertion that deleting terms decreases the absolute value of a signed sum.

Full proof and review: [SMALL_GCD_CONDUCTOR_REDUCTION.md](SMALL_GCD_CONDUCTOR_REDUCTION.md) · [SMALL_GCD_CONDUCTOR_REVIEW.md](SMALL_GCD_CONDUCTOR_REVIEW.md).

## 2. A signed dyadic average is enough

Use the fixed universal smooth test \(W_*\) whose Mellin transform is nonzero in \(\Re s>0\). Combining the preceding inequality with PR #917's averaged extraction proves that the following still-open estimate is sufficient:

\[
\boxed{
\int_X^{2X}\mathcal S_h(D)\frac{dD}{D}
\le C_\epsilon X^{h+2+e+\epsilon}
\quad\text{for every }\epsilon>0\text{ and every }X\ge2.
}
\]

Here \(e\ge0\), \(h\) is fixed in the range above, and the constants may depend on the fixed character, bad-prime set and tests. This is only an upper bound for a signed integral. A pointwise remainder estimate or an absolute-value integral is not required by the implication.

If this arithmetic hypothesis holds, each fixed primitive row twist is zero-free in

\[
\Re s>\frac12+\frac{5h}{24}+\frac e4.
\]

The source extraction uses exact sixth-power row copies, an invertible average of Euler-removal operators with its moving cutoff retained, and a holomorphic Mellin transform. The independent audit checks the low-scale forcing term and applies the causal inverse on finite intervals before passing to infinity; it does not assume the unknown integrability at infinity.

These fourth-moment reductions use classical character sieves, elementary conductor accounting and the proved averaged extraction. They do **not** assume the imported native inverse second moment or the imported quasi-Riemann zero-free theorem. Their arithmetic signed-average premise is still unproved.

The limiting milestones below require the corresponding hypothesis along arbitrarily small fixed \(h-1>0\). They are conditional targets:

| Averaged fourth-moment excess \(e\) | Limiting zero-free boundary |
| --- | --- |
| \(0\) | \(17/24\) |
| \(1/2\) | \(5/6\) |
| \(2/3\) | \(7/8\) |
| \(e<79997/120000\) | Strictly below the earlier \(139999/160000\) boundary |

The last threshold is exactly \(4(139999/160000)-17/6\). For one fixed \(h>1\), subtract \(5(h-1)/6\) from that allowed excess. Thus a first new numerical improvement need not wait for the ideal fourth moment with \(e=0\), but it still requires a new arithmetic estimate.

Source audit: [SCALE_AVERAGED_SOURCE_AUDIT.md](SCALE_AVERAGED_SOURCE_AUDIT.md).

## 3. A broader cofinal higher-moment criterion

For the higher moments, keep PR #918's double residual \(\mathcal T_{k,Q_0}^{\Phi}\), with \(Q>Q_0\) on each side and the same full-tuple conductor restrictions. This part of the argument uses the inherited native second moment. Its optional pointwise exponent is \(1/2<b\le1\); \(b=1\) needs only elementary counting in addition to that second-moment input.

Choose \(Q_0=D^q\), with fixed \(q\ge0\). If the signed dyadic average of this remainder has excess \(e\), the proved total moment excess is

\[
\lambda=\max\{e,(2b-1)q\},
\]

and the conditional extraction boundary becomes

\[
\boxed{
\Re s>\frac12+\frac{5h}{12k}
 +\frac{\max\{e,(2b-1)q\}}{2k}.
}
\]

Along an unbounded sequence of fixed orders, \(h_k=o(k)\), \(e_k=o(k)\), and \(q_k=o(k)\) suffice if the stated arithmetic and native-input hypotheses are proved. The \(h_k\) must remain in the native input's allowed range; a single fixed admissible \(h>1\) works. This permits polynomial cutoffs, for example \(q_k=\sqrt{k}\), and moment excesses such as \(e_k=\sqrt{k}\). It does not prove the corresponding signed averages.

The target character and row remain fixed while taking the sequence of orders. Fixed finite exclusions may depend on the order; their deleted Euler factors do not hide zeros in \(\Re s>0\). A critical-line conclusion for a complex character also requires coverage of its contragredient. The all-finite-order-character premise supplies that coverage, while the principal member is self-dual and includes ordinary zeta.

This is a qualitative implication. Constants may depend on the fixed order, and no height-dependent shrinking band or uniformity as the order grows has been obtained.

Full theorem and independent review: [COFINAL_AVERAGED_REDUCTION.md](COFINAL_AVERAGED_REDUCTION.md) · [COFINAL_AVERAGED_REVIEW.md](COFINAL_AVERAGED_REVIEW.md).

## 4. What the collision kernel adds, and what it cannot add

The bounded [all-order kernel audit](ALL_ORDER_KERNEL_AUDIT.md) confirms PR #916's logarithmic norm transfer under its explicit fixed enlargement of \(S\) by primes of norm at most \((2k)^3\). This avoids the positive kernel's small-prime singularity. A full fixed-row-range rectangular estimate is still required. The kernel's Möbius multiplicativity does not directly remove the different Gauss-family exclusions in the A2/theta interface.

Combining that transfer with only the current anisotropic estimate gives

\[
\lambda_k=(k-1)(2b-1),\qquad
\alpha_k=b+\frac{5h/6-(2b-1)}{2k}.
\]

For the current \(b\) near \(7/8\), with \(h>1\), this approaches \(b\) from above. It does not improve that boundary or make the defect sublinear. A new cancellation estimate is required; repeated norm transfer alone does not provide it.

## Evidence and remaining task

The packet contains complete derivations, scoped independent AI-agent reviews at exact content hashes, verbatim [source snapshots](sources/README.md), [source locks](SOURCE_LOCK.json), a [manifest](MANIFEST.json), and [validation boundaries](VALIDATION.md). The new proofs were reviewed analytically. No numerical moment experiment, new finite-field theorem test, human peer review, or Lean formalization is claimed.

The next arithmetic task is now explicit: bound the signed dyadic average of the small-gcd, large-conductor fourth-order remainder, or prove sublinear averaged residual losses along cofinal higher orders. Completely disjoint long tuples remain part of that unresolved problem. The new packet reduces its domain and weakens the necessary quantifiers; it does not assert the missing bound.
