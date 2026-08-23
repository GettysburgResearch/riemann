# L-105214 — The entire-window Bezoutian splits into residue pivots and one Cauchy boundary Loewner kernel

Claim ID: `L-105214`  
Status: **PROVED EXACT ENTIRE-FUNCTION IDENTITY; BOUNDARY SIGN OPEN**  
Created: 2026-08-23  
Depends on: `L-105204--L-105206`, `L-105213`; PR #720 `L-104518--L-104521`  
RH status: **not assumed**

Let `F` be entire and real on the real axis. Let `Omega` be a bounded,
conjugation-symmetric Jordan domain whose real slice contains an interval `I`.
Assume that `F'` has no zero on `partial Omega` and that every zero

\[
c\in\Omega,
\qquad F'(c)=0,
\]

is simple. Put

\[
\rho_c={F(c)\over F''(c)}
\tag{L-105214.1}
\]

and

\[
m_F(z)={F(z)\over F'(z)}.
\]

## 1. Exact Cauchy–Mittag-Leffler split

For `z in Omega` away from the critical points, define

\[
\boxed{
H_{F,\Omega}(z)
={1\over2\pi i}
\int_{\partial\Omega}
{m_F(\zeta)\over\zeta-z}\,d\zeta.
}
\tag{L-105214.2}

The residue theorem gives

\[
\boxed{
m_F(z)
=H_{F,\Omega}(z)
+\sum_{F'(c)=0,\ c\in\Omega}
{\rho_c\over z-c}.
}
\tag{L-105214.3}

This is a finite-window identity. No canonical-product exhaustion or
asymptotic interchange is used.

## 2. Exact Bezoutian decomposition

Define the entire-function Bezoutian

\[
\mathscr B_F(x,y)
={F(x)F'(y)-F'(x)F(y)\over x-y},
\tag{L-105214.4}
\]

with diagonal `F'(x)^2-F(x)F''(x)`. For real `x,y in I` avoiding critical
points, (L-105214.3) gives

\[
\boxed{
\mathscr B_F(x,y)
=\mathscr R_{F,\Omega}(x,y)
-\sum_{F'(c)=0,\ c\in\Omega}
\rho_c
{F'(x)\over x-c}
{F'(y)\over y-c},
}
\tag{L-105214.5}

where the complete boundary remainder is

\[
\boxed{
\begin{aligned}
\mathscr R_{F,\Omega}(x,y)
&=F'(x)F'(y)
{H_{F,\Omega}(x)-H_{F,\Omega}(y)\over x-y}\\
&={F'(x)F'(y)\over2\pi i}
\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)
 \over(\zeta-x)(\zeta-y)}\,d\zeta.
\end{aligned}
}
\tag{L-105214.6}

Conjugate critical points pair, so the full kernel is real symmetric on real
packets even when nonreal critical points are present.

## 3. Real critical points are exact diagonal pivots

Let `c_1,...,c_R` be the real critical points in `I`. The boundary remainder
contains a factor `F'(x)F'(y)` and is analytic at every `c_j`. Hence

\[
\mathscr R_{F,\Omega}(c_i,c_j)=0.
\tag{L-105214.7}

Every nonmatching residue feature also vanishes. Therefore

\[
\boxed{
\mathscr B_F(c_i,c_j)
=0\quad(i\ne j),
\qquad
\mathscr B_F(c_j,c_j)
=-\rho_{c_j}F''(c_j)^2.
}
\tag{L-105214.8}

The Levinson boundary remainder cannot hide or compensate a positive residue
on the critical-point packet. The `PRES` alternative is exactly the sign of
these diagonal pivots.

## 4. The boundary event is one Loewner kernel

The factor multiplying `F'(x)F'(y)` in (L-105214.6) is the divided-difference
kernel

\[
\boxed{
\mathscr L_{H,\Omega}(x,y)
={H_{F,\Omega}(x)-H_{F,\Omega}(y)\over x-y}.
}
\tag{L-105214.9}

Thus the whole non-residue obstruction is one concrete Pick/Loewner question
for the Cauchy boundary function `H_(F,Omega)`.

If:

1. every critical point of `F'` in the relevant exhaustion is real;
2. every real residue satisfies `rho_c<=0`; and
3. the boundary Loewner kernel (L-105214.9) has no negative square,

then every term on the right of (L-105214.5) is positive semidefinite. The
Hermite–Biehler kernel of `F-i lambda F'` is therefore positive under the
canonical exhaustion, and the lower-half-plane companion index vanishes by
the criterion used in `L-104510`.

The third item is the exact kernel version of the horizontal
Levinson/`HARG` difficulty. It is not proved here.

## 5. Polynomial outer-window check

For a polynomial `p`, take an outer contour containing every critical point.
Then

\[
H_{p,\Omega}(z)={z\over n}+b,
\]

so

\[
\mathscr R_{p,\Omega}(x,y)={1\over n}p'(x)p'(y)\succeq0.
\]

Equation (L-105214.5) reduces exactly to the finite diagonalization
`L-105213.5`. Thus the classical polynomial reverse–Rolle theorem has no
separate boundary obstruction; the entire Xi problem differs from it by the
single explicit Cauchy remainder (L-105214.6).

## 6. Scope

This theorem does not prove that the boundary remainder is positive, does not
justify an unbounded Xi exhaustion, and does not exclude nonreal critical
points at a fixed low derivative order. Its contribution is to replace the
vague height-localization gate by one literal Cauchy–Loewner kernel whose
negative squares can be reviewed and attacked independently of the exact
residue pivots.