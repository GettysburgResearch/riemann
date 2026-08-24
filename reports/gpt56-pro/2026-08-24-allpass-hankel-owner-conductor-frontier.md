# All-pass Hankel owner-conductor frontier for ninety percent

Date: 2026-08-24  
Programme PR: #731  
Checkpoint: T-105290  
Scientific status: **substantial exact reduction; ninety percent and RH unproved**

## Executive result

The all-pass programme has been moved from an abstract `H^(1/2)` transfer
request to a source-typed operator moment with an explicit fixed numerical
budget.

The key identities are:

```text
matrix determinant winding
 = signed Fourier H^(1/2) energy;

negative Fourier H^(1/2) energy
 = Hilbert-Schmidt norm squared of one block Hankel operator;

wrong extrema across K derivative rungs
 <= one block Hankel charge;

square-phase owner-conductor orthogonality
 acts directly in the Hilbert space of those Hankel operators.
```

Thus the phase-cardinality removal on PR #751 is not merely compatible with
the all-pass route: it applies to the exact topological norm which pays
converse-Rolle loss.

Using Conrey's fifth-derivative proportion and a degree-five physical Wick
calculation gives

```text
unphased five-rung frozen source cost < 1/3700;
complete defect reserve above 90% = 97/1000;
remaining phase-family/coherent/transfer allowance = 3579/37000
                                                    = 0.0967297297...
```

The remaining statement `HOCH105290` is therefore a fixed `9.67%` estimate,
not an RH-strength subpower estimate.

## 1. Matrix all-pass charge

For a matrix unitary boundary function

```text
U(t)=sum_n U_n exp(i n t),
```

Parseval gives

```text
wind det U = sum_n n ||U_n||_F^2.
```

The negative part is exactly

```text
sum_(n<0) |n| ||U_n||_F^2 = ||H_U||_S2^2.
```

For the block diagonal adjacent companion quotients, determinant winding is
minus twice the total wrong-extremum count. This replaces separate rung prices
by one positive operator charge.

## 2. Finite-alpha bridge

For

```text
F_k(t)=i^k xi^(k)(1/2+it),
alpha=1/lambda,
```

the companion symbol is exactly

```text
Theta_(lambda,k)
 = -[(xi^(k+1)-alpha xi^k)/(xi^(k+1)+alpha xi^k)]^(-1).
```

It is therefore the finite-shifted oriented ratio of PR #726. Functional
reflection folds the two safe lines at finite alpha, before differentiating in
the shift parameter. The logarithmic derivative of a rational all-pass symbol
is a signed sum of Poisson kernels with **unit divisor charges**. This is the
correct current for near-line phase slips.

PR #729's six-dimensional Newton source is residue weighted. The two currents
are complementary but not interchangeable; an order/residue conversion must
be explicit.

## 3. Exact square-phase action in Hankel space

PR #751 `L-106020` is Hilbert valued. Choosing its Hilbert space to be the
Hilbert-Schmidt Hankel operators gives, sectorwise,

```text
||physical unphased Hankel field||^2
 <= (p-1)/(p+1)
    * sum_(nonzero square phases) ||phase Hankel field||^2.
```

The complete even-character family and the principal/quadratic root fibre are
retained. The Gauss transform is constant unitary, so determinant winding and
Fourier energy are preserved. The owner quadratic class must remain indexed
until after the transform.

This closes:

```text
local squareclass physical occupancy;
phase cardinality;
finite Gauss/character change versus winding;
source-paid local principal leverage.
```

It does **not** show that the sum of all phase-family diagonal energies is no
larger than the unphased frozen energy. Nor does it close coherent physical
collisions between different owner packets. `R-105290` records exact
counterexamples to both promotions.

## 4. Improved unphased source budget

For

```text
P_5(x)=1-x/2-x^2/8-x^3/16-5x^4/128-7x^5/256,
```

the quotient `P_5^2/(1-x)` has zero coefficients through degree five and
positive tail

```text
q_6=21/512,
q_7=27/512,
q_8=945/16384,
q_9=245/4096,
q_m=3969/65536 for m>=10.
```

At corrected physical scale alpha=2,

```text
D_5(2)
 <= 702881150201/52176522785587200
 < 1/74000.
```

Both analytic orientations of the **unphased frozen source** cost less than
`1/18500` per derivative rung. Five rungs cost less than `1/3700`.

The retained Conrey input is `alpha_5>0.9970`. Exact reverse Rolle therefore
leaves every additional phase-family and transfer term the allowance

```text
997/1000 - 9/10 - 1/3700 = 3579/37000.
```

## 5. Corrected coherent ledger

Let `H_i` be the prescribed source-owned owner-conductor Hankel packets and let
`R` be the literal difference between their sum and the actual five-rung Xi
Hankel operator. Define

```text
S = unphased five-rung frozen source energy,
D = sum_i ||H_i||^2,
P = (D-S)_+,
C+ = 2 sum_(i<j) (Re tr(H_i^* H_j))_+.
```

For every `eps>0`, put

```text
A(eps)
 = eps S
   +(1+eps)(P+C+)
   +(1+1/eps)||R||^2.
```

Then, exactly,

```text
H_actual <= S + A(eps).
```

`HOCH105290` asks for some source-predeclared `eps_T` with

```text
limsup A(eps_T)/N < 3579/37000.
```

This one positive ledger retains:

```text
phase-family diagonal excess;
cross-owner and cross-conductor coherence;
the two quadratic owner sectors;
finite-alpha archimedean freezing;
complete contour/shell/taper exhaustion;
near-real Blaschke slips.
```

If it holds, more than ninety percent of zeta zeros are on the critical line.

## 6. Hostile correction

The first T-105290 deposit identified `D` itself with the `1/3700` frozen
source bound. That was too strong. The degree-five computation proves `S`, the
unphased frozen energy. Resolving it into the complete square-phase/even-
character family introduces a positive diagonal excess `P` which must be
estimated together with coherent assembly. The corrected theorem retains `P`
inside `HOCH105290` and makes no global phase-family diagonal claim.

## 7. Relation to the attached factor-67 manuscript

The finite factor-67 paired-source manuscript is not imported as a proved
premise. Its own status notice identifies the finite stopping line and terminal
Target-Lorenz certificate as the two highest-risk interfaces. Later hostile
reconstruction on PR #586 finds the proposed source-faithful induction and
reserve domination invalid as used, leaving completed-parity scalar Lorenz
feasibility open.

Its exact two-row Mellin algebra and noncancellation remain useful in the
arithmetic programme, but they do not discharge the all-pass Hankel estimate
or establish RH.

## 8. Next attack

The next source theorem should target the H^(1/2)-weighted version of PR #751's
explicit owner-conductor moment:

```text
phase-family diagonal excess;
principal/quadratic-root channel;
nonprincipal even-character channel;
positive cross-owner Gram;
actual-source finite-alpha remainder.
```

For RH, PR #751 asks for subpower bounds. For the present objective it is enough
to prove the combined normalized ledger is below `3579/37000`. This is a much
weaker quantitative target and is now the preferred unconditional ninety
percent assault.

## Exact boundary

```text
matrix winding/Hankel identity                  PROVED
finite-alpha oriented ratio                     PROVED
unit divisor Poisson current                     PROVED
square-phase contraction in Hankel space        PROVED
unphased five-rung source cost < 1/3700         PROVED
phase-family diagonal excess                    OPEN / EXPLICIT
remaining fixed allowance 3579/37000            PROVED
HOCH105290                                      OPEN / RECORD-BEARING
90% / density one / RH                          UNPROVED
```
