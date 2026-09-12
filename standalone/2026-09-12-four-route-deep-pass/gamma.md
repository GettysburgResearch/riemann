# Native gamma route: deep audit, an exact path comparison, and a sign obstruction

Date: 2026-09-12. This is a read-only research assessment of frozen proposed manuscripts. The new lemmas below are written arguments awaiting independent review. **No vanishing-defect estimate or RH proof is established.**

The main conclusion is more specific than a ranking: the gamma route has a defensible source-to-defect consumer and now two genuinely different native interpolation mechanisms. Its obstruction is the sign and cumulative size of a complete oscillatory current. The latest shape interpolation improves analytic regularity enough to handle every exceptional zero throughout one fixed step; it does not make that current dissipative. A new exact comparison below explains how the shape and scale paths differ. A positive-density counterexample explains why normalization, variance constraints, and Fisher information cannot supply the missing sign by themselves.

## 1. Sources read and boundaries of this review

The principal frozen sources are:

- **GFD26 / #862**, `67d5d6a5f588642f4c451fe35d2369b5ddac9346`, [finite-defect proof](https://github.com/GettysburgResearch/riemann/blob/67d5d6a5f588642f4c451fe35d2369b5ddac9346/standalone/2026-09-10-gamma-finite-defect/PROOF.md). Full proof read, including source convergence, two-sector endpoint argument, spectral repair, and defect convergence.
- **RGT26 / #865**, `03cb3cb0b14922b839d0a6a64a59236377b1848d`, [positive tail-compression proof](https://github.com/GettysburgResearch/riemann/blob/03cb3cb0b14922b839d0a6a64a59236377b1848d/standalone/2026-09-12-positive-gamma-tail-compression/PROOF.md). Full proof previously read; source, remainder, convergence, and changed-source stress statements revisited. Its high-order Radau computation was not replayed.
- **MCF26 / #868**, `8ae3ea4855fd89882f4b5d782bbd72b721ebf47b`, [native scale-path and collision proof](https://github.com/GettysburgResearch/riemann/blob/8ae3ea4855fd89882f4b5d782bbd72b721ebf47b/standalone/2026-09-12-native-gamma-collision/PROOF.md). Full proof read. The proposed local double-zero certificate and two-zero tube are imported, not newly reconstructed here.
- **#869**, `6603f8b04f9a2d073123a328ac0298a498c93a96`, [gamma packet](https://github.com/GettysburgResearch/riemann/tree/6603f8b04f9a2d073123a328ac0298a498c93a96/standalone/2026-09-12-three-route-completion/gamma). The anchored production proof and native-step appendix were developed in the preceding session and cross-reviewed there. They are not treated as independently accepted mathematics merely because this review can explain them.
- **#875**, `be149104721ae7b65b624c100118edfd7b76b69b`, [native shape-flow manuscript](https://github.com/GettysburgResearch/riemann/blob/be149104721ae7b65b624c100118edfd7b76b69b/standalone/2026-09-12-astra-collision-chain-flow/GAMMA.md). Full GAMMA.md read, with special attention to its positive series, fixed-step exceptional disk and persistent-multiplicity formula. No whole Fourier contour or zero current was numerically evaluated.

The classical identification with xi is the Biane--Pitman--Yor/Jacobi identity, in the scaling explicitly retained by these sources. Complex Watson asymptotics, Hadamard factorization, Jensen, Rouche, Weierstrass preparation and local Puiseux parametrization are classical analytic inputs. No new literature-priority claim is made for these mechanisms or for third-order stochastic comparison. The argument supplied below proves the particular comparison and its constants directly.

The only new execution in this review is the small integer/Fraction program `gamma-controls.py` and its receipt `gamma-controls.json`. Its scope is stated in Section 8. It is not a formal proof or a native zero certificate.

## 2. The consumer is soundly separated from the difficult source geometry

Let G_n be independent Gamma(2,rate 1),

    X_N=sum_(n<=N)G_n/n^2, X=sum_(n>=1)G_n/n^2,
    tau_N=2sum_(n>N)n^-2, Y_N=X_N+tau_N.

