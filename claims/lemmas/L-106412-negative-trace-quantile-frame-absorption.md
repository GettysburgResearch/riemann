# L-106412 — Negative-trace quantile absorption for an endpoint bank

Claim ID: `L-106412`  
Status: **PROVED EXACT FINITE LINEAR ALGEBRA**  
Created: 2026-08-24  
Depends on: the spectral theorem  
RH status: **not assumed**

Let \(G_0,G>0\) be \(d\times d\) Hermitian matrices and put

\[
\widetilde G=G_0^{-1/2}GG_0^{-1/2}.
\]

Assume the one-sided deficit estimate

\[
\operatorname{tr}(I-\widetilde G)_+\le\varepsilon d.
\tag{L-106412.1}

Fix \(0<a<1\), and let \(P_a\) be the spectral projection of
\(\widetilde G\) onto eigenvalues at least \(a\).

Every discarded eigenvalue contributes more than \(1-a\) to
\((I-\widetilde G)_+\).  Hence

\[
\boxed{
\operatorname{rank}(I-P_a)
\le\frac{\varepsilon}{1-a}d.
}
\tag{L-106412.2}

On the retained subspace,

\[
P_a\widetilde G^{-1}P_a\preceq a^{-1}P_a.
\tag{L-106412.3}

Therefore, for every \(\widetilde Q\succeq0\),

\[
\boxed{
\operatorname{tr}
\bigl(P_a\widetilde G^{-1/2}\widetilde Q
      \widetilde G^{-1/2}P_a\bigr)
\le a^{-1}\operatorname{tr}\widetilde Q.
}
\tag{L-106412.4}

In particular, if \(\varepsilon=o(1)\), then with \(a=1/2\) the frame loses
only \(o(d)\) dimensions and inversion costs at most two.  Thus a normalized
negative-trace comparison \(o(d)\) is sufficient for the endpoint frame; a
Frobenius-square or operator-norm comparison is not necessary.

This lemma is designed to consume the horizontal-bank form

\[
C_{\rm hor}=G_0+E,
\qquad
\operatorname{tr}
\bigl((G_0^{-1/2}EG_0^{-1/2})_-\bigr)=o(d),
\]

once that bank is identified source-for-source with the endpoint denominator
Gram.  It does not make that identification.
