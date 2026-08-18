# L-98100 — A slowly growing complete rough cube has subpower remainder

Claim ID: `L-98100`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Frozen base: PR #599 at `8daa0a5d94de56c68a1ce710824b26cacc1a9bbc`  
RH status: **not assumed**

Use the normalized complete `P_61` scalar base from PR #599:

\[
u(Y)={b(Y)\over\sqrt Y}=a_*+e(Y),
\qquad |e(Y)|\le {C_b\over\sqrt Y},
\qquad a_*>0.
\tag{L-98100.1}
\]

For a prime cutoff `Z>=67`, put

\[
U_Z(X)=
\sum_{\substack{m\ \mathrm{squarefree}\\
                 67\le P^-(m),\ P^+(m)\le Z}}
{\mu(m)\over m}u(X/m),
\tag{L-98100.2}
\]

\[
P_Z=\prod_{67\le p\le Z}\left(1-{1\over p}\right),
\qquad
E_Z=\prod_{67\le p\le Z}\left(1+{1\over\sqrt p}\right).
\tag{L-98100.3}
\]

The complete cube identity of PR #599 gives uniformly in `X,Z`

\[
\boxed{
U_Z(X)=a_*P_Z+\varepsilon_Z(X),
\qquad
|\varepsilon_Z(X)|\le {C_bE_Z\over\sqrt X}.
}
\tag{L-98100.4}
\]

Let

\[
L=\log X,
\qquad
\ell_3=\log\log\log X,
\qquad
Z_X=\ell_3^2
\tag{L-98100.5}
\]

for all sufficiently large `X` (rounding the real cutoff down changes no
estimate). Then

\[
\log E_{Z_X}
\le
\sum_{p\le Z_X}p^{-1/2}
\ll {\sqrt{Z_X}\over\log Z_X}
\ll {\ell_3\over\log\ell_3}
=o(\log L).
\tag{L-98100.6}
\]

Consequently

\[
\boxed{E_{Z_X}=L^{o(1)}.}
\tag{L-98100.7}
\]

Mertens' product theorem gives

\[
P_{Z_X}\asymp {1\over\log Z_X}.
\tag{L-98100.8}
\]

Since `E_(Z_X) log Z_X=o(sqrt X)`, (L-98100.4) implies

\[
\boxed{
U_{Z_X}(X)
=a_*P_{Z_X}(1+o(1))>0.
}
\tag{L-98100.9}
\]

This is a complete all-depth positive cube, not a fixed-depth Bonferroni
truncation. Its purpose is different from the near-critical cutoff of PR #599:
the very slow growth makes `E_Z` subpower in `log X`, which permits a
polylogarithmic product-boundary localization.