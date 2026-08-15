# Independent frozen-head review of PR #497 at `bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74`

## Freeze

```text
repository:       gfreund123/riemann
review cutoff:    2026-08-15T18:55:44Z
proposal PR:      #497
proposal base:    research/gpt56-pro/91381-euler-shell-recovery
base SHA:         9e2ae6d26a7920055e1f11327dc0ddeb7b855c61
proposal branch:  research/gpt56-pro/93600-target-lorenz-complete-successor
reviewed head:    bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74
review branch:    review/pr497-target-lorenz-frozen-bd2a3c32-20260815
```

This review treats PR #497 as its own Target-Lorenz construction. PR #495's Volterra fibre is not imported and is not counted as confirmation.

The retained compact and tail artifacts were inspected. The 702,511,095-cell compact sweep and the 51,118,080-record tail sweep were not rerun.

## Executive verdict

```text
mathematical type:  candidate-complete Target-Lorenz native-root proposal
review verdict:     UNPROVEN / GAP
RH status:          UNPROVEN
```

Two distinct boundaries must be recorded.

### First proof-object break

`L-93601` reduces the real tail to a finite exact-event sweep correctly, but the retained generator evaluates all transcendental quantities and prefix sums with ordinary `long double`. It provides no outward-rounding contract, no `LDBL_MANT_DIG` or platform assertion, no accumulated error bound, and no interval enclosure of the reported minima. The Python wrapper checks the numbers printed by that program; it does not certify them.

Thus the tail statement is **computationally supported but not exact-certified** at the repository's directed-proof standard.

### First structural break even granting the tail theorem

`L-93603.2` introduces an endpoint fibre `\mathcal S_{X,s}` and a leaf expansion

\[
\mathcal S_{X,s}
=
\sum_{\ell}\omega_{s,\ell}(E_{s,\ell}-O_{s,\ell}),
\]

but never defines the initial fibre packet in the native endpoint normalization or proves its identification with the fibre integrated against

\[
d\mu_X(s)=\frac{2L(X/s)}s\,ds.
\]

`L-91362` decomposes an already specified paired packet `\mathbf P_1^{(a)}(Z)`, and `L-91650` decomposes an already specified packet family. Neither theorem supplies the missing map from the endpoint-frame fibre to that discrete source tree. The path products `\omega_{s,\ell}` are concrete only after this initial packet, its parameter `a`, endpoint `Z`, and source coefficients have been supplied.

The endpoint fixture in `X-93601` uses two fabricated rational leaf examples; it does not instantiate the actual `P_61` leaves or their path weights.

Therefore the proposed common parent is still conditional on a missing endpoint-fibre-to-leaf identity.

# Reconstruction

## 1. Euler-ramp remainder: `L-93600`

For

\[
S(Y)=\sum_{n\le Y}n^{-1/2}\log(Y/n),
\]

the Hurwitz-zeta decomposition is correct:

\[
S(Y)=
\log Y\,[\zeta(1/2)-\zeta(1/2,a)]
+\zeta'(1/2)-\partial_s\zeta(s,a)|_{s=1/2},
\qquad a=\lfloor Y\rfloor+1.
\]

Stopping Euler-Maclaurin after `B_2`, differentiating, and writing
`h=\log(a/Y)` gives the stated remainder normal form. The elementary terms have scaled absolute bound

\[
2+1+\frac1{12}=\frac{37}{12},
\]

and the differentiated Bernoulli remainder is bounded by

\[
\frac19+\frac{\log2}{24}+\frac1{36}<0.168.
\]

Their sum is below `5`. The component-row remainder obtains the correct factor

\[
\frac{10}{j(j-1)}Y^{-3/2}.
\]

No sign error was found in the zeta derivative, the `h` terms, or the component-row constants.

**Disposition:** `VERIFIED`.

## 2. Tail envelope and row-66 minimum: `L-93601`

The generator's symbolic architecture reconstructs:

1. target prefixes change at `x=d`;
2. row strip state changes at `x=jd`;
3. bulk row state changes at `x=(j+1)d`;
4. on each event interval the parent lower envelope has the form
   \[
   At^2+Bt\log t+Ct+D\log t+E+Ft^{-2}+Gt^{-3};
   \]
5. the termwise derivative lower bound implemented by `der_lb` has the correct endpoint orientation;
6. the even first strip is omitted from a lower row bound and the odd strip is charged by its exact maximum;
7. the bulk error signs and the factors `5 C_j D_\pm/x^{3/2}` are correct;
8. the child correction is a conservative absolute cross-term bound and is nonincreasing between events;
9. after all prefixes are complete, the `t^2` and bare `log t` coefficients cancel algebraically, reducing the final interval to the stated polynomial second-derivative test.

The retained output reports

```text
parent minimum:       79.237289759903788... at x=166000, j=66
full minimum:         26.786236008153155... at x=166000, j=66
parent derivative:    0.2397174267... minimum
rows swept:           65
event records:        51,118,080
```

