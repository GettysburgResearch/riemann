# L-23202 — High-order fixed-ratio Mertens differences retain the full RH exponent

Claim ID: `L-23202`  
Title: Every finite order of the geometric `2/3` difference is RH-equivalent, while the first Farey cell supplies only the scalar first rung  
Status: **CORE VERIFIED BY REVIEW WITH NOTATION AND INTERFACE FIXES**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Corrected: 2026-08-07 after review of frozen PR #233  
Issue: #232  
Dependencies: PR #229 `L-23003/T-23002`; the classical Mertens criterion  
Scope: scalar RH equivalence, not a packet estimate or decoder

## 1. Geometric differences

Extend

\[
M(x)=\sum_{n\le x}\mu(n)
\]

by `M(x)=0` for `0<=x<1`.  Put

\[
c=\frac23,
\qquad
(T_cF)(x)=F(cx),
\qquad
\Delta_c=I-T_c.
\]

For every integer `m>=1`, define

\[
G_m(x)=\Delta_c^mM(x)
=
\sum_{r=0}^{m}(-1)^r{m\choose r}M(c^rx).
\tag{L-23202.1}
\]

All real arguments are interpreted through the defining floor in `M`.

## 2. Exact pointwise inversion

For fixed `x`, `T_c^jM(x)=0` once `c^jx<1`.  Hence the formal binomial series
terminates pointwise and gives

\[
\boxed{
M(x)
=
\sum_{j\ge0}{m+j-1\choose j}G_m(c^jx),
}
\tag{L-23202.2}
\]

where the sum is finite at every `x`.

## 3. RH equivalence

For every fixed `m>=1`, the following are equivalent:

1. RH;
2. for every `epsilon>0`,
   \[
   G_m(x)=O_{m,\epsilon}(x^{1/2+\epsilon});
   \tag{L-23202.3}
   \]
3. for every `epsilon>0`,
   \[
   \boxed{
   |G_m(x)|^2/x=O_{m,\epsilon}(x^\epsilon).
   }
   \tag{L-23202.4}
   \]

The third formulation is an upper bound; it is not a two-sided assertion
`x^{o(1)}` and remains valid when `G_m` vanishes.

RH implies (L-23202.3) from the classical Mertens formulation.  Conversely,
substitution into (L-23202.2) gives

\[
|M(x)|
\ll_{m,\epsilon}
 x^{1/2+\epsilon}
 \sum_{j\ge0}{m+j-1\choose j}c^{j(1/2+\epsilon)}.
\]

The series converges, so the Mertens criterion gives RH.

## 4. First critical Farey cell

For integer `D`, PR #229 proves

\[
\boxed{
B_{D,1}
=
\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
\left[M(D)-M(\lfloor2D/3\rfloor)\right].
}
\tag{L-23202.5}
\]

Thus the first cell is the scalar `m=1` member of the hierarchy.  Applying
finite differences to the scalar function `D -> B_(D,1)` produces the
corresponding scalar geometric differences, with floors retained at every
cutoff.

No exact map is asserted here from `G_m` to the terminal or balanced
Heath--Brown packet families.  Such a decoder must be constructed separately if
used in a machine certificate.

## 5. Audit role

The scalar hierarchy is a proof firewall.  It shows that the coherent low
Farey mode already carries the full square-root Möbius-cancellation burden.
Therefore a proposed prime or Type-II proof that takes generic operator norms,
removes low cells, or forgets the actual signed arithmetic vector is
insufficient.

This firewall is logical, not an already exported finite packet mutation.

## 6. Proof boundary

Verified by the review:

- exact pointwise inversion;
- equivalence with the Mertens formulation of RH;
- the inherited first-cell identity.

Open:

- any bound for `G_m`;
- a packet-level decoder into `G_m`;
- the balanced Type-II theorem;
- RH.