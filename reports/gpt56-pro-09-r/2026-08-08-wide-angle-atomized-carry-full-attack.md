# Wide-angle RH attack: atomized carry frame, Selberg–Kummer reserve, and endpoint trees

Agent: `gpt56-pro-09-r`  
Date: 2026-08-08  
Branch: `agent/gpt56-pro-09-r/281-carry-window-selberg-kummer`  
Status: **SERIOUS FULL CONDITIONAL PROPOSAL; RH UNPROVED**

## Executive result

The repository's strongest live elementary/reflected routes can be reorganized
around one two-variable carry object

\[
 C(x,\theta)
 =\lfloor x\rfloor-\lfloor\theta x\rfloor-
  \lfloor(1-\theta)x\rfloor.
\]

The important operation is to retain `theta` until after the physical square.
Doing so gives all of the following at once:

1. an exact symmetric Nyman–Beurling generator;
2. a vector-valued pole detector whose frame norm is nonzero at every zeta zero;
3. an exact equality between the physical normal energy and a finite carry Gram;
4. the factor-four opposite-parity carry wavelet of PR #269;
5. a pointwise Selberg–Kummer reserve on every interior split;
6. an exact balanced-tree representation of the only zero-reserve endpoint
   contacts.

The previous open physical-to-carry transference is removed.  The new remaining
theorem is a signed endpoint-tree recurrence, `ETSR`.

## 1. Repository-wide scope corrections retained

The attack accepts all exact negative results already in the repository:

```text
one-frequency physical-block identification           false
absolute endpoint-face count independent of order      false
bounded-rank Möbius contagion                           false
cellwise alternating derivatives => Hankel positivity  false
monotone positive-part carry cover                      false
polylog finite-prefix inversion                         false
```

This pass adds exact fixed-order Abel counterexamples through order eight.
Higher fixed cumulative order is not a soft substitute for source-specific
cancellation.

## 2. Nyman and carry are the same physical window

For `0<y<=1`,

\[
 C(1/y,\theta)=\rho_\theta(y)+\rho_{1-\theta}(y).
\]

After the unitary logarithmic map

\[
 f(y)\mapsto e^{-u/2}f(e^{-u}),
\]

the symmetric Nyman generator is the atomized carry window.  Its transform is

\[
 \zeta(s)\frac{1-\theta^s-(1-\theta)^s}{s}.
\]

The carry programme and the Nyman–Beurling programme are therefore not merely
analogous.  They are the same filter bank in different coordinates.

## 3. Pole-preserving balanced filter bank

Apply the complete opposite-parity inverse-zeta source and then the ordinary
prime measure.  The resulting field has transform

\[
 -E(s)N_\theta(s)\frac{\zeta'}\zeta(s).
\]

For any fixed balanced interval `[eta,1-eta]`,

\[
 \int_\eta^{1-\eta}|N_\theta(\rho)|^2d\theta>0
\]

at every nontrivial zeta zero.  Thus the atomized local energy is
RH-equivalent.

At a finite physical scale `X`, the same field is exactly

\[
 X^{-1/2}\sum_m\Lambda(m)
 [g_m(X)-g_m(\theta X)-g_m((1-\theta)X)],
\]

where

\[
 g_m=\mathbf1_{[m,2m)}-rac12\mathbf1_{[2m,4m)}.
\]

Squaring and integrating in `theta` gives an explicit finite positive carry
Gram.  No Fourier approximation, numerical source map, or abstract
transference theorem remains.

## 4. Exact Selberg–Kummer reserve

For every binomial row,

\[
 \left(\sum_q\Lambda(q)\chi_{n,q}(j)\right)^2
 \ge
 \sum_d[\Lambda(d)\log d+(\Lambda*\Lambda)(d)]
        \chi_{n,d}(j).
\]

The difference has an explicit positive covariance decomposition.  It vanishes
only at

\[
 j=0,1,n-1,n.
\]

On a fixed balanced cone, the Selberg forcing consumes only

\[
 O\left(\frac{\log^2n}{n}\right)
\]

of the Kummer square.

This establishes a sharp structural separation:

```text
interior reflected arithmetic: unconditionally positive reserve;
endpoint-neighbor arithmetic:  complete zero-reserve RH channel.
```

## 5. Endpoint contacts are balanced-tree commutators

Let `T_n` be a full central fragmentation tree.  Then

\[
 \partial T_n=e_n-ne_1,
 \qquad
 L_q(T_n)=\lfloor n/q\rfloor,
 \qquad
 \mathcal H(T_n)=\log(n!).
\]

Therefore

\[
 [n,1]\equiv T_n-T_{n-1}
\]

with exact preservation of every carry column and entropy.  An endpoint family
satisfies the Abel identity

\[
 \sum_{n=2}^{N}c_n[n,1]
 \equiv
 c_NT_N+
 \sum_{n=2}^{N-1}(c_n-c_{n+1})T_n.
\]

Every proper tree descendant is at half scale or lower.  The broad balanced
Type-II obstruction has become one signed first-variation ledger plus one
outer tree.

## 6. Proposed completion

The remaining theorem `ETSR` must assemble the actual reflected source before
estimating it and prove

\[
 \mathscr E_\eta(J)+\mathscr Q_\eta(J)
 \le C(1+J)^A+
 \sum_\nu\theta_\nu\mathscr E_\eta(J_\nu),
\]

with

\[
 \mathscr Q_\eta\ge0,
 \qquad J_\nu\le J-\delta,
 \qquad \sum\theta_\nu\le1.
\]

A coefficient-one fixed-delay recurrence is enough for polynomial energy.  The
vector-valued pole criterion then gives RH.

## 7. Why this is a full-problem attack

The proposal does not attempt to prove another arbitrary finite matrix
positive.  Its target energy contains every nontrivial zeta zero with a
strictly positive carry-frame residue norm.  It also removes the growing packet
and physical-transference mismatches that blocked the reflected route.

The remaining endpoint recurrence is still RH-bearing.  It is not represented
as established.  Its advantage is that every positive interior term and every
geometric endpoint operation are now explicit.

## Exact status

```text
Nyman/carry identification                  proposed complete
atomized pole frame                         proposed complete
physical energy = finite carry Gram         proposed complete
ordinary Selberg-Kummer reserve             proposed complete
endpoint balanced-tree commutator           proposed complete
fixed Abel orders 1--8                      refuted at listed scopes
ETSR                                        open / RH-bearing
ETSR -> polynomial energy -> RH             complete conditional
Riemann Hypothesis                          unproved
```

## Recommended adversarial order

1. check the logarithmic half-shifts and the finite dyadic gauge;
2. replay the Nyman/carry identity;
3. verify the vector-valued residue frame;
4. reconstruct the exact finite carry Gram;
5. inspect the Selberg reserve decomposition term by term;
6. verify endpoint equality and tree replacement;
7. attack the source-specific first-variation ledger required by `ETSR`.
