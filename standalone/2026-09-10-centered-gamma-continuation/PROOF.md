# Centered gamma continuation: variance-scale xi approximation and a critical-strip defect

Date: 2026-09-10. Status: **PROPOSED component proofs and computer-assisted finite counterexamples; independent review required. RH is not proved.** This continuation uses PR #849 at `11a12b8ceb7db98c7961a5cebf3870b2f31dfa79`. Its original ten files are not changed. Local CG labels are not canonical acceptance IDs.

The positive outcome is a prescribed compactly supported reciprocal approximation with full-strip error O(N^-3), and an explicit leading error expressed by xi on the safe line Re(s)=9/2. The negative outcome is a rigorously enclosed nonreal zero *inside* the critical strip during the original gamma interpolation. Thus literal critical-strip preservation along every interpolation time is false. Neither result settles the cofinal confinement problem.

## 1. Source, target and the two families

Let G_n be independent shape-two, rate-one gamma variables, and retain

    X_N=sum_(n<=N) G_n/n^2,  X=sum_(n>=1) G_n/n^2.

Write f_N and f for their densities, extended by zero on the negative real axis when they represent probability laws. For positive x the source has the holomorphic representation

    f(x)=sum_(n>=1)(4n^4 x-6n^2) exp(-n^2 x),
    f(pi^2/x)=(x/pi)^(5/2) f(x).                         (1)

The series is locally normally convergent on Re(x)>0. The reciprocal identity extends there, using its principal power. The Biane--Pitman--Yor gamma/xi representation and Jacobi transformation are classical imports; the parent reconstructs our scaling:

    E (sqrt(X/pi))^s=2 xi(s),
    h(t)=sqrt(f(pi exp(2t))f(pi exp(-2t)))=phi(t)/pi,
    Phi(z)=integral h(t) exp(izt)dt / integral h(t)dt
          =Xi(z)/Xi(0),  Xi(z)=xi(1/2+iz).             (2)

In particular f(x)>0 for x>0. The entire completion has xi(0)=xi(1)=1/2.

Define the exact omitted-tail mean, variance and third power sum

    tau_N=2 sum_(n>N) n^-2 = pi^2/3-2 sum_(n<=N)n^-2,
    v_N=2 sum_(n>N) n^-4,
    w_N=2 sum_(n>N) n^-6.                              (3)

Integral comparison gives

    2/(N+1)<=tau_N<=2/N,
    2/[3(N+1)^3]<=v_N<=2/(3N^3),
    2/[5(N+1)^5]<=w_N<=2/(5N^5).                        (4)

The raw reciprocal family F_N uses h_N(t)=sqrt(f_N(x)f_N(y)), where x=pi exp(2t), y=pi exp(-2t). The **new, mean-centered** family uses the density of X_N+tau_N:

    g_N(x)=f_N(x-tau_N) for x>tau_N, and zero otherwise;
    hhat_N(t)=sqrt(g_N(x)g_N(y));
    Fhat_N(z)=integral hhat_N(t)exp(izt)dt / integral hhat_N(t)dt. (5)

This is a positive ordinary law, not a signed Richardson correction. Since tau_N<=3/2<pi, its reciprocal projection has nonempty support

    |t|<T_N=(1/2)log(pi/tau_N).                         (6)

Thus Fhat_N is entire of exponential type at most T_N, even, real on the real axis, and Fhat_N(0)=1. T_N=(log N)/2+O(1). This support statement concerns the density variable t, not a proved zero-free spectral window.

The raw N=1 family has the parent's Bessel/Sturm real-zero proof. **The new centered N=1 member is not that Bessel function. Its real-rootedness is not asserted.** Centering supplies an approximation tool, not an inherited spectral theorem.

## 2. CG1: an exact convergent tail-removal operator

Let the countable positive list alpha contain two copies of n^-2 for every n>N, and let e_k be its elementary symmetric functions, e_0=1. Then sum alpha=tau, sum alpha^2=v, sum alpha^3=w. For real x>tau,

    f_N(x)=sum_(k>=0) e_k f^(k)(x).                    (7)

The identity extends holomorphically to Re(x)>tau, and the series converges locally normally there. At a real center x>tau, choose tau<r<x for the Cauchy estimates below. Convergence on an arbitrary disk that crosses Re(x)=tau is NOT asserted. This is not a formal differential product applied without a domain.

**Proof.** For finite M>N, convolution gives

    f_N=product_(N<n<=M)(1+n^-2 d/dx)^2 f_M

