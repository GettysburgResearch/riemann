# X-91553 — exact component entropy and fixed-67 score domination

This standard-library directed replay certifies the finite part of `L-91553`:

- `E(67)-(5 sqrt(67)-3)>3`;
- every logarithmic-cell derivative of
  `E(Y)-E(Y/67)-5(sqrt(Y)-sqrt(Y/67))`
  is positive for `67<=Y<536`;
- the smallest directed derivative lower endpoint is greater than `22`.

Above `536`, `L-91553` uses the elementary subset bound from integers in
`(Y/4,Y]`.

All transcendental signs use exact `Fraction` arithmetic and directed rational
enclosures of square roots and logarithms. The replay does not certify the
native root-amplitude normalization or RH.

```bash
python3 verify.py
```
