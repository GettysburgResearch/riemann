# Strong Xi log-concavity and the critical-depth collar

This pass continued the durable Xi programme on PR #729 after verifying its
remote head and zero-behind status.

## 1. Uniform source curvature

The theta-mixture proof of strict log-concavity contains a much larger rational
margin than was previously extracted. The first theta orbit has mass greater
than `200/201`, while the complete score variance consumes less than
`1881/7000` of its elementary `4x` curvature floor. Hence

\[
-(\log\Phi)''
>{20476\over2345}>8
\]

on the complete real line.

This is a strong source theorem, not a claim that log-concavity implies RH.

## 2. Exponential current/Turan envelope

The exterior-square conditional law gives

\[
R_H(\xi)
={e^{-H\xi}\over
 E[\sinh(2HX)/(2HX)]},
\]

and therefore

\[
R_H(\xi)\le e^{-H\xi}.
\]

For base `b`, scale `h`, and total height `H=b+h`,

\[
r_{b,h}(\xi)
\le {h\over H}e^{-H\xi}.
\]

The profile is thus simultaneously monotone, exponentially enveloped, and
backed by the higher exterior-square chaos reserve.

## 3. Exact model-space depth price

In the upper-half-plane Paley--Wiener normalization, every finite inner
function satisfies

\[
\operatorname{tr}_{K_B}M_{e^{-H\xi}}
={1\over2\pi H}
\int_{\mathbb R}(1-|B(x+iH/2)|^2)dx.
\]

One Blaschke zero at shifted depth `y` costs exactly

\[
{2y\over H+2y}.
\]

A finite anti-inner Xi-prime packet is consequently bounded by its vertical
depth sum. If `H=beta_1-delta`, `delta<=beta_1/2`, its current charge is at
most

\[
{4\delta\over\beta_1}N_1(T;H).
\]

Every fixed-depth packet is source-expensive; only a vanishing top collar can
become source-cheap.

## 4. Binding firewall

The same one-factor formula proves that weighted charge is not degree:

\[
\deg B_y=1,
\qquad
{2y\over H+2y}\to0.
\]

Therefore the depth theorem localizes the RH-bearing obstruction but does not
remove it. The live target is `BCOLLAR105643`: retain the signed all-pass index
or pointwise two-trace evaluation through the microscopic anti-inner collar.

## 5. Exact status

```text
uniform Xi strong log-concavity                 PROVED / REVIEW
current/Turan exponential envelope              PROVED EXACT
finite model-space exponential trace            PROVED EXACT
Xi-prime anti-inner soft-depth bound             PROVED EXACT
weighted charge -> degree shortcut              REFUTED
BCOLLAR105643                                    OPEN / RH-BEARING
POINTID105630                                    OPEN / RH-BEARING
ENDIDX105630                                     OPEN
Riemann Hypothesis                              UNPROVEN
```

Replay:

```text
PASS_X_105640_STRONG_LC_DEPTH_COLLAR
checks=4219
769c7f5f517949d0591e8cc33032a6f081abbf5ea43ad53556daeac2499b4a69
RH_UNPROVEN
```