# L-91734 — Activation-knot collars have vanishing score by absolute continuity, and retained-cell refinement preserves strict native reserve

Claim ID: `L-91734`
Status: **PROVED MEASURE-THEORETIC SCORE REPAIR / CONDITIONAL FINITE-CELL RELATIVE-REFINEMENT COMPILATION**
Created: 2026-08-15
Depends on: `L-91107`, `L-91110`, `L-91674`, the retained-cell refinement of PR #479, `L-91733`
Corrects: the unnecessary pointwise score-majorant premise in `L-91724.15--.16`
RH status: **unproved**

## 1. The factor-67 endpoint measure is finite and atomless

On `1<=x<67`, the normalized endpoint measure is

\[
 d\nu(x)=\frac{2L(x)}x\,dx,
 \qquad
 0<L(x)<\frac{183}{100}.
\tag{L-91734.1}
\]

Hence

\[
 0<\frac{d\nu}{dx}<\frac{183}{50}<4,
\]

so `nu` is finite and atomless.

Let `S` be the finite set of activation knots for the complete fixed-window
typed root map, including small-divisor, row, ordinary, detail, boundary and
port activations.  Put

\[
 U_\eta=
 \{x:\operatorname{dist}(x,S)<\eta\}
 \cap[1,67).
\tag{L-91734.2}
\]

Then `1_(U_eta)->0` almost everywhere as `eta->0`.

## 2. Collar score tends to zero without a pointwise `A sqrt(X)+B` bound

Let `g_X(x)>=0` be the literal-score coordinate of the complete positive
post-Hall fiber at endpoint `X`.  Finiteness of the root packet means

\[
 g_X\in L^1(\nu).
\]

Dominated convergence gives

\[
 \boxed{
 \int_{U_\eta}g_X(x)d\nu(x)
 \longrightarrow0.
 }
\tag{L-91734.3}
\]

The same argument applies simultaneously to any finite collection of
nonnegative target, source-mass, boundary and port coordinates.  Thus, for each
endpoint `X`, the collar radius can be chosen so that every such removed
coordinate, including literal score, is below a prescribed tolerance such as
`X^-2`.

This is the exact score theorem needed at the knots.  No uniform pointwise
majorant for every normalized fiber is required.

## 3. Uniform relative refinement away from the knots

Let

\[
 A_X=[1,67)\setminus U_{\eta_X}.
\]

It is a finite union of compact cells.  On each cell:

```text
the active source labels are fixed;
every active normalizing capacity has a positive minimum;
the complete post-Hall typed map is Lipschitz;
Hall basis switches remain Lipschitz because min is one-Lipschitz.
```

Choose a mesh which does not cross a knot collar.  On a mesh interval `[a,b]`,
write

\[
 \theta=\frac{b-x}{b-a}
\]

and use the positive same-cell barycentric refinement

\[
 \mathcal H_h(x)
 =\theta\mathcal H(a)+(1-\theta)\mathcal H(b).
\tag{L-91734.4}
\]

For every active finite coordinate `a`, compactness gives a positive capacity
minimum `m_(X,a)` and a finite Lipschitz constant.  Therefore, for every
`epsilon_X>0`, a sufficiently fine mesh satisfies

\[
 \boxed{
 \sup_{x\in A_X}
 \max_{a:c_a(x)>0}
 \frac{|(\mathcal H_h-\mathcal H)_a(x)|}
      {c_a(x)}
 <\epsilon_X.
 }
\tag{L-91734.5}
\]

Inactive coordinates vanish throughout their mesh cell.  The barycentric
weights are nonnegative and sum to one, so this is a positive Markov
pushforward on the frozen endpoint-frame interpretation and does not duplicate
endpoint measure.

## 4. Pay the refinement from the strict all-column reserve

For fixed `X`, let `C_X` be the complete finite observation/correction map on
the retained finite typed space.  Its norm is finite; no uniform-in-`X` norm is
needed because the mesh may be chosen after `X` is fixed.

Choose the mesh so that

\[
 10152\|C_X\|\epsilon_X
 <\frac1{2(\sqrt K+130)}.
\tag{L-91734.6}
\]

Then the strict reserve from `L-91733` pays the complete amplified interpolation
error and leaves

\[
 \boxed{
 s_X^{\rm final}(q)>
 \frac{\Omega_X(q)}{2(\sqrt K+130)}
 \qquad(2\le q\le X/4).
 }
\tag{L-91734.7}
\]

The terminal omission is preserved because the activation collar removes
positive source and the same square-root thinning is no weaker than the one in
the frozen terminal proof.

## 5. Integrated interpolation score also tends to zero

On each retained compact cell, the literal-score coordinate converges uniformly
under same-cell refinement.  Since `nu` is finite, choose the mesh still finer
so that

\[
 \int_{A_X}|g_{X,h}(x)-g_X(x)|d\nu(x)<X^{-2}.
\tag{L-91734.8}
\]

Combining (L-91734.3) and (L-91734.8), the activation-collar plus interpolation
score cost is `o(1)`.

## 6. Compatibility with child mass and source labels

Remove the collar and perform the positive same-cell refinement before the
current/child labels are forgotten.  This replaces the endpoint measure by a
common positive restriction/pushforward.  The aggregate-list inequality and
the variable-list pointwise mass inequality of `L-91732` are therefore
preserved.

This theorem retains the finite-cell source interpretation as a frozen input.
It does not independently prove that the endpoint-frame pushforward realizes
the native arithmetic source; that remains part of the hostile reconstruction
boundary.

```text
atomless factor-67 endpoint measure                   exact
shrinking activation-collar literal score ->0         exact
uniform relative refinement off knots                 finite-cell exact
strict all-column reserve after refinement            conditional on frozen map
collar plus interpolation score                       o(1)
pointwise A sqrt(X)+B score premise                    unnecessary
endpoint-frame source interpretation                  frozen review input
Riemann Hypothesis                                    unproved
```
