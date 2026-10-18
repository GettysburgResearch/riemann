# Independent review of the degree-20 theta realization

Reviewer: primary agent, separate from the theta proof and certificate author.
Status: proposed finite theorem supported by independent mathematical
reconstruction, a separate exact finite implementation, and the assembled
replay recorded in the packet validation. This is an AI review, not external
human referee acceptance or a proof-assistant verification.

## Exact reviewed identities

| Object | SHA-256 |
|---|---|
| theta/PROOF20.md | `ddf054aa7915699ea923f21ff703ecb06ebad9eb8cebe4cd49862d688a833e22` |
| theta/connected_blocks.py | `b376526980faf4e98fc9060695befa65e1a1c7c3b1f143b52b3c7dafa7c95978` |
| theta/parameters20.json | `2bfeb0b5ff376e2fb2b1f3773b726f4679af15dd01af0037ac2b10fa87db8bd4` |
| theta/certify20.py | `7125cfc48903320b247bb7326794d0d41880b198613b89c0a5258693dbc6ac7c` |
| theta/certificate20.json | `0cf3307c9493dc6b6c813e2aa0b18a6e1a637ab89ce6f3ffaf5719f161ddcc0c` |
| theta/check_connected.py | `40bc152a27094745fd7973ab291bf4e5ba752cd4b45d37b04eb7de3a68182fab` |
| theta/theta_source.py | `75a239c2724afbd6d5ab343a00c1f3c4d1e7062eaab9ff99b0379eecde27e92d` |
| theta/pr886_primitive.py | `2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55` |
| theta/tree_core.py | `edab764577f7c4a1553d1dfb3f19b838f536ff48273aba8cf91acb4289a8577a` |

I read the complete mathematical proof and all seven accepting code/input
files. The only requested correction during review was to make the claimed
variance comparison an explicit runtime predicate. The final checker above
includes that predicate and its regenerated certificate. No substantive
mathematical correction was required.

## The complete graph and exact moment map

There are 256 one-spin components and 24 two-spin components: the first dimer
type is repeated ten times and fourteen others appear once each. The shared
hub therefore joins 280 component roots. Its 280 incident edges and the 24
internal dimer edges give 304 edges on 305 vertices, with 304 positive-weight
observed spins. The hub has observable weight zero.

I independently reconstructed the Gibbs probability 2^-305 times the product
of (1+q_e s_i s_j). On a tree, a fair hub spin and independent edge products
give a bijective generative description of every configuration. This proves
normalization and the equivalence with finite positive couplings
J_e=atanh(q_e); it does not discard any spin configuration.

For one dimer, put u=(A+B)/2 and w=(A-B)/2. Given its root sign sigma and its
independent edge product epsilon, the observed value is sigma(u+w epsilon).
It is sigma A with probability p and sigma B with probability 1-p. Conditional
on the positive hub, sigma has mean eta. Thus the even component moment is
pA^n+(1-p)B^n and the odd one is eta times the SAME bracket. In particular,
the sign of B in the conditional odd terms cannot be arbitrarily reversed.

All component roots are independent only after conditioning on the hub.
Adding their conditional cumulants with the exact multiplicities, recovering
conditional moments, and THEN keeping only the even part is correct. Taking
the even part before multiplying the components would remove actual shared-
hub correlations. The final cumulant calculation is a polynomial operation
on the complete unconditional moments. Dividing by the nonzero fair-sign
cumulants merely rescales the ten equations.

The parameter file keeps all p_i fixed within (1/2,1); its ten active
coordinates vary observable amplitudes. Throughout the actual cube, 0<B_i<A_i
gives two strictly positive observed weights in every dimer. The explicit
correlation tests and the rational partial sum for exp(6) prove
10^-11<J_e<3. The complete support sum is below 11. These inequalities are
proved on the whole cube, so they apply at the exact root rather than only
at the decimal center.

## The infinite theta source and rounding contract

I independently reconstructed all three analytic remainder bounds. For every
explicit density term, the Cauchy circle has radius 1/8 while the half-cell is
1/32. On that circle Re exp(2t)>0, so the outer exponential has magnitude at
most one. The finite prefactor bound below 10^11 holds for all six theta
indices and every center. The radius ratio 1/4, t^j<=2^j, and total full-line
cell length 49/4<16 give exactly the Taylor error in the proof, including
order j=20.

On each of the six omitted time intervals, convexity of exp(2u) gives the
linear exponent with lambda=2q exp(2U)-9/2>0. Integrating the full binomial
(U+u)^j gives its stated sum of k!/lambda^(k+1). For indices n>=7, the ratio
of consecutive positive numerator bounds is below 1/2 and the denominators
increase. Twice the first omitted bound therefore pays the entire index
tail. The real density terms are positive, so adding time/index tails only
to the upper endpoint is justified; the Taylor error must have both signs.

