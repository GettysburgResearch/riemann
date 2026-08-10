# Integration-wave route Rosetta stone

**Cutoff:** `2026-08-10T22:28:10Z`  
**Frozen base:** `d6409319b4041cd09bee85f55a344631508f2501`

This document maps repository acronyms and apparently separate proposals to canonical mathematical objects. An alias means that two routes share an exact object or an explicit transform. It does not mean that every claimed theorem transfers between them.

## Canonical object map

| Canonical object | Repository names and acronyms | Main PRs / claims | Exact relation | Scope warning | Current status |
|---|---|---|---|---|---|
| **CARRY-DIV**: Möbius-inverted carry divergence | carry saturation, Pascal packing, node divergence `R_X`, balanced fragmentation | #247, #272, #301, #335 | `w_X(q)=sum_m R_X(m) floor(m/q)` and `partial d=R_X` | exact finite identity; positivity is separate | VERIFIED WITH FIXES |
| **GREEN-POLICY**: size-biased descending Markov occupation | fragmentation producer, Green occupation, policy debt, Cycle Debt dual | #292, #335, #356 | `M-MP=s`; feasible flow and occupation are equivalent for a realizable policy | a stationary characteristic does not cover adaptive policies | VERIFIED WITH FIXES |
| **FROZEN-BT**: half-binary/half-ternary policy | BTF, frozen producer, GFEP exit, first-entrance chain | #247, #292, #351, #355, #356 | same finite stationary Green chain observed at a node, first entrance, or total negative variation | PR #356 refutes this policy, not all fragmentation | REFUTED AS STATED |
| **UNIFORM-PASCAL**: internal-uniform split Green kernel | SHARP inverse, average-carry inverse, uniform Pascal occupation, local-vs-tail inequality | #326, #329, #335, #347, #356 | `P_m(k)=2k/[m(m-1)]`, hit law `2/(n+1)`, explicit Green inverse | full nonnegativity is RH-bearing; finite bands are sub-RH | LIVE |
| **LOWROW-ZS**: zero-safe two-low-row source | low-row SHARP, critical-log scalar, WSTS low-row source | #337, #348, #356 | critical-log scalar is a positive Volterra smoothing of the same source | smoothing transfers one-sided bounds only in the correct direction | LIVE |
| **ETA-CENTRAL**: reciprocal-eta central producer | eta resolvent, pure central producer, Mersenne cascade, CEV | #302, #309, #317, #337 | all-generation eta recombination equals the unique pure central-halving flow | pure-central pointwise positivity is false; noncentral cycles remain live | DORMANT BUT LIVE |
| **BOUNDARY-DEC**: actual-coordinate boundary decoder | Möbius adjacent decoder, source-to-carry decoder, terminal commutator | #301, #303, #312, #304 | exact decoder retains gcd and noncoprime destinations | formal modal/Hausdorff positivity does not imply decoded positivity | VERIFIED WITH FIXES |
| **BOUNDARY-OPT**: optimized carry boundary norm | COBT, CEV, cycle-optimized leakage, column-capacity mass | #315, #317, #335 | linear atomic norm can map to zero/polylog optimized carry debt | never take componentwise total variation before destination recombination | DORMANT BUT LIVE |
| **SHARP-PSI**: continuum SHARP scalar | `Psi`, all-depth SHARP margin, Möbius Green trajectory | #329, #347 | `Psi(x)=4 sqrt(x)B(x)-3A(x)` and is the fixed-ratio limit of scaled carry inverse | eventual one-sign is RH-bearing | LIVE / RH-BEARING |
| **SHARP-C**: shifted-zeta bottom-tail scalar | bottom tail, one-tail gate, finite-band tail state | #347 | Mellin symbol `1/[s(s+1)(2s+1)zeta(s+1)]` | distinct from critical `zeta(s+1/2)` scalar | LIVE |
| **ENDPOINT-FLUX**: prime–radical occupancy flux | WSTS, endpoint `A(X)`, positive occupancy, mean age, prime-radical flux | #348, #351, #352, #353 | all are Green potentials or finite filters of one positive occupancy source | pointwise column sign and moving endpoint sign are different | LIVE |
| **ANN64**: zero-safe endpoint annular filter | factor-729/125/81/64 criteria, minimal phase-blind annulus | #352 | fixed polynomial in the dilation operator applied to `A(X)` | eventual sign remains RH-equivalent | LIVE / RH-EQUIVALENT |
| **PP-GAP**: complete prime-power carry gap | complete Lambda gap, prime-square moat, endpoint packing score | #352, #353 | subtracting the positive prime-square source converts prime endpoint to complete gap | `o(log^2 X)` is the open arithmetic estimate | LIVE |
| **GAMMA-CARRY**: critical endpoint/carry probability law | Gamma approximant, centered carry convex order, endpoint atom, exponential delay | #335, #353 | endpoint atom `V` equals carry law `T` plus an elementary independent delay; Gamma is target law | independent deconvolution positivity is stronger than a state-dependent coupling | LIVE |
| **Q4-SOURCE**: compact radix-four zero-safe source | Euler–Blaschke Q4, `B_4`, compact relative source, two-tap source | #325, #339, #345, #357 | finite radix-four filter of `1/zeta`, main pole removed, open-strip zeros retained | source order must follow #349/#350 corrections | VERIFIED WITH FIXES |
| **Q4-FRAME**: plus/minus all-pass current frame | Q4 pair, parity frame, tight ordinary current frame, root-Haar pair | #325, #346, #350 | two filtered channels reconstruct the ordinary current with exact critical-line norm identity | frame identity alone supplies no dissipative sign | VERIFIED WITH FIXES |
| **Q4-JORDAN**: vector source curvature | vector Jordan curvature, compact Schur row, augmented parity curvature | #345, #350, #357, #359 | Hermitian `2x2` curvature combines reserve, current, and source legs | diagonal/trace/determinant data do not imply full current control | LIVE |
| **Q4-STATE**: reflected two-state recurrence | RDP, QIDR, critical-Haar ledger, coefficient-one recurrence | #325, #341, #342, #357, #359 | same current-scale/delayed-scale state after exact all-pass synthesis | recurrence remains unproved | LIVE |
| **PIG**: positive compact innovation energy | positive innovation gate, filtered Chebyshev mean square, final product block | #357, #359, #362 | exact radix-four finite difference of `E(x)=psi(x)-x`, with logarithmic gauge | in corrected Q4 assembly, PIG is RH-equivalent | LIVE / RH-EQUIVALENT |
| **BRN-RAW**: raw Brownian Dirichlet average | raw gamma truncation, Dirichlet mean, reciprocal Hermite interpolation | #296, #343 | beta-gamma factorization reduces zeros to explicit exponential polynomial `H_N` | finite/N=2 results do not imply cofinal stability | DORMANT |
| **BRN-SYM**: symmetrized Brownian mixture | reflected-tail mixture, Robin cardinal fiber, BACS | #55, #63, #296, #318 | corrected aggregate integral of `cosh(ell z/2)+2z sinh(ell z/2)` | individual fiber stability is not closed under positive mixtures | DORMANT |
| **XI-CARD**: off-line Xi-cardinal difference | Gaussian terminal pair, Xi-cardinal source, exact finite interpolant | #199, #364, #365 | divide Xi by the off-line zero factors and take reflected difference | depends on a hypothetical off-line zero; used for a false-RH moat | VERIFIED WITH FIXES |
| **GABOR-CAP**: finite critical-frame capture | Gabor packet, strip RKHS capture, Schur target moat | #363, #364, #365 | minimum interpolation cost is controlled by one global source and decays like `1/L` | fixed support is not uniform over arbitrary growing packets | VERIFIED WITH FIXES |
| **JET-GRAM**: confluent invariant packet metric | Newton divided differences, Hermite jets, cluster renormalization | #366 | raw coalescing evaluation Gram converges after Newton transform to a positive jet Gram | fixed order is closed; order `O(log T)` is open | DORMANT BUT LIVE |
| **KERNEL-FLOOR**: complete Schur-corrected arithmetic floor | corrected kernel floor, radical synthesis, complete-kernel classifier | #199, #365, #366 | false RH yields a fixed negative Xi-cardinal moat in any complete hierarchy | after zero-side capture, the floor is RH-equivalent | LIVE / RH-EQUIVALENT |
| **Z23-2TRACE**: Anthropic signature-moment architecture | zeta-23, Gabor/Fejér compression, first trace/Frobenius square | #358, #361 | rank/inertia lower bound depends on two aggregate spectral statistics | upstream theorem is source-pinned; native extensions need review | LIVE |
| **WINDOW-COLLAPSE**: finite window-bank no-gain | co-lattice multiwindow collapse, finite no-alias multirate collapse, coherent spectrum collapse | #358, #360, #363 | aggregate profile or coisometry preserves the relevant spectrum | growing irregular or prime-resonant banks are outside the class | VERIFIED WITH FIXES |
| **CAYLEY-CURRENT**: boundary-current RH criterion | Cayley sign theorem, Herglotz current, current-energy obstruction | #54, #184-#188 | local Cayley transform rewrites the same boundary sign/current | compact criterion is RH-equivalent | ARCHIVAL FRONT DOOR |

