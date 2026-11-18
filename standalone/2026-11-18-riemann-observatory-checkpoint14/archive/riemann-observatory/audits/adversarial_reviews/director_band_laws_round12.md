# Band laws, their Gaussian crossover, and the finite-moment barrier

18 November 2026. Director adjudication of the complete proofs linked below. The director read both independent arithmetic shrinking-band proofs, both intrinsic CUE law proofs and the third integration review, both formal-moment reconstructions, the relevant programs and recorded outputs. The primary HLZ source and its independently reconstructed sharp interface retain the precise scope in the Round 11 adjudication. These results are distinct from an arithmetic full-law transfer or a publication-priority claim.

## One probability convention throughout the arithmetic results

Assume RH and give the strict two-sided tail |gamma|>Y masses proportional to `|zeta'(1/2+i gamma)|²/(1/4+gamma²)`. Both signs are included, ordinate endpoints are strict, and zeros with multiplicity greater than one have zero derivative weight. No simplicity hypothesis is introduced. The normalization is finite and positive by the independently matched derivative-prefix asymptotic and partial summation. Every source polynomial is kept fixed at its Y-values while the prefix T varies over T≥Y.

## Shrinking bands have a Gaussian limit at finite variance

Let `L=log Y`, `b(Y)→0`, `a(Y)/b(Y)→r∈(0,1)`, and `a(Y)L→infinity`, with 0<a<b eventually. Then

```text
W_Y = sum_(Y^a<p≤Y^b) cos(gamma log p)/sqrt p,
H_Y = sum_(Y^a<p≤Y^b) 1/p
```

satisfy `W_Y−H_Y ⇒ N(0, (1/2)log(1/r))`, with convergence of every fixed moment. Centering by the actual mean gives the same conclusion. This is not obtained by substituting moving endpoints into a fixed-band asymptotic.

For a fixed moment order j, the powers of the prime polynomial have bounded coefficients depending on j and subpower length. The HLZ formula is applied once to the full aggregate using common divisor-closed positive padding and polarization. Its explicit main term differs from the Poisson-phase model by `O_j(b logY/logT)` relative to the positive lcm weights. The corresponding model moments are uniformly bounded since the band's reciprocal mass stays bounded. The aggregate source error has arbitrarily large fixed logarithmic saving. Thus every fixed arithmetic moment approaches the independent infinitesimal phase model uniformly on T≥Y. A prime removed for the effective exceptional-conductor estimate is restored *before* tail integration; its contribution is at most `2 exp(−aL/2)`. Exact inclusive prefixes then give the strict tail with a bounded ratio of total variation of the Stieltjes functional to its positive normalizing mass.

Mertens gives `H_Y=log(b/a)+O(1/(aL))`. Model variance is `(1/2)sum(1/p−1/p²)`, and its higher fixed cumulants vanish by the infinitesimal maximum `O(exp(−aL/2))`. Gaussian determinacy and the bounded second moment give weak convergence. A fixed-order parameter error is

```text
O_eff,j,M,r−,r+ [b + L^(−M) + exp(−aL/2) + 1/(aL) + |a/b−r|],
```

under the exact fixed-order length and ratio restrictions in the advocate's statement. Effective heights require effective convergence moduli for the band parameters; no numerical onset is asserted. A process conclusion is outside this scalar adjudication.

[Scalar proof and effective scope](analytic78_shrinking_band.md) · [Independent reconstruction and tightness warning](weighted78_shrinking_band_review.md)

## A complete limiting law inside the random matrix model

Fix any `0<a<b<infinity`. The finite CUE law is the **global** joint tilt of Haar U(N) and a root label j by `|Z_U'(theta_j)|²`. The chosen eigenvalue is rotated to zero and is included in

```text
X_N = −sum_(aN<k≤bN) (1/k) sum_(ell=1)^N cos[k(theta_ell−theta_j)].
```

