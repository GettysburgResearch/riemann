# Extra-high redo — root source, two-contact physical field, and asymmetric reflection

Date: 2026-08-08  
Agent: `gpt56-sol`  
Status: **RESEARCH PASS — NEW EXACT THEOREMS; UNCONDITIONAL RH PROOF NOT OBTAINED**

## 1. Why this pass exists

The previous two user-facing passes were too quick relative to the state of the repository.

The first compressed a deep PR #304 audit into a high-level zero-safe-source story. The second opened PR #319 with only one research report and named `ZSST` as the remaining theorem. That was not commensurate with the requested “rock the boat” pass: it renamed the obstruction without first proving where the obstruction sits in the exact finite carry complex.

This redo starts from the live repository, including PRs #316--#323, and reconstructs the proof-facing source before proposing another completion.

## 2. Corrections to the previous two passes

### PR #319 is not a full proof packet

PR #319 contains a useful strategic observation but only one report. Its `ZSST` theorem is open. It should not be read as an unconditional RH proposal ready for final review.

New `L-32401` proves something stronger and more precise: the dyadic two-contact source is **exactly the root divergence** of every finite carry realization. Therefore any claimed signed-debt theorem must still consume that root coordinate; it cannot disappear through Pascal cycles or a different atomic norm.

### Radix five is not a harmless finite automaton

The live PR #323 independently identifies the missing arithmetic content of PR #322: the nonzero residue classes modulo five decompose into the principal zeta channel and three nonprincipal Dirichlet-L channels. A source-complete norm contraction of that state is at least a simultaneous mod-five GRH problem.

Thus the preferred self-similar radix is again two, whose unit group has no nonprincipal character.

## 3. New exact theorem: the RH scalar is the root node

Let

```text
b2=(epsilon-delta_2)*mu.
```

Then

```text
1*b2=epsilon-delta_2,
```

so its floor potential is one at node one and zero at every node `n>=2`.

Consequently

```text
sum_q b2(q) chi_(n,j)(q)
 =-1_(j=1)-1_(j=n-1).
```

For every exact flow with carry target `w` and node divergence `r`,

```text
sum_q b2(q) w(q)=r(1).
```

For the critical target this is exactly

```text
R(X)-2^(-1/2)R(X/2),
R(X)=sum_(n<=X)mu(n)n^(-1/2)log(X/n).
```

The Mellin transform is

```text
[1-2^(-z-1/2)]/[z^2 zeta(z+1/2)],
```

and the numerator is zero-free in `Re z>0`.

Moreover the negative of the root indicator, scaled by an explicit constant `c_eta`, is an admissible Cycle-Debt dual potential. Hence

```text
CycleDebt(X) >= c_eta [r_X(1)]_+.
```

This is a repository-wide identification: fixed-ratio Möbius, bottom charge, and Cycle Debt all contain the same principal root mode.

## 4. New exact theorem: `zeta^M` has a strict row reserve

For one binomial row write

```text
F = log binom(n,j),
A = carry(Lambda log),
B = carry(Lambda*Lambda),
Q = F^2-A-B >=0.
```

For `zeta^M`, generalized primes are `M Lambda` and the forcing is

```text
M Lambda log + M^2 Lambda*Lambda.
```

The exact row defect is

```text
F_M^2-S_M
 =M^2 Q+M(M-1)A.
```

For `M>1`, `A>0` on every nontrivial split. Thus the generalized row reserve is strict even on the endpoint neighbors where the ordinary theorem is an equality.

This looked like a possible closure of the root channel.

## 5. Exact firewall: standard reflection erases that gain

Powering the product and both reflected factors by the same `M` gives

```text
C_(x,M)-C_(+,M)-C_(-,M)
 =2M^2 Lambda_+*Lambda_-.
```

After normalization this is exactly the ordinary reflected identity. The strict `M(M-1)A` row term is linear and cancels.

Therefore uniform power lifting does not close RH by itself.

## 6. New algebraic breakthrough: asymmetric power reflection

Do **not** power the product. Keep

```text
A_x=A_+ A_-
```

at power one, but subtract the two individual `M`-power identities normalized by `M^2`. Exact coefficient algebra gives

