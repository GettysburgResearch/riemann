# Joint cubic dependence and the shrinking-band Brownian process

18 November 2026. The director read the complete independent prime81 and weighted81 signed HLZ/CUE reconstructions and both complete uniform81 and analytic82 process arguments. This adjudication separates two different cutoff regimes. Both arithmetic conclusions assume RH and use the strict symmetric derivative-square tail with atom weights `|zeta'(1/2+i gamma)|²/(1/4+gamma²)`. The intrinsic CUE statements are unconditional. No full arithmetic band law, practical numerical onset, or publication novelty follows.

## A zero covariance can coexist with persistent cross-band dependence

Fix 0<a<b<1/6. For bounded real Riemann-integrable weights supported in [a,b], let

```text
C_f = sum_p f(log p/log Y) cos(gamma log p)/sqrt p,
S_g = sum_p g(log p/log Y) sin(gamma log p)/sqrt p.
```

The mixed centered cubic satisfies

```text
lim kappa(C_f,S_g,S_h)
 =12 [integral_a^b f(x)(x²−2)dx]
      [integral_a^b g(y)y dy] [integral_a^b h(z)z dz].
```

The centered cosine kernel is the earlier cubic kernel; all entries with an odd number of sine slots vanish exactly by reflection. Together these determine the full third tensor. For an unweighted common band, writing Delta_j=b^j−a^j, the new entry is `(Delta_3−6Delta_1)Delta_2²`. At [1/20,1/10] it equals exactly `−21537/1280000000`.

The source calculation is signed, not inferred from the all-cosine average. Use `D(rho)=W−iS` and `W S²=(Re(D² conjugate(D))−Re(D³))/4`. The signed J coefficient in HLZ (5) is `−yz(x+y+z−1)/2`; the reflected I coefficient in (24) is `yz(x−yz+y+z−1)/2`. After normalization by 1/12 their sum is the distinct raw kernel `−6y²z²`. Subtract the cosine mean `F(x)=1−4x+2x³` times the distinct sine covariance `−6y²z²`, giving the centered kernel `12xy²z²(x²−2)`.

An equal-prime sine pair supplies the constant mode `(1/2)sum gh/p` times the cosine mean. It cancels its covariance diagonal after centering. A cosine–sine equal-prime pair has no constant mode. Other repetitions carry a p^−2 lcm weight and vanish. All source remainders are charged to the finite list of whole polynomial polarizations before expanding the arithmetic main term. Their longest arm has length Y^(3b), so 3b<1/2 is essential in this argument. Inclusive prefixes at Y give the strict boundary after Stieltjes transfer. The bounded Riemann weights are evaluated at the fixed Y-scale throughout that transfer.

The independent CUE calculation expands the third mixed projection trace for P=E−Q, with Q the same two-mode removal as in the full-law proof. It expresses each term with Q as a product of two-by-two polynomial path-integral matrices. The base E third cumulant cancels, including the resonant signed sum zero case. Exact polynomial identities agree on all order/triangle chambers: the proponent checks 12, and the independent reviewer uses the sine-exchange symmetry to reduce to six. Boundaries follow by continuity. The director replayed both independent symbolic programs; the rational witness is also obtained directly from the displayed integrals.

Fourth moments are uniformly bounded on both sides: the arithmetic uses `|Re D|⁴,|Im D|⁴≤|D²|²` and the aggregate source, and CUE uses its projection exponential bound plus Fourier L² orthogonality. Hence cubic vector monomials are uniformly integrable. For nonnegative f,g with strictly positive integrals, the limit of `kappa(C_f,S_g,S_g)` is negative, even when the supports are disjoint. Nonzero values confined to null sets do not suffice. Reflection gives exact zero covariance. Every weak subsequential vector limit therefore has dependent cosine and sine coordinates: independence would make the centered mixed cubic zero. This does not decide a sine marginal's Gaussianity or existence of a full arithmetic vector limit.

[Independent source and 12-chamber proof](prime81_joint_third.md) · [Separate signed source and six-chamber proof](weighted81_joint_third_review.md)

## Brownian motion throughout a shrinking subpower band

Fix 0<r0<1, let b(Y)→0 with b(Y)logY→infinity, and set

```text
X_Y(r)=sum_(Y^(r0 b)<p≤Y^(r b)) [cos(gamma logp)/sqrt p−1/p], r0≤r≤1.
```

Then X_Y converges in D([r0,1]) with J1 topology to `B_((1/2)log(r/r0))`. A complete proof of tightness, beyond scalar Gaussian limits, is essential. The reusable estimate is that for **every** subset I of the band, h=sum_(p in I)1/p,

```text
E_Y |sum_(p in I)(cos(gamma logp)/sqrt p−1/p)|⁴ ≤ C_(r0) h^(3/2).
```

