# Fixed logarithmic Möbius windows: multiplicity ceilings and a variable-order missing estimate

Date:2026-11-17. Independent reconstruction by equivalences from root's proposed interface. Status: proof below for fixed-order necessary conditions; variable-order approximation is an explicitly unproved research target. No novelty, RH proof, or sufficient RH criterion for a prescribed fixed array is claimed.

## Definitions and exact necessary statements

For fixed real α≥0 and integer N≥2 define

\[
 V_{N,\alpha}(s)=\sum_{n\le N}\mu(n)
   \left(1-\frac{\log n}{\log N}\right)^\alpha n^{-s}.
\]

For α>0 the endpoint n=N has weight0. For α=0 use the hard cutoff weight1, including n=N; taking the strict cutoff instead changes the coefficient sum by at most1 and does not affect any asymptotic conclusion below. This specifies the otherwise ambiguous0^0.

For every fixed integer q≥1 let

\[
 d_q(V)^2=\frac1{2\pi}\int_{\mathbb R}
  \frac{|1-\zeta(1/2+it)V(1/2+it)|^2}{|1/2+it|^{2q}}\,dt.
\]

The quantity d_q is the norm, not its square; the array is prescribed, not optimized over coefficients. All limits below are along **every** sufficiently large integer N, unless a limsup is explicitly written.

**Fixed-order necessity.** If d_q(V_(N,α))→0, then RH holds and every nontrivial zero of multiplicity m satisfies

\[
 \boxed{m<\alpha+1.}
\]

For α>0 this is equivalent to m≤ceil(α). At α=0 the convergence is impossible, since RH plus the existence of nontrivial zeros would give a critical zero of positive integer multiplicity, contradicting m<1. In particular, any fixed0<α≤1 still requires simplicity; increasing the fixed taper order changes the ceiling, while changing only fixed spectral q does not.

**Quantitative version.** Let ρ=1/2+iγ be any critical zero of multiplicity m≥1. Then for every fixed α≥0 and integer q≥1,

\[
 \boxed{
 \limsup_{N\to\infty}
 \frac{d_q(V_{N,\alpha})}{(\log N)^{m-\alpha-1}}
 \ge\frac{m\Gamma(\alpha+1)}{|\rho|^{\alpha+1}|\zeta^{(m)}(\rho)|}.}
\]

An infinite limsup makes this automatic. If m>α+1 the norm has an unbounded subsequence, at least of the indicated logarithmic scale. If m=α+1 it has a positive limiting upper bound. If m<α+1 the inequality is a rate restriction and does not prevent convergence. No conclusion uniform in growing q or moving α is asserted here.

## 1. The scalar coefficient witness survives every fixed spectral integration

The exact unitary Mellin/reflection identity in `audits/adversarial_reviews/weighted_selberg_round2.md` applies to **any** finite coefficient vector. For V=Σ_(n≤N)a_n n^(−s), C_N=Σa_n, set

\[
 W_N(u)=\sum_{n\le N}\frac{a_n}{n}\{nu\},\qquad
 g(u)=-\sin(2\pi u)/\pi,
 \quad I h(u)=\int_0^u h(v)\,dv/v.
\]

With H=L²((0,∞),du/u²), that identity is

\[
 d_q(V)=\|I^{q-1}(W_N-g)\|_H.
\]

It follows from Mellin multipliers1/s and the unitary boundary reflectionχ(s)((1−s)/s)^q on Re(s)=1/2. The boundary measure is dt/(2π). The finite-vector identity has no α-dependent assumption.

On0<u<1/N, W_N(u)=uC_N and Iu=u. Also

\[
 I^{q-1}g(u)=-2u+O_q(u^3),\quad
 |I^{q-1}g(u)+2u|\le(4\pi^2/3^q)u^3.
\]

Restricting the norm to that shrinking interval gives

\[
 d_q(V)\ge\frac{|C_N+2|}{\sqrt N}
       -\frac{4\pi^2}{3^q\sqrt5}N^{-5/2}. \tag{1}
\]

Thus

