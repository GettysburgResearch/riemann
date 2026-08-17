# Parity-Completed Factor–67 Gluing and the Scalar Lorenz Frontier

## A hostile reconstruction of a two-row Mellin–Landau proposal for the Riemann hypothesis

**Scientific status:** rigorous reconstruction and exact conditional reduction; the uniform arithmetic producer is open. The Riemann Hypothesis is not proved.

## Abstract

We reconstruct the parity-resummed factor–67 route from the literal source to its reciprocal-zeta Mellin transform. Two mandatory adversarial inputs change the conclusion. First, target/scalar total positivity and Cauchy–Binet do not imply the global target capacity required by Hall. Second, exact matching of the scalar `5Q(2)+3Q(3)` generally decreases row two while increasing row three, so scalar exactness cannot be lifted to two-row feasibility. We prove the complete finite parity owner ledger, the exact completed-parity scalar Hall problem as a fractional-knapsack/Lorenz linear program with one-parameter dual, the precise scope of the compact-plus-MPFR terminal certificate, and the complete Mellin–Landau implication. The first unsupported arrow is the uniform completed-parity scalar Lorenz inequality `CPSL67`. Its dual already contains the conclusion-producing scalar sign, so this is exactly where zero-free-strip strength enters. The paper therefore gives a sharp conditional theorem and an honest downgrade of the claimed reserve closure.

## 1. Frozen genealogy and rule of reconstruction

The frozen base is PR #566 at

`2407b4ffe5024a2e3898922cf0b722d5cf69e496`.

The mandatory adversarial inputs are:

- PR #574 at `74fba7f3e55fa9a53d1eb814e5067f5011ef5e86`;
- PR #575 at `265c481ebd02807ab7d9a95cb0cf905a22c1876f`.

Repository claims are used only as provenance. Every conclusion-producing statement is restated here with its quantifiers, source category and coordinates. A certificate is credited only for the statement its interval or algebraic object actually proves.

## 2. Canonical rows and the unique scalar

For `j>=2`, put

```text
A_j=(j+1)/(j-1),
B_j=(j+1)(j-2)/(j(j-1)),
C_j=2/(j(j-1)).
```

For real `Y>=1`,

```text
Q_Y(j)= A_j j^(-1/2) log(Y/j) 1_(Y>=j)
       -B_j (j+1)^(-1/2) log(Y/(j+1)) 1_(Y>=j+1)
       +C_j sum_(m>=j+2) m^(-1/2)log(Y/m)1_(Y>=m).
```

Each hinge is continuous at activation because its logarithm vanishes there. The native Möbius row is

`c_X(j)=sum_(k<=X/j) mu(k)k^(-1/2)Q_(X/k)(j)`.

The scalar used by the direct Mellin consumer is

`R_X=5c_X(2)+3c_X(3)`.

Its unsieved dictionary is

```text
q_*(1)=0,
q_*(2)=15,
q_*(3)=6,
q_*(4)=3,
q_*(m)=6  (m>=5).
```

The dictionary is nonnegative. This simplifies the scalar terminal objective, but it does not erase history parity or imply two-row positivity.

After Möbius convolution,

```text
a_*(n)=6 1_(n=1)-6mu(n)
      +9 1_(2|n)mu(n/2)-3 1_(4|n)mu(n/4),
```

and

`R_X=sum_(n<=X)a_*(n)n^(-1/2)log(X/n)`.

## 3. Literal completed-parity source

Every squarefree `k` has the unique decomposition

`k=d p_1...p_t`,

where `d|P_61` and `67<=p_1<...<p_t`. The ordered history is `h=(p_1,...,p_t)`. If `S` swaps the parity channels, signed observation satisfies

`O(S^mP)=(-1)^mO(P)`.

Moving one rough prime from the source index into the history preserves the physical quotient and coefficient magnitude:

```text
(X/p)/(k/p)=X/k,
p^(-1/2)(k/p)^(-1/2)=k^(-1/2).
```

