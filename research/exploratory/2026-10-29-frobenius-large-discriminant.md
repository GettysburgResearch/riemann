# Larger-height Frobenius transfer at large discriminant

**Status:** Proposed deduction from Zaman's published zero-free theorem and the cited Frobenius/low-order argument. The analytic inputs, this deduction, and publication priority have not been independently audited. The threshold below is nonexplicit. It is not an all-discriminant numerical theorem, and no global frontier claim is made; a recent unaudited fixed-half-plane claim would be stronger if valid.

Let `p` be an odd prime, let `r>=3` divide `p-1`, and write `g=gcd(2,r)`. Fix integers `n_M,n_E>=1`. Consider finite Galois extensions `K/k` with a subgroup `H=C_p⋊C_r` acting faithfully on `C_p`; put `M=K^H`, `E=K^(C_p)`, `F=K^(H²)` and `D=|disc(K/Q)|`. Assume `[M:Q]=n_M`, `[E:Q]=n_E` and `[F:Q]>=7`. Set

```text
C = min{ 0.1764(p-1), p*r/(g*11.51910) }.
```

For every `0<epsilon<C`, there is a **nonexplicit** threshold `D0`, depending on `p,r,n_M,n_E,epsilon` and on the fixed auxiliary function in Zaman's theorem, such that for `D>=D0`, in

```text
Re(s)>1-(C-epsilon)/log D,        |Im(s)|<=1,
```

every irreducible Artin factor of degree at least two and every nonreal one-dimensional factor is holomorphic and nonzero. At most one simple real zero can remain among the real one-dimensional factors. If `k=Q` and the Galois group has no quotient of order two, `zeta_K` is zero-free there apart from its pole at 1.

Fixing the group and `[k:Q]` is a sufficient way to fix the intermediate degrees. Fixing just `p,r,[k:Q]` is not enough if the ambient group is allowed to vary.

## Derivation and nonexplicit threshold

The factorization and conductor bounds in the [composite-complement note](2026-10-29-frobenius-transfer/README.md) imply

```text
zeta_K/zeta_F = product_(ord omega>2) L_M(s,omega)
                * product_([lambda]) L_E(s,lambda)^r,
log(d_E Nf_lambda) = log(D/d_E)/(p-1) <= log D/(p-1),
log(d_M Nf_omega) <= log D/[p phi(r)].
```

Here each `lambda` has order `p>=7`; the `omega` are powers of a character `omega_0` of order `r`, and every conductor divides `f_omega0`. The second conductor inequality applies in particular to `omega_0`. Each character is interpreted on the appropriate narrow ray class group; replacing the primitive Euler product by the imprimitive ray-class one adds only factors nonzero for `Re(s)>0`.

Zaman's [Theorem 1.1](https://arxiv.org/html/1502.05679) supplies a `|t|<=1` rectangle for a product of characters with order at least `a`, with coefficient `.1764` for `a=6` and `.1227` for `a=3`, over the denominator

```text
log d_T + (3/4)log Nq + [T:Q] nu([T:Q]).
```

Any sole exceptional zero is associated to a **real** character; the products restricted to order at least three therefore have none. For the order-`p` factors, use modulus `f_lambda` over `E` and `a=6`. The denominator is at most `log D/(p-1)+n_E nu(n_E)`. The parameter `d_E Nf_lambda` tends to infinity uniformly with `D`, because `d_E^p<=D` gives `d_E Nf_lambda >= D^(1/p)`. Therefore Zaman's sufficiently-large hypothesis eventually holds uniformly in this fixed-degree family.

For the complement characters use the common modulus `f_omega0` over `M` and `a=3`. When its `d_M Nf_omega0` exceeds the nonexplicit Zaman threshold, the denominator is at most `log D/[p phi(r)]+n_M nu(n_M)`. When that quantity stays below the threshold, Hermite–Minkowski gives finitely many fields `M` of fixed degree and bounded discriminant, and each has finitely many integral ideals and finite-order primitive Hecke characters with bounded finite conductor. Classical nonvanishing of nontrivial Hecke L-functions on `Re(s)=1` and compactness of `|t|<=1` therefore give a positive zero-free width uniformly over this finite collection. This nonexplicit fixed width contains the proposed shrinking width once `D` is large enough. This split is needed: the complement modulus need not tend to infinity as `D` grows. Ahn–Kwon's quoted `.13`-height theorem alone cannot handle the full `|t|<=1` interval. All powers preserve their order on the common narrow ray group.

Since `phi(r)>=2`, the complement coefficient `.1227*p*phi(r)` is at least `.2454p`, exceeding `.1764(p-1)`. The fixed degree-dependent additions in both denominators are absorbed by the strict `epsilon` when `D` is sufficiently large. The factorization then gives `ord zeta_K=ord zeta_F` away from 1 in this region. The Das et al. low-order theorem applies because `d_F^(pr/g)<=D` and the stated coefficient does not exceed `pr/(g*11.51910)`; its possible real zero is simple by the separate Ahn–Kwon low-height Dedekind result. Stark's theorem and conjugation yield the stated Artin conclusion. At `s=1`, use the classical nonvanishing of nontrivial Artin factors. Over `Q`, the remaining trivial factor is zero-free at `|t|<=1` and `Re(s)>1/2` by the cited partial-RH verification and the real-axis sign; the region lies there for sufficiently large `D`.

## Infinite family

