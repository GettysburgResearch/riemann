# R-105320 — Exact saddles and root compressions do not close low-order descent for free

Claim ID: `R-105320`  
Status: **BINDING SCOPE FIREWALL**  
Created: 2026-08-23  
RH status: **unproved**

The new `105320` continuation supplies an exact finite compression theorem and
a proposed near-linear high-derivative entry. Neither may be promoted to RH
without a new low-order theorem.

## 1. The compression theorem assumes a real-rooted parent

`L-105320` begins with

\[
p(z)=\prod_j(z-x_j),
\qquad x_j\in\mathbb R.
\]

Its Hermitian root matrix, spectral pinching and Krylov compression cease to be
positive self-adjoint coordinates once the parent polynomial has nonreal
roots. In a reverse-Rolle descent this is exactly the first level where a wrong
extremum may occur.

Therefore

```text
high coherence while every parent is real-rooted
```

does not by itself cross the first non-real-rooted parent. The theorem is a
quantitative geometry **inside** the real-rooted cone, not a proof that the
cone is invariant under antiderivation.

## 2. High-tail coherence is not a cumulative budget

`L-105322` proposes

\[
\mathfrak C_m=1-o(1)
\]

uniformly for `m>=M` in a height box of size `M/log M`. At height `T`, this
removes the terminal off-real term at derivative order `O(T log T)`. It says
nothing automatic about

\[
\sum_{j<O(T\log T)}R_j(1-\mathfrak C_j)
\]

or about the endpoint/winding sum. The quantifiers may not be reversed to infer
fixed-order coherence as `T->infinity`.

## 3. The exact phase cannot be replaced by a linear lattice count

At the `m/log m` height scale, the complex saddle moves by order one. The phase
correction accumulated across the box is generally `O(T)`, not `O(1)`. The
normative count is

\[
N_m(T)
={\Theta_m(T)-\Theta_m(-T)\over\pi}+O(1),
\]

with only the coarser expansion

\[
N_m(T)={2w_mT\over\pi}+O(T).
\]

Any proof quoting an `O(1)` error after replacing `Theta_m` by `w_mx` at this
scale is invalid.

## 4. A local saddle is not enough

Existence of the solution of

\[
S_m'(u)+iz=0
\]

near `w_m` does not prove the relative Fourier asymptotic. The shifted contour
could in principle contain a competing saddle or a tail larger than the local
contribution after the latter has decayed by `exp(-c kappa_m)`. The load-bearing
claim in `L-105321` is the **global shifted-contour dominance relative to the
moving saddle**.

If that estimate fails, the near-linear entry theorem is withdrawn while the
exact finite compression theorem remains unaffected.

## 5. The quotient spectrum is a coordinate, not a variance estimate

The identity

\[
-U={1\over n}\operatorname{Pin}_C(bb^*)
\]

shows where the residue weights come from. It does not force them to be flat.
Arbitrary positive spectral measures can occur in finite rank, and the inverse
participation ratio may be as small as `1/(n-1)`. A separate Xi-specific input
is required to control the angular defect.

## 6. Boundary charge remains load bearing

The exact Xi transport retains

\[
\sum_j(B_j+W_j-1).
\]

Neither the finite compression theorem nor the high-tail saddle signs or
bounds this term. Dropping it would repeat the open-flux error already fenced
on the parent reverse-Rolle programme.

```text
finite root compression and pinching       PROPOSED EXACT
moving complex saddle                      PROPOSED ANALYTIC
near-linear high derivative entry          PROPOSED ANALYTIC
low-order coherence defect budget          OPEN
endpoint / winding budget                  OPEN
Riemann Hypothesis                         UNPROVEN
```
