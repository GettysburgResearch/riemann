# Primary literature for the prefix inverse theorem

17 November 2026. The prefix Taylor coefficients give positive moments on the triangular multiplicity lattice, and the constant term gives the remaining simple mass. These primary works identify hypotheses needed for exact recovery, certify finite-jet information, or describe the inverse spectral ambiguity when full moments are indeterminate. [Exact prefix theorem](../audits/adversarial_reviews/director_prefix_inverse_round8.md)

Three source versions have full readings recorded. The remainder have selected primary text or theorem passages read, with locators and limitations in the JSONL. Journal identities and the exact local proof PDFs are tracked separately. [Machine-readable records](latest62_inverse_adjacent_records.jsonl) · [Inherited full-read audit](../audits/latest62_inverse_adjacent_fullreads.md) · [Lattice certificate audit](../audits/latest62_inverse_adjacent_lattice.md)

## Full moments and determinacy

### PAPER-INV62-HARDY · Hardy’s condition in the moment problem for probability distributions

Jordan Stoyanov, Gwo Dong Lin (2012). Teoriya Veroyatnostei i ee Primeneniya 57(4), 811–820. Selected passages read. Read the square-root criterion and discussion of the cosine-transform proof, sharpness statement, factorial-moment condition, and the two Hardy references. Later multivariate claims are outside this scope. [Primary PDF](../sources/latest62_inverse_adjacent/hardy_stoyanov.pdf)

For nonnegative X, E exp(c√X)<∞ for some c>0 implies Stieltjes determinacy. The condition is equivalent to a (2j)! moment envelope, and the exponent 1/2 is sharp for general nonnegative measures. Apply after normalizing ν by M₀>0. The director proof implements the same square-root symmetrization with cosh transferring a finite exponential moment to every positive competitor. Sharpness over arbitrary half-line laws does not establish sharpness over the triangular lattice. [Source version](https://www.mathnet.ru/php/getFT.phtml?jrnid=tvp&paperid=4485&what=fullt&option_lang=eng)

### PAPER-INV62-RATIO · Moment Determinacy of Powers and Products of Nonnegative Random Variables

Gwo Dong Lin, Jordan Stoyanov (2015). Journal of Theoretical Probability 28(4), 1337–1353. Selected passages read. Read selected statement and proof passages for the ratio-to-Carleman and ratio-to-Hardy implications. Product-specific sections outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/1403.0301.pdf)

The bound m_{j+1}/m_j=O((j+1)^2) implies both the Stieltjes Carleman condition and a square-root exponential moment. After extracting the true moments from the prefix germ, this offers a separate sufficient certificate via the ratios M_{j+1}/M_j for M₀>0. The actual proof instead directly bounds the square-root exponential moment. No asymptotic ratio bound follows just from the stated moment envelope. [Source version](https://arxiv.org/pdf/1403.0301v2)

### PAPER-INV62-GROWTH · On the Moment Determinacy of Products of Non-identically Distributed Random Variables

Gwo Dong Lin, Jordan Stoyanov (2014). arXiv. Selected passages read. Read Lemma 1, Theorem 1 and the start of its sharpness construction. Applications to products are outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/1406.1654.pdf)

