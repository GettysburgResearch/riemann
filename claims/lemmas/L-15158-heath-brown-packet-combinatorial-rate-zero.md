# L-15158 — The Heath--Brown packet has zero combinatorial exponent

Claim ID: `L-15158`  
Title: At every fixed identity order, all tuple multiplicities and coefficient words in the exact Heath--Brown packet are subexponential in the logarithmic block scale  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: the coefficient tuple ledger in `L-15156`; the elementary fixed-order divisor bound  
Scope: separates combinatorial growth from the analytic coefficient rate in `CP(K)`

## 1. Fixed-order divisor bound

Fix `K>=2`. Every coefficient tuple in `L-15156` has at most `2K` positive
integer variables. Therefore the number of tuples representing one integer `n`
is bounded by the ordered divisor function

\[
 d_{2K}(n).
 \tag{L-15158.1}
\]

For every fixed `r` and every `epsilon>0`, the elementary divisor bound gives

\[
 d_r(n)\ll_{r,\epsilon}n^\epsilon.
 \tag{L-15158.2}
\]

Equivalently, when `n=exp(J+O_K(1))`,

\[
 \boxed{
 \log d_{2K}(n)=o_K(J).}
 \tag{L-15158.3}
\]

## 2. Coefficient-word bound

One tuple coefficient is

\[
 (-1)^{j-1}{K\choose j}
 \mu(d_1)\cdots\mu(d_j)\log q.
 \tag{L-15158.4}
\]

Hence

\[
 |c_{K,j}(\mathbf t)|
 \le2^K(J+O_K(1)).
 \tag{L-15158.5}
\]

Summing all tuples assigned to one integer and one destination packet gives

\[
 \boxed{
 |c_{K,\tau,J}(n)|
 \le2^K(J+O_K(1))d_{2K}(n)
 =\exp(o_K(J)).}
 \tag{L-15158.6}
\]

The number of combinatorial destination types is finite for fixed `K`, so it
also contributes only a constant to the logarithmic rate.

## 3. Signed packet grouping does not create an exponential rate

Combining all identity indices `j` assigned to one destination packet adds at
most the finite factor

\[
 \sum_{j=1}^K{K\choose j}=2^K-1.
 \tag{L-15158.7}
\]

Therefore the complete signed packet coefficient ledger still satisfies

\[
 \boxed{
 \max_{\tau,n}
 \log(1+|c_{K,\tau,J}(n)|)=o_K(J).}
 \tag{L-15158.8}
\]

No rowwise total-variation estimate is asserted; (L-15158.8) merely proves that
retaining the exact tuple ledger has zero exponential combinatorial cost.

## 4. Consequence for `CP(K)`

The coefficient rate `epsilon_K` in `T-15122/M-15112` is not needed to absorb:

- binomial multiplicities;
- fixed-order divisor multiplicities;
- logarithmic coefficient words;
- the finite number of auxiliary packet types.

All of those have rate zero for every fixed `K`.

Any positive `epsilon_K` must therefore come from the **analytic** operations in
the centered packet estimate, such as:

1. norm growth in a Type-I or Type-II contraction;
2. cutoff and shifted-boundary transition estimates;
3. terminal Type-I bounds;
4. an auxiliary tensor-energy comparison.

Thus a proof that these analytic operations also cost only `exp(o_K(J))` would
establish `CP(K)` with

\[
 \varepsilon_K=0
 \tag{L-15158.9}
\]

at one fixed order and would already imply RH through `T-15121`.

The increasing-order theorem `T-15122` remains useful if the analytic estimate
has a small positive rate tending to zero with `K`.

## 5. Proof boundary

Closed here:

- zero exponential rate of the entire finite coefficient ledger;
- separation of combinatorial and analytic losses.

Not closed:

- any analytic normal-energy bound for the packets;
- `CP(K)`;
- RH.
