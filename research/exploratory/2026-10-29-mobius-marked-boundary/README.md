# Exact Möbius factorization extends the sixth-power marked obstruction

**Status:** Proposed exact spectral-growth identity for the sixth-power row subfamily, with a conditional implication and unconditional failure criterion for a broad all-element-row mixed moment. Two independent reviewers checked the upper bound and source scope. This is not a zero-free theorem and does not contradict the stated OpenAI marked-moment range. It uses unrestricted rows including sixth powers, not just the physical sixth-free rows. No priority claim is made.

Let K=Q(√−3), fix a finite prime set S including primes above 6, and write `ζ_(K,S)` for the S-deleted Dedekind zeta function. Put

    Θ = sup {Re ρ : ζ_K(ρ)=0, 0<Re ρ<1} ∈ [1/2,1].

Fix exponents `m,r>0` and `z≥0`; when z=0 use the empty slot product Q=1. There is one fixed nonnegative C∞ compact-annular profile W, independent of Z and of the zeros of ζ_K, with the following property. For z>0 use all good primes in a fixed annulus at scale `Z^z`, with a fixed nonnegative slot profile positive on a subannulus and coefficients identically 1. With this choice, or Q=1 if z=0, the corresponding marked inverse moment over all element rows of norm `≪Z^m` has

    limsup_(Z→∞) log(moment)/log Z ≥ m/6+z+2r(Θ−1/2).     (1)

The inverse length is `Z^r`, with the usual inverse normalization `Z^(−r/2)` and Möbius coefficients, and the slot has normalization `Z^(−z/2)`. The slot and inverse use the common zero-extended sextic symbol and trivial fixed ray character. Thus if a source theorem asserts the upper bound `O_ε(Z^(m+ε))` for every ε>0 for this fixed W and all admissible prime coefficients, it forces

    Θ ≤ 1/2 + (5m/6−z)/(2r).                               (2)

In particular, since Θ≥1/2, the asserted upper bound is impossible whenever `z>5m/6`, for **every** fixed r>0. The earlier [positive-inverse obstruction](../2026-10-29-positive-inverse-obstruction/README.md) established that unconditional criterion only for `r<m/3`; the exact factorization below removes that restriction. Relation (2) gives no improvement when its right side is at least 1, and no unconditional zero-free region follows from it.

## The fixed profile and uniform inverse bound

The [compact-annular construction](../2026-10-29-cubic-full-inverse-mean/README.md) supplies a fixed W≥0 supported in a compact subinterval of `(0,∞)` such that its Mellin transform `Ŵ(s)` is entire, rapidly decreasing in vertical strips, and has no zeros off the imaginary axis. Therefore `Ŵ(ρ)≠0` at every nontrivial zero ρ.

Set

    S_W(X) = Σ_{(n,S)=1} μ_K(n) W(Nn/X).

For `Re s>1`, its Mellin transform is `Ŵ(s)/ζ_(K,S)(s)`. For each nontrivial zero `ρ=β+iγ`, the finite Euler factors at S are nonzero at ρ. Therefore the transform has a pole at ρ, and the Mellin Ω argument gives, for each η>0, an unbounded sequence X with

    |S_W(X)| ≥ X^(β−η).                                    (3)

For every fixed a>Θ, if Θ<1 and a<1, zero-freeness on `Re s≥a` and the fixed-field Hecke zeta estimates imply

    |S_W(T)| ≪_(a,W,S) T^a                                  (4)

uniformly for all T>0. One uses Mellin inversion on `Re s=a`; a standard polynomial vertical bound on `1/ζ_(K,S)(a+it)` follows from the zero-free half-plane with a fixed margin and the finite-order zeta bounds: apply Borel–Carathéodory to a holomorphic logarithm on zero-free discs centered on a fixed line to the right of 1, where the Euler product bounds the reciprocal, and use the polynomial zeta growth on the outer discs. Treat bounded heights separately; the pole at 1 is removable for the reciprocal. The transform `Ŵ` is rapidly decreasing. For small T the sum vanishes once its compact annulus lies below norm 1, while on a fixed compact interval it is bounded. If Θ=1, elementary ideal counting gives (4) with a=1. The only possible pole of ζ_K at 1 is a zero, not a pole, of its reciprocal. The case `Θ<1` is conditional on this standard fixed-strip reciprocal bound; it is not an assumption that RH holds.

## Exact treatment of the sixth-power row masks

For a prime ideal v outside S let

    S_(W,v)(X) = Σ_{(n,Sv)=1} μ_K(n) W(Nn/X).

Möbius multiplicativity and `μ(v)=-1` give the exact identity

    S_W(X) = S_(W,v)(X) − S_(W,v)(X/Nv),
    S_(W,v)(X) = Σ_(j≥0) S_W(X/(Nv)^j).                    (5)

The sum is finite because W is annular. Thus (4) gives, uniformly for all Nv≥2,

    |S_(W,v)(X)−S_W(X)| ≪ X^a (Nv)^(−a).                  (6)

This retains the original zero mask and replaces the previous trivial count `O(X/Nv)` by the exact zero-free-half-plane estimate. It is valid for any fixed ratio between the inverse length and the row scale.

