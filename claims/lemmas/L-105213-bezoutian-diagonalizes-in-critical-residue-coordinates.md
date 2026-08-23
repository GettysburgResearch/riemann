# L-105213 — The reverse–Rolle Bezoutian diagonalizes exactly in critical-residue coordinates

Claim ID: `L-105213`  
Status: **PROVED EXACT FINITE-POLYNOMIAL THEOREM**  
Created: 2026-08-23  
Depends on: `L-104500`, `L-104510`, `R-105202`  
RH status: **not assumed**

Let `p` be a real polynomial of degree `n>=2`. Assume that every zero

\[
c_1,\ldots,c_{n-1}
\]

of `p'` is simple and that `p(c_j)\ne0`. Put

\[
\rho_j={p(c_j)\over p''(c_j)}.
\tag{L-105213.1}
\]

Define the symmetric Bezoutian kernel

\[
\boxed{
\mathscr B_p(x,y)
={p(x)p'(y)-p'(x)p(y)\over x-y},
}
\tag{L-105213.2}

with its diagonal value defined by continuity:

\[
\mathscr B_p(x,x)=p'(x)^2-p(x)p''(x).
\tag{L-105213.3}
\]

## 1. Exact residue factorization

The rational function `p/p'` has polynomial part of degree one. Comparing at
infinity gives

\[
{p(z)\over p'(z)}
={z\over n}+b+
\sum_{j=1}^{n-1}{\rho_j\over z-c_j}
\tag{L-105213.4}
\]

for one real constant `b`. Therefore

\[
\boxed{
\begin{aligned}
\mathscr B_p(x,y)
={}&{1\over n}p'(x)p'(y)\\
&-\sum_{j=1}^{n-1}
\rho_j
{p'(x)\over x-c_j}
{p'(y)\over y-c_j}.
\end{aligned}
}
\tag{L-105213.5}

All apparent singularities are removable. At `x=c_j`, the corresponding
feature has value `p''(c_j)`.

A direct proof avoiding partial fractions is also immediate. The right side of
(L-105213.5) has the same value as `mathscr B_p` whenever `x=c_j`; their
difference is divisible by `p'(x)`. Symmetry and the leading coefficient then
force the remaining factor to vanish.

## 2. Critical-point diagonalization

For distinct critical points,

\[
\boxed{
\mathscr B_p(c_i,c_j)=0
\qquad(i\ne j),
}
\tag{L-105213.6}

while

\[
\boxed{
\mathscr B_p(c_j,c_j)
=-\rho_jp''(c_j)^2
=-p(c_j)p''(c_j).
}
\tag{L-105213.7}

Thus the restriction of the Bezoutian to the critical-point packet is already
diagonal. A positive residue is literally one negative diagonal pivot; no
first/second moment or coherence averaging is needed to detect it.

## 3. Exact inertia

The `n` polynomials

\[
p'(x),
\qquad
{p'(x)\over x-c_1},\ldots,
{p'(x)\over x-c_{n-1}}
\]

are linearly independent. Indeed, evaluating a linear relation at the
critical points eliminates every coefficient except the corresponding one.
Hence (L-105213.5) is a congruence diagonalization with diagonal coefficients

\[
{1\over n},
\qquad
-\rho_1,\ldots,-\rho_{n-1}.
\tag{L-105213.8}
\]

Consequently

\[
\boxed{
\operatorname{ind}_-(\mathscr B_p)
=\#\{j:\rho_j>0\}.
}
\tag{L-105213.9}

By the exact reverse–Rolle conservation theorem `L-104500`, the right side is
the wrong-extremum count and

\[
\boxed{
2\operatorname{ind}_-(\mathscr B_p)
=N_{\rm nr}(p).
}
\tag{L-105213.10}

Thus the nonreal root pairs, lower-half-plane companion index, wrong extrema,
positive derivative-ratio residues and negative Bezoutian squares are five
exact coordinates of one finite defect.

## 4. Hermite–Biehler companion kernel

For `lambda>0`, put

\[
E_{\lambda,p}=p-i\lambda p'.
\]

On real nodes,

\[
\boxed{
{E_{\lambda,p}(x)\overline{E_{\lambda,p}(y)}
 -\overline{E_{\lambda,p}(x)}E_{\lambda,p}(y)
 \over2\pi i(x-y)}
={\lambda\over\pi}\mathscr B_p(x,y).
}
\tag{L-105213.11}

Hence the de Branges/Hermite–Biehler kernel has exactly
`N_nr(p)/2` negative squares, agreeing with the lower-half-plane zero count in
`L-104510`.

## 5. Meaning for the Xi programme

The sharp real-critical gate is pointwise:

\[
\boxed{
\rho_c\le0
\quad\Longleftrightarrow\quad
\mathscr B_F(c,c)\ge0.
}
\]

A global coherence condition is only one sufficient way of forcing all these
signs. It is not intrinsic. For an entire function in a finite window, the
only additional object absent from (L-105213.5) is an explicit Cauchy boundary
remainder; `L-105214` isolates it exactly.