Thus every literal atom has one owner and retains activation `X/k`, magnitude `k^(-1/2)` and character `mu(d)(-1)^|h|=mu(k)`. At fixed `X`, the expansion is finite.

For active rough primes put

```text
r_i=p_i^(-1/2),
s_0=1,
s_i=product_(h<=i)(1-r_h),
lambda_i=r_i s_(i-1),
alpha_i=r_i lambda_i.
```

Then

```text
P=s_kP+sum_i lambda_i(P-r_iU_iP_i)+sum_i alpha_iU_iP_i
```

is exact in every linear coordinate. The identity is used in a free labelled source category. Oriented differences are never declared positive rows. Expanding atomwise, the negative `lambda_i r_i` and positive `alpha_i` child terms cancel, leaving the original coefficient exactly once. Hence, after completed parity and only then scalar observation, the root is exactly `R_X`, not a rough-lift surrogate.

## 4. Why leafwise Hall is impossible

At

```text
X=67*71*13=61841,
history=(67),
terminal=(p,y)=(71,13),
```

the certified complete `P_61` target difference in canonical orientation satisfies

`E_T-O_T>17`.

The incoming history is odd, so actual even capacity is `O_T` while actual odd demand is `E_T`. Canonical leafwise exact-target Hall would require `O_T>=E_T`, contradiction. Therefore terminal certificates may enter only as local canonical data inside a global completed-parity optimization.

## 5. Why Cauchy–Binet is insufficient

With terminal-by-source incidence `H` and terminal feature matrix `K`, the correct source-feature matrix is `H^T K`. After ordering sources by owner, incidence minors are nonnegative, and Cauchy–Binet transports terminal determinant signs.

It does not prove total target capacity. The exact finite countermodel

```text
H=I_2,
K=[[1,1],[2,4]]
```

has positive entries and determinant, but even target capacity `1` is smaller than odd demand `2`. Thus TP2 is compatible with Hall infeasibility.

## 6. Why scalar exactness cannot be lifted to two rows

Let

`rho(Y)=Q_Y(3)/Q_Y(2)`.

The exact analytic theorem of PR #575 shows that `rho` is nondecreasing. If an even coefficient is chosen to match the scalar

`5Q(2)+3Q(3)`

exactly against an odd demand, then

```text
Delta_2=-3bQ_o(2)(rho_e-rho_o)/(5+3rho_e),
Delta_3= 5bQ_o(2)(rho_e-rho_o)/(5+3rho_e).
```

Hence `5Delta_2+3Delta_3=0`, but generally `Delta_2<0<Delta_3`. The route is type-correct only if it stays in the scalar quotient all the way to the scalar Mellin transform.

## 7. The exact finite scalar Lorenz program

After full parity expansion at one endpoint, let even atoms have capacities `a_i`, target masses `t_i>0` and scalar coordinates `r_i`. Let the complete odd source have totals `(T_O,R_O)`.

We seek `0<=u_i<=a_i` such that

```text
sum_i t_i u_i=T_O,
sum_i r_i u_i>=R_O.
```

Define

`Phi_X(T)=max sum_i r_i u_i`

under the target equality. The source is feasible if and only if

`T_O<=T_E:=sum_i a_i t_i`

and

`R_O<=Phi_X(T_O)`.

Order atoms by `theta_i=r_i/t_i` decreasing. The optimizer saturates them in that order and uses at most one fractional atom. Equivalently,

`Phi_X(T)=min_lambda [lambda T+sum_i a_i(r_i-lambda t_i)_+]`.

The minimizing threshold is an exact finite separator when feasibility fails.

This theorem includes target-active scalar-zero atoms. For real `X`, the target `4sqrt(Y)-3` is nonzero already at `Y=1`, whereas row hinges may still vanish. Such atoms affect target capacity and cannot be discarded merely because they carry no scalar output.

Uniform validity of this Lorenz inequality for every sufficiently large real `X`, including both activation sides, is `CPSL67`.

## 8. What the terminal certificate proves