## Acronym dictionary

| Acronym / label | Expansion or repository usage | Canonical object |
|---|---|---|
| BTF | binary–ternary weighted negative variation theorem | FROZEN-BT / GREEN-POLICY |
| MPR | pointwise mixed producer recurrence | GREEN-POLICY; a finite atomic policy variant |
| GFEP | Global First-Entrance Positivity | FROZEN-BT |
| DCD | descendant/cycle debt, depending on branch vocabulary | BOUNDARY-OPT / GREEN-POLICY |
| COBT | Cycle-Optimized Boundary Transference | BOUNDARY-OPT |
| CEV | Critical Eta Variation | ETA-CENTRAL / BOUNDARY-OPT |
| RMBR | Reflected Mersenne Boundary Recurrence | ETA-CENTRAL |
| MCF | Mersenne-Collar Fragmentation | fixed support subclass of ETA-CENTRAL; dead cofinally |
| SHARP | average-carry inverse positivity / carry saturation | UNIFORM-PASCAL |
| WSTS | theta-bridge weighted sign theorem | ENDPOINT-FLUX / LOWROW-ZS |
| PMSD | Principal-Mode Schur Descent | dyadic source-complete matrix descendant of Q4-SOURCE |
| CISR | Coupled Interior Source Recurrence/matrix | Q4-JORDAN predecessor from ordinary-prime carry window |
| RDP | Reflected Dissipative Placement | Q4-STATE |
| QIDR | Q4 inertia/dissipative recurrence terminology | Q4-STATE |
| PIG | Positive Innovation Gate | PIG |
| BACS | Brownian Aggregate Canonical System | BRN-SYM |
| RCM | reflected cardinal domination/mixture claim | BRN-SYM; false for finite N |
| GCF | Gamma-carry factorization/equality obstruction | GAMMA-CARRY |
| ESGS / ESBT | older endpoint-scale greedy/slack targets | superseded by PP-GAP signed score |
| BLNRZ | Brownian local/aggregate real-zero target | BRN-SYM |
| N-UNI | finite-update uniform reservoir no-go | dead producer mechanism class |

