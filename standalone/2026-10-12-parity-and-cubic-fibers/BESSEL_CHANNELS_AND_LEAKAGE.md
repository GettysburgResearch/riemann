# Exact Bessel channels, constrained compression, and the covariance interface

**Status:** proposed finite harmonic-analysis theorems and exact obstruction identities, with a separately labeled comparison to the available analytic estimates. All proofs in Sections 2–7 are supplied below. No generalized sextic moment or new zero-free half-plane is claimed.

**Scope:** the Eisenstein field; every good prime ideal, every squarefree product of good primes, and the actual sixth-order residue characters with literal zeros. The native fourth-moment and fully singleton fixed-order character classes are distinguished from their theta completions. Fixed bad-prime and ray factors, changing conductors, and physical weights are not silently identified with the normalized finite model.

**Smallest remaining gap:** construct and estimate the actual weighted covariance between a native singleton column and its quadratic leakage channel, with the source Gauss ratios, conductor-dependent dilations, finite-ray reunion, cube inverse, and moving coprimality masks all retained. The local zero compression proved here is not that covariance estimate.

**Computation:** the companion finite diagnostic checks the stated channel permutations, tensor leakage, exact residue characters at four Eisenstein prime ideals above 7 and 13 and the inert prime above 5, and the unit-row mismatch. It is diagnostic support for the written proofs, not a finite verification of the analytic moment conjecture. Its exact execution record is separate.

## 1. Sources and the structural diagnosis

The following mathematical sources were retrieved at the indicated immutable commits. Their complete relevant proof files were read, and the retrieved UTF-8 bytes were checked against the Git blobs returned by GitHub.

| Source | Immutable commit | File and SHA-256 |
|---|---|---|
| PR #927 | f9939c957f5aac6b2099b591e4988991700a152b | [SIGNED_AUXILIARY_REUNION.md](https://github.com/GettysburgResearch/riemann/blob/f9939c957f5aac6b2099b591e4988991700a152b/standalone/2026-10-10-sextic-signed-reunion/SIGNED_AUXILIARY_REUNION.md), 6b8277e64adb1121704fbf7dc4553aeda31b598c65e0279d80316a35d66d38bf |
| PR #927 | same | [SMALL_W_CORE_AUDIT.md](https://github.com/GettysburgResearch/riemann/blob/f9939c957f5aac6b2099b591e4988991700a152b/standalone/2026-10-10-sextic-signed-reunion/SMALL_W_CORE_AUDIT.md), c0d07ccc7ed2fc1490a631c73db47044df256b7ca6f946ecacd5c735e457f9d9 |
| PR #928 | ab98878279cd5614fe79bb94aa916e97c9ee50b4 | [CENTERED_COVARIANCE_AND_CUBE_ALIASES.md](https://github.com/GettysburgResearch/riemann/blob/ab98878279cd5614fe79bb94aa916e97c9ee50b4/standalone/2026-10-10-signed-graph-and-joint-descent/CENTERED_COVARIANCE_AND_CUBE_ALIASES.md), d121c94e9eaf8142d160ece29194d186cf2b915dfc53273d351e2baeec7becde |
| PR #928 | same | [PRINCIPAL_SHORT_LONG_COVARIANCE.md](https://github.com/GettysburgResearch/riemann/blob/ab98878279cd5614fe79bb94aa916e97c9ee50b4/standalone/2026-10-10-signed-graph-and-joint-descent/PRINCIPAL_SHORT_LONG_COVARIANCE.md), 7de2f4fbf8b085bc37cc83d0767748eee1c8478a590b3551935870b616f9166e |
| PR #928 | same | [JOINT_GAUSS_REUNION_CONTINUATION.md](https://github.com/GettysburgResearch/riemann/blob/ab98878279cd5614fe79bb94aa916e97c9ee50b4/standalone/2026-10-10-signed-graph-and-joint-descent/JOINT_GAUSS_REUNION_CONTINUATION.md), 31e2395999301d56ce63751db7c907fc6147b689574aaf268133d706ad3aa0aa |
| PR #929 | 97bf40329489992e9384c34d7595af6d01a40774 | [JOINT_CONTINUATION.md](https://github.com/GettysburgResearch/riemann/blob/97bf40329489992e9384c34d7595af6d01a40774/standalone/2026-10-10-conductor-averages/JOINT_CONTINUATION.md), 67643be282fbc27e8f0b42d30032d185218b4e70fb96baa14566df49aacf012a |

The underlying theta normalization is the imported October 5 source, OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, file preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex. Its canonical bytes are 169005 bytes, SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d, Git blob 2000faddbbebac5de0ecfe0b962534ea61a852d5. The relevant interfaces are eq:theta-local-factors, eq:theta-weight, eq:ray-local-transform, and the displayed exact scalar following eq:theta-mellin-functional-equation. These interfaces, not the source's zero-free assertions, are used below.

The diagnosis is specific. PR #927 completely reunites the auxiliary Möbius divisor and returns exactly to the original native centered energy. Its SMALL_W_CORE_AUDIT, equation (1.5), gives

