# O-91312 — The corrected factor-54 frontier reduces to one live row-provenance/Hall-entry theorem

Claim ID: `O-91312`  
Status: **CROSS-STACK SYNTHESIS / EXACT CONDITIONAL REDUCTION — NOT AN RH CLAIM**  
Created: 2026-08-13  
Frozen direct-row main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Frozen hardening input: PR `#424` at `20b6cc5c4b9d4c9191a83e1f7fcf24c73dd7e7bb`  
Depends on: `R-91310`; `L-91352/L-91353`; `L-91554/L-91559/L-91560`; review PR `#431`  
RH status: **unproved**

## 1. Three formerly entangled obligations

The direct-Euler factor-54 proposal treated the remaining frontier as one large
statement involving:

```text
arithmetic score;
positive row realization;
radix-four child placement;
terminal debt;
branch provenance.
```

The live repository now separates these obligations.

### Raw arithmetic score

`R-91310` refutes the declared scalar score surplus.  The correct literal row
entropy is nevertheless favorable.  Two independent proofs give

\[
 \mathcal E_{P,p}(py)>\mathfrak T_{Pp}(py),
 \qquad
 \mathcal E_{P,p}(py)>\mathfrak S_{Pp}(py)
 \tag{O-91312.1}
\]

uniformly for `P=P_79`, `p>=83`, `1<=y<83`.  The quantitative margins are
`(4/15)sqrt(py)` in `L-91352` and `86/9` in `L-91353`.

### Physical child placement

On the hardening branch, `L-91559` proves that positive canonical component
packets admit the exact identity embedding

\[
 d_X=a(Q_X-Q_Y)+d_Y,
 \tag{O-91312.2}
\]

which is coefficientwise nonnegative, coefficient-one in entropy, and feasible
in every ordinary and radix-four integer column.  No affine Pascal lift,
colored fiber or fractional column is needed.

### Terminal source debt

`L-91554` proves that on the fixed finite Euler support every source coefficient
has one unique terminal quotient and pays at most once.  The complete
unnormalized all-depth deficit is bounded by absolute constants:

\[
 E_{\rm source}(P_{79})<5600,
 \qquad
 E_{\rm source}(P_{61})<3600.
 \tag{O-91312.3}
\]

Thus the score, physical-placement and terminal-summability problems each have a
separate exact solution at their stated frozen scopes.

## 2. What is still missing

The unresolved joint is not another analytic inequality.  It is an exact
source-typing theorem on the **live one-prime input**.

> **Live Row-Provenance Theorem (`LRPT`).**  Starting from the exact live
> `P_79` one-prime residual-plus-child packet, construct positive source
> measures `c_s,c_h`, positive target-null row bonuses `B_s,B_h`, and actual
> scalar child coefficients `omega_s,omega_h` such that:
>
> \[
> T(c_s)+T(c_h)=T_{\rm parent},
> \tag{O-91312.4}
> \]
>
> \[
> R_{\rm live,parent}
> =R_s(c_s)+R_h(c_h)+B_s+B_h
> \tag{O-91312.5}
> \]
>
> coefficientwise in every exact finite row, with the literal child coefficient
> `r=p^{-1/2}` retained in the residual-plus-child cocycle;
>
> \[
> c_s(d),c_h(d)\in[0,1]
> \quad(d\mid P_{79}),
> \tag{O-91312.6}
> \]
>
> \[
> \omega_s,\omega_h\ge0,
> \qquad
> \omega_s+\omega_h\le1;
> \tag{O-91312.7}
> \]
>
> and every Hall edge obeys the **actual parent causal cutoff** before its target,
> score or row contribution is evaluated.

The theorem must be proved directly from the live finite source definition.  An
abstract target equality, a pointwise source partition or a Hall checker that
uses nodes beyond `py` does not satisfy `LRPT`.

## 3. Why `LRPT` is sufficient

Assume `LRPT` at one frozen live input.

1. Equation (O-91312.5) makes the Hall step an exact identity of literal row
   vectors, so entropy is preserved by linearity before any capacity estimate.
2. `L-91559` replaces arbitrary child packings by identity embeddings in the
   same physical row space, preserving ordinary and radix-four feasibility and
   coefficient-one entropy.
3. `L-91554` bounds the entire terminal frontier debt sourcewise by one absolute
   constant, with no multiplication by the root target amplitude or the number
   of generations.
4. `L-91352/L-91353` supply a strictly favorable raw arithmetic score budget, so
   no refuted declared-score orientation is needed.
5. The scalar subprobability weights in (O-91312.7) then feed the actual-packet
   branching consumer without the invalid passage from pointwise source mass to
   an unrelated normalized loss.

The resulting recurrence has the form

\[
 \mathfrak L_X
 \le C+
 \sum_b\omega_b\mathfrak L_{X_b},
 \qquad
 \sum_b\omega_b\le1,
 \qquad
 X_b\le cX+C_0,
 \tag{O-91312.8}
\]

and therefore gives `mathfrak L_X=O(log X)` after the source-pinned finite base
and loss-to-RH consumer are independently reconstructed.

## 4. Why current files do not yet prove `LRPT`

Review PR `#431` gives an exact obstruction to the current low-prefix Hall
certificate: the displayed formula includes formal capacities above the parent
support `py`.  It also identifies three further provenance gaps:

```text
hidden hazard score is not automatically the score of an r-scaled child;
pointwise source fractions do not automatically become scalar signed-loss weights;
noninherited frontier rows are outside the scope of L-91346.
```

The frozen hardening theorem `L-91560` is a promising exact three-ledger cocycle,
and `L-91545` is the correct form of a target-Hall row identity, but both must be
replayed from the moving live `P_61/P_79` source with the corrected causal
support.  Their summaries are not a substitute for `LRPT`.

## 5. Finite attack plan

`LRPT` is finite-interface and can be attacked without a new global asymptotic
theorem:

1. enumerate the live parent source nodes `d|P_79` and the active child cutoff
   `d<=y`;
2. retain parent activation `d<=py` in every Hall margin;
3. solve one target-mass flow with survival/hazard labels and literal row
   coefficients `1-r^2,r^2`;
4. certify score superordination and normalized-row monotonicity on every real
   activation cell;
5. export the exact positive residual coefficients and row bonuses;
6. verify the residual-plus-child cocycle, including `r`, coefficientwise;
7. feed the exported packet unchanged into `L-91559` and the sourcewise terminal
   telescope.

The output should be one hash-locked packet containing the flow, source
coefficients, row-bonus vectors, branch target weights and final integer-column
capacity replay.  Separate scalar checkers are insufficient.

## 6. Boundary

```text
raw arithmetic physical entropy surplus           PROVED / TWO ROUTES
nested identity physical embedding                 PROVED AT FROZEN HARDENING INPUT
finite-Euler all-depth terminal debt               PROVED AT FROZEN HARDENING INPUT
live causal Hall/source row provenance             OPEN / LRPT
source-pinned finite base and loss consumer        RECONSTRUCTION REQUIRED
corrected factor-54 recurrence                     CONDITIONAL ON LRPT
Riemann Hypothesis                                 UNPROVEN
```
