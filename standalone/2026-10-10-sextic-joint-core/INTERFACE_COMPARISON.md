# Exact composition of the A2 projection and coupled theta completion

Status: a proved finite arithmetic composition, its positive row-norm inequality, and the existing classical all-row envelope for the resulting mixed family, uniform in its moving exclusions and auxiliaries. The arithmetic statements use only the explicitly recorded coefficient identities; the classical envelope also uses the refined all-row sieve from PR #913. No stronger reflected estimate, centered signed off-diagonal bound, or fourth-moment target is proved. The two published packets are unchanged.

Pins: PR #914, commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`, `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`, especially Theorem 4.1 and the fixed-auxiliary discussion after Corollary 5.3; PR #915, commit `9959364671f89b86f3992ec5ed5e19f804eb607b`, `COUPLED_THETA_COMPLETION.md`, Sections 1–6. The imported October 5 `paper2.tex` at OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a` supplies `eq:crt-a`, `eq:T` (1287–1300), `eq:completed-twist` (1304–1308), and the completely multiplicative cube inverse `eq:cube-inverse` (1361–1373). The derivation below also proves the version of that inverse needed here directly, including every added zero mask.

## 1. Conventions and the common squarefree face

Work over the Eisenstein field, with multiplicatively chosen primary generators outside a fixed finite set S containing the primes over 6. Every ideal in this note is outside S unless a contrary condition is stated. Let

\[
\alpha(a)=a/|a|,\qquad
\lambda(a)=\overline{\alpha(a)}\xi(a),\qquad
a_\xi(a)=\lambda(a)\gamma_2(a)\quad(a\text{ squarefree}).
\tag{1.1}
\]

Here lambda is the multiplicative coefficient from PR #914, not a generator of the ramified prime. Character powers always retain the zero on nonunits. For coprime squarefree a,b, the source identity is

\[
a_\xi(ab)=a_\xi(a)a_\xi(b)\chi_b(a)^4.                 \tag{1.2}
\]

Fix smooth compactly supported weights W_1,W_2 on positive intervals [a_1,b_1] and [a_2,b_2], and use the tensor test V(x,y)=W_1(x)W_2(y). The following statements concern this exact test. They can be integrated over a common Mellin-separated representation of a general smooth test if the estimates being transferred have the requisite uniform seminorm control; no such additional analytic estimate is presumed here.

For squarefree q,f, with no requirement that (q,f)=1, put

\[
P_q(A,B;k,f)=
\sum_{\substack{ab\text{ squarefree}\\(ab,qS)=1}}
a_\xi(ab)\chi_{ab}(k)\chi_{ab}(f)^4
W_1(Na/A)W_2(Nb/B).                                    \tag{1.3}
\]

This is the raw two-factor face in PR #914. The scales A,B are positive; an empty rectangle contributes zero. All row identities hold for every nonzero k, without a squarefreeness assumption on k.

## 2. The mixed coupled family required by the projection

For a row-independent coefficient v(a), define

\[
\Psi_{k,af;q}(n)
=\xi(n)\chi_n(k)\chi_n(af)^4\mathbf1_{(n,qS)=1},
\tag{2.1}
\]

and let T(X;Psi) be the literal source sum

\[
T(X;\Psi)=\sum_{n\text{ squarefree}}\sum_b
\frac{\overline{\alpha(n)}\gamma_2(n)\Psi(n)
      \overline{\alpha(b)}^3\Psi(b)^3}
     {\sqrt{Nn}\,Nb}\,
V_*\!\left(\frac{Nn\,(Nb)^3}{X}\right),
\qquad V_*(y)=\sqrt y\,W_2(y).
\tag{2.2}
\]

The squarefree index n and unrestricted cube index b are both primary and outside S; n and b need not be coprime. This is the source's physical completion. Its reflected cusp indices can meet S and must not be restricted by this physical-sum convention; no reflected expansion is truncated in this note. Define the mixed completion

\[
\mathcal C_{q,v}(A,B;k,f)=\frac1{\sqrt A}
\sum_{\substack{a\text{ squarefree}\\(a,qS)=1}}
a_\xi(a)\chi_a(k)\chi_a(f)^4 v(a)W_1(Na/A)
T(B;\Psi_{k,af;q}).                                    \tag{2.3}
\]

The outside factor chi_a(f)^4 removes (a,f)>1, so af is squarefree on all surviving terms. The q mask acts on the outer factor and on both the inner squarefree and cube factors. All sums in (2.2)–(2.3) are finite on physical support. In particular this definition needs no analytic continuation.

