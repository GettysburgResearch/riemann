# L-24901 — Superorder Euler purge by residual depth

Claim ID: `L-24901`  
Title: In the exact finite Möbius resolvent, every row below the top residual depth contains a complete free lattice exponentially far from its residual cutoff  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #249  
Dependencies: `L-23201`, `L-15160`; elementary product geometry  
Scope: one-sided and reflected finite-resolvent rows; does not estimate the top-top balanced corner

## 1. Expanded resolvent rows

Fix `K>=4`, an endpoint

\[
X=e^{J+O_K(1)},
\qquad
V=\lceil X^{1/K}\rceil,
\]

and the exact row

\[
\mu_V*r_V^{*j},
\qquad 0\le j<K.
\]

For `n>1`, expand each residual coefficient as

\[
r_V(n)
=-\sum_{ab=n,\,a\le V}\mu(a).
\tag{L-24901.1}
\]

An active tuple has the form

\[
N=d_0\prod_{i=1}^{j}a_ib_i,
\tag{L-24901.2}
\]

with

\[
d_0,a_i\le V,
\qquad a_ib_i>V,
\qquad e^{J-C_K}\le N\le e^{J+C_K}.
\tag{L-24901.3}
\]

The `a_i,d_0` are truncated coordinates and the `b_i` are unrestricted positive
integer lattice coordinates.

Put

\[
\ell=K-j-1.
\tag{L-24901.4}
\]

The top row is `ell=0`. This lemma treats `ell>=1`.

## 2. A residual factor lies far above its cutoff

Assume the row is active and `ell>=1`. The case `j=0` is empty for sufficiently
large `J`, because then `N=d_0<=V<<X`. Thus `j>=1`.

Since `d_0<=V`,

\[
\prod_{i=1}^{j}{a_ib_i\over V}
={N\over d_0V^j}
\ge
\exp\left({\ell J\over K}-O_K(1)\right).
\tag{L-24901.5}
\]

Consequently one index `i` satisfies

\[
{a_ib_i\over V}
\ge
\exp\left({\ell J\over Kj}-O_K(1)\right)
\ge
\exp\left({\ell J\over K^2}-O_K(1)\right).
\tag{L-24901.6}
\]

Equivalently,

\[
\boxed{
{b_i\over V/a_i}
\ge
\exp\left({\ell J\over K^2}-O_K(1)\right).}
\tag{L-24901.7}
\]

The residual support condition on this coordinate is only

\[
b_i>V/a_i.
\]

Every compact safe window at fixed `K` restricts the active `b_i` lattice to a
multiplicative interval of ratio `e^{O_K(1)}`. Equation (L-24901.7) therefore
places the residual lower cutoff exponentially outside the active lattice for
all sufficiently large `J`. After all other coordinates are frozen, the chosen
`b_i` is a complete unrestricted integer lattice variable.

Moreover,

\[
\log b_i
\ge {\ell J\over K^2}-O_K(1),
\tag{L-24901.8}
\]

so its complementary product is at most

\[
\exp\left[\left(1-{\ell\over K^2}\right)J+O_K(1)\right].
\tag{L-24901.9}
\]

## 3. Superorder window

Take the smooth safe window of `L-15160` with

\[
R_K=K^3
\tag{L-24901.10}
\]

Euler derivatives and enough half-pole moments for the fixed-order polynomial
source word. The added spline factor introduces no zero in the open
counterexample strip. For every fixed `K`, its support and norm are constants
independent of `J`.

Apply the Hilbert-valued form of `L-15160` to the complete `b_i` lattice. The
free logarithmic fraction is

\[
\eta_i\ge {\ell\over K^2}-o_K(1).
\]

The amplitude exponent in `L-15160` is therefore

\[
{1\over2}-R_K\eta_i+o_K(1)
\le
{1\over2}-K\ell+o_K(1).
\tag{L-24901.11}
\]

For `ell>=1` this is strictly negative, with a margin growing linearly in `K`.
The fixed-order divisor and coefficient mass is already included in the
summed-packet estimate.

Thus every non-top row satisfies

\[
\boxed{
\|h_{K,j}(J)\|
\le e^{-c_KJ}}
\tag{L-24901.12}
\]

for some `c_K>0`.

The vector-valued extension is immediate from the periodic-Bernoulli formula:
the derivative identity and integral remainder hold for Bochner-integrable
Hilbert-valued functions, and the scalar absolute value is replaced by the
Hilbert norm.

## 4. Reflected double packet

Apply the argument independently to the two reflected inverse factors. If a
row has depths `(j_+,j_-)` and either

\[
j_+\le K-2
\quad\text{or}\quad
j_-\le K-2,
\]

one reflected side contains the complete free lattice above. Sum that side
before taking the reflected norm. Cauchy--Schwarz against the other side and the
trivial normalized coefficient bound preserve exponential decay because the
margin in (L-24901.11) is larger than any fixed physical counting exponent.

Hence the only reflected row not closed by this lemma is

\[
\boxed{(j_+,j_-)=(K-1,K-1).}
\tag{L-24901.13}
\]

This is the top-top all-truncated Möbius corner.

## 5. Why the top row survives

At `j=K-1`, the truncated capacity is `V^K`, equal to the full output scale.
All unrestricted quotients may remain of bounded logarithmic size and every
residual factor may sit near its cutoff `a_ib_i=V`. No positive free-lattice
fraction follows from product geometry.

This is not a technical omission. The top row is the first `K`-fold Möbius
boundary tensor of `L-23006` and retains the complete fixed-logarithm Möbius
exponent by `R-23005`.

## 6. Proof boundary

Closed by this lemma, subject to review:

- exact residual expansion;
- a complete free variable for every residual-defect row;
- separation of that variable from its residual cutoff;
- exponential Euler closure with `R_K=K^3`;
- reduction of the reflected packet to the top-top corner.

Not closed:

- the reflected reserve for the top-top corner;
- the boundary-charge map;
- `RBC(K)` or RH.
