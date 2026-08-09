# Q4 compact/parity continuation — full three-jet routing and cross-free odd relative state

Status: **new exact state reductions; final coefficient-one dissipative recurrence open; RH unproved**

## 1. Full three-jet routing — L-34405

The exact compact-source reconstruction

```text
B_circ=W_+ B_+ + W_- B_-
```

now lifts through the complete zeroth/first/second source jets.

The first gauge is

```text
G1=(log2) z R_H(z) B0.
```

Differentiating once more gives

```text
t_circ
 =W_+ t_+ + W_- t_-
  + dot(W_+) q_+ + dot(W_-) q_-
  +(log2) z R_H q0
  -(log2)^2 z(R_H+zR_H')B0.
```

Every term outside the same finite parity second-jet synthesis has an explicit factor `z`, hence is delayed by at least one dyadic block.

The conversion from the own compact derivatives to the actual scale-four Q4 innovation jets adds only the already-known scale-four delayed `b4,q4` gauges.

Thus differentiation through curvature order creates **no new zero-delay arithmetic source species**.

## 2. Cross-free odd relative state — L-34406

For the odd Möbius source

```text
B_odd=prod_(p odd)(1-p^-s),
```

one has

```text
1*b_odd=sum_(r>=0) delta_(2^r).
```

Hence its bare carry charge is the number of binary carry levels.

Aligned scale-four dilation shifts every nontrivial binary level by exactly two and creates no new level-one/two carry. Therefore

```text
Y_odd(4n,4j)=Y_odd(n,j)
```

exactly.

For the relative source leg

```text
(epsilon-delta_4)*K_(odd,tau)
```

the zeroth coordinate therefore vanishes.  Combining with the relative odd Jordan partition gives one two-component path whose curvature is exactly

```text
A_odd^rel
 =Delta_4 R_odd + |I_odd|^2.
```

There is no `Y*T` cross term at all.

PR #346 `L-34404` already proves

```text
Delta_4 R_odd = Theta_eta(n log n)
```

on every fixed balanced cone.  Thus this is the cleanest scale-matched source-complete positive relative state presently resident.

## 3. Matching parity state compression pushed separately

PR #329 now also contains `L-32315`, proving

```text
A_pair = curvature of one four-component Jordan path V_e(tau).
```

Both parity channels factor over one common odd Jordan carrier:

```text
J_+/- = J_odd * p(+/-z)/p(+/-2^tau z),
K_+/- = K_odd * p(+/-z)^2/p(+/-2^tau z).
```

Therefore the remaining recurrence is finite two-adic state-space algebra coupled to a single odd-prime carrier, not a growing arithmetic packet family.

## 4. Live composition after this pass

The Q4/parity graph now reads

```text
compact Q4 innovation
 -> exact parity jet frame                     L-34402
 -> one matching A_pair curvature              PR #329 L-32306
 -> A_pair = curvature of a four-state path    PR #329 L-32315
 -> common odd carrier + finite 2-adic dressing L-32315
 -> no new source through second derivative    L-34405
 -> cross-free scale-matched odd relative state L-34406
 -> coefficient-one delayed dissipative law    OPEN
 -> polynomial/subexponential block energy     conditional
 -> RH                                         conditional
```

## 5. Scope firewalls retained

- positivity of a curvature is a lower statement and does not upper-bound the contained current square;
- the naive scalar two-parameter Fisher/Schur family has an indefinite Hessian on PR #345;
- the raw parity radix-four reserve is the wrong scale because explicit dyadic inverse modes have large signed increments;
- the odd-prime reserve increment is the correct deterministic `n log n` scale;
- first-derivative synthesis alone does not prove a second-order curvature recurrence.

## Exact boundary

```text
compact current parity jet frame                 complete exact / review
matching local no-double-spend A_pair             complete cofinal / review
full compact three-jet routing                    complete exact
odd bare-charge radix-four invariance              complete exact
cross-free odd relative curvature                 complete exact
odd deterministic critical increment              imported complete cofinal
four-state/common-odd state compression            pushed on PR #329
coefficient-one delayed curvature recurrence       OPEN / RH-bearing
Riemann Hypothesis                                 UNPROVED
```
