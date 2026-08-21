# L-104101: exact two-key root/excess absorption

Claim ID: `L-104101`  
Status: **PROVED EXACT**  
Created: 2026-08-21  
RH status: **unproved**

Let `(Omega,mu)` be a measure space.  Let `g` be real-valued, let `E,R>=0`,
and let `0<=theta<1`.  Define

```text
Q = |g|^2 + E.
```

Assume pointwise

```text
|g|^2 <= theta Q + R.
```

## Pointwise conclusion

Writing `delta=1-theta`,

```text
delta |g|^2 <= theta E+R <= E+R,
```

and therefore

```text
g_- <= |g|
    <= delta^(-1/2) sqrt(E+R)
    <= delta^(-1/2)(sqrt(E)+sqrt(R)).
```

## Proof

Substitute `Q=|g|^2+E` into the assumed return inequality and move
`theta|g|^2` to the left.  Since `theta<=1`, the first displayed inequality
follows.  Taking square roots and using `sqrt(a+b)<=sqrt(a)+sqrt(b)` proves the
last display.

## Dyadic consequence

For each integer `L`, suppose the hypotheses hold on

```text
B_L=[2^L,2^(L+1)]
```

with a block parameter `theta_L`, and suppose

```text
(1-theta_L)^(-1)=2^o(L),

integral_(B_L) [sqrt(E_L)+sqrt(R_L)] dX/X=2^o(L).
```

Then

```text
integral_(B_L) (g_L)_- dX/X=2^o(L).
```

Indeed the pointwise estimate multiplies the packing bound by
`(1-theta_L)^(-1/2)=2^o(L)`.

This is the one-dimensional Schur/Perron quotient of the matrix absorption in
PR #697.  It is also compatible with PR #704: a matched transfer may first be
used to define the source-faithful remainder `R`, after which this lemma
performs the scalar absorption.
