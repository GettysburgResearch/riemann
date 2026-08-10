# R-90201 — The frozen binary–ternary GFEP exit and producer are not eventually positive

Claim ID: `R-90201`  
Status: **PROPOSED COMPLETE ANALYTIC REFUTATION WITH DIRECTED INTERVAL CERTIFICATE — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90204` Euler–fragmentation factorization; `L-90205` renewal continuation; `L-90207` integer Landau transfer; exact first-entrance definitions of `L-28001/L-32301`  
Certificate: `X-90204-certified-fragmentation-resonance`  
Scope: refutes full coordinatewise GFEP and pointwise positivity of the frozen half-binary/half-ternary producer; it does not refute the conditional implications from those hypotheses to RH and does not prove or disprove RH

## 1. Two fixed traces at `n=2`

Let

\[
 \Sigma_2(X)=\Sigma_{X,2}(2)
 \tag{R-90201.1}
\]

be the bottom first-entrance exit of the frozen half-binary/half-ternary chain.

Write

\[
 G_2(m)=mE_2(m,2),
 \qquad
 a_2(m)=G_2(m)-G_2(m-1).
 \tag{R-90201.2}
\]

The boundary values are

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

The actual producer trace at `n=2` uses

\[
 h_2(2)=1,
 \qquad
 h_2(3)=Q(3,2)=\frac23.
 \tag{R-90201.5}
\]

Put

\[
 P_2(X)=2A_X(2)
 =\Sigma_{X,2}(2)+\frac23\Sigma_{X,2}(3),
 \tag{R-90201.6}
\]

and let

\[
 G_P(m)=mh_2(m),
 \qquad a_P(m)=G_P(m)-G_P(m-1).
 \tag{R-90201.7}
\]

Its boundary values are

\[
 G_P(1)=0,
 \qquad G_P(2)=2,
 \qquad G_P(3)=2,
 \tag{R-90201.8}
\]

with the same recurrence above the boundary.

`L-90205` gives the global exact bounds

\[
 |a_2(m)|\le4,
 \qquad
 |a_P(m)|\le2.
 \tag{R-90201.9}
\]

## 2. Common characteristic and trace numerators

For either trace `T in {2,P}`, put

\[
 \mathcal A_T(u)=\sum_{m\ge1}a_T(m)m^{-u}
 \tag{R-90201.10}
\]

in the initial half-plane. `L-90205` proves the continuation

\[
 \boxed{
 \mathcal A_T(u)={N_T(u)\over\Delta(u)},
 \qquad \Re u>0,
 }
 \tag{R-90201.11}
\]

where

\[
 \Delta(u)=1-\frac12
 \left[2^{1-u}+3^{-u}+(3/2)^{-u}\right]
 \tag{R-90201.12}
\]

and `N_T` is analytic on `Re u>0`.

For reference, the finite renewal defects on `m=1,2,3,4` are

\[
 (b_2(1),b_2(2),b_2(3),b_2(4))=(0,2,-4,2),
 \tag{R-90201.13}
\]

\[
 (b_P(1),b_P(2),b_P(3),b_P(4))=(0,2,-2,0).
 \tag{R-90201.14}
\]

The remaining parts of `N_T` are the absolutely convergent shifted-difference series of `L-90205`.

## 3. Certified simple resonance

Define

\[
\begin{aligned}
 c={}&0.7422293980561885240550493534416845585452288947464107663790628089924\\
 &+17.3619424994722740596801161362202749268628893017519727763861538918768i
\end{aligned}
 \tag{R-90201.15}
\]

and

\[
 r=10^{-18}.
 \tag{R-90201.16}
\]

The directed interval verifier proves on the disk `|u-c|<r`:

\[
 |\Delta(c)|<3.425\times10^{-68},
 \tag{R-90201.17}
\]

\[
 |\Delta'(c)|>0.70517,
 \qquad
 \sup_{|u-c|\le r}|\Delta''(u)|<0.61507.
 \tag{R-90201.18}
\]

Thus on `|w|=r`,

\[
 |\Delta(c)+R_2(w)|
 <3.076\times10^{-37}
 <7.051\times10^{-19}
 <|\Delta'(c)w|,
 \tag{R-90201.19}
\]

where `|R_2(w)|<=sup|Delta''|r^2/2`. Rouché's theorem gives exactly one zero, counted with multiplicity, in the disk. Denote it by `u_0`. It is simple and satisfies

\[
 \boxed{
 \Re u_0>0.742229398056188523,
 \qquad
 \Im u_0\ne0.
 }
 \tag{R-90201.20}
\]

## 4. Certified numerator noncancellation

The verifier constructs every increment through `R=20000` as an exact `Fraction`, evaluates the finite numerator over the complete rectangular enclosure of the root disk with directed complex interval arithmetic, and bounds the infinite shifted-difference tail using (R-90201.9).

For the exit trace,

\[
 |N_2(u_0)|>0.2815082855.
 \tag{R-90201.21}
\]

For the sparse producer trace,

\[
 |N_P(u_0)|>0.0895557448.
 \tag{R-90201.22}
\]

The tail estimate used for a trace with `|a(m)|<=A_0` is

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
 \tag{R-90201.23}
\]

It gives the directed upper bounds

\[
 T_R<0.025277315\quad(T=2),
 \qquad
 T_R<0.012638658\quad(T=P),
 \tag{R-90201.24}
\]

well below the finite interval modulus margins.

Therefore both continued fragmentation factors have a genuine simple pole at `u_0`.

## 5. Physical Mellin poles

By `L-90204`, with

\[
 s_0=u_0-\frac12,
 \tag{R-90201.25}
\]

we have

\[
 \boxed{
 \widehat{\Sigma_2}(s)
 ={N_2(s+1/2)
   \over s^2\Delta(s+1/2)\zeta(s+1/2)},
 }
 \tag{R-90201.26}
\]

and

\[
 \boxed{
 \widehat{P_2}(s)
 ={N_P(s+1/2)
   \over s^2\Delta(s+1/2)\zeta(s+1/2)}.
 }
 \tag{R-90201.27}
\]

The point `s_0` is nonreal and

\[
 \boxed{
 \Re s_0>0.242229398056188523.
 }
 \tag{R-90201.28}
\]

Since $u_0\ne1$, the meromorphic function `1/zeta(u)` cannot have a zero there; if `u_0` happens to be a zeta zero, it contributes an additional pole rather than a cancellation. Hence both transforms are singular at `s_0`.

## 6. No positive-real singularity

For real `s>1/2`, the original absolutely convergent fragmentation/Euler factorization is analytic.

For `0<s<1/2`, put $u=s+1/2\in(1/2,1)$. The real function

\[
 2^{1-u}+3^{-u}+(3/2)^{-u}
\]

is strictly decreasing and equals two only at `u=1`; hence $\Delta(u)\ne0$. Also $\zeta(u)\ne0$ on the real interval $(0,1)$: the alternating eta series is positive for $u>0$, while $\zeta(u)=\eta(u)/(1-2^{1-u})$.

At `s=1/2`, `Delta(u)` has a simple zero and `zeta(u)` has a simple pole, so

\[
 \Delta(u)\zeta(u)\longrightarrow\Delta'(1)\ne0.
 \tag{R-90201.29}
\]

Because each `N_T` is analytic, the apparent point is removable. Thus both continued physical transforms are holomorphic at every positive real `s`.

## 7. Integer sign oscillation and refutation

The increment bounds (R-90201.9) and `L-90207` give

\[
 |\Sigma_2(X)-\Sigma_2(\lfloor X\rfloor)|
 \le16{1+\log X\over\sqrt X},
 \tag{R-90201.30}
\]

\[
 |P_2(X)-P_2(\lfloor X\rfloor)|
 \le8{1+\log X\over\sqrt X}.
 \tag{R-90201.31}
\]

Each transform has a nonreal singularity with positive real part and no positive-real singularity. Applying `L-90207` separately to each trace gives

\[
 \boxed{
 \Sigma_{N,2}(2)
 \text{ takes both signs for arbitrarily large integers }N,
 }
 \tag{R-90201.32}
\]

and

\[
 \boxed{
 A_N(2)
 \text{ takes both signs for arbitrarily large integers }N.
 }
 \tag{R-90201.33}
\]

Consequently:

1. **GFEP-full is false.** The fixed coordinate `(n,p)=(2,2)` is negative at arbitrarily large integer endpoints.
2. **Pointwise positivity of the frozen half-binary/half-ternary producer is false.** Its coefficient at node two is negative at arbitrarily large endpoints.
3. The conditional implications
   \[
   \mathrm{GFEP}\Rightarrow\mathrm{RH}
   \]
   and
   \[
   \text{producer positivity}\Rightarrow\mathrm{RH}
   \]
   remain logically valid; this theorem refutes their antecedents, not their consumers.
4. The positive-kernel, flow, and Boolean-descendant identities remain exact. Their empty Möbius boundary coefficient oscillates because a deterministic fragmentation resonance survives.

## 8. Route consequence

The Exact Flow Gambit has now reached a definitive end for the frozen binary–ternary chain:

```text
positive packet kernels                    PROVED
multiplicative/nonempty class directions   DESCENDANT-POSITIVE
empty current coefficient                  CERTIFIED OSCILLATORY
GFEP-full                                   REFUTED
frozen producer pointwise positivity       REFUTED
```

A future fragmentation route must change the policy/kernel, weaken the target to a signed debt estimate, or use a different analytic consumer. It cannot complete RH by proving eventual positivity of this frozen producer.

## 9. Certificate and proof boundary

`X-90204-certified-fragmentation-resonance` verifies:

- one simple characteristic zero in the stated disk by Rouché;
- exact dyadic increment recurrences;
- directed finite numerator intervals;
- analytic infinite-tail bounds;
- nonzero exit and producer numerator margins.

The Landau and integer-interpolation deductions are proved in prose in `L-90207` and this file.

This refutation proves no statement about the truth or falsity of RH. It also does not refute Cycle Debt, prime-endpoint criteria, or alternative state-dependent fragmentation policies.
