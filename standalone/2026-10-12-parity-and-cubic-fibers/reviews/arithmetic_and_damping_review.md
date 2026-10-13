# Exact-source independent review: arithmetic parity and damped moments

**Verdict: scoped PASS.** No mathematical blocker was found in the two proof files identified below. The positive damping theorems preserve their pointwise and weighted second-moment premises. The arithmetic obstruction theorems retain their principal-twist and subsequential scopes. The committed damping checker was inspected and independently executed normally and with Python optimization; both executions reproduced the committed result byte for byte.

**Reviewer:** automated research agent /root/amplification.

**Review date:** 2026-10-13 UTC.

**Review type:** independent nonauthor proof and bounded-checker review at one exact published source commit. This is not human review, repository integration, approval of an unspecified later head, or a proof of the undamped generalized moment or RH.

## 1. Frozen source and authorship boundary

Repository: [GettysburgResearch/riemann](https://github.com/GettysburgResearch/riemann).

Source PR: [#930](https://github.com/GettysburgResearch/riemann/pull/930).

Source commit: [c07b9f653b8d0eb82d9f056d935a4ecef6770f56](https://github.com/GettysburgResearch/riemann/commit/c07b9f653b8d0eb82d9f056d935a4ecef6770f56).

Source tree: [0f72b503dc11e229e674db1f4d99e8559e8658b3](https://api.github.com/repos/GettysburgResearch/riemann/git/trees/0f72b503dc11e229e674db1f4d99e8559e8658b3).

Parent commit: 086bf0560c0c2679a1fe41418f583d2c5ca743c3.

All paths in the identity table are relative to:

standalone/2026-10-12-parity-and-cubic-fibers/

I fetched the files through the GitHub connector with the exact commit as the reference, decoded the returned base64, computed SHA-256 and Git blob SHA-1 directly from the decoded bytes, and compared the computed Git blob IDs with those returned by GitHub. The Git commit endpoint supplied the displayed tree and parent.

| Published path | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| [ARITHMETIC_PARITY_OBSTRUCTION.md](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/ARITHMETIC_PARITY_OBSTRUCTION.md) | 20,193 | b18d210c8aac21e477ad031a89a9432c9eeb86a60917d06624a4081b603ab6ff | d90f394a8026eb983da28edb82a5fba8fa91bb29 |
| [PARITY_DAMPED_MOMENTS.md](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/PARITY_DAMPED_MOMENTS.md) | 38,285 | fed521f2865b428e5a0eebd1d6f36ae09cc6d51f513952547ba6087910d0d232 | dbc13956b5eb5f3b5b2028dc9ebcd81a7c48a8c3 |
| [checks/verify_parity_damping.py](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/checks/verify_parity_damping.py) | 14,661 | 7a855e686be65379abe64e13ed0694ed3237dc9f2d3c9dc71270402f8bb46676 | 7c60663318107292f112930d6a2aa210bc5a31c2 |
| [results/parity_damping.json](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/results/parity_damping.json) | 5,980 | 2d11b779c54f6710a5a3a439fd3f9493d955b44602b482d307ecf2d38e3c7253 | b7654d598cd62b0e256d17c5ad29a4a59bfafe61 |
| [results/parity_damping_optimized.json](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/results/parity_damping_optimized.json) | 5,980 | 2d11b779c54f6710a5a3a439fd3f9493d955b44602b482d307ecf2d38e3c7253 | b7654d598cd62b0e256d17c5ad29a4a59bfafe61 |

The root agent authored the arithmetic parity note. The moment agent authored the damping note and its checker. I did not author or edit those proof or checker files during this review. I previously supplied a content-only review of the root parity proof and a caution concerning universal zeta centering. The committed parity proof is byte-identical to that earlier content-review target; I nevertheless reread the committed proof in full for this receipt.

I separately authored the companion CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md. This receipt does not independently approve that companion note, my checker for it, or any result that depends on treating my own work as independently reviewed. The two proofs reviewed here were checked from their displayed arguments without using my companion note as a premise.

The local damping author draft had SHA-256 b64002a7581bd07e29e9b75439e9283afd117ce3f01feafc90cb9b32097da4ca. A direct text diff against the fetched published proof found exactly one change: the source-manifest reference changed from attack4_moment_sources.json to sources/repository_sources.json. The published identity in the table, rather than the draft identity, is the target of this PASS.

I also fetched [sources/repository_sources.json](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/sources/repository_sources.json): 23,563 bytes; SHA-256 e13e0ebabd9b734906187d2f676ce6c9fc3dd815caccfbc801069f4887d902e6; Git blob bb7b724c4b051c25d213070d72eaff130aeb7671. Identifying this manifest does not independently certify every upstream theorem listed in it. The packet README was fetched for context; this receipt does not issue a separate README or whole-packet verdict.

## 2. Arithmetic parity obstruction: proof review

**Scoped PASS:** the native counting and Mellin lemmas, Theorem 3.1, Theorem 4.1, and Corollary 4.2, with the domains stated in the committed note.

### Native rows, ideals, and coprimality

The ideal count has the correct normalization. The Eisenstein lattice has covolume \(\sqrt3/2\); division by its six units gives

\[
 I(X)=\frac{\pi}{3\sqrt3}X+O(\sqrt X).
\]

The lattice boundary estimate suffices for the displayed continuation of the counting Mellin integral to \(\Re s>1/2\), and hence the simple zeta pole at \(1\). The small-\(X\) version used inside inclusion-exclusion is valid: when \(0<X<1\), the ideal count is zero and \(X\le\sqrt X\).

The map from an ideal to the sixth power of any generator is well-defined and injective. It yields actual element rows of norm at most \(V^6\), without inserting multiplicity or omitting nonsquarefree bases. The identity \(\chi_n(v^6)=\mathbf1_{(v,n)=1}\) retains the required mask.

In (1.5), the error is uniform in the squarefree column ideal, including divisors with norm larger than \(V\). Retaining those divisors in the main term is essential for the subsequent complex-coefficient average.

### Mellin growth and the selected prime face

The smoothing identity is

\[
 \int_0^\infty C(D)D^{-s}\frac{dD}{D}
 =\widehat W(s)F(s).
\]

The lower limit creates no singularity because \(C(D)=0\) below a fixed positive scale. A bound \(C(D)=O(D^{1-\delta})\) would give a holomorphic continuation through \(1\). The value \(\widehat W(1)>0\) preserves the singularity. Together with the trivial coefficient/counting upper bound, this proves growth index \(1\), with subsequences allowed to depend on the requested loss. No prime number theorem or Tauberian positivity theorem is needed.

The prime logarithm has the asserted singularity, since its prime-power tail is analytic near \(1\). For \(V=D^{h/6}<aD\), every base ideal of norm at most \(V\) is coprime to every contributing prime. Thus all those sixth-power rows reproduce the principal prime sum exactly.

The repeated-position sector has absolute bound \(O(HD^{2k-1})\). The exponent difference between the replicated prime lower bound and this error is \(1-5h/6-2k\delta\). It is positive in the required range \(0<h<6/5\), after choosing the loss sufficiently small. Subtracting this error from the nonnegative prime moment is legitimate even though the selected all-distinct sector is initially a real signed sum.

The conclusion concerns the **selected prime face for the principal coefficient twist**. It is not a lower bound for the complete singleton sector or full Möbius moment, because composite squarefree columns remain available for cancellation. The note preserves this boundary.

### Nonintegral prime-count deformation

The Euler factorization in (4.5)–(4.6) has the correct excluded-prime factors. The logarithm of each good-prime correction begins with \(z(Np)^{-s-1}\), with error \(O_z((Np)^{-2\Re s})\). Both prime sums converge locally uniformly for \(\Re s>1/2\). With good prime norm at least \(7\) and \(|z|<5/4\), the local numerator is nonzero throughout that half-plane. The correction product is therefore holomorphic and nonzero on the claimed domain.

Near \(1\), the factorization \((s-1)^zG_z(s)\), with \(G_z(1)\ne0\), has a nonremovable branch for every fixed nonintegral \(z\) in the stated disk. Differentiation at \(z=1\) leaves the nonzero \((s-1)G_1(s)\log(s-1)\) term; the analytic term cannot cancel it.

The averaging step (4.10) retains the exact sixth-power coprimality density. The error-to-main ratio is bounded by a constant times \(D^{-h/12+\epsilon+\delta}\). The choice \(\epsilon+\delta<h/12\) makes it small along the Mellin subsequence for each fixed \(h>0\). Hölder then gives lower exponent \(2k+h/6\). Passing to a limsup and comparing all-epsilon exponents is valid even with constants depending on each fixed \(k,z,h\).

The proof excludes \(z=1\), permits only the stated principal twist, and derives no new zero-free region. The centering discussion in Section 5 remains exploratory; this PASS does not turn it into a uniform centering or moment-comparison theorem.

## 3. Parity-damped moments: proof review

**Scoped PASS:** the native algebra, coefficient bounds, finite exclusion adapter, Theorems 6.2–6.3 under their exact premises, the Jensen and pointwise equivalence statements with their declared uniformity, and the explicitly limited norm-data and complete-residue obstructions.

### Exact parity and literal zero symbols

The identity \(\chi_p=Q_pC_p\) holds both on sixth roots and at zero. If \(p\mid u\), the cubic polynomial is independent of that sign coordinate; every Walsh coefficient involving it vanishes. Consequently the substitution of \(-Q_p(u)\) is made only on active sign coordinates. No Walsh identity on a sign cube is illicitly evaluated at a zero coordinate.

For each supported tuple, the total Möbius sign equals \(\mu_K(r)\), where \(r\) is its odd-multiplicity prime product. The cubic factors retain the even-multiplicity masks. The baseline is nonnegative, but is not identified with only the principal-character diagonal.

I checked the one-sign binomial inequality, its \(L^k\) triangle step, and the induction giving the weighted Rademacher inequality. The fixed-order ideal divisor sum gives the uniform baseline and Parseval bounds. In Lemma 3.2 the full tuple product has the unique form \(rg^2\); counting the possible \(g\), then the fixed-order factorizations of \(rg^2\), proves the \(D^{k+\epsilon}/\sqrt{Nr}\) coefficient bound without discarding incidence patterns. Its small-parity consequence does not cover the long singleton range.

### Moving exclusions and the two analytic premises

The correction identity is a native Euler convolution for the good-prime exclusions used in this family. The good part of the exclusion is operative, since the fixed bad set is already removed from every column. At a correction prime the finite-support convolution of the inverse local factor with the original Möbius factor cancels exactly. A zero symbol makes both nonconstant factors vanish; no symbol is divided out.

Every contributing correction scale is bounded below by the fixed support constant and above by the original scale. The same ambient \(D\) and physical row range are maintained throughout. The finite correction products at exponents \(b>0\) and \(1/2\) are \(O((NQ)^\eta)\); the polynomial bound on the exclusion permits these factors to be absorbed into the requested loss.

This validates the use of PW_b only in its stated **all-nonempty-shorter-scales, same-row-range, finite-test-seminorm** form. It does not follow from a top-scale pointwise statement alone. The weighted NM2_w premise is separate: total nonnegative row mass \(O(H)\) supplies no such second moment. The masked second moment uses the weighted \(L^2\) triangle inequality and contraction by the literal row phases, not a replacement by arbitrary masked coefficients.

### Centered signs and the positive hierarchy

With mean \(m_p=-(Np)^{-t}\), the exact centered coefficient is

\[
 B_d(u)=\xi_u(d)(X/Nd)^{-t}
 A_u^{(dq)}(X/Nd;x^{-t}W(x)).
\]

There is no missing factor \(\mu_K(d)\). The remaining Möbius sign belongs to the cofactor ideal, and \((m,d)=1\) is exactly what the original squarefree column requires. The factor \(\xi_u(d)\) is a contraction, including its possible zero.

The symmetrization proof in Lemma 6.1 is valid at degenerate marginals. Conditional expectation over an independent copy sends products of \(e_p-e'_p\) to the centered monomials. Conditional on their magnitudes, the differences have independent fair signs and magnitude at most two. This gives \([4(2k-1)]^{\omega(d)}\).

Putting \(\gamma=2(b-t)\), the squared random norm is bounded by

\[
 D^\epsilon X^\gamma
 \sum_{Nd\le\beta X}\mu_K(d)^2[4(2k-1)]^{\omega(d)}(Nd)^{-\gamma}.
\]

The divisor estimate yields \(X^{\max(1,\gamma)}\), up to the allowed loss. The proof treats the logarithmic boundary \(\gamma=1\) and negative \(\gamma\) correctly. Nonempty subunit scales stay within a fixed bounded interval. Finite test seminorms are uniform on compact \(t\)-ranges, and all moment orders are fixed independently of \(D\).

This establishes Theorem 6.2 as stated. Its unconditional counting case is \(b=1\), reaching diagonal size at \(t=1/2\). The example \(b=7/8,\ t=3/8\) remains conditional on PW_7/8. No theorem supplying that pointwise exponent is independently certified by this review.

For Theorem 6.3, the weighted second-moment adapter gives

\[
 \sum_u w_H(u)|B_d(u)|^2
 \ll HD^\epsilon(X/Nd)^{1-2t}.
\]

Summing the nonnegative centered-coefficient weights gives
\(\sum_u w_H(u)\mathcal Q_{k,t}(u)\ll HD^\epsilon X\).
Combining this with
\(\sup_u\mathcal Q_{k,t}(u)\ll D^\epsilon X^m\),
\(m=\max(1,2b-2t)\), yields exactly

\[
 HD^\epsilon X^{1+(k-1)m}
 =HD^\epsilon X^{k+(k-1)(2b-2t-1)_+}.
\]

The argument remains valid at \(t=0\), for \(t>1/2\), and at \(k=1\); it still requires the separate weighted shorter-scale second moment.

### Jensen, endpoints, and non-equivalences

The mean identity has the correct power and test shift:

\[
 \mathbb E Z_{u,t}(X;V)
 =X^{-t}A_u(X;x^{-t}V(x)).
\]

Choosing \(V=x^tW\) proves the reverse Jensen adapter with cost \(X^{2kt}\). The pointwise randomized second-moment equivalence for \(0\le t\le1/2\) preserves the same ambient parameter, shorter scales, physical rows, and uniform test-family quantifiers on both sides. It is not an equivalence with an ordinary averaged native second moment.

At \(t=0\), the signs are deterministically minus one and the functional is the original native moment. A diagonal bound there from PW_1/2 is conditional on that endpoint premise. Positivity of the semigroup does not imply monotonicity at the distinguished sign vector or a cheaper reverse comparison. The bounded-coefficient sharpness example in Section 7 is correctly labeled as a comparison model rather than an actual fixed Hecke row.

The all-fixed-order averaged statement in Section 7 gives the indicated top-scale pointwise implication by retaining a row and taking a sufficiently large fixed order. It does not silently supply the stronger same-height, all-shorter-scale premise.

### Full-file review of the remaining obstructions

I checked the three branches of \(F_h(x)\), the continuous maximum \(hc(b)\), the finite integer optimization for \(\delta_{\mathbb Z}\), and the resulting common-spike exponents. For \(h>1\), \(\delta_{\mathbb Z}<h\), so the finite model has a growing number of occupied rows; its even occupied-row floor preserves mean zero and the claimed powers. The obstruction is valid conditional on granting exactly the displayed product-norm profile and native pointwise/second-moment bounds. It does not assert that the synthetic vectors satisfy the literal arithmetic identities.

The integer endpoint calculations at \(b=7/8\) and \(b=1\), the attained envelope for sufficiently large fixed \(k\), and the cofinal deduction with \(h_k=o(k)\) follow from that optimization. No constant uniform in \(k=k(D)\) is used or asserted. The fixed-order cumulant calculation retains the leading rare-event power.

The complete-residue quadratic/cubic independence statement is correct on units, and inactive primes are handled by the cubic zero masks. The final residue-coordinate heat-bath argument uses \(N(\mathfrak Q/p)>4H\) and the norm triangle inequality to force each conditional fiber to contain one row. Its scope is full residue-coordinate resampling on the short row set; it does not forbid every chain on coarser character data.

## 4. Independent checker replay

The checker source was read in full before execution. It uses exact integers and fractions.Fraction, with explicit exceptions through require; optimization does not disable the acceptance predicates.

The primitive ring implementation uses the basis \(1,\zeta_6\), with

\[
 \zeta_6^2=\zeta_6-1,\qquad
 \overline{a+b\zeta_6}=(a+b)-b\zeta_6,\qquad
 |a+b\zeta_6|^2=a^2+ab+b^2.
\]

Its multiplication, conjugation, and norm formulas agree with these identities. Sextic symbols are reconstructed by finite-field exponentiation at the embeddings \(\zeta_6\mapsto3\pmod7\) and \(\zeta_6\mapsto4\pmod{13}\), each checked to have order six and satisfy its cyclotomic relation. The complete CRT loop covers all 91 residue rows, including literal zero cases. This is a primitive finite-field replay, not merely validation of supplied derived JSON.

The following commands were actually run from /workspace/scratch/5b23d9b20a3a, against copies freshly fetched from the reviewed commit:

~~~bash
python attack4_amplification_sources/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/checks/verify_parity_damping.py --note attack4_amplification_sources/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/PARITY_DAMPED_MOMENTS.md --json attack4_amplification_sources/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/parity_damping_replay_normal.json
~~~

~~~bash
python -O attack4_amplification_sources/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/checks/verify_parity_damping.py --note attack4_amplification_sources/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/PARITY_DAMPED_MOMENTS.md --json attack4_amplification_sources/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/parity_damping_replay_optimized.json
~~~

Both commands completed with exit status zero and reported **PASS, 44,091 explicit guards**. Each independent replay produced 5,980 bytes with SHA-256 2d11b779c54f6710a5a3a439fd3f9493d955b44602b482d307ecf2d38e3c7253 and Git blob b7654d598cd62b0e256d17c5ad29a4a59bfafe61.

A separate Python byte-comparison and hash computation checked all four result files: the two fetched committed files and the two newly generated files. All four were byte-identical. The same verification checked that the committed arithmetic parity proof was byte-identical to the preliminary content-review target and produced the one-line packaging diff for the damping proof described above.

The finite coverage includes 1,092 native Walsh cases, 2,184 biased cases at \(t=0,1\), all four local exclusion masks, moment orders \(1,2,3\), centered cofactor identities and inactive coordinates, coefficient and Parseval guards, 40 rational exponent-parameter pairs with integer degrees through 64, cumulants through order 12, and the stated bounded Eisenstein residue-resampling example.

These counts include arithmetic precondition checks; they are not counts of independent infinite theorems. The proof hash binds the inspected text to the run. The checker does not parse or formally verify the analytic proof. Its finite identities support normalization and algebra checks; the infinite arguments were reviewed separately above.

## 5. Remaining limitations and exact verdict

The PASS applies only to the exact files and identities in Section 1, with their stated scopes and premises. It does not certify:

- PW_b for any \(b<1\), including \(b=7/8\) or \(b=1/2\);
- NM2_w for arbitrary weights or outside its supplied row-height and shorter-scale domain;
- a new proof or broader scope of the upstream physical-product sieve imported in (8.1);
- a prime number theorem, uniform Selberg–Delange asymptotic, or independently authenticated historical priority claim;
- an incomplete-row replacement of complete CRT independence;
- an estimate removing the remaining parity damping;
- uniformity in a moment order growing with the column parameter;
- the undamped cofinal generalized moment hypothesis, a new zero-free region, RH, human approval, or repository integration.

The elementary Eisenstein counting, Mellin noncontinuation, local probability inequality, moving-mask convolution, and fixed-order divisor estimates used by these proofs are proved within the reviewed files and were checked as arguments. The contextual external literature and upstream manifest do not substitute for those arguments, and their other results are not promoted by this receipt.

**Final scoped verdict: PASS at source commit c07b9f653b8d0eb82d9f056d935a4ecef6770f56; no blocking finding.** No published mathematics or frozen packet file was edited during this review. Only reviewer-owned fetched copies, fresh replay outputs, and this receipt were written.

Signed: /root/amplification, automated nonauthor reviewer, 2026-10-13 UTC.
