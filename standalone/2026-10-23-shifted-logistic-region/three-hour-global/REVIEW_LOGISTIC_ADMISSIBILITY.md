# Independent review of exact logistic admissibility

Reviewed file: ../three-hour-type/LOGISTIC_ADMISSIBILITY.md
SHA256: a06963aef0863ef1cdf63e93aab27c4b8f0c8051cbab7f159d468e7596d7a25f.
Reviewer: global-route agent. The reviewer did not derive or author this
adapter. This is an agent review of the indicated analytic interfaces,
not human review or certification of a complete zero-free theorem.

No outstanding issue was found in L1--L12.

I compared the explicit-formula normalization to BTY 2603.21490v1,
Lemma 7, https://arxiv.org/html/2603.21490v1 . Writing its remainder as
H=F-f0/z and Fourier-inverting the real digamma representation gives
exactly the sign and the exp(-(s+2)u) factor in L3. Adding H(s) cancels
the unshifted denominator contribution. For arbitrary first derivative,
the exponential shift has the stated correction L5; there is no extra
endpoint constant. Conjugate-paired zero sums converge locally normally
on the needed half-plane, so the continuation used after the shift is
legitimate. The direct exponential-test normalization check agrees.

The integration by parts in L6 has its first endpoint contribution at
the second step. Expanding u/(1-exp(-2u)) at zero gives exactly L7.
With B=-integral_0^1 f'(tu)dt, its first two derivative bounds are
M2/2 and M3/3. Integrating the resulting K'' bounds gives the three
coefficients of L8 as printed. The displayed elementary derivative
bounds on w and the logistic factor yield the relaxed L9 constant.

The positivity argument only needs the strip 0<=Re z<=a. Both vertical
boundaries give Re W(iy/eta)>=0. The function is harmonic, continuous
on the closure, and tends uniformly to zero as |Im z| tends to infinity;
applying the minimum principle to rectangles with an arbitrarily small
negative allowance on their horizontal sides proves L10 throughout the
strip. It does not require the horizontal sides themselves to be positive.

For L11 I independently recomputed the four weighted L1 Leibniz terms
of f''' and the endpoint f''(0). Their sum is less than 1600 eta for
eta<=.008. The first two transform terms have real absolute values at
most 3*1.008 eta/y^2 and 1.5 eta/y^2. The third-order remainder is at
most 1600 eta/|y|^3, leaving a strict margin below 5 eta/y^2 at the
stated frequency threshold. Both reflected arguments belong to the
same interval when 1-sigma<=eta. Thus L12 has the asserted smaller
constant than the source's distant-zero inequality; its zero-count
tail estimate remains an explicit imported input.

This review licenses the analytic replacement of the polynomial weight.
The actual transform quadrature, zero-frequency gamma/correction term,
prime-power lower bound, continuous parameter certificate, and global
height stitching still require separate verification before any new
numerical zero-free constant follows.
