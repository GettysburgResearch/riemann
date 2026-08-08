# Parity–Green two-frequency continuation

Date: 2026-08-08  
Agent: `gpt56-pro-09-p`  
Base: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Status: **SERIOUS FULL PROPOSAL WITH ONE SOURCE-SPECIFIC FINITE-PREFIX THEOREM OPEN**  
RH status: **UNPROVED**

## 1. Objective

The prior parity-comb route had reduced the fixed-ratio Möbius shell to the positive kernel

```text
P_2(t)=exp(-t/2) 1_(floor(exp t) odd),
```

but had not produced a source lower bound. This pass returns to that exact object with the newest carry and Green-correction work in view. The main question was whether a genuine two-frequency inequality could be obtained without replacing the RH-bearing source by a generic operator norm.

## 2. Exact positive digit-comb family

For every integer `p>=2`, define

```text
P_p(t)=exp(-t/2) (floor(exp t) mod p).
```

Then

```text
(partial+1/2)P_p
 =sum_n [1-p 1_(p|n)]/sqrt(n) delta_(log n),
```

and

```text
Laplace[P_p](z)
 =[1-sqrt(p) exp(-z log p)] zeta(z+1/2)/(z+1/2).
```

Convolution with the complete Möbius source gives one two-tap exponential. Convolution with the Euler-aligned source

```text
beta_p=(I-p^(-1/2) tau_(log p)) alpha_mu
```

gives a three-tap exponential supported on `[0,2 log p]`.

This is useful exact structure, but it also supplies a decisive scope warning: a positive digit comb can have compact output on the actual cofinal source. Therefore one-kernel translated-tail coercivity is impossible.

## 3. Exact parity/carry dipole

Let `k` be the continuum carry kernel from PR #252. Its transform and the parity transform share the complete zeta factor. Their quotient is nevertheless elementary:

```text
P_2 = ell * k,
ell = delta_0-sqrt(2)delta_h+2 exp(t/2)1_[0,h)(t)dt,
h=log 2.
```

Equivalently,

```text
(partial-1/2)P_2
 =(partial+3/2)(I-sqrt(2)tau_h)k.
```

On `L2(exp(-t)dt)`, the dyadic shift `U=sqrt(2)tau_h` is unitary. A finite-run discrete Poincare inequality gives

```text
||f||_[0,Nh] <= N ||(I-U)f||_[0,Nh].
```

Thus, for any smoothed causal source `gamma`,

```text
||k*gamma||_[0,Nh]
 <= (N/2) ||(partial-1/2)(P_2*gamma)||_[0,Nh].
```

This is a genuine finite-horizon comparison of the two positive output channels. It does not invert their common zeta factor.

For the canonical carry inverse `g`, the two exact outputs are positive:

```text
k*g=t,
P_2*g=r(t)>=0,
```

with `r` given explicitly by one exponential branch on `[0,log2)` and one increasing affine branch thereafter.

## 4. Bulk rank-one no-go

Because

```text
P_hat=zeta*N_P,
k_hat=zeta*N_K,
```

the pointwise two-channel spectral Gram has determinant zero. Any strict reserve must therefore come from finite boundaries, the endpoint-projected Green correction, or a source-specific signed transport. A generic bulk `2x2` frame cannot prove RH.

This is recorded as `R-23007` so the new two-frequency language is not mistaken for an automatic source coercivity theorem.

## 5. Exact dyadic Green path

At `X=2^N`, the power-of-two principal block of the endpoint-projected divisor Green matrix is

```text
G(2^a,2^b)=2^(N-max(a,b)+1)-1-2^(-N).
```

It factors as

```text
t^T G t = sum_a d_a (sum_(j<=a)t_j)^2,
```

with explicit positive weights. Its inverse is tridiagonal, and the dyadic correction energy is exactly

```text
sum_(a<N) (r_a-r_(a+1))^2/d_a + r_N^2/d_N.
```

Therefore the entire power-of-two carry sector is coercive and machine-free. The remaining finite obstruction lies in the odd/mixed Schur complement and in preserving coefficient nonnegativity while deforming the canonical signed Green correction.

## 6. Digital recurrence and compact tail

The aligned shell satisfies the exact recurrence

```text
B_2(x)
 =-1-sum_(k>=3)[1-v_2(k)] B_2(x/k).
```

In logarithmic normalization,

```text
q(t)
 =-exp(-t/2)
  -sum_(k>=3)[1-v_2(k)]/sqrt(k) q(t-log k).
```

Split this operator at a finite prefix `R`. Abel summation uses the exact partial sums

```text
sum_(n<=N)[1-v_2(n)] = s_2(N) <= 1+log(N)/log 2
```

to prove

```text
||T_R f||_2
 <= epsilon_R (||f||_2+||f'||_2),
epsilon_R=O(log R/sqrt R).
```

Thus all infinite digital arithmetic is an arbitrarily small `H1 -> L2` perturbation of one finite delay system.

## 7. Proposed closing theorem

The remaining theorem is `PGC(R)`, finite-prefix parity–Green coercivity.

For an unbounded sequence of prefixes `R`, the exact independent-frequency reflected normal block, the explicit dyadic Green projection, and a positivity-preserving signed deformation of the odd/mixed Green correction must prove

```text
||q_H||_(H1(0,J))^2
 <= C (log R)^A
    [1+||A_R q_H||_(L2(0,J+C_H))^2].
```

This is source-specific. The certificate must retain every cross term of PR #241's two-frequency identity and cannot use the rank-one bulk pair as a strict frame.

Substitution of the digital recurrence gives

```text
E(J)
 <= C(log R)^A [1+epsilon_R^2 E(J-log R+O(1))].
```

Since

```text
(log R)^A epsilon_R^2
 =O((log R)^(A+2)/R),
```

one sufficiently large retained prefix gives strict contraction and subexponential dyadic-shell energy. The reviewed all-ratio filters then export the exact `2/3` first Farey cell, and RH follows through the fixed-ratio Mertens criterion.

## 8. Exact regression

`X-23005` verifies:

```text
positive digit-comb rows                         768
digital recurrence rows                         191
dyadic Green entries                            203
dyadic cumulative-square controls                49
finite-horizon Poincare matrix entries           263
formal parity/carry quotient and rank-one rows     3
mutation tests                                   8/8 PASS
```

Retained proof-object SHA-256:

```text
8fa35fbb1fd6643c2aea6b6c1e660c21e47ba1a473204eb549ef2dc3a6ee45ad
```

This is exact finite algebra only.

## 9. Exact boundary

```text
positive p-adic digit combs                   PROPOSED COMPLETE
parity/carry compact dipole                   PROPOSED COMPLETE
finite-horizon output inequality              PROPOSED COMPLETE
dyadic Green path factorization               PROPOSED COMPLETE
digital Sobolev tail                          PROPOSED COMPLETE
bulk source coercivity                        REFUTED
two-frequency finite-prefix PGC(R)            OPEN
PGC(R) => dyadic shell => 2/3 cell => RH      COMPLETE CONDITIONAL
Riemann Hypothesis                            UNPROVED
```

The proposal is now materially stronger than a restatement of an RH-equivalent shell bound. It proves that the infinite tail, complete dyadic carry sector, and bulk two-channel ambiguity are no longer the unknowns. The surviving theorem is a finite, source-specific Schur reserve with an explicit polylogarithmic conditioning target.
