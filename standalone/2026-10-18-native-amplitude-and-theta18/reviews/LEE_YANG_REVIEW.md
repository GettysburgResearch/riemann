# Independent analytic and interval review of T18C

Reviewer: the native Newton/amplitude track, separate from the Lee–Yang
author and the root agent's independent graph-transfer implementation.
The author's files were read only.

**Finding:** no substantive mathematical defect found in the finite
degree-18 theorem, the full-theta moment enclosures or the rational
contraction argument. The result concerns a new connected finite Ising
model. It neither identifies its characteristic function with the theta
transform nor supplies an unbounded-order extension rule.

## Reviewed identities

The following computational files and receipt were inspected:

| File | SHA-256 |
| --- | --- |
| `chain_parameters.json` | `69b4684910551e1dd6330253516e3ac6e8399cff634e55f1b6fcda4dbe2f8f92` |
| `chain_exact.py` | `97700436cea54899ce14027bbd9a0a02dcd0a98da7cac382d903b5d600eb189c` |
| `theta_source.py` | `75a239c2724afbd6d5ab343a00c1f3c4d1e7062eaab9ff99b0379eecde27e92d` |
| `certify_chain.py` | `5eefec31e9ab8c29c8597a6851170af824e2c07a8e2fb34ae4e806941422cae6` |
| `chain_controls.py` | `4e4899a8120f16e2900efce8840a26b57bc24d739d4e528dcb57c81fe955e9ff` |
| `pr886_primitive.py` | `2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55` |
| `tree_core.py` | `edab764577f7c4a1553d1dfb3f19b838f536ff48273aba8cf91acb4289a8577a` |
| `chain_certificate.json` | `df51d1773b151b6f89b316faa84416507b90cebb6d068ad6bd4947d1ddaac964` |

Initial proof reviewed: `PROOF.md` at SHA-256
`9173982c74846ea347391920fb2b3102d92b9e152064fa09bb032441e3d79eb1`.
A final-byte addendum below binds the subsequent prose clarification.

## Exact graph and moment map

There are 266 repeated leaves, 14 weighted core spins and one auxiliary
hub: 281 vertices and 280 tree edges. The Gibbs product
`2^(-281) product_e(1+q_e s_i s_j)` is normalized by the bijection between
the hub spin plus independent edge-product signs and the complete spin
configuration. Its graph is exactly the one in the parameter file.

The core recurrence is correct: condition on its first spin, write the
remaining observable recursively as `w_i + tau_i A_(i+1)`, and use the
independence of `tau_i` from the remaining edge products. Conditional on
the hub, the core and all leaves are independent, so their conditional
cumulants add. Averaging the fair hub preserves even moments and kills
odd moments; unconditional cumulants must then be recomputed, as the code
does. The leaf correlation is `eta*a`, so its conditional odd raw moment
is `eta*a^(n+1)`; its derivative is correctly included in the active
Jacobian. No product-law substitution is made for the correlated graph.

Root independently implemented the complete 281-spin generating function
using probability transfer and polynomial multiplication, and compared all
raw orders 0 through 20 with this map. I read that separate implementation
and its report, including its 128-state small-graph enumeration and edge
deletion controls. Those checks authenticate graph encoding; they are not
the proof of existence of the nearby exact root.

## Complete original source and tails

