# Finite rational-inner coupling: an explicit self-adjoint realization and counting cost

Campaign date:2026-11-17. The statements below are independently reconstructed auxiliary operator results. Related factorization and passive-realization literature is identified at the end. No literature novelty or theorem about locations of Riemann zeros is asserted. Parent review has checked the phase-count and full matrix-realization algebra; a separate third reconstruction is pending.

The same asymmetric bound also holds for **every finite Hermitian auxiliary boundary model** defined in §8, including nonminimal realizations with dark states. The factor class below gives an explicit construction; §8 identifies the general mechanism and counts all hidden finite-dimensional states.

## 1. Exact class and conclusion

Let E≥1 and let ℓa>0, 1≤a≤E, with total length L=Σaℓa. Let C be a constant E×E unitary matrix. For finitely many indices j, take orthogonal projections Pj on C^E and complex zj=dj+iaj with aj>0. Write rj=rankPj and M=Σjrj. Define

    bj(k)=(k−dj−iaj)/(k−dj+iaj),
    Fj(k)=I−Pj+bj(k)Pj,
    S(k)=C F1(k)···Fn(k),
    D(k)=diag(exp(ikℓa)),        W(k)=S(k)D(k).

Zero-rank factors may be omitted. We count real roots in(0,K] of det(I−W(k))=0 with multiplicity dim ker(I−W(k)). These multiplicities will equal those of one explicit compact-resolvent self-adjoint operator, constructed below.

Then the root count has the exact representation

    N(K)=LK/(2π)+G(K)+F(0)−F(K),
    0≤F(k)<E,
    G(K)=Σj (rj/π)[atan((K−dj)/aj)−atan(−dj/aj)].

G(0)=0, G is nondecreasing, and0≤G(K)≤M for K≥0. With

    ΔN(K)=N(4K)−3N(2K)+2N(K)

one consequently has the stronger asymmetric estimate

    −3E−2M < ΔN(K) < 3E+M,

and hence |ΔN(K)|<3E+2M. No bound on the pole locations, resonance widths or lengths is needed beyond the stated finite parameters and positive lengths/widths.

This is a **finite rational-inner** class. Unitarity on the real axis alone does not imply these hypotheses, and a general energy-dependent unitary function is not silently declared inner or physically realizable. Mixed-half-plane all-pass factors, real-axis singularities, infinite products and additional uncounted internal states require separate treatment.

## 2. Positive phase velocity, including noncommuting factors

For real k, each Fj and W are unitary. The scalar phase derivative is

    −i conjugate(bj(k)) bj′(k)=2aj/((k−dj)²+aj²)=:qj(k)>0.

Let Vj(k)=F(j+1)(k)···Fn(k), the empty product being I. Product differentiation gives

    QS(k):=−iS(k)*S′(k)=Σj Vj(k)* qj(k)Pj Vj(k) ≥0.

This is a sum of unitary conjugates of positive semidefinite matrices. It does not require that the Pj commute. Consequently

    QW(k):=−iW(k)*W′(k)
          =diag(ℓa)+D(k)* QS(k)D(k) >0.

In particular QW≥min(ℓa)I. Taking traces removes all conjugations:

    Tr QW=L+Σj rj qj(k).

Equivalently detS=(detC)∏j bj^rj. Its continuously unwrapped phase change from0 to K is2πG(K). Every factor contributes total phase2πrj on the full real line; its phase increase on any positive interval is at most that amount. All zj lie in the upper half-plane, so there is no cancellation of determinant zeros against lower-half-plane poles. This is the crucial restriction absent from a general para-unitary factorization.

## 3. Endpoint-correct root counting

For a unitary matrix W(k), let F(k) be the sum of its eigenvalue arguments in[0,2π), divided by2π. Eigenvalue1 is assigned argument0. Thus F(k)∈[0,E). Away from roots this is smooth locally and

    F′(k)=Tr QW(k)/(2π).

At a root k0, put P=projection onto ker(I−W(k0)). The compressed infinitesimal phase matrix is P QW(k0)P, positive definite on that eigenspace. Thus all crossing eigenphases increase through1. For example the Schur complement of I−W(k) near k0 has leading block

    −i(k−k0) P QW(k0)P + O((k−k0)²),

