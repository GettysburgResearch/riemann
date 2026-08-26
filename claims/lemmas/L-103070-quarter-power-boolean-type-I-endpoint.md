# L-103070 — The quarter-power Boolean cutoff leaves a subpower complete Type-I row

Claim ID: `L-103070`  
Status: **PROVED EXACT ENDPOINT EXTENSION OF THE FROZEN TYPE-I THEOREM**  
Created: 2026-08-26  
Depends on: `L-102747`, `L-102880`, `L-102953`, `L-106080`  
RH status: **not assumed**

Work on one dyadic physical block

\[
Y\le X<2Y.
\]

Partition the canonical equal-pair owner products into dyadic blocks

\[
A\le P<2A.
\]

For one such block put

\[
Z_{Y,A}=\frac{2Y}{A},
\qquad
V_{Y,A}=\left\lfloor Z_{Y,A}^{1/4}\right\rfloor .
\tag{L-103070.1}
\]

The cutoff is frozen on the complete `(Y,A)` source block. It is selected
before the physical observation and is not part of the detector.

## 1. The squarefree lattice estimate is uniform in the cutoff

For an owner/exclusion set `R`, the frozen squarefree lattice theorem gives

\[
\mathscr L_{K,\mathrm{sf}}^{(R)}(Z)
=
\sum_{\substack{k\ge1\\(k,R)=1}}
\frac{\mu(k)}{k^2}
\mathscr L_K^{(R)}(Z/k^4)
\]

and

\[
\boxed{
\left|\mathscr L_{K,\mathrm{sf}}^{(R)}(Z)\right|
\ll
Y^{o(1)}Z^{-1/4}.
}
\tag{L-103070.2}
\]

The proof of `L-102953` uses no special property of the historical choice
`U=Y^(1/6)`. For any integer cutoff `V`, the complete Boolean Type-I row
therefore satisfies

\[
\boxed{
\left|\mathcal T_{V,\mathrm{sf}}^{K,(R)}(W)\right|
\ll
Y^{o(1)}
W^{-1/4}
\left(\sum_{d\le V}d^{-1/2}\right)^2
\ll
Y^{o(1)}V W^{-1/4}.
}
\tag{L-103070.3}
\]

The estimate is Hilbert-valued and remains valid after every inherited
owner, equal-pair, marked-`67`, carrier, shell, gauge and regional projection.
All these operators commute with the square shifts in (L-103070.2).

## 2. Quarter-power endpoint

For

\[
P\in[A,2A),
\qquad
X\in[Y,2Y),
\]

the core scale obeys

\[
\frac{Y}{2A}
<
\frac XP
<
\frac{2Y}{A}.
\tag{L-103070.4}
\]

Using (L-103070.1),

\[
\begin{aligned}
V_{Y,A}\left(\frac XP\right)^{-1/4}
&\le
\left(\frac{2Y}{A}\right)^{1/4}
\left(\frac{Y}{2A}\right)^{-1/4}\\
&=\sqrt2.
\end{aligned}
\]

Hence

\[
\boxed{
\left|\mathcal T_{V_{Y,A},\mathrm{sf}}^{K,(R)}
       (X/P)\right|
\le Y^{o(1)}
}
\tag{L-103070.5}
\]

uniformly on every nonterminal owner block.

For large core horizons the finite `2 mu_V` row is inactive because `K_L` is
supported in `[1,8]` and `d<=V=O(W^(1/4))`. For bounded core horizons,
`V=O(1)` and the complete row contains only finitely many core coordinates;
the same bound follows directly. No large owner product is discarded as a
``finite terminal'' term.

## 3. Complete owner assembly

The canonical pair allocation assigns an occurrence of depth `k` equally to
its `binom(k,2)` owner pairs. `L-102747` proves that collapsing these
coordinates costs at most

\[
\binom{k}{2}\ll(\log(2Y))^2.
\]

The Type-I operator in (L-103070.3) is bounded before that collapse.
There are only `O(log Y)` dyadic owner-product blocks. Consequently the
complete quarter-power Type-I packet has

\[
\boxed{
\int_Y^{2Y}
\left|\mathcal T_{V,\mathrm{sf}}^K(X)\right|
\frac{dX}{X}
=
Y^{o(1)}.
}
\tag{L-103070.6}
\]

This is a subpower endpoint estimate, rather than the power-saving estimate
obtained from `U=Y^(1/6)`. Subpower is exactly the conclusion-facing scale.
