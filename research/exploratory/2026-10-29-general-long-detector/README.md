# A fixed-field long detector and common-profile reduction

**Status.** This is a source-qualified analytic proof, generalized from the separately reviewed [short-detector packet](../2026-10-29-cubic-short-detector-proof/README.md). The inputs are the standard analytic continuation, Euler product and functional equation for primitive finite-order Hecke characters over a fixed field, standard fixed-strip growth and individual zero counting, and the explicit conductor and Euler-mask identities stated below. The final family-density theorem additionally uses de Faveri's printed large sieve and the family identification. This note does not independently establish those external facts, the Lean candidate's conventional interpretation, or an individual zero-free region.

## Statement

Fix a number field K, a finite set S of finite places, and constants C₀ and a fixed infinity type. Let ψ range over presentations on ideals whose primitive inducing characters ξ are unitary and nonprincipal, with finite conductor norm and original deleted radical at most C₀X. Assume ψ equals ξ times the zero masks at those deleted primes, and that the corresponding Dirichlet series and functional equations have the usual Hecke interpretation. Fixed finitely many norm-character or principal exceptions can be treated by their individual zero counts. Fix `1/2<σ<1`, `1<t<3/2`, and ε>0.

For each sufficiently large X and each row with a primitive zero of real part at least σ and height at most `X^τ`, the following holds for sufficiently small fixed τ>0. The row has one of finitely many bins a, a zero `ρ=β+iγ` of one of ψ or its conjugate, two dyadic scales `D=X^r` and `N=X^m`, and one common frequency h, such that

    0≤r≤t+O(1/log X),  0≤m≤1/2+ε,
    r+m≥t−O(1/log X),  a≥σ−ε,
    |M_r(β,h)|² ≳ X^((2a−1)r−ε),
    |S_m(β,h)|² ≳ X^((2a−1)m−ε).                              (1)

Here, using good ideals and their original zero masks,

    M_r(β,h)=D^(−1/2) Σ_l μ_K(l)ψ(l) W_M(Nl/D)(Nl/D)^(−β−ih),
    S_m(β,h)=N^(−1/2) Σ_k ψ(k) W_S(Nk/N)(Nk/N)^(−β−ih).       (2)

The profiles have fixed compact positive annular support and uniform smooth seminorms. They are common within a fixed dyadic/bin/presentation class: their only row-varying real parameters are β,h, with `|h|≪X^τ`. Polynomially many logarithmic dyadic choices and finitely many bins are allowed. The displayed O and ε losses are selected in advance: in an application first fix the desired final loss, then choose bin and contour losses, profile derivative orders and finally τ.

## Buffer and normalized pointwise bounds

Take `1/2<σ_f<σ` and a small fixed e>0. Set `T=X^τ`. For each row take nested maxima of real parts of zeros of both ξ and its conjugate above σ_f at heights `3jT`, for a fixed number O(1/e) of j. Since these maxima lie in `[σ_f,1]`, some consecutive increment is ≤e. A grid rounding gives a bin a and a zero of one presentation with `a≤β<a+e`, `a≥σ−e`, such that both presentations are zero-free in `Re s>a+2e` in the next, slightly larger height window. This selection controls existence of a bad row; an individual zero count at height `O(T)` converts a row bound to a zero count, at an extra `X^τ log X` cost.

Euler convergence anchors `log L(2+iv,ξ)` and bounds it on a fixed small disk. Standard fixed-strip growth controls its real part on a larger disk contained in the zero-free rectangle. Borel–Carathéodory followed by Hadamard three-circles yields, uniformly after fixing e,

    |L_orig(s,ψ)| + |L_orig(s,ψ)|^(−1) ≪ X^η
    (Re s≥a+6e, |Im s|≤C_e T),                               (3)

for every prescribed fixed η>0, after τ is chosen sufficiently small. The disk radii and proof are written explicitly in the [buffer derivation](../2026-10-29-cubic-short-detector-proof/README.md). The Euler deletion product has no zeros in Re s>0 and, because its radical has norm O(X), both it and its reciprocal are `≪X^η` on every fixed half-plane Re s≥b>0. To see this, separate finitely many small primes and use `Σ_{p|R}(Np)^(−b)≪_{b,η}η log NR+O(1)`.

The functional equation for ξ, (3) for the conjugate and the original deletion factors give on `Re s=1−a−6e` the bound

    |L_orig(s,ψ)| ≪ X^(a−1/2+12e+η)(1+T)^C,                  (4)

with C fixed by K and the infinity type. Mellin inversion of each fixed annular profile, partial contour shifts inside the buffer, and rapid decay on the remaining frequency tails then imply, uniformly for the allowed h and bounded r,m,

    |M_r|² ≪ X^((2a−1)r+O(e+η+τ)),
    |S_m|² ≪ X^((2a−1)min(m,1−m)+O(e+η+τ)).                (5)