There is no asserted uniform Ch² bound throughout the full subpower range. The exponent 3/2 is obtained by combining two genuinely different estimates, and any fixed exponent 2−eta, 0<eta<1, is available by the same comparison.

First, the aggregate HLZ source gives a uniform fourth bound `C_M(h²+(logY)^−M)`. One direct proof uses `|Re D_I|⁴≤|D_I²|²`, bounded divisor-closed padding, and the exact positive lcm main weights. The independent Poisson model's complex fourth moment is O(h²), since its centered independent coordinates have sum of variances O(h) and sum of fourth moments O(sum p^−2)≤O(h²). Its mean contributes only bounded h⁴. If an exceptional prime is omitted, its centered fourth power is at most 16/p²≤16h², so restore it before varying the prefix endpoint or integrating the tail. The absolute logarithmic remainder alone is insufficient at arbitrarily small h.

Second, a separate analytic sampling argument proves `C(logY)²h²` with exact h-dependence. For each fixed prefix T≥Y, set F(s)=zeta(s)D_I(s)². At each zero on RH, `F'(rho)=zeta'(rho)D_I(rho)²`, also at multiple zeros. Analytic disk orthogonality on radius R=1/logT gives

```text
|F'(rho)|² ≤ 2/(πR⁴) integral_(disk) |F(s)|² dA(s).
```

The multiplicity-counting overlap is O(logT) by the unit-window zero count. On the strip `|sigma−1/2|≤1/logT`, the continuous fourth moment of zeta is O(T log⁴T), and the continuous eighth moment of D_I is O(Th⁴). The latter follows directly from the coefficients of D_I⁴, bounded by 4!, and a diagonal/off-diagonal Dirichlet mean estimate; its support Y^(4b) is eventually at most T^(1/2). Cauchy–Schwarz gives O(T log²T h²) per vertical line. Multiplying by disk factor log⁴T, overlap logT and strip width 1/logT gives O(T log⁶T h²). Divide by the true derivative-prefix mass of order T log⁴T.

The thin-strip fourth moment does not require a hypothesis on higher discrete derivative moments. Use the classical Ingham fourth moment, matched in Titchmarsh–Heath-Brown (7.6.2)/(7.21.1). On [1/2,2] localize analytically by `((s−1)/(s+1))zeta(s)exp(s²/T²)`; its full vertical L⁴ norms at both boundary lines are bounded by Gaussian dyadic summation and the absolutely convergent series. Pairing with L^(4/3) tests permits three-lines interpolation. The factors are bounded away from zero in the thin strip for |t|≤T+1. The functional equation gives its left half. This step and the disk power accounting were independently rebuilt. The entire classical fourth-moment proof ancestry is an accepted matched external input, not a whole-monograph audit.

Transfer both positive fourth bounds to the strict tail. The inclusive boundary term has favorable negative sign and can be discarded for an upper bound. The extra log²T costs only O(log²Y) under inverse-quadratic tail integration. Thus, L=logY,

```text
fourth moment ≤ C_M min(h²+L^−M, L²h²).
```

For h≤L^−4 use the second term; for h≥L^−4 use the first with M≥6. Both give Ch^(3/2). Empty subsets vanish exactly. This comparison closes the small-scale gap rather than silently replacing a vanishing remainder by a mass-sensitive one.

Interpolate at exact reciprocal-prime times `v_j=(1/2)sum_(i≤j)1/p_i`. Fractional increments have fourth powers and therefore satisfy the same 3/2 time exponent. Splitting an arbitrary interval into at most three pieces and using Minkowski gives the all-time estimate. A dyadic fourth-moment argument with Hölder exponent below 1/8 gives uniform continuity in probability and tightness of the interpolants. Mertens gives the uniform clock approximation `(1/2)sum_(Y^(r0b)<p≤Y^(rb))1/p=(1/2)log(r/r0)+O(1/(bL))`. The original step process equals the interpolant at its exact clock; jumps are at most `2exp(−r0bL/2)`.

Finite-dimensional real projections have bounded piecewise constant prime coefficients and all fixed model moments by the aggregate subpower argument. Infinitesimal model coordinates give the Gaussian covariance `(1/2)log(min(r,s)/r0)`, and Cramér–Wold identifies Brownian motion. Clock approximation and the uniform modulus transfer the continuous surrogate's limit to the original step process in J1. Effectivity requires computable r0, effective band moduli, and the explicitly audited effective aggregate input; no numerical threshold or increasing-dimensional uniform claim is made.

[Full process proof](uniform81_shrinking_band_process.md) · [Independent sampling, clock and tightness audit](analytic82_shrinking_process_skeptic.md)
