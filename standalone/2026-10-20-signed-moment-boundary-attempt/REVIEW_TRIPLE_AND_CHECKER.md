# Independent review of the triple comparison and finite checker

Reviewer: beyond_boundary. Date: 20 October 2026.

Reviewed proof: work3/TRIPLE_COMPARISON.md

    8ce1ef4e64f1a80cbcd66ddc95af25003e79f9b7992ff76633db114071beacb8

Reviewed checker: work3/verify_signed_components.py

    c03ba99038503a43aaef7a0afb6e4a2ba467c797d925bef56e495c976f1af91b

**Finding: no blocking mathematical or implementation issue.** Neither
reviewed file was modified. The comparison is an algebraic and
fixed-character component, with its reflection closure explicitly
conditional on the stated common-measure rule.

## Proof review

The six choices of distinct maximal and minimal coordinates give the
claimed positive increments, seven comparison vertices, and upper
ceiling \(L+4\sigma\). Positivity of \(a,b,c\) means a collision of two
cube vertices would require \(a=b=c\) and the terminal vertex to equal
the initial one; the strict maximum increase excludes that collision.

The three zero coordinate projections cancel the all-main term and
every term with exactly one mean error. Arbitrary fixed complex
profiles are permitted: their Mellin constants depend on the position
and the common twist, but not on the comparison vertex. Uniform
coordinate extraction preserves the projected signed measures and
lowers the raw volume by the exact total removal. The stated saving
\((A-L-4\sigma-r)_+\) follows.

The individual incoming norm-mode instruction has the necessary
normalization. Explicitly, at the initial scales \(T_i\), write

\[
\widetilde W_i(y)=y^{it_i}W_i(y),\qquad
\prod_i\sum_l\psi(l)(Nl)^{it_i}W_i(Nl/T_i)
=\left(\prod_i T_i^{it_i}\right)
 \prod_i\sum_l\psi(l)\widetilde W_i(Nl/T_i).
\]

The scalar \(\prod_i T_i^{it_i}\) is frozen outside the entire
comparison. At a new vertex it must not be replaced by the analogous
scalar at that vertex. Keeping the normalized profiles fixed then
leaves one common subsequent explicit norm twist, precisely as needed
for cancellation. Profile seminorms retain their polynomial dependence
on the incoming \(t_i\).

The buffered reflection threshold \(B=L+\sigma\) is correct. If a
coordinate \(z>B\) is reflected with
\(z'\le 2L-z+\xi\), \(\xi\le\sigma/2\), its decrease is strictly more
than \(3\sigma/2\), and its new value is below \(B\). This remains true
when the terminal vertex crosses \(B\) by arbitrarily little. If the
terminal vertex stays inside the box, the maximum instead increases
by at least \(\sigma\) at unchanged total length.

For nonempty vertices with actual coordinates at least \(-\eta\),
\(q_A,q_{\max}\) are nonnegative and \(q_{\max}\le N\). Reflection
lowers \(q_A\) by at least one, so the factor \(N+1\) pays for the
largest possible reset of \(q_{\max}\). A terminal step lowers
\(q_{\max}\) by at least one. The rank therefore decreases strictly.
No rounding of negative actual scales is used inside the identities.

These checks do not supply an analytic centered-family bound.
Functional-equation tails, profile orders and a common measure for
the reflected triple remain the hypotheses of the reflection
interface. The rank is not a bound for a product of separately
averaged scale suprema.

## Checker review and replay

Executed:

    python -I -S -B work3/verify_signed_components.py

The command exited with code zero and reported PASS. Its producer
hash matched the checker hash recorded above.

The implementation uses exact rational coefficients and symbolic
linear forms. I checked the interpretation of all six max/min cases,
the positive certificates for increments and upper ceilings, the
coordinate marginal counters before and after the \(g_i\)
translations, and the exact terminal-vertex formula.

The integer Möbius checks cover \(1\le n\le512\). The six alias models
compare complete formal Fourier polynomials for functions invariant
under the sixth-power multiplier. Their graph residues and scale
normalizations are correct. The deleted-vertex and dropped-modulus
controls reject their stated alterations.

The rank argument and profile normalization were reviewed
mathematically; the checker does not claim to certify them
analytically. Likewise its finite integer models do not establish
number-field Poisson summation or global cancellation estimates.
Its explicit exclusions of a sixth-moment bound, signed width
decrease, and a boundary below \(0.874886647039964\ldots\) accurately
describe the scope of the replay.
