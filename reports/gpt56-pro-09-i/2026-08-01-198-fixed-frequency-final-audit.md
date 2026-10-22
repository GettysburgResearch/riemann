# Final audit of the square-cell closure: the inner block is the theorem

Agent: `gpt56-pro-09-i`  
Date: 2026-08-01  
Issue: #198  
PR: #202

## Requested endpoint

The remaining proposed estimate was

\[
[\mathcal R_\beta(n)-\mathcal B_\beta(n)]_+=n^{o(1)},
\]

or, more strongly,

\[
\mathcal R_\beta(n)\le\mathcal B_\beta(n)
\quad\text{eventually}.
\]

By `T-19804`, either statement implies RH; by `L-19802`, the optimal power
exponent of the negative part is exactly the horizontal displacement of the
rightmost zeta zero.

## 1. Source-level audit

Nakamura--Suzuki prove the exact zero expansion

\[
\Psi(t)=\sum_\gamma m_\gamma{1-e^{-i\gamma t}\over\gamma^2}
\]

and the one-sided Fourier--Laplace identity

\[
\int_0^\infty\Psi(t)e^{izt}dt
=-z^{-2}{\xi'\over\xi}(1/2-iz).
\]

Suzuki's later weighted-Chebyshev theorem proves that eventual one-sidedness of

\[
\sum_{m\le x}{\Lambda(m)\over\sqrt m}\log{x\over m}-4\sqrt x
\]

is itself equivalent to RH. The square-cutoff and beta-cell criteria are a
critical discretization and a local positive smoothing of this theorem; they do
not weaken the fixed-frequency obstruction.

## 2. Exact square-cell uncertainty calculation

For every normalized positive cell weight `w`, put

\[
J_{n,w}(z)=\int_0^1w(u)[n^2+(2n+1)u]^{-iz}du.
\]

`L-19808` proves, uniformly on compact `z`-sets,

\[
J_{n,w}(z)
=n^{-2iz}\left(1-{2iz\mu_1\over n}+O_z(n^{-2})\right).
\]

For one fixed off-line zero parameter `z=a+ib`, `b>0`,

\[
|J_{n,w}(z)|=n^{2b}(1+O_z(n^{-1})).
\]

Thus the local smoothing is an approximate identity at every fixed frequency.
Its logarithmic width is `Theta(1/n)`, so it resolves frequencies only at the
moving scale `Theta(n)`. Endpoint vanishing can suppress ordinates comparable to
or larger than `n`; it cannot suppress a fixed off-line mode.

## 3. Exact quartet signal

One nonreal quartet contributes

\[
C_{w,z}(n)
=C_z^{(0)}
-2m n^{2b}
\Re\left({e^{-2ia\log n}\over z^2}\right)
+O_z(n^{2b-1})+O_z(n^{-2b}).
\]

For an isolated quartet, integers can be selected with phase error `o(1)`, so
negative values of order `n^(2b)` occur infinitely often. For the complete zero
set, `L-19802` supplies the aggregate, cancellation-safe statement:

\[
\Theta_\zeta
=\limsup_{n\to\infty}
{\log(1+(-\mathscr C_\beta(n))_+)\over2\log n}.
\]

No assumption that a rightmost quartet is isolated or that its phase is linearly
independent is needed.

## 4. What the high-zero theorem really accomplishes

`L-19807` gives an unconditional `O_A(log n)` radius for the complete block

\[
|\Re\gamma|\ge An.
\]

This is useful and exact: it removes the infinite high-frequency tail. But every
fixed zero lies in the complementary moving block for all sufficiently large
`n`. Therefore the high-zero theorem does not approach the fixed-frequency RH
obstruction.

The remaining block is finite at each stage but not uniformly finite in the
cofinal problem. Calling it a finite computation obscures the quantifiers.

## 5. Möbius and renewal audit

PR #204 proves exact local Möbius extension of every compact localized target
into the global Weil radical. Its residual transform is

\[
\widehat t(z)
=[\zeta(s)P(s)-1]\widehat h(z)
-\text{pole correction},
\qquad s=1/2-iz.
\]

At every nontrivial zeta zero,

\[
\widehat t(z_\rho)=-\widehat h(z_\rho)
\]

for every Möbius cutoff and every affine tail optimization. Hence local
inversion, von-Mangoldt-chain contractivity, and analytic tail minimization can
improve positive realization costs but cannot alter the zero signature.

The renewal identity

\[
\mu*\nu=t\nu
\]

is exact in the Euler-product half-plane. Extending its inverse with a uniform
critical square-function bound is equivalent to excluding the same interior
poles. Ordinary Markov contractivity does not cross that boundary.

## 6. Routes explicitly ruled out

The requested subpolynomial estimate cannot follow from any argument that remains
valid in the presence of one fixed off-line zero. This rules out, by itself:

1. stronger zero-density estimates that still permit one exception;
2. any fixed verified-zero height;
3. additional endpoint zeros or cell smoothness;
4. a smaller `O(log n)` outer-tail constant;
5. phase-blind PNT or classical zero-free-region estimates;
6. local Möbius reconstruction with optimized analytic tails;
7. Markov-chain contraction confined to the Euler-product half-plane.

Each mechanism is compatible with the `n^(2b)` fixed-frequency term.

## 7. What would constitute a real completion

A proof must introduce one genuinely strip-sensitive statement, for example:

- a sum-of-squares identity for the complete finite logarithmic Riesz mean;
- a positivity-preserving contour identity whose multiplier is nonzero
  throughout `0<Re rho-1/2<1/2`;
- a self-adjoint realization whose resolvent—not merely its analytic
  continuation—has the zeta zeros as poles;
- a direct proof that the prime-side renewal inverse has no exponentially growing
  mode at any fixed frequency.

Any one of these, proved with complete constants, would prove RH. None is
currently supplied by this branch or by the cited primary literature.

## 8. Verdict

The square-screw and beta-cell reductions are legitimate new scalar criteria.
The fixed-frequency calculation is also a useful breakthrough because it
prevents a false asymptotic closure: the outer tail is solved, but the inner
block is exactly the RH theorem.

No proof of the final inequality, and therefore no proof of RH, is claimed.