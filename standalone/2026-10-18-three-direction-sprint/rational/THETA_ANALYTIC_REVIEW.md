# Independent internal review of the analytic-tail extension

Reviewed `../theta/ANALYTIC_TAIL_OBSTRUCTION.md`, actual file-byte SHA256
`edd26b59e4c5cb829e1d744e091507e004a3d4df2c59ef51278d752cb3ac0204`,
against the already reviewed harmonic-lattice argument. This is independent
internal component review, not external acceptance, an existence theorem for
theta approximants, or an RH result. No blocking error found at its stated
analytic-tail, fixed-hub, compact finite-head scope.

I reconstructed the following extensions independently.

- Inverting `W(u)=u/2+c*u^2+O(u^3)` gives
  `x(w)=1/(2w)+2c+O(w)` and therefore
  `w^2*(-x'(w))=1/2+O(w^2)`. The absent linear density term preserves
  the logarithmic coefficients used in the two-branch obstruction.
- At the first saddle, `y_s^2=i/(2*pi)`, so the quadratic weight
  perturbation multiplies the leading contribution by `exp(4*pi*i*c)`.
  It changes the phase and cannot erase the amplitude. The exact shifted
  harmonic family has `c=-d/2` and reproduces shift `a+d`.
- The analytic amplitude and higher weight terms have relative saddle
  expansion in `t^(-1/2)`. The apparent first `t^(-1/4)` Gaussian term
  is odd. On the quarter ray the quadratic correction is imaginary;
  after choosing a sufficiently late fixed endpoint, all remaining
  terms fit a fixed fractional loss in the real Laplace exponent.
  Thus every `m*k>=2` term still decays faster than the first saddle.
- The analytic inverse density can be included in the previous Cauchy
  remainder proof of the continuum Gevrey1 expansion. A fixed finite
  head with real couplings has positive conditional leading coefficients
  and contributes only linear, constant, and exponential corrections.
- The cofinal claim needs coordinate control at the finitely many early
  tail arguments outside the common holomorphy disks. The reviewed file
  explicitly includes that premise; it does not infer it from local
  Montel bounds. Uniform Cauchy bounds give `|W_N(u)|<=C|u|`, so one fixed
  late index puts every remaining argument and image inside both disks.
  The two uniform `O(1/L)` tails then justify locally uniform conditional
  product convergence. Moment convergence identifies the entire limit.

The conclusion excludes precisely this uniformly analytic, bounded-head,
single-hub scheme. It leaves nonanalytic tails, growing heads, noncompact
limits, and other graph architectures open.
