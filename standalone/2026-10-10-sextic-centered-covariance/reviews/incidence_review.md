# Independent review of the signed incidence and Hermitian gcd adapters

**Reviewer:** replica_extraction_attack, independent of the mathematical author and the root-owned checker.

**Final verdict:** PASS for the specified source-conditional signed component theorems. The exact final source below includes the row-weight, character-multiplier and zero/one-active-axis corrections. No full moment or new zero-free theorem is approved.

**Mathematical source reviewed:** /workspace/scratch/6ec6134c1535/singleton_cancellation_attack.md, SHA-256 714c9f69b9db58f3ada027c8902ded42b781d759b746c117f952748baafd4cc2, Sections 1–8. The initial review checkpoint was 6a7503108664ca6b9fe0a9816a3317338b8fa16af2209e7b108f2dc5d0e58447; the corrections were read and checked in the final bytes.

**Checker source reviewed and independently run:** /workspace/scratch/6ec6134c1535/riemann/standalone/2026-10-10-sextic-centered-covariance/checks/check_incidence_adapters.py, SHA-256 35f2913340ecd4f5b471b63af67d4c5bdf92e57a58e8d68c86d3042f8f450dbf.

**Imported analytic premises:** the native smaller-scale, moving-exclusion second moment in PR #913, head 6498d6cc2eded03159c7332b25fd224ad07f89c1, FOURTH_MOMENT_ATTACK.md, Proposition 2.1, with the finite smooth seminorm dependence inherited from its pinned October 5 Poisson/canonical proof. The optional beta<1 assertions additionally require its Section 8 uniform reciprocal hypothesis. This review verifies the new deductions from those stated inputs, not the original analytic theorem itself.

## 1. Exact forward correction and the two second moments

Outside the moving exclusion C, multiplication of

\[
\frac{1-\sum_i z_i}{\prod_i(1-z_i)}
\quad\text{by}\quad\prod_i(1-z_i)
\]

gives the required disjoint squarefree local factor. Its coefficient at a nonzero exponent vector is 1 minus the number of its active axes, independently of the sizes of the positive exponents. At a prime in C the correction is the product of the inverse one-axis factors and every coefficient is one. At S both sides retain the already imposed exclusions.

This is a forward correction; no inverse factor 1/(1-sum z_i) is present. Hence there is no fixed-small-prime radius obstruction. Row characters, including conjugates and nonunit zeros, are attached to each monomial by complete multiplicativity. The integer coefficient e_C need not have absolute value at most one. Only the separate character product has that bound; the final note now says this explicitly.

For two selected axes at weights 1/2 and the others at beta>1/2, only the selected mutual pair is at the divergent boundary. Replacing their two weights by 1/2+delta makes every support of size at least two summable over good primes. Restoring the original two weights on the actual finite support costs O(D^(2delta)). At mask primes the finite geometric product is O((NC)^eta), uniformly in polynomially bounded C. Choosing delta and eta before the asymptotic parameter proves the claimed subpower correction norm.

After this exact separation, two row-L2 estimates and row Cauchy give H times the square root of their two lengths. Every remaining factor is bounded pointwise. The shifted column scales, the fixed test functions and the moving exclusions satisfy the stated native input. No arbitrary arithmetic coefficient vector is substituted into that native second moment.

## 2. Odd repeated incidence factors and the coupled tests

An incidence with multiplicity m and signed count e has exactly mu(q)^m nu(q)^e times the literal row product. If m is odd, its Möbius coefficient is mu(q). If e is 1 modulo 6, the row character is chi_q(u); if e is 5, it is its conjugate, retaining zero on nonunits. The latter second moment follows by conjugating the entire sum and using the finite-order datum conjugate(nu^e). This belongs to the fixed finite family of data required by the input. Since m and e have the same parity, the note's eligibility criterion automatically selects only odd incidences.

When e is 3 modulo 6, the row character is quadratic. Such a factor is not selected for the native sextic M2; it uses only the explicitly optional pointwise premise, or counting at beta=1. Every even incidence is frozen before the remaining row estimate. Its exact row factor, including an e=0 coprimality mask, has absolute value at most one.

Mellin inversion on the original 2k compactly supported column tests separates the coupled products without an arithmetic change. For an odd incidence I its normalized test is

\[
\psi(x)x^{-i\sum_{i\in I}t_i}.
\]

Its fixed C^J seminorm is polynomial in 1+sum|t_i|. The same is true after conjugation and after the finite forward-correction shifts, because the test itself is unchanged and only its positive scale changes. The original Mellin transforms decrease faster than every power, so the product of the finite test seminorms is integrable. These imaginary norm powers are smooth test parameters with explicit bounds, not moving Hecke infinity types inserted into an automorphic theorem.

The first block bound therefore is exactly

\[
H D^\epsilon\left(\prod_{\text{even }I}Q_I\right)
(Q_JQ_L)^{1/2}
\prod_{\substack{\text{odd }I\\I\ne J,L}}Q_I^\beta.
\]

The mass identity product Q_I^m_I asymp D^(2k) gives

\[
\prod_I Q_I\asymp D^k\sqrt{L_1/\Gamma},
\]

and hence the displayed normalized criterion in Theorem 4.1. Choosing the two largest eligible scales minimizes the bound obtained from only these M2 and pointwise inputs.

## 3. Signed selections and the fixed-core theorem