If g_N is the density of Y_N, define

    h_N(t)=sqrt(g_N(pi e^(2t))g_N(pi e^(-2t))),
    F_N(z)=int h_N(t)e^(izt)dt / int h_N(t)dt.

The limit Phi is Xi(z)/Xi(0) under the classical arithmetic identity. The weighted defect is

    Delta(F)=(1/4)sum_(F(rho)=0) mult(rho)(Im rho)^2/|rho|^4.

For finite native stages this is equivalently a finite sum of b^2/|a+ib|^4 over first-quadrant nonreal quartets, with multiplicity. For the limit it can be infinite, but converges absolutely.

### 2.1 What the source convergence really uses

The globally Lipschitz density x e^(-x)1_(x>0) of the first gamma factor gives the direct estimate

    sup_x |g_N(x)-f(x)| <= sqrt(2sum_(n>N)n^-4).

This proof uses only coupling with the centered missing tail. It is independent of the faster formal differential expansion in #855. Complete exponential envelopes and a uniform positive normalizer then give locally uniform convergence of F_N and each fixed spectral derivative on the entire plane.

This is an important strength: the main defect consumer does not depend on accepting the most delicate claimed approximation rate.

### 2.2 Why convergence of the entire zero sum is justified

#862 derives a common zero-free origin disk and, for all stages, a complete inverse-square zero-tail bound

    sum_(|rho|>R) mult(rho)/|rho|^2
       <=26/R^2+4[log(4R)+1]/R, R>=1.

On a fixed disk with zero-free limiting boundary, Rouche controls the full multiplicities in small clusters. The defect weight is continuous away from the protected origin. Consequently finite weighted sums converge even when several approximant zeros approach a multiple real xi zero. The displayed uniform tail then permits removal of the disk. Thus

    Delta(F_N)->Delta(Phi),
    RH iff Delta(Phi)=0 iff Delta(F_N)->0.

No assumption that the approximant roots remain real near a multiple limit root enters this reasoning. The proof also does not need the fixed-stage eventual-real-zero theorem: that theorem gives a finite exceptional list and finite repair, while uniform zero-tail control already suffices for convergence of the weighted sums.

The Radau-compressed diagonal in #865 uses the same architecture. Its positive drift and finite gamma factors give the finite-stage endpoint structure; its common full-source envelopes, rather than a uniform exceptional radius, control the limit. Exponentially accurate approximation proves convergence to the unknown Delta(Phi), not that the limit is zero.

### 2.3 Constants and factorization checked

Even pairing of the order-at-most-one Hadamard product removes its residual linear exponential. A quartet contributes 4m b^2/|rho|^4 to the difference between the absolute inverse-square sum over positive-real-part representatives and the signed coefficient at the origin. Therefore

    Delta(F)=(1/2)int_0^infinity J_F(r)dr/r^3 - mu_2/8,
    J_F(r)=(1/(2pi))int_0^(2pi)log|F(re^(i theta))|dtheta.

The factors 1/2 and 1/8 are correct. The finite radial replacement changes a quartet factor by 4b^2 z^2/|rho|^4 and yields the uniform compact-error bound in #862. This proves the analytic cost of removing exceptions. It does not estimate their native cost to begin with.

I found no circular RH premise or missing multiplicity term in this consumer. Its deliberately huge constants may prevent practical direct computation but do not invalidate the stated implication.

## 3. The three paths must not be conflated

Write B=(N+1)^2. Each row below is a different path.

| Path | Positive-variable source | What its regularity currently supports |
|---|---|---|
| Native scale, #868 | X_N+tau_N-2v/B+Gamma(2,scale v/B), 0<=v<=1 | Exact martingale transitions; a certified local annihilation at N=5; uniform exceptional disk only on compact substeps v>=v0>0 in that manuscript. |
| Native shape, #875 | X_N+tau_N-u/B+Gamma(u,rate B), 0<=u<=2 | Fixed rate and continuously varying endpoint exponent; proposed common exceptional disk for the entire fixed step, including u=0. |
| Bessel anchor, #869 | Explicit positive convolution from Gamma(4,rate 4) to the desired finite native source | Known zero-defect starting value and a regularized integrated Jensen balance; the anchor path is not a native mean-preserving integer update. |

