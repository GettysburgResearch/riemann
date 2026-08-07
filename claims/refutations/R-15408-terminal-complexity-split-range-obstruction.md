# R-15408 — The internal Type-I split in L-15450 is not valid on the full stated reserve range

Claim ID: `R-15408`  
Title: The frozen internal regrouping drops the already-exposed small packet; a counterexample appears for `delta>1/3`  
Status: **EXACT REFUTATION OF THE STATED ROUTING STEP; TERMINAL PROGRAM REPAIRABLE**  
Review base: PR #165 at `13d32ea7a694acf64f5e55b4a41b9b632cd22dd0`  
Scope: Section 3 of `L-15450`; does not refute `L-15449` or the possibility of a corrected terminal partition

## 1. The issue

In `L-15450`, a Type-I tuple has already exposed a small multiplicative packet

\[
A\le e^{\delta J+O(1)},
\]

and the complementary same-scale coefficient word is then internally split as

\[
UV.
\]

The file declares a balanced Type-II destination when both `U` and `V` are at most

\[
e^{(1-\delta)J+O(1)}.
\]

But a genuine factorization of the complete tuple must place the already-frozen factor `A` on one side. The possible whole-product splits are therefore

\[
(AU,V)\qquad\text{or}\qquad(U,AV).
\]

Internal bounds for `U,V` alone do not imply that either complete split lies below the claimed scale.

## 2. Explicit counterexample

Take the allowed reserve

\[
\delta={2\over5}
\]

and logarithmic sizes

\[
\log A={2\over5}J,
\qquad
\log U={3\over10}J,
\qquad
\log V={3\over10}J.
\]

Then

\[
AUV=e^J,
\]

and both internal groups satisfy

\[
U,V\le e^{(1-\delta)J}=e^{3J/5}.
\]

Thus the stated Section-3 test labels this internally balanced. However the complete splits have scales

\[
(\log AU,\log V)=\left({7\over10}J,{3\over10}J\right),
\]

or symmetrically

\[
(\log U,\log AV)=\left({3\over10}J,{7\over10}J\right).
\]

Since

\[
{7\over10}>{3\over5},
\]

neither whole-product factorization is balanced at the declared reserve.

Therefore the recursive routing claim in `L-15450` is false on its full range `0<delta<1/2`.

## 3. Minimal repair for the intended fixed reserve

The repository repeatedly uses the concrete reserve `delta=1/5`. More generally, for

\[
0<\delta\le{1\over3},
\]

a local repair is possible.

Assume `U<=V`. Since the complete tuple has scale `J+O(1)` and `A<=e^(delta J+O(1))`,

\[
UV\le e^{(1-\delta)J+O(1)},
\]

hence

\[
U\le e^{(1-\delta)J/2+O(1)}.
\]

Attach the old small packet to the smaller internal group. Then

\[
\log(AU)
\le
\left(\delta+{1-\delta\over2}\right)J+O(1)
={1+\delta\over2}J+O(1).
\]

For `delta<=1/3`,

\[
{1+\delta\over2}\le1-\delta.
\]

Thus `(AU,V)` is genuinely balanced whenever both internal groups are below the required scale.

If instead `V>e^((1-delta)J+O(1))`, then

\[
AU={N\over V}\le e^{\delta J+O(1)},
\]

so `U` can be absorbed into the small packet and the unresolved coefficient word strictly decreases in complexity.

This repairs the recursive proof at the intended reserve `delta=1/5`, but it is not the argument currently written in `L-15450`.

## 4. Stronger replacement

A cleaner repair avoids the recursive same-scale Type-I graph entirely. `L-15451` gives a direct full-tuple partition into exactly two classes:

```text
one unrestricted terminal variable with small complement,
or
one balanced factorization with strict logarithmic reserve.
```

That replacement automatically keeps every already-exposed factor inside the whole-product geometry and removes the counterexample above.

## 5. Required mutation

Any future regression for terminal geometry should include the exact scale cell

```text
delta = 2/5
(log A, log U, log V)/J = (2/5, 3/10, 3/10)
```

and must reject the old inference

```text
U,V balanced  =>  complete tuple balanced.
```

## 6. Classification

```text
L-15449 one-row Euler theorem              unaffected
L-15450 Section-3 routing as written       REJECTED
L-15450 intended terminal conclusion       repairable
balanced Type-II theorem BTP(K)            still open
RH                                          unproved
```