This supports the stated row-66 extremality among the swept rows.

### Certificate limitation

The event ordering is exact `uint128`, but the proof-relevant values are not directed:

```text
hard-coded decimal zeta constants;
conversion of large integers to long double;
naive long-double prefix sums;
long-double logarithms and square roots;
long-double determinant and derivative evaluation.
```

No theorem in the packet bounds these errors. The claimed “one-unit reserve” is also not literally present in the final margin:

\[
26.786236\ldots-26=0.786236\ldots<1.
\]

This is not a counterexample to the tail inequality. It is a proof-object gap.

**Disposition:** `UNPROVEN / COMPUTATIONALLY SUPPORTED`; the analytic/event reduction is `VERIFIED WITH FIXES`.

## 3. Exact compact/tail coverage: `L-93602`

The frozen compact theorem has domain

\[
py<166000
\]

for every real admissible `(p,y)` and every row `2,...,66`. The new tail statement has domain

\[
py\ge166000.
\]

These domains meet exactly and omit no real boundary cell. The compact retained certificate records 702,511,095 cells, four dependency exceptions, and directed positive margins. Its checker uses explicit perturbation budgets and exact rational square-root bounds for the parity-prefix reserve.

Therefore, conditional on the tail theorem, `L-93602` correctly closes all rows `2,...,66`. Rows beyond `66` are separately delegated to the frozen child-inactive finite-Euler theorem rather than silently extrapolated.

**Disposition:** `VERIFIED CONDITIONAL ON L-93601`.

## 4. Concrete Target-Lorenz coefficients at a supplied leaf

For a supplied leaf with ordered even atoms `e_1<...<e_n`, target weights `t_i>0`, and odd target demand `M`, the Target-Lorenz coefficients are completely explicit:

\[
u_i=1\quad(i<c),\qquad
u_c=\frac{M-\sum_{i<c}t_i}{t_c},\qquad
u_i=0\quad(i>c).
\]

`L-91720` correctly proves that this one coefficient vector simultaneously minimizes score cost and maximizes every ordered row. `L-91780` correctly reduces row feasibility to the proportional determinant. Once the determinant is nonnegative,

\[
\nu=E-U\ge0,
\qquad
B_j=R_j(U)-O_R^{(j)}\ge0,
\]

and

\[
R_j(\nu)+B_j=E_R^{(j)}-O_R^{(j)}.
\]

This leafwise algebra is exact.

**Disposition:** `VERIFIED ON AN ACTUAL SUPPLIED LEAF`.

## 5. First structural broken arrow: endpoint fibre to actual leaves

The missing object is not the greedy coefficient formula. It is the initial leaf ledger to which that formula is applied.

`L-93603` does not specify:

```text
the exact endpoint-frame fibre packet S_(X,s);
the parameter a and endpoint Z in P_1^(a)(Z);
the coefficient of every root source occurrence;
the map from that packet to the positive infinitesimal endpoint row;
the target, score, ordinary, detail and child-boundary coordinates
of each resulting leaf in one native normalization.
```

The displayed path weight

\[
\omega_{s,\ell}
\]

is described only as a product of stopping and causal coefficients. That is an exact recursive rule **after** the root occurrence and its coefficient are known; it is not the missing root-to-tree identification.

There is also a typed-vector gap. The file defines

\[
g_{s,\ell}=R(\nu_{s,\ell})+B_{s,\ell}
\]

as a nonnegative row and proves a row identity. To substitute it into the product-cone Fubini theorem, one must define one packet carrying target, declared/literal score, every row, ordinary responses, boundary coordinates, and ownership with the same source coefficients. In particular, the row bonus `B` is not itself the positive source submeasure `\nu`. The necessary typed adapter is not written.

Thus formula

\[
\Lambda_X^{\rm TL}
=
\int_{I_X}\sum_\ell
\omega_{s,\ell}g_{s,\ell}\,d\mu_X(s)
\]

is explicit as notation but not yet an instantiated native packet identity.

**Disposition:** `UNPROVEN / GAP` at `L-93603.2--5`.

### Density provenance

The interval `I_X` needs `L(x)>0` for `1\le x<67`. The cited `L-91107` only proves positivity through `c_0^{-1}\approx54.2`. The factor-67 theorem exists as `L-91692` on a sibling branch, but it is absent from the frozen PR #497 tree and lock. A direct 66-cell check gives the same positive minimum

```text
0.3186174007... on the cell 32 <= x < 33,
```

so this is repairable provenance, not a negative witness.

## 6. Common-parent construction

If one adds the missing exact fibre-to-tree identity and the typed leaf packet, then the remaining construction is sound:

- the stopping/casual tree has finite depth because each recursive endpoint falls by at least `67`;
- unique least rough prime gives one owner;
- leafwise Target-Lorenz uses one coefficient vector in every row;
- positive Tonelli preserves nonnegativity;
- all actual child responses may remain internal colours;
- one global pushforward and one positive quantizer may be applied after summation.

