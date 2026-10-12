# A periodic dilation filter that preserves positive power bounds

Status: elementary operator and profile identities proved below. Their application to a native moment is conditional on the explicitly stated native bound for one derivative window at the same row height. No new native moment estimate, zero-free boundary, or Riemann hypothesis is proved here.

The purpose is concrete. Multiplication by the fixed factor `L(s, chi_{-3})` can remove the companion quadratic L-function from the Eisenstein reciprocal source. Taking the absolute values of the Dirichlet coefficients of that factor would destroy bounds below exponent one. Its bounded periodic partial sums avoid that loss, at the cost of one scale derivative. This is a forward transfer; its reciprocal is a different, unproved problem in a subcritical half-plane.

## 1. Exact Abel identity, including its lower boundary

Write

\[
\chi(m)=\chi_{-3}(m)=
\begin{cases}0&3\mid m,\\1&m\equiv1\pmod3,\\-1&m\equiv2\pmod3,
\end{cases}
\qquad C(t)=\sum_{1\le m\le t}\chi(m).
\tag{1.1}
\]

For all real `t >= 0`, `C(t)` is either zero or one; it is one exactly when `floor(t)` is one modulo three. In particular its sign is known, not merely its absolute size.

Let `F:(0,infinity)->B` be locally absolutely continuous with values in a finite dimensional normed space, or a Banach space where the following integrals exist. Assume that `F(y)=0` for `0<y<a` for some fixed `a>0`. Define the finite causal sum

\[
(\mathcal T F)(D)=\sum_{m\ge1}\chi(m)F(D/m).
\tag{1.2}
\]

**Proposition 1.** For every `D>0`,

\[
\boxed{\quad
(\mathcal T F)(D)=\int_0^D C(D/y)F'(y)\,dy.
\quad}
\tag{1.3}
\]

**Proof.** Put `g(t)=F(D/t)`. It vanishes for `t>D/a`. Stieltjes summation by parts against `C(t)` on `[1-,infinity)` gives

\[
\sum_{m\ge1}\chi(m)g(m)
=-\int_1^\infty C(t)g'(t)\,dt
=\int_1^\infty C(t)\frac{D}{t^2}F'(D/t)\,dt.
\]

The lower boundary at `1-` is zero because `C(1-)=0`; the jump at `1` is included in the Stieltjes sum. The upper boundary is zero by causality. Substituting `y=D/t` proves (1.3). Local absolute continuity suffices, so derivative jumps are allowed. A jump of `F` itself would instead require its full Stieltjes derivative and is not silently omitted. QED.

Consequently

\[
\|\mathcal T F(D)\|\le\int_0^D\|yF'(y)\|\,\frac{dy}{y}.
\tag{1.4}
\]

If, for a fixed `alpha>0`, `||y F'(y)|| <= M y^alpha` for all `y>0`, then

\[
\|\mathcal T F(D)\|\le\frac{M}{\alpha}D^\alpha.
\tag{1.5}
\]

There is no restriction `alpha>1`. The divergence of `sum |chi(m)| m^{-alpha}` for `alpha<=1` is irrelevant to this argument. The derivative hypothesis is essential and has not been inferred from a bound for `F` alone.

## 2. Native row moment transfer with its exact quantifiers

Let a fixed row set `U_H` carry any nonnegative weights `omega_H(u)`. The row set, its zero masks, and these weights stay fixed while the column scale `y` varies. For a smooth compact column window `W`, put

\[
A_u(y;W)=\sum_{(\mathfrak n,S)=1}
\mu_K(\mathfrak n)\nu(\mathfrak n)\chi_{\mathfrak n}(u)
W(N\mathfrak n/y),
\qquad W_1(t)=-tW'(t).
\tag{2.1}
\]

The sum is finite at each scale and

\[
y\partial_y A_u(y;W)=A_u(y;W_1).
\tag{2.2}
\]

**Corollary 2.** Fix `p>=1`, `alpha>0`, and `D,H`. If

\[
\left(\sum_{u\in U_H}\omega_H(u)|A_u(y;W_1)|^p\right)^{1/p}
\le M H^{1/p}y^\alpha
\quad(0<y\le D),
\tag{2.3}
\]

then

\[
\left(\sum_{u\in U_H}\omega_H(u)
\left|\sum_{m\ge1}\chi(m)A_u(D/m;W)\right|^p\right)^{1/p}
\le\frac{M}{\alpha}H^{1/p}D^\alpha.
\tag{2.4}
\]

**Proof.** Apply (1.3), Minkowski's integral inequality in the fixed weighted row space, and (2.3). QED.

In particular, a literal common-height estimate

\[
\sum_u\omega_H(u)|A_u(y;W_1)|^{2k}
\ll H y^{k+\lambda+\epsilon}
\quad(0<y\le D)
\tag{2.5}
\]

transfers with the *same exponent* `k+lambda+epsilon` at scale `D`. Constants may depend on the fixed order and epsilon. If the available source theorem requires `H >= y^{1+theta}`, then choosing `H >= D^{1+theta}` satisfies that geometric requirement throughout this integral; all its other source hypotheses must also hold. An estimate known only on the curve `H=y^h`, only for `W`, or only at sampled values of `y` does not by itself establish (2.3).

Fixed finite dilation polynomials can also be applied without an exponent loss. For

\[
(\mathcal R F)(D)=\sum_{j=1}^J c_j F(D/a_j),
\qquad a_j>0\text{ fixed},
\tag{2.6}
\]

