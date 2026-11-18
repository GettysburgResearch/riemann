# The rooted CUE moment window, its first correction, and an all-rank positivity barrier

18 November 2026. This adjudication is entirely within random matrix theory. The director read the two independent rank-two proofs, their third finite-endpoint review, both independent higher-rank reconstructions, and the finite/continuum certificate proofs and source code. The director also implemented a separate exact fourth-cumulant matrix calculation. No arithmetic moment range is extended here. The RH arithmetic input remains the finite window rb<1/2, whereas the intrinsic matrix window below is rb≤1. Publication priority has not been established.

## Measure and exact complementary determinant

For rank J≥1 fixed, give Haar U(N) and a selected eigenvalue label global joint probability proportional to `|Z'_U(theta_root)|^(2(J−1))`. Include that root after rotating it to angle zero. The free N−1 angles have Vandermonde squared times `prod|1−z|^(2J)`. Thus their projection is the subspace of polynomials divisible by (z−1)^J inside Fourier degrees 0 through N+J−2. Its ambient dimension is n=N+J−1; the J-dimensional complement consists of discrete polynomial coefficient vectors of degrees 0 through J−1. This is the HKO (2.2)–(2.8) tilt. It is not Haar first followed by a within-matrix normalization of root weights.

For J=2 use negative cosine and sine bands, with 0<a<b<1,

```text
C_N = −sum_(aN<k≤bN) (1/k) sum_ell cos(k theta_ell),
S_N = −sum_(aN<k≤bN) (1/k) sum_ell sin(k theta_ell).
```

Let F=z_c f_c+z_s f_s be the free-point multiplier, E the n=N+1 Fourier space, A=T_n(exp F), and U its two removed orthonormal coefficient vectors. Jacobi's complementary minor identity gives exactly, as a formal Taylor identity at zero,

```text
E exp(z_c C_N+z_s S_N)
 = exp(−H_N z_c) det(A) det(U* A^−1 U),
H_N=sum_(aN<k≤bN)1/k.
```

The root factor is essential. The ordinary U(n) determinant is an auxiliary factor, not the N−1 free-point law. Schur orthogonality, or the precisely matched Diaconis–Evans trace theorem, gives its Gaussian Wick coefficients whenever the common balanced positive/negative weighted degree is at most n. In a word of degree r this only requires r K_N/2≤n, K_N the largest band frequency. This factor therefore remains stable at the first correction considered below.

## Why the separate signed totals control the window

Tag the Fourier sources before specializing the two real variables. For a word let P,Q be its positive and absolute negative frequency totals. In the inverse's formal Neumann expansion, each matrix step groups some tagged frequencies. A path that visits both forbidden regions must traverse between at most −1 and at least n, requiring n+1 frequency in one direction. If P,Q≤n, inclusion–exclusion of the two boundaries is therefore exact coefficientwise. The inverse equals left half-line inverse plus right half-line inverse minus the whole-line inverse for that coefficient. This does not invoke a strong Szegő theorem for an N-dependent symbol outside its hypotheses.

Half-line triangular factorization expresses the left inverse as T(exp(−F_+))T(exp(−F_-)), and reverses their order on the right. Compressing onto the removed constant/linear vectors gives an **oriented** sum from Q to n−P. If P+Q>n while both individual totals remain at most n, the sum over the gap is negative. Replacing it by zero would give incorrect mixed coefficients.

Put ell=n−P−Q, D=P−Q. The exact finite matrix entries are

```text
D00=ell/n,
D01=−sqrt(3) ell D/[n sqrt(n²−1)],  D10=−D01,
D11=ell(ell²−1−3D²)/[n(n²−1)].
```

They remain valid at P=n or Q=n. For example, the tagged coefficient of st in T_n(exp(s z^n+t z^−1))^−1 is −T_n(z^(n−1)); its compression exactly equals the endpoint formula at P=n,Q=1. A pure total equal to n gives zero, and a pure total above n has no actual endpoints. The finite upper index N and ambient dimension N+1 must not be interchanged.

## Joint quartic and exact finite-size surrogate

Set H=log(b/a), d=b−a, J2=(b²−a²)/2, J3=(b³−a³)/3. Through every fixed total degree r with rb≤1, the limiting mixed moments are the factorial-weighted coefficients of

```text
F_form(z_c,z_s)
 = exp[H z_c+H(z_c²+z_s²)/4]
   [(1−d z_c)^4+2J3 z_c(1−d z_c)−3J2² z_s²].
```