while its complementary block is invertible. Therefore the zero is isolated, its determinant zero order is dimker(I−W(k0)), and F has a downward jump of exactly that dimension. Assigning argument0 makes F right-continuous at that crossing.

Integrate TrQW/(2π) from0 to K and subtract these jumps. The result is the displayed exact count. A root at K is included, and a root at0 is excluded: F(0) is already the right-hand value at0. This is why the initial fractional phase cannot simply be dropped.

Analyticity of the finite rational/exponential matrix path and the positive crossing block exclude accumulating or tangential roots on a bounded real interval. No independent choice of globally ordered eigenphase branches is required.

## 4. The improved one-sided cost

Put x=G(2K)−G(K) and y=G(4K)−G(2K). Then x,y≥0 and x+y≤M. Thus

    G(4K)−3G(2K)+2G(K)=y−2x ∈[−2M,M].

The fractional-phase contribution is

    −F(4K)+3F(2K)−2F(K) ∈(−3E,3E).

The linear LK/(2π) term and the constant F(0) cancel. This proves the asymmetric estimate. The coefficients−2 and1 for the G contribution can be approached by concentrating narrow resonances in(K,2K) or(2K,4K), respectively. This does not assert that the combined bound is jointly sharp for every fixed E,M or every realization.

The positive-curvature target matters. The Riemann–von Mangoldt count of nontrivial zeta-zero ordinates, with multiplicities, has

    ΔNζ(K)=K log2/π+O(logK).

If one member of this model class matches those three counts with errors of absolute value≤εK K at K,2K,4K, then

    3E+M ≥ K log2/π−6εK K−O(logK).

For a family indexed by K with εK→0 this forces

    liminf (3E_K+M_K)/K ≥ log2/π.

The coefficient of auxiliary rational-inner degree in this **positive-target** consequence is1, rather than2 from the absolute estimate. The same model parameters must be fixed at all three heights in each comparison. Lengths, poles and dimensions may vary with the external family index K. This is a model-counting obstruction, not RH or an approximation theorem for zeta.

## 5. Explicit full matrix self-adjoint realization

Choose isometries Vj:C^rj→C^E with Pj=VjVj*. Put

    Gj=sqrt(2aj)Vj,       G=[G1 ... Gn]:C^M→C^E.

On C^M=⊕j C^rj define the Hermitian block matrix Ω by

    Ωjj=dj I,
    Ωjt=(i/2)Gj*Gt      for j>t,
    Ωjt=−(i/2)Gj*Gt     for j<t.

Hermiticity follows by conjugate transposition of the off-diagonal blocks. The ambient Hilbert space is

    H=(⊕a L²(0,ℓa)) ⊕ C^M.

For f with each fa∈H¹(0,ℓa), write

    ξ=f(starts),     η=f(ends),     ω=C*ξ,
    μ=(η+ω)/2,       δ=η−ω.

Define

    D(H)={(f,q): f∈⊕H¹, q∈C^M, δ=Gq},
    H(f,q)=(-if′, Ωq+iG*μ).

This is a fixed linear operator/domain, not a domain chosen separately at each energy.

### Density, closedness and self-adjointness

The domain is dense: compactly supported smooth functions approximate arbitrary edge data, while arbitrarily thin H¹ boundary layers produce the required finite endpoint jump Gq with arbitrarily small L² norm, for every prescribed q. Endpoint averages μ are free, as is q.

Use the inner product linear in the second argument. Integration by parts for u=(f,q), v=(g,p) yields the boundary form

    <u,Hv>−<Hu,v>
      =−i(ηf*ηg−ωf*ωg)
         +i q*G*μg+i μf*Gp.

Since δf=Gq, δg=Gp and η*η−ω*ω=μ*δ+δ*μ, the terms cancel.

To check maximality rather than symmetry alone, let(g,p) belong to the adjoint domain. Compactly supported test functions force g∈⊕H¹ and the first adjoint component−ig′. Denote the unknown auxiliary component by r. Testing arbitrary endpoint averages μf and arbitrary q gives

    i μf*(Gp−δg)+q*(r−Ωp−iG*μg)=0.

