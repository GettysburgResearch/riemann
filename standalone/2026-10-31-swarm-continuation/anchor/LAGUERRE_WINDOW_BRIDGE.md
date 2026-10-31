# From moving-anchor matrices to literal support windows

Status: proposed component theorems with complete proofs. The results identify the proportional degree/anchor limit, justify passage of the **complete** prime operator, and transfer a compact-window lower bound to the actual xi matrices. They do not prove positivity on unbounded windows, RH, or a new zero-free boundary.

The preceding packet's exact observation map identifies the matrix space with

\[
 V_{N,a}=\operatorname{span}\{u_{n,a}:0\le n\le N\},\qquad
 u_{n,a}(u)=\sqrt{2a}e^{-au}L_n(2au)
\]

inside `H=L^2(0,infinity)`. Let P_(N,a) be its orthogonal projection. The present arguments use the geometric Laguerre coefficients already proved there. The Laguerre multiplication identity used below is also classical; see [DLMF 18.18.12](https://dlmf.nist.gov/18.18.E12).

## 1. The proportional regime has an exact support limit

For `ell>=0`, let Q_ell be multiplication by the indicator of `[0,ell]` on H.

**Theorem 1.** If `a_j -> infinity` and `N_j/a_j -> L` with `0<=L<infinity`, then

\[
 P_{N_j,a_j}\longrightarrow Q_{2L}
 \quad\text{strongly on }H.
\tag{1}
\]

For `N_j/a_j -> infinity`, the limit is the identity. Thus a finite ratio is a literal finite time-support window, rather than an unspecified incomplete test space.

**Proof.** Put `h_b(u)=sqrt(2b)exp(-bu)` for b>0. Its coefficient in u_(n,a) is

\[
 \langle u_{n,a},h_b\rangle=
 \frac{2\sqrt{ab}}{a+b}\left(\frac{b-a}{b+a}\right)^n.
\]

Summing the geometric cross-product gives the exact identity

\[
 \langle h_b,P_{N,a}h_c\rangle
 =\frac{2\sqrt{bc}}{b+c}
 \left[1-\left(\frac{(a-b)(a-c)}{(a+b)(a+c)}\right)^{N+1}\right].
\tag{2}
\]

For a tending to infinity, the logarithm of the parenthesized ratio is
`-2(b+c)/a+O(a^-3)`. Under the finite-ratio assumption, (2) tends to

\[
 \frac{2\sqrt{bc}}{b+c}(1-e^{-2L(b+c)})
 =\langle h_b,Q_{2L}h_c\rangle.
\]

The span of the h_b is dense, by uniqueness of the Laplace transform. Since the P are contractions, the displayed convergence extends to weak convergence on all H. A weak limit that is itself an orthogonal projection is automatically a strong limit here: for every h,

\[
 \|P_jh-Qh\|^2
 =\langle h,P_jh\rangle-2\Re\langle P_jh,Qh\rangle+\|Qh\|^2\longrightarrow0.
\]

The same argument gives the identity for infinite ratio. Alternatively that case is the completeness theorem in the preceding packet. This proves (1).

There is no operator-norm convergence to Q_(2L) when L>0: each P has finite rank and Q_(2L) has infinite rank. The distinction matters for spectral-floor claims and is addressed separately in Section 5.

## 2. Uniform exponential-weight control

Strong unweighted convergence alone cannot justify summing the prime terms. The following estimate supplies the missing control.

**Lemma 2.** For `eta>0`, `a>eta`, and every phi in V_(N,a),

\[
 \|e^{\eta u/2}\phi\|_2^2\le W_{N,a}(\eta)\|\phi\|_2^2,
\tag{3}
\]

where

\[
 W_{N,a}(\eta)=\frac a{a-\eta}
 \left[\frac{a(a+\eta/2)}{(a-\eta)(a-\eta/2)}\right]^N.
\tag{4}
\]

If `a_j -> infinity`, `N_j/a_j -> L<infinity`, then `W_(N_j,a_j)(eta) -> exp(2 eta L)`.

**Proof.** Write `phi=sqrt(2a)exp(-au) sum_(n=0)^N c_n L_n(2au)`, so `||phi||²=sum |c_n|²`. Set `q=a/(a-eta/2)`, which lies between one and two. Changing variable to `y=(2a-eta)u` and using the multiplication formula gives

\[
 \|e^{\eta u/2}\phi\|^2=q\|D(q)c\|_{\ell^2}^2,
 \quad D_{kn}(q)=\binom nk q^k(1-q)^{n-k}\quad(k\le n).
\]

Its maximum absolute column sum is `(2q-1)^N`. Its row sums satisfy

\[
 \sum_{n=k}^N\binom nk q^k(q-1)^{n-k}
 \le\frac{q^k}{(2-q)^{k+1}}
 \le\frac{q^N}{(2-q)^{N+1}}.
\]

The elementary Schur estimate `||D||_2²<=||D||_1||D||_infinity` therefore gives

\[
 q\|D\|_2^2\le\frac q{2-q}
 \left[(2q-1)\frac q{2-q}\right]^N=W_{N,a}(\eta).
\]

The stated limit follows by taking logarithms: the logarithm of the bracket in (4) is `2 eta/a+O_eta(a^-2)`. This proves the lemma.

**Corollary 3.** Under Theorem 1's finite-ratio assumptions, for every fixed eta>=0 and h in H,

\[
 e^{\eta u/2}P_jh\longrightarrow e^{\eta u/2}Q_{2L}h
 \quad\text{in }L^2.
\tag{5}
\]

More generally, if `phi_j in V_(N_j,a_j)` is bounded in norm and converges strongly in unweighted L² to phi, it converges in every fixed exponentially weighted L² norm.

**Proof.** On a bounded u interval this follows from unweighted convergence. For the tails, apply (3) at any larger exponent eta'>eta:

\[
 \int_R^\infty e^{\eta u}|\phi_j(u)|^2du
 \le e^{-(\eta'-\eta)R}W_j(\eta')\|\phi_j\|^2.
\]

The constants are bounded. The limit has the same weighted tail bound by Fatou. Let R tend to infinity after taking the local limit. This proves (5) and the more general assertion.

## 3. The complete prime operator converges to a finite delay operator

Let `T_t phi(u)=phi(u+t)` for t>=0, and let Lambda denote the von Mangoldt function. Define on H

\[
 \mathcal P_j=\sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}
 P_jT_{\log m}P_j.
\tag{6}
\]

This is the complete arithmetic operator appearing in the observation representation of the actual matrix source. Translation preserves V_(N,a), so the leading P_j in each term is redundant, but is retained to display the compression.

**Theorem 4.** Under the finite-ratio assumptions,

\[
 \mathcal P_j\longrightarrow
 \mathcal P_{2L}:=
 \sum_{2\le m<e^{2L}}\frac{\Lambda(m)}{\sqrt m}
 Q_{2L}T_{\log m}Q_{2L}
\tag{7}
\]

strongly, and their adjoints also converge strongly. Their operator norms are bounded uniformly for all sufficiently large j. The arithmetic Hermitian parts therefore converge strongly as well.

**Proof.** If phi lies in V_j, then

\[
 \|T_t\phi\|^2=\int_t^\infty|\phi(u)|^2du
 \le e^{-\eta t}W_j(\eta)\|\phi\|^2.
\]

Choose any fixed eta>1. Consequently

\[
 \left\|\frac{\Lambda(m)}{\sqrt m}P_jT_{\log m}P_j\right\|
 \le\sqrt{W_j(\eta)}\frac{\Lambda(m)}{m^{(1+\eta)/2}}.
\tag{8}
\]

The right-hand series converges and its prefactor is eventually bounded. For each fixed m, strong convergence of P_j proves strong convergence of the compressed shift; the same is true of its adjoint. Split the sum at a finite cutoff and use (8) on the tail. This proves strong and strong-adjoint convergence of the complete operator, rather than just of a finite prime prefix.

Finally `Q_ell T_t Q_ell=0` for t>=ell. Thus the limit is the finite sum displayed in (7); equality at the endpoint contributes nothing in L². This proves the theorem.

### Exact prime visibility

A prime power m first becomes visible precisely when `2L>log m`. The first prime appears at `L>(log 2)/2`. The old unconditional family `a=100(N+1)` has `L=1/100` and limiting support length `1/50`: **its entire arithmetic operator tends strongly to zero**. This supplies a literal source explanation for that family's limited reach.

This does not mean that finite matrices in the family contain no primes. They contain the full convergent arithmetic sum; it is the proved limiting operator that vanishes.

## 4. The actual xi form in physical coordinates

To handle the spectral floor, more than fixed-vector convergence is needed. The logarithmic archimedean term supplies the required compactness.

Extend phi in H by zero to the full line and write

\[
 C_\phi(t)=\int_0^\infty\overline{\phi(u)}\phi(u+t)du,\qquad
 k(t)=\frac{e^{-t/2}}{1-e^{-2t}},
\]

\[
 \kappa=\tfrac12\psi(1/4)-\tfrac12\log\pi,
 \qquad
 D(\phi)=\int_0^\infty k(t)
    (\|\phi\|^2-\Re C_\phi(t))\,dt.
\tag{9}
\]

The integrand in D is nonnegative. Define the pole moments

\[
 F_\pm(\phi)=\int_0^\infty e^{\pm u/2}\phi(u)du.
\]

On finite support, or for sufficiently exponentially decaying phi in the form domain of D, define

\[
\begin{aligned}
 \mathcal Q(\phi)={}&\kappa\|\phi\|^2+D(\phi)
 +\Re\{F_+(\phi)\overline{F_-(\phi)}\}\\
 &-\sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}\Re C_\phi(\log m).
\end{aligned}
\tag{10}
\]

