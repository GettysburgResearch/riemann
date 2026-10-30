# Exact source operators and theta approximation: October 30 swarm

**Status: proposed component mathematics, with proofs, scoped independent AI-agent reviews, and reproducible checks. RH remains unproved. This packet establishes no smaller zero-free half-plane for zeta or an L-function family.**

The purpose of this pass was to explore mechanisms outside the recent scalar moment optimization. Three parallel research lanes developed exact source calculations, then exchanged independent reviews. The work is additive: it does not change the repository's accepted scientific status.

## Main results

| Direction | What is established in the packet | What remains open |
|---|---|---|
| Moving-anchor xi operators | An RH criterion with the cofinal scaling `N/a -> infinity`; an unconditional positive family at `a >= 100(N+1)`; a necessary and sufficient completeness threshold for its Laguerre test spaces; an exact rank-two boundary formula for changing the anchor | Positivity of the actual source in the complete regime, or a bound on the transported boundary term that preserves the known positive margin |
| Theta-to-Bessel approximation | A whole-source rational certificate excluding a natural fixed Pólya envelope; an obstruction for every fixed envelope; an explicit positive sampling construction converging to the actual theta source in every exponentially weighted L1 norm; a self-adjoint boundary construction and all-real zeros through order two | A zero-location theorem for a cofinal family of complete Bessel sums; the global rational sign test fails for some actual coefficients |
| Native arithmetic phase | An exact classification: the limiting logarithmic arithmetic law is not infinitely divisible, its symmetrization is, and a specified log-gamma convolution repairs infinite divisibility exactly at noise strength one; a rationally certified three-point phase witness | A source-preserving way to pay the repair's exponential deconvolution cost, or an upper bound on the original Nyman–Beurling approximation error |

The existing Li/Weil/Laguerre/Schur machinery is credited as prior art. The high-height arithmetic kernel asymptotic was independently recovered and then found in stronger recent work; it is explicitly attributed. The new-to-this-packet statements are not worldwide priority claims.

## 1. The lead operator result: a precise completeness scale

For the actual completed xi function, set

\[
 f(s)=\frac{\xi'(s)}{\xi(s)},\qquad
 s_a(z)=\frac12+a\frac{1+z}{1-z},\qquad
 2af(s_a(z))=c_0(a)+2\sum_{n\ge1}c_n(a)z^n,
\]

and let `T_N(a)=(c_(j-k)(a))` for indices 0 through N.

For any prescribed sequence with the displayed scaling, the [moving-anchor proof](spectral/MOVING_ANCHOR_THEOREM.md) establishes:

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 T_{N_j}(a_j)\succeq0\text{ eventually, where }
 a_j\ge1,\quad N_j/a_j\longrightarrow\infty.
\]

The nontrivial issue is that the evaluation point itself may run to infinity. A fixed Cayley transform and repeated Schwarz lemma give the required continuation without an extra logarithmic loss. The proof does not assume that the actual logarithmic derivative is holomorphic in the unproved half-plane.

The same paper proves the unconditional estimate

\[
 a\ge100(N+1)\quad\Longrightarrow\quad T_N(a)\succ\frac a6 I.
\]

This really is a theorem for every order, but its ratio N/a stays small. Its interpretation is fixed by an exact formula. For the Laguerre space

\[
 V_{N,a}=\{e^{-au}p(u):\deg p\le N\}\subset L^2(0,\infty),
\]

the squared projection error of the normalized exponential `h_b(u)=sqrt(2b)exp(-bu)` is

\[
 \|(I-P_{N,a})h_b\|_2^2
 =\left|\frac{a-b}{a+b}\right|^{2(N+1)}.
\]

Consequently `P_(N_j,a_j) -> I` strongly if and only if `N_j/a_j -> infinity`. In the unconditional family `a=100(N+1)`, the error for `b=1/2` tends to `exp(-0.02)`, about 0.9802. Increasing matrix size in that family leaves almost all of this one vector outside the test space. This is a precise completeness statement; it is not an assertion that every incomplete family is useless for every source-specific purpose.

### A concrete transport problem

The [anchor-flow proof](spectral/ANCHOR_FLOW.md) shows how to move from the unconditional region toward the complete one. After normalization `G_N=T_N/(2a)`, changing `log a` has the form

\[
 \partial_{\log a}G_N=K_N^*G_N+G_NK_N+
 \frac{N+1}{2}(e_Nr_N^*+r_Ne_N^*),
\]