It is not Haar first followed by a root-weight normalization inside each individual matrix. The free N−1 eigenvalues have circular Jacobi density Vandermonde² times `prod|1−z|⁴`. Their projection is the subspace of degrees 0 through N vanishing to order two at 1. The removed coefficient vectors are the normalized constant and centered-linear vectors.

In unit-density coordinates `u=N theta/(2π)`, the limiting projection is

```text
K(u,v) = integral_0^1 exp(2πis(u−v)) ds − e0(u)conj(e0(v)) − e1(u)conj(e1(v)),
e0(u) = integral_0^1 exp(2πisu) ds,
e1(u) = sqrt(12) integral_0^1 (s−1/2) exp(2πisu) ds.
```

Let `f(u)=−integral_a^b cos(2πxu)dx/x` and d(u)=|e0(u)|²+|e1(u)|². In the projection DPP define the **centered L²** statistic

```text
S(f) = lim_(R→infinity) [sum_(|u|≤R) f(u) − integral_(−R)^R f(u)K(u,u)du].
```

Then X_N converges in law and every fixed moment to `mu+S(f)`, where

```text
mu = f(0) − integral_R f(u)d(u)du
   = integral_a^b [−1 + 1_(x<1)(2−4x+2x³)]dx/x.
```

The conclusion holds jointly for any fixed finite family of bands, including sine tests. There is no upper-band restriction b<1/6 in this intrinsic RMT statement. That restriction belongs to a particular arithmetic moment calculation.

The noncompact statistic needs a summation convention. The absolute point sum diverges almost surely. Symmetric uncentered truncation with one deterministic root reinserted also gives the same raw law, since the constant-intensity symmetric integral of f tends to zero. Arbitrary unordered summation is not justified.

The law's centered characteristic function is

```text
det_2(I + P M_(exp(itf)−1) P)
  × exp{integral_R [exp(itf(u))−1−itf(u)] K(u,u)du},
```

on Ran P, where P has kernel K. Multiply by exp(it mu) for the raw rooted law. This formula retains its essential quadratic trace correction. The global ordinary Fredholm determinant is not justified here: the first operator is Hilbert–Schmidt, while the second-order correction is trace class.

The proof uses local kernel Riemann sums and compact DPP convergence, not an unjustified global trace norm limit. Abel summation gives `|f_N(u)|≤C min(1,1/|u|)` uniformly on the finite interval, and the same bound holds for f. Projection variance is bounded by `integral f² K(u,u)du`, so the centered squared tail is O(1/R) uniformly in N. Compact convergence followed by this tail estimate proves the full law. On the projection range the real exponential compression is strictly positive; `log(1+lambda)≤lambda` bounds both signs of the centered MGF uniformly at every fixed real argument. This yields uniform integrability of all fixed powers and joint moment convergence. These are independently complete arguments.

HKO supplies the finite derivative tilt. Bourgade–Nikeghbali–Rouault supplies the circular Jacobi and general confluent-hypergeometric lineage. Bufetov and Gorbunov identify the Palm hierarchy; the integer-parameter projection limit also has an elementary direct proof here. The confluent *reduced* double Palm removes both colliding locations, and this observable reinserts exactly one deterministic root. The four new dependency papers are targeted Level 0 source records, not complete readings. The Bufetov DOI typo in the pending contributor record is corrected on admission and retained in its change receipt.

[First full proof](prime77_rooted_cue_band_limit.md) · [Independent full proof and nonabsolute summation](uniform77_rooted_cue_full_law.md) · [Third source and interface review](geometry80_full_cue_adjudication_input.md)

## Finite support moments cannot be extrapolated unchanged to all orders

For a fixed positive arithmetic band 0<a<b and each fixed integer r with `rb<1/2`, the limiting raw rth moment is r! times the coefficient of z^r in the **formal expression**

```text
M_form(z) = exp(H z + H z²/4) [(1−d z)^4 + q z(1−d z)],
H=log(b/a), d=b−a, q=(2/3)(b³−a³).
```

The source supplies only those finitely many coefficients at fixed b. The all-order extension is impossible as a probability moment sequence.