Put `U=Z^m`, `X=Z^r`. Choose prime ideals v with `Nv≈U^(1/6)` in a fixed small annulus, outside S and, when z>0, disjoint from the prime slot support. At equal exponents z=m/6, choose disjoint fixed proportional annuli; otherwise the polynomial scales separate automatically. Choose a generator v and the row `u=v^6`. There are `≫U^(1/6)/log U` such distinct rows, and `Nu≪U`. For z>0, every slot prime is coprime to v, so the sixth-power character is 1 on the slot. A fixed nonnegative slot profile positive on a subannulus and coefficients identically 1 yield a slot magnitude `≫Z^(z/2)/log Z` by the prime ideal theorem. If z=0 the empty product is exactly 1. The inverse equals `X^(−1/2) S_(W,v)(X)` exactly.

Fix an arbitrary small δ>0. Choose a nontrivial zero with `β>Θ−δ`, and take a in (4) arbitrarily close to Θ (or a=1 if Θ=1). The correction in (6), with `Nv≈X^(m/(6r))`, is `O(X^(a−am/(6r)))`. Choosing δ and `a−Θ` small enough, then η>0 small, makes `a−am/(6r)<β−η`. Along the Ω-sequence (3) and with `Z=X^(1/r)`, all chosen rows therefore satisfy

    |X^(−1/2) S_(W,v)(X)| ≫ X^(β−1/2−η).

Squaring and summing over the v rows yields

    moment ≫ Z^[m/6+z+2r(β−1/2−η)]/(log Z)^2

along that sequence. Since β can approach Θ and η can be arbitrarily small, (1) follows. The unbounded sequences can depend on the selected β; the fixed W, S, slot profile and exponents do not. □

The criterion concerns the unrestricted all-element moment and arbitrarily chosen bounded prime-slot coefficients. It does not assert that sixth-power rows satisfy the detector-zero witness, nor that the physical prime-slot selected operator exceeds its intended bound. It gives no contradiction in the source detector's parameter region unless the right-hand side of (2) becomes a nontrivial new zero-free statement.

## Exact logarithmic growth on the sixth-power sector

The lower bound in (1) is sharp for the sixth-power rows themselves. Let `H(Z)` be the supremum over all slot coefficient choices `|a_p|≤1` of the marked moment restricted to the distinct rows `u=v^6` with `Nv≪Z^(m/6)`, choosing one generator per integral ideal v. The Eisenstein field has class number one; two generators differ by a sixth root of unity, so their sixth powers are identical and different ideals give distinct rows. Arbitrary prime valuations in v are allowed: the source zero mask depends only on rad(v). Use the same inverse W, fixed slot profile and bad set as above; for z=0 take Q=1. Then

    limsup_(Z→∞) log H(Z)/log Z = m/6+z+2r(Θ−1/2).         (7)

The lower bound is already proved, with prime v and coefficients equal to 1. For the upper bound, suppose `Θ<1` and choose `a>Θ`. For any ideal v the masked inverse has Mellin transform

    Ŵ(s)/ζ_(K,S)(s) · ∏_(p|v, p∉S) (1−Np^(−s))^(−1).

On `Re s=a`, the variable product is uniformly `≪_(a,e) (Nv)^e` for every fixed e>0: for sufficiently large primes each local factor is at most `(Np)^e`, and the finitely many smaller primes contribute a fixed constant. The same fixed-strip reciprocal-ζ bound and Mellin decay give

    |S_(W,v)(X)| ≪_(a,e,W,S) X^a (Nv)^e.

If `Θ=1`, the trivial ideal count gives `|S_(W,v)(X)|≪X`, uniformly in v. There are `≪Z^(m/6)` ideal labels v, and for z>0 the prime number bound and `|a_p|≤1` give `|Q|²≪Z^z`; for z=0, `Q=1`. Incorporating `X^(−1/2)` and arbitrarily small power losses yields the matching upper limsup. As `a↓Θ`, (7) follows. The supremum is used only for the uniform upper statement; the exhibited all-one slot already supplies the lower limsup. This identity characterizes a special row sector, not the entire marked moment or the physical sixth-free detector.

## A consistency consequence for the published marked-moment range

The stated OpenAI Lemma 17.1 permits the empty slot `z=0` and each fixed `r<m`. If that lemma holds as stated for the unrestricted element rows and this W, then (2) gives `Θ≤1/2+5m/(12r)` for each `r<m`. Sending r upward to m yields the conditional conclusion `Θ≤11/12` for the Eisenstein zeta function. Since `ζ_K(s)=ζ(s)L(s,χ_{−3})`, this also excludes Riemann ζ zeros with real part greater than 11/12. The same conclusion follows with a positive z tending to zero and strict source margins.

This is weaker than the paper's separately claimed zero-free boundary and is not a new record. It quantifies how much base-field zero-free information is already encoded in that stated inverse-moment input. Moreover, using only this sixth-power-row mechanism with the stated constraint `r+2z<m`, one cannot obtain a better boundary than 11/12: for `z≥0`,

    (5m/6−z)/r ≥ (5m/6−z)/(m−2z) ≥ 5/6.

This last comparison limits the present lower-bound argument, not the moment theorem or any other proof method. The source lemma and the reciprocal-ζ contour bound remain explicit dependencies.

**Independent review:** Families and High_match independently checked the deletion identity, fixed-profile choice, near-supremum zero and tail comparison, variable-Euler-factor upper bound, exact limsup and unrestricted-row scope, subject to the standard reciprocal-ζ bound on a fixed zero-free line. High_match checked that the cited source permits empty slots and fixed r<m.
