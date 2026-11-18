# Critical strip regularity gives the signed explicit formula

18 November 2026. The director reconstructed the contour and Fourier arguments, inspected the controlling Titchmarsh source displays and Bombieri–Lagarias condition (A), and compared the independent constructions and adversarial reviews. **The ordinary inclusive symmetric height formula holds at the critical strip H^{1/2} norm**, with the stated local regularity at one. In particular the earlier smooth p=3 absolute-divergence example has a convergent signed symmetric sum. This resolves a question left open in the dated Round 15 adjudicated ledger. It does not establish a necessary condition or publication novelty.

Proof and review chain: [first p>1 signed construction](weighted146_signed_endpoint_research.md), [independent p>1 reconstruction and cusp](uniform147_signed_endpoint_adversarial.md), [third p>1 adjudication](geometry149_signed_endpoint_third.md), [critical contour construction](weighted152_signed_p1_campaign.md), [independent critical contour review](uniform153_contour_signed_critical_review.md), and [third contour/cusp review](geometry154_critical_contour_and_cusp_adjudication.md). These are scoped mathematical audits, not a whole-work promotion of any source.

## Statement and distinction from absolute sampling

Let f be continuous on (0,infinity), with f(x)=O(x^delta) at zero and O(x^(-1-delta)) at infinity for some delta>0. Put

```text
F(u)=exp(u/2)f(exp u),
h(s)=integral_0^infinity f(x)x^(s-1) dx,
N_0²=integral_(-epsilon)^(1+epsilon) integral_R
          sqrt(1+t²) abs(h(beta+it))² dt d beta,
```

where 0<epsilon<delta. Assume N_0 finite and F belongs to H^1 on a neighborhood of u=0. A C^1 test near x=1 suffices for the latter condition. Then, unconditionally,

```text
lim_(T→infinity) sum_(abs(Im rho)≤T) h(rho)
 =h(0)+h(1)−sum_(n≥1) Lambda(n)[f(n)+f(1/n)/n]
  −(log pi+EulerGamma)f(1)
  −integral_1^infinity
    [f(x)+f(1/x)/x−2f(1)/x²] x/(x²−1) dx.
```

Nontrivial zeta zeros are counted with multiplicity. No restriction to a subsequence of heights, smoothing of the zero sum, RH, or simplicity is present. The arithmetic terms and the compensated integral have ordinary absolute convergence. The spectral sum need not converge absolutely. Every logarithmic weight w_p(t)=sqrt(1+t²)log^p(e+abs(t)) with p>=0 dominates the stated weight and therefore also suffices under these hypotheses.

There is also a formulation with the manuscript's literal (A) in place of continuity and local H^1. That condition gives finite one-sided limits of both f and f′ at finitely many exceptional interior points and gives f its midpoint value. The critical norm excludes every actual value jump, and the bounded one-sided derivatives then imply local H^1. The proof of this implication is given below. Value decay alone, without the norm, still admits the earlier smooth raw-height counterexample.

## Endpoint sharp Fourier inversion

We may shrink epsilon below 1/2. Holomorphic disk mean value on an inner strip gives both

```text
abs(h(beta+it)) <= C N_0 (1+t²)^(-1/4)
```

and uniform vertical L^2(sqrt(1+t²)dt) control there. The vertical weighted tails tend to zero uniformly in beta: integrate the disk inequality over abs(t)>R, then bound it by the area tail above R minus a fixed radius. This also supplies derivative traces when needed.

For F_beta(u)=exp(beta u)f(exp u), the Fourier transform with positive exponent is h(beta+it). These physical functions are continuous, exponentially decaying, and uniformly equicontinuous as beta varies on a compact inner strip. Define

```text
I_(T,beta)(u)=(1/(2pi)) integral_(-T)^T h(beta+it)exp(−itu) dt.
```

It converges uniformly in u and beta to F_beta. To see the critical step, compare the sharp multiplier with exp(-t²/T²). Their difference m_T satisfies

```text
integral_R abs(m_T(t))²/sqrt(1+t²) dt
 <= integral_R abs(1_(abs(v)≤1)−exp(−v²))²/abs(v) dv < infinity,
```

uniformly in T. Near zero the final integrand is O(abs(v)^3); at infinity it decays rapidly. On any fixed frequency interval the multiplier tends uniformly to zero. Above a large fixed frequency, Cauchy–Schwarz uses this bounded kernel norm and the small vertical weighted tail. The resulting difference tends to zero uniformly in the physical point and line. Gaussian inversion converges uniformly by the physical approximate identity. Thus **the sharp inversion itself** converges; the Gaussian is only a comparison device. Using Cauchy–Schwarz with the full inverse weight, without this difference multiplier, would be invalid at the endpoint.

