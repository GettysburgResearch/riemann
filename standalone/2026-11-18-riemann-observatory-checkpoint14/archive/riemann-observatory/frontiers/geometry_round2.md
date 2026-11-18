# Geometry campaign: what purity adds beyond a functional equation

Snapshot: 2026-11-17. This campaign read Weil's twelve-page 1949 paper in full, inspected specified theorem/proof passages of Deligne's 1974 and 1980 originals, reconstructed two small arguments, and ran exact finite-field and symbolic checks. It did not audit the whole proof of either Deligne paper or the external SGA foundations. “RH” below always specifies which zeta function is meant.

## 1. The established finite-field theorem, with the correct hypotheses

Let X0 be smooth and proper over Fq, let X=X0×Fq Fqbar, and choose a prime ℓ different from char(Fq). With geometric Frobenius F, put

    Pi(t)=det(1−tF | H^i_et(X,Qℓ)).

Then Pi has integer coefficients independent of ℓ, and every complex conjugate of every eigenvalue α on H^i has |α|=q^(i/2). The zeta function is

    Z(X0,t)=∏i Pi(t)^((-1)^(i+1)),
    #X0(Fq^m)=∑i (−1)^i Tr(F^m | H^i).

Deligne I, Theorem (1.6), printed p. 276, proves the statement with **projective and smooth** hypotheses; Weil II, Corollary (3.3.9), p. 207, supplies **proper and smooth**. Do not silently give the 1974 theorem its later generality. The determinant/trace identities are recalled in Deligne I (1.5.1)–(1.5.4), pp. 275–276.

For a smooth projective geometrically connected curve C/Fq of genus g this becomes

    Z(C,t)=P1(t)/((1−t)(1−qt)),
    deg P1=2g,  P1(t)=∏j(1−αj t),  |αj|=sqrt(q),
    |#C(Fq^m)−(q^m+1)| ≤ 2g q^(m/2).

Under t=q^(−s), the numerator zeros lie on Re(s)=1/2, periodically with period 2πi/log q. This is the RH for this **function-field** zeta function. It is not RH for ζ(s) over the integers. Deligne I (1.1), p. 273, explicitly introduces the general Hasse–Weil Euler product, observes that Spec Z gives the Riemann zeta function, and then restricts the article to finite fields.

## 2. The actual positivity mechanism in Deligne I

Theorem (3.2), pp. 283–285, concerns a lisse Qℓ-sheaf F0 on an open subset U0 of P1/Fq. Its three substantial hypotheses are:

1. A nondegenerate alternating pairing F0⊗F0→Qℓ(−β), β∈Z.
2. The geometric monodromy image is an **open subgroup** of the associated symplectic group.
3. For every closed point x of U0, det(1−tFx | F0,x) has rational coefficients.

Its conclusion is pointwise purity of weight β: all complex conjugates of the local eigenvalues have magnitude |k(x)|^(β/2). “Symplectic self-duality implies purity” omits hypotheses 2 and 3 and is false.

The inspected proof uses even tensor powers. For every integer k≥1,

    Tr(Fx^m | F0,x^(⊗2k)) = Tr(Fx^m | F0,x)^(2k) ≥ 0,

because the trace on the right is rational. Exponentiating the logarithmic local Euler series preserves coefficient nonnegativity; this is Lemmas (3.3)–(3.4), p. 284. Positivity lets the convergence radius of a local factor be compared with that of the global product, Lemmas (3.5)–(3.6). **The decisive extra ingredient is not positivity alone:** symplectic invariant theory and Poincaré duality identify the possible global poles of the tensor-power L-function, through its compactly supported H². This pole control gives a bound whose exponent error shrinks as k→∞; the alternating duality supplies the opposite inequality.

For the geometric family, the relevant local system is the vanishing-cycle quotient E/(E∩Eperp). Openness of monodromy is supplied by (5.10), and rationality of the local characteristic polynomials by (6.2), p. 295. Keeping the quotient matters: the proof does not simply assume the vanishing-cycle form has no radical. The full SGA and monodromy proofs were not independently reconstructed here.

