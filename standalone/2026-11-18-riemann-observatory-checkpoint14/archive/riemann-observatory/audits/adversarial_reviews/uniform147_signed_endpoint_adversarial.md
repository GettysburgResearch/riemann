# Independent check of conditional zero summation in the logarithmic strip scale

I independently reconstructed the candidate and found no gap for the following statement. Let f be continuous with f(x)=O(x^δ) at zero and O(x^(−1−δ)) at infinity. Suppose F(u)=e^(u/2)f(e^u) belongs to H¹ on a neighborhood of u=0, and the Mellin transform h has finite strip area norm N_p with weight w_p(t)=sqrt(1+t²) log^p(e+|t|) on β∈[−ε,1+ε], 0<ε<δ. For every p>1 the raw symmetric sum over actual zeros converges and equals the ordinary compensated Guinand–Weil formula. The proof in fact gives convergence on each half-height axis. A local C¹ or continuous piecewise C¹ test with locally bounded one-sided derivatives at x=1 meets the local H¹ hypothesis. This does not establish convergence for the whole finite-p=3 norm class without any such local assumption. No RH is used.

## External estimates and conventions

I inspected the source passages in the stored [Titchmarsh second-edition scan](../../sources/selberg_round2/titchmarsh_zeta.pdf), chapter IX Theorem 9.19(C) (printed p. 237), Theorem 9.3 and the adjoining definition of S(T), and the Notes §9.25, (9.25.1). Theorem 9.19(C) states the Selberg bound uniformly for 1/2≤σ≤1, with exactly one factor log T:
```text
N(1/2+v,T) ≪ T log T exp(−cv log T)
```
for a fixed c>0. Its uniformity as v decreases with T is essential. The Notes give Selberg's unconditional even moments of S(T); the second moment is O(T log log T). These are source-passage checks in the standard monograph, not a review of the entire monograph or Selberg's original proof. The use of either strict or non-strict real-part counting has no effect on the layer-cake integral. Theorem 9.3 uses the right-hand limit at ordinate jumps. Taking right limits of the standard O(log T) remainder also gives a pointwise bound there. Any alternative pointwise convention changes S only at a discrete set and leaves the mean square unchanged.

Use M(t)=(t/(2π)) log(t/(2π))−t/(2π) for t≥2, and define S₀(t)=N(t)−M(t), with N counting 0<γ≤t. By Theorem 9.3 this differs from S(t) by O(1) and has S₀(t)≪log t at every height, with ∫_[T,2T]|S₀|²≪T log log T. Also N(n+1)−N(n−1)≪log(2+|n|) on positive unit cells, with the negative-height counterpart by conjugation of zeros.

## Off-line projection and exact raw cutoff

The disk Cauchy formula and area mean-value inequality give, for a fixed small radius depending on ε,
```text
Σ_n w_p(n) sup_(0≤β≤1,n≤t≤n+1) (|h(β+it)|+|h′(β+it)|)² ≪_(ε,p) N_p².
```
Use nested fixed disks wholly inside the norm strip, then enlarge each cell by their radii. Moderate weights and bounded vertical overlap suffice. In particular the vertical trace of the derivative of H(t)=h(1/2+it) lies in L²(w_p dt).

Put a_ρ=|β−1/2|. Reflection in the critical line at the same ordinate and the density estimate give
```text
Σ_(T≤γ≤2T) a_ρ² ≪ T log T ∫₀^(1/2) v exp(−cv log T) dv ≪ T/log T.
```
Counts at both dyadic endpoints can be bounded by the cumulative count at 2T or 3T. Let A_n be the sum of a_ρ in a half-open unit cell. By Cauchy–Schwarz in the cell, A_n² is bounded by its zero count times the sum of squares there. Thus Σ_(T≤n<2T) A_n²≪T including multiplicities. Applying the fundamental theorem along each horizontal segment to Re s=1/2 bounds the difference between h(ρ) and H(γ) by a_ρ times the derivative supremum. Cauchy–Schwarz over all cells bounds the absolute projection correction by N_p times the square root of Σ_n A_n²/w_p(n). The dyadic blocks of this latter series cost O((log T)^−p), which are summable for p>1. The same proof holds on negative heights and on tails, giving an O(N_p(log T)^((1−p)/2)) projection correction beyond height T.

