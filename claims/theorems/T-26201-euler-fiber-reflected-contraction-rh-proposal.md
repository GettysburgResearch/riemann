# T-26201 — Critical Euler-fiber reflected contraction: a fixed-source RH proposal

Claim ID: `T-26201`  
Status: `FULL CONDITIONAL PROPOSAL — one explicit source-bound reflected contraction remains open`  
Scope: proposed completion joining carry/LP, signed defect transport, fixed-ratio Möbius shells, and reflected Selberg blocks  
Date: 2026-08-08  
Depends on: `L-26201`, `L-26202`; PR #241 `L-9518`; PR #234 fixed-ratio shell criterion; the corrected block-Laplace/Landau consumer

## 1. One fixed arithmetic source

Retain the coefficient sequence

\[
\sum_{n\ge1}\frac{b_{\mathcal E}(n)}{n^s}
=\frac{(1-2^{1-s})(1-2^{1/2-s})^2}{\zeta(s)}.
\tag{T-26201.1}
\]

Let `W` be the nonnegative compact window from `L-26201`,

\[
W=u_1*u_{1/2}*u_{1/2},
\qquad
\operatorname{supp}W\subset[0,3\log2].
\tag{T-26201.2}
\]

Define the centered compact signal

\[
\boxed{
Z(t)=
\sum_{n\ge1}
\frac{b_{\mathcal E}(n)}{\sqrt n}
W(t-\log n).}
\tag{T-26201.3}
\]

At each `t` this is a finite sum.  Its Laplace transform is

\[
\widehat Z(z)
=\widehat W(z)
\frac{P(z+1/2)}{\zeta(z+1/2)}.
\tag{T-26201.4}
\]

Neither factor in the numerator vanishes for

\[
0<\Re z<\frac12.
\tag{T-26201.5}
\]

Hence every hypothetical off-line zero produces an uncancelled pole of `widehat Z`.

For dyadic logarithmic blocks

\[
I_m=[m\log2,(m+1)\log2],
\tag{T-26201.6}
\]

put

\[
\boxed{
E_m=\int_{I_m}|Z(t)|^2dt.}
\tag{T-26201.7}
\]

The fixed-window Hardy/Laplace argument gives

\[
\boxed{
\mathrm{RH}
\iff
E_m=e^{o(m)}.}
\tag{T-26201.8}
\]

This is the same RH-bearing source as the carry profile of PRs #243/#247/#252 and the fixed-ratio Möbius shell of PRs #234/#236, after the exact Euler-fiber and Green transforms of `L-26201`.

## 2. Why this source is different from the rejected closures

The proposal uses none of the following false mechanisms:

```text
one-frequency global integral = one physical block;
conditional-Hankel positivity of the frozen carry spline;
absolute Bohr-rank bound independent of packet order;
nonnegative monotone Divisibility Cover;
terminal endpoint dimension as a substitute for signed cancellation.
```

Instead the source has four exact properties simultaneously:

1. a compact nonnegative window `W`;
2. a positive Dirichlet inverse `a_E`;
3. a nonnegative generalized prime sequence `Lambda_E^#`;
4. the strict annular multiplier reserve of `L-26202`.

It is also fixed: every odd Möbius coefficient is completed by one five-tap two-adic fiber.  There is no growing packet order and no claim that the odd-prime source has bounded rank.

## 3. Correct reflected block

Apply the conjugate-product Selberg identity to

\[
A_{\mathcal E}(s+it),
\qquad
A_{\mathcal E}(s-is),
\qquad
A_{\mathcal E}(s+it)A_{\mathcal E}(s-is),
\]

with two independent frequencies.  Multiply by the actual inverse pair and by the Fourier transforms of the fixed window packet

\[
\boxed{
\mathcal W=\operatorname{span}\{W,uW\}.}
\tag{T-26201.9}
\]

Here `uW` denotes `u mapsto uW(u)`.  PR #241 `L-9518` then gives the exact physical block in the factor-ratio normal orientation.  The second window is included because

\[
\sum_n\frac{b_{\mathcal E}(n)\log n}{\sqrt n}
 W(t-\log n)
=tZ(t)-
\sum_n\frac{b_{\mathcal E}(n)}{\sqrt n}
 (uW)(t-\log n).
\tag{T-26201.10}
\]

Thus the reflected logarithmic-derivative energy controls the original block after one fixed two-window completion; no growing derivative packet is required.

