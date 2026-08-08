# Full-problem attack — eta source-flow audit, exact obstruction, and repaired RH proposal

**Agent:** `gpt56-pro`  
**Date:** 2026-08-08  
**Repository:** `gfreund123/riemann`  
**Branch:** `research/gpt56-pro-302-source-flow-manifest`  
**Frozen parent:** PR #301 at `1855957a18b7ea43229cde626178920f7a538951`  
**Status:** **EXACT REFUTATION OF ONE LOAD-BEARING SOURCE BINDING + NEW FULL CONDITIONAL REPAIR**  
**RH:** **UNPROVEN**

## 1. Objective

The preceding work had consolidated the elementary carry programme to the
weighted-shell scalar `WSTS`, exactly equivalent to RH.  The user requested a
step back and a direct attack on the full problem rather than another reduction
to an ever smaller scalar.

The live repository had meanwhile advanced to PR #301, which proposed a full
proof through:

```text
positive stopped-power analytic resolution
-> analytic contraction 6/7
-> Hausdorff ordered eta boundary sources
-> nonnegative central/sibling Pascal flow
-> triangular boundary contraction
-> Cycle Debt
-> sharp prime ramp
-> RH.
```

This pass froze that proposal and audited the one place where an analytic source
coefficient becomes a balanced-flow edge coefficient.  That type conversion is
load bearing: the spectral radius is useful only if the boundary source is
actually realized by the declared nonnegative flow.

The result is twofold:

1. one exact source-to-flow assertion in PR #301 is false;
2. the surrounding analytic mechanism admits a sharper repaired formulation
   with one finite, fail-closed source-capacity theorem `SFC`.

## 2. Exact local algebra retained

At parent `4k`, define

\[
C_k=[4k,2k],
\qquad
S_k=[4k,2k-1].
\]

For every integer carry column `q`, direct floor algebra gives

\[
\boxed{
\chi_{S_k}(q)-\chi_{C_k}(q)
=\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}.
}
\]

Therefore, when a flow already contains a central edge `A C_k`, the replacement

\[
A C_k
\longmapsto
(A-B)C_k+B S_k,
\qquad A\ge B\ge0,
\]

is coefficientwise nonnegative and changes the carry vector by exactly

\[
B(\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}).
\]

This relative replacement is exact and useful.

## 3. Exact false claim in the completed source-flow bridge

PR #301 also treated the same nonnegative edge pair as a realization of the
formal paired divisor source

\[
A e_{2k}-B e_{2k+1}.
\]

That inference is false.

The formal source has carry load

\[
A\mathbf1_{q\mid2k}-B\mathbf1_{q\mid2k+1}.
\]

The edge pair has load

\[
A\chi_{C_k}(q)
+B(\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}).
\]

At `q=4k`, the formal source load is zero while both declared splits carry one,
so the edge load is exactly `A`.

The smallest eta witness is

\[
k=1,\qquad A=rac12,\qquad B=rac13.
\]

At columns `q=2,3,4`:

```text
formal paired source     1/2, -1/3, 0
nonnegative edge pair    1/3,  1/6, 1/2
```

The mismatch is exact.  Thus the standalone conclusion in `L-29807.4` and the
resulting zero-debt assertion are not established by the displayed local
identity.

The correct statement is affine:

\[
[(A-B)C_k+B S_k]-A C_k=B(S_k-C_k).
\]

An incoming central edge `A C_k` must be shown to exist before the replacement
can be used.

## 4. Exact absolute source coordinate

The repository already contains the right object for a formal divisor atom.
Let `T_n` be the complete central halving tree with divergence

\[
\partial T_n=e_n-n e_1.
\]

Define the adjacent commutator

\[
\mathcal E_h=T_{h+1}-T_h.
\]

For all `q>=2`,

\[
L_q(\mathcal E_h)
=\left\lfloorrac{h+1}{q}ightfloor
-\left\lfloorrac hqightfloor
=\mathbf1_{q\mid h+1}.
\]

Thus

\[
e_m\longleftrightarrow\mathcal E_{m-1}
\]

in carry space.  The exact signed flow for the paired source is

\[
A\mathcal E_{2k-1}-B\mathcal E_{2k}.
\]

Pascal algebra yields

\[
\mathcal E_{2k-1}-\mathcal E_{2k}
\equiv S_k-C_k
\]

at the level of complete carry vectors.  Hence

