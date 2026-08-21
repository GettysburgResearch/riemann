# L-101501: adaptive finite-completion residual bound

Let `F` be one fixed real detector and let

```text
C_Z = I + R_Z
```

be any finite completion operator.

## Statement

At every point `X` where

```text
(C_Z F)(X) >= 0,
```

one has

```text
F(X)_- <= [(R_Z F)(X)]_+.
```

The parameter `Z` may be selected as a function of `X`.

## Proof

If `F(X)>=0`, the assertion is immediate. If `F(X)<0`, then

```text
0 <= F(X)+(R_ZF)(X),
```

so `(R_ZF)(X)>=-F(X)>0`, proving the bound.

## Scope firewall

This lemma estimates the negative part of the fixed detector `F`; it does not feed the endpoint-dependent completed observable `C_{Z(X)}F` into Mellin-Landau. Any conclusion therefore requires a separate bound for the positive residual on the right.
