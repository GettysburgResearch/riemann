# Independent review of the qualitative native window extension

Status: analytical acceptance of the new open-extension argument.
Reviewed source: `operators/OPEN_WINDOW_PROPAGATION.md`, SHA
`2ddf5a57e16c8b931b19299591cd2a9b99b280e8a13e3ebd0035d57630030d3c`.
Scope: the exact source/domain hypotheses O1--O4, complete native kernel,
codimension-14 complement theorem and completed strict native lower gate at
`L=1` are imported. This review checks their proposed local continuation;
it does not repeat the native matrix or continuum residual computation.

The length-dependent complement estimate follows from the same clamped
primitive Fourier identity, with the first retained sine frequency
`12*pi/L`. The displayed rational inequality gives the uniform gap `6/5`
for `1<=L<=1.0001`; its coupling multiplier is exactly
`(3/2)^2/(6/5)=15/8`. The full prime-power tail remains in the same rank-two
form since the length cap is below `log3`. Nothing in this argument discards
that tail or asserts a native L2 spectral gap.

After the substitution `t=L*s`, the native Gram entries are continuous.
The finite exponential/sine family stays independent, so the positive
diagonal Cholesky choice and the resulting orthonormal basis are continuous.
The projected high sines are continuous too. Fixing the exact previously
certified correction coefficients therefore supplies legitimate nearby
trials, with the certified trials recovered exactly at one. New energy
optimality is unnecessary for the completion inequality.

I checked the kernel regularity against CONTINUUM_RESIDUAL_DERIVATION.md.
The gamma derivative coefficients are
`lambda_j/(lambda_j^2-b^2)<=1/j`, for `lambda_j=2j+1/2`, `b=3/2`.
Their exponential sum is bounded by a constant times
`1+abs(log(abs(x)))`. The prime2 term is continuous at its cusp and its
one-sided first derivatives have a bounded jump; it creates no delta in
the first weak derivative. The other source terms are smooth on the fixed
length cap. Thus the stated derivative bound is valid for the full source.

Under rescaling, `1+abs(log(abs(s-r)))` is an integrable uniform majorant.
The finite trial functions remain uniformly bounded. Their convolution
derivatives converge almost everywhere as L varies; the diagonal and the
prime-cusp curves have measure zero. The integral of the logarithmic
majorant is uniformly bounded in s, so dominated convergence also gives
L2 continuity of the complete `K_z'` and `F_z`. The finite constraint Gram
and its inverse vary continuously and remain nonsingular. Consequently
the full projected residual Gram is continuous, including the gamma series
and complete prime tail.

The imported strict lower reserve `10^-11 I` at one persists on some
nonzero right neighborhood by finite-matrix continuity. The uniform
complement gap and exact source coupling then permit the same square
completion. Nonzero finite coordinates are paid by the finite reserve;
a nonzero pure-complement vector is paid by the primitive gap and
injectivity. The existing smaller-length positivity joins that neighborhood.

Verdict: the existence of some `eta>0`, `eta<=1/10000`, with strict native
positivity for all `0<L<=1+eta` is valid at the stated imported source and
completed-gate scope. No numerical eta, positivity at a specified length
above one, all-window positivity or RH conclusion is established.
