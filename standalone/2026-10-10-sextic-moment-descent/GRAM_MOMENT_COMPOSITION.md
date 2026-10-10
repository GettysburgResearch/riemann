# What the sextic Gram bound gives for the actual inverse moments

Status: proved composition and parameter comparison, conditional only on the stated classical inputs to the packet's Gram and refined sieve theorems. No new full moment or zero-free region is claimed, and no literature-novelty claim is made.

Dependencies: [SEXTIC_GRAM_BOUND.md](SEXTIC_GRAM_BOUND.md), Theorem 1.1, reviewed at SHA-256 `c2b6c326f929de85a4f6d50ae2f4bdf4fc089f4f4705961d1c59ea1ad35d4fe1`; [REFINED_ALL_ROW_SIEVE.md](REFINED_ALL_ROW_SIEVE.md), Theorem 3.4, reviewed at SHA-256 `6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8`; and the exact incidence identity and coefficient-mass bound in [GENERAL_MOMENT_ATTACK.md](GENERAL_MOMENT_ATTACK.md), Sections 1 and 3. All symbols retain their zeros at nonunits.

## 1. The Gram consequence, including every element row

Let \(P,H\ge1\), and let \(z_n\) be arbitrary complex coefficients on squarefree primary ideals outside the fixed bad-prime set \(S\), supported on \(P\le Nn<2P\). The Gram theorem implies

\[
\sum_{0<Nu\le H}\left|\sum_n z_n\chi_n(u)\right|^2
\ll_{S,\epsilon}(PH)^\epsilon
\left[H+P H^{1/2}+P^{3/2}H^{1/6}\right]\sum_n|z_n|^2.
\tag{1.1}
\]

This statement includes sixth powers, elements divisible by bad primes, and all units.

**Proof.** First restrict \(u\) to primary elements and use a fixed nonnegative smooth radial weight at scale \(Z\ge1\). The modulus Gram matrix has diagonal \(O(Z)\). There are \(O(P)\) column moduli, and its squared off-diagonal row sum is at most

\[
(PZ)^\epsilon G(P,Z),\qquad G(P,Z)=PZ+P^2Z^{1/3}.
\]

Cauchy–Schwarz bounds its absolute off-diagonal row sum by \(O(P^{1/2}G(P,Z)^{1/2})\), with the subpower loss reassigned. The Hermitian matrix norm, and therefore its quadratic form at \(z\), is bounded by

\[
(PZ)^\epsilon
\left[Z+\sqrt P\sqrt{PZ+P^2Z^{1/3}}\right]\sum_n|z_n|^2
\ll(PZ)^\epsilon
\left[Z+PZ^{1/2}+P^{3/2}Z^{1/6}\right]\sum_n|z_n|^2.
\tag{1.2}
\]

To cover all elements, write uniquely \(u=\eta\lambda^e w\), where \(\lambda=\sqrt{-3}\), \(e\ge0\), \(\eta\) is a unit, and \(w\equiv1\pmod3\) is the chosen primary generator of an ideal prime to \(3\). For fixed \(\eta,e\), replace the coefficients by \(z_n\chi_n(\eta\lambda^e)\), and use the primary row range \(Nw\le H/3^e\). This multiplier has modulus at most one and is independent of \(w\). It retains every zero; no row is replaced by its inducing primitive character. Only \(e\) with \(3^e\le H\) can contribute.

Choose the fixed nonnegative smooth weight to majorize the interval \([1/2,1]\). Cover each primary norm ball by dyadic annuli of scales \(Z=(H/3^e)2^{-j}\ge1\), ending with the scale in \([1,2)\). Apply (1.2) on each annulus. All three powers of \(Z\) are positive, so both the annular sum and the sum over \(e\) are bounded geometric sums at those powers. Bound the preliminary loss by \((PH)^\epsilon\); the six units give a fixed factor. This proves (1.1). Column support in any fixed compact multiple of \(P\) is handled by a fixed number of modulus annuli and Cauchy–Schwarz. \(\square\)

## 2. Comparison with the refined sieve

Write the two resulting operator majorants as

\[
K_G(H,P)=H+PH^{1/2}+P^{3/2}H^{1/6},\qquad
K_R(H,P)=H+(HP)^{2/3}+PH^{1/6}.
\tag{2.1}
\]