I freshly read the theta density and weighted Lee–Yang statements in
[Newman–Wu, arXiv:1901.06596v2](https://arxiv.org/html/1901.06596v2),
Section 2.1, equation (7), and Section 2.5, equation (21) and the following
display. The density in the replay has exactly that time-variable
normalization. Multiplicative conventions for xi cancel in the normalized
probability law.

The following analytic bounds were independently rederived:

- On every radius-1/8 Cauchy circle, the real part of `exp(2t)` is positive.
  With all six indices, `q<144` and `Re t<17/8`, the stated `10^11` bound
  for the analytic summand is valid. A real cell has half-width 1/32,
  so the discarded density series costs `4^(-121)/(1-1/4)`. The complete
  two-sided integration length is `49/4<16`; multiplying by `2^j` gives
  the displayed error for every even `j` through 20.
- For each of the six time tails, `exp(2u)>=1+2u` gives the stated positive
  decay parameter. Integrating the binomial expansion of `(U+u)^j`
  gives exactly the sum of factorial terms in the checker, with the
  full-line factor retained.
- For all omitted indices `n>=7`, the consecutive numerator ratio is
  below 1/2 and the denominator increases. The bound starts at index 7
  and includes every subsequent term. Positivity permits these tails
  to enter only the upper moment endpoint; the Taylor error enters both.

The source moments are regenerated from cell coefficients and all these
tails. Normalization uses an enclosed strictly positive mass. The variance
is then enclosed and the target is standardized by its appropriate power.
The saved source receipt and optimizer outputs are not inputs to the root
acceptance predicate.

## Directed arithmetic and source provenance

I inspected the integer floor/ceiling interval operations, the reciprocal
and square-root rules, the alternating arctangent enclosure and the
positive Taylor/exponential remainder with outward squaring. They supply
inclusion bounds for the actual operations used in the moment and
Jacobian maps. The fixed denominator is `2^320`; no ordinary floating
arithmetic decides acceptance.

A fresh fetch of #886's `primitive.py` at commit
`d998605c0718e332ac503baf078704b862f8250e` returned Git blob
`712bb0f0114cbba85e8082c3130ebf09b53e8936`, of length 6,533 bytes. The local
authenticated implementation has one additional trailing newline, length
6,534 bytes. Removing exactly that final newline reproduces the upstream
Git blob. The mathematical implementation is unchanged. The author was
asked to qualify the original phrase "copied exactly" accordingly, without
changing the frozen executable or certificate identities.

## Whole-box root and positivity

For the actual fixed theta target, the map is `z -> z-R(B(z)-s)` on nine
active coordinates. `R` is the exact rational inverse of the center
Jacobian, with both inverse identities checked. The residual bound uses
the complete interval enclosure of `s`, so it is valid for the true target
even though its components are correlated. The whole-box interval
Jacobian encloses the derivative at every point of the exact rational
cube; the outward interval enlargement is harmless.

The receipt's displacement is about `2.84*10^(-41)` and its contraction
constant about `4.31*10^(-12)`, in radius `10^(-30)`. The exact predicates
give strict self-mapping and contraction, hence a unique root in that
cube. This is a genuine existence argument, not acceptance of the
approximate rational center as an exact solution.

All observed weights, all edge correlations and all finite couplings are
controlled throughout the cube. The inequalities `q>10^(-9)` and
`q/(1-q^2)<1/4`, together with the elementary atanh integral, give the
claimed coupling bounds. The covariance of the first core pair is
exactly `w_0*w_1*q_0`, and the support bound follows from the sum of all
positive weights. The hub's observable weight is explicitly zero.

At the root, the graph has variance 1 and matches the standardized theta
law through order 18. To return to the original theta law, multiply
observable weights by `sqrt(v)` while leaving **all couplings fixed**.
In particular the parametrization `q_leaf=eta*a` is not reapplied to the
rescaled weights. The author was asked to spell out this convention.

## Real zeros and finite endpoint

The freshly read finite ferromagnetic Lee–Yang statement permits
nonnegative unequal real weights. The proof's separate positive-hub-weight
limit is also sound: the finite characteristic sums converge locally
uniformly, and their limit is not identically zero. Hurwitz therefore
preserves absence of zeros in each open nonreal half-plane.

The cumulant equations are triangularly equivalent to moment matching
through degree 18. Both direct raw order 20 and the order-20 cumulant
diagnostic are separately enclosed on the entire box; each discrepancy
lies strictly between `0.45` and `0.451`. Equality of lower cumulants
makes them agree at the root. Consequently this model does not already
realize the full theta transform.

This scoped review inspected the analytic proof, source formulas, interval
mechanism and certificate. It did not rerun the expensive complete source
calculation or provide an independent transcendental backend; the author
performed a full replay, and root is arranging another assembled-packet
replay. No unbounded-order approximation or RH conclusion is approved.

## Final-byte addendum

The final publication proof was read in full at
`research_pass2/lee_yang/publication/PROOF.md`, SHA-256
`5528524383cf68322a77e4b98292344fefb16d703dc34811f89d4527232e5d8d`.
The normalization now explicitly rescales observable weights only, leaving
all couplings fixed. The inherited primitive's one extra trailing newline
is explicitly recorded, and `SOURCES.json` includes both upstream and
local identities. The printed strict diagnostic bounds for beta and the
contraction constant were checked directly against the exact rational
receipt. The mathematical conclusions and the finite scope are unchanged.

All eight computational and receipt files listed above are byte-identical
in the publication copy. The finding of no substantive defect applies to
these final proof bytes and the listed computational identities. This
addendum does not claim an additional full-source execution by this reviewer.