**Exact source identity.** If `phi=O_(N,a)q` and a>1/2, then

\[
 \mathcal Q(\phi)=q^*G_N(a)q.
\tag{11}
\]

**Proof.** The arithmetic term is the exact observation identity from the preceding packet. For the two rational terms of `xi'/xi`, the semigroup formula gives

\[
 \Re\langle\phi,(A^{-1}+(A-I)^{-1})\phi\rangle
 =\int_0^\infty2\cosh(t/2)\Re C_\phi(t)dt
 =\Re\{F_+\overline{F_-}\}.
\]

These integrals converge because phi is an exponential times a polynomial with a>1/2. The last equality is the symmetric double-integral identity for the kernel `cosh((u-v)/2)`.

For the gamma factor, the digamma integral, with its cancellation at t=0 retained, gives

\[
 \Re\langle\phi,[\tfrac12\psi(A/2)-\tfrac12\log\pi]\phi\rangle
 =\kappa\|\phi\|^2+
 \int_0^\infty k(t)(\|\phi\|^2-\Re C_\phi(t))dt.
\]

One can check the scalar normalization at `phi=h_b`: the added integral is `1/2[psi(1/4+b/2)-psi(1/4)]`. Functional calculus for the finite matrix or the semigroup integral then proves the formula. Near zero the difference of autocorrelations is O(t) for these smooth exponentially decaying functions, so the integral is finite. This proves (11) with the exact actual source.