\[
 \mathcal O_\xi[v]
 =\frac1L\sum_\eta c_\eta\sum_{s\ne0}\Phi(Ns/H)
 \bigl(|B_{\xi\eta,v}(s)|^2-\Delta_v(s)\bigr),                 \tag{1.1}
\]
where
\[
 B_{\nu,v}(s)=\sum_{n\ {\rm sf}}\mu(n)\overline{\nu(n)}
                  \chi_n(s)v(n),\qquad
 \Delta_v(s)=\sum_{n\ {\rm sf}}|v(n)|^2\mathbf1_{(n,s)=1}.
\]
All moving exclusions remain in \(v\). The coefficients \(c_\eta\) are the Fourier coefficients of the actual fixed finite-ray function; neither their positivity nor positivity of \(\Phi\) is assumed.

Thus a second use of the same reunion is a return map, not an additional estimate. PR #928 cancels the artificial complete-residue principal correlations of cube completion, while retaining a genuinely oscillating remainder. PR #929 preserves more of the two-axis continuation but explicitly finds that its final scalar envelope is dominated in the adverse range. The next issue is therefore the action on the constrained native coefficients before any absolute-value estimate. The finite analysis below resolves that action exactly.

## 2. The normalized good-prime transform

Let \(\mathfrak p\nmid6\) be a prime ideal of \(K=\mathbb Q(\sqrt{-3})\), let \(q=N\mathfrak p\), and identify its residue field with \(\mathbb F_q\). Then \(q\equiv1\pmod6\). Fix the actual sextic residue character \(\chi\), extended by zero at zero, and a nontrivial additive character \(e\). Set

\[
 (F_-f)(h)=q^{-1/2}\sum_{x\in\mathbb F_q}f(x)e(-hx),
 \qquad F_+=F_-^{-1}.
\]
All finite Hilbert norms use counting measure. Put
\[
 (Rg)(v)=
 \begin{cases}
 \chi(v)^2g(v^{-1}),&v\ne0,\\
 0,&v=0,
 \end{cases}
 \qquad T=F_+RF_-.                                      \tag{2.1}
\]
This defines \(T\) on the whole \(q\)-dimensional space, including zero residues. Its kernel is
\[
 (Tf)(y)=\frac1q\sum_{x\in\mathbb F_q}f(x)
          \sum_{v\ne0}\chi(v)^2e(yv-x/v).                 \tag{2.2}
\]

### Theorem 2.1. Exact primitive involution and spectrum

Let \(P_0\) be orthogonal projection onto constant functions. Then

\[
 T^*=T,\qquad T^2=I-P_0.                                 \tag{2.3}
\]
In particular \(T\) is a unitary involution on the mean-zero subspace. Its full spectrum is

| Eigenvalue | Multiplicity |
|---|---:|
| \(+1\) | \((q+1)/2\) |
| \(-1\) | \((q-3)/2\) |
| \(0\) | \(1\) |

**Proof.** Additive orthogonality makes \(F_-\) unitary. On nonzero residues, inversion is a permutation and \(\chi(v)^2\chi(v^{-1})^2=1\). The weight on the reverse edge is the complex conjugate of the forward weight. Hence \(R^*=R\) and \(R^2\) is projection onto functions supported away from zero. The orthogonal complement is the line spanned by the point mass at zero, whose Fourier image is the constant line. This proves (2.3).

The trace of \(R\) comes only from the fixed points of inversion, namely \(1\) and \(-1\). Both weights are one because \(\chi(-1)^2=1\). Thus the trace is two. The nonzero eigenspace has dimension \(q-1\), and its eigenvalues are \(+1,-1\), giving the displayed multiplicities. Unitary conjugation transfers the spectrum to \(T\). \(\square\)

### Lemma 2.2. Every character channel, including the two exceptional cases

Define
\[
 \gamma_j=q^{-1/2}\sum_{x\ne0}\chi(x)^j e(x)\quad(j\not\equiv0\pmod6),
 \qquad \delta=\chi(-1)\in\{1,-1\},
\]
and
\[
 u=\mathbf1_{\mathbb F_q^\times},
 \qquad r(y)=q^{-1/2}(q\mathbf1_{y=0}-1).
\]
For \(j\ne0,4\), with indices read modulo six,
\[
 T\chi^j=\delta^j\gamma_j\gamma_{j+2}\chi^{-j-2}.            \tag{2.4}
\]
The exceptional formulas are
\[
 T\chi^4=\gamma_4r,\qquad
 Tu=-q^{-1/2}\gamma_2\chi^4,\qquad
 Tr=\gamma_2\chi^4,\qquad T1=0.                            \tag{2.5}
\]
All nontrivial \(\gamma_j\) have modulus one, and
\[
 \gamma_j\gamma_{-j}=\chi(-1)^j.
\]

**Proof.** Finite additive orthogonality gives the usual Gauss identities directly: a nonprincipal multiplicative character has sum zero, and the squared modulus of its Gauss sum is \(q\). Changing \(x\) to \(-x\) and conjugating gives the product identity. For \(h\ne0\),
\[
 F_-\chi^j(h)=\delta^j\gamma_j\chi(h)^{-j}.
\]
Apply \(R\), which changes this to \(\delta^j\gamma_j\chi^{j+2}\), and then \(F_+\). If \(j+2\ne0\), this gives (2.4). If \(j=4\), the last function is the unit indicator; its Fourier transform is \(r\). Also \(F_-u=r\), \(F_-r=u\); after dropping the zero coordinate and applying the cubic weight these give the remaining formulas. All identities hold at zero as written. \(\square\)

