# Generator and spectrum of the Manzur–Noor jump group

17 November 2026. This independent derivation uses the unitary step model and the exact norm established in the [director adjudication](director_manzur_noor_round8.md). I checked the primary source title, formulas (7)–(14), (20), and the hypotheses of Theorem 5.1 in arXiv:2610.03568v1. These calculations concern the group on the step subspace. The source supplies the operator and diagonal intertwining. [Archived primary PDF](../../sources/prefix_skeptic62_criteria2/manzur_noor.pdf) · [Pinned version](https://arxiv.org/pdf/2610.03568v1)

## Exact spectral antecedent

Sklyar–Marchenko already constructed the log-frequency group in Theorem 8 of arXiv:1405.2731v2. For the standard coordinate basis their \(H_1\) is the completion of finite sequences \(c=(c_1,c_2,\ldots)\) in the norm \(\big(\sum_{n\ge1}|c_n-c_{n-1}|^2\big)^{1/2}\), with \(c_0=0\). The map \(U:H_1\to H^2\) taking \(c\) to the sequence \((c_n-c_{n-1})_{n\ge1}\) is unitary. Its initial image on finite sequences has dense span, because \((I-S^*)a=0\) forces a constant disk coefficient sequence \(a\), which in \(\ell^2\) is zero. Here \(S\) in the shift identity denotes the unilateral shift. Manzur–Noor (15) gives
\[
 T_{-\tau}^*U=U\,\operatorname{diag}(n^{i\tau})
\]
on finite sequences and therefore on \(H_1\). Their model is exactly the adjoint time-reversal of the disk group. Sklyar–Marchenko's later Theorem 3.1 already treats the pure point spectrum and resolvent multiplier in this coefficient model. The proof below gives the step-coordinate realization, its direct compactness factorization, projection and metric calculations, and the arithmetic full-flow consequence. These statements carry no priority claim. [Sklyar–Marchenko, Theorem 8](https://arxiv.org/pdf/1405.2731v2) · [Sklyar–Marchenko, J. Spectr. Theory 11 (2021), Theorem 3.1](https://doi.org/10.4171/JST/344)

## Closed generator

Write \(S=\ell^2(w)\) with \(w_n=1/[n(n+1)]\) and \(b_n=f|_{[n,n+1)}\). Put \(b_0=0\), \(j_n(b)=b_n-b_{n-1}\), and \(\ell_n=\log n\). The exact transport is
\[
 (J_\tau b)_n=\sum_{k=1}^n e^{i\tau\ell_k}j_k(b)
 =e^{i\tau\ell_n}b_n-i\tau (H_\tau b)_n,\qquad
 (H_\tau b)_n=\sum_{k<n} b_k\int_{\ell_k}^{\ell_{k+1}}e^{i\tau u}\,du .
\]
The second equality is summation by parts followed by the fundamental theorem of calculus, including \(\tau=0\).

For the bound, identify \(b\) with \(g(t)=b_{\lfloor e^t\rfloor}\) in \(L^2([0,\infty),e^{-t}dt)\). For \(t\in[\ell_n,\ell_{n+1})\), \(|(H_\tau b)_n|\le\int_0^t|g(u)|\,du\). Conjugating the latter Volterra operator by multiplication by \(e^{-t/2}\) gives half-line convolution with \(e^{-v/2}1_{v\ge0}\), of \(L^1\) norm 2. Thus \(\|H_\tau\|\le2\). Write \(H=H_0\). Each coordinate of \(H_\tau b\) tends to that of \(Hb\), with \(|(H_\tau b-Hb)_n|\le2(H|b|)_n\). Dominated convergence gives \(H_\tau b\to Hb\) in \(S\).

Let \(Db=(\ell_n b_n)_n\) on \(\mathcal D(D)=\{b\in S:\sum w_n\ell_n^2|b_n|^2<\infty\}\). The diagonal unitary \(M_\tau b=(e^{i\tau\ell_n}b_n)_n\) is strongly continuous by dominated convergence. Its strong difference quotient exists on \(\mathcal D(D)\) and equals \(iDb\), using \(|e^{i\tau\ell_n}-1|\le|\tau|\ell_n\). Conversely any strong difference quotient must have coordinates \(i\ell_n b_n\), so \(b\) must lie in that domain. The formula \(J_\tau=M_\tau-i\tau H_\tau\) now gives the exact closed infinitesimal generator
\[
 \mathcal D(A)=\mathcal D(D),\qquad A=i(D-H),\qquad
 (Hb)_n=\sum_{k<n}(\ell_{k+1}-\ell_k)b_k .
\]
Closedness also follows from the closedness of the diagonal operator and the boundedness of \(H\). Its graph norm is equivalent to \(\|b\|+\|Db\|\). On this domain the separate jump identity is
\[
 j_n(Ab)=i\ell_nj_n(b).
\]
With \(\mathcal M f(s)=\int_1^\infty f(x)x^{-s-1}dx\), the same generator acts as
\[
 \mathcal M(Af)(s)=-i\left[\frac{d}{ds}\mathcal M f(s)+\frac{\mathcal M f(s)}{s}\right],
 \qquad \Re s>1/2 .
\]
This follows by differentiating the exact Mellin transport using the continuity of evaluation on \(S\). The \(1/s\) term comes from the group multiplier, including on the constant eigenvector.

## Spectrum, resolvent, and projections

For \(\lambda\notin\{i\ell_n:n\ge1\}\), define \(q_n=(\lambda-i\ell_n)^{-1}\). The jump equation for \((\lambda-A)b=c\) forces \(j_n(b)=q_nj_n(c)\). Summation by parts gives
\[
 (R_\lambda c)_n=\sum_{k\le n}q_kj_k(c)
 =q_nc_n+\sum_{k<n}(q_k-q_{k+1})c_k,
 \qquad
 R_\lambda=\operatorname{diag}(q_n)-iH\operatorname{diag}(q_nq_{n+1}).
\]
Here \(q_k-q_{k+1}=-i(\ell_{k+1}-\ell_k)q_kq_{k+1}\). Both diagonal sequences tend to zero and are bounded, since the proposed eigenvalue set is discrete and escapes to infinity. This gives a compact operator on \(S\) with bound \(d^{-1}+2d^{-2}\), where \(d=\inf_n|\lambda-i\ell_n|>0\). For \(b=R_\lambda c\) the coordinate equation yields \(iDb=\lambda b+iHb-c\in S\), so \(b\in\mathcal D(A)\). The equation has a unique solution because the prescribed jumps and \(b_0=0\) determine \(b\). This proves the resolvent formula without relying on spectral inheritance from a diagonal intertwining.

For \(u_n=(1_{k\ge n})_{k\ge1}\), one has \(u_n\in\mathcal D(A)\) and \(Au_n=i\ell_nu_n\). In the disk model \(B^{-1}u_n=(1+z+\cdots+z^{n-1})/n\), as substitution in the step formula for \(B\) shows. Hence the entire spectrum is \(\{i\log n:n\ge1\}\), with no finite accumulation point. At each of these points the resolvent integral around a small positive circle can be taken coordinatewise, because coordinate evaluation is continuous. The only term with a pole in the coordinate formula has \(k=n\). Its residue gives the rank-one Riesz projection
\[
 P_nb=j_n(b)u_n .
\]
In particular the isolated eigenvalues are algebraically simple. Since \(\|u_n\|^2=1/n\) and \(\|j_n\|^2=2n^2\), including \(n=1\), one obtains
\[
 \|P_n\|=\sqrt{2n}.
\]
The resolvent is compact at every point of its domain and fails the Hilbert–Schmidt condition. In the normalized cell basis its diagonal entries are \(q_n\), whose absolute squares have divergent sum. The bounded perturbation \(H\) itself also fails compactness: let \(b^{(N)}\) have value \(\sqrt{2N}\) on cells \(N,\ldots,2N-1\) and zero elsewhere. For \(N=3^r\) these are orthonormal, while the tail \(k\ge2N\) of \(Hb^{(N)}\) has constant value \(\sqrt{2N}\log 2\) and norm \(\log 2\).

For completeness the fixed-time operators have a different spectral set. For \(\tau\ne0\), the spectral radius formula and \(\|J_\tau^k\|=\|J_{k\tau}\|\le1+2k|\tau|\) give radius at most one. Apply the same argument to \(J_{-\tau}\) to put all spectral values on the unit circle. The eigenvalues \(e^{i\tau\log n}\) are dense there, as one can round \(e^{(2\pi k+\theta)/\tau}\) to the nearest integer along the direction \(k/\tau\to\infty\). Thus \(\sigma(J_\tau)=\mathbb T\) for every \(\tau\ne0\). The jump identity shows that exactly the displayed phases are eigenvalues, with possible coincidences. At other phases \(\lambda-J_\tau\) is injective and its range contains every \(u_n\), so the range is dense. Surjectivity would imply a bounded inverse, so these are continuous-spectrum points. At \(\tau=0\) the group element is the identity. Each \(J_\tau\) is noncompact because it is invertible on an infinite-dimensional space.

## Core and failure of basis bounds

Finite linear combinations of the \(u_n\) are exactly the finite-jump vectors. Their span contains the finitely supported cell sequences since \(u_n-u_{n+1}\) is the single cell at \(n\). Cell truncations converge in the \(D\)-graph norm and hence in the \(A\)-graph norm. The finite-jump span is therefore a graph core.

The \(u_n\) fail the Schauder basis condition in every ordering. Their uniquely prescribed coefficient functionals are the continuous \(j_n\), because \(j_n(u_m)=1_{n=m}\). If an ordering gave a Schauder basis, the partial sums would be uniformly bounded and their successive differences \(P_n\) would be uniformly bounded, contrary to the exact projection norms. In natural order the partial sums have \(\|\sum_{n\le N}P_n\|=\sqrt{N+1}\), since they replace the tail after \(N\) by \(b_N\). The unit vectors \(\sqrt n\,u_n\) also have consecutive inner product \(\sqrt{n/(n+1)}\), whose limit 1 violates the lower Riesz bound.

There is still strong subsequence approximation by the natural jump partial sums for each \(b\in S\). Summability implies \(\liminf_N |b_N|^2/N=0\), since a positive lower bound would make \(\sum w_N|b_N|^2\) dominate a harmonic series. Along a subsequence where that ratio tends to zero,
\[
 \left\|b-\sum_{n\le N}P_nb\right\|^2
 \le 2\sum_{k>N}w_k|b_k|^2+\frac{2|b_N|^2}{N+1}\longrightarrow0 .
\]
This supplies a separate convergence fact for any prescribed jump support.

## Bounded invariant forms and their limits

If a bounded positive metric \(G\) satisfies \(G\ge cI\) for \(c>0\) and \(J_\tau^*GJ_\tau=G\), its form norm makes the group unitary and gives \(\|J_\tau\|\le\sqrt{\|G\|/c}\). The known sharp value \(\sqrt{1+\tau^2}+|\tau|\) rules this out. The same obstruction applies to unitarizing one fixed \(J_\tau\) for \(\tau\ne0\) because its integer powers have these unbounded norms. There is likewise no bounded invertible similarity taking \(A\) to a skew-adjoint operator, since its generated group would then be boundedly similar to a unitary group.

Bounded injective invariant positive forms do exist when their norm is allowed to be weaker. Their characterization is explicit. Invariance and distinct frequencies give orthogonality of different \(u_n\) in the form. With \(d_n=\langle Gu_n,u_n\rangle\ge0\), the form on finite jumps is \(\sum_n d_n|j_n(b)|^2\). Applying boundedness to the unit cell \(u_n-u_{n+1}\) gives \(d_n+d_{n+1}\le\|G\|w_n\). Conversely any nonnegative sequence \(d_n\le Cw_n\) defines a bounded invariant form since
\[
 \sum_n w_n|j_n(b)|^2\le 4\|b\|^2.
\]
Density extends the diagonal formula to every \(b\in S\). Injectivity is equivalent to \(d_n>0\) for every \(n\). Coercivity fails in every case because \(d_n/\|u_n\|^2=nd_n\le C/(n+1)\). In particular \(d_n=w_n\) gives a bounded injective example. Its norm completes the jumps to an ordinary diagonal unitary model in a weaker topology. The source's relation \(\Delta T_\tau=D_\tau\Delta\) in (13) also directly yields the example \(G=\Delta^*\Delta\) on the disk.

## Consequence for invariance under the full flow

Let \(V\) be a closed subspace of \(S\) with \(J_tV\subseteq V\) for every \(t\ge0\). For \(\Re\lambda>0\), the strong integral \(R_\lambda b=\int_0^\infty e^{-\lambda t}J_t b\,dt\) exists by the group growth bound. Applying each jump functional inside the integral gives \(q_nj_n(b)\), proving the identity with the resolvent above. This makes \(R_\lambda V\subseteq V\) first on the right half-plane and then by analyticity on the connected set \(\mathbb C\setminus\{i\log n\}\). Indeed, for fixed \(b\in V\) the quotient-valued analytic function \(R_\lambda b+V\) vanishes on the right half-plane. Contour integration shows \(P_nV\subseteq V\). The subsequence approximation then gives
\[
 V=\overline{\operatorname{span}}\{u_n:u_n\in V\}
   =\{b\in S:j_n(b)=0\text{ for every }n\text{ with }u_n\notin V\}.
\]
Conversely every subspace defined by such jump constraints is invariant at every real time. Thus every vector whose jumps are all nonzero has a forward orbit of dense linear span. For the Manzur–Noor vector \(B h_k=k\lfloor x/k\rfloor-\lfloor x\rfloor\), its \(n\)-th jump is \(k1_{k\mid n}-1\) and is nonzero for every \(n\). Using the source's equivalence (A), invariance of \(\overline{\operatorname{span}}\{B h_k:k\ge2\}\) under all positive times is therefore equivalent to RH. This argument uses the whole forward flow. The primary source's criterion at a single fixed nonzero time uses additional arithmetic information. [Manzur–Noor, (A) and Theorem 5.1](https://arxiv.org/pdf/2610.03568v1)
