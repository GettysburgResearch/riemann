# R-90201 — The frozen binary–ternary GFEP exit, producer positivity, and BTF all fail

Claim ID: `R-90201`  
Status: **PROPOSED COMPLETE ANALYTIC REFUTATION WITH DIRECTED INTERVAL CERTIFICATE — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Strengthened: 2026-08-10, near-conservation resonance  
Depends on: `L-90204`, `L-90205`, `L-90207`; exact first-entrance definitions of `L-28001/L-32301`; frozen producer `L-23811`  
Certificate: `X-90204-certified-fragmentation-resonance`  
Scope: refutes full coordinatewise GFEP, pointwise positivity, and subpower absolute variation of the frozen half-binary/half-ternary producer; it does not refute the downstream conditional consumers and does not prove or disprove RH

## 1. Two fixed traces at `n=2`

Let

\[
 \Sigma_2(X)=\Sigma_{X,2}(2)
 \tag{R-90201.1}
\]

be the bottom first-entrance exit of the frozen half-binary/half-ternary chain. Write

\[
 G_2(m)=mE_2(m,2),
 \qquad
 a_2(m)=G_2(m)-G_2(m-1).
 \tag{R-90201.2}
\]

The boundary is

\[
 G_2(1)=0,
 \qquad G_2(2)=2,
 \qquad G_2(3)=0,
 \tag{R-90201.3}
\]

and for every `m>=4`,

\[
 G_2(m)=\frac12\left[
 G_2(\lfloor m/2\rfloor)+G_2(\lceil m/2\rceil)
 +G_2(\lceil m/3\rceil)+G_2(\lfloor2m/3\rfloor)
 \right].
 \tag{R-90201.4}
\]

The actual producer trace at node two is

\[
 h_2(2)=1,
 \qquad h_2(3)=Q(3,2)=\frac23,
 \tag{R-90201.5}
\]

so

\[
 \boxed{
 P_2(X):=2A_X(2)
 =\Sigma_{X,2}(2)+\frac23\Sigma_{X,2}(3).
 }
 \tag{R-90201.6}
\]

Its Green trace satisfies

\[
 G_P(1)=0,
 \qquad G_P(2)=2,
 \qquad G_P(3)=2.
 \tag{R-90201.7}
\]

`L-90205` gives the exact global bounds

\[
 \boxed{|a_2(m)|\le4,\qquad |a_P(m)|\le2.}
 \tag{R-90201.8}
\]

## 2. Common characteristic

For either trace `T in {2,P}`, put

\[
 \mathcal A_T(u)=\sum_{m\ge1}a_T(m)m^{-u}
 \tag{R-90201.9}
\]

in its initial half-plane. `L-90205` proves

\[
 \boxed{
 \mathcal A_T(u)=\frac{N_T(u)}{\Delta(u)},
 \qquad \Re u>0,
 }
 \tag{R-90201.10}
\]

where `N_T` is analytic and

\[
 \boxed{
 \Delta(u)=1-\frac12\left[2^{1-u}+3^{-u}+(3/2)^{-u}\right].
 }
 \tag{R-90201.11}
\]

The finite renewal defects are

\[
 (b_2(1),b_2(2),b_2(3),b_2(4))=(0,2,-4,2),
 \tag{R-90201.12}
\]

\[
 (b_P(1),b_P(2),b_P(3),b_P(4))=(0,2,-2,0).
 \tag{R-90201.13}
\]

The rest of each numerator is the absolutely convergent shifted-difference series of `L-90205`.

## 3. Certified near-conservation resonance

Let

\[
\begin{aligned}
 c={}&0.9965737487663334042655023867051966592025584349245531871104107217274\\
 &+108.6843160063763813085769124318175668569125542061140136301106006425683i
\end{aligned}
 \tag{R-90201.14}
\]

and let

\[
 r=10^{-18}.
 \tag{R-90201.15}
\]

The directed verifier proves

\[
 |\Delta(c)|<1.717\times10^{-69},
 \tag{R-90201.16}
\]

