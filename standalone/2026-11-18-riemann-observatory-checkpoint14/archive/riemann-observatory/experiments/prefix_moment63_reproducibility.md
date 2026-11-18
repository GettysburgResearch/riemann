# Reproduce the finite prefix moment certificates

The [calculator](code/prefix_moment63_certificates.py) uses Python 3.10 or newer and the standard library. Its inputs are the true limiting Taylor coefficients of the prefix profile, or rigorous rational enclosures for those coefficients. The archived inputs come from a synthetic nonnegative profile. The scope and lattice inequalities are established in the [prefix inverse theorem](../audits/adversarial_reviews/director_prefix_inverse_round8.md) and the [independent finite-jet review](../audits/adversarial_reviews/finite_moment63_review.md).

Run from the repository root.

~~~sh
python3 experiments/code/prefix_moment63_certificates.py \
  experiments/inputs/prefix_moment63_exact.json
python3 experiments/code/prefix_moment63_certificates.py \
  experiments/inputs/prefix_moment63_intervals.json
~~~

The saved outputs are [exact](results/prefix_moment63_exact.json) and [interval](results/prefix_moment63_intervals.json). For a byte-for-byte check, pipe either command's output to `diff - experiments/results/<matching-name>.json`. To read JSON from standard input, supply `-` in place of the input path.

## Input and arithmetic

Set `provenance` to `synthetic_profile` or `certified_limiting_coefficients` and describe the coefficient source in `coefficient_source`. Supply `taylor_coefficients` in order from \([b]C(b)\) through \([b^M]C(b)\). This uses Taylor coefficients rather than unnormalized derivatives. Include `constant_term` if you have \(C(0)\) and want an enclosure for \(W_1\). An exact quantity can be a JSON integer or a string such as `"1/6"` or `"0.125"`. A closed rational interval is a two-element array of endpoints in the same format. Bare JSON floating-point numbers are rejected.

Use distinct JSON keys and valid Unicode in `coefficient_source`. Each higher Taylor coefficient of a nonnegative profile is at least the first. If a higher coefficient's entire interval lies below the first interval, the calculator rejects the data.

The calculator constructs the Legendre-derived triangular polynomials and expresses each requested integral as a linear functional of the original coefficients. For interval input, it projects the original box using the sign of every rational multiplier. The lattice weight endpoints combine each cardinal polynomial and its tail correction into a single functional before projecting the coefficient box. All bounds use exact `Fraction` operations. A lower endpoint of the raw `tail_polynomial_integral` can be negative because it describes the whole coefficient box. The reported weighted-mass bounds use positivity to intersect with \([0,\infty)\).

Every claim is conditional on a nonnegative triangular-lattice profile realizing the supplied data. The output records `feasibility_checked: false`. A successful run applies the computed necessary inequalities and leaves the full truncated feasibility problem and input provenance open. A limiting arithmetic application needs its own rigorous estimates for the coefficients. Derivatives of finite-\(N\) staircase approximants are outside the input model.

## Referencing the output

- The moments are \(y_j=\int x^j\,d\nu(x)\) with \(\nu\{\mu_m\}=t_m=\mu_m^2W_m\) and \(\mu_m=m(m-1)\).
- The row `normalized_tail_functional` integrates \(P_M/P_M(\mu_{M+1})\) against \(\nu\). Its upper endpoint bounds \(\sum_{m>M}t_m\). The field `tail_weighted_mass` also uses conservation of \(y_0\) and the interval mass bounds on the first \(M-1\) lattice nodes.
- `tail_status_if_feasible` reports `zero_tail`, `positive_tail`, or `undetermined`. For `zero_tail`, every realizing profile has zero mass above the cutoff. With exact nonconstant data in this case, the enclosures for the remaining multiple weights are singletons. When \(M=1\), \(P_1=1\), and the weighted tail is exactly \(y_0\). There are then no lattice weights to print below the cutoff.
- `positive_tail` can occur when the numerical lower bound for tail mass is zero. A positive integral of \(P_M\) forces some mass in the tail of any realizing profile. A remote node can contribute a large polynomial integral with small mass.

For the exact fixture, \(W_1=1/3\), \(W_2=1/2\), \(W_3=1/6\), and \(W_m=0\) for \(m\ge4\). With \(s=b/(1-b)\), the first two nonconstant cost functions are \(c_2=4+4s\) and \(c_3=9+36s+72s^2+48s^3\). Thus \(C(0)=23/6\) and the first three nonconstant Taylor coefficients are \((8,20,40)\). The output reconstructs all three weights and certifies zero tail. The interval fixture encloses those coefficients with radius \(10^{-6}\). It gives \(\sum_{m>3}t_m\le1/1562500\), with intervals enclosing the known weights.
