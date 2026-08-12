# R-91405 — The aligned continuous Lévy measure cannot dominate the prime atomic sampling measure

Claim ID: `R-91405`  
Status: **EXACT MUTUAL-SINGULARITY FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91413`  
Corrects: the unqualified fully polarized sampling target in the first version of `L-91413.23`  
RH status: **unproved**

## 1. The tempting inequality

At the plastic-aligned scale, `L-91413` constructs a positive absolutely
continuous Lévy measure

\[
 d\omega_\diamond(u)
 =w_\diamond(u)du
\]

and positive prime-power weights

\[
 c_n>0,
 \qquad
 u_n=\log n.
\]

A tempting strengthening of the scalar carrier inequality is

\[
 \int_0^\infty|F(u)|^2d\omega_\diamond(u)
 \ge
 \sum_{n\ge2}c_n|F(u_n)|^2
 \tag{R-91405.1}
\]

for every finite linear combination of carrier defects

\[
 F(u)=\sum_jz_j(e^{ix_ju}-1).
 \tag{R-91405.2}
\]

This inequality is false.

## 2. Fejér isolation of one prime atom

Fix one prime power `n0` and put

\[
 u_0=\log n_0>0.
\]

For `T>0`, define

\[
 A_T(u)
 =\frac1T\int_0^T e^{ix(u-u_0)}dx
\tag{R-91405.3}
\]

and

\[
 F_T(u)=A_T(u)-A_T(0).
\tag{R-91405.4}
\]

The Bochner integral in (R-91405.3) is the local-uniform limit of Riemann sums,
so `F_T` belongs to the closure of the finite carrier-defect span.  Moreover,

\[
 F_T(u_0)=1-A_T(0)\longrightarrow1,
\tag{R-91405.5}
\]

while for every fixed `u not equal u0`,

\[
 A_T(u)\longrightarrow0.
\tag{R-91405.6}
\]

Since `|A_T|<=1`, dominated convergence gives

\[
 \boxed{
 \int_0^\infty|F_T(u)|^2d\omega_\diamond(u)
 \longrightarrow0.
 }
\tag{R-91405.7}

Here absolute continuity is load bearing: the single point `u0` has zero
`omega_diamond` mass.

## 3. The prime norm stays positive

The prime sampling measure is

\[
 d\nu_{\rm p}(u)
 =\sum_{n\ge2}c_n\delta_{u_n}(du).
\]

Its total mass is finite at the safe aligned scale.  For every prime-power
atom distinct from `u0`, (R-91405.6) gives `F_T(u_n)->0`; at `u0`,
(R-91405.5) gives convergence to one.  Dominated convergence for the finite
atomic measure therefore yields

\[
 \boxed{
 \sum_{n\ge2}c_n|F_T(u_n)|^2
 \longrightarrow c_{n_0}>0.
 }
\tag{R-91405.8
}

Equations (R-91405.7)--(R-91405.8) contradict (R-91405.1).

The same proof works with finite Riemann-sum approximants and a small strict
margin, so the failure already occurs inside the algebraic finite-carrier
span.

## 4. Finite anchor coordinates do not repair pure measure domination

Suppose finitely many continuous linear functionals

\[
 L_1,\ldots,L_m
\]

on the carrier-defect closure are adjoined to the left side.  By taking a
linear combination of `m+1` Fejér packets centred at distinct prime atoms, one
may impose

\[
 L_j(F_T)=0
 \quad(1\le j\le m)
\]

while retaining a nonzero value at at least one chosen atom.  Hence no finite
anchor augmentation converts the continuous measure into a dominating measure
for the complete prime sampling norm.

This statement does not apply to the full connection kernel of `T-91402`,
which is not assumed finite rank and is coupled to the prime endpoint ports.

## 5. Correct role of plastic alignment

Plastic alignment remains exact and useful:

```text
the nonprime scalar channel is a positive Lévy increment;
all prime scalar coefficients have one sign;
all continuous sign mismatch is removed;
the scalar problem becomes one positive continuum-minus-prime formula.
```

What fails is the attempt to prove the **fully polarized** form by uncoupled
measure domination.  The connection and endpoint ports in CPPD are not
technical leftovers; they are mathematically necessary to prevent prime-atom
isolation.

## 6. Relation to the finite-compression lesson

Claude's Zeta23 argument succeeds by using a finite critical-density
compression and only the first two trace moments.  It explicitly does not
claim positivity of the full Weil form.  The present no-go is the complementary
full-resolution fact: once every carrier is allowed, the prime atomic channel
can be isolated from an absolutely continuous reserve.  A conclusion-producing
proof must preserve the coupled finite-jet/endpoint geometry rather than
compare the two measures separately.

## 7. Correct remaining target

The valid final theorem remains CPPD:

\[
 \mathcal C_a^\lambda+\mathcal P_a
 \succeq\mathcal N_a.
\]

The connection block and endpoint ports must be used jointly.  The pure
sampling inequality is removed from the production target.

## 8. Exact boundary

```text
plastic-aligned continuous measure positive          EXACT
prime residual weights positive                      EXACT
continuous measure dominates prime sampling          FALSE
failure on finite carrier packets                     EXACT
finite-anchor repair                                  FALSE IN GENERAL
coupled connection/endpoint CPPD                      OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
