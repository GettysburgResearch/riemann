# A growing-rank obstruction for the sextic natural-row operator

**Status.** This is a deduction from the stated Proposition 3.1 and the proof of Lemma 4.2 in Xu–Sang, [arXiv:2610.17675v2](https://arxiv.org/abs/2610.17675v2), and the standard sixth-power-free sextic large-sieve upper bound quoted in their (2.3). The cited Gram formula imports further source inputs, which are not independently proved here. The conclusion concerns **all good natural element rows**, with a fixed smooth nonnegative row weight, and **squarefree columns**. It does not establish a corresponding growing-rank bound after restricting the rows to sixth-power-free, squarefree, or prime-selected elements, nor does it establish a zero-free region.

Use the character, Gauss-sum, ray and row-weight conventions of Xu–Sang §§2–3. Let S be enlarged by a fixed good-prime cutoff so that the C₀ of their Lemma 4.2 satisfies C₀−1<1/4; S is thereafter independent of Y. Fix one primary S-supported ray class σ and a nonzero nonnegative U∈C_c^∞((1/2,1)). Define

    (T_Y b)(m) = w(m/√Y)^{1/2} Σ_s b(s) overline(χ_s(−m)),

where m ranges over all nonzero good elements and s over squarefree good primary elements of the ray class σ with Y/2<Ns<Y. All residue characters retain their nonunit zero masks. Let λ₁≥λ₂≥…≥0 be the eigenvalues of T_Y* T_Y, including multiplicities.

**Source-conditional proposition.** For every ε>0 and sufficiently large Y,

    #{j : λ_j ≥ Y^(8/7−ε)} ≫_ε Y^(5/42−ε).

The implicit constant may depend on S, w, U, the fixed ray class and ε. The statement is about actual eigenvalues of the full operator; it does not claim that the eigenvectors themselves are the Gauss test columns below or lie in their span.

## Many separate Gauss tests

Choose a fixed δ>0 sufficiently small in terms of ε, and let H=Y^(1/7−δ). Take all good prime ideals p with H/2≤Np≤H. As K=Q(ω) has class number one, these have primary generators; the prime ideal theorem gives J≫H/log H choices. Write P=Np. Define

    b_p(s) = Y^(−1/2) U(Ns/Y)(Ns/Y)^(−1/2) G(s,1) J₆(p⁵,s).

The zero-extended symbol automatically excludes p|s. Squarefree ideal counts in fixed ray classes show ||b_p||² is bounded above and below by positive constants, uniformly for P in the indicated range. The exclusion of the varying prime p affects the relevant density by O(1/P); an elementary squarefree count has uniform power-saving error.

For squarefree s the normalized primitive Gauss identity gives G(s,−m)=overline(χ_s(−m))G(s,1). Thus, with d=p and e_p=5 in Xu–Sang (3.1),

    ||T_Y b_p||² = Y ||F^{sf}_{p,5;U}(·;Y)||²_Y.

In Proposition 3.1, q=L=Y, X=L²/q=Y, D=P, j_p=(−5 mod 6)=1, and

    Ω(p,5) = P^(−1/6)/(1+P^(−1))² ≍ P^(−1/6).

Therefore, uniformly for P≤H,

    ||F_{p,5;U}||²_Y
      = C_{S,w} I(U)² Y^(1/6) Ω(p,5)
        + O_η(Y^η(1+Y^(1/12)+P)),                        (1)

where I(U)>0. The ratio of the worst error in (1) to the main term is O(Y^(η−7δ/6))+O(Y^(η−5/84−δ/6)); select η>0 smaller than both margins. Thus the all-column norm has the asserted positive main term uniformly.

The proof of Lemma 4.2 separates the unit powerful component from all nonunit components and bounds the latter by (C₀−1) times the square root of the same main term, plus O_η(Y^η(1+Y^(1/24)+P^(1/2))). Its argument explicitly retains the factor Ω(d,e), so this applies with d=p and e_p=5. The largest tail error divided by the square root of the main term is O(Y^(η−7δ/12))+O(Y^(η−5/168−δ/12)). Taking η small and using C₀−1<1/4 gives the uniform lower bound

    ||T_Y b_p||² ≫ Y^(7/6) P^(−1/6) ≫ Y^(7/6)H^(−1/6).  (2)

Here the main-term dominance uses P≤Y^(1/7−δ); it does not follow merely by inspecting the upper estimate in the statement of Lemma 4.2. The lower bound uses its proof's estimate for the nonunit components and the triangle inequality, as in the source's Corollary 4.3.

## Uniform near-orthogonality

For distinct p and q, the Gauss factors cancel in ⟨b_p,b_q⟩. Sextic reciprocity, in the fixed ray class, identifies the remaining product of symbols with a finite-order Hecke character ξ_{p,q} of conductor norm ≪_S P Q. It is nonprincipal because its local character at p is nontrivial while q≠p; multiplying by any fixed S-supported ray character does not alter this. The zero masks at p and q remain present.

Expand the fixed ray restriction into finitely many ray characters. For each term, squarefree inversion gives, up to bounded finite Euler factors,

    Σ_{s squarefree} ξ_{p,q}(s)/(Ns)^z = L_K(z,ξ_{p,q})/L_K(2z,ξ_{p,q}²).

The numerator is entire. On Re z=1/2+η, the denominator and its reciprocal are uniformly bounded in the moving characters by the absolutely convergent Euler product; the fixed smooth radial transform decays rapidly. Standard Hecke convexity on this line gives L_K(z,ξ_{p,q}) ≪_η (PQ)^(1/4+η)(1+|Im z|)^C. Consequently

    |⟨b_p,b_q⟩| ≪_η Y^(−1/2+η)(P Q)^(1/4+η)
                  ≪_η Y^(−1/2+η) H^(1/2+2η).          (3)

The implied constants are uniform in p,q, with fixed S and profiles. After normalizing b_p to unit length, the Gram matrix is I+o(1) in operator norm: the sum of the magnitudes of off-diagonal entries in each row is ≪ J Y^(−1/2+η)H^(1/2+2η)=o(1). Normalize the family into the column operator B; then ||B||²=1+o(1). The usual individual norm count ensures the normalization is uniformly bounded.

## Operator upper bound and eigenvalue count

The sextic sieve quoted as Xu–Sang (2.3) gives squared norm

    ≪_η (AB)^η {A+B+A^(5/6)B^(1/3)+A^(1/3)B^(5/6)}

for sixth-power-free good rows of norm ≤A and sixth-power-free columns of norm ≤B. To cover all natural rows here, write m=m₀v⁶ with m₀ sixth-power-free and Nv≪Y^(1/6). For each fixed v, χ_s(m₀v⁶)=χ_s(m₀)1_(s,v)=1; the mask is a restriction on the fixed coefficient vector and cannot increase its ℓ² norm. Apply the sieve at A=Y/(Nv)⁶ and B=Y and sum over v. Using Σ_v(Nv)^(−6), Σ_v(Nv)^(−5) and Σ_v(Nv)^(−2) convergent, and # {v:Nv≤Y^(1/6)}≪Y^(1/6), gives

    ||T_Y||² ≪_η Y^(7/6+η).                                (4)

The fixed row and column ray blocks and bounded radial weight cost constants; the all-row decomposition keeps the sixth-power mask rather than dropping it pointwise.

By (2) and uniform test normalization,

    tr(B* T_Y* T_Y B) ≫ J Y^(7/6)H^(−1/6).                 (5)

Since B*B=I+o(1), Ky Fan's variational inequality bounds the left-hand side by (1+o(1))Σ_{j≤J} λ_j. Set t=cY^(7/6)H^(−1/6) for a sufficiently small fixed c. If N eigenvalues are ≥t, then (4) and (5) yield

    N · O(Y^(7/6+η)) + Jt ≫ J Y^(7/6)H^(−1/6),
    N ≫_η J H^(−1/6)Y^(−η) ≫_η H^(5/6)Y^(−η)/log H.

Now t is a fixed multiple of Y^(8/7+δ/6), and H^(5/6)=Y^(5/42−5δ/6). Choosing δ and η sufficiently small in terms of ε and absorbing the logarithm proves the stated thresholds.

The argument shows that a fixed-dimensional or sub-Y^(5/42−ε)-dimensional orthogonal projection cannot eliminate every eigenvalue above the stated threshold. It does not identify an invariant theta spectrum, show how much of the Möbius vector lies in it, or control the rest of the operator.
