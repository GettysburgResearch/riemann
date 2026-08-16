# Independent exact-head review of PR #508

## Freeze

```text
repository:       gfreund123/riemann
review cutoff:    2026-08-15T23:51:56Z
main at cutoff:   9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
proposal PR:      #508
proposal base:    research/gpt56-pro/93600-target-lorenz-complete-successor
base SHA:         bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74
proposal branch:  research/gpt56-pro/93780-target-lorenz-directed-hardening
reviewed head:    4ae97dffd1f76ed3244b8f3028560ffa80663caf
```

This review is confined to PR #508. PR #498 is not used as confirmation or as a substitute for any Target-Lorenz interface. The retained 51,118,080-event artifact was inspected but not rerun. A small inclusion self-test was run against the exact Boost interval policy and flags declared by `X-93780`.

## Executive verdict

```text
mathematical type:  PROPOSED COMPLETE THEOREM
review verdict:     UNPROVEN / GAP
RH status:          UNPROVEN
```

PR #508 makes two real repairs:

1. `L-93780` gives credible directed decimal enclosures for `zeta(1/2)` and `zeta'(1/2)` from an explicit Euler--Maclaurin remainder;
2. `L-93783` correctly separates the positive residual source `nu`, the current-only nonnegative row bonus `B`, and the score surplus `sigma` at an already supplied Target-Lorenz leaf.

It does not close either load-bearing issue isolated by review PR #504:

1. the C++ tail sweep still lacks a valid directed transcendental inclusion contract;
2. the new typed leaf begins after the endpoint fibre has already been converted into even/odd leaf packets and therefore does not instantiate the actual endpoint-fibre-to-tree/common-parent identity.

The downstream one-quantizer, all-column, `Y_4`, and endpoint-consumer algebra remains valid only conditionally.

# I. Directed numerical hardening

## 1. Zeta primitives

At `a=100000`, `L-93780` uses the Hurwitz Euler--Maclaurin formula through `B_2`. The displayed remainder radii

\[
|R(1/2,a)|\le\frac1{24a^{3/2}}
\]

and

\[
|\partial_sR(1/2,a)|\le a^{-3/2}\left(\frac5{36}+\frac{\log a}{24}\right)
\]

are consistent with the differentiated periodic-Bernoulli integral. Python `Decimal.ln` is correctly rounded in `ROUND_HALF_EVEN`; the script uses 100-digit precision and widens every primitive and interval operation by `10^{-82}`. The final analytic remainder is much larger than the accumulated decimal-rounding allowance, and the retained intervals lie strictly inside the published six-decimal enclosures.

**Disposition:** `VERIFIED WITH FIXES`. Pin the Python and `libmpdec` versions in the result metadata.

## 2. Event and aggregation algebra

The symbolic/event architecture reconstructs:

```text
exact uint128 event ordering at x=d, jd, (j+1)d;
correct parent lower-envelope coefficients;
correct child correction envelope;
correct finite-interval derivative orientation;
correct final-tail persistence polynomial;
65 independent row outputs;
row-66 upper-at-boundary versus row-65 global lower comparison;
exact compact/tail half-open join at 166000.
```

`aggregate.py` correctly uses the **upper** interval endpoint of row 66 at the boundary and the lower endpoint of every competitor. If every primitive interval were enclosing, the aggregation would establish the published positive determinant, derivative, and row-66 separation bounds.

**Disposition:** `VERIFIED AS FORMAL INTERVAL ALGEBRA`.

## 3. Exact numerical first broken arrow

The sweep defines

```cpp
using Round = save_state<
    rounded_transc_std<long double, rounded_math<long double>>
>;
```

and compiles with

```text
-frounding-math -fno-fast-math.
```

Boost's `Rounding Policies` documentation states that `rounded_transc_std` expects the standard transcendental functions to respect the current rounding mode and warns that this is rarely the case:

https://www.boost.org/doc/libs/1_85_0/libs/numeric/interval/doc/rounding.htm

The packet contains no independent enclosure wrapper for `sqrt` or `log`, no MPFR/Arb backend, and no inclusion self-test.