There is no claim in this source that Frobenius is a positive self-adjoint operator on a canonically given complex Hilbert space. Étale Qℓ-cohomology, a bilinear duality, complex absolute values of algebraic eigenvalues, and positive Euler coefficients are distinct structures.

## 3. A precise all-degree obstruction: positive Euler exponents still do not imply purity

**Proposition G-OBSTRUCTION-1 (independently established auxiliary example; no novelty claim).** Set q=5 and

    Z*(t)=(1−5t+5t²)/((1−t)(1−5t)).

This rational function has all of the following properties:

- Z*(0)=1 and Z*∈1+t Z[[t]]. Indeed Z*=1+t/((1−t)(1−5t)), so its coefficient of t^n, n≥1, is (5^n−1)/4.
- The genus-one reciprocal equation Z*(1/(5t))=Z*(t) holds as a rational identity.
- It has an Euler product ∏n≥1(1−t^n)^(−bn) with **bn nonnegative integers for every n**, not merely for a tested finite range.
- It has a finite-dimensional trace expression with dimensions (1,2,1), integer characteristic polynomials, and a nonsingular alternating duality of multiplier 5.
- Its numerator eigenvalues α±=(5±sqrt(5))/2 lie strictly between 1 and 5 and are reciprocal under α↦5/α, but neither has magnitude sqrt(5).

It therefore violates the curve RH while satisfying this explicitly listed algebraic, symmetry, and positivity package. It is an abstract zeta function; it is not the zeta function of a smooth proper curve and supplies no counterexample to Weil or Deligne.

### Proof of the nonnegative Euler exponents for all n

Take the directed multigraph with adjacency matrix

    A = [[2,1],[1,3]].

Label its edges as follows. At vertex 1 there are loops labeled 1 and 2, and an edge to vertex 2 labeled 3. At vertex 2 there are loops labeled 3, 4 and 5, and an edge to vertex 1 labeled 1.

Every label determines its arrival vertex: 1 and 2 arrive at vertex 1; 3, 4 and 5 arrive at vertex 2. Thus any cyclic label word determines its whole vertex sequence. At a specified source vertex there is at most one edge of a given label. It follows that a labeled periodic word determines at most one periodic edge path. If the cyclic word had smaller period than the path, uniqueness would force the path to have that smaller period too. Therefore primitive graph orbits inject into primitive necklaces of the full five-symbol shift **at each exact period**.

Write en for the number of primitive graph orbits of period n, and fn for the number of primitive full-shift necklaces. Both are nonnegative integers and en≤fn. Decomposing periodic points into primitive orbits gives

    1/det(1−tA)=∏n(1−t^n)^(−en),
    1/(1−5t)=∏n(1−t^n)^(−fn).

Since det(1−tA)=1−5t+5t², the asserted exponents are

    bn=fn−en+1[n=1] ≥0.

This proves the all-n assertion. The elementary trace identity also gives

    Nn := n[t^n](log Z*) = 5^n+1−Tr(A^n),
    Tr(A^n)=5 Tr(A^(n−1))−5 Tr(A^(n−2)).

The first counts Nn are 1,11,76,451,2501; the first bn are 1,5,25,110,500. They were independently recomputed by exact integer arithmetic, but the finite check is supplementary to the proof.

For the bilinear-duality claim, let J=[[0,1],[−1,0]]. Every 2×2 matrix satisfies AᵀJA=(det A)J; here det A=5. Taking H⁰ and H² one-dimensional with eigenvalues 1 and 5, and H¹ with operator A, gives exactly Z*. Thus Poincaré-type alternating reciprocity, even paired with a symmetric positive definite real matrix A, does not give weight-one purity. A positive definite metric G satisfying A*GA=5G would force purity and cannot exist for this A.