The source code does exactly these operations at every even order 0--20,
then normalizes by the positive mass and standardizes by the enclosed
variance. Odd moments are zero by the even source definition. The actual
variance is explicitly enclosed within (1/25,1/20). No saved target moment
file or special-function library is read by the accepting reconstruction.

I read the inherited integer interval implementation. Its signed four-endpoint
multiplication and positive-reciprocal endpoint order round outward. Division
by a negative scalar or interval reverses signs correctly, which matters for
the alternating fair-sign cumulants. Its Machin arctangent series retains
the first omitted alternating term. Its exponential routine reduces positive
arguments to [0,1/8], encloses the complete positive Taylor tail, and squares
outward; negative arguments use reciprocation. The cell Taylor recurrence is
the exact formal exponential-series recurrence, and the full polynomial
moment integral retains the factor two for the even full line.

This is a review of the inherited backend, not an independently written second
transcendental implementation. Its exact source lineage and the extra final
newline relative to #886 are recorded in the packet sources.

## The exact root argument

The Jacobian at the rational center is computed over Fraction values and its
inverse is checked on BOTH sides. Automatic differentiation uses only the
polynomial operations in the complete moment map. Interval evaluation of the
same derivatives over the full cube contains every actual Jacobian there.
The sum of absolute entries in each row is the correct induced infinity norm.

The certified bounds are beta<1.561e-39 and L<1.371e-10 for a cube radius
10^-30. The acceptance predicates are exact rational strict inequalities;
they imply beta+L r<r. Hence the Newton map using the fixed exact center
inverse maps the cube strictly into itself and is a contraction. Banach gives
a unique fixed point in that ten-coordinate cube. Invertibility of the fixed
matrix converts that fixed point into all ten exact source equations.
Triangular moment-cumulant inversion then gives the moment equalities through
20, including variance one. Raw interval overlap has no role in proving
existence; it is correctly described as a diagnostic.

The complete certificate is regenerated before comparison with its stored
JSON. Thus its reported contraction constants do not supply inputs to their
own acceptance. Rational-center construction is an optional producer; the
certificate does not trust its Newton iterations or historical scout path.

## Independently implemented finite map and derivatives

I wrote `root/check_theta_product_independent.py` before publication. Its
source SHA-256 is
`7ad686d5c9dd25b203c10be8a0e74c293e4e88a7542ed471f08dfdeeeb9d92ba`.
It builds the complete conditional exponential generating polynomial by
ordinary exact convolution and integer powers, and projects to the even part
after the complete product. It obtains cumulants from the formal logarithm,
rather than the author's cumulant recurrence. For every active coordinate it
differentiates the full product directly and multiplies by its formal
reciprocal to obtain the derivative of the logarithm.

At the specified full 305-vertex rational center, every raw moment 0--20,
all ten normalized cumulants, and ALL 100 Jacobian entries agree exactly.
The receipt SHA-256 is
`a1f1204686adccd12ace4ed93b0f73d202eb775d810280999c85226de12dd93d`.
Ordinary and optimized runs give identical bytes. Two separately executed
optimized corruptions fail at the intended gates: permuting derivative
columns fails the complete Jacobian comparison, and erasing the hub fails
the complete graph moment map. Another agent has reviewed this independent
checker at its exact hashes.

The author's separate seven-spin enumeration and full generating-product
assembly provide additional finite checks. Neither implementation enumerates
all 2^305 configurations explicitly, reimplements the theta transcendental
backend, or proves a root solely from equality at the rational center.

## Real-zero conclusion and full-proof boundary

The classical weighted finite Lee--Yang theorem applies to the constructed
zero-field ferromagnet with positive observed weights. The zero-weight hub
is covered either by its nonnegative-weight version or by giving the hub a
positive weight delta and taking delta to zero. The finite configuration sums
converge locally uniformly, their limit equals 1 at zero, and Hurwitz excludes
new nonreal zeros. Scaling the observed variable by sqrt(v)>0 preserves this
real-zero property while giving the original, unstandardized theta moments.

The matching theorem has finite order 20. The boundary identities used during
the search do not prove a certified continuation path, an always-feasible
next step, or an unbounded sequence of matching orders. The #981 compactness
consumer correctly needs only such cofinal feasibility; bounded variance
already supplies the common analytic bound for the real-zero laws. The
remaining problem is construction at unbounded order. The reviewed theorem
does not establish that premise or prove RH.