For `G=PSL_2(F_p)` and any fixed prime `p>=7`, a Borel subgroup has `H=C_p⋊C_((p-1)/2)`. Its `H²` fixed field has degree `p+1` if `p≡3 mod 4`, and `2(p+1)` if `p≡1 mod 4`, both at least seven. The Das coefficient exceeds `.1764(p-1)` for this family. Thus, for fixed `p` and fixed base degree, the proposed large-discriminant deduction gives width `(.1764(p-1)-epsilon)/log D` for `|t|<=1`, compared with the earlier all-field `.1149(p-1)/log D` for `|t|<=.13`. Over `Q`, `PSL_2(F_p)` is simple and there is no exceptional factor. [Zywina, Theorem 1.1](https://pi.math.cornell.edu/~zywina/papers/PSL2Galois.pdf), proves such Galois groups occur over `Q` for every prime `p>=5`; this establishes nonvacuity of the group family, not that each fixed group has infinitely many fields above the unspecified threshold.

## Elementary abelian kernels with cyclic quotient

The same reasoning extends to any `H` with a normal elementary abelian subgroup `N` of order `P=p^f`, `p` odd, and cyclic quotient `H/N` of order `r>=3`. A splitting and fixed-point-free action are **not** required. Let `t` be the minimum orbit size of `H/N` on the projective lines of the character group `N^`. More generally, one may instead take the minimum orbit size of `N_G(N)/N`: its action also preserves the absolute conductor norms used below. Put `w=(p-1)max{t,p^(f-1)}`. With `M=K^H`, `E=K^N`, `F=K^(H²)` and `g=gcd(2,r)`, assume `[F:Q]>=7`.

For this subgroup, the all-discriminant coefficient obtainable from the explicit low-height inputs is

```text
C_exp = min{ a_p w, P phi(r)/15.10, P r/(g*11.51910) },
a_p = 1/15.10 if p=3, and 0.1149 if p>=5,
```

at `|Im(s)|<=.13`. For fixed `p,f,r,n_M,n_E` and `t`, and every `0<epsilon<C_asym`, sufficiently large `D` also gives the same Artin conclusions and the same conditional Dedekind conclusion at `|Im(s)|<=1`, with the nonexplicit-onset coefficient

```text
C_asym-epsilon,
C_asym = min{ b_p w, .1227 P phi(r), P r/(g*11.51910) },
b_p = .1227 if p=3, .1489 if p=5, and .1764 if p>=7.
```

The minimum `t` can equivalently be bounded uniformly below across a family. The nonexplicit threshold can be chosen uniformly when the displayed degrees and group parameters are fixed; it is sufficient to fix the ambient group and base degree.

To check the new conductor input, let `lambda` be a nontrivial character of `N`. Scalar powering by `F_p^×` preserves its conductor, and conjugation by the normalizer of `N` transports its conductor by an automorphism of `E`, preserving its absolute norm. Consequently its joint orbit under scalar powering and the chosen normalizer action consists of `(p-1)t_lambda` characters with a common value `A_lambda=d_E Nf_lambda`. The conductor-discriminant formula counts those characters separately and yields

```text
log A_lambda <= log D/[(p-1)t_lambda] <= log D/[(p-1)t].
```

Independently, `L_lambda=K^(ker lambda)` has degree `p` over `E`, and its `p-1` nontrivial characters all share the conductor of `lambda`. Hence `d_Llambda=d_E A_lambda^(p-1)` and the tower relation `D>=d_Llambda^(P/p)` gives `log A_lambda<=log D/[p^(f-1)(p-1)]`. Taking the better of this and the orbit inequality gives `log A_lambda<=log D/w`; the two counts are not multiplied.

The `omega` and `F` estimates become `log A_omega<=log D/[P phi(r)]` and `log d_F<=log D/(P r/g)`. The subgroup `H²` contains `N` because `N` has odd order, and `H/H²` is the part of `H/N` of order at most two. Two abelian tower factorizations, without any Frobenius character theory, give

```text
zeta_K/zeta_F = product_(ord omega>2) L_M(s,omega)
                * product_(lambda != 1 in N^) L_E(s,lambda).
```

Indeed, first factor `zeta_K/zeta_E` for the abelian extension `K/E`, and separately factor `zeta_E/zeta_F` using the cyclic extension `E/M`. Every factor is nonreal, so the same low-order argument applies.

Unlike the prime-kernel case, an individual `A_lambda` need not grow with `D`. For **both** lambda and omega inputs use the threshold split already described above: apply Zaman for sufficiently large parameters, and the finite-family, line-nonvanishing and compactness argument for parameters below the fixed threshold. Fixed degrees make the latter lower width uniform at `|t|<=1`; choosing `D` sufficiently large absorbs the finite constants. This establishes the deductions conditional on the cited source theorems and the standard induction/conductor identities, not an independently verified analytic theorem.

For a scalar complement of order `r` in `F_(p^f)^×`, every projective orbit has size `t=r/gcd(r,p-1)`. In particular a Borel subgroup of `PSL_2(F_27)` has `p=3`, `f=3`, `P=27`, `r=13`, `t=13`, and `[F:Q]=28` over `Q`. The coefficients are `26/15.10≈1.72185` in the explicit `.13`-height result and `3.1902-epsilon` in the nonexplicit-onset height-one refinement. The ambient group is simple, so the Dedekind statement has no quadratic exception. [Zywina's modular-forms theorem](https://doi.org/10.4153/S0008439522000534) realizes `PSL_2(F_(p^3))` over `Q` for the indicated congruence classes, including `p=3`; as above, this does not by itself establish an infinite fixed-group family beyond the onset.