on x>0, and hence as an identity between holomorphic continuations. On any disk inside Re(x)>0, f_M is uniformly bounded and converges normally to f. Indeed the parent's finite partial-fraction formula has B_(n,M)<=4 and |c_(n,M)|<=1/2+2n^2; its terms have a normally summable polynomial times exp(-n^2 Re x) majorant. Cauchy estimates give |f_M^(k)(x)|<=k! A_r/r^k, uniformly in M. Also e_k(N,M)<=tau^k/k!. Consequently the whole differential sum is dominated by A_r sum (tau/r)^k. Each fixed coefficient and derivative converges. Dominated passage to the limit proves (7), with no unresolved boundary distribution. QED.

### 2.1 Collision counting supplies the remainder, not a heuristic cumulant expansion

For every k, with absent negative factorial terms interpreted as zero,

    e_k=tau^k/k! -(v/2) tau^(k-2)/(k-2)! + d_k,
    0<=d_k<= (w/2) tau^(k-3)/(k-3)!
              +(v^2/8) tau^(k-4)/(k-4)!.              (8)

For k=0,1 take d_k=0. This follows from the first two Bonferroni bounds for the event that two entries in an ordered k-tuple coincide. The one-pair sum is binom(k,2)v tau^(k-2). Intersections of two pairs sharing an index contribute 3 binom(k,3)w tau^(k-3); disjoint pairs contribute 3 binom(k,4)v^2 tau^(k-4). Divide by k!. Finite positive truncation and monotone limits justify the countable version. Triple coincidences are not omitted or treated as independent events.

If A_r=max_(|z-x|=r)|f(z)| and q=tau/r<1, (7),(8) give the explicit complete remainder

    f_N(x)=f(x+tau)-(v/2)f''(x+tau)+R_N(x),
    |R_N(x)|<=A_r[3w/(r^3(1-q)^4)+3v^2/(r^4(1-q)^5)]. (9)

For example sum_(k>=3) k(k-1)(k-2)q^(k-3)=6/(1-q)^4. This pays every differential order, not a finite Taylor fit. The less precise but useful bound

    |f_N(x)-f(x+tau)|<= A_r v/[r^2(1-q)^3]             (10)

follows directly by a union bound for one collision. The actual random tail is therefore a translation to leading order, with a rigorously controlled variance correction.

## 3. A relative Cauchy estimate for the actual reciprocal source

There is an absolute finite C such that, with

    r(x)=min(1,x^2)/1000,
    max_(|z-x|<=r(x)) |f(z)| <= C f(x)                 (11)

for every x>0. Constants here and in the following asymptotic theorems are not numerically optimized or certified.

**Proof.** For real x>=pi and |z-x|<=1/100, the n=1 term of (1) gives f(x)>=(4x-6)e^-x, and the remaining normally convergent series bounds the complex numerator by a fixed multiple of this expression. The quotient is uniformly bounded as x tends to infinity; compact positive x completes that range. If 0<x<=pi and |z-x|<=r(x), then |z-x|<x/1000 and

    |pi^2/z-pi^2/x| <= pi^2/[1000(1-1/1000)] <1/100.

Use the holomorphic reciprocal identity (1). Its prefactor ratio (x/z)^(5/2) is uniformly bounded, and the transformed center pi^2/x is at least pi. The established large-center estimate proves (11). QED.

In particular every fixed derivative satisfies

    |f^(j)(x)|/f(x) <= C_j(1+x^(-2j)).                 (12)

No all-order uniform C_j is asserted. We use (11) for convergent sums and only finitely many instances of (12).

## 4. CG2: full-strip O(N^-3) approximation, with a sharper first correction

For every fixed R>=0 and nonnegative integer k,

    sup_(|Im z|<=R) |d_z^k(Fhat_N(z)-Phi(z))|=O_(R,k)(N^-3). (13)

The supremum includes all real frequencies. More precisely, define

    (D P)(z)=[(z^2+3/4-iz)P(z-4i)
               +(z^2+3/4+iz)P(z+4i)]/(16pi^2).        (14)

Then

    Fhat_N(z)=Phi(z)+v_N[D Phi(z)-Phi(z)D Phi(0)]
                     +O_(R,k)(w_N+v_N^2),             (15)

also after k spectral derivatives, uniformly on the whole strip. In particular the remainder in (15) is O_(R,k)(N^-5). The last expression means differentiation of the displayed leading functions and then a bound on the differentiated remainder.

These are absolute errors, not relative errors near small values or zeros. No zero-location assumption is used. The constants and a practical first usable N have not been evaluated.

### 4.1 Pointwise expansion where both reciprocal arguments are resolved