Square-root exponential integrability is equivalent to a bounded limsup of m_j^{1/(2j)}/j and equivalent to m_j≤c₀^j(2j)!. Theorem 1 gives a nonnegative indeterminate law with m_j=O(j^{aj}) for every a>2. The bounds on the director’s Taylor-to-moment outputs can be compared directly with this factorial envelope. The arbitrary half-line example sets a limit on moment growth criteria, and the director supplies the separate same-lattice counterexample. [Source version](https://arxiv.org/pdf/1406.1654v2)


## Lattice feasibility and bounds

### PAPER-INV62-INFUSINO · The truncated moment problem on ℕ₀

Maria Infusino, Tobias Kuna, Joel L. Lebowitz, Eugene R. Speer (2017). Journal of Mathematical Analysis and Applications 452(1), 443–468. Selected passages read. Read constructions in §2, the interior/boundary argument and the extension in §8. The degree 4–5 algorithms and remaining proofs are outside this reading. [Primary PDF](../sources/latest62_inverse_adjacent/1504.02989.pdf)

Realizable boundary vectors have an annihilating nonnegative polynomial and a unique measure on its lattice zeros. Interior realization is governed by strict polynomial inequalities; §8 extends the criteria to lower-bounded infinite discrete supports. Normalize and translate the triangular lattice to {0,4,10,…}. The polynomial P_M is in the adjacent-pair family, with a minimum-node factor for odd degree. Its saturation is a direct special case. Interior jets permit planting mass at any lattice node, with C(0) preserved when there is simple-mass slack. [Source version](https://arxiv.org/pdf/1504.02989v2)

### PAPER-INV62-CUBATURE · The proof of Tchakaloff’s Theorem

Christian Bayer, Josef Teichmann (2006). Proceedings of the American Mathematical Society 134(10), 3035–3040. Whole source read. Read all six pages of v2, including the closed-cone supporting-hyperplane argument, the pushforward in Corollary 2, the admissible polynomial space and references. [Primary PDF](../sources/latest62_inverse_adjacent/tchakaloff.pdf)

Finite moments through degree n on a possibly unbounded support have positive cubature on that same support with at most n+1 points in one dimension. Corollary 2 permits any finite list of integrable test functions. Finite lattice jets belong to the actual convex hull of lattice moment vectors. Applying Corollary 2 with the extra function 1/(m−1)^2 also preserves the multiple contribution to C(0), using at most n+2 nodes. Exact finite jet agreement can therefore coexist with radically different support beyond the sampled moments. [Source version](https://arxiv.org/pdf/math/0502473v2)

### PAPER-INV62-DUAL · Optimal Inequalities in Probability Theory: A Convex Optimization Approach

Dimitris Bertsimas, Ioana Popescu (2005). SIAM Journal on Optimization 15(3), 780–804. Selected passages read. Read the generalized moment primal and dual, weak-duality proof, interior hypothesis for strong duality and boundary discussion. Later optimizers and bounds are outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/bertsimas.pdf)

A polynomial majorizing an event indicator on the allowed domain gives a moment upper bound. Strong duality is stated for interior realizable moment vectors, with a separate boundary discussion. On the triangular lattice P_M/P_M(μ_{M+1}) majorizes the tail indicator. Its integral gives a certified tail bound from the finite prefix jet. The result is sharp over profiles concentrated through μ_{M+1}; this does not assert pointwise optimality for all moment vectors. [Source version](https://doi.org/10.1137/S1052623401399903)


## Flat extension and finite reconstruction

### PAPER-INV62-FLAT · A generalized flat extension theorem for moment matrices

Monique Laurent, Bernard Mourrain (2009). Archiv der Mathematik 93(1), 87–98. Whole source read. Prior audit read all 12 published pages and reconstructed the truncated multiplication and unique extension mechanism. Inherited reading scope, with the title page and audit checked here. [Primary PDF](../sources/latest62_inverse_adjacent/laurent.pdf)

A flat Hankel matrix on a monomial set connected to 1 and its border extends uniquely at the same rank. A real positive semidefinite extension gives a finite atomic measure. Rank equality of H_r and H_{r−1} with exact positive moments through degree 2r certifies r-node recovery after 2r+1 nonconstant Taylor coefficients. The kernel gives support and the Vandermonde system gives weights. [Source version](https://homepages.cwi.nl/~monique/files/archivlm.pdf)

### PAPER-INV62-LOCALIZE · Truncated K-moment problems in several variables

Raúl E. Curto, Lawrence A. Fialkow (2005). Journal of Operator Theory 54(1), 189–226. Selected passages read. Read main theorems and set-up for flat extension with localizing matrices. Remaining proofs outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/curto.pdf)

A flat extension with positive localizing matrices gives a minimal-rank atomic measure on the associated semialgebraic set. The flat extension’s unique positive representing measure lies on the associated moment variety. For prefix moments with a separately certified cutoff M, the support K={μ₂,…,μ_M} has the polynomial description −P_M²≥0. This permits finite-support localization, whereas the unbounded triangular lattice requires discrete moment machinery. Given true prefix moments and a matching flat Hankel block, the recovered variety can instead be checked node by node. [Source version](https://arxiv.org/pdf/math/0507067v1)

### PAPER-INV62-PRONY · On the Accuracy of Solving Confluent Prony Systems

Dmitry Batenkov, Yosef Yomdin (2013). SIAM Journal on Applied Mathematics 73(1), 134–154. Selected passages read. Read the recurrence and reconstruction setup and the local inverse error statement and its Jacobian factorization. Numerical sections and other proofs are outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/1106.1137.pdf)

A finite confluent moment system satisfies an annihilating recurrence. At a regular point of the moment map, the local bound for a node error scales with noise divided by its highest-order amplitude. For the prefix ν an occupied multiplicity class is an ordinary Prony atom, with coefficient a_m and no derivative terms even for a repeated zeta zero. Small positive a_m precludes a uniform unknown-support guarantee in this model. With lattice support known, recovering only the weights avoids the node-inverse Jacobian. [Source version](https://arxiv.org/pdf/1106.1137v3)


## Positive superresolution

### PAPER-INV62-MINEXTRAP · Exact Reconstruction using Beurling Minimal Extrapolation

Yohann de Castro, Fabrice Gamboa (2012). Journal of Mathematical Analysis and Applications 395(1), 336–354. Selected passages read. Read the exact positive-measure theorem and nonnegative interpolation framework. Remaining algorithmic examples and Appendix proof outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/1103.4951.pdf)

An s-node nonnegative measure on an interval is recovered by generalized minimal extrapolation using 2s+1 observations from a homogeneous Markov system. For finitely supported prefix ν in a bounded interval, use monomials 1,x,…,x^{2s} and moments from the jet through b^{2s+1}; the underlying polynomial ∏(x−x_i)^2 enforces the same finite-support conclusion. Known lattice geometry supplies certificates of lower degree for adjacent nodes. [Source version](https://arxiv.org/pdf/1103.4951v2)

### PAPER-INV62-GAUSSIAN · Superresolution without Separation

Geoffrey Schiebinger, Elina Robeva, Benjamin Recht (2018). Information and Inference: A Journal of the IMA 7(1), 1–30. Selected passages read. Read exact recovery hypotheses and the certificate reduction, with Gaussian specialization statement. Full determinant construction outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/1506.03144.pdf)

The true M-node positive measure uniquely minimizes the stated objective under point-spread assumptions and more than 2M samples. The certificate interpolates a positive weight at occupied nodes and dominates it elsewhere. In the exact prefix moment model, choose the constant weight 1, measured by M₀, and certificate 1+∏(x−x_i)^2 in the span of measured moments through degree 2M. Equality forces lattice support on the roots and the lower moments give the weights. This applies the certificate mechanism with monomials, independently of the Gaussian determinant theorem. [Source version](https://arxiv.org/pdf/1506.03144v2)

### PAPER-INV62-POSSTABLE · Sparse non-negative super-resolution — simplified and stabilised

Armin Eftekhari, Jared Tanner, Andrew Thompson, Bogdan Toader, Hemant Tyagi (2021). Applied and Computational Harmonic Analysis 50, 216–280. Selected passages read. Read exact uniqueness via a T-system and the statement of the dual-margin/Wasserstein estimates. Long determinant and Gaussian constant proofs are outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/1804.01490.pdf)

A k-node positive measure on an interval is uniquely feasible from at least 2k+1 T-system samples. Quantitative versions require separate margin and approximation hypotheses. For bounded-support prefix competitors, an affine rescaling of the monomials gives a T-system. On the full known lattice, the square-support polynomial itself has a positive minimum off the finite support, so its measured moment integral divided by that minimum gives a certified off-support mass bound. The Gaussian numerical constants do not follow for a finite-N staircase. [Source version](https://arxiv.org/pdf/1804.01490v2)

### PAPER-INV62-FOURIER · Super-resolution of positive near-colliding point sources

Ping Liu, Habib Ammari (2023). Information and Inference: A Journal of the IMA 12(4), 3087–3111. Selected passages read. Read observation model, statements of upper/lower bounds and conditions in Theorem 2.3. Minimax proofs and numerical section outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/2212.00536.pdf)

With a fixed positive sparse clustered class and bounded-band Fourier observations, Theorem 2.3 quantifies the superresolution factor in the worst-case location and amplitude errors. Prefix moments determine derivatives at zero of the Fourier transform when they exist. With a separately certified common cutoff x≤X, the order-n Taylor remainder on |ω|≤Ω is at most M₀(2πΩX)^{n+1}/(n+1)! for the transform with e^{2πiωx}. Fourier recovery guarantees still require the stipulated sparsity, amplitude and geometry assumptions; the ambient continuous-cluster lower bound is not a lower bound on the restricted triangular lattice. [Source version](https://arxiv.org/pdf/2212.00536v1)


## Inverse spectral ambiguity

### PAPER-INV62-BERG · Indeterminate Stieltjes moment problems revisited

Christian Berg (2026). Arabian Journal of Mathematics 15(2), 561–571. Whole source read. Prior audit read all 15 pages in v1, §§1–4 and references, and reconstructed selected proofs. Inherited reading scope; title page and reading notes checked here. [Primary PDF](../sources/latest62_inverse_adjacent/2407.08511.pdf)

Different self-adjoint extensions of an indeterminate minimal Jacobi operator have different cyclic measures. For Stieltjes indeterminacy the Friedrichs solution uniquely maximizes the bottom of the support among Hamburger solutions. The moments of a hypothetical indeterminate prefix profile would fix the common Jacobi coefficients and might leave the operator realization undetermined. Lattice-preserving ambiguity needs its own construction. The actual Stieltjes tail criterion selects a unique half-line measure. [Source version](https://arxiv.org/pdf/2407.08511v1)

### PAPER-INV62-JACOBI · Indeterminate Jacobi operators

Christian Berg, Ryszard Szwarc (2025). Journal of Operator Theory 93(1), 123–145. Selected passages read. Read the minimal operator setup and selected statements about domains of the extensions and their supporting zero sets. Remainder of the 29-page preprint outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/2301.00586.pdf)

The closed minimal Jacobi operator of an indeterminate sequence has deficiency indices (1,1). The Nevanlinna parameters give distinct extremal supports and different domains, whose distinction is visible in the explicit sequences in §3. Gram–Schmidt on the entire recovered M_j fixes the minimal Jacobi coefficients when all Hankel matrices are positive definite. For an indeterminate synthetic sequence this need not fix a self-adjoint boundary condition. No operator or support involving individual zeta ordinates is constructed. [Source version](https://arxiv.org/pdf/2301.00586v1)

### PAPER-INV62-EXTREMAL · Special N-extremal solutions to indeterminate moment problems

Christian Berg, Ryszard Szwarc (2026). Complex Analysis and Operator Theory 20(6), article 138. Selected passages read. Read the Friedrichs/Krein setup, the negative-first-moment constraints and selected proof of Theorem 3.3. Other weighting regimes outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/2603.26302.pdf)

For a normalized Stieltjes-indeterminate sequence, dividing the Friedrichs measure by x gives a determinate measure; dividing other specified N-extremal measures by x gives indeterminate sequences with new total mass t. For any lattice-supported prefix profile, σ=dν/x has moments of degree j≥1 equal to M_{j−1}, and degree zero equal to ∫x⁻¹dν. The example explains how this last scalar can select among negative moment data in indeterminate half-line problems. C(0) weighs a_m by 1/(m−1)^2 and includes W₁, so it does not supply that inverse moment directly. [Source version](https://arxiv.org/pdf/2603.26302v1)

### PAPER-INV62-FRACTION · Continued-fraction characterization of Stieltjes moment sequences with support in [ξ, ∞)

Alan D. Sokal, James Walrad (2026). Proceedings of the American Mathematical Society. Selected passages read. Read the exact continued-fraction condition, including the insufficiency of the odd-coefficient lower bound. Proof and remaining examples outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/2404.12131.pdf)

The parameterization of the S-fraction by nonnegative g_i is equivalent to the existence of a representing measure supported on [ξ,∞). At ξ=2, apply to the full moment sequence M_j after triangular extraction to test the left-edge half-line support condition. This criterion cannot enforce discrete gaps or constrain the largest occupied multiplicity. [Source version](https://arxiv.org/pdf/2404.12131v1)

### PAPER-INV62-SIMON · The Classical Moment Problem as a Self-Adjoint Finite Difference Operator

Barry Simon (1998). Advances in Mathematics 137(1), 82–203. Selected passages read. Read the operator correspondence and criteria statements, with selected proof passages. The long Padé and entire-function analyses are outside scope. [Primary PDF](../sources/latest62_inverse_adjacent/simon.pdf)

The Hamburger operator correspondence distinguishes essential self-adjointness from multiple self-adjoint extensions. The Stieltjes criteria distinguish half-line determinacy from Hamburger determinacy, and the paper develops the Jacobi strong-resolvent approach to Padé convergence. The lifted signed-square-root distribution in the prefix proof is a different moment sequence and a different Jacobi operator from the original ν. Stieltjes determinacy of ν alone does not imply that its minimal Jacobi operator is essentially self-adjoint. [Source version](https://arxiv.org/pdf/math-ph/9906008v1)

## Selection and source boundaries

The Laurent–Mourrain preprint and published article count once. The two Stieltjes files originally staged beside this corpus are incomplete downloads and are outside the records. Related heat-flow papers, signed near-collision work and the newer density-tail criterion have different input hypotheses. No claim of full reading, publication priority, or a global multiplicity bound follows from their presence among the archived leads.
