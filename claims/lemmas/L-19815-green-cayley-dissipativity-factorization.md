# L-19815 — Green–Cayley dissipativity factorization

Claim ID: `L-19815`  
Title: The completed-domain contraction is exactly a Dirichlet-to-Neumann accretivity statement, with an explicit defect factorization  
Status: `PROPOSED — COMPLETE ABSTRACT FACTORIZATION; THETA ACCRETIVITY OPEN`  
Authoring agent: `gpt56-pro-09-k`  
Created: 2026-08-01  
Dependencies: the normalized plus/minus feature algebra; `L-19814`; elementary Cayley-transform identities  
Scope: the internal normalized contraction `||CKE||<=1`

## 1. Actual plus/minus feature geometry

Let `H_+` be the completed lifted plus-feature space and `Y` the observed
plus-profile space. Let

\[
C:H_+\to Y
\]

be Volterra integration in the source coordinate. Let `R>=0` be multiplication
by the raw coordinate `r=s+u`, and put

\[
K=(I-R)(I+R)^{-1}.
\tag{L-19815.1}
\]

For a raw lifted source `F`, the plus and minus integrands are

\[
g_+=(I+R)F,\qquad g_-=(I-R)F=Kg_+.
\tag{L-19815.2}
\]

Let

\[
E:Y\to H_+
\]

be the Green-minimizer lift from the observed plus profile to the lifted plus
integrand, so

\[
CE=I_Y.
\tag{L-19815.3}
\]

The observed branch transport is exactly

\[
\boxed{T=CKE.}
\tag{L-19815.4}
\]

## 2. Zeroth/first-moment parametrization

Recover the raw lift by

\[
F_y=(I+R)^{-1}Ey.
\tag{L-19815.5}
\]

Define the observed zeroth and first moments

\[
Uy=CF_y,
\qquad
Vy=CRF_y.
\tag{L-19815.6}
\]

Then

\[
U+V=I_Y,
\qquad
T=U-V.
\tag{L-19815.7}
\]

Assume first that `U` is one-to-one with dense range and that

\[
\boxed{L=VU^{-1}}
\tag{L-19815.8}
\]

is closed on `Ran U`. This is the induced Dirichlet-to-Neumann, or
first-moment, operator on the Green range: if `m=Uy` is the zeroth observed
moment, then `Lm=Vy` is the first observed moment.

Equations (L-19815.7)--(L-19815.8) imply

\[
U=(I+L)^{-1},
\qquad
V=L(I+L)^{-1},
\tag{L-19815.9}
\]

and hence the exact Cayley representation

\[
\boxed{T=(I-L)(I+L)^{-1}.}
\tag{L-19815.10}
\]

The same statement has a standard maximal-accretive linear-relation version
when `U` is not injective. The operator form is sufficient for every finite
proof object and for the completed domain whenever the zeroth moment uniquely
parametrizes the Green range.

## 3. Exact contraction defect

Direct multiplication gives

\[
\begin{aligned}
I-T^*T
={}&(I+L)^{-*}
\bigl[(I+L)^*(I+L)-(I-L)^*(I-L)\bigr]
(I+L)^{-1}\\
={}&4(I+L)^{-*}(\operatorname{Re}L)(I+L)^{-1}.
\end{aligned}
\]

Thus

\[
\boxed{
I-T^*T
=4(I+L)^{-*}(\operatorname{Re}L)(I+L)^{-1}.}
\tag{L-19815.11}
\]

Consequently

\[
\boxed{
\|CKE\|\le1
\iff
\operatorname{Re}L\succeq0.}
\tag{L-19815.12}
\]

For `y in Y`, put `m=(I+L)^{-1}y`. Then

\[
\boxed{
\|y\|^2-\|Ty\|^2
=4\operatorname{Re}\langle m,Lm\rangle.}
\tag{L-19815.13}
\]

The requested positive factorization is therefore exactly a representation

\[
\operatorname{Re}L=J^*J
\tag{L-19815.14}
\]

for an explicit theta/Volterra operator `J`.

## 4. Direct lifted anticommutator

Let

\[
A_C=C^*C.
\]

Since `CE=I`,

\[
\boxed{
I-(CKE)^*(CKE)
=E^*(A_C-KA_CK)E.}
\tag{L-19815.15}
\]

Using `K=(I-R)(I+R)^{-1}` and the commutation of `R` with `I+R`,

\[
\boxed{
A_C-KA_CK
=2(I+R)^{-1}(RA_C+A_CR)(I+R)^{-1}.}
\tag{L-19815.16}
\]

This is the exact place where the pointwise multiplier argument fails.
`|kappa|<=1` proves `I-K^2>=0` before Volterra observation, while the completed
observed defect is governed by the noncommutative anticommutator

\[
RA_C+A_CR.
\]

## 5. Identification with the theta Hankel form

At `omega=0`, after the positive diagonal normalization, the zeroth and first
moment maps are the Hankel operators

\[
M=\mathsf H_{\Psi}f,
\qquad
N=\mathsf H_{t\Psi}f.
\]

Hence

\[
4\operatorname{Re}\langle M,N\rangle
=\left\langle f,
\{\mathsf H_{\Psi},\mathsf H_{t\Psi}\}f
\right\rangle.
\tag{L-19815.17}
\]

In the multiplicative theta coordinates of `L-19814`, the same form is

\[
\boxed{
2\mathcal T^*L_R\mathcal T
+\{L_X,\mathcal T^*\mathcal T\}.}
\tag{L-19815.18}
\]

Under the exact primitive/normalization/Green-range congruence, (L-19815.18) is
`4 Re L`. A constructive completion must therefore produce

\[
\boxed{
2\mathcal T^*L_R\mathcal T
+\{L_X,\mathcal T^*\mathcal T\}
=4\mathcal J^*\mathcal J.}
\tag{L-19815.19}
\]

This is not a new RH-equivalent reformulation. It is the exact internal square
missing from the advertised `CKE` proof.

## 6. Theta dilation identity

For

\[
a_X(R)=X^{3/4}R^{1/4}h(XR),
\]

one has

\[
\boxed{
(X\partial_X-R\partial_R)a_X(R)=\frac12a_X(R).}
\tag{L-19815.20}
\]

Thus the anticommutator is tied to oppositely directed dilation generators in
the source and Volterra variables. A valid theta proof must combine
(L-19815.20), the modular endpoint condition, and the actual Green trace
condition to convert (L-19815.18) into a boundary square plus nonnegative bulk
energy.

## 7. Green stationarity is not accretivity

The Green minimizer obeys the Euler equation against the trace-zero fiber. That
condition determines the lift `E`, but does not imply `Re L>=0`:

```text
Green equation:
    stationarity of the indefinite plus-minus form along an affine trace fiber;

CKE contraction:
    nonnegativity of the minimized quotient form,
    equivalently Re L >= 0.
```

`R-19803` gives an exact two-node control satisfying Green stationarity,
trace-zero coercivity, `CE=I`, and `||K||<1`, but with `||CKE||=5`.

## 8. Proof boundary

- The Cayley representation and both defect factorizations are exact.
- They use the actual plus-profile metric rather than an unrelated lifted norm.
- They identify the theta Hankel anticommutator as the real part of the induced
  Dirichlet-to-Neumann map.
- The final theta square `J` has not been constructed.
- Therefore this lemma does not claim `||CKE||<=1`.