All three have legitimate roles. They do not have the same intermediate zero trajectories. The local scale-path collision cannot simply be relabelled as a shape-path collision.

### 3.1 The genuine scale-endpoint issue and its existing repair

For every v>0 the native scale density has boundary exponent 2N+1; at v=0 that exponent is 2N-1. The leading coefficient also degenerates as the incoming scale tends to zero. Therefore taking a minimum over v in [0,1] in a fixed-v Watson estimate is unjustified. #868 correctly restricts its common exceptional disk to v>=v0>0.

The #869 appendix handles the endpoint without such a disk. Its fixed-anchor Fisher argument gives an integrable whole-step derivative of the reciprocal kernel. A stronger Gamma(6,rate 9) anchor for N>=3 gives, with d=tau_(N+1), T=(1/2)log(pi/d),

    int e^(R|t|)|partial_v h_v(t)|dt
       <100 e^(RT) v/[B^2 sqrt(d)].

The constants retain their fixed-stage dependence. This is enough for absolute continuity and the regularized Jensen balance through v=0. It is not a bound on the sign of the zero current, nor an N-uniform finite exceptional radius.

### 3.2 Audit of #875's positive series and score

The new shape path has nu=2N+u and w=x-b_u, b_u=tau_N-u/B. Its density is

    g_u(x)=(N!)^4 B^u w^(nu-1)e^(-Bw)/Gamma(nu)
             *sum_(k>=0) h_k w^k/(nu)_k.

The h_k are the complete homogeneous coefficients of the 2N nonnegative rate differences B-n^2. Expanding the exact Laplace product about s+B proves the formula with positive coefficients. The bound h_k/(nu)_k<=(B-1)^k/k! pays the entire series. In particular h_k is independent of u, which is essential when differentiating.

At fixed x, partial_u w=1/B. Differentiating the density gives the score stated in #875, including both the -1 from e^(-Bw) and the harmonic derivative of (nu)_k. Its constant log B-psi(nu)-1 cancels after reciprocal normalization. This cancellation is valid; it is not a replacement of an unsigned score by a positive one.

The normalized reciprocal score is even and centered. Its transform derivative is a complex-bilinear covariance, and can have either sign or phase. Positive series coefficients make the score computable; they do not make the covariance nonnegative.

### 3.3 Completing the justification for a common fixed-step disk

I found no counterexample to #875's G1, and its mechanism differs materially from the invalid scale-endpoint uniformization. Here is a more explicit version of the compactness argument that a final proof should retain.

Put t=T_u v, with v in [-1,1]. Both b_u and T_u stay strictly positive at a fixed N. Factor the endpoint zeros from

    w_+(u,v)w_-(u,v)
       =pi^2+b_u^2-2pi b_u cosh(2T_u v).

The quotient by 1-v^2 is jointly analytic and strictly positive on the compact real parameter rectangle, including its removable values at v=+-1. The positive series S_(2N+u)(w) is also jointly analytic and nonzero near that compact set: on the real nonnegative arguments it is at least one, and its derivative series have common exponential majorants. Small complex neighborhoods in u preserve the nonvanishing Pochhammer denominators. Compactness then supplies common zero-free complex neighborhoods and fixed logarithm/square-root branches.

Thus the pulled-back kernel has the form

    h_u(T_u v)=(1-v^2)^(N+(u-1)/2) Q(u,v),

where Q is jointly analytic and positive on the real compact rectangle. Its endpoint amplitudes have positive minima; its complex derivative bounds have finite maxima. The exponent varies in the compact interval [N-1/2,N+1/2], rather than jumping at u=0.