The compact theorem covers `py<166000` cell by cell. The MPFR theorem covers `py>=166000` with 256-bit directed primitive enclosures and outward arithmetic, all 65 rows and the full event census. The boundary `py=166000` belongs to the tail. In canonical parity, the complete grouped `P_61` Target–Lorenz optimizer has nonnegative row margins.

The certificate is true and useful, but it does not reverse orientation after odd history, prove global target capacity, or prove `CPSL67`.

## 9. Independent finite reconstruction

The included verifier reconstructs:

- the `5:3` dictionary and Möbius coefficients;
- parity, activation and magnitude invariants;
- the formal causal coefficient cancellation;
- the odd-history target witness;
- the R-97300 scalar/row tradeoff;
- the exact fractional-knapsack primal and dual on rational fixtures;
- literal finite target/scalar atom tables over a range of endpoints;
- the Mellin numerator factorization;
- hostile mutations at each load-bearing interface.

The finite diagnostic is falsification only. It does not prove uniform `CPSL67` or RH.

## 10. Complete scalar Mellin transform

The coefficient bound `|a_*(n)|<=24` gives

`|R_X|<=60sqrt(X)(1+log X)`.

Thus the Mellin integral is absolutely convergent for `Re s>1/2`. With `z=s+1/2`, the substitution `X=kY` contributes `k^(-s-1/2)`, and Fubini gives

```text
int_1^infty R_X X^(-s-1)dX
 = 6/s^2
   -3(1-2^(-z))(2-2^(-z))/(s^2 zeta(z)).
```

The `6/s^2` term is the unit source. The continuation is analytic at every positive real `s`; at `z=1`, reciprocal zeta vanishes. The numerator is zero-free in `Re z>0` because `|2^(-z)|<1` there. A zeta zero of any multiplicity with real part greater than one half therefore creates a nonremovable pole in `Re s>0`.

## 11. Landau and the exact conditional conclusion

If `R_X>=0` eventually, put `X=e^t`. After discarding a compact initial interval, the Mellin transform is the Laplace transform of a nonnegative locally integrable function plus an entire correction. Landau’s theorem forces its real abscissa of convergence to be a singularity. Since the continuation is analytic at every positive real point, the abscissa is at most zero, so the defining transform is holomorphic throughout `Re s>0`.

An off-line zeta zero would create a pole there, contradiction. Functional-equation symmetry then yields RH.

Therefore

`CPSL67 => R_X>=0 eventually => RH`.

## 12. Exact status and strength location

The manuscript proves every interface downstream of `CPSL67` and every finite structural statement upstream of it. It does not prove `CPSL67`.

The zero-free-strip strength lives exactly in the uniform scalar Lorenz inequality. At dual threshold `lambda=0`, the required inequality already contains the global scalar sign. It is not supplied by local certificates, determinant signs, parity algebra or finite scans.

```text
completed-parity source ledger          PROVED EXACT
finite Lorenz primal/dual               PROVED EXACT
terminal certificate scope              RECONSTRUCTED EXACT
scalar type discipline                  PROVED EXACT
Mellin-Landau implication               PROVED EXACT CONDITIONAL
uniform CPSL67                          OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVEN
```

## 13. Response to PR #574 and PR #575

| Finding | Disposition |
|---|---|
| Correct product is `H^T K` | Independently reproved |
| Owner ordering required for incidence minors | Accepted and incorporated |
| TP2/Cauchy–Binet does not imply global Hall | Accepted; old implication withdrawn |
| Odd-history target witness is binding | Reproduced and used as mandatory firewall |
| Completed-parity owner ledger is finite | Independently reproved |
| `Q_3/Q_2` is monotone | Accepted; only used for the scalar/row firewall |
| Scalar exactness does not lift to two rows | Accepted; route kept scalar |
| Finite scalar Lorenz LP and dual | Independently reproved |
| Uniform CPSL67 remains open | Accepted as the first unsupported arrow |

## 14. Final statement

This is a complete standalone reconstruction and an exact downgrade, not a proof of the Riemann Hypothesis. Its strongest honest theorem is the source-complete equivalence between completed-parity scalar feasibility and a finite Lorenz inequality, together with the complete implication of the uniform inequality to RH.
