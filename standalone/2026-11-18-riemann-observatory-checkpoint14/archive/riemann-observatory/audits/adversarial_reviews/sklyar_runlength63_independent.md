# Consecutive runs and bases of powers of a shift difference

Date 2026-11-17. For a Riesz basis \((e_n)_{n\ge1}\) of a Hilbert space, let \(T\) be its associated right shift \(Te_n=e_{n+1}\). Fix an integer \(k\ge1\) and a nonempty subset \(G\subseteq\mathbb N\). The family \(\phi_n=(I-T)^k e_n\), \(n\in G\), is a Riesz sequence exactly when the lengths of consecutive runs in \(G\) are bounded. In that case it is a Riesz basis of its closed span in every ordering. When the run lengths are unbounded, no ordering gives a Schauder basis of its closed span. This is an independent theorem for the sequence defined in the pinned Sklyar–Marchenko preprint. The comparison among source versions is a separate audit. [Sklyar–Marchenko v2, §2.3 and the associated shift definition](https://arxiv.org/pdf/1405.2731v2)

## Bounded runs and the unilateral endpoint

Write \(e_n=V\delta_n\), with \(V\) the bounded invertible synthesis map from \(\ell^2(\mathbb N)\), and let \(S_+\delta_n=\delta_{n+1}\). Then \(T=VS_+V^{-1}\), so it suffices to work in the orthonormal model. For every finitely supported coefficient sequence \(c\) supported in \(G\),
\[
 \sum_{n\in G} c_n\phi_n=V(I-S_+)^k c .
\]
This argument uses the shift associated with the starting basis. For a separately prescribed ambient shift, a permutation of the starting basis can change the subsets of physical indices that form long runs.

Let \(r\ge1\) bound the run lengths. Extend \(c\) by zero for \(n\le0\) and apply the bilateral right shift \(U\) on \(\ell^2(\mathbb Z)\). Its difference \(\Delta=I-U\) and all its powers preserve the vectors supported in \(\mathbb N\), so the \(\ell^2(\mathbb Z)\) power norms coincide with the required unilateral ones. For the first difference the energy separates exactly over maximal runs. On a run \([a,b]\) of length \(l\), its term is
\[
 |c_a|^2+\sum_{n=a+1}^{b}|c_n-c_{n-1}|^2+|c_b|^2 .
\]
The same formula applies at \(a=1\) because the zero extension gives \(c_0=0\). Distinct runs contribute to disjoint difference supports \([a,b+1]\). The displayed form is the Dirichlet tridiagonal matrix with diagonal 2 and adjacent entries \(-1\). Its sine eigenvectors have eigenvalues \(2-2\cos(j\pi/(l+1))\), \(1\le j\le l\). The least eigenvalue is at least \(\lambda_r=2-2\cos(\pi/(r+1))>0\). Therefore
\[
 \|\Delta c\|_2^2\ge\lambda_r\|c\|_2^2.
\]

For higher powers the supports from different runs can overlap. Use the positive operator \(A=\Delta^*\Delta\), with \(\Delta\) normal on the bilateral space. Put \(u_j=\langle A^jc,c\rangle=\|\Delta^j c\|_2^2\). For nonzero \(c\), all these numbers are positive because a constant bilateral \(\ell^2\) sequence is zero and \(\Delta\) is injective. Cauchy–Schwarz for \(A^{(j-1)/2}c\) and \(A^{(j+1)/2}c\) gives \(u_j^2\le u_{j-1}u_{j+1}\). Their successive ratios are nondecreasing, so \(u_k\ge u_0(u_1/u_0)^k\). Combining this with the first-difference estimate and \(\|\Delta\|\le2\) gives
\[
 \lambda_r^k\|c\|_2^2\le\|(I-S_+)^k c\|_2^2\le4^k\|c\|_2^2.
\]
If the original basis has squared Riesz bounds \(a_0,b_0\), the resulting bounds are \(a_0\lambda_r^k\) and \(b_0 4^k\). The finite-vector estimate extends the synthesis map to a bounded isomorphism from \(\ell^2(G)\) onto the closed span. The orthonormal basis of \(\ell^2(G)\) works in every ordering, which proves the corresponding ordering assertion for the sequence.

## Exact finite controls on arbitrarily long runs

A polynomial witness gives the required coordinate instability. Identify \(\delta_n\) with \(z^{n-1}\), so that \(I-S_+\) multiplies by \(1-z\). For \(m\ge1\), set \(D_m(z)=1+z+\cdots+z^{m-1}\) and let \(M_m\) be the largest coefficient of \(D_m^{k+1}\). There are \((k+1)(m-1)+1\) coefficients whose sum is \(m^{k+1}\), so \(M_m\ge m^k/(k+1)\). Take any run containing at least \((k+1)(m-1)+1\) indices starting at \(a\), and choose coefficients with polynomial
\[
 C_m(z)=z^{a-1}\frac{D_m(z)^{k+1}}{M_m}.
\]
They are supported inside the run and at least one coefficient is exactly 1. The output polynomial is exactly
\[
 (1-z)^k C_m(z)
   =\frac{z^{a-1}}{M_m}(1-z^m)^kD_m(z).
\]
The \(k+1\) shifts \(z^{jm}D_m(z)\), \(0\le j\le k\), have disjoint coefficient supports. Counting the squares of their coefficients therefore gives
\[
 \|(I-S_+)^k c^{(m)}\|_2^2
   =\frac{m}{M_m^2}\sum_{j=0}^{k}\binom{k}{j}^2
   =\frac{m}{M_m^2}\binom{2k}{k}.
\]
The norm is \(O_k(m^{1/2-k})\), which tends to zero for every \(k\ge1\). Unbounded run lengths provide such coefficients for every \(m\), even when there is no infinite run. This rules out a lower Riesz bound since the coefficient norm is at least 1.

There is also a bounded, finitely supported coordinate functional for each individual \(\phi_n\) in the orthonormal model. On a vector with coordinates \(x_j\) it is
\[
 \ell_n(x)=\sum_{j=1}^n \binom{n-j+k-1}{k-1} x_j.
\]
Its values on the difference vectors are \(\ell_n(\phi_j)=\delta_{nj}\) by formal multiplication by \((1-z)^{-k}\). Composing with \(V^{-1}\) gives the functionals for the original basis. Thus the family stays minimal in its closed span for every \(G\).

Suppose an ordering were a Schauder basis of that span. Its partial sum projections would be uniformly bounded, so their successive differences, the single-coordinate projections, would also be uniformly bounded. Apply the projection for any coefficient of size 1 in the witness \(x_m=V(I-S_+)^k c^{(m)}\). It sends \(x_m\) to the corresponding \(\phi_n\), by uniqueness of the basis coefficients or by the explicit biorthogonal functional. Every such \(\phi_n\) has norm at least \(\|V^{-1}\|^{-1}\sqrt{\binom{2k}{k}}\), while \(\|x_m\|\to0\). This is a contradiction independent of where the index lies in the ordering. In particular it is the individual projections that fail uniform boundedness, without any need to describe the ordering of run boundaries.

For a simple finite check, \(k=1\) gives the triangular coefficient vector \(D_m^2/m\), whose first difference has norm \(\sqrt{2/m}\). For a sparse check, choose \(G=\{1+j(k+1):j\ge0\}\). The canonical \(\phi_n\) have disjoint supports and common norm \(\sqrt{\binom{2k}{k}}\), so they form an orthogonal basis of their closed span in the orthonormal model. Both checks use the same unilateral endpoint convention.
