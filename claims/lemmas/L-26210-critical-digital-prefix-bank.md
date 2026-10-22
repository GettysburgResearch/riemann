# L-26210 — Exact critical-order digital prefix bank

Claim ID: `L-26210`  
Title: The binary-digit prefix family and the opposite-parity Möbius source form an exact finite Calderón bank with the sharp critical \(R\)-order observability scale  
Status: **PROPOSED COMPLETE — exact finite convolution and Hilbert-space algebra pending independent review**  
Date: 2026-08-08  
Depends on: PR #236 `L-23011/L-23016/R-23008`; PR #268 `L-26202`; PR #269 `L-26901/L-26903`  
Scope: finite prefix-bank algebra and its exact norm scale; no physical factor-five upper estimate and no RH conclusion

## 1. The two exact arithmetic sequences

Put

\[
c_2(n)=1-v_2(n)
\]

and

\[
\omega_2(n)
=
\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
+rac12\mathbf1_{4\mid n}\mu(n/4).
\]

Their Dirichlet series are

\[
C_2(s)
=
\zeta(s)\frac{1-2^{1-s}}{1-2^{-s}},
\qquad
\Omega_2(s)
=
\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
\tag{L-26210.1}
\]

Therefore

\[
\boxed{
C_2(s)\Omega_2(s)
=(1-2^{1-s})(1-2^{-s-1})
=1-\frac52\,2^{-s}+4^{-s}.
}
\tag{L-26210.2}
\]

Equivalently, in the Dirichlet-convolution algebra,

\[
\boxed{
c_2*\omega_2
=
\varepsilon-\frac52\delta_2+\delta_4.
}
\tag{L-26210.3}
\]

This is the finite digital identity already visible in the bottom-charge and binary-digit branches.  The new point is to retain all multiplicative prefixes simultaneously rather than invert one nearly singular prefix.

## 2. Exact hyperbola prefix-bank identity

For a real number \(Y>1\), define the strict prefix

\[
C_{<Y}(s)
=
\sum_{1\le n<Y}\frac{c_2(n)}{n^s}.
\tag{L-26210.4}
\]

Fix an integer \(R\ge5\). Then

\[
\boxed{
\sum_{1\le d<R}
\frac{\omega_2(d)}{d^s}
C_{<R/d}(s)
=
1-\frac52\,2^{-s}+4^{-s}.
}
\tag{L-26210.5}
\]

Indeed the coefficient of \(m^{-s}\) on the left is

\[
\sum_{dn=m\atop dn<R}\omega_2(d)c_2(n)
=(\omega_2*c_2)(m)
\]

for \(m<R\), and no coefficient with \(m\ge R\) occurs.  Since the complete convolution in (L-26210.3) is supported on \(1,2,4\), truncation at any \(R\ge5\) is exact.

This is a finite multiplicative Calderón formula.  It is not an asymptotic inversion and has no omitted tail.

## 3. Physical translation form

Let

\[
(\tau_n f)(t)=f(t-\log n)
\]

on a Hilbert-valued \(L^2(\mathbb R)\) space, and define

\[
\mathcal A_Y
=
\sum_{1\le n<Y}
\frac{c_2(n)}{\sqrt n}\tau_n.
\tag{L-26210.6}
\]

Define the fixed three-tap operator

\[
\boxed{
\mathcal H
=I-\frac5{2\sqrt2}\tau_2+\frac12\tau_4.
}
\tag{L-26210.7}
\]

Then (L-26210.5), evaluated at \(s=z+1/2\), is the exact operator identity

\[
\boxed{
\mathcal H
=
\sum_{1\le d<R}
\frac{\omega_2(d)}{\sqrt d}
\tau_d\mathcal A_{R/d}.
}
\tag{L-26210.8}
\]

Every delay and every prefix is declared.  The source coefficients in the synthesis bank are precisely the opposite-parity coefficients whose carry image is localized to the factor-five transition sector on PR #269.

## 4. Uniform lower frame bound for the three-tap output

On the Fourier line, with \(L=\log2\) and \(z=e^{-iL\xi}\), the multiplier of \(\mathcal H\) factors as

\[
1-\frac5{2\sqrt2}z+\frac12z^2
=(1-\sqrt2z)(1-2^{-3/2}z).
\tag{L-26210.9}
\]

Hence

\[
\boxed{
\|\mathcal H f\|_2
\ge
\kappa_*\|f\|_2,
\qquad
\kappa_*
=(\sqrt2-1)(1-2^{-3/2})
=\frac{5\sqrt2-6}{4}>0.
}
\tag{L-26210.10}
\]