\[
 |\Delta'(c)|>0.66532,
 \qquad
 \sup_{|u-c|\le r}|\Delta''(u)|<0.49760.
 \tag{R-90201.17}
\]

Hence, on `|w|=r`,

\[
 |\Delta(c)+R_2(w)|
 <2.488\times10^{-37}
 <6.653\times10^{-19}
 <|\Delta'(c)w|.
 \tag{R-90201.18}
\]

Rouché's theorem gives exactly one zero, counted with multiplicity, in the disk. Call it `u_0`. It is simple and

\[
 \boxed{
 \Re u_0>0.996573748766333403,
 \qquad \Im u_0\ne0.
 }
 \tag{R-90201.19}
\]

## 4. Directed numerator noncancellation

The verifier constructs every increment through `R=20000` as an exact `Fraction`, evaluates the complete finite numerator over a directed complex interval enclosure of the root disk, and bounds the remaining infinite series analytically.

For the bottom exit,

\[
 \boxed{|N_2(u_0)|>0.00987978337.}
 \tag{R-90201.20}
\]

For the sparse producer,

\[
 \boxed{|N_P(u_0)|>0.00199031875.}
 \tag{R-90201.21}
\]

The analytic tail estimate for a trace with `|a(m)|<=A_0` is

\[
\begin{aligned}
 T_R(u)
 \le{}&{A_0\over2}|u|
 \left[
 \alpha_2^{-\sigma-1}
 +2\alpha_3^{-\sigma-1}
 +{1\over2}(3/2)^{-\sigma-1}
 \right]{R^{-\sigma}\over\sigma},\\
 \alpha_2={}&2-{1\over R+1},
 \qquad
 \alpha_3=3-{2\over R+1},
 \qquad
 \sigma=\inf\Re u.
\end{aligned}
 \tag{R-90201.22}
\]

and gives

\[
 T_R<0.007855148\quad(T=2),
 \qquad
 T_R<0.003927574\quad(T=P).
 \tag{R-90201.23}
\]

These are already subtracted in the margins (R-90201.20)--(R-90201.21). Thus both continued fragmentation factors have a genuine simple pole at `u_0`.

There is also an exact structural check. The two exit traces satisfy

\[
 G_2(m)+G_3(m)=m,
 \tag{R-90201.24}
\]

and the producer trace is `G_P=G_2+(2/3)G_3`. The total trace has no nonconservation characteristic pole, so at every zero of `Delta` other than `u=1`,

\[
 \boxed{N_P(u)=\frac13N_2(u).}
 \tag{R-90201.25}
\]

The independent directed producer calculation is retained as a mutation check.

## 5. Physical Mellin poles

By `L-90204`, with

\[
 s_0=u_0-\frac12,
 \tag{R-90201.26}
\]

we have

\[
 \boxed{
 \widehat{\Sigma_2}(s)
 =\frac{N_2(s+1/2)}
 {s^2\Delta(s+1/2)\zeta(s+1/2)},
 }
 \tag{R-90201.27}
\]

and

\[
 \boxed{
 \widehat{P_2}(s)
 =\frac{N_P(s+1/2)}
 {s^2\Delta(s+1/2)\zeta(s+1/2)}.
 }
 \tag{R-90201.28}
\]

The certified pole satisfies

\[
 \boxed{
 \Re s_0>0.496573748766333403.
 }
 \tag{R-90201.29}
\]

The reciprocal zeta factor cannot cancel this pole: `1/zeta(u)` has a zero only at the pole `u=1`; if `u_0` itself were a zeta zero, it would add another pole.

## 6. No positive-real singularity

For real `s>1/2`, the original absolutely convergent factorization is analytic.

For `0<s<1/2`, put `u=s+1/2 in (1/2,1)`. The real function

\[
 2^{1-u}+3^{-u}+(3/2)^{-u}
\]

is strictly decreasing and equals two only at `u=1`; hence `Delta(u)\ne0`. Also `zeta(u)\ne0` on `(0,1)`: the alternating eta series is positive for `u>0`, while

