# O-91312 — The corrected factor-54 frontier reduces to one live row-provenance/flow-export theorem

Claim ID: `O-91312`  
Status: **CROSS-STACK SYNTHESIS / EXACT CONDITIONAL REDUCTION — NOT AN RH CLAIM**  
Created: 2026-08-13  
Updated: 2026-08-13 after causal Hall repair `L-91354/X-91312`  
Frozen direct-row main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Frozen hardening input: PR `#424` at `20b6cc5c4b9d4c9191a83e1f7fcf24c73dd7e7bb`  
Depends on: `R-91310`; `L-91352/L-91353/L-91354`; `L-91554/L-91559/L-91560`; review PR `#431`  
RH status: **unproved**

## 1. Four formerly entangled obligations

The direct-Euler factor-54 proposal treated the remaining frontier as one large
statement involving:

```text
arithmetic score;
finite Hall positivity;
positive row realization and provenance;
radix-four child placement;
terminal debt.
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

### True causal Hall positivity

Review PR `#431` correctly observed that `L-91350.2` inserted formal parent
capacities above `py`.  `L-91354/X-91312` restores the cutoff and proves

\[
 \boxed{
 \mathcal H_{4,t}^{(8)}(p,y)>\frac74,
 \qquad
 \mathcal H_{5,t}^{(8)}(p,y)>\frac32
 }
 \tag{O-91312.2}
\]

for every prime `p>=83`, every real `1<=y<83`, and every active sign-demand
threshold `t<4096`.  The certificate checks `18,180,604` directed inequalities,
including both sides of every missing parent activation.

Thus Hall **sign feasibility** is no longer part of the open gate.

### Physical child placement

On the hardening branch, `L-91559` proves that positive canonical component
packets admit the exact identity embedding

\[
 d_X=a(Q_X-Q_Y)+d_Y,
 \tag{O-91312.3}
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
 \tag{O-91312.4}
\]

Thus score, Hall sign, physical placement and terminal summability each have a
separate exact solution at their stated frozen scopes.

## 2. Exact remaining theorem

The unresolved joint is constructive source typing on the **live one-prime
input**.

> **Live Row-Provenance Theorem (`LRPT`).**  Starting from the exact live
> `P_79` one-prime residual-plus-child packet and the causal capacities certified
> by `L-91354`, export positive source measures `c_s,c_h`, positive target-null
> row bonuses `B_s,B_h`, and actual scalar child coefficients
> `omega_s,omega_h` such that:
>
> \[
> T(c_s)+T(c_h)=T_{\rm parent},
> \tag{O-91312.5}
> \]
>
> \[
> R_{\rm live,parent}
> =R_s(c_s)+R_h(c_h)+B_s+B_h
> \tag{O-91312.6}
> \]
>
> coefficientwise in every exact finite row, with the literal child coefficient
> `r=p^{-1/2}` retained in the residual-plus-child cocycle;
>
> \[
> c_s(d),c_h(d)\in[0,1]
> \quad(d\mid P_{79}),
> \tag{O-91312.7}
> \]
>
> \[
> \omega_s,\omega_h\ge0,
> \qquad
> \omega_s+\omega_h\le1;
> \tag{O-91312.8}
> \]
>
> the exported flow uses only the true parent capacities `d<=py`; and the score
> superordination and normalized-row lift are verified for that **same** flow.

`L-91354` proves that a finite Hall flow exists separately in target and declared
score units.  `LRPT` must export one source-labelled target flow and prove that
its score and row bonuses have the required signs.  Separate existence
certificates are not a provenance packet.

## 3. Why `LRPT` is sufficient

Assume `LRPT` at one frozen live input.

1. Equation (O-91312.6) makes the Hall step an exact identity of literal row
   vectors, so entropy is preserved by linearity before any capacity estimate.
2. `L-91559` replaces arbitrary child packings by identity embeddings in the
   same physical row space, preserving ordinary and radix-four feasibility and
   coefficient-one entropy.
3. `L-91554` bounds the entire terminal frontier debt sourcewise by one absolute
   constant, with no multiplication by the root target amplitude or the number
   of generations.
4. `L-91352/L-91353` supply a strictly favorable raw arithmetic score budget, so
   no refuted declared-score orientation is needed.
5. The scalar subprobability weights in (O-91312.8) then feed the actual-packet
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
 \tag{O-91312.9}
\]

and therefore gives `mathfrak L_X=O(log X)` after the source-pinned finite base
and loss-to-RH consumer are independently reconstructed.

## 4. Surviving hostile-review obligations

The causal-support objection in PR `#431` is closed by `L-91354`.  Three
provenance objections survive:

```text
hidden hazard score is not automatically the score of an r-scaled child;
pointwise source fractions do not automatically become scalar signed-loss weights;
noninherited frontier rows are outside the scope of L-91346.
```

The frozen hardening theorem `L-91560` is a promising exact three-ledger cocycle,
and `L-91545` has the correct form of a target-Hall row identity, but both must
be replayed from the moving live `P_61/P_79` source with the causal flow exported
by `L-91354`.  Their summaries are not a substitute for `LRPT`.

## 5. Finite attack plan

`LRPT` is finite-interface and no longer requires a sign search:

1. run max-flow on the exact target capacities already certified positive by
   `L-91354`;
2. export one canonical target flow with rational/algebraic edge weights;
3. evaluate the declared-score residual of that same flow;
4. evaluate every normalized component-row bonus of that same flow;
5. retain parent activation `d<=py` in all three ledgers;
6. verify the residual-plus-child cocycle, including `r`, coefficientwise;
7. compute actual branch target masses and certify their sum is at most one;
8. feed the packet unchanged into `L-91559` and the sourcewise terminal
   telescope.

The output should be one hash-locked packet containing the flow, source
coefficients, row-bonus vectors, branch target weights and final integer-column
capacity replay.

## 6. Boundary

```text
raw arithmetic physical entropy surplus           PROVED / TWO ROUTES
true causal finite Hall signs                      PROVED / L-91354
nested identity physical embedding                 PROVED AT FROZEN HARDENING INPUT
finite-Euler all-depth terminal debt               PROVED AT FROZEN HARDENING INPUT
live source-labelled flow/row provenance           OPEN / LRPT
source-pinned finite base and loss consumer        RECONSTRUCTION REQUIRED
corrected factor-54 recurrence                     CONDITIONAL ON LRPT
Riemann Hypothesis                                 UNPROVEN
```
