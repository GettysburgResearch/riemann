# Sixth-power frequencies in the additive Gram bound

**Status:** Proposed elementary obstruction, not a zero-free region or a sharpness result for the Gram bound.
**Scope:** Counting a subclass of the exceptional nonzero frequencies and the behavior near the origin of any fixed nonnegative row majorant.
**Source:** Proposition 15.2, especially its exceptional-frequency paragraph, in OpenAI, *The Quasi-Riemann Hypothesis* ([PDF](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), Git blob `8132b77eeb270a70b25df8d6609f008e83e65d91`). The proposition and its analytic applications are not independently reviewed here.
**What was done:** The elementary counting and Fourier-continuity arguments below were derived on paper; no claim of literature novelty is made.
**Smallest remaining gap:** Establish a lower bound or cancellation estimate for the **actual weighted arithmetic correlations** in the Gram sum. Counting frequencies and a Fourier window alone does neither.

## An elementary obstruction to a notch/counting shortcut

Let `O=Z[omega]`, the Eisenstein integers, embedded as a plane lattice, and let `m` be any nonzero ideal. For every fixed `epsilon>0` there are constants `c,T0>0` depending on `epsilon` and `m` such that, for every `T>=T0`, at least `c T^(1/6)` distinct nonzero `k in O` have

    k = a^6,   a = 1 (mod m),   N(k) <= epsilon T.

Indeed, choose a Z-basis `b1,b2` of the lattice `m`, and set `a=1+n1 b1+n2 b2` with `|n1|,|n2|<=R`, for sufficiently small `R` proportional to `T^(1/12)`. The triangle inequality ensures `N(a^6)=|a|^12<=epsilon T`. There are `(2 floor(R)+1)^2` such `a`; discard at most one zero. Each `k` has at most six preimages since `z^6-k` has degree six. This yields the lower bound. The congruence can incorporate any fixed primary and coprimality masks: `a=1 mod m` is a unit modulo each prime dividing `m`, and so is `a^6`.

Now let `w` be any fixed integrable nonnegative, nonzero row majorant on the plane, and define its Fourier transform using any fixed nondegenerate real bilinear phase. Then `w_hat(0)=integral w>0`, and continuity gives `|w_hat(x)| >= (1/2) integral w` on some neighborhood of zero. Taking `epsilon` smaller if needed, the same count therefore gives `c T^(1/6)` distinct sixth-power `k` for which `|w_hat(k/sqrt(T))|` is bounded below by a positive constant. A fixed invertible linear change of Fourier coordinates changes only the constants.

The proof of Proposition 15.2 takes a first shell with Fourier argument bounded by a fixed constant and counts exceptional frequencies of the form `(k)=a_1^6 e`, where the sixth-power-free factor `e` is supported on primes of the common divisor and a fixed set. The subclass `e=1` already has the order `T^(1/6)` above, including after fixed congruence restrictions. Thus a fixed nonnegative majorant cannot simply have a Fourier hole around zero, and a universal counting improvement to `o(T^(1/6))` for that subclass is impossible. These statements explain why a direct improvement based *only* on deleting a zero-frequency neighborhood or counting fewer sixth powers cannot work.

They do **not** prove that the paper's `P_a^(1/6)` Gram term is sharp: its contribution also contains common-divisor, ray, zero-mask, correlation and profile factors, whose support or cancellation may change the answer. The sixth powers above need not satisfy all the restrictions of an individual summand, and this note does not prove that they add with the same sign. A stronger Gram bound could still come from the actual arithmetic or from a genuinely different physical probe. In particular this observation neither proves nor rules out any zero-free region.

## Prior art and comparison

Xu and Sang, [*Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291), Section 1.1, report that Xu's unpublished October 2026 manuscript *A sharp lower bound for the sextic large sieve* proves a lower bound of scale `A^(5/6) B^(1/3)`, up to arbitrarily small powers, for a sextic character matrix with squarefree indices in `B^(16/11+delta) <= A <= B^(2-delta)`, `0<delta<3/11`. They state that this evaluates an exceptional sixth-power contribution and shows it survives squarefree restrictions. This is a substantially stronger and arithmetic result than the elementary counting fact above; the underlying manuscript and its hypotheses have not been independently inspected here. Xu and Sang explicitly warn that an operator-norm lower bound does not prove optimality of the zero-free boundary from their particular probe. No claim of novelty over that work is made.
