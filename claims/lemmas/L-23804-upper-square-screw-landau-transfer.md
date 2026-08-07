# L-23804 — Upper square-screw Landau transfer

Claim ID: `L-23804`  
Title: A subexponential upper envelope for the zeta screw function at square samples excludes every zero to the right of the critical line  
Status: **PROPOSED EXACT ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-23`  
Created: 2026-08-07  
Issue: #238  
Dependencies: PR #202 `L-19801` at `d4c8e59f8f3f992a76fd48ad13bef78505dca7cc`  
Scope: sign-orientation repair; no carry estimate

## 1. Imported screw transform

Use the even zeta screw function `Psi` normalized in PR #202. Its
Fourier--Laplace transform is

\[
\boxed{
\int_0^\infty\Psi(t)e^{izt}dt
=-\frac1{z^2}
\frac{\xi'}{\xi}\left(\frac12-iz\right),
\qquad\Im z>\frac12.}
\tag{L-23804.1}
\]

PR #202 also proves the unconditional derivative budget

\[
|\Psi'(t)|\le C(1+t)e^{t/2}
\tag{L-23804.2}
\]

between prime-power knots, with continuity across the knots.

## 2. Square sampling interpolation

Let

\[
t_N=2\log N.
\]

Since

\[
t_{N+1}-t_N=O(N^{-1})=O(e^{-t_N/2}),
\]

the exponential factor in (L-23804.2) is exactly cancelled by the square mesh.
Thus, if for some `sigma>=0`

\[
\Psi(t_N)\le C(1+t_N)^B e^{\sigma t_N}
\tag{L-23804.3}
\]

eventually, then

\[
\Psi(t)\le C'(1+t)^{B'}e^{\sigma t}
\tag{L-23804.4}
\]

eventually on the full half-line.

## 3. One-sign Landau argument

Choose a positive polynomial `P(t)` dominating the polynomial factor and put

\[
H(t)=-\Psi(t)+P(t)e^{\sigma t}.
\tag{L-23804.5}
\]

After adding one compactly supported continuous correction, whose transform is
entire, assume

\[
H(t)\ge0
\qquad(t\ge0).
\tag{L-23804.6}
\]

Its transform is

\[
\int_0^\infty H(t)e^{izt}dt
=
\frac1{z^2}
\frac{\xi'}{\xi}\left(\frac12-iz\right)
+\widehat P_\sigma(z)
+	ext{entire},
\tag{L-23804.7}
\]

where `widehat P_sigma` is holomorphic for `Im z>sigma`.

Landau's one-sign theorem says that the abscissa of convergence of the Laplace
transform of a nonnegative, non-eventually-zero function is a singularity on
the real Laplace axis. On that axis, `z=iy`, `y>sigma`, the xi argument

\[
\frac12+y
\]

is a positive real number at which `xi` has no zero. Therefore the abscissa
cannot exceed `sigma`. If `H` is eventually zero, the same conclusion is
immediate.

Hence the transform of `H` converges and is holomorphic throughout

\[
\Im z>\sigma.
\]

Equation (L-23804.7) then forbids a pole of `xi'/xi(1/2-iz)` there. Thus

\[
\boxed{
\xi(s)\ne0
\qquad\left(\Re s>\frac12+\sigma\right).}
\tag{L-23804.8}
\]

Multiplying the screw transform by `-1` has changed no pole location; this is
the exact sign-symmetric counterpart of `L-19801`.

## 4. RH consequence

If, for every `epsilon>0`,

\[
\boxed{
\Psi(2\log N)
\le C_\varepsilon N^{2\varepsilon}}
\tag{L-23804.9}
\]

eventually, then (L-23804.8) excludes all zeros in

\[
\Re s>\frac12+\varepsilon.
\]

Let `epsilon` tend to zero. Functional-equation symmetry then gives

\[
\boxed{\mathrm{RH}.}
\tag{L-23804.10}
\]

## 5. Proof boundary

This lemma proves only the analytic transfer. It corrects the common orientation
mistake that a prime-ramp lower bound would directly control
`(-Psi)_+`. It controls an upper envelope of `Psi`, and that upper envelope is
sufficient by the sign-symmetric Landau argument.
