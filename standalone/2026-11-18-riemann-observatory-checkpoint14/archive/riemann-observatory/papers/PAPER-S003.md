# PAPER-S003 — Endres and Steiner,2010

**Identity.** Sebastian Endres and Frank Steiner, *The Berry–Keating operator on L²(R_>,dx) and on compact quantum graphs with general self-adjoint realizations*, Journal of Physics A: Mathematical and Theoretical43(2010),095204. DOI10.1088/1751-8113/43/9/095204. arXiv0912.3183 first2009-12-16; inspected v5,2011-05-09: https://arxiv.org/pdf/0912.3183v5 . Institutional copy independently accessed: https://www.uni-ulm.de/fileadmin/website_uni_ulm/nawi.inst.260/paper/09/tp09-7.pdf . Access2026-11-17. Publisher metadata records publication2010-02-15. Institutional copy not assumed to be the version of record.

**Audit scope.** Level0 complete. Primary text inspected in§2,§§6–9,§15 and Example16.2, plus relevant introductory/concluding passages; §§4–5 and10–14 not fully audited. Whole-work Level1 incomplete. Local Level2 audit reconstructed the log-coordinate unitary, scalar endpoint spectrum, and count normalization. An apparent local factor-two/definition inconsistency was sent for independent review; it does not undermine the fixed-graph no-go conclusion. Do not label the whole article erroneous.

## Results and exact hypotheses

1. On L²(R_+,dx), the differential expression H_BK=−iℏ(xd/dx+1/2) initially on C_c^∞(R_+) is essentially self-adjoint with purely continuous spectrum (§2,p4–6). The Mellin modes(10)–(20) are generalized eigenfunctions, not L² eigenvectors.
2. On E finite edges[a_j,b_j],0<a_j<b_j<∞, the direct sum has deficiency indices(E,E); fixed self-adjoint domains correspond to maximal isotropic endpoint spaces. Proposition8.1,p15, uses matrices A,B with AB*=BA* and rank(A,B)=E. The normalization includes sqrt(endpoint) factors, equations(60)–(73).
3. Proposition9.1,p17: k is an eigenvalue iff det(I−S(A,B)T(a,b;k))=0, T=diag(exp(iklog(b_j/a_j))); S=i(A−iB)(A+iB)^(−1) is unitary and independent of k. Kernel multiplicity equals operator eigenvalue multiplicity.
4. Theorem15.4,p27: the squared second-order operator has count N(λ)~L sqrtλ/π, with L=∑log(b_j/a_j). Theorem15.6,p28: this fixed compact class cannot realize the complete Riemann-zero spectrum because its counting growth has the wrong order. The comparison needs no RH: the full nontrivial zero count grows like TlogT.

## Count-convention issue under review

Theorem15.5,p27,equation(139), explicitly refers to **positive** eigenvalues yet prints N(k)~Lk/π. Example16.2,p29,equation(150), gives the single-edge spectrum k_n=2π(n+c)/L, n∈Z,c∈[0,1). Counting only0<k_n≤K yields LK/(2π)+O(1); counting absolute values gives LK/π+O(1). Both the v5 PDF render and institutional PDF print the positive wording and L/π coefficient. The local ambiguity is naturally repaired either by changing the coefficient or counting both signs. The no-go theorem only uses linear versus KlogK growth and survives either repair. Pending independent adjudication, this is a count-normalization inconsistency requiring expert review, not an attack on the paper's principal conclusions. Searches for an erratum were limited and yielded none; absence was not established.

## Independent reconstruction

With y=log(x/a_j), g_j(y)=sqrt(x)f_j(x), the norm and operator reduce exactly to L²([0,l_j],dy) and −i d/dy. For one edge every self-adjoint boundary condition is g(0)=exp(−2πic)g(l); the solution g(y)=Ae^(iky) gives exp(ikl)=exp(2πic), hence the spectrum in(150). This calculation is independent of the paper's general graph trace formula.

The general finite-channel phase-flow proof gives |N_+(K)−LK/(2π)|<E and a three-height curvature bound<3E. It is developed separately in the campaign note. It assumes a fixed energy-independent S and positive finite edge lengths. It is not a theorem about arbitrary Hilbert–Pólya models.

## Dependency graph and reuse

Boundary form → endpoint maximal isotropic spaces → unitary S → exact secular determinant → phase flow / trace formula → linear counting law → no-go. The useful negative knowledge is a sharply delimited model exclusion. Adding bounded real scalar edge potentials only changes endpoint phases under a unitary gauge and cannot evade the finite-channel counting barrier. Infinite graphs and genuine auxiliary dynamics remain outside its hypotheses.

## Research question

For a self-adjoint auxiliary system eliminated into S(k), bound total phase advance and its dyadic curvature in terms of auxiliary spectral complexity. Can causality or resolvent positivity prevent a small auxiliary model from supplying the missing K-scale curvature? First establish an exact realization theorem; an arbitrary k-dependent unitary matrix is not automatically the boundary condition of one self-adjoint operator.