A shorter classical Tauberian variant uses the Fejér triangular multiplier (1-abs(t)/T)_+. Its difference from the sharp multiplier is abs(t)/T on abs(t)<=T and zero elsewhere. The squared inverse-weight norm is at most 1, by sqrt(1+t²)>=abs(t). The same fixed-low-frequency and weighted-tail split proves uniform sharp-minus-Fejér convergence, while the Fejér physical kernel is an approximate identity. This is another proof of the endpoint inversion lemma, using an established summability device. The [primary-source provenance review](analytic156_signed_critical_provenance.md) also identifies Weil's earlier folded contour and height-cutoff framework; his final test hypotheses add derivative decay. No novelty of the contour method or this Tauberian mechanism is asserted.

## A folded contour keeps the prime side summable

Take a=1+epsilon/2 and vertical lines a and 1-a. The entire completed xi function has precisely the nontrivial zeros, with their multiplicities. A good height lies in every sufficiently high interval [T,T+1]: remove intervals of radius c/log T about the O(log T) nearby ordinates, choosing the fixed c sufficiently small. On the remaining height, the local partial fraction formula gives xi′/xi=O(log² T) across the horizontal segment. The area trace makes both horizontal integrals O(N_0 log²T/sqrt(T)), which tends to zero.

The director inspected Titchmarsh, second edition, Theorem 9.6(A), printed p.217, which gives the uniform local logarithmic derivative for -1<=Re s<=2, and the source convention for the count at ordinates. The pinned scan SHA-256 is `ee495ba7e6b7af4722317baa79087881c16f648cb8af72843eb869c7497a03d0`. This is a scoped check of the book's theorem exposition, not a whole book or original proof audit. [Source and exact review locators](uniform153_contour_signed_critical_review.md).

Counterclockwise residue calculus and xi′/xi(1-s)=-xi′/xi(s) give, at good heights,

```text
sum_(abs(Im rho)≤T) h(rho)
 =(1/(2pi)) integral_(-T)^T [h(a+it)+h(1−a−it)]
                               (xi′/xi)(a+it) dt +o(1).
```

The reflected term has a **plus** sign. Any target height differs from a good height by at most one; the intervening zero mass, including an exact endpoint atom, is O(N_0 logT/sqrt(T)). This restores every ordinary inclusive cutoff.

On a>1, the absolutely convergent series for zeta′/zeta can be inserted in every finite integral. The two resulting sharp Fourier inverses have arguments (a,log n) and (1-a,-log n). Uniform inversion permits passage through sum Lambda(n)n^(-a). Their physical values are n^a f(n) and n^(a-1)f(1/n). The prime term is therefore exactly the one in the statement. This argument never assumes absolute Fourier integrability of h on that line. Continuity of the gamma functional alone will be in norm plus local H^1; convergence of the prime terms in the later approximation also uses the uniform physical value envelope, rather than an unstated global point-evaluation bound from H^{1/2}.

## The archimedean singularity is a separate local condition

Write xi′/xi=zeta′/zeta+Q on the right line, where

```text
Q(s)=1/s+1/(s−1)−(log pi)/2+(1/2)(Gamma′/Gamma)(s/2).
```

For large positive or negative t,

```text
Q(a+it)=(1/2)log(abs(t)/(2pi))+(i pi/4)sgn(t)+O_a(1/abs(t)).
```

The sign term cannot be absorbed into an absolute inverse-weight estimate. Treat its two constant half-axis values separately. The O(1/abs(t)) remainder is absolutely integrable against the vertical tests by weighted Cauchy–Schwarz.

Choose a smooth compact cutoff chi equal to one near zero and supported where F is H^1. The transform of chi F_beta is absolutely integrable with the extra factor 1+log(2+abs(t)). For the exterior part set m(u)=(1-chi(u))/(iu), smoothly extended through zero, and G_beta=Fourier(m F_beta). Then G_beta′ is the transform of (1-chi)F_beta. The multiplier m and all its derivatives lie in L^2, so its Fourier transform has every fixed polynomially weighted L^1 bound. Weight moderation gives G_beta and G_beta′ in the same weighted L^2 space. Unit-interval Sobolev estimates imply G_beta(t)=O(N_0(1+t²)^(-1/4)).