In particular \(\chi^4\) transforms to a Ramanujan function with value \((q-1)/\sqrt q\) at zero. Replacing that value by zero would change the transform and invalidate its involution. Likewise the present exponent-zero character is \(u\), not the everywhere-one function.

### Exact adapter to the source local formula

For a fixed active set in the source, put
\[
 c=c_0\prod_{\mathfrak p\ {\rm active}}p,\qquad
 \sigma_p=\lambda^2c/p,\qquad
 \epsilon_p=-\bigl(\lambda^5(c/p)^2\bigr)^{-1}\pmod p.
\]
The source gives the good-prime operator
\[
 \mathcal T_{p,\sigma_p,\epsilon_p}
       =\chi_p(\sigma_p)^{-2}D_{\epsilon_p}T_p,\qquad
 (D_\epsilon f)(x)=f(\epsilon x).                         \tag{2.6}
\]
Equations (2.4)–(2.5) then reproduce every active case in eq:ray-local-transform, including
\[
 \omega_{p,j}
 =\chi_p(-1)^j\gamma_j(p)\gamma_{j+2}(p)
                    \chi_p(\epsilon_p)^{-j-2}
\]
for \(j\ne0,4\), \(\omega_{p,4}=\gamma_4(p)\), and
\(\omega_{p,0}=-\gamma_2(p)\chi_p(\epsilon_p)^{-2}\).

The complete scalar retained by the source is
\[
 -\frac{i}{81}\overline{\alpha(c)}^{\,2}
 \widehat\phi(h_0)\overline{\kappa_0}
 \prod_{p\ {\rm inactive}}(1-(Np)^{-1})
 \prod_{p\ {\rm active}}\chi_p(\sigma_p)^{-2}\omega_{p,j_p}.
                                                               \tag{2.7}
\]
An inactive \(j=0\) prime belongs to a different conductor branch and contributes its density \(1-q_p^{-1}\). It is not removed by declaring \(T1=0\). We make no claim that the complete sum of ramified and inactive branches has already been identified with a single unitary finite operator.

The unit factors and \(D_\epsilon\) in (2.6) preserve norms and multiplicative-character orientations. Thus the zero-compression results below survive them at a fixed common conductor and fixed active set. Their dependence on the conductor remains a real obstruction when columns and moduli vary. A coefficient-dependent family of dilations is not one common operator unless that dependence has been separately arranged.

## 3. The actual native character class

Put
\[
 q_p=\chi_p^3,\qquad c_p=\chi_p^4.
\]
Here \(q_p\) is quadratic, \(c_p\) is cubic, and all three symbols have literal zero values on nonunits. Consequently
\[
 \chi_p=q_pc_p,\qquad \overline{\chi_p}=q_p\overline{c_p}.  \tag{3.1}
\]
The two possible native odd local modes are therefore
\[
 V_p=\operatorname{span}_{\mathbb C}\{\chi_p,\chi_p^5\}
     =q_p\operatorname{span}_{\mathbb C}\{c_p,\overline{c_p}\}.
\]
Their minimal invariant enlargement under the reflection is
\[
 O_p=\operatorname{span}_{\mathbb C}
                  \{\chi_p,\chi_p^3,\chi_p^5\}.           \tag{3.2}
\]
Let \(P_p\) be orthogonal projection onto \(V_p\).

For the original fourth moment, a prime occurs at most twice on each Hermitian side. Its signed incidence is \(a-b\), \(0\le a,b\le2\). Every odd signed incidence is therefore \(+1\) or \(-1\); an exponent three cannot occur in the native fourth-moment tuple. For every fixed higher order the same assertion holds on the fully singleton primes. It does not hold on all odd primes of an arbitrary sixth or higher moment: three occurrences on one side already give exponent three.

For a nonempty squarefree product \(r\) of good primes, let
\[
 V_r=\bigotimes_{p\mid r}V_p,\qquad T_r=\bigotimes_{p\mid r}T_p,
 \qquad P_r=\bigotimes_{p\mid r}P_p.
\]
A sign word \(\sigma\in\{+,-\}^{\omega(r)}\) denotes the orthogonal character tensor using \(\chi_p\) for \(+\) and \(\chi_p^5\) for \(-\). Let \(V_r^{\rm mix}\) be the span of the words containing both signs, and \(P_{\rm mix}\) its orthogonal projection. Write \(\Pi_-\) and \(\Pi_+\) for projection onto the all-minus and all-plus words.

### Theorem 3.1. Rank-one native compression and exact mixed-sign zero

For every such \(r\),
\[
 \boxed{P_rT_rP_r=\Pi_-.}                                \tag{3.3}
\]
In particular,
\[
 \boxed{P_{\rm mix}T_rP_{\rm mix}=0.}                     \tag{3.4}
\]
These statements tensor with an arbitrary Hilbert space and any bounded operator \(A\) on it:
\[
 (P_r\otimes I)(T_r\otimes A)(P_r\otimes I)=\Pi_-\otimes A.
                                                               \tag{3.5}
\]

**Proof.** Put \(a_p=\gamma_1(p)/\gamma_3(p)\), so \(|a_p|=1\). The Gauss product identities in Lemma 2.2 give
\[
 T_p\chi_p=a_p\chi_p^3,\qquad
 T_p\chi_p^3=\overline{a_p}\chi_p,\qquad
 T_p\chi_p^5=\chi_p^5.                                   \tag{3.6}
\]
The three characters are orthogonal. Thus \(P_pT_pP_p\) is exactly projection onto \(\chi_p^5\). Tensoring proves (3.3) and (3.5). Every mixed word has at least one plus sign, which becomes quadratic, so its image is orthogonal to every native word. This gives (3.4). \(\square\)

