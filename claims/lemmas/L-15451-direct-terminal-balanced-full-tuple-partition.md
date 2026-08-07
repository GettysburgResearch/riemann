# L-15451 — Direct full-tuple terminal/balanced partition

Claim ID: `L-15451`  
Title: Every exact finite source tuple is either one free unrestricted terminal lattice variable with small complement, or admits a strict balanced factorization  
Status: **PROPOSED REPAIR — COMPLETE GEOMETRIC LEMMA PENDING INDEPENDENT REVIEW**  
Review base: PR #165 at `13d32ea7a694acf64f5e55b4a41b9b632cd22dd0`  
Dependencies: PR #158 exact Heath–Brown tuple dictionary; PR #233 finite Möbius resolvent after explicit residual divisor expansion; `L-15449`  
Scope: replacement for the recursive Type-I complexity step of `L-15450`; no balanced packet estimate

## 1. Abstract tuple geometry

Fix a finite source tuple

\[
N=w_1\cdots w_r,
\qquad r\le R_K,
\]

with

\[
e^{J-C_K}\le N\le e^{J+C_K}.
\]

Every variable is declared either:

1. **truncated**, with
   \[
   w_i\le e^{J/K+O_K(1)};
   \]
2. **unrestricted**, meaning it is summed over the complete positive-integer lattice subject only to the common compact output window once all other tuple variables are frozen.

Fix a reserve parameter

\[
0<\eta<{1\over2}.
\]

For the concrete application below one may take

\[
\eta={1\over4}.
\]

## 2. Terminal alternative

Call an unrestricted variable `w_i` terminal when its complementary product

\[
A_i={N\over w_i}
\]

satisfies

\[
A_i\le e^{\eta J+O_K(1)}.
\tag{L-15451.1}
\]

For sufficiently large `J`, at most one variable can satisfy (L-15451.1). Indeed, if distinct `i,j` did, then

\[
N\le A_iA_j
\le e^{2\eta J+O_K(1)},
\]

contradicting `N>=e^(J-C_K)` because `2eta<1`.

If such a variable exists, freeze every other tuple coordinate. By definition the terminal coordinate runs over the complete integer lattice selected by the common compact window. The row is therefore of the exact form

\[
\sum_{n\ge1}
{P_A(\log n)\over\sqrt{An}}
W(x-\log(An)),
\tag{L-15451.2}
\]

provided the source coefficient depends polynomially on the terminal logarithm. This is precisely the normal form of `L-15449`.

## 3. Nonterminal variables are individually subcritical

Assume there is no terminal variable.

For every unrestricted variable,

\[
{N\over w_i}>e^{\eta J-O_K(1)},
\]

hence

\[
w_i<e^{(1-\eta)J+O_K(1)}.
\tag{L-15451.3}
\]

Every truncated variable satisfies

\[
w_i\le e^{J/K+O_K(1)}.
\]

Thus if

\[
{1\over K}<1-\eta,
\tag{L-15451.4}
\]

all variables satisfy a common bound

\[
w_i\le e^{(1-\eta)J+O_K(1)}.
\tag{L-15451.5}
\]

For `eta=1/4`, condition (L-15451.4) holds for every `K>=2`.

## 4. Direct balanced split

Traverse the variables in their fixed source order and stop at the first prefix `P` satisfying

\[
P\ge e^{\eta J/2}.
\tag{L-15451.6}
\]

The preceding prefix is below `e^(eta J/2)`. By (L-15451.5), the newly appended variable is at most `e^((1-eta)J+O_K(1))`. Consequently

\[
P\le
 e^{(\eta/2+1-\eta)J+O_K(1)}
=e^{(1-\eta/2)J+O_K(1)}.
\tag{L-15451.7}
\]

Let

\[
Q={N\over P}.
\]

Using (L-15451.6) and the upper support bound for `N`,

\[
Q\le e^{(1-\eta/2)J+O_K(1)}.
\tag{L-15451.8}
\]

Therefore every nonterminal tuple has an exact whole-product factorization

\[
\boxed{N=PQ}
\]

with

\[
\boxed{
P,Q\le e^{(1-\eta/2)J+O_K(1)}.}
\tag{L-15451.9}
\]

This is a genuine strict logarithmic reserve. No already-exposed small packet is lost because the partition is applied to the complete tuple from the beginning.

For the useful concrete choice `eta=1/4`,

\[
\boxed{
\text{terminal complement scale}\le {1\over4}J+O_K(1),
}
\]