\[
 \zeta(u)=\frac{\eta(u)}{1-2^{1-u}}.
\]

At `s=1/2`, `Delta(u)` has a simple zero and `zeta(u)` has a simple pole, so

\[
 \Delta(u)\zeta(u)\longrightarrow\Delta'(1)\ne0.
 \tag{R-90201.30}
\]

The apparent point is removable. Both physical transforms are therefore holomorphic at every positive real `s`.

## 7. Integer oscillation and essentially square-root excursions

The increment bounds and `L-90207` give

\[
 |\Sigma_2(X)-\Sigma_2(\lfloor X\rfloor)|
 \le16{1+\log X\over\sqrt X},
 \tag{R-90201.31}
\]

\[
 |P_2(X)-P_2(\lfloor X\rfloor)|
 \le8{1+\log X\over\sqrt X}.
 \tag{R-90201.32}
\]

The nonreal pole and absence of positive-real singularities imply

\[
 \boxed{
 \Sigma_{N,2}(2)
 \text{ takes both signs for arbitrarily large integers }N,
 }
 \tag{R-90201.33}
\]

and

\[
 \boxed{
 A_N(2)
 \text{ takes both signs for arbitrarily large integers }N.
 }
 \tag{R-90201.34}
\]

More sharply, for every

\[
 0\le\delta<0.496573748766333403,
 \tag{R-90201.35}
\]

we have

\[
 [\Sigma_{N,2}(2)]_+,
 \ [-\Sigma_{N,2}(2)]_+
 \ne O(N^\delta),
 \tag{R-90201.36}
\]

and

\[
 [A_N(2)]_+,
 \ [-A_N(2)]_+
 \ne O(N^\delta).
 \tag{R-90201.37}
\]

Thus the deterministic policy creates two-sided excursions at every fixed exponent strictly below square root up to the certified gap `0.003426...`.

## 8. Consequences

1. **GFEP-full is false.** The fixed coordinate `(n,p)=(2,2)` is negative at arbitrarily large integer endpoints.
2. **Pointwise positivity of the frozen half-binary/half-ternary producer is false.** Its node-two coefficient changes sign cofinally.
3. **The frozen BTF estimate `L-23811.13` is false.** Since
   \[
   \operatorname{BTF}(N)
   =\sum_{n=2}^N|A_N(n)|\sqrt n
   \ge\sqrt2|A_N(2)|,
   \]
   it is not `O(N^delta)` for any `delta<0.496573748766333403`, and in particular is not `N^{o(1)}`.
4. The weaker signed pairing condition `L-23811.15`, Cycle Debt, and state-dependent policies are not refuted by this single coordinate.
5. The conditional implications from GFEP, positivity, or BTF to RH remain logically valid; their frozen-policy antecedents are false.

## 9. Route consequence

The Exact Flow Gambit and the fixed binary–ternary producer now have a definitive status:

```text
positive packet kernels                    PROVED
nonempty multiplicative directions         PROPER DESCENDANTS
empty frozen coefficient                   CERTIFIED OSCILLATORY
GFEP-full                                   REFUTED
frozen producer positivity                 REFUTED
frozen BTF absolute variation              REFUTED NEAR SQUARE-ROOT SCALE
signed pairing / Cycle Debt                STILL LIVE
```

A future fragmentation route must change the policy, retain signed cancellation, or use a different consumer. `L-90208` identifies the resonance-free uniform Pascal policy as the canonical remaining stationary front.

## 10. Certificate boundary

`X-90204-certified-fragmentation-resonance` verifies:

- one simple characteristic zero in the stated disk by Rouché;
- exact dyadic recurrence coefficients;
- directed finite numerator intervals;
- analytic infinite-tail bounds;
- nonzero exit and producer margins;
- 39,998 exact trace-relation checks.

The Landau, quantitative excursion, and integer-interpolation deductions are proved in `L-90207` and this file.

This refutation proves no statement about the truth or falsity of RH. It does not refute the prime-endpoint, annular, uniform-Pascal, signed-pairing, or cycle-optimized routes.
