# Independent scoped supplement: completion tails and the exact signed dual diagonal

Reviewer: the independent `moment_structure_attack` agent. Date: 2026-10-10.

## Verdict

**PASS for Theorem 5.4 and the strengthened Theorem 6.1 at their stated scope.** The completed-energy bound and its large-correction tail follow from the previously reviewed exact norm adapter and the stated refined all-row sieve. The full signed first-Poisson dual diagonal is exactly the original algebraic diagonal minus its zero Fourier term. With the fixed smooth row profile, its normalized magnitude is at most a divisor-weighted coefficient mass and hence is **O(D^epsilon), uniformly for every H > 0** under the draft's hypotheses.

The exact diagonal identity is stronger than cancellation of only a continuum approximation. It follows by undoing the source's reversible coprimality-removal transformations while preserving the chosen diagonal subset. This supplies a complete proof of the claimed cancellation, including the unit ideal and the original zero row.

I found no load-bearing defect in these two additions and requested no repairs. This supplement does not prove the remaining signed off-diagonal bound, the fourth moment, the generalized moment hierarchy, a moving-twist reflection estimate, 17/24, or RH. No repository file was edited.

## 1. Frozen scope and provenance

The reviewed draft is `/workspace/scratch/6ec6134c1535/balanced_core_attack.md`, with SHA-256:

```text
d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad
```

Its exact 36,064 bytes are frozen as `review_supplement_final_snapshot_balanced_core_attack.md`. The earlier supplement draft at hash `c585cf10dde4606c6eb591229cf143773167b5d52825cee18c153857ac47201b` was retained separately, and its complete delta to the final source was inspected. Full source paths, byte counts and hashes are recorded in `moment_structure_independent_review_supplement_manifest.json`.

The earlier review and its manifest were left unchanged. This supplement evaluates the added Theorem 5.4 and the strengthened Section 6 against the already reviewed arithmetic identities; it does not retroactively change the earlier byte-bound review.

The source inputs checked directly were:

| Input | Exact content checked | SHA-256 |
|---|---|---|
| Pinned October 5 `paper2.tex` | `lem:poisson`; `eq:expanded-ms`; `eq:initial-poisson-rows`; `eq:initial-paired-gauss`; all changes of variables preceding `eq:initial-column-output`; that output itself | `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d` |
| PR #913 `REFINED_ALL_ROW_SIEVE.md` | Theorem 3.4, including literal nonunit zeros and arbitrary squarefree column coefficients | `6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8` |

The October 5 source is imported from pinned upstream commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The PR #913 source is the inspected local snapshot at commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`. This review verifies how the quoted sieve is used; it does not replace the sieve's own proof and review history.

## 2. Theorem 5.4: all-row bound and completion tail

### 2.1 Raw coefficient mass and normalization

Write L = AB. At each fixed auxiliary ideal f, collecting the two squarefree factors into n = ab gives squarefree product columns of norm O(L). The number of representations is bounded by a fixed-order ideal divisor function. The fixed test is bounded, and the Gauss, ray and auxiliary phases have modulus at most one. Thus the squared coefficient mass is O(D^epsilon L), uniformly in f and in the moving exclusion q0. The latter simply deletes columns before applying the arbitrary-coefficient sieve.

The sieve consequently gives the unnormalized row bound

\[
\sum_{0<Nk\le\mathcal H}|P_{q_0}(A,B;k,f)|^2
\ll D^\epsilon\left(\mathcal HL+\mathcal H^{1/6}L^2+
\mathcal H^{2/3}L^{5/3}\right).
\]

There are O(F) ideals in the auxiliary annulus. Dividing their sum by the original normalizer LF gives exactly (5.9) for P. This application needs no positivity of the original column coefficients.

Factor scales below one cause no new loss: a nonempty child has A' and B' bounded below by fixed positive constants determined by the compact factor supports. Replacing a bounded subunit product length by a fixed positive comparison scale changes only a support-dependent constant. The draft already restricts the row range and auxiliary scale to Hcal, F >= 1.

### 2.2 Completion and projection

The previously reviewed adapter has norm cost 1/(NC), where C = cde, and its exact child product length is

\[
L'=\frac{L}{(Nc)^3(Nd)^3(Ne)^4}.
\]

Inserting the square root of the raw bound into this adapter gives the three norm weights

\[
\begin{array}{c|c}
\text{scale factor}&\text{label weight}\\
\sqrt{\mathcal H}&(Nc)^{-1}(Nd)^{-1}(Ne)^{-1}\\
\mathcal H^{1/12}\sqrt L&(Nc)^{-5/2}(Nd)^{-5/2}(Ne)^{-3}\\
\mathcal H^{1/3}L^{1/3}&(Nc)^{-2}(Nd)^{-2}(Ne)^{-7/3}.
\end{array}
\]

Only the first weight has harmonic sums, bounded by a fixed logarithmic cube. The others are absolutely summable. Squaring yields (5.9) for Q. The use of the forward adapter is not circular: its analytic input is the independently bounded P family.

