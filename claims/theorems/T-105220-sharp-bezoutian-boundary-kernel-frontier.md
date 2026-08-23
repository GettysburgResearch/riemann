# T-105220 — Sharp low-order Xi descent through residue pivots and one boundary Loewner kernel

Claim ID: `T-105220`  
Status: **MAJOR UNCONDITIONAL COORDINATE REDUCTION; TWO SHARP SIGN THEOREMS OPEN**  
Created: 2026-08-23  
Depends on: `R-105202`; `L-105206--L-105216`; PR #720 `L-104510--L-104521`  
RH status: **unproved**

## 1. Binding correction to the preceding frontier

`R-105202` gives an exact polynomial with five simple real zeros, no wrong
extremum, and all derivative-ratio residues negative, but

\[
R(1-\mathfrak C)>2.
\]

Thus `ESDE105212` remains a valid sufficient condition but is not the sharp or
natural last-defect theorem. It is demoted from the normative frontier. The
actual real-critical condition is simply

\[
\boxed{
\rho_c={F(c)\over F''(c)}\le0
\quad\text{at every real zero }c\text{ of }F'.
}
\tag{T-105220.1}

No averaging over different critical points is required.

## 2. Finite reverse–Rolle defect is one Bezoutian inertia

For a real polynomial, `L-105213` proves

\[
\boxed{
\begin{aligned}
\mathscr B_p(x,y)
={}&{1\over n}p'(x)p'(y)\\
&-\sum_{p'(c)=0}
\rho_c
{p'(x)\over x-c}
{p'(y)\over y-c}.
\end{aligned}
}
\tag{T-105220.2
}

The congruence coefficients are

\[
{1\over n},\quad -\rho_c.
\]

Hence

\[
\operatorname{ind}_-(\mathscr B_p)
=\#\{c:\rho_c>0\}
={N_{\rm nr}(p)\over2}.
\tag{T-105220.3}

At the critical-point packet the matrix is diagonal:

\[
\mathscr B_p(c_i,c_j)
=\delta_{ij}\left[-\rho_{c_i}p''(c_i)^2\right].
\]

This is the exact finite version of the Hermite–Biehler last-defect theorem.

## 3. The entire Xi difference is one boundary remainder

For an entire function in a regular symmetric window, `L-105214` proves

\[
\boxed{
\mathscr B_F
=\mathscr R_{F,\Omega}
-
\sum_{F'(c)=0,\ c\in\Omega}
\rho_c\,q_c\otimes q_c,
}
\tag{T-105220.4}

where

\[
q_c(x)={F'(x)\over x-c}
\]

and

\[
\boxed{
\mathscr R_{F,\Omega}(x,y)
={F'(x)F'(y)\over2\pi i}
\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)
 \over(\zeta-x)(\zeta-y)}\,d\zeta.
}
\tag{T-105220.5}

Equivalently,

\[
\mathscr R_{F,\Omega}(x,y)
=F'(x)F'(y)
{H_{F,\Omega}(x)-H_{F,\Omega}(y)\over x-y}.
\tag{T-105220.6}

Thus the complete non-polynomial obstruction is one divided-difference
Pick/Loewner kernel of the explicit boundary Cauchy transform `H_(F,Omega)`.
It is not an unspecified winding error.

The boundary term vanishes on every real critical-point row and column, so it
cannot hide a positive residue. The two last-defect alternatives are
orthogonal in the exact interpolation coordinates:

```text
positive residue       one negative diagonal Bezoutian pivot;
boundary event          one negative square of the Cauchy remainder kernel.
```

## 4. Unconditional mean and short-chord structure

`L-105207--L-105208` prove all-order exterior-square Fourier positivity and
strict mean Hermite–Biehler orientation at every fixed low derivative order.
`L-105216` strengthens the geometry by proving

\[
\mathscr B_F(x,y)
=\int_0^1
\Gamma_F((1-t)x+ty,tx+(1-t)y)\,dt
\tag{T-105220.7}

and, for `F=Xi^(k)`,

\[
\int_{\mathbb R}
\mathscr B_F(m+h/2,m-h/2)dm
=4\pi\int_{\mathbb R}
 u^{2k+2}\varphi(u)^2{\sin(hu)\over hu}du.
\tag{T-105220.8}

In particular, this center average is strictly positive for every

\[
|h|<\sqrt{
6\int u^{2k+2}\varphi(u)^2du
 \big/
 \int u^{2k+4}\varphi(u)^2du}.
\tag{T-105220.9}

So the low-order failure is neither source-level nor short-chord on average.
It is a fixed-center negative-square localization problem.

## 5. The sharp two-gate continuation

Let `F=Xi^(k)` be the last defective derivative in the exact PR #720
Hermite–Biehler descent, with the next companion zero-free in the common
regular exhaustion.

Define:

`PRES105220` — every real critical residue of `F` in the exhaustion satisfies

\[
\rho_c\le0,
\]

with common-zero and multiplicity events retained separately.

`BRP105220` — after the exact far-right/lower-boundary exhaustion, the Cauchy
boundary function `H_(F,Omega)` has a positive-semidefinite Loewner kernel

\[
{H(x)-H(y)\over x-y}
\]

on every finite real packet, and the nonreal `F'` critical correction is absent
at the last level.

Under these two hypotheses, every term on the right side of (T-105220.4) is
positive semidefinite. Since

\[
{E_{k,\lambda}(x)\overline{E_{k,\lambda}(y)}
 -\overline{E_{k,\lambda}(x)}E_{k,\lambda}(y)
 \over2\pi i(x-y)}
={\lambda\over\pi}\mathscr B_F(x,y),
\]

the complete companion kernel has no negative square. The canonical
Hermite–Biehler criterion of `L-104510`, together with the high endpoint and
exact telescope `L-105206`, gives

\[
\boxed{
\mathrm{PRES105220}
\ \wedge\
\mathrm{BRP105220}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105220.10}

Neither gate is proved.

## 6. Relation to the preceding names

```text
ESDE105212   overstrong optional sufficient condition; demoted
HLOC105210   sharpened to the explicit boundary remainder BRP105220
PRES104518   sharpened to pointwise residue pivots PRES105220
HARG104521   represented by the Cauchy-Loewner negative-square gate
```

The new frontier no longer asks benign real-rooted functions to have almost
constant residues. It asks exactly for the two defects that can create a
negative Hermite–Biehler square.

## 7. Exact boundary

```text
subunit global residue coherence as canonical gate  REFUTED
finite Bezoutian residue diagonalization             PROVED EXACT
negative index = positive residues = nonreal pairs/2 PROVED EXACT
entire-window Cauchy remainder decomposition         PROVED EXACT
all-order Fourier-compound mean orientation          PROVED
short-chord center-averaged positivity                PROVED
PRES105220 pointwise real-critical sign               OPEN / RH-BEARING
BRP105220 boundary Loewner positivity                 OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVEN
```
