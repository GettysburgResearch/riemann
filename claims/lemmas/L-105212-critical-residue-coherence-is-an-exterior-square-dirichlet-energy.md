# L-105212 — Critical-residue incoherence is controlled by an exterior-square near-collision Dirichlet energy

Claim ID: `L-105212`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-23  
Depends on: `L-104522`; `L-105207`  
RH status: **not assumed**

This theorem acts directly on the real critical points of any fixed Xi
derivative.  It converts the first/second residue-moment condition into one
positive Gram-distance estimate.

## 1. Critical residues as exterior-square projections

Fix an integer `k>=0` and put

\[
F=\Xi^{(k)}.
\]

Let

\[
c_1,\ldots,c_R
\]

be distinct simple real zeros of

\[
F'=\Xi^{(k+1)}
\]

in one regular interval, and assume

\[
h_j=F''(c_j)=\Xi^{(k+2)}(c_j)\ne0.
\]

Define

\[
\rho_j={F(c_j)\over h_j}.
\tag{L-105212.1}
\]

Choose any split

\[
a+b=k,
\qquad a,b\in\mathbb Z_{\ge0}.
\]

Use the exterior vectors `omega_(a,t)` of `L-105207`, for which

\[
\langle\omega_{a,t},\omega_{b,s}\rangle
=\Lambda_{a+b}(s-t),
\qquad
\Lambda_k=F'^2-FF''.
\]

Put

\[
x_a=\omega_{a,0},
\qquad
y_j={\omega_{b,c_j}\over h_j^2}.
\tag{L-105212.2}
\]

At a critical point,

\[
\Lambda_k(c_j)=-F(c_j)F''(c_j).
\]

Therefore

\[
\boxed{
\langle x_a,y_j\rangle
={\Lambda_k(c_j)\over h_j^2}
=-\rho_j.
}
\tag{L-105212.3}
\]

Thus every derivative-ratio residue is one scalar projection of the complete
positive Xi Fourier compound.

## 2. The curvature-normalized critical Gram

Define

\[
\boxed{
K_{ij}^{(b)}
=\langle y_i,y_j\rangle
={\Lambda_{2b}(c_j-c_i)
 \over h_i^2h_j^2}.
}
\tag{L-105212.4}
\]

Then

\[
K^{(b)}\succeq0.
\]

More strongly, the complete block Gram is positive:

\[
\boxed{
\begin{pmatrix}
\Lambda_{2a}(0)&-\rho^T\\
-\rho&K^{(b)}
\end{pmatrix}
\succeq0.
}
\tag{L-105212.5}
\]

Consequently, for every real vector `q`,

\[
\boxed{
\left(\sum_{j=1}^Rq_j\rho_j\right)^2
\le
\Lambda_{2a}(0)\,q^TK^{(b)}q.
}
\tag{L-105212.6}
\]

This is an unconditional critical-point sampling inequality.  The signs of
the residues are not discarded; they occur as the cross Gram with one fixed
source vector.

## 3. Pairwise residue dispersion

For every pair `i,j`, (L-105212.3) and Cauchy--Schwarz give

\[
\boxed{
(\rho_i-\rho_j)^2
\le
\Lambda_{2a}(0)\,
\|y_i-y_j\|^2.
}
\tag{L-105212.7}

The Gram distance is explicit:

\[
\boxed{
\begin{aligned}
\|y_i-y_j\|^2
={}&\Lambda_{2b}(0)
\left({1\over h_i^4}+{1\over h_j^4}\right)\\
&-2{\Lambda_{2b}(c_j-c_i)\over h_i^2h_j^2}.
\end{aligned}}
\tag{L-105212.8}

Thus the variation of adjacent or distant residues is controlled by a literal
translation near-collision of the exterior-square Xi source.

Summing over all pairs and using the Hilbert-space variance identity,

\[
\sum_{i<j}\|y_i-y_j\|^2
=R\sum_i\|y_i\|^2
-\left\|\sum_i y_i\right\|^2,
\]

gives

\[
\boxed{
\sum_{i<j}(\rho_i-\rho_j)^2
\le
\Lambda_{2a}(0)
\left[
R\operatorname{tr}K^{(b)}
-\mathbf1^TK^{(b)}\mathbf1
\right].
}
\tag{L-105212.9}

The bracket is nonnegative because it is the complete pairwise Gram
Dirichlet energy.

## 4. Exact coherence-defect identity

Put

\[
M_1=-\sum_{j=1}^R\rho_j,
\qquad
M_2=\sum_{j=1}^R\rho_j^2.
\]

Assume `M_1>0`, so the mean residue is negative and the positive-part
convention in `L-104522` is inactive.  Then

\[
\mathfrak C={M_1^2\over RM_2}.
\]

The elementary variance identity is

\[
\boxed{
RM_2(1-\mathfrak C)
=RM_2-M_1^2
=\sum_{i<j}(\rho_i-\rho_j)^2.
}
\tag{L-105212.10}

Combining with (L-105212.9),

\[
\boxed{
1-\mathfrak C
\le
{\Lambda_{2a}(0)\over RM_2}
\left[
R\operatorname{tr}K^{(b)}
-\mathbf1^TK^{(b)}\mathbf1
\right].
}
\tag{L-105212.11}

This is a concrete same-height sufficient estimate for residue coherence.
It may be optimized over every split `a+b=k`.

## 5. New low-order target

Define `ESDE105212` to be the statement that, at the required fixed low
Xi derivative levels and regular height windows,

\[
\boxed{
\Lambda_{2a}(0)
\left[
R\operatorname{tr}K^{(b)}
-\mathbf1^TK^{(b)}\mathbf1
\right]
=o(RM_2)
}
\tag{ESDE105212}

for one admissible split `a+b=k`, together with `M_1>0`.

Then

\[
\mathrm{ESDE105212}
\Longrightarrow
\mathfrak C=1-o(1),
\]

and the residue-coherence component of the low-order reverse-Rolle descent is
closed at that level.

Unlike the original opaque moment statement, `ESDE105212` is one explicit
positive near-collision energy built from:

```text
actual real critical-point separations c_j-c_i;
actual curvatures Xi^(k+2)(c_j);
the unconditional positive-definite kernel Lambda_(2b);
and one fixed source norm Lambda_(2a)(0).
```

## 6. Scope

The theorem does not prove `ESDE105212`.  Curvature weights can be large and
critical points can cluster.  Source-blind estimates of the diagonal recover
a power loss.  The advance is the exact positive Gram coordinate in which the
remaining same-height residue-dispersion theorem must be proved.
