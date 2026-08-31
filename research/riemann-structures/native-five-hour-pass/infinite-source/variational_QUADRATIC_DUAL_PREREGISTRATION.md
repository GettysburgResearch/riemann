# Fixed quadratic-potential global certificate

Registered after the exact failure of the linear menu. Keep the enclosed
ordered root, original Gram and seven-column current unchanged. Test only

`k(u)=3u^2`, so `k'(u)=6u`,

in the potential
`Phi=theta10*u^2*v+w*R-k(u)w(1-v)`. There is no parameter search in this
identity. The residuals are the formulas in
`variational_ORDERED_DUAL_THEOREM.md` with `K` replaced by `k'(u)` in
`A`, by `k(u)` in `B`, and by `k(u)(1-v)` in the `dw` coefficient.

Acceptance requires the same strict five-dimensional Krawczyk enclosure,
all declared clipping and crossing regimes, and:

1. `k>=0`;
2. `B-k>=0` on the full cube;
3. `A-q_v(u,f)>=0` before the true crossing;
4. `A-[q_v(u,1)+q_w(u,g)]>=0` after it.

Eliminate `w` exactly. In the early region use the three cases for
`p` in the theorem. In the late region use its `C,L,N0` cases. All sign
decisions and polynomial inequalities are continuum statements. Directed
Bernstein subdivision is permitted with dyadic boxes of depth at most 20;
boxes touching an exact calibrated equality must instead use a Taylor
model whose constant is set to zero only by the enclosed self-consistency
or branch-crossing equation. Retain the equality identity and every
derivative margin. A grid is forbidden as an acceptance predicate.

Use Arb precision 192, rational endpoint bit cap 4096, at most 200000
subboxes and 200 MiB. Any unresolved box is `UNKNOWN`; do not enlarge the
root box, change the coefficient 3 or introduce a fitted correction.
Success would prove a global original-measure optimizer among all legal
monotone paths. Failure refutes only this quadratic dual, not the ordered
candidate or other nonlinear potentials.

## Preregistration deviation

The final paragraph of this note required exact Sturm isolation for the
reduced univariate gates, even though the controlling resource clause
above had also permitted directed Bernstein subdivision. The executed
producer used the Bernstein route and did not run Sturm isolation.
Accordingly the resulting acquisition is **not** reported as a literal
preregistration-compliant success. It is retained as a source-exact,
post-registered continuum certificate subject to independent proof and
hostile-code review. The candidate `k(u)=3u^2`, root box, precision,
subdivision cap, maximum depth, and acceptance inequalities were not
changed after observing the result.

The first implementation incorrectly used the unconstrained `v`-profile
minimum below its lower clipping point. Its false-success output is
preserved as `variational_quadratic_dual.invalid_missing_lower_clip.v1.json`
and is not evidence. The corrected contract splits at the directed
`u0=-lambda_v/mu_v`. On `0<=u<=u0` it subtracts the true clipped value
zero and, in the vertex case, proves
`4q[(theta1-2theta10 u)v+cv v^2]-p^2>=0`. Only on `u0<=u<=t` may it use
the unconstrained square and its earlier numerator. Both pieces and their
common boundary must pass independently.

For this fixed quadratic correction, the semialgebraic problem reduces
further. The early `p` is affine in `u`, `q` depends only on `v`, and
`Lv` is affine in `u`; hence both early gates are quadratic in `u`. In
the late branch `C` depends only on `v`, while `L` is affine and `N0` is
quadratic in `u`, so all three late gates are also quadratic in `u`. On
each sign cell their minima occur at a `u` endpoint, a sign-cell boundary,
or the single quadratic vertex. Substitution leaves univariate
polynomials in `v`, which must be checked by exact Sturm isolation. This
preserves the calibrated zeros and avoids a two-dimensional grid.