The review runs the exact policy and flags on:

```text
g++ 14.2.0
Boost 1.83
x86_64 GNU/Linux
glibc 2.41
```

It returns singleton intervals for nonsquare radicands, including

```text
sqrt([2,2])
 = [0xb.504f333f9de6484p-3,
    0xb.504f333f9de6484p-3]

sqrt([67,67])
 = [0x8.2f73477d6a4563cp+0,
    0x8.2f73477d6a4563cp+0]

sqrt([166000,166000])
 = [0xc.bb72a369e3c68b5p+5,
    0xc.bb72a369e3c68b5p+5].
```

Each exact square root is irrational, whereas a finite binary `long double` is rational. Therefore each singleton interval excludes the exact value. This is an exact contradiction to the claimed inclusion contract, not a request for a slightly wider heuristic reserve.

Retained review artifact:

```text
FAIL_PR508_BOOST_ROUNDED_TRANSC_STD_INCLUSION_CONTRACT
7ffb59b9209d8d1db2527f363631708db9d4ed8ac89d45b793d2ee267d5ccfa8
```

This targeted probe does not rerun the tail sweep and does not show that the Target-Lorenz inequality is false. It shows that the retained numbers are not certified by the stated directed mechanism.

```text
Boost directed-transcendental contract  FALSE
L-93781 tail theorem                    UNPROVEN / GAP
retained all-row artifact               COMPUTATIONALLY SUPPORTED ONLY
```

## 4. Row 66 and compact/tail coverage

The half-open domains

\[
67\le x<166000,
\qquad x\ge166000
\]

are disjoint and exhaustive, with the boundary assigned to the tail. The row-66 aggregation logic is correct. The numerical lower and upper endpoints cannot be promoted to directed theorem bounds until the primitive interval backend is replaced.

**Disposition:** `VERIFIED CONDITIONAL ON A VALID TRANSCENDENTAL INTERVAL BACKEND`.

# II. Typed leaf and common parent

## 5. Leaf-local compiler

At an already supplied terminal leaf, let `E` and `O` be positive even and odd source packets, and let `U` be the leftmost even submeasure with exact odd target. Then

\[
\nu=E-U\ge0,
\qquad B=R(U)-R(O)\ge0,
\qquad \sigma=S(O)-S(U)\ge0.
\]

The direct-sum type

\[
G_\omega=(\nu_\omega;B_\omega;\sigma_\omega)
\]

correctly records

```text
nu       positive arithmetic source;
B        current-only physical row with zero source target;
sigma    declared-score surplus.
```

The exact identities are

\[
T(\nu)=T(E)-T(O),
\]

\[
S(\nu)=S(E)-S(O)+\sigma,
\]

and

\[
R(\nu)+B=R(E)-R(O).
\]

Applying the ordinary response map at `q` and `4q` before forming radix-four detail is correct. This repairs the leaf-local source/row-bonus type conflation noted by PR #504.

**Disposition:** `VERIFIED EXACT ABSTRACT LEAF COMPILER`.

## 6. Missing endpoint-fibre initialization

PR #504 asked for the initial endpoint-fibre-to-leaf identity. The new files still do not supply it.

`L-93784` starts with

\[
d\mu_X(s)=\frac{2L(X/s)}sds
\]

and then declares a stopped leaf set `L_(X,s)` with path products `omega_(s,l)`. It never defines the initial typed packet to which the stopping and causal identities are applied.

A complete derivation must specify, for almost every `s`:

1. the exact endpoint-frame fibre packet `S_(X,s)`;
2. the parameter `a` and endpoint `Z` in the paired source `P_1^(a)(Z)` of `L-91362`;
3. every initial arithmetic source coefficient;
4. the exact map from the endpoint-frame seed/density to that paired source;
5. target, declared score, literal score, all component rows, ordinary responses, radix-four responses, and boundary coordinates;
6. an equality proving that the weighted leaf sum reproduces the fibre in all coordinates.

`L-91362` decomposes an already specified paired source. `L-91650` decomposes an already specified packet family. Neither constructs the missing initial fibre. The path-product formula is exact only after the initial occurrence and coefficient are known.

