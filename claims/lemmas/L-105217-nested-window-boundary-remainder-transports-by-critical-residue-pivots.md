# L-105217 — Nested-window boundary remainders transport exactly by critical-residue pivots

Claim ID: `L-105217`  
Status: **PROVED EXACT ENTIRE-FUNCTION TRANSPORT IDENTITY**  
Created: 2026-08-23  
Depends on: `L-105214`  
RH status: **not assumed**

Let `F` be entire and real on the real axis. Let

\[
\Omega_1\Subset\Omega_2
\]

be bounded conjugation-symmetric Jordan domains. Assume `F'` has no zero on
either boundary and every critical point in the closed annulus

\[
\Omega_2\setminus\Omega_1
\]

is simple. Use the Cauchy boundary functions

\[
H_j(z)
={1\over2\pi i}
\int_{\partial\Omega_j}
{F(\zeta)/F'(\zeta)\over\zeta-z}\,d\zeta,
\qquad j=1,2.
\tag{L-105217.1}

## 1. Exact boundary-function transport

For `z in Omega_1`, the two finite Mittag-Leffler decompositions of
`L-105214` give

\[
{F(z)\over F'(z)}
=H_1(z)+
\sum_{c\in\Omega_1}{\rho_c\over z-c}
=H_2(z)+
\sum_{c\in\Omega_2}{\rho_c\over z-c}.
\]

Therefore

\[
\boxed{
H_1(z)
=H_2(z)+
\sum_{\substack{F'(c)=0\\c\in\Omega_2\setminus\Omega_1}}
{\rho_c\over z-c}.
}
\tag{L-105217.2}

No limiting argument is used.

## 2. Exact Loewner-kernel transport

For real `x,y in Omega_1`, put

\[
\mathscr L_j(x,y)
={H_j(x)-H_j(y)\over x-y}.
\]

Since

\[
{{1\over x-c}-{1\over y-c}\over x-y}
=-{1\over(x-c)(y-c)},
\]

(L-105217.2) yields

\[
\boxed{
\mathscr L_1(x,y)
=\mathscr L_2(x,y)
-
\sum_{c\in\Omega_2\setminus\Omega_1}
{\rho_c\over(x-c)(y-c)}.
}
\tag{L-105217.3}

Multiplying by `F'(x)F'(y)` gives the boundary-Bezoutian transport

\[
\boxed{
\mathscr R_{F,\Omega_1}(x,y)
=\mathscr R_{F,\Omega_2}(x,y)
-
\sum_{c\in\Omega_2\setminus\Omega_1}
\rho_c\,q_c(x)q_c(y),
}
\tag{L-105217.4}

where

\[
q_c(x)={F'(x)\over x-c}.
\]

The total Bezoutian is unchanged because the same rank-one terms move from the
boundary remainder into the explicit interior-residue ledger.

## 3. Monotonicity under real nonpositive residues

Suppose every annular critical point is real and

\[
\rho_c\le0.
\]

Then each increment

\[
-\rho_c\,q_c\otimes q_c
\]

is positive semidefinite. Consequently

\[
\boxed{
\mathscr R_{F,\Omega_1}
\succeq
\mathscr R_{F,\Omega_2}
}
\tag{L-105217.5}

on every real packet in `Omega_1`.

Thus a positive boundary remainder on one outer window descends through any
annulus containing only Rolle-generating real critical points. A loss of
boundary positivity can occur only through:

```text
one positive real residue;
one nonreal critical conjugate packet;
or a negative square already present in the outer remainder.
```

## 4. Finite exhaustion consequence

For a nested finite exhaustion

\[
\Omega_1\Subset\cdots\Subset\Omega_N,
\]

iteration gives

\[
\boxed{
\mathscr R_{F,\Omega_1}
=\mathscr R_{F,\Omega_N}
-
\sum_{c\in\Omega_N\setminus\Omega_1}
\rho_c\,q_c\otimes q_c.
}
\tag{L-105217.6}

If the outer remainder is positive semidefinite and every crossed critical
point is real with nonpositive residue, then the inner remainder is positive
semidefinite.

This is the exact domain analogue of reverse–Rolle descent. It shows that the
boundary gate `BRP105220` can be attacked by finding one positive terminal
window and proving the sharp pointwise residue sign in the intervening
annulus—without estimating a continued argument separately at every
intermediate window.

## 5. Scope

The theorem does not supply a positive terminal window for a fixed low Xi
derivative and does not prove that annular critical points are real or have
nonpositive residues. Nonreal conjugate pairs give real symmetric but not
sign-definite rank-two increments. The advance is the exact transport law and
its monotonicity under precisely the sharp residue condition.