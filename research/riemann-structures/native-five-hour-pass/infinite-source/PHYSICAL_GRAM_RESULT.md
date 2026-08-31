# A directed frame in the original infinite physical norm

Research theorem packet. The prime set is exactly `{2,3,5}`. This proves a
statement about the twenty declared occupation coordinates and the original
Mellin measure; it neither identifies the retained-gamma source nor changes
the observation norm. RH remains unproved.

## Theorem

For the literal ordered, factor-two source, write

    F_infinity = Z_0 + sum_(j=1)^20 M_j Z_j,
    T_infinity v = sum_(j=1)^20 v_j Z_j.

Then, for every real vector v,

    ||v||_2^2 / 12000000 <= ||T_infinity v||_(L2(nu))^2 <= 68 ||v||_2^2.

The exact source and measure are authenticated by the three commit/blob
bindings in `physical_infinity.py`; in particular the ordered twenty-moment
note is blob `2113ce2bef593e19ca647c12c4fbb3c0728572a2` at commit
`69b5322bc872b46d42d4f74e13dcbeb96c1421da`. The measure mass is
`nu_0=128(3+sqrt(2))*log(2)-288`. A Euclidean norm appears only on the
declared source-coordinate domain. The range norm is the unchanged physical
`L2(nu)` norm, not the Euclidean norm of selected Fourier coefficients.

## Complete finite algebra for an infinite source

Put `z_p=p^(-1/2+it)`, `A(z)=sqrt(1-z^2)`,
`D(z)=sqrt(1-z)-A(z)` and `phi_a=product_p A^(1-a_p)D^a_p`.
The exact integer decoder satisfies

    2 integral x^b d(x^a) = d_(0,a,b) + sum_j d_(j,a,b) M_j,
    Z_j = sum_(a,b) d_(j,a,b) phi_a conjugate(phi_b).

Every one of the 64 ordered pairs is retained. The tests independently
integrate all those monomial currents on three rational power paths and
check the ordered reversal identity. No factorial or symmetry quotient is
inserted.

Let `Q=(A^2,AD,D^2)`. With `g=(1-z)sqrt(1+z)`, these are exactly

    Q_0=1-z^2, Q_1=g-(1-z^2), Q_2=2-z-z^2-2g.

For `alpha in {0,1,2}^3`, let `U_alpha=product_p Q_(alpha_p)(z_p)` and
`K_(alpha,beta)=integral U_alpha conjugate(U_beta) dnu`. The physical
affine Gram is the finite contraction

    G_(j,k)=sum_(a,b,c,d) d_(j,a,b)d_(k,c,d) K_(a+d,b+c).

The order `a+d,b+c` follows from `Z_j conjugate(Z_k)` and is checked
against a separate enumeration of every ordered record in a degree-one
primitive model. Covariances are real by conjugation and evenness of nu.
The 20-by-20 direction Gram is the submatrix j,k=1,...,20.

## Directed treatment of all omitted exponents

Local Q-products are truncated at degree L. If `c_n=[z^n]sqrt(1+z)`, the
exact recurrence computes `g_n=c_n-c_(n-1)`. For n>=2 the magnitudes of
g_n decrease. Consequently the omitted absolute q-series is bounded by

    T_L(q)=|g_(L+1)| q^(L+1)/(1-q),

and the local three tails are `(0,T_L,2T_L)`. The producer uses the exact
prefix absolute mass plus that tail as its full mass bound. Product
telescoping gives feature bounds M_alpha and eta_alpha for the full
supremum and omitted supremum respectively. Thus a valid covariance error is

    nu_0 (eta_alpha M_beta + M_alpha eta_beta).

This formula follows by subtracting the two products using one full factor
and one prefix factor; both are bounded by M. It does not discard a
tail-tail term. The producer adds this error before contracting the exact
decoder.

Each finite covariance is evaluated by complete difference-frequency
correlations and the exact autocorrelation Gamma of the three-piece kernel
in L-102880. Support decisions use integer comparisons between the ratio
numerator and denominator, including the exact boundary ratio eight.
Radicals and logarithms use outward Arb arithmetic. No time quadrature,
floating support classification, or approximate positivity projection is
used. A local Q-product cutoff is not the physical horizon `nm<=H`.

The reshuffled approximate matrix is not assumed positive. Interval LDL
on the true-Gram enclosure proves all twenty pivots positive. A directed
inverse gives `lambda_min(G)>=1/||G^(-1)||_infinity`; the maximum row sum
gives the upper bound. Symmetry is a proved source identity, and opposing
entry intervals are separately checked to overlap.

## Acquisitions and independent replay

The registered L64/192 attempt refuses at LDL pivot 13 and is retained as
`physical_infinity_L64_p192.acquisition.json`. That refusal is not evidence
of a negative true eigenvalue. L96/192 and L128/256 pass. Their independently
acquired enclosures overlap in all 441 affine entries. L96 certifies a
lower bound exceeding `9.0008890e-8` and an upper bound below `67.858533`,
which imply the conservative rational theorem constants.

The L96 capture has SHA256
`e828069e8898a464741553a44f53a13bb11d93c5c27ed5475130656a99749757` and its
producer has LF SHA256
`9eaad7aac963f0ad13d2d4a2656258bf172e61fc51fbb5af74a0aff7f1b13207`.
Those exact bytes are input-bound by the separate variational and horizon
consumers. The producer's acquisition status deliberately remains unchanged;
this review note records the subsequent replay.

Root independently replayed L96 in ordinary and `-O` Python and L128/256
in ordinary Python, reproducing the complete exact captures. The nine
primitive/orientation/measure controls pass ordinarily and under `-O`.
The source/tail/contraction proof and implementation were separately read
by the native variational agent, which found no mathematical blocker.
The L96 and L128 replays used streaming slabs and completed in seconds.
No dense large-horizon record array was built.

Commands, from the branch root:

    python research/riemann-structures/native-five-hour-pass/infinite-source/physical_infinity.py --check 96
    python -O research/riemann-structures/native-five-hour-pass/infinite-source/physical_infinity.py --check 96
    python research/riemann-structures/native-five-hour-pass/infinite-source/physical_infinity.py --check 128 --precision 256
    python -m unittest discover -s tests -p test_native_infinity_physical.py

The task-local binary dependency is python-flint 0.9.0. No system Python
package was replaced. The L16/L32 files remain explicitly labelled floating
reconnaissance and supply no theorem sign.

## Original-horizon consequence

`physical_horizon_tail.py` separately authenticates the L96 capture and
its producer before using this lower bound. Its positive coefficient tail
counts every smooth product and every ordered-pair contribution. The
registered test passes at H=2^48 and proves

    ||T_H v||^2 >= ||v||^2 / 48000000  for every H>=2^48.

The complete statement joining this to the old finite certificates is in
`variational_ALL_HORIZON_FAITHFULNESS.md`: rank twenty at every integer
H>=450. The old selected minor's limiting rank defect remains true.
Neither result says that an arbitrary twenty-vector is attainable by a
monotone source path or that the constants persist when primes are added.
