# Cycle-Debt/Q4 fourth strike: discrepancy duality and scalarization

Date: 2026-08-15  
Target: draft PR #474  
Frozen parent: `0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b`

**Scientific status: RH remains unproved.**

## Repository reconciliation

At cutoff, `main` remained
`9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`; PR #474 was open, draft,
mergeable, and had no submitted reviews. The only material overlap was PR #483
at `87bd7ad2127f98b6141b4c03355556f2b95f6404`, whose complete Q4 prime-base
Gram was already imported by the third strike. Newer visible work was concentrated
in factor-67 branches and was not imported.

## Cycle Debt: remove the artificial baseline and bottom payment

For positive carry weights `a_q`, the functions

```text
g_q(n) = a_q floor(n/q)
```

form a triangular basis of node potentials with value zero at node one. If
`H=sum theta(q)g_q`, then every split defect is

```text
delta_H(e) = sum_q theta(q) a_q chi_e(q).
```

For the critical target, the objective diagonalizes with

```text
ell_X(q) = log(X/q)/q.
```

Translating the asymmetric Cycle-Debt dual before taking an absolute value gives
the exact one-sided discrepancy problem

```text
N_X = max_( -W <= A psi <= 0 ) <ell_X,psi>.
```

Its positive finite dual is

```text
N_X = min W^T v
      subject to A^T(u-v)=ell_X, u,v>=0.
```

This avoids the irrational-source rationality overstatement corrected earlier:
a proof certificate may authenticate the target weights symbolically or with
outward primitive intervals.

The split `2=1+1` implies `-1<=psi(2)<=0`. Since `ell_X(2)>=0`, the bottom
coordinate cannot increase the objective. Under `X=2Y`, even objective weights
inherit exactly one half of the lower endpoint. Retaining odd variables and
their borrowing against doubled constraints in one LP gives

```text
N_(2Y) <= (1/2)N_Y + B_(2Y)
```

with no `+(1/4)log Y` term. The exact remaining theorem is One-sided Parity
Borrowing (`OPB`): `B_(2Y)<=polylog(Y)`. OPB would imply polylogarithmic Cycle
Debt and then RH through the resident consumer. OPB is not proved here.

## Q4: the complete endpoint energy is one scalar problem

For arbitrary coefficients with prefix `C` and endpoint mean `M`,

```text
M(N) = C(N) - (2/N) sum_(j<N) C(j).
```

A telescoping recurrence gives the exact finite inverse

```text
C(N)
 = M(N)
   - 2(N+1) sum_(k=N)^K M(k)/((k+1)(k+2))
   + 2(N+1)S(K)/((K+1)(K+2)),
```

where `S(K)=sum_(j<=K)C(j)`. The boundary term is load bearing: the fixture
`c(n)=1` shows that deleting it without a zero-linear-mode hypothesis gives a
false formula. This firewall is recorded as `R-93020`.

For the actual compact-Q4 source,

```text
C_circ(N)=psi(N)-4psi(N/4)+O(log N)=o(N)
```

by the unconditional prime number theorem, so the boundary term vanishes. The
infinite inverse preserves all polynomial exponents below one and, in
particular, square-root/polylog growth. Therefore

```text
|M_circ(N)| <= sqrt(N) log^A N
    => C_circ(N) <= sqrt(N) log^A N
    => every row R_N(j) has the same bound
    => P_circ(N) <= log^(2A) N.
```

The converse follows from the coefficient-one variance inequality
`|M_circ(N)|^2 <= N P_circ(N)`. Composed with the zero-safe Mellin transform in
`T-93010`, this yields the candidate equivalence

```text
RH
<=> square-root/polylog control of M_circ
<=> polylog control of complete endpoint PIG.
```

The previous distinct-prime major-arc normal form remains useful for arithmetic
attacks and inverse theorems, but is not a logically independent completion
gate once the global mean is controlled.

## Exact scale-four source bridge

Define

```text
B4(s)=(1-4^(1-s))/(1-4^(-s)),
A4(s)=B4(s)/zeta(s).
```

Then `B4(s)=1-3 sum_(r>=1)4^(-rs)`. Writing `a4=b4*mu` gives explicit
two-adic coefficients and preserves every open-strip reciprocal-zeta pole.
Direct logarithmic differentiation proves

```text
sum c_circ(n)n^(-s)
 = (1-4^(1-s)) A4'(s)/A4(s),
```

and coefficientwise

```text
c_circ*a4 = -(epsilon-4 delta_4)*(a4 log).
```

This identifies the Q4 source as the scale-four logarithmic derivative of a
zero-safe Mobius state. It does not by itself construct a bounded positive or
capacity-faithful map between the routes.

## Lightweight verification

```text
PASS_X_93017_CYCLE_DEBT_CARRY_DISCREPANCY
PASS_X_93018_Q4_HARDY_LOGDERIVATIVE
```

The first replay checks triangular basis reconstruction, split defects, target
pairing, four exact small-LP equivalences, bottom signs, dyadic scaling, and
hostile mutations. The second checks finite Hardy identities, exact backward
inversion, vanishing and nonvanishing boundary fixtures, 512 explicit `a4`
coefficients, 512 formal prime-log convolution identities, and hostile
mutations. No broad scans or heavy computation were used.

## Exact remaining frontier

```text
Cycle Debt: prove OPB.
Q4: prove M_circ(N)=O(sqrt(N) log^A N).
Cross route: make the logarithmic-derivative dictionary capacity faithful.
Riemann Hypothesis: UNPROVEN.
```
