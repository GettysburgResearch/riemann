# Cancellation of the long-dual diagonal in a separated model

**Status.** This is a source-conditional calculation for a separated model, not the coupled physical Poisson expression. It uses the off-diagonal estimate in §10 of [rStation paper 5 v3](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3), as extracted and independently reviewed in [the diagonal note](2026-10-29-sextic-dual-diagonal-obstruction.md). Those inputs import other manuscripts and have not been independently proved here. No new zero-free region follows.

Let V∈C_c^∞(C) be radial and supported away from 0, with the self-dual Fourier transform for the additive character and measure used in Xu–Sang §3.1. Set f(t)=V̂(z) for |z|²=t. Fourier inversion and V(0)=0 give

    ∫_C V̂(z) dμ(z)=V(0)=0,  hence  ∫₀∞ f(t)dt=0.          (1)

Fix a nonzero smooth annular U and the exact good-prime and finite-ray conventions of the diagonal note. Let P_v(D) be its normalized angular Gauss polynomial, and take

    H=D²/Y,     D=Y^(6/5),     H=D^(7/6).

In particular P_0(D)=0 for all sufficiently large D: for every contributing squarefree n≠1 the original sextic symbol χ_n(0) is zero. Define the separated signed mean

    S_f(H,D)=Σ_{v≠0} f(Nv/H)|P_v(D)|².                     (2)

**Source-conditional lemma.** With any fixed ε>0,

    S_f(H,D) ≪_{f,U,S,ε} (HD)^ε [D + H^(5/6)D^(1/6)]. (3)

Consequently at the displayed scales

    (Y/D) S_f(H,D) ≪ Y^(7/6+ε),                         (4)

and the D part of (3) contributes only Y^(1+ε). Here the multiplier Y/D is the normalized version of the October 5 manuscript's schematic Poisson comparison, not an equality asserted for the exact physical moment.

## Proof of the separated lemma

Paper 5's section 10 off-diagonal argument, including the fixed finite ray expansion, gives for each fixed smooth compactly supported radial profile w and each X≥1, in a fixed polynomial range,

    Σ_{v≠0} w(Nv/X)|P_v(D)|²
      = c_D X ∫₀∞w(t)dt
        + O_{w,ε}((XD)^ε [D + X^(5/6)D^(1/6)]).         (5)

The diagonal coefficient c_D is independent of X and w; explicitly it is a fixed lattice constant times D^(−1)Σ_n |U(Nn/D)|²φ(n)/Nn with the fixed finite masks. The source gives estimates for nonnegative profiles; to allow a fixed signed compact profile one can write its real and imaginary parts as finite differences of nonnegative fixed profiles with the same compact support. The off-diagonal proof itself also bounds mixed fixed-ray terms by Cauchy. The error constant depends on finitely many fixed profile seminorms, so the same reduction applies to uniformly controlled profile families.

Use a dyadic partition of unity for t>0, writing f(t)=Σ_j f_j(t), each f_j supported at t≈2^j. Put X_j=2^jH and w_j(u)=f_j(2^j u). At j≤0 the profile seminorms of w_j are bounded uniformly; at j>0 they decay faster than every fixed power of 2^j by the Schwartz decay of V̂. Apply (5) for X_j≥1. Sum the diagonal terms **before** taking absolute values: by (1), their total over all dyads is exactly zero. For the bounded number of transition dyads with X_j<1 but support still meeting a nonzero norm, rescale the profile and apply (5) at X=1; their contribution and the corresponding main terms are O(D^(1+ε)). For all smaller X_j, the discrete sum is empty and the remaining integral contributes O(c_D); it is absorbed by the error. For very large X_j outside any chosen fixed polynomial range, use rapid decay of f and the trivial polynomial bound for |P_v|² to make the tail smaller than any requested power.

The sum of the D errors over the O(log(HD)) nondecaying dyads costs only a small power; the X_j^(5/6) errors form a convergent geometric sum towards zero and a rapidly decaying sum towards infinity. This proves (3). With H=D^(7/6), its second term is D^(41/36), and Y/D=D^(−1/6), giving D^(35/36)=Y^(7/6).

## What this does and does not control

The cancellation in (1) is an exact statement about the integral of the signed transform. It explains why a positive bound for the complete dual energy cannot simply be substituted into the signed physical sum: the dual diagonal can cancel after the Fourier weight is retained. It does not say that the whole physical off-diagonal has a separable profile f(Nv/H)|P_v|². In the actual gcd/Poisson formula of the [61/72 signed-correlation note](2026-10-29-61-72-dual-correlation/README.md), the Fourier argument depends on Nr₁·Nr₂, the gcd d and divisor k; root phases, ray fibers and original nonunit masks are also coupled to the two residual columns. A physical proof must preserve that dependence through any common-profile separation and control the signed resulting family. The present calculation is only the special **d=k=1, factorized-kernel model**, not an evaluation of that actual block, and says nothing directly about d>1.

To reach a normalized O(Y^(1+ε)) bound from this separated calculation at D=Y^(6/5), the signed theta remainder after diagonal cancellation would have to be O(D^(1+ε)); the source remainder is D^(41/36+ε), so it needs an additional fixed saving D^(5/36). Equivalently, the second term H^(5/6)D^(1/6) would need to be reduced by D^(5/36). For the complete physical proof this is only a target scale: other gcd and divisor blocks must be summed with their actual kernels, and their cancellation may differ. The source's coefficient-blind high-gcd region already bounds all d≥7/10 at Y scale, as detailed in the signed-correlation note; it supplies no such gain for the d=k=1 low-gcd model. No improved signed remainder is claimed here.

**Independent review:** High_match checked the Fourier-integral cancellation, extension to signed profiles, zero row, tails and exponent arithmetic. The review identified the subunit transition dyads, now handled explicitly above. It is conditional on the source estimates and does not establish the coupled physical transfer.