Integrate G_beta′ against log(abs(t)) on each half-axis. The boundary G_beta(t)log(abs(t)) vanishes, and the remaining G_beta(t)/t integral is absolute. The constant half-axis terms similarly use G_beta(t)→0. This proves convergence and continuity of the Q functional in N_0 plus the fixed local H^1 norm.

Finally cut off F in u and mollify with smooth compact kernels. These operations converge in the full weighted strip norm and in a smaller fixed local H^1 neighborhood. Exponential tilts of the mollifiers are uniformly bounded on the strip. The approximants preserve a common exponential value envelope and converge pointwise, so h(0), h(1) and the prime sum pass by dominated convergence. Uniform local H^1 gives a 1/2-Hölder majorant at one for the compensated archimedean singularity. Its tail is covered by the value envelope. Apply the classical smooth compact formula and pass to the limit using the Q-contour convergence just proved. This identifies the exact ordinary formula, without citing the overly broad noncompact manuscript statement.

## Literal local hypotheses and the independent Selberg route

The area-to-line trace and Plancherel give central F in H^{1/2}. A first-kind value jump would force its Gagliardo seminorm to dominate a positive constant times integral_0^b integral_0^b (u+v)^(-2) du dv, which is infinite. Thus genuine jumps are excluded. The manuscript's midpoint values select the continuous representative, and finite one-sided limits of f′ give bounded local derivatives on either side of every exceptional point. Continuity then implies local H^1. This argument replaces the p>1 proof using absolute Fourier integrability, which is unavailable at p=0.

The independent Selberg proof remains useful: at p>1 it establishes separate convergence on each half-height axis, not just the symmetric statement above. The director inspected the uniform density bound at Titchmarsh Theorem 9.19(C), printed p.237, and Selberg's second moment of S(T), §9.25 (9.25.1), p.245. The density bound yields sum_(T≤gamma≤2T) abs(beta-1/2)²=O(T/logT). Cellwise Cauchy–Schwarz makes the off-line projection correction absolutely summable for p>1. The argument-count remainder gives another convergent integral, using integral_T^(2T) abs(S(t))²dt=O(T loglogT). A local-origin split handles the smooth logarithmic density. Its tail bounds and its stronger half-axis conclusion are retained in the earlier reviews. Failure of that dyadic majorant at p=1 was a limitation of the proof, not an endpoint counterexample; the contour proof removes it for the symmetric formula.

## A counterexample when the local-origin condition is omitted

There is a different continuous real compactly supported f, smooth away from x=1, with finite p=3 norm but signed raw sum tending to positive infinity. It lies **outside** the literal manuscript class because its derivative lacks the required finite one-sided behavior. This is not another author-error finding.

Take a positive smooth even frequency profile k(t) equal to 1/[abs(t)log²(abs(t))loglog(abs(t))] at high frequency. It is L^1 and L^2(w_3), but integral k(t)log(abs(t))dt diverges. Let K be its inverse transform. Multiply K in physical coordinates by D=phi*reflected(phi), for a real smooth compact bump with nonzero integral, and put F=DK. The central transform H is the convolution of k with the nonnegative profile abs(Fourier(phi))², up to the Fourier constant; hence H>=0 and H(t)>=c k(t) at high frequency. All tilted transforms have finite weighted norm by uniform Schwartz convolution. The function is continuous, compactly supported and smooth off zero in u.

The Selberg projection and S-remainder pieces converge at p=3, while the smooth logarithmic density integral diverges positively. This proves signed divergence. An independent folded-contour calculation gives the same conclusion from the middle-line digamma kernel. The local archimedean obstruction matches it: Fourier inversion and Tonelli give integral_0^b [F(0)-F(u)]du/u=infinity because integral_0^(bt)(1-cos v)dv/v=log t+O_b(1). The compensated gamma term therefore diverges with the corresponding sign. Local H^1 cannot hold.

The distinctions are now explicit: source value and local conditions alone allow smooth raw-height failure; the critical strip norm plus those local conditions restores the signed symmetric formula; p>3 gives universal absolute sampling; and a smooth p=3 test can have signed convergence with absolute divergence. The sharp necessary boundary below the critical norm and weaker possible local-origin conditions remain unresolved here. Luecking's embedding theorem explains the ambient absolute-sampling threshold, not this signed convergence conclusion. [Bounded predecessor comparison](prime146_mellin_trace_prior_art.md). No field-priority claim follows.
