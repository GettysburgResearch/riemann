# X-91559 — nested component identity embedding

This replay supports `L-91559` and the exact counterexample `R-91558`.

It performs three separated checks.

## 1. Formal component response

Treat every logarithmic atom `h_Y(m)` as an independent formal symbol.  For
all integer support endpoints through `80`, the script reconstructs

```text
Q_Y(n)=(n+1) Delta^2[S_Y(n)/(n-1)]
```

using exact `Fraction` coefficients and verifies at every physical column

```text
sum_n Q_Y(n) beta_(n,q)
  = sum_(kq<=Y) h_Y(kq),

sum_n Q_Y(n)[beta_(n,q)-2 beta_(n,4q)]
  = sum_(kq<=Y)h_Y(kq)-2 sum_(4kq<=Y)h_Y(4kq).
```

This gives `6,320` exact formal-coefficient checks.

## 2. Affine separation

The script checks the rational carry data in the canonical witness

```text
child endpoint 3;
child row Q_3 supported at n=2;
fixed affine scale 67;
parent endpoint 201;
unmatched physical detail column 200.
```

Together with the elementary logarithm and square-root bounds written in
`R-91558`, these data prove strict parent-capacity overdraw.

## 3. Nested monotonicity windows

The script replays the positive index window in

```text
D'(Z)=Z^-1 sum_(Z/4<k<=Z) k^-1/2
```

through `Z=500`.  The analytic formula itself is proved in `L-91559`.

```bash
python3 verify.py
```

The replay does not certify the imported Hall entry, the row-budget
normalization, live-parent compatibility, or RH.