**Independent check:** the parent reviewer independently supplied and checked the label injection, exact-period preservation, recurrence, and off-circle eigenvalues before this write-up. Full third-party literature novelty review remains absent. Source provenance is the explicit construction and proof here, not an attribution to Deligne.

### What this rules out, and what it does not

Any purported derivation of RH using only the listed rational-zeta axioms, positive Euler exponents, reciprocal symmetry and a finite-dimensional alternating trace model has omitted an indispensable additional input. The example also has an elementary prime-number-type main term Nn=5^n+O(α+^n), with α+<5; that is still insufficient.

The example does not disprove an approach that supplies actual algebraic geometry, a positive polarization compatible with the relevant operator, tensor-power pole control, or another stronger analytic inequality. In particular it does not satisfy Deligne's full monodromy/purity hypotheses. It concerns neither the Euler factors of classical ζ(s) nor a modification of their primes.

### A genuine lisse-sheaf test of the missing hypothesis

Fix ℓ≠5. The same matrix A lies in GL2(Zℓ). Sending **geometric** Frobenius to A (and arithmetic Frobenius to A⁻¹) extends to a continuous representation of Gal(F5bar/F5): the map from Z extends to its profinite completion through the compact procyclic closure of the powers of A. Pull this representation back to A¹/F5. The resulting lisse sheaf V has a perfect alternating pairing to Qℓ(−1), since AᵀJA=5J. At a closed point x, its characteristic polynomial is det(1−t A^deg(x)), with integer coefficients. Nevertheless V is not pure of weight 1.

This is a literal deletion test for Deligne I (3.2): its geometric monodromy is trivial, so hypothesis (ii), openness in Sp2, fails. The other displayed pairing and rationality requirements hold. Even tensor local coefficients remain nonnegative, but

    L(A¹/F5, V^(⊗2k),t)=det(1−5t A^(⊗2k))⁻¹.

Its poles include t=(5 α+^(2k))⁻¹, rather than being restricted to absolute radius 5^(−k−1). Geometric coinvariants are the whole tensor space, rather than the symplectic invariant-contraction sector. This explains exactly why the source proof cannot drop its monodromy input. The parent reviewer independently checked the continuity, Frobenius convention and pole formula. This is not an error in Deligne.

## 4. The missing number-field counterpart, stated as a testable requirement

Deligne I, Lemma (7.1), pp. 298–300, first obtains a uniform weak estimate in middle degree d (d even):

    q^(d/2−1/2) ≤ |α| ≤ q^(d/2+1/2).

In (7.3), p. 301, Künneth places α^k in middle cohomology of X^k. The same weak estimate on even cartesian powers gives

    q^(d/2−1/(2k)) ≤ |α| ≤ q^(d/2+1/(2k)),

and k→∞ proves purity. The error 1/2 does **not grow with k**. This exact uniformity is the actionable feature of the geometric argument.

**Elementary amplification lemma.** Let q>1, w∈R and α≠0. Suppose for arbitrarily large integers k one has

    q^(kw/2−Ck) ≤ |α|^k ≤ q^(kw/2+Ck),  with Ck=o(k).

Taking logarithms, dividing by k, and passing to the limit proves |α|=q^(w/2). A fixed C is sufficient. Conversely an error Ck proportional to k gives no such conclusion. This lemma is independently checked; it is an abstraction of the inspected power argument, not a new RH theorem.

For an additive hypothetical number-field spectral generator Θ whose eigenvalues are the zeta zeros ρ, a tensor-compatible construction would place kρ in a k-fold generator. A sufficient missing estimate would be

    |Re λ−k/2| ≤ Ck=o(k)

for all eigenvalues λ of those generators. Then λ=kρ forces Reρ=1/2. Applying the usual trivial strip 0≤Reρ≤1 separately to each factor gives only 0≤Re(kρ)≤k, an error k/2; it supplies no improvement. A genuine proposal must specify the space, generator and domains, the tensor construction, the trace/determinant formula, the treatment of poles and archimedean terms, and the source of the sublinear-in-k error. No such construction or bound is established in this campaign.

