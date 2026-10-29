# Audit of a cyclic-field counting assertion over a cyclotomic base

**Scope:** This records an apparent conflict in the field-count asymptotic displayed in [Chen An, *Log-free zero density estimates for automorphic L-functions*, arXiv:2004.14410v2, Theorem 1.2 and §6.4](https://arxiv.org/html/2004.14410v2). It does **not** conclude that the paper's separate zero-density or almost-all Chebotarev statements are false. The calculation uses standard class-field theory, the conductor–discriminant formula and a standard positive-coefficient Tauberian theorem, together with the explicitly cited FHL character identities in [de Faveri §2.5.1](https://arxiv.org/abs/2610.04045v1). The arXiv v2 text was checked directly; the final journal text and any corrections have not been separately checked.

An's theorem defines `Z_n^*(k;Y)` by relative discriminant norm ≤Y, for cyclic degree-n Galois extensions satisfying its total-ramification condition. The displayed theorem asserts `|Z_n^*(k;Y)|∼c_n Y^(1/(n−1))` for fixed k and n, and explicitly notes that when n is prime every cyclic degree-n extension qualifies. For `k=Q(ζ₅)` and n=5, the following gives instead the lower bound

    |Z_5^*(k;Y)| ≫_k Y^(1/4) (log Y)^3.                          (1)

This lower bound is incompatible with the displayed constant-times-`Y^(1/4)` asymptotic. It is a lower bound only; no leading constant or exact asymptotic for the full field family is asserted here.

## Labels, characters and fields

Take the fixed good set S and the order-five Hecke family of de Faveri §2.3, and let g range over good fifth-power-free ideals. For each squarefree good radical r there are exactly `4^ω(r)` choices of g with `rad(g)=r`, by assigning each prime of r an exponent in {1,2,3,4}. Source §2.5.1 states that the primitive character χ_g has conductor

    f_g=c_g rad(g),    c_g|c,

with c a fixed S-supported modulus, and that primitive inducing characters inherit the multiplicativity of (2.4). Hence `N rad(g)≤N f_g≤C_k N rad(g)` for a fixed C_k.

Every nonunit g gives a character of **exact** order five: the source says its order divides five, and its conductor has a good prime factor, so the primitive character is nontrivial. Distinct fifth-free labels give distinct primitive characters. Indeed, if χ_g=χ_h, multiplicativity makes the primitive character attached to `g h⁴` trivial. If a good prime has unequal valuations in g and h, its valuation in `g h⁴` is nonzero modulo five, and the same source conductor formula forces this prime into that character's conductor, a contradiction. Thus the labels agree at every prime. This argument uses the actual source character multiplicativity and conductor formula, not conductor support alone.

By class field theory, each exact-order-five character cuts out a cyclic C₅ extension L/k. A field has exactly four nontrivial characters of its cyclic Galois group, so at most four labels in this injective family give the same field. Each of these four characters has the same conductor: raising a one-dimensional order-five character to a nonzero power does not change its kernel on any ramification group. The conductor–discriminant formula gives

    N Disc(L/k) = (N f_g)^4 ≤ C_k^4 (N rad(g))^4.                 (2)

The only archimedean places of k are complex, and the fixed S factors are included in f_g.

## The logarithmic lower count

For `Re s>1`, the generating series for the number of labels with a given radical is

    Σ_(r good squarefree) 4^ω(r)/(Nr)^s
      = ∏_(p∉S) (1+4(Np)^(−s))
      = ζ_k(s)^4 H_S(s),                                          (3)

where the fixed S factors are included in H_S. After cancelling the linear Euler terms, H_S is holomorphic in a neighborhood of s=1 and `H_S(1)>0`; indeed its good local factors are `(1+4q^−s)(1−q^−s)^4=1+O(q^−2 Re s)`. Since ζ_k has a simple pole at 1, the standard Delange/Ikehara Tauberian theorem for nonnegative coefficients yields

    Σ_(Nr≤T, r good squarefree) 4^ω(r) ∼ C T(log T)^3,   C>0.      (4)

Applying (2) with `T=(Y/C_k^4)^(1/4)` and dividing by at most four proves (1). Counting prime-ideal labels alone would give only a `Y^(1/4)/log Y` lower bound and would not expose the discrepancy; the logarithm in (1) comes from allowing all four local fifth-power-free exponents.

## Location of the pole discrepancy in §6.4

The same arXiv text defines, with fixed bad primes deleted,

    B(s)=∏_(χ mod 5) L_k(s,χ∘N_(k/Q)),

and states that B has only a simple pole at 1. Here there are four Dirichlet characters modulo 5. For k=Q(ζ₅), every good prime ideal 𝔭 has `N𝔭≡1 (mod 5)`: its residue field contains μ₅. Therefore every pulled-back χ is principal on the good ideals, and in fact

    B(s)=ζ_(k,S)(s)^4,

which has a **fourth-order** pole at 1. More generally, pullback through the norm is principal for the Dirichlet characters corresponding to `Gal(k∩Q(ζ₅)/Q)`, so the pole order depends on the cyclotomic intersection. Thus the source's simple-pole sentence is not valid in this base-field case; it is not merely a discrepancy in the notation for relative versus absolute discriminants.

Theorem 1.2's almost-all Chebotarev assertion and the paper's Theorem 1.1 density theorem are logically separate from the quoted simple-pole field asymptotic. This audit does not determine whether their proofs can be repaired, nor whether an updated journal version changes the asymptotic. No conclusion about those other assertions should be inferred from this calculation alone.

**Independent review:** A second researcher checked the arXiv v2 PDF, the total-ramification and relative-discriminant scope, the four principal norm-pullbacks, FHL conductor/injectivity argument, Tauberian lower bound and at-most-four field fibers. They identified and corrected the source locator to §6.4, pages 41–42. The final journal version and any corrections remain unchecked.