The equality is only a finite Taylor window for a fixed positive band. The sine term is required: it reproduces variance H/2−6J2² and the mixed cubic (Delta3−6Delta1)Delta2², agreeing with the earlier independent signed HLZ calculation in its smaller domain.

For clarity the exact finite surrogate replaces H,d,Jj by

```text
H_N=sum 1/k, d_N=(number of frequencies)/n,
Jj_N=sum k^(j−1)/n^j, epsilon=1/n², L_c=1−d_N z_c,
```

and replaces the bracket by

```text
[L_c^4+2J3_N z_c L_c−3J2_N² z_s²−epsilon L_c²]/(1−epsilon).
```

It agrees exactly through degree r whenever r K_N≤n, and coefficientwise under the stronger information P,Q≤n. The proof sums the polynomial compression against the two formal compound-Poisson coefficient families of exp(−F_+) and exp(−F_-). Their total masses supply exp(2H_N z_c) to the two-by-two determinant; the root removes exp(H_N z_c), and the base Wick factor supplies the quadratic exponential. Opposite off-diagonal entries must be retained for a sine source. Their determinant cancels all extra z_c z_s² and z_c² z_s² terms. When r b=1 the finite support inequality still holds, so the limiting boundary is included.

## First new frequency chamber

Suppose (r−1)b≤1<r b. Every mixed-sign word still has P,Q≤n for large N. Only all-same-sign words whose total exceeds n depart from the polynomial continuation. At their first departure, the complementary determinant differs by the trace of that missing coefficient because its constant matrix is I and all lower degrees agree. For J=2 this trace continuation is

```text
A_n(p)=2(p−n)(p²+n p−n²+1)/[n(n²−1)],
A(t)=2−4t+2t³=2(t−1)(t²+t−1).
```

Consequently the first cosine raw moment minus its formal value is

```text
−2^(1−r) I_r,
I_r=integral_([a,b]^r, sum x_i>1) A(sum x_i) prod_i dx_i/x_i >0.
```

For the joint generating series the homogeneous difference is

```text
−[(z_c−i z_s)^r+(z_c+i z_s)^r] I_r/(2^r r!).
```

The cosine correction is strictly negative. A mixed ray's correction can change sign or vanish; no universal joint sign is asserted. The fourth moment first departs when 1/4<b≤1/3, and the fifth when 1/5<b≤1/4. These are intrinsic matrix ranges, not new arithmetic theorems. Later chambers require the full path constraints, not repetition of the first correction.

## Independent exact finite and continuum checks

At N=40, n=41, with frequencies 9,10,11, the 81 ordered four-tuples split into 50 below, 16 equal to, and 15 above the threshold. A full rational projection-determinant program and the director's independent cumulant formula give

```text
direct fourth moment = 483952530159221/9042666599736000,
formal fourth moment = 30253355007779/565166662483500,
difference           = −3384187/302541624000.
```

The difference agrees exactly with the first-crossing sum. Moments through three agree exactly. The director uses `kappa4=Tr(PF4)−4Tr(PF1PF3)−3Tr(PF2PF2)+12Tr(PF1PF1PF2)−6Tr((PF1)^4)`, then converts cumulants to raw moments and adds the deterministic root to the mean only. The other program uses the matrix-series inverse recurrence, providing an independent algebraic check.

For the partial-crossing continuum band (0.22,0.28), r=4, the correction is enclosed near −1.116093794622113479066e−5 with exact rational width below 2.63e−27. Substituting y_i=b−x_i gives a simplex of radius 2(b−a); inclusion–exclusion removes four single caps, while double-cap intersections have measure zero. A positive geometric-product expansion with explicit remainder and exact radial Dirichlet monomial integrals certifies the enclosure. An independent total-degree expansion in slack coordinates gives a narrower rational interval inside it and checks the Arb decimal endpoints exactly.

When r a≥1 the whole cube crosses. Writing m_j=(b^j−a^j)/j, expansion of the sum's first and third powers gives, for r≥3,

```text
I_r=2H^r+(2r m3−4r m1)H^(r−1)
    +6r(r−1)m2 m1 H^(r−2)
    +2r(r−1)(r−2)m1³ H^(r−3).
```

At (a,b)=(0.26,0.32), r=4, the correction is approximately −0.0001099788872477072953195452, with the recorded 160-bit interval. These certificates are RMT calculations. Floating benchmarks at N=100 and the inclusive N=99 endpoint test supplement the exact proof but provide no arithmetic result or certified convergence rate.

## Every fixed integer tilt rank has an extrapolation barrier

