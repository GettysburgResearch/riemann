# L-97701 — Exact residual completion absorbs `r-2r^2` and `(R-A)F`

Claim ID: `L-97701`  
Status: **PROVED EXACT PAIRED-SOURCE AND RESOLVENT THEOREM**  
Created: 2026-08-18  
Depends on: `L-97700`  
RH status: **not assumed**

Let `R` be the strictly upper-triangular raw first-owner operator on the finite
rough-history DAG. Its entries are the literal coefficients `p^{-1/2}`. Let
`b` be the vector of complete grouped local `P_61` scalars and let `F` be the
native completed-parity scalar. The exact root recursion is

\[
\boxed{F+RF=b.}
\tag{L-97701.1}
\]

For an arbitrary threshold operator `A` satisfying `0<=A<=R`, define the
current

\[
\boxed{
g=(I+A)F=b-(R-A)F.
}
\tag{L-97701.2}
\]

Then

\[
\boxed{F+A F=g.}
\tag{L-97701.3}
\]

Equations (L-97701.1)--(L-97701.3) are coefficient, activation, owner and
history-parity exact.

## Positive paired-source realization

If the raw positive paired-source identity is

\[
P_v=B_v\oplus\bigoplus_w r_{v,w}S P_w,
\]

then the thresholded current is literally

\[
\boxed{
C_v=B_v\oplus\bigoplus_w(r_{v,w}-a_{v,w})S P_w
}
\tag{L-97701.4}
\]

and the recursive children are `a_(v,w) S P_w`. Their direct sum is the raw
parent. Signed observation of (L-97701.4) is exactly the nonlocal current in
(L-97701.2).

## One-prime correction

For one prime write `r=p^(-1/2)`. If an older unsigned causal packet places one
`r^2` child in the current and another `r^2` child recursively, the compulsory
unspent source is

\[
\boxed{\delta_p=r-2r^2=r(1-2r)>0.}
\tag{L-97701.5}
\]

Adding `delta_p` gives `delta_p+2r^2=r`. The cleaner one-use split with one
recursive `r^2` child has residual `r-r^2`. Both are special cases of
`(R-A)F` and neither may be omitted.

## Raw-exposure conservation

For every scalar child value `F_w`,

\[
(r-a)F_w+aF_w=rF_w.
\tag{L-97701.6}
\]

Thus contraction relocates raw signed exposure between current and recursion;
it does not reduce it. The two-node fixture `b=(0,1)`, raw edge `r`, and
threshold `a<r` gives the exact current `a-r<0`. This is the minimal separator
against any universal local one-channel positivity inference.
