# R-95500 — Common-divisor dispersion is the resonant Euler completion, not an independent average

Claim ID: `R-95500`  
Status: **EXACT MECHANISM FIREWALL**  
Created: 2026-08-18  
Depends on: `L-95500`

A natural SACF attack treats the sign-free common divisor `d` as an averaging
or modulus variable and hopes to gain cancellation before confronting the two
Möbius signs.

At one prime, however, the source-owned `d` state contributes exactly

\[
p^{-(s_1+s_2)}=p^{-s_1}p^{-s_2}=uv.
\]

The complete local source is

\[
1-u-v+uv=(1-u)(1-v).
\]

Thus the `d` average is not independent noise. It is the precise Euler state
which completes the two reciprocal Möbius factors. Any argument that:

```text
replaces d by its unsigned density;
drops coprimality before reassembly;
takes absolute values in d;
or treats the d-sum as an external modulus average
```

must separately recover the lost `+uv` source state. Otherwise it is not an
estimate of SACF.

The large-gcd sector closed on PR #580 may be removed at polylogarithmic cost,
but reattaching it restores the exact Euler completion. Hence no conclusion-
scale gain comes merely from naming `d` a dispersion variable.

This firewall does not forbid a source-faithful dispersion theorem. It requires
such a theorem to retain the complete local factor and therefore to confront
the reciprocal-zeta square explicitly.