With a fixed  B≥2, Stieltjes integration for the projected sum in (B,T] gives
```text
∫_(B,T] H dN = ∫_B^T H M′ dt + H(T)S₀(T) − H(B)S₀(B) − ∫_B^T H′(t)S₀(t) dt.
```
Right-continuous N includes every zero at the exact upper endpoint. Since the pointwise trace satisfies |H(T)|≪N_p w_p(T)^−1/2, the upper boundary goes to zero uniformly in the height convention. The absolute integral of H'S₀ is bounded by Cauchy–Schwarz because on a dyadic block ∫ S₀²/w_p ≪ (log log T)/(log T)^p. Summing over blocks yields convergence for p>1 and a tail O(N_p (log T)^((1−p)/2) sqrt(log log T)). This step uses the global dyadic mean bound and needs no short-interval S mean square. Replacing H(t) with h(1/2−it) proves the negative-height statement, even for complex f.

## Logarithmic density term and smooth approximation

The smooth main term is not a consequence of the strip norm alone by absolute Cauchy–Schwarz when p≤3. Take χ smooth compactly supported where F is H¹, with χ=1 near zero, and use Fourier convention exp(itu). The transform H_near of χF is absolutely integrable against log(2+|t|), by Cauchy–Schwarz with 1+t². For the remaining part take m(u)=(1−χ(u))/(iu); its Fourier transform is in weighted L¹ for any fixed polynomial weight because m and every derivative lie in L². Set G=Fourier(mF). Then G'=H_far. Both G and G' are in L²(w_p dt): weighted convolution proves this for G, using the moderate weight and weighted L¹ of Fourier(m), and H_far follows from bounded smooth localization of H. Local one-dimensional H¹ therefore gives |G(T)|≪N_p w_p(T)^−1/2. Integration by parts against M'(t)=log(t/(2π))/(2π) yields a convergent endpoint G(T)M'(T) and absolute integral of G(t)/(2πt). Thus the full signed trace is continuous in N_p plus the fixed local H¹ norm. Contrary to a tempting shortcut, this argument does not require far-support F to be globally H¹ or its ordinary derivative to decay.

For identifying the limit, approximate F first by χ_R F with χ_R(u)=χ_*(u/R), a smooth cutoff equal to 1 on increasing neighborhoods, then by convolution with compact smooth mollifiers of radii tending to zero. On each β-line the cutoff acts by a uniformly bounded weighted Fourier approximate identity, strongly tending to the identity since the weight is polynomially moderate. The mollification has bounded Fourier multipliers from the exponentially tilted mollifiers, tending to 1 uniformly on compact (β,t) sets. Dominated convergence over β and a diagonal choice give convergence in N_p. On a fixed smaller neighborhood of u=0 the cutoff eventually equals 1, and the mollification converges in local H¹, by using a translated compact localization inside the original H¹ interval. The approximants inherit uniform original exponential envelopes in u, converge pointwise, and are smooth with compact support. This proves convergence of the terms h(0), h(1) and the discrete Mangoldt sum by dominated convergence. For the compensated archimedean term the reflected value f(1/x)/x retains the same uniform bounds; near x=1 local H¹ implies a uniform 1/2-Hölder bound, and the compensated integrand is O((x−1)^−1/2). Hence that term also converges by domination. Apply the classical compact smooth explicit formula to each approximant and use the signed-trace norm continuity above. This procedure uses no interpolation over exceptional heights, Abel zero weighting, or appeal to the broader failed manuscript assertion.

## Boundaries