\[
A e_{2k}-B e_{2k+1}
\longleftrightarrow
(A-B)\mathcal E_{2k-1}+B(S_k-C_k).
\]

This identity is exact, but signed.  It cleanly identifies the remaining task:
replace the negative central component by an actually available positive
central capacity, or pay its precise Cycle-Debt cost.

## 5. New all-generation Hausdorff residual theorem

The audit found that PR #301's analytic source ordering can be strengthened.
For the actual shifted pair

\[
A_k(q,s)=rac{(2kq-1)^{-s}}{2k},
\qquad
B_k(q,s)=rac{((2k+1)q)^{-s}}{2k+1},
\]

put

\[
R_k(q,s)=A_k(q,s)-B_k(q,s).
\]

Using

\[
x^{-s}=rac1{\Gamma(s)}\int_0^\infty t^{s-1}e^{-xt}\,dt
\]

and

\[
rac1m=\int_0^\infty e^{-mu}\,du,
\]

one obtains

\[
\boxed{
R_k(q,s)=rac1{\Gamma(s)}\int_0^\infty\int_0^\infty
 t^{s-1}igl[e^t-e^{-(qt+u)}igr]e^{-2k(qt+u)}\,du\,dt.
}
\]

The integrand is nonnegative.  After pushing forward

\[
z=e^{-2(qt+u)},
\]

this becomes

\[
R_k(q,s)=\int_{(0,1]}z^k\,d\lambda_{q,s}(z)
\]

for a positive measure.  Therefore

\[
\Delta^mR_k(q,s)\ge0
\qquad(m\ge0).
\]

The residual is itself a Hausdorff moment sequence.  Positive finite-difference
jets and exact Euler/Taylor remainders insert only nonnegative factors in the
integral, so the conclusion survives every analytic boundary generation.

This closes the **source-type invariance** which PR #301 needed: common-tail
residuals remain positive Hausdorff sources and do not regenerate the analytic
bulk.

It does not supply edge capacity.

## 6. Exact source-mass versus capacity obstruction

For a decreasing divisor source

\[
c_2\ge c_3\ge\cdots\ge c_N\ge0,
\]

the exact nonnegative central-tree realization is

\[
\mathcal T(c)=\sum_{n=2}^N(c_n-c_{n+1})T_n.
\]

Its carry load is

\[
\sum_n(c_n-c_{n+1})\left\lfloorrac nqightfloor
=\sum_{m\ge1}c_{mq}.
\]

The coefficient of the root central edge of size `n` is therefore

\[
c_n-c_{n+1},
\]

not `c_n`.

For the eta source `c_n=1/n`, at node `2k` the analytic pair is

\[
A_k=rac1{2k},
\qquad
B_k=rac1{2k+1}.
\]

The canonical central capacity is

\[
A_k-B_k=rac1{2k(2k+1)},
\]

while the sibling replacement needs `B_k`.  Their exact ratio is

\[
rac{B_k}{A_k-B_k}=2k.
\]

At the first pair, the positive source flow supplies `1/6`, while the proposed
switch spends `1/3`.  The gap grows with `k`.

Thus the following implication is false:

```text
Hausdorff source coefficient A_k
-> available central edge coefficient A_k.
```

Pascal cycles may permit a different positive realization with more central
capacity.  Determining whether they do is the true finite arithmetic problem.

## 7. New fail-closed source-flow certificate

`D-30201` defines the required proof object.  For every endpoint, cascade depth,
stopped-power layer, jet, cutoff cell, and common arithmetic destination, it
must emit:

```text
paired coefficients A_k,B_k;
complete incoming flow;
actual central edge C_k and its available coefficient;
one-use capacity tokens;
new central/sibling edges;
complete relative carry equality;
next-generation residual source;
all unmatched cutoff/collar rows;
weighted capacity defect.
```

The source-flow capacity debt is

\[
\mathfrak C_a(X)
=\sum\omega(C_k)[A_k-c_k]_+
+	ext{collar debt}
+	ext{negative edge debt after replacement}.
\]

The corrected source-flow theorem is

\[
oxed{
\mathfrak C_a(X)\le C\log^A(2X)
}
\]

uniformly over the `O(log X)` cascade depths.

This theorem is called **SFC**.

## 8. Exact finite LP and Farkas dual

Let `B` be the balanced fragmentation divergence matrix, `r` the exact target
divergence, and `a` the vector of required central capacities.  A zero-defect
completion satisfies

