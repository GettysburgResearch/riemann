# L-105341 — Functional-equation folding of the oriented ratio

Claim ID: `L-105341`  
Status: **PROVED EXACT**

Assume `F(1-s)=F(s)`. Then `F'(1-s)=-F'(s)` and

\[
E_\alpha(1-s)=-E_{-\alpha}(s),\qquad
E_{-\alpha}(1-s)=-E_\alpha(s).
\]

Therefore

\[
\boxed{\mathcal M_\alpha(1-s)=\mathcal M_\alpha(s)^{-1}.}
\tag{L-105341.1}
\]

Writing `m_alpha=M_alpha'/M_alpha`, differentiation gives

\[
\boxed{m_\alpha(1-s)=m_\alpha(s).}
\tag{L-105341.2}
\]

For a rectangle with vertical sides `Re s=sigma` and `Re s=1-sigma`, the sum
of the two oriented vertical integrals is

\[
\boxed{
\int_{(\sigma)}[\Psi(s)-\Psi(1-s)]m_\alpha(s)\,ds.}
\tag{L-105341.3}
\]

For a Paley--Wiener test whose horizontal caps vanish, this is the complete
oriented explicit formula. At `alpha=0`, a further integration by parts gives

\[
\boxed{
\frac2{2\pi i}\int_{(\sigma)}
[\Psi'(s)+\Psi'(1-s)]\frac{F(s)}{F'(s)}\,ds.}
\tag{L-105341.4}
\]

The left safe line is therefore the reflected copy of the right one; no
separate shifted seam theorem is required.
