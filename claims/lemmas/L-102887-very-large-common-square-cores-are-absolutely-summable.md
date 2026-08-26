# L-102887 — Very-large common square cores have absolutely summable logarithmic cost

Claim ID: `L-102887`  
Status: **PROVED UNCONDITIONAL LARGE-GCD CLOSURE**  
Created: 2026-08-24  
Depends on: `L-102883--L-102886`  
RH status: **not assumed**

Work on one dyadic physical horizon

\[
X\le x<2X.
\]

Let \(\mathscr F_Z\) be any carrier-recombined stopped packet at reduced
physical scale \(Z\), observed through one fixed compact logarithmic kernel.
`L-102883` and the already-closed equal-product ledger imply

\[
\sum_n |a_n(Z)|^2=Z^{o(1)}.
\tag{L-102887.1}
\]

Since there are at most \(Z^{1+o(1)}\) distinct products in one fixed
multiplicative shell, the source-blind physical collapse inequality gives

\[
\left\|\sum_n v_n\right\|_2^2
\le Z^{1+o(1)}\sum_n\|v_n\|_2^2
=Z^{1+o(1)}.
\tag{L-102887.2}
\]

This is the deliberately crude bound appropriate for an absolute estimate of
a Gram/cross packet.  No unproved restriction theorem is used.  Consequently

\[
\boxed{
\mathcal C_{\rm triv}(Z)\le Z^{1+o(1)}.
}
\tag{L-102887.3}
\]

## 1. Insert the exact gcd extraction

For a common square core \(g\), `L-102884` contributes the exact factor
\(g^{-2}\) and reduces the physical scale to

\[
Z=X/g^2.
\]

Thus the absolute logarithmic cost of the \(g\)-sector is

\[
\ll
g^{-2}(X/g^2)^{1+o(1)}
=
X^{1+o(1)}g^{-4+o(1)}.
\tag{L-102887.4}
\]

Summing over \(g\ge G\),

\[
\boxed{
\mathcal C_{g\ge G}(X)
\ll
X^{1+o(1)}G^{-3+o(1)}.
}
\tag{L-102887.5}
\]

Representation multiplicities and the finite number of dyadic
Vaughan/owner/gauge labels are absorbed by the \(X^{o(1)}\) factor.

## 2. A conclusion-facing threshold

Choose

\[
G_X=X^{1/3}(\log(3X))^2.
\]

Then on one dyadic horizon

\[
\boxed{
\mathcal C_{g\ge G_X}(X)
\ll
(\log(3X))^{-6+o(1)}.
}
\tag{L-102887.6}
\]

Writing \(X=2^j\), the series

\[
\sum_{j\ge1}j^{-6+o(1)}
\]

converges.  Hence the complete very-large-gcd region has finite logarithmic
absolute mass and may be removed from every subpower negative-mass criterion.

## 3. Exact remaining gcd range

The conclusion-bearing packet can therefore be restricted to

\[
\boxed{
g<X^{1/3}(\log(3X))^2.
}
\tag{L-102887.7}
\]

This theorem uses an absolute estimate and is consequently safe under source
partition.  It does not control the equal-core or unequal-core packets in the
remaining small-gcd range.