\[
 |C_N|\le\sqrt N\,d_q(V)+2+O_q(N^{-2}). \tag{2}
\]

No assertion about inverse boundedness of I is used. The operator has eigenvalue1 on the local linear term u; this is why every fixed q leaves the coefficient obstruction intact.

For the present array put

\[
 \Psi_\alpha(x)=\sum_{n\le x}\mu(n)\log(x/n)^\alpha.
\]

For α=0 interpret this as the ordinary summatory Möbius function with the chosen hard cutoff. At integer N,

\[
 \Psi_\alpha(N)=(\log N)^\alpha C_{N,\alpha}. \tag{3}
\]

Consequently norm convergence gives Ψα(N)=o(√N(logN)^α). The next step verifies that a fractional taper does not hide a cutoff interpolation problem.

## 2. Integer-to-real interpolation, including0<α<1

Let N≤x<N+1, N≥2, and δ=log(x/N)≤1/N. For α>0 no new positive-weight index enters before N+1, and

\[
 |\Psi_\alpha(x)-\Psi_\alpha(N)|
 \le\sum_{n\le N}\{(\log(N/n)+\delta)^\alpha-\log(N/n)^\alpha\}.
\]

All terms on the right are nonnegative.

For0<α<1, separate n=N, which contributes δ^α≤1. For n≤N−1, concavity and the mean-value bound give

\[
 (a+\delta)^\alpha-a^\alpha\le\alpha\delta a^{\alpha-1},\quad a=\log(N/n)>0.
\]

Since log(N/n)≥(N−n)/N and the exponentα−1 is negative,

\[
 \sum_{n\le N-1}\log(N/n)^{\alpha-1}
 \le N^{1-\alpha}\sum_{k=1}^{N-1}k^{\alpha-1}
 \le N/\alpha.
\]

The last step follows by comparison with∫_0^N t^(α−1)dt. Hence the difference is at most2, uniformly in N (indeed also in this interval of α). No derivative was taken at a=0.

For α≥1, convexity gives

\[
 (a+\delta)^\alpha-a^\alpha\le\alpha\delta(a+\delta)^{\alpha-1}.
\]

The function t↦log(x/t)^(α−1) is nonincreasing on(0,N] and integrable at0, so

\[
 \sum_{n\le N}\log(x/n)^{\alpha-1}
 \le\int_0^N\log(x/t)^{\alpha-1}dt
 \le x\Gamma(\alpha).
\]

It follows that the interpolation difference is at most(3/2)Γ(α+1). At α=1 this argument also works directly. At α=0 the hard-cutoff sum is constant on[N,N+1), so the difference is0 (and the alternative strict-endpoint convention costs at most1).

Thus, for every fixed α≥0,

\[
 \boxed{\Psi_\alpha(x)-\Psi_\alpha(\lfloor x\rfloor)=O_\alpha(1).} \tag{4}
\]

Since √x(logx)^α→∞, full-sequence integer little-o bounds transfer to every real x. This does not establish an analogous conclusion from a sparse subsequence of N.

## 3. Mellin transform and the pole-order argument

For Re(s)>1, absolute convergence permits termwise integration and the substitution x=ne^v:

\[
\begin{split}
 \int_1^\infty\Psi_\alpha(x)x^{-s-1}dx
 &=\sum_{n\ge1}\mu(n)n^{-s}\int_0^\infty v^\alpha e^{-sv}dv\\
 &=\frac{\Gamma(\alpha+1)}{s^{\alpha+1}\zeta(s)}. \tag{5}
\end{split}
\]

The branch s^(α+1)=exp((α+1)Log s) is the analytic principal branch in Re(s)>0. Γ(α+1)>0 and s≠0 in the half-plane used below.

If Ψα(x)=O(√x(logx)^B) for any fixed finite B≥0, the integral on the left is holomorphic in Re(s)>1/2, by absolute convergence locally uniformly there. Equation(5) continues there and excludes zeros of ζ in that open half-plane. Reflection gives RH. In particular the little-o bound from(2)–(4) yields RH.

