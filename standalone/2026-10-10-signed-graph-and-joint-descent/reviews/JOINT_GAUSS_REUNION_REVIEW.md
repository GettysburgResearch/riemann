# Independent scoped review of the joint Gauss reunion continuation

**Verdict:** PASS at the stated source-conditional scope. I found no mathematical gap in the new two-factor continuation, its exact adapter to the reunited three-cusp series, or its comparison with the same physical completed family. This review does not independently establish the imported theta or sieve foundations.

**Frozen target:** *JOINT_GAUSS_REUNION_CONTINUATION.md* in the sibling *descent_synthesis* directory.

**Target SHA-256:** **31e2395999301d56ce63751db7c907fc6147b689574aaf268133d706ad3aa0aa**.

**Reviewer:** moving_labels. The reviewer authored parts of the PR #924 input packet. The present review independently checks the new composition and deductions in this target; it is not a claim that its previously imported analytic foundations were independently reconstructed again.

**Review method:** read the complete target at the stated hash; derive its cutoff exponents, dyadic convergence inequalities, exact two-factor coefficient identity, cusp summability and physical-envelope comparisons; compare the load-bearing identities with the pinned source files below. No numerical fit or finite local diagnostic is used to validate the analytic continuation.

## 1. Exact sources checked

1. PR #924, commit **725b2d25ab47e57500049d93985560098c7ef3fa**, *standalone/2026-10-10-sextic-moving-labels/ANISOTROPIC_A2_NORM_TRANSFER.md*, especially Theorem 2.1 and its proof for every positive inverse cutoff.
2. At the same pin, *MIXED_LABEL_COMPLETION.md*, Theorem 2.1 and its explicit bounded outer-multiplier extension for the counting exponent. Its exact physical cube identity and the companion sixth-power-stratified row proof supply the source operators used in the envelope comparison.
3. PR #922, commit **f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32**, *standalone/2026-10-10-signed-covariance-descent/SECOND_REFLECTION_BOOTSTRAP.md*, Sections 1–3: the variables, the relation \(K_py_p=x_p\), the complete cube sum, and the conditioned Gauss coefficient.
4. At the same pin, *FULL_CUSP_DESCENT.md*, Sections 1–2: the actual reunited function, its complete bad/ramified decomposition, the cube law, the exact coefficient identity (2.5), and the uniform coefficient bound (2.6) on bounded real strips.
5. At the same pin, *FINITE_RAY_REUNION.md*, equation (4.3) and the surrounding finite coefficients: the exact gamma normalization and the entire norm-power dependence of the finite coefficients on \(s\).

The October 5 OpenAI/math theta source remains an imported dependency as named in the target. The review does not claim to verify its automorphy theorem, all individual cusp formulas, or the underlying classical large sieve from first principles.

## 2. The raw family and the cutoff estimate

The target's two factors really carry different fixed finite ray multipliers. Its adapter is exact:
\[
a_\xi(ab)\omega(b)=a_{\xi\omega}(ab)\overline{\omega(a)}
\]
on the good support. The character \(\omega\) has its conductor in the fixed bad set, so its surviving values are units. The counting completed theorem explicitly permits this bounded row-independent outer multiplier. The corresponding cube inverse must use the inner ray \(\xi\omega\); the target says this explicitly.

For the other orientation, take \(b\) as outer variable and use ray \(\xi\), leaving \(\omega(b)\) as its outer multiplier. These two completions need not coincide. Their exact finite inverses recover the same raw polynomial, which is all that is required to choose the shorter physical axis. Thus the orientation change does not assume an unsupported symmetry of a single theta completion.

With the counting exponent \(\beta=1\), PR #924 gives precisely the target's six-term bound
\[
HA+FH^2AB^{-1/2}R^{3/2}
+F^{2/3}H^{4/3}A^{4/3}B^{-2/3}R^2
+H+ABR^{-3}+(HAB)^{2/3}R^{-2}.
\]
The source proves it for every \(R>0\), including the empty short part when the cutoff is below one and the physical upper cap when the long part is empty. Those cases are needed for the target's cutoff and are not extrapolated from an \(R\ge1\) theorem.

