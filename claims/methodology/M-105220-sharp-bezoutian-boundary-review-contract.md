# M-105220 — Hostile review contract for the sharp Bezoutian/boundary frontier

Claim ID: `M-105220`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

This packet changes the normative low-order frontier of PR #724. Reviewers
should reconstruct the exact finite identities first and must not infer the
entire-function conclusion from finite polynomial inertia alone.

## Frozen source context

```text
canonical main: 852d8aa05c701ea7818ce8a50543e68987fef5cc
stacked base:   PR #723 live branch
programme PR:   #724
prior frontier: L-105206--L-105212 / T-105210
new claims:     R-105202--R-105203, L-105213--L-105216, T-105220
```

## Required review order

1. `R-105202`: replay the five-real-root polynomial and verify that all
   residues are negative while `R(1-C)>2`.
2. `L-105213`: verify the sign convention of the Bezoutian, the partial
   fraction factorization and the exact congruence inertia.
3. `L-105214`: verify the Cauchy orientation, the sign of every residue term,
   and the finite-window boundary remainder.
4. `L-105216`: verify the factor two in the chord derivative and the Fourier
   constants in the translation average.
5. `R-105203`: retain the packet-size firewall; do not promote order-three
   Pick positivity to an all-packet theorem.
6. Run the exact replay and hostile mutations.
7. Review `T-105220` only as a conditional entire-exhaustion theorem.

## Load-bearing signs

The chosen Bezoutian is

\[
\mathscr B_F(x,y)
={F(x)F'(y)-F'(x)F(y)\over x-y}.
\]

Its diagonal is

\[
\mathscr B_F(x,x)=F'(x)^2-F(x)F''(x).
\]

At a real critical point,

\[
\mathscr B_F(c,c)=-\rho_cF''(c)^2.
\]

Thus a **positive** derivative-ratio residue is a **negative** Bezoutian pivot.
Any review using the opposite Bezoutian convention must reverse every inertia
statement consistently.

## Exact finite theorem versus proposed entire use

`L-105213` is a complete finite-polynomial theorem.

`L-105214` is an exact identity on one bounded regular window. It does not
prove:

- positivity of its Cauchy remainder;
- absence of nonreal critical points;
- convergence of an unbounded Xi exhaustion;
- the generalized Hermite--Biehler negative-square criterion under the exact
  proposed limiting protocol.

Those requirements are bundled into the explicit open gate `BRP105220`.
Reviewers must reject any wording that silently converts the finite-window
identity into global positivity.

## Relation to existing actual-Xi Pick results

The integrated repository proves the actual-Xi safe Pick packets through size
three. The boundary function `H_(F,Omega)` is not automatically the same
coordinate. A valid import requires an exact map of:

```text
function and normalization;
safe-axis domain;
node variables;
window/exhaustion protocol;
critical-reserve resource use.
```

Even after such a map, `R-105203` proves that packet size three does not
bootstrap abstractly to all packet sizes.

## Replay contract

```bash
python -B experiments/X-105220-bezoutian-boundary-decomposition/verify.py \
  --output experiments/X-105220-bezoutian-boundary-decomposition/results/verification.json
```

Expected:

```text
PASS_X_105220_BEZOUTIAN_BOUNDARY_DECOMPOSITION
```

Arithmetic class: exact rational arithmetic plus a complete-real-line Sturm
count. The replay does not evaluate Xi and does not certify `PRES105220`,
`BRP105220` or RH.

## Binding scientific boundary

```text
ESDE105212 as canonical gate                 REFUTED
finite Bezoutian diagonalization             PROVED EXACT
finite-window Cauchy remainder identity      PROVED EXACT
short-chord translation-average positivity   PROVED
PRES105220                                   OPEN
BRP105220                                    OPEN
Riemann Hypothesis                           UNPROVED
```
