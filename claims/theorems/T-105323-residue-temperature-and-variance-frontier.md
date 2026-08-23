# T-105323 — Conserved residue temperature and the variance-production frontier

Claim ID: `T-105323`  
Status: **PROPOSED EXACT FINITE ADVANCE; XI LOCALIZATION AND LOW-ORDER VARIANCE OPEN**  
Created: 2026-08-23  
Depends on: `L-105320`, `L-105323`; parent reverse-Rolle ledger  
RH status: **unproved**

## 1. Exact conserved carrier

For every monic finite polynomial `p` of degree `n>=2`, define

\[
\mathcal T(p)
={1\over n(n-1)}
\sum_{j=1}^{n}(z_j-\bar z)^2.
\]

`L-105323` proves

\[
\boxed{
\mathcal T(p'/n)=\mathcal T(p).
}
\tag{T-105323.1}
\]

Thus one normalized centered root moment survives every derivative step
exactly. If the critical points are simple, the complete algebraic first
residue moment is

\[
\boxed{
-\sum_{p'(c)=0}{p(c)\over p''(c)}
={n-1\over n}\mathcal T(p).
}
\tag{T-105323.2}
\]

The adjacent first-moment loss is therefore the explicit square-summable
factor

\[
\boxed{
1-{A(p'/n)\over A(p)}={1\over(n-1)^2}.
}
\tag{T-105323.3}
\]

No unknown arithmetic estimate enters these identities.

## 2. Exact normal form for coherence

At a real-rooted level, put

\[
a_c=-{p(c)\over p''(c)}>0,
\qquad
\alpha_c={n a_c\over\mathcal T(p)}.
\]

Then the `alpha_c` have exact mean one, and

\[
\boxed{
\mathfrak C(p)
={1\over1+\operatorname{Var}_p(\alpha)}.
}
\tag{T-105323.4}
\]

Consequently

\[
\boxed{
R(1-\mathfrak C)
=R{\operatorname{Var}(\alpha)
 \over1+\operatorname{Var}(\alpha)}.
}
\tag{T-105323.5}
\]

This is exactly the residue term paid by reverse Rolle. The low-order problem
is therefore not loss of the first residue carrier: that carrier is conserved.
It is **production of normalized inverse-curvature variance** around the
conserved carrier.

## 3. Compression interpretation

The same variance controls the root-compression mismatch:

\[
\sin^2\theta_p
\le
\min(1,\operatorname{Var}_p(\alpha)),
\]

and hence

\[
\max_j|d_j-k_j|
\le
2\operatorname{diam}(C)
\sqrt{\min(1,\operatorname{Var}_p(\alpha))}.
\tag{T-105323.6}
\]

Thus one scalar variance has two exact meanings:

```text
reverse-Rolle wrong-extremum budget;
adjacent derivative versus Krylov spectral-flow defect.
```

## 4. Exact replay

```text
PASS_X_105323_RESIDUE_TEMPERATURE
de47366ec7a4145b645cd864ca855fef228f7fb8b328d26602fba4c516a935e0
RH_UNPROVEN
```

The replay performs 20 exact rational derivative-chain checks. Together with
`X-105320`, the finite part of this programme now has 117 exact checks.

## 5. Xi continuation target

For a finite symmetric canonical-product approximation to a Xi derivative,
the proposed high-tail saddle theorem predicts

\[
\alpha_c=1+o(1),
\]

hence negligible variance. To use (T-105323.4) in the entire Xi ladder one
must still prove:

1. a height-localized passage of the conserved carrier through the chosen
   canonical-product exhaustion;
2. a one-sided bound for the accumulated normalized variance at the first
   `O(T log T)` low derivative levels;
3. compatibility with the exact endpoint/winding ledger.

Define `RVP105323` as the statement that the localized variance-production and
boundary budgets together are below two in every sufficiently large regular
Xi rectangle. Then

\[
\boxed{
\mathrm{RVP105323}
\Longrightarrow
\mathrm{CRDB105200}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105323.7}

The first implication is an exact change of variables using (T-105323.5). The
premise remains open.

## 6. Status

```text
normalized root-temperature invariance       PROPOSED EXACT / REPLAYED
first residue carrier flow                    PROPOSED EXACT / REPLAYED
coherence = normalized curvature variance     PROPOSED EXACT
variance -> compression mismatch              PROPOSED EXACT
Xi height-localized carrier passage            OPEN
low-order variance-production budget           OPEN / RH-BEARING
endpoint/winding budget                        OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