The immediate mathematical task is narrower than inventing a “Frobenius for Spec Z”: formulate one actual analytic or operator model with tensor-compatible spectra and prove a **quantified** localization estimate. Test its claimed axioms on Z* above before treating symmetry or coefficient positivity as sufficient. A counterexample satisfying all the proposed axioms would eliminate that model's inference; success against this test would still not prove RH.

## 5. A documented analytic-to-geometric transfer worth preserving

Weil II, §2, explicitly develops the Hadamard–de la Vallée-Poussin method; (2.1.9), p. 191, describes the logarithmic derivative of classical ζ as a Fourier transform of a positive prime-power measure and invokes Mertens's positivity argument. The geometric output is Corollary (2.2.10), p. 196:

    X0/Fq smooth curve, F0 lisse and iota-pure of weight β
    ⇒ every α on Hc¹(X,F) has wq(α)<β+2,
    wq(α)=2 log_q |iota(α)|.

The strict inequality starts a geometric product/vanishing-cycle iteration. Lemma (3.2.4)(k), pp. 197–204, improves the weight-zero Hc¹ bound to wq(α)≤1+2^(−k), and the limiting bound plus duality gives the relevant purity theorem (3.2.3). The introduction, pp. 139–141, explains the square/product mechanism and integer-weight step. This campaign inspected these passages and theorem statements, not every intermediate local calculation.

This is a real historical transfer from classical analytic number theory into the function-field proof. It is not a newly discovered literature connection, and reversing its direction does not automatically produce a classical RH argument. A concrete future question is whether an explicit analytic family admits both the needed positive representation-theoretic L-functions and the geometric-style contraction of its localization error. The error contraction, rather than the reuse of a positivity polynomial alone, is the missing statement.

## 6. Properness and boundary weights are not optional details

Weil II (3.3.4), p. 206, gives **weights ≤n+i** on Hc^i for a mixed sheaf of weights ≤n. On smooth X and a lisse sheaf of weights ≥n, (3.3.5) gives weights ≥n+i on ordinary H^i. The image Hc^i→H^i is pure of weight n+i for a pure lisse sheaf, (3.3.6). If X is proper, compact and ordinary cohomology agree, producing purity in all degrees. Without properness the two groups need not agree.

For example, #Gm(Fq^m)=q^m−1 gives Z(Gm,t)=(1−t)/(1−qt). Its boundary terms have weights different from a naive proper-curve H¹ interpretation. Likewise #A¹(Fq^m)=q^m gives Z(A¹,t)=1/(1−qt). These examples refute an unrestricted modern paraphrase that drops properness from the full proper-curve factorization.

Weil's 1949 p. 507 conjectural paragraph says “without singular points” in its historical terminology, after discussing projective diagonal hypersurfaces. A modern record must state the proper/projective setting explicitly. This observation is a warning about unrestricted modern paraphrase and historical conventions, **not a verified mathematical error in a proved theorem of Weil**.

## 7. Exact curve experiment and independently reconstructed lemma

For E/F5 given by y²=x³−x, the projective curve is smooth: the short-Weierstrass discriminant is 64, nonzero modulo 5, and the projective point at infinity is nonsingular. Exact enumeration over F5 gives #E(F5)=8, so a5=−2 and

    P1(t)=1+2t+5t²,
    α=−1±2i,   |α|²=5.

The recurrence Sm=a5 S(m−1)−5 S(m−2), S0=2, S1=a5, predicts N25=32 and N125=104. Independent direct enumeration over F5[u]/(u²−2) and F5[u]/(u³+u+1) confirms both. The code directly checks inverses of all nonzero elements, rather than merely assuming that a named polynomial defines a field. These are exact finite checks; they do not reprove Deligne's general theorem.

The Gauss-sum lemma in Weil 1949, equation (4), pp. 500–501, was reconstructed independently. If χ is a nontrivial multiplicative character of Fq* and ψ a nontrivial additive character, then

    G(χ,ψ)=∑x≠0 χ(x)ψ(x),
    |G|²=∑u≠0 χ(u)∑y≠0 ψ((u−1)y)
         =(q−1)−∑u≠1 χ(u)=q.