the bound `||F(y)|| <= M y^alpha` implies
`||R F(D)|| <= M D^alpha sum_j |c_j| a_j^{-alpha}`. The field-to-integer restoration in the companion note uses precisely such a finite operator, with one factor for every excluded prime **ideal**, retaining repeated norms of split primes.

## 3. One fixed profile absorbs the entire periodic filter

Extend `W in C_c^infinity((a,b))`, `0<a<b<infinity`, by zero to the real line and define

\[
\widetilde W(x)=\sum_{m\ge1}\chi(m)W(mx),\qquad x>0.
\tag{3.1}
\]

This is a finite sum for each positive `x`. It vanishes for `x>=b` and extends smoothly by zero to `x=0`. More precisely, for every two nonnegative integers `j,A`,

\[
|\widetilde W^{(j)}(x)|\le C_{j,A,W}x^A
\qquad(0<x\le1).
\tag{3.2}
\]

**Proof.** With the Fourier convention `W_hat(xi)=integral W(t) exp(-2 pi i t xi) dt`, periodic Fourier expansion and ordinary Poisson summation give

\[
\widetilde W(x)=\frac{1}{i\sqrt3\,x}
\sum_{r\in\mathbb Z}
\left[
\widehat W\left(\frac{r-1/3}{x}\right)
-\widehat W\left(\frac{r-2/3}{x}\right)
\right].
\tag{3.3}
\]

Every frequency is nonzero, with absolute value at least `1/(3x)`. Differentiating a fixed number of times gives powers of `x^{-1}` and of these frequencies. The Fourier transform and all its derivatives decrease faster than every power. Choosing that power larger than `A`, the derivative losses, and two more powers for the `r`-sum proves (3.2), with absolute convergence also justifying termwise differentiation. QED.

Finite rearrangement now identifies the transformed family exactly:

\[
\sum_{m\ge1}\chi(m)A_u(D/m;W)
=\sum_{(\mathfrak n,S)=1}\mu_K(\mathfrak n)\nu(\mathfrak n)
\chi_{\mathfrak n}(u)\widetilde W(N\mathfrak n/D).
\tag{3.4}
\]

Both double sums are finite, since nonzero terms have `m Nn < bD`. Thus this construction changes one fixed column profile and leaves the actual ideal coefficients and row masks intact. The profile is not supported away from zero, and is generally signed. Neither property is concealed by calling it the original compact positive window.

Its Mellin transform is entire by (3.2), and

\[
\boxed{\quad
\widehat{\widetilde W}_{\rm Mellin}(s)
=L(s,\chi_{-3})\widehat W_{\rm Mellin}(s).
\quad}
\tag{3.5}
\]

For `Re s>1`, absolute summation and `t=mx` prove the identity directly. Analytic continuation proves it everywhere. The zeros of the extra L-factor are deliberate: this profile cancels that factor in the **principal** reciprocal Dedekind source. It is not a universal zero-detecting window for arbitrary Hecke twists.

The point of Section 2 is that one can transfer estimates without assuming a new theorem for every such profile. It uses the single fixed derivative window `W_1` and the stated common-height range.

## 4. A one-sided transfer for real sources

When `F` is real, the exact sign `C>=0` gives the additional inequality

\[
(\mathcal T F(D))_-
\le\int_0^D C(D/y)(F'(y))_-\,dy,
\qquad x_-:=\max(0,-x).
\tag{4.1}
\]

For each real `sigma>0`, Tonelli's theorem therefore yields

\[
\int_0^\infty(\mathcal T F(D))_-D^{-\sigma}\frac{dD}{D}
\le\frac{L(\sigma,\chi_{-3})}{\sigma}
\int_0^\infty(F'(y))_-y^{-\sigma}\,dy.
\tag{4.2}
\]

This holds as an inequality of nonnegative extended integrals. Indeed the inner change of variables `D=yt` contributes

\[
\int_1^\infty C(t)t^{-\sigma}\frac{dt}{t}
=\frac{L(\sigma,\chi_{-3})}{\sigma},
\tag{4.3}
\]

by ordinary Abel summation, valid for `sigma>0` because `C` is bounded. In particular the displayed constant is positive and at most `1/sigma`.

On a finite horizon `D<=X`, the same argument gives (4.2) with both outer integrals cut off at `X` and the same upper constant. This supplies a source-compatible route from a bound on negative variation to a bound on negative mass. It **does not** obtain a derivative bound from positivity of a smoothed higher power; the repository's existing obstruction to that reverse inference remains in force. A further finite restoration polynomial has signed coefficients, so (4.1) cannot automatically be propagated through it using a positive-kernel argument.

## 5. What this resolves, and the arithmetic estimate still needed

The companion restoration identity makes the principal transformed row exactly the ordinary integer Möbius detector, rather than a merely analogous Hecke detector. Proposition 1 and Corollary 2 remove an otherwise artificial power loss in passing to it. Section 3 shows why the transformation fits the same character sum family with an explicitly changed test. Section 4 identifies a possible interface to the repository's negative-variation work.

None of these identities bounds the remaining signed primitive covariance or proves a rare-event estimate. A full native high moment remains a sufficient input, not a result of this filter. The sampled capture argument in the companion note supplies a different sufficient input, with its arithmetic inequality stated as open. A bounded inverse for `T` near the critical exponent would require information about `1/L(s,chi_{-3})`; no such inverse is claimed.

The proofs here use finite coefficient identities, periodic cancellation, Abel summation, and Poisson summation for a fixed smooth function. They do not use the imported quasi-Riemann theorem or assume GRH.
