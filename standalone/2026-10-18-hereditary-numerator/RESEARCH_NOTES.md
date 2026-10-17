# What was tried and what changed

Status: exploratory assessment alongside the proposed proofs. This is not a
lower bound for the arithmetic source or an optimality/no-go theorem.

The early searches tried merely optimizing the shifted detector line and
separately bounding higher full-family numerator moments. That largely reproduced
the small improvements already appearing in #966/#969/#971. A proposed direct
mollified second-norm shortcut did not supply a justified power improvement;
no such shortcut is a premise here.

The useful change was to retain the exceptional cardinality BEFORE taking the
moment. Every complete dyad has both the R-row triangle estimate and the full
sieve estimate. The crossing is explicitly solvable, which leads to a hereditary
moment bound rather than just a numerical optimizer's output. In the zero
detector, apply it to the actual mollifier as well as the numerator. The clean
5/7 example is dominated by a long-numerator/short-mollifier term and a mixed
sieve endpoint; it does not require that BOTH moments improve at that same
specific point. The general formula improves sparse off-central sixth/eighth
moments needed in the global comparison.

The global table was found with numerical linear programming and searches over
fixed detector lines and orders. It was then rationalized, and every resulting
inequality was reconstructed without floating point. Some choices lie close to
an envelope intersection, hence the many finite strata. This is a valid finite
certificate if the analytic inputs are valid, not evidence of optimality. No
statement that all orders, asymmetric scales, mixed norms, or source operations
have been exhaustively optimized is made.

Two tempting shortcuts were explicitly rejected before freezing:

1. The old small-frequency line z=2/5 is too expensive at these scales. The
   separate small-frequency line z=1/3 is legal and gives a genuine margin.
2. A negative dual-conductor power cannot be replaced by the same power of U.
   Splitting by actual Q and using rq>=2v proves the needed bound instead.

Further progress should consider a genuinely source-sensitive estimate for the
numerator-mollifier PRODUCT before separate Holder norms, or a signed physical
operation that avoids the positive comparison entirely. Neither bound has been
proved here. The transverse/resonant work newly described in #974/#975 is a
separate route, not an upper estimate supplied by this packet.

The finite parameter 633/700 is deliberately below the old proposals but does
not suggest that RH follows by iterating these fractions. The research gain is
a reusable subset-sensitive analytic estimate, with a precise full comparison.
