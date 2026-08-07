# M-20802 — Prime-curvature transport attack on the full Riemann Hypothesis

Claim ID: `M-20802`  
Title: Replace the proliferating finite bottleneck chain by one exact cofinal prime-moment transport theorem  
Status: `PROPOSED RESEARCH PROGRAM — T-20802/L-20808/L-20809 PROVED AS IDENTITIES; COFINAL SIGN OPEN`  
Authoring agent: `gpt56-03-u`  
Created: 2026-08-07  
Primary theorem: `T-20802`  
Scope: direct attack on the full RH, not another finite packet closure

## 1. Why step back

The repository has developed several powerful but increasingly nested routes:

- finite D-0001 carrier matrices and Schur closures;
- direct-`xi` and `xi'/xi` Pick/Loewner witnesses;
- zero deflation and selected-line frames;
- cardinal-radical capture and complete-kernel synthesis;
- square-screw and beta-cell sampling;
- pole-free terminal-prime windows;
- theta/Volterra and canonical-system factorizations.

Many of their local algebraic gates are now closed.  Their remaining gates are
not small technicalities: each is another representation of the same fixed
strip-sensitive obstruction.

The present attack chooses the scalar zeta-screw route because it permits an
exact collapse of the *entire real continuum* to one sequence over prime-power
prefixes:

\[
 \boxed{
 M_j=Q_j-A_+^*(P_j).
 }
\]

By `T-20802`, RH is equivalent to `M_j>=0` for every prefix, apart from one
fixed compact archimedean gate.  This is not a sampled sufficient condition and
not a finite-dimensional approximation.  It is the exact global minimum of the
full screw function.

## 2. The full arithmetic target

For

\[
 P_j=\sum_{q\le q_j}{\Lambda(q)\over\sqrt q},
 \qquad
 Q_j=\sum_{q\le q_j}{\Lambda(q)\log q\over\sqrt q},
 \tag{M-20802.1}
\]

`L-20809` gives

\[
 \boxed{
 A_+^*(P_j)
 =2(P_j-B)\left[
 \log\left({P_j-B\over2}\right)-1
 \right]
 +8-{C\over4}+\Delta_j,
 }
 \tag{M-20802.2}
\]

with

\[
 0\le\Delta_j=O(P_j^{-5}).
 \tag{M-20802.3}
\]

Thus the full problem has become the one-sided entropy-scale inequality

\[
 \boxed{
 Q_j
 \ge
 2(P_j-B)\left[
 \log\left({P_j-B\over2}\right)-1
 \right]
 +8-{C\over4}+\Delta_j
 \quad(j\ge1).
 }
 \tag{M-20802.4}
\]

The leading asymptotics cancel.  The surviving margin is of constant scale, so
ordinary PNT or zero-density error terms are not enough.  Any proof must retain
arithmetic phase/strip information rather than estimate it away.

## 3. Three serious proof mechanisms

### A. Canonical block transport

`L-20808` constructs the explicit smooth reference measure

\[
 \mu_*=\chi_*(dp)
 \tag{M-20802.5}
\]

and matches the prime atom of mass `w_j` at `tau_j` to the mass slice
`[P_(j-1),P_j]`.  The safety reserve obeys

\[
 M_j=M_0+\sum_{r\le j}w_r(\tau_r-\bar\tau_r).
 \tag{M-20802.6}
\]

The first genuine proof target is therefore a cofinal partition into consecutive
blocks for which:

1. every total prime-minus-curvature block moment is nonnegative, or has a
   declared finite debit;
2. each within-block drawdown is smaller than the incoming reserve;
3. the construction is uniform and does not hide an infinite scan.

A successful block theorem is a complete RH proof.

### B. Positive convolution / Selberg-square factorization

The margin in (M-20802.4) uses exactly the first two logarithmic moments of the
von Mangoldt prime-power measure.  The most attractive arithmetic completion is
an identity of the form

\[
 Q_j-A_+^*(P_j)
 =\mathcal Q_j^{\rm pos}+\mathcal R_j,
 \qquad
 \mathcal Q_j^{\rm pos}\ge0,
 \tag{M-20802.7}
\]

where `mathcal Q` is a finite prime-convolution square and
`mathcal R_j>=0` is explicit.  Selberg's symmetry formula shows that the right
kind of positive prime convolution exists at leading order, but its classical
error is far too large.  The task is to retain the complete centered
pole/gamma/trivial-zero cancellation before bounding the remainder.

This is the scalar analogue of the repository's successful rule:

