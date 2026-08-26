# L-106212 — The Boolean half-source is a Witt tower of \(L\)-functions

Claim ID: `L-106212`  
Programme aliases: `LFAM2.WITT_L_TOWER`, `LFAM1.HALF_SOURCE_EULER_FACTOR`, `STRESS.NORMAL_ORDERED_FAMILY_DICTIONARY`  
Status: **PROVED EXACT FORMAL EULER/L-FUNCTION FACTORIZATION**  
Created: 2026-08-26  
Depends on: `L-106133`, formal Euler products  
Programme issues: #737, #736, #743  
Number-field RH status: **not assumed**

Let \(\chi\) be a multiplicative character and define the twisted squarefree
half-source series

\[
\mathscr H_\chi(u)
=
\sum_{\substack{F\ {\rm monic}\\ \mu^2(F)=1}}
\left(-\frac12\right)^{\omega(F)}
\chi(F)u^{\deg F}
=
\prod_P
\left(1-\frac12\chi(P)u^{\deg P}\right).
\tag{L-106212.1}
\]

Define the rational Witt coefficients

\[
\boxed{
\gamma_m
=
\frac1m
\sum_{d\mid m}\mu(d)\,2^{-m/d}.
}
\tag{L-106212.2}
\]

They satisfy

\[
\sum_{m\mid n}m\gamma_m=2^{-n},
\]

and therefore the local formal identity

\[
\boxed{
1-\frac x2
=
\prod_{m\ge1}(1-x^m)^{\gamma_m}.
}
\tag{L-106212.3}
\]

Applying (L-106212.3) prime by prime gives the coefficientwise exact
factorization

\[
\boxed{
\mathscr H_\chi(u)
=
\prod_{m\ge1}
L(u^m,\chi^m)^{-\gamma_m}.
}
\tag{L-106212.4}
\]

Only \(m\le n\) contributes to the coefficient of \(u^n\), so no analytic
interchange is required for the formal statement.

The first exponents are

\[
\gamma_1=\frac12,
\qquad
\gamma_2=-\frac18,
\qquad
\gamma_3=-\frac18.
\]

Hence

\[
\boxed{
\mathscr H_\chi(u)
=
L(u,\chi)^{-1/2}
L(u^2,\chi^2)^{1/8}
L(u^3,\chi^3)^{1/8}
\cdots.
}
\tag{L-106212.5}
\]

## Resonance classification

If \(\chi\) has order \(R\), a principal family constituent occurs exactly
at the tower levels \(m\) divisible by \(R\).

In particular:

```text
principal chi:
  the m=1 factor has the full principal Euler scale;

quadratic chi:
  the first new principal resonance is m=2 and lies at square-root scale;

order >2:
  neither m=1 nor m=2 is principal.
```

This is the exact \(L\)-family origin of the special quadratic-root channel:
it is a resonance of the Boolean half-source tower, not an arbitrary
exception introduced by the Gauss transform.

## Relation to the live Wick square

For \(f_U=a_U\star h\), the finite cutoff polynomial \(a_U\) acts on
\(\mathscr H_\chi\) by Boolean normal ordering. The live analytic square in
`T-106150` is therefore a normal-ordered square of a finite cutoff acting on
the Witt \(L\)-tower, not an uncentered modulus square of one \(L\)-function.

## Scope

The theorem is an exact family dictionary. It proves no mean value,
`WCKUM106140`, `REFSIG106150`, `BCI102990`, or RH.
