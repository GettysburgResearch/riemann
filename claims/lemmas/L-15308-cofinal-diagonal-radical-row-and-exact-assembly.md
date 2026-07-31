# L-15308 — Cofinal diagonal extraction for radical rows and exact assembly

Claim ID: `L-15308`  
Title: Fixed-packet tail convergence is enough to obtain a growing cofinal packet, and exact form blocks have zero analytic assembly radius  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-k`  
Created: 2026-07-31  
Dependencies: elementary diagonal extraction; finite-dimensional form convergence; `L-14309`; `L-15306`  
Scope: the `kappa_lambda -> 0` and `delta_lambda -> 0` gates

## 1. Fixed-packet data

For every positive integer `m`, let

\[
R_{m,\lambda}
\]

be an `m`-dimensional packet obtained by localizing `m` exact global
Weil-radical vectors at support `lambda`. Let `G_(R,m,lambda)>0` be its declared
metric. Suppose a positive triangular block

\[
D_{0,m,\lambda}>0
\]

has already been certified on the visible-plus-ambient sector, as in
`L-15306`.

Let `L_(m,lambda)` denote the complete radical row into that sector. Define the
exact squared dual loss

\[
\boxed{
\kappa_m(\lambda)
=
\left\|
G_{R,m,\lambda}^{-1/2}
L_{m,\lambda}^*
D_{0,m,\lambda}^{-1}
L_{m,\lambda}
G_{R,m,\lambda}^{-1/2}
\right\|.}
\tag{L-15308.1}
\]

Let `e_m(lambda)` be any exact relative lower loss for the radical block:

\[
B_{R,m,\lambda}\succeq-e_m(\lambda)G_{R,m,\lambda}.
\tag{L-15308.2}
\]

Assume that for every fixed `m`,

\[
\boxed{
e_m(\lambda)\longrightarrow0,
\qquad
\kappa_m(\lambda)\longrightarrow0
\quad(\lambda\to\infty).}
\tag{L-15308.3}
\]

No estimate uniform in `m` is assumed.

## 2. Growing-packet diagonal theorem

There are strictly increasing integers

\[
m_j\longrightarrow\infty
\]

and an unbounded support sequence

\[
\lambda_j\longrightarrow\infty
\]

such that

\[
\boxed{
e_{m_j}(\lambda_j)\le2^{-j},
\qquad
\kappa_{m_j}(\lambda_j)\le2^{-j}.}
\tag{L-15308.4}
\]

Thus the radical packet may grow cofinally even when every available analytic
tail theorem is only fixed-rank.

### Proof

Take `m_j=j`. By (L-15308.3), for each `j` there is a threshold `Lambda_j` such
that both losses are at most `2^-j` for every `lambda>=Lambda_j`. Choose

\[
\lambda_j>\max\{\lambda_{j-1},\Lambda_j,j\}.
\]

Then (L-15308.4) holds and both sequences increase. QED.

## 3. One-functional sufficient condition

For an exact global radical `r=k+t`, the radical-tail identity gives

\[
Q(k,g)=-Q(t,g).
\]

Suppose, uniformly over the fixed `m`-packet,

\[
\left|Q(t_{\lambda,c},v)\right|
\le
\eta_m(\lambda)
\|c\|_{G_R}\|v\|_{D_0}.
\tag{L-15308.5}
\]

Then

\[
\boxed{\kappa_m(\lambda)\le\eta_m(\lambda)^2.}
\tag{L-15308.6}
\]

This is exactly the Riesz-representation definition of the dual norm. Hence
fixed-packet convergence of one complete tail functional implies the second
limit in (L-15308.3).

For the Gaussian/Hermite packets in the current repository, the external tails
decay super-Gaussianly for each fixed packet. Therefore any dual embedding whose
growth is sub-Gaussian preserves (L-15308.3). In particular, polynomial losses
from packet rank, inverse ordinary complement floors, and finite metric
conditioning are harmless.

## 4. Exact assembly has `delta=0`

Let `A_lambda` be the exact closed localized form and let

\[
R_\lambda\oplus V_\lambda\oplus E_\lambda
\]

be an exact orthogonal decomposition of its form domain. Define every block by
the exact sesquilinear pairing of `A_lambda` on those spaces. Then the block
matrix is the form itself, and

\[
\boxed{\delta_{\rm analytic,\lambda}=0.}
\tag{L-15308.7}
\]

An assembly radius is not an intrinsic fourth asymptotic theorem. It appears
only when exact pairings are replaced by finite bases, directed special-function
enclosures, quadrature, or Galerkin projections.

## 5. Directed computational diagonal

Suppose that at one exact support and packet:

1. all required finite blocks are continuous in the chosen graph/form topology;
2. the visible and ambient inequalities have strict margins;
3. a nested proof-producing discretization converges to those finite blocks.

Then, for every rational `delta>0`, a sufficiently large truncation and
sufficiently strong directed precision produce a block enclosure with total
lower-floor loss at most `delta`.

Consequently, after choosing the analytic diagonal in Part 2, choose the
discretization and precision at level `j` so that

\[
\boxed{\delta_j\le2^{-j}.}
\tag{L-15308.8}
\]

Therefore

\[
\delta_j\longrightarrow0.
\]

### Proof

Only finitely many matrix entries and Loewner inequalities occur at each fixed
level. Entrywise directed convergence implies operator-norm convergence in
finite dimension. Strict positive margins are open conditions, so they survive
all sufficiently small enclosures. Choose the enclosure radius below both the
declared margin retreat and `2^-j`. QED.

## 6. What the diagonal theorem does not solve

The theorem removes an often unnecessary demand for one tail estimate uniform
over every packet rank at once. It does **not** prove that the positive
visible-plus-ambient block required to define `D_0` exists at the selected
supports.

The order of construction must be:

1. certify the exact visible/ambient positive block at a candidate support;
2. measure the radical row in that exact triangular metric;
3. enlarge the support, or retreat to a slower rank schedule, until the dual
   loss is small;
4. only then choose numerical truncation and precision.

If the visible Schur margin collapses super-Gaussianly, fixed-packet Gaussian
tail decay need not dominate its inverse. A source-bound lower margin such as
`L-15307.8` is therefore still required.

## 7. Proof boundary

- The diagonal extraction and exact-assembly statements are unconditional.
- Fixed-packet convergence (L-15308.3) remains an analytic input.
- Current Gaussian radical-tail results establish it for fixed explicitly
  controlled packets against sub-Gaussian dual metrics; a complete
  source-bound proof for every production packet must still be recorded.
- This lemma does not establish the visible Schur margin and does not by itself
  prove RH.