The reflected identity is an equality.  The new arithmetic theorem below is the required inequality.

## 4. Euler-Fiber Reflected Contraction (`EFRC`)

A production `EFRC` certificate consists, for every sufficiently large integer `m`, of the complete two-frequency physical block for the source `b_E` and the window packet `mathcal W`, with all quotient, cutoff, and endpoint terms retained before a norm.

It must prove an inequality of the form

\[
\boxed{
\kappa_0 m^2 E_m+Q_m
\le
C(1+m)^A
+
\sum_{r=1}^{4}\theta_r(m-r)^2E_{m-r},}
\tag{T-26201.11}
\]

where

\[
Q_m\ge0,
\qquad
\kappa_0>0,
\qquad
\theta_r\ge0,
\qquad
\boxed{\sum_{r=1}^{4}\theta_r<\kappa_0.}
\tag{T-26201.12}
\]

The certificate must bind these constants to the actual source.  In block-matrix language the same condition is obtained from

\[
G_m-C_m^*D_m^{-1}C_m\succeq\kappa_0G_m,
\tag{T-26201.13}
\]

followed by an exact routing of every unmatched dyadic boundary row to one of the four prior blocks.  The fixed number four comes from the complete local two-adic polynomial

\[
(1-z)(1-2z)(1-\sqrt2z)^2,
\]

not from an asserted bound on the odd-prime rank.

The source-bound production object must contain:

1. the complete five-tap two-adic fiber at every odd core;
2. the two-frequency block of PR #241;
3. the actual matrices `G_m,C_m,D_m` or an equivalent exact scalar ledger;
4. the strict Schur reserve;
5. every boundary destination and its coefficient;
6. the first `2/3` Mertens-shell mutation through the all-ratio causal transfer;
7. the same-sign odd Möbius-cube mutation.

## 5. `EFRC` implies RH

Put

\[
F_m=m^2E_m.
\]

Let

\[
\vartheta=\sum_{r=1}^{4}\theta_r<\kappa_0.
\]

Dropping `Q_m` from (T-26201.11) and taking a running maximum gives

\[
F_m
\le
C_1(1+m)^A
+\frac{\vartheta}{\kappa_0}
\max_{1\le r\le4}F_{m-r}.
\tag{T-26201.14}
\]

Since `vartheta/kappa_0<1`, elementary induction yields

\[
F_m=O((1+m)^A),
\]

and hence

\[
E_m=e^{o(m)}.
\tag{T-26201.15}
\]

Equation (T-26201.8) then gives RH.

Thus

\[
\boxed{
\mathrm{EFRC}\Longrightarrow\mathrm{RH}.}
\tag{T-26201.16}
\]

## 6. Relation to the carry/LP routes

The carry programmes currently expose the same final mode as:

```text
Greedy Slack / DCRS,

Green energy GET,

signed defect-to-slack transport,

continuum Gamma-carry minorants.
```

`L-26201` gives a direct source map from their continuum Green state to `Z`.  A successful `EFRC` proof therefore supplies the missing signed contraction rather than another equivalent scalar criterion.

Conversely, a sharp carry minorant immediately gives (T-26201.8), so the two endgames share one consumer while retaining genuinely different producers:

```text
positive carry producer
or
reflected Euler-fiber reserve
-> fixed source energy
-> RH.
```

## 7. Automatic rejection conditions

Reject the proposal if any one of the following occurs:

1. the actual reflected block is one-frequency rather than two-frequency;
2. the five-tap source omits a two-adic companion;
3. an internal face is taken in absolute value before source recombination;
4. the Schur reserve is zero or depends on the truth of RH;
5. the sum of lower-block charges is at least the reserve;
6. a boundary term remains at the current block;
7. the odd same-sign Möbius cube is silently deleted;
8. the `2/3` shell mutation is not reproduced;
9. finite block evidence is promoted to `EFRC` without a theorem uniform in `m`.

## 8. Exact status

```text
critical Euler-fiber algebra                 PROPOSED COMPLETE
positive inverse and generalized primes      PROPOSED COMPLETE
strict annular multiplier reserve             PROPOSED COMPLETE
fixed-source RH criterion                     PROPOSED COMPLETE TRANSFER
correct two-frequency reflected block         IMPORTED / REVIEWED
actual source-bound EFRC inequality            OPEN / RH-BEARING
EFRC -> polynomial block energy -> RH          PROPOSED COMPLETE
Riemann Hypothesis                             UNPROVED
```
