# Independent internal review of the Gaussian mediator obstruction

Reviewed the actual bytes of
`../theta/GAUSSIAN_MEDIATOR_OBSTRUCTION.md`, SHA256
`610977f33da3482ec955521d48d8d5a4801e0411d7185fb90d666026bc4f716d`,
and the native local compactness lemma and ratio passage in
`../theta/RANK_ONE_HIERARCHY_OBSTRUCTION.md`, SHA256
`42a8a85db9ec53c6bc8efd06b912706f08f2ddfc546c2f406ae516610fde8ba0`.
No blocking error found at the declared bounded-support symmetric real-zero
auxiliary, single Gaussian mediator, everywhere-positive continuous weak
limit scope. This is independent internal component review, not external
acceptance, an all-Lee--Yang classification, or an RH result.

The following points were reconstructed independently.

1. Bounded support gives an even entire characteristic function of order
   at most one. Pairing its real zeros cancels the genus-one exponentials
   and leaves a product of `1-z^2/lambda^2`; the remaining linear
   Hadamard exponential vanishes by evenness. There is no quadratic
   Gaussian factor. The paired reciprocal squares are summable.

2. The transformed potential is convex in u=x^2 because each
   `log(1+t*u)` is concave. Weak convergence of X implies weak convergence
   of U=X^2. Restricting to an interval away from zero, weighting by
   sqrt(u), and renormalizing is valid because the limiting endpoints
   have zero measure and the normalizing mass is positive.

3. The native concave-log-density lemma has sufficient anchors: positive
   limiting masses give one positive-density point on each side of a
   larger compact interval. Concavity gives a uniform lower bound;
   integrating half the segment from a candidate maximum to an anchor
   gives its uniform upper bound. Secant bounds give interior
   equicontinuity. Subsequential limits identify the positive continuous
   limiting density, so the required local ratios really converge.

4. The finite-difference coefficients at x=1,2,3 cancel both constants
   and x^2. Strict concavity gives G(t)>0, its small-t coefficient is
   exactly20*t^2, and its positive infinity limit bounds the number of
   large t, with multiplicities. Positivity makes the infinite resource
   passage legitimate.

5. Subtracting the small-t quadratic parts can leave an unbounded raw
   sum of t, but the resulting c_N is bounded by the1-to-2 local ratio,
   the bounded sum of t^2, and at most S logarithmic increments bounded
   by log4. For x>=1 the remaining large-t logarithmic differences have
   the favorable sign. This proves one global quartic envelope with
   constants fixed by the same three local ratios.

6. Passing separately at every fixed x keeps those global constants;
   no convergence of tails is inferred from weak convergence. The exact
   complete theta kernel has potential `pi*exp(2x)-(9/2)x+O(1)`, so it
   violates that envelope. Integrating the Gaussian in the proposed
   graph indeed adds positive couplings `b_i*b_j/(2a)`.

The argument does not exclude arbitrary ferromagnetic or Lee--Yang
constructions. It excludes the specified single-coordinate quadratic
mediator architecture even with correlated auxiliary graphs and
unrestricted varying parameters.
