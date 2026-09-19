# Newton extension as orthogonal arithmetic innovations

**NIR26: PROPOSED component proofs; RH and the unbounded native gain remain OPEN.**
This continues the actual BNR26 packet in PR848, not a conjectured breakthrough
in an interrupted trace. All ten parent files remain unchanged.

The useful connection is a change of coordinates in the SAME physical norm.
With `m(k)=sum_(n<=k)mu(n)/n`, the one-safe-point optimum of PR836 is exactly

    F_Y=E_Y+(Y+1)u_Y^2=sum_(k=1)^Y m(k)^2.

The two-moment state from BNR26 obeys F_Y<=A_Y<=2F_Y. Its normalization price
has not disappeared: it is the constant component of the reciprocal partial
sums. In fact E_Y is their exact variance, including m(0)=0.

## What the new coordinates buy

For a finite source a, its complete causal norm factors as

    J(a)=sum_(k>=0) (P_a(1)-m_a(k))^2.

At P_a(1)=0, m_a(k) are orthonormal coordinates. The canonical source is now

    c_Y(n)=mu(n), n<=Y;  c_Y(Y+1)=-(Y+1)m(Y),

with no other coefficient. One reciprocal moment is enough: the raw Newton
source v=2c_Y-1*c_Y*c_Y still has a bounded cumulative tail, zero reciprocal
moment, and finite WHOLE energy. Removing its coordinates above B=(Y+1)^2-1
is exact orthogonal projection:

    projection(v)=c_B,
    J(v)=F_B+sum_(k>B)m_v(k)^2.

There is no factor-two recompletion loss and no resetting a distribution.
The retained coefficients are exactly mu(n) through B, generated from the
short input. The omitted coefficient b^2 remains outside that claim.

## The all-integer nonlinear map to attack

For b=Y+1, x_r=m(r), and H_j=sum_(l<=j)1/l, set

    D_k(r,s)=H_floor(k/(rs))-H_floor(k/((r+1)s))
             -H_floor(k/(r(s+1)))+H_floor(k/((r+1)(s+1))).

Then the full next energy is EXACTLY

    F_(b^2-1)=F_Y+sum_(k=b)^(b^2-1) |x^T D_k x|^2.

This uses only the prescribed short source. The mixed differences remove the
separated logarithmic main term but retain every signed integer hyperbola
boundary. The native vector is distinguished by the explicit triangular
system in PROOF.md (20), not by a random-sign model.

A fixed subquadratic gain in F across this square-scale map would imply RH.
Even vanishing gains can suffice if they accumulate nonsummably with the stated
loss budget. Neither gain is proved. The new target has the same arithmetic
strength as the parent's target, up to constants; a better coordinate is not
an excuse to call that estimate solved.

## Claims and scope

| Claim | Supplied result | Essential limit |
|---|---|---|
| NIR26-1 | Exact full-norm isometry, orthogonal atoms, variance/mean identity | Classical algebra; no bound on the native energy |
| NIR26-2 | Single-coefficient optimal completion and norm-one projection | Preserves P(1)=0, not zero total coefficients |
| NIR26-3 | Whole infinite quadratic source and explicit physical/coordinate tails | Well-definedness is not a small norm |
| NIR26-4 | Exact native square-scale map in mixed-difference coordinates | No unknown future mu enters; generation is not cancellation |
| NIR26-5 | Full conditional RH chain | Native gain remains OPEN |
| NIR26-6 | Exact all-scale countermodels to generic norm substitutes | Fake sources violate the complete native divisor equations |

Read [PROOF.md](PROOF.md), especially Sections 1, 3 and 4. Attribution and source
pins are in [SOURCE_LOCK.json](SOURCE_LOCK.json). The convolution identity and
weighted hyperbola lineage are classical (Huxley--Watt); no priority claim is
made for them, the Cholesky factorization, or elementary projections.

## Actual evidence

Both [produce.py](produce.py) and [verify.py](verify.py) reconstruct the declared
finite artifact without importing one another or repository modules:

    python -S -B produce.py --check result.json
    python -S -B verify.py result.json --self-test
    python -S -O -B produce.py --check result.json
    python -S -O -B verify.py result.json --self-test

The recursive ladder reaches 65535 and every generated coefficient is checked
against primitive arithmetic. Other tests include 48 complete isometries,
48 orthogonal perturbations, 300 divisor constraints, 24 sharp endpoint cases,
440 kernel panels with 28358 entries, 64 outward energy panels, 35 FINITE gain
tests, three full raw-tail enclosures, and two explicitly non-native families.

Normal/optimized reports agree; the verifier rejects twelve resealed changes
and duplicate JSON keys. It uses trial factorization, a different convolution
order, pair-kernel norms, and literal signed boundary sums. The large directed
energy panels share a documented rounding contract, not an independent analytic
proof. Both implementations have the same author.

[VALIDATION.md](VALIDATION.md) and [validation.json](validation.json) describe
actual commands and omissions. No complete repository validation, external
formal build, or all-scale arithmetic gain is claimed. The exact missing
statement is an upper bound on the native value in the displayed quartic
identity, using its complete divisor constraints before taking absolute values.
