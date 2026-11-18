# Independent skeptic reconstruction: finite-graph complexity barrier

Date: 2026-11-17. Status: **independently checked with no issue found in the stated first-order, fixed-boundary model**. The proposer draft was not read before this reconstruction. Source material inspected: Endres–Steiner arXiv:0912.3183v5, §9 Proposition 9.1 and equations (82)–(85); §15 Theorem 15.5 and definition (135); §16 Example 16.2 and equation (150). This is a scoped technical inspection, not a full-paper audit.

## Exact model and proposition

Let E≥1, let l_j>0 be finite edge lengths, let L=sum_j l_j, and let S be a fixed E×E unitary matrix independent of the spectral parameter k. On the direct sum of E finite intervals consider the self-adjoint first-order momentum operator −i d/dy with boundary condition f(0)=S f(l), where the endpoint vectors collect the E edges. Its eigenvalues k∈R are characterized by

U(k)=S diag(exp(i k l_j)), det(I−U(k))=0.

Multiplicity is dim ker(I−U(k)). Define N(t)=number of eigenvalues in (0,t], counting multiplicity. Then there is a bounded function F(t)∈[0,E) such that, for every t≥0,

N(t)=Lt/(2π)+F(0)−F(t).

Consequently |N(t)−Lt/(2π)|<E. More strongly, for every K>0,

|N(4K)−3N(2K)+2N(K)|<3E.

The latter improvement over the immediate 6E estimate uses cancellation of the *same* F(0); it does not bound the three remainders independently.

## Independent proof

The matrix path U(k) is analytic and unitary. Its logarithmic derivative is

−i U(k)* U'(k)=diag(l_j)>0.

At a simple eigenphase exp(iθ(k)) with normalized eigenvector v, differentiating the eigenvalue equation gives θ'(k)=v*diag(l_j)v∈[min_j l_j,max_j l_j]. At a multiple eigenvalue, the first-order phase derivatives are eigenvalues of the compression of diag(l_j) to the eigenspace, so they remain strictly positive. Thus all crossings of eigenvalue 1 are forward crossings, including their full multiplicity. Eigenphases have continuous real lifts, which can be chosen piecewise analytically through collisions. The sum of their increments from 0 to t is Lt, by the determinant identity det U(t)=det S exp(iLt).

Choose each lifted initial phase θ_j(0) in [0,2π). Write each lifted endpoint as θ_j(t)=2π m_j(t)+φ_j(t), with 0≤φ_j(t)<2π. Because all crossings are forward, sum_j m_j(t) counts precisely the crossings in (0,t]. A zero eigenvalue at the starting endpoint is excluded; an eigenvalue at t is included, because its lifted phase is then exactly an integer multiple of 2π and is assigned remainder zero. Let F(t)=sum_j φ_j(t)/(2π). Summing the phase-increment identity gives the claimed exact counting formula.

Applying the three-scale combination cancels both Lt/(2π) and F(0):

N(4K)−3N(2K)+2N(K)=3F(2K)−F(4K)−2F(K).

Since all three F-values lie in [0,E), the right side is strictly between −3E and 3E. Branch relabeling at collisions does not change the sum F(t), so no common global ordering assumption enters this cancellation.

## Comparison with a Riemann–von Mangoldt target

Suppose a target zero-counting function has

Z(t)=[t/(2π)]log[t/(2π)]−t/(2π)+O(log t).

Endres–Steiner equation (32), manuscript p.8, records this asymptotic. For the classical Riemann zeta function this is the usual count of nontrivial zeros with positive ordinates up to t, including multiplicities; choosing conventional endpoint values affects only the stated error. It follows by direct expansion that

Z(4K)−3Z(2K)+2Z(K)=K log 2/π+O(log K).

Now allow a different graph at every scale K, with E=E_K, lengths and S also depending on K. The theorem still applies provided the graph and its boundary matrix remain fixed while evaluating its counts at K,2K,4K. If

max_{t∈{K,2K,4K}} |N_K(t)−Z(t)|=o(K),

then

E_K ≥ [log 2/(3π)+o(1)] K.

Indeed the counting discrepancies contribute at most six times that maximum to the three-scale difference. Thus sublinearly many first-order edges cannot achieve sublinear counting error simultaneously at these three proportional heights, even if the total edge length and the boundary matrix are retuned for each K.

This does not prohibit a graph with E_K proportional to K, an infinite or noncompact graph, an operator with potentials or another principal symbol, an energy-dependent boundary/scattering model, or approximation on a much narrower moving window. It also does not establish a spectral construction of xi or prove anything about the location of actual zeta zeros.

## Skeptical issues resolved

1. **Endpoints:** the half-open interval (0,t] and phase remainder convention [0,2π) are essential to the exact formula. Replacing them without adjustment can change counts by up to E. The 3E bound is established for the explicit convention above.
2. **Multiplicity:** the compressed derivative is positive definite, so all branches at a degenerate root cross forward and are counted with their eigenspace dimension.
3. **Length uniformity:** the discrepancy bound is independent of min l_j and max l_j. These parameters enter the local crossing proof, but disappear from the remainder bound. No uniform lower bound on lengths is needed across the K-dependent family; every individual graph must have strictly positive lengths.
4. **Boundary independence:** S may depend on the family index K, but may not change between k=K,2K,4K within a single member. A genuinely k-dependent S(k) adds −iU*U' terms and can invalidate monotonicity and the linear total phase.
5. **Narrow-window limitation:** matching a count at one height does not trigger the barrier. The argument requires simultaneous accuracy at the three stated heights.
6. **Original paper's no-go theorem:** its fixed-graph linear-versus-T log T obstruction remains intact regardless of the normalization issue below. The quantitative varying-complexity statement is a further elementary consequence of the first-order secular model; no literature novelty is asserted.

## Source normalization issue requiring adjudication

In arXiv:0912.3183v5, Theorem 15.5 (manuscript p.27) literally states a coefficient L/π for the count of *positive* first-order eigenvalues, with L=sum l_j in (135). However, equation (150) (p.29) gives, for one edge, k_n=2π(n+c)/log(b/a), n∈Z. Set a=1,b=e,c=0. The positive eigenvalues are then 2π,4π,6π,…, hence N(t)=floor(t/(2π)) and the positive-count coefficient is 1/(2π). This is also the exact consequence of Proposition 9.1.

A plausible explanation is that the L/π formula counts both positive and negative eigenvalues by their absolute value, consistent with a preceding absolute-value ordering convention in §15, whereas Theorem 15.5 says positive eigenvalues. The attempted passage from the squared operator likewise merges both signs and does not preserve a positive-only count. This is a precise internal convention conflict under the literal positive-count reading. It should be classified at this checkpoint as **unresolved counting-convention ambiguity requiring adjudication**, not as a newly established failure of the paper's substantive no-go result. Check the final published version and any errata before public characterization. The reviewer has not performed an exhaustive correction search.

Primary source: Sebastian Endres and Frank Steiner, *The Berry–Keating operator on L²(R>,dx) and on compact quantum graphs with general self-adjoint realizations*, arXiv:0912.3183v5 (9 May 2011), https://arxiv.org/abs/0912.3183 . Local inspected files: `sources/spectral/endresssteiner.pdf` and extracted text. The paper's secular equation and multiplicity statement are the source-supported model; the phase-flow bound and three-scale deduction above were reconstructed independently.
