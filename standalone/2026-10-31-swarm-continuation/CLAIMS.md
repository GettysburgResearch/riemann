# Claim ledger and exact remaining obligations

Status: proposed components of this continuation. The identifiers below are local to this new packet and do not change any integrated claim. The full proofs, domains, and normalizations are in the linked manuscripts.

| ID | Statement and quantifiers | Evidence | Boundary |
|---|---|---|---|
| SW2-A1 | For `N>=1`, `a0>=100(N+1)`, `1<=a1<a0`, the old integrated positive-part budget exceeds the initial minimum eigenvalue by more than `0.5 log((N+1)/a1)-29/12`. It cannot succeed when the ratio is at least 128. | [Budget proof](anchor/ANCHOR_BUDGET_OBSTRUCTION.md); exact scalar margins and a positive two-dimensional control. | Failure of a sufficient estimate, not endpoint indefiniteness. |
| SW2-A2 | If `a_j->infinity` and `N_j/a_j->L<infinity`, then `P_j->Q_(2L)` strongly; for infinite ratio the limit is I. | [Bridge Theorem 1](anchor/LAGUERRE_WINDOW_BRIDGE.md); exact cross-projection formula. | Not operator-norm convergence. |
| SW2-A3 | For `eta>0`, `a>eta`, all vectors in `V_(N,a)` satisfy the displayed exponential-weight bound W. For finite L, the complete compressed prime operator and its adjoint converge strongly to the finite delay operator on `[0,2L]`. | Bridge Lemma 2, Corollary 3, Theorem 4; full summable Mangoldt majorant. | Applies at fixed finite L, not uniformly as L tends to infinity. |
| SW2-A4 | For `0<L<infinity`, the actual xi matrices satisfy `liminf lambda_min G >= lambda(2L)`; a positive compact-window lower bound gives eventual matrix positivity. | Bridge Theorem 5; spatial/frequency compactness of moving minimizers. | Conditional on the specified window inequality; no unbounded positive windows are supplied. |
| SW2-A5 | The compact-window floor is nonincreasing and continuous for `ell>0`. The compressed delay Hermitian norm is `cos(pi/(ceil(ell/t)+1))` for `0<t<ell`. | Bridge Section 6; chain decomposition and compactness/core approximation. | Continuity does not keep the floor positive indefinitely. |
| SW2-B1 | The complete theta-sampled kernels converge with error at most `C_(R,c)(1/a+exp(-cM/(2a)))` for every fixed R, `0<c<2pi`, `a>=1`, and integer `M>=0`. | [Companion Theorem A](bessel/COFINAL_COMPANION.md); full-source Skellam estimate and cutoff control. | Constants depend on the fixed weight. |
| SW2-B2 | The actual companion J converges locally uniformly to the explicit entire `J_infinity` along every cofinal sequence `a->infinity`, `M/a->infinity`; the stated quantitative bound and logarithmic schedule hold. | Companion Theorem B; closed-strip theta cusp and endpoint Fourier decay. | No sign of the entire companion is inferred. |
| SW2-B3 | On each fixed energy compact along a cofinal sequence, normalized A and B differ from F by `O_R(exp(-2a))`; at each simple target zero the displayed paired-zero limits hold. If the companion value is nonzero, the residue divided by `2pi a exp(-2a)` tends to `J_infinity/X'`. | Companion Theorem C and exact Wronskian. | The residue sign conclusion requires a simple real target zero and nonzero limiting ratio. Multiple zeros and zero companion values need separate analysis. |
| SW2-B4 | On each fixed compact energy disk along a cofinal sequence, outside fixed neighborhoods of target zeros, the rational upper-half-plane sign is eventually negative; for the actual positive coefficients negative energy is excluded at every order. | Companion Sections 7 and 8. | The excluded target-zero neighborhoods contain the unresolved nonreal-pole/sign problem. |
| SW2-B5 | Exact companion special values and negative-axis behavior rule out the two global Pick shortcuts discussed in the appendix. | Companion appendix; ODE and contour identities. | Does not rule out local sign statements with the growing-solution background retained. |
| SW2-L1 | Every zero of each actual finite Bessel transform with `(a,M)=(10,50)` or `(20,100)` in `|z|<=sqrt(2000)` is real. | [Local proof](local_gate/LOCAL_WINDOW_CERTIFICATE.md), primitive rational replay, complete complex denominator count, all residues and all boundary points. | A theorem for two specified approximants and one disk; not a zeta zero census, global real-rootedness, or a cofinal statement. |
| SW2-L2 | The local consumer rejects an interior-complex-pole model and a negative-residue model even though their whole outer semicircle has the apparent correct sign. | Exact rejection controls and their receipt. | Validates these two failure modes, not every possible implementation defect. |
| SW2-C1 | The whole-strip deterministic transfer has multiplier order `3/2-alpha` for `1<alpha<2`; its central member is unitary. It maps the specified q source to p with the stated normalization. | [Cosine Theorems 1 and 2](cosine/COSINE_PHASE_AND_NATIVE_SYNTHESIS.md). | Does not preserve products or pointwise positivity. The underlying cosine/inversion operator is classical. |
| SW2-C2 | The literal native generators have the displayed sine images including `y log(n)/n`, and the complete finite norm is exactly the displayed integral (or infinite cosine-series norm). | Cosine native synthesis identities. | Finite samples alone do not compute the entire norm. |
| SW2-C3 | The off-line-zero functional remains continuous after the transfer on bounded native vectors. For `3/2<=alpha<2`, vanishing transformed minima are equivalent to the classical native RH criterion. | Cosine dual-functional and Sobolev arguments. | The reverse density implication for positive-order `alpha<3/2` is not asserted. |
| SW2-C4 | Bounded native vectors satisfy the stated fractional Sobolev interpolation inequalities; their complete cosine frequency tail is at most `16 B^2/sqrt(Y)` for `Y>=2`. | Cosine native regularity lemma and full-tail theorem. | The budget B must be controlled for the actual residual family. |
| SW2-C5 | Mobius synthesis converges on compact frequency intervals; its initial native residual and energy lower bound are exact. An exactly zero prefix forces the stated low-index coefficients and a growing budget. | Cosine full-series identities and prefix analysis. | The existing compact and tail estimates do not prove complete-norm convergence. |