where `K_N` is an explicit skew-symmetric tridiagonal matrix and `r_N` is the actual next covariance row. The first two terms change the basis unitarily. The last term, of rank at most two, accounts for every change of the eigenvalues.

The proof gives the exact integrated positive-part budget sufficient to carry the known `G_N > I/12` margin down to smaller anchors. That budget is the next source-specific estimate; it is not supplied by the rank-two identity itself. The boundary term generally has both signs.

The prime matrices also have a common exact translation model:

\[
 \langle q,m^{-A_N}q\rangle
 =m^{-1/2}\int_0^\infty\overline{\phi(u)}\phi(u+\log m)\,du.
\]

This keeps the correlations at actual prime-power logarithms. Summing independent operator norms would discard them and produce a divergent series at exponent one half.

## 2. A complete theta approximation with an explicit zero problem

The [theta proof](theta/PROOF.md) works with the full classical source `Phi`, normalized by

\[
 \Xi(z)=\int_{\mathbb R}\Phi(t)e^{izt}\,dt.
\]

It first proves, using rational outward intervals and an analytic bound for every omitted theta summand,

\[
 -8{,}951{,}861<
 \left.\frac{d^8}{dt^8}
 \big(e^{2\pi\cosh(2t)}\Phi(t)\big)\right|_{t=0}
 <-8{,}951{,}860.
\]

Thus a positive cosh-mixture construction with that fixed Pólya envelope cannot even match the source near zero. A separate modular-cusp argument excludes an entire multiplier for *any* fixed envelope `exp(-a cosh(2t))`. Successful positive finite-cosh approximations must have both `a -> infinity` and their frequency bandwidth divided by a tending to infinity.

The constructive replacement is explicit. Put

\[
 w(x)=\Phi(\tfrac12\operatorname{arsinh}x),\qquad
 \mathcal K_{a,M}(t)=e^{-a\cosh(2t)}
 \sum_{|n|\le M}I_{|n|}(a)w(n/a)e^{2nt}.
\]

When `a -> infinity` and `M/a -> infinity`, these kernels converge to `Phi` in every exponentially weighted L1 norm. The proof uses an exact tilted Skellam expectation, not fitted moments. It includes a common double-exponential tail bound and the first correction

