# Hughes–Rudnick 2002: whole-note audit and exact averaging-weight repair

18 November 2026. The director read all four journal pages 667–670 of Chris Hughes and Zeév Rudnick, *Linear statistics for zeros of Riemann's zeta function*, C. R. Math. 335(8), DOI `10.1016/S1631-073X(02)02541-4`, and the complete independent advocate and skeptic reconstructions and repair review. The controlling Numdam journal PDF SHA-256 is `b4572e5bdbf3cf7e891a4128aeb3bb56d151f2b16d23f9e63a94b1a2d2c09139`. Both reviewers additionally read the nine-page arXiv:math/0208220v1, SHA-256 `2225d590d97abd13a4b973bd3d936a7b07fb45a3296739438f8ce57f657cdebd`. The whole-work promotion is pinned to `2002 journal typeset version, C. R. Math. 335(8), 667–670`.

The intended finite Gaussian moment theorem is reconstructed, including an explicit repair of the literally printed weight class and an additive replacement for a proof shortcut. The original oscillatory prime theorem works with the printed weight assumptions. There is no RH premise and no proof of a full Gaussian law for a fixed test. These boundaries matter when comparing it to the derivative-weighted zero-tail campaigns.

## Statistic, literal hypotheses and repaired theorem

Write nontrivial zeros as rho=1/2+i gamma, with multiplicity; gamma may be complex. For real even f with Fourier transform `fhat(v)=integral f(x)exp(−2πixv)dx` in C_c^infinity, define

```text
N_f(tau)=sum_gamma f[(logT)(gamma−tau)/(2π)],
<W>_(T,H)=integral_R W(T+Hu)w(u)du,
H=T^a, 0<a≤1.
```

The entire extension of f is required when RH is not assumed. Rapid decay on horizontal strips and the standard zero count give normal convergence at fixed T; critical-line reflection makes the statistic real. The indicator-counting interpretation in the introduction is conditional on RH and is only motivational.

The printed weight class is `w≥0`, integral w=1 and compact support of what. No Schwartz or logarithmic-tail condition is specified there or in the longer v1. Fix m≥1 and a strict radius sigma with `supp fhat⊂[−sigma,sigma]`, `m sigma/2<a`. The exact sufficient repair for the first m Gaussian moments is

```text
integral f=0  OR  integral_R w(u)log^m(2+|u|)du<infinity.
```

Under that alternative, all raw moments through m tend to those of mean `I=integral f` and variance

```text
V=integral_R min(|v|,1) fhat(v)^2 dv.
```

For m≥2 the support lies strictly inside (−1,1), so V=2 integral_0^infinity v fhat(v)^2dv. For m=1 the assertion concerns the mean only. When I≠0 the added logarithmic moment is also necessary for the mth **absolute** moment to be finite at any fixed T>1 and H>0. When I=0 no extra weight tail is needed. In particular the usual nonnegative Schwartz bandlimited weights are valid, as are many slower-decaying weights with all logarithmic moments. A fixed moment window does not establish convergence in law to a Gaussian.

## Explicit witness to the literal omission

Choose a nonzero real even Schwartz function q with smooth compact Fourier transform, and set `b=q²/integral q²`. This b is nonnegative, Schwartz, bandlimited and has mass one. Define a single fixed weight

```text
w(u)=sum_(j≥1) 2^(−j) b(u−exp(4^j)).
```

The sum converges in L1, is nonnegative, has mass one and has compact Fourier support. In fact it is smooth, so merely adding smoothness would not fix the problem. A fixed fraction of each bump's mass lies a bounded distance from its center; Tonelli gives `integral w log(2+|u|)=infinity`. One may symmetrize the weight if desired. It is independent of T.

Take real even f with fhat smooth, supported in a sufficiently small strict Fourier window, and I>0. Such tests can also be obtained as bandlimited Schwartz squares. The actual explicit formula in journal (2)–(4), valid without RH, gives at every fixed T

```text
N_f(tau)= [I/logT]log(1+|tau|)+O_(f,T)(1),   tau real.
```

The prime sum is finite and bounded in tau; the polar evaluations of the entire f are bounded on the fixed horizontal lines. For the gamma term use Omega(r)=log(1+|r|)+O(1) and

```text
|log(1+|tau+c x|)−log(1+|tau|)| ≤ log(1+|c x|).
```

The latter integrates against |f|, proving the stated bounded remainder directly from the primary formula. Substitution tau=T+Hu shows `<N_f>=+infinity` for this allowed weight at every fixed T>1. Thus the literal first-moment assertion fails for the printed weight class. For I≠0 the same asymptotic proves the exact fixed-T absolute-moment equivalence with integral w log^m finite. The statement that tau is near T in probability when a<1 does not provide the missing uniform integrability.

This is a version-specific missing-hypothesis finding about the literally defined average. It is not a rejection of the valid Schwartz theorem, prime-product method, ordinary CUE comparison, or other papers using finite height intervals.

## Reconstruction of the valid argument

Lemma 2.1 is the smooth explicit formula. Integrate the completed logarithmic derivative against the entire test, use pole residues at 0 and 1, reflect by the functional equation, and substitute the absolutely convergent Mangoldt series. Rapid strip decay and good heights remove horizontal edges. With the paper's Fourier convention this gives exactly its `1/(2π)` gamma integral, two polar terms and prime coefficients. The specific transformed test has `g(u)=exp(−i tau u)fhat(u/logT)/logT`.