I independently substituted
\[
R=B^{1/3}A^{-1/15}H^{-8/21}F^{-2/9}.
\]
All powers of \(B\) cancel. The nontrivial short terms become
\[
H^{10/7}F^{2/3}A^{9/10},
\qquad
H^{4/7}F^{2/9}A^{6/5};
\]
the two long tails become
\[
H^{8/7}F^{2/3}A^{6/5},
\qquad
H^{10/7}F^{4/9}A^{4/5}.
\]
For \(H,F,A\ge1\), these and the retained \(HA,H\) terms are bounded by \(H^{10/7}F^{2/3}A^{6/5}\). The bounded nonempty scales below one are covered by the source's fixed-support convention. This proves the target's shorter-axis bound with its actual leading \(HA\) term included.

The polynomial reference-scale loss can be written as \((2HFAB)^\epsilon\) by beginning with a smaller source loss. Fixed compact real strips give polynomial vertical seminorm growth after insertion of the Mellin weights. No parameter-dependent smoothness constant is discarded.

## 3. The two-variable continuation

The normalized dyadic block at \(A,B\) is multiplied by
\(A^{1/2-t}B^{1/2-u}\). Its row norm is bounded by
\[
H^{5/7+\epsilon}F^{1/3+\epsilon}
A^{1/2-\Re t}B^{1/2-\Re u}\min(A,B)^{3/5}
\]
up to the stated vertical polynomial and arbitrarily small scale losses.

On \(A\le B\), summing \(B\) first requires \(\Re u>1/2\) and leaves the \(A\)-power \(8/5-\Re(t+u)\). On \(B\le A\), the same argument requires \(\Re t>1/2\). Therefore the exact tube is
\[
\Re t>\tfrac12,\qquad
\Re u>\tfrac12,\qquad
\Re(t+u)>\tfrac85.
\]
All inequalities are strict. The preliminary losses can be chosen smaller than the margins on each closed real subregion.

Each block is a finite entire sum, and its sum converges locally normally in the finite-dimensional row Hilbert space. It agrees with the original double Dirichlet series for \(\Re t,\Re u>1\), so it continues that same coefficient family. The resulting row norm is \(O(H^{5/7+\epsilon}F^{1/3+\epsilon})\). Restricting to a row subset is legitimate here because this step uses a positive row norm, not the complete smooth character kernel from a different argument.

## 4. The exact adapter to the reunited source function

The target retains the source variables
\[
t=1-s,\qquad u=v-s,\qquad
w=u+2t-\tfrac12,
\]
and the fixed cube relation
\(\varrho^3=\overline{\rho}^{\,3}\).

The conditioned source coefficient is
\[
\frac{\widetilde a_k(d)h(d)}{(Nd)^u}
\frac{\widetilde a_k(m)\chi_m(d)^4}{(Nm)^u},
\qquad
h_p=K_p^{-1}(1-x_p).
\]
Using \(\widetilde a_k=\kappa a_k\), the Gauss CRT identity and
\(u+1-v=t\) gives exactly
\[
\frac{a_k(dm)\kappa(m)}{(Nd)^t(Nm)^u}
\prod_{p\mid d}(1-x_p).
\]
In particular the fixed factor \(\kappa\) belongs to the \(m\)-axis. Its placement is material to the adapter and is correct in the target.

Expanding the finite product and writing \(d=za\) yields
\[
a_k(zam)=a_k(z)a_k(am)\chi_{am}(z)^4
\]
on the actual pairwise-coprime squarefree support. Consequently the correction is
\[
\frac{\mu_K(z)a_k(z)\chi^-_k(z)}{(Nz)^{t+w}}
\mathcal B_{k,z}^{\varrho,\kappa}(t,u).
\]
The auxiliary is exactly \(z\), and the twist \(\chi_{am}(z)^4\) retains its zero when a column meets \(z\). No second exclusion parameter is needed. The outer factor retains the zero when \(z\) meets \(k\). Thus the displayed correction is a coefficient identity, not a substitution of a merely similar canonical family.

The reciprocal orientation \(\chi_k(am)\) is converted into \(\chi_{am}(k)\) using the same fixed primary residue partition and finite ray family as the pinned sources. The positive row theorem allows each such subset. No assertion is made that an individual artificial finite Fourier label has the continuation independently of its actual reunion.

The cube factor is in its absolute Euler half-plane because
\(\Re(3t-1/2)>1\). Further,
\[
\Re(t+w)
=\Re(t+u)+2\Re t-\tfrac12
>\tfrac{21}{10}.
\]
The auxiliary cost of the inner row norm is only \((Nz)^{1/3+\epsilon}\), so the complete \(z\)-sum converges locally normally with a strict margin. This verifies continuation and the norm estimate for the same \(\mathcal Z_k\).

## 5. Every cusp and bad label is retained