\[
 \mathcal K_a(t)=\Phi(t)+\frac1{8a}
 \frac d{dt}\big(\operatorname{sech}(2t)\Phi'(t)\big)+O_T(a^{-2}).
\]

Their complete Fourier transforms are finite sums of Bessel functions with shifted order, with the literal source sample weights. They converge locally uniformly to Xi on the complex plane. This closes the source-approximation part of this proposed route. Their zero geometry is a separate mathematical problem.

The easiest universal-multiplier shortcut fails eventually along every cofinal sequence: the associated reciprocal polynomial violates its necessary central/leading coefficient inequality. It is not permissible to substitute zeros of the kernel's coefficient polynomial for zeros of its Fourier transform.

### A constructive boundary realization, and its limit

The [boundary reduction](theta/BESSEL_BOUNDARY.md) writes the complete Bessel sum as

\[
 F(E)=A(E)y_E(0)+B(E)y_E'(0),\qquad
 -y_E''+a^2e^{2u}y_E=Ey_E,\qquad E=z^2/4.
\]

Here `y_E(u)=K_(i sqrt(E))(a exp(u))`, so the boundary derivative is the radial derivative `a K'(a)`. This factor matters in interpreting the resulting boundary mass. The [self-adjoint construction](spectral/BESSEL_SELFADJOINT_GATE.md) proves an all-zero theorem when the reduced rational boundary function has the form

\[
 -A(E)/B(E)=h-bE+\sum_j\frac{\gamma_j}{E-\lambda_j},
 \qquad b\ge0,\quad\gamma_j>0,\quad\lambda_j>0.
\]

Within that class, the exact threshold for nonnegative energy is `r(0)>=-a*K_1(a)/K_0(a)`. Common polynomial factors and poles are accounted for explicitly. Positive mixtures through order two satisfy the gate and have all their z zeros real.

At order three, a rational interval certificate for the actual theta coefficients proves that the gate passes at `a=1/4,1/2,1,2,5,10` and fails at `a=20,50`. An equal-coefficient control has all-real transform zeros while failing the same gate, so this is a limitation of the sufficient representation. Ordinary high-precision calculations also find failures of its higher-order J-fraction test. None of these finite observations settles every possible cofinal choice of parameters.

The constructive alternative is local: anti-Herglotz sign on an expanding energy disk, together with negative-energy exclusion and common-factor control, suffices. The proof needs no control of remote zeros. This could combine with the established source convergence, but the required local inequalities remain open. Exploratory pole calculations warn why a grid is inadequate: some numerator/denominator cancellations leave residues far below ordinary floating-point resolution.

## 3. The arithmetic phase obstruction and its exact repair

The [arithmetic proof](arithmetic/ARITHMETIC_KERNEL.md) starts from the actual harmonic-step zero functionals. Its high-height limiting constant is

\[
 C(\alpha)=\frac{\pi}{\Gamma(1+\alpha)\sin(\pi\alpha/2)},
 \qquad0<\alpha<2.
\]

Those kernel/jet asymptotics overlap stronger work by Scott Schubr and are retained as an attributed derivation. The subsequent semigroup analysis concerns the literal probability law

\[
 p_\alpha(x)=\frac{2}{C(\alpha)}e^{-\alpha x}(1-\cos(e^x)),
 \qquad \varphi_\alpha(t)=\frac{C(\alpha-it)}{C(\alpha)}.
\]

Although its characteristic function has no real zeros, this law is not infinitely divisible. The proof identifies a negative interval in its signed Lévy density. More sharply, at `alpha=3/2`, a three-point complex-coefficient test gives a strictly negative quadratic; a sixteen-term rational calculation proves an upper bound below `-1.434` for the complete quantity.

Every real-coefficient version of that logarithmic test passes. The reason is exact: the symmetrized law is infinitely divisible, and at `alpha=3/2` its characteristic function is the product of two centered Laplace characteristic functions. The failure is carried by complex phase cross terms.

There is also a positive construction with a sharp threshold. Add an independent member of a specified log-gamma convolution semigroup. The result becomes infinitely divisible exactly at noise strength one. Undoing that repair amplifies Fourier frequencies by `exp(pi |t|/4)` up to a polynomial. No bound paying that amplification for the native approximation problem is proved. The result rules out a specific phase-preserving interpolation, not all probabilistic or operator methods.

## Proofs, review and execution

- [Moving-anchor and completeness theorems](spectral/MOVING_ANCHOR_THEOREM.md), [anchor transport](spectral/ANCHOR_FLOW.md), and [independent review](spectral/REVIEW_SPECTRAL_AND_FLOW.md).
- [Theta proofs and exact source certificate](theta/PROOF.md), [independent theta review](theta/REVIEW_THETA.md), [boundary reduction](theta/BESSEL_BOUNDARY.md), [self-adjoint construction](spectral/BESSEL_SELFADJOINT_GATE.md), and [independent boundary review](theta/REVIEW_BESSEL.md).
- [Arithmetic classification and finite phase witness](arithmetic/ARITHMETIC_KERNEL.md), with [independent review](arithmetic/REVIEW_ARITHMETIC.md).
- [Validation scope](VALIDATION.md), [claim ledger](CLAIMS.md), and [repository/source context](SOURCE_CONTEXT.md).

From this directory, the exact standard-library programs are:

```sh
python -I -S -B spectral/verify_anchor_flow.py
python -I -S -B theta/verify_polya_obstruction.py
python -I -S -B theta/verify_bessel_m3.py
python -I -S -B arithmetic/verify.py
```

The spectral algebra and floating diagnostics additionally use NumPy/SciPy:

```sh
python -I -B spectral/verify_spectral.py
```

The optional theta quadrature/root exploration is `theta/skellam_diagnostic.py`. Its located roots are ordinary floating-point diagnostics, not a complete or certified zero census. The saved rational certificates and the written analytic proofs have separate roles.

## Next mathematical decisions

1. For the xi operator, estimate the transported actual boundary row in the complete scaling regime. The identity, normalization and required budget are explicit.
2. For the theta approximation, prove the local boundary sign conditions on growing energy disks for a family with both required parameters escaping. This requires control of near-common polynomial zeros and any additional complex poles. A fixed-order theorem or a sampled grid alone does not provide that family.
3. For the arithmetic law, retain its phase and native target. Any use of the positive completion must include a quantitative deconvolution estimate; its positivity by itself does not bound the original approximation error.

These are the remaining mathematical obligations. The packet does not count them as established consequences of finite checks or of agreement between agents.