For the oscillatory part S_f, compact support of what eliminates every unequal signed product M/N for all sufficiently large T. Indeed an unequal integer pair has |log(M/N)|≥constant/min(M,N), while min(M,N)≤T^(j sigma/2) for a word of length j≤m. The averaging multiplier requires this logarithm to be O(1/H). Strict `m sigma/2<a` makes that impossible, uniformly in the height center. Equal products have multiplier what(0)=1.

Group balanced prime powers by their base prime. Surviving leading groups are opposite-sign equal primes, with the usual pair partitions and their two orientations. Every group with at least three entries, higher prime powers, or collisions between nominal pairs has total exponent at least four and a convergent p^−2 majorant; after normalization it is negligible. PNT and partial summation give

```text
(logT)^−2 sum_n Lambda(n)^2 fhat(logn/logT)^2/n
   → integral_0^infinity v fhat(v)^2dv.
```

For m≥2 the last integral equals V/2; m=1 concerns only the mean and may have support beyond 1. The pair counts therefore give `(2k)! V^k/(2^k k!)` for order 2k, and odd signed moments tend to zero. This proves the oscillatory theorem with the original full weight class and no RH. The longer preprint's pairing lemma is independently reconstructed in both reviews rather than taken on faith from a cited abstract.

Journal Proposition 2.3's phrase H→infinity is read in the established setting H=T^a, 0<a≤1. With the first logarithmic moment (or I=0), the repaired mean proof also covers 1≪H≤T. An unrestricted height claim would fail even for Schwartz w: H=T² gives mean 2I+O(1/logT) for I≠0. This contextual boundary is separate from the weight omission.

The smooth gamma contribution G satisfies `G(tau)=I log(1+|tau|)/logT+O_f(1/logT)` uniformly. For I=0 it is uniformly small. For I≠0 its deviation from I, with u=(tau−T)/H and K=T/H, is bounded by a constant times

```text
(logT)^−1 [1+log(2+|u|)+log_+(1/(|u+K|+H^−1))].
```

The far logarithm uses the assumed log moments. The moving logarithmic singularity is integrable using boundedness of w, which follows from its L1 property and compact Fourier support. For the required mixed powers one must do more than apply Hölder to an odd highest moment.

Both independent proofs close that issue by localizing the oscillatory moments. A fixed nonnegative bandlimited Schwartz bump dominating a slab of width delta gives the same equal-product argument at scale H delta, uniformly in its center, for delta≥T^−epsilon with epsilon smaller than the strict Fourier margin. This yields unweighted local absolute moments O(delta) at every even order needed for a mixed term. Reproduce w as w*eta with eta Schwartz and etahat=1 on the Fourier support of w; the suprema of w on unit cells, weighted by log^q of the cell index, are summable whenever its qth logarithmic moment is finite. This controls the far mixed terms. Exponentially shrinking slabs around u=−K control the local logarithm; the innermost slab costs O(T^−epsilon log^qT). For every r+q≤m with q≥1, an available even order at least r is still at most m. This proves the mixed gamma error additively, including odd m.

Fourier integration by parts bounds the polar terms by `C_A T^(sigma/2)(1+|tau|)^−A`, while the finite prime sum is bounded by C T^(sigma/2). Every averaged mixed term containing a polar factor is therefore O(T^(m sigma/2)/H), with possible harmless fixed log powers, and tends to zero by the same strict margin. Expansion compares the raw N_f moments to those of I+S_f with an additive O(1/logT) error. This is the correct replacement for the multiplicative comparison on p. 669; a vanishing signed odd moment cannot support that shortcut.

## Other claims, version checks and whole-work scope

The smooth count's 7/8 constant follows from the branch of the gamma factor and its initial 1. Selberg and Fujii supply historical longer-window Gaussian results; those deep proofs are background, not hidden premises in this argument. The ordinary CUE comparison uses periodized f and its Fourier coefficients n^−1 fhat(k/n). Haar scalar invariance and Schur orthogonality give the Gaussian trace pairings when each balanced weighted degree is at most n, yielding the closed support window in the source. Trace covariance min(|k|,n) gives exactly the stated variance. The higher-moment remark is a failure in general beyond the guaranteed window, not a claim about the zero test. Character-family sampling and derivative-weighted zero sampling remain different probability laws.

Both independent complete reviews cover all four controlling pages, the full explicit formula, mean and moment argument, ordinary CUE comparison, both abstracts, acknowledgment, three reference roles and the longer v1 proof. Accepted matched upstream inputs are the functional equation, Stirling, standard zero count/good-height bounds, PNT and Schur orthogonality. The entire cited Selberg/Fujii works and every ancestry proof were not reaudited. The director checked all controlling journal displays and the counterexample directly from the source.

An early suspicion that longer-v1 Proposition 2.5 omitted a factor of two was withdrawn after the rendered p. 6 showed that factor. The printed variance is consistent; no error is assigned to it. Bounded correction searches found no separately verified corrigendum. Some later expositions repeat the weaker weight description, while examined sharp-interval results have their own proofs and avoid this tail problem. Those limited readings do not establish errors in the later papers. The source assessment remains confined to the pinned original class and its explicit repair.

[Complete advocate](analytic89_hr_whole_advocate.md) · [Complete skeptic](weighted88_hr_whole_skeptic.md) · [Independent repair and later-use audit](analytic85_hughes_weight_repair_review.md) · [Initial independent witness](weighted82_hughes_rudnick_weight_review.md) · [Primary journal](https://archive.numdam.org/item/CRMATH_2002__335_8_667_0.pdf)