## Exact alias chains

### 1. SHARP ↔ uniform Pascal Green occupation

For the internal-uniform size-biased split,

```text
P_m(k)=2k/[m(m-1)],
Pr_m(hit n)=2/(n+1),
M_n=s_n+2/(n+1) sum_{m>n}s_m.
```

The average-carry inverse coefficient is a positive scalar multiple of `M_n`. Therefore:

```text
SHARP coefficient c_X(n) >= 0
<=> uniform Pascal signed Green occupation M_n >= 0
<=> explicit local-vs-tail inequality for R_X.
```

The equivalence does not imply the sign.

### 2. Low-row critical-log scalar ↔ SHARP source

The zero-safe source

```text
omega=(epsilon-delta_2)*(2epsilon-delta_2)*mu
```

appears in both routes. The critical-log scalar is related to its square-root hinge scalar by a positive Volterra transform in logarithmic time. Thus these are source aliases with different consumers, not independent arithmetic inputs.

### 3. Fragmentation ↔ Markov occupation ↔ Cycle-Debt dual

Size-weighting a balanced split flow gives a descending Markov kernel. Its node equation is `M-MP=s`. Every normalized dual potential factors through a policy-capacity drift `theta d_G`, with `0<=theta<=1`. Hence:

```text
negative optimized Cycle Debt
= worst bounded policy-drift pairing
<= negative Green occupation for one chosen policy.
```