```text
C[A_+A_-]
 -M^-2 C[A_+^M]
 -M^-2 C[A_-^M]
 =2 Lambda_+*Lambda_-
  +(1-1/M)(Lambda_++Lambda_-)log.
```

The analytic self-squares cancel while a linear Selberg term survives.

At zero twist the corresponding carry forcing is

```text
B+(1-1/M)A,
```

and the ordinary Kummer square has the **strict** reserve

```text
F^2-[B+(1-1/M)A]
 =Q+A/M >0
```

on every nontrivial row, including the root/two-contact endpoint rows.

This is the first reflected polarization found in this pass which preserves a strict endpoint-sensitive term after self-square cancellation.

The physical caveat is equally explicit: on a vertical line the surviving term is

```text
2(1-1/M) Re sum_n Lambda(n)log(n)n^(-sigma-it),
```

which is not pointwise positive. A completion must bind this linear term to the exact source before taking a norm.

## 7. Simpler positive-source physical field

The same two-contact inverse has

```text
A_2(s)=zeta(s)/(1-2^-s),
a_2(n)=v_2(n)+1>0,
Lambda_2(n)=Lambda(n)+log(2)1_(n=2^r)>=0.
```

Its real carry prefix is exactly

```text
G_2(x)=1_[1,2)(x).
```

Thus the continuous carry profile has a literal one-crossing source geometry:

```text
1<=x<2:  Z_2(x,theta)>=0,
x>=2:    Z_2(x,theta)<=0.
```

At `theta=1/2` it is the compact wavelet

```text
+1 on [1,2),
-2 on [2,4),
 0 otherwise.
```

The positive generalized-prime pole field is the Jensen defect of

```text
A_2(y)=psi_2(y)-psi_2(y/2).
```

Its endpoint packet closes completely: each source scale is the two-edge balanced-tree wavelet

```text
V_m=D_m-D_(2m)=-E_m,
```

and every nonnegative source superposition has the strict exact reserve

```text
Q_end
 =log^2(2) X0^2
  +2log(2) X1
  +log^2(2) X0 >0.
```

A two-color dyadic decomposition bounds the full physical endpoint step norm by this reserve with an absolute constant `4/log 2`.

So the endpoint source-binding problem is closed for the simplest root-sensitive positive-prime field.

## 8. What remains after the redo

The live problem is now considerably sharper:

```text
root / two-contact principal mode       exact and RH-bearing;
all transverse Pascal cycles            cannot remove it;
positive generalized-prime source       available;
continuous carry source geometry         one crossing;
endpoint physical source binding         closed exactly;
asymmetric reflected endpoint reserve    survives algebraically;
physical sign/Schur binding of the
  surviving linear term                  OPEN.
```

The proposed next theorem should therefore **not** be another atomic boundary norm, residue automaton, or unnamed signed-debt certificate.

The smallest honest target is:

> **Root-Polarized Asymmetric Selberg Certificate.** Insert the `L-32404` asymmetric identity into the independent-frequency block of PR #241, bind its surviving `Lambda log` source to the two-contact endpoint fibers of `L-32403`, and prove that the remaining interior Schur complement is nonnegative or routes with a fixed scale drop.

A proof must explicitly emit the two-frequency matrix and the source map. Until that is done, RH remains unproved.

## 9. Exact status

```text
previous PR319 as complete final packet       SUPERSEDED / TOO SHALLOW
five-adic scalar automaton as RH-only closure SCOPE-CORRECTED BY PR323
two-contact = root divergence                 PROPOSED COMPLETE
root Cycle-Debt dual lower bound               PROPOSED COMPLETE
uniform zeta-power strict row reserve          PROPOSED COMPLETE
standard powered reflection                    EXACT NO-GO
asymmetric power reflection                    PROPOSED COMPLETE EXACT ALGEBRA
two-contact positive-prime endpoint binding   PROPOSED COMPLETE
root-polarized physical Schur certificate      OPEN
Riemann Hypothesis                             UNPROVEN
```

This is the replacement for the previous two passes. The reviewer is asked only to verify the theorems actually supplied here; no missing proof is being assigned as an exercise.
