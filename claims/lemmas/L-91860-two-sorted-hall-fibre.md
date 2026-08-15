# L-91860 — Compact factor-67 Hall fibres split into a positive residual source and a direct nonnegative row bonus

Claim ID: `L-91860`  
Status: **PROPOSED COMPLETE EXACT TWO-SORTED FIBRE THEOREM ON FROZEN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `R-91860`; frozen `L-91690`, `L-91545`, `L-91688`, `L-91654`, `L-91658`  
RH status: **unproved**

## 1. Hall data

Fix one retained factor-67 fibre. Let `E` and `O` be its positive and negative source occurrences. Each occurrence has positive target and declared-score atoms

\[
T(n)>0,\qquad S(n)>0,
\]

and a nonnegative exact component row `R(n)`. Put

\[
q(n)=\frac{T(n)}{S(n)},\qquad
h_j(n)=\frac{R_j(n)}{T(n)}.
\]

The deterministic no-upward target Hall coupling satisfies

\[
\sum_e t_{o,e}=T(o),\qquad
\sum_o t_{o,e}\le T(e),\qquad
 t_{o,e}>0\Rightarrow e\le o.
\tag{L-91860.1}
\]

The frozen factor-67 monotonicities give

\[
e\le o\Rightarrow q(e)\ge q(o),
\qquad h_j(e)\ge h_j(o).
\tag{L-91860.2}
\]

## 2. Positive complete residual source

Define

\[
c_e=1-\frac1{T(e)}\sum_o t_{o,e}\ge0.
\tag{L-91860.3}
\]

Then the residual is a genuine positive source packet on the original target/score kernel type, with

\[
\boxed{T(c)=T(E)-T(O)}
\tag{L-91860.4}
\]

and

\[
\begin{aligned}
S(c)-[S(E)-S(O)]
&=\sum_{o,e}t_{o,e}
\left(\frac1{q(o)}-\frac1{q(e)}\right)\\
&\ge0.
\end{aligned}
\]

Hence

\[
\boxed{S(c)\ge S(E)-S(O).}
\tag{L-91860.5}
\]

Only this target-bearing residual source is eligible for rough first ownership, the causal split, and same-index child placement.

## 3. Direct row-only Hall bonus

Define the finite component-row vector

\[
\boxed{
B_j=\sum_{o,e}t_{o,e}[h_j(e)-h_j(o)]\ge0.
}
\tag{L-91860.6}
\]

Then

\[
\boxed{R(E)-R(O)=R(c)+B}
\tag{L-91860.7}
\]

coefficientwise. The row `B` carries:

```text
Hall-edge ownership;
nonnegative component coefficients;
its induced ordinary and radix-four responses;
its literal physical score.
```

It carries no target-bearing source mass and no declared-score packet coordinate. In particular the negative exact edge-score correction from `R-91860` is not assigned to `B`.

The row bonus is current-generation only:

```text
no rough first owner;
no causal split;
no recursive child;
no child port;
no B-spline source quantization.
```

## 4. Rough ownership and causal colours of the residual source

Apply the least-rough-prime partition only to `c`. For each first-owner residual packet `P`, ordered active rough primes give

\[
P=s_kP+\sum_i\lambda_i(P-r_iU_{p_i}P_{/p_i})
   +\sum_i\alpha_iU_{p_i}P_{/p_i},
\tag{L-91860.8}
\]

where every displayed source packet is positive on the frozen causal theorem and

\[
s_k+\sum_i\lambda_i=1,
\qquad
\sum_i\alpha_i<\frac18.
\tag{L-91860.9}
\]

Same-index placement transports the actual child component row and every linear response with the same coefficient.

## 5. One two-sorted fibre

Let `K_src` be the cone of positive complete source packets and `K_row` the cone of nonnegative finite physical rows. The correct fibre is

\[
\boxed{
\mathfrak f_x
=\bigl(\mathfrak f_x^{\rm src},B_x\bigr)
\in K_{\rm src}\oplus K_{\rm row}.
}
\tag{L-91860.10}
\]

Its component-row observation is the sum of the two sorts. Its target and declared-score observations are taken only from the source sort. Equations (L-91860.4), (L-91860.5), and (L-91860.7) give simultaneously:

```text
target equality;
declared-score superordination;
exact component-row equality;
nonnegative current row bonus.
```

Every original source occurrence is used once by the Hall residual/matched-edge marginal law. Every rough monomial in the residual has one first owner. The row bonus is owned by exactly one Hall edge and is never reinterpreted as source.

## 6. Boundary

```text
Hall residual as positive complete source       exact
Hall bonus as nonnegative physical row          exact
Hall bonus as complete target-null packet       false / R-91860
residual score superordination                   exact
rough ownership and causal split                residual source only
same-index internal children                    exact on frozen inputs
whole-cell common realization                   next lemma
Riemann Hypothesis                              unproved
```
