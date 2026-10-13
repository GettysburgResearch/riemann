# The remaining finite short-trace contract and its exact source price

Status: an explicitly OPEN analytic contract, with proved implication and
incidence pricing. No complementary trace estimate, new moment theorem,
or new zero-free region is asserted.

## CT1. Literal finite family, row range and exclusions

Import the exact source family, all-order incidence decomposition and
controlled critical sectors in P8 of `PRIME_SLOT_CANCELLATION.md`, SHA256
`d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`.
Fix k, source ray data, fixed smooth norm tests supported in `[a,b]`,
`h=1+theta` with `0<theta<=1/10`, `H=D^h`, and `Y=bD`.
Every allocation below is the actual pairwise coprime squarefree family
q_I over subsets I of the r=2k labeled Hermitian slots with |I|>=2.
Define `c_i=product_(I contains i)q_I`, `Q=product_I q_I`, require
Nc_i<=Y, and retain exactly the exterior source character omega_q(u).
An exponent divisible by six keeps its principal nonunit zero mask.
All fixed nu factors and source Möbius signs are retained outside the trace.

Fix 1/3<sigma<1/2. Let T_i,Y be the literal coefficient truncations SC2,
not an arbitrary coefficient class. Let Q_coll be the exact rational
finite collision factor SC1. The source spatial Phi is Schwartz, and all
rows u!=0 are retained with their original norm scaling Phi(u/sqrtH).

The exact filtered short representation is frozen in
`SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`, SHA256
`c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac`.
Its whole-integral identity does not claim pointwise identity with the
original finite Euler integrand.

## CT2. OPEN complementary-frequency target

Fix any allowed positive width kappa in WT1 of
`WIDE_SUBCRITICAL_TUBE.md`, SHA256
`53568631060432784811d8474e8d774257664826e8fb9fa59c0ba47959745f02`.
Let T_Y be precisely that common conjugate tube. The target S(k,h,sigma)
is the following: for every epsilon>0 there exist fixed B,C, independent
of D, the moving allocations, and all independent frequencies, such that

\[
 \left|\sum_{u\ne0}\Phi(u/\sqrt H)\omega_q(u)
     Q_{\rm coll}(\sigma+i\mathbf t)
                  \prod_{i=1}^{2k}T_{i,Y}(\sigma+it_i)\right|
 \le C H D^\epsilon\prod_i(1+|t_i|)^B,
               \qquad\mathbf t\in\mathbb R^{2k}\setminus T_Y.
\tag{CT1: OPEN}
\]

There is no physical norm test or c_i length scale inside this trace.
The cutoff of each literal T_i is the common Y, even when the eventual
filtered column length D/Nc_i is shorter. The assertion supplies every
exact incidence allocation, its moving mask, the one common row range,
and independent left/right frequencies. It is stronger than a bound for
one filtered moment or only the fully coprime leading face.

On T_Y, WT5 and SC5 already bound the same short trace by O_M(HY^(-M))
for every fixed M, after complete Schwartz row summation. Thus CT1, if
proved on the complement, extends to all frequencies. This is a paid
frequency component and an unpaid target; it is not permission to drop
the complement from the actual source integral.

## CT3. The exact below-half incidence cost

The elementary source norm identity gives

\[
 \prod_i(Nc_i)^{-\sigma}
 =\prod_I(Nq_I)^{-|I|\sigma}\le(NQ)^{-2\sigma},\qquad
 (NQ)^2\le\prod_i Nc_i\le Y^{2k}.
\tag{CT2}
\]

Hence NQ<=Y^k. Each eligible squarefree Q has at most m^(omega(Q))
allocations, with the fixed integer m the number of allowed subsets I.
The complete fixed-order divisor bound gives this multiplicity at most
C_delta (NQ)^delta. Fixed-field ideal counting and partial summation
therefore prove

\[
 \sum_{\rm eligible\ allocations}\prod_i(Nc_i)^{-\sigma}
 \ll_\epsilon Y^{k(1-2\sigma)+\epsilon}.
\tag{CT3}
\]

Choose the preliminary delta smaller than epsilon/k. This argument uses
the complete source allocation census, not a prime-only substitute,
and preserves same-side and cross pair labels. Higher-cardinality
incidences only decrease the displayed positive upper bound.

## CT4. Conditional full moment and signed remainder

Apply the exact finite short Mellin identity to each allocation. If CT1
holds, integrability of the fixed smooth transforms gives

\[
 |\text{one incidence contribution}|
 \ll H D^{2k\sigma+\epsilon}\prod_i(Nc_i)^{-\sigma}.
\tag{CT4: conditional}
\]

Combining CT3 and D comparable to Y cancels the below-half incidence cost:
`2k sigma+k(1-2sigma)=k`. After assigning smaller preliminary losses,

\[
 M_{2k}^{\Phi}(D,H)\ll H D^{k+\epsilon}.
\tag{CT5: conditional}
\]

The source sharp moment is bounded by its actual smooth majorant.
The imported PR914 controlled sectors then give the literal signed
R_k=O(H D^(k+epsilon)), exactly as in P14–P15. No arbitrary divisor-bounded
coefficient hypothesis has been introduced.

## CT5. Source extraction price and what remains open

More generally an additional D^a on the right of CT1, a>=0, gives the
same additional D^a in CT5. The literal all-order family is frozen in
four-hour-wave `literature/GENERALIZED_MOMENT_ATTACK.md`, G1–G2, SHA256
`923fac6659314cff53319a80207d1aca7b58d90a154efec4f6de31844f21e94e`.
The extraction is imported from PR915's fixed universal Mellin test and
positive-density sixth-power replicas in `LOG_FREE_REPLICATED_SPIKES.md`,
Theorem 2.1 and Section 4 equation (4.6), SHA256
`b59978c1c5d3b5cb904c7f22d675a67bb71b2af512db9f0577e568a04565a86b`.
It prices the conditional estimate at precisely

\[
 \Re s>\frac12+\frac{5h}{12k}+\frac{a}{2k}.
\tag{CT6: conditional}
\]

Neither CT1 nor CT5 nor a new boundary is proved. The new completed
reduction identifies a finite literal short family, proves its negligible
common conjugate component, and prices the remaining independent-frequency
trace with the exact incidence cost. Pointwise collision decay or paired-plane
estimates do not supply CT1; their local indefinite kernels do not support
an automatic positive-kernel Cauchy extension.