Without that added identity, the common parent is not derived from the frozen endpoint source.

**Disposition:** `CONDITIONAL IMPLICATION`.

## 7. Every physical column, including `q<K`: `L-93604`

The imported retained-cell theorem `L-91733` genuinely addresses the small-column range. Its carry identity is

\[
v_q(E_X^I)=\sum_{jq\in I_X}\varepsilon_X(jq),
\]

so for every `q>=2`,

\[
|\mathcal D_4v_q(C_X-E_X^I)|
<
\frac{971}{4q\sqrt K},
\qquad
\frac{|e_X(q)|}{\Omega_X(q)}
<
\frac{129}{\sqrt K}.
\]

No cutoff atom is created, and `2<=q<K` is included.

The thinning algebra is exact:

\[
\tau_K\left(1+\frac{129}{\sqrt K}\right)
=
\frac{\sqrt K+129}{\sqrt K+130}
<1.
\]

The terminal reserve `581X^{-3/2}` and triangular zero response above support then complete detail feasibility; positive radix-four inversion gives ordinary feasibility.

This chain is valid **if** the ideal positive common parent uses at most the native packet before the signed comparison is added. That antecedent is exactly what `L-93603` has not yet established.

**Disposition:** `VERIFIED CONDITIONAL ON L-93603`.

## 8. Direct native endpoint cost: `L-93605`, `T-93600`, `T-93601`

The native currency is correct:

\[
J_\Lambda(X)-\mathcal H(d_X)
=
\langle Y_4,\Omega_X-\Xi(d_X)\rangle.
\]

The charge arithmetic reconstructs:

```text
thinning                    <12012
nonterminal comparison      <4
terminal comparison         <48972
positive omissions          <1
port/base                    0
total                        <60989<61000
```

No estimate of `J_\Lambda(X)-4\sqrt X` is used. The endpoint consumer has the correct one-sided orientation.

These are valid downstream implications after a genuine feasible row exists. They do not establish the missing common parent or harden the tail sweep.

**Disposition:** `VERIFIED CONDITIONAL`; complete theorem `UNPROVEN`.

# Computational-certificate audit

## Compact certificate

```text
classification:          PASS_TARGET_LORENZ_COMPACT_PROPORTIONAL_AVLT
activation-row cells:    702,511,095
direct coarse passes:    702,511,091
dependency exceptions:   4
minimum certified lower: >0.001
```

The checker records explicit perturbation caps and exact rational square-root enclosures for the parity-prefix reserve. It was inspected, not rerun.

## Tail certificate

```text
classification:          PASS_COMPLETE_TARGET_LORENZ_TAIL_AVLT
proof object:            e30b0e4e08802002b160ddfaaefebb4b6ab8aa5a3562785fc854cc93f4101aa0
```

It exhausts the intended event list but is not a directed numerical certificate for the reasons above.

## Native endpoint fixture

```text
classification:          PASS_TARGET_LORENZ_TWO_LEDGER_NATIVE_ENDPOINT_PACKET
proof object:            7207cbe3b241173e02d3c9a346056df861801522e4633675ecc2740711f96f02
```

This checker uses two synthetic rational leaf fixtures and boolean type declarations. It validates abstract Target-Lorenz/Fubini algebra, reserve arithmetic, and hostile schema mutations. It does not generate the actual stopped-leaf coefficients, actual common parent, or native endpoint row.

# Claim status

```text
L-93600  VERIFIED
L-93601  UNPROVEN / COMPUTATIONALLY SUPPORTED
L-93602  VERIFIED CONDITIONAL ON L-93601
L-93603  UNPROVEN / GAP
L-93604  VERIFIED CONDITIONAL ON L-93603
L-93605  VERIFIED CONDITIONAL ON L-93603/L-93604
T-93600  UNPROVEN / GAP
T-93601  CONDITIONAL ENDPOINT COMPOSITION ONLY
X-93600  EXHAUSTIVE EVENT REGRESSION, NOT DIRECTED CERTIFICATE
X-93601  SYNTHETIC INTERFACE REGRESSION
RH        UNPROVEN
```

# Shortest serious repair

1. Replace the tail `long double` evaluation by outward interval arithmetic or publish a rigorous platform-pinned total error bound below the available `0.786...` margin.
2. Define the actual endpoint fibre packet `\mathcal S_{X,s}` in all native coordinates.
3. Give the exact root occurrence coefficients and the map from the endpoint frame to the `P_61`/causal tree.
4. Emit the actual leaf list or a generator whose output is authenticated to that fibre identity.
5. Define the full typed Target-Lorenz leaf packet, not only its row.
6. Replay the common-parent identity on those actual weights.
7. Then apply the already reconstructed `q<K`, terminal, `Y_4`, and endpoint-consumer chain.

PR #495 cannot be used to fill item 2: it is a different Volterra packet family and its causal child interface fails independently.
