# A wider independent-frequency tube with a quadratic phase cost

Status: proved enlargement of the subcritical collision tube. The region
still shrinks as 1/logY; its complement and the full source moment remain
unpaid. Every row, source ray phase and principal zero is retained.

## WT1. Exact pair floor without a linear perturbation loss

Use the full pair factorization P1–P4 of `PRIME_SLOT_CANCELLATION.md`,
SHA256 `d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`.
Fix k>=1, 1/3<sigma<1/2, and

\[
 0<\kappa<\arcsin(1/\sqrt{2k}).
\tag{WT1}
\]

The tube consists of all independent frequencies satisfying, for some
arbitrary central t,
`|t_i-t|<=kappa/logY` on the left and
`|t_(k+j)+t|<=kappa/logY` on the right.
At an eligible prime q=Np<=Y, write its normalized variables as

\[
 v_i=a e^{-i\delta_i\log q},\quad
 v_{k+j}=\overline a e^{-i\varepsilon_j\log q},\qquad
 a=\eta_u(p)q^{-it},\quad |a|=1.
\tag{WT2}
\]

All k^2 cross pairs have real part at least cos(2kappa): the central
frequency and a phases cancel exactly, and
`|(delta_i+epsilon_j)logq|<=2kappa<pi/2`. The total of the k(k-1)
same-side pairs has real part at least -k(k-1), with no constraint on a.
Therefore the complete pair sum has the uniform floor

\[
 \Re\sum_{i<j}v_i v_j\ge
 k^2\cos(2\kappa)-k(k-1)
 =k[1-2k\sin^2\kappa]=:\lambda_{\rm quad}>0.
\tag{WT3}
\]

No separate same-side phase was assumed conjugate after perturbation.
Both collections were bounded with their actual factors present. The
quadratic loss in WT3 improves the earlier linear perturbation loss.

## WT2. Rapid collision decay on the enlarged region

Put alpha=2sigma. The elementary pair logarithm estimate of ST9 has a
summable quadratic remainder because 2alpha>1. WT3 consequently bounds
the pair product by a constant times
`product_(eligible p)(1-(Np)^(-alpha))^(lambda_quad)`.
The degree-three remainder remains uniformly bounded since 3sigma>1.
The arbitrary-power positive Euler lemma RD1–RD4 of
`SUBCRITICAL_RAPID_COLLISION_DECAY.md`, SHA256
`a41b84b54f0e4052e6700887bad5cd82552ab452744f29c1b5f70e68cbf0735e`,
and the explicit moving-mask bound then give, for every A>0,

\[
 |Q_{\rm coll}|\ll_A Y^{-A}(Nu NQ)^{\epsilon_0}.
\tag{WT4}
\]

For source NQ<=Y^k and H comparable to Y^h, enlarging the fixed power
requested in RD4 absorbs the factor Y^((h+k)epsilon_0), giving the
complete row version

\[
 |Q_{\rm coll}|\ll_A Y^{-A}(1+Nu/H)^{\epsilon_0}.
\tag{WT5}
\]

The constants may depend on k,sigma,kappa,A,epsilon_0,h and fixed source
data, but not on Y,u,Q,the central frequency or slot perturbations.
The same short-polynomial transport SC2–SC5 in
`SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`, SHA256
`c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac`,
therefore makes the enlarged tube's complete source-incidence component
O_M(HY^(-M)) for every fixed M>0. This concerns the short representation,
not a claimed pointwise equality with the original Euler integrand.

## WT3. A simple explicit width and exact limitations

One may take `kappa=1/(2sqrt(k))`, because sin(kappa)<kappa gives
`lambda_quad>k/2`. This replaces the older half-floor width
`1/[4(2k-1)]` by a larger explicit width. Its actual Mellin width is
still kappa/logY, not a fixed positive width as Y grows.

The arbitrary-power statement is uniform for fixed k and kappa; no
uniformity as k grows or kappa reaches the critical endpoint is claimed.
The individual original reciprocal factors may be large, and the short
representation's complement remains unpaid. No full moment or RH
boundary is deduced from this larger region.

`check_wide_subcritical_tube.py` directly controls all source sextic
phases, four actual good prime norms, three central frequencies, and
every endpoint sign allocation for k=1,2,3,4. It checks the complete
pair floor and convergent-log local inequality. The continuum and
arbitrary source ray phases are proved by WT2–WT3, not by a finite
phase sample.