When q=f=1 and v=1, (2.3) is exactly the family in PR #915. Its proved multiplier corollary allows v(a) to be row-independent and divisor-bounded on polynomially bounded support. It does not already assert the corresponding reflected component estimates for growing q,f. Corollary 3.3 below supplies the existing classical envelope for that enlarged family.

### Lemma 2.1. Exact cube inversion with the outer zero mask

Let \(v_h(a)=\mathbf1_{(a,h)=1}\). Then

\[
\boxed{
\frac{P_q(A,B;k,f)}{\sqrt{AB}}
=\sum_{\substack{h\text{ squarefree}\\(h,qfS)=1}}
\frac{\mu_K(h)\lambda(h)^3\chi_h(k)^3}{Nh}
\mathcal C_{q,v_h}\!\left(A,\frac{B}{(Nh)^3};k,f\right).
}                                                        \tag{2.4}
\]

This is a finite identity, including at rows k sharing primes with h or the other factors.

**Proof.** Fix the outer a in (2.3). Complete multiplicativity, including zeros, gives the source cube inverse for Psi=Psi_(k,af;q). One can verify it without reflection: substitute (2.2), group the cube factors h and b by their product d=hb, and use

\[
\sum_{h\mid d}\mu_K(h)=\mathbf1_{d=1}.
\tag{2.5}
\]

The coefficient outside T in that inverse is

\[
\frac{\mu_K(h)\overline{\alpha(h)}^3\Psi_{k,af;q}(h)^3}{Nh}
=\frac{\mu_K(h)\lambda(h)^3\chi_h(k)^3}{Nh}
\mathbf1_{(h,afqS)=1}.                                  \tag{2.6}
\]

Here chi_h(af)^12 is the displayed coprimality indicator, not the constant one. Its h,f,q restrictions may be placed outside the a sum, while its a restriction is precisely v_h(a). The b=1 face of T is B^(-1/2) times the squarefree inner sum. Multiply it by the outside coefficient in (2.3), use (1.2), and sum a to obtain (2.4). Every rearrangement is finite: a nonempty term has (Nh)^3<=b_2 B. No prime-sharing term has been replaced by a unit-modulus phase. Squarefree h follows from mu_K(h). This proves the identity. □

## 3. Compose with the exact A2 correction map

Let Q_q be PR #914's A2 arithmetic completion with the same tensor test. For pairwise-coprime squarefree c,d,e with C=cde and (C,q_0 fS)=1, set

\[
A_t=\frac{A}{Nc\,(Nd)^2(Ne)^2},\qquad
B_t=\frac{B}{(Nc)^2Nd\,(Ne)^2},\qquad
q_t=q_0 C,\qquad f_t=ef,
\tag{3.1}
\]

where t=(c,d,e). The ideals q_t,f_t are squarefree, but they overlap at e. Retaining that overlap is essential. Define

\[
\Omega_t(k,f)=\sqrt{NC}\,\lambda(C)^3 a_\xi(e)
\chi_{cd}(k)^3\chi_e(k)^4\chi_e(f)^4,
\qquad \omega_t(k,f)=\frac{\Omega_t(k,f)}{\sqrt{NC}}.
\tag{3.2}
\]

Thus |omega_t|<=1. The forward projection, PR #914 Theorem 4.1, is

\[
Q_{q_0}(A,B;k,f)=\sum_t\Omega_t(k,f)P_{q_t}(A_t,B_t;k,f_t).
\tag{3.3}
\]

### Theorem 3.1. Exact A2-to-coupled-theta composition

With the preceding conventions,

\[
\boxed{
\begin{split}
\frac{Q_{q_0}(A,B;k,f)}{\sqrt{AB}}
={}&\sum_{\substack{t=(c,d,e)\text{ disjoint squarefree}\\(C,q_0fS)=1}}
\sum_{\substack{h\text{ squarefree}\\(h,q_t f_t S)=1}}
\frac{\omega_t(k,f)\mu_K(h)\lambda(h)^3\chi_h(k)^3}
     {Nc\,Nd\,(Ne)^{3/2}\,Nh}\\
&\hspace{8mm}\times
\mathcal C_{q_t,v_h}\!\left(A_t,\frac{B_t}{(Nh)^3};k,f_t\right).
\end{split}}
\tag{3.4}
\]

The equality retains all phases, angular factors, and moving zero masks. It is an arithmetic representation by finite physical theta completions. It does not assert a two-variable Weyl functional equation for its left side.

**Proof.** Apply Lemma 2.1 to each child in (3.3). The scalar normalization is exactly

\[
\sqrt{NC}\sqrt{\frac{A_t B_t}{AB}}
=\frac1{Nc\,Nd\,(Ne)^{3/2}}.                         \tag{3.5}
\]

