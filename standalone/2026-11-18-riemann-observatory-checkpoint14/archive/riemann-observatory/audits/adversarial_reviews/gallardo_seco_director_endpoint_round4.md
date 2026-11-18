# Director adjudication: the inclusive endpoint in Proposition5.1

Later scope update: the endpoint finding below remains separate from the subsequently verified Theorem5.5 reverse-implication counterexample at(-3,7/4). See weighted_criterion_director_round5.md for that new witness and the complete corrected parameter threshold. Statements below that the endpoint alone does not refute the later theorem remain limited to this earlier argument.

2026-11-17. Source: PAPER-E012, inspected arXiv2206.02654v6 and the actual2025 publisher PDF, DOI10.1007/s11785-025-01661-2. The director inspected the published page21 image and the coefficient-norm definition on page3. Three agents independently reconstructed the relevant operator calculation; two independently checked the exact primary hypotheses before comparing proofs.

## Verdict and exact scope

**Verified mathematical error in the inclusive endpoint of the printed auxiliary Proposition5.1.** The statement admits alpha=-3,a=1, but T1:D_-1→D_-3 is not onto and is not bounded below. This is not a claim that the paper's earlier main zero-free theorems are false. The finding is specific to the identified versioned operator assertion. Publication novelty/priority is unassessed.

The source imposes alpha in[-3,-2), a>0, and the ordinary full Hilbert spaces

D_beta={f(z)=Sum_(n>=0)c_nz^n : Sum|c_n|²(n+1)^beta<infinity},

T_a f=[((1−z)^a f)prime]/(1−z)^a=fprime−a f/(1−z).

It states bounded bijectivity iff a>=−(1+alpha)/2. No quotient, initial-coefficient constraint or weaker inverse topology is specified. At alpha=-3,a=1 all printed hypotheses hold.

## First independent witness: normalized polynomials

Let f_K(z)=Sum_(n=0..K)z^n. Then

||f_K||²_D_-1=H_(K+1)→infinity,

T1 f_K=−(K+1)z^K/(1−z),

||T1f_K||²_D_-3=(K+1)² Sum_(j=K+1..infinity)j^(-3)
<=1/(K+1)+1/2<=3/2.

The finite coefficient identity is exact. The infinite upper bound follows from the decreasing-sum integral test; the harmonic divergence is elementary. Thus the unit vectors f_K/sqrt(H_(K+1)) have images tending to zero. A bounded bijection between these Hilbert spaces must have a bounded inverse, so the printed bounded-bijection claim cannot hold. This witness does not rely on numerical truncation of an infinite norm.

## Second independent witness: an explicit vector outside the range

Put g(z)=Sum_(n>=0)b_nz^n with b_n=(n+1)/log(n+2). This is holomorphic in the disc and

||g||²_D_-3=Sum_(n>=0)1/[(n+1)log²(n+2)]<infinity.

For any analytic solution f=Sum c_nz^n of T1f=g, set S_n=Sum_(k=0..n)c_k and u_n=S_n/(n+1). Coefficient comparison gives

u_(n+1)−u_n=b_n/[(n+1)(n+2)]=1/[(n+2)log(n+2)],

c_n=u_n+b_(n−1)/(n+1), n>=1.

Consequently Re(u_n) tends to infinity for every initial complex constant c0, and Re(c_n) does too. Therefore Sum|c_n|²/(n+1) diverges, and no preimage belongs to D_-1. This directly disproves surjectivity, independently of the bounded-inverse theorem. The symbolu in these equations is one sequence; a line beginning 'u_' is not the Greek letter nu.

## Repair independently reconstructed

The two independent Hardy-repair notes and the advocate's separate coefficient proof agree. For every alpha<-1,a>0, set delta=a+(alpha+1)/2. The correct classification is:

- delta>0: T_a is a bounded bijection with bounded inverse;
- delta<0: T_a is bounded and onto, with one-dimensional kernel;
- delta=0: T_a is bounded and injective, with proper dense nonclosed range.

Exact recurrence: H_n=(a+1)_n/n!, c_n^(hom)=(a)_n/n!, u_n=S_n/H_n. Then

u_(n+1)−u_n=g_n/[(n+1)H_(n+1)],

f_n=c_n^(hom)u_n+g_(n−1)/(n+a).

For positive delta use a future-tail solution; for negative delta use a past-prefix solution. After conjugating the weighted coefficient spaces, their kernels are bounded by constant multiples of n^(delta−1/2)j^(−delta−1/2) in the respective triangular half-plane. Schur's test with weightsn^(-1/2) proves the required bounded maps. Fixed gamma-ratio comparability constants cover every finite initial index. At zero delta, truncated homogeneous solutions have logarithmically divergent domain norm and bounded image norm; polynomials remain in the range, proving density without closedness.

The source-range bijection condition must therefore be strict. This is an independently reconstructed standard weighted-Hardy mechanism, with no novelty claim.

## Dependency and version limitations

Theorem5.5's publisher page26 permits alpha in[-3,-2] and a in[1,(1−alpha)/2); only(alpha,a)=(-3,1) hits this critical T_a endpoint. Its stated forward sufficient approximation implication survives the operator objection. A reverse closure equivalence or an argument using multiplication by(1−z)^(a−1) needs its own topology/core justification. These are separate proof-dependency questions; no falsity of Theorem5.5 is established here. The earlier Theorems2.1/3.1 do not depend on Proposition5.1 in the inspected argument.

The source owner checked the actual arXiv version list, Crossref relations and publisher Crossmark record through execution date. The retrieved Crossmark content says the document is current and lists no correction; no relevant correction was located in the checked official/search records. This is not a claim that no mathematician previously noticed the endpoint or that every possible erratum source was searched.

Evidence: audits/gallardo_seco_endpoint_round3.md; audits/adversarial_reviews/gallardo_seco_endpoint_skeptic_round4.md; gallardo_seco_hardy_repair_skeptic_round4.md; gallardo_seco_hardy_repair_equivalences_round3.md; gallardo_seco_operator_impact_advocate_round4.md. Exact supplementary finite checks: weighted_dirichlet_endpoint_round3.py/results. Copyrighted primary PDF/images remain private; the archive provides canonical URLs, version hashes, original analysis and the explicit witnesses.
