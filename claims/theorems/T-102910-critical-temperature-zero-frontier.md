# T-102910 — Critical-temperature zero frontier for the geometric midpoint square

Claim ID: `T-102910`  
Status: **MAJOR UNCONDITIONAL PHASE-TRANSITION REDUCTION; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

The geometric completion family

\[
E_t(z)
=
\prod_\ell(1-p_\ell^{-z})(1+p_\ell^{-z})^t
\]

interpolates exactly between the native source, its geometric midpoint
half-source, and the squared completion.

For its arithmetic source square observed through the fixed outer kernel,
`L-102895` proves the sharp sign law

\[
\boxed{
\begin{aligned}
\mathscr S_t(X)&<0 &&(0<t<1/2),\\
\mathscr S_t(X)&>0 &&(1/2<t<1),
\end{aligned}
}
\]

with \(t\) fixed and \(X\) large.

At the unique interior critical temperature,

\[
t={1\over2},
\]

the deterministic real branch vanishes and

\[
\mathscr S_{1/2}
\]

is exactly the arithmetic geometric-midpoint square
\(\eta*\eta=\beta*\beta^\square\).

`L-102896` proves that the finite-horizon sign-transition zero
\(\vartheta(X)\) is unique in an exponentially thin layer and satisfies

\[
\boxed{
|\vartheta(X)-1/2|
\ll
(\log X)^2
\exp\!\left[
-a(\log X)^{3/5}(\log\log X)^{-1/5}
\right].
}
\]

`L-102897` proves that the conclusion-bearing negative mass is precisely the
positive weighted drift of this zero:

\[
\boxed{
(\mathscr S_{1/2}(X))_-
\asymp
{\sqrt X\over(\log X)^2}
\left(\vartheta(X)-{1\over2}\right)_+.
}
\]

Thus the exact new criterion is

```text
CTZD102897:
  the positive weighted drift of the unique geometric-completion
  temperature zero has subpower logarithmic mass.
```

The implication chain is

\[
\boxed{
\mathrm{CTZD}_{102897}
\Longleftrightarrow
\mathrm{GMBC}_{102893}
\Longrightarrow
\mathrm{RH}.
}
\]

With the standard RH-to-compact-observation implication, `CTZD102897` is
RH-equivalent.

## Relation to the stopped-current route

The live programme now has two exact coordinates on the same endpoint
difficulty:

```text
SGIC102890:
  source/owner/gcd/phase coordinate;

CTZD102897:
  one-dimensional completion-temperature-zero coordinate.
```

The former exposes arithmetic cancellation.  The latter proves that all
strict completion temperatures are already decided and that the unresolved
sign is an exponentially small displacement at the unique critical
temperature.

`R-102871` is binding: strict-temperature signs do not determine the side of
the limiting zero.

```text
strict source-square phase transition     PROVED
critical midpoint identification          PROVED EXACT
transition-zero localization              PROVED
drift/negative-mass equivalence            PROVED EXACT
CTZD102897                                OPEN / RH-EQUIVALENT
Riemann Hypothesis                        UNPROVED
```