Multiply this by the cube-inverse coefficient 1/Nh. This is (3.4). The masks needed in Lemma 2.1 apply even though q_t and f_t overlap. The finiteness follows from the positive lower bound on nonzero ideal norms and the compact support of W_1,W_2. □

### Corollary 3.2. Positive norm transfer with three harmonic factors

Let \(\mathscr R\) be any finite collection of nonzero rows, equipped with any fixed nonnegative row weights. Write \(\|\cdot\|_{\mathscr R}\) for its Hilbert norm. Then

\[
\left\|\frac{Q_{q_0}(A,B;\cdot,f)}{\sqrt{AB}}\right\|_{\mathscr R}
\le\sum_{t,h}
\frac{
\left\|\mathcal C_{q_t,v_h}
 (A_t,B_t/(Nh)^3;\cdot,f_t)\right\|_{\mathscr R}}
{Nc\,Nd\,(Ne)^{3/2}\,Nh}.
\tag{3.6}
\]

Set Z=max(2,b_1 A,b_2 B). Terms with empty physical supports may be omitted. If every displayed mixed child has squared row norm at most M, then

\[
\boxed{
\left\|Q_{q_0}(A,B;\cdot,f)/\sqrt{AB}\right\|_{\mathscr R}^2
\ll_K M(\log(2Z))^6.
}
\tag{3.7}
\]

Here the implied constant depends on the number field K and fixed supports, not on the chosen collection of rows or its weights.

**Proof.** All row-dependent exterior multipliers in (3.4) have modulus at most one, so they act as contractions. Minkowski gives (3.6). Nonempty terms imply Nc,Nd,Ne,Nh<=Z, after harmless fixed support constants. Ideal counting yields

\[
\begin{split}
\sum_{t,h}\frac1{Nc\,Nd\,(Ne)^{3/2}\,Nh}
&\le
\left(\sum_{Nj\le Z}\frac1{Nj}\right)^3
\sum_j(Nj)^{-3/2}\\
&\ll (\log(2Z))^3.
\end{split}                                               \tag{3.8}
\]

The c,d,h sums are harmonic; the e sum is absolutely convergent. Drop restrictions only after taking the positive norm. Squaring proves (3.7). This is a fixed-auxiliary positive-norm statement, not the auxiliary-annulus energy inequality of PR #914, and not a transfer of a covariance-subtracted form. □

### Corollary 3.3. The mixed children satisfy the existing classical envelope

Assume all labels and scales are polynomially bounded in D, H>=1, and the row-independent v is bounded by D^epsilon for every epsilon on its support. The refined all-row sextic sieve in PR #913 implies, uniformly in the moving q,f,

\[
\boxed{
\sum_{0<Nk\le H}|\mathcal C_{q,v}(A,B;k,f)|^2
\ll D^\epsilon\left[H+H^{1/6}AB+(HAB)^{2/3}\right].
}
\tag{3.9}
\]

An empty rectangle contributes zero; all bounded nonempty rectangles below one are included with fixed support-dependent constants. In particular this applies to every v_h in Theorem 3.1. It is the existing classical envelope, not the stronger analytic estimate needed for the moment target.

**Proof.** Expand the cube factor b in (2.2). Put B_b=B/(Nb)^3. For fixed b outside qfS, the remaining normalized sum is P_q(A,B_b;k,f)/sqrt(A B_b), with its outer coefficient multiplied by \(v(a)\mathbf1_{(a,b)=1}\). Denote this polynomial by P_q^[v,b]. Exact complete multiplicativity gives

\[
\mathcal C_{q,v}(A,B;k,f)
=\sum_{\substack{b\text{ arbitrary}\\(b,qfS)=1}}
\frac{\lambda(b)^3\chi_b(k)^3}{Nb}
\frac{P_q^{[v,b]}(A,B_b;k,f)}{\sqrt{A B_b}}.
\tag{3.10}
\]

The moving q,f and b exclusions all remain in the coefficients. Group the squarefree product a n=m in P_q^[v,b]. Its coefficients are divisor-bounded, are independent of k, have squared mass O(D^epsilon A B_b), and are supported at Nm comparable to A B_b. The refined all-row sieve therefore bounds its normalized squared row norm by

\[
D^\epsilon[H+H^{1/6}A B_b+(H A B_b)^{2/3}].
\tag{3.11}
\]

In (3.10), the row multiplier chi_b(k)^3 is a contraction. Minkowski and sqrt(x+y+z)<=sqrt(x)+sqrt(y)+sqrt(z) give a bound for the row norm by

