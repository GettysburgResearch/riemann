# Route 2: fixed-frequency reduction and sharp causal twist transport

Status: complete mathematical arguments supplied, **PROPOSED / INDEPENDENT REVIEW REQUIRED**.
Scope: deterministic theorems for arbitrary coefficients, their exact Möbius specialization, and a failed source-blind exponent-improvement attempt. No new Möbius power saving.
Sources: PR #779 at `38023e22913eacdb8af9da804f6301f20da0332c`; the stationary coarea and maximal-prefix comparisons are rederived below.
What was run: exact summation-by-parts and sharp rational multiplier identities in `../code/verify.py`.
Smallest remaining gap: a signed arithmetic estimate for one fixed bounded frequency window, uniformly in all prefixes.

## R2.1. General frequency-ensemble theorem

Let `(b_n)` be any complex sequence and

\[
 P_t(Y)=\sum_{n\le Y}b_n n^{-it},\qquad
 B(X)=\max_{1\le Y\le X}|P_0(Y)|.
\]

For a probability measure `nu` on the real frequency line with finite second moment, define

\[
 T_2=\left(\int t^2d\nu(t)\right)^{1/2},\qquad
 E_\nu(X)=\max_{1\le Y\le X}\int|P_t(Y)|^2d\nu(t),
 \qquad C_\nu(X)=1+T_2\log X.
\]

All finite sums and integrals exist. In particular `nu` need not have compact support, a density, or a lower frame bound.

**Theorem.** For every `X>=1`,

\[
 \boxed{C_\nu(X)^{-2}B(X)^2\le E_\nu(X)\le C_\nu(X)^2B(X)^2.}
 \tag{1}
\]

### Proof

Abel summation, with the contribution at `n=1` retained, gives

\[
 P_t(Y)=Y^{-it}P_0(Y)+it\int_1^Y x^{-it}P_0(x)\frac{dx}{x}.
 \tag{2}
\]

Minkowski in `L^2(nu)` bounds the norm by `(1+T_2 log X)B(X)`.

Conversely, apply Abel summation to `b_n n^{-it}` and `n^{it}`:

\[
 P_0(Y)=Y^{it}P_t(Y)-it\int_1^Y x^{it}P_t(x)\frac{dx}{x}.
 \tag{3}
\]

Average this equality over `nu` **before** estimating. Cauchy–Schwarz gives

\[
 |P_0(Y)|\le \|P_\cdot(Y)\|_{L^2(\nu)}
 +T_2\int_1^Y\|P_\cdot(x)\|_{L^2(\nu)}\frac{dx}{x}
 \le C_\nu(X)\sqrt{E_\nu(X)}.
\]

The finite second moment suffices; a bound for `||t P_t||_2` is neither assumed nor used. Taking the maximum proves (1).

### Moving ensembles: the quantifier matters

For each outer terminal horizon `X`, one may choose `nu_X`; (1) remains valid with its root-mean-square frequency. The **same** `nu_X` must be used for every inner prefix `Y<=X`. Choosing a different measure at each inner prefix does not follow from the proof.

If `1+T_2(X)=X^{o(1)}`, this averaging cannot change the maximal-prefix power exponent. In particular, an arbitrarily narrow bounded-frequency ensemble is not an easier exponent problem simply because it is narrow.

## R2.2. Exact stationary-energy comparison

For `q>1`, set `L=log q` and

\[
 Q_q(Y)=\sum_{m,n\le Y}b_m\overline{b_n}
            \left(1-\frac{|\log(m/n)|}{L}\right)_+,
 \qquad \mathfrak Q_q(X)=\max_{Y\le X}Q_q(Y).
\]

Average the squared sums in the translated multiplicative bands
`q^(j+tau)<n<=q^(j+tau+1)` over `0<=tau<1`. A pair belongs to the same band for precisely the triangular fraction of shifts displayed in the kernel. Thus `Q_q` is that averaged band-square sum and is nonnegative.

There are at most `N_q(X)=2+ceil(log_q X)` occupied bands. Each band sum is a difference of two prefixes; the complete prefix is the sum of the bands. Therefore

\[
 B(X)^2/N_q(X)\le\mathfrak Q_q(X)\le4N_q(X)B(X)^2.
 \tag{4}
\]

Combining (1) and (4) gives

\[
 \boxed{
 \frac{\mathfrak Q_q(X)}{4N_q(X)C_\nu(X)^2}
 \le E_\nu(X)
 \le N_q(X)C_\nu(X)^2\mathfrak Q_q(X).
 }
 \tag{5}
\]

For any fixed `nu` of finite second moment the loss is `O((log X)^3)`.

This closes a useful part of the proposed architecture: the growing square-root frequency window is unnecessary **for equivalence at the subpower scale**. A fixed interval, such as `[1,2]`, suffices. This is not a claim that the discarded frequencies are absolutely small or that their separate values have been estimated.

## R2.3. Literal Möbius specialization and complete RH implication

Take

\[
 b_n=\mu(n)\mathbf1_{67\nmid n}/\sqrt n.
\]

Let `nu` be uniform probability on `[1,2]`, fixed once and for all. Then

\[
 \boxed{\mathfrak Q_{67}(X)=X^{o(1)}
 \quad\Longleftrightarrow\quad
 \max_{Y\le X}\int_1^2
 \left|\sum_{n\le Y,\,67\nmid n}\mu(n)n^{-1/2-it}\right|^2dt=X^{o(1)}.}
 \tag{6}
\]