For fixed J, the removed discrete basis converges to shifted orthonormal Legendre polynomials `u_j(t)=sqrt(2j+1)P_j(2t−1)`, 0≤j<J, on [0,1]. The same coefficientwise proof gives the cosine formal window

```text
exp[(J−1)H z+H z²/4] P_J(z),   r b≤1,
P_J(z)=det B_J(z),
B_J(z)=E_form integral_q^(1−p) u(t+p−q)u(t)^T dt.
```

The two normalized formal frequency sums p,q have independent compound-Poisson cumulants `(z/2)m_k`. This notation computes polynomial moments; it does not identify the oriented matrix as a positive compression outside the source window. Each entry has degree at most i+j+1 in p,q, hence polynomial degree at most i+j+1 in z. Thus deg P_J≤J² and P_J(0)=1. Swapping p,q transposes the matrix and reflection gives parity. With identical real cosine intensities B_J is real symmetric, and opposite parity blocks vanish.

Let d=m1>0. The universal entries indexed 0,1,2 satisfy, with l=1−d z,

```text
B00=l,
B11=l³+2m3 z,
B02=B20=sqrt(5)/2 [l³−l+6l z m2−4z m3].
```

For J=3, P_3(1/d)=−40(m3/d)³<0. For **every J≥3**, the 0,2 principal minor at 1/d has determinant −20(m3/d)²<0. Since B_J(0)=I, continuity of its least eigenvalue forces det B_J(z*)=0 for some 0<z*<1/d. For J=1,2 the determinant vanishes at 1/d directly. This proves a positive real zero of the formal scalar MGF for every fixed integer tilt rank.

The entire exponential-polynomial series has a signed Gaussian-polynomial inverse. Its absolute Gaussian moments dominate any putative positive measure with all the formal moments, giving finite exponential moments by the monotone cosh series. Such a measure cannot have the positive-real MGF zero. There is a finite square witness even if the determinant only touches zero: take the first positive zero z*, and let Q_M be the degree-M Taylor polynomial of exp(z* X/2). Gaussian domination gives L(Q_M²)→0 and L(Q_M)→F_form(z*/2)>0. Hence `L((Q_M−L(Q_M))²)` tends to a negative number. A sufficiently large finite Hankel test therefore fails. None of these witnesses contradicts the true finite window.

The first correction also has a rank-dependent sign. The pure-sign trace continuation is

```text
A_J(t)=sum_(j<J) integral_0^(1−t) u_j(s+t)u_j(s) ds.
```

For t>1, Christoffel–Darboux and Legendre parity show its sign is (−1)^J on the reversed interval: the two Legendre arguments lie on opposite outer half-lines. Therefore the first cosine raw-moment discrepancy has sign (−1)^(J+1). Rank three has `A_3(t)=−6t^5+12t³−9t+3<0` for t>1, and an exact finite rank-three example gives correction +9/160. This is a mathematical explanation of why the missing corrections cannot be uniformly assigned one sign across all root tilts.

## Provenance, limitations and next arithmetic step

The HKO primary density supplies the tilt. Diaconis–Evans supplies the matched ordinary trace Wick range. Bump–Diaconis, Borodin–Okounkov and Basor–Widom supply the Toeplitz-minor and factorization lineage; a fixed-symbol asymptotic is not silently substituted for this moving-frequency coefficient proof. Relevant primary passages were inspected by the independent reviewers, with the original-source boundaries recorded. No priority claim follows from the calculation.

For the arithmetic fourth moment with 1/8<b<1/6, the mixed D³ conjugate(D) and D² conjugate(D)² arms already fit the available HLZ length. Only the pure D⁴ versus 1 arm exceeds the half-power range. Thus a precise next target is its one-sided long discrete twisted estimate, not a claim that the entire general HLZ theorem must be extended. The independent arithmetic reduction and its unresolved reflected saddle/character sum are documented separately; the intrinsic matrix calculation does not supply that estimate.

[First rank-two proof](prime84_cue_moment_window.md) · [Independent proof](weighted84_cue_moment_window_review.md) · [Endpoint and source QA](uniform86_cue_window_adjudication_input.md) · [Finite and continuum certificate](prime89_first_chamber_certificate.md) · [Independent continuum certificate](uniform92_first_chamber_certificate_review.md) · [Rank-three and general-rank proof](geometry93_rank_three_barrier.md) · [Independent general-rank reconstruction](analytic93_rank_three_skeptic.md) · [Director exact fourth calculation](../../experiments/results/director_round13_cue_fourth.json)