### Real coefficient consequence

Suppose \(f\in V_r\otimes\mathcal K\) is fixed by ordinary complex conjugation, where \(\mathcal K\) is closed under that conjugation, and \(\|A\|\le1\). Then
\[
 \left|\langle (T_r\otimes A)f,f\rangle\right|
       \le\frac12\|f\|^2.                               \tag{3.7}
\]
Indeed the all-minus and all-plus components of a real \(f\) have equal norm. By (3.5), the left side is at most the squared norm of its all-minus component, which is at most half of the total. No factor \(2^{-\omega(r)}\) follows: reality pairs a word with its global conjugate, not with each single-prime sign change independently.

Equivalently, if \(\mathfrak c\) denotes conjugation, the real symmetrized operator
\[
 T_r^{\mathbb R}=\tfrac12(T_r+\mathfrak cT_r\mathfrak c)
\]
has native compression
\[
 P_rT_r^{\mathbb R}P_r=\tfrac12(\Pi_-+\Pi_+).             \tag{3.8}
\]
Its mixed compression is zero. A block of the physical moment may be called real only after its actual conjugate block and conjugate coefficients have been included.

### Which balance hypotheses suffice

If every prime in both product columns is fully singleton, and each product column is nonunit, their sign word is mixed. Theorem 3.1 applies on that entire product conductor. It does not follow that the odd squarefree part of every balanced fourth-moment tuple is mixed. For example,
\[
 n_1=n_2=p,\qquad m_1=q,\quad m_2=s
\]
with distinct primes has an even exponent \(+2\) at \(p\), while its odd part \(qs\) is entirely minus. Those even and shared-prime factors must be retained in the second tensor factor in (3.5). Present exponent-zero factors are unit masks.

Fixed coefficient scalars do not change these incidence facts. Nor does reciprocity permit one to discard the actual orientation of a good prime. Intermediate A2/cube-completed product exponents include \(0,1,3,4\); their differences can contain the quadratic odd mode three. Thus the completed intermediate family is not confined to \(V_r\). Exact inversion restores the native family only after all correction terms have been reunited.

## 4. The entire missing mass is in the complementary channel

Let
\[
 E_r=\bigotimes_{p\mid r}1^\perp\subset\ell^2(\mathcal O_K/r).
\]
All vectors in \(V_r\) lie in \(E_r\), and \(T_r\) is a unitary involution on \(E_r\).

### Theorem 4.1. Exact leakage and return

On \(V_r\),
\[
 \boxed{
 P_rT_r(I-P_r)T_rP_r=I_{V_r}-\Pi_-.
 }                                                       \tag{4.1}
\]
On the mixed native subspace,
\[
 \boxed{
 P_{\rm mix}T_r(I-P_r)T_rP_{\rm mix}=I_{V_r^{\rm mix}}.
 }                                                       \tag{4.2}
\]
Consequently every \(f\in V_r^{\rm mix}\) satisfies
\[
 \|(I-P_r)T_rf\|=\|f\|,\qquad
 \langle T_rf,f\rangle=0,\qquad T_r^2f=f.                 \tag{4.3}
\]

**Proof.** Insert \(I=P_r+(I-P_r)\) between the two factors of \(T_r\). Since \(T_r^2=I\) on \(E_r\), the resulting compression is
\[
 I_{V_r}=(P_rT_rP_r)^2+
                P_rT_r(I-P_r)T_rP_r.
\]
Use (3.3), and then restrict to the mixed subspace. The norm statement follows because \(T_r\) is unitary and its native projection vanishes there. \(\square\)

For the actual fixed-conductor local map \(U=D_\epsilon T_r\), including any unit scalar, the corresponding stable statement is
\[
 P_rU^*(I-P_r)UP_r=I_{V_r}-\Pi_-.                        \tag{4.4}
\]
One must use the adjoint here: an arbitrary output dilation need not leave \(U^2=I\). Formula (4.4) follows from unitarity and from \(D_\epsilon\) preserving the character subspaces.

The zero in (3.4) is therefore not a small-norm estimate for the reflected vector. It says that all its mass is outside the native class. A proposed iterative bound must account for the term in (4.2), whose coefficient is exactly one.

## 5. The second symmetry gives an exact finite Weyl orbit

On \(O_p\) define
\[
 S_p=F_+/\gamma_3(p).
\]
This is a unitary involution on that subspace: \(F_+^2f(x)=f(-x)\), which is \(\delta f(x)\) on all three odd characters, and \(\gamma_3(p)^2=\delta\).

Use the common-norm orthogonal basis
\[
 e_1=\chi_p,\qquad e_3=a_p\chi_p^3,\qquad e_5=a_p\chi_p^5,
 \qquad a_p=\gamma_1(p)/\gamma_3(p).
\]
Then the exact actions are

| Basis vector | \(T_p\) | \(S_p\) |
|---|---|---|
| \(e_1\) | \(e_3\) | \(e_5\) |
| \(e_3\) | \(e_1\) | \(e_3\) |
| \(e_5\) | \(e_5\) | \(e_1\) |

