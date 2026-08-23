# T-105231 — Weighted spectral exterior-square extinction frontier

Claim ID: `T-105231`  
Status: **PROVED EXACT IMPLICATION; Xi centered spectral estimate open**  
Created: 2026-08-23  
Depends on: `L-105222`, `L-105225`, `L-105226`; PR #724 `L-105212`  
RH status: **unproved**

## 1. The exact spectral port

At one derivative step and one centre \(a\), retain the notation of
`L-105225`. Define

\[
\Theta_{a;k;r,s}
=
\frac{N_a\Lambda_{2r}(0)}{B_a}
\left\|L_{w,a}^{1/2}K_a^{(s)}L_{w,a}^{1/2}\right\|_{\rm op},
\qquad r+s=k-1.
\tag{T-105231.1}
\]

Call the uniform large-centre estimate

\[
\boxed{
\mathrm{WSEG105231}:
\qquad
\inf_{r+s=k-1}\Theta_{a;k;r,s}<\frac9{25}
}
\tag{T-105231.2}
\]

the **weighted spectral exterior-Gram** gate.

By `L-105225`,

\[
\frac{N_aB_a-A_a^2}{B_a}
\le
\Theta_{a;k;r,s}.
\tag{T-105231.3}
\]

Therefore `L-105222` gives the exact implication

\[
\boxed{
A_a>0
\quad\wedge\quad
\mathrm{WSEG105231}
\quad\Longrightarrow\quad
\text{no wrong extremum in }[a-1,a+1].
}
\tag{T-105231.4}
\]

This is the integrality scale. A limit
\(\Theta_{a;k;r,s}=o(1)\) is sufficient only when it is uniform enough to
cross \(9/25\) on every interval of the tail.

## 2. Trace relaxation

The stronger but sometimes easier sufficient estimate is

\[
\boxed{
\frac{\Lambda_{2r}(0)}{B_a}
\left[
N_a\operatorname{tr}(W_aK_a^{(s)})
-\mathbf w_a^TK_a^{(s)}\mathbf w_a
\right]
<\frac9{25}.
}
\tag{T-105231.5}
\]

The subtraction term is mandatory by `R-105221`.

## 3. The former two open interfaces collapse to one

`L-105226` constructs the entire de Branges moment vectors directly from
Clark sampling whenever the derivative is real-rooted and the weighted second
moment is finite. Hence a separate canonical-product exhaustion gate is not
needed on the simple stratum.

`L-105225` constructs the exact contraction from the exterior-square Fourier
bundle to the de Branges residue wedge. Hence the previously postulated
source-faithful intertwiner is now explicit.

The live low-order frontier is consequently one typed estimate:

```text
same multipole weight Omega_a;
same actual real critical points;
same curvatures Xi^(k+1)(c);
same unconditional exterior-square Xi kernel;
centered spectral norm below the 9/25 integrality threshold.
```

It contains no safe-line correction, \(p''\)-zero debt, or post-hoc
interpolation.

## 4. Composition with the derivative cascade

PR #726 supplies a summable high-derivative coherence tail. For the finite
remaining derivative prefix, suppose:

1. each already-reached derivative is simple and real-rooted;
2. \(A_a>0\) and `WSEG105231` hold uniformly for all sufficiently large
   positive and negative centres;
3. the compact-height endpoint, multiplicity, and winding ledger is closed.

Then every low-order tail contains no wrong extremum, and the exact
reverse--Rolle identities descend through the finite prefix.

This is a conditional composition, not a proof of its analytic premise.

## 5. Exact boundary

```text
finite de Branges/Fourier intertwiner        PROPOSED EXACT
direct entire Clark construction             PROPOSED EXACT
weighted spectral-to-extinction implication  PROVED EXACT
diagonal-only closure                        REFUTED
WSEG105231 fixed-low-order Xi estimate        OPEN / RH-BEARING
compact endpoint/multiplicity/winding ledger  OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
