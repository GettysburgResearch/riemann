# L-15450 — Every fixed-reserve terminal packet has one free large lattice variable

Claim ID: `L-15450`  
Title: Complexity elimination puts every terminal Heath–Brown or finite Möbius-resolvent row into the Euler-cancellable normal form of `L-15449`  
Status: **PROPOSED — COMPLETE COMBINATORIAL/ANALYTIC REDUCTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: PR #158 `L-15156`--`L-15158`; PR #233 `L-23201/L-23203`; `L-15449`  
Scope: terminal and shifted-boundary rows only; balanced Type-II packets remain open

## 1. Packet sources

There are two exact finite source dictionaries relevant here.

### Prime dictionary

For fixed order `K`, endpoint `X`, and

\[
V=\lceil X^{1/K}\rceil,
\]

`L-15156` writes every coefficient of `Lambda(n)`, `n<=X`, as a finite signed
sum over tuples

\[
(d_1,\ldots,d_j;q;r_1,\ldots,r_{j-1})
\tag{L-15450.1}
\]

with

\[
d_i\le V,
\qquad
d_1\cdots d_jq r_1\cdots r_{j-1}=n.
\]

The coefficient is a fixed binomial factor times

\[
\mu(d_1)\cdots\mu(d_j)\log q.
\tag{L-15450.2}
\]

The variables `q,r_i` are unrestricted positive integers.

### Möbius dictionary

`L-23201` writes every coefficient of `mu(n)`, `n<=X`, as a finite signed sum
of

\[
(d;n_1,\ldots,n_j),
\qquad d\le V,
\qquad n_i>V,
\qquad dn_1\cdots n_j=n,
\tag{L-15450.3}
\]

with exact source-bound divisor coefficients.

The argument below applies to either dictionary. It uses only:

1. finitely many variables at fixed `K`;
2. truncated variables bounded by `V`;
3. unrestricted variables summed over the positive integers;
4. divisor-order coefficient multiplicity.

## 2. Fixed reserve and complexity

Fix once and for all

\[
0<\delta<\frac12
\tag{L-15450.4}
\]

and take

\[
K>\delta^{-1}.
\tag{L-15450.5}
\]

At output logarithmic block `J`, every active product is

\[
e^{J-C}\le n\le e^{J+C}
\tag{L-15450.6}
\]

for a fixed window support constant `C`.

Apply the first-crossing partition of `L-15157`. A Type-I row has a small factor
group with product

\[
A\le e^{\delta J+C}.
\tag{L-15450.7}
\]

Give the complementary large coefficient word the complexity rank

\[
\mathfrak c=
\text{number of unresolved nontrivial variables in that word}.
\tag{L-15450.8}
\]

Variables forced to equal one are deleted from the word.

## 3. Exact finite complexity elimination

Suppose a Type-I large word has `mathfrak c>=2`. Select its first nontrivial
variable and separate it from the remaining product. This is an exact finite
regrouping of the tuple sum, with no estimate.

Apply the fixed-reserve dichotomy to that internal split.

1. If both groups are below `e^((1-delta)J+O_K(1))`, the row is a balanced
   Type-II destination.
2. Otherwise one internal group is below `e^(delta J+O_K(1))`. Absorb it into
   the small packet. The remaining same-scale coefficient word has complexity
   strictly smaller than `mathfrak c`.

Thus every same-scale Type-I transition strictly lowers the integer rank
`mathfrak c`. Repeating at most `2K` times produces either:

```text
balanced Type II,
strict lower-scale packet,
or
one-variable terminal row.
```

There is no same-scale cycle.

This makes the acyclicity hypothesis of `L-23203` explicit for these exact
finite dictionaries.

## 4. The terminal variable is unrestricted

A one-variable terminal large side has product at least

\[
e^{(1-\delta)J-O_K(1)}.
\tag{L-15450.9}
\]

Every truncated Möbius variable satisfies

\[
d_i\le V
\le e^{J/K+O(1)}.
\tag{L-15450.10}
\]

Since `1/K<delta<1-delta`, (L-15450.10) is exponentially smaller than
(L-15450.9). Hence a truncated variable cannot be the terminal large variable
for sufficiently large `J`.

Therefore:

- in the Heath–Brown packet, the terminal variable is `q` or one of the
  unrestricted `r_i`;
- in the finite Möbius resolvent, it is one of the unrestricted residual
  variables after its finite divisor expansion.

