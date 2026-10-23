# Review of the quadratic frequency detector

Reviewed `three-hour-boundary/QUADRATIC_SIGMA_LOGISTIC_DETECTOR.md`,
SHA-256 `2922cbb84355ead8db6af9bcce8cf35bfb71cf5051798b2bf521296f1dadf68a`.
This review covers its new analytic interfaces, not an independent replay
of the full scalar certificate or the imported theorems. The baseline
minimum-zero wrapper was partly co-developed by this reviewer; the
quadratic profile was independently read and checked here.

No unresolved defect was found in the new analytic interfaces.

* The representation `sech(sqrt(s))=integral exp(-sx)dmu(x)` follows from
  the cosh product and the closure of Laplace transforms of probability
  measures. For each fixed v, substitution of `v^2(a^2+lambda*k^2)`
  gives a positive mixture of Gaussian positive-definite sequences.
  The non-unit value of q0 causes no problem: both absolute squares in
  the exact trigonometric polynomial use this same Toeplitz kernel.
* The arithmetic identity includes the exact factor
  `eta*w(eta*v)*exp(-v/2)/2`. Applying the Toeplitz form proves that
  every omitted prime-power term is nonnegative, despite differing
  real parts. This essential step is justified independently of
  coefficientwise positivity.
* Concavity gives the upper increment `d*(eta/l)*k^2`. Together with
  `|sech'|<=1/2` and `w<=6`, the variation cost is
  `(3/2)*eta*d*(eta/l)*sum k^2*a_k*sum m(log p)^2*p^(-m/2)`.
  Thus the stated bounds 14 and 16 give precisely `336*d*eta^2/l`.
  The sign is adverse and the comparison is only charged to retained
  prime powers; the rest use positivity directly.
* Squaring the individual cutoff inequality is reversible. When
  `L_k>c`, it reduces exactly to Q6. Replacing its quadratic coefficient
  by `.21/(2*.4925*28^2)` enlarges the left side. The subsequent
  replacement of `log(k+10^10 exp(-l))/(l+log(k+10^10 exp(-l)))`
  by `log(k+.01)/l` has the correct direction.
* The zero-frequency cutoff lies inside the finite RH verification.
  For positive frequencies, the individually cut off Lehman estimate
  has the same distance `10^10` and no larger height logarithm than
  the baseline allowance. Since `1-eta<=sigma_k<=1`, every far-zero
  real argument stays inside `[-eta,alpha_k+eta]`.
* The selected pair uses F1 at `eta*rho` and `sigma1-eta`; the real
  pole uses F0 at `sigma0-1`. Rationalizing `sqrt(a^2+2ad*eta/l)-a`
  gives exactly the displayed rho and its continuous A=0 value.
  The complement transforms therefore require alpha1 for the two
  selected terms and alpha0 for the real pole, as Q8 states.
* All f_k have the same `f_k(0)=eta*w0/2`, so the same gamma resource
  is valid. The real-axis negative error concerns f0 and is unchanged.
  Combining prime and real-error gains gives `1.57eta`, with both
  curvature and prime-variation losses subtracted. The source margin
  implementation agrees with these signs and factors.

The domain keeps eta<.0075 and .99<sigma_k<1 for A>0. At A=0 the
scalar expression is used continuously, not as a physical zero detector.
The final proposed R=4.806 implication still requires the independent
full-rectangle arithmetic replay and the declared external inputs.
This review proves neither RH nor a smaller fixed Hecke boundary.
