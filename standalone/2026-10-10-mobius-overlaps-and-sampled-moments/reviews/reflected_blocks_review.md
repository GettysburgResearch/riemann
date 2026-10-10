# Independent review: negative-allocation averaging and the physical all-row block

**Reviewer:** \(\texttt{/root/amplification}\), a nonauthor of the target note and of its all-row extension.

**Date:** 2026-10-10.

**Verdict:** PASS for the native trilinear deduction and the explicitly source-qualified physical applications at the exact target hash below. No blocking mathematical issue was found. This does not certify the imported theta or reciprocal theorems, the full reflected sum, a generalized moment, or a zero-free conclusion.

## 1. Exact target and reviewed dependencies

The complete frozen target is:

| File | SHA-256 |
| --- | --- |
| attack3_theta.md | c75be63f43de6efb0d9f820da008f256afc53351fdbfe38870f9e97207955bd5 |

I read all sections, reconstructed the three-variable estimate and the physical all-row extension independently, and checked the displayed numerical examples and scope qualifications. I also inspected the following local copies of the pinned PR #923 source interfaces:

| Source file under attack3_theta_sources | SHA-256 verified from bytes |
| --- | --- |
| 923_PRUNED_COUPLED_MEAN_SQUARE.md | 411d7b28c0dabc97807d21683d731126e742d16424b1809787c87849dfb9e8d1 |
| 923_ALL_ROW_COMPLETION_AND_RAW_GAIN.md | a0e6bd5517a81f44d2a18bd32dc4f0db623b9951c17068e56af7009c8914fdec |

The companion 923_ALL_ROW_LOCAL_AUDIT.md was read to check the stated row-prime normalization and inactive-prime interpretation. This receipt authenticates the target by its local content hash. It does not independently authenticate every upstream repository fetch or reconstruct every earlier theorem listed in the target's source table.

No author mathematical source was edited by this reviewer. This is an attributable review statement, not a cryptographic signature.

## 2. The trilinear squarefree-row theorem

### 2.1. Grouping the coprime product

When \((g,n)=1\), the product \(m=gn\) is squarefree, and its quadratic character is exactly the quadratic product column required by (QLS). Its coefficient includes the complete \(e\)-sum. Cauchy on the finite set of representations \(m=gn\) costs only a divisor factor; it does not replace the cubic \(e\)-sum by its absolute coefficient count.

After this Cauchy step, fixing \(g\) makes \(\mathbf1_{(g,e)=1}\) a permissible row-independent coefficient mask for (CLS), whose row is \(n\). The resulting coefficient energy is

\[
\sum_m|\beta_m|^2
\ll D^\epsilon GE\bigl[E+U+(EU)^{2/3}\bigr].
\]

The quadratic sieve then contributes \(H+GU\). Dividing by the squared normalizer \(G^2EU\) gives exactly (2.3). The dependence on \(g\) and \(n\) of the original separate coefficient vectors is harmless here; arbitrary coupled coefficients in all three variables would not be covered.

### 2.2. The moving row mask

The identity

\[
\mathbf1_{(k,e)=1}
=\sum_{r\mid k,\ r\mid e}\mu_K(r)
\]

is exact. Applying Cauchy to the divisor sum separately for each row \(k\) gives a sum of squared norms over \(r\), with a divisor loss absorbed in \(D^\epsilon\). This is the appropriate place to use Cauchy; a sum of norms over all such \(r\) would not give the claimed weights.

