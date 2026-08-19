# L-99100 — Literal-score debt is a target-mass supermartingale on the typed factor-67 tree

Claim ID: `L-99100`  
Status: **PROVED EXACT ABSTRACT COMPOSITION THEOREM; ARITHMETIC INPUTS EXPLICIT**  
Created: 2026-08-19  
Frozen parent: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
Depends on: the typed two-sort identity `L-99020`, exact residual causal identity and actual-mass normalization `L-99021`, and the terminal unit-debt bound stated in `L-99024`  
RH status: **unproved**

## 1. Typed recursive packet

Let `v` be a normalized positive residual-source state. Write `m_v>0` for its
actual target mass and `P_v` for its ideal physical row. Assume the local
construction gives the exact physical-row identity

\[
P_v=C_v\oplus\bigoplus_{w\in\operatorname{ch}(v)}a_{vw}P_w,
\qquad a_{vw}\ge0,
\tag{L-99100.1}
\]

where:

1. `C_v` is current-owned and contains the residual current and the target-free
   Hall row bonus;
2. only the displayed children cross to later source states;
3. every child is normalized by its own actual target mass;
4. target mass is exact:

\[
m_v=m(C_v)+\sum_w a_{vw}m_w;
\tag{L-99100.2}
\]

5. the normalized recursive mass satisfies

\[
\sum_w a_{vw}m_w<\frac18m_v.
\tag{L-99100.3}
\]

For the PR #620 causal identity, the `a_(vw)` are the normalized
`alpha_i`-child masses. Survival and current coefficients do not define child
states.

Let `H` be the literal physical-row score. It is nonnegative and linear on
positive rows. Let `P_hat_v` denote the recursively realized row and put

\[
D_v=\bigl(H(P_v)-H(\widehat P_v)\bigr)_+.
\tag{L-99100.4}
\]

Assume that every current-owned nonterminal packet is realized with no literal
score shortfall, while a terminal current packet of mass `m` has shortfall at
most `D_0 m`.

## 2. Bellman debt inequality

Let `c_v=m(C_v)`. Exact row linearity and positive homogeneity give

\[
D_v\le D_0c_v+\sum_w a_{vw}D_w.
\tag{L-99100.5}
\]

This inequality is deliberately pessimistic: it charges the full terminal
unit debt `D_0` even to nonterminal current mass, although the retained local
score inequality charges no debt there.

Define

\[
\mathscr B_v=D_0m_v.
\tag{L-99100.6}
\]

Then by (L-99100.2),

\[
D_0c_v+\sum_w a_{vw}\mathscr B_w
=D_0\left(c_v+\sum_w a_{vw}m_w\right)
=D_0m_v
=\mathscr B_v.
\tag{L-99100.7}
\]

Thus `mathscr B` is an exact superharmonic envelope for literal-score debt.
Since each child endpoint is smaller by a rough prime and the finite source DAG
is nilpotent at fixed endpoint, backward induction gives

\[
\boxed{D_v\le D_0m_v}
\tag{L-99100.8}
\]

for every state.

The conclusion is independent of:

```text
number of children;
actual rough primes on a path;
branching geometry;
history depth;
choice of a distinguished prime;
number of terminal leaves.
```

The strict one-eighth estimate is not needed to improve the constant in
(L-99100.8); it supplies absolute convergence and finite/backward exhaustion.
The score bound itself comes from exact target-mass conservation.

## 3. Direct sums and fixed P61 ledger

Debt is positively homogeneous and subadditive under positive direct sums.
For the native fixed-small-prime root source, the total source weight is

\[
W_{61}=\sum_{d\mid P_{61}}d^{-1/2}
=\prod_{p\le61}(1+p^{-1/2}).
\tag{L-99100.9}
\]

The terminal estimate used by PR #620 is

\[
D_0\le2(4\sqrt{67}-3).
\tag{L-99100.10}
\]

Consequently

\[
D_{\rm root}
\le2(4\sqrt{67}-3)
\prod_{p\le61}(1+p^{-1/2}).
\tag{L-99100.11}
\]

The exact-rational outward checker `X-99100` proves

\[
\boxed{
D_{\rm root}<3534.675221310728<3600.
}
\tag{L-99100.12}
\]

No generation-by-generation debt, geometric `1/(1-rho)` factor, or fictitious
`67^j` source path occurs.

## 4. Statement-to-use boundary

This theorem closes one composition interface only. To conclude the score bound
claimed in PR #620, an independent review must still establish:

- the compact two-sort Hall theorem and its all-real row profiles;
- the local literal-score inequality and terminal unit-debt bound;
- the equality endpoint measure and score normalization;
- the all-column thinning and root-only omission ownership;
- the endpoint and Mellin–Landau consumer.

No conclusion about RH is asserted here.
