# Certified endpoints of two positive-root extension steps

Status: **PROPOSED finite existence theorems with directed certificates.**
The endpoints below were found by the moving-root construction in
`extension/POWER_SUM_EXTENSION.md`. The complete continuation paths are
numerical; each endpoint existence theorem has a separate complete interval
certificate. No infinite extension or new zeta zero-free boundary is claimed.

## 1. The stronger finite endpoints

There are even entire functions of the form

\[
 P_N(z)=e^{-az^2}
       \left[\prod_{j=1}^{N-20}(1-b_jz^2)\right](1-xz^2)^{20},
 \qquad a>0,\quad b_j>0,\quad x>0,                     \tag{1}
\]

which match the actual variance-one normalized Xi function H as follows:

| Matched Taylor order | Factors N | Degree of the polynomial factor |
|---|---:|---:|
| 24 | 84 | 168 |
| 26 | 104 | 208 |

Both have only real zeros and obey

\[
                  |P_N(z)|\le e^{|z|^2/2}
                      \quad\text{on the whole plane}. \tag{2}
\]

The physical Xi approximants are `P_N(sqrt(v_theta) z)`, as in
`PROOF_GAUSSIAN.md`. No probability-density representation is assumed.

These factor counts improve on the separate 128-factor order-24 and order-26
certificates. The producer also supplies an actual two-step incremental
search: 64 factors at order 22, then 84 at order 24, then 104 at order 26.
Each step appends 20 equal positive roots and moves selected old roots to
preserve the earlier powers. This is a successful empirical construction
chain, not only independently initialized higher-order fits. The endpoint
certificates below do not certify its intervening paths.

## 2. Exact equations and the parameter cubes

Use the same complete-source target Q_r as the main Gaussian proof. For the
endpoint matching order 2M, set

\[
 a=\frac12-\sum_{j=1}^{N-20}b_j-20x.
\]

The finite equations are

\[
                \sum_{j=1}^{N-20}b_j^r+20x^r=Q_r,
                            \qquad 2\le r\le M.       \tag{3}
\]

`incremental_parameters.json` specifies the two complete exact rational
centers, each including 20 identical final centers for x. There are M-1
active old nodes, varying independently in the full closed infinity-norm
cube of radius `10^-50`. Their zero-based indices are:

| Endpoint | Active old-node indices |
|---|---|
| 84 factors, order 24 | `0, 1, 2, 4, 12, 3, 16, 14, 5, 17, 6` |
| 104 factors, order 26 | `0, 1, 2, 4, 9, 3, 11, 5, 25, 20, 29, 12` |

Every other center is fixed, including all 20 copies of its endpoint's x.
The useful center values are:

| Endpoint | Common new node x | Gaussian parameter a | Smallest node |
|---|---:|---:|---:|
| 84 / order 24 | `0.0013973139741951181` | `0.06523527090391532` | `0.0002990452313572408` |
| 104 / order 26 | `0.0008920433980003671` | `0.05779857340028779` | `0.0002826378218144249` |

These decimals describe the rational centers. The checker proves strict
positivity over each entire cube, not merely at its center.

The checker calls the previously reviewed `check_gaussian.check_model` for
each declared order and factor count. It recomputes every term in each power
sum, every whole-cube Jacobian entry, and the full rational preconditioner
action, using the authenticated complete theta source. The additional wrapper
explicitly checks that the 20 cloud nodes are identical and none is active.

The upward directed bounds are:

| Endpoint | Upper bound for `||R f(center)||_infinity` | Upper bound for `sup_cube ||I-R Df||_infinity` |
|---|---:|---:|
| 84 / order 24 | `4.499e-90` | `1.749e-36` |
| 104 / order 26 | `1.231e-87` | `9.236e-35` |

For both models, `beta+L*10^-50 < 10^-50` and `L<1` hold by exact rational
arithmetic. Consequently `y -> y-Rf(y)` is a contraction strictly into its
parameter cube. As proved in the main Gaussian note, the derivative bound
also establishes invertibility of R, so the unique fixed point solves (3).
The source contains the actual theta target, including all analytic
remainders. The logarithmic coefficient identity gives the claimed matching,
positivity gives the exact real zero locations, and the sum identity defining
a gives (2).

Each exact solution may differ from its center in the active old nodes. The
certificates make no assertion that those solutions lie on the numerical
paths used to find the centers, or that the second certified solution
continues the first certified solution along that same path. The fixed
20-fold cloud structure of each endpoint is retained exactly.

## 3. Search provenance and its limits

The curated `extension/power_extension_candidates.json` retains the complete
84-, 88-, and 96-node order-24 centers, targets, provenance, and crossing
summaries. The selected 84-node producer used 20 new roots and 35 changes of
active anchor set. `extension/power_extension26_candidates.json` retains the
104- and 148-node order-26 alternatives and explicitly identifies the prior
84-node numerical endpoint as their starting input. The selected 104-node
producer used 20 new roots and 20 changes of active anchor set.

Tiny ordinary-Decimal residuals were only search acceptance conditions. They
are not assumptions in either endpoint proof. Likewise, the unused numerical
alternatives are not covered by these certificates.

`produce_incremental_certificate.py` selects the 84- and 104-node centers and
prepares their rational preconditioners. It uses ordinary Decimal arithmetic
and floating-point QR, restricted to the old-node columns. The directed
checker verifies each resulting cube regardless of how its preconditioner
was found.

Two successful extension steps do not guarantee that every later target gap
has the required sign or fits within available collision-free anchor ranges.
Those gates and the relevant exact continuation identities are stated in the
companion proof. The weaker weighted all-order consumer in
`WEIGHTED_CANONICAL.md` supplies another way to avoid unit-root restrictions;
its cofinal feasibility also remains open.

## 4. Replay

From this theta directory in the repository:

```sh
python -O check_incremental.py
```

The default source path is the pinned earlier theta packet. In another staging
layout, pass `--source /path/to/pinned/theta`. The receipt is
`incremental_certificate.json`. To reconstruct its rational parameters without
overwriting the checked input:

```sh
python produce_incremental_certificate.py --output /tmp/incremental_parameters.json
```

The wrapper and imported checker use explicit guards, which remain active
under Python optimization. Their source hashes, source-data hash, primitive
hash, input hash, full source intervals, and directed endpoint bounds appear
in the receipt.
