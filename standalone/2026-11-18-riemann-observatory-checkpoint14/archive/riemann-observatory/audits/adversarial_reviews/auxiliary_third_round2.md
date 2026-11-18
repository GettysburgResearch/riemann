# Third independent reconstruction: finite bounded auxiliary coupling

Reviewer: equivalences agent.2026-11-17. The reviewer received the statement and sharp example but did not read the parent or advocate proof before writing the reconstruction below. This is ordinary mathematical review, not formal verification.

## Statement and domain

Let A be self-adjoint with compact resolvent on a Hilbert space H_A; its spectrum may extend in both directions. Let D be self-adjoint on a finite-dimensional space of dimension M, and B:C^M→H_A bounded. Define

H=[[A,B],[B*,D]], Dom(H)=Dom(A) directsum C^M.

For K>0 define Delta_T(K)=#sigma(T) in(2K,4K] minus2 times#sigma(T) in(K,2K], counting multiplicity. Then

|Delta_H(K)-Delta_A(K)|<=3M.

No lower bound on A and no common indexing of its two-sided eigenvalues are needed. The bounded block coupling assumption is essential to this proof; arbitrary self-adjoint extension/boundary coupling is outside the claim.

## Independent proof

First consider a finite-dimensional Hermitian matrix T with an n-by-n principal submatrix A_0 obtained by removing M rows and columns. Cauchy interlacing gives, for every real t,

0<=F_T(t)-F_(A_0)(t)<=M,

where F counts eigenvalues at mostt. To check the direction, adjoining an auxiliary dimension can move the old eigenvalues down, while adding at most M eigenvalues below any threshold. More formally, ordered interlacing lambda_j(T)<=lambda_j(A_0)<=lambda_(j+M)(T) yields exactly the displayed count inequality.

For any three ordered thresholds t_1<t_2<t_3,

#(t_2,t_3]-2#(t_1,t_2]=F(t_3)-3F(t_2)+2F(t_1).

Write g(t)=F_T(t)-F_(A_0)(t), with0<=g<=M. The difference of the two expressions is g(t_3)-3g(t_2)+2g(t_1), which lies in[-3M,3M]. This proves the finite assertion, including endpoints exactly.

For the infinite case, let P_R=1_[-R,R](A). Compact resolvent makes P_R finite rank and P_R→I strongly. Since the domain of B is finite dimensional, B_R=P_RB converges toB in operator norm. On H_A directsum C^M set

H_R=[[A,B_R],[B_R*,D]].

The bounded perturbations H_R-H converge to zero in norm. In particular their resolvents converge in norm. Each H_R splits orthogonally into the finite matrix

T_R=[[A restrictedto ranP_R,B_R],[B_R*,D]]

and the untouched A restrictedto ran(I-P_R). On the finite matrix, the principal-submatrix argument gives the same3M bound.

If K,2K,4K lie outside the spectra of H and A, norm-resolvent convergence and compact resolvent imply eventual equality of the ranks of the corresponding bounded-interval spectral projections. One can justify this with Riesz projections around a rectangle enclosing each finite spectral interval; the contour lies in a common resolvent set for all sufficiently largeR. Since the untouched A tail has no eigenvalues in the bounded windows onceR is large, the finite-matrix3M inequality passes to H and A.

For arbitrary endpoint eigenvalues, choose epsilon>0 so small that neither spectrum contains a point in any(t_j,t_j+epsilon], where(t_1,t_2,t_3)=(K,2K,4K), and all shifted thresholds avoid both spectra. This is possible because the spectra are discrete and each bounded interval contains finitely many eigenvalues. The half-open interval counts for H and A are unchanged on replacing everyt_j byt_j+epsilon: eigenvalues exactly at a threshold remain assigned to the same adjacent half-open interval. The finite-dimensional bound above applies to any three ordered thresholds, so it applies to the shifted triple even though it is no longer geometric. Then pass to the norm-resolvent limit as in the preceding paragraph. This proves the original endpoint-sensitive statement.

At no point are two infinite half-line counting functions subtracted. Half-line counts appear only in finite compressions. This is the necessary repair if one tries to use interlacing directly for a two-sided unbounded A.

## Sharpness

Take K=1,M=1,A=[3/2],D=[3/2],B=[1]. The eigenvalues of H are1/2 and5/2. Thus Delta_A=-2 and Delta_H=1, and the absolute difference is3=3M. For generalM, direct sums of this example give equality3M, so the constant cannot be reduced.

## Compact-resolvent and scope checks

- Diag(A,D) has compact resolvent, and bounded finite-rank perturbation preserves compact resolvent by the resolvent identity. All bounded-window counts are finite.
- B_R→B in norm uses finiteM, not merely strong convergence of P_R on arbitrary bounded operators.
- Endpoint shifting is necessary for a proof by spectral-projection convergence; raw interval counts can jump under norm-small perturbations at an endpoint eigenvalue.
- Zero modes do not enter the intervals for K>0. No separate zero-mode convention is needed.
- This result constrains changes to a spectrum caused by finite-dimensional bounded attachments. It does not identify the zeta zero spectrum or control unbounded boundary-condition perturbations.

Verdict: independently verified with no issue found under the stated bounded-coupling and finite-M assumptions. Prior publication novelty unassessed.

## Comparison with existing proof

Pending at the time of this reconstruction; record comparison separately after the parent identifies or exposes the proof file.

After completing the independent argument, the reviewer opened auxiliary_skeptic_round2.md. Its proof agrees on finite Cauchy interlacing, full two-sided spectral cutoffs, operator-norm convergence of the bounded finite-dimensional coupling, and spectral-projection rank stability. It handles endpoints by scaling K from above; the independent proof here instead shifts the three thresholds additively and uses the more general three-threshold finite inequality. Both preserve the half-open/right-closed counts and are valid. The advocate supplies an additional negative sharp witness; the positive witness and its direct sums already establish sharpness. No disagreement found.
