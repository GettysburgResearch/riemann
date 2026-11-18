# Independent review: asymptotic coinvariant bound as a purity criterion

Reviewer: history/spectral agent. Date2026-11-17. The proof in sections1–7 was reconstructed from the task statement without reading the geometry agent's proposed proof. It is a scoped verification of a conditional sheaf-theoretic criterion, not a new proof of the Weil conjectures or classicalRH. Source comparison follows the independent derivation.

## 1. Exact hypotheses and conventions

Let U_0 be a nonempty smooth affine open subscheme of P¹ overF_q, geometrically connected, and let F_0 be a lisse finite-rank Q_ell-sheaf, ell different from the characteristic. Assume positive even rank2n, an integerβ and a perfect alternating pairing

    F_0⊗F_0 → Q_ell(−β).

For each closed pointx of degreed, assume det(1−Frob_x T|F_x)∈Q[T]. Frob is **geometric** Frobenius; on Q_ell(−1), Frob_q acts byq, and Frob_x acts byq^d=q_x. All complex absolute values below concern roots of rational local characteristic polynomials, hence algebraic numbers. No semisimplicity of these Frobenius operators is assumed.

Let V be a geometric generic fiber and G=π_1(U_0⊗F_q Fbar_q). For an unbounded set of positive integersk let

    C_(2k)=(V^(⊗2k))_G

be the **coinvariant quotient**, with its well-defined geometric arithmetic Frobenius action. Assume its eigenvaluesλ are algebraic overQ under a fixed compatible inclusion Qbar→Qbar_ell, and every complex conjugate satisfies

    |λ|≤q^(kβ+c_k), with c_k/k→0

along that set ofk. The additive constant need not be uniform ink; sublinearity is the crucial point. Merely giving an ell-adic absolute-value bound would not be sufficient.

Claim verified below: every local eigenvalueα has |ι(α)|=q_x^(β/2) for every complex embeddingι. Thus F_0 is pure of weightβ in the stated all-embeddings sense.

## 2. Positivity needs rational local traces

Put E_k=F_0^(⊗2k). Newton identities imply Tr(Frob_x^r|F_x)∈Q for every integerr≥1. Therefore

    Tr(Frob_x^r|E_(k,x))=[Tr(Frob_x^r|F_x)]^(2k)≥0

as a real number. It follows that the local factor

    L_x(E_k,t)=exp(∑_(r≥1)Tr(Frob_x^r|F_x)^(2k)t^(r degx)/r)

has rational nonnegative Taylor coefficients and constant coefficient1. Finite products do also, and the Euler product is formally well-defined because there are finitely many closed points of bounded degree. Removing a single point leaves another such nonnegative-coefficient product. Hence, coefficient by coefficient,

    [t^m]L(U_0,E_k,t)≥[t^m]L_x(E_k,t)≥0.

The rationality is doing real work. An arbitrary complex trace raised to an even power need not be nonnegative. A polynomial overQ_ell alone provides no ordered real positivity.

## 3. Compact-support cohomology and complex poles

The lisse sheaf on the connected nonproper curve has H_c^0=0: a nonzero lisse section cannot be supported on a finite closed subset. Poincaré duality identifies

    H_c²(U,E_k)≅C_(2k)(−1).

Thus geometric Frob_q eigenvalues on H_c² areqλ. The trace formula gives, overQ_ell,

    L(U_0,E_k,t)=det(1−tFrob_q|H_c¹)/det(1−tFrob_q|H_c²).

Grothendieck rationality is an external established input, not re-proved in this review. All possible finite poles of the reduced function are reciprocals ofqλ. Cancellation with H_c¹ may **remove** those poles; it cannot introduce new ones.

To speak about a complex Taylor radius, descend the rational function toQ(t). Its formal Taylor coefficients are rational by section2, while the trace formula puts it inQ_ell(t). The standard rational-series descent gives

    Q[[t]]∩Q_ell(t)=Q(t).

One proof uses the finite-rank Hankel criterion: matrix ranks of rational coefficient matrices do not change on extending scalars fromQ toQ_ell, so a rational linear recurrence exists already overQ. This step must not be replaced by choosing an unspecified embedding of allQ_ell intoC.