With \(k=rk'\) and \(e=re'\), the phases \(\rho_r(g)\), \(\rho_r(n)\), and \(\chi_n(r)^4\) enter separate \(g\)- and \(n\)-coefficients. All nonunit zeros survive, \((k',r)=1\) is a fixed row restriction, and the two new lengths are \(H/R\) and \(E/R\), where \(R=Nr\).

The normalizer ratio is \(R^{-1/2}\), hence the fixed-\(r\) energy is

\[
R^{-1}\frac{H/R+GU}{GU}\mathcal B(E/R,U).
\]

I independently expanded its six powers of \(R\): they are \(-3,-2,-8/3,-2,-1,-5/3\), in the order stated in (2.10). Only the \(UR^{-1}\) term has a logarithmic ideal sum, and its actual support is polynomially bounded. The moving mask therefore causes no missing power loss.

### 2.3. Every collision between \(g\) and \(n\)

For the exact squarefree gcd \(c=(g,n)\), write \(g=cg'\), \(n=cn'\). Then \(g',n'\) are coprime and both avoid \(c\). The identities

\[
\rho_k(c^2g'n')=\mathbf1_{(k,c)=1}\rho_k(g'n'),
\qquad
\chi_{cn'}(e)^4=\chi_c(e)^4\chi_{n'}(e)^4
\]

retain the essential zero mask. For fixed \(c\), the new coefficient vectors are still separate even if the original vectors were not multiplicative.

At \(Nc\asymp C\), the new \(g,n\) lengths are \(G/C,U/C\), and the normalization ratio is \(C^{-3/2}\). There are \(O(C)\) ideals in this dyad. Minkowski over these labels therefore contributes \(C^{-1}\) after squaring, which is the prefactor in (2.16). Expanding gives

\[
\frac{HEC}{GU}+\frac HG+
\frac{HE^{2/3}C^{1/3}}{GU^{1/3}}
+\frac EC+\frac U{C^2}+\frac{(EU)^{2/3}}{C^{5/3}}.
\]

Since \(C\ll\min(G,U)\), summation over dyads proves (2.2). This includes the entire collision contribution and gives exactly the stated improvement over freezing \(g\). There is no unrecorded coprimality assumption \((g,n)=1\) in the final theorem.

## 3. The squarefree physical adapter and its comparison

The completed-group order is respected: the full projected Ramanujan group is retained, the source support cutoff in \(g\) is inserted there, and only then are \(d=ef\), \(n=en'\), and \(b=fb'\) allocated. The note does not infer that an individual reflected frequency block vanishes from a statement about a completed group.

Given the imported full scalar and all-cusp coefficient formulas, the remaining varying characters and masks agree with the family in (2.1). After fixing \(f,b'\), the masks involving \(f\) are fixed column exclusions or a row restriction. The remaining moving row mask is precisely \((k,e)=1\), which Section 2 treated explicitly. The cubic CRT factor has the orientation \(\chi_{n'}(e)^4\) required by (CLS).

The coefficient normalizer

\[
\frac1{\sqrt A\sqrt F\sqrt G\sqrt U\,C}
\asymp \frac1{FC}\frac1{G\sqrt{EU}}
\]

is correct when \(A\asymp EFG\). The \(O(F)\) choices of \(f\) and the \(O(1)\) sum of \(1/Nb'\) over a cube norm dyad remove the displayed frozen-label normalization without an additional factor of \(G\). The \(g\)-average is already inside the trilinear theorem.

The note explicitly uses the source's common Mellin majorant to separate all coupled smooth norm weights before applying either sieve. This is load-bearing for the physical adapter. The restriction to the literal physical coefficient, separate norm factors, and original factorwise masks is correctly preserved; a general multiplier \(v(efg)\) is excluded.

For \(A=B=D\), \(H=D^{3-\theta}\), \(E=G=D^{1/2}\), \(F=1\), the transformed scale is \(Y=D^{13/2-2\theta}\). The choice \(U=D^2\), \(C=D^{3/2-2\theta/3}\) satisfies \(UC^3=Y\). The six exponents in (4.4) are correct and have maximum \(5/2-\theta\) for \(0\le\theta<1/2\).

The previous angular comparison requires its separate source-qualified reciprocal input and gives \(35/12-\theta\) after absorbing a fixed margin above \(11/12\). Its difference from the new exponent is \(5/12\). The new trilinear bound itself uses neither that angular reciprocal estimate nor Möbius cancellation.

The whole-allocation majorant in Section 5 retains the term \(E\) in its full rectangular range. It is absorbed by \(HE/G\) only when \(H\ge G\). The surviving \(U\) and \((EU)^{2/3}\) terms are explicitly present, so summing all long-frequency blocks is not claimed to reach a moment target.

## 4. Detailed audit of the physical all-row extension

### 4.1. The exact object and the shortening mechanism

Theorem 6.1 bounds a specified physical component. The cube norm dyad is fixed. The transformed weight is multiplied by a fixed smooth profile \(\psi(x)\) supported in a compact positive annulus of its actual ratio variable. This is stronger localization than an upper bound \(U\ll Y/C^3\): it supplies comparability of the reflected frequency length. The theorem does not bound the entire \(n'\)-sum at that cube dyad or the sum of all profiles approaching \(x=0\).

For \(k=sv^2\), the further decomposition \(s=ts'\), with \(t=(s,\operatorname{rad}v)\), is exact and allows overlap of the square part and the squarefree part. The varying squarefree row length is

\[
H'=\frac{H}{TV^2}.
\]

The imported row-prime adapter supplies active conductor \(s'r_v\), with \(R_v=Nr_v\le V\), and the physical reflected length is therefore

\[
U_v\asymp U_0\frac{R_v^2}{T^2V^4}.
\]

This use of the active conductor, instead of retaining \(U_0\) unchanged for every square part, is necessary. The target retains the possible local amplitude \(\sqrt{Q_4}\), and after fixing the cube label the remaining row-prime factors are separate \(e,n'\) coefficients with no new \(g\)-dependence. Those assertions agree with the inspected PR #923 adapter and remain source-qualified.

### 4.2. The local Euler exponents and interpolation

At a prime with \(a=v_p(v)\ge1\), the local exponent is \(j\equiv2a+\varepsilon_p\pmod6\). For \(a=1,2\), it cannot be zero, so that prime is active. The \(j=4\) case requires \(\varepsilon_p=0\), \(a\equiv2\pmod3\), and thus \(a\ge2\). Consequently \(Q_4\le J(v)=\prod_{p^2\mid v}Np\).

Substituting the two physical lengths into the interpolation factor gives the positive series

\[
\mathcal Z_\eta=
\sum_{v,t,\mathrm{active}}
Q_4 T^{2\eta-1}V^{4\eta-2}R_v^{-2\eta}.
\]

For \(0\le\eta<1/3\), dropping \(T^{2\eta-1}\) enlarges it. The valuation-one and valuation-two local weights are bounded respectively by \(q^{2\eta-2}\) and \(q^{6\eta-3}\). At valuation three the actual loss is one, and allowing inactivity gives \(q^{12\eta-6}\). Replacing this by the larger \(q^{12\eta-5}\) permits the single geometric tail used in (6.11). Every resulting prime exponent is strictly below \(-1\), with geometric decay in higher valuations.

In particular, the valuation-two \(j=4\) branch gives \(q^{-1}\) at \(\eta=1/3\). The proof is correct to retain a strict margin. The notation with exponent \(1/3\) in the theorem is justified by choosing a fixed \(\eta<1/3\) in terms of the final epsilon and using the fixed polynomial scale range; it is not an endpoint Euler-product theorem.

The first term uses \(\min(1,G/U_v)\le(G/U_v)^\eta\). The third uses

\[
\min\{1,(G/U_v)^{1/3}\}\le(G/U_v)^\eta.
\]

Together with \(\mathcal Z_\eta<\infty\) and the separate choice \(\eta=0\), these give the two minima in (6.14) and (6.16). Taking the smaller of separately valid upper bounds is legitimate. The second term sums using \(\mathcal Z_0\). No square-part row multiplicity has been omitted: the sum is over the actual ideals \(v\), while \(H'\) has already supplied \(T^{-1}V^{-2}\).

### 4.3. The row-independent terms

The positive Euler product

\[
\sum_v J(v)(Nv)^{-\rho}<\infty,\qquad \rho>1,
\]

has local terms \(q^{-\rho}\) at valuation one and \(q^{1-a\rho}\) for \(a\ge2\). This gives, with a fixed small margin, the Rankin bound \(\sum_{Nv\ll\sqrt H}J(v)\ll D^\epsilon\sqrt H\), explaining the retained term \(E\sqrt H\).

The inequality \(U_v\ll U_0/V^2\) gives convergent square-part sums for the remaining terms, with exponents \(2\) and \(4/3\). Hence their costs are \(D^\epsilon U_0\) and \(D^\epsilon(EU_0)^{2/3}\), without a spurious factor \(\sqrt H\).

Different \(v,t\) describe disjoint original row sets, so their estimates are summed as energies. The active-set branches for a fixed row do require a norm inequality; their divisor costs can be absorbed with fixed positive convergence margins or in \(D^\epsilon\), as the note states.

### 4.4. Bad-prime towers, general rows, and the example

The dual bad and ramified labels replace \(U_0\) by \(U_0/[3^m(Nb_S)^3]\), with norm weights \(3^{-m/3}/Nb_S\). In the most demanding negative-frequency term, taking square roots before Minkowski costs \([3^m(Nb_S)^3]^{1/6}\). The remaining weight is

\[
3^{-m/6}(Nb_S)^{-1/2},
\]

which is summable over the fixed-prime towers. Both branches of each minimum can be summed separately and their minimum then taken. No unjustified interchange of a minimum and a norm sum is needed.

For a bad row factor \(z\), the source physical identity first transfers \(k=uzk_0\) into one of finitely many supplementary twists at good row height \(H/Nz\). Substituting this height also changes \(U_0\) by \((Nz)^{-2}\). The negative-frequency branch then carries \((Nz)^{-1/3}\); the other branches carry strictly positive decay powers as well. All fixed-prime row sums converge. Empty or bounded subunit support ranges are explicitly accounted for by the fixed support convention.

In the example, the six all-row powers are \(5/2-\theta\), \(5/2-\theta\), \(7/3-\theta\), \(2-\theta/2\), \(2\), and \(5/3\). Their maximum is \(5/2-\theta\) for \(0\le\theta<1/2\). Thus (6.24) follows within the stated fixed ratio component, including row square factors and sixth-power copies.

## 5. Dependencies, finite computation, and limits of this verdict

The native theorem in Section 2 assumes the displayed classical (QLS) and (CLS), with the stated squarefree, good-primary, and finite-ray conventions. This review reconstructs their use; it does not reprove the external sieve theorems.

The physical applications retain the imported all-cusp scalar and coefficient orientation, completed-group support theorem, uniform smooth transformed-weight bounds, row-prime amplitudes and active conductor, and the fixed bad-row twist identity. I checked their compatibility against the identified PR #923 interfaces. Their deeper automorphy and reflection sources were not independently rebuilt here. The comparison involving infinity type \(-3\) additionally retains its stated conductor-uniform angular reciprocal premise. The finite-ray reunion assertions in Section 7 remain identified upstream inputs; their displayed cancellation identity itself is algebraically correct.

No computation was used to infer the convergence of an infinite Euler product or the validity of a large sieve. This receipt concerns the full analytic note and manual exact algebra. It does not claim to replay a subsequently supplied companion checker; any such execution must have its own source and result hashes.

The all-row result cannot be read as an arbitrary-coefficient extension at a fixed reflected length. It uses both the literal source adapter and the shortening of that length with the square part. It also cannot be summed over all cube dyads, all small positive ratio profiles, or all allocations while retaining the example's exponent. The term \(U+(EU)^{2/3}\) in the long, small-cube blocks and the additional moving-conductor moment interface remain unproved targets.

The note states these limits explicitly. Its source-qualified component gain is therefore reviewable without asserting a full fourth moment, a cofinal generalized moment hierarchy, or a new zero-free half-plane.

**Signed:** \(\texttt{/root/amplification}\), independent nonauthor reviewer, 2026-10-10.
