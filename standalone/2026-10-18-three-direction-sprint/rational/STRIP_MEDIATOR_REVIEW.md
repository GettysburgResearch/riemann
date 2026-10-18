# Independent internal review of the fixed-strip mediator obstruction

Reviewed `../theta/STRIP_MEDIATOR_OBSTRUCTION.md`, actual SHA256
`98e7fad0fa6682a9aead5421c2729118d768f1b2ffa62ce8fae48cbc00550f6c`.
No blocking error found at its stated fixed auxiliary zero-strip,
bounded-support symmetric auxiliary law, nonnegative quartic onsite,
everywhere-positive continuous weak-limit scope. This is independent
internal component review, not external acceptance or an RH result.

Before reading this file, I independently derived the same extension
from a fixed-band zero quartet: in Fourier coordinates a+ib with
|b|<=delta, its MGF polynomial in u=x^2 is
`u^2+2(a^2-b^2)u+(a^2+b^2)^2`. Its logarithm is concave for
u>2delta^2. The file's MGF-zero coordinates and fixed rescaling are
equivalent and simplify the remaining constants.

The exact reviewed argument was reconstructed as follows.

- An even bounded-support MGF has the stated paired order-one Hadamard
  product, with no residual quadratic exponential. Real MGF zeros are
  impossible; allowing them only as compact-limit parameters does not
  harm the estimates. Pure imaginary pairs have weight1/2 and the
  positive real square root is unambiguous.
- The identity `-2*Re((u-zeta^2)^(-2))` is negative once
  `u>2*(Re zeta)^2`. Adding a nonnegative quartic onsite term preserves
  the needed concavity in u. The previously reviewed native weak-to-local
  density-ratio lemma therefore applies away from zero.
- The three-anchor resource has the exact large-radius coefficient
  `40*Re(zeta^(-4))`, a strictly positive uniform zero-radius limit,
  and a positive compact minimum. Its finite difference adds `40*d_N`,
  with the favorable sign. Thus both the quartic onsite coefficient and
  the complete weighted quartet resource are uniformly bounded.
- For far zeros, `A>=1.96/r^2` and `A^2>=2B` hold after the fixed
  rescaling. They imply the claimed nonnegative increasing remainder
  and the global bound `q<=2*r^(-4)*x^4`.
- For near zeros, `|1-zeta^2|>=Re(1-zeta^2)>=0.99`, while
  `|4-zeta^2|<=5`. Their anchor cost is uniformly bounded and their
  tail log ratios have the favorable sign. The renormalized quadratic
  coefficient is consequently bounded by the1-to-2 density ratio.
- The envelope constants are fixed from the same three local ratios,
  so they survive the separate limit at every x; no weak-limit tail
  convergence is asserted.
- In the purely quadratic controlled-field transfer of Section8, the
  exact conditional Gaussian variance is `1/(2*a_N)`. Its characteristic
  factor bounds the marginal modulus by `exp(-t^2/(4*a_N))`; a
  subsequence a_N->0 contradicts continuity at zero of any probability
  weak limit. Thus the displayed auxiliary strip is uniformly bounded.

The Section8 application additionally uses the explicitly stated
positive-edge real-field strip theorem. This receipt checks the budget
translation and Gaussian/tightness argument, not a new independent proof
of that prior graph-theoretic interface. The analytic mediator theorem
itself assumes only its auxiliary zero strip and does not require that
graph realization. Direct spin observables and transfer energies of
unbounded degree remain outside its conclusion.
