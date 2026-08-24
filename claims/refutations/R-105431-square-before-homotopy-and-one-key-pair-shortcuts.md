# R-105431 — Square-before-homotopy and one-key pair shortcuts are invalid

Claim ID: `R-105431`

Status: **PROVED EXACT FINITE-DIMENSIONAL FIREWALLS**

## 1. Premature source splitting

For any \(N>0\), take

\[
p=(N,-192N),
\qquad
w=(-N,192N).
\]

Then

\[
\|p+w\|=0,
\]

while both \(\|p\|^2\) and \(\|w\|^2\) are proportional to \(N^2\).  Thus a
favorable signed carrier and an opposite Wick remainder may cancel completely,
even though either isolated positive energy is power-sized.

## 2. Pair diagonal is not physical restriction

For four labels and scalar pair vectors

\[
v_{12}=v_{34}=1,
\qquad
v_{ij}=0\ \text{otherwise},
\]

the pair diagonal is \(2\), while

\[
\left|\sum_{i<j}v_{ij}\right|^2=4.
\]

The missing contribution is the four-distinct-label intersection.

## 3. Four-label cycle alone is not enough

Take all six pair vectors equal to one.  Shared-owner star energy is nonzero and
the physical total is \(6\).  A theorem for primitive row-zero cycles does not
control this degree/star packet.

## 4. Shared-owner stars alone are not enough

The first fixture has nonzero disjoint-pair intersection.  Bounding only the
row energies cannot delete the four-label term in the exact identity

\[
\|S\|^2
=
\mathcal Q_2-\text{diagonal}+\text{star}.
\]

Therefore the star and cycle estimates in `T-105430` are genuinely conjunctive.
