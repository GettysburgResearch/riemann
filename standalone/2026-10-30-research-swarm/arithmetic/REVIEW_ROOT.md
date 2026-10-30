# Root review of the arithmetic profile extension

Status: **INDEPENDENT MATHEMATICAL REVIEW; no blocking defect found**.  
Reviewed file: `progression_profile.md`.  
Reviewed SHA256: `1314c3a59a08245b56c032635ed11fde09531129eb18d8f1486522988ed97a31`.  
Reviewer: root, separate from the arithmetic author. Date: 2026-10-30.

The review reconstructed the following steps rather than relying on the numerical experiment.

1. For fixed k, expansion of phi(m)/m gives the coefficient k times the absolutely convergent sum of mu(d)/(d phi(kd)). Fixed reduced-progression PNT handles each fixed d. Brun–Titchmarsh is uniform for d at most sqrt(Y), since the logarithm of the progression length is then comparable to log(Y). The remaining elementary sum is bounded by a constant times Y^(3/2) log(Y) + Y log(Y)^2. Proper prime powers contribute o(Y^2). This justifies the order of the two limiting operations.
2. Factoring the resulting series produces the stated C(k), including the different local factor at primes dividing k. The appearance of Artin's Euler product is classical and assumes no primitive-root conjecture.
3. The complement q>Q is exactly switched to the finitely many k<u at x=uQ. The normalization by Q(Q−1) and the integer endpoints do not change the limit. Monotonicity and continuity give uniform convergence on each fixed compact u interval. This does not give uniformity on intervals growing with Q.
4. The Euler factors give both residue one at s=1 and C(2)=1. Writing C(k) as a nonnegative divisor convolution shows sum(C(k), k<=v)<=v and supplies the model's growth bound without a Tauberian hypothesis.
5. The Mellin calculation starts in 1<Re(s)<2. Subtraction of x^2/(2Q) over 0<x<1 gives exactly the term −Q^(−1)/(2−s). The point s=2 is removable. No reciprocal Euler factor is introduced; in Re(s)>0 only the pole at 1 can occur in the compensator.
6. The compensator cancels residue −1 of T_Q at 1 and leaves every nontrivial-zeta-zero residue positive. The finite conductor count in the parent report remains unchanged.

The main unresolved issue is substantive: fixed-scale o(Q) error becomes only o(Q^(1−sigma)) in a Mellin block at sigma<1. Neither decay there nor control of the unbounded x/Q tail follows. The report states this correctly. Its illustrative experiment cannot supply that missing estimate.

The proof is suitable for an exploratory research PR under its explicitly stated classical inputs. The review does not establish global novelty, formal proof verification, or a new zero-free result.