On the specified polynomial portion NC >= R, dropping the extra decay in the e label reduces the second and third sums to

\[
\sum_{NC\ge R}d_{3,K}(C)(NC)^{-5/2}
\ll R^{-3/2+\delta},\qquad
\sum_{NC\ge R}d_{3,K}(C)(NC)^{-2}
\ll R^{-1+\delta}.
\]

This is ordinary ideal counting and partial summation. The first, harmonic term need not gain any R decay. The resulting energy is

\[
D^\epsilon\left\{\mathcal H+
\mathcal H^{1/6}LR^{-3}+
(\mathcal HL)^{2/3}R^{-2}\right\}.
\]

The subpower factors of R can be absorbed because a nonempty correction range has polynomial size in D; otherwise the tail is empty. For the inverse tail, the same argument uses the now-proved Q estimate. It does not assume the unproved envelope Hcal + ABF.

Finally R^6 >= L^2/Hcal implies

\[
(\mathcal HL)^{2/3}R^{-2}\le\mathcal H,
\qquad
\mathcal H^{1/6}LR^{-3}\le\mathcal H^{2/3}\le\mathcal H,
\]

where the last comparison uses Hcal >= 1. The threshold and the example R >= D^((1+theta)/6) at L = D^2, Hcal = D^(3-theta) are correct.

This controls the stated large-correction polynomial portion. It does not control the complementary small-correction part, which contains the all-unit correction and hence the original balanced core.

## 3. The exact diagonal: source normalization and residual coefficient

The original smooth moment has normalizer 1/L. After conjugating its inner sum, a general finitely supported residual coefficient v(n) must enter the source's norm-adjusted column as

\[
R_L(n)=\sqrt{L/Nn}\,\overline{v(n)}.
\]

This agrees with the source's W0(x) = x^(-1/2) conjugate(W(x)). A fixed scalar cutoff equal to one on the support permits carrying v as a residual column coefficient through every row-Poisson step; neither smoothness nor multiplicativity of v is required for this finite regrouping.

On m1 = m2 = m, the prefactor in (6.3) becomes

\[
\frac H{L^2}\mu(f)Nb\,|R_L(bfm)|^2
=\frac HL\frac{\mu(f)}{Nf\,Nm}|v(bfm)|^2.
\]

The Gauss factor has squared modulus one for the supported squarefree m. Literal character zeros enforce both (m,f) = 1 and (k,m) = 1. Together with the displayed masks this makes b,f,m pairwise coprime. In particular, the diagonal formula (6.4) has exactly the stated H/L coefficient, all its masks, and k != 0 even when m = 1.

The source removes the zero Fourier frequency before the coprimality transformation but expressly retains every nonzero frequency with z1 = z2 = 1. The reviewed identity concerns precisely those retained frequencies. There is no omitted original principal contribution.

## 4. Independent derivation of the reversal cancellation

Start with the exact diagonal formula. For each summand define

\[
e=(f,k),\quad t=f/e,\quad h=k/e,\quad g=be,\quad z=tm.
\]

Here gcd(f,k) is the ideal gcd, represented with the same fixed generator convention as in the source. The inverse reconstruction is

\[
b=g/e,\quad f=et,\quad m=z/t,\quad k=eh.
\]

Because f is squarefree, (t,h) = 1. Because b,f,m were pairwise coprime, g,z are coprime squarefree ideals, e divides g, and (e,m) = 1. Hence (k,m) = 1 is equivalent to (h,m) = 1. The two row masks combine to (h,z) = 1 and have no remaining dependence on the divisor t of z.

The coefficient and Fourier argument transform exactly as follows:

\[
\frac{\mu(f)}{Nf\,Nm}
=\frac{\mu(e)\mu(t)}{Ne\,Nz},\qquad
bfm=gz,\qquad
\frac{HNk}{(Nf)^2(Nm)^2}
=\frac{HNh}{Ne(Nz)^2}.
\]

Thus every factor except mu(t) is independent of t. Conversely, for every admissible fixed g,z,e,h, every divisor t of z reconstructs a summand: (h,z) = 1 ensures gcd(et,eh) = e. This verifies both surjectivity and the required gcd condition in the reverse change of variables. The divisor sum therefore gives

\[
\sum_{t\mid z}\mu(t)=\mathbf1_{z=1}.
\]

The diagonal reduces exactly to

\[
\mathcal D[v]=\frac HL\sum_g|v(g)|^2
\sum_{e\mid g}\frac{\mu(e)}{Ne}
\sum_{h\ne0}\Psi(HNh/Ne).
\]

This is an identity of finite column sums and convergent, or compactly supported, Fourier sums. No estimate or exchange with a nonconvergent series is used.

Applying the principal-character case of the source's `lem:poisson`, with primitive modulus 1 and exclusion g, gives exactly