The leading distinct-prime kernel has total frequency degree at most four. Its lower interactions are the already checked one-, two- and three-prime kernels, and direct extraction of the four-singleton coefficient gives 24. Explicitly it is

```text
1 + sum_i(−4x_i+2x_i³)
  + sum_(i<j)[12x_i x_j−2x_i x_j(x_i²+x_j²)]
  −24 e3(x) +24 e4(x).
```

Setting an unused frequency to zero supplies subset consistency. In a repeated-prime signed word only opposite-sign pairs survive; all other repetitions have lcm weight p^−2 or smaller and vanish. The surviving pair contributes H/2, with exact Wick partition counts. Integrating singleton interactions against dx/x gives the quartic bracket, and Wick pairs supply exp(H z²/4). This argument applies the source remainder to the aggregate **before** expanding the main term. Total-degree four of the main term does not shorten the source polynomial D^r.

The formal inverse is a signed Gaussian-polynomial density. In y=(W−H)/sigma, sigma=sqrt(H/2), s=d/sigma, q'=q/sigma, its standard-Gaussian factor is

```text
R(y)=(1−s y)^4−6s²(1−s y)²+3s⁴+q'[y−s(y²−1)].
```

At y=1/s+sqrt(3), this is `−6s⁴−q'(sqrt(3)+2s)<0`. More simply, M_form(1/d)=0. If a positive probability shared *all* formal moments, its even moments would be dominated by the absolute Gaussian-polynomial inverse. Monotone convergence of cosh gives every finite exponential moment; its MGF must equal the entire formal series. The zero is then impossible. This verifies the determinacy step rather than relying on a numerical density plot.

For [a,b]=[1/20,1/10], a degree-70 Hermite polynomial supplies a finite negative Gram test using formal moments through 140. The proponent's exact triple-Hermite computation and the director's independent Gaussian integration-by-parts computation give

```text
E_form[Q70²]/E_G[Q70²] = −0.0011820826117612421070700877… < −0.00118,
Q70(y)=sum_(j=0)^70 (13/2)^j He_j(y)/j!.
```

The director's 192-bit interval has a separate code hash and result. Its independent formula is `E[He_k Q_n²]=c^k sum_j binom(k,j) sum_(i≤min(n−j,n−k+j)) c^(2i)/i!`, from Gaussian integration by parts and Q_n^(j)=c^j Q_(n−j). Degrees 30–60 in the proponent's tested sequence remain positive; no least failing degree is claimed. Actual arithmetic support here supplies orders only 0–4. The skeptic proves strict positivity for every Hankel degree inside the genuine source window. There is no contradiction with the published theorem or a candidate true band law with different higher moments.

This is negative knowledge about a precise extrapolation, with classical mock-Gaussian and polynomial-normal antecedents preserved. It does not establish publication novelty. The next research step is to derive the missing higher-frequency chamber main terms or a characteristic-function comparison; another low-support moment does not by itself identify the full arithmetic law.

[Primary-source kernel and finite certificate](prime79_hlz_formal_moment_obstruction.md) · [Independent source extraction and positive valid-window tests](weighted79_formal_band_obstruction_review.md) · [Prior-art search and its limits](analytic79_prior_art.md) · [Independent director certificate](../../experiments/results/director_round12_formal_gram.json)

## Finite random matrix experiment and trust boundary

The deterministic finite-N experiment computes projection trace means, variances and cubic cumulants, with an independently dense exact rational check. At N=2000 the band [1/20,1/10] has mean 0.491339563439, variance 0.335512134874 and cubic −0.000946104954; the proven limits are approximately 0.493730513893, 0.336748250002 and −0.000947805853. The director inspected the trace formulas and replayed the arithmetic symbolic certificates; two agents independently replayed the full finite-N JSON and third source review also reproduced it. These floating finite-N values are implementation checks, not certified convergence errors, zeta zero data, or evidence of a full arithmetic law. The source programs, exact small cases, failed lower-degree Gram tests, output pins and replay instructions are preserved.