\[
Bd=r,
\qquad d\ge a	ext{ on required edges},
\qquad d\ge0	ext{ elsewhere}.
\]

Writing `d=a+x`, the problem becomes

\[
x\ge0,
\qquad Bx=r-Ba.
\]

Finite Farkas duality says this is feasible exactly when

\[
\langle F,r-Baangle\ge0
\]

for every balanced-superadditive node potential

\[
F(n)-F(j)-F(n-j)\ge0.
\]

The weighted-defect version is a finite linear programme with exact primal and
dual certificates.  This is a source-pinned strengthening of the repository's
BCT/Cycle-Debt cone, not a vague new norm.

## 9. Corrected full conditional RH proposal

The analytic bank obeys

\[
A_{a+1}\lerac67A_a+\operatorname{polylog}.
\]

The eta source/cost calculation supplies one absolute

\[
	heta<1
\]

for the boundary source.  Under SFC, the corrected boundary recurrence is

\[
D_{a+1}\le	heta D_a+C_0A_a+\mathfrak C_a+\operatorname{polylog}.
\]

There is no boundary-to-analytic feedback.  `L-30202` keeps all common-tail
residuals in the boundary Hausdorff cone; `SFC` accounts for every capacity
shortage and cutoff collar explicitly.

The triangular matrix

\[
\begin{pmatrix}
6/7&0\\
C_0&	heta
\end{pmatrix}
\]

has spectral radius below one.  Iteration through `O(log X)` half-scale levels
gives polylogarithmic analytic and capacity debt.  The actual edge manifest then
gives polylogarithmic Cycle Debt.  The inherited consumer yields

\[
\sum_{p^a\le X}rac{\Lambda(p^a)}{\sqrt{p^a}}\lograc X{p^a}
=4\sqrt X+X^{o(1)},
\]

and the square-screw/Landau chain gives RH.

Therefore

\[
oxed{
\mathrm{SFC}\Longrightarrow\mathrm{RH}.
}

SFC is not proved on this branch.

## 10. Exact verification

`X-30201` uses only standard-library integer and rational arithmetic.

Main source-flow replay:

```text
sibling carry identity                         28,920 cases
standalone source mismatch                        120 witnesses
relative replacement                           28,920 cases
adjacent-tree divisor commutators                3,320 cases
paired source / Pascal-cycle identities          4,880 cases
shifted residual finite Hausdorff checks         36,936 cases
cutoff start-parity ledger                      45,149 cases
```

Retained result digest:

```text
29e2fda98df6f244f6e13a323652418e6a49824a4e92295401e5ca61c2168a20
```

Capacity replay:

```text
eta central-tree layer cakes                   44,850 cases
exact capacity ratio B/(A-B)=2k                10,000 cases
general decreasing-source layer cakes           6,318 cases
```

Retained result digest:

```text
3300081ea6a9fc2f0f495549bf189bd7f8807cf0808a17ee2c6ea671cbd26daf
```

The finite Hausdorff scan supports, but does not replace, the positive-measure
proof.  Neither checker proves SFC, Cycle Debt, or RH.

## 11. Review order

1. `R-30201` minimal source/edge mismatch.
2. `L-30201` relative replacement and absolute commutator source.
3. `L-30202` positive-measure Hausdorff residual theorem.
4. `R-30202` source mass versus central capacity.
5. `X-30201` and capacity addendum.
6. `D-30201` source-flow certificate schema.
7. `L-30203` exact primal-dual capacity theorem.
8. `T-30201` conditional recurrence and RH composition.
9. `M-30201` fail-closed protocol.
10. Frozen PR #301 analytic claims and PR #272 Cycle-Debt consumer.

## 12. Final status

```text
analytic stopped-power contraction                  retained / proposed complete
relative eta carry replacement                      verified exact
standalone eta paired-source flow                    false
shifted residual Hausdorff invariance                proposed complete
source mass -> central edge capacity                 false
finite source-capacity primal/dual                   proposed complete exact
polylogarithmic SFC                                  open / RH-bearing
SFC -> triangular recurrence -> Cycle Debt -> RH     proposed complete
Riemann Hypothesis                                   unproved
```

The pass does not validate PR #301 as an RH proof.  It replaces its hidden type
conversion with one concrete finite arithmetic theorem and preserves the most
promising global cascade around it.