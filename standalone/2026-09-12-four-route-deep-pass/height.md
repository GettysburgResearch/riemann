# Branching height control and a uniform weighted-defect alternative

The branching route now has explicit comparison on complete growing windows,
not merely the original fixed height-30 result. Its remaining obstacle is
centrality of the limiting zero clusters. The large sufficient cutoff T_n
does not measure that obstacle by itself. Two deductions below clarify how
to work around the cutoff without assuming the desired centrality.

The new deductions are proposed arguments from this review, not externally
accepted results. Their analytic inputs are stated explicitly. No native
zero census is newly computed here.

## 1. Frozen sources and the actual theorem chain

The literal orbit is X_0~Gamma(5/2, rate5/2) and
X_(n+1)=(X_n+X'_n)/U², with independent children and the same independent
U uniform on[1,2] dividing their sum. Set V_n=(pi/6)(X_n+X'_n),
M_n(s)=E V_n^(s/2), and

    H_n(s)=[M_n(s)+M_n(1-s)]/[2(1+M_n(1))].

All positive-variable powers use the real logarithm. The Brownian fixed law
has M_*(s)=2xi(s), so H_n tends to xi locally uniformly in the domains used
here. The classical probabilistic identity is due to Biane, Pitman and Yor
[S5]; the source/order normalization is rederived in[S2–S4].

[S1] #860, e1a782cffaafbc9cc228273ed94ce63ae0407632,
[BHH26 proof](https://github.com/GettysburgResearch/riemann/blob/e1a782cffaafbc9cc228273ed94ce63ae0407632/standalone/2026-09-10-astra-branching-high-height/PROOF.md).
Every fixed depth has only finitely many off-central critical-strip zeros.
Above the supplied T_n, all those zeros are central and simple. Its proof
retains a full signed BV remainder after the positive atomic polynomial;
positivity of the polynomial alone is not the theorem.

[S2] #870, ee7f76736c235714496526f999e028d181302b56,
[BPW26 proof](https://github.com/GettysburgResearch/riemann/blob/ee7f76736c235714496526f999e028d181302b56/standalone/2026-09-12-branching-permanent-window/PROOF.md).
One full theta contour certificate protects the entire height-30 window for
every depth n>=32. The three counted zeros are simple and central. This is
a finite-window computer-assisted input, not a verified all-height census.

[S3] #873, 4d25182333f5900ebfbc97f36f823d256a2ee340,
[BUB26 proof](https://github.com/GettysburgResearch/riemann/blob/4d25182333f5900ebfbc97f36f823d256a2ee340/standalone/2026-09-12-branching-unbounded-bands/PROOF.md).
Depth D(R,a) <=(88/105)R+O((a+1)log(R+10)) suffices for tracking the actual
Xi divisor to resolution2^-a in the height-R rectangle. Conrey's imported
simple-central-zero proportion plus reflection gives infinitely many clean,
disjoint full-width bands, each permanently central after its own depth.
Neither their widths nor their depth thresholds are uniform. They do not
cover the whole strip.

[S4] #874, 80844a3778390ff744235cf2b021cfaea80ff512,
[BHT26 proof](https://github.com/GettysburgResearch/riemann/blob/80844a3778390ff744235cf2b021cfaea80ff512/standalone/2026-09-12-branching-height-transfer/PROOF.md).
For N>=2^18 and every m>=N, the whole height-N window tracks actual Xi
clusters with shrinking radius exp[-Theta(N/logN)]. Every component's total
multiplicity is retained. Its centers are not shown central, and no simplicity
assumption is silently imposed on Xi.

[S5] Biane, Pitman and Yor, *Probability laws related to the Jacobi theta
and Riemann zeta function and Brownian excursions*,
[arXiv:math/9912170](https://arxiv.org/abs/math/9912170).

[S6] Conrey, *More than two fifths of the zeros of the Riemann zeta function
are on the critical line*, J. reine angew. Math.399(1989),1–26,
[original paper](https://doi.org/10.1515/crll.1989.399.1).
The simplicity assertion is part of the imported proportion. It is not a
new branching zero-proportion theorem.

## 2. What the high-height proof gets right, and what is not uniform

The derivative-measure induction in[S1] explicitly keeps all shared-U endpoint
atoms and all mixed signed densities. Beta averaging squares only matching
atomic coefficients; it does not make the mixed term positive. The atomic
recurrence u_(n+1,j)=u_(n,j)^2-2u_(n,j-1)^2 yields P_n(z)=sum u_(n,j)^2 z^j.
Its roots lie in |z|<=1/4 by the coefficient-ratio bound. Therefore the
leading factor P_n(2^-s) has no critical-strip zeros.

The exact Mellin factorization is M_n(s)=G_n(s)[P_n(2^-s)+R_n(s)]. Full BV
bounds give |R_n|<=E0/|t| and |R_n'|<=E1/|t|. These are genuine full-source
estimates, but E0,E1 depend severely on depth. Only after paying these terms
does the horizontal logarithmic-modulus-ratio derivative become positive.
That derivative forces reflected-sum zeros to be central and simple.

The printed T_n is a sufficient recipe, not the smallest valid cutoff. Its
floor320*16^n is not a lower bound on the actual height of exceptional zeros.
The first values320,279109,about1.788e15 and3.097e39 are proof majorants,
not observed last-exception locations. A hypothetical fixed off-line Xi zero
can persist below them as depth grows without violating any cited result.

The new minimum-modulus comparisons also have correct scope: they remove
neighborhoods of every actual Xi zero before applying Harnack and Rouche.
The allowance O(R³(31/80)^n) competes with the gamma envelope exp(-piR/4).
Its limiting comparison speed is4log(80/31)/pi≈1.20708129. This is a limit
of that allowance, not a proved lower bound for the true error. It does not
prove centrality even when the allowance is small.

## 3. Proposed deduction: an exponential zero-defect tail uniform in depth

This gives a complete weighted target without computing up to T_n. It uses
only bounded analyticity on a wider strip, not eventual reality of high zeros.

### 3.1 Uniform bounded strip and nonzero anchor

For n>=1, source third-order monotonicity gives

    E X_n^-1 <= E X_1^-1 =35/24,
    E V_n =pi/3 <4/3,
    E V_n^-1 <=(6/pi)E X_n^-1 <3.

The first inequality follows by integrating the positive Laplace bound
L_n(t)<=L_1(t) against dt. Hölder bounds E V_n^a by3 for every
a in[-1/4,3/4]. Thus |H_n(s)|<=3 on -1/2<Re s<3/2.
All these Mellin functions are holomorphic there, by domination on smaller
closed strips. The bounds hold for all imaginary parts, not just a window.

At the midpoint, Jensen applied to the convex function y^(-1/4) gives

    E V_n^(1/4) >=(E V_n^-1)^(-1/4)>3/4,
    E V_n^(1/2) <=sqrt(E V_n)<7/6,
    H_n(1/2)> (3/4)/(13/6)=9/26>1/3.

Consequently f_n(z)=H_n(1/2+iz)/H_n(1/2) satisfies f_n(0)=1 and |f_n|<=9
on |Im z|<1. The same weak bounds hold for the locally uniform limit.

### 3.2 Disk mapping and the full zero sum

Map this strip to the disk by w=tanh(pi z/4). Jensen's formula for the bounded
disk function gives, counting every zero with multiplicity,

    sum log(1/|w_rho|) <=log9.

This follows first on disks of radius r<1 and then by monotone convergence.
For z=x+iy with |y|<=1/2, put A=pi|x|/2 and c=cos(pi y/2)>=1/2.
The identity |w|²=(cosh A-c)/(cosh A+c) implies

    1-|w| >= c/(cosh A+c) >= (1/4)exp(-A).

Since1-|w|<=log(1/|w|), every n>=1 obeys

    sum_(H_n(s)=0, 0<=Re s<=1) mult(s) exp(-pi|Im s|/2) <=4log9.   (H1)

The sum includes possible boundary zeros and all heights. No assumption
about a simple or finite exceptional divisor enters (H1).

### 3.3 A positive defect, convergence, and exact missing premise

Define

    B_n =sum_(H_n(s)=0,0<=Re s<=1)
                mult(s)(Re s-1/2)² exp(-pi|Im s|).

Then, uniformly in n>=1,

    0<=B_n<=log9,
    sum_(|Im s|>R) mult(s)(Re s-1/2)²exp(-pi|Im s|)
        <= log9 exp(-piR/2).                                  (H2)

Indeed the squared displacement is at most1/4, and the second exponential
factor costs at most exp(-piR/2) in that tail. This pays the entire complement.

Let B_xi be the same sum over Xi's nontrivial zeros. Local uniform convergence
and Rouche yield convergence of finite zero multisets, including multiplicity,
inside any rectangle whose limiting boundary has no zeros. Xi has no zeros
on Re s=0 or1; choose horizontal boundaries avoiding its discrete ordinates.
The continuous weight therefore converges on each such compact rectangle.
The uniform bound(H2) permits removal of both horizontal tails. Hence

    B_n -> B_xi,
    RH if and only if B_n ->0.                                (H3)

The familiar critical-strip facts used here are summarized in
[NIST DLMF25.10](https://dlmf.nist.gov/25.10). Jensen and conformal strip
mapping are classical; this is their source-specific composition, not a
priority claim for a new type of RH criterion.

This deduction supplies a branching analogue of the gamma defect consumer.
The weights differ: this one decays exponentially in height, whereas the
gamma construction uses inverse powers. A tiny value is consequently weak
numerical information about very high zeros. It is vanishing, not numerical
smallness, that would prove RH. The height-30 certificate alone only gives
a fixed tiny upper bound through(H2), not decay with n.

Useful sufficient next estimates include a native contraction of B_n or
centrality in complete expanding lower windows combined with(H2). Nothing
in the source-order inequalities above establishes such a sign. The main
practical advantage is an explicit, depth-independent complement bound; one
does not have to enumerate all exceptional zeros below an enormous T_n.

## 4. Proposed deduction: improve the leading-factor derivative estimate

This concerns one part of T_n only; the complete BV costs still remain.
Use the source polynomial and recurrence from[S1]. For n>=2 let

    r_n=|u_(n,n-1)/u_(n,n)|.

Then r_2=1/4 and r_(n+1)=1/2-r_n². The interval[1/4,7/16] is invariant.
All earlier adjacent coefficient ratios are at most1/4 after squaring.
Writing A_n=u_(n,n)^2 and

    P_n(z)=A_n z^n Q_n(1/z),  Q_n(w)=1+sum_(j=1)^n b_j w^j,

gives b_1<=49/256 and b_j<=b_1*4^(-(j-1)). For |w|<=2,

    |Q_n(w)-1|<=49/64,
    |wQ_n'(w)|<=49/32,
    |wQ_n'(w)/Q_n(w)|<=98/15<7.

At n=1, Q_1(w)=1+w/4 yields a bound1 instead; n=0 is constant. Therefore
throughout the critical strip,

    d_s log P_n(2^-s)=-n log2+e_n(s),
    |e_n(s)|<7log2.                                         (H4)

The earlier2nlog2 absolute bound loses the uniform leading-term structure.

The gamma factor also has an exact useful cancellation. With p=s/2,
a=5*2^n and m=2^(n+1)-2,

    Gamma(a+p)/(1+p)_m
       =Gamma(1+p) product_(k=m+1)^(a-1)(p+k).

Every logarithmic derivative of the polynomial product has positive real
part on the critical strip. Binet's remainder gives

    Re psi(1+s/2)>=log(|t|/2)-7/12,

because Re(1+s/2)>=1, |1/[2(1+s/2)]|<=1/2, and the derivative of the
Binet remainder has modulus<=1/12. Consequently

    Re(G_n'/G_n)>= (1/2)log[(pi/15)|t|/2]-7/24.             (H5)

Combining(H4),(H5) with the full remainder constants E0,E1,L_n from[S1]
gives an alternative sufficient threshold

    T_hat_n=ceil max{2, 2E0/L_n,
                    4[E1+(n+7)E0]/L_n, 2^21*4^n}.         (H6)

For t>=T_hat_n, |R/P|<=1/2 and

    |(P+R)'/(P+R)-P'/P|
        <=2[E1+(n+7)E0]/(L_n t)<=1/2.

Thus the horizontal log-modulus-ratio derivative is at least

    log[(pi/15)t/2]-7/12-2(n+7)log2-1 >0.

For the last strict inequality use pi/15>1/5, t>=2^21*4^n,
2^21/10>2^17, and log2>2/3. The lower bound exceeds
3log2-19/12>0. The reflected-sum argument of[S1] then gives the same
eventual centrality and simplicity. Both signs of height follow by reality.

This replaces the explicit phase floor16^n by a constant times4^n, while
retaining every remainder term. It is not an effective linear-depth cutoff.
The new threshold may be worse at small n; the minimum of it and the old
valid threshold remains valid. The rapidly growing BV terms can dominate
both. No computation or argument here identifies the optimal safe height.

An exact reconstruction of the frozen rational recurrence is included in
`height-cutoffs.py` and `height-cutoffs.json`. At depths0–6 the alternative
is worse, so the old cutoff should be retained. At depth7 it is slightly
smaller; at depth8 its ratio to the old cutoff is about0.95833, while the old
cutoff already has2811 decimal digits. This confirms the practical limitation:
improving the isolated exponential phase floor does not remove the enormous
mixed-density majorant. These are exact recurrence calculations with rounded
ratios for display, not zero computations.

## 5. Research consequence

The height route has two viable next tasks. One is to improve the genuinely
signed remainder, rather than only its total-variation majorant. The other
is to exploit the source recurrence to control the full weighted defect(H3).
The latter avoids demanding overlap with the huge sufficient upper cutoff,
but it still requires a native zero-geometric sign.

Neither the exact spectrum in #872 nor positivity of its survival mixture
provides that sign. Its random Laplace cutoff is distinct from T_n. The
operator's universal eigenvalue list cannot distinguish Xi from other
normalized analytic sources; its exact hyperbolic and shifted-Xi identities
are the more source-sensitive objects worth testing against(H3).

## 6. Review and execution scope

The arithmetic and gamma route agents separately reviewed Sections 3–4,
including the bounded-strip constants, full exponential zero tail, convergence
with multiplicities, polynomial coefficient ratios, gamma-factor cancellation
and complete remainder allowances in the alternative cutoff. Neither reported
a defect in the stated arguments. These are analytic cross-reviews within one
agent session, not external mathematical acceptance or formal verification.

The exact recurrence calculation covers depths 0 through 8 using the literal
pinned #860 checker source. It reconstructs sufficient bounds only. No new
native zero location, contour count or all-height real-zero certificate was
computed. The finite height-30 certificate and the cited manuscript theorems
remain explicit imported inputs.
