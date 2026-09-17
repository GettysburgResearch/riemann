# 07. Same-cutoff source transfer, crossings, and unconditional bounds

**Status:** proposed finite inequalities and consequences of classical source cancellation. No improvement to the classical global exponent is claimed.

## 1. Keep the two Möbius cumulative quantities distinct

Write
\[
M(x)=\sum_{n\le x}\mu(n),\qquad
m(x)=\sum_{n\le x}\mu(n)/n,
\quad
\mathscr E(N)=\int_1^N m(x)^2dx=\sum_{k=1}^{N-1}m(k)^2.
\]
This is the repository's reciprocal-Möbius accumulated energy with the displayed endpoint. It is not the same as \(\sum M(k)^2/[k(k+1)]\), though repository identities relate them with endpoint terms. Dropping those terms changes the source contract.

## 2. Finite transfer theorem

For integers N>=2 and j>=0,
\[
\boxed{Q_j(N)\le\frac N2m(N)^2+2\sqrt{2j+3}\,\mathscr E(N).}
\]
At a crossing with mu(N) nonzero and m(N-1)m(N)<=0, |m(N)|<=1/N, hence
\[
Q_j(N)\le1/(2N)+2\sqrt{2j+3}\,\mathscr E(N).
\]
The crossing removes the endpoint term. It does not bound the accumulated energy.

### Proof with complete multiplier constants

Partial summation against m gives
\[
P_N(s)=N^{1-s}m(N)+(s-1)\int_1^Nm(x)x^{-s}dx.
\]
Set v_N(u)=e^(u/2)m(e^u)1_[0,log N](u), so ||v_N||_2^2=mathscr E(N). On s=1/2+i tau,
\[
P_N(s)=\sqrt N m(N)e^{-i\tau\log N}+(-1/2+i\tau)\widehat v_N(\tau).
\]
With r=2j+3 and K_j(u)=(1/4)sech^r(u/2), its Fourier transform is W_j. We have (2pi)^(-1)integral W_j=1/4 and
\[
\sup_\tau(1/4+\tau^2)W_j(\tau)\le\sqrt r.
\]
Indeed, this multiplier is the transform of K_j/4-K_j''. The integral norm obeys ||K_j||_1<=pi/4 for r>=3. Also
\[
\|K_j''\|_1=4\max_{u>0}|K_j'(u)|
=\frac r{2\sqrt{r+1}}\left(\frac r{r+1}\right)^{r/2}
\le\sqrt r/2.
\]
Thus ||K_j||_1/4+||K_j''||_1<=sqrt r. The triangle inequality in the W_j-weighted Fourier norm gives
\[
\sqrt{Q_j(N)}\le\tfrac12\sqrt N|m(N)|+r^{1/4}\sqrt{\mathscr E(N)}.
\]
Squaring with (a+b)^2<=2a^2+2b^2 proves the theorem.

## 3. What classical cancellation currently yields

Put
\[
\Psi(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}
\]
for sufficiently large x. The classical Vinogradov–Korobov-type bound, in the forms discussed by [LL22], gives
\[
M(x)\ll xe^{-a\Psi(x)}
\]
for some a>0 after absorbing logarithmic factors.

This makes integral_1^infinity M(u)u^(-2)du absolutely convergent. Taking s down to 1 in the reciprocal-zeta Mellin identity shows that integral is zero. Partial summation then gives
\[
m(x)=M(x)/x-\int_x^\infty M(u)u^{-2}du.
\]
Writing V(v)=v^(3/5)/(log v)^(1/5), the tail is bounded by a constant times exp(-(a/2)V(log x)), since integral exp(-(a/2)V(v))dv converges. Thus
\[
|m(x)|\ll e^{-(a/2)\Psi(x)}.
\]
Because V'(v) tends to zero,
\[
\mathscr E(N)\ll N e^{-a\Psi(N)}.
\]
The finite theorem gives, uniformly in j,
\[
Q_j(N)\ll\sqrt{j+1}\,N e^{-a\Psi(N)}.
\]
At j_N=ceil(log^4N), absorb the polylogarithm by reducing the constant:
\[
B_{j_N}(N)\le Q_{j_N}(N)
\ll N\exp[-c(\log N)^{3/5}/(\log\log N)^{1/5}].
\]
This saves every fixed logarithmic power, but its logarithmic exponent still tends to 1, not 0. It does not give any fixed power saving N^(1-delta), and does not construct sparse subpower cutoffs. This packet claims the transfer, not a new underlying bound for M(x).

## 4. Why crossings alone do not close the estimate

The non-arithmetic model
\[
m_\beta(x)=x^{\beta-1}\sin(\gamma\log x),\quad1/2<\beta<1,
\]
tends to zero and has exact crossings X_r=exp(r pi/gamma). Yet with kappa=2beta-1,
\[
\int_1^{X_r}m_\beta(x)^2dx
=\frac{2\gamma^2}{\kappa(\kappa^2+4\gamma^2)}(X_r^\kappa-1).
\]
This is not a Möbius counterexample. It proves that crossing geometry and decaying pointwise values do not force small accumulated energy.

The repository's completed Newton source at reciprocal crossings has an annular covariance term. Its diagonal is logarithmic in a different normalization; the covariance remains open. Neither its favorable endpoint collar nor its cofinal crossing theorem supplies an upper estimate for that entire term.

## 5. Keep the actual finite inverse identity

For P_y(s)=sum_(n<=y)mu(n)n^(-s),
\[
\frac1{\zeta(s)}=2P_y(s)-\zeta(s)P_y(s)^2
+\frac{(1-\zeta(s)P_y(s))^2}{\zeta(s)}.
\]
Since 1-zeta P_y has no coefficients below y+1, the last term has none below (y+1)^2. Hence for y<=x<(y+1)^2,
\[
M(x)=2M(y)-\sum_{a,b\le y}\mu(a)\mu(b)\lfloor x/(ab)\rfloor
\]
\[
=2M(y)-xm(y)^2+
\sum_{a,b\le y}\mu(a)\mu(b)\{x/(ab)\}.
\]
At a crossing, the continuous term is controlled. The signed fractional-part sum is not. Product identities of this kind are classical; see [HW18] and the frozen repository Newton arguments. Decomposing the expression into absolute Type-I/II estimates can lose the cancellation that makes it an inverse in the first place.

## 6. Averaged fixed-shift estimates are not automatically variance-scale bounds

On n~X, the j_N detector sees shifts of typical size H~X/log^2N. There are XH pairs, each with weight about 1/X, so their trivial weighted mass is H. Relative o(1) cancellation gives only o(H), still of almost linear size. The averaged Chowla–Elliott results [MRT15] and the more recent short-interval uniformity results [MRSTT] do not, merely by substitution, supply the required near-diagonal/random-variance scale. Chapter 09 corrects the Fourier normalization and explains this distinction exactly.