Hence δg=Gp and r=Ωp+iG*μg. These are exactly the original domain and action, so H*=H. This argument does not require G to be injective or surjective.

The graph norm is equivalent to the H¹ edge norm plus the finite-dimensional q norm. One direction uses the first output−if′; the other follows from the trace estimate and bounded finite matrices. Rellich compactness on finitely many bounded intervals, plus finite-dimensional compactness for q, makes the graph-domain embedding compact. Thus H has compact resolvent.

### Elimination that remains valid at every real resonance center

At real eigenvalue k the equations are

    f_a(x)=ξ_a exp(ikx),       η=D(k)ξ,
    δ=Gq,                     (k−Ω)q=iG*μ.

Using μ=η−Gq/2 gives

    T(k)q=iG*η,     T(k)=kI−Ω+(i/2)G*G.

By the chosen Ω, T(k) is block upper triangular:

    Tjj(k)=(k−dj+iaj)I,
    Tjt(k)=iGj*Gt  for j<t,
    Tjt(k)=0       for j>t.

Every diagonal block is invertible for every real k because aj>0. Thus no division by k−dj is needed, and no real resonance center is lost.

Set x_n=η and x_j=η−Σt>j Gtqt, so x_0=ω. The j-th row of Tq=iG*η gives

    qj=i (k−dj+iaj)⁻¹ Gj*x_j,
    x_(j−1)=x_j−Gj qj
            =[I−Pj+bj(k)Pj]x_j=Fj(k)x_j.

Therefore

    ω=F1(k)···Fn(k)η,
    ξ=Cω=S(k)D(k)ξ.

Conversely every ξ∈ker(I−W(k)) determines exactly one q through invertible T(k) and one edge eigenfunction. Hence full operator eigenspaces are in bijection with these kernels, with equal multiplicity. No purely auxiliary eigenstate is missing: ξ=0 implies f=0 and T(k)q=0, hence q=0. In this particular cascade realization, there are **no dark real states**, even when M>E and kerG is nontrivial.

This completes an actual self-adjoint compact-resolvent realization for the entire prescribed finite factor class, not merely for its scalar example. It does not prove that an arbitrary unitary matrix function belongs to this class.

## 6. Scalar model: centers, zero, poles and dark-state failure control

For E=M=1, C=1, G=γ∈R\{0}, Ω=d and edge length ℓ, the construction reads

    H(f,z)=(-if′, dz+iγ(f(ℓ)+f(0))/2),
    f(ℓ)−f(0)=γz.

It is precisely the proposed scalar operator, with a=γ²/2. Without dividing by k−d, the eigenvalue equation becomes

    [(k−d)−ia] exp(ikℓ)−[(k−d)+ia]=0,

equivalently b(k)exp(ikℓ)=1 for every real k. In particular:

- k=d is an eigenvalue exactly when exp(idℓ)=−1; then z=−2f(0)/γ. Resonance elimination must retain it.
- k=0 is never an eigenvalue for γ≠0: the undivided expression is−2ia≠0. Equivalently a constant edge function forces z=0 and then f=0.
- The rational scattering pole d−ia is nonreal and is not an operator eigenvalue. The entire undivided secular expression is nonzero at that pole. Its corresponding zero d+ia is not a physical eigenvalue either.
- No nonzero eigenvector can have f=0 because the trace jump would force z=0.
- If γ=0 is allowed, the operator becomes periodic derivative⊕[d]. The reduced scattering factor is1, while the decoupled auxiliary eigenvalue d survives. It is then a dark state omitted by the reduced secular equation. Thus γ≠0/minimality is substantive, not a cosmetic assumption.

### Why the earlier common-dense-S theorem cannot erase the auxiliary state

Compare this coupled scalar H with the periodic derivative⊕[d] on the full enlarged space. The latter has f(ℓ)−f(0)=0, while the coupled domain has f(ℓ)−f(0)=γz. Their common domain therefore imposes z=0. Its closure in L²⊕C is contained in L²⊕{0}, so it is **not dense**. A common symmetric restriction contained in both domains cannot be dense either.

