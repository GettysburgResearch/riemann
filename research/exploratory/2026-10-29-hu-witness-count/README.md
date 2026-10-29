# Fixed-type detector and first-stage row count

Status: source-dependent reduction, not a completed zero-free-region theorem. This note isolates the detector and counting step from the contour estimates. It uses Hu's moment theorems and the detector construction in OpenAI, and the numerical row-count optimization of Xu–Sang. No source is asserted to state the displayed fixed-type, variable-geometry combination verbatim.

## Inputs and statement

Let K be the fixed field in Hu's setup, and fix the finite collection of unitary archimedean types and finite sector characters which occur in its row decomposition, including conjugates and the physical prime-character presentations. Let β be the supremum of real parts of zeros of all their primitive Hecke L-functions in the prescribed family, with β>51/100. Let U be a retained row dyad, and assume all primitive conductors in the detector are O(U), the deleted Euler factors have radical norm U^O(1), and the physical row count is O(U^{1+ε}). The physical amplitudes have disjoint complete smooth prime windows of total length U^L, in the sense that the sum of their logarithmic lengths lies in a fixed bounded range and is L>1/5 with a fixed margin. Their phases, masks, exceptional-row exclusions, and row-dependent profiles are exactly those permitted by Hu's Theorems 4.1–4.2 and Proposition 4.14. Assume also the prime-amplitude upper bound from the same buffered detector: each main slot satisfies |Q_i| ≪ U^ε P_i^{a−1/2+O(e)}, with its prime-character presentation included in the buffer and its frequency charged to the same cumulative height allowance. This bound, not moment admissibility alone, gives g_i≤δ/2 up to the prescribed subdivision loss. In particular, any inducing finite character excluded by the fourth-moment theorem is removed before applying the estimate; in Hu's sixth-power-free rows such exceptional rows have bounded norm, by the conductor argument in Hu §7.1.

Take κ=3/4. Hu's seven-eighths result for finite-order characters supplies the moment premise β_finite≤(1+κ)/2. On a fixed nonfloor detector bin, let a be its left endpoint, δ=2a−1, and partition rows into Xu–Sang amplitude classes with 0≤g_i≤δ/2 and q=(Σ_i w_i g_i)/L, where w_i=log(P_i)/log U. Each positive bin supplies the width-relative lower bound |Q_i|≥U^{w_i(g_i−ε₀)}; no lower bound is imposed on zero bins. The upper bounds hold with matching width-relative loss, including zero bins. Put x=q/δ∈[0,1/2]. The small excess in the prime upper bound is absorbed into the prescribed loss when clipping the amplitude bins at δ/2; it is not assumed to vanish literally. A bounded range for L makes the sum of relative bin losses uniformly small. When β≤7/8, one has δ≤3/4. Then, for every ε>0, the number of physical rows in an amplitude class is

    #B ≪ U^{R(δ,x)+ε}(1+T₁)^A,
    c = 4/9,  α = 5/6,
    D = 3−(1+2c)x,  P = (2−2cx)(1−x),
    J = (α−δ)D+δP,
    R = 1−δ+(α−δ)δP/(2J).

The bounded exponent A and the row-independent constants can depend on the fixed field, types, sectors, allowed profile orders, loss and chosen finite slot system. The detector cutoff T₁=Z^τ is selected with τ>0 sufficiently small after these orders are known; height factors can therefore be absorbed into the requested U^ε on dyads U=Z^d with d bounded below. The floor bin is handled by the total row count. The bound is valid for each fixed slot and error pattern, including slots of zero amplitude.

## Why the detector applies to fixed type

OpenAI Lemma 4.9 is written for finite-order characters. Its proof uses only a polynomial bound for |L| in fixed vertical strips, absolute convergence of the Euler logarithm on Re s≥151/100, and a zero-free disk. All three hold uniformly for the fixed unitary types above, with analytic conductor O(U(3+|t|)^C). In detail, on the zero-free disk centered at 2+it, Borel–Carathéodory first bounds a branch of log L by O_e(log C); on the fixed inner disk Re s>1 the Euler logarithm is O(1); three-circles then gives O_e((log C)^θ), with θ<1 uniform for 1/2≤a≤1. Exponentiating gives |L|+|1/L|≪_{e,ε} C^ε on the smaller concentric disk. The same Cauchy estimate gives L'/L≪_e log C. OpenAI Lemma 4.10 handles deleted Euler factors and their reciprocals on positive real parts. The primitive functional equation and the fixed-type gamma estimates of Hu Lemma 3.3 give the reflected bound, with a fixed polynomial height factor.

Now repeat OpenAI Lemma 8.1 with the finite presentation set for each row. The increasing sequence of zero maxima at nested heights produces a bin i,a with M_i∈[a,a+e), M_{i+1}<a+2e. If a>51/100, an actual zero is attained with real part at least a, so a≤β. The preceding disk bound and reflected functional equation give the same buffered bounds as OpenAI Lemma 8.1. These estimates imply the pointwise inverse and plain polynomial bounds of OpenAI Lemma 8.2 by the same truncated Mellin shifts. The single cumulative Fourier-frequency allowance must be retained; no new allowance is granted at successive contour shifts. The tail order is chosen only after the finite internal seminorm and height orders and τ have been fixed.