Put delta=tau_N^(1/4). On the region x,y>=delta, and for N sufficiently large, x-tau>=x/2 and r(x-tau)>=r(x)/4. Thus tau/r(x-tau)=O(tau^(1/2))<1/2 uniformly on this region. Apply (9) at x-tau and (11) at x; the segment x-tau stays inside the corresponding Cauchy disk. This gives

    g_N(x)=f(x)-(v/2)f''(x)+rho_N(x),
    |rho_N(x)|<=C f(x)[w(1+x^-6)+v^2(1+x^-8)].        (16)

The leading relative perturbation is O(v(1+x^-4)). At the least allowed x, it is O(v/tau)=O(N^-2), hence uniformly small. The two error terms in (16) are also uniformly small there, by (4). Taylor's formula for sqrt((1+a)(1+b)) on |a|,|b|<=1/2 now yields

    hhat_N(t)=h(t)-(v/4)h(t)[f''(x)/f(x)+f''(y)/f(y)] + eta_N(t),
    |eta_N(t)|<=C h(t){w(1+x^-6+y^-6)
                              +v^2(1+x^-8+y^-8)}.     (17)

The cross products are absorbed by a^2+b^2 and xy=pi^2. Quadratic remainders of the already small rho_N/f may be bounded by a constant times their first absolute powers. This accounts for the whole nonlinear geometric mean, not just its formal first variation.

### 4.2 The moving endpoint and both unbounded t tails

The parent proves f_N(x),f(x)<=4xe^-x. Hence globally

    h(t)<=4pi exp(-pi cosh(2t)),
    hhat_N(t)<=4pi exp(tau_N) exp(-pi cosh(2t)).        (18)

The second bound remains true when one of the shifted arguments is nonpositive: hhat_N is then zero. On the omitted region min(x,y)<delta, max(x,y)>pi^2/delta. Integrating (18), with any fixed weight exp(R|t|)(1+|t|^k) and any fixed polynomial in x,y, gives O(exp(-c/delta)) for a smaller positive c. By (4), this is smaller than every fixed power of 1/N. The same applies to the linear correction in (17), by (12). Thus neither the new compact-support endpoints nor a small-x tail is silently dropped.

Integrate (17) with the same weight on the remaining region. Every weighted integral of h times the displayed powers is finite by (18). Therefore the complete weighted L1 remainder is O_(R,k)(w+v^2). Dominated convergence gives positive normalization constants tending to Z=integral h. Dividing the Fourier transforms pays the normalizer correction as well. These arguments prove (13) and reduce (15) to an exact integration by parts.

### 4.3 The complete reciprocal variance correction is a linear spectral difference

