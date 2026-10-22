# M-29001 — Review protocol for the atomized carry-frame/source-matrix route

Claim ID: `M-29001`  
Status: **FAIL-CLOSED REVIEW AND PRODUCTION PROTOCOL**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08

## 1. Review order

1. `L-29001-atomized-nyman-carry-frame.md`
2. `X-29001-atomized-carry-selberg-kummer/verify.py`
3. `L-29002-selberg-kummer-interior-reserve.md`
4. `R-29002-rowwise-selberg-reserve-is-not-source-cone-coercivity.md`
5. `L-29003-endpoint-balanced-tree-commutator.md`
6. `L-29005-dyadic-filtered-endpoint-reserve.md`
7. `L-29006-positive-prime-endpoint-fiber-binding.md`
8. `X-29002-source-binding-firewall/verify.py`
9. `L-29004-prime-jensen-defect-and-convolution-energy.md`
10. PR #241 `L-9518` at its independent-frequency identity scope
11. PR #269 `L-26901`--`L-26904` at their source/carry scopes
12. PR #289 `L-27601`--`T-27601`
13. `T-29001-atomized-frame-endpoint-tree-rh-proposal.md`
14. a future source-complete `CISR` certificate

## 2. Mandatory normalization checks

A reviewer must reconstruct:

```text
s=z+1/2;
H_theta(u)=exp(-u/2)C(exp u,theta);
Hhat_theta=zeta(s)[1-theta^s-(1-theta)^s]/s;
Omega_2(s)=E(s)/zeta(s);
P_theta_hat=-E(s)N_theta(s) zeta'(s)/zeta(s).
```

The finite dyadic logarithmic gauge in `L-29001.20` must remain explicit.
Reject the packet if it replaces

```text
Lambda*omega_2
```

by

```text
-omega_2 log
```

without the `(e log)*mu` correction.

## 3. Atomized-frame mutations

Reject upon any of:

1. averaging `theta` before the square;
2. dropping the reflected `1-theta` Nyman generator;
3. using a one-frequency analytic square;
4. asserting that one chosen `theta` is nonzero at every zeta zero;
5. replacing the positive frame norm by a point sample;
6. omitting a breakpoint in the exact carry Gram;
7. losing one dyadic sibling in `omega_2`;
8. treating the gauge term as RH-bearing.

The correct pole firewall is the integrated frame factor

\[
 \mathfrak A_\eta(\rho)>0.
\]

## 4. Selberg–Kummer and source-cone mutations

The ordinary row checker must retain both pieces

```text
Lambda log
Lambda*Lambda
```

of the Selberg coefficient.  A claimed row reserve is rejected if it:

- omits the linear term;
- replaces a carry indicator by an arbitrary vector;
- asserts strict reserve at `j=1` or `j=n-1`;
- takes rowwise absolute values before the coefficient identity.

The source-coupled proof has two additional mandatory counterexamples:

```text
ordinary row (n,j)=(4,2), amplitude 1/2:
4 defect=-log(3/2)^2-4log(2)^2<0;

generalized-prime row (n,j)=(6,2):
P_omega^2-S_omega=log(3)log(25/32)<0.
```

Therefore reject any `CISR` object that:

- multiplies the ordinary row inequality by a source coefficient;
- asserts `P_omega^2>=S_omega`;
- checks only diagonal source blocks;
- omits any independent-frequency/source cross term.

The interior certificate must be a genuine Hermitian source matrix whose
diagonal specializes to `L-29002`.

## 5. Endpoint-fiber mutations

A production object must verify:

```text
partial T_n=e_n-n e_1;
L_q(T_n)=floor(n/q);
H(T_n)=log(n!);
D_n=T_n-T_(n-1);
W_n=D_n-(3/2)D_(2n)+(1/2)D_(4n);
W_n=(1/2)E_(2n)-E_n.
```

For the prime Jensen potential it must also verify, before any estimate,

```text
sum_r [A_x(r)-A_x(r-1)]D_r=sum_m Lambda(m)W_m.
```

The source coefficients on the right are nonnegative.  The checker must retain:

- all three jumps `m,2m,4m`;
- the aggregate endpoint Kummer coordinate;
- the aggregate endpoint Selberg coordinate;
- every dyadic annulus;
- the three-color assembly;
- all finite endpoints.

Reject a proof that re-expands `omega_2` and takes absolute values before the
complete `W_m` fiber is formed.

## 6. Fixed-Abel firewall

The exact witnesses in `R-29001` remain mandatory.  Complete monotonicity of the
critical target plus one fixed source-independent cumulative order does not
prove producer positivity.

## 7. Required `CISR` output

A proof-producing certificate must emit:

1. a duplicate-free ordinary-prime source manifest;
2. the full carry-position interval partition;
3. the exact normal Gram in rational endpoint form;
4. every Selberg linear and convolution matrix entry;
5. the complete coupled interior Schur complement;
6. the exact positive endpoint-fiber packet;
7. every annular physical-frame comparison;
8. every lower-scale destination;
9. the total recurrence coefficient;
10. a separate prime-annulus and first-cell consumer.

The final recurrence may have coefficient one only if every child is separated
by a fixed positive logarithmic distance and the inhomogeneous channel is
proved polynomial.

## 8. Status firewall

```text
finite frame and row algebra              proposed complete / reviewable
naive row-to-source lifts                 refuted
positive endpoint source binding          proposed complete / reviewable
coupled interior source matrix            open
CISR -> RH                                conditional
RH                                        unproved
```

No finite computation, diagonal-only matrix, finite Abel order, or empirical
spectral radius may be promoted to `CISR`.