It is invalid to invoke the preceding finite-deficiency theorem for densely defined common symmetric operators to charge this coupling only to the edge boundary count. The M auxiliary coordinates remain visible. A symmetric-linear-relation theorem would require its own hypotheses and bookkeeping. The direct rational-inner count and explicit realization above avoid this mistake.

## 7. Primary literature provenance and limits

Two actual primary PDFs were read selectively:

1. Alpay–Jorgensen–Lewkowicz, arXiv:1410.0283v2, *Characterizations of rectangular (para)-unitary rational functions*. Theorem3.1, pp10–11, gives a Blaschke–Potapov representation by rank-one factors and constant (co)isometries; its discussion explicitly allows mixed pole locations. The remarks after the proof warn that arbitrary factor products can have degree cancellation. Theorem2.1, pp5–6, gives a minimal state-space lossless realization in its Schur-stable convention. These establish prior factorization/realization context; the whole19-page preprint was not audited.
2. Tabak–Mabuchi, arXiv:1510.08942v2, *Trapped Modes in Linear Quantum Stochastic Networks with Delays*. Section5, equations15–20, pp6–7, treats half-plane inner Potapov factors and the separate singular/delay factor. Section9, equations39–43, p18, gives a passive oscillator realization of a rank-one factor and a cascade interpretation. The source's Laplace coordinate is related to ours by s=−ik; for λ=−a−id its factor(s+conjugateλ)/(s−λ) equals(k−d−ia)/(k−d+ia). The passive input-output realization is prior context; the full closed Hilbert-space operator proof above is separately supplied. The whole26-page paper, numerical simulations and all factorization prerequisites were not audited.

These sources make prior-work claims about rational-inner and passive cascades; this campaign does not claim to originate them. The exact cost inequality and explicit realization are recorded as independently reconstructed consequences, with novelty unassessed. No original Potapov1950s full-text audit was completed.

Reproduce the finite exact algebra checks with `python experiments/code/factored_inner_round2.py`. They compare noncommuting factor products with the full cascade realization at rational real energies, including resonance centers; verify Hermiticity, triangular elimination and positivity; and preserve the scalar dark-state control. Those checks supplement, rather than prove, the all-energy operator argument.

## 8. General theorem: arbitrary finite Hermitian auxiliary boundary dynamics

The factor construction is sufficient but unnecessary. Let Ω be **any** M×M Hermitian matrix, let G:C^M→C^E be **any** linear map, keep ℓa>0 and constant unitary C, and define exactly the same full operator

    η=f(ends),  ω=C*f(starts),  μ=(η+ω)/2,
    D(H)={η−ω=Gq},
    H(f,q)=(-if′, Ωq+iG*μ).

The density, adjoint-domain calculation and compact graph embedding in §5 use only Ω*=Ω and finite dimensions. Therefore this is self-adjoint with compact resolvent for arbitrary Ω,G, including G=0 and rank-deficient G. The total number M of auxiliary coordinates will remain in the bound.

### Dark-state decomposition, without a minimality assumption

Define

    Hd=⊕λ∈specΩ [ker(Ω−λI)∩kerG],
    Hv=Hdperp,     Md=dimHd,    Mv=dimHv.

Hd is the largest Ω-invariant subspace contained in kerG. Since Ω is Hermitian, it is reducing; G annihilates Hd. In this decomposition the full closed operator splits orthogonally as

    H = H_visible ⊕ Ω_dark.

The first summand is the same boundary model with Ωv,Gv on Hv. The second is a finite Hermitian matrix with no edge component. This is not a heuristic removal of modes: it is an exact reducing decomposition. In particular, even when a dark eigenvalue coincides with a visible eigenvalue, their multiplicities **add**.

Put Av=Ωv−(i/2)Gv*Gv. If Av q=λq, then

    Imλ · ||q||²=−||Gv q||²/2 ≤0.

If equality holds, Gv q=0 and Ωv q=λq, which would put q in Hd∩Hv={0}. Hence every eigenvalue of Av is strictly in the lower half-plane. This argument does not require diagonalizability. For every real k,

    R(k)=(kI−Ωv+(i/2)Gv*Gv)⁻¹

