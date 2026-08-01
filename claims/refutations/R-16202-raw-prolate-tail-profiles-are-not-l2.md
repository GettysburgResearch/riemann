# R-16202 — Raw prolate-mode tails are not the admissible L2 profile packet

Claim ID: `R-16202`  
Status: **REFUTED AS FORMULATED; EXACT REPAIR GIVEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Targets: the raw-mode formulation in `L-16207` and `T-16202`

## 1. Decisive Poisson correction terms

Use the additive Fourier convention

```text
Ff(y)=integral_R f(x) exp(2 pi i x y) dx
```

and, for an even source,

```text
E(f)(u)=u^(1/2) sum_(n>=1) f(nu).
```

Poisson summation gives the exact identity

```text
E(f)(u)
 =E(Ff)(u^-1)
  +(1/2)[u^(-1/2) integral_R f
         -u^(1/2) f(0)].                                (R-16202.1)
```

This follows by separating the zero term in

```text
sum_(n in Z) f(nu)
 =u^-1 sum_(k in Z) Ff(k/u).
```

The source conditions

```text
f(0)=0,
integral_R f=0                                           (R-16202.2)
```

are therefore not cosmetic. They remove two explicit power-law terms.

## 2. Application to one positive prolate mode

Let `e_n` be one time-limited positive-Fourier prolate mode and write

```text
F e_n=chi_n e_n+r_n,
q_n=e_n(0),
ell_n=integral_R e_n=chi_n q_n.                          (R-16202.3)
```

For `u<lambda^-1`, put `v=u^-1>lambda`. Since every sample `kv` lies outside
the additive support of `e_n`, (R-16202.1) gives

```text
E(e_n)(u)
 =v^(1/2) sum_(k>=1) r_n(kv)
  +(1/2)[v^(1/2) ell_n-v^(-1/2)q_n].                    (R-16202.4)
```

For the modes `n=0,4,8,12`, neither `q_n` nor `ell_n` is zero. The first
correction in (R-16202.4) behaves like `u^(-1/2)` and is not square integrable
for `d*u=du/u` near zero.

Consequently, the individual objects denoted

```text
T_(n,lambda), n=0,4,8,12,
```

cannot be used as an ordinary L2 omitted-tail packet with Gram of order `d_n`.
The profile equation in the raw-mode version of `T-16202` is ill-posed in that
interpretation.

## 3. Exact repaired packet

Let `c=(c_0,c_4,c_8,c_12)` satisfy

```text
sum_n c_n q_n=0,
sum_n c_n ell_n=0.                                      (R-16202.5)
```

For

```text
f_c=sum_n c_n e_n,
r_c=sum_n c_n r_n,
```

all correction terms cancel exactly and

```text
boxed:
E(f_c)(u)
 =v^(1/2) sum_(k>=1) r_c(kv),
0<u<lambda^-1.                                          (R-16202.6)
```

This is the valid omitted-tail object. The first four positive modes have a
two-dimensional exact-radical coefficient space. A convenient basis is:

1. the repaired target `p_rad` from `T-16201`;
2. an independent vector satisfying the same two constraints, for example the
   `v_rad` vector used in the proof of the mode-8 theorem.

Only these repaired combinations, or another basis of the same constraint
space, should enter the tail-profile theorem.

## 4. The hierarchy survives the repair

Let `U_lambda` be a `4 x 2` coefficient matrix whose columns span

```text
ker[q^T; ell^T].                                         (R-16202.7)
```

The first-sample leakage Gram is exactly

```text
U_lambda^T
 diag((1-chi_n^2)/2)
U_lambda.                                                (R-16202.8)
```

By `T-16201`, after coefficient normalization its first two generalized scales
are

```text
Theta(d_4),
Theta(d_8).                                              (R-16202.9)
```

Thus the correction does not lose the target/next-mode separation. It merely
places the Poisson and Mellin analysis on the correct finite-dimensional
space.

## 5. Basis invariance

If `U` is replaced by `US` for an invertible `2 x 2` matrix `S`, every tail
Gram and Weil matrix changes by congruence. The generalized eigenvalues and all
relative scalarization statements are unchanged. The corrected theorem should
therefore be stated for the two-dimensional radical packet, not for four raw
mode labels.

## 6. Consequences for the four-gate program

Gate 1 must be replaced by

```text
widehat(T_(j,lambda))(s)
 =sqrt(delta_(j,lambda)/R_lambda)
  exp(-is x_lambda)
  Phi_(j,lambda)(s/R_lambda),

j=1,2,                                                    (R-16202.10)
```

where `T_1,T_2` are exact-radical combinations and

```text
delta_1=Theta(d_4),
delta_2=Theta(d_8).                                      (R-16202.11)
```

The correct profile Gram is the `2 x 2` Gram of these repaired tails.

## 7. Proof boundary

The Poisson identity and the scope refutation are exact. This claim does not
prove the radial asymptotics or the uniform profile theorem for the repaired
packet. It identifies the only packet on which those statements are
well-defined in the declared L2 geometry.