```text
assemble prime, pole, and archimedean channels jointly;
only then take a norm or a sign.
```

### C. Strip reflection to transport reserve

`L-19810/L-19811` identify every off-line zero with a positive anti-causal
Poisson energy having a universal gap.  `T-20802` identifies the same failure
with one negative transport reserve.

The most ambitious bridge is an exact inequality

\[
 \mathcal E_\omega
 \le
 \mathfrak C_\omega
 \sup_j[-M_j]_+
 \tag{M-20802.8}
\]

or its reverse separating form.  It would identify the real prime transport
reserve with the causal/anti-causal reflection energy and could turn a
prime-side positive convolution into the missing minimum-phase theorem.

No such bridge is claimed yet.  It is a high-value target because it would
unify the strongest scalar and operator routes instead of adding another gate.

## 4. Production plan

### Phase 1 — immutable finite reconnaissance

1. certify the fixed compact gate on `[0,log2]`;
2. stream every prime power once and maintain only `(P_j,Q_j,M_j)`;
3. preserve every new record-low reserve and its exact prefix digest;
4. evaluate the same prefix by the exact Fenchel form and by the entropy envelope;
5. stop treating a long positive run as a proof.

`O-20805/X-20806` record the first reconnaissance through `10^7`.

### Phase 2 — search for transport structure, not a negative eigenvector

For each long block emit:

```text
prime mass
prime first moment
smooth curvature mass
smooth first moment
total transport defect
maximum internal drawdown
incoming and outgoing reserve
```

Rank blocks by normalized drawdown and by deviation from a candidate positive
convolution identity.  This exposes the actual arithmetic mechanism needed for
a cofinal theorem.

### Phase 3 — prove one cofinal block theorem

The proof must quantify over an unbounded tail.  Acceptable endpoints include:

- an explicit local transport map with nonnegative barycenter surplus;
- an exact nonnegative prime-convolution decomposition;
- a recursively invariant cone for block moment pairs `(P,Q)`;
- a strip-reflection estimate forcing every block drawdown to vanish.

A theorem that merely shrinks a classical PNT error, enlarges a verified zero
height, or checks more finite prefixes is not a completion.

## 5. Connection to located literature

### Suzuki screw and canonical-system criteria

Masatoshi Suzuki's `arXiv:2206.03682v4` supplies the explicit screw function and
pointwise RH criterion used by `D-9501`.  His earlier
`arXiv:1204.1827` associates the shifted completed-zeta quotient with canonical
systems for sufficiently large strip offset and identifies extension to every
positive offset as an RH criterion.  The transport reserve is a prime-side
real-variable target for the same missing minimum-phase/accretivity statement.

### Uniform coefficient-tail positivity

Wojciech Michałowski, *An explicit uniform cubic wedge for consecutive Toeplitz
minors of the Riemann xi coefficients*, `arXiv:2607.16795`, proves positivity in
the tail region `k>=10^18 r^3` by a certified saddle, q-Pascal, and Banach-algebra
argument.  The paper explicitly leaves the RH-critical complementary region
open.  Its useful lesson here is methodological: a successful proof may need a
uniform saddle comparison plus a nonlinear majorant, but the comparison must be
applied to the prime-transport reserve rather than to a region already known to
be asymptotic.

### Theta/Volterra positivity

Marvin B. Freedman's `arXiv:2606.29555` develops finite-core Volterra reductions
for the Riemann phase kernel and explicitly does not claim RH.  Repository PR
#202 has since isolated its surviving sign as a theta Dirichlet-to-Neumann
accretivity problem.  The transport criterion offers a scalar test against which
any proposed theta factorization can be checked immediately.

Only these located references are cited.  None is represented as a proof of RH.

## 6. What would count as a breakthrough

A true completion is now sharply recognizable:

\[
 \boxed{
 \exists J_0\ \forall j\ge J_0:\quad
 Q_j-A_+^*(P_j)\ge0.
 }
 \tag{M-20802.9}
\]

Together with a finite directed prefix and the compact initial gate, this proves
RH.

A strict negative value for one `j` disproves RH.

Everything else—more carrier dimensions, another selected-zero frame, a larger
finite scan, or a tighter but still sign-indefinite error term—is supporting work,
not the final theorem.

## 7. Honest status

The repository now has an exact, one-dimensional, prime-only full-RH target and
a canonical induction law.  The cofinal arithmetic sign has not been proved.
This methodology is intended to focus future work on that sign rather than
continue decomposing it into progressively smaller equivalent bottlenecks.
