# Fixed actual-prime tests of the four-prime boundary layer

This is a new declared experiment, before either new prime acquisition
or kernel evaluation. It keeps the previously acquired first three
primes `99999931,101999927,104039917` from
`1d1088d36f0d873ffc94d786415616df95b00edc`. The old fourth prime
`106120717` and its frozen central-face certificate are the control.

There are exactly two new fourth-prime windows. With X=100000000 and
R=51/50, their exact rational centers are

    X R^3 (2501/2500),   X R^3 (2503/2500).

Each window has half-width100. Search odd integers in increasing order,
take the first prime, and use the same complete bounded trial-division
certificate as the previous acquisition. At most101 odd candidates are
allowed in either window. Do not enlarge a window, choose a later prime,
or change the prefix after observing a source energy.

For epsilon=log R the ideal boundary parameters are exactly
`h=log(2501/2500)/epsilon^2` and
`h=log(2503/2500)/epsilon^2`, respectively. The three-phase theorem
predicts the first panel will have one inactive endpoint and the second
will be interior. This is a prediction for these fixed finite tuples,
not an invocation of an asymptotic theorem at an unspecified threshold.

The original native Gram uses all16 source allocations, actual2ds,
physical1/sqrt(K), and every same-cardinality pair; different cardinality
bands must be proved disjoint by exact integer inequalities. Kernel
entries are evaluated from the literal nine overlap integrals and
checked against the native closed formula. The earlier256-bit input cap
and outward512-bit dyadic serialization are retained.

All15 nonempty activation supports will be examined. On each support,
define the exact equality-constrained minimizer from its positive
original Gram matrix, enclose its activations and every inactive KKT
slack by certified rational interval arithmetic, and retain all support
outcomes. The complete original-kernel KKT test decides the actual
minimizer. If the predicted support is wrong or cannot be certified,
preserve that result instead of changing the primes or the support list.

No new high-arity computation, broad prime sweep, numerical quadrature,
full-gamma identification or large-moment claim is part of this test.
