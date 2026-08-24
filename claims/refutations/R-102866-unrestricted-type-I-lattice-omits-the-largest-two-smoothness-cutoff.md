# R-102866 — The unrestricted Type-I lattice omits the largest-two smoothness cutoff

Claim ID: `R-102866`  
Status: **EXACT SOURCE-TYPING REFUTATION OF L-102867 AS SUBMITTED**  
Created: 2026-08-24  
Depends on: `L-102831`, `L-102866--L-102868`  
RH status: **unproved**

The largest-two squareclass packet is not

\[
\sum_a\frac{\mu(a)}a R_L(Y/a^2)
\]

over all integers `a`. It is

\[
\boxed{
\sum_{\substack{a\ge1\\P^+(a)<q}}
\frac{\mu(a)}a R_L(Y/a^2),
}
\tag{R-102866.1}

where `q` is the second owner prime.

Consequently, after applying the Vaughan identity, the Type-I lattice is

\[
\boxed{
\sum_{\substack{m\ge1\\P^+(dem)<q}}
\frac1m R_L\!\left(\frac{Y}{d^2e^2m^2}\right),
}
\tag{R-102866.2}

not the unrestricted sum used in `L-102867.4`.

The zero continuous moment of `L-102866` proves

\[
\sum_{m\ge1}\frac1mR_L(Z/m^2)=O(Z^{-1/2}),
\]

but it does not prove the same estimate after the `q`-smooth stopping rule.
The missing terms are not a finite endpoint error: they are a moving
largest-prime boundary.

## Exact Buchstab boundary

For

\[
\mathscr L_{<q}(Z)
=\sum_{P^+(m)<q}\frac1mR_L(Z/m^2),
\]

largest-prime disintegration gives

\[
\boxed{
\mathscr L_{<q}(Z)
=\mathscr L_\infty(Z)
-\sum_{\ell\ge q}\frac1\ell
\mathscr L_{\le\ell}(Z/\ell^2),
}
\tag{R-102866.3}

with only terms meeting the support of `R_L` retained. The second term is the
literal smooth-boundary/owner-transfer current.

Thus the unrestricted zero-moment lattice is one closed coordinate, but the
stopped smooth boundary must be retained. It may be treated through the
Dickman--Stieltjes/Bellman corridor only at that corridor's proved uniform
scope; the dynamic critical finite block is still open in the integrated
front door.

## Disposition

```text
L-102866 zero unrestricted lattice moment      VERIFIED
L-102867 unrestricted square-core composition  FALSE AT SOURCE-TYPING LAYER
L-102868 claims depending on global Type-I closure SUPERSEDED IN THAT SCOPE
```

The corrected source decomposition is deposited in `L-102869`. No conclusion
about RH follows from the unrestricted lattice estimate alone.
