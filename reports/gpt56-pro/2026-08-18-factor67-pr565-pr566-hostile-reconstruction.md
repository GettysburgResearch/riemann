# Audit findings and repairs

## Executive determination

PR #565 and PR #566 contain substantial correct infrastructure, but neither complete proposal survives source-faithful reconstruction. Both ultimately substitute a scalar statement about one packet for a theorem about a different completed rough-history source.

The audit repaired the finite `P_61` arithmetic from the false constant `1/40` to the true certified constant `1/42`. That repair is quantitatively strong enough for a factor-67 contraction, but it does not manufacture the missing history/source interface.

## PR #565

### What survives

The following components are exact:

- the `5:3` scalar dictionary;
- the definition of the finite `P_61` signed scalar `F(x)` and unsigned mass `M(x)`;
- monotonicity of `M`;
- the formal coefficient identities
  `s_i = product_{h<=i}(1-r_h)`, `lambda_i=r_i s_{i-1}`, `alpha_i=r_i lambda_i`;
- the bound `sum alpha_i < 1/sqrt(67) < 1/8`;
- the rational contraction arithmetic after replacing `1/40` by `1/42`;
- the scalar Mellin-Landau endpoint, conditional on eventual scalar nonnegativity.

### Finding 565-A: the `1/40` bias is false

At `x=184`, the reconstructed values are

```text
F(184) = 10.69357964877382995080531550498546444...
M(184) = 445.85760354260283631557807730110764267...
F/M    = 0.02398429355876630...
```

Therefore

```text
40 F(184) - M(184) = -18.11441759164963828... < 0,
F(184) - M(184)/40 = -0.45286043979124095... < 0.
```

This is a large, stable countercertificate, not a rounding ambiguity.

### Repair 565-A: corrected `1/42` theorem

A 256-bit directed replay proves

```text
0 <= F(x) <= M(x)                 for 1 <= x < 67,
M(x)/42 <= F(x) <= M(x)/8         for x >= 67.
```

The finite proof checks every real activation cell through `10^6`. The tail uses the Euler-ramp expansion

```text
S(Y) = 4 sqrt(Y) + zeta(1/2) log Y + zeta'(1/2) + R(Y),
|R(Y)| < 5 Y^(-3/2),
```

and the induced scalar asymptotic. The replay in this packet repairs the rational argument helpers so division is enclosed outward before logarithm/square root, and evaluates coverage and tail penalties entirely by interval operations.

The decisive directed margins are:

```text
min_{x>=67, x<=1e6} (42F-M)  > 3.272741706...
min_{x>=67, x<=1e6} (M-8F)   > 135.51663...
tail lower margin             > 119.87156...
tail upper margin             > 40007.499...
```

### Finding 565-B: the current has the wrong source type

A genuine positive restriction subtracts a placed child in the same source channel. For a one-atom even source and `r=p^(-1/2)`:

```text
same-channel restriction: (1,0) - r(1,0) = (1-r,0) >= 0;
PR #565 swapped version:   (1,0) - r(0,1) = (1,-r),
```

and the latter is not a positive paired source. Parity swap belongs to the signed observation of a placed child; it cannot be inserted into a positive source subtraction without an additional theorem.

### Finding 565-C: the all-history induction fails at depth one

With one rough prime, `s=1-r`, `lambda=r`, `alpha=r^2`. If `F(x)` and `F(y)` are the finite-`P_61` scalar values, PR #565's swapped current gives

```text
s F(x) + lambda [F(x)+rF(y)] = F(x)+r^2 F(y).
```

Subtracting the recursive child `alpha F(y)` returns exactly `F(x)`. The native one-prime Euler extension is

```text
F(x) - r F(y).
```

The difference is the nonzero term `rF(y)`. Thus the recursion is a tautological split of the base packet, not the rough Euler history expansion. This defect persists even after the bias constant is repaired.

### Finding 565-D: base cases and first ownership are not reached

Because the depth-one coefficient is already wrong, low-child recombination does not establish native base cases. An owner label is not an exhaustive atomwise partition. No all-history induction exists until the source map, channel action, and exact coefficient of every rough history are simultaneously proved.

### Quantitative salvage

The corrected bias would support the formal lower margin

```text
(1 - 8/sqrt(67))/42 > 1/2730.
```

This is a useful conditional margin, but it applies only after a correct source-faithful recursion is supplied.

## PR #566

### What survives

The following components are exact or valid in their declared scope:

- the `5:3` scalar and Mellin numerator;
- the odd-history obstruction;
- the factor-67 coefficient economy and finite depth;
- the imported canonical Target-Lorenz terminal theorem;
- the positive nilpotent operator lemma;
- the algebraic identity `(I+T)^-1=(I-T)(I-T^2)^-1`.

### Finding 566-A: L-96651 proves the wrong inequality

The theorem states

```text
G_v = H_v direct-sum R_v,
g_v = scalar(H_v),
alpha G_w injects into R_{v->w}.
```

The injection can imply

```text
scalar(R_{v->w}) >= alpha scalar(G_w).
```

It says nothing about `scalar(H_v)`, which is disjoint from the reserve. Hence it does not imply

```text
g_v >= sum_w alpha scalar(G_w) = (Tg)_v.
```

An exact one-parent countermodel is

```text
scalar(H)=1/2,
scalar(R)=1,
alpha scalar(G_child)=1.
```

All stated decomposition and injection clauses hold, but `g=1/2 < 1=Tg`.

### Finding 566-B: mass and barycenter are not Hall/Lorenz capacity

Let even supply be

```text
E = (1/2) delta_0 + (1/2) delta_2
```

and odd demand be

```text
O = delta_1.
```

They have equal total mass and equal first moment. Nevertheless a no-upward coupling `e <= o` is impossible because at threshold `1` the odd prefix demand is `1` while available even prefix supply is only `1/2`.

A reserve-preserving Hall theorem must preserve every prefix capacity inequality at every activation threshold. Target mass and barycenter alone are insufficient.

### Finding 566-C: the imported Target-Lorenz theorem is canonical only

For

```text
T(z)=4 sqrt(z)-3,
K_T(d;p,y)=d^(-1/2)[T(py/d)-p^(-1/2) 1_{d<=y} T(y/d)],
```

the complete `P_61` theorem proves a common-source, no-upward coupling from the base even channel to the base odd demand. Its compact and tail certificates cover all real endpoints in that orientation.

At `(p,y)=(71,13)` the canonical target difference satisfies

```text
E_T(71,13)-O_T(71,13) > 17.
```

After the legitimate odd history `(67)`, the channels swap, so the required target feasibility inequality reverses. The theorem cannot be applied leafwise to an odd-history state.

### Finding 566-D: the operator lemma is conditional, not a producer

For positive nilpotent `T`, if a current vector `g` satisfies `g>=Tg`, then

```text
(I+T)^(-1)g = (I-T)(I-T^2)^(-1)g >= 0.
```

This is exact. The failure is upstream: PR #566 never proves `g>=Tg` for the same `g` that appears in the parity recursion.

### Repair template for #566

A valid repair must simultaneously prove:

1. `G_v=H_v direct-sum reserves` in an explicit positive source category;
2. a residual Hall flow on `H_v` satisfying every prefix constraint;
3. disjoint activation/channel/coordinate-preserving child injections into reserves;
4. an atomwise one-use identity `(I+T)U=g_total` with no reserve counted once in `g_total` and again as an independent child;
5. `g_total>=Tg_total` in that same coordinate system;
6. finite/nilpotent state graph and root identification.

Redefining `g` as the total parent scalar can make domination plausible, but without item 4 it double-counts the reserve and changes the source expansion.

## Exact finite scalar Lorenz theorem

For one fixed, fully expanded endpoint, let even atom `i` have capacity `a_i`, target `t_i>0`, and scalar `r_i`. Let the odd demands be `(T_O,R_O)`. Define

```text
Phi_X(T) = max sum_i r_i u_i
subject to 0<=u_i<=a_i and sum_i t_i u_i=T.
```

Then scalar common-source feasibility is equivalent to

```text
T_O <= T_E,
R_O <= Phi_X(T_O).
```

Ordering by decreasing `theta_i=r_i/t_i` gives the explicit fractional-knapsack Lorenz formula, and

```text
Phi_X(T)=min_lambda [lambda T + sum_i a_i(r_i-lambda t_i)_+].
```

This finite theorem is exact. The open uniform assertion for every real endpoint and both one-sided activation limits is `CPSL67`.

## Final boundary

The repaired arithmetic is not the bottleneck. The exact missing theorem is:

```text
completed rough-history ledger
+ cumulative parity
+ exact first ownership
+ common target/scalar source selection
+ residual Hall prefixes
+ one-use parity recursion
=> global scalar nonnegativity.
```

Until this is proved, the Mellin-Landau consumer remains conditional and RH remains unproved.
