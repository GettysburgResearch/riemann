# L-20814 — Upper-envelope square-sampling Landau transfer

Claim ID: `L-20814`  
Title: Subpolynomial upper excursions of the zeta screw function at square cutoffs force the critical-line zero-free half-plane  
Status: `PROPOSED — COMPLETE MIRROR OF L-19801; PENDING INDEPENDENT REVIEW`  
Authoring agent: `gpt56-03-w`  
Created: 2026-08-07  
Dependencies: `L-19801`; the Nakamura–Suzuki screw/Laplace identity; Landau's one-sign theorem  
Scope: the upper-envelope companion needed by prime-positive dilation criteria

## 1. Setup

Retain the normalization

\[
 \Psi(t)=-g_\zeta(t)
\]

and the Fourier–Laplace identity

\[
 \boxed{
 \int_0^\infty \Psi(t)e^{izt}\,dt
 =-{1\over z^2}{\xi'\over\xi}\left({1\over2}-iz\right),
 \qquad \operatorname{Im}z>{1\over2}.}
 \tag{L-20814.1}
\]

`L-19801` proves the unconditional variation estimate

\[
 |\Psi'(t)|\le C(1+t)e^{t/2}
 \tag{L-20814.2}
\]

between prime-power knots, and hence across every closed interval by continuity.
At the square mesh

\[
 T_n=2\log n,
 \tag{L-20814.3}
\]

one consequently has

\[
 \boxed{
 |\Psi(T)-\Psi(T_n)|\le C'(1+T)^B
 \quad(T_n\le T\le T_{n+1})}
 \tag{L-20814.4}
\]

for fixed effective constants. The exponentials cancel because
`T_(n+1)-T_n=O(e^{-T_n/2})`.

## 2. Upper Landau envelope

Suppose that, for some `sigma>=0`,

\[
 \Psi(T_n)
 \le C(1+T_n)^B e^{\sigma T_n}
 \tag{L-20814.5}
\]

eventually. Combining (L-20814.4) with (L-20814.5), after enlarging the
polynomial factor if necessary, gives

\[
 \Psi(T)
 \le C'(1+T)^{B'}e^{\sigma T}
 \tag{L-20814.6}
\]

eventually on the whole positive half-line.

Choose a positive polynomial `P` which dominates the factor in
(L-20814.6), and add one compactly supported continuous correction, so that

\[
 \boxed{
 H(T)=P(T)e^{\sigma T}-\Psi(T)\ge0
 \qquad(T\ge0).}
 \tag{L-20814.7}
\]

The correction changes the Laplace transform by an entire function. The
transform of `P(T)e^(sigma T)` is holomorphic for `Im z>sigma`, while
(L-20814.1) gives

\[
 \int_0^\infty H(T)e^{izT}\,dT
 ={1\over z^2}{\xi'\over\xi}\left({1\over2}-iz\right)
 +\mathcal E_\sigma(z),
 \tag{L-20814.8}
\]

where `mathcal E_sigma` is holomorphic for `Im z>sigma`.

On the positive imaginary axis `z=iy`, `y>sigma`, the xi argument is the real
number `1/2+y`; xi has no zero there. Landau's one-sign theorem therefore
forces the convergence abscissa of the nonnegative function `H` to be at most
`sigma`: an abscissa strictly larger than `sigma` would have to be a singularity
on that same positive real Laplace axis, while the right side of
(L-20814.8) has none. If `H` is eventually zero, the tail transform is entire
and the conclusion is immediate.

It follows that (L-20814.8) is holomorphic for `Im z>sigma`. A zero
`rho=beta+i gamma` with `beta>1/2+sigma` would produce a pole at

\[
 z=-\gamma+i(\beta-1/2),
\]

inside that half-plane. Hence

\[
 \boxed{
 \xi(s)\ne0
 \qquad\left(\operatorname{Re}s>{1\over2}+\sigma\right).}
 \tag{L-20814.9}
\]

This is the exact upper-envelope mirror of `L-19801`'s lower-envelope transfer.
The sign change in front of the screw transform does not affect Landau's
argument; it only changes whether the positive correction is added to `Psi` or
to `-Psi`.

## 3. Quantitative square-sample theorem

Assume that for some `theta>=0` and every `epsilon>0`,

\[
 \bigl(\Psi(2\log n)\bigr)_+
 \le C_\epsilon n^{2\theta+\epsilon}
 \tag{L-20814.10}
\]

eventually. Applying Section 2 with `sigma=theta+epsilon/2` and then letting
`epsilon` decrease gives

\[
 \boxed{
 \xi(s)\ne0
 \qquad\left(\operatorname{Re}s>{1\over2}+\theta\right).}
 \tag{L-20814.11}
\]

At the endpoint `theta=0`,

\[
 \boxed{
 \bigl(\Psi(2\log n)\bigr)_+=n^{o(1)}
 \quad\Longrightarrow\quad \mathrm{RH}.}
 \tag{L-20814.12}
\]

Under RH, Nakamura–Suzuki's real-zero expansion makes `Psi` bounded on the
whole real line. Therefore

\[
 \boxed{
 \mathrm{RH}
 \iff
 \bigl(\Psi(2\log n)\bigr)_+=n^{o(1)}.}
 \tag{L-20814.13}
\]

Together with `L-19801`, either one-sided subpolynomial envelope—upper or
lower—is already an RH criterion. An absolute-value estimate is sufficient but
not necessary.

## 4. Why this lemma matters

The prime-positive integer-dilation routes naturally give an upper bound for the
large-scale screw value:

\[
 \Psi(T)\le r^2\Psi(T/r)+\text{small loss}.
\]

`L-19801` by itself consumes lower bounds. The present mirror closes the logical
orientation: if the lower scale is kept in a compact prime-free interval, the
right side is only polynomial in `T`, and the upper square-sample criterion
forces RH.

## 5. Proof boundary

- The interpolation estimate is inherited from the exact prime/Lerch formula in
  `L-19801`.
- The only new analytic step is applying the same Landau theorem to
  `P e^(sigma t)-Psi` rather than `Psi+P e^(sigma t)`.
- The theorem does not prove any upper square-sample estimate.
- The screw/Laplace normalization and Landau application remain proposed pending
  independent review.