Thus
\[
 T_p^2=S_p^2=(T_pS_p)^3=I.                               \tag{5.1}
\]
This is the three-dimensional permutation representation of \(S_3\). Its invariant line is spanned by \(e_1+e_3+e_5\); its orthogonal complement is the standard two-dimensional representation. The one-prime alternating representation is absent.

For \(r\), put \(S_r=\bigotimes S_p\). The pair \(T_r,S_r\) generates the simultaneous, or diagonal, \(S_3\) action on all prime positions. This is not the independent product group \(S_3^{\omega(r)}\); no prime-selective physical reflection has been supplied.

### Theorem 5.1. Mixed six-state orbits and their projections

For every mixed native sign word, its orbit under \(T_r,S_r\) consists of six orthogonal words. Exactly two are native: the original word and its global complement. The other four contain quadratic symbols. Let \(w,\overline w_{\rm sign}\) denote the two native basis words in the unitary basis above; the bar in this notation means sign complement, not a claim about the phase of complex conjugation.

Let \(\Pi_{\rm triv}\) and \(\Pi_{\rm alt}\) be the orthogonal projections obtained by averaging this diagonal \(S_3\) action with the trivial and alternating characters. On the native pair their compressions are
\[
 P\Pi_{\rm triv}P=\frac16
       \begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
 P\Pi_{\rm alt}P=\frac16
       \begin{pmatrix}1&-1\\-1&1\end{pmatrix}.             \tag{5.2}
\]
Both have norm \(1/3\). Globally on the mixed native subspace,
\[
 \boxed{
 P_{\rm mix}(\Pi_{\rm triv}+\Pi_{\rm alt})P_{\rm mix}
       =\frac13I_{V_r^{\rm mix}}.
 }                                                       \tag{5.3}
\]

**Proof.** A mixed word uses exactly the two different colors \(1,5\). A permutation fixing it must fix both colors, hence all three, so its stabilizer is trivial and its orbit has six elements. Only the identity and the transposition \(S_r=(1\ 5)\) give words using the colors \(1,5\) alone. In the group average their coefficients are \(1/6,1/6\); in the signed average they are \(1/6,-1/6\). This proves (5.2). Distinct native pairs belong to disjoint orthogonal orbits, and the two matrices sum to \(I/3\). \(\square\)

The alternating representation does occur in these mixed six-state orbits; it would be wrong to extend the one-prime absence of that representation to a tensor product. What is missing is an arithmetic identification of the actual Möbius coefficients with that signed orbit average. The Möbius sign on fully singleton tuples is the same under exchange of the two sides and does not furnish the four quadratic orbit coefficients.

There is a useful equivalent cyclic formulation. Let \(C=T_rS_r\), so \(C^3=I\). Then
\[
 \Pi_C=\frac13(I+C+C^2)=\Pi_{\rm triv}+\Pi_{\rm alt}
\]
on the orbit closure, and
\[
 \boxed{\|\Pi_Cf\|^2=\frac13\|f\|^2
          \quad(f\in V_r^{\rm mix}).}                    \tag{5.4}
\]
Indeed \(f,Cf,C^2f\) occupy three mutually orthogonal two-color sectors.

### Corollary 5.2. A sharp barrier to repeated symmetric reflections

Let \(W=(T_r+S_r)/2\). For every \(f\in V_r^{\rm mix}\) and integer \(n\ge0\),
\[
 \boxed{
 \|W^nf\|^2=
 \left(\frac13+\frac23\,4^{-n}\right)\|f\|^2.
 }                                                       \tag{5.5}
\]
In particular this natural repeated-reflection averaging never contracts a nonzero mixed native vector below \(1/\sqrt3\) of its initial norm.

**Proof.** On the trivial and alternating representations, \(W\) is \(+1\) and \(-1\). On the standard two-dimensional representation it has eigenvalues \(+1/2,-1/2\): this follows by computing \(T+S\) in the displayed three-dimensional permutation model and removing its invariant line. The regular representation of each mixed orbit contains only these three representation types. Equation (5.3) places exactly one third of the original squared norm in the first two types and two thirds in the standard types. Taking the \(2n\)-th eigenvalue powers proves (5.5). \(\square\)

Thus even a perfectly normalized finite Weyl walk retains a nonzero cyclic-invariant component for every nonzero native mixed vector. This is a more specific obstruction than merely observing that a unitary operator has norm one.

A potential signed completion would have to supply substantial complementary coefficients. Work in the invariant space \(O_r=\bigotimes_{p\mid r}O_p\), where all the operators above are defined. Precisely, if \(f\in V_r^{\rm mix}\), \(g\in O_r\) is orthogonal to \(V_r^{\rm mix}\), and
\(\Pi_C(f+g)=0\), then
\[
 \|g\|^2\ge\frac12\|f\|^2.                               \tag{5.6}
\]
The minimum is attained by \(g=-\tfrac12(Cf+C^2f)\). To prove optimality, project \(g\) onto the invariant space \(V_r^{\rm mix}\oplus CV_r^{\rm mix}\oplus C^2V_r^{\rm mix}\), whose three color sectors are orthogonal. Since \(g\perp V_r^{\rm mix}\), write this projection as \(Ch_1+C^2h_2\), with \(h_i\in V_r^{\rm mix}\). Equation (5.4) implies that the cyclic projection is injective on the native sector, so the cancellation condition requires \(h_1+h_2=-f\). Their squared norms are minimized by taking each to be \(-f/2\), giving (5.6). Components orthogonal to these sectors can only increase the norm. This identifies the size and precise phase relation of the counterterms that a successful arithmetic completion would need to create.

