## Checkpoint 6 — fixed-window CRT jet selectors

Exact checkpoint base:
75bf12b76014da6ea983ac1dc8083aaac79132ce.

The local-jet/global-observable gate now has an exact finite-window solution
conditional on the complete denominator-event manifest. Confluent CRT
polynomials \(W_1,W_2\) annihilate every nontarget actual pole and give

\[
\frac1{2\pi i}\int W_1\frac F{F'}=\sum\rho_c^{\rm jet},
\qquad
\frac1{2\pi i}\int W_2\frac{F^2}{F'F''}
=\sum(\rho_c^{\rm jet})^2.
\]

At an order-\(r\) target, the second selector uses
\(r(z-c)^{2r-2}\) modulo \((z-c)^{2r-1}\). Omitting \(r\) leaves only
\(\rho^2/r\); squaring the first weighted flux creates a double pole and can
have zero residue.

The polynomial corollary constructs all-odd-stratum carriers by exact
square-free decomposition and CRT without root finding. It is explicitly
scoped as an all-root trace encoder, not an arbitrary rational real-window
projector.

Exact replay:

    PASS_T105105_FIXED_WINDOW_CRT_JET_SELECTORS
    16/16 focused tests in normal and optimized Python
    digest 3edde4fdb651ae0c3781e4f832884f0d7c81247edd3b5a151c6b2c54f051cf05

Xi event manifests, selector norm/weighted-edge estimates, multiplicity
defect, cofinal passage, RCMV104530, and RH remain open.
