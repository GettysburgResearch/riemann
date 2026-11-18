# Third review: relative Hilbert–Schmidt control and a conditional weak-law route

Reviewer: semantic_skeptic. Date: 17 November 2026. Scope: the finite matrix/limiting-law implication, not the sine-process construction or an arithmetic moment theorem. The finite-prefix clipped route has a separate review and needs fewer hypotheses.

**Conclusion:** the proposed chain is correct when "moment determinate" means Hamburger determinate (uniqueness among probability measures on the whole real line), or when an exponential moment supplies that stronger property. Stieltjes determinacy should not be silently substituted in this elementary proof without a separate argument identifying the whole-line moment law. The separately proposed sine-model exponential moment addresses this distinction; no original interpolation/probability proof is audited here.

Let F_T,G_T be Hermitian matrices on the same positive dimension d_T, and rho_T=||F_T-G_T||_HS/sqrt(d_T)->0. Sorted real eigenvalues satisfy

sum_i(lambda_i(F_T)-lambda_i(G_T))²<=||F_T-G_T||_HS².

One direct proof writes TrFG=sum_(i,j)lambda_i(F)lambda_j(G)|<u_i,v_j>|²; this matrix of weights is doubly stochastic. Rearrangement bounds that trace by the pairing of equally sorted eigenvalues, including negative values. Expanding the squared Hilbert–Schmidt norm proves the inequality. Consequently, for every bounded Lipschitz test function f,

|integral f dmu_F-integral f dmu_G|<=Lip(f)rho_T.

Thus a weak empirical-law limit transfers. Neither commutation nor positive semidefiniteness of F,G is required, but their common dimension and actual matrix-difference estimate are required.

Suppose every fixed normalized moment of F_T converges to the corresponding finite moment of a probability law nu on R. The second-moment bound gives tightness by Markov. To identify moment k in any weak subsequential limit, choose a fixed even2r>k. Convergence of the2r-th moments bounds integral|x|^(2r) uniformly, hence the k-th moment tails by C R^(k-2r). Continuous truncation therefore passes every fixed moment to the limit. Hamburger determinacy of nu identifies every subsequential limit with nu, proving full weak convergence. No uniformity in a growing moment order is needed; each order is fixed before taking T to infinity.

If nu is supported in[0,infinity) and nu({0})=0, the closed set(-infinity,0] has nu-measure0. Portmanteau then gives

n_+(G_T)/d_T->1.

The zero-atom hypothesis is essential for this exact conclusion from weak convergence alone: G_T=-I/d_T has empirical law tending to delta0 but no positive eigenvalues. Rare large negative outliers, by contrast, are allowed. They need not obstruct weak convergence or the positive proportion if their empirical mass tends to0.

For example, take d=k^6,F=I_d,G=I_d-diag(k²,0,...,0). Then rho=1/k->0 and both laws tend to delta1, but the normalized fourth moment difference diverges. This proves why the argument may not replace weak-law transfer by transfer of every polynomial moment or by an operator bound tending to0.

Now assume separately the exact zero-block inequalities

n_+(G_T)<=s1_T+s2_T+pairs_T,

N_T>=s1_T+2s2_T+2pairs_T,

with N_T>0 and nonnegative counts. Algebra gives s1_T>=2n_+(G_T)-N_T. If d_T/N_T->1, then s1_T/N_T->1, since also s1_T<=N_T. For a different limit d_T/N_T->delta, the same deduction only gives liminf s1_T/N_T>=2delta-1. Any fixed-bandwidth lambda<1 application must keep that dimension factor; approaching lambda=1 through separate fixed-lambda statements is a further quantified step.

This is an asymptotic density statement, not RH: density-one simple critical zeros can coexist with a sparse set of off-line or multiple zeros. No prime-side all-moment matching is proved by this conditional bridge. If moments or laws are random, the convergence mode must be specified and the conclusion stated in that same justified mode; deterministic/a.s. convergence cannot be silently obtained from convergence in probability.
