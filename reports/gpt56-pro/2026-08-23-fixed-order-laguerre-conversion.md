# Fixed-order Laguerre route from Xi''' to Xi''

## Objective

Produce a direct mathematical bridge from Conrey's known line-zero proportion
for `xi'''` to a line-zero proportion for `xi''`.

## Exact bridge

At a real zero of `Xi'''`, the sign of

```text
Xi'''^2-Xi'' Xi''''
```

is exactly the good/wrong-extremum orientation.  If the expression is
nonnegative at a proportion `q` of those zeros, then

```text
alpha_2 >= (2q-1) alpha_3.
```

Pointwise nonnegativity gives `alpha_2>=alpha_3>0.9873`.

## Kernel reduction

The expression is the Fourier transform of the explicit nonnegative kernel

```text
K_2(x)=integral y^2 [u^2 Phi(u)]_(u=x+y)
                     [u^2 Phi(u)]_(u=x-y) dy.
```

This proves positive definiteness of the Laguerre profile and every positive
Fourier-smoothed average.  The missing theorem is positive definiteness of
`K_2`, equivalently pointwise nonnegativity of the Laguerre profile.

## Boundary

The reduction is exact but the final kernel theorem is open.  It must not be
reported as an unconditional conversion of the Conrey row.

RH remains unproved.
