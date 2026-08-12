# Compact dyadic pole-bridge continuation

## Freeze

```text
main:        b837c12199dd407116f604ce6c938039d1a76da4
parent PR:   #414
parent head: 0fe80e32781e109aee1882f2a069dbb2e3787f7e
branch:      research/gpt56-pro/91530-compact-dyadic-bridge
```

## Result

The global pole-zero cancellation has been reorganized into one exact compact
source factor.

Let

```text
s0=1-omega,
s1=1+omega,
F_L(z)=(1-exp(-z log 2))/z.
```

The dyadic factor and the rational gamma endpoint satisfy

```text
[(1-2^(-(s-s0)))/(1-2^(-(s-s1)))]
*[(s-s1)/(s-s0)]
 =F_L(s-s0)/F_L(s-s1).
```

Consequently the horizontal completed quotient factors as

```text
paired eta ratio
x finite-interval Laplace ratio
x residual beta/gamma factor.
```

The free pole source `exp(s0 t) 1_(t>0)` is truncated exactly to

```text
exp(s0 t) 1_(0<t<log 2).
```

After Hardy weighting it is square integrable for the complete hard range.

## Full-carrier advance

The finite interval supports a canonical exponential-tilt unitary:

```text
U_(omega,q) f(t)
 =sqrt(F_L(q)/F_L(q+2omega)) exp(-omega t) f(t).
```

It commutes with every carrier modulation and physical delay. Thus the
pole/dyadic bridge is closed not only at one vector but at full polarization.

## Surviving obstruction

The paired eta source lives on an unbounded union of log intervals. Its hard
change of exponent requires multiplication by `exp(omega y)`, whose truncated
operator norm grows like `(2N)^omega`. The compact bridge does not remove this
tail-sector obstruction.

The reduced theorem `EBOC_omega` must entangle that eta growth with the
remaining beta/gamma source, or work on the one-node graph domain, before
norms are taken.

## Exact state

```text
dyadic zero x gamma pole                     COMPACT LAPLACE BRIDGE
completed quotient factorization             EXACT
bridge carrier/delay covariance              EXACT
free pole non-Hilbert tail                    REMOVED
paired eta tail same-space map                UNBOUNDED
eta-tail–beta/gamma completion                OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
