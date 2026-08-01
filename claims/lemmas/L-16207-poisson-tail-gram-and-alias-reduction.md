# L-16207 — The E-tail Gram is the prolate leakage Gram plus an explicit arithmetic alias remainder

Claim ID: `L-16207`  
Status: **PROVED DECOMPOSITION; FIXED-MODE ALIAS DECAY OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: Poisson summation for compact BV sources; `L-16205`, `L-16206`

## 1. Purpose

`L-16206` shows that the localized Weil source matrix factors exactly through
the omitted multiplicative tails. To compare the ordinary tail Gram with the
standard prolate defect, one must understand what the arithmetic map `E` does
to Fourier leakage.

The result is exact: the first sampling term is precisely the orthogonal
prolate leakage Gram, while every discrepancy is an explicit alias remainder
involving samples at integer multiples `2v,3v,...`.

## 2. Prolate modes and Fourier leakage

Let `f_n`, with indices `n=0,4,8,...`, be real even orthonormal functions
supported on `[-lambda,lambda]`, extended by zero. Suppose the finite Fourier
operator satisfies

```text
P_lambda F f_n=chi_n f_n,
0<chi_n<1,                                                (L-16207.1)
```

where `P_lambda` is the additive support projection and `F` is the unitary
Fourier transform in the CCM normalization.

Define the Fourier leakage

```text
r_n=F f_n-chi_n f_n.                                     (L-16207.2)
```

Then `r_n` vanishes almost everywhere on `[-lambda,lambda]`. Unitarity and
orthogonality give

```text
<r_m,r_n>_(L2(R))
 =(1-chi_n^2) delta_(mn).                                (L-16207.3)
```

Because the modes and leakages are even,

```text
boxed:
int_lambda^infinity r_m(v)r_n(v)dv
 =[(1-chi_n^2)/2] delta_(mn).                            (L-16207.4)
```

Put

```text
e_n=(1-chi_n^2)/2.                                       (L-16207.5)
```

If `d_n=1-chi_n`, then

```text
e_n=d_n(1+chi_n)/2=d_n(1+o(1))                           (L-16207.6)
```

at every fixed near-one prolate mode.

## 3. Multiplicative omitted tails

Assume the two source cancellations so that Poisson summation gives, almost
everywhere,

```text
E(f_n)(u)=E(F f_n)(u^-1).                                (L-16207.7)
```

Since `f_n` is supported on `[-lambda,lambda]`, `E(f_n)(u)=0` for `u>lambda`.
For `0<u<lambda^-1`, put `v=u^-1>lambda`. Every sample `kv` lies outside the
additive support, so

```text
E(f_n)(u)
 =E(r_n)(v)
 =v^(1/2) sum_(k>=1) r_n(kv).                            (L-16207.8)
```

Let `T_n` denote the omitted multiplicative tail. Its Gram is therefore

```text
boxed:
D_tail,(mn)
 =int_lambda^infinity
   [sum_(k>=1)r_m(kv)]
   [sum_(ell>=1)r_n(ell v)] dv.                          (L-16207.9)
```

The `k=ell=1` term is exactly the diagonal matrix

```text
D_0=diag(e_n).                                            (L-16207.10)
```

## 4. Alias remainder and exact bound

Define

```text
b_n(v)=sum_(k>=2) r_n(kv),
v>lambda,                                                 (L-16207.11)

alpha_n=||b_n||_(L2(lambda,infinity)),
s_n=sqrt(e_n).                                            (L-16207.12)
```

Then

```text
D_tail=D_0+R_alias,                                       (L-16207.13)
```

with the entrywise bound

```text
boxed:
|R_alias,(mn)|
 <=s_m alpha_n+alpha_m s_n+alpha_m alpha_n.              (L-16207.14)
```

Moreover, Minkowski and the substitution `x=kv` give the proof-producing
estimate

```text
boxed:
alpha_n
 <=sum_(k>=2) k^(-1/2)
   [int_(k lambda)^infinity |r_n(x)|^2dx]^(1/2).          (L-16207.15)
```

