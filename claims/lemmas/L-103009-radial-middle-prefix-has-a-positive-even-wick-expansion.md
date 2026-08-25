# L-103009 — The radial middle prefix has a positive even-Wick expansion

Claim ID: `L-103009`  
Status: **PROVED EXACT ALL-CHAOS SOURCE IDENTITY**  
Created: 2026-08-25  
Depends on: `L-103008`  
RH status: **not assumed**

Let

\[
H_R=\int_0^1\prod_{r\in R}(1-tx_r)\,dt
\]

be the radial middle prefix on a finite labelled set `R`.

Put

\[
m_r=1-x_r/2,
\qquad
y=t-1/2.
\]

Then

\[
1-tx_r=m_r-yx_r.
\]

Expanding the finite product and integrating `y` uniformly on `[-1/2,1/2]` gives

\[
H_R
=
\sum_{S\subseteq R}
(-1)^{|S|}
\left[
\int_{-1/2}^{1/2}y^{|S|}\,dy
\right]
x_S
\prod_{r\notin S}m_r.
\]

Every odd moment vanishes. For `|S|=2j`,

\[
\int_{-1/2}^{1/2}y^{2j}\,dy
={1\over(2j+1)2^{2j}}.
\]

Therefore

\[
\boxed{
H_R
=
\sum_{\substack{S\subseteq R\\|S|\text{ even}}}
{1\over(|S|+1)2^{|S|}}
\,x_S
\prod_{r\notin S}(1-x_r/2).
}
\tag{L-103009.1}
\]

Every coefficient in this expansion is nonnegative.

## 1. Exact chaos structure

The empty subset gives the arithmetic midpoint prefix

\[
\prod_{r\in R}(1-x_r/2).
\]

Every nonempty term has even degree at least two. In particular:

```text
all odd centered chaoses vanish exactly;
the first correction is one positive unordered-pair current;
every higher correction is a positive even-owner current;
all corrections retain the same midpoint factors on unselected labels.
```

The pair coefficient is `1/12`, agreeing with the Peano formula in `L-103008`.

## 2. Source ownership

For each even subset `S`, the occurrence is owned by the literal selected labels in `S`; no owner is chosen after physical observation. Equal allocation among the unordered pairs of `S` recovers the canonical Duhamel pair gauge at a cost bounded by `O(log^2 Y)` on the physical horizon.

Thus every nonempty row belongs to the established all-chaos equal-pair/Boolean source hierarchy.

## 3. Hodge interpretation

Since

\[
1-x/2=M(x)+x^2/2,
\qquad
M(x)=1-x/2-x^2/2,
\]

the empty row is the unique harmonic midpoint modulo primewise squared transfer.

Consequently the complete radial prefix has only two critical coordinate types:

```text
the harmonic midpoint;
positive even-owner currents generated from that midpoint.
```

There is no independent odd, gauge, or endpoint-color current.

## Boundary

Positive coefficients in the Wick expansion do not orient the signed midpoint source or the physical collapse of its even-owner currents. The conclusion-bearing remainder remains `BCI102990`.