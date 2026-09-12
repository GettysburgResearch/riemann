# BJR26 — complete complex response and the first certified local motion of the beta–Brownian homotopy

Date: 2026-09-13.
Status: **Proposed component proofs and bounded computer-assisted certificates. Independent mathematical and implementation review required. RH IS NOT PROVED.**
Scope: the unchanged fixed-point path of #876/#878. The new weighted norm controls the whole complex-response tail, not only a Laplace sup norm. A separate exact endpoint series certifies a local real zero velocity. No nondegenerate double collision, global no-birth theorem, nonpositive total production, or unbounded critical-line confinement is proved.

This is an add-only continuation of PR #878 at `e28fd6c04d315c5f31f37b2240a263cd2e0cfeaf`. The earlier 12-file packet is not edited. Its outside-strip zero–pole cancellation and its unsuccessful derivative scout remain historical results, not newly accepted global zero information.

## 1. Literal source and inherited estimates

Let k=5/2, c=pi/6, and let B~Beta(k,k), W=U^-2 with U uniform on [1,2]. Write mu_theta=(1-theta)Law(B)+theta Law(W), 0<=theta<=1. The unique nonnegative mean-one finite-second-moment fixed law is

    X_theta =_d C_theta (X_theta + X_theta'),

with independent children and ONE independent multiplier C_theta~mu_theta. Put S_theta=X_theta+X_theta', L_theta(t)=E exp(-tX_theta),

    M_theta(s)=E(c S_theta)^(s/2),
    H_theta(s)=[M_theta(s)+M_theta(1-s)]/[2(1+M_theta(1))].

All powers of positive real variables use their real logarithm. Parameter theta=1 is the Brownian endpoint, not the first iterate of the old branching algorithm.

The frozen source proofs provide, and the following arguments retain:

* X_0~Gamma(k, rate k), X_1=(6/pi^2)sum_{j>=1}E_j/j^2, and M_1=2xi, H_1=xi. The source identity is classical BPY [B].
* E X_theta=1, E X_theta^2=7/5, E X_theta^3=21(30+theta)/[5(50-theta)]. All fixed positive moments are uniformly finite.
* nu_0 <=_3 nu_theta <=_3 nu_1; in particular

      0<L_theta(t)<=L_g(t):=(1+t/k)^(-5/2), t>=0,
      E S_theta^(-5/2)<5/8.

* With the nonnegative Peano kernel

      kappa(v)=[E(W-v)_+^2-E(B-v)_+^2]/2,

  one has support [0,1], integral kappa=1/960, and 0<=kappa(v)<=v^(9/2).
* The response source and operator are

      A_theta(t)=E[S_theta^3 integral_0^1 kappa(v) exp(-tvS_theta) dv],
      (R_theta q)(t)=2 integral c0^3 L_theta(c0 t)q(c0 t) mu_theta(dc0).

  On ordinary C_b, ||R_theta||=(30+theta)/80 and the previously proposed response is

      -partial_theta L_theta(t)=t^3 Q_theta(t),
      Q_theta=sum_{j>=0}R_theta^j A_theta,
      Q_theta(0)=chi_theta=56/(50-theta)^2.

The ordering is based on the exact three-switch pattern of the B/W density difference and quadratic interpolation, not stochastic randomness of arithmetic. The endpoint normalization and these paper proofs remain proposed imports pending independent review. We strengthen the response's norm contract below and independently justify its analytic parameter realization.

Classical ingredients are beta integrals, gamma integration, the implicit/contraction theorem in a Banach space, Laguerre orthogonality, and Rouché/implicit functions. No external priority claim is made for these mechanisms.

## 2. A gamma-shaped norm that survives the ENTIRE response operator

Define

    g(t)=(1+t/k)^(-11/2),
    B_g={q continuous on [0,infinity): ||q||_g=sup |q(t)|/g(t)<infinity}.

This is a Banach space, isometric to C_b by division by g. It is not the parent's unweighted C_b space. Its decay condition is the essential extra information.

### Theorem BJR1

For every theta in [0,1],

    ||R_theta||_(B_g -> B_g) <= 2/3,
    0<=A_theta(t)<=11g(t),
    0<=Q_theta(t)<=33g(t).                                      (1)

Moreover, for every integer J>=0,

    0<=Q_theta(t)-sum_{j=0}^J R_theta^j A_theta(t)
      <=33 (2/3)^(J+1) g(t),  ALL t>=0.                         (2)

The norm bound 3 for the new inverse is not claimed to improve the parent's 80/49 bound in a different, unweighted space. It prices additional whole-tail decay.

### 2.1 Exact beta cancellation

Since L_theta<=L_g, compare R_theta with the positive operator obtained by replacing L_theta by L_g. The beta component obeys exactly

    2 E[B^3(1+xB)^(-8)] = (3/8)(1+x)^(-11/2), x>=0.            (3)

Indeed B^3 changes Beta(5/2,5/2) to Beta(11/2,5/2), with mass E B^3=3/16. The beta integral for total exponent 8 is (1+x)^(-11/2). Thus this part has weighted bound 3/8, including all t.

### 2.2 The uniform component: one rational polynomial proves the global bound

For x=t/k,

    R_W g(t)/g(t)
      =2(1+x)^(11/2) integral_1^2 u^10/(u^2+x)^8 du
      =(1+x)^(11/2) integral_1^4 r^(9/2)/(r+x)^8 dr.

Use sqrt(1+x)<=1+x/2 and sqrt(r)<=(r+4)/4. Therefore this ratio is at most

    B(x)=(1+x)^5(x+2)/8 * integral_1^4 (r^5+4r^4)/(r+x)^8 dr
       =3(x+2)(35021x^6+279255x^5+984828x^4+2002000x^3
                   +2525376x^2+1908480x+680960)
          /[560(x+1)^2(x+4)^7].

Exactly,

    2/3-B(x)=P(x)/[1680(x+1)^2(x+4)^7],

where

    P(x)=1120x^9+33600x^8+124971x^7+149127x^6+1539078x^5
        +10918776x^4+31552416x^3+44026752x^2+28331520x+6092800.

Every coefficient is strictly positive. This proves the uniform component bound below 2/3 for every x>=0, not merely at sampled x. Combining the two components proves the first assertion of (1).

The checker regenerates the polynomial by expanding r=v-x and integrating v^(j-8) exactly. It also checks a separate set of rational evaluations, but those samples are not the continuum argument.

### 2.3 The forcing and the complete inverse

At the origin, A_theta(0)<=1/70. For t>0, kappa(v)<=v^(9/2), extending the v-integral to infinity gives

    A_theta(t)<=Gamma(11/2) E S_theta^(-5/2) t^(-11/2)
              <(4725/128)t^(-11/2).

For t<=k, (1+t/k)^(11/2)A_theta(t)<64/70<1. For t>=k,

    (1+t/k)^(11/2)A_theta(t)
       <=(4725/128)(4/5)^(11/2)<11.

Here sqrt(4/5)<9/10 suffices. Thus A_theta belongs to B_g with norm at most 11. The positive Neumann series proves (1)–(2); its convergence is in the actual weighted Banach norm. Its sum agrees with the parent's response by uniqueness in C_b.

## 3. A complete complex Mellin tail for the response

The functions A_theta and R_theta^j A_theta are Laplace transforms of positive finite measures. Let alpha_{theta,j} denote these measures, and let

    eta_{theta,J}=Law(X_theta) * sum_{j=0}^J alpha_{theta,j}.

The full eta_theta has transform L_theta(t)Q_theta(t) and mass chi_theta. Define p=s/2 and the finite-resolvent transform

    D_{theta,J}(s)=2 c^p p(p-1)(p-2)
                          integral x^(p-3) eta_{theta,J}(dx).   (4)

For the full measure, this equals partial_theta M_theta(s). Each term retains the literal fixed-point law: truncating J is NOT yet a completely finite stochastic tree. Section 5 supplies that separate approximation.

### Theorem BJR2

For 0<=Re s<=1 and every J>=0,

    |partial_theta M_theta(s)-D_{theta,J}(s)|
       <=13 |p(p-1)(p-2)| (2/3)^(J+1),                        (5)

uniformly in theta. The value at p=0 is interpreted by its removable continuation. There is no bound on |Im s| hidden in this theorem; the right side has the displayed cubic height growth.

**Proof.** The omitted eta measure is positive. Its Laplace transform is, by (2), at most

    33(2/3)^(J+1)(1+t/k)^(-8).

For a=Re p in [0,1/2], the negative-moment formula gives

    integral x^(a-3) eta_tail(dx)
      <=33(2/3)^(J+1) k^(3-a) Gamma(5+a)/Gamma(8).

Take the absolute value AFTER using this real positive measure. Multiplication by the cubic factor in (4) gives (5), since c^a<=1, k^(3-a)<16, Gamma(5+a)<60 and 66*16*60/5040<13.

An estimate using only the unweighted bound |Q-tail|<=constant would make the t-integral diverge. An estimate using |1/Gamma(-p)| after taking the absolute value of a signed Laplace integral pays an unnecessary exponential-height factor here. Positivity of the omitted measure allows the stated cancellation. It still does not determine the sign of the complex Mellin transform itself. QED.

The same proof provides every inverse moment of eta of order b<8, not merely the previously stated orders through four. No inverse moment at b=8 is asserted.

## 4. Holomorphic parameter continuation on a uniform neighborhood

A local collision calculation needs more than formal differentiation of moments. The following supplies a genuine analytic family.

### Theorem BJR3

At every real theta in [0,1], the function L_theta has a holomorphic continuation in the parameter z on |z|<1/4096, of the form

    L_{theta+z}(t)=L_theta(t)+t^3 q_z(t),
    ||q_z||_g<=1/64.                                         (6)

For real theta+z in [0,1], this is the literal fixed law. Complex parameters are analytic extensions, NOT probability laws. In particular

    || (partial_theta^r L_theta)/t^3 ||_g
        <= r! 4096^r/64, r>=1.                               (7)

The continuations also give jointly holomorphic M and H on a parameter neighborhood of every point of the closed critical strip, with the removable Mellin values retained.

**Proof.** Put nu=Law(W)-Law(B). Substitute L_theta+t^3q into the fixed equation with scale measure mu_theta+z nu, and divide by t^3. The equation for q is a polynomial fixed-point map with forcing -z A_theta. Its linear operator has norm at most

    2/3+(25/24)|z|,

because the two absolute component bounds add to 3/8+2/3=25/24. Its quadratic bilinear norm is at most

    125/24+(3125/384)|z|.

For the last assertion use the pointwise inequality

    t^3 g(t)^2 <=k^3 L_g(t)g(t).

On the ball R=1/64 and parameter disk delta=1/4096, the image norm is bounded by

    11delta+[2/3+(25/24)delta]R
            +[125/24+(3125/384)delta]R^2 <R,

and its Lipschitz constant is strictly below 5/6. Both inequalities are exact rational checks. Holomorphic contraction iteration gives (6). For the real source, (1) integrated over the parameter gives ||(L_{theta+z}-L_theta)/t^3||_g<=33|z|<R; hence uniqueness identifies the continuation. Cauchy's estimate gives (7). The branches on overlapping disks agree by the identity theorem.

For completeness, changes in the pair transform can be written as

    c^p/Gamma(-p) * integral_0^infinity
                     t^(-p-1)[L_{theta+z}(t)^2-L_theta(t)^2] dt.

The integrand's numerator is O(t^3) at zero and O(t^-5) at infinity. It therefore defines the joint analytic difference for -5<Re p<3, with the zeros of reciprocal Gamma retaining the removable cases. Agreement initially at 0<Re p<1 identifies the original Mellin expectation. At s=1, this difference has absolute value below 1/8 on the displayed parameter ball: bound it by

    K(1/2)[2R+k^3R^2],
    K(p)=c^(Re p) k^(3-Re p) Gamma(3-Re p)Gamma(5+Re p)
                       /[Gamma(8)|Gamma(-p)|],

and use K(1/2)<1/16. Thus 1+M_{theta+z}(1) stays away from zero. This pays the reflected transform's normalization as well. QED.

## 5. Replacing the fixed law by an actual finite tree, INCLUDING its parameter derivative

Let X_{theta,0}=X_0 and X_{theta,m+1}=C_theta(X_{theta,m}+X_{theta,m}'). Write L_m for its Laplace transform, M_m for the corresponding pair Mellin transform, and

    Q_m=-partial_theta L_m/t^3.

At every finite m this derivative is defined by the literal finite mixture over the internal scale nodes. The two children are independent; the multiplier at a node is shared only by those siblings. The derivative replaces ONE node's scale law by Law(W)-Law(B), and sums over all nodes. This is a finite signed measure operation, not an omitted infinite-tree derivative.

Let q=2/3. Uniformly in theta,

    0<= (L_m-L_theta)/t^3 <=33 q^m g(t),                     (8)
    0<= Q_m(t)<=33g(t),                                     (9)
    ||Q_m-Q_theta||_g <=(33+18000m)q^m.                     (10)

For every fixed s with 0<Re(s/2)<1,

    |partial_theta M_m(s)-partial_theta M_theta(s)|
      <=36000(m+1)q^m K(s/2),                              (11)

where K is the explicit gamma expression in Section 4. At p=0 the derivative difference is zero. The right side is a complete bound, not claimed polynomial in height: K contains |1/Gamma(-p)|. No complex cancellation is assumed for the SIGNED difference between two response measures.

**Proof.** The initial difference (L_0-L_theta)/t^3 is the integral of the positive Q_eta from eta=0 to theta, so its weighted norm is <=33. Factoring the difference of squares in each recursion and using Section 2 gives (8), preserving a positive Laplace representation. Every finite iterate lies between the gamma and endpoint source in the same third-order order, so the forcing A_m obeys the same 11g bound. Exact differentiation gives

    Q_{m+1}=A_m+R_m Q_m,
    R_m h=2 integral c0^3 L_m(c0t)h(c0t)mu_theta(dc0), Q_0=0.

This proves (9). Put eps=q^m. By the total variation bound |nu|<=mu_B+mu_W and (8),

    ||A_m-A_theta||_g <=(275/8)eps,
    ||(R_m-R_theta)Q_theta||_g <=(90750/8)eps.

For the second use t^3 g^2<=k^3 L_g g; no coefficient or scale is dropped. Thus e_{m+1}<=q e_m+(91025/8)q^m, e_0<=33. Solving proves (10), since (91025/8)/q<18000.

Finally

    |L_m Q_m-L_theta Q_theta|
      <=18000(m+1)q^m L_g g.

Differentiate the compensated Mellin integral and integrate its absolute value. The complete beta integral is k^(3-a)Gamma(3-a)Gamma(5+a)/Gamma(8), which gives (11). Cauchy estimates on a slightly wider s-domain give spectral-derivative variants; no parameter differentiation of an unbounded remainder is needed. QED.

This supplies a finite-source route to arbitrary fixed-point response precision, with a stated cost. It does not make the exponential-size finite tree cheap. It also does not show that a desired collision sign has either orientation.

## 6. A separate exact endpoint response calculation

The preceding estimates are uniform but conservative. At theta=0 one can solve the response in an orthogonal gamma space, without unknown fixed-law inputs.

Let gamma_k be Gamma(k, rate k). Define the Markov update

    Z_new=B(Z+G),  B~Beta(k,k), G~gamma_k,

independently. Its stationary law is gamma_k. Given Z+G, the old and new Z are independent identically distributed beta fractions of the same total, so the Markov operator P is reversible. Degree-j polynomials have leading multiplier

    beta_j=(k)_j/(2k)_j.

Self-adjointness and preservation of polynomial degree imply that the orthogonal Laguerre polynomial L_j^(k-1)(kx) is an eigenfunction with eigenvalue beta_j. Completeness is the classical gamma/Laguerre one, also reconstructed in the parent.

The signed one-step forcing density is Law(W Gamma(5,rate k))-gamma_k. Its ratio to gamma_k is square integrable: the first density is

    k^5 x^4/24 * integral_1^2 u^10 exp(-ku^2x)du,

and its ratio to gamma_k is at most a fixed constant times x^(5/2). Its first three moments (orders 0,1,2) vanish. On the orthogonal complement of those polynomials, ||2P||=2beta_3=3/8. The derivative density is therefore the ordinary signed L2(gamma_k) solution (I-2P)^-1 of this forcing.

This is not merely a formal derivative series. Its Laplace transform satisfies the parameter-response equation and has the three matching origin moments. Dividing by t^3 puts it in the parent's unweighted C_b response class, where the inverse is unique; it therefore equals the derivative of the actual fixed law. Convolution with the independent gamma child gives the pair derivative. Conditional expectation bounds its pair-gamma-relative L2 norm.

Let w_j be the coefficients of

    W(z)=(1-z)^(5/2) E[1-(1-W)z]^-5.

Then d_0=d_1=d_2=0 and

    d_j=2w_j/(1-2beta_j), j>=3.                              (12)

Since M_0(s)=(pi/15)^p Gamma(5+p)/24 is nonzero in the critical strip,

    R(s):=partial_theta log M_theta(s)|_(theta=0)
         =sum_{j>=0} d_j (-p)_j/(5)_j, p=s/2.                (13)

This is the logarithmic response of RAW M, not of normalized H. It is exactly the required quantity in the zero-velocity calculation below.

### An O(N) rational coefficient recurrence

Set a_j=[z^j](1-z)^(5/2), v_j=[z^j](1-z)^(5/2)(1-3z/4)^-5. Then

    a_0=v_0=w_0=1,
    a_j=(2j-7)a_(j-1)/(2j),
    j v_j=((7j-2)/4)v_(j-1)-((6j+3)/8)v_(j-2),
    (2j-1)w_j=(2j+3)w_(j-1)-2v_j+a_j,

with the v_-1 term zero. These follow by differentiating the two elementary generating functions and integrating d/du[u^11/((1-z)u^2+z)^5] on [1,2]. In particular

    w_1=w_2=0, w_3=-7/32, d_3=-7/10.

The mean equation is not inverted at j=1.

### The complete remainder of (13)

Let N>=5, m=floor((N+1)/2). The coefficients a_j are negative for j>=3, and

    sum |a_j|=23/4,
    sum_(j>=m)|a_j|=|binom(3/2,m-1)|.

The coefficients r_j of E[1-(1-W)z]^-5 are nonnegative, have total mass

    sum r_j=E W^-5=2047/11,

and satisfy r_j<=binom(j+4,4)(3/4)^j. Therefore

    sum_(j>N)|d_j| <= (16/5)[
       (2047/11)|binom(3/2,m-1)|
       +(23/4)1024 binom(m+4,4)(3/4)^m].                     (14)

To verify the last tail, use binom(m+r+4,4)<=binom(m+4,4)binom(r+4,4), then sum the binomial generating function. In the convolution for w_j, any index pair summing to j>N has at least one index >=m. This overcounts safely and proves (14).

If a=Re p and

    (2a+10)N+25>=|p|^2, 2a+10>0,

the magnitudes |(-p)_j/(5)_j| decrease for j>=N. Multiplying (14) by |(-p)_N/(5)_N| bounds the WHOLE complex remainder of (13). The same argument works on a complex interval by using the maximum |p| and minimum a before checking the inequality.

This tail decreases algebraically but much faster than the generic L2 estimate in #878, because it uses the exact gamma endpoint forcing. It is not asserted for all theta.

## 7. New native numerical certificates: complex response and local zero velocity

The accepting computation uses N=512, exact rational coefficients, and outward dyadic elementary functions. It proves

    0.031965371550 < Re R(1/2+4i) < 0.031965371552,
   -0.100126977071 < Re R(1/2+8i) < -0.100126977068.            (15)

The retained receipt provides sharper outward intervals and their complete tail costs. These opposite signs concern the actual homotopy's logarithmic amplitude response at its gamma endpoint. They are not off-line zeros and are not double-collision discriminants.

Let t_0 be the unique solution in

    13.7654722174 < t_0 < 13.7654722175

of H_0(1/2+it)=0. The certificate uses the continuous gamma phase

    phi(t)=(t/2)log(pi/15)+Im log Gamma(21/4+it/2).

It verifies phi(left)<pi/2<phi(right) and phi'(t)>0.28 throughout the entire interval. Thus the zero exists, is unique in the stated real bracket, and is simple. This is a zero of the gamma ANCHOR, not a zero of xi. No first-zero label or full zero census is required.

The analytic implicit-function theorem from Section 4 gives a real analytic zero branch t(theta) for theta near zero. The reflected transform is real on real t, so local uniqueness keeps the branch real for real theta. The normalization denominator is nonzero and does not change zero positions.

At the anchor zero, M_0(1/2+it_0) is nonzero and purely imaginary. Exact differentiation yields

    t'(0)=-Im R(1/2+it_0)/phi'(t_0).                        (16)

The entire bracket, rather than a rounded center, is used in (13) and in the digamma phase derivative. The resulting certificate is

    2.08931 < t'(0) < 2.08932.                              (17)

Hence for some positive, UNEVALUATED epsilon, this simple critical-line branch persists for 0<=theta<epsilon and t(theta)>t_0+2theta when theta>0. This is a local motion theorem. It neither locates the branch at theta=1 nor excludes any later collision or entry from a boundary.

The complex gamma calculation uses 24-term shifted Stirling expansions at Re z>=64, with all Bernoulli-integral remainders, then 64 exact recurrence steps back. Bounds use Re z, not merely |z|. The 512-bit interval code is adapted from the earlier PR #853 backend, not an independent implementation. The root bracket and response points were selected by nondirected scouts; the accepting inequalities reconstruct their defining formulas without using those scout values.

## 8. The attempted global conclusion and the exact remaining task

The work attacks the previous derivative-tail problem directly. It now supplies:

1. a named, uniformly contractive weighted response space and a complete complex Mellin tail;
2. a genuine analytic parameter family, not formal rational moments;
3. finite-source C1 convergence, retaining the infinite tree and parameter derivative costs;
4. one actual local critical-line zero branch with a certified nonzero initial velocity.

None of these establishes the required sign at a real DOUBLE zero. At such an event the quantities F=F_t=0 impose different conditions, and the discriminator is still

    D'=-2 F_theta/F_tt.

The uniform operator bound controls the size and computation of F_theta, not its sign relative to F_tt. The new simple-zero velocity is not used as a double-zero calculation. The opposite signs in (15) demonstrate directly why positive Laplace response does not mean a universally increasing complex modulus, but do not refute the homotopy's possible strip zero property.

A completed RH argument would still require either a source-specific confinement theorem on the full path, or a bound on total nonreal-zero production that retains births, deaths, higher collisions and boundary entry. No such sign or total upper bound is proved here. The nearby two real zero–pole cancellations outside the strip from #878 do not change this conclusion.

The contribution is a complete analytic/computational interface for attacking that sign, plus an actual source-bound local motion calculation. It is not a proof of RH awaiting a routine final review.

## References and review boundaries

[B] Biane, Pitman, Yor, Probability laws related to the Jacobi theta and Riemann zeta function and Brownian excursions, arXiv:math/9912170. Exact endpoint scaling is inherited from the frozen source; this pass reread the primary record, not the full paper.
[D1] NIST DLMF 18.3, 18.5 and 18.12.13: gamma/Laguerre normalization and generating function. The source-specific identities are derived above.
[D2] NIST DLMF 5.11: log-Gamma/digamma asymptotic normalization and complete right-half-plane remainder. The implemented absolute bounds follow from the periodic Bernoulli integral with |B_(2m)({x})|<=|B_(2m)|.
[P] PR #876 and PR #878 at the exact SHAs in SOURCES.json. Their paper results have not been independently accepted here. Parent executable suites were not rerun.

No broad external novelty audit, formal proof, full repository build, remote CI success, global zero census or independent referee acceptance is claimed.
