# T-29802 — Amortized Hausdorff eta–Pascal closure of the central carry cascade

Claim ID: `T-29802`  
Title: Positive stopped powers, strict analytic contraction, and a conserved Hausdorff/Pascal boundary budget give polylogarithmic Cycle Debt and RH  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Branch: `agent/gpt56-pro-global/296-triangular-eta-pascal-closure`  
Supersedes: the stronger arbitrary-label boundary factor in `T-29801/L-29803`  
Scope: corrected complete proposed RH chain; **RH is not represented as independently verified**

## 1. Frozen dependencies

Review against the frozen heads

```text
PR #272  5cb703bcc1593c4ce8f1f2d8d3840dc61d573dba
          exact dyadic commutator normal form and Cycle-Debt consumer

PR #286  6bba6161887b6913f4f50c1b90ee46a0fd84c339
          shifted analytic 6/7 contraction and finite Euler/Peano cutoff ledger

PR #294  839900f2738c6a3da67f4754b462e953bc1034ba
          complete eta boundary comb and local capacity-feasible Pascal switches
```

The native correction is `L-29806/R-29802`.

## 2. Positive finite critical source

For every integer endpoint `X`,

\[
\boxed{
 q^{-1/2}\log(X/q)
 =\sum_{Y=q}^{X-1}
   \log{Y+1\over Y}\,q^{-1/2}.
}
\tag{T-29802.1}

Thus the complete critical target is a finite positive layer cake of stopped pure powers

\[
 p_Y(q)=q^{-1/2}\mathbf1_{q\le Y}.
\]

This removes the signed Mellin-exponent derivative from the finite producer.

## 3. Strict analytic bulk contraction

PR #286 proves that the infinite shifted central operator acts on pure powers by

\[
 \mathscr Cp_s
 =[1-\eta(s)]p_s
 +\sum_{r\ge1}c_{s,r}p_{s+r},
 \qquad c_{s,r}>0,
\]

and contracts the declared positive coefficient norm:

\[
\boxed{
 A_{a+1}(X)\le{6\over7}A_a(X).
}
\tag{T-29802.2}

Every shifted correction is a faster positive power.  The analytic source cone is invariant and strictly contracting.

## 4. Exact finite cutoff source

For

\[
 \Delta_hf(x)=f(x)-f(x+h),
\]

`L-29801/L-29806` give

\[
 \Delta_h^m(x+jh)^{-s}
 =\int_{[0,1]}y^j(1-y)^m\,d\nu(y)
 \ge0,
\tag{T-29802.3}

and the exact alternating Euler remainder

\[
 R_K^{(m)}
 =\int_{[0,1]}
 {y^K(1-y)^m\over1+y}\,d\nu(y)
 \ge0.
\tag{T-29802.4}

Both sequences decrease with the quotient index.

Consequently every finite jet and exact remainder in PR #286 `L-28402` is a positive decreasing source on the common paired tail.  The unmatched first omitted terms remain in the explicit finite collar and are not silently paired.

## 5. Unequal eta pairs and exact Pascal payment

For one paired tail let `V_e>=V_o>=0` be the internal even/odd source values.  Put

\[
 M={V_e\over2k},
 \qquad
 T={V_o\over2k+1}.
\]

Then `T<=M`, and

\[
\boxed{
 M e_{2k}-T e_{2k+1}
 =(M-T)e_{2k}+T(e_{2k}-e_{2k+1}).
}
\tag{T-29802.5]

The dipole is the exact balanced Pascal sibling switch

\[
 [2k+2k]\to[(2k-1)+(2k+1)]
\]

at parent `4k`.  Its logarithmic objective cost is

\[
 T\log{2k+1\over2k}.
\]

Since the logarithm is below one,

\[
\boxed{
 (M-T)+T\log{2k+1\over2k}\le M.
}
\tag{T-29802.6]

Thus every boundary source unit pays both its residual lower-scale source and its complete Pascal objective cost without exceeding its incoming mass.

This is the corrected invariant.  It permits unequal internal labels and does not require a uniform strict boundary factor.

## 6. Global amortized boundary ledger

Let

- `J_a(X)` be total positive boundary source mass entering depth `a`;
- `C_a(X)` be the exact objective cost of all Pascal switches at that depth;
- `I_a(X)` be new boundary source injected by the analytic cutoff and finite collar.

After common-destination recombination, summing (T-29802.6) gives

\[
\boxed{
 J_{a+1}(X)+C_a(X)
 \le J_a(X)+I_a(X).
}
\tag{T-29802.7]

Hence

\[
\boxed{
 J_A(X)+\sum_{a<A}C_a(X)
 \le J_0(X)+\sum_{a<A}I_a(X).
}
\tag{T-29802.8]

The analytic injection obeys

\[
 I_a(X)
 \le C_MA_a(X)
   +C_M'(1+a)^{r_M}\log^{s_M}(2X),
\tag{T-29802.9]

where the polynomial term is the complete first-omitted collar of PR #286.  Because `A_a<=(6/7)^aA_0` and the cascade has only `O(log X)` half-scale levels,

\[
\boxed{
 J_A(X)+\sum_{a<A}C_a(X)
 =O(\log^B(2X))
}
\tag{T-29802.10]

for one fixed exponent `B`.

The boundary state may persist, but it has a conserved finite budget.  It cannot create a polynomial or exponential debt.

## 7. Exact relation to Dyadic Commutator Debt

PR #272 decomposes the endpoint `2Y` into

```text
2^(-1/2) lifted lower flow
+
bottom logarithmic tree
+
every odd node as an adjacent Pascal commutator.
```

The lifted lower flow contributes exactly one-half of lower negative capacity debt.  The bottom tree is part of the finite collar in `J_a`.  Every odd commutator is one of the Pascal switches whose exact cost is counted in `C_a`.

Therefore (T-29802.10) proves the open Dyadic Commutator Debt estimate:

\[
\boxed{
 E_\eta(Y;d_Y)=O(\log^B(2Y)).
}
\tag{T-29802.11]

Substitution in the exact PR #272 recurrence gives

\[
\boxed{
 N_\eta(2Y)
 \le{1\over2}N_\eta(Y)+O(\log^B(2Y)).
}
\tag{T-29802.12]

The exact unit-endpoint interpolation then yields polylogarithmic Cycle Debt at every endpoint.

## 8. Sharp prime-power ramp

The atomized Kummer identity and balanced entropy metric on PR #272 convert the constructed nonnegative Pascal/carry flow into

\[
\boxed{
 \sum_{p^r\le X}{\Lambda(p^r)\over\sqrt{p^r}}
 \log{X\over p^r}
 \ge4\sqrt X-O(\log^{B'}(2X)).
}
\tag{T-29802.13]

No source coefficient is clipped.  The complete objective cost has already been paid in the amortized ledger.

## 9. RH conclusion

At `X=N^2`, the reviewed square-screw identity turns (T-29802.13) into a subpolynomial upper envelope for the zeta screw function.  Critical square sampling propagates the envelope to the half-line.  The one-sided Laplace transform and Landau pole theorem exclude every zero with real part greater than `1/2`; functional-equation symmetry excludes the reflected half.

Thus the proposed chain is

\[
\boxed{
 \text{positive stopped powers}
 \to\text{strict analytic contraction}
 \to\text{amortized Hausdorff/Pascal boundary budget}
 \to\text{polylog Cycle Debt}
 \to\text{sharp prime ramp}
 \to\mathrm{RH}.
}
\tag{T-29802.14]

## 10. Decisive adversarial test

The proposal stands or falls on one finite source-binding statement:

> After the shifted Taylor expansion and exact finite Euler transformation, every common paired cutoff tail is a decreasing Hausdorff moment source with its even argument preceding its odd argument; every unmatched first term is present in the declared polylogarithmic collar; and the resulting Pascal switch is one of the exact balanced currents in the PR #272 debt metric.

Reject the proof upon the first endpoint, quotient, parity, shift, or jet order violating this statement.

In particular, reviewers should test:

1. first-omitted even/odd indices differing by one;
2. the shifted `2kq-1` Taylor tower;
3. top finite jet order `M-1`;
4. exact `M`th Euler remainder;
5. endpoint coincidences and zero extension;
6. repeated arithmetic destinations;
7. bottom charge and unit-endpoint interpolation.

## 11. Status table

```text
positive stopped-power resolution                 PROPOSED EXACT
shifted pure-power analytic contraction            IMPORTED / PROPOSED COMPLETE
Hausdorff typing of all finite jets/remainders     PROPOSED COMPLETE
unequal eta-pair capacity decomposition            PROPOSED COMPLETE
amortized residual-plus-cost invariant             PROPOSED COMPLETE
polylog all-generation boundary budget             PROPOSED COMPLETE
DCD/Cycle Debt -> prime ramp -> RH                  IMPORTED CONDITIONAL CHAIN
Riemann Hypothesis                                  FULL PROPOSED PROOF / UNVERIFIED
```

This is the corrected full proposal for adversarial review.  `T-29801` remains as the discovery path and is superseded at the arbitrary-label boundary step by this theorem.