The fixed repeated-core estimate charges a complete singleton sum at each selected repeated-core configuration. Under its budget condition the arithmetic core weights become precisely product (Nc_I)^(-1); each ideal lies in a polynomially bounded range, so a fixed product of harmonic sums gives the claimed subpower total. Arbitrary deletions inside a singleton sum are not covered, and the note correctly distinguishes them.

Similarly, the odd-incidence theorem bounds the absolute value of each complete signed smooth block. It may then sum those absolute block values over any selected collection satisfying the budget condition. This does not bound the sum of absolute values of all individual tuple terms.

For the sector with singleton primes confined to at most two axes, the final proof explicitly includes the 0- and 1-active-axis cases: they cost O(H) and O(H sqrt(X)), respectively, by counting rows or Cauchy with the constant sequence. The 2-active-axis case uses the proved two-factor estimate. Unit subtraction is a finite exact expansion, and each frozen unit forces its original scale into a fixed compact interval.

## 4. Exact global Hermitian gcd identity

For squarefree c,

\[
\sum_{q\mid c}\sum_{\substack{d\mid q\\Nd\ge R}}\mu(q/d)
=\sum_{\substack{d\mid c\\Nd\ge R}}\sum_{h\mid c/d}\mu(h)
=\mathbf1_{Nc\ge R}.
\]

Thus w_R vanishes below R and has absolute value at most tau(q). Extracting q from all 2k original squarefree columns forces all residual columns to be coprime to q. The common coefficient is

\[
\mu(q)^{2k}|\nu(q)|^{2k}|\chi_q(u)|^{2k}
=\mathbf1_{(u,q)=1}.
\]

There is no norm factor from this extraction, and W(Nn/D) becomes exactly W(Nm/(D/Nq)). The inner residual expression is the positive 2k-th power of the excluded native inverse sum, multiplied by the retained row weight. The weights w_R themselves may be negative; the full exact identity is used before absolute values.

For rho=1+2(k-1)beta, the stated uniform excluded weak moment is H D^epsilon X^rho. The finite tail is supported on R<=Nq<=bD, so X lies in [1/b,D]. Summing tau(q)(Nq)^(-rho) gives R^(1-rho) up to a subpower, because rho>1. The exact cutoff is

\[
\frac{\rho-k}{\rho-1}=\frac{2\beta-1}{2\beta}.
\]

This verifies R>=D^(1/2) at beta=1, R>=D^(3/7) at beta=7/8, and R>=D^(59999/139999) at the cited conditional beta. This global Hermitian sector is a distinct, narrower object than the norm of an old within-half polynomial gcd tail. The source correctly preserves that distinction.

## 5. Row-weight correction and the proved Schwartz adapter

The initial checkpoint conflated compact row support with the Fourier-compact Schwartz majorant used in PR #914's A2 note. The final source distinguishes that profile from the separate compactly supported majorant in CONDUCTOR_SECTORS.md and supplies the following valid adapter as its Lemma 1.1.

On the j-th dyadic row annulus use the native input with reference

\[
D_j=2^{j/(1+\theta)}D,
\qquad H_j=D_j^{1+\theta}=2^jH.
\]

Keep every actual column scale, exclusion ideal and incidence block fixed. Their polynomial bounds in D remain valid in D_j. Every preceding estimate costs at most H_j D_j^(epsilon_0) times its original column-length expression. A fixed Schwartz profile contributes O_A(2^(-Aj)) on the annulus. The sum therefore converges for A>1+epsilon_0/(1+theta) and is O(H D^(epsilon_0)) times that same expression. The core budgets involve the actual column scale D, so they are unchanged. The optional uniform pointwise input is also applicable at D_j because its conductor hypotheses quantify over every reference parameter. The zero row is a separate bounded unit contribution and is harmless.

This argument resolves the source-row mismatch without discarding any tail or inserting an unproved moving-row bound.

## 6. Independently reproduced checker scope

Normal and optimized Python executions both pass exactly 36,190 predicates and produce byte-identical JSON, SHA-256 a04fcadefc94a6627a9a7b9ead2f45c45916df0c3c134b72759ce483565f3881. The independently produced records are /workspace/scratch/6ec6134c1535/incidence_review_normal.json and /workspace/scratch/6ec6134c1535/incidence_review_optimized.json. The checker uses integer coordinates in Z[zeta_6] and exact rational cutoff exponents. Its explicit require checks remain enabled under python -O.

The tested finite predicates are:

- local forward Euler identities for the listed 2-, 4-, and 6-axis exponent boxes, with mixed signs and the nonunit value;
- incidence parity, the native Möbius eligibility condition, literal nonunit zeros, and the mass exponent identity at every nonempty incidence for k=2,...,6;
- genuine sextic residue symbols at the two split prime ideals of norms 7 and 13, over the full 54-row norm ball Nu<=15, including all six units and 12 rows with a nonunit symbol;
- exact squarefree extraction and full Hermitian gcd reconstruction for moment orders 4 and 6 and all eight displayed norm thresholds;
- the rational global-gcd and upper-branch triple-core cutoff identities at the three displayed beta values.

The finite column datum in the gcd test is a sampled unitary multiplicative datum on its two-prime support; the checker does not certify that it extends to a globally prescribed Hecke character. That extension is unnecessary for the tested algebraic identity, whose proof is already independent of such a construction. The checker does not verify the native analytic M2 premise, a Mellin contour argument, any asymptotic component estimate, or a zero-free result. Its finite coverage is not being used as an infinite proof.
