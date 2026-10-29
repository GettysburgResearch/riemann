# Uniform subconvexity for the moving twist Gram matrix

Han Wu, [*Burgess-like subconvexity for GL(1)*, Theorem 1.1](https://doi.org/10.1112/S0010437X19007309), Compositio Math. 155 (2019), proves for every number field K and every varying unitary Hecke character χ

    L(1/2,χ) ≪_{K,ε} C(χ)^(1/4−(1−2θ)/16+ε),

where C is the **analytic** conductor and θ is an admissible Ramanujan exponent over K. The theorem does not require prime, squarefree, or cube-free conductor. With the standard θ=7/64, the displayed exponent is

    α = 103/512 = 0.201171875 < 1/4.

The frequently cited exponent 3/16 would follow from θ=0 in this theorem, but that is not the unconditional statement being used here. For K=Q(ω), fixed infinity type and arithmetic conductor norm Q, twisting by |·|^{it} gives C ≍_K Q(1+|t|)², and hence

    L(1/2+it,χ) ≪_{K,ε} Q^(α+ε)(1+|t|)^C

for a fixed exponent C. The bound remains uniform over arbitrary composite Q, fixed finite ray twists and primitive inducing characters; the latter description is useful when a presentation is imprimitive. Euler factors deleted at finitely many fixed primes, or moving prime factors at which the original character is zero, must be retained and contribute at most an absorbed Q^ε on the Mellin line described below.

For distinct good prime ideals p,q of norms ≍H, the sextic reciprocity character ξ_{p,q} in the [growing-rank note](2026-10-29-gauss-growing-rank/README.md) has conductor norm ≪_S (Np)(Nq) ≪ H², is nonprincipal at p, and has fixed infinity type. For its smoothed squarefree sum, shift the Mellin transform of L_K(s,ξ)/L_K(2s,ξ²), after expanding the fixed S-ray condition, to Re s=1/2+η. Wu's hybrid bound and Phragmén–Lindelöf give, with arbitrary small power losses,

    |⟨b_p,b_q⟩| ≪ Y^(−1/2+ε) H^(2α+ε)
                   = Y^(−1/2+ε) H^(103/256+ε).

The denominator has an absolutely convergent reciprocal Euler product there, and the smooth Mellin transform controls the polynomial height factor. Since J≪H primes are used, the Gram matrix tends to the identity in operator norm whenever

    H^(1+2α) ≪ Y^(1/2−ε),
    H ≤ Y^(128/359−δ),       128/359 ≈ 0.356546,

for any fixed δ>0 after choosing all auxiliary powers small enough. The corresponding bound using convexity α=1/4 allows H≤Y^(1/3−δ).

**This does not enlarge the present eigenvalue result.** Its separate Xu–Sang error term O(Y^ε P) forces the Gauss input's uniform lower bound to the more restrictive range P≤Y^(1/7−δ). Better Gram conditioning would matter only if the individual-twist Gauss moment were extended and controlled uniformly at larger P, or in another construction with a weaker moment constraint. No such extension follows from Wu's theorem.

**Other apparently stronger results have different scopes.** Balkanova–Frolenkov–Wu, [arXiv:2108.12283v5](https://arxiv.org/abs/2108.12283v5), treat cube-free characters over totally real fields; Q(ω) is not totally real. Petrow–Young, [*The Weyl bound for Dirichlet L-functions of cube-free conductor*](https://doi.org/10.4007/annals.2020.192.2.3), concerns Dirichlet characters over Q, not an arbitrary sextic Hecke character over Q(ω). Aggarwal, [arXiv:1712.00363](https://arxiv.org/abs/1712.00363), assumes a split-prime conductor and gives a stated hybrid bound in the range p≪t; it does not cover the composite p q and bounded t required by this Gram estimate. The search does not establish that Wu's bound is optimal.
