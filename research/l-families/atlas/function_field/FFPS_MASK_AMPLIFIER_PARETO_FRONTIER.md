# FFPS hard-mask amplifier: exact leverage/mode/anomaly Pareto frontier

Status: **exact cyclic-projector algebra and exact finite-amplitude
cancellation theorem; arithmetic realization inherited only in the fixed
physical fibres of PR #756**.  No varying-conductor estimate or
individualization theorem is proved.

## Start here

The cyclic hard masks have one unavoidable joint design parameter.  Put

\[
 A={Q\over N},\qquad B={P\over N},\qquad
 \rho={t\over k},\qquad
 u={1-\rho\over\rho}={k\over t}-1,
\]

where `rho` is the retained quotient density.  Then

\[
 \boxed{L(u)={(1+u)^2\over A+Bu}}
 \tag{0.1}
\]

is the sharp restricted inverse-Gram leverage, while

\[
 \boxed{\sum_{r=1}^{k-1}|\gamma_r|^2=u}
 \tag{0.2}
\]

is the total mass of the selected nonprincipal Fourier modes.  Thus changing
the retained set at fixed density can redistribute the selected-mode burden,
but cannot reduce it.

When `B>2A`, the continuous leverage minimum occurs at

\[
 \boxed{u_* = 1-{2A\over B},\qquad
 L_*={4(B-A)\over B^2}.}
 \tag{0.3}
\]

The interval `0<=u<=u_*` is the exact leverage/selected-mass Pareto frontier.
Past `u_*`, both leverage and selected mass are worse.  As the number of
local factors grows and `B/A` grows, `u_*` tends to one: the strongest formal
leverage regime necessarily carries an order-one selected Kummer burden.

There is a matching anomaly-cancellation statement.  A pure principal
amplitude is preserved exactly by the normalized hard observation.  But one
hard observation can be cancelled by selected modes, and the least possible
selected squared amplitude is

\[
 \boxed{
 \min\left\{\sum_{r=1}^{k-1}|H_r|^2:
       \sum_{r=1}^{k-1}\gamma_r H_r=-P_0\right\}
 ={ |P_0|^2\over u}.}
 \tag{0.4}
\]

At the continuous leverage optimum this cost is

\[
 {|P_0|^2\over u_*}={B\over B-2A}|P_0|^2,
\]

which tends to `|P_0|^2`, not infinity, on large panels.  Hard restriction
therefore preserves a pure principal signal but does not individualize it:
selected modes of comparable size can cancel it at bounded energy.

Equations (0.1)--(0.4) are the exact algebraic co-design frontier that a
sheaf estimate or principal amplifier must beat.

## 1. Frozen dependencies and scope

This packet starts from PR #756 at exact head
`6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`.  The three load-bearing source
notes and their git blobs there are:

| source | blob | role |
|---|---|---|
| `FFPS_CYCLIC_CHARACTER_MASKS.md` | `80a56f847a1d272c43e092164503ecdfdd4c4b5d` | restricted-Gram formula |
| `FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md` | `9012f96b34a3ffe55b66282ba1e62bc02514b5c6` | physical orientation and hard projector |
| `FFPS_CYCLIC_CLOSURE_BUDGET.md` | `b576c8a114d7e502b9b474cfed0db7e4cf6e2475` | selected-mode and invisible-direction ledger |

The present proof is finite cyclic Fourier algebra.  The source-realization
scope is exactly the fixed owner sectors already proved in those packets.
No statement below promotes that realization to the varying-conductor FFPS
sum.

## 2. One density controls leverage and total selected mass

Let

\[
 H_i=\mathbf F_{p_i}^{\times}/\{\pm1\},\qquad
 m_i=|H_i|,
\]

and choose exact-order-`k` quotient characters.  Write

\[
 N=\prod_i m_i,\qquad Q=\prod_i(m_i+1),\qquad
 P=\prod_i p_i.
\]

For a retained set `S` in `mu_k`, with `|S|=t`, define

\[
 \gamma_r={1\over t}\sum_{s\in S}s^{-r}.
\]

The normalized hard observation has Fourier expansion

\[
 O_j=P_0+\sum_{r=1}^{k-1}\zeta_k^{-jr}\gamma_rH_r,
 \tag{2.1}
\]

up to the harmless common choice of rotation convention.  The coefficient of
the principal amplitude `P_0` is one because the retained weight is `k/t`.

Parseval for the indicator of `S` gives

\[
 1+\sum_{r=1}^{k-1}|\gamma_r|^2={k\over t}.
\]

This proves (0.2).  In particular, the shape of `S` cannot lower the total
selected mass at a fixed density.

The sharp cyclic-mask leverage from the frozen packet is

\[
 L(\rho)={1\over A\rho^2+B\rho(1-\rho)}.
\]

Substituting `rho=1/(1+u)` proves (0.1).

## 3. Exact Pareto interval

Differentiation is elementary and sign-exact:

\[
 {dL\over du}
 ={(1+u)(2A-B+Bu)\over(A+Bu)^2}.
 \tag{3.1}
\]

If `B<=2A`, every `u>0` initially increases leverage, so no proper cyclic
mask supplies a continuous improvement.  Suppose `B>2A`.  Equation (3.1)
has the unique nonnegative zero (0.3), and `L` decreases before it and
increases after it.  Since selected mass is exactly `u`, the nondominated
two-objective interval is precisely

\[
 0\le u\le u_*.
\]

Comparison with the complete mask gives the larger strict-improvement
interval

