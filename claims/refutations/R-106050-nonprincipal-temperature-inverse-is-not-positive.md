# R-106050 — The nonprincipal temperature-square inverse is not positive

Claim ID: `R-106050`  
Status: **PROVED EXACT SIGN FIREWALL**  
Created: 2026-08-24  
Depends on: `L-106050`; PR #719 `L-102893`  
Programme issues: #743, #736, #737  
RH status: **unproved**

For the untwisted midpoint product, PR #719 constructs the positive square-
lattice inverse

\[
S_1^{-1}
=
\prod_p(1-p^{-1}U_p^2)^{-1},
\]

whose coefficients are nonnegative. This positivity is load-bearing in the
negative-mass transfer from the midpoint square to the native detector.

For a character-square channel `eta`, the analogous inverse is

\[
\boxed{
S_\eta^{-1}
=
\prod_p
(1-\eta(p)p^{-1}U_p^2)^{-1}.
}
\tag{R-106050.1}
\]

Its coefficient at the square `n^2` is

\[
\boxed{
\frac{\eta(n)}n
}
\tag{R-106050.2}
\]

on the unramified monoid.

If `eta` is nonprincipal, there exists an unramified integer `n` with

\[
\eta(n)\ne1.
\]

Therefore (R-106050.2) is either negative or nonreal for some coefficient. The
inverse is not a nonnegative source kernel.

## Consequence

The memberwise implication

```text
positive or small-negative-mass twisted midpoint square
 -> positive or small-negative-mass twisted native source
```

is unavailable for nonprincipal `eta`. It cannot be obtained by copying the
untwisted argument of `L-102893`.

The correct order is instead:

```text
retain the complete quadratic root fibre;
form the positive Kummer/Gauss family moment;
keep the owner quadratic-class charts separate;
perform the collective physical assembly;
use the positive inverse only in the principal eta=1 channel.
```

Thus the L-family programme supplies a positive **family frame**, not a
positive inverse in each member.

This firewall does not refute the twisted flat factorization `L-106050` or the
Kummer chart theorem `L-106051`. It rules out a false memberwise sign transfer
and proves no RH result.