Here `X^{o(1)}` means an upper bound `O_epsilon(X^epsilon)` for every positive epsilon; it does not prescribe a nonzero asymptotic main term.

For completeness, the finite-Euler transport is exact. With

\[
 A_q(Y)=\sum_{n\le Y,q\nmid n}\mu(n)/\sqrt n,
 \quad A(Y)=\sum_{n\le Y}\mu(n)/\sqrt n,
\]

one has `A(Y)=A_q(Y)-q^(-1/2)A_q(Y/q)` and

\[
 A_q(Y)=\sum_{j\le\log_qY}q^{-j/2}A(Y/q^j).
\]

Both maximal-prefix transports have bounded cost. Thus (6) is equivalent to `A(Y)=O_epsilon(Y^epsilon)`. A second Abel summation yields

\[
 M(Y)=\sum_{n\le Y}\mu(n)
 =\sqrt Y A(Y)-\tfrac12\int_1^Y A(x)x^{-1/2}dx
 =O_\epsilon(Y^{1/2+\epsilon}).
\]

The Dirichlet series for `1/zeta(s)` then converges locally uniformly on `Re s>1/2`, excluding zeta zeros there; reflection gives RH. Conversely, the standard RH-to-Mertens bound and Abel summation give the premise. The reverse analytic implication is classical, not a new estimate of this pass.

The final uniformity is over **all** prefixes. A bound at a sparse sequence of endpoints has not been substituted.

## R2.4. Sharp damped Hilbert-space transport

There is an exact operator strengthening of (2)–(3). For `sigma>0`, define

\[
 \mathcal E_\sigma(t)=\int_1^\infty |P_t(X)|^2X^{-2\sigma}\frac{dX}{X}.
\]

Initially take finite coefficient support, so every integral is finite. More generally, the result holds whenever the untwisted function below belongs to `L^2(0,infinity)`.

**Theorem.** With

\[
 k(\sigma,t)=\frac{\sqrt{t^2+4\sigma^2}+|t|}{2\sigma},
\]

one has

\[
 \boxed{k(\sigma,t)^{-2}\mathcal E_\sigma(0)
 \le\mathcal E_\sigma(t)
 \le k(\sigma,t)^2\mathcal E_\sigma(0).}
 \tag{7}
\]

These are sharp operator constants on the ambient causal `L^2` space, not a claim of sharpness on the particular Möbius vector.

### Proof

Put `u=log X`, `f(u)=e^(-sigma u)P_0(e^u)` and
`g_t(u)=e^(-sigma u)e^(itu)P_t(e^u)`. Equation (2) becomes

\[
 g_t(u)=f(u)+it\int_0^u e^{-(\sigma-it)(u-v)}f(v)dv.
 \tag{8}
\]

After extending by zero to the negative line, its Fourier multiplier is

\[
 R_{\sigma,t}(\omega)=\frac{\sigma+i\omega}{\sigma+i(\omega-t)}.
 \tag{9}
\]

The inverse is the causal multiplier `1-it/(sigma+i omega)`. The supremum and reciprocal infimum of the modulus of (9) equal `k(sigma,t)`. One exact algebra check is

\[
 \sigma^2(A-B)^2-t^2AB
 =-t^2(\sigma^2+t\omega-\omega^2)^2,
\quad A=\sigma^2+\omega^2,\ B=\sigma^2+(\omega-t)^2.
 \tag{10}
\]

The equality frequencies solve `omega(omega-t)=sigma^2`. Plancherel proves (7). Long causal wave packets concentrated at such a frequency prove sharpness; their initial boundary contribution is negligible relative to their length.

For fixed nonzero `t`, the norm diverges like `|t|/sigma` as `sigma` tends to zero. The critical boundary is not obtained by setting `sigma=0` in a bounded-invertibility assertion.

## R2.5. Attempted exponent contraction: what failed

The proposed goal remains a source-specific implication

\[
 \mathfrak Q(X)\ll_\epsilon X^{a+\epsilon}
 \ \Longrightarrow\
 \mathfrak Q(X)\ll_\epsilon X^{(1-\kappa)a+\epsilon}
 \tag{11}
\]

with fixed `kappa>0`, or a sufficiently uniform weakening that iterates to exponent zero. No instance with new arithmetic power saving is proved here.

The following attempted shortcut fails. Average over a long frequency interval, use the standard Dirichlet-polynomial mean value bound, and transfer back using (1). For a length-`X` half-weighted bounded source, the mean-value envelope is of size `log X+X/T` at frequency length `T`. The back-transfer costs roughly `(1+T log X)^2`. Even after optimization this does not give a power improvement over `X`.

There is a direct countercontrol against a source-blind improvement. The positive coefficients `b_n=n^(-1/2)` satisfy all deterministic identities above, while uniformly for `t` in a fixed compact interval

\[
 P_t(Y)=\frac{Y^{1/2-it}}{1/2-it}+O_t(1),
\]

and hence their fixed-band energy grows like a positive constant times `Y`. Thus transport, frequency averaging and positivity alone cannot prove (11). The Möbius signs must enter in a genuinely new estimate.

The immediate arithmetic task can now be frozen at the small, explicit target in (6), with exact signed polarization before any norm. Existing almost-all short-interval theorems are a methodological input, not a proof of this all-prefix critical bound. This pass has reduced the presentation and quantified the transport cost; it has not reduced the arithmetic exponent.