## 6. Growing conductors and the archimedean normalization

For squarefree \(Q=\prod\mathfrak p\), tensoring Theorem 2.1 on
\[
 E_Q=\bigotimes_{\mathfrak p\mid Q}1^\perp
\]
gives dimension \(\phi(Q)=\prod(q_{\mathfrak p}-1)\), trace \(2^{\omega(Q)}\), and eigenvalue multiplicities
\[
 \dim E_Q^\pm=
 \tfrac12\bigl(\phi(Q)\pm2^{\omega(Q)}\bigr).              \tag{6.1}
\]
These are exact growing-conductor formulas. Removing a bounded number of vectors cannot eliminate their large positive and negative eigenspaces.

On the Hilbert direct sum over infinitely many good primes, the direct sum of the \(T_p\) is not compact. Choose one normalized \(\chi_p^5\) in each summand; they are orthogonal fixed vectors. Their images have no norm-convergent subsequence. The operator \(I-T\) on this direct sum has infinite-dimensional kernel, and on its primitive space
\[
 (I-zT)^{-1}=\frac{I+zT}{1-z^2}\qquad(z\ne\pm1).         \tag{6.2}
\]
In particular no compact-Fredholm or convergent-Neumann argument at parameter one follows from this normalization. This statement concerns this exact direct-sum model; it does not rule out a different weighted arithmetic operator after additional cancellations have been proved.

The source's archimedean transform has the same absence of an intrinsic norm gain. For \(f\in C_c^\infty(0,\infty)\), set
\[
 \mathcal Hf(x)=\frac1{2\pi i}\int_{(0)}
       \widehat f(-t)\,R(t)(C_0x)^{-t}\,dt,
\]
where
\[
 R(t)=\frac{\Gamma(7/6+t)\Gamma(5/6+t)}
            {\Gamma(7/6-t)\Gamma(5/6-t)},\qquad
 C_0=\frac{(2\pi)^4}{27},\qquad
 \widehat f(s)=\int_0^\infty f(x)x^s\,\frac{dx}{x}.       \tag{6.3}
\]

### Proposition 6.1. Exact Mellin involution

The operator \(\mathcal H\) extends to a unitary involution on
\(L^2((0,\infty),dx/x)\).

**Proof.** On the imaginary axis, \(|R(it)|=1\), \(R(t)R(-t)=1\), and \(|C_0^{-it}|=1\). Mellin-Plancherel, which is ordinary Fourier-Plancherel after \(x=e^y\), applies to
\[
 \widehat{\mathcal Hf}(s)=C_0^{-s}R(s)\widehat f(-s),
 \qquad \Re s=0.
\]
This preserves the \(L^2\) norm. Applying it twice cancels both \(C_0^{-s}\) and the gamma quotient. Density of smooth compactly supported functions completes the proof. \(\square\)

The physical reflection also replaces scale \(X\) by \(N(c)^2/X\). This is reversible at a fixed denominator. It is not legitimate to discard the denominator's dependence on the tuple or change it between reflections. Nor does Proposition 6.1 identify the raw squarefree inverse coefficient with the full theta coefficient at every cusp: that separate completion and inverse remain necessary.

## 7. An exact native finite-row mismatch

The preceding compression would be directly useful if the physical centered covariance were \(\langle T_rf,f\rangle\) for its native coefficient polynomial \(f\). It is not.

Here is a concrete native four-column test at equal product norms, with trivial finite datum and the bad set consisting of the primes above 6. Let \(\omega^2+\omega+1=0\), and choose four distinct primary prime generators
\[
 \pi_7=-2-3\omega,\quad \overline{\pi_7}=1+3\omega,\qquad
 \pi_{13}=1-3\omega,\quad \overline{\pi_{13}}=4+3\omega.
\]
Their norms are \(7,7,13,13\), respectively. Their residue embeddings of \(\omega\), and hence of \(\zeta_6=1+\omega\), are

| Prime ideal | Residue field | \(\omega\) | \(\zeta_6\) |
|---|---|---:|---:|
| \((\pi_7)\) | \(\mathbb F_7\) | 4 | 5 |
| \((\overline{\pi_7})\) | \(\mathbb F_7\) | 2 | 3 |
| \((\pi_{13})\) | \(\mathbb F_{13}\) | 9 | 10 |
| \((\overline{\pi_{13}})\) | \(\mathbb F_{13}\) | 3 | 4 |

Use the actual residue symbol at each ideal, with its value zero on that ideal. Define
\[
 \varphi(u)=
 \chi_{\pi_7}(u)\chi_{\pi_{13}}(u)
 \overline{\chi_{\overline{\pi_7}}(u)
           \chi_{\overline{\pi_{13}}}(u)},\qquad
 f(u)=\varphi(u)+\overline{\varphi(u)}.                   \tag{7.1}
\]
The product columns \(\pi_7\pi_{13}\) and
\(\overline{\pi_7}\,\overline{\pi_{13}}\) are distinct ideals, both of norm 91. Every prime is singleton, so \(f\in V_r^{\rm mix}\), where \(Nr=7^2\,13^2\).