\[
D^\epsilon\left[
\sqrt H\sum_{Nb\ll B^{1/3}}\frac1{Nb}
+H^{1/12}\sqrt{AB}\sum_b(Nb)^{-5/2}
+(HAB)^{1/3}\sum_b(Nb)^{-2}\right].
\tag{3.12}
\]

The first sum is logarithmic, and the other two converge. Squaring and adjusting epsilon proves (3.9). Thus no new obstruction to this elementary envelope is introduced by the moving labels. The missing estimate is at the stronger scale or for the signed centered form described below. □

## 4. The two completions are not identical under an outer multiplier

The composition above is required because the published completions have different local support. For q=f=1 and v=1, direct expansion of (2.3) gives

\[
\sqrt{AB}\,\mathcal C_{1,1}(A,B;k,1)
=\sum_{\substack{a,n\text{ squarefree},\ b\text{ arbitrary}\\(a,nb)=1}}
\sqrt{Nb}\lambda(b)^3a_\xi(an)\chi_{a n b^3}(k)
W_1(Na/A)W_2(Nn\,(Nb)^3/B).
\tag{4.1}
\]

Its factor axes are n_1=a, n_2=nb^3. At a good prime p put a_p=a_xi(p) and b_p=sqrt(Np)lambda(p)^3. The local formal coefficient series is

\[
\frac{1+a_p y}{1-b_p y^3}+a_p x.                      \tag{4.2}
\]

This records coefficients at a single prime; it does not assert an ordinary global Euler product for the twisted Gauss coefficients. By contrast the A2 completion's local polynomial is

\[
1+a_p(x+y)+b_p(xy^2+x^2y)+b_p a_p x^2y^2.
\tag{4.3}
\]

They share the singleton face (0,0),(1,0),(0,1). The one-axis completion additionally has (0,3); the A2 completion instead has (1,2),(2,1),(2,2). A multiplier v(a) can change coefficients on existing support, but cannot add a pair absent from the support of (4.1). Consequently the published divisor-multiplier corollary cannot by itself identify (2.3) with the A2 completion. The finite correction and cube-inversion operations in Section 3 solve this arithmetic mismatch, with the enlarged mixed family explicitly displayed.

## 5. Which analytic hypotheses are still missing

The exact composition exposes a concrete analytic interface. None of the following requirements can be removed by (3.6):

1. **Moving exclusions on both axes at the stronger analytic scale.** q_t=q_0C acts on the outer factor, inner squarefree index, and theta cube index. The outer multiplier v_h removes (a,h)>1 and is covered by the published coefficient-stability corollary. It does not remove q_t from the inner theta family. The source's general pointwise reflection can represent principal local factors with their zero extension, but that fact is not the stronger coupled conductor-uniform mean-square bound required for all these children. Corollary 3.3 supplies the already available classical envelope.
2. **An additional moving auxiliary ideal.** The theta twist involves af_t, while the outside coefficient has chi_a(f_t)^4. The exact scalar computation in PR #915 concerns the particular pairing of the outer a with the theta auxiliary a, with squarefree k. Extra primes of f_t and their possible intersections with k change the local exponents and amplitudes. The q_t/f_t overlap at e also remains literal. No theorem in the published coupled component proof states uniformity in these added labels.
3. **All rows and the complete reflected sum.** PR #915's coupled component estimates average squarefree rows and bound specified reflected allocation blocks. PR #914's energy includes all nonzero k, and its required conclusion involves the full sum. In particular the generic negative allocation's long-dual term remains H^2 A^2/B in the current coupled estimate. It cannot be replaced by a diagonal-size bound through the arithmetic composition.
4. **A domain closed under smaller rectangles.** The children in (3.4) retain the original row range but lower the factor scales. An estimate confined to a positive conductor gap therefore need not apply to them. The initial fourth-moment frequency length D^(3-theta) versus product length D^2 is unchanged by an arithmetic identity; an all-scale estimate or preserved signed cancellation is still needed.
5. **The exact centered covariance.** PR #914 already removes the entire signed first-Poisson dual diagonal. Its remaining sufficient target is a signed strict off-diagonal form, with the original mu(f) weight and coupled row kernel. Substitution of (3.4) into both columns creates cross terms between independently corrected and cube-inverted children. Their reconstructed original product-column equality, phases, exclusions, and generally different auxiliaries must be retained. The positive norm inequality (3.6) proves no estimate for that subtraction.

The combination therefore makes a useful exact reduction: the full A2 polynomial is a controlled finite superposition of explicitly defined mixed one-axis theta completions, and those mixed families satisfy the existing classical envelope uniformly in their moving labels. It neither supplies the stronger reflected or centered estimates nor turns the proved component gains into the full fourth moment. There is no established 17/24 or generalized 2k-moment conclusion from this interface alone.