The earlier p=3 random-sign smooth counterexample to absolute zero sampling satisfies local H¹ and therefore has signed convergence under this theorem. The norm and value bounds alone do not imply signed convergence, as the separate cusp example below shows. Finding a weaker local condition under which signed convergence holds remains open here. The pinned manuscript's literal condition (A) explicitly imposes finite one-sided limits of both f and f′ at its finitely many exceptional points. In that class, finite p>1 strip norm gives H∈L¹ by Cauchy–Schwarz, so Fourier inversion gives a continuous representative and precludes genuine jumps; the midpoint convention fixes the actual point values. The finite one-sided limits of f′ then give local bounded derivative on either side of x=1 and local H¹. Thus the signed sufficiency assertion also applies with literal (A) and the strip norm. The separate cusp below falls outside literal (A). A local Hölder/Dini alternative or a different use of the main density integral would need its own proof. At p=1 the dyadic Cauchy–Schwarz sums above diverge, which does not establish failure. This check is next-round research and leaves the frozen Round 15 record unchanged.


## A separate cusp obstruction when local regularity at one is omitted

There is a continuous real compactly supported f, smooth off x=1, with finite p=3 strip norm whose real symmetric raw-height sum tends to +infinity. This concerns the norm and value bounds alone. It has a divergent local archimedean integral and is distinct from both the smooth p=3 absolute-divergence example and the smooth raw-height counterexample with finite arithmetic side. It falls outside the manuscript's literal condition (A), since finite one-sided limits of f′ would give local H¹.

Choose a smooth positive even k(t) with k(t)=1/(|t| log²|t| log log|t|) for large |t|. Then k is L¹, and
\[
\int^\infty w_3(t) |k(t)|^2\,dt\ll\int^\infty \frac{dt}{t\log t(\log\log t)^2}<\infty,
\qquad
\int^\infty k(t)\log t\,dt=\infty.
\]
Let K be its inverse Fourier transform. Take a real even nonzero smooth compact bump φ with nonzero integral, set D=φ*φ̃ with φ̃(u)=φ(−u), and set F=DK and f(x)=x^(−1/2)F(log x). All these definitions use the same exp(itu) Fourier convention. The function F is real, continuous, even and compactly supported, and f has the required value bounds for every δ. For smoothness away from u=0, the high-frequency symbol obeys |k^(j)(t)|≪_j |t|^(−1−j). A smooth dyadic partition and m+2 integrations by parts in t on each piece of the m-th differentiated Fourier series makes those pieces O_(m,I)(2^(−2r)) on compact u intervals I avoiding zero. This proves smoothness off u=0.

At β=1/2, its Mellin transform is H=(k*hat D)/(2π), with hat D=|hat φ|² nonnegative and positive near zero. Thus H≥0 and H(t)≥c k(t) at large |t|, since k(t−v) is uniformly comparable to k(t) for |v|≤1. At every other real β in the fixed strip the Mellin transform is the convolution of k with Fourier(e^((β−1/2)u)D), divided by 2π. These kernels are uniformly Schwartz on this compact β range. Weighted Young's inequality gives a uniform L²(w₃) bound and hence the required finite area norm.

The off-line projection correction and the counting-remainder integral proved above at p=3 use only the strip norm and value bounds. The upper S₀ boundary tends to zero at exact ordinate heights. The projected smooth term nevertheless tends to positive infinity, since M′(t)=(log(t/(2π)))/(2π) and H(t)≥c k(t) for large t. Evenness and reality give the same sign on both height halves. This proves signed raw-height divergence in the continuous class, with no RH.

There is a matching local arithmetic obstruction. Since H is nonnegative even and L¹, Fourier inversion gives F(0)−F(u)=(1/π)∫₀^∞ H(t)(1−cos(tu))dt≥0. Tonelli on a fixed small u interval shows ∫₀^a (F(0)−F(u))du/u diverges. Indeed after substituting v=tu, ∫₀^(at)(1−cos v)dv/v=log t+O_a(1) as t grows. This is the singular part of the compensated archimedean integral under x=e^u. The replacement of its leading 1/u factor by the exact kernel, together with the smooth tilt and compensator, introduces only locally integrable error. In particular F cannot be locally H¹ at zero.
