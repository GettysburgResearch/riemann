# The exact tilted determinant does not equal its formal moment polynomial

18 November 2026. The director read Petrov's primary v1 §§2–4, including Theorem 2.4, (2.6), (3.3)–(3.7), Theorem 4.4, and Propositions 4.6–4.7. The two independent comparisons and a separate exact rational replay agree. This is a checked compatibility result and a rejected identification, not an objection to Petrov's theorem or a claim of publication novelty. The newer finite Schur-complement and quantitative witness investigations remain separate pending reviews.

Primary source: Leonid Petrov, *A Borodin–Okounkov–Geronimo–Case identity for tilted Toeplitz minors*, arXiv:2605.24976v1, 24 May 2026, 34 pages. SHA-256 `f8b1c3386d49e61e767ae969a02131b509a42af276151ff04492b8be75a79214`. [Versioned PDF](https://arxiv.org/pdf/2605.24976v1). Local source bytes are retained privately in `sources/round13_petrov/`; the distribution provides links and original analysis.

## Applicable source theorem and exact matching

The source assumes a nonvanishing zero-winding symbol with log phi in C^alpha for some alpha>1/2, bounded interior analytic column tilts and bounded exterior analytic row tilts, and invertible finite Gram matrix Gamma. Its Theorem 4.4 factors the unnormalized tilted minor as G(phi)^m times the strong Szegő factor, det Gamma and a Fredholm determinant on an oblique tail. The CUE specialization below separately normalizes by the value at zero. Proposition 4.6 requires an additional invertibility condition for a fixed-tail chart; this is not an unconditional change of coordinates.

Let N≥2 be CUE size, J≥1 the fixed deleted rank, m=N−1 free angles and n=m+J=N+J−1 ambient modes. The global root/derivative tilt |Z'|^(2(J−1)) gives the free-angle weight product |1−w|^(2J). Put X=T((1−w)^J)|_(P_m); X has range in P_n. Let

```text
F_+(w)=−sum_(k in band) w^k/(2k), F_−(w)=F_+(w^−1),
phi=exp(z(F_++F_−)), H_N=sum_(k in band)1/k.
```

The symbol and tilt regularity hypotheses hold at every fixed N and complex z. Gram invertibility is established here for real z and in a complex neighborhood of zero. With its R=X* T(phi_+), C=T(phi_−)X and Gamma=RC, Theorem 4.4, ordinary BOGC and finite Jacobi yield

```text
det(U* A_n^−1 U)=(det Gamma/det Gamma(0)) L_obl/L_n,
A_n=P_n T(phi)|_(P_n),
L_obl=det_(ker R)(I−Pi_(ker R) K|_(ker R)),
L_n=det_(Q_n)(I−Q_n K|_(Q_n)).
```

Here U is an orthonormal basis for the J-dimensional complement of X in P_n, K=H(phi_−/phi_+)H(tilde(phi_+/phi_−)), and the marked root factor cancels in this quotient. Its transform has the separate factor exp(−H_N z); the strong Szegő factor is exp(H_N z²/4). An all-order polynomial obtained by extrapolating low Taylor coefficients cannot be identified with the Gram alone.

For real z, C*=R, C is injective, Gamma=C*C is positive definite, and the oblique projection becomes an orthogonal projection. The Toeplitz product formula gives I−K=T(b)T(b)* with b=phi_−/phi_+. Both Wiener–Hopf factors are boundedly invertible. Thus I−K and its compression to ker R are bounded below by positive constants at every fixed N,z; K is trace class and L_obl>0. The exact Gram and exact tail factor have no real zero. This concerns the real Laplace axis; no arbitrary complex transversality is asserted.

## The tail contributes already at order two

Inside the coefficient window, where both signed frequency totals are ≤n, the ordinary ambient tail has no nonconstant contribution. The tilted tail has the term

```text
L_obl(z)=1−kappa_(J,N) z²+O(z³),
kappa_(J,N)=sum_(j<J)||H(F_+)* U_j||²>0
```

whenever the largest band index is ≤n and the band is nonempty. The constant deleted mode and the common sign of its Hankel coefficients give strict positivity. Therefore the normalized Gram differs from the complementary determinant even at quadratic order, for 2 max(band)≤n. Remove the same mass factor exp(J H_N z) from both when comparing with the formal polynomial; since constant and linear terms agree, the quadratic difference stays kappa_(J,N).

For fixed 0<a<b≤1/2 the Riemann-sum limit of this difference is

```text
(1/4)sum_(j<J) integral_0^b
 [integral_0^1 1_(a<s+t≤b) u_j(s)/(s+t) ds]^2 dt >0,
u_j(s)=sqrt(2j+1) P_j(2s−1).
```

The kernel is bounded because a>0; the discontinuity lines have measure zero. This proves a genuine mismatch within the valid moment range, rather than relying only on an extrapolated positive-real zero. The mass-normalized complementary determinant agrees coefficientwise with the formal polynomial through the supported window; its full polynomial degree need not fit in that window. The exact quotient involves both factors. A positive zero of the formal polynomial does not force an exact factor to become zero or negative.

## Exact finite witness and optional chart

For N=4,J=2 and the single frequency k=2, m=3,n=5. Independent rational matrix extraction gives

```text
det Gamma/det Gamma(0)=1+z/4+33z²/800+O(z³),
det(U* A_n^−1 U)=1+z/4−3z²/200+O(z³).
```

The quadratic gap is exactly 9/160, also obtained from the projected Hankel trace. The optional chart B=R P_m has

```text
det B=−(z³+4z²−64z−128)/128.
```

It equals 1 at z=0 and −1 at z=8. Thus it is singular at a positive real point while the exact Gram, oblique tail and finite Laplace transform remain positive. This witnesses failure of the extra chart hypothesis, not failure of Theorem 4.4. It does not identify that singularity with the formal polynomial's zero.

[Independent geometric derivation](geometry97_petrov_gram_match.md) · [Independent functional-analytic check](analytic100_petrov_match_skeptic.md) · [Director's exact rational code](../../experiments/code/director_petrov_quadratic_round13.py) · [PASS receipt](../../experiments/results/director_petrov_quadratic_round13.json)

## Concrete next question

Find a quantitative finite-dimensional representation of the tail quotient with a uniform error in N and bounded real z. The algebra must keep both factors; discarding the tilted tail is already false at degree two. A useful result would control the higher Fourier chambers and explain how the exact positive transform repairs the signed polynomial. Extending this intrinsic RMT calculation would not extend the separate RH-conditional arithmetic moment support rb<1/2.
