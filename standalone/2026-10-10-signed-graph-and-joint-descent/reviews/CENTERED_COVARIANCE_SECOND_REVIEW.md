# Independent second review of the centered covariance manuscript

## Reviewed bytes and verdict

Reviewer: `/root/signed_sector`, author of the separate graph-sector manuscript, but not author of the covariance manuscript reviewed here. This is an independent mathematical and scope review, not a formal verification or a review of the reviewer's own graph theorem.

Reviewed manuscript: `CENTERED_COVARIANCE_AND_CUBE_ALIASES.md` in the sibling `moving_labels` work directory.

SHA-256: `d121c94e9eaf8142d160ece29194d186cf2b915dfc53273d351e2baeec7becde`.

**Verdict: supported within its stated scope.** I found no remaining defect in the finite alias identities, the principal-energy tail proof, the complete radial Poisson estimate, or the explicit original signed-comparison application. The finite-budget formulation of Theorem 7.1 is sufficient and its physical application has the stated coarse polynomial budget. This receipt binds only the bytes above.

The principal-energy result is a complete-residue, zero-frequency estimate. It is not a finite-height centered moment estimate. The rapid-decay result applies only to the specified complete smooth radial row kernel and the actual reconstructed A2 phases. Neither result closes the adverse-height oscillating remainder.

## Source and normalization audit

I checked the explicit physical application against PR #914, commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`, `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`: the coefficient formula (3.2), child scales (4.3), exterior factor (4.4), inverse identity (4.6), original first-Poisson formula (6.3), and the strict selector described in Section 6.3. These are exact native arithmetic interfaces, not a claimed quantitative theta reflection theorem.

For an allocation \(bf=r_1r_2\), the product of allocated scales is \(L/(Nb\,Nf)\). Dividing a raw column by the square root of this product changes the inverse factor to

\[
\frac{\mu(C)\lambda(C)^3a_\xi(e)\chi_e(f)^4}
{Nc\,Nd\,(Ne)^{3/2}}.
\]

The remaining child factor is its own normalized full A2 polynomial. Multiplying both normalized columns back into the original prefactor \(H_{\rm orig}\mu(f)Nb/L^2\) gives exactly \(H_{\rm orig}\mu(f)/(L\,Nf)\). Thus manuscript (7.5b,c) retains the correct normalization.

Both allocations and both correction triples are independent. The auxiliary ideals are \(ef\) and \(e'f\); the child exclusion has its genuine overlap with the auxiliary at \(e\) or \(e'\). The exterior row phase reconstructs \(N=c^3d^3e^4n_1n_2\), so the strict selector is \(N\ne N'\), not inequality of factor pairs. The exact product-dependent smooth kernel is constant during the coefficient inverse and can be carried through it.

## Principal tail: counterexample search and proof audit

The potential issue is that subtracting equality of physical products does not remove every principal correlation of cube-completed columns. The manuscript handles that issue explicitly rather than assuming it away.

At fixed physical cube product \(d=hb\), all inverse-divisor dependence is in \(\mu(h)\). The constraints include \((a,rd)=1\) and \((an d,qfS)=1\), but not \((n,d)=1\). The long-tail coefficient is therefore exactly

\[
c_R(d)=\sum_{h\mid d,\ Nh>R}\mu(h).
\]

It is zero for \(Nd\le R\) and is divisor-bounded uniformly in the physical support. Combining all \(an=m\) factorizations before using coefficient norms is essential and is done in the proof.

The unique decomposition \(d=sj^2\), with squarefree \(s\), does not require \((s,j)=1\). The phase identity is

\[
\chi_{md^3}(k)=\chi_{ms^3}(k)\mathbf1_{(k,j)=1}.
\]

The squarefree pair \((m,s)\), including its possible overlap, is uniquely determined by the reduced column \(ms^3\), whose local exponents are \(0,1,3,4\). These reduced columns are orthogonal for the principal norm. Multiplication by the fixed \(j\)-mask is a contraction.

For fixed \(j,s\), coefficient counting gives the mass \(D^{\epsilon_0}(Nj)^{-4}(Ns)^{-2}\). Summation over \(Ns>R/(Nj)^2\), followed by Minkowski over \(j\), gives

\[
\|L_R\|_{\rm pr}
\ll D^{\epsilon_0}\left(
R^{-1/2}\sum_{Nj\le\sqrt R}(Nj)^{-1}
+\sum_{Nj>\sqrt R}(Nj)^{-2}\right).
\]

This is \(D^\epsilon R^{-1/2}\) on the polynomial physical support. Beyond that support the tail is identically zero. Nonempty scales below one have a fixed support-dependent positive lower bound, so no unaccounted additive counting term occurs.

The physical product map \((m,d)\mapsto md^3\) is injective because the exponent of squarefree \(m\) is recovered modulo three. Its diagonal mass has the independent direct bound \(D^\epsilon\sum_{Nd>R}(Nd)^{-2}\). The two-column principal and physical-diagonal bounds then follow by the appropriate positive-norm Cauchy–Schwarz inequalities. Subtraction bounds their strict difference. Fixed product shifts preserve the required injection.

I did not find a counterexample to this \(R^{-1}\) principal-energy claim under the actual literal-tail hypotheses. The manuscript correctly does not promote it to an \(H/R\) estimate for the entire finite-height energy.

## Complete row kernel and cutoff quantifiers

The local principal correlation is \(\delta_6(n,n')\rho(\operatorname{rad}(nn'))\), with the nonunit masks retained even at positive exponents divisible by six. The conductor/mask decomposition in (2.1)–(2.2) is correct.