is therefore defined.

### The actual transfer function is rational inner

Set

    S0(k)=I−iGv R(k)Gv*,    S(k)=C S0(k).

For real k, the resolvent identity gives

    R*−R=iR*Gv*Gv R.

It follows directly that S0*S0=I and

    −iS0*S0′=Gv R*R Gv* ≥0.

More generally, for z in the upper half-plane the same calculation gives

    I−S0(z)*S0(z)=2 Imz · Gv R(z)*R(z)Gv* ≥0.

Thus S0 is genuinely analytic/contractive in the upper half-plane and unitary on the real boundary. The conclusion is proved from this specific realization, not inferred from boundary unitarity alone.

The matrix determinant identity gives

    detS0(k)=det(kI−Ωv−iGv*Gv/2)
              /det(kI−Ωv+iGv*Gv/2)
            =det(kI−Av*)/det(kI−Av).

All denominator eigenvalues λj=dj−iaj lie strictly below the axis, and all numerator eigenvalues are their conjugates above it. They are counted with algebraic multiplicity. There is no upper/lower cancellation, so the continuous determinant phase increases by **2πMv over the whole real line**. Its increase on[0,K] divided by2π, call it Gv_phase(K), is nonnegative, nondecreasing and at most Mv. Jordan blocks change neither the determinant identity nor this phase budget.

If one wrote the transfer function using the unreduced Ω,G, factors from Ω_dark would give apparent real poles in the inverse matrix. They disappear from G R G* exactly because of the reducing decomposition. Transfer values at these real points are defined by the visible formula above; simply evaluating an unreduced singular inverse is invalid.

### Exact full spectral count, including coincident dark eigenvalues

On the visible subspace the eigenvalue-elimination argument in §5 remains valid for every real k because R(k) exists. Hence visible eigenmultiplicity is dimker(I−S(k)D(k)). Positive edge lengths and the positive transfer derivative again imply that all these crossings are positive.

Define

    Nd(K)=N_Ωdark((0,K]),
    A(K)=Gv_phase(K)+Nd(K).

Then the exact full count is

    N_H((0,K])=LK/(2π)+A(K)+F(0)−F(K),
    0≤F(k)<E,       0≤A(K)≤Mv+Md=M.

A is nondecreasing, though it may jump at dark eigenvalues. A dark eigenvalue at0 is excluded by(0,K], while the initial right-continuous F(0) excludes visible zero modes correctly. A simultaneous visible and dark eigenvalue at K is counted with the sum of its two multiplicities. For example, with E=1, ℓ=π, C=1, Ω=diag(1,1) and G=[1,0], k=1 is a visible resonance eigenvalue and also a dark eigenvalue. The full eigenspace has dimension2, whereas the reduced scalar secular equation has a simple root. This explicitly tests the missing multiplicity.

The proof of §4 now applies to A, giving for **all** such finite Ω,G models

    −3E−2M < ΔN_H(K) < 3E+M,
    |ΔN_H(K)|<3E+2M.

The positive-zeta-curvature consequence 3E_K+M_K≥K log2/π−6εK K−O(logK) remains valid. No minimality assumption is needed, because all dark states have been charged.

Finally, if G≠0, comparison with the uncoupled reference graph(C boundary)⊕Ω again has a nondense common domain: its intersection imposes Gq=0. Therefore the earlier densely-defined-common-S theorem cannot be used to discard the auxiliary cost.

### Provenance and remaining review

Under the Laplace change s=−ik, the transfer becomes

    I−Gv(sI+Gv*Gv/2+iΩv)⁻¹Gv*,

which is exactly the passive finite-state pattern A=−Gv*Gv/2−iΩv, B=−Gv*, C_out=Gv, D_out=I in Tabak–Mabuchi §9 equation41. That source supplies prior passive input-output context; the closed boundary self-adjointness, dark-state accounting and counting-cost arguments are given explicitly here. The parent independently checked the general transfer identities and decomposition strategy. A separate third reconstruction remains pending. No claim of new realization theory is made.
