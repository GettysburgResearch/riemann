# T-105380 — Xi source endpoint and trigonometric capacity frontier

Claim ID: `T-105380`  
Status: **UNCONDITIONAL FIXED-ORDER SOURCE ENDPOINT; CRITICAL CAPACITY OPEN**  
Created: 2026-08-23  
Depends on: `T-105371`, `L-105380--L-105385`  
RH status: **unproved**

## 1. Source matrices are explicit positive-kernel moment functions

For every odd Xi derivative `F=Xi^(r)`, the regular source germ

\[
{F(z)\over F'(z)}=z\sum_{n\ge0}a_nz^{2n}
\]

is computed from the positive tilted law

\[
d\mathbb P_r(u)
\propto u^{r+1}\Phi(u)\,du.
\]

For every even derivative, the central residue

\[
\rho_0={F(0)\over F''(0)}<0
\]

is removed first, and the remaining odd germ is computed from the tilt

\[
d\mathbb P_r^{\rm ev}(u)
\propto u^{r+2}\Phi(u)\,du.
\]

The exact quotient recurrences are `L-105380--L-105381`. Thus the fixed source
matrices in `T-105371` are source-owned functions of ordinary positive moments,
not hidden zero data.

## 2. Exact first source layers

For odd derivatives, put

\[
x=\mathbb E[X],
\qquad y=\mathbb E[X^2],
\qquad z_3=\mathbb E[X^3],
\qquad X=U^2.
\]

Then

\[
a_0=1,
\qquad a_1={x\over3},
\qquad a_2={5x^2-y\over30},
\qquad
a_3={210x^3-77xy+3z_3\over2520}.
\tag{T-105380.1}
\]

In particular, both order-one source matrices are unconditionally positive.
The two order-two determinants are

\[
\det\mathsf A_2^{(0)}={5x^2-3y\over90},
\tag{T-105380.2}
\]

\[
\det\mathsf A_2^{(1)}
={35x^2y+15xz_3-42y^2\over37800}.
\tag{T-105380.3}
\]

The single concentration condition

\[
\boxed{
{\mathbb E[X^2]\over\mathbb E[X]^2}
\le{35\over27}
}
\tag{T-105380.4}
\]

pays both matrices.

For even derivatives, put

\[
h=\mathbb E[X^{-1}],
\qquad x=\mathbb E[X],
\qquad y=\mathbb E[X^2].
\]

The first source pivots are

\[
a_0^{\rm ev}={3-hx\over6},
\tag{T-105380.5}
\]

\[
a_1^{\rm ev}={15x-10hx^2+3hy\over360}.
\tag{T-105380.6}
\]

The single reciprocal concentration condition

\[
\boxed{
\mathbb E[X]\mathbb E[X^{-1}]
\le{15\over7}
}
\tag{T-105380.7}
\]

pays both even order-one source matrices.

## 3. Exact order-one boundary capacities

Assume the nonzero critical points in the symmetric window are real with
nonpositive residues and put

\[
s_c=c^{-2},
\qquad
W_c=-{2F(c)\over c^2F''(c)}\ge0.
\]

At an odd level, the complete order-one boundary gate is exactly

\[
\boxed{
\sum_cW_c\le1,
\qquad
\sum_cW_cs_c\le{x\over3}.
}
\tag{T-105380.8}
\]

At an even level it is

\[
\boxed{
\sum_cW_c\le{3-hx\over6},
\qquad
\sum_cW_cs_c
\le{15x-10hx^2+3hy\over360}.
}
\tag{T-105380.9}
\]

These formulas combine the source and critical programmes in literal scalar
inequalities at the first Stieltjes order.

## 4. Trigonometric saturation is exact at all orders

For

\[
F(z)=\sin(\omega z)
\quad\text{or}\quad
F(z)=\cos(\omega z),
\]

with the central cosine pole removed, `L-105382` proves that the complete
source Stieltjes measure equals the complete critical-residue atom measure.
For every finite symmetric window, the boundary reserve is the positive tail
of that measure. Hence every boundary matrix is positive, and the terminal
reserve tends coefficientwise to zero.

The normalized critical-capacity operator is exactly the identity at infinite
exhaustion. The trigonometric model therefore lies on the sharp boundary of
the capacity cone, not in its interior.

## 5. Unconditional real-saddle endpoint for every fixed source order

Define the fixed-order source statement:

```text
FOSP105380 — fixed-order source positivity

For every finite k there is R_k such that, for every derivative order r>=R_k
of the specified parity,

    A_k^(0)(Xi^(r)) > 0
    and
    A_k^(1)(Xi^(r)) > 0.
```

The real-line concentration theorem `L-105385` proves

\[
\boxed{
\mathrm{FOSP105380}.
}
\tag{T-105380.10}
\]

The proof uses only the positive Xi kernel and its real Mellin saddle. It does
not use the proposed moving complex saddle or any zero-location result.

The quantifier order is essential:

\[
\boxed{
\forall k\ \exists R_k,
}
\tag{T-105380.11}
\]

not `exists R for all k`.

## 6. What remains in the high tail

For every fixed order, the high-derivative source matrix eventually has strict
positive reserve. The remaining boundary inequality is exactly

\[
\boxed{
\mathsf C_{k,\Omega}^{(a)}
\preceq
\mathsf A_k^{(a)},
\qquad a=0,1,
}
\tag{T-105380.12}
\]

where `C` is formed from the actual critical locations and residues. In the
trigonometric model this is equality at full exhaustion. For Xi, proving that
the actual critical atom frame does not overfill the source space remains
open.

Thus the unresolved high-tail object is **critical-capacity matching**, not
finite-order source positivity.

## 7. Relation to the RH frontier

The clean sharp implication remains

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{OSCC105371}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105380.13}
\]

`FOSP105380` discharges the finite-order source-positivity prerequisite of
`OSCC105371` in the derivative tail, order by order. It does not prove the
critical domination, does not give one derivative level valid at every order,
and does not descend to the low Xi levels.

## 8. Exact frontier

```text
odd/even Xi origin source formulas              PROVED EXACT
order-one critical capacity formulas            PROVED EXACT
trigonometric all-order saturation               PROVED EXACT
real-saddle fixed-moment concentration           PROVED / HOSTILE REVIEW
FOSP105380 fixed-order source endpoint            PROVED
all-order source positivity at one Xi level       OPEN
actual critical capacity C<=A                     OPEN
CRVH105330                                        OPEN / SHARP
OSCC105371                                        OPEN / SHARP
Riemann Hypothesis                                UNPROVEN
```
