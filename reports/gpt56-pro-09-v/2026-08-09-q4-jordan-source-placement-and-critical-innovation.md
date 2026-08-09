# Q=4 Jordan source placement and critical-innovation synthesis

Date: 2026-08-09  
Agent: `gpt56-pro-09-v`  
Branch: `agent/gpt56-pro-09-v/339-q4-jordan-carry-identification`  
Parent: PR #339  
Status: **NEW EXACT THEOREMS; RH REMAINS UNPROVED**

## Executive result

The Q=4 Euler--Blaschke route has moved past its former source-placement and terminal-state ambiguities.

This branch proves, subject to independent review:

1. physical prefix localization and atomized carry localization are exactly identical for every source of the form `c=1*f`;
2. the *entire* Q=4 Jordan physical deformation is therefore the exact carry transform of the same source-convolved Jordan state;
3. the true Q=4 pole current is exactly the `q_4` carry current from the augmented reserve, not a surrogate coordinate;
4. product-source Jordan curvature and augmented Kummer curvature cancel the inverse-source `Y T` term algebraically;
5. ordinary PNT plus the exact four-adic renewal closes the previously miscited cofinal current/full-reserve ratio;
6. the complete augmented reserve is uniformly positive directly on the continuous balanced carry-position bank;
7. the all-pass terminal Jordan state is a positive four-adic filter and has cofinally nonnegative curvature;
8. every adverse endpoint row of the compact main-pole-killing innovation current is only a fixed-width local generalized-prime sum of logarithmic size;
9. the critical-scale radix-four reserve increment is exactly a relative Jordan log-curvature.

The remaining RH-bearing theorem is no longer physical/carry placement, endpoint control, terminal-state sign, or inverse-source curvature. It is a source-specific control of the **balanced compact one-step current innovation** by the newly created radix-four reserve, equivalently the missing second parameter in a `2 x 2` relative Jordan/Schur curvature certificate.

No proof of that final domination is claimed here.

## 1. Exact physical/carry identity

For `c=1*f`,

```text
centered prefix defect of c
= atomized carry transform of f
```

for every real parent `X` and carry position `theta`.

For the Q=4 Jordan family,

```text
c_(4,tau)=e_4*J_(4,tau)=1*K_(4,tau),
K_(4,tau)=b_4*J_(4,tau).
```

Hence

```text
physical Jordan field
= carry(K_(4,tau))
```

exactly. Its first jets are the existing source coordinates

```text
Y = carry(b_4),
Q = carry(q_4),
T = carry(t_4).
```

This is `L-34001`.

## 2. Exact no-double-spend curvature cancellation

The physical Jordan energy satisfies pointwise

```text
(1/2) E''(0)=Q^2+Y T.
```

The source-complete augmented row reserve is

```text
A=R+Q^2-Y T.
```

Therefore

```text
A+(1/2)E''(0)=R+2Q^2.
```

The inverse-source `Y T` cross term has disappeared identically. A future proof must not charge it a second time.

## 3. Repair of the Q=4 current/reserve dependency

The current PR #325 description uses the correct physical-current asymptotic, but its historical file dependency was ambiguous. `L-34002` supplies a direct proof.

The exact renewal is

```text
G_4(X)=G_4(X/4)+H_4(X),
H_4(X)=psi(X)-4psi(X/4)+3 floor(log_4 X) log4.
```

PNT gives `H_4(X)=o(X)`. Geometric iteration gives

```text
G_4(X)=o(X).
```

Thus on quarter-balanced rows

```text
Q_4^phys(n,j)=o(n)
```

uniformly. Since the deterministic Q=4 Kummer reserve is `Omega(n^2)`,

```text
|Q_4^phys|^2/R_4 -> 0.
```

This is an ordinary-PNT-scale theorem and is not the critical innovation bound.

## 4. Continuous source-complete reserve

For real `X` and fixed balanced `theta`, the carry indicator is exactly the floor defect of

```text
N=floor X,
J=floor(theta X),
K=floor((1-theta)X),
J+K in {N-1,N}.
```

The continuous Q=4 coordinates obey

```text
P = Omega(X),
S = O(X log X),
Y = O(log X),
T = O(X log^4 X).
```

Therefore

```text
A(X,theta)=P^2-S+Q^2-YT >= c_eta X^2
```

uniformly on every fixed balanced interval, outside a finite base. This is `L-34003`.

The source-complete augmented Jordan reserve is therefore already positive in the actual continuous physical carry-position geometry.

## 5. Terminal all-pass state

