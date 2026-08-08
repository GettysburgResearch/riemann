# M-29001 — Review protocol for the atomized carry-frame/end-point-tree route

Claim ID: `M-29001`  
Status: **FAIL-CLOSED REVIEW AND PRODUCTION PROTOCOL**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08

## 1. Review order

1. `L-29001-atomized-nyman-carry-frame.md`
2. `X-29001-atomized-carry-selberg-kummer/verify.py`
3. `L-29002-selberg-kummer-interior-reserve.md`
4. `L-29003-endpoint-balanced-tree-commutator.md`
5. `R-29001-fixed-abel-escalation-fails-through-order-eight.md`
6. PR #241 `L-9518` at its independent-frequency identity scope
7. PR #269 `L-26901`--`L-26904` at their source/carry scopes
8. PR #289 `L-27601`--`T-27601`
9. `T-29001-atomized-frame-endpoint-tree-rh-proposal.md`
10. a future source-complete `ETSR` certificate

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

## 4. Selberg–Kummer mutations

The checker must retain both pieces

```text
Lambda log
Lambda*Lambda
```

of the Selberg coefficient.  A claimed reserve is rejected if it:

- omits the linear term;
- replaces a carry indicator by an arbitrary vector;
- asserts strict reserve at `j=1` or `j=n-1`;
- takes rowwise absolute values before the coefficient identity;
- imports the generalized-prime row without separately auditing its digital correction.

The exact endpoint equality is a required mutation, not a nuisance boundary.

## 5. Endpoint-tree mutations

A production object must verify:

```text
partial T_n=e_n-n e_1;
L_q(T_n)=floor(n/q);
H(T_n)=log(n!);
[n,1] congruent T_n-T_(n-1);
```

and must retain:

- the outer coefficient `c_N T_N`;
- every first difference `c_n-c_(n+1)`;
- the signs of those differences;
- every Pascal-cycle correction;
- all tree roots at the current scale;
- all strict half-scale descendants.

A bound on total variation after taking absolute values is not an `ETSR`
certificate unless it is itself subpower and includes the outer tree.

## 6. Fixed-Abel firewall

The exact witnesses in `R-29001` must remain passing mutations.  Any proof that
uses complete monotonicity plus one fixed source-independent cumulative order
without addressing those witnesses is rejected.

## 7. Required `ETSR` output

A proof-producing certificate must emit:

1. a duplicate-free source manifest;
2. the full carry-position interval partition;
3. the exact normal Gram in rational endpoint form;
4. every Selberg forcing coefficient;
5. every pointwise reserve;
6. the endpoint coefficient sequence;
7. the tree/cycle ledger;
8. the destination scale of every child;
9. the total recurrence coefficient;
10. a separate prime-annulus and first-cell consumer.

The final recurrence may have coefficient one only if every child is separated
by a fixed positive logarithmic distance and the inhomogeneous channel is
proved polynomial.

## 8. Status firewall

```text
finite identities and reserve algebra    proposed complete / reviewable
ETSR recurrence                          open
ETSR -> RH                               conditional
RH                                       unproved
```

No finite computation, finite order, or empirical spectral radius may be
promoted to `ETSR`.