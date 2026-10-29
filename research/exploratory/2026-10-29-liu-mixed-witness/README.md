# A source-qualified mixed witness at one sextic scale

**Status.** This is a local mixed-moment deduction, conditional on [Liu v1, Theorem 12.14 and Remark 12.16](https://arxiv.org/html/2610.26835v1#S12.Thmtheorem14), [De Faveri v1, Theorem 1.1](https://arxiv.org/abs/2610.04045v1), and the finite-presentation matching below. Neither preprint's analytic proof is independently established here. It improves one scalar witness bound, not yet a complete zero-density theorem or zero-free region.

**Stronger source consequence.** The local gain calculated here is not a density record: Liu's own unmarked inverse and ordinary fourth moments give a stronger full sixth-free count at σ=4/5 by the separate calculation at the end of this note. The earlier paper states those inputs over Q(ω), and the cyclotomic version is also source-qualified. Their proofs and the detector bridge remain unverified inputs.

Fix a cyclotomic F containing μ₁₂, fixed good-prime data S, and a sextic FHL family over F. At σ=4/5 take

    r=30/37,  m=15/37,  D=X^r,  N=X^m,  r=2m.

For fixed common annular profiles and fixed unitary norm twists, define

    M_u=D^(−1/2) Σ_l μ_F(l)χ_u(l)W₁(Nl/D),
    S_u=N^(−1/2) Σ_k χ_u(k)W₂(Nk/N),

with original zero masks, and sum over good sixth-free FHL ideal labels `Nu≤X` whose primitive inducing character is nonprincipal. Provided the presentation bridge below and the two cited moment inputs hold uniformly,

    Σ_u |M_u S_u|² ≪ X^(149/111+ε)(1+H)^C,                  (1)

where H bounds the norm-twist heights and C depends only on the fixed source data and profile orders. This is a source-qualified comparison at one fixed scale; constants may depend on the fixed field, S and ε.

## Source matching

Liu fixes a cyclotomic field containing μ₁₂, enlarges S so the S-integer ring is principal, and uses exterior ideal norms. [Lemma 3.3](https://arxiv.org/html/2610.26835v1#S3.Thmtheorem3) states that each exterior fractional ideal has an allowed generator unique modulo sixth powers of S-units; allowed generators satisfy `χ_n(k)=χ_k(n)` with the source's zero conventions. For a sixth-free FHL ideal u choose its allowed generator k, whose exterior norm is Nu. Different ideal labels have different allowed-generator classes, so these selected rows inject into the source row set.

The [finite Kummer-phase comparison](../2026-10-29-general-field-collapsed-sieve/README.md), equations (3)–(5), identifies `χ_n(k)=η_u(n)χ_u(n)` with original nonunit zeros, where η_u ranges over a fixed finite group of Hecke characters unramified outside S. It uses a frozen FHL decomposition and one fixed sixth-root embedding; its source reciprocity and identification of the two papers' embeddings must be checked in an application. Partition rows by η_u and use the fixed source background `ν=η_u^(−1)` on each part. The chosen presentation is then exactly the FHL row, so its primitive inducing character is nonprincipal exactly when the FHL row is. The finite partition and subcollection cost only fixed constants. No growing row-dependent character is absorbed into ν.

In the source's **z=0**, q=0 basic presentation, Remark 12.16 explicitly gives the ordinary fourth moment

    Σ_{q_k≤X; ψ_k nonprincipal} |S_k(X^m)|⁴
       ≪ X^(1+ε)(1+H)^C,                                   (2)

for `0≤m≤1/2+r_F/100+ε`, fixed smooth profile families and finite profile seminorms. Thus m=15/37 is in range. The statement excludes principal inducing rows, permits fixed finite ν, and includes common masks and polynomial height costs. No prime-polynomial factor or κ-dependent zero-free hypothesis is invoked for this z=0 specialization. This is the printed source statement, not an independent verification of its centering induction. Its field hypothesis does **not** cover Q(ω), which lacks μ₁₂.

## Fourth inverse moment and arithmetic

Square M_u. Its product coefficients have divisor-bounded size. Writing each column ideal uniquely as `a=a₁v²`, with a₁ squarefree, fixing v and pulling the row-dependent factor `χ_u(v²)` out as a contraction retains every zero. De Faveri's arbitrary-coefficient sixth-free sieve and Minkowski yield

    Σ_u |M_u|⁴ ≪ X^ε Θ₆(X,D²),
    Θ₆(X,D²) ≪ X^ε[X+D²+X^(5/6)D^(2/3)
                                  +X^(1/3)D^(5/3)].          (3)

At r=30/37 the largest face is `1/3+(5/3)r=187/111`. Apply Cauchy–Schwarz to (2) and (3); the exponent is `(1+187/111)/2=149/111`, proving (1) under the inputs. The same fixed-profile derivatives have bounded normalized coefficient mass, so a common-parameter Sobolev step may be made with the source's polynomial height costs; its uniformity remains part of the input if detector profiles vary by row.

By contrast, applying Θ₆ directly to the convolution of the inverse and ordinary blocks, of total length `DN=X^(45/37)`, gives the largest face `1/3+(5/6)(45/37)=299/222`. The source-qualified mixed bound (1) is smaller by exactly `1/222`. At δ=2σ−1=3/5, simultaneous detector thresholds divide either mixed moment by `X^[δ(r+m)]=X^(27/37)`, so the scalar count exponent at this **one witness configuration** decreases from `137/222` to `68/111`. Fixed small-power and height losses must be smaller than this gap.

This calculation does not bound all other detector witness lengths, prove that zeros realize the chosen configuration, or by itself improve the global minimax. A complete application needs a uniform neighborhood of the scale, the remaining detector cases, source/profile matching and the stated number-field assumptions. The β/height factors must be retained in both moments rather than replaced by row-specific coefficient vectors.

## Stronger consequence of the source's unmarked inverse input

Over E=Q(ω), [Liu v2, Lemma 9.2 (9.3) and Lemma 9.3 (9.4)](https://arxiv.org/html/2610.12234v2#S9.SS2), state respectively, for sixth-free row elements u and the same fixed source character presentation,

    Σ_(Nu≈X) |M_u(X^r)|² ≪ X^[max{1,(1+5r)/6}+ε](1+H)^C,
    Σ_(0<Nu≪X; ψ_u nonprincipal)|S_u(X^m)|⁴
       ≪ X^(1+ε)(1+H)^C.                                   (4)

For the second estimate use `z_p=0`, so the printed statement allows arbitrary bounded ordinary lengths and excludes only principal inducing characters; no κ-dependent zero-free hypothesis for selected primes is used. The paper's bound includes unit associates and retains fixed ray twists, defining-modulus zeros, common profiles and polynomial height/seminorm costs. Its ordinary statement is for two **plain** factors, not an inverse–ordinary product. In the compatible primary FHL presentation discussed in [the sextic family review](../2026-10-29-cyclic-sextic-family/INDEPENDENT-REVIEW.md), every good sixth-free ideal has one primary generator and `χ_u(n)=(u/n)_6=χ_n(u)` with the original zero masks; a finite S-ray twist can be fixed before applying (4).

Assuming the uniform simultaneous-witness detector, fixed finite-sector/profile and zero-count transfers, set δ=3/5, `t=25/19` and `r_*=2t/3=50/57`. If a witness has r≤r_*, then `m≥t−r≥t/3`, and the second bound in (4) gives count exponent at most `1−2δt/3=9/19`. If `r_*≤r≤1`, the first bound gives `1−δr≤9/19`. If `1≤r≤t`, it gives `(1+5r)/6−δr≤9/19`. All actual m satisfying the detector constraints are covered. Fixed losses and polynomial heights are chosen small compared with the requested final ε. Thus these inputs imply a source-qualified `X^(9/19+ε)` sixth-free zero-density count at σ=4/5, stronger than the local four-face exponent 137/222 and the intermediate 181/298.

Liu explicitly records the unmarked `t=1` zero-class count `1−2δ/3` in [§10.2](https://arxiv.org/html/2610.12234v2#S10.SS2); at δ=3/5 its exponent 3/5 already improves on 181/298. Liu's [Proposition 2.7](https://arxiv.org/html/2610.26835v1#S2.Thmtheorem7) has additional available-prime-length and class hypotheses; the 9/19 argument above is a direct deduction from the two **unmarked** source moments and the separately supplied detector, not an assertion that those extra hypotheses can be omitted from Proposition 2.7.

To pass from dyadic `Nu≈U` estimates at height `U^τ₀` to all `Nu≤X` with the common height `X^τ`, choose a fixed `0<c<9/19`. Count labels `Nu≤X^c` trivially using fixed-field ideal and individual zero counts, choosing τ small enough that their total remains `O(X^(9/19+ε))`. For larger dyads take `τ<cτ₀` and sum O(log X) scales; choose all exponent and profile losses before τ. The preprint's analytic moments, FHL identification and all profile/height transfers remain source inputs; no independent all-height result follows.