The same estimate holds componentwise in any Hilbert space and after applying one physical derivative, because translations commute with differentiation.

## 5. Exact critical-order bank observability

Put

\[
w_d=\frac{|\omega_2(d)|}{\sqrt d},
\qquad
W_R=\sum_{1\le d<R}w_d.
\tag{L-26210.11}
\]

Triangle inequality followed by weighted Cauchy–Schwarz in (L-26210.8) gives

\[
\|\mathcal H f\|_2^2
\le
W_R
\sum_{d<R}w_d
\|\mathcal A_{R/d}f\|_2^2.
\tag{L-26210.12}
\]

Combining with (L-26210.10),

\[
\boxed{
\|f\|_2^2
\le
\kappa_*^{-2}W_R
\sum_{d<R}w_d
\|\mathcal A_{R/d}f\|_2^2.
}
\tag{L-26210.13}
\]

The local \(2\)-adic formula for \(\omega_2\) is

\[
1,-\frac52,2,-\frac12,0,0,\ldots
\]

on every odd squarefree core. Thus

\[
|\omega_2(n)|\le\frac52.
\]

Using \(\sum_{n<R}n^{-1/2}\le2\sqrt R\),

\[
\boxed{W_R\le5\sqrt R.}
\tag{L-26210.14}
\]

If \(\pi_R(d)=w_d/W_R\), then

\[
\boxed{
\|f\|_2^2
\le
\frac{25}{\kappa_*^2}\,R
\sum_{d<R}\pi_R(d)
\|\mathcal A_{R/d}f\|_2^2.
}
\tag{L-26210.15}
\]

The same estimate holds with the \(H^1\) norm on both sides.

The exponent \(R^1\) is exactly the critical order identified by PR #236 `R-23008`.  The bank does not falsely suppress genuine critical-line modes, and it does not require a polylogarithmic inverse of one digital prefix.

## 6. Causal block and endpoint collars

Let \(\chi_J\) be the indicator of \([0,J]\), and let \(f\) be causal.  Applying (L-26210.8) to \(\chi_Jf\) is exact on the full line.  For each prefix,

\[
[\mathcal A_Y,\chi_J]f
=
\sum_{n<Y}\frac{c_2(n)}{\sqrt n}
[\tau_n,\chi_J]f.
\tag{L-26210.16}
\]

Because \(f=0\) on the negative half-line, the commutator is supported only in the upper endpoint collar

\[
J\le t\le J+\log Y.
\tag{L-26210.17}
\]

Thus the finite-horizon form of (L-26210.15) has one completely explicit endpoint channel.  No interior remainder is introduced by localization.

This is the correct place for the tempered endpoint channel in PR #236 `T-23005`; it is not permissible to hide target transition energy in that channel.

## 7. Relation to the factor-five source

The synthesis sequence in (L-26210.8) is \(\omega_2\), not an arbitrary vector. PR #269 proves for this same source:

1. a pointwise compact carry wavelet;
2. localization of every potentially negative logarithmic-Kummer row to
   \[
   2m\le n<5m;
   \]
3. a uniform carry-feature Schur reserve;
4. positive generalized-prime synthesis.

Consequently the former open problem

```text
invert one digital prefix with polylogarithmic loss
```

is replaced by the source-compatible problem

```text
estimate one exact critical-order bank through the complete
independent-frequency factor-five transition ledger.
```

The critical \(R\)-order conditioning is already closed by (L-26210.15).  What remains is an upper source-image estimate for the bank observations, with every signed cross term and collar retained.

## 8. What this theorem does not prove

The bank identity and its frame inequality do not by themselves bound the bank observations.  In particular, using triangle inequality a second time on the digital recurrence would return the unresolved balanced Möbius source.

A full proof still needs a source-specific physical theorem showing that the weighted bank observation energy is the sum of:

- a tempered critical-line/end-point channel;
- the factor-five carry transition form;
- strict lower-scale outputs;

with a net reserve sufficient for the pole-exclusion argument.

## 9. Proof boundary

Closed exactly, subject to review:

- the finite hyperbola prefix-bank identity;
- the physical translation identity;
- the uniform three-tap lower frame bound;
- the sharp \(O(R)\) bank observability rate;
- the exact finite-horizon collar support;
- compatibility with the opposite-parity factor-five source.

Open:

- the physical upper estimate for the bank observations;
- the complete transition/collar ledger;
- RH.
