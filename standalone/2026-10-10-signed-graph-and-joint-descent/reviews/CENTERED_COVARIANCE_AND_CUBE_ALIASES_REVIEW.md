# Independent review of the centered covariance and cube-alias manuscript

**Reviewer:** descent_synthesis. **Disposition:** accepted within the exact source-qualified scope below; no material gap found in the reviewed proof. This is a review of the frozen bytes, not a certification of the imported theta foundations or the original Riemann moment target.

**Target:** `CENTERED_COVARIANCE_AND_CUBE_ALIASES.md`, SHA-256 **`d121c94e9eaf8142d160ece29194d186cf2b915dfc53273d351e2baeec7becde`**.

I read the complete manuscript, checked the principal/remainder and long-inverse proofs independently, and compared the expanded original A2 application against its pinned source identities. The new bounds are about complete smooth radial row sums and complete-residue principal energy, respectively. They are not estimates for arbitrary selected pieces of a finite-height signed row sum.

## 1. Principal kernel and complete smooth Poisson

The exact common period is the radical of both physical products. At a present prime, even an exponent divisible by six retains the nonunit zero. Thus the complete-residue average is exactly

\[
\Pi(n,n')=\mathbf1_{v_p(n)\equiv v_p(n')\ (6)\ \forall p}
\prod_{p\mid nn'}(1-(Np)^{-1}).
\]