Apply the TWO-sector endpoint proof from #862 with these uniform data. In the near-horizontal sector, both endpoint terms and their complete remainder are uniform, and the late cosine roots have uniformly separated real centers. Rouche on O_N(1/|z|) disks gives one root counted with multiplicity, hence a real simple root. In the near-vertical sector a single endpoint dominates uniformly. This yields one finite exceptional radius for the entire fixed shape step.

This proves existence at fixed N if the cited endpoint argument is accepted. It supplies no useful numerical radius and no radius uniform in N. Describing it as merely a consequence of real-axis asymptotics would still be wrong; both sectors are needed.

### 3.4 Every multiplicity and collision in the current

The same fixed-domain integral gives a joint holomorphic family F(u,z) on a complex neighborhood of the closed real parameter interval. The normalizer is positive there on the real interval and nonzero in a smaller complex neighborhood. The common exceptional disk and common zero-free origin disk confine every nonzero defect contribution to a compact annulus.

Local Weierstrass polynomials have convergent Puiseux root parametrizations after finite ramification. Persistent repeated factors must first be separated; an identically zero discriminant is not evidence for isolated collisions. After that separation, the remaining branch values are isolated, and a finite cover of the compact parameter interval gives finitely many local root families. A branch has coordinate derivative bounded locally by a power |u-u0|^(1/m-1), which is integrable. At a real collision its squared imaginary part is even better behaved, of order at least |u-u0|^(2/m).

The smooth weight (Im rho)^2/|rho|^4 therefore gives an absolutely continuous total defect. One may enlarge the exceptional radius slightly; every root near its artificial boundary is real throughout, and contributes zero. This avoids losing a nonreal root at an observation boundary.

At a persistently m-fold root, differentiating F^(m-1)(rho(u),u)=0 gives exactly

    rho'=-partial_u partial_z^(m-1)F/partial_z^m F.

