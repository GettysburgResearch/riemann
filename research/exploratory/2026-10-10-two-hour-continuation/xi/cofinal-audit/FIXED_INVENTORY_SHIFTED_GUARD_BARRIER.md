# A quantitative actual-source barrier for a fixed shifted inventory

Status: complete proposed analytic corollary of the reviewed actual global
scalar theorem. No new numerical moment, endpoint or census experiment.
Scope: a fixed finite collection of N actual real occurrences; all scalar
orders and large shifts. A complete normalized residual lower bound forces
the safe shifted exclusion predicate to fail once order or shift is too large.
This is a sufficient obstruction, with deliberately loose constants.
Exact dependencies: GS1–GS11 in `../GLOBAL_SCALAR_MOMENT_POSITIVITY.md`, SHA256
`bc0e85724fdd33ff1a0c5fe1a6e97d7f925823066847d2eff74435ab71db1826`;
its directed finite guard `../global_scalar_positivity.json`, SHA256
`316a88278fc8854c3a649d39c478b43d6e35588160eae0bc325e9b983cb45ace`;
the safe SM shifted guard in `../SHIFTED_COMPLETE_MOMENTS_V2.md`, SHA256
`84dff8dd45a579649bf8c515ef273559147d0b3f4a12a158ce1d7fcad1e9505b`;
and the elementary Gamma mean and Markov inequality.
What was actually run: the cited native GS guards were independently replayed
normal/optimized; the exact recorded margin exceeds 4/5. The argument below
is analytic and computes no new high-order jet or scalar residual.
Smallest remaining gap: an actual growing selection and precision mechanism
that meets exclusion guards cofinally. Increasing order or shift alone
cannot rescue a fixed inventory.

## IB1. A uniform actual-source small-time lower bound

The directed GS receipt has exact lower margin `C-2D>4/5`. This comparison
can be made on its stored rational lower endpoint; it is not based on its
decimal display. With the elementary `pi<4`, GS7 therefore implies

\[
              K(u)>\frac1{10\sqrt u}
                \qquad 0<u\le U=1/100000.
 \tag{IB1}
\]

Indeed `4 sqrt(pi)<8` and the additional `exp(u/4)` term is positive.
The complete actual-source theorem also proves K(u)>0 for every u>0,
so discarding its integral outside a small-time interval is safe.

## IB2. Normalize the complete moment as a Gamma expectation

For t>0 and integer k>=1, the complete Gamma/Laplace identity gives

\[
 t^{2k}C_k(t)=\int_0^\infty
     \frac{t^{2k}}{(k-1)!}u^{k-1}e^{-t^2u}K(u)du
                  =\mathbb E[K(V)],
 \tag{IB2}
\]

where V has Gamma shape k and rate t^2, with `E[V]=k/t^2`. Markov's
inequality gives `P(V<=2k/t^2)>=1/2`. If

\[
                         2k/t^2\le U,
 \tag{IB3}
\]

then IB1 holds on that whole event, and there
`1/sqrt(V)>=t/sqrt(2k)`. The strict complete-source inequality and positive
probability imply

\[
                       t^{2k}C_k(t)>
                            \frac{t}{20\sqrt{2k}}.
 \tag{IB4}
\]

No saddle-point approximation or asymptotic Gamma ratio is used. This
lower bound retains all actual unknown real and complex occurrences.

## IB3. A fixed real removal can subtract at most N normalized units

Remove one occurrence at each of N actual real selections, retaining every
unselected occurrence and multiplicity. Every selected scalar term obeys

\[
             0<t^{2k}(\gamma^2+t^2)^{-k}\le1.
\]

Thus the exact complete residual T_k(t) has the lower bound

\[
 t^{2k}T_k(t)
       =t^{2k}C_k(t)-\sum_{\rm selected}
                              (1+\gamma^2/t^2)^{-k}
       >\frac{t}{20\sqrt{2k}}-N
                         \qquad\text{under IB3}.
 \tag{IB5}
\]

A valid directed residual upper endpoint U_k must be at least T_k. If

\[
                         t\ge20\sqrt{2k}(N+1),
 \tag{IB6}
\]

then `U_k t^(2k)>1`. The safe shifted census guard requires
`U_k(H^2+A^2+t^2)^k<c`, with a projection price `0<c<=1`. Its left side
is at least `U_k t^(2k)>1`, so the strict guard fails for EVERY H>=0.
This is a limitation of that sufficient exclusion predicate, not proof
that the actual source contains an unselected zero below a given H.

## IB4. Explicit order barriers in the actual strip

Actual Xi has A=1/2. For the standard globally acute choice `t>=2kA=k`,
IB3 and IB6 follow whenever

\[
               k\ge\max\{200000,\ 800(N+1)^2\}.
 \tag{IB7}
\]

Consequently, for that whole shift family and any fixed inventory of N real
occurrences, every safe shifted guard fails at all orders beyond IB7.
Larger shifts only strengthen the present lower bound.

More generally the sharp support-only acute condition
`k arcsin(A/t)<pi/2` entails `t>2kA/pi=k/pi>k/4`.
The last strict inequality uses only pi<4. Therefore, for EVERY globally
acute shift permitted by this condition, IB3 and IB6 follow at all orders

\[
               k\ge\max\{3200000,\ 12800(N+1)^2\}.
 \tag{IB8}
\]

These are loose sufficient numerical barriers, not optimal transition
orders. For example the experimental inventory contains only 8049 selected
occurrences; its bounded k<=32 computations are far below either barrier
and are unaffected by this theorem. The statement explains why an infinite
order ladder over the SAME finite inventory cannot by itself yield cofinal
exclusion, even after global positivity of every actual scalar moment has
been established.

Growing real selections, directed root precision and full coefficient
accuracy can still improve a bounded census. Their successful uniform
cofinal transport is a different premise and remains open. The positivity
and multiplicity countermodels in the companion notes identify why raw
scalar signs alone do not supply that premise.
