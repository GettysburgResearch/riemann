# Round seven: a general transfer, a forbidden derivative premise, and finite certificates

The thousand-work mission remains incomplete. This update records conditional analytic theorems, exact operator calculations, source repairs and finite validated certificates. It makes no claim to resolve RH or establish publication priority.

## What the adaptive argument now establishes in this archive

The director and independent reviewers reconstructed a fixed-function extension of the adaptive source method. For each fixed Selberg-classF, assume its zero-free-half-plane form of GRH, with its pole at1 permitted. Then

    lim_N(logN) inf_{A=Σ_(n≤N)a_n n^(-s)}
      (2π)^(-1)∫_R |1−F(1/2+it)A(1/2+it)|²/(1/4+t²)dt
       =Σ_(distinctnontrivialρ)mρ²/|ρ|².

The coefficients are arbitrary complex numbers on ordinary integers. The gamma degree, conductor, pole order and all other data stay fixed. Signed ordinates need not pair; a central zero is included once. There is no effective rate, uniformity across the Selberg class, prescribed-array assertion or extra vanishing constraint at1. See THM-ADAPTIVE-SELBERG-OPT and director_selberg_transfer_round6.md.

The upper proof combines the versioned RST048 construction with a degree-dependent fixed mesh. The lower comparator is de Roton's2006 theorem. A tested Mellin shift supplies itsL² premise at every fixed degree under the stated GRH; the unconditional degree<4 sufficient criterion is not a restriction of that lower theorem. Literature priority remains unresolved, including two inaccessible earlier general-criterion fulltexts. The source upper method and the published generalized lower bound retain their credit.

## Higher-order poles require a tail, not an invented coefficient constraint

The complementary function is

    ψ_F(t)=Res_(s=1)[F(s)t^(-s)/s]−Σ_(n≤1/t)a_n

for *every*t>0. Its residue term persists fort>1. Under GRH, a contour shift tested against compact smooth functions inlogt and critical-line subpower growth identify itsL² Mellin transform as−F(s)/s. Deleting that tail changes the approximation model. ForF=ζ² it is(2γ_E−1−logt)/t on t>1 and exactly supplies the double-pole contribution. This is the concrete compatibility check that permits arbitrary fixed pole order in the full boundary norm.

## A published derivative premise is universally impossible in its application

The source phase proof has two independently checked local issues. Proposition6.4 leaves its Hardy factor outside a parameter derivative; atF=ζ,w=1/4,ε=1/8,j=k=1 the omitted nonzero term is(16/9)Uζ(1/4)t^(-1/4), outside its statedO(t^(-1/8)) remainder. Putting the factor inside the derivative recovers its Proposition6.5.

More structurally, Proposition5.1 asserts decay andL² membership forΦ=xφ′,φ=U_F1_(0,1). Forζ, φ=sin(2πx)/(πx), soΦ=2cos(2πx)−φ is notL² and equals2 at every positive integer. The primitiveχ4 kernel gives a second elementary counterexample. The conditional Proposition4.1 remains unchallenged; its application after the false estimate fails.

The obstruction holds for every unitary Mellin phase, not merely those examples. Ifu(s) is its unit-modulus symbol, Mφ=u(s)/s and the weak derivative would have transform−u(s), which is notL². The logarithmic-coordinate weak derivative proof avoids a formal boundary integration. Thus unitary phase multiplication cannot regularize the indicator into the dilation derivative domain. See OBS-MELLIN-PHASE-DERIVATIVE-BARRIER.

A complete replacement proof uses two weighted Mellin lines and holomorphic cutoff families to construct the zero jets. It preserves exact orthogonality, the Hilbert Gram blocks, target pairings and the generalized lower constant under the originalL² premise. The source errors are exact assertions requiring repair; they are not counterexamples to the final lower theorem. Verified findings retain the pinned source hash and independent witnesses.

## The cost of relaxing that impossible derivative premise is exact

ForD=x∂_x,g=U1_(0,1] and0<ε<1, let0<z<1 solve z+z³=2ε². Then

    inf_{f∈DomD,||f−g||≤ε}||Df||²=(1−z²)²/(8z).

The unique optimizer is the spectral filteru(s)/[s(1+τ|s|²)],z=sqrt(τ/(4+τ)). In particular the sharp small-error productε inf||Df|| tends1/4. This classical Hilbert-space filtering calculation quantifies the domain obstruction; it supplies no RH inference. The centered generatorD+1/2 has a different finite curve despite the same limiting constant. See THM-PHASE-REGULARIZATION-PARETO.

## Prior negative examples now have reproducible interval witnesses

All four Conrey–Li negative shift examples were reproduced with FLINT ball arithmetic at256bits. The director rerun matched the saved output exactly. Their zero-based examples separately certify actual root existence and the negative form throughout the root box. Their reciprocal-kernel examples additionally have strictly interior witnesses, so extension across the boundary is unnecessary for the finite negative test.

For the zeta interior pointw=−282+i10^-6, a separate interval implementation with explicit Euler–Maclaurin/Stirling remainders encloses the actual kernel ratio's real part between−0.004750153564007396 and−0.004750153564007395. This is a scoped reproduction of correct prior negative results, with the original attribution preserved. It does not rule out different domains, shifts or spectral constructions. See CERT-CONREYLI-NEGATIVE-SHIFTS.

## What remains actionable

The repaired lower proof now gives fixed-finite-zero-set quantitative errors and concrete finite-cutoff certificate candidates. Those numerical candidates have their own pending director status and must not be inferred from the qualitative limit. Their exact Gram calculations exploit unitarity to subtract only a convergent small-cutoff series. Combining a verified effective lower with the source-dependent upper certificate requires explicit global upper inputs and certified finite zero/tail bounds.

Three Ye short-window corollary candidates have independent parameter checks. The oscillatory sum has fixed nonzero phaseαn^(3/5), smoothing windowK^(7/10), and a separate7/8 zero-free cutoff assumption; it is not a PNT error statement. Keep that cutoff's unverified source status. A single-window weighted-density estimate still does not supply global BGSTB tail tightness.

The third adapted continuum search has completed with exact expected counters. The second remains a separate active search until its final counters match. The newer pinned39/17 Lean target has a separate source build and actual query status; registry-reported checks do not replace that execution. The earlier main Multiplicity build and12 queries remain completed. Read live artifact records rather than promoting partial components to a headline audit.

The next team should make the source-based adaptive constants effective, independently assess the consequential recent analytic claims, and expand full primary readings across the undercovered families. Completed repairs and finite-model limits should not be proposed again as open tasks. Publication novelty, complete-paper audits and a balanced thousand-work corpus remain outstanding.
