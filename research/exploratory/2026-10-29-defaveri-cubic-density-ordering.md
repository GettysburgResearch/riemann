# de Faveri's cubic zero-density estimate and conductor ordering

[de Faveri, arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1), Corollary 1.5, states for a fixed degree-d field K containing μ_n, fixed S and the associated residue-character family that

    Σ_{a ∈ I(S), a n-th-power-free, Na ≤ N} N(σ,T,a)
       ≪_{K,S,ε} N^(1−δ_n(σ)+ε) T^[1+d(1−σ)/(3−2σ)+ε],

for 1/2<σ<1, T>1 and N>1. N(σ,T,a) counts zeros, with multiplicity, of L(s,χ_a) in σ≤Re s≤1 and |Im s|≤T. The source defines its sum symbol immediately before (1.3): it means **n-th-power-free**, not squarefree. The ordering in the displayed corollary is the **label norm Na**, not the conductor norm. The source explicitly distinguishes these orderings in §1.2.

For n=3, K=Q(ω), σ=4/5 and d=2, the first branch of δ_n gives δ_3=(2σ−1)/(4+3(1−2σ))=3/11. Therefore the statement is

    Σ_{a cubefree, Na≤N} N(4/5,T,a)
       ≪ N^(8/11+ε) T^(9/7+ε).                             (1)

This includes every squarefree label with Na≤N and, by positivity, every fixed ray-sector subfamily of those labels. For a squarefree good a, the primitive conductor is c_a a with c_a supported on fixed S, so its norm is comparable to Na by constants depending only on fixed data. Consequently (1) gives exponent 8/11 for the squarefree-label subfamily ordered by conductor, including the usual fixed principal-ray cubic family. At finite S, deleting Euler factors does not introduce zeros with Re s>0, so the zero count in the corollary's strip agrees with that of the inducing primitive character.

The same exponent **does not follow directly for all cubefree labels ordered by conductor**. Write a=u v² with u,v squarefree and coprime. The good part of the primitive conductor is u v, whereas the label norm is Nu·(Nv)². For example, if u=1 and Nv≈X, then conductor ≍X but label norm ≍X². Simply applying (1) to the entire conductor≤X family takes N≪X² and yields the weaker X^(16/11+ε) T^(9/7+ε) bound.

For the general fixed K,S family, the source’s §2.5.1 equation (2.4) makes χ_g multiplicative in its integral-ideal label, including the zero masks. Since its values lie in μ₃, χ_{u v²} is the complex conjugate of χ_{u² v} on all integral ideals; both vanish at exactly the same forbidden primes. The literal Eisenstein family of Example 2.2 is one example. For every pair, select the smaller of these two cubefree labels. If Nu·Nv≤X, the selected label norm is at most X^(3/2). Each selected label has at most two preimages; complex conjugation reflects zero ordinates, preserving the count in |Im s|≤T. Thus (1) implies for the full conductor-ordered family at σ=4/5 only

    Σ_{a cubefree, Ncond(χ_a)≤X} N(4/5,T,a)
       ≪ X^(12/11+ε) T^(9/7+ε).                            (2)

The 12/11 exponent comes from (3/2)·(8/11); it is weaker in the X-aspect than the elementary X^(1+ε) family-size estimate together with standard per-function zero counting at fixed height. The reordering bound (2) does not establish an X^(8/11) conductor-aspect density estimate. The label conjugation in (2) needs no extra fixed twist because (2.4) includes the imprimitive zero extensions. An independently imposed fixed external twist is different: conjugating zeros also conjugates that twist, and Corollary 1.5 does not itself assert a bound for arbitrary external twists.

Theorem 1.2 of the same paper **does** use conductor ordering, but it is a central second-moment theorem, not Corollary 1.5's zero-density result. A squarefree-label result or a conductor-ordered central moment should not be silently substituted for the full conductor-ordered zero count.