Equation (10) is the classical Weil form in the normalization of the present matrices. It is **one half** the common normalization whose RH zeros-side expression is `sum_rho |hat phi(Im rho)|²`. The compact-window mechanism and prime thresholds are classical; the point here is the proved transfer from the moving Laguerre family. Numerical constants from other papers must be converted to this normalization before use.

### Logarithmic frequency control

With `hat phi(tau)=integral_R phi(u)exp(-i tau u)du`, Tonelli and Plancherel give

\[
 D(\phi)=\frac1{2\pi}\int_{\mathbb R}d(\tau)|\widehat\phi(\tau)|^2d\tau,
 \quad d(\tau)=\int_0^\infty k(t)(1-\cos(\tau t))dt.
\tag{12}
\]

This is a closed nonnegative quadratic form. The elementary bounds on k near zero and its exponential tail show that d grows comparably to `log(2+|tau|)`, up to additive constants. For a direct lower bound, on 0<t<=1 one has `k(t)>=exp(-1/2)/(2t)`, and for R>=1,

\[
 \int_0^R\frac{1-\cos x}{x}dx\ge\log R-3.
\]

The latter follows by integrating `cos x/x` by parts on [1,R]. Hence

\[
 d(\tau)\ge\frac{e^{-1/2}}2(\log|\tau|-3),\qquad |\tau|\ge1.
\tag{13}
\]