### Proposition 7.1. Zero compression and nonzero physical row sum

With these exact characters,
\[
 \langle T_rf,f\rangle=0,\qquad
 \sum_{0<Nu\le1}f(u)=12,\qquad
 \sum_{0<Nu\le13}f(u)=30.                               \tag{7.2}
\]

**Proof.** The first assertion is Theorem 3.1. The nonzero elements of norm at most one are exactly the six Eisenstein units. If \(\epsilon=\zeta_6^t\) is any unit, then
\[
 \chi_{\mathfrak p}(\epsilon)
      =\epsilon^{(N\mathfrak p-1)/6}.
\]
The two norm-7 exponents cancel across the Hermitian sides, as do the two norm-13 exponents. Thus \(\varphi(\epsilon)=1\), and each unit contributes two.

For the height-13 statement, \(4N(a+b\omega)=3a^2+(a-2b)^2\), with the analogous bound for \(b\). Thus every row of norm at most 13 has \(|a|,|b|\le4\). Exact enumeration, or the usual splitting of primes in the Eisenstein integers, gives the following complete shells:

| Norm | Number of rows | Sum of \(f\) |
|---:|---:|---:|
| 1 | 6 | 12 |
| 3 | 6 | 6 |
| 4 | 6 | 12 |
| 7 | 12 | 0 |
| 9 | 6 | \(-6\) |
| 12 | 6 | 6 |
| 13 | 12 | 0 |

To verify the values without a numerical character approximation, set \(\lambda_0=1-\omega\). Directly in the four residue fields, \(\varphi(\lambda_0)=\zeta_6\) and \(\varphi(2)=1\). Unit invariance and multiplicativity then give the values at norms 3, 4, 9, and 12. Rows of norm 7 or 13 meet a literal zero mask. The displayed sums total 30 over 54 rows. \(\square\)

The Möbius product for this four-prime tuple is \(+1\). The tuple and its conjugate are actual terms in a native fourth-moment expansion with trivial finite datum and smooth column weights equal to one at the four displayed norm ratios. In particular, take \(D=H=13\) and a fixed smooth test supported in \((1/2,2)\) equal to one at \(7/13\) and 1. No principal character has replaced a present zero mask. The example has equal product norms and an actual off-diagonal product pair.

This is not a counterexample to a moment estimate at \(H\asymp D\), and it does not evaluate the whole fourth moment. It refutes the proposed algebraic identification of native row covariance with the zero Bessel compression, even for a single Hermitian pair of native tuples.

## 8. What the physical adapter would have to preserve

There are four distinct interfaces.

1. **Linear versus quadratic coefficient degree.** After expansion, a fixed native tuple polynomial \(f(u)\) is sampled by the linear functional
   \(\sum_u w_H(u)f(u)\). The expression
   \(\langle T_rf,f\rangle\) is quadratic in its tuple coefficients. Treating these as identical changes the coefficient degree. Proposition 7.1 also refutes the identification without relying on that abstract observation.

2. **The two Fourier variables.** Ordinary row Poisson acts on \(\chi^j(u)\) by \(j\mapsto-j\). It preserves the two native signs and their mixed class. The theta Bessel map acts by \(j\mapsto-j-2\) after Fourier inversion and a cubic multiplier. In the source it acts on a column variable at a row/auxiliary conductor. Reciprocity does not by itself identify these Hilbert spaces or their product-dependent norm weights.

3. **The weight transforms too.** Even in a common primitive Hilbert space, if \(M\) is the sampling operator and \(T\) the involution, the valid relation is
   \[
    \langle Mf,f\rangle=\langle TMT\,Tf,Tf\rangle.        \tag{8.1}
   \]
   A centered error \(E\) becomes \(TET\), with exactly the same operator norm. The zero in (3.4) does not remove this transformed weight. On the full finite space one first compresses \(M\) to the primitive space; multiplication by a physical sampling weight need not preserve that space.

4. **Completion, conductors, and orientations.** Each source summand has its own \(c,\epsilon_p,\sigma_p\), cusp coefficient \(d_\sigma(\ell)\), additive character, and Mellin argument \(N\ell\,X/N(c)^2\). Finite rays and coprimality masks must be reunited literally. A frozen conductor's \(j=0,2,4\) modes remain in the complementary tensor factor; cube completion introduces \(j=3\) modes. Side balance on the original tuple alone does not remove them term by term.

These statements identify a possible productive target. Derive an actual two-column identity in which the native weighted covariance and the mixed quadratic leakage occur with their exact coefficient phases. Then estimate their signed combination, rather than taking the norm of each completed column. The finite analysis tells which terms have to cancel and which zeros cannot be used as estimates.

## 9. Comparison with the available quadratic inverse bound

This section is an analytic comparison, not an assertion that the missing physical adapter has been proved.

