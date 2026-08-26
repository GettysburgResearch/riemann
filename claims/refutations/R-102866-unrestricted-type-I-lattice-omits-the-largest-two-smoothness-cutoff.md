# R-102866 — The unrestricted Type-I lattice omits the largest-two smoothness cutoff

Claim ID: `R-102866`  
Status: **EXACT SOURCE-TYPING REFUTATION OF L-102867 AS SUBMITTED**  
Created: 2026-08-24  
Corrected: 2026-08-24  
Depends on: `L-102831`, corrected `L-102866`, `L-102869`  
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

not the unrestricted sum used in the first version of `L-102867`.

Corrected `L-102866` proves

\[
\sum_{m\ge1}\frac1mR_L(Z/m^2)
=4(1-\sqrt2)(\log2)^2+O_R(Z^{-1/2}),
\]

so the unrestricted Type-I coordinate has a favorable nonnegative square main
after the leading minus sign. That does not determine the stopped lattice.
The missing terms are a moving largest-prime boundary, not a fixed endpoint
error.

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

with only support-active terms retained. The second term is the literal
smooth-boundary/owner-transfer current.

It may be treated through Dickman--Stieltjes/Bellman coordinates only at their
proved uniform scope; the integrated front door explicitly leaves the dynamic
critical finite block open.

## Disposition

```text
L-102866 exact unrestricted lattice asymptotic    VERIFIED / NONZERO MAIN
L-102867 literal largest-two composition           SUPERSEDED
L-102868 conclusions using unrestricted Type-I     SUPERSEDED IN THAT SCOPE
L-102869 stopped-prime decomposition                VERIFIED EXACT
```

No conclusion about RH follows from the unrestricted lattice estimate alone.