If \(P\ge H^{1/2}\), then

\[
PH^{1/2}\ge(HP)^{2/3},\qquad
P^{3/2}H^{1/6}\ge PH^{1/6}.
\]

Thus \(K_G\ge K_R\) term by term in the unresolved long-column range. If \(P\le H^{1/2}\), both majorants are \(O(H)\): for the Gram expression the last term is at most \(H^{11/12}\le H\), and the other terms are immediate. Therefore this direct Gram-to-operator composition gives no additional uniform balanced-core range beyond the refined sieve. This compares the proved upper-bound formulas; it is not a lower bound on the actual energy or an impossibility theorem for a different use of signed correlations.

For the actual inverse polynomial

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\]

the coefficient energy is \(O_W(D)\). Equation (1.1) consequently gives

\[
\sum_{0<Nu\le H}|A_u(D)|^2
\ll(DH)^\epsilon
\left[HD+D^2H^{1/2}+D^{5/2}H^{1/6}\right].
\tag{2.2}
\]

Near \(H=D^{1+\theta}\), this is weaker than the imported \(D^\epsilon HD\) second moment. No stronger actual-polynomial estimate follows from this direct operator bound.

## 3. Exact fourth-polynomial common-gcd consequence

Use the squarefree balanced core

\[
B_{c,u}(X)=\sum_{\substack{ab\ \mathrm{squarefree}\\(ab,cS)=1}}
\mu_K(ab)\nu(ab)\chi_{ab}(u)W(Na/X)W(Nb/X).
\]

Its product-column scale is \(P=X^2\), and its coefficient energy is \(O(D^\epsilon X^2)\), uniformly in the moving \(c\), whenever \(X\le D\). Applying (1.1) gives

\[
\sum_{0<Nu\le H}|B_{c,u}(X)|^2
\ll D^\epsilon
\left[HX^2+H^{1/2}X^4+H^{1/6}X^5\right].
\tag{3.1}
\]

Here and below \(1\le H\le D^{C_0}\) for fixed \(C_0\). Nonempty bounded scales \(X<1\) are covered by a fixed support-dependent constant.

The exact gcd decomposition of \(A_u(D)^2\) has summands \(\mu_K(c)^2\nu(c)^2\chi_c(u)^2 B_{c,u}(D/Nc)\); the exterior factor has modulus at most one. Let \(T_{\ge C}\) be its portion with \(Nc\ge C\ge1\). Take square roots in (3.1) and sum by Minkowski. The three ideal sums are, respectively, \(O(\log(2D))\), \(O(C^{-1})\), and \(O(C^{-3/2})\), from the exponents \(1,2,5/2\). Squaring and absorbing the logarithm gives

\[
\|T_{\ge C}\|_2^2
\ll D^\epsilon\left[
HD^2+H^{1/2}D^4C^{-2}+H^{1/6}D^5C^{-3}\right].
\tag{3.2}
\]

This reaches \(D^\epsilon HD^2\) when

\[
C\ge\max\{1,DH^{-1/4},DH^{-5/18}\}
=\max\{1,DH^{-1/4}\}.
\tag{3.3}
\]

It recovers the already established fourth-moment common-gcd threshold exactly; it does not enlarge it. Section 2 explains why the same direct operator composition cannot improve the uniform general incidence-core bounds either.

## 4. The product-length obstruction in the Gram formula itself

Trivially \(|T_{p,p'}(Z)|\ll_W Z\), so the off-diagonal square-sum is \(O_W(PZ^2)\). The second term of the proved Gram bound improves this trivial power only if

\[
P^2Z^{1/3}<PZ^2
\quad\Longleftrightarrow\quad Z>P^{3/5}.
\tag{4.1}
\]

For the longest fourth-moment product columns, \(P=D^2\) and \(Z=H=D^{1+\theta}\). The ratio of that term to the trivial bound is

\[
\frac{P^2Z^{1/3}}{PZ^2}=D^{(1-5\theta)/3}.
\]

It is larger by a fixed power when \(0<\theta\le1/10\); the threshold for a strict power gain is \(\theta>1/5\). Arbitrarily small sieve losses require a strict margin at the comparison boundary. The Gram theorem supplies additional correlation information, but its current absolute-square bound does not provide the short-row balanced moment needed for the proposed \(17/24\) zero-free exponent.