The second estimate uses the direct line when m≤1/2 and the reflected line (4) when m≥1/2. The explicit normalized variable `(Nq/D)^(−β−ih)` in (2) is essential. The external Mellin-tail differentiation order is chosen after the fixed small τ, so the tails are negligible even though the absolute-line bounds may have polynomial X-growth.

## Gamma convolution and simultaneous witnesses

Take a smooth V₀ equal to 1 near [0,1] and vanishing past a fixed larger point, set `D*=X^t`, and choose a fixed large B. Define the finite inverse

    Cψ(s)=Σ_l μ_K(l)ψ(l)V₀(Nl/D*)(Nl)^(−s)

and integrate `X^(Bz) Γ(z)L_orig(ρ+z,ψ) Cψ(ρ+z)` on Re z=2. Shift to Re z=−1/4. The only crossed Γ pole is at z=0, and its residue vanishes because `L_orig(ρ,ψ)=0`. The shifted integral is o(1) for B large in terms of t and fixed field data, with τ then sufficiently small. On the original line the Euler/Möbius identity makes the coefficient of every nonunit ideal j with `Nj≤D*` vanish; the unit coefficient tends to 1. Insert a smooth product cutoff vanishing there and use the Γ exponential to truncate the outer product at a fixed polynomial in X, with o(1) error.

Dyadically separate l and k. The number of pairs is `O(log²X)`, their lengths obey `r≤t+O(1/log X)` and `r+m≥t−O(1/log X)`, and their product weight has uniformly bounded logarithmic derivatives on the fixed product annulus. Fourier inversion in `log((Nl/D)(Nk/N))` separates it into the two common profiles with one shared frequency. The Fourier tail outside a small fixed fraction of T is negligible by an arbitrarily high fixed derivative order. One pair and one frequency therefore satisfy

    |M_r S_m|² ≳ X^((2a−1)(r+m)−O(e+η)) .                   (6)

Combine (6) with both bounds (5). Since `2a−1` is uniformly positive, the plain upper bound forces `m≤1/2+ε`, and division by the opposite factor's upper bound gives the two separate lower bounds in (1). This is valid for every fixed t in `(1,3/2)`; there is no short-t extension here.

## Row-varying profiles and Θₙ

For each fixed bin, dyadic pair, finite source presentation and reciprocity class, the profiles in (2) are common apart from `(β,h)` in a fixed bounded β interval and `|h|≪X^τ`. Cover this parameter region by `O(1+X^τ)` unit rectangles. The standard two-dimensional Sobolev inequality bounds the rowwise supremum on each rectangle by integrals of the profile and its first derivatives in each variable. Those derivatives insert only bounded powers of log of the annular argument. Hence the source coefficient vector is common across rows for every integration parameter, has the same support and has ℓ² mass bounded up to X^ε. The `X^τ` cover and zero-count losses are absorbed by selecting τ after all ε losses. This is the [explicit Sobolev interface](../2026-10-29-detector-profile-sobolev/README.md); no pointwise-only moment is being substituted for a row-varying supremum.

For the de Faveri family, the inverse source coefficients are squarefree, and so are admissible columns for the printed n-free Θₙ. For an ordinary block or its square, decompose the source ideal uniquely as `a=a₁v²` with a₁ squarefree. For fixed v, `ψ_u(v²)` is a row contraction, and the a₁ vector is common. The normalized squared coefficient mass is `≪X^ε/(Nv)²`, including divisor-bounded convolution and Sobolev derivatives. Minkowski and `Σ_{Nv≲X^C}(Nv)^(−1)≪log X` recover the same four-term Θₙ bound. Original masks are multiplicative and remain in this decomposition.

If the selected buffered zero belongs to the conjugate presentation, place it in a separate orientation group and conjugate the entire common coefficient vector before applying Θₙ. This leaves the operator norm and zero masks unchanged and does not require relabeling the conjugate character by an ideal of a different norm.

For the particular FHL n-free family, its primitive conductor and the radical of the deleted good primes are `≪rad(u)≤Nu≤X`, up to fixed S factors; all good u≠1 give nonprincipal primitive characters. Apply the detector to ψ and its conjugate, the printed Θₙ estimate to the common vectors, and the four-face calculation of the [direct density note](../2026-10-29-direct-nfree-density/README.md). This establishes that note's detector/profile interface from the named standard Hecke facts and the stated FHL identities. The family and sieve theorems are still source inputs; they are not proved here.

**Independent review.** High_match checked the buffer, Γ convolution and saturation, shared Fourier height budget, uniform cutoff derivatives, unit endpoints, fourth-moment square decomposition and row masks, and the Sobolev cover, conditional on the stated Hecke, FHL and Θₙ inputs.
