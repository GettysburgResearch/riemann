# State-augmented Markov–Pascal global attack

Authoring agent: `gpt56-pro-22`  
Date: 2026-08-08  
Issue: #283  
Branch: `agent/gpt56-pro-22/283-markov-pascal-global`  
Status: **FULL CONDITIONAL PROPOSAL; SAPC OPEN; RH UNPROVED**

## Executive conclusion

The repository does not presently contain an unconditional proof of the
Riemann Hypothesis.  The newest carry consolidation, PR #276, identifies one
finite weighted shell theorem equivalent to RH.  The newest explicit
producers, however, still need a quantitative arithmetic mechanism.

This pass attacked those producers rather than adding another equivalent
scalar.

The principal results are:

1. the proposed fixed third-Abel producer kernel is exactly false at
   `Q=X=520,n=15`, with coefficient `-91/256`;
2. the fixed fourth Abel kernel also fails, at `Q=X=10000,n=7`;
3. the exact Gamma domination of the carry law yields a positive
   **state-dependent Markov factorization**, even though it does not yield an
   independent scalar convolution factor;
4. the central carry lattice commutator is exactly a half-scale adjacent
   divisor source;
5. switching a central split to its nearest sibling acts on that source by one
   first difference and has a complete entropy/von-Mangoldt ledger;
6. the state-dependent factorization lifts as a completely positive
   two-frequency Gram identity and commutes with complete arithmetic-fiber
   congruence;
7. these ingredients define one new full proposal, the **State-Augmented Pascal
   Cascade** (`SAPC`).

The load-bearing theorem remains open:

\[
D_{j+1}
\le
\rho_*D_j+\operatorname{polylog}(X),
\qquad
\rho_*<1,
\]

after complete Markov-state and Pascal-cycle recombination.

If proved, SAPC gives subpower optimized fragmentation debt, the sharp prime
ramp, and RH.

## 1. Repository-wide position

The mature proof graph has several exact front ends and several false generic
closures.

### 1.1 Durable exact or proposed-complete interfaces

The following are now reusable at their declared scopes:

```text
fixed-ratio Möbius shells and first-cell Mertens firewall;
prime-only and complete prime-power Hardy/screw criteria;
correct independent-frequency reflected Selberg block;
finite Möbius resolvents and complete source packetization;
complete-lattice high-order Euler closure;
parabolic carry seed and exact 4 sqrt(X) normalization;
carry/fragmentation Möbius divergence;
complete Pascal fundamental-cycle basis;
cycle-optimized capacity debt and bounded-superadditive dual;
central continuum carry contraction with ratio 1-log 2;
WSTS <=> RH consolidation.
```

### 1.2 Exact false shortcuts

The project must retain the existing counterexamples to:

```text
one-frequency physical localization;
Farey determinant cancellation without noncoprime chains;
generic critical-cluster operator contraction;
globally positive Hankel approximation of the compact ramp;
conditional-Hankel carry factorization;
absolute bounded-rank Möbius contagion;
nonnegative monotone divisibility covering;
prime-only subpower tail charge;
pure ternary nonnegative fragmentation;
fixed third/fourth Abel producer positivity.
```

The present proposal is designed to survive these mutations.

## 2. Why the newest fixed-Abel proposal fails

PR #279 starts from a valid idea: the critical target

\[
w_X(q)=q^{-1/2}\log(X/q)
\]

is completely monotone inside its finite source interval.  Repeated summation
by parts can therefore turn source derivatives into positive coefficients.

The missing claim was positivity of the cumulative producer kernel.

Exact replay of the committed recurrence gives

\[
A_{w_{520,3}}(15)=-\frac{91}{256},
\]

where

\[
w_{Q,3}(q)=\binom{Q-q+2}{2}\mathbf1_{q\le Q}.
\]

The proposed third-kernel theorem is therefore false.

The same test at the next fixed order gives

\[
A_{w_{10000,4}}(7)
=-\frac{10512404675923}{16384}.
\]

Hence a proof cannot simply choose Abel order three or four and place all
remaining difficulty in a finite endpoint collar.

The valid lesson is narrower:

```text
source complete monotonicity is real;
fixed low-order kernel positivity is not.
```

Any future Abel argument needs growing order, signed cancellation, or cycle
repair.

## 3. The state that scalar factorization discarded

The carry probability law has the exact construction

\[
M=\lfloor V^{-2}\rfloor,
\qquad
T=\log\frac{M(M+1)}{M+U},
\]

with independent `Beta(2,1)` variables `U,V`.  The variable

\[
G=-4\log(UV)
\]

has the `Gamma(2,1/2)` law and satisfies

\[
G\ge T.
\]

The former scalar proposal asked whether

\[
G\overset d=T+S,
\qquad S\perp T.
\]

That is exactly a complete-monotonicity/reciprocal-zeta factor theorem and is
not supplied by stochastic domination.

But the explicit coupling supplies something stronger than an inequality and
weaker than independence: the joint law of

\[
(T,S),
\qquad S=G-T\ge0.
\]

Disintegration gives a positive state-dependent kernel

\[
\kappa_t(ds)
\]

with

\[
\int F(y)g(y)dy
=
\int p(t)\int F(t+s)\kappa_t(ds)dt.
\]

This is the correct probability object for the atomized carry system.  The
quotient layer and carry state were being averaged away in the scalar
convolution proposal.

