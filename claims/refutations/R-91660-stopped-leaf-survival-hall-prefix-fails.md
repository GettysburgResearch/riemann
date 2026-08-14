# R-91660 — An admissible stopped leaf violates the reused survival target-Hall prefix condition

Claim ID: `R-91660`  
Status: **EXACT LOAD-BEARING REFUTATION OF THE FROZEN HALL APPLICATION**  
Review date: 2026-08-14  
Frozen proposal: PR `#455` at `1b502acbe511776178da3dc916e3cd3464cd5e77`  
Normative content commit: `c696d2a356eeacb3097d4ea6cc727b84548d7a03`  
Refutes as stated: the stopped-leaf Hall entry in `L-91621`, its reuse in `L-91663/L-91671`, and the resulting conclusion in `T-91656`  
Does not refute: the single-SHARP atom identity or the finite equality-seed Fubini identity  
RH status: **unproved**

## 1. Frozen one-prime variables

The controlled cocycle uses

\[
r=p^{-1/2},\qquad z=\sqrt{x/n},
\]

and its survival target is a positive multiple of

\[
w_{\alpha_s}(x,n)
=\frac{\alpha_s\sqrt x}{n}-\frac1{\sqrt n},
\qquad
\alpha_s=\frac{2(r+2)}{r+3}.
\]

The positive multiplier is

\[
g_s=(1-r)(r+3)>0.
\]

In the preferred stopped `P_61` packet, the parent endpoint is

\[
x=py,\qquad p\ge67,\qquad1\le y<67,
\]

and the parent-index source coefficients are exactly `mu(d)` for `d|P_61`.
For `d<=y`, the one-prime child is active. These are the variables fixed in
`O-91310`, `L-91554`, and `L-91560`.

## 2. Necessary Hall prefix

For a no-upward Hall transport supported on `e<=o`, odd demands up to an
odd threshold `t` can only use even capacities up to `t`. Therefore

\[
\mathcal H_{s,t}(x)
:=\sum_{\substack{e\le t\\mu(e)=1}}w_{\alpha_s}(x,e)
 -\sum_{\substack{o\le t\\mu(o)=-1}}w_{\alpha_s}(x,o)
\ge0
\]

is necessary. Put

\[
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad
B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\]

Then

\[
\mathcal H_{s,t}(x)=\alpha_s\sqrt x\,A_t-B_t.
\]

## 3. Explicit stopped-leaf counterexample

Choose

\[
\boxed{p=67,\qquad y=13,\qquad x=py=871,\qquad t=13.}
\]

Every squarefree source node `d<=13` lies in the active one-prime sector because

\[
p^{-1/2}\sqrt{x/d}=\sqrt{13/d}\ge1.
\]

Moreover

\[
\boxed{A_{13}=-\frac{2323}{30030}}.
\]

The directed exact checker `X-91672` proves

\[
\boxed{
-2.139513718150116
<\mathcal H_{s,13}(871)
<-2.139513718150115
<-2.
}
\]

Multiplication by `g_s>0` preserves the strict negative sign. Hence

\[
\boxed{
\text{no survival target-Hall transport supported on }e\le o
\text{ exists on this stopped leaf.}
}
\]

This is not a finite-base exception. Since \(A_{13}<0\),
\(\alpha_s>4/3\), and \(\sqrt{13p}\) increases with \(p\), the conservative
bound

\[
\frac43\sqrt{13\cdot67}\,A_{13}-B_{13}<-2.0799
\]

implies the same Hall-prefix failure for **every prime \(p\ge67\)** at
\(y=13\).

## 4. Why the cited Hall certificate does not apply

`L-91550` certifies the survival and hazard Hall corridors only on

\[
1\le x<55.
\]

The stopped child parameter `y=13` is bounded, but the controlled parent target
and literal parent row in `L-91560` are evaluated at `py/d`, not at `y/d`.
Replacing `py` by `y` changes the target atom and is not one of the frozen
three-ledger identities.

The abstract disintegration theorem `L-91545` is correct conditional on a
Hall transport. The counterexample shows that its hypothesis is absent on an
admissible family of stopped leaves.

## 5. Independent row-margin scope failure

`L-91670` states that the `a=1` derivative numerator obeys

\[
M_1>\frac1{20}
\]

at every activation-cell right endpoint by `L-91322`. The cited directed
theorem checks only `N<=54`. At

\[
N=71,\qquad j=70,\qquad Y=72,
\]

`X-91672` proves

\[
\boxed{0<M_1<0.049925670420019<\frac1{20}.}
\]

This refutes the promoted global numerical margin, not global monotonicity
itself: the displayed probe remains positive.

## 6. Consequences

The following downstream objects require the missing positive Hall output:

```text
L-91621: positive residual survival/hazard sources and Hall row bonuses;
L-91663: positive complete parent row R_parent;
L-91671: one-use parent ownership and equality-deficit recurrence;
T-91656: feasible d_X with logarithmic native loss.
```

The same-index child-replacement formula remains a correct conditional capacity
identity, but the required positive parent packet has not been produced.

## 7. Surviving mathematics

```text
historical factor-three diagnosis                         EXACT
w_Psi = 3 w_(4/3)                                        EXACT
one-copy atomwise row normalization                       EXACT
finite equality-seed Fubini identity                      EXACT
R[b_X^star] = c_X                                         EXACT
4 sqrt(X) distinct from P_Lambda(X)                       CORRECTLY TYPED
same-index arbitrary-child replacement                    CONDITIONAL EXACT
v2 object freeze                                          CONSISTENT ON INSPECTED OBJECTS
```

## 8. Replacement gate

A successor must either:

1. construct a valid parent-index target/score/row transport for every
   `p>=67`, `1<=y<67`, and every active odd prefix; or
2. Hallize only a bounded child quotient and prove an exact, nonduplicating
   ledger back to the parent row `Q_(py/d)` and its native score.

It must explicitly pass the `y=13,t=13` hostile family and supply a correctly
scoped normalized-row theorem on its actual Hall edges.

```text
single-SHARP normalization                           SURVIVES
stopped-leaf survival Hall at y=13                  FALSE FOR ALL p>=67
positive parent Hall packet                          NOT PRODUCED
T-91656                                               REJECTED AS PROOF
Riemann Hypothesis                                    UNPROVEN
```