At a critical zero ρ of multiplicity m, put s=ρ+ε, ε>0. With x=e^v, the little-o estimate gives

\[
 \epsilon^{\alpha+1}\int_1^\infty
 \Psi_\alpha(x)x^{-\rho-\epsilon-1}dx\longrightarrow0.
\]

Proof: split at a fixed large v; on the tail e^(−v/2)|Ψα(e^v)|≤ηv^α, then use ε^(α+1)∫_0∞v^αe^(−εv)dv=Γ(α+1); the fixed compact part vanishes, and η is arbitrary. This absolute estimate is valid even though the integrand has the oscillation e^(−iγv).

But(5) has radial Laurent leading term

\[
 \frac{\Gamma(\alpha+1)m!}
      {\rho^{\alpha+1}\zeta^{(m)}(\rho)}\epsilon^{-m}.
\]

Multiplication by ε^(α+1) cannot tend to0 when m≥α+1. This proves the strict ceiling m<α+1.

## 4. Quantitative limsup constant, with norm rather than norm square

Write

\[
 D=\limsup_N d_q(V_{N,\alpha})/(\log N)^{m-\alpha-1}.
\]

Assume D finite; the infinite case needs no argument. Equations(2)–(4) imply

\[
 |\Psi_\alpha(x)|\le(D+o(1))\sqrt x(\log x)^{m-1}. \tag{6}
\]

The additive terms2(logx)^α and Oα(1) disappear after division by √x(logx)^(m−1), for every fixed m≥1,α≥0. The bound also supplies the open-half-plane analyticity needed above; no independent RH assumption is inserted.

Multiplying(5) at ρ+ε by ε^m, the absolute integral bound from(6) gives

\[
 \limsup_{\epsilon\downarrow0}\epsilon^m
 \left|\int_1^\infty\Psi_\alpha(x)x^{-\rho-\epsilon-1}dx\right|
 \le D\Gamma(m)=D(m-1)!.
\]

The pole coefficient has modulus Γ(α+1)m!/[|ρ|^(α+1)|ζ^(m)(ρ)|]. Comparing proves the stated constant. Real α makes|ρ^(α+1)|=|ρ|^(α+1) on the chosen branch. All factorials and the distinction between d and d² are retained.

## 5. Precise finite-model interface; necessity is not sufficiency

For the finite polynomial model Q=(1−z)^m and the scalar taper(1−n/M)^p, the terminal coefficient prevents convergence when p≤m−1. Conversely the same twisted-difference upper proof used for the sharp1/M threshold gives collision-uniform convergence for every p>m−1:

* m−1<p<m−1/2: E_M=O_(m,p)(M^(−2(p−m+1)));
* p=m−1/2: E_M=O_m(logM/M);
* p>m−1/2: E_M=O_(m,p)(1/M).

For the first range the power sum has exponent2(p−m)<−1 and is bounded; the finite terminal block has the same decaying scale. At p≤m−1, the exact final coefficient stays nonzero or grows at complete coalescence. Thus the finite model's **convergence** threshold is p>m−1, while its optimal-order1/M threshold is stricter, p>m−1/2.

The arithmetic ceiling m<α+1 is the same inequality α>m−1. This is a concrete match of fixed-window multiplicity constraints, not merely shared terminology. What is proved arithmetically here is a necessary obstruction. The finite model supplies no sufficient Möbius cancellation estimate, no infinite-zero summability bound, and no RH-alone convergence of a prescribed fixed-order window.

## 6. Variable order: an exact contour identity and a missing weighted estimate

Fixed α imposes a fixed ceiling. One can instead ask about α_N→∞. Set L=logN and α_N=ε_N L, with ε_N→0 but ε_NL→∞; a natural scale suggested by the audited Báez-Duarte argument is ε_N=c/loglogN, c sufficiently large. Pointwise in u=logn≪L,

\[
 (1-u/L)^{\alpha_N}
 =\exp\{-\epsilon_Nu-\epsilon_Nu^2/(2L)+O(\epsilon_Nu^3/L^2)\}.
\]