The poles of the descended rational function are algebraic. Under the fixed algebraic closure inclusion intoQbar_ell, each is a reciprocal ofqλ, and every complex conjugate is covered by the assumed all-conjugates bound. Therefore the complex Taylor radius satisfies

    R_global≥q^(−kβ−c_k−1).

No bound on H_c¹ eigenvalues is required. No assertion that all potential poles survive is required. Pringsheim's theorem is optional here: rationality and the complete pole bound already control the radius.

## 4. Local radius and the degree normalization

Coefficient domination of nonnegative sequences implies

    R_global≤R_local.

Ifα is any eigenvalue of Frob_x onF_x, thenα^(2k) is an eigenvalue onE_(k,x). The local factor is the reciprocal of det(1−t^dFrob_x|E_(k,x)), with numerator1. Consequently it has a genuine pole of modulus |α|^(−2k/d), or another pole no farther from0. Thus

    q^(−kβ−c_k−1)≤R_global≤R_local≤|α|^(−2k/d).

This gives exactly

    |α|≤q_x^[β/2+(c_k+1)/(2k)].

The exponentd comes from t^d in the Euler factor. The extra+1 is the Tate twist inH_c². Omitting either factor changes the assertion. Sendingk→∞ along the assumed unbounded set yields |α|≤q_x^(β/2).

## 5. Self-duality supplies the opposite inequality

The perfect pairing makes the multiset of local eigenvalues stable under

    α↦q_x^β/α.

This follows from the similitude matrix identity even in the presence of Jordan blocks. The relation is algebraic and therefore holds after every complex embedding. Applying the upper bound to the paired eigenvalue gives |α|≥q_x^(β/2). Equality follows.

## 6. What this does and does not weaken

The proposed conditional criterion is mathematically sound under the exact hypotheses above. It replaces control of all even-tensor coinvariant Frobenius eigenvalues by an asymptotic exponent bound; it does not remove that arithmetic input. A perfect alternating form alone supplies a nonzero Tate quotient of each even tensor, so the assumption is not a vacuous zero-coinvariant condition.

The hypothesis is genuinely broader than open symplectic geometric monodromy: the constant rank2 trivial sheaf withβ=0 has trivial geometric monodromy, not an open subgroup ofSp_2, yet all its coinvariant eigenvalues are1 andc_k=0 works. Establishing the asymptotic coinvariant hypothesis in an interesting new family may be as difficult as establishing its purity. No novelty claim or claim of a new route to classicalRH follows.

A useful next problem is to isolate independently checkable monodromy/representation conditions forcing c_k=o(k), without assuming the local purity one wishes to prove. Energy-like language or formal functional equations supply none of those estimates by themselves.

## 7. Failure modes checked

- H_c^0 vanishing requires the affine/nonproper connected curve setting; a proper base would add a denominator term and needs separate treatment.
- The action on coinvariants must be arithmetic geometric Frobenius, not merely the geometric fundamental group action.
- A single unspecified complex embedding of the assumed eigenvalues is weaker than the all-conjugates assumption used here.
- Local characteristic polynomials rational overQ are essential for the stated positivity argument; Q_ell-rationality alone does not suffice.
- Cancellation in cohomology only improves the global radius bound. Positivity compares Euler coefficients before cancellation.
- An unbounded subsequence ofk suffices; a fixed finite family of tensor powers does not remove the residual(c_k+1)/(2k).
- The alternating form is used for reciprocal eigenvalue symmetry; it does not by itself prove upper purity.

Finding class: independently checked with no issue found in the reconstructed implication, contingent on the explicitly named cohomological identities and rationality theorem.

## 8. Formal genus-one zeta countermodel to deleted axioms

Consider

    Z(t)=(1−5t+5t²)/[(1−t)(1−5t)].

Let α=(5+sqrt5)/2 andβ_0=(5−sqrt5)/2 (the notationβ_0 here is unrelated to the sheaf weightβ). They have sum5 and product5, but neither has modulus sqrt5. The numerator is reciprocal:5t²P(1/(5t))=P(t). The denominator has the same reciprocity, so

    Z(1/(5t))=Z(t),

the genus-one functional-equation shape. This is not the zeta function of a curve overF_5; its hypotheticalN_1=1 lies below the genus-one Hasse bound.

It nevertheless has a positive-integer Euler product. Write S_0=2,S_1=5,S_r=5S_(r−1)−5S_(r−2)=α^r+β_0^r and

    N_r=1+5^r−S_r,
    b_n=(1/n)∑_(d|n)μ(n/d)N_d.

