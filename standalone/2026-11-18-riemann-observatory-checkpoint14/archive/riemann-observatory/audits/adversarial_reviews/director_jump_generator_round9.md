# Director adjudication: the logarithmic jump group, its domains and its exact antecedent

17 November 2026. I independently reconstructed the closed domain, resolvent, projections, metric classification and subspace argument after reading both complete proofs, jump_generator63_proponent.md and jump_generator63_skeptic.md. I also checked the source intertwining and the primary Sklyar–Marchenko theorem. Historical evidence is in finite_moment63_manzur_noor_operator_antecedents.md. All results are scoped ordinary reconstructions, not a new-operator or publication-priority claim.

## 1. Source identity and a closed operator, not a finite matrix

Use S=ℓ²(w), w_n=1/[n(n+1)], b_0=0, j_n(b)=b_n−b_(n−1). The already adjudicated source group satisfies

    (J_t b)_n=Σ_(r≤n) r^(it) j_r(b).

Sklyar–Marchenko's 2014 logarithmic multiplier group on the completion with norm ‖(I−S_forward)c‖_ℓ² is exactly the time-reversed adjoint of the Manzur–Noor group: the difference map U is unitary onto ℓ² and T_(−t)^* U=U D_t. The equality follows first on finite coefficients from Manzur–Noor(15), then by density. Their later resolvent work is a direct primary antecedent. Use the latest preprint for current statements; earlier versions have separately documented superseded clauses. The source's RH membership application is distinct from this established operator family.

Put D b=(log n)b_n and

    (H b)_n=Σ_(r<n) log((r+1)/r)b_r.

Summation by parts gives J_t=M_t−it H_t, with ‖H_t‖≤2: in log coordinates it is dominated by convolution with e^(−u/2)1_(u≥0). Moreover H_t→H strongly by dominated convergence. The exact strong generator is

    G=i(D−H),
    Dom G={b: Σ w_n(log n)²|b_n|²<∞}.

The diagonal difference quotient and the bounded H_t term prove both inclusions in this domain description. Its graph norm is equivalent to ‖b‖+‖Db‖. Finite cells, hence finite jumps, form a graph core. For Re s>1/2, the Mellin expression is M(Gb)=−i[(Mb)' +(Mb)/s], including the rational correction. Merely writing the diagonal jump rule would not identify the closed domain.

## 2. Exact resolvent and spectral geometry

For λ outside {i log n:n≥1}, set q_n=(λ−i log n)^(-1). The full resolvent is

    R_λ=diag(q_n)−iH diag(q_n q_(n+1)).

Indeed its jumps are q_n j_n(b), and q_n−q_(n+1)=−i log((n+1)/n)q_nq_(n+1). The formula is bounded on S; the coordinate equation puts its image in Dom G, and the jump recurrence proves two-sided inversion. Both diagonals tend to zero, so the resolvent is compact. The entire spectrum is therefore exactly the algebraically simple eigenvalues i log n, with eigenvectors u_n=1_[n,∞). The rank-one Riesz projection is

    P_n b=j_n(b)u_n,      ‖P_n‖=sqrt(2n).

The norm follows from ‖u_n‖²=1/n and ‖j_n‖²=2n², including n=1. It rules out a Schauder eigenbasis in every ordering. Complete finite-jump span and a graph core are compatible with this failure. Natural spectral partial sums have norm sqrt(N+1), but every b has a convergent subsequence because liminf |b_N|²/N=0. This last fact follows directly from summability against w_n.

The resolvent singular values satisfy s_j(R_λ)~1/log j: its diagonal has that asymptotic and the H times diagonal remainder has singular values O(1/log²j); the two Weyl inequalities with indices proportional to j finish the comparison. Thus it belongs to no finite Schatten class. For each fixed t≠0 the group element instead has unit-circle spectrum, since its powers and inverse powers grow only linearly and the eigenphases n^(it) are dense on that circle. Phases outside the countable eigenphase set have continuous spectrum, not additional eigenvectors.

This explicit spectrum counts integers exponentially on the positive imaginary axis. Zeta zeros enter through the arithmetic subspace and its Mellin annihilators, not as these eigenvalues.

## 3. Every bounded invariant positive metric is weaker

Invariance makes distinct u_n orthogonal in any bounded positive invariant form. Every such form is exactly

    Q(b)=Σ d_n |j_n(b)|²,
    d_n≥0,   sup_n n²d_n<∞.

Necessity follows by testing the single cell u_n−u_(n+1); sufficiency follows from the two-term difference inequality. Density of finite jumps then gives the formula on all S. The form is injective iff every d_n>0. It is never coercive: Q(u_n)/‖u_n‖²=nd_n→0. A bounded injective invariant metric therefore exists, but its inverse is unbounded and completion changes the topology. The source's difference intertwiner supplies one such example. A boundedly invertible change of metric cannot unitarize the group, also directly contradicted by its sharp norm sqrt(1+t²)+|t|. The same applies to any fixed nonzero time through its powers.

## 4. Whole-flow invariant subspaces

If a closed V satisfies J_t V⊂V for every t≥0, its Laplace resolvent preserves V for Re λ>0. Quotient-valued analyticity continues that property over the connected resolvent set, so every P_n preserves V. The convergent subsequence of spectral partial sums then proves

    V=closed span{u_n:u_n∈V}
     ={b:j_n(b)=0 whenever u_n∉V}.

Conversely each such jump-support subspace is invariant at all real times. Every vector with all jumps nonzero is forward-orbit cyclic. In particular the source's B h_k has jumps k1_(k|n)−1, all nonzero. Whole-flow invariance of its arithmetic closed span forces density. The source's stronger criterion at a single fixed nonzero time uses additional arithmetic information. These two formulations and the first-generator criterion in the separate director note must not be conflated.
