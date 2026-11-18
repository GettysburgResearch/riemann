# Third independent review: finite inner realization and exact spectral counts

Reviewer: equivalences agent.2026-11-17. The reviewer received the proposed model and conclusions but did **not** read the corpus/parent draft before deriving the checks below. This is ordinary independent mathematical reconstruction, not formal proof-assistant verification. No novelty claim.

## Scope and conclusion

The proposed result is correct for **E>=1 finite intervals of strictly positive lengths**, a finite-dimensional auxiliary spaceC^M, HermitianOmega, arbitrary finite matrixG:C^M→C^E, and unitaryU onC^E, with the domain and action specified below. The energy-dependent scattering matrix is derived from that explicit self-adjoint realization; arbitrary energy-dependent unitaries are not covered.

One degenerate-case qualification: ifE=0 is allowed, the asserted strict discrepancy bounds require modification to weak finite-dimensional inequalities. The natural interval model hasE>=1, and the proof below uses that assumption. No semiboundedness of the first-order operator is assumed.

## Domain, Green identity and maximality

For f in the direct sum of H¹(0,ell_e), set eta=f(ends), alpha=f(starts), omega=U*alpha, mu=(eta+omega)/2 and delta=eta-omega. Define

D(H)={(f,q):delta=Gq},

H(f,q)=(-if',Omega q+iG*mu).

Use the inner product linear in its second argument. Integration by parts gives the field boundary form

i(eta_f*eta_g-omega_f*omega_g)
 =i(mu_f*delta_g+delta_f*mu_g).

The auxiliary boundary form is

-i(mu_f*Gq_g+q_f*G*mu_g),

which cancels exactly on delta=Gq. The sign of iG*mu is therefore consistent with the specified orientation and -i derivative.

The domain is dense. Compactly supported fields withq=0 approximate the field subspace. For any fixedq, choose fields supported in arbitrarily short endpoint neighborhoods with eta-omega=Gq and L² norm tending to0; these approximate(0,q) in the ambient Hilbert space. Graph-norm boundedness is not required for density.

For maximality, a vector in the adjoint domain has H¹ field components by testing compactly supported fields. Green's formula against domain vectors withq=0 and arbitrary common endpoint valueeta=omega=mu forces delta_g=Gq_g. Such endpoint values can be prescribed independently by H¹ interpolation on each interval. Allowing arbitraryq then fixes the adjoint auxiliary action asOmega q+iG*mu. Thus D(H*)=D(H) and H is self-adjoint.

The graph norm controls ||f'|| as well as ||f|| and||q||. Its domain embeds compactly into the ambient space by the finite-interval H¹→L² compact embedding and finite-dimensionality ofq. Hence H has compact resolvent. This argument addresses the full domain realization, not merely its scattering determinant.

## Dark subspace and real resonances

Let D_dark be the largest Omega-invariant subspace contained inkerG. SinceOmega is Hermitian, it is reducing and equals the sum over eigenvalueslambda ofker(Omega-lambda) intersectkerG. Its orthogonal complementV is alsoOmega-invariant and contains the range ofG*. The complete operator splits into the visible interval realization onV and the independent Hermitian matrixOmega restrictedtoD_dark.

OnV put Gamma=G*G and A=Omega-iGamma/2. IfAv=lambda v, then

Im(lambda)||v||²=-||Gv||²/2<=0.

If lambda were real, Gv=0 andOmega v=lambda v, puttingv inD_dark, impossible onV. Thus all visible eigenvalues ofA lie strictly in the lower half-plane. The real resolventR(k)=(k-A)^(-1) therefore exists for every realk. Merely deletingkerG, without taking its maximalOmega-invariant part, would be incorrect.

If one starts from the full auxiliary matrix, apparent real poles from dark eigenvectors are removable in G(k-A)^(-1)G*, because the whole dark block is annihilated byG. Its eigenvalues must be counted separately, not discarded. After the reduction there are no unresolved real auxiliary resonances.

## Scattering matrix from the domain equations

For a visible eigenfunction of real energyk,

(k-Omega)q=iG*mu.

Using mu=eta-Gq/2 gives q=iR(k)G*eta, and then

omega=[I-iG R(k)G*]eta, alpha=Uomega=S(k)eta,

S(k)=U[I-iG R(k)G*].

This derives the claimed matrix directly from the original boundary/auxiliary equations. Ifeta=0, the field and visibleq both vanish, so no visible eigenstates are lost by the secular equation.

For complexz in the upper half-plane letT(z)=I-iG(z-A)^(-1)G*. A direct resolvent calculation gives

T(z)*T(z)=I-2Im(z)G(z-A)^(-1)* (z-A)^(-1)G*.

Hence S is analytic and contractive there and unitary on the real axis: it is rational inner in the upper half-plane convention. The adjoint and sign conventions have been checked in this identity; changing the differential orientation would change the corresponding convention.

For realk, R'(k)=-R(k)². Since R*-R=iR*Gamma R,

-iS(k)*S'(k)=G R(k)*R(k)G*>=0.

The positivity does not requireOmega andGamma to commute orG to have full rank.

## Determinant and total phase

Sylvester's determinant identity gives

detS(k)=detU det(k-A*)/det(k-A).

The visible poles are strictly lower and the zeros strictly upper; there is no determinant cancellation between them. If eigenvalues ofA are a_j-ib_j, b_j>0, counted algebraically, the derivative of the continuous determinant phase is

sum_j 2b_j/[(k-a_j)²+b_j²].

It is positive unlessM_visible=0 and its integral over the whole real line is2pi M_visible. Non-normality and repeated complex eigenvalues do not change this determinant calculation. For k>=0 define

g_phase(k)=[arg detS(k)-arg detS(0)]/(2pi),

using a continuous lift. This is nondecreasing, starts at0 and has total increase at mostM_visible on the positive axis; it need not achieveM_visible there because the full2pi winding is over all realk.

## Exact spectral count, crossing direction and ties

LetD(k)=diag(exp(ik ell_e)). Field propagation giveseta=D(k)alpha, so visible eigenvalues are exactly the real solutions of1 in sigma(V(k)), V(k)=D(k)S(k), with multiplicitydimker(I-V(k)). The correspondence with visible H eigenvectors is bijective, including energies equal to eigenvalues ofOmega before the dissipative reduction.

Its logarithmic derivative satisfies

-iV*V'=S*diag(ell_e)S-iS*S'>=ell_min I>0.

Thus every eigenphase crossing has positive velocity. Local analytic phase lifts exist through degeneracies; at a multiple crossing their compressed phase-velocity matrix remains positive definite. Consequently a zero of the secular determinant is counted with exactly the self-adjoint eigenspace multiplicity, and no negative or tangential crossings occur.

Choose continuous unwrapped eigenphase branchesbeta_j(k) on a finite positive k-interval, continuing labels through crossings. Then

N_visible((0,K])=sum_j[floor(beta_j(K)/(2pi))-floor(beta_j(0)/(2pi))].

This formula includes upper endpoint ties and excludes initial zero modes. PutF(k)=sum_j frac(beta_j(k)/(2pi)); then0<=F(k)<E. The value at a crossing uses fractional part0, so F is right-continuous and jumps down by its crossing multiplicity. In particular F(0) is the actual right-continuous value, not a left limit. Integer changes of phase lifts or branch permutations do not changeF.

Taking traces of the logarithmic derivative, or the determinant ofV, yields

N_H((0,K])=L_total K/(2pi)+g_phase(K)+N_dark((0,K])+F(0)-F(K).

Dark and visible eigenvalues can coincide; their orthogonal eigenspaces contribute additively. Dark zero modes are excluded by the same(0,K] convention. There is no missing tie correction at0.

## Curvature statistic and dimension obstruction

Letg(k)=g_phase(k)+N_dark((0,k]). It is nondecreasing and its total positive-axis increase is at mostM=M_visible+M_dark. For

Delta=N_H((2K,4K])-2N_H((K,2K]), K>0,

the linear length term cancels, and its g contribution is

[g(4K)-g(2K)]-2[g(2K)-g(K)] in[-2M,M].

The F contribution is-F(4K)+3F(2K)-2F(K), strictly between-3E and3E. Therefore

-3E-2M<Delta<3E+M.

The asymmetry of the M terms follows from monotonicity, not from an arbitrary bound on three unrelated phase values.

If the model counts are intended to match the positive ordinates of the classical zeta zeros at K,2K,4K with errors o(K), Riemann–von Mangoldt gives

Delta_zeta=K log2/pi+o(K).

Thus necessarily3E+M>=K log2/pi-o(K). For fixed finiteE,M, exact matching at all sufficiently large heights is impossible. For a family with dimensions depending onK, the same realization must be used at the three comparison heights for the length term to cancel. This is an assumption about the proposed spectral model, not a theorem identifying its eigenvalues with zeta zeros.

## Adversarial scope checks

- E=0: the interval fractional-part strict bound is unavailable; use weak finite-dimensional inequalities instead. E>=1 and positive lengths suffice for the stated strict form.
- Zero or negativeOmega eigenvalues: permitted; only positive dark counts enterN_dark, and total increase is still at mostM_dark.
- G=0: all auxiliary directions are dark; S=U and the formula reduces correctly to graph phases plus independent finite eigenvalues.
- rankG<M: permitted; only the maximal invariant dark subspace can be split off. A visible real eigenvalue would contradict its definition.
- NoncommutingOmega,G*G and repeated complex poles: permitted; the resolvent identities and determinant proof remain valid.
- Arbitrary energy-dependentU(k), a non-HermitianOmega, nonunitaryU, negative/zero interval lengths, unbounded auxiliary dimension, or unspecified boundary extensions are outside the proof.
- The present boundary-coupled realization changes the field domain. It is not automatically the bounded off-diagonal attachment covered by the earlier3M interlacing theorem; its count estimate was separately derived here.

Verdict: independently checked with no issue found under the explicit finite positive-interval assumptions. The E=0 convention and positive-axis versus whole-line phase distinction should be retained in any final statement. No claim of historical novelty or RH resolution.

## Comparison with draft

Not read at the time this independent reconstruction was saved. A subsequent comparison, if needed, should be recorded separately.
