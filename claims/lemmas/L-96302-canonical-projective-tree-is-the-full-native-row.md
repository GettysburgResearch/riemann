# L-96302 — Canonical projective paired-source gluing realizes the full native Möbius row

Claim ID: `L-96302`
Status: **PROPOSED COMPLETE EXACT SOURCE THEOREM — HOSTILE ATOMWISE REVIEW REQUIRED**
Created: 2026-08-16
Inputs: `L-91362`, `L-91650`, `L-94120`, `L-96301`; live source registry
RH status: **unproved**

## 1. One canonical source family

For real `X>=1`, define the positive parity-labelled source

\[
 \mathscr N_X
 =\sum_{\substack{k\le X/2\\k\ {
m squarefree}}}
 {1\over\sqrt k}\,[k,\operatorname{parity}(\mu(k))].
\]

It carries the complete canonical row vector `Q_(X/k)`.  Signed physical
observation is applied only after source coupling.  In row `j`, its observation
is exactly

\[
 \mathcal O_j(\mathscr N_X)
 =\sum_{k\le X/j}{\mu(k)\over\sqrt k}Q_{X/k}(j)
 =c_X(j).
\tag{L-96302.1}
\]

No Volterra fibre occurs in this definition.

Every squarefree colour has the unique factorization

\[
 k=d\,p_1\cdots p_t,
 \qquad d\mid P_{61},
 \qquad67\le p_1<\cdots<p_t.
\tag{L-96302.2}
\]

The label stores `d`, the ordered rough history, its first owner, parity and the
causal path.  At a rough edge `p`,

\[
 {1\over\sqrt p}{1\over\sqrt{k/p}}={1\over\sqrt k},
\]

and parity flips once.  Thus the tree changes no arithmetic coefficient.

## 2. Exact paired stopping identity

Apply the exact least-prime stopping line of `L-91362` before physical
observation.  The finite forcing and its actual oriented children are one paired
source.  At every node, the causal coefficients of `L-91650` satisfy

\[
 s_k+\sum_i\lambda_i=1,
 \qquad
 \alpha_i=p_i^{-1/2}\lambda_i,
 \qquad
 \sum_i\alpha_i<1/8.
\tag{L-96302.3}
\]

Consequently the parent incidence is spent exactly once; every recursive child
has one first owner; and the unresolved frontier has at most one eighth of the
incoming target mass and scale at most one sixty-seventh of the incoming scale.
Intermediate oriented children remain source-only.  Their known negative
`q=2` coordinate is therefore preserved as a regression rather than contradicted.

## 3. Terminal canonical leaves

A stopped current leaf has parameters `(p,y)` with `p>=67` and `1<=y<67`.
For every `d|P61`, its row coordinate is exactly

\[
 {\mu(d)\over\sqrt d}
 \left[Q_{py/d}(j)-p^{-1/2}Q_{y/d}(j)\right].
\tag{L-96302.4}
\]

This is precisely the canonical family of `L-96301`.  Its common
Target-Lorenz coupling produces a nonnegative row while preserving the complete
signed row marginal.

After `n` source-only levels, the remaining frontier has scale at most
`X/67^n`.  For fixed `X` it eventually lies below 67.  The residual full native
row in `1<=x<67` is nonnegative on every real endpoint cell: the MPFR-directed
outer certificate checks 4,355 endpoint-row pairs, and on each cell `[N,N+1]`
the row is affine in `log x`, so endpoint positivity covers the full cell.  Its
smallest strict lower bound is

\[
 0.00190798966122613211700185
\]

at endpoint 67, row 66.

## 4. Projective equality and positivity

Substitute the exact source identity only in the unresolved frontier.  At depth
`n`,

\[
 \mathscr N_X=\mathscr G_n+\mathscr F_n,
 \qquad
 M(\mathscr F_n)\le8^{-n}M(\mathscr N_X),
 \qquad
 \operatorname{scale}(\mathscr F_n)\le X/67^n.
\]

At the finite terminal depth, replace every stopped leaf by its `L-96301`
positive realization and every outer frontier source by its directed positive
row.  Linearity and one-use ownership give the exact full-row identity

\[
 \boxed{
 c_X
 =\sum_{\ell\in\mathcal L_X}\omega_\ell g_\ell
  +\sum_{u\in\mathcal O_X}\eta_u c_{x_u},
 }
\tag{L-96302.5}
\]

where every coefficient and every row on the right is nonnegative.  Hence

\[
 \boxed{c_X(j)\ge0\quad(X\ge1,\ j\ge2).}
\tag{L-96302.6}
\]

The same path coefficient is used in every component row and in every terminal
coordinate.  There is no finite/continuum comparison, physical child export,
full-child-capacity promotion, or endpoint packing slack in (L-96302.5).

## 5. Replay scope

The live registry at `X=536` checks all 327 squarefree colours and 2,473 literal
endpoint occurrences.  The hostile `(p,y)=(67,13)` leaf contains all 229
`P_61` atoms, and the endpoint 871 causal file contains all 132 active rough
weights.  The replay verifies unique factorization, owner, parity and coefficient
identities; the general proof is the factorization and source induction above,
not extrapolation from the fixture.

```text
source family                            canonical Q only
native row marginal                      exact
parent ownership                         one-use
recursive mass                           <1/8
intermediate physical observation        absent
terminal AVLT                            complete
outer native row                         directed finite
full c_X(j)>=0                            proposed complete
```
