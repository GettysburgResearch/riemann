# T-27902 — Complete Endpoint Stability: a Selberg-compatible full RH proposal

Claim ID: `T-27902`  
Title: A sublogarithmic complete von-Mangoldt endpoint scalar proves RH directly and, through the prime-square reserve, forces zero WSTS debt  
Status: **FULL CONDITIONAL PROPOSAL — ONE EXPLICIT COMPLETE-SOURCE RATE THEOREM OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-27901`--`L-27906`; PR #241 reflected block; PR #216 prime-only layer audit; PR #276 WSTS consumer  
Scope: full Riemann Hypothesis; RH is not claimed proved

## 1. Final source correction

The first version of the dyadic sign proposal ended at the ordinary-prime sign `EPD`. `L-27905` shows that this sign has two distinct components:

```text
complete von-Mangoldt endpoint oscillation;
minus a deterministic c log X proper-power reserve.
```

The complete source is the correct proof-facing object because it is compatible with the exact Selberg and reflected identities.

Define

\[
\boxed{
\mathcal A_\Lambda(X)
=\sum_{q=p^a\le X}\Lambda(q)
 [v_q(\dot b_X)-q^{-1/2}],}
\tag{T-27902.1}

where

\[
\dot b_X(m)=2\sqrt m(1-\sqrt{m/X})\mathbf1_{m\le X}.
\]

The sole new theorem is

\[
\boxed{
\mathrm{CEP}:\qquad
\mathcal A_\Lambda(X)=o(\log X).}
\tag{T-27902.2}

## 2. Exact scalar formula

The von Mangoldt divisor identity gives

\[
\boxed{
\begin{aligned}
\mathcal A_\Lambda(X)
={}&\sum_{m=2}^{X}
2\sqrt m(1-\sqrt{m/X})
\log{m\over m-1}\\
&-\sum_{n\le X}{\Lambda(n)\over\sqrt n}.
\end{aligned}}
\tag{T-27902.3}

Thus CEP is a single explicit comparison between a smooth endpoint benchmark and the complete weighted Chebyshev function. It contains no LP existence statement, tail maximum, or packet family.

## 3. Direct Mellin consumer

`L-27906` proves

\[
\boxed{
\int_1^\infty
\mathcal A_\Lambda(X)X^{-z-1}dX
={\Phi(z)\over z(z+1/2)}
+{1\over z}{\zeta'\over\zeta}(z+1/2),}
\tag{T-27902.4}

where

\[
\Phi(z)=\zeta(z+1/2)-1+R(z)
\]

and `R` is holomorphic for `Re z>-1/2`.

A zero `rho` with `Re rho>1/2` creates the genuine residue

\[
{m_\rho\over\rho-1/2}.
\]

CEP makes the left side holomorphic throughout `Re z>0`, so it excludes every such zero. Functional-equation symmetry gives

\[
\boxed{
\mathrm{CEP}\Longrightarrow\mathrm{RH}.}
\tag{T-27902.5}

## 4. Prime-square reserve and the elementary consumer

`L-27905` proves

\[
\boxed{
\mathcal A_\Lambda(X)-\mathcal A_{\mathbb P}(X)
\ge c_{\rm pp}\log X-O(1),
\qquad c_{\rm pp}>0.}
\tag{T-27902.6}

Therefore CEP gives

\[
\mathcal A_{\mathbb P}(X)<0
\]

cofinally. This is Endpoint Prime Domination, so `Delta_X` is nonincreasing.

`L-27904` supplies finite dyadic one-crossing and `L-27903` gives

\[
\mathcal B_X
=[\Delta_X-\Delta_{\lfloor X/2\rfloor}]_+.
\]

Hence CEP also yields

\[
\boxed{
\mathcal B_X=0}
\tag{T-27902.7}

cofinally, and PR #276 again gives RH.

Thus CEP has two independent proof consumers:

```text
Mellin pole exclusion;
prime-square reserve -> EPD -> zero WSTS debt.
```

## 5. Why complete primes are structurally preferable

The complete source retains the prime squares which PR #216 identifies as the dominant cancellation partner of the prime layer. Removing them creates a boundary pole that must be canceled by an external difference.

For CEP:

- the source is exactly `Lambda`, not the analytically continued ordinary-prime series;
- the generalized Selberg coefficient identity applies directly;
- the independent-frequency Hermitian square of PR #241 is correctly typed;
- the endpoint kernel is explicit;
- the prime-square layer supplies a strict logarithmic reserve for the ordinary-prime consumer.

The complete scalar is not one-signed; finite positive excursions are retained as mutations. The theorem asks only for sublogarithmic growth.

## 6. Proposed reflected completion

The preferred analytic route is an **Endpoint Reflected Selberg Certificate (`ERSC`)**.

A production object must:

1. insert the endpoint source `dot b_X` into the exact independent-frequency physical block;
2. use the complete von Mangoldt sequence and retain every prime-power layer;
3. form the generalized Selberg identity before any absolute value;
4. isolate the explicit benchmark term in (T-27902.3);
5. retain every endpoint and compact-window commutator;
6. prove that the remaining boundary scalar is `o(log X)`;
7. replay the prime-square reserve and the `2/3` Mertens mutation.

A sufficient output is

\[
\mathcal A_\Lambda(X)
=O((\log X)^{1-\delta})
\]

for one fixed `delta>0`, or any explicit `o(log X)` modulus.

### Candidate Selberg ledger

Use

\[
\mu*(1\log^2)=\Lambda\log+\Lambda*\Lambda
\]

or the reflected two-frequency form. The quadratic term must be retained as a complete Hermitian prime-power square. The endpoint benchmark is then the linear adjoint term; the production question is whether the square and boundary commutators leave only sublogarithmic debt.

### Candidate explicit-formula ledger

Equation (T-27902.4) shows the zero contribution has coefficient `1/(rho-1/2)`. On the critical line this is an oscillatory boundary phase, whereas an off-line zero has polynomial growth. A source-specific symmetric summation or de Branges/Weil positivity theorem controlling the critical-line phase by `o(log X)` would also prove CEP.

## 7. Mandatory mutations

Reject a claimed CEP proof if it:

```text
M1  removes prime squares before the Selberg square is formed;
M2  claims A_Lambda is always nonpositive;
M3  drops the endpoint benchmark Phi(z);
M4  uses zeta'/zeta with the wrong residue sign;
M5  cancels an off-line pole with an undeclared numerator;
M6  proves only O(log X) with no constant below c_pp;
M7  takes absolute values before reflected recombination;
M8  uses a one-frequency global integral as a physical block;
M9  loses the m=1 or endpoint commutator;
M10 omits the prime-square reserve or 2/3 shell mutation;
M11 promotes finite boundedness to CEP;
M12 claims RH while CEP remains assumed.
```

## 8. Exact status

```text
continuum and finite dyadic one-crossing      PROPOSED COMPLETE
WSTS tail collapse                             PROPOSED COMPLETE
proper prime-power logarithmic reserve         PROPOSED COMPLETE
complete endpoint scalar and Mellin firewall   PROPOSED COMPLETE
Complete Endpoint Stability CEP                OPEN / RH-BEARING
CEP -> direct Mellin RH                        PROPOSED COMPLETE
CEP -> EPD -> zero WSTS debt -> RH             PROPOSED COMPLETE
Riemann Hypothesis                             UNPROVED
```

This is now the preferred full-problem formulation on PR #291. It has one complete-source rate theorem rather than an ordinary-prime transport existence theorem.