The target uses exactly the source identity
\[
\mathcal Y_k
=\sum_{\sigma,c_0,j,\varepsilon,n_0,b_0,\varrho}
B_{\sigma,c_0,j,\varepsilon,n_0,b_0,\varrho}(s,k)\mathcal Z_k(s,v;\varrho).
\]
The coefficient estimate
\[
\sup_k|B(s,k)|
\ll
3^{-j(\Re t-1/6)}(Nb_0)^{-(3\Re t-1/2)}
\]
is stated by the source on every bounded real \(s\)-strip, not only on the older \(\Re s<0\) domain. Its defining finite norm powers are entire in \(s\). It is therefore valid for this new composition.

The infinite ramified and fixed bad-prime cube sums converge when \(\Re t>1/6\), and the new tube has \(\Re t>1/2\). Minkowski with the sum of the coefficient suprema includes all cross-cusp terms. It does not rely on orthogonality or delete a nonstandard cusp.

Transforming coordinates gives exactly
\[
\mathcal J
=\{\Re s<\tfrac12,\quad
\Re(v-s)>\tfrac12,\quad
\Re(v-2s)>\tfrac35\}.
\]
The resulting complete squarefree-row energy is \(O(H^{10/7+\epsilon})\). The squarefree restriction in this conclusion comes from the source's exact reunited identity and is not removed merely because the intermediate raw polynomial admits all rows.

The source gamma factor has no numerator poles for \(\Re s<1/2\), its reciprocal denominator factors are entire, and Stirling gives a fixed-strip polynomial. Reintroducing \((Nk)^{1-2s}\) changes the squared row power to
\(H^{24/7-4\Re s+\epsilon}\), as written.

At \(v=1\), both real Gauss variables equal \(1-\Re s\). The strict summed inequality is \(\Re s<1/5\). Thus the continuation really crosses \(v=1\) for the same complete function on that larger range; no endpoint or zeta zero-free claim follows.

## 6. Same-family physical-envelope comparison

The revision reviewed here includes an explicit physical cube derivation of the classical completion bound. This resolves the main possible object mismatch in the comparison.

The exact identity is
\[
\mathcal C_{1,1}(A,B;k,1)
=\sum_b\frac{\lambda(b)^3\chi_b(k)^3}{Nb}
\mathscr P_{1,b}(A,B/(Nb)^3;k,1).
\]
The new mask excludes the outer squarefree factor from \(b\); it does not exclude the inner squarefree factor. The cube sum is unrestricted and physically finite. Fixed outer finite characters remain bounded coefficients in every child.

For the normalized raw child, grouping its squarefree product gives bounded coefficient mass. Splitting rows by their full sixth-power divisor in the sixth-power-free operator yields
\[
H+H^{1/6}L+(HL)^{2/3}.
\]
The middle term is repeated over \(O(H^{1/6})\) row factors; the other two row-factor sums converge. At \(L=AB/(Nb)^3\), Minkowski then has weights
\((Nb)^{-1},(Nb)^{-5/2},(Nb)^{-2}\).
The first is physically truncated and harmonic; the others converge. Hence the full completion, with the same fixed rays, satisfies
\[
H+H^{1/6}AB+(HAB)^{2/3}.
\]
This really is a bound for the same completed object as the counting completion estimate.

For \(A=B=D\), I checked both claimed comparisons with the hypothetical contour output \(H^{10/7}D^{6/5}\). The counting completion is dominated when \(H\le D^{49/40}\). The full-cube classical bound is dominated when \(H\ge D^{168/265}\); its mixed term needs only \(H\ge D^{7/40}\). These ranges overlap and cover \(H,D\ge1\). The larger holomorphy tube therefore does not, through that scalar route alone, improve the existing physical positive-energy envelope.

## 7. Exact acceptance boundary

The accepted new conclusions are the joint coefficient representation, its normally convergent tube, the all-cusp continuation and squarefree-row mean for the actual reunited series, the explicit \(v=1\) crossing, and the stated same-family envelope comparison.

The review does not approve a signed covariance estimate, a bound after pulling back the original strict two-column product diagonal, a fourth moment of the original Möbius polynomial, the target \(17/24\), or RH. The target expressly keeps those interfaces open.

The smallest load-bearing analytic premise is the PR #924 counting anisotropic raw estimate for the finite-character family, uniformly in the moving auxiliary and for every positive cutoff. The target derives that extension using an explicitly permitted outer multiplier and exact inverse. Failure of that imported premise would invalidate the new continuation, while the finite algebraic identity would remain meaningful on its initial absolute domain.