Then Z(t)=∏_(n≥1)(1−t^n)^(−b_n) formally. Integrality ofb_n follows either by the integral Witt-vector identity or directly by induction: Z∈1+tZ[[t]], and canceling each first remaining coefficient with an integral power of(1−t^n) constructs unique integer Euler exponents.

For positivity, α,β_0 lie in(0,4), so0<S_r<2·4^r andN_r≤5^r+1. We have N_1=1,N_2=11,N_3=76, and for r≥4 the lower bound 5^r+1−2·4^r is positive; thus every N_r is nonnegative. Directlyb_1=1,b_2=5,b_3=25. Forn≥4, every proper divisor is≤n/2 and

    n b_n≥N_n−∑_(d|n,d<n)N_d
           ≥5^n+1−2·4^n−(5/4)5^(n/2)−n/2.

After dividing by5^n, the subtracted terms are at most

    2(4/5)^4 + (5/4)5^(−2) + 2/625
    = 514/625+1/20 <1.

Here n/(2·5^n) decreases forn≥1. The lower bound is strictly positive, provingb_n>0 for alln≥4 as well. Thus positivity and integrality of an Euler product, rationality, reciprocity and a genus-one functional-equation shape do not by themselves force the reciprocal roots onto the Weil circle.

This formal countermodel concerns deleted axioms. It does not refute the sheaf criterion above: it supplies neither a lisse sheaf satisfying the prescribed tensor coinvariant bounds nor the required positive even-tensor trace family and cohomological interpretation.

## 9. Original-source comparison after independent derivation

The original Deligne1974 text was then inspected in `sources/geometry_round2/deligne1974.txt`,§3.1–3.7, printedpp283–285, with the source PDF manifest already supplied by the geometry track. Canonical source: https://www.numdam.org/item/10.1007/BF02684373.pdf . This is a scoped primary-source reading, not a whole-paper reading count.

Theorem3.2 assumes alternating pairing, open symplectic geometric monodromy and rational local characteristic polynomials. Lemmas3.3–3.6 give precisely the even-tensor trace positivity and Euler-product radius comparison reconstructed above. Section3.7 uses symplectic invariant theory to identify coinvariants as copies of Q_ell(−kβ), hence H_c² as copies of Q_ell(−kβ−1). The text explicitly says that only the complex absolute value of the possible poles is used in the remainder of the argument. The proposed sublinear coinvariant bound therefore substitutes for that specific input, and the rest of Deligne's proof continues with the modified pole exponent.

No discrepancy found with the primary argument's normalization: local Euler variables are t^(degx), and the compact-support top cohomology contributes the +1. The conditional generalization should be described as an abstraction of this existing proof engine, not as a discovery of a new purity method. No original source claim is alleged erroneous.

## 10. Actual sheaf stress test when the coinvariant estimate is deleted

The same polynomial also gives a concrete lisse-sheaf example showing why pairing and rationality alone do not prove purity. Fixell≠5 and A=[[3,1],[1,2]]∈GL_2(Z_ell), detA=5. The map sending geometric Frobenius ofF_5 toA extends continuously from the cyclic group to its profinite completion: powers moduloell^m have finite order for everym. Pulling this representation ofGal(Fbar_5/F_5) back toU_0 gives a lisse sheaf with trivial **geometric** monodromy. It is not the constant sheaf with trivial arithmetic action.

For J=[[0,1],[−1,0]], A^tJA=5J, so the perfect pairing has targetQ_ell(−1), weight parameterβ=1. At a closed point of degreed the action isA^d, hence local characteristic polynomials are rational (indeed integral). But the eigenvaluesα,β_0 above are not of modulus sqrt5.

Here C_(2k)=V^(⊗2k), andα^(2k) is a coinvariant eigenvalue. The proposed estimate would force

    c_k/k≥2log_5α−1>0,

contradictingc_k=o(k). Thus this actual sheaf example fails precisely the new arithmetic hypothesis, and also fails Deligne's open symplectic geometric-monodromy hypothesis. It is compatible with both the original theorem and the conditional criterion reviewed here. The formalZ(t) of section8 is a separate would-be curve zeta function; one must not identify its numerator with actual curveH¹ merely because this two-dimensional arithmetic representation exists.