Thus the alias remainder depends only on the distribution of the known Fourier
leakage beyond successive multiples of the band edge.

## 5. Relative Gram theorem

For a fixed finite source packet `I`, define

```text
eta_n=alpha_n/s_n,
eta=max_(n in I)eta_n.                                    (L-16207.16)
```

Then, in the normalized leakage metric,

```text
boxed:
|[D_0^(-1/2)R_alias D_0^(-1/2)]_(mn)|
 <=eta_m+eta_n+eta_m eta_n.                              (L-16207.17)
```

Consequently, for packet size `r=|I|`,

```text
boxed:
||D_0^(-1/2)D_tail D_0^(-1/2)-I||_op
 <=r(2eta+eta^2).                                        (L-16207.18)
```

Hence

```text
eta->0
```

implies

```text
boxed:
D_tail=D_0^(1/2)(I+o_op(1))D_0^(1/2).                   (L-16207.19)
```

Together with (L-16207.6), the ordinary omitted-tail Gram has exactly the
prolate `d_0,d_4,d_8,...` hierarchy.

## 6. Proof

Equation (L-16207.3) follows from

```text
<Ff_m,Ff_n>=delta_mn
```

and the orthogonal decomposition

```text
Ff_n=chi_n f_n+r_n,
```

whose two terms have disjoint additive supports. Evenness gives half the total
leakage on the positive ray, proving (L-16207.4).

For compact BV functions, Poisson summation holds at continuity points and with
symmetric endpoint values; the exceptional set is measure zero. The two
cancellations remove the zero-frequency terms and give (L-16207.7). Equation
(L-16207.8) follows because every `kv` lies outside the support of `f_n`.
Changing variables under inversion gives (L-16207.9).

Write the bracket in (L-16207.9) as `r_n(v)+b_n(v)`. Expanding, applying
Cauchy--Schwarz, and using `||r_n||_(L2(lambda,infinity))=s_n` proves
(L-16207.14). Finally,

```text
||r_n(k .)||_(L2(lambda,infinity))^2
 =k^-1 int_(k lambda)^infinity |r_n(x)|^2dx,
```

and Minkowski proves (L-16207.15). Dividing (L-16207.14) by `s_ms_n` gives
(L-16207.17); the maximum row-sum bound gives (L-16207.18). QED.

## 7. Exact remaining tail-metric theorem

For the repaired source packet, it is sufficient to prove only

```text
boxed:
eta_n(lambda)->0
for n=0,4,8,12.                                          (L-16207.20)
```

No matrix-level superexponential estimate is needed. A stronger quantitative
version compatible with the Hardy fallback is

```text
lambda^(2tau_lambda) eta_n(lambda)->0.                    (L-16207.21)
```

The fixed-mode spheroidal radial asymptotics should decide this because the
alias terms begin at twice the band edge. This asymptotic has not yet been
reconstructed with a directed error bound in the CCM normalization.

## 8. Full revised bridge

Combining `L-16204`, `L-16206`, and this lemma, the source-sector part of the
original desired theorem follows from two dimensionless statements:

```text
A. prolate alias suppression:
   lambda^(2tau) max_(n=0,4,8,12) eta_n ->0;

B. normalized tail Weil scalarization:
   lambda^(2tau)(M_lambda-m_lambda)/(M_lambda+m_lambda)->0,
                                                                    (L-16207.22)
```

where `m_lambda,M_lambda` are the generalized eigenvalues of the tail Weil
matrix relative to `D_tail`.

The superexponential factor `d_8` has disappeared from both estimates because
it is carried exactly by the leakage Gram.

## 9. Proof boundary

The decomposition and bounds are exact. The fixed-mode alias suppression
(L-16207.20)--(L-16207.21) is not proved here, and neither is the normalized
tail Weil scalarization. The global floor/background/coupling gates of
`L-16201` also remain open. No RH proof is claimed.
