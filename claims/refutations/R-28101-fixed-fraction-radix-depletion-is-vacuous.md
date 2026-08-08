# R-28101 — The fixed-fraction radix depletion is vacuous on the top source

Claim ID: `R-28101`  
Title: A radix of size `exp(delta J)` shifts the complete top Möbius source beyond its finite coefficient range, so the advertised fixed-scale dipole is the original source  
Status: **EXACT SCOPE REFUTATION OF THE SCALE-ADAPTED RADIX IN PR #266**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #281  
Targets: PR #266 `L-25803`, `L-25806`, `D-25801`, `T-25801`  
Dependencies: PR #266 `L-25801`; elementary support arithmetic  
Scope: the fixed-fraction choice `Q >= V/2`; fixed radices such as `Q=2` survive

## 1. The top source has a large lower support edge

Retain

\[
r_V=\varepsilon-\mathbf1*\mu_V
\]

and

\[
T_{K,V}=\Lambda*r_V^{*(K-1)}.
\tag{R-28101.1}
\]

Every nonzero coefficient of `r_V` is supported at an integer at least `V+1`,
while `Lambda` is supported at integers at least `2`. Therefore

\[
\boxed{
\operatorname{supp}T_{K,V}
\subset
[\,2(V+1)^{K-1},\infty).
}
\tag{R-28101.2}
\]

The bound is coefficientwise and does not use cancellation.

## 2. Exact vanishing of a large multiplicative shift

Let `delta_Q` be the arithmetic atom at the integer `Q>=2`. If

\[
(\delta_Q*T_{K,V})(n)\ne0,
\]

then `Q` divides `n` and

\[
\frac nQ\ge2(V+1)^{K-1}.
\]

Consequently

\[
n\ge2Q(V+1)^{K-1}.
\tag{R-28101.3}
\]

Hence, coefficientwise through `V^K`,

\[
\boxed{
\delta_Q*T_{K,V}=0
\quad\text{whenever}\quad
2Q(V+1)^{K-1}>V^K.
}
\tag{R-28101.4}
\]

Since

\[
\frac{V^K}{2(V+1)^{K-1}}
=
\frac V2\left(\frac V{V+1}\right)^{K-1}
<\frac V2,
\]

the simpler sufficient condition is

\[
\boxed{Q\ge\lceil V/2\rceil.}
\tag{R-28101.5}
\]

## 3. Application to the PR #266 radix

PR #266 chooses

\[
Q=V^{m_K},
\qquad
m_K=\lfloor\delta_0K\rfloor
\]

or, in the later block formulation,

\[
Q=2^{\lfloor\delta_0J/\log2\rfloor}
=e^{\delta_0J+O(1)}
\]

for one fixed `delta_0>0`.

For every `K` with `m_K>=1`, the first choice has `Q>=V`. For the second choice,
when `J` is large and `K>1/delta_0`, one again has `Q>>V`. Thus (R-28101.4)
applies.

The proposed dipole

\[
D_Q=(\varepsilon-\delta_Q)T_{K,V}
\]

therefore satisfies

\[
\boxed{D_Q=T_{K,V}\qquad(n\le V^K).}
\tag{R-28101.6}
\]

Likewise

\[
Z_Q=\mathbf1*(\varepsilon-\delta_Q)*T_{K,V}
\]

reduces on the active range to

\[
Z_Q=\mathbf1*T_{K,V}.
\tag{R-28101.7}
\]

The identity

\[
\mu_V*Z_Q=T_{K,V}
\]

remains algebraically correct, but it creates neither a current/shifted pair
nor a fixed lower-scale source.

## 4. Consequence

The scale-adapted radix mechanism in PR #266 does not produce the proposed
recurrence

```text
current top source
= damped source at J-log Q
+ nontrivial dipole.
```

The shifted top source is absent before any estimate is made. The “dipole” is
the original RH-bearing source itself.

Therefore the following part of PR #266 is withdrawn:

```text
fixed-fraction radix depletion
-> strict multiplicative scale dipole
-> PADT recurrence.
```

This does not refute:

- the top-source normal form;
- the positive nonmultiple kernel;
- the exact finite nilpotence identity;
- a fixed radix `Q<V/2`;
- signed carry transport in another source coordinate;
- RH.

## 5. Correct replacement

The first nonvacuous canonical choice is the fixed dyadic radix

\[
Q=2.
\]

For sufficiently large `V`, `delta_2*T_(K,V)` occurs inside `V^K`. The resulting
fixed additive-delay filter is stably invertible and retains every off-line pole.
Its exact factorization is given in `L-28101`.

## 6. Proof boundary

Proved exactly:

- the support floor (R-28101.2);
- the shift-vanishing criterion (R-28101.4);
- vacuity of every `Q>=V/2`;
- failure of the fixed-fraction dipole interpretation.

Not proved here:

- contraction of the fixed dyadic dipole;
- the fibered factor-five boundary theorem;
- RH.
