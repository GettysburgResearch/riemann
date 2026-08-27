# T-106800 — One beta harmonic is a quantitative zero-abscissa detector

Claim ID: `T-106800`  
Status: **UNCONDITIONAL QUANTITATIVE DETECTOR THEOREM AND UNCONDITIONAL STRETCHED-EXPONENTIAL ENERGY SAVING**  
Created: 2026-08-27  
Depends on: `L-106800--L-106801`; beta band-pass PR #758 at the frozen parent head  
RH status: **unproved**

Let

\[
\Theta
=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

Fix once and for all:

- one compact infinite-dyadic beta kernel \(B_{r,\infty}\);
- one nonzero guarded harmonic \(h\in\mathbf Z\setminus\{0\}\);
- optionally, one outer-frozen rough cutoff
  \(y_X\to\infty\) with \(y_X\le(\log X)^{2+o(1)}\).

Define

\[
t_{h,X}=\frac{2\pi h}{\log X+S_{r,\infty}+\delta},
\]

\[
\mathfrak D_h(X)
=
\max_{N\le X}
\left|
\sum_{n\le N}
\frac{\beta(n)}{n^{1/2+it_{h,X}}}
\right|,
\]

\[
w_{h,X}
=
\frac{
|\widehat B_{r,\infty}(t_{h,X})|^2
}{
\log X+S_{r,\infty}+\delta
},
\]

and

\[
\mathfrak W_h(X)=w_{h,X}\mathfrak D_h(X)^2.
\]

Also let

\[
\mathfrak E_B(X)
=
\max_{Y\le X}
\int_{\mathbf R}
\left|
\sum_{n\le Y}
\frac{\beta(n)}{\sqrt n}
B_{r,\infty}(u-\log n)
\right|^2du.
\]

Then

\[
\boxed{
\limsup_{X\to\infty}
\frac{\log(1+\mathfrak W_h(X))}{\log X}
=
2\Theta-1,
}
\tag{T-106800.1}
\]

and

\[
\boxed{
\limsup_{X\to\infty}
\frac{\log(1+\mathfrak E_B(X))}{\log X}
=
2\Theta-1.
}
\tag{T-106800.2}
\]

The same single-harmonic exponent is obtained after replacing beta by
ordinary Möbius, 67-free Möbius, or the complete outer-frozen rough Möbius
coordinate in the stated cutoff range.

Equivalently, for every \(1/2\le\sigma\le1\),

\[
\boxed{
\zeta(s)\ne0\quad(\Re s>\sigma)
\Longleftrightarrow
\mathfrak W_h(X)
\ll_\epsilon X^{2\sigma-1+\epsilon}
\quad(\epsilon>0),
}
\tag{T-106800.3}
\]

and the same equivalence holds with \(\mathfrak E_B\).

Thus one fixed nonzero spectral coordinate does not merely detect RH. Its
growth exponent records the complete rightmost-zero abscissa.

Unconditionally, if

\[
\Psi(X)
=
(\log X)^{3/5}(\log\log X)^{-1/5},
\]

then for some \(c_B>0\),

\[
\boxed{
\mathfrak W_h(X),\ \mathfrak E_B(X)
\ll_B
X\exp(-c_B\Psi(X)).
}
\tag{T-106800.4}
\]

This is a genuine nontrivial bound for the exact RH detector. It is still
\(X^{1-o(1)}\), so it proves neither a new fixed zero-free half-plane nor RH.

## Conceptual interpretation

The following operations form one quantitative universality class:

```text
ordinary Mertens prefix
 -> half weighting
 -> one logarithmic phase
 -> small-prime rough deletion
 -> duplicate-67 filtering
 -> one fixed band-pass harmonic
 -> the complete maximal beta energy.
```

Every arrow preserves the power exponent after the deterministic half-weight
shift, and the final squared energy has exponent \(2\Theta-1\).

This replaces a binary implication graph by a calibrated renormalization
observable: any future improvement in the beta harmonic translates
immediately into a zero-free half-plane, with no further detector
reconstruction.