The prime-amplitude input is the fixed-type analogue of OpenAI Lemma 19.1: after finite-character expansion, use the buffered logarithmic-derivative bound, smooth von Mangoldt inversion, and removal of prime powers. The relevant prime characters must be nonprincipal; any rows for which the finite inducing character belongs to the fixed exceptional family are handled separately as above. Prime-window Mellin frequency consumes part of the same height allowance. This source-to-physical identification is an explicit input here, not a consequence of the moment inequalities.

OpenAI Proposition 8.3's smoothed truncated-inverse identity applies to these fixed-type entire nonprincipal functions: the long outer shift uses only polynomial strip bounds and fixed-type gamma factors, while the zero at ρ annihilates the residue at the origin. Thus, for each row and each 1≤t≤3/2, there are inverse and plain polynomials for **one common presentation and one common twist height**, with uniformly smooth annular profiles, lengths U^r,U^m, and

    r≤t+o(1),   r+m≥t−o(1),   0≤m≤1/2+O(ε),
    |M_r|² ≳ U^{δr−ε},   |S_m|² ≳ U^{δm−ε}.

For the general fixed field choose the detector smoothing length U^B with B a sufficiently large fixed constant depending on the fixed strip-growth bounds; the pre-saturation dyadic lengths then lie in [0,B+1+o(1)]. Choose B before profile and tail orders and the height exponent. The proof compares the lower bound for the product at the zero with the two individual pointwise upper bounds. Presentation choices are finite, and the dyadic length choices cost only O((log U)²); rowwise profile and height choices are controlled by the uniform Sobolev bounds in Hu Proposition 4.14. This is the detector argument in the proof of Hu Proposition 6.3, used here separately from that proposition's printed hypothesis B>7/8. The deduction does not require that hypothesis: its bin proof only uses a≤1 and the fixed-type estimates just listed. The zero used must be nonprincipal; bounded exceptional rows are already excluded.

## Moment matching and numerical count

For a witness presentation λ_u=ω₀ξ_u, Hu (7.7) expresses every physical slot as a sum of λ_u(p)ω₀(p)^{-1}b_i(p), with b_i a fixed permitted finite-character combination. The actual prime character remains finite order. The same formula covers conjugate presentations: if the plain moment requires the other orientation, conjugate the whole witness-slot product, including its profiles. This preserves the absolute values, masks and support. Moment sums are nonnegative, so Hu's estimates also hold on each detected subfamily. Their relevant forms are

    Σ |M_r|² ∏_{i∈I}|Q_i|² ≪ U^{1+ε},
       r+2z<1,  2r+8z<3;
    Σ |S_m|⁴ ∏_{i∈I}|Q_i|² ≪ U^{1+ε},
       2m+6κz≤1, z>0;
    Σ |M_r|² ≪ U^{max(1,(1+5r)/6)+ε},

with z the sum of selected slot lengths. The zero-slot plain estimate is separately available for a nonprincipal inducing character. Polynomial height factors are suppressed here and restored in the statement. Strict inverse inequalities are enforced with a fixed margin, and the plain slot mesh is fixed before the slot count. Small capacities are handled by the unmarked estimate and a small loss.

Apply Xu–Sang Proposition 4.1 and its proof: select whole positive-amplitude slots by decreasing amplitude, discard at most one fractional slot, and absorb this by the mesh; if positive slots are exhausted, their total gain qL is at least the requested qz. Zero-bin slots need not be selected. The inverse capacity is (1−r)/2, while the plain capacity is (1−2m)/(6κ). Their short-witness exponents cross for r between 3/5 and 1; the second inverse constraint then has at least 1/5 margin before the small slack. Balancing this branch with the long inverse exponent 1−δ+(5/6−δ)(t−1) gives the displayed R. The source proposition is stated abstractly in terms of these moment, coefficient and witness hypotheses, and its κ-range includes 3/4. Here δ≤3/4<5/6, so J>0. Thus there is no need to extrapolate Hu's fourth moment below κ=3/4 for the first-stage count.

This completes the detector/count reduction **under the listed physical moment and row-decomposition inputs**. It does not prove the remaining dynamic-contour estimates or the resulting improved zero-free boundary.

## Sources

* Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), Lemma 3.3, Theorems 4.1–4.2, Proposition 4.14, proof of Proposition 6.3, and §7.1, especially (7.4)–(7.7).
* OpenAI, [*The Quasi-Riemann Hypothesis*](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), the source preprint used by Hu as [16], Lemmas 4.9–4.10, 8.1–8.2 and Proposition 8.3.
* Xu–Sang, arXiv:2610.15291v2, Proposition 4.1 and its proof.

**Independent internal review:** A second agent checked the formula, κ-range, witness lengths, strict inverse margin, zero-slot exception, and Hu (7.7) coefficient identity. The complete transfer of OpenAI’s detector and prime bound to every fixed-type physical presentation, including all masks and the common height allowance, remains a source-dependent bridge; the reviewer did not independently verify Hu’s moments or theta construction.