Write h(t)=exp(5t/2)f(x). Direct differentiation, using evenness for y, gives

    h[f''(x)/f(x)+f''(y)/f(y)]
       ={cosh(4t)[h''+(45/4)h]+7 sinh(4t)h'}/(2pi^2). (19)

The apparent logarithmic-derivative squares combine into h''; no nonlinear term is omitted. The coefficient of v in (17) is therefore

    -{cosh(4t)[h''+(45/4)h]+7 sinh(4t)h'}/(8pi^2).

Two integrations by parts and the entire double-exponential tails turn its Fourier transform into (14) applied to the unnormalized transform. Specifically the two coefficients before substituting q=iz are

    (q+4)^2-7(q+4)+45/4 = q^2+q-3/4,
    (q-4)^2+7(q-4)+45/4 = q^2-q-3/4.

Normalization subtracts Phi(z)D Phi(0). The division has an additional O(v^2) remainder, already covered by (15). This proves CG2. For finitely many smaller N, enlargement of the finite constants extends the O bounds; that is not a numerical certificate for those constants.

For real z, Phi(z-4i)=xi(9/2+iz)/xi(1/2) and Phi(z+4i) is its conjugate. The leading error is consequently determined by values in an absolutely convergent Euler half-plane. D Phi(0)=3 Phi(4i)/(32pi^2). This identity does not give a sign for the error at unknown zeros.

### 4.4 CG3: the parent's auxiliary translation is now connected to the actual cascade

Let Phi_epsilon be the reciprocal projection of f(x+epsilon), normalized, as in the parent. The same proof using (10) instead of (9) gives

    F_N-Phi_(tau_N)=O_(R,k)(v_N).                     (20)

For fixed finite derivative order, (12),(18) justify differentiating Phi_epsilon near epsilon=0 under its complete integral. The parent's exact tangent is

    (A P)(z)=[(2iz-1)P(z-2i)-(2iz+1)P(z+2i)]/(8pi),
    F_N=Phi+tau_N[A Phi-Phi A Phi(0)]+O_(R,k)(tau_N^2). (21)

Thus the raw family itself improves from the old O(N^-1/2) estimate to O(N^-1), while positive mean-centering removes its leading translation and reaches the variance scale N^-3. This does not identify finite raw and centered zeros with each other.

## 5. CG4: two certified finite nonreal zeros

The complete Taylor-integral computation described in [CERTIFICATE.md](CERTIFICATE.md) gives exactly one simple zero in each radius-10^-12 disk centered at

    N=4:
    28.0555855384091825810295021076097455522309
       +2.6219979332686197954925378014004831147962 i;

    X_2+(7/10)G/9, with reciprocal projection:
    26.8135855368140614010181412691765400069731
       +0.4209949404628029929584207065487732398251 i.    (22)

The centers are exact terminating decimals, not definitions by numerical roots. The second law has rates 1,4,90/7. Its disk lies strictly inside 0<Im(z)<1/2. The first result upgrades the old N=4 scout to a computer-assisted proof. The second disproves a proposed invariant that would keep every nonreal approximant zero outside the critical band throughout every gamma step.

The proof encloses the defining integral and its first two derivatives, includes the whole time tail, and uses a third-derivative bound in Rouche's theorem. It does not call zeta, gamma, a floating eigensolver, or the parent's numerical code. The packet remains proposed pending independent inspection of the analytic certificate and implementation.

**These are zeros of changed finite laws, not zeros of xi.** The second is an interpolation-time result, not a nonreal zero asserted at an integer stage. Neither counterexample disproves eventual shrinking confinement along integer stages, or such a theorem for the new centered family.

A preceding non-directed scout suggests a real-pair collision near interpolation parameter 0.66. The completed proof does not locate that collision, provide an exhaustive rectangle census, or certify a continuous root trajectory. Only the two disks in (22) receive a root-count verdict. A local simple-real-root velocity being real does not exclude a collision; nor does it control boundary entry.

## 6. End-to-end consequence and the exact remaining research task

A sufficient closing theorem is: for some N_j->infinity, R_j->infinity and epsilon_j->0, every zero of Fhat_(N_j) in |Re z|<=R_j, |Im z|<=1 has |Im z|<=epsilon_j. By (13), a fixed off-real xi zero would force approximant zeros in a small off-real disk by Rouche, contradicting that confinement. Multiplicities cause no problem in this argument.

**This source-specific confinement theorem has not been proved.** Faster absolute approximation is not a substitute for it. Indeed at a fixed simple zero z0 of Phi, the implicit-function/Rouche argument and (15) give a nearby zero

    z_N=z0-v_N D Phi(z0)/Phi'(z0)+O(N^-5).              (23)

This holds whether z0 is real or nonreal. A hypothetical nonreal zero would persist just as faithfully. Multiple zeros require their own splitting analysis, not division by Phi'(z0).

The useful new attack is to separate the large deterministic translation from the small signed variance flow and study (19), rather than assume false strip invariance for the original interpolation. The safe-half-plane identity (14) makes its leading arithmetic coefficient explicit. A valid argument still needs quantitative control of multiple-zero splitting and boundary entry at increasing height, for the exact centered construction, not a generic positive even density.

No metric similarity, all-rank positivity, modular identity for finite stages, new xi zero-free region, or repaired Lean proof follows here. The unmodified infinite source and all tail budgets are retained. The results improve the construction and falsify a particular finishing mechanism without advertising an incomplete RH proof as complete.

## Sources and review boundaries

[P] PR #849, `11a12b8ceb7db98c7961a5cebf3870b2f31dfa79`, `standalone/2026-09-10-reciprocal-gamma-cascade/PROPOSAL.md`, blob `c324ba15d3f7f3e073b902042ec61c685b555f53`, 24,737 bytes. The supplied local file matches that remote blob. Its complete construction was read, not independently accepted by this continuation. Its original scout/checker was not used in accepting the new certificate.

[E1] P. Biane, J. Pitman, M. Yor, *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*, Berkeley technical report 569; arXiv:math/9912170. Proposition 1, especially (21),(24), and the shape-h gamma scaling in (6),(7) fix the imported law. Parsed text and the image of printed page 7 were inspected. https://statistics.berkeley.edu/sites/default/files/tech-reports/569.pdf

[E2] NIST DLMF 10.32.9 supplies the parent's Bessel integral: https://dlmf.nist.gov/10.32 . The seed's Sturm argument is inherited and is not used to certify (22).

Cauchy estimates, positive convolution, Bonferroni counting, Fourier integration by parts and Rouche's theorem are classical mechanisms, explicitly applied above. No external novelty or priority claim is made. Numerical certificate execution is not independent mathematical acceptance of CG1--CG4.