The new experiment confirms the limitation: its 512 leaves are synthetic rational fixtures with hand-selected target and row ratios. It never generates the actual endpoint-frame fibre, `P_61` atoms, path weights, or native observations.

**Disposition:** `UNPROVEN / GAP` at the start of `L-93784.2`.

## 7. Density provenance

The lock pins `L-91107`, whose stated positive window ends at `c_0^{-1}<54.2192`, while `I_X` requires positivity for `1<X/s<67`. A factor-67 density theorem exists on another lineage, but its blob is not in the PR #508 tree or producer-dependency lock. This is a repairable provenance omission, not a negative density witness.

## 8. One quantizer and every column

Assume a genuine typed common parent has been proved and uses at most the native parent packet before signed comparison. Then the rest of `L-93784` reconstructs:

1. positive bottom/top omissions;
2. one scalar thinning;
3. one parent pushforward;
4. one label-blind positive quantizer;
5. common ordinary sums before detail;
6. signed mismatch/collar/terminal comparison outside the source cone;
7. every `q>=2`, including `q<K`;
8. terminal reserve `581X^{-3/2}`;
9. ordinary feasibility by positive radix-four inversion;
10. zero exported recursion and zero matrix port.

The algebra

\[
\tau_K\left(1+\frac{129}{\sqrt K}\right)
=\frac{\sqrt K+129}{\sqrt K+130}<1
\]

is correct.

**Disposition:** `VERIFIED CONDITIONAL ON THE MISSING COMMON-PARENT IDENTITY`.

## 9. Native cost and endpoint consumer

Conditional on a valid feasible row, the charges sum correctly:

```text
thinning                  <12012
nonterminal comparison    <4
terminal comparison       <48972
positive omissions        <1
port/base                  0
--------------------------------
total                      <60989 <61000.
```

The native currency

\[
J_\Lambda(X)-\mathcal H(d_X)
=\langle Y_4,\Omega_X-\Xi(d_X)\rangle
\]

and the one-sided endpoint orientation

\[
F_\Lambda(X)\le J_\Lambda(X)-\mathcal H(d_X)
\]

are correct. The endpoint/WSTS/Mellin--Landau chain remains explicitly imported and is not reached because the producer row is absent.

**Disposition:** `VERIFIED CONDITIONAL`; RH remains unproved.

## Computational artifact audit

The retained tail object has the intended 65 rows and 51,118,080 event records. Its exact event census and JSON aggregation are coherent; its transcendental inclusion mechanism is not valid on the tested declared platform.

The typed-ledger object is exact `Fraction` algebra on 512 synthetic leaves. It validates the direct-sum type and compiler schema but does not instantiate the actual source tree.

## Claim status

```text
L-93780  VERIFIED WITH FIXES
L-93781  UNPROVEN / GAP; interval backend fails inclusion self-test
L-93782  VERIFIED CONDITIONAL ON A VALID TAIL CERTIFICATE
L-93783  VERIFIED EXACT ABSTRACT LEAF COMPILER
L-93784  UNPROVEN / GAP at endpoint-fibre-to-leaf identity
L-93785  VERIFIED CONDITIONAL ON L-93784
T-93780  UNPROVEN / GAP
T-93781  CONDITIONAL ENDPOINT IMPLICATION ONLY
X-93780  COMPUTATIONALLY SUPPORTED, NOT EXACT-DIRECTED
X-93781  EXACT SYNTHETIC COMPILER REGRESSION ONLY
RH        UNPROVEN
```

## Exact first-broken-arrow summary

```text
numerical certificate:
    rounded_transc_std sqrt/log inclusion contract

structural DAG, even granting the tail:
    endpoint-frame fibre -> initial typed P61/causal source tree
```

Either failure blocks the complete proposal.

## Repair requirements

Numerically, replace the standard-library transcendental policy by MPFR/Arb or exact serialized primitive enclosures, and pin the complete runtime contract. Structurally, deposit one immutable fibre certificate containing the initial paired source, every source coefficient, every native coordinate, all path products, the Target-Lorenz coefficients, and one equality back to the endpoint-frame fibre.