# Full repair pass: Gauss atomic ledger, Wick centering, and Boolean half-source transport

Date: 2026-08-25  
Execution PR: #751  
Programmes: #743, #736, #737  
Parent scientific frontier: PR #719 `T-102990 / BCI102990`  
Status: **binding normalization correction and exact repaired implication matrix; RH unproved**

## Executive result

The bilateral L-family construction is source-exact, but its claimed complete
atomic diagonal omitted the number of nonzero phases/character channels.

For one conductor `q`,

\[
\sum_{\eta\ {\rm even}}w_q(\eta)=q-1.
\]

For the bilateral tensor, the total atomic coefficient is therefore

\[
(\ell-1)(\rho-1),
\]

not one. The old diagonal calculations remain valid only for the principal
and principal--principal channels, whose weights are bounded.

The repair is exact Wick normal ordering. After subtracting the literal atom
from every channel before the conductor sum,

\[
\mathfrak A^\circ
=
\mathfrak P^\circ
+
\mathfrak K^\circ,
\]

where:

```text
A^circ  = atomic-free additive/CV-XD trace;
P^circ  = atomic-free principal--principal trace;
K^circ  = atomic-free mixed/double Kummer trace.
```

The principal atomic diagonal is already subpower, so

```text
WCADD106140
AND
WCKUM106140
  -> principal bilateral moment is subpower
  -> BCI102990
  -> RH.
```

Both new gates remain open.

## New source identity

The Boolean balanced coefficient has the exact half-source square

\[
b_U=f_U\star f_U,
\qquad
f_U=a_U\star h,
\qquad
h(S)=(-1/2)^{|S|}.
\]

If `ell` is the least prime and the remaining support lies above it,

\[
f_U(\ell u)
=
\frac12F_{U,>\ell}(u)-F_{U/\ell,>\ell}(u),
\]

and hence

\[
b_U(\ell u)
=
F_{U,>\ell}^{\star2}(u)
-
2F_{U,>\ell}\star F_{U/\ell,>\ell}(u).
\]

Thus a least-prime row is a signed cutoff difference, not an independent
positive conductor square. This gives a concrete source-side attack on
`WCADD106140`.

## Binding dispositions

```text
L-106110 / L-106120 exact family identities        retained
R-106122 physical-squareclass firewall             retained
R-106123 local/global conductor firewall           retained
L-106112 owner Wick factorization                   retained
L-106121 conditional domination                    retained

full M_DA atomic diagonal claimed paid              corrected
full M_BT atomic diagonal claimed paid              corrected
principal / PP atomic diagonals                     retained paid
uncentered nonprincipal moments                     no longer conclusion gates
```

## Replay

```text
PASS_X_106140_WICK_CENTERED_FAMILY_REPAIR
exact_checks=23035
proof_object_sha256=d4b5920eb5a4a68210ba2c22c9ed426de6ef9b46bc37749ef73947cd9a9e07ef
```

The replay checks finite exact operator and Boolean-source identities. It does
not prove either open global trace estimate, `BCI102990`, or RH.
