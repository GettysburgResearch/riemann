# Original-measure faithfulness at every horizon from 450 onward

This theorem concerns the literal source on the fixed primes `2,3,5`,
its twenty declared occupation coordinates, and the original Mellin
measure. It combines a finite, exhaustive rank certificate with a new
positive-tail estimate for the complete physical observation. It is not
a frame theorem for all sixty-four product coordinates or for varying
prime sets.

## 1. Statement and exact interfaces

Write the original current, with the literal factor two, as

\[
 F_H(\gamma)=Z_{H,0}+\sum_{j=1}^{20}M_j(\gamma)Z_{H,j},\qquad
 T_Hv=\sum_{j=1}^{20}v_jZ_{H,j}.
\]

Here the physical cutoff is the ordered-record condition `nm<=H`.
The norm is in `L^2(nu)`, where

\[
 d\nu=|\widehat\kappa(t)|^2dt/(2\pi),\qquad
 \nu_0=128(3+\sqrt2)\log2-288.
\]

Subject to the separately authenticated physical Gram and positive-tail
certificates below, the conclusions are:

1. `T_H` is injective for **every integer H>=450**.
2. For every `H>=2^48` and every real twenty-vector `v`,

\[
 \frac{\|v\|_2^2}{48000000}
 \leq\|T_Hv\|_{L^2(\nu)}^2\leq69\|v\|_2^2.       \tag{1}
\]

The numerical lower constant in (1) is not asserted for the finite
prefix `450<=H<2^48`. The existing exact rank certificates prove its
pointwise positivity there. Their finite number also implies existence
of a positive common lower constant, without evaluating one here.

The source coordinates, their exact affine decoder, and the original
infinite-current normalization are those of
`NATIVE_INFINITY_VARIATIONAL_THEORY.md`, sections 1--2. Its inherited
twenty-moment source blob is
`2113ce2bef593e19ca647c12c4fbb3c0728572a2`. The two numerical inputs are
the directed original infinite Gram and
`physical_horizon_tail.verification.json`, under the separate
`PHYSICAL_GRAM_PREREGISTRATION.md` and
`PHYSICAL_HORIZON_TAIL_PREREGISTRATION.md` contracts. A final bound
replay must authenticate the Gram lower bound as well as the tail
producer; the tail calculation alone does not establish that input.

## 2. A positive majorant for the actual product horizon

Put `A(z)=sqrt(1-z^2)` and `D(z)=sqrt(1-z)-A(z)`. Let

\[
 w_e=|[z^e]A|+|[z^e]D|,\qquad
 u_e=\sum_{i=0}^e w_iw_{e-i}.
\]

All these coefficients are nonnegative exact rationals. Directly from
the binomial signs, for `0<=q<=1`,

\[
 W(q)=\sum_{e\geq0}w_eq^e
      =2+\sqrt{1+q}-2\sqrt{1-q^2}.                    \tag{2}
\]

In particular `w_0=1` and `W(1)=2+sqrt(2)`. This is the original
`(1,x)` coordinate basis, not the different constant/linear basis used
in a coefficient-frame minor.

For a `2,3,5`-smooth integer `n`, let `w_n` be the product of the three
local weights. Every coefficient in the exact affine monomial decoder
has absolute value at most two. Expanding each field before coalescing
equal physical ratios therefore gives, uniformly in real `t`,

\[
 |Z_{\infty,j}(t)-Z_{H,j}(t)|\leq P_H,
\]
\[
 P_H=2\sum_{nm>H}\frac{w_nw_m}{\sqrt{nm}}
 =2\left\{\prod_{p\in\{2,3,5\}}W(p^{-1/2})^2
 -\sum_{2^a3^b5^c\leq H}
       \frac{u_au_bu_c}{\sqrt{2^a3^b5^c}}\right\}.    \tag{3}
\]

The factor two in (3) is the exact decoder coefficient bound. Every
ordered pair is retained in the convolution; no diagonal or alias is
discarded. Absolute convergence justifies regrouping by the product
`nm`. In particular this is an estimate for the original physical
cutoff, unlike a local holomorphic-product degree truncation.

The omitted sum is positive and decreases with `H`. Cauchy--Schwarz
on the twenty coordinate coefficients and integration against the
unchanged measure give

\[
 \|T_\infty-T_H\|_{\ell_2^{20}\to L^2(\nu)}
 \leq\sqrt{20\nu_0}\,P_H.                           \tag{4}
\]

## 3. The registered threshold closes the analytic tail

The directed infinite Gram supplies the conservative bounds

\[
 \frac1{12000000}I\preceq G_\infty\preceq68I.         \tag{5}
\]

The tail acquisition uses Arb precision 192 and the predeclared panel
`H=2^32,2^40,2^48,2^56,2^61`. At `H=2^48` its complete prefix has
5811 smooth products, digest
`5d8151d905f5b2673c6a5a44de21ee5475d974825fb920328cdc48928460d99e`.
It certifies `P_H<0.000002480322` and, more precisely, the strict exact
predicate

\[
 20\nu_0P_H^2<\frac1{48000000}.                      \tag{6}
\]

The positive margin in (6) is bounded below by the rational number

\[
\frac{3404237455957046972055869815947915383932281313635051490925}
 {421249166674228746791672110734681729275580381602196445017243910144}.
\]

The first two registered thresholds fail this sufficient test; those
failures are retained and are not rank failures. The later two pass,
but no optimal threshold is claimed. By monotonicity, (6) persists for
every larger physical horizon. Equations (4)--(6) and the operator
triangle inequality imply

\[
 \|T_Hv\|\geq
 \left(\frac1{\sqrt{12000000}}-\sqrt{20\nu_0}P_H\right)\|v\|_2
 >\frac{\|v\|_2}{\sqrt{48000000}}.
\]

The corresponding upper bound is
`(sqrt(68)+sqrt(1/48000000))^2<69`, proving (1).

## 4. Exact finite coverage and scope

The preceding finite results are imported without rerunning their
matrix eliminations here:

| Coverage | Exact source |
|---|---|
| `450<=H<=900` | commit `a4d610431d5edaf26b00bae903bb9111837e4c31`, `native_horizon_rank_certificate.json`, blob `5e1e3471e9428b339d652440b04cda829673b54d`, proof `faad848e3f7742a2390b92ce8659859d2288cd6cae18c88e0a6c012d355c4e69` |
| `900<=H<=2^48` | commit `7448c5a4eb1cd2ad7c300b7332abf4e39392a138`, `native_event_minor.collection.json`, blob `3f183d72122d33daa6ea05acd9d3ae92c92b9a06`, proof `02a7065a92e272f6764eb235f78b011c8312358ec914adf994e4019cf8d304a8` |

Both paths are under `research/riemann-structures/native-six-hour/`.
The collector authenticates and composes forty accepted components,
with complete event coverage and no integer gaps. It does not itself
rerun their source updates or modular eliminations. Together these
certificates and (1) cover every integer horizon from 450 onward.

The old selected minor's limiting rank at most fifteen remains true.
The new estimate controls the complete original physical observation,
so it does not rehabilitate that minor or assign it a uniform inverse.
Likewise the coefficient-frame result in PR783 is a different normed
statement and is not the numerical input to (5).

Injectivity distinguishes different twenty-coordinate source currents;
it does not make all twenty-vectors attainable by monotone paths. It
does not identify the full retained-gamma observation, extend to all
prime families, or imply a zeta-function conclusion.
