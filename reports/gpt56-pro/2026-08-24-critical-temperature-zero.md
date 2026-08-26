# Critical-temperature zero of the geometric midpoint square

## Result

The geometric completion family

\[
E_t(z)=\prod_\ell(1-p_\ell^{-z})(1+p_\ell^{-z})^t
\]

provides one real interpolation from the native duplicate-67 source to its
squared completion.  Squaring the source changes the Selberg--Delange exponent
to `2t-2`.

For every fixed strict temperature,

```text
0<t<1/2:  the fixed outer observation is eventually negative;
1/2<t<1:  the fixed outer observation is eventually positive.
```

At `t=1/2`, the deterministic real-branch coefficient vanishes and the source
is exactly the geometric midpoint square

```text
eta*eta = beta*beta_square.
```

The finite-horizon sign-transition zero is unique in an exponentially thin
Vinogradov--Korobov layer around one half.  Its positive weighted displacement
is quantitatively equivalent to the midpoint-square negative mass.  Through
the already-proved positive square-lattice inverse, this yields an exact
RH-equivalent criterion.

## Exact frontier

```text
CTZD102897:
  integral sqrt(X)/log^2(X) * (vartheta(X)-1/2)_+ dX/X = X^o(1).
```

The criterion is not proved.  The theorem converts the endpoint arithmetic
sign into the orientation of one exponentially localized real zero; it does
not infer that orientation from the strict-temperature signs.

```text
phase transition                         proved
critical midpoint identification         proved exact
transition-zero localization             proved
weighted drift / adverse mass            proved equivalent
CTZD102897                               open / RH-equivalent
Riemann Hypothesis                       unproved
```