\[
 \boxed{0<u<{B-2A\over A}.}
 \tag{3.2}
\]

Masks between `u_*` and the endpoint in (3.2) do beat the complete frame, but
are dominated by the continuous optimum in both leverage and selected mass.

For a fixed prime panel the character order must satisfy

\[
 k\mid\gcd(m_1,\ldots,m_d).
\]

Thus the arithmetic design problem is discrete: among the available rational
densities `t/k`, choose a point near the continuous frontier and then account
for the actual trace-sheaf cost of its nonzero Fourier labels.

## 4. Exact single-observation anomaly budget

Fix one rotation in (2.1).  For a prescribed principal amplitude `P_0`, the
selected modes cancel that observation exactly when

\[
 \langle\overline\gamma,H\rangle=-P_0
\]

under one consistent complex-inner-product convention.  Cauchy--Schwarz and
(0.2) give

\[
 |P_0|^2\le u\sum_{r=1}^{k-1}|H_r|^2.
\]

Equality is attained by taking `H` proportional to the conjugate coefficient
vector.  This proves (0.4), including sharpness.

Three consequences must be kept distinct.

1. If every `H_r=0`, every rotated hard observation equals `P_0`; the hard
   normalization loses no pure principal amplitude.
2. One rotated observation does not individualize `P_0`: selected modes with
   the exact energy (0.4) can erase it.
3. Averaging all rotated amplitudes recovers `P_0` exactly, because all
   nonconstant Fourier modes average to zero.  The squared/Wick-centered
   family problem does not retain this signed amplitude identity for free;
   its replacement is precisely the selected-mode subtraction and `CYSEL`
   gate in the frozen closure packet.

The cancellation vector in (0.4) is finite linear algebra.  It is not a
claim that an arithmetic family realizes an arbitrary vector of `H_r`
values.  Conversely, no arithmetic rigidity excluding that vector is known.

## 5. Fourier-label complexity lower bounds

Let `R(S)` be the number of nonzero Fourier coefficients of the indicator of
`S`, including the constant coefficient.  The elementary finite-group
uncertainty proof gives

\[
 \boxed{tR(S)\ge k.}
 \tag{5.1}
\]

Indeed, the maximum Fourier coefficient is at most the `l1` norm, the `l1`
norm is at most `sqrt(t)` times the `l2` norm, and Parseval completes the
inequality.  Hence at least

\[
 \left\lceil{k\over t}\right\rceil-1
\]

nonconstant character labels must occur.

If `k` is prime, every nonempty proper `S` has all `k-1` nonconstant
coefficients nonzero.  Otherwise a vanishing coefficient would make the
zero-one polynomial of `S` divisible by
`1+X+...+X^(k-1)`, forcing `S` to be empty or full.

For composite `k`, periodic masks can have smaller Fourier support.  If the
indicator is invariant under a nontrivial translation subgroup, Fourier
inversion shows that it factors through the smaller quotient and its support
lies in the annihilator.  Such a mask is genuinely a lower-order mask written
with redundant labels.  A higher-order presentation is therefore not itself
a complexity saving.

`R(S)-1` is an exact lower ledger for distinct selected character powers.  It
is not yet a Betti-number theorem: geometrically related sheaves may share
cohomology, while collision strata may add further complexity.

## 6. Two exact panels

### The minimal ternary physical control

For `(p_1,p_2,k,t)=(7,13,3,2)`,

\[
 A={14\over9},\quad B={91\over18},\quad u={1\over2},
 \quad L={27\over49}.
\]

The continuous optimum is

\[
 u_*={5\over13},\qquad L_*={648\over1183}.
\]

Both nonconstant ternary modes occur, and cancelling a unit principal
amplitude in one rotated observation costs selected squared amplitude `2`.

### A panel supporting quadratic and ternary masks

For `(p_1,p_2)=(13,37)`,

\[
 A={133\over108},\qquad B={481\over108}.
\]

The quadratic half-mask has

\[
 (u,L,R-1)=\left(1,{216\over307},1\right),
\]

whereas the ternary two-thirds mask has

\[
 (u,L,R-1)=\left({1\over2},{54\over83},2\right).
\]

Thus the ternary mask has both lower leverage and lower total selected mass,
but one additional selected character label.  The actual sheaf complexity,
not the Gram calculation alone, decides which is arithmetically preferable.

The continuous optimum is

\[
 u_*={215\over481},\qquad
 L_*={150336\over231361},
\]

so the ternary density is close to the exact panel optimum.

## 7. What this changes, and what remains open

Proved exactly:

- the one-parameter leverage/selected-mass identity (0.1)--(0.2);
- the continuous Pareto interval, optimum, and strict-improvement interval;
- the sharp finite-amplitude cancellation energy (0.4);
- the Fourier-label uncertainty bound and prime-order full-support theorem;
- the two rational control panels.

Still open:

- the geometric invariant constituents and Betti/conductor growth of the
  selected Kummer modes after every FFPS collision stratum is removed;
- conductor-uniform `CYSEL`, `WCADD106140`, or `WCKUM106140`;
- an arithmetic theorem forbidding the cancellation vector in (0.4);
- any family-to-principal individualization theorem;
- RH or GRH.

The design conclusion is therefore precise: inverse-Gram leverage and the
selected analytic burden are the same one-parameter tradeoff.  Geometry can
still distinguish masks with the same density by their Fourier-label support
and collision strata, so the next optimization must be sheaf-aware.