Only finite sums are interchanged. Nontriviality of **both** characters is indispensable. Weil's Jacobi sum relation j=q^(−1)∏r_i G(χ_i), with r+1 nontrivial characters whose product is trivial, then gives |j|=q^((r−1)/2). This explains the square-root cancellation in the diagonal examples without confusing it with a proof for arbitrary varieties.

Reproduce: `python experiments/code/geometry_round2_exact.py`. Results: `experiments/results/geometry_round2_exact.json`. The graph proof above establishes all-degree positivity; the program only tests the first 80 Euler exponents and cyclic coding through period 8.

## 8. Next concrete tasks

1. Independently review Proposition G-OBSTRUCTION-1, including exact-period preservation, and search for prior formulations before assigning novelty.
2. For any proposed number-field trace model, list which axioms are stronger than those satisfied by Z*. If none are, stop that inference and preserve the counterexample.
3. Formalize the small Gauss-norm and amplification lemmas in a proof assistant; these are finite, source-grounded targets with few analytic prerequisites.
4. Audit the precise pole-control step for one concrete rank-two lisse sheaf in Deligne I (3.7), then compute low even tensor powers and identify the invariant contractions. This checks a real hypothesis/conclusion match, not a vocabulary analogy.
5. Reconstruct Weil II (2.2.10)→(3.2.4) completely for one specified family, keeping the strict initial inequality and the contraction constant explicit. This campaign inspected, but did not independently verify, that full argument.

## 9. Derived sufficient condition proposed for independent review

The inspected proof suggests a weaker sufficient hypothesis than open symplectic monodromy. Let U0 be a nonempty affine open of P¹/Fq, ℓ≠char Fq, and F0 a lisse Qℓ-sheaf with a perfect alternating pairing to Qℓ(−β), β∈Z, and rational local characteristic polynomials at every closed point. Let V be its geometric generic fibre and G the geometric monodromy image. Suppose that for arbitrarily large k all eigenvalues of geometric Frobenius on

    Wk=(V^(⊗2k))_G

are algebraic and all their complex conjugates have magnitude at most q^(kβ+Ck), where Ck≥0 and Ck=o(k). Then the proposed conclusion is that F0 is pointwise pure of weight β. This is a **derived lemma pending separate review**, not a claimed new theorem of the literature.

Proof reconstruction: Hc⁰(U,F^(⊗2k))=0 and Hc²(U,F^(⊗2k))=Wk(−1), by Deligne I (2.10). Thus possible global Euler-product poles have magnitude at least q^(−kβ−Ck−1). Rational local characteristic polynomials make even-tensor traces nonnegative rational numbers, hence local inverse determinants have nonnegative real power-series coefficients, as in I (3.3)–(3.4). The formal Euler product has only finitely many factors at each degree. Positivity therefore forces each local convergence radius to be at least the global radius, I (3.5)–(3.6). For a local Fx eigenvalue α at degree e, a local pole has magnitude |α|^(−2k/e). Consequently

    |α| ≤ q_x^(β/2+(Ck+1)/(2k)).

Pass to arbitrarily large k, and apply the same upper bound to q_x^β/α, which is also an eigenvalue by the pairing. This gives equality. Every complex conjugate is handled in the same way. Grothendieck rationality and the rational formal Euler coefficients justify regarding the global function as rational over Q; this descent can also be proved by the Hankel determinant argument recalled in Deligne I (1.7)⇒(1.6).

The source's open-Sp hypothesis supplies exact Tate coinvariants, corresponding to Ck=0. The constant arithmetic sheaf above violates the proposed replacement because Wk includes α+^(2k), whose excess exponent over kβ grows linearly in k. The next step is an independent audit of the pole-radius argument and coefficient-field descent; no classical-RH assertion is made.
