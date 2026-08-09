# Endpoint negative drift and post-PR-351 route audit

Date: 2026-08-09  
Authoring agent: `gpt56-pro`  
Status: **new exact endpoint transform + RH-equivalent eventual-sign theorem; RH remains unproved**

## 1. Starting point

This pass began at PR #351, frozen at

```text
c83723e711aa18e94330c9c3b929c031af9d3974.
```

The main consolidation survives targeted review:

```text
T-90001   WSTS <=> RH architecture;
T-90002   dyadic z-collapse;
T-90003   GFEP above X/10 and the bottom-sign Landau fence;
T-90005   GFEP above X/20 and full GFEP -> RH;
T-90004   exact Q4 decompilation and Q4 gate -> RH.
```

The review changed route priority.  Q4 contains an unsmoothed Chebyshev
innovation, while WSTS has already collapsed to one twice-smoothed endpoint
scalar.  The latter is the logically minimal target.

## 2. Provenance repair

The text of `T-90001` still carries its historical Flag 0 saying that full
consumers are absent.  This branch imports the complete independent files from
PR #348:

```text
L-90006  resident WSTS -> prime ramp -> Landau -> RH;
L-90007  resident RH -> WSTS with the conservative O(log^4 X) bound.
```

`O-90007` records the updated flag ledger.  The equivalence no longer depends on
unavailable session transcripts.

## 3. New exact endpoint symbol

For

```text
A(X)=sum_p log(p) r_X(p),
```

`L-90004` derives the exact Mellin transform

```text
Ahat(z)=G(z+1/2)/z^2,
G(s)=D(s-1)/s-P1(s),
P1(s)=sum_p log(p)p^-s.
```

The shifted-multiple term is

```text
D(w)=sum_(r>=1)(-1)^(r+1)(w)_r/r! zeta(w+r)P1(w+r).
```

Möbius inversion gives

```text
P1(s)=sum_(m>=1)mu(m)(-zeta'/zeta)(ms).
```

The `m=2` copy of the main zeta pole produces

```text
G(1/2+z)=(1+zeta(1/2))/(2z)+O(1).
```

Therefore

```text
Ahat(z)=(1+zeta(1/2))/(2z^3)+O(z^-2).
```

The dyadic shell

```text
T(X)=A(X)-A(X/2)
```

has transform `(1-2^-z)Ahat(z)` and hence the exact negative drift coefficient

```text
kappa=(1+zeta(1/2))log(2)/2
     =-0.15954671491971181285...
```

This analytically explains the persistent negative endpoint shell seen in every
finite scan.  The coefficient is not fitted data; it is the prime-square pole of
the prime-only Euler series.

## 4. New RH-equivalent sign theorem

`T-90006` performs the pole audit and contour shift.

- The real pole at `s=1` cancels.
- Every nontrivial zero `rho` survives with shell residue
  
  ```text
  m_rho(1-2^(-(rho-1/2)))/(rho-1/2)^2.
  ```
- Under RH this zero series is absolutely bounded.
- The nearest unextracted prime-zeta singularity lies at `z=-1/6`.

Thus RH gives

```text
T_X^s(2)=kappa log X+O(1),
kappa<0.
```

Combining with `T-90002` yields the sharpened equivalence

```text
RH
<=> WSTS
<=> T_X^s(2)<=0 eventually
<=> B_X=0 eventually.
```

This is stronger descriptively than the old polylog bound: under RH the maximum
positive shell debt eventually vanishes exactly.

It is not an unconditional RH proof.  An off-line zero contributes an
`X^(Re rho-1/2)` oscillation and can dominate the logarithmic drift.  The final
sign remains precisely the zero-location problem.

## 5. Q4 status correction

`T-90004` correctly proves

```text
Q4 eventual gate -> RH
```

and identifies a Montgomery-class sufficient estimate.  It does not prove the
strict logical nonimplication `RH !-> Q4 gate`.  The fact that the standard RH
error term cannot prove the gate is not a separation theorem.

`R-90003` replaces the status by the justified arrows

```text
Montgomery-class estimate -> Q4 gate -> RH,
RH -> Q4 gate unknown.
```

This does not make Q4 the preferred producer: its zero response is still less
smoothed than the endpoint scalar.

## 6. GFEP continuation attempt

The certified `X/20` band was examined for a self-replicating Abel induction.
For one entrance coordinate define

```text
F(m)=m E_n(m,p),
c(m)=F(m)-F(m-1),
K=c*mu.
```

There is an exact transformed identity

```text
Sigma_(X,n)(p)=sum_(q<=X)K(q)w_X(q).
```

A natural proposal was to prove positivity of the fourth cumulative prefix of
`K`.  It fails exactly:

```text
X=1000, n=p=21,
C4(841)=-21060753/8.
```

`R-90004` and `X-90008` retain the Fraction-exact witness.  The GFEP coordinate
itself remains positive there; only the fixed-order sufficient mechanism is
false.  This confirms that the certified bands do not automatically propagate
to `n=o(X)` by a fixed number of Abel integrations.

## 7. Validation

`X-90007` independently checks:

```text
z^3 Ahat(z) -> (1+zeta(1/2))/2;
z^2 shell_hat(z) -> kappa;
```

and computes the finite scalar by exact radical switching.  Through `X=10^6`,
all retained dyadic shells are negative and `shell/log X` moves toward `kappa`.
The checker is explicitly regression-only; the contour shift is mathematical,
not delegated to floating data.

`X-90008` verifies the GFEP cumulative counterexample using only integers and
`fractions.Fraction`.

## 8. Current frontier

The strongest minimal statement is now one line:

```text
T_X^s(2)<=0 for every sufficiently large X.
```

It is equivalent to RH and has the exact decomposition

```text
negative prime-square drift
+ twice-smoothed zeta-zero Fourier series
+ decaying prime-zeta descendants.
```

The remaining problem is not floor geometry, tail maximization, source typing,
or a missing consumer.  It is to prove that the nonreal pole contribution cannot
overcome the explicit negative drift — equivalently, to locate the zeros.

RH remains unproved.