In Section 3, inclusion–exclusion uses only the principal mask \(q_0\), disjoint from the primitive residual conductor \(f\). After substituting \(k=dh\), the primitive Poisson scale is
\(T=X/(Nd\,Nf)\). I checked the normalization
\(\sqrt{Nf}\,T\sum_{h\ne0}(1+\sqrt T|h|)^{-B}\).
For \(T\le1\), planar counting gives a uniform bound after multiplying by \(T\); for \(T\ge1\), choosing \(B>2A+2\) gives the claimed arbitrary decay. Since \(Nd\le Nq_0\), the uniform denominator is \(N\operatorname{rad}(nn')\).

For \(f=1\), the unweighted lattice main terms sum to the exact density factor. The full-lattice discrepancy is bounded at subunit scales and rapidly decreasing at large scales; summing over divisors preserves the displayed error. The only omitted-row correction is \(\Psi(0)\) when both physical products are the unit ideal. In particular it vanishes on the strict product off-diagonal.

Radiality is necessary for the rotation-free inclusion–exclusion formula as written and is explicitly part of the theorem. The leading constant is explicitly the lattice density times the planar integral. No undocumented Fourier-normalization constant is used in the later physical scale calculation.

## 2. Cube aliases, exact inversion and principal long-tail energy

For squarefree \(m,m'\), reduction modulo three of the prime valuations in \(md^3\) and \(m'(d')^3\) forces \(m=m'\). The remaining congruence modulo six is parity equality of the valuations of \(d,d'\). This proves the stated alias classification, including primes shared by \(m\) and \(d\). The density involves every prime in both physical products, not just the common squarefree cube part.

The grouped physical cube summand is independent of the inverse divisor \(h\mid d\), with the masks \((a,rd)=1\) and \((and,qfS)=1\) retained. Hence the complete divisor sum annihilates every \(d\ne1\) before any norm or coupled kernel. The same statement holds in both independent columns. The lcm cutoff identity is also exact: at a prime present on both sides, the three nonempty assignments have total coefficient \(-1\), so each selected squarefree lcm has coefficient \(\mu_K(\ell)\). No positivity is inferred from that signed identity.

For the analytic tail theorem I independently reproduced the calculation with \(d=sj^2\). The reduced column \(ms^3\) has prime exponents in \(\{0,1,3,4\}\), which uniquely determine the pair \((m,s)\). Those columns are orthogonal for the complete-residue principal norm. The remaining fixed \(j\)-mask is a contraction in that norm, including its zeros.

The squared coefficient mass at fixed \(j\) is bounded by

\[
D^\epsilon(Nj)^{-4}
\min\{1,(Nj)^2/R\}.
\]

Its square roots sum to
\(D^\epsilon R^{-1/2}\log(2D)\): below \(\sqrt R\) the sum is harmonic, and above it the ideal tail has exponent two. This proves the stated principal energy \(D^\epsilon/R\). Empty supports and nonempty subunit scales are handled correctly; when \(R\) exceeds physical support the tail is zero.

The genuine product diagonal is checked separately. The map \((m,d)\mapsto md^3\) is injective because \(m\) is squarefree, and its squared coefficient mass is bounded by the ideal tail \(\sum_{Nd>R}(Nd)^{-2}\). This justifies the diagonal estimate without incorrectly inferring it from a potentially cancellation-sensitive principal energy. Cauchy–Schwarz gives the two-column bound for both forms. The statement with fixed bounded residue multipliers is valid at principal norm level; the proof does not promote that permission to Section 7's rapid-decay theorem.

## 3. The exact physical A2 application

The A2 product exponents \(\{0,1,3,4\}\) have distinct residues modulo six. Outer inverse correction primes are excluded from their full children. Consequently a strict reconstructed product pair remains nonprincipal after the finite A2 expansion.

The radical calculation is exact:

\[
\frac{X_{N,N'}}{N\operatorname{rad}(NN')}
=\frac{(Nf)^2\Delta(N)\Delta(N')
N\gcd(\operatorname{rad}N,\operatorname{rad}N')}{H_{\rm orig}}.
\]

For \(N=ab c^3d^3e^4\) with disjoint squarefree labels,
\(\Delta(N)=(Ncde)^2Ne\). Additional child corrections multiply the defect by a factor at least one, so the sufficient outer-label cutoff follows.

I checked the added literal application, equations (7.5b)–(7.5c), against PR #914. The residual test satisfies
\(R_L(bfm)=\sum_{r_1r_2=bf}\sum_{an=m}V_*(Na/A_\alpha,Nn/B_\alpha)\).
The normalized inverse A2 factor is exactly
\((Nc\,Nd\,(Ne)^{3/2})^{-1}\); its child contributes the further normalizer
\((A_{\alpha,t}B_{\alpha,t})^{-1/2}\). The exterior row phase belongs to the reconstructed product \(s_tn_1n_2\), while every remaining displayed coefficient is row-independent.

Multiplying the two normalized columns back contributes
\(A_\alpha B_\alpha=L/(Nb\,Nf)\). This converts the original source prefactor
\(H_{\rm orig}\mu_K(f)Nb/L^2\) exactly to
\(H_{\rm orig}\mu_K(f)/(L\,Nf)\). Both \(bf\)-allocations, the original sign, both generally different auxiliaries \(ef,e'f\), their overlap with the child exclusions, and the original coupled radial scale are present.

The finite coefficient budget is sufficient. There are twelve freely counted ideal indices, two divisor-bounded allocations, two coefficient factors each bounded by \(D^{B_0}\), an exterior factor bounded by \(D^{2B_0}\), and residual square-root conductor bounded by \(D^{B_0}\). These give \(D^{17B_0+\epsilon}\). The explicit budget hypothesis (7.5a) and the choice of Fourier decay order make every prescribed rapid-decay conclusion uniform. The manuscript correctly distinguishes an invariant selector on reconstructed products from a selector on artificial correction subdivisions.

## 4. Source checks and finite reproduction

The directly checked source interfaces were:

| Commit | File | SHA-256 |
| --- | --- | --- |
| `0cc0428fedbbfc340044c7451b3d392c1da9a103` | `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md` | `d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad` |
| same | `standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md` | `c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983` |
| `cfa102748b26f840ccc4b963a660711424db0ec3` | `standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md` | `203df24a48e54cb088a28c1236c78569ae75ea84a6b589f72a30b35720cc8e4c` |
| `725b2d25ab47e57500049d93985560098c7ef3fa` | `standalone/2026-10-10-sextic-moving-labels/MIXED_LABEL_COMPLETION.md` | `5e77ec88d6a191ec214bcedebc2b42d37f95735ba2bb18955b2f8a16aedfbcad` |
| `086bf0560c0c2679a1fe41418f583d2c5ca743c3` | `standalone/2026-10-10-mobius-overlaps-and-sampled-moments/JOINT_REFLECTED_BLOCKS.md` | `c75be63f43de6efb0d9f820da008f256afc53351fdbfe38870f9e97207955bd5` |

The last source explicitly allows coefficient vectors and subsets of its squarefree row range. Thus the unit-row witness in Section 8 is legitimate for the stated arbitrary-vector obstruction; it is not a theorem about the complete physical radial covariance or its literal Gauss vector.

I independently ran `check_principal_aliases.py` with the expected manuscript hash, directing its output to my own review directory. It passed all **9,392** listed finite checks. The script SHA-256 was **`38f659316d8445e85e11a8e2150dd2e778d1cee8263c4ac64d1fc3f757e1554f`**; the independent report SHA-256 is **`9c70640d8a8e15cc05394a212388b15c396e162e17e6003489c1bedc85cce744`**.

That reproduction checks finite character, zero-mask, divisor and rational identities only. The analytic conclusions above were reviewed from their proofs. This receipt does not assert an estimate for the oscillating finite-height remainder, deletion of the \(U+(EU)^{2/3}\) terms, a physical fourth moment, a new zero-free boundary, or RH.