In every case it runs over a complete positive-integer lattice inside the
compact window. The first-crossing inequalities are automatic on the active
window once the small product (L-15450.7) is frozen; they introduce no new
terminal cutoff.

## 5. Exact terminal normal form

After combining all tuples with the same small product `A`, every terminal
signal is a finite sum of rows

\[
\boxed{
\sum_{n\ge1}
\frac{P_A(\log n)}{\sqrt{An}}
W\!\left(x-\log(An)\right),}
\tag{L-15450.11}
\]

where:

1. `W=H^[K+1]` is the common high-order safe window;
2. `A<=e^(delta J+C)`;
3. `P_A` has degree at most `K`;
4. all coefficient signs remain the exact Möbius/binomial signs until this
   terminal grouping is complete.

For the original Heath–Brown tuples the degree is in fact at most one, because
there is only one `log` factor. The larger bound permits finite complexity
substitutions and is matched by the `K+1` half-pole moments of `W`.

## 6. Coefficient mass of the small packet

At fixed `K`, the number of tuple representations of one small product `A` is
bounded by

\[
d_{2K}(A).
\]

The binomial and logarithmic coefficient word is at most polynomial in `J`.
Thus, uniformly over all terminal types,

\[
\max_A
\log\left(
1+|c_A|\,\|P_A\|_{\rm coeff}
\right)=o_K(J).
\tag{L-15450.12}
\]

There are at most `e^(delta J+C)` possible small products. Consequently

\[
\boxed{
\sum_A |c_A|
\max_{J\le x\le J+1}\mathcal P_{A,x}
\le e^{(\delta+o_K(1))J},}
\tag{L-15450.13}
\]

with `mathcal P` as in `L-15449.11`.

This uses only the fixed-order divisor bound; no cancellation is spent in
(L-15450.13).

## 7. Terminal closure

Apply `L-15449` to every row in (L-15450.11), then use
(L-15450.13). One obtains

\[
\boxed{
\sup_{J\le x\le J+1}
|\mathcal T_{K,\rm term}(x)|
\le
\exp\left[-\left(\frac12-\delta-o_K(1)\right)J\right],}
\tag{L-15450.14}
\]

and

\[
\boxed{
E_{K,\rm term}(J)
\le
\exp\left[-\left(1-2\delta-o_K(1)\right)J\right].}
\tag{L-15450.15}
\]

Hence the complete terminal family satisfies `STC(K)` with exponent

\[
\boxed{\eta_K=0.}
\tag{L-15450.16}
\]

No positive-Hankel interpolation or terminal Selberg forcing estimate is needed
for these rows.

## 8. Shifted-boundary and transition rows

All truncations `d_i<=V` occur inside the small product. Their boundaries alter
only the finite coefficient `c_A` and are already included in
(L-15450.12)--(L-15450.13).

An internal first-crossing boundary has one of two outcomes:

1. it is absorbed into a reduced-complexity packet and therefore disappears
   after the finite induction of Section 3;
2. it fixes a product below `e^(delta J+O_K(1))` and is included in the small
   packet `A`.

The unrestricted terminal variable itself has no artificial boundary. Its
active range is cut only by the common compact window and is therefore exactly
the lattice row treated by `L-15449`.

Thus no unnamed terminal transition residual remains.

## 9. Consequence for the full packet proposal

The open theorem `CP(K)` on PR #158 contained four qualitatively different
burdens:

```text
reduced-complexity Type I,
terminal Type I,
cutoff/transition rows,
balanced Type II.
```

The finite complexity induction plus (L-15450.15) remove the middle two burdens.
Reduced-complexity rows are bookkeeping once their exact destination is emitted.
The sole independent analytic obligation is now the signed balanced Type-II
normal-energy estimate.

This sharpened proposal is stated in `T-15415`.

## 10. Independent-review targets

1. Check that the declared complexity is decreased by every same-scale Type-I
   regrouping.
2. Verify that `K>1/delta` excludes all truncated variables from the terminal
   large side.
3. Check that every terminal unrestricted variable has a complete lattice range
   on the active compact window.
4. Recompute the divisor-order coefficient mass in (L-15450.13).
5. Audit the absence of a hidden large-variable cutoff in Section 8.

Failure of one of these points reopens the terminal family but does not restore
the rejected Farey proof.

## 11. Proof boundary

Closed here, subject to independent review:

- a well-founded exact terminal reduction;
- the unrestricted-variable normal form;
- all terminal and terminal-transition energy bounds.

Still open:

- the centered balanced Type-II estimate;
- its vanishing-rate recurrence;
- RH.