## 4. Completely positive two-frequency lift

The Markov identity remains valid for matrix-valued functions:

\[
\int g(y)H(y)H(y)^*dy
=
\int p(t)\int\kappa_t(ds)
H(t+s)H(t+s)^*.
\]

Every off-diagonal cross term is preserved.  Thus the factor is compatible with
the corrected independent-frequency physical block, not with the rejected
one-frequency specialization.

If `M_H` is a complete arithmetic-fiber source map, then

\[
M_H^*\left(\int G(t)d\mu(t)\right)M_H
=
\int M_H^*G(t)M_Hd\mu(t).
\]

Therefore a fixed state-resolved base theorem can lift through the top Möbius
fiber by congruence.  This supplies a genuine bridge between the elementary
carry route and the fixed-source reflected route.

Positivity alone is not strict coercivity.  A production certificate still has
to prove a reserve-minus-lower-block recurrence.

## 5. The finite lattice commutator is not opaque

The central discrete residual differs from its continuum dilation model by

\[
(\mathcal Er)(q)
=
\sum_{k\ge1}[r(2kq-1)-r(2kq)].
\]

Put

\[
\sigma(h)=r(2h-1)-r(2h).
\]

Then exactly

\[
(\mathcal Er)(q)=\sum_{q\mid h}\sigma(h).
\]

Thus the lattice error is the divisor-zeta transform of one adjacent source at
half scale.  It has the exact Möbius inverse

\[
\sigma(h)=\sum_k\mu(k)(\mathcal Er)(hk).
\]

This explains why the first commutator is small but later raw central debt can
become large: the divisor source is repeatedly transported without using the
available cycle freedom.

## 6. The local Pascal move

For an even parent `2h`, compare the central split

\[
h+h
\]

with the nearest sibling split

\[
(h-1)+(h+1).
\]

Their carry-column difference is exactly

\[
\chi_{2h,h-1}(q)-\chi_{2h,h}(q)
=
\mathbf1_{q\mid h}-\mathbf1_{q\mid h+1}.
\]

Their entropy difference is

\[
\log\frac{\binom{2h}{h-1}}{\binom{2h}{h}}
=
\log\frac h{h+1},
\]

which is also the von-Mangoldt weighted carry difference.

A switch schedule `t_h` changes the half-scale divisor source by

\[
\sigma(h)\mapsto\sigma(h)-(t_h-t_{h-1}).
\]

This is precisely the finite adjacent transport suggested by the Markov
state.  It is strict lower-scale arithmetic, not a generic norm inequality.

A formal cumulative solution cancels the source, but may exceed the available
central edge capacity.  The complete Pascal fundamental-cycle basis supplies
the remaining legal repair directions, and the cycle-debt functional measures
the exact unpaid amount.

## 7. State-Augmented Pascal Cascade

The proposed proof object keeps the Markov state throughout the central
support-halving cascade.

At each stage it emits:

```text
positive Markov state cells and masses;
complete balanced split manifest;
exact node divergence and carry loads;
sibling-switch schedule;
complete Pascal fundamental-cycle coordinates;
post-recombination capacity debt;
strict lower-scale destinations;
full two-frequency Gram and arithmetic fiber when using the reflected consumer.
```

The theorem sought is

\[
D_{j+1}(X)
\le
\rho_*D_j(X)+C(1+j)^A\log^B(2X),
\qquad\rho_*<1.
\]

The continuum value `1-log 2` nominates the scale but is not asserted as the
finite constant.

Since there are only `O(log X)` support halvings, this recurrence gives

\[
\sum_jD_j(X)=X^{o(1)}.
\]

The cycle-debt adapter then gives

\[
\sum_{p^a\le X}
\frac{\Lambda(p^a)}{\sqrt{p^a}}
\log\frac X{p^a}
=
4\sqrt X+X^{o(1)},
\]

and the square-screw/Landau transfer gives RH.

Alternatively, the same finite state manifest can feed a strict
independent-frequency physical recurrence and close the top-source route.

## 8. Exact regression

The standard-library checker validates:

```text
third-Abel counterexample       -91/256
fourth-Abel counterexample      -10512404675923/16384
central/sibling carry rows      16,383
commutator/divisor rows         140
sibling transport rows          121
rational Gamma-domination rows  2,552
matrix-lift entries             9
mutation tests                  6/6
```

Proof-object SHA-256:

```text
b0d970ace6e892709f36ead9e453d1937cad3f481ea534c15422686e83b27fb0
```

This authenticates finite algebra and mutation controls only.

## 9. Honest proof boundary

```text
fixed third/fourth Abel positivity       REFUTED
explicit state-dependent Gamma factor    PROPOSED COMPLETE EXACT
Markov two-frequency CP lift             PROPOSED COMPLETE EXACT
sibling-switch identity                  PROPOSED COMPLETE EXACT
commutator divisor factorization         PROPOSED COMPLETE EXACT
Pascal cycle basis and debt               IMPORTED PROPOSED COMPLETE
continuum contraction                     IMPORTED PROPOSED COMPLETE
SAPC contracting finite recurrence        OPEN / RH-BEARING
SAPC -> sharp prime ramp -> RH             COMPLETE CONDITIONAL
Riemann Hypothesis                        UNPROVED
```

This is a full-problem attack because one finite source object is designed to
serve both the elementary and reflected global consumers.  It is not an
unconditional proof, and the branch does not present it as one.