while every nonterminal tuple has

\[
\boxed{
\log P,\log Q\le {7\over8}J+O_K(1).
}
\]

## 5. Exact signed grouping

The partition above is deterministic tuple-by-tuple and uses no estimate. After every tuple receives either a terminal label or the ordered balanced destination `(P,Q)`, all source contributions with the same destination may be recombined with their exact Möbius/binomial signs before Cauchy–Schwarz, total variation, or divisor bounds.

Hence the direct partition is compatible with the load-bearing signed-grouping rule of PR #158.

## 6. Heath–Brown terminal rows

For the exact Heath–Brown tuple

\[
(d_1,\ldots,d_j;q;r_1,\ldots,r_{j-1}),
\]

the `d_i` are truncated and the variables `q,r_i` are unrestricted.

A terminal coordinate cannot be one of the `d_i`: terminality implies its size is at least

\[
e^{(1-\eta)J-O_K(1)},
\]

whereas

\[
d_i\le e^{J/K+O_K(1)}.
\]

Thus, under `1/K<1-eta`, every terminal variable is `q` or some `r_i`.

If the terminal variable is `q`, the source coefficient is linear in `log q`. If it is one of the `r_i`, the unique logarithmic factor `log q` belongs to the frozen complement. Hence every terminal row has polynomial degree at most one in the terminal logarithm and is covered by `L-15449`.

The number and coefficient mass of frozen complements of product

\[
A\le e^{\eta J+O_K(1)}
\]

has fixed-order divisor growth. Therefore

\[
\sum_A |c_A|\mathcal P_{A,x}
\le e^{(\eta+o_K(1))J}.
\tag{L-15451.10}
\]

Applying `L-15449` gives

\[
\sup_{J\le x\le J+1}|T_{K,\mathrm{term}}(x)|
\le
\exp\left[-\left({1\over2}-\eta-o_K(1)\right)J\right],
\tag{L-15451.11}
\]

and

\[
E_{K,\mathrm{term}}(J)
\le
\exp\left[-\left(1-2\eta-o_K(1)\right)J\right].
\tag{L-15451.12}
\]

At `eta=1/4`, the terminal energy decays like

\[
\boxed{e^{-(1/2-o_K(1))J}.}
\]

## 7. Möbius-resolvent terminal rows after exact residual expansion

The raw residual variable in PR #233 is not unit-weight unrestricted: it carries

\[
r_V(n)=-\sum_{\substack{a\mid n\\a\le V}}\mu(a)
\qquad(n>1).
\]

Therefore first expand each residual factor exactly as

\[
n_i=a_ib_i,
\qquad a_i\le V,
\]

so that

\[
r_V(n_i)
=-\sum_{a_ib_i=n_i,\,a_i\le V}\mu(a_i).
\]

A `j`-residual row becomes a finite tuple in truncated variables

\[
d,a_1,\ldots,a_j\le V
\]

and unrestricted variables

\[
b_1,\ldots,b_j\ge1,
\]

with exact Möbius signs retained.

The original residual support condition `a_ib_i>V` introduces no cutoff on a terminal `b_i`. Indeed terminality gives

\[
b_i\ge e^{(1-\eta)J-O_K(1)},
\]

while `a_i>=1` and `V=e^(J/K+O_K(1))`. Under

\[
1-\eta>{1\over K},
\]

one has `a_i b_i>V` throughout the active terminal window for sufficiently large `J`.

Thus the terminal `b_i` is a complete unrestricted integer lattice variable and `L-15449` applies after this exact divisor expansion.

## 8. Consequence

The recursive categories

```text
reduced-complexity Type I
terminal Type I
balanced Type II
```

can be replaced for terminal analysis by the simpler exhaustive dichotomy

```text
terminal: one unrestricted coordinate with complement <= exp(eta J),
or
balanced: both full-tuple factors <= exp((1-eta/2)J).
```

This removes the same-scale Type-I cycle issue entirely. The only remaining analytic problem is a signed estimate for the balanced destination packets.

## 9. Proof boundary

Closed by this lemma, subject to independent review:

- exact whole-tuple terminal/balanced dichotomy;
- strict balanced reserve independent of packet order;
- complete unrestricted terminal lattice for Heath–Brown tuples;
- complete unrestricted terminal lattice for the Möbius resolvent after residual divisor expansion;
- exponential terminal energy decay via `L-15449`.

Not closed:

- any signed balanced Type-II energy recurrence;
- vanishing balanced coefficient rate;
- RH.