An upper bound `d(tau)<=C log(2+|tau|)` follows by splitting t at `1/(1+|tau|)` and at one, using `1-cos x<=min(x²/2,2)`.

## 5. A source-specific spectral-floor transfer

For ell>0 define

\[
 \lambda(\ell)=\inf\{\mathcal Q(\phi):
    \|\phi\|=1,\ \operatorname{supp}\phi\subset[0,\ell],\ D(\phi)<\infty\}.
\tag{14}
\]

The pole and prime terms are bounded operators on a fixed finite window, so this infimum is finite. The closed form has compact resolvent on that window, by the logarithmic frequency bound; thus its infimum is attained. Compactness can also be proved directly as below, without invoking operator terminology.

**Theorem 5.** If `a_j -> infinity` and `N_j/a_j -> L` with `0<L<infinity`, then for the actual xi matrices,

\[
 \liminf_{j\to\infty}\lambda_{\min}G_{N_j}(a_j)
 \ge\lambda(2L).
\tag{15}
\]

In particular a verified compact-window inequality `Q(phi)>=c||phi||²` on `[0,2L]`, with c>0, implies `G_(N_j)(a_j)>=(c/2)I` eventually. This is an all-order implication for a fixed ratio, not merely convergence on a fixed finite list of vectors.

**Proof.** If the liminf in (15) is infinite there is nothing to prove. Otherwise choose a subsequence and normalized minimum eigenvectors q_j whose eigenvalues tend to that liminf and remain bounded above. Let `phi_j=O_j q_j`, so `||phi_j||=1` and `Q(phi_j)` equals the eigenvalue by (11).

By Lemma 2, the phi_j have uniformly bounded exponential-weighted norms at every fixed exponent. In particular the arithmetic forms are uniformly bounded in absolute value by (8). The pole form is also uniformly bounded: for eta>1,

\[
 |F_+(\phi_j)|\le
  \frac{\|e^{\eta u/2}\phi_j\|}{\sqrt{\eta-1}},
 \qquad |F_-(\phi_j)|\le\|\phi_j\|=1.
\]

Equation (10) therefore bounds D(phi_j) above uniformly. It also bounds the eigenvalues below uniformly, so the selected liminf is finite.

The exponential weight bound makes spatial tails uniformly small. Equations (12)--(13) make Fourier tails uniformly small. These two properties imply precompactness in L²: cut off space at R and Fourier frequency at T; the resulting operator is Hilbert–Schmidt, and the discarded L² tails tend to zero uniformly as R,T increase. After a subsequence, `phi_j -> phi` strongly in L², with `||phi||=1`.

Since `P_j phi_j=phi_j` and `P_j -> Q_(2L)` strongly, the limit satisfies `Q_(2L)phi=phi`. It is therefore supported in the required window. Corollary 3 upgrades the convergence to every fixed exponential weight. The pole moments consequently converge. The complete arithmetic form also converges: its bilinear autocorrelations obey

\[
 |C_{v,w}(t)|\le e^{-\eta t/2}
 \|e^{\eta u/2}v\|\,\|e^{\eta u/2}w\|,
\]

