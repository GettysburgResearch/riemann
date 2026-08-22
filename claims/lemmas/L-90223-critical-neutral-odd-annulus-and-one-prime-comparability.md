# L-90223 — The CN3 scalar is an odd-squarefree width-eight annulus with only one-prime comparability

Claim ID: `L-90223`  
Status: **PROPOSED COMPLETE EXACT COMBINATORIAL NORMAL-FORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: critical-neutral source `L-90221/T-90206`; elementary two-adic switching  
Scope: exact annular source and divisor-poset geometry; no sign theorem, injection, or RH conclusion

## 1. Two-adic local coefficients

Retain

\[
 b_\star
 =(\varepsilon-\delta_2)
  *(\varepsilon-\sqrt2\,\delta_2)*\mu.
 \tag{L-90223.1}
\]

At the prime two its unnormalized local polynomial is

\[
 (1-t)^2(1-\sqrt2t).
 \tag{L-90223.2}
\]

Thus, for odd `m`,

\[
 \boxed{
 \begin{aligned}
 b_\star(m)&=\mu(m),\\
 b_\star(2m)&=-(2+\sqrt2)\mu(m),\\
 b_\star(4m)&=(1+2\sqrt2)\mu(m),\\
 b_\star(8m)&=-\sqrt2\,\mu(m),
 \end{aligned}}
 \tag{L-90223.3}
\]

and `b_star(2^a m)=0` for `a>=4`.

After critical normalization, the local polynomial is

\[
 \boxed{
 (1-z)(1-z/\sqrt2)^2
 =1-(1+\sqrt2)z
  +(1/2+\sqrt2)z^2-rac12z^3.
 }
 \tag{L-90223.4}
\]

## 2. Exact odd-annulus kernel

For real `X>=2`, define the CN3 scalar

\[
 \mathcal K_\star(X)
 =-\sum_{2\le q\le X}b_\star(q)
  (q^{-1/2}-X^{-1/2}).
 \tag{L-90223.5}
\]

Put

\[
 \boxed{
 \kappa(y)=
 \begin{cases}
 y^{-1/2}-1,&1\le y<2,\\[1mm]
 \sqrt2-(1+\sqrt2)y^{-1/2},&2\le y<4,\\[1mm]
 \sqrt2\,y^{-1/2}-1/2,&4\le y<8,\\[1mm]
 0,&y<1\text{ or }y\ge8.
 \end{cases}}
 \tag{L-90223.6}
\]

Grouping (L-90223.3) over the odd part gives

\[
 \boxed{
 \mathcal K_\star(X)
 =1-X^{-1/2}
 +\sum_{\substack{m\ge1\\m\ {m odd}}}
  \frac{\mu(m)}{\sqrt m}\,
  \kappa(X/m).
 }
 \tag{L-90223.7}
\]

### Proof

For a fixed odd `m`, set `y=X/m`.  The complete four-term contribution,
including the unit when `m=1`, is

\[
 -\sum_{a=0}^{3}
 \frac{b_\star(2^am)}{\sqrt{2^am}}
 \left(1-\sqrt{\frac{2^am}{X}}\right)
 \mathbf1_{2^a\le y}.
 \tag{L-90223.8}
\]

Substitution of (L-90223.3) gives successively

\[
 y^{-1/2}-1,
\]

\[
 \sqrt2-(1+\sqrt2)y^{-1/2},
\]

\[
 \sqrt2y^{-1/2}-1/2,
\]

and zero after all four powers have activated.  This is (L-90223.6).
The complete source includes the unit hinge `1-X^(-1/2)`; restoring the
convention that `K_star` omits `q=1` gives (L-90223.7). ∎

Because `kappa` is supported in `[1,8)`, the arithmetic sum in
(L-90223.7) is exactly

\[
 \boxed{
 \sum_{X/8<m\le X\atop m\ {m odd}}
 \frac{\mu(m)}{\sqrt m}\kappa(X/m).
 }
 \tag{L-90223.9}
\]

Only one fixed multiplicative annulus survives.

## 3. Exact sign sectors of the packet

The kernel is negative on

\[
 1<y<2
 \tag{L-90223.10}
\]

and on the first part of the next sector.  Its unique interior zero is

\[
 \boxed{
 y_0=\left(1+\frac1{\sqrt2}\right)^2
 =\frac32+\sqrt2.
 }
 \tag{L-90223.11}
\]

Thus

\[
 \kappa(y)<0\quad(1<y<y_0),
 \qquad
 \kappa(y)>0\quad(y_0<y<8),
 \tag{L-90223.12}
\]

with zeros at `y=1,y_0,8` and the declared continuous matching at the dyadic
breaks.

The sign to be transported is therefore explicit; no oscillation is hidden in
the kernel itself.

## 4. One-prime comparability theorem

Let

\[
 \mathcal A_X
 =\{m:m\text{ odd and squarefree},\ X/8<m\le X\}.
 \tag{L-90223.13}
\]

Suppose `m,n in A_X`, `m|n`, and `m!=n`.  Then

\[
 \frac nm<8.
 \tag{L-90223.14}
\]

Because both integers are odd and squarefree, `n/m` is a product of distinct
odd primes.  A product of two distinct odd primes is at least

\[
 3\cdot5=15>8.
\]

Therefore

\[
 \boxed{
 n/m\in\{3,5,7\}.
 }
 \tag{L-90223.15}
\]

In particular, the divisor poset induced on `A_X` has height at most two:
there is no strict chain

\[
 m_0|m_1|m_2
\]

inside the annulus.

Every sign-reversing divisor edge toggles exactly one of the primes `3,5,7`.
Thus the full combinatorial problem is a finite bipartite transport graph,
not an unbounded divisor lattice.

## 5. Exact flow interface

Assign node mass

\[
 w_X(m)=\frac{|\kappa(X/m)|}{\sqrt m}
 \tag{L-90223.16}
\]

and color a node by the sign of

\[
 \mu(m)\kappa(X/m).
 \tag{L-90223.17}
\]

Then `CN3` is exactly the statement that the deterministic reservoir

\[
 1-X^{-1/2}
\]

plus the positive-color mass dominates the negative-color mass.

The only intrinsic divisor edges available within the support are

\[
 m\longleftrightarrow3m,\qquad
 m\longleftrightarrow5m,\qquad
 m\longleftrightarrow7m.
 \tag{L-90223.18}
\]

Hence any divisor-respecting exact injection or max-flow proof may be posed on
this explicit height-two graph.  Failure of such a flow would be witnessed by
a cut in the same finite graph.

This does not prove that the available edges have enough capacity.  Isolated
nodes and source-specific cuts remain possible; introducing them by a signed
majorant would merely rename the Möbius annulus.

## 6. Relation to the other normal forms

The same scalar now has four exact descriptions:

```text
three-source inequality:       L-90221/T-90206;
positive divisor renewal:      L-90221;
five-coordinate cap cascade:  L-90222;
odd width-eight annulus:       this lemma.
```

The annular form is the preferred interface for the original Exact Flow
Gambit: it is the smallest genuine combinatorial network left after all
algebraic cancellations.

## 7. Proof boundary

Proved exactly:

- complete two-adic switching;
- the piecewise packet kernel;
- support in one width-eight odd annulus;
- exact sign sectors;
- height-two divisor comparability;
- restriction of every divisor edge to primes `3,5,7`.

Not proved:

- a feasible sign-absorbing flow on the annular graph;
- `CN3`;
- RH.
