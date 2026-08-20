# L-103103 — Positive narrow-scale factorization of the fixed dyadic Haar field

**Status:** PROVED EXACT.

For `a>1`, put `h_a=log a` and

\[
\psi_a(u)=\mathbf 1_{(0,h_a)}(u)-\sqrt a\,\mathbf 1_{(h_a,2h_a)}(u).
\]

Its Mellin multiplier is

\[
\widehat\psi_a(s)
=\frac{(1-a^{-s})(1-\sqrt a\,a^{-s})}{s}.
\tag{L-103103.1}
\]

Fix an integer `M>=1` and take `a=2^{1/M}`. The two algebraic factorizations

\[
1-2^{-s}=(1-a^{-s})\sum_{r=0}^{M-1}a^{-rs},
\]

\[
1-\sqrt2\,2^{-s}
=(1-\sqrt a\,a^{-s})
\sum_{r=0}^{M-1}(\sqrt a\,a^{-s})^r
\]

give

\[
\boxed{
\psi_2
=
\left(\sum_{r=0}^{M-1}S_{a^r}\right)
\left(\sum_{r=0}^{M-1}a^{r/2}S_{a^r}\right)\psi_a,
}
\tag{L-103103.2}
\]

where `(S_cf)(Y)=f(Y/c)`. All reconstruction coefficients are nonnegative.

The total coefficient mass is

\[
C_M
=M\sum_{r=0}^{M-1}a^{r/2}
=M\frac{\sqrt2-1}{2^{1/(2M)}-1}
=O(M^2).
\tag{L-103103.3}
\]

Scale shifts are isometries on `L^2(dY/Y)`. Therefore every finite source field satisfies

\[
\boxed{
\|H_{\psi_2}\|_{L^2(dY/Y)}^2
\le C_M^2\|H_{\psi_a}\|_{L^2(dY/Y)}^2
\ll M^4\|H_{\psi_a}\|_2^2.
}
\tag{L-103103.4}
\]

The autocorrelation of `psi_a` vanishes outside `|log(m/n)|<2log a`; equivalently, its physical near-collision window is

\[
\boxed{a^{-2}<m/n<a^2=2^{2/M}.}
\tag{L-103103.5}
\]

Thus a subpower choice of `M` shrinks the ratio-four collision window to `1+o(1)` at only subpower reconstruction cost. This is a valid positive reduction, not a source-blind inversion. It does not by itself bound the remaining signed correlations.
