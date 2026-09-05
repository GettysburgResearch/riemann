# L-106611 — Residue coherence and projective edge energy control fifth-step sign transitions

Claim ID: `L-106611`  
Status: **PROVED EXACT FINITE INEQUALITIES**  
Created: 2026-08-26  
Depends on: `L-106610`; the residue-coherence coordinate of `L-105203/L-105220`  
RH status: **not assumed**

Let \(\rho_1,\ldots,\rho_M\) be nonzero real numbers and define

\[
A=\left|\sum_{j=1}^M\rho_j\right|,
\qquad
B=\sum_{j=1}^M\rho_j^2,
\qquad
\mathfrak C=\frac{A^2}{MB}.
\tag{L-106611.1}
\]

Let \(V\) be the number of adjacent sign transitions.

## 1. Coherence bound

Choose the sign of \(\sum\rho_j\). If \(G\) residues have that sign, then

\[
A\le\sum_{\text{majority}}|\rho_j|
\le\sqrt{GB}.
\]

Hence \(G\ge A^2/B=M\mathfrak C\). The minority has size at most
\(M(1-\mathfrak C)\), and a path has at most two sign-transition edges incident
to each minority vertex. Therefore

\[
\boxed{
V\le2M(1-\mathfrak C).
}
\tag{L-106611.2}
\]

Combined with `L-106610`,

\[
\boxed{
N_{\mathbb R}(F;(c_1,c_M))
\ge (2\mathfrak C-1)M-1.
}
\tag{L-106611.3}
\]

This is the sharp conclusion obtainable from only the first two unweighted
residue moments and no magnitude lower bound.

## 2. Projective edge energy

For nonzero real \(x,y\),

\[
\mathbf 1_{\{xy<0\}}
\le
\frac{(x-y)^2}{x^2+y^2}.
\tag{L-106611.4}
\]

Indeed the numerator is \(x^2+y^2-2xy\ge x^2+y^2\) when \(xy<0\).
Consequently the scale-invariant energy

\[
\boxed{
\mathfrak E_{\rm proj}(\rho)
=
\sum_{j=1}^{M-1}
\frac{(\rho_{j+1}-\rho_j)^2}
     {\rho_j^2+\rho_{j+1}^2}
}
\tag{L-106611.5}
\]

satisfies

\[
\boxed{
V\le\mathfrak E_{\rm proj}(\rho).
}
\tag{L-106611.6}
\]

Thus

\[
\boxed{
N_{\mathbb R}(F;(c_1,c_M))
\ge M-1-\mathfrak E_{\rm proj}(\rho).
}
\tag{L-106611.7}
\]

The projective energy is invariant under a common nonzero rescaling of all
residues and does not lose tiny but sign-changing critical values.

## 3. Exact fifth-derivative constants

The branch-pinned input is

\[
\liminf\frac{R_5(T,2T)}{N(T,2T)}>\frac{997}{1000}.
\]

In the regular simple regime, the coherence threshold solving

\[
\frac{997}{1000}(2\mathfrak C-1)>\frac9{10}
\]

is

\[
\boxed{
\mathfrak C>\frac{1897}{1994}
=0.9513540621\ldots .
}
\tag{L-106611.8}
\]

Equivalently, the direct projective-energy allowance is

\[
\boxed{
\limsup\frac{\mathfrak E_{\rm proj}}{N}<\frac{97}{1000}.
}
\tag{L-106611.9}
\]

Common-zero, multiplicity and finite-window charges must be subtracted from
these allowances rather than silently classified as simple residues.

## Scope

The theorem supplies two exact positive coordinates for the microscopic
fifth-step obstruction. It proves neither the \(95.1354\%\) coherence estimate
nor the \(9.7\%\) projective-energy estimate for Xi.