For the complete smooth radial row sum, inclusion–exclusion over the principal mask leaves a primitive character sum. The normalized dual scale is \(T=(X/Nd)/Nf\). Primitive Gauss Poisson and two-dimensional lattice counting give the stated uniform bound both for \(T\le1\) and for \(T\ge1\). Radiality removes ideal-generator rotations. The principal-character case has the displayed density main term and uniformly controlled lattice discrepancy. Removing the zero row contributes only for \(n=n'=1\), which is absent from the strict product off-diagonal.

Before unrestricted theta cubes, full and inversely projected A2 products have local exponents only in \(\{0,1,3,4\}\). Distinct such products cannot have equal exponents modulo six at every prime. The principal term thus vanishes on the actual strict reconstructed support. The radical identity gives exactly

\[
\frac{X_{N,N'}}{N\operatorname{rad}(NN')}
=\frac{(Nf)^2\Delta(N)\Delta(N')G(N,N')}{H_{\rm orig}}.
\]

The precise weighted budget (7.5a), not finiteness alone, permits summation of the rapid-decay errors. For each fixed positive margin \(\delta\), prescribed \(J\), and fixed budget exponent \(C_0\), a sufficiently large Fourier decay order proves the conclusion. The stated fixed-profile or bounded-Schwartz-seminorm convention is sufficient for this choice.

The physical budget is deliberately coarse but valid: twelve independent ideal indices cost \(D^{12B_0}\), the two allocations cost a subpower, the two coefficients cost \(D^{2B_0}\), the exterior coefficient costs \(D^{2B_0}\), and the conductor square root costs \(D^{B_0}\). The convention must cover \(L\), its needed reciprocal, and \(H_{\rm orig}\); the manuscript explicitly permits enlarging the fixed scale ceiling once for these forced products. The resulting \(O(D^{17B_0+\epsilon})\) is sufficient.

## Boundary found during review and now explicitly excluded

Arbitrary residue-character multipliers allowed for the principal-norm contraction cannot be inherited by Theorem 7.1. For distinct primes \(N=p\), \(N'=q\), multiplying the respective columns by \(\overline{\chi_p(k)}\) and \(\overline{\chi_q(k)}\) creates a principal mask at \(pq\) from a strict pair. Its complete smooth row sum has a main term. The reviewed manuscript now states this exact counterexample and requires the actual reconstructed A2 row phases in the cutoff theorem.

Similarly, a cutoff on outer correction labels is a portion of the lifted signed expression. It is generally not invariant under all subdivisions of one reconstructed product. The exact \(\Lambda\) selector is invariant. The manuscript now distinguishes those statements. Its joint correction cutoff is not claimed to improve or dominate the earlier single-column tail cutoff everywhere.

The local lcm Möbius identity is correct, but its cutoff is signed. The examples show that it is neither the rectangular cutoff nor a positive improvement over it. The arbitrary-vector centered witness in Section 8 rules out deleting the \(U\) term solely by subtracting the product diagonal; it is appropriately not asserted to be the actual reflected Gauss coefficient vector.

## Exact diagnostic rerun

I independently reran the author's diagnostic with an expected-manuscript-hash gate, writing its output only into my own work directory. It passed the stated 784 residue, 4,096 alias, 2,304 masked inverse, 160 cube-zero, 1,792 lcm, and 256 A2/radical cases.

| Artifact | SHA-256 |
| --- | --- |
| `check_principal_aliases.py` | `38f659316d8445e85e11a8e2150dd2e778d1cee8263c4ac64d1fc3f757e1554f` |
| `principal_aliases_second_review.json` | `9c70640d8a8e15cc05394a212388b15c396e162e17e6003489c1bedc85cce744` |

These finite exact checks corroborate the listed arithmetic identities only. The written arguments, not this diagnostic, support the infinite principal-energy and Poisson-decay estimates. No completed moving-twist theorem, finite-height centered moment, new zero-free boundary, or RH statement has been verified by the computation or proved by this manuscript.