PR #926, commit 086bf0560c0c2679a1fe41418f583d2c5ca743c3, [QUADRATIC_INVERSE_PRODUCTS.md, Theorem 4.1](https://github.com/GettysburgResearch/riemann/blob/086bf0560c0c2679a1fe41418f583d2c5ca743c3/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/QUADRATIC_INVERSE_PRODUCTS.md), SHA-256 7cc4f91049d6e8b22a24080099a2947e4f30d5be68ea050bb7bcdf52a94c0696, proves under its stated uniform pointwise premises
\[
 \sum_{0<Nu\le H}\left|\prod_{i=1}^k
       \sum_{(n,q_iS)=1}\mu(n)\nu_i(n)\chi_n(u)^3
                                      W_i(Nn/L_i)\right|^2
 \ll D^\epsilon\min\{HR^2,\ HP+\sqrt H\,PR\},
                                                               \tag{9.1}
\]
where \(P=\prod L_i\), \(R=\prod L_i^{b_i}\), and each \(\nu_i\) is in the stipulated finite-order family. The moving exclusions remain literal. This estimate was checked in the source proof; its source-qualified pointwise inputs are not reproved here.

A global permutation of the three odd colors cannot send both different native colors \(1,5\) to the single quadratic color \(3\). A mixed native word therefore retains one sextic side after every Weyl permutation. Cauchy can compare a quadratic product with a sextic product, but it does not convert both to quadratic columns.

There is an additional coefficient obstruction. Equation (3.6) inserts
\[
 a_p=\gamma_1(p)/\gamma_3(p)
\]
on every plus-to-quadratic transition. These are unit Gauss ratios, not automatically fixed finite-order Hecke characters. The source also inserts the conductor-dependent factors in (2.6)–(2.7). Hence the actual leakage coefficient is not automatically one of the Möbius inverse columns in (9.1). On squarefree rows the classical quadratic large sieve permits arbitrary row-independent column coefficients, but at product length \(P\) its generic product bound is \(D^\epsilon(HP+P^2)\). It does not provide the required short-row improvement.

Even an optimistic Gauss-free, factor-preserving, same-height adapter would leave a quantitative problem. If all \(L_i=D\), \(b_i=b>1/2\), the second bound in (9.1) is
\[
 Q_k\ll D^\epsilon
       \bigl(HD^k+\sqrt H\,D^{k(1+b)}\bigr).             \tag{9.2}
\]
For a factorized mixed covariance against a sextic product of energy \(M_k\), Cauchy gives exactly
\[
 |\mathcal C_{\rm mixed}|\le\sqrt{Q_kM_k}.              \tag{9.3}
\]
If, additionally, a physical identity bounded \(M_k\) by its diagonal plus a fixed multiple of (9.3), the elementary quadratic inequality would give
\(M_k\ll HD^k+Q_k\), not a smaller envelope. The extra term in (9.2), relative to the target \(HD^k\), is
\[
 D^{kb}/\sqrt H.                                       \tag{9.4}
\]
It reaches the target only when \(H\ge D^{2kb}\). At \(H=D^{1+\theta}\) the loss is \(D^{kb-(1+\theta)/2}\). At \(k=2,b=7/8,H=D\), for example, (9.2) is \(D^{17/4+\epsilon}\), while the desired fourth moment is \(D^{3+\epsilon}\). The fully pointwise alternative \(HD^{2kb}\) does not repair this initial range.

This calculation is deliberately favorable to the proposed adapter: it assumes the Gauss ratios, cross-column exclusions, product weights, and changed physical scale have all been resolved. None of those assumptions follows from the finite orbit. The remaining useful statement is a genuinely signed mixed covariance estimate stronger than Cauchy with (9.1), or a new physical identity that changes its scale advantageously and keeps the transformed coefficient family within a proved theorem.

## 10. What has and has not been established

The new exact results are the rank-one native compression, its mixed-sign zero, the norm-one leakage and return, the simultaneous \(S_3\) orbit, the compulsory one-third cyclic-invariant energy, the sharp repeated-reflection formula, and the native equal-product-norm mismatch. They hold at every good prime and every squarefree conductor in their stated character classes. The archimedean transform is also exactly unitary in its natural Mellin norm.

The local results supply an explicit target for signed cancellation. They do not produce a physical contraction, a bound on the remaining two-column covariance, a generalized short-row moment, or a new zero-free region. No zero-free assertion, GRH, unproved angular extension, or growing-conductor spectral estimate was used in their proofs.

## 11. Finite diagnostic contract

The companion is checks/verify_bessel_channels.py. From this packet directory its normal invocation is:

```sh
python checks/verify_bessel_channels.py \
  --note BESSEL_CHANNELS_AND_LEAKAGE.md \
  --output results/bessel_channels.json
```

The same invocation with python -O must produce identical JSON bytes. The checker has no external Python dependencies. Every failed predicate raises an explicit exception; optimization cannot disable the checks.

Its arithmetic is exact integer arithmetic in cyclotomic quotient rings and exact rational arithmetic. It constructs the unscaled Bessel kernel \(K=qT\) directly for the actual prime-ideal characters at the four displayed split primes and at the inert norm-25 prime. It checks every matrix entry of \(K^*=K\) and \(K^2=q^2I-qJ\), the literal zero and present-unit-mask channels, all nontrivial Gauss products, and the Gauss-gauged \(T,S\) permutations. There are 1061 ordered matrix positions across these five cases. It also checks 510 native words at one through eight prime positions, all 247 mixed complement pairs, walk powers zero through eight, the exact counterterms, and both finite-row examples. The final acceptance count is 11562 explicit finite predicates.

The result binds the executed checker and supplied proof-note bytes by SHA-256. This binding does not certify the truth of the Markdown proof: the finite calculations have exactly the scope described above, and the general statements rest on the written proofs. The checker neither authenticates a remote repository on its own nor tests the missing analytic adapter, generalized moments, or RH.