The Q=4 unitary scattering state is

```text
x_K=(sqrt3/2) sum_(r=0)^(K-1) 2^-r u_(K-1-r),
```

or, in centered Dirichlet coordinates,

```text
R(s)=(sqrt3/2)/(1-4^-s).
```

It is a positive geometric four-adic filter.

Applying the cofinal Jordan estimates to any positive geometrically delayed state gives

```text
P_state = Omega(X),
S_state = O(X log X),
Y_state = O(log X),
T_state = O(X log^4 X),
```

and therefore positive Jordan curvature with a quadratic moat.

Thus the terminal-state sign explicitly left open in the unitary-curvature ledger is closed cofinally. This is `L-34004`.

## 6. Compact innovation endpoint rows are soft

The one-step compact source is

```text
B_circ=(1-4^(1-s))/zeta(s),
1*b_circ=epsilon-4 delta_4.
```

Its first source current satisfies

```text
1*q_circ
=(epsilon-4 delta_4)*Lambda_circ.
```

The exponentially large four-adic generalized-prime coefficients cancel in this difference; the resulting prefix-current coefficients obey

```text
|c_circ(m)| << log(2m).
```

For a fixed endpoint child `r`,

```text
carry_(n,r)(q_circ)
=sum_(h=0)^(r-1)c_circ(n-h)-constant_r.
```

The bare compact source is adverse only at `r=1,2,3` and reflections. Hence every cofinal adverse endpoint current is `O(log n)` pointwise and belongs to polynomial block forcing.

This is `L-34005`.

## 7. Critical-scale reserve is a relative Jordan curvature

For one row define

```text
F_e(tau)=1+carry_e(J_(4,tau)).
```

Then

```text
R_e = -d_tau^2 log F_e(0).
```

Define the scale-four relative partition

```text
H_e(tau)=F_(4e)(tau)/F_e(4 tau).
```

Then

```text
(log H_e)'(0)=P_(4e)-4P_e=:E_e,
```

and

```text
-d_tau^2 log H_e(0)
 =R_(4e)-16R_e
 =Delta_4 R(e).
```

Moreover

```text
Delta_4 R
 =E(8P+E)+16S-S^+
 >=8PE>=0.
```

This is `L-34006`.

Thus the newly created reserve at one radix-four step is an exact relative log-curvature, not merely a difference of two large positive numbers.

## 8. The sole preferred closing theorem

Let

```text
I_e=Q_4^phys(4n,4j)-Q_4^phys(n,j).
```

PR #342 identifies this as the current of the compact two-tap source, up to one explicit delayed bare-source gauge. The scale-matched target is

```text
|I_e|^2 <= C Delta_4 R(e)
```

outside a fixed finite base, or an equivalent independent-frequency block inequality.

Finite floating reconnaissance is encouraging but is not proof and is not part of any theorem here.

The most promising proof mechanism exposed by `L-34006` is now precise:

```text
construct a two-parameter source-bound positive/reflected Jordan family
whose first score is E_e,
whose second score is I_e,
and whose 2x2 negative log-Hessian is PSD.
```

The `(1,1)` Hessian entry is already exactly `Delta_4 R`. Schur/Cramér--Rao would then prove the required current domination. Scalar positivity of `H_e` alone is insufficient.

A second possible mechanism is the source-complete reflected Selberg identity for the compact source. `L-34005` removes all adverse endpoint rows, so only the balanced interior component remains RH-sensitive.

## 9. Exact status

```text
entire physical/carry Jordan placement               CLOSED / proposed exact
true-current typing                                   CLOSED / proposed exact
inverse-source curvature double-spend                 CLOSED algebraically
PNT current/full-reserve ratio                        CLOSED unconditionally
continuous augmented reserve                          CLOSED cofinally
terminal all-pass state curvature sign                CLOSED cofinally
compact adverse endpoint current                      CLOSED / polylog local
radix-four reserve increment as relative curvature    CLOSED exactly
balanced compact current <= new reserve increment     OPEN / RH-BEARING
renormalized coefficient-one recurrence               OPEN
Riemann Hypothesis                                    UNPROVED
```

## Review order

1. `L-34001`
2. `L-34002`
3. `L-34003`
4. `L-34004`
5. `L-34005`
6. `L-34006`
7. parent PR #342 `L-34002/L-34003/L-34004`
8. PR #325 `L-32405/L-32406/L-32412/L-32414`
9. PR #337 `L-32710/L-32711`
10. PR #241 independent-frequency block identity

This branch does not request merge as an RH proof.
