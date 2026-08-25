# L-103006 — The minimum-pair cycle is a positive average of symmetric Plücker rectangles

Claim ID: `L-103006`  
Status: **PROVED EXACT POSITIVE CYCLE DECOMPOSITION**  
Created: 2026-08-25  
Depends on: `L-102961`; PR #730 `T-105440--L-105451`  
RH status: **not assumed**

Fix one squarefree labelled occurrence

\[
S=\{p_1<\cdots<p_k\},
\qquad k\ge4.
\]

Let `c=(c_ij)` be the row-zero cycle component of the minimum-pair minus equal-pair owner gauge from `L-102961`.

The coefficients are

\[
\boxed{
\begin{aligned}
c_{12}&={k-3\over k-1},\\
c_{1j}=c_{2j}&=-{k-3\over(k-1)(k-2)}\qquad(j\ge3),\\
c_{ij}&={2\over(k-1)(k-2)}\qquad(3\le i<j\le k).
\end{aligned}
}
\tag{L-103006.1}
\]

For every pair `3<=i<j<=k`, define the symmetric four-label rectangle

\[
\boxed{
R_{ij}
=
2e_{12}+2e_{ij}
-e_{1i}-e_{1j}-e_{2i}-e_{2j},
}
\tag{L-103006.2}
\]

where `e_ab` is the edge basis vector. Each `R_ij` has zero row sums.

A direct coefficient count gives

\[
\boxed{
c
=
{1\over(k-1)(k-2)}
\sum_{3\le i<j\le k}R_{ij}.
}
\tag{L-103006.3}
\]

Indeed:

```text
edge 12:
  2*C(k-2,2)/((k-1)(k-2))=(k-3)/(k-1);

edge 1i or 2i:
  -(k-3)/((k-1)(k-2));

edge ij, i,j>=3:
  2/((k-1)(k-2)).
```

Thus every coefficient in the rectangle expansion is nonnegative.

## Two elementary Plücker rectangles

Each symmetric rectangle is the sum of the two bipartition rectangles

\[
R_{ij}^{(1)}
=e_{12}+e_{ij}-e_{1i}-e_{2j},
\]

\[
R_{ij}^{(2)}
=e_{12}+e_{ij}-e_{1j}-e_{2i},
\]

so

\[
\boxed{R_{ij}=R_{ij}^{(1)}+R_{ij}^{(2)}.}
\tag{L-103006.4}
\]

These are two of the three canonical four-label bipartitions in the cycle localization of PR #730. Their endpoint differences are exactly the augmentation/Plücker coordinates of `L-105451`.

## Meaning

The surviving minimum-owner cycle is not a general row-zero source. It is a positive average of one uniform family of four-label rectangles, each containing:

```text
the two minimum labels p1,p2;
one later-label pair pi,pj;
two source-exact endpoint discrepancies;
the literal middle Euler block.
```

Therefore a one-sided theorem for this symmetric rectangle family closes the complete cycle without a further cycle-space Cauchy loss.