so eta>1 supplies a convergent dominating prime series for differences of the quadratic forms. Finally D is lower semicontinuous by (12). Thus

\[
 \lambda(2L)\le\mathcal Q(\phi)
 \le\liminf_j\mathcal Q(\phi_j)
 =\liminf_j\lambda_{\min}G_{N_j}(a_j).
\]

This proves (15).

The proof does not pass an unbounded form through bare strong convergence. It uses the actual source's logarithmic frequency coercivity to obtain compactness of possible minimizing vectors, and the exponential-weight lemma to control the full arithmetic sum and pole moments.

## 6. What happens as a window crosses a prime threshold

The limiting arithmetic interaction at a fixed delay t is a truncated shift. Its Hermitian part has an exact norm description. Decompose `[0,ell]` into chains `r,r+t,r+2t,...` with `0<=r<t`. Each chain carries the path-graph matrix with off-diagonals one half. Hence, when 0<t<ell,

\[
 \left\|\frac{Q_\ell T_tQ_\ell+Q_\ell T_t^*Q_\ell}{2}\right\|
 =\cos\frac{\pi}{\lceil\ell/t\rceil+1}.
\tag{16}
\]

The same number is its maximum eigenvalue; its minimum is the negative of that number. The chain eigenvectors have coordinates `sin(j k pi/(n+1))`, proving the formula directly.

In particular, for `t<ell<2t`, a newly visible prime-power term has Hermitian norm exactly `Lambda(m)/(2 sqrt(m))`, however small `ell-t` is. It acts between the two short endpoint intervals. Thus window extension is not a small perturbation in the ordinary operator norm merely because the newly exposed interval is short. Archimedean frequency control, signed interactions, or a form-relative estimate is needed.

There is nevertheless no jump of the actual spectral floor at a prime threshold. The function lambda(ell) is nonincreasing and continuous for ell>0. Monotonicity follows from inclusion of form domains. For lower semicontinuity, repeat the compactness argument for minimizing vectors in a bounded family of windows; the bounded prime and pole terms converge in L², and D is lower semicontinuous. For upper semicontinuity, approximate a minimizer by smooth functions supported strictly inside the window and use those same trial functions at nearby lengths.

For completeness, that core approximation is legitimate in the logarithmic form domain: slightly contract and translate the function into the interior, then mollify. In Fourier space contraction/translation are strongly continuous in `L²((1+log(2+|tau|))d tau)` (first verify this on compact-frequency functions and use the bounded comparability of the logarithmic weight under nearby dilations); mollification converges by dominated convergence. The prime and pole forms are bounded on a common compact window. This proves the required approximation and continuity. Continuity alone cannot propagate positivity through all window lengths: the floor can approach or reach zero.

## 7. Attribution, consumers, and the remaining gap

Compact-support Weil positivity and its prime-entry thresholds are established research directions, not inventions of this packet. Primary sources include Connes–Consani, [Weil positivity and trace formula, the archimedean place](https://arxiv.org/abs/2006.13771), and [arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2), whose HTML version credits Xuefeng Zhu. The latter states a certified inequality for support length 1.6, along with a retraction of an earlier larger-support claim. Its full certificate has not been replayed here, so no numerical constant from that paper is imported as an independently checked premise. Its standard Weil form has twice the normalization of (10).

The source-specific additions developed here are the elementary support-limit formula, the explicit exponential-weight estimate, passage of the entire prime operator, and the lower-spectral-bound transfer to actual moving-anchor matrices. No exhaustive priority claim is made.

The old positive-part anchor budget is ruled out by the companion obstruction theorem. The replacement is now precise: establish compact-window coercivity for increasing window lengths, preserving the signed prime correlations, and use (15) at each fixed length before a diagonal choice of large anchors. An unbounded sequence of positive windows would combine with the preceding moving-anchor criterion to imply RH. **No such unbounded window theorem is proved here.**
