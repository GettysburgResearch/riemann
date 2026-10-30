# The theta off-diagonal returns the same long-inverse scale

**Status.** This is a bookkeeping identity inside source upper-bound arguments, not a proof of an inverse moment or a zero-free region. It compares the schematic first Poisson passage in the [OpenAI October 5 manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex) with the stated §10 proof of [rStation paper 5 v3](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3). These sources and their imported analytic inputs have not been independently verified here. The exact physical expression retains gcds, masks, sectors and a nonfactorized kernel, so the comparison does not identify an individual physical term with the simplified theta family.

Let the primal all-row normalized inverse moment have row scale Y and source length D:

    I(Y,D)=Σ_{0<Nu≤Y} |D^(−1/2)Σ_n μ(n)ν(n)χ_n(u)W(Nn/D)|².

After the schematic row Poisson step, the dual theta row scale is H=D²/Y, with the squarefree theta column scale still D. The source θ polynomial is P_h(D)=B_h(D)/√D, and the October 5 outline's raw comparison becomes schematically

    I(Y,D) ≲ Y + (Y/D) Σ_{Nh≲H}|P_h(D)|²,                  (1)

before restoring the suppressed coupled gcd and weight structure. Separating the θ diagonal and the signed Fourier weight may cancel its main mass, as in [the signed-theta model](2026-10-29-signed-theta-mass-cancellation.md); this is only a separated model.

Consider instead the paper 5 §10 **off-diagonal estimate** for the θ norm. Its j=0 Gauss/μ coefficient identifies with the ℓ=−1 theta coefficient up to a fixed finite ray phase, so its inverse factors have the original Möbius shape, with conjugate orientations and fixed ray characters retained. Take its label F=1 and examine its unit-gcd, unit-projector block G=S₁=1. Its displayed scale relations are

    T₀=D²/H=Y,       Y_src=D/(G S₁)=D.

Thus the two inverse factors inside the Cauchy estimate are precisely at row scale Y and inverse length D; the original zero masks and fixed phases remain present. Its (10.10) and (10.11), using the all-row input (10.2), bound this block by

    (H/D) [Y + Y^(1/6)D^(5/6)] (YD)^ε.                     (2)

The baseline on the right is the same function of the same original scales as the input I(Y,D). On returning through the prefactor in (1),

    (Y/D)·(H/D)=YH/D²=1,

so (2) gives, at the level of these positive majorants,

    Y + Y^(1/6)D^(5/6),

exactly the original amplification benchmark up to small powers. For D=Y^(6/5), this is Y^(7/6+ε). The desired inverse norm is Y^(1+ε); the corresponding θ off-diagonal target in this schematic pipeline is

    (H/D)Y = D,

rather than the available D^(41/36) bound (because H=D^(7/6)).

This is **not** an equality of the full signed physical moment with I(Y,D), nor proof that I actually attains its upper bound. It identifies a unit-scale, unit-gcd branch where the source's positive-Cauchy proof invokes the original inverse-moment problem again, with no reduction of either relevant scale. No contraction constant less than one follows from an unspecified ≪ constant; the Cauchy bound has also discarded phases that might enable cancellation. Paper 5's subsequent cube-completion argument proves a row-size **upper** bound for its θ norm, but at H>D it is O(H), which is larger than the desired signed off-diagonal O(D).

Branches with G S₁>1 do shorten the daughter source length to D/(G S₁), and restricted frequency shells can shorten the inverse row scale. They do not remove the G=S₁=1, T₀=Y branch. A valid improvement would need a new signed estimate, an actual common-factor/row restriction that reduces the unit branch, or a proved recursive inequality with genuine contraction and all tails controlled. The existing source bounds as printed do not supply any of these. In particular an O(Y^(1+ε)) bound for the full same-scale inverse input at D=Y^(6/5) is exactly the previously identified hard target and would imply ζ_{Q(ω)}(s)≠0 for Re s>61/72 by the power-row identity; no such conclusion is derived here.

**Independent review:** High_match checked the source's F=1, G=S₁=1 scales and inverse factor, the schematic Poisson normalization, and the exponent arithmetic. The review does not verify the source inputs or claim a physical signed equality.