This resembles n^(−ε_N) only in a restricted range; it is **not** a norm estimate or a global coefficientwise approximation through n=N.

For α>0 and c>max(0,1−Re(s)), the logarithmic Perron identity is

\[
 V_{N,\alpha}(s)=\frac{\Gamma(\alpha+1)}{2\pi iL^\alpha}
 \int_{\Re w=c}\frac{e^{Lw}}{w^{\alpha+1}\zeta(s+w)}dw. \tag{7}
\]

Its justification is the inverse Laplace formula for(L−logn)_+^α/Γ(α+1), absolute convergence of1/ζ(s+w) on the initial line, and integrability of|w|^(−α−1). At n=N the inverse Laplace value is0 for α>0. The branch of Logw is principal on Re(w)>0. This is an exact initial-line formula, not a contour shift across zeros.

The phase Lw−(α+1)Logw has a saddle near w=(α+1)/L≈ε_N, width√α/L. Formal moment expansion suggests the target1/ζ(s+ε_N); its first correction involves−ε_N(1/ζ)''(s+ε_N)/(2L). This expansion is only motivation until contour tails and derivative growth are bounded uniformly in height.

A precise sufficient missing estimate is

\[
 \int_{\mathbb R}\frac{|\zeta(s)|^2}{|s|^{2q}}
 \left|V_{N,\alpha_N}(s)-\frac1{\zeta(s+\epsilon_N)}\right|^2dt
 \longrightarrow0,\qquad s=1/2+it. \tag{8}
\]

Together with the separately audited RH-conditional limit ζ(s)/ζ(s+ε_N)→1 in the same weighted L² space, this would yield prescribed-array convergence **under RH**. The needed contour/saddle lemma must control the neighborhood of the critical zeros, uniform reciprocal-zeta growth as ε_N shrinks, and the full t-integral. No such estimate is proved here. Increasing α_N removes the fixed finite multiplicity ceiling from this particular necessary argument; it does not by itself establish convergence or any converse theorem.

## Primary-source provenance and priority limits

* Wei–Wu2022, PAPER-C105, Proposition1.9 and proof, supplies the established qualitative α1,q1 necessary-simplicity result. The fixed-q extension is already reconstructed in `audits/adversarial_reviews/weighted_selberg_round2.md`; the present scalar-coefficient argument reuses that exact lemma.
* Shōta Inoue, *Relations among Some Conjectures on the Möbius Function and the Riemann Zeta-Function*, arXiv1705.00853v2,22June2017: actual primary Theorem1 p3, Lemma6 and proof pp13–14 inspected. It proves, underRH, a multiplicity ceiling m<β+1 from a little-o √x(logx)^β bound on fixed-order **arithmetic** Riesz means M_τ(x)=Γ(τ+1)⁻¹Σμ(n)(1−n/x)^τ. Its Mellin kernel is Γ(s)/[ζ(s)Γ(1+τ+s)], unlike(5). It demonstrates clear prior art for the pole-order/Abelian mechanism; neither its τ nor its bound exponent β should be silently identified with this logarithmic window's α.
* G.H.Hardy and Marcel Riesz, *The General Theory of Dirichlet's Series* (1915), PAPER-M002: the actual Cornell facsimile was inspected at printed pp21–23 and49–51. The positive real order κ is explicitly allowed in the first-kind definition p21; p23 names the first-kind means with λ_n=logn **logarithmic** means, and the second-kind means **arithmetic** means. Theorem39 and Lemma10 p50, with shifted formula(2) p51, give the inverse-Laplace kernel used in(7). Theorem40 p51 instead gives the Gamma-ratio kernel for the second kind. We apply the first formula only on an absolutely convergent initial line, not its more delicate continued-region extension. Logarithmic Riesz summability is not the Riesz1916 entire-function criterion for RH; those are distinct constructions.
* The finite polynomial source background and precise dependence of prior constants are recorded in PAPER-E010 and `unit_circle_scalar_window_round3.md`. No discovery-priority claim is made for any elementary extension above.
