# Independent review: growing-prime raw-frame no-go

Verdict: **PASS** at exact scientific commit
`78ad7200a48fc51d76cc208346a53839ee5e8df6`.

Review date: 2026-09-01. The target was preregistered at
`1434cd8d2` and is an ancestor of the science. The 164-line proof file
`NATIVE_GROWING_PRIME_RAW_FRAME_NO_GO.md` has Git blob
`f6017d2456929d3eaeb410fd4cc42bb398788068` and normalized-LF SHA256
`61a704e4cb1f04c7828405a078234c7ec6de263436316609ad5da626a07a7ae8`.
No numerical calculation, scientific-source edit or push was used.

## Exact raw direction

The complete A/C observation has rows and columns indexed by local A/C
words. Fixing the all-A column and all-A row choices away from `P`, then
putting coefficients `+1` on the row with local C at `P` and `-1` on the
row with local A there, gives exactly two raw matrix entries. Hence
`||M_(S,P)||_F^2=2`, and direct substitution in the literal observation is

    (C(x_P)-A(x_P)) A(y_P)
      product_(q in S\{P}) A(x_q)A(y_q).

Thus NG1 is an actual ambient coefficient direction, with no missing column
factor, Hermitian restriction, path-attainability assumption, coefficient
truncation or removal of arithmetic aliases.

## Constant audit

On the value-one unit-disk branches,

    A(z)=C(z)sqrt(1+z),
    C(z)-A(z)=-C(z)z/(1+sqrt(1+z)).

The last square root has positive real part, so its displayed denominator
has modulus at least one. With `|z|=P^(-1/2)`, this gives

    |C(z)-A(z)|^2 < 2/P.

Also `|A(y_P)|^2=|1-y_P^2|<2`. For every other prime, branch conjugacy gives

    |A(x_q)A(y_q)|^2=|1-x_q^2|^2<=(1+q^(-1))^2.

Consequently NG1 has pointwise squared modulus at most

    (4/P) product_(q in S\{P})(1+q^(-1))^2.

Integration against the unchanged finite positive physical measure and
division by the exact raw norm squared two prove NG2 with the stated
constant `2 nu(R)/P`.

## Nested panels and coordinate cost

For `S={q prime:q<=P}`, omitting the factor at `P` only decreases the
product. The elementary comparison

    1+q^(-1) <= (1-q^(-1))^(-1)

and the classical Mertens product upper bound give a squared test-vector
ratio `O((log P)^2/P)`. Since the least singular value is the infimum of all
such ratios before squaring, NG7 correctly yields
`sigma_min(O_S)=O(log(P)/sqrt(P))`. The singleton choice independently
forces the raw lower-frame constant to zero across growing primes.

Finally let new coordinates be `n=R_S m`. A norm lower bound

    ||O_S R_S^(-1)n|| >= c||n||

applied to `n=R_S M_(S,P)` first gives
`||R_S M||<=c^(-1)||O_S M||`. The operator-norm definition then gives

    ||R_S^(-1)|| >= ||M||/||R_S M||
                     >= c||M||/||O_S M||.

Thus NG8 has the correct inverse orientation and reciprocal scale. A
uniform positive reparameterized lower bound costs at least
`sqrt(P)/log(P)` on the nested panels and `sqrt(P)` on singletons, up to
the fixed physical-mass constant.

The theorem does not rule out an adaptively weighted topology, fixed-prime
coercivity, or a normalized frame whose inverse cost is explicitly paid.
It also makes no monotone-path or RH assertion.
