# MHB32 — Mellin–Hankel bandwidth control

**Proposed mathematics, not RH completion. Independent mathematical review is required.**
Continuation of strategy #902 and draft #904. Date: 21 September 2026.

The previous MCB31 executable packet really landed at
`aaea3f9605a430600bea0189397d93ca315b5f98`. Its mathematical proof and four
executable/receipt artifacts were checked against the companion archive by
Git blob identity. Both complete local reconstructions and both 12-method
suites were freshly replayed on Linux. The publisher's older Windows symlink
error is preserved as historical scope, not relabelled a pass.

## Actual mathematical change

For the **same** complete smoothly selected microscopic contribution U on
[X,M], X<=M<2X, X>=8H, supported source length L with L^2<=8X,

```
old MCB31:  sum |U(k)|^2 <= 2^21 H^4 E_local^2,
new MHB32:  sum |U(k)|^2 <= 2^60 H^(191/82) E_local^2.
```

Here 191/82=2.329268... and E_local is the previously defined recent
reciprocal-source energy, including completion costs. The entire selected
function is squared after summation: all its covariance is included.
The constants are deliberately coarse. Keep the minimum of the two bounds;
the new constant is much worse at the tested small H.

The estimate follows from an exact centered Müntz/Hankel representation,
uniform oscillatory bounds for its Mellin symbol, and the **imported**
Patel–Yang zeta exponent 27/164. It does not establish new zeta subconvexity.
It closes the centering and transform-domain obligations for that bridge,
not the remaining arithmetic estimate. Additive and Mellin projections have
not been declared commuting.

An exact rank-one term `(integral g / X)(sum c)^2` survives reciprocal
balance. A rational polynomial fixture makes it exactly 1/5; removing it
changes the answer. The transformed source appears as a complex square,
not a modulus square.

## Consequence for the whole native covariance

Combining with the complete angular complement gives

```
sum_[X,M] m(k)^2 <= C [ H^(191/82) E_local^2
                                    + K^4 (X/H) H_L^9 ].
```

Optimizing this proved inequality for the native cap-three short source gives

```
sum_[X,M] m(k)^2
 <= C (1+log X)^9 X^(191/273) (1+F_y)^(164/273).
```

The former bandwidth tradeoff had powers X^(4/5) and F_y^(2/5).
This is a quantitative change to a full-covariance bound, **not** a new
zero-free region: `191/273+(164/273)/2=1`. It still has a positive cutoff
power, and the microscopic input-energy exponent remains two. No recurrence
with subpower cutoff cost and input exponent strictly below two is supplied.

On a full native square step, recent-energy overlap yields

```
||U||^2 <=2^62 H^(191/82) (12+2ceil(log_2 H)) F_Y Delta_max.
```

The native bound making Delta_max sufficiently small, and affordable
control across every remaining bandwidth, remain open.

## Read and reproduce

Read [PROOF.md](PROOF.md), especially the retained term in Section 3,
the uniform estimates in Section 4, and the explicit limitation in Section 6.
[SOURCES.md](SOURCES.md) separates imported mathematics and copied code from
this continuation. [VALIDATION.md](VALIDATION.md) records the actual runs.

Python 3.10+ standard library is sufficient for all accepting commands:

```sh
python -S -B check.py --check results.json
python -O -S -B check.py --check results.json
python -S -B test_check.py
python -O -S -B test_check.py
```

The checker validates exact polynomial/rank identities, all source coefficients
in the declared native prefix reconstructions, directly evaluated spectral
bands, and every shell cross term. It does **not** verify the infinite analytic
proof or independently certify the imported zeta theorem.

`inherited_mcb.py` is an exact copy of MCB31's checker, renamed; `exact.py`
is its unchanged arithmetic backend. Their SHA-256 identities are enforced
before new calculations. This is reuse, not independent implementation.
The new wider-band evaluator periodically reseeds trigonometric rotations
with exact rational phases; all interval operations remain outward.

Optional nonrigorous sanity check (requires mpmath):

```sh
python -B mellin_scout.py --write mellin_scout.json
```

Its finite quadrature error is unknown. Even with the displayed analytic tail
ceiling, it is NOT a numerical Mellin certificate and is not used by acceptance.

## Finite native result and scope

Two full observation blocks are evaluated, not a complete square stage:
[128,255] using y=15 at H=1,2,4, and [512,1023] using y=31 at H=1,2,4,8.
All 640 observation cells are covered. The 1,278 future/prefix coefficient
comparisons count overlaps. The largest native endpoint is 1,023.

For the second block the actual energy is 0.0197124703956821... . At H=8,
the band energy is 0.0186124426311633..., the complete complementary energy
is 0.0010438750143420..., and twice their covariance is positive,
0.0000561527501767... . All ten cross terms among the four shells and their
complement are recorded. They have both signs.

The complementary component uses exact subtraction from the independently
checked native output; it is not another exhaustive sum of every unselected
mode. Shrinkage of this finite complement is not an unbounded-rate theorem.

No predecessor file, canonical status, formal proof, workflow or main branch
is changed by this additive packet. Publication identifiers belong in the
PR receipt, not in invented local commit claims.