\[
\mathcal D[v]=\frac1L\sum_g|v(g)|^2
\left[\sum_{(u,g)=1}\Phi(Nu/H)
-H\Psi(0)\prod_{p\mid g}(1-(Np)^{-1})\right].
\]

The source already absorbs the Eisenstein lattice covolume and its additive-character convention into Psi. There is no additional unspecified constant in this formula.

The result is independent of the fixed ray character xi. As an additional consistency check, substituting z1 = z2 = 1 into the source's paired Gauss identity gives sum_xi c_xi = 1, since a_xi(1) = 1. Thus recombining the finite ray expansion recovers precisely one copy of the original centered algebraic diagonal.

## 5. Uniformity, row zero, and the optional exact cutoff

Set

\[
E_\Phi(T)=\sum_{u\in\mathcal O_K}\Phi(Nu/T)-T\Psi(0).
\]

For 0 < T <= 1, the zero row is bounded by |Phi(0)|, and Schwartz decay bounds the remaining rows by a convergent sum of (Nu)^(-A), with A > 1. For T >= 1, the same normalized Poisson identity yields

\[
E_\Phi(T)=T\sum_{h\ne0}\Psi(TNh)=O_{K,\Phi}(T^{1-A}).
\]

Therefore sup_(T>0) |E_Phi(T)| is finite. Fixed smoothing is essential to the stated constant. The proof applies to any fixed radial Schwartz Phi, and the source's compact Fourier support is a stronger available condition.

Finite inclusion-exclusion now proves

\[
\sum_{(u,g)=1}\Phi(Nu/H)
-H\Psi(0)\prod_{p\mid g}(1-(Np)^{-1})
=\sum_{e\mid g}\mu(e)E_\Phi(H/Ne)
=O_{K,\Phi}(\tau_K(g)).
\]

Consequently

\[
|\mathcal D[v]|\ll_{K,\Phi}
\frac1L\sum_g|v(g)|^2\tau_K(g).
\]

The assumed subpower coefficient-mass estimate and a fixed polynomial bound Ng << D^B absorb the ideal divisor function after redistributing arbitrary epsilon losses. This gives O(D^epsilon), with no dependence on H and no lower or upper condition on H/L.

The original smoothing sums over every u, including u = 0. For g > 1, its coprimality mask deletes that row; inclusion-exclusion implements this because sum_(e|g) mu(e) = 0. For g = 1, the zero row remains and is included in E_Phi(H). These conventions are consistent in every displayed formula, even for arbitrarily small positive H. Omitting u = 0 would change the exact identity by the corresponding unit-column term, although it would not invalidate a separate bounded-error estimate.

There is also a valid optional strengthening. In the exact source normalization, h ranges over the Eisenstein integers and Nh >= 1 for h != 0. If support(Psi) is contained in [0,C_Phi], then

\[
E_\Phi(T)=0\qquad(T>C_\Phi).
\]

For column support Ng <= uL, every divisor satisfies Ne <= uL. It follows that

\[
\boxed{H>C_\Phi uL\quad\Longrightarrow\quad\mathcal D[v]=0.}
\]

The strict inequality avoids any endpoint issue. This cutoff is a consequence of the source's band-limited smoothing; the uniform divisor-mass bound does not require compact Fourier support.

## 6. What the result permits analytically

The zero Fourier main term has size O(H D^epsilon) by the normalized coefficient-mass bound. The retained signed dual diagonal has the stronger size O(D^epsilon). For H >= 1, it follows that proving the strict dual off-diagonal estimate in (6.9) would suffice for the desired normalized raw moment.

This reduction needs the entire signed auxiliary sum and the original coupled Fourier kernel. The cancellation generally does not hold separately on a dyadic b or f block: the inverse divisor reconstruction crosses such blocks. Replacing mu(f) by its absolute value, taking independent nonnegative energies before centering, or dropping the literal nonunit masks destroys the proved mechanism. Likewise, applying separate A2 projections to the two columns requires preserving their possibly distinct auxiliary ideals, moving masks, phases, and reconstructed strict off-diagonal condition.

These are boundaries on further use, not defects in the reviewed theorems. The large-correction energy theorem and exact diagonal cancellation are complete at their declared scope. The remaining signed off-diagonal estimate is expressly unproved.

The final editorial delta makes this boundary more explicit, and its reconstruction formula is correct. For a correction triple t = (c,d,e), the original product column is reconstructed from the child pair by the factor s_t = c^3 d^3 e^4. Cross terms between two independently projected columns therefore have the pulled-back diagonal condition

\[
s_t n_1n_2=s_{t'}n'_1n'_2.
\]

Equality of the factor pairs would remove too small a diagonal, even when both correction triples are the unit triple: distinct allocations (a,b) and (b,a) have the same product column. The new paragraph correctly declines to infer a centered sesquilinear estimate from positive Hilbert-norm transfer. The only other final edit is a corrected link to the separately reviewed interaction-graph note. Neither edit changes a proved theorem or its hypotheses.
