# L-91843 — A sequential source ledger produces the corrected native root identity

Claim ID: `L-91843`  
Status: **PROVED EXACT COMPOSITION THEOREM ON THE FROZEN STAGE INPUTS**  
Created: 2026-08-15  
Primary inputs: `L-91674`, `L-91688`, `L-91690`, `L-91733`, `L-91754`, `L-91755`, `L-91840--L-91842`  
RH status: **unproved**

## 1. Typed ledger

Work in one additive labelled space carrying

\[
(\text{source},T,S,E,Q,\Gamma,\Xi,\text{boundary},\text{port},\text{declared capacity}).
\]

Each positive split is implemented by substochastic Markov kernels whose
outgoing current, child and unused weights sum to the incoming weight. Labels
are never forgotten before all physical observations have been formed.

## 2. Fourteen stages

Starting from the full native equality datum, apply in order:

1. native/full-Mobius source typing;
2. inner-versus-outer scale split;
3. bottom omission;
4. top omission;
5. whole-cell or restriction-before-quadrature support selection;
6. exact deterministic root Hall residual/bonus split;
7. first-owner rough partition;
8. causal current/internal-child split;
9. positive endpoint integration;
10. positive same-cell refinement, or the identity in the exact Hall route;
11. one global labelled martingale quantizer;
12. one common square-root thinning;
13. retained mismatch/collar/taper/base comparison;
14. one current-owned port completion, or the zero port of PR #487.

At stage `i`, let `Sigma_(i-1)` be the still-unassigned labelled source. The
stage supplies disjoint positive packets

\[
 C_i,\qquad (P_{i,b})_b,\qquad U_i,\qquad\Sigma_i
\]

with

\[
\boxed{
 \Sigma_{i-1}=C_i+\sum_bP_{i,b}+U_i+\Sigma_i.
}
\tag{L-91843.1}
\]

No term from an earlier stage is available to a later stage.

## 3. Telescoping source identity

Summing (L-91843.1) over the fourteen stages gives

\[
\boxed{
 \Sigma_0=C_X^{\rm src}
 +\sum_bP_b^{\rm src}
 +U_X^{\rm src},
}
\tag{L-91843.2}
\]

where all three terms are positive and source-disjoint. `L-91841` makes every
child operator first-owner restricted. `L-91840` ensures that a partially
retained endpoint cell contributes only its restricted defect. `L-91842` types
any port surplus explicitly on the current side.

## 4. Native detail identity

Apply the ordinary response at `q` and `4q` separately and then form detail.
Let `d_X^cur` be the final current row, let `P_b` be any exported positive child
packet with its declared full native capacity, and let `r_X` be the sum of the
explicit unused detail packets produced at stages 3, 4, 5, 10, 12 and 13. Then

\[
\boxed{
 \Omega_X
 =\Xi(d_X^{\rm cur})+r_X
 +\sum_b\beta_bU_b^{(1)}\Omega(P_b),
 \qquad r_X\ge0.
}
\tag{L-91843.3}
\]

This equality is obtained by observing the telescoping source partition. The
slack is not defined afterward as a coordinatewise complement in order to infer
positivity.

Every terminal, taper and finite-base vector which is inserted into the
current row is already included in `Xi(d_X^cur)` and is not charged again to
`r_X`.

## 5. One-shot specialization

For PR #487, all causal child colours remain inside `d_X`. Thus the exported
family in (L-91843.3) is empty and the identity becomes

\[
\boxed{\Omega_X=\Xi(d_X)+r_X,\qquad r_X\ge0.}
\tag{L-91843.4}
\]

The port term is zero. This is exactly the conclusion-producing producer
identity requested by PR #484.

## 6. Recursive specialization

If children are exported, normalize them by actual target mass as in
`L-91841`. Inserting feasible child rows into (L-91843.3) gives the exact native
slack cocycle

\[
 s_X=r_X+\sum_b\beta_bU_b^{(1)}s_b.
\tag{L-91843.5}
\]

The actual weighted child mass is below one eighth. No root omission,
quantizer, correction or port is repeated in a child.

## 7. Boundary

```text
fourteen-stage operation order                 explicit
one owner per source occurrence                exact
partial-cell defect ownership                  exact
first-owner child restriction                  exact
complete port demand                           explicit or zero
native root identity                           exact on frozen stages
one-shot exported family                       empty
recursive slack cocycle                        exact optional specialization
Riemann Hypothesis                             unproved
```
