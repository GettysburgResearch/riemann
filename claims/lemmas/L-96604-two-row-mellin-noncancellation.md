# L-96604 — Two fixed positive rows retain every off-line zeta pole

For fixed `j`,

```text
int_1^infinity c_X(j) X^(-s-1) dX
 = C_j/s^2 + P_j(s+1/2)/(s^2 zeta(s+1/2)).
```

For rows two and three,

```text
P_2(z)=2*2^(-z)-1-3^(-z),
3P_3(z)=5*3^(-z)-2^(-z)-1-3*4^(-z).
```

If both vanish, with `a=2^(-z)` and `b=3^(-z)`, then `b=2a-1` and

```text
-3(a-1)(a-2)=0.
```

This is impossible for `Re z>0`, since `|a|<1`. Thus every hypothetical zero with `Re rho>1/2` creates a pole in at least one nonnegative row transform.
