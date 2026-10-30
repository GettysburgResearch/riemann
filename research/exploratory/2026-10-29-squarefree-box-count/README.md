# Coprime squarefree ideal pairs in independent boxes

For a fixed number field K and fixed finite bad set S, let U=X^a and V=X^(1−a) with fixed `0<a<1`. In fixed positive-width norm annuli there are `≫_(K,S,a) UV= X` ordered pairs (A,B) of good squarefree integral ideals with `(A,B)=1`. The same holds with only B varying when A=1, giving `≫X` good squarefree B.

A proof with uniformity in the moving A is useful for the family counts. Let h=[K:Q]≥2. Standard fixed-field ideal counting gives `I(T)=c_K T+O_K(T^(1−1/h))` for T≥1; extending I(T)=0 for T<1 preserves a bound of the same form there. For any good squarefree A, Möbius inversion of squarefreeness and of `(A,B)=1` gives, for each fixed positive annulus and ε>0,

    #{B good sf: NB≈V, (A,B)=1}
      = c_(K,S,ann) V ∏_(p|A)(1+1/Np)^(−1)
        + O_(K,S,ann,ε)(V^(1−1/h+ε) τ_K(A)).               (1)

The main Euler factors follow from `∏_(p∤AS)(1−Np^(−2))·∏_(p|A)(1−Np^(−1))`. In the error, the squarefree-divisor sum `Σ_(Nd≤√V)(Nd)^(−2+2/h)` is `O(V^ε)` (a logarithm when h=2), while the divisors of A cost τ_K(A). The tail of the absolutely convergent main product is smaller; the finitely many fixed S factors only change the positive constant.

A positive proportion of good squarefree A in its annulus have `Σ_(p|A)1/Np≤C` for a fixed C. Indeed squarefree ideal counting gives `≫U` such A in total, while

    Σ_(NA≈U, A sf) Σ_(p|A)1/Np
       ≪ U Σ_p (Np)^(−2) ≪ U.                              (2)

For these A, the product in (1) is bounded below by a fixed positive constant. Since `τ_K(A)≪_ε U^ε` and U,V are fixed positive powers of X, choose ε small enough that the error is o(V) uniformly. Summing the ≫U admissible A gives ≫UV pairs. The upper bound `≪UV` follows from ideal counting, so the family has the expected linear order. No uniformity in varying K,a or S is asserted.

For the fixed-order FHL family in the linked field notes, the source conductor formula and tame local Kummer character show that for `g=AB^(n−1)` each good prime of A has local exponent 1 and each good prime of B has exponent n−1. For n>2 these are distinct, so the local inertia characters recover the ordered coprime squarefree pair (A,B) from the primitive character. Multiplication by one fixed background character preserves injectivity. In a cyclic degree-p field, at most p−1 distinct primitive order-p characters determine the same field; for cyclic quartic fields, at most two order-four characters do. Thus the linear number of labels gives ≫X fields whenever the relevant source character has exact order p or 4. The labels A,B are restricted to positive-power annuli, so the order-n character is nontrivial and has exact order n at any good prime dividing either factor.

The argument uses classical fixed-field ideal counting and the source's local-conductor identification; it makes no assertion about zero-density estimates or about uniformity in n.

**Independent review.** Other_families checked the uniform inversion/error, positive-proportion Euler-factor argument, tame local-exponent injectivity, and bounded character-to-field fibers. For quartic quadratic cores, a core's good conductor recovers AB but not the ordered factors; at most `τ_K(AB)≪X^ε` pairs share it, which is absorbed in a density bound's ε-loss.
