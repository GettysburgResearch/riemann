# L-106001 — Character moments reduce semiprime squareclasses to two core-collision lines

Claim ID: `L-106001`  
Programme aliases: `LFAM1.SQUARECLASS_CHARACTER_MOMENT`, `STRESS.HYBRID_COLLISION_LINES`  
Status: **PROVED EXACT FAMILY-MOMENT AND COLLISION REDUCTION**  
Created: 2026-08-24  
Depends on: `L-106000`; PR #719 `L-102831`, `L-102868`, `L-102883--L-102885`  
RH status: **not assumed**

This theorem expands the completed Dirichlet family before any absolute
source-blind estimate. It shows exactly what character orthogonality does to
the clean CV/XD four-owner packet.

## 1. The uncompleted moment matrix

Fix an odd prime `ell`, and let `a_X(n)` be any finitely supported complex
coefficient packet with

\[
a_X(n)=0\qquad(\ell\mid n).
\tag{L-106001.1}
\]

Put

\[
V_\chi(X)=\sum_n a_X(n)\chi(n).
\tag{L-106001.2}
\]

For two scales `X_1,X_2`, define

\[
\mathcal M_\ell(X_1,X_2)
=
{1\over \ell-1}
\sum_{\chi\;(\mathrm{mod}\ \ell)}
V_\chi(X_1)\overline{V_\chi(X_2)}.
\tag{L-106001.3}
\]

Complete character orthogonality gives

\[
\boxed{
\mathcal M_\ell(X_1,X_2)
=
\sum_{\substack{n\equiv m\;(\mathrm{mod}\ \ell)\\
                 \ell\nmid nm}}
a_{X_1}(n)\overline{a_{X_2}(m)}.
}
\tag{L-106001.4}
\]

No positivity, large sieve or asymptotic theorem is used.

For any scales `X_1,...,X_r`, the matrix

\[
[\mathcal M_\ell(X_i,X_j)]_{i,j=1}^r
\]

is positive semidefinite because it is the Gram average of the character
vectors `[V_chi(X_i)]_i`.

## 2. Ramified completion remains one positive matrix form

Use the local completion vector

\[
v_\ell=
\begin{pmatrix}
1\\-\ell^{-1/2}
\end{pmatrix}
\tag{L-106001.5}
\]

and put

\[
W_\chi(X)=V_\chi(X)-\ell^{-1/2}V_\chi(X/\ell).
\tag{L-106001.6}
\]

Then

\[
\boxed{
{1\over\ell-1}\sum_\chi |W_\chi(X)|^2
=
\mathcal M_\ell(X,X)
-2\ell^{-1/2}\Re\mathcal M_\ell(X,X/\ell)
+\ell^{-1}\mathcal M_\ell(X/\ell,X/\ell).
}
\tag{L-106001.7}
\]

Equivalently, this is

\[
v_\ell^*
\begin{pmatrix}
\mathcal M_\ell(X,X)&\mathcal M_\ell(X,X/\ell)\\
\mathcal M_\ell(X/\ell,X)&\mathcal M_\ell(X/\ell,X/\ell)
\end{pmatrix}
v_\ell
\ge0.
\tag{L-106001.8}
\]

Thus the ramified carrier is recombined before the square. Estimating the
three entries separately is not part of the theorem.

The `ell`-shift in (L-106001.6) remains a two-scale completion coordinate. It
is **not** relabelled as a new largest owner and the PR #719 owner
decomposition is not rerun separately on the two completion terms.

The marked-67 source contributes only four finite local sectors. If
`e,f in {0,1}` label the two marked-prime shifts, replace `n,m` below by
`67^e n,67^f m`; every conclusion remains exact.

## 3. Clean semiprime-squareclass packet

In the clean largest-two-owner sector of PR #719, write

\[
n=P c^2,
\qquad
m=Q d^2,
\tag{L-106001.9}
\]

where

\[
P=pq,\qquad Q=rs
\]

are squarefree semiprime owner products, and assume

\[
\ell\nmid PQcd.
\]

The congruence selected by (L-106001.4) is

\[
P c^2\equiv Qd^2\pmod\ell.
\tag{L-106001.10}
\]

Put

\[
u=QP^{-1}\in\mathbf F_\ell^\times.
\]

### Nonsquare owner ratio

If

\[
\left({u\over\ell}\right)=-1,
\]

then (L-106001.10) has no solution. Hence that owner-pair sector vanishes
exactly in the complete character moment.

### Square owner ratio

If

\[
\left({u\over\ell}\right)=1,
\]

choose either square root `tau` with

\[
\tau^2=u.
\]

Then

\[
\boxed{
P c^2\equiv Qd^2\pmod\ell
\iff
c\equiv \tau d\pmod\ell
\quad\text{or}\quad
c\equiv-\tau d\pmod\ell.
}
\tag{L-106001.11}
\]

The physical squareclass correlation has become at most two *linear*
core-collision lines.

For marked-67 sectors, the local ratio is

\[
67^{\,f-e}QP^{-1},
\tag{L-106001.12}
\]

so the same square/nonsquare and two-line classification applies separately to
each of the four finite sectors.

## 4. Compatibility with the existing nonzero phases

All additive owner phases and the internal discrepancy phase of
`L-102860--L-102885` commute with (L-106001.4). On a surviving collision line,
a phase of the form

\[
e_M(\alpha c+\beta d)
\]

restricts to

\[
e_M((\pm\alpha\tau+\beta)d).
\tag{L-106001.13}
\]

Thus character orthogonality does not discard the phase cancellation already
proved in PR #719. It converts the remaining coherent packet into a hybrid
additive-multiplicative shifted-convolution problem.

## 5. The diagonal is already subpower

The `n=m` terms in (L-106001.4) are precisely the equal-product physical
energy. PR #719 `L-102883` proves that, after the exact stopped-Vaughan
decomposition and representation collapse, this diagonal is subpower.

The two-by-two completion in (L-106001.7) uses only the two fixed scales
`X` and `X/ell`; Cauchy--Schwarz in the positive moment matrix therefore
keeps its complete diagonal contribution subpower for every
`ell=X^{o(1)}`.

Accordingly the first new analytic obligation is not the diagonal. It is the
sum over:

```text
distinct owner squareclasses;
local owner ratios that are squares modulo ell;
the two linear core-collision lines;
the inherited nonzero additive phases;
the exact stopped-Vaughan coefficients.
```

## 6. Scope

The theorem proves exact reduction, not cancellation on the surviving lines.
In particular it does not infer that congruence density `1/ell` is a saving:
coefficients can concentrate coherently on one line.

The hybrid collision-line estimate is isolated in `T-106000`.
