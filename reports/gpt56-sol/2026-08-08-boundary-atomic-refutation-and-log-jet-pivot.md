# Boundary-source reconstruction, exact refutation, and cancellation-preserving pivot

**Agent:** `gpt56-sol`  
**Date:** 2026-08-08  
**Parent:** PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
**Status:** **load-bearing refutation plus new exact finite operator reserve**  
**RH:** **unproved**

## Result

I did not leave PR #304's source-manifest reconstruction to a reviewer.  I
reconstructed the actual stopped-power cutoff source and found that the proposed
polylogarithmic atomic norm is false.

For

```text
p_N(n)=n^(-1/2) 1_(n<=N),
```

the exact cutoff tail on `N/3<q<=N/2` satisfies

```text
sqrt(q) Q_N p(q) < -1/20.
```

At the output endpoint `M=floor((N+1)/2)`, these coordinates lie above `M/2`,
so multiples-Möbius inversion is a singleton.  Hence the actual divisor source
obeys

```text
sum_(m<=M) sqrt(m)|sigma_N(m)| >= N/240.
```

This rejects the central estimate of `L-30403` and the full proof claim on PR
#304.  Positive Peano coefficients on an internal quotient label are not a
positive divisor source.

## Exact cancellation-preserving replacement

The signed central cascade itself remains a complete finite producer.  New
`L-30501` proves exactly

```text
prime ramp
 =log(2) sum_(stage a) sum_n r_a(n)
  +sum_a sum_(odd n) r_a(n) log(n/(n+1)).
```

Thus a source-blind capacity norm is sufficient but not necessary.  The correct
object is the complete signed residual profile before Möbius inversion.

For

```text
r(q)=q^(-1/2)F(log(X/q)),
```

new `L-30502` derives the exact finite log-coordinate operator, retaining the
`2kq-1` shift and zero extension.  A residual-plus-transport decomposition and
rational square certificate give

```text
||A_z F||_infinity
 <=(9/10)(||F||_infinity+8||F'||_infinity),
0<=z<=1/2.
```

The certified upper constant is

```text
157933/176000 < 9/10.
```

This is the first strict reserve on the **complete finite endpoint profile**;
it does not split the endpoint into macroscopic atomic sources.

## Corrected full-problem route

The new proposed theorem `CPLJR` is an explicit weighted finite log-jet renewal
combining:

```text
9/10 complete current-value reserve;
6/7 faster-power Dirichlet-Taylor reserve;
exact derivative coupling;
causal endpoint atoms;
fixed low-coordinate base table.
```

A completed transition would dominate the exact signed objective above and give
the sharp prime ramp, square-screw envelope, Landau pole exclusion, and RH.

`CPLJR` is not proved on this branch.  The work completed here is the exact
rejection of the false atomic route and the exact zeroth row of its
cancellation-preserving replacement.

## Exact artifacts

```text
R-30501  terminal atomic boundary norm is macroscopic
L-30501  exact central entropy Abel identity
L-30502  exact finite shifted log transport reserve
T-30501  corrected cancellation-preserving full-problem proposal
X-30501  standard-library rational certificates
```

Proof-object digests:

```text
boundary atomic firewall
32c1317529f8559b845fe3016d50424e9d213c9d7f6de3ea8be0672253eb3016

shifted log transport reserve
44e56e7893cf076e76efef289a4a890dd00bbf98388a709827a5519e86906cc1
```

## Honest boundary

```text
PR #304 full proof claim                     rejected
macroscopic atomic source theorem            proved
exact signed objective identity              proved/proposed complete
complete finite current-value reserve 9/10   proved/proposed complete
all-jet cancellation-preserving renewal      open
Riemann Hypothesis                           unproved
```