The factor m is already accounted for by the derivatives; no further 1/m belongs here. The current identity

    d[y^2/|rho|^4]/du
       =2y/|rho|^2 * Im(rho'/rho^2)

also has the correct factors. Integrating its multiplicity-weighted sum is consistent with #869's zero-safe Jensen balance. No collision atom is missing. This is a defensible finite-step current theorem, subject to the analytic details just spelled out, not a dissipativity theorem.

## 4. New deduction: a sharp third-order comparison between the two native paths

This gives a precise replacement for the tempting claim that shape and scale interpolation are equivalent. Fix B>0 and 0<=v<=1. Compare the following sources with the same independent base X_N:

    Y_scale=X_N+tau_N-2v/B+Gamma(2,scale v/B),
    Y_shape=X_N+tau_N-2v^2/B+Gamma(2v^2,rate B).

The shape parameter u=2v^2 is chosen to match variance, not to match the original path parameter. Both means coincide and both added variances equal 2v^2/B^2. Their third-cumulant difference is

    kappa_3(Y_shape)-kappa_3(Y_scale)
       =4v^2(1-v)/B^3.                                  (G1)

For every real C^3 test phi with bounded third derivative and phi'''>=0,

    E phi(Y_scale)<=E phi(Y_shape).                      (G2)

More strongly, for every real OR complex such test,

    |E phi(Y_shape)-E phi(Y_scale)|
       <=[2v^2(1-v)/(3B^3)] ||phi'''||_infinity
       <=[8/(81B^3)] ||phi'''||_infinity.                (G3)

The first constant is sharp for this test norm, since cubic tests attain equality. The test may have cubic growth; the gamma laws have all needed moments. Smooth compactly supported tests also suffice for the derivation and standard cutoff passage.

### Proof: the full signed generator has a positive third-order kernel

The centered infinitely divisible increments have Levy measures

    nu_scale(dy)=2 e^(-By/v)dy/y,
    nu_shape(dy)=2v^2 e^(-By)dy/y,

with the obvious limiting interpretation at v=0. Let mu=nu_shape-nu_scale. Its second moment is zero. Both endpoint laws can be joined by the positive marginal interpolation

    Y_lambda=X_N+tau_N-2[(1-lambda)v+lambda v^2]/B
       +Gamma(2(1-lambda),rate B/v)
       +Gamma(2lambda v^2,rate B), 0<=lambda<=1.

All factors are independent. For the native B=(N+1)^2 its deterministic drift remains at least tau_(N+1)>0. The variance is constant along lambda. This comparison path is NOT claimed to be a martingale: a nontrivial square-integrable martingale cannot have constant variance.

Differentiating its exact logarithmic Laplace transform gives the signed generator

    A phi(x)=int [phi(x+y)-phi(x)-y phi'(x)]mu(dy).

Since int y^2 mu(dy)=0, subtract y^2 phi''(x)/2 as well. Taylor's integral remainder, with the full finite third absolute moment of mu, yields

    A phi(x)=int_0^infinity K_v(t)phi'''(x+t)dt,
    K_v(t)=(1/2)int_t^infinity (y-t)^2 mu(dy).         (G4)

There is no omitted small-jump or large-jump part. For 0<v<1 put

    Psi(z)=int_z^infinity ((r-z)^2/r)e^(-r)dr.

It is strictly decreasing on [0,infinity), with Psi(0)=1. Substitution in (G4) gives the explicit complete kernel

    K_v(t)=(v^2/B^2)[Psi(Bt)-Psi(Bt/v)]>=0.           (G5)

It is strictly positive for t>0 and 0<v<1. An equivalent elementary explanation is that y^2 nu_shape and y^2 nu_scale have equal total mass; after normalization they are Gamma(2,rate B) and Gamma(2,rate B/v), and the former is stochastically larger. The increasing test (1-t/y)_+^2 gives the same inequality.

The exact total mass is

    int_0^infinity K_v(t)dt
       =(1/6)int y^3 mu(dy)=2v^2(1-v)/(3B^3).        (G6)

The usual compensated-generator differentiation can be justified here by truncating the gamma Levy measures, retaining both mean drifts, applying Taylor's third-order remainder, and then using int y^3|mu|(dy)<infinity. It gives the exact identity

    E phi(Y_shape)-E phi(Y_scale)
       =int_0^1 int_0^infinity K_v(t)
                              E phi'''(Y_lambda+t)dt dlambda. (G7)

Equations (G2)--(G3) follow. The maximum v^2(1-v)=4/27 occurs at v=2/3. For phi(x)=x^3 the right side is six times (G6), proving (G1) and sharpness. The endpoint cases v=0,1 have identical laws and zero kernel. QED.

### What this comparison buys

It proves that the paths first differ at a fully priced third-order level after matching mean and variance. It also gives real Mellin inequalities: for example x^p has positive third derivative when 0<p<1, so the shape source has the larger such moment. Appropriate inverse-moment bounds justify those unbounded-at-zero derivatives by cutoff; the native sources have positive lower support at a fixed step.

It does NOT order the reciprocal Fourier zeros. Complex powers and Fourier tests have no positive third derivative. Moreover the finite reciprocal projection is nonlinear and its normalizer changes. Even small bounded-test discrepancies need not preserve the orientation of a nearly colliding zero. The local #868 collision is therefore not transported to #875 by (G3).

The lemma extends to other positive base laws; its positivity cannot by itself characterize the integer-square arithmetic source. Its useful role is to isolate an actual path difference and provide controlled comparison or preconditioning for a future native computation.

## 5. Score orthogonality is exact, but it supplies energy rather than direction

Let ell_u=q_u/g_u be the physical score of the shape flow, and let m=E Y_u=pi^2/3. Differentiating the exact normalized moments gives

    E ell_u=0,
    E[(Y_u-m)ell_u]=0,
    E[(Y_u-m)^2 ell_u]=1/B^2,
    E[(Y_u-m)^3 ell_u]=2/B^3.                       (G8)

For the scale parameter v the last two right sides are 4v/B^2 and 12v^2/B^3. These identities retain the centering drift and are useful exact checks on any numerical score implementation.

For the shape flow, let kappa_j denote the physical cumulants. Project the centered quadratic test off constants and the centered linear test:

    Q=(Y-m)^2-kappa_2-(kappa_3/kappa_2)(Y-m).

Then E(Q ell)=1/B^2 and

    E Q^2=kappa_4+2kappa_2^2-kappa_3^2/kappa_2.

Cauchy--Schwarz gives the nonzero score-energy lower bound

    int q_u^2/g_u
       >= B^-4/[kappa_4+2kappa_2^2-kappa_3^2/kappa_2]. (G9)

For the actual finite gamma sums all these cumulants are explicit positive rational expressions in u and the rates. The denominator is positive because a nondegenerate continuous law cannot be supported on the roots of this quadratic. This is a source Fisher-information bound, not a spectral dissipation bound.

After reciprocal projection the centered score is a(t)=partial_u log p_u(t). Its Fisher information is E_p a^2>=0, while

    partial_u F_u(z)=E_p[e^(izt)a(t)],
    partial_u mu_2=Cov_p(t^2,a).

The physical orthogonality in (G8) is not orthogonality under the different measure p_u. Even under p_u, Fisher information bounds absolute covariance sizes; it does not fix their signs. Away from zeros, differentiating log F produces the bilinear term -(F'/F)^2, not the nonnegative |F'/F|^2. At zeros that logarithmic derivative is not a legitimate globally integrable substitute for the regularized Jensen current.

### An explicit positive-density fold with fixed variance

The following exact control rules out a variance/Fisher-only inference. It is a changed family, NOT a native gamma counterexample.

Take the even triangular probability density p(t)=(1-|t|)_+ on [-1,1]. Its entire characteristic function is

    F_0(z)=2(1-cos z)/z^2,

with the value one at zero. At omega=2pi it has a double real zero and F_0''(omega)=1/(2pi^2)>0. Define

    A(t)=cos(2pi t)+(90t^2-15)/(7pi^2),
    p_epsilon(t)=p(t)[1+epsilon A(t)], |epsilon|<=1/4.

Using E t^2=1/6, E t^4=1/15, E cos(2pi t)=0 and E[t^2 cos(2pi t)]=-1/(2pi^2), one gets EXACTLY

    E A=0, E[t^2 A]=0.

Thus every p_epsilon is normalized and has the same variance. Since |A|<3, these are positive densities for the displayed parameters. Yet

    partial_epsilon F_epsilon(omega)|_0
       =R:=1/2-45/(7pi^4)>0.

Indeed E cos^2(2pi t)=1/2. With z=omega+sqrt(epsilon)w,

    epsilon^-1 F_epsilon(z) -> w^2/(4pi^2)+R.

Rouche near the two simple roots of this limiting quadratic gives a conjugate nonreal pair for every sufficiently small positive epsilon, while the corresponding negative-epsilon perturbation gives two simple real roots. The reflected pair occurs near -omega. The local quartet defect for epsilon>0 is

    R epsilon/(4pi^2)+O(epsilon^(3/2)).               (G10)

Its normalized score has finite nonnegative Fisher information in both directions. Normalization, symmetry, fixed variance and score energy therefore do not determine the fold orientation.

One can preserve a positive physical source's mean as well. Project cos(2pi t) in L2(p) off the finite-dimensional span of 1,t^2,cosh(2t),cosh(4t), and call the nonzero residual A_*. The residual is bounded and E[cos(2pi t)A_*]=||A_*||^2>0. For small |epsilon|, p(1+epsilon A_*) is positive and keeps all four listed moments fixed. Define on [pi e^-2,pi e^2]

    g_epsilon(x)=C p_epsilon((1/2)log(x/pi)),
    C=[2pi E_p cosh(2t)]^-1.

This is a normalized positive physical density, its mean pi E_p cosh(4t)/E_p cosh(2t) is fixed, and its normalized reciprocal projection is exactly p_epsilon. The same fold argument applies. The residual is nonzero because a cosine of nonzero real frequency is not in the stated finite span on an interval. This is not a gamma law or an asserted martingale coupling; it specifically rules out extracting the native sign from positivity and finitely many moment/energy constraints alone.

## 6. What still requires genuinely arithmetic input

All finite-stage currents integrate to the same endpoint difference Delta_(N+1)-Delta_N, regardless of the admissible connecting path. A known zero-defect anchor removes the unknown starting constant, and using one common spectral radius makes endpoint tail errors telescope. Those are real improvements in formulation and validation, but neither says the total production tends to zero.

#865's changed-source stress example is an additional warning. Positive gamma components, positive tail compression, rapid full-source convergence, and the broad derivative/current machinery survive a changed low rate, while its limiting transform has a nonreal zero. The shape-series construction and physical score identities similarly extend well beyond the exact integer-square source. Any closing argument must use information absent from that larger class, such as the literal square-rate/Jacobi reciprocity in a sign-sensitive way.

The total physical variance added after stage N is O(N^-3). Therefore a mere summable bound on absolute root displacement, or even motion in a favorable direction, can be consistent with a positive limiting off-line height. A useful contraction must have non-summable effective strength, or some different global cancellation mechanism that forces the residual to vanish.

An exact sufficient target is the cofinal block inequality

    Delta_(N_(j+1))<=(1-a_j)Delta_(N_j)+b_j,
    0<a_j<=1, sum a_j=infinity, b_j/a_j->0.

Nothing audited or derived here proves this inequality. Its remaining difficulty is not a routine missing normalization, endpoint term, or multiplicity convention.

## 7. A concrete next pass that would test the missing mechanism

The most informative bounded mathematical/computational task is a COMPLETE native shape step at one small N: compute its positive-series score and transformed current while simultaneously supplying a certified exterior radius or an independent complete Jensen-tail allowance. Include every exceptional cluster and every collision. The current fixed-step analyticity permits this in principle; the manuscript presently supplies neither a numerical common radius nor a total current sign.

A full negative step would establish an actual dissipation event, but not a stage-uniform contraction. A positive step would immediately refute monotonicity of Delta_N and redirect the search toward block budgets. Either outcome would distinguish a real native mechanism from a favorable local fold. The #868 tube alone does not decide that question.

The new variance-matched comparison provides an independent consistency check for such a computation: score moment identities, endpoint laws and third-order differences must match (G1), (G6), (G8). It does not justify transferring individual zero labels between the two paths. Any attempted energy argument should first survive the positive-density control (G10), then state the additional square-rate identity that defeats that control.

## 8. Validation and final audit disposition

`gamma-controls.py` uses Python integers and Fractions only. It reconstructs 21 variance-matched shape/scale panels, checks the exact relation between the third-cumulant gap and the complete Peano mass, checks the sharp mass ceiling, verifies the triangular-score normalization and variance equations, and checks four rational native physical-score energy panels. The Fourier identities used by the triangular control are analytically derived in this note; the code does not numerically integrate them.

Executed commands:

```text
python -I -S -B gamma-controls.py --write
python -I -S -B gamma-controls.py
python -I -S -B -O gamma-controls.py
```

Normal and optimized runs use the same arithmetic implementation. They do not constitute independent analytic review. No native zero location, all-zero census, local #868 contraction certificate, new directed Fourier integral, high-order Radau solve, repository build, or remote CI run is represented by these controls.

The root agent also reviewed the signed-generator/Peano argument, sharp constant and positive-density fold constructions in Sections 4–5. No defect was identified in that source-scope review; it is a second analytic review within the same session, not external acceptance or formal verification.

The audit found no fatal defect in the source-to-defect consumer, the properly scoped scale endpoint repair, or the fixed-step shape-current mechanism. It did identify the specific analytic details required to justify the latest uniformization and persistent-multiplicity assertions. The two new deductions supply a sharp physical comparison and a concrete obstruction to a moment/Fisher-only spectral sign. **The native cumulative signed-production estimate remains open.**
