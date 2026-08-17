# R-97400 — L-96651 does not prove the global completed-parity Lorenz inequality

Claim ID: `R-97400`  
Status: **EXACT PROOF-SCOPE CORRECTION; THE GLOBAL INEQUALITY IS NOT REFUTED**  
Created: 2026-08-18  
Frozen base: PR #566 at `2407b4ffe5024a2e3898922cf0b722d5cf69e496`  
Mandatory adversarial inputs: PR #574 at `74fba7f3e55fa9a53d1eb814e5067f5011ef5e86`; PR #575 at `265c481ebd02807ab7d9a95cb0cf905a22c1876f`

## 1. What L-96651 actually says

The deposited `L-96651` states, in prose, that actual child reserves are extracted from the grouped `P_61` parent source and that the remaining grouped Hall packet satisfies a scalar domination `g>=Tg`. It does not define the complete atom set, the reserve injection, the target-prefix ordering, the Hall coefficient vector, or the finite global optimization whose feasibility would imply that inequality.

The abstract parity lemma `L-96652` is correct: if a positive nilpotent operator `T` and a vector `g` satisfy `g>=Tg`, then the solution of `(I+T)F=g` is nonnegative. The missing statement is therefore not the algebraic resummation; it is the concrete inequality `g>=Tg` in the literal completed-parity source.

## 2. Why local determinant data do not supply it

PR #574 proves that corrected owner incidence and terminal target/scalar TP2 propagate determinant signs by Cauchy--Binet. It also gives the exact countermodel

```text
H=I_2,
K=[[1,1],[2,4]].
```

All entries and the relevant determinant are positive, but even target capacity is `1` and odd target demand is `2`. Thus TP2 does not imply global target feasibility or a Lorenz inequality.

## 3. Why scalar exactness does not supply two-row feasibility

PR #575 proves that if an edge is normalized by exactness of the scalar

`R_*(Y)=5Q_Y(2)+3Q_Y(3)`,

then, for `Y_e>=Y_o>2`,

```text
Delta_2 = -3 b Q_o(2)(rho_e-rho_o)/(5+3rho_e),
Delta_3 =  5 b Q_o(2)(rho_e-rho_o)/(5+3rho_e).
```

Hence scalar exactness trades row two against row three. It cannot be promoted to simultaneous two-row nonnegativity. Conversely, a proof that remains entirely in the scalar quotient need not prove rowwise positivity, but it must prove that every source, ownership, reserve, and resummation operation is closed in that quotient.

## 4. Binding odd-history witness

At

```text
X=67*71*13=61841,
history=(67),
terminal=(p,y)=(71,13),
```

PR #561 proves `E_T-O_T>17` in canonical orientation. The odd history swaps the parity channels, so actual even capacity is `O_T` and actual odd demand is `E_T`. Leafwise canonical Hall is impossible. Any valid proof must compensate this deficit using other histories in one global completed-parity source.

## 5. Exact replacement frontier

After complete parity expansion at one endpoint, let even atoms have capacities `a_i`, targets `t_i>0`, and scalar coordinates `r_i`; let the odd source have totals `(T_O,R_O)`. Define

`Phi_X(T)=max sum_i r_i u_i`

subject to

`0<=u_i<=a_i` and `sum_i t_i u_i=T`.

The completed-parity scalar Hall problem is feasible exactly when

```text
T_O <= sum_i a_i t_i,
R_O <= Phi_X(T_O).
```

Uniform validity of this inequality for every real endpoint is the exact producer `CPSL67`. It is not proved by L-96651, TP2, Cauchy--Binet, or the finite diagnostic replay.

```text
L-96652 abstract parity algebra           PROVED EXACT
L-96651 concrete global reserve theorem   UNPROVEN / SUPERSEDED
CPSL67 finite-at-each-X formulation       PROVED EXACT
CPSL67 uniform validity                    OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