The inequality is one-policy upper control, not an equivalence between every producer and every policy.

### 4. WSTS ↔ endpoint ↔ annulus ↔ occupancy

The minimal prime endpoint scalar has one positive occupancy source. WSTS is a differentiated/weighted endpoint statement; factor-64 criteria are finite dilation filters; Gamma criteria are positive kernel potentials; and the complete prime-power gap subtracts the explicit prime-square source. These should be one integration family with four theorem packets: source, transforms, consumers, and firewalls.

### 5. Q2/Q4 source aliases

The root-Haar complement, Q2/Q4 all-pass pair, odd-parity jet, and compact radix-four source are finite local-filter presentations of the same principal `1/zeta` current after source-order correction. The exact source order is load-bearing: convolving a formed current is not the same as differentiating a filtered Dirichlet system.

### 6. Xi-cardinal ↔ Gabor capture ↔ corrected floor

Under false RH, the Xi-cardinal difference is a global negative Weil direction. Compact finite interpolation and critical Gabor truncation capture its target vector. Newton jet coordinates remove finite collision artifacts. The corrected-kernel floor is the arithmetic claim that would forbid this captured negative direction. These are successive interfaces, not independent proof proposals.

## Non-alias warnings

The following pairs look similar but must remain distinct.

1. **Finite SHARP band versus all-depth `Psi` sign.** The former is exact finite arithmetic; the latter is RH-bearing.
2. **Shifted-zeta bottom tail `C` versus critical SHARP scalar `Psi`.** Their zeta arguments differ by one half.
3. **Corrected one-fiber Robin stability versus aggregate mixture stability.** Positive superposition does not preserve the zero set.
4. **Negative inertia versus positive current energy.** One cannot be substituted for the other.
5. **Finite packet Gram conditioning versus growing-order cofinal conditioning.** PR #366 closes only fixed finite clusters.
6. **Finite atomic policy no-gap versus adaptive/continuum policies.** PR #356 does not cover the latter.
7. **Upstream zeta-23 theorem versus repository short-window/conductor extension.** They have different verification status.
8. **Artifact hash consistency versus mathematical certification.** A matching hash only identifies the bytes.

## Suggested canonical identifiers for the next integration

```text
OBJ-CARRY-DIV
OBJ-GREEN-POLICY
OBJ-FROZEN-BT
OBJ-UNIFORM-PASCAL
OBJ-LOWROW-ZS
OBJ-ETA-CENTRAL
OBJ-BOUNDARY-DEC
OBJ-BOUNDARY-OPT
OBJ-SHARP-PSI
OBJ-ENDPOINT-FLUX
OBJ-ANN64
OBJ-PP-GAP
OBJ-GAMMA-CARRY
OBJ-Q4-SOURCE
OBJ-Q4-FRAME
OBJ-Q4-JORDAN
OBJ-Q4-STATE
OBJ-PIG
OBJ-BRN-RAW
OBJ-BRN-SYM
OBJ-XI-CARD
OBJ-GABOR-CAP
OBJ-JET-GRAM
OBJ-KERNEL-FLOOR
OBJ-Z23-2TRACE
OBJ-WINDOW-COLLAPSE
```

Claims should point to one canonical object identifier plus a transform/consumer relation. This prevents the same scalar, Green occupation, or current-energy obstruction from being counted repeatedly under new acronyms.
