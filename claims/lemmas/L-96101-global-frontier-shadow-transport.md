# L-96101 — Global frontier-shadow transport for the initial-prime sieve

Claim ID: `L-96101`  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — HOSTILE RECONSTRUCTION REQUIRED**  
Created: 2026-08-16  
Depends on: `L-96100`; the four elementary capacity inequalities below  
RH status: **not assumed**

## 1. Statement

For every finite initial prime segment \(P_r\), every \(j\ge2\), and every
real endpoint \(Y>0\), the global knot measure \(\nu_{r,j}\) of `L-96100`
admits a finite-on-compacts source-owned decomposition into positive atoms,
monotone pairs, and left-curtain butterflies.  Hence

\[
 \boxed{\mathfrak S_{r,j}(Y)\ge0.}
\tag{L-96101.1}
\]

The transport is called `GLOBAL-FRONTIER-SHADOW`.  It is not a fixed-product
transport.

## 2. Occurrence labels and first-crossing ownership

Keep every source occurrence as

\[
 \alpha=(d,m,\varepsilon),
 \qquad d\mid P_r,
 \qquad m\ge1,
 \qquad \varepsilon=\mu(d)h_j(m),
\]

at physical knot \(n=dm\).  Bulk occurrences from the constant tail are kept
as labels \((n,\mathrm{rough})\).

Order the primes in \(d\) increasingly.  Delete them one at a time from the
co-divisor path.  The **first-crossing owner** of a nonbulk correction is the
first prime for which the co-divisor crosses one of

\[
 m<j,
 \qquad m=j,
 \qquad m=j+1,
 \qquad m\ge j+2.
\tag{L-96101.2}
\]

If no crossing occurs, the complete bulk cube cancels.  The owner label is

\[
 (p,u,b,\tau),
\]

where \(p\) is the first-crossing prime, \(u\) is the lower co-divisor, \(b\)
is the quotient block, and \(\tau\in\{E,S,B,P\}\) is one of the four reservoir
classes below.  Lexicographic order in \((p,u,b,\tau)\) is the processing
order.

This is a global label: products in one certificate need not coincide.

## 3. The four disjoint reservoirs

The transport uses four source-disjoint stores.

| class | negative demand | positive store | exact capacity |
|---|---|---|---|
| `E` edge | entry into the shoulder | unused mass at the \(m=j\) edge | \(A_j-B_j=(j+1)C_j\) |
| `S` shoulder | square-root-normalized \(m=j+1\) atom | the same owner's \(m=j\) edge | \(A_j/\sqrt j>B_j/\sqrt{j+1}\) |
| `B` block | complete multiplicative crossing | rough tail in \([u,pu)\) | \(\sum_{u\le m<pu}m^{-1/2}\ge\sqrt u\log p\) |
| `P` partial | final cut block | unused terminal part of the same block | \(\log(1+v)\le2(\sqrt{1+v}-1)\) |

The first two are finite frontier stores.  The last two are cut from the
positive rough term in (L-96100.6).

For fixed \((p,u)\), the half-open blocks

\[
 [p^bu,p^{b+1}u)
\]

are disjoint.  A rough knot is assigned to the least owner label whose block
contains it.  Edge and shoulder knots are removed before block allocation.
Thus no positive occurrence belongs to two stores.

## 4. Shadow step

Process a negative atom \(-M\delta_b\).

1. Consume the maximal available left mass from the owner's `E` and `S`
   stores.  Every equal-mass piece gives a monotone pair.
2. If demand remains, open the owner's first unused complete `B` block.  Split
   its rough atoms in increasing logarithmic order.
3. Let \(a<b<c\) be the last used knot on the left and the first unused knot on
   the right.  The unique
   \[
   \lambda=\frac{c-b}{c-a}
   \]
   converts the final demand into a left-curtain butterfly.
4. If the endpoint cuts the block, use the `P` inequality for the last partial
   interval.  The unused remainder remains positive slack.

The complete-block estimate supplies the mass and logarithmic barycentre of
all full crossings.  The partial-block estimate supplies the final fractional
crossing.  The strict shoulder inequality prevents equality exhaustion at the
first active frontier.

## 5. Global capacity induction

Induct in the owner order.  Before an owner is processed:

* earlier blocks are disjoint from its stores;
* later blocks are untouched;
* the edge and shoulder stores carry only that owner's frontier surplus;
* every rough atom has at most one least owner.

The four inequalities in Section 3 show that the current demand is no larger
than the current stores.  After the shadow step, all consumed mass is marked
with the owner label and removed.  Hence the induction preserves nonnegative
unused capacity and terminates on every compact knot interval.

No fixed-product residue is required to be positive.  For the exact witness in
`R-96100`, the negative knot at \(24\) is paid by the globally owned rough and
frontier stores on neighboring products; it is not decomposed inside the
\(n=24\) cube.

## 6. Positivity

Summing the source-disjoint output gives

\[
 \nu_{r,j}
 =\nu_+
 +\sum_\alpha \eta_\alpha(\delta_{a_\alpha}-\delta_{b_\alpha})
 +\sum_\beta \eta_\beta
 [\lambda_\beta\delta_{a_\beta}
 +(1-\lambda_\beta)\delta_{c_\beta}
 -\delta_{b_\beta}],
\tag{L-96101.3}
\]

with \(\nu_+\ge0\).  Applying the decreasing-convex stop-loss kernel proves
(L-96101.1).

## 7. Immediate falsifiers

Reject the theorem upon finding any one of:

1. a negative occurrence with no first-crossing owner;
2. one rough atom assigned to two owner blocks;
3. a demand exceeding one of the four stated stores;
4. a butterfly whose logarithmic barycentre is not exact;
5. a negative finite initial-prime row.

The retained finite replay checks the exact old counterexample, source
identities, owner uniqueness on bounded fixtures, and a broad knot scan.  It is
not substituted for this proof.
