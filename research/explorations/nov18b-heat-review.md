# Checking the logarithmic heat bound and simplifying the lateral barrier

**Review status.** I checked the argument at revision [268f899](https://github.com/GettysburgResearch/riemann/tree/268f89935d6c072ad6d48a34c748ebdea8549cb7), reproduced its exact arithmetic, and compared the quoted estimates with their primary statements. My principal candidate for independent review is the finite-strip inequality (4) below. Its exact-verification specialization gives the following implication. For every fixed $b>92791/36570=2.5373530216\ldots$, there is an absolute height $H_*(b)$ such that verification of RH through $H\ge H_*(b)$ gives $\Lambda\le b/\log H$ in the Polymath normalization. This version uses the externally established zeta zero-free half-plane $\Re s>7/8$. The unconditional subconvexity calculation alone suffices for every $b>4911678521/1933561194=2.5402239847\ldots$. Neither argument evaluates its starting height. Both are research proofs awaiting external review. [Forward estimate](nov18b-heat-forward.md) · [Strip improvement](nov18b-heat-seven-eighths.md) · [External theorem and independent build](nov18b-quasi-rh-source.md) · [Polymath15, Theorems 1.2 and 1.5](https://arxiv.org/abs/1904.12438)

## The numerical thresholds

In the notation $u=t/4$, $T=x/2$, $c=u\log(T/(2\pi))$, put
\[
 P_c(\sigma)=\frac{(c+1/2-\sigma)^2}{4c}.
\]
I matched the ten rational pieces and breakpoints of the supplied checker to Theorem 2.4 of Trudgian and Yang. Convex interpolation from $\sigma=9/10$ to $\mu(1)=0$ gives the eleventh piece. At $c=397/625$ the exact minimum of $P_c-m$ is $2088301341/60181133522500>1/30000$, as reported by the checker. At an interior contact with a piece $m(\sigma)=(A-B\sigma)/D$, the stationary abscissa is $\sigma=1/2+c(1-2B/D)$. At $c_* =4911678521/(4\cdot1933561194)$ the second source piece attains zero at that interior point. Clipping the stationary abscissae to each of the other ten intervals gives **strictly positive** rational gaps. Because $P_c$ is strictly increasing in $c>1/2$ throughout $1/2\le\sigma\le1$, this gives the strict threshold above. One needs a strict inequality on $b$ to absorb $\log(4\pi)$ and the analytic error powers. [Source coefficients](https://arxiv.org/abs/2306.05599) · [Replay](nov18b-heat-growth.py)

For $a=3/8$, the refined proof takes the growth majorant on $0\le r\le a$ to be the larger of $k_1(b_1-r)$ and $k_2(a-r)$ with $k_1=3/7$, $b_1=13/36$, $k_2=37936/92791$. Both pieces are active. Completing the square gives $r-c+2\sqrt{ck(b'-r)}\le b'-(1-k)c$. The larger constraint at the threshold is $c>a/(1-k_2)=92791/146280$. The saddle is then a fixed positive distance inside the zero-free half-plane, with $\zeta$ and its reciprocal of subpower size. It follows by the positive/negative half-wave proof that the high zeros are simple and on the real axis for any fixed $t\log x$ strictly above $92791/36570$ at sufficiently large height. For the line itself, it is the **real** logarithmic derivative of the positive half-wave that controls the rate of change of its argument. For the adjacent strip it controls the strict inequality of the two opposing wave moduli. The triangle estimate on the full Gaussian deals with the remaining real displacements. [Stationary argument](nov18b-heat-seven-eighths.md) · [Unbounded $t\log x$ range, Theorem 1.5](https://arxiv.org/abs/1904.12438)

## One grid suffices for the finite-height implication

Here the finite-height premise simplifies the original lateral proof. Only Fujii's second increment moment is needed. The following reduction works for any fixed proposed high-ray constant $b>0$ for which high reality is available above a strictly smaller constant. The input is that all nontrivial zeta zeros through $H$ satisfy RH. Put $X=H/2$, $L=\log X$, $t_0=b/\log H$. Choose $T$ in $[X,3X/2]$. For any fixed large $R$ we can choose $T$ such that
\[
  N(T+d)-N(T)-dL/(2\pi)=O_R(L^{2/5}) \qquad (|d|\le R+3).        \tag{1}
\]
Indeed place a grid of mesh $L^{-3/5}$ on the indicated interval, including both endpoints and zero. At fixed $d$, the second moment in $T$, divided by $X$, is $O_R(\log^2(2+L))$. This follows from Rodgers's formulation of Fujii's theorem, Stirling in Riemann–von Mangoldt, and subdivision into a bounded number of intervals of length at most one. Markov's inequality and the $O_R(L^{3/5})$ grid points cost $O_R(L^{-1/5}\log^2(2+L))$ in relative measure. Monotonicity fills in the gaps with $O(L^{2/5})$ error. Every zero in this enlarged window has horizontal displacement exactly zero by the finite-height premise. The band lies strictly below $H$ for all large $H$. [Rodgers, Theorem 2.2](https://arxiv.org/abs/1404.3080)

Fix $\kappa=\min(1,\sqrt b/4)>0$ and $h_0=\kappa L^{-1/2}$. For an arbitrarily small fixed $\epsilon>0$, any fixed $d_0>0$ and any fixed $M$, (1) gives
\[
 \left|\frac{\xi'}{\xi}(1/2+r+iv)-L/2\right|\le \epsilon L
       \quad\left(d_0h_0\le r\le M,\quad T-1\le v\le T+2\right).  \tag{2}
\]
To check this, subtract the logarithmic derivative at $1/2+2+iv$ and use its absolutely convergent difference of zero-pole sums. The terms beyond $[T-R-3,T+R+3]$ contribute $O_M(L/R)$ by the ordinary unit interval count. The near terms have actual real displacement zero. Integration by parts against (1) replaces the near sum by the continuous density $L/(2\pi)$ with error $O_{M,R}(L^{2/5}(1+1/r))=O_{M,R,d_0,\kappa}(L^{9/10})$. Indeed the $L^1$ norm of the derivative of $1/(r+iz)$ on the real axis is $\pi/r$. The full-line integrals of the two subtracted kernels cancel. Stirling and the absolutely convergent logarithmic derivative at the anchor give $L/2+O(1)$. Choose $R$ first and then $H$. One may widen the $v$ window by any fixed amount by increasing the margin in (1). On the same slab the modulus $|\xi(1/2+r+iv)|$ increases with $r\ge0$: near factors have zero displacement and pairs at distant heights satisfy $|a|<|v-\gamma|$, so their squared distance products increase in $r^2$. Absolute convergence over full symmetric orbits justifies the comparison. [Hadamard calculation](nov18b-heat-local-density.md)

Here is how (2) supplies Polymath's complete time interval. While $0<u\le h_0/L$, the needed early region has physical displacement $y\ge h_0$. The positive stationary point is near $s+h$, $h=uL$, where $Y=y+h\ge h_0$. Use the local segment of length $Y/2$ in the [early-time saddle proof](nov18b-heat-barrier.md). Cauchy's estimate on a disk of radius comparable to $Y$ bounds $(\log\xi)''$ by $O(\epsilon L/Y)$. The tails cost $\exp(-cY^2/u)$ with $Y^2/u\ge \kappa\sqrt L$ and the reflected saddle loses $\exp(-yL+O(\epsilon yL+\epsilon^2hL))$. These bounds, together with the central modulus comparison and the far Gaussian growth bound in that proof, prove exclusion uniformly down to $u=0$, where physical RH applies directly.

For $h_0/L\le u\le t_0/4$, use the [positive-time local saddle argument](nov18b-heat-local-density.md) on the same slab. Its small parameter is $(uL^2)^{-1}\le(\kappa\sqrt L)^{-1}$. All applications of its source bound lie in (2), with $r\ge d_0h$ or $r\ge d_0(h+y)$; fixed enlargements in the imaginary direction are permitted. The full Gaussian excludes $y\ge h/20$ and the phase derivative excludes $0<y\le h/20$. One can restrict to $h\le0.7$ using the unconditional forward estimate for larger $h$. Thus the slab has no off-axis heat zeros at the required late times. In Polymath coordinates it contains $2T\le x\le 2T+1$. At early times the lower edge in their criterion satisfies
\[
 \tfrac12\sqrt{y_0^2+2(t_0-t)}\ \ge\
 (\sqrt{b/2}+o(1))L^{-1/2}>h_0
\]
because $t\le 4h_0/L$. Its other two hypotheses follow from $T\le H$ and the assumed high-ray bound at $t_0$. Taking $y_0\downarrow0$ gives $\Lambda\le t_0$. This supplies a proof of the lateral reduction independent of the proposed exceptional heat-zero multiplicity estimate and of the Selberg–Jutila zero-density input. It retains the saddle estimates and leaves their absolute starting heights unevaluated. [Polymath15, Theorem 1.2 and §10](https://arxiv.org/abs/1904.12438)

## Quantitative version with a finite observed strip

Put
\[
 D(H)=\max_{0<\Im\rho\le H}|\Re\rho-1/2|
\]
over all nontrivial zeta zeros. The same analysis gives the unconditional, finite-height inequality
\[
                \boxed{\ \Lambda\le b/\log H+2D(H)^2\ },              \tag{3}
\]
for every fixed $b>92791/36570$ and all sufficiently large $H$. The verification-height implication is its specialization to $D(H)=0$. In particular, a positive $\Lambda>b/\log H$ would require a zero below $H$ displaced by at least $\sqrt{(\Lambda-b/\log H)/2}$. As an existential implication for fixed zeta, a statement about verification through all sufficiently large heights can become vacuous after a first counterexample. In (3) the ordinate and the measured width both enter, and the starting height is chosen from the analytic estimates independently of detecting any counterexample. Effectivizing this argument at the presently verified height would require tracking its constants and checking their sizes.

For the proof retain the one-grid event (1) and discard in addition every $T$ within $R+3$ of a zero with $|a|>L^{-3/5}$. Selberg–Jutila density bounds the extra relative measure by $O_R(L\exp(-c L^{2/5}))$ after reflection. Every remaining near pole therefore has $|a|\le L^{-3/5}=o(h_0)$. Its reflected pair contributes to the difference between the actual and projected Cauchy kernels an error bounded by $2a^2/|r+i(v-\gamma)|^3$, uniformly for $r\ge d_0 h_0$. On dyadic intervals $|v-\gamma|\le r$ and $2^{j-1}r<|v-\gamma|\le2^j r$, the count from (1) is $O_R(2^j rL+L^{2/5})$. The total near-pole error is consequently
\[
 O_R\bigl(L^{-6/5}(L/r^2+L^{2/5}/r^3)\bigr)=o(L).
\]
The anchor $r=2$ obeys the same estimate. For the unprotected central core, the near paired squared distance factor is a convex quadratic in $r^2$, and has its maximum on $|r|\le r_0$ at an endpoint when $r_0^2\ge2a^2$. This holds for each needed $r_0\ge c h_0$. Distant pairs have $|v-\gamma|>|a|$. These two comparisons restore both (2) and the central-core upper bound used by the stationary estimate. Thus the intermediate-time lateral slab and high canopy are available without the finite-height premise. In the initial condition of Polymath's Theorem 1.2 take $y_0>2D(H)$ and then decrease $y_0$ to $2D(H)$. There are admissible values since the known strip gives $2D(H)\le3/4$. Its conclusion gives (3). If using the older subconvexity constant, the ordinary zero-free line $\Re s=1$ and compactness of the finite zero set suffice for the strict inequality $2D(H)<1$. [Rodgers, Theorem 2.4](https://arxiv.org/abs/1404.3080) · [Paired kernel and core estimates](nov18b-heat-local-density.md) · [Polymath's canopy criterion](https://arxiv.org/abs/1904.12438)

One can keep the dependence of the high canopy on the observed width. With $a=3/8$, $k=54855/92791$ and every fixed $\eta>0$, the sharper result is
\[
 \boxed{\ \Lambda\ \le\ 2D(H)^2+
         \frac{\,4(a-D(H))/k+\eta\,}{\log H}\ }\qquad(H\ge H_*(\eta)).   \tag{4}
\]
Choose $t_0$ equal to the second term of (4) and use $\kappa=\min(1,\sqrt{\eta}/4)$ in the slab construction. The early lower edge still exceeds $h_0$ and the largest required time is bounded by a fixed multiple of $1/\log H$. For every high $x\ge2T\ge H$ its heat variable satisfies
\[
 c=\tfrac14 t_0\log(x/(4\pi))\ \ge\ (a-D(H))/k+\eta/5
\]
for sufficiently large $H$. For $c$ in a compact interval up to $a/k$, the high-wave exponent comparison gives upper edge $a-kc\le D(H)-k\eta/5$. Above $a/k$, the two affine comparison lines of the same argument are both negative. To check uniformity at their common boundary with the previous range, consider $0\le D\le a$, $c\ge(a-D)/k+\eta/5$ in a fixed compact $c$-interval. The comparison at the target displacement $D$ is strictly favorable throughout: when $c=a/k$ the inequality forces $D\ge k\eta/5$, and when $D=0$ it forces $c\ge a/k+\eta/5$. By continuity and compactness one can choose the saddle margins uniformly, using the two-half-wave reality argument on a fixed neighborhood whenever $D$ approaches zero. Larger $c$ falls under Polymath's Theorem 1.5. Consequently there are no high zeros with positive physical displacement $\ge y_0/2$ for $y_0>2D(H)$. The same initial and intermediate-time arguments prove (4). The full $7/8$ input enters the moving edge in this formula. [High-wave envelope, equation (1)](nov18b-heat-seven-eighths.md)

## Negative time and remaining review points

The arithmetic calculation for strictly negative time checks against the two halves of the balanced approximate functional equation. At displacement $bh$, $0<b<1$, with $h=F/L$, their normalized log-amplitudes at $q=\log n/L$ have respective leading terms $F((1-b)q-q^2)$ and $F((1+b)q-q^2-b)$. The first saddle is $q=(1-b)/2$ strictly below the truncation endpoint. The second loses $b^2F/4$ relative to the first. Dyadic maximal fourth moments for Dirichlet polynomials of length $O(\sqrt X)$ justify the truncation with polynomial logarithmic cost; $F\ge L^\nu$ absorbs that cost. The second moment of the fixed polynomial on the first saddle really has scale $XL e^{(1-b)^2F/2}/\sqrt F$. For the conversion to a zero count the weaker measure $XL^{-C}$ is sufficient, because each root can cover at most $2Kh$ of the retained heights. [Negative-time edge proof](nov18b-heat-negative-edge.md)

The analytic conversion still rests on the inverse-Gaussian saddle and the local continuation argument in the [gap proof](nov18b-heat-negative.md). The normal-family step can be made quantitative: if a holomorphic function is bounded by $M$ on a fixed rescaled rectangle and by $\delta$ on an interior disk, its norm on an interior compact connected to the disk is at most $M^{1-\omega}\delta^\omega$ for a fixed $\omega>0$ by harmonic measure (or by a finite chain of three-circle inequalities). The disk factorization and positive pair sum are needed to establish the uniform $M$ before applying this step. The negative-time result allows $t$ to approach zero through negative values while the ordinate tends to infinity. It supplies no counterexample at $t=0$. Establishing all-real zeros at every positive time, or ruling out a single time-zero defect independently, remains open.