## Smallest outstanding statements that would advance the RH route

### Window route

Produce a sequence `ell_j->infinity` with a proved positive lower bound for the actual form on every `[0,ell_j]`, allowing the bound to depend on j. The finite-window-to-matrix transfer is now proved. The missing input is signed arithmetic positivity as more prime delays enter, not matrix completeness or a fixed list of prime terms. The old positive-part budget cannot supply this input in its obstructed regime.

### Bessel route

Produce `a_j->infinity`, `M_j/a_j->infinity`, and `R_j->infinity` for which the actual boundary polynomials satisfy the complete local gate, with common factors handled explicitly. On fixed compacts the only unresolved neighborhoods are those of target zeros. A proof that the limiting residue ratio is positive at all simple real target zeros would address one part of this obligation, but would not by itself exclude nonreal target zeros or resolve multiple-zero cases.

The two new finite certificates establish attainability at specified higher orders. Their fixed value `M/a=5` is not cofinal. No extrapolation of them is used.

### Native route

Construct one finite-coefficient sequence whose **entire** transformed residual norm tends to zero. A usable finite-window scheme must simultaneously control the residual budget and the complementary frequency integral. Compact Mobius synthesis alone is insufficient, as the exact native lower bound and the incompatible safe ranges demonstrate.

## No composed RH assertion

The three routes are complementary experiments. This packet does not claim that one route supplies another route's missing positivity input, that a companion sign conjecture implies RH without complex-pole control, or that the local Bessel examples prove positivity of the moving-anchor form. Each composition would require its own theorem and review.
