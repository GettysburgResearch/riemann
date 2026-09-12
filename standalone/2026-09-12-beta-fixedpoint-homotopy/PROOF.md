# BFC26 — a uniformly stable fixed-point homotopy from gamma to the exact Xi source

Date: 2026-09-12.
Status: **Proposed component proofs; independent mathematical review required. RH is NOT proved.**
Scope: an alternative source continuation, not a new theorem about all zeros of the previously prescribed discrete iterates. The exact source response is positive in Laplace coordinates. Its complex zero-production sign is explicitly OPEN.

This packet changes the branching RULE and solves its fixed point at every parameter. It does not average the characteristic functions of two zero-safe models. Its endpoints are the previously used Gamma(5/2, rate 5/2) seed and the unmodified Biane–Pitman–Yor source. It supplies an exact third-order metric, a positive uniformly invertible response equation, a complex Mellin response, and a uniform tail for one nonnegative off-line-zero functional. These results do not establish a zero-preserving homotopy.

General beta–gamma algebra, smoothing-transform contraction, third-order stochastic comparison, Peano kernels, resolvent series, Jensen's formula and local zero motion are classical. No general priority claim is made. The source-specific composition and constants below are proposed for review.

## 1. A new one-parameter source, with both endpoints fixed

Let

\[
B\sim\operatorname{Beta}(5/2,5/2),\qquad W=U^{-2},\quad U\sim\operatorname{Unif}[1,2].
\]

For 0 <= theta <= 1, let the probability measure mu_theta be

\[
\mu_\theta=(1-\theta)\operatorname{Law}(B)+\theta\operatorname{Law}(W).
\tag{1}
\]

Let C_theta have this law. Define the nonlinear probability map

\[
\mathcal T_\theta(\nu)=\operatorname{Law}\big(C_\theta(X+X')\big),
\tag{2}
\]

where X,X' are independent with law nu, and one independent C_theta multiplies their SUM. Independent sibling multipliers would give a different map.

Write a_j(theta)=E C_theta^j. Exactly,

\[
a_j(\theta)=(1-\theta)\frac{(5/2)_j}{(5)_j}
 +\theta\frac{1-2^{1-2j}}{2j-1}\quad(j\ge1),\qquad a_0=1.
\tag{3}
\]

In particular

\[
a_1=\tfrac12,\quad a_2=\tfrac7{24},\quad
 a_3=\frac{30+\theta}{160},\quad r_\theta=2a_3=\frac{30+\theta}{80}.
\tag{4}
\]

### Theorem BFC1: uniformly contractive fixed points

On nonnegative mean-one laws with finite second moment,

\[
W_2(\mathcal T_\theta\nu,\mathcal T_\theta\eta)
 \le \sqrt{7/12}\,W_2(\nu,\eta).
\tag{5}
\]

There is a unique fixed law nu_theta, and

\[
E X_\theta=1,\quad E X_\theta^2=7/5,\qquad
X_\theta\overset d=C_\theta(X_\theta+X_\theta').
\tag{6}
\]

Its endpoints are exactly

\[
X_0\sim\Gamma(5/2,\mathrm{rate}\ 5/2),\qquad
X_1\overset d=\frac6{\pi^2}\sum_{j\ge1}\frac{E_j}{j^2},
\tag{7}
\]

with independent mean-one exponentials E_j. This subscript 1 means parameter theta=1, NOT the first discrete branching iterate in #853/#857.

**Proof.** Couple X,Y optimally, take two independent copies of that coupling, and use the same C_theta. Since E(X-Y)=0, the cross term in the squared sum disappears. Its expectation is 2 a_2 W_2(nu,eta)^2=(7/12)W_2(nu,eta)^2. This proves (5). The normalized class is closed in W_2 and complete; Banach's theorem proves existence and uniqueness. The fixed second-moment equation m_2=a_2(2m_2+2) gives m_2=7/5.

At theta=0, the beta–gamma change of variables (G,G')=(TB,T(1-B)) shows that an independent Beta(5/2,5/2) times Gamma(5, rate 5/2) is Gamma(5/2, rate 5/2). The beta normalization follows from Euler's beta integral [D1].

For the other endpoint, the positive series in (7) converges almost surely and in L2. Its Laplace transform is

\[
L_1(t)=\frac{\sqrt{6t}}{\sinh\sqrt{6t}},\quad L_1(0)=1.
\]

The sinh product proves the formula. For b=sqrt(6t),

\[
\int_1^2L_1(t/u^2)^2du
 =b\int_{b/2}^b\operatorname{csch}^2v\,dv
 =b[\coth(b/2)-\coth b]=b/\sinh b.
\]

Laplace uniqueness identifies the fixed law. This endpoint and the fixed-point identity are classical BPY material [B], independently normalized here. No zero information is an input. Finally a fixed atom at zero would have probability p=p^2. The mean excludes p=1, so every X_theta is strictly positive almost surely. □

Every fixed positive integer moment exists. One proof starts the iteration at the gamma endpoint and inducts in moment order, using

\[
m_j(\theta)=\frac{a_j(\theta)}{1-2a_j(\theta)}
 \sum_{i=1}^{j-1}\binom ji m_i(\theta)m_{j-i}(\theta),\quad j\ge2.
\tag{8}
\]

The denominators are positive. Uniform bounds for the lower moments give uniform bounds for the next one for all finite iterates and all theta. Passing the nonnegative truncations or uniformly integrable moments to the fixed point justifies (8), rather than presupposing it. In particular there is a uniform fourth-moment bound. For each j, m_j is a rational function of theta with no pole in [0,1]. This fact alone has no zero-location implication.

## 2. A source-ordered path with an exact metric

For laws having the same first two moments, write nu <=_3 eta when E_nu f <= E_eta f for every real C3 function on [0,infinity) with bounded nonnegative third derivative. Define

\[
d_3(\nu,\eta)=\sup_{\|f'''\|_\infty\le1}|E_\nu f-E_\eta f|.
\tag{9}
\]

Lower-degree polynomial parts cancel. Finite third moments make this finite.

### The basic beta/uniform comparison

The scale densities are

\[
b(x)=\frac{128}{3\pi}x^{3/2}(1-x)^{3/2}\mathbf1_{(0,1)},\qquad
w(x)=\frac1{2x^{3/2}}\mathbf1_{[1/4,1]}.
\]

They have matching moments of orders 0,1,2. On (1/4,1),

\[
\frac{w(x)}{b(x)}=\frac{3\pi}{256x^3(1-x)^{3/2}}.
\]

This ratio decreases to its unique minimum at 2/3 and then increases. Its right value at 1/4 is 2pi/sqrt(3)>1; its minimum is 243pi sqrt(3)/2048<1; its limit at 1 is infinity. Thus w-b has exactly three sign switches, with pattern -, +, -, +. For a function with f''' >= 0, quadratic interpolation at those switches has an error with that same sign pattern (the third divided difference is nonnegative). The interpolating quadratic integrates to zero against w-b. Hence B <=_3 W.

Equivalently the complete Peano kernel

\[
\kappa(v)=\tfrac12\{E(W-v)_+^2-E(B-v)_+^2\}
\tag{10}
\]

is nonnegative, supported on [0,1], and

\[
E f(W)-E f(B)=\int_0^1 f'''(v)\kappa(v)\,dv,\qquad
\int_0^1\kappa(v)dv=1/960.
\tag{11}
\]

Approximation of the truncated-square test by smooth third-convex tests proves the pointwise kernel assertion. The identity itself is Taylor's integral remainder and the three matching moments. It also gives, for j >= 0,

\[
\int v^j\kappa(v)dv=
\frac{E W^{j+3}-E B^{j+3}}{(j+1)(j+2)(j+3)}.
\tag{12}
\]

A useful complete small-v bound is

\[
0\le\kappa(v)\le\frac{1024}{945\pi}v^{9/2}<v^{9/2},\quad 0\le v\le1.
\tag{13}
\]

Indeed matching moments rewrites (10) using lower truncated squares, so it is at most (1/2)E(v-B)_+^2. Bound (1-x)^{3/2} by 1 and evaluate the beta integral B(5/2,3)=16/315. This proves (13), including its endpoint range.

### Theorem BFC2: exact ordering and metric along the fixed-point path

For 0 <= alpha <= beta <= 1,

\[
\nu_\alpha\preceq_3\nu_\beta,\qquad
m_3(\theta)=\frac{21(30+\theta)}{5(50-\theta)},
\tag{14}
\]

and

\[
\boxed{d_3(\nu_\alpha,\nu_\beta)
 =\frac{56(\beta-\alpha)}{(50-\alpha)(50-\beta)}.}
\tag{15}
\]

The total endpoint distance is 4/175. Reparameterizing by 56/(50-theta) makes this path a constant-speed metric segment. This does not mean the fixed laws are convex mixtures of the two endpoint laws.

**Proof.** Positive scaling and independent addition preserve the third order. For fixed children, the function of the scale has third derivative (X+X')^3 f'''(c(X+X')) >= 0. Hence T_theta is order-preserving in the input law and increasing in theta. Start every iteration at nu_0. Its first step lies above nu_0, so the iterations increase in both their iteration index and theta. W2 convergence together with a uniform fourth moment permits passage of all at-most-cubic tests to the limits. This proves the order.

Equation (8) at j=3 gives (14), with m_3'=336/(50-theta)^2. For any |f'''| <= 1, both x^3/6+f and x^3/6-f have nonnegative third derivative. The discrepancy is at most (m_3(beta)-m_3(alpha))/6, and x^3/6 attains that bound. Simplifying yields (15). □

For t >= 0 the third derivative of exp(-tx) is nonpositive, so

\[
L_0(t)\ge L_\theta(t)\ge L_1(t),\qquad
L_0(t)=(1+2t/5)^{-5/2}.
\tag{16}
\]

The negative-moment Laplace integral gives the uniform bounds

\[
E X_\theta^{-b}\le(5/2)^b\frac{\Gamma(5/2-b)}{\Gamma(5/2)},\quad0<b<5/2,
\tag{17}
\]

and, for S_theta=X_theta+X_theta',

\[
E S_\theta^{-b}\le(5/2)^b\frac{\Gamma(5-b)}{\Gamma(5)},\quad0<b<5.
\tag{18}
\]

In particular E X_theta^-2 <=25/3 and E S_theta^-1 <=5/8. Positive moments are uniformly bounded by their theta=1 values, either by the ordered moment recurrence or by smooth truncation followed by uniform higher moments.

## 3. A uniformly stable, positive RESPONSE equation

Let L_theta(t)=E exp(-tX_theta). The nonlinear fixed equation is

\[
L_\theta(t)=\int L_\theta(ct)^2\mu_\theta(dc).
\tag{19}
\]

The response must be computed AFTER solving this equation. It is not the derivative of a convex mixture of endpoint Laplace transforms.

Define the finite positive measure A_theta by its Laplace transform

\[
A_\theta(t)=E\left[S_\theta^3\int_0^1\kappa(v)e^{-tvS_\theta}\,dv\right].
\tag{20}
\]

Its mass is

\[
b_\theta=A_\theta(0)=\frac{E S_\theta^3}{960}
 =\frac7{10(50-\theta)}.
\tag{21}
\]

On the Banach space C_b([0,infinity)), define

\[
(\mathscr R_\theta q)(t)=2\int c^3L_\theta(ct)q(ct)\mu_\theta(dc).
\tag{22}
\]

It is a positive operator. Its EXACT norm is r_theta=(30+theta)/80: the upper bound uses 0<L<=1, and equality follows by evaluating the constant function at t=0.

### Theorem BFC3: differentiability and a positive full-source resolvent

The path is continuously differentiable in the weighted Laplace norm

\[
\|f\|_{(3)}=\sup_{t>0}|f(t)|/t^3
\]

for differences of its transforms (with the continuous value at zero). Its response is

\[
\boxed{-\partial_\theta L_\theta(t)=t^3Q_\theta(t),\qquad
Q_\theta=(I-\mathscr R_\theta)^{-1}A_\theta
 =\sum_{j=0}^{\infty}\mathscr R_\theta^j A_\theta.}
\tag{23}
\]

One-sided derivatives are intended at 0 and 1. The inverse norm and the entire remainder are

\[
\boxed{\|(I-\mathscr R_\theta)^{-1}\|=\frac{80}{50-\theta}\le\frac{80}{49},}
\tag{24}
\]

\[
0\le Q_\theta(t)-\sum_{j=0}^{J}\mathscr R_\theta^jA_\theta(t)
 \le\chi_\theta r_\theta^{J+1},\qquad
\chi_\theta=\frac{56}{(50-\theta)^2}.
\tag{25}
\]

The inequalities hold for every t >= 0 and every J >= 0. Q_theta is the Laplace transform of a finite POSITIVE measure of total mass chi_theta. In particular the complete response is not only a formal Taylor jet.

**Difference-quotient proof.** For h>0 put L_+=L_(theta+h). Subtract (19) with the scale mixture split at theta:

\[
L_+-L_\theta
 =\int(L_++L_\theta)(ct)(L_+-L_\theta)(ct)\mu_\theta(dc)
 +h\int L_+(ct)^2(\mu_W-\mu_B)(dc).
\]

By (11) the last integral equals -h t^3 A_+(t). Thus q_h=-(L_+-L_theta)/(h t^3) solves

\[
q_h=A_++\mathscr R_{\theta,h}q_h,
\quad \mathscr R_{\theta,h}q=\int c^3(L_++L_\theta)(ct)q(ct)\mu_\theta(dc).
\]

Its norm is at most r_theta<1. Formula (15) already bounds q_h uniformly and gives its continuous origin value. The family L_theta is continuous uniformly on [0,infinity): weak convergence controls each compact t-interval, while (16) supplies a uniform vanishing tail. It follows that R_(theta,h) -> R_theta in operator norm.

A_+ -> A_theta uniformly as well. On compact t-intervals this follows from weak convergence and uniform fourth moments of S. For its entire tail, exp(-x)<=1/x and (13) give A_theta(t)<=t^(-1) E S_theta^2 integral_0^1 kappa(v)/v dv <=16/(15t), uniformly in theta. This justifies uniform convergence, not just coefficient convergence. The resolvent identity now proves (23) in C_b. The left quotient is handled identically; the same estimates give continuous dependence of Q_theta.

Each term of the series is a positive Laplace transform: the action on a positive measure beta is multiplication by mass 2E C^3 and pushforward of the independent sum X_theta+Y by the c^3-biased scale. Summable masses prove the positive measure statement. At zero its mass is b_theta/(1-r_theta)=chi_theta. Geometric summation gives (25). Evaluation of the inverse applied to 1 at zero gives the lower equality in (24). □

### An ordinary random-variable representation

Let V have density 960 kappa on [0,1]. Let S_theta^[3] denote the pair law biased by S^3/E S^3. Set Y_theta=V S_theta^[3], independently. Let C_theta^[3] have probability measure c^3 mu_theta(dc)/a_3(theta).

The probability law Z_theta defined by

\[
Z_\theta\overset d=
\begin{cases}
Y_\theta,&\text{with probability }1-r_\theta,\\
C_\theta^{[3]}(X_\theta+Z_\theta'),&\text{with probability }r_\theta
\end{cases}
\tag{26}
\]

uses fresh independent variables in each branch. The recursion terminates after a geometric number of repetitions almost surely. It yields

\[
\boxed{Q_\theta(t)=\chi_\theta E e^{-tZ_\theta}.}
\tag{27}
\]

This is an exact full-law representation; truncating its geometric depth has the complete mass error in (25). No zeta zero defines any of its variables. All its fixed positive moments are finite, uniformly in theta: the geometric depth has all moments, the scales are at most one, and the source variables have the required moments.

## 4. Complex Mellin response with all small-value contributions retained

Use c=pi/6, V_theta=cS_theta, and define

\[
M_\theta(s)=E V_\theta^{s/2},\qquad
H_\theta(s)=\frac{M_\theta(s)+M_\theta(1-s)}{2(1+M_\theta(1))}.
\tag{28}
\]

By (18) and the uniform positive moments, these are holomorphic on Re s>-10 and -10<Re s<11 respectively, locally uniformly in theta. We assert no entire continuation for intermediate theta. Reflection, conjugation and H_theta(0)=H_theta(1)=1/2 hold exactly.

Let Z_theta in (26) be independent of a fresh X_theta, and put R_theta=X_theta+Z_theta. Then

\[
\boxed{E R_\theta^{-b}<400\qquad(2\le b\le4,\ 0\le\theta\le1).}
\tag{29}
\]

**Proof of the complete negative-moment bound.** Equation (13) gives E V^-b <=960/(11/2-b)<=640 for b<=4. Also E S^3>=8 and E S^(3-b)<=1+E S+E S^-1<=29/8 on 2<=b<=4. On the first branch of (26), R>=Y and its inverse moment is at most 640*(29/8)/8=290.

On every continuing branch R>=X+C^[3]X'. Arithmetic–geometric mean gives

\[
E R^{-b}\le2^{-b}E(C^{[3]})^{-b/2}(E X^{-b/2})^2.
\]

Here E(C^[3])^-b/2=a_(3-b/2)/a_3<=16/3, and (17) plus Lyapunov gives E X^-b/2<=25/3 for 1<=b/2<=2. Thus this branch is bounded by 10000/27<400, even without the favorable factor 2^-b. Both cases together prove (29). The remainder Z' has not been replaced by zero as an equality; it was dropped only in this valid inverse-moment upper bound. □

### Theorem BFC4: exact complex response

For p=s/2 with -1<Re p<1,

\[
\boxed{
\partial_\theta M_\theta(s)
 =2\chi_\theta c^p p(p-1)(p-2)E R_\theta^{p-3}.
}
\tag{30}
\]

At p=0 use the removable value. In particular, for 0<=Re s<=1,

\[
|\partial_\theta M_\theta(s)|
 \le800\chi_\theta |p(p-1)(p-2)|.
\tag{31}
\]

This is a complex response formula for the exact fixed-law path, not a formula for the old discrete step. All normalizing derivatives of H_theta follow by the ordinary quotient rule; they are not omitted.

**Proof.** First take -1<Re p<0. Negative-moment inversion gives M=c^p/Gamma(-p) integral t^(-p-1)L_theta(t)^2 dt. Differentiate using (23),(27). The derivative is

\[
-\frac{2\chi_\theta c^p}{\Gamma(-p)}
 \int_0^\infty t^{2-p}E e^{-tR_\theta}dt.
\]

The full integral equals Gamma(3-p) E R^(p-3). Since Gamma(3-p)/Gamma(-p)=-p(p-1)(p-2), this proves (30). For 0<Re p<1 use the standard subtracted Laplace formula, with L^2-1; its derivative is the same integral. Uniform bounds at both integration ends justify differentiation: (23) pays the origin, and (29) at a slightly larger inverse exponent pays infinity uniformly on compact p-substrips. They also justify continuation through p=0. Positive moments handle the remaining harmless logarithms. Bound (31) follows from c<1 and (29). □

For real 0<s<2, the right side of (30) is positive. This real Mellin ordering is NOT a sign theorem for its complex oscillatory counterpart.

### Exact endpoint identification

At theta=1 the pair variable has Laplace transform pi t/sinh^2(sqrt(pi t)). For real r>0,

\[
E V_1^{-r}
 =\frac{2\pi^{-r}}{\Gamma(r)}\int_0^\infty
       x^{2r+1}\operatorname{csch}^2x\,dx
 =2^{1-2r}\pi^{-r}\frac{\Gamma(2r+2)}{\Gamma(r)}\zeta(2r+1).
\]

Expand csch^2 x=4 sum_(j>=1) j exp(-2jx); positivity justifies the integral. Duplication and the ordinary xi functional equation [D2] identify the answer as 2xi(-2r). All positive and negative moments of this endpoint exist, so analytic continuation proves M_1(s)=2xi(s) for every s. Hence

\[
\boxed{H_1(s)=\xi(s).}
\tag{32}
\]

At theta=0,

\[
M_0(s)=(\pi/15)^{s/2}\Gamma(5+s/2)/\Gamma(5).
\tag{33}
\]

## 5. The gamma endpoint really is zero-safe on the whole critical strip

For completeness this subsection rederives only the required k=5/2 starting case; it does not import an unproved zero property of intermediate laws.

The right-half-plane digamma remainder is

\[
\left|\psi(z)-\log z+\frac1{2z}\right|\le\frac1{12(\Re z)^2}.
\tag{34}
\]

It follows from the integral for psi whose remainder integrand is (1/2)coth(t/2)-1/t, lying strictly between 0 and t/12. The integral is classical [D3]. The two elementary bracket bounds follow by differentiating x cosh x-sinh x and (1+x^2/3)sinh x-x cosh x.

For f(s)=M_0(s), 0<=sigma<=1 and 0<=t<=4, put a=5+sigma/2. The continuous phase is integral from 0 to t/2 of log(pi/15)+Re psi(a+iu). Since a>=5 and sqrt(a^2+u^2)<6, that integrand lies between -31/300 and 9/35+1/300. Its integrated phase lies strictly between -31/150 and 18/35+1/150, inside (-pi/2,pi/2). Both f(s) and f(1-s) therefore have positive real part on this low rectangle.

At |t|>=4,

\[
\partial_\sigma\log|f(\sigma+it)/f(1-\sigma-it)|
\ge \log(\pi/3)+\tfrac12\log(1+4/25)-\tfrac1{10}-\tfrac1{300}
>\frac{77}{7500}>0.
\tag{35}
\]

Use pi>25/8, log(25/24)>1/25 and log(1+x)>=x-x^2/2 at x=4/25 for the last rational lower bound. On sigma=1/2 the ratio has modulus one. Away from that line its modulus is strictly on one side of one, so it cannot equal -1. The reflected sum cannot vanish there. Thus every zero of H_0 in 0<=Re s<=1 is central; below height four there are none. This is an all-height analytic starting theorem, not a root scan. □

## 6. A global zero functional with a uniform, COMPLETE height tail

An interval of source parameters does not itself prevent zeros from entering at high heights. We now price a weighted version of the entire zero set rather than ignoring that issue.

Throughout the larger strip -1/2<=Re s<=3/2, (18) and positive moments give

\[
|H_\theta(s)|<4,\qquad H_\theta(1/2)>1/20,
\tag{36}
\]

uniformly in theta. For the upper bound use V^a<=1+V+V^-1 for -1/4<=a<=3/4; E V=pi/3<4/3 and E V^-1<=15/(4pi)<5/4, so |M|<4 and the denominator of H is at least two. For the lower bound, E S=2 and E S^2=24/5 give P(S>=1)>=5/24 by the elementary Paley–Zygmund/Cauchy inequality. Therefore E V^(1/4)>1/6, while 1+E sqrt(V)<3. This is stronger than the displayed 1/20 bound.

Map the open larger strip to the disk by

\[
w=\tan\big(\pi(s-1/2)/4\big).
\]

Jensen's formula applied at its center gives sum log(1/|w_rho|)<log80<5 for all its zeros, with multiplicity. If 0<=Re rho<=1, write x=pi(Re rho-1/2)/4 and y=pi Im rho/4. Then

\[
1-|\tan(x+iy)|^2=\frac{2\cos(2x)}{\cosh(2y)+\cos(2x)}
 \ge\tfrac12 e^{-\pi|\Im\rho|/2}.
\]

Since -log r >=(1-r^2)/2 for 0<r<1,

\[
\boxed{
\sum_{\substack{H_\theta(\rho)=0\\0\le\Re\rho\le1}}
 m_\rho e^{-\pi|\Im\rho|/2}<20,\quad0\le\theta\le1.
}
\tag{37}
\]

This is a uniform weighted count, not a height census or a bound on the number of zeros by a polynomial in height.

Define the nonnegative functional

\[
\Delta(\theta)=\sum_{\substack{H_\theta(\rho)=0\\0<\Re\rho<1}}
 m_\rho(\Re\rho-1/2)^2\Re\rho(1-\Re\rho)
 e^{-\pi|\Im\rho|}.
\tag{38}
\]

Both signs of the ordinate and every multiplicity are included. Each off-central zero in the open critical strip contributes positively; central zeros contribute zero. The factor Re rho(1-Re rho) makes crossings of the strip's vertical edges continuous in this bookkeeping.

### Theorem BFC5: uniform zero-tail and endpoint meaning

With Delta_T the same sum restricted to |Im rho|<=T,

\[
\boxed{0\le\Delta(\theta)-\Delta_T(\theta)
 \le\frac5{16}e^{-\pi T/2}\quad(T\ge0,\ 0\le\theta\le1).}
\tag{39}
\]

Delta is continuous on [0,1], and

\[
\boxed{\Delta(0)=0,\qquad \Delta(1)=0\ \Longleftrightarrow\ \mathrm{RH}.}
\tag{40}
\]

**Proof.** Writing d=Re rho-1/2, the real weight is d^2(1/4-d^2)<=1/64. Combine this with (37) to prove (39), including every omitted zero. For continuity, at any fixed parameter choose a sufficiently large bounding rectangle whose boundary contains no zero. Local uniform continuity of H_theta and the argument principle give continuous finite zero multisets inside, retaining multiplicity. Extend the real weight by zero outside [0,1]; it is continuous at the two edges. Thus finite weighted sums are continuous locally in theta. Formula (39) gives a uniform tail, so the full sum is continuous. The starting theorem proves Delta(0)=0. At theta=1, (32) and the classical critical-strip theorem for zeta [D4] give (40). □

Uniformly small tails do NOT force Delta to be zero. In particular zeros may enter from arbitrarily high heights with arbitrarily small positive contributions. The theorem permits that and bounds their combined weight; it does not prohibit entry.

## 7. The exact local collision test: the presently OPEN sign

This section attacks how zeros could leave the line along the new path. It is not an assertion that they cannot.

At a simple zero rho(theta), in s coordinates,

\[
\rho'(\theta)=-\frac{\partial_\theta H_\theta(\rho)}{H_\theta'(\rho)}.
\tag{41}
\]

The changing positive normalization in (28) drops from this ratio only because its numerator is evaluated at a zero. At a simple central zero, reflection and conjugation force the motion to remain central locally. Noncentral creation must involve a multiple zero or entry across a boundary; no global exclusion follows from the simple-root formula.

Use z coordinates s=1/2+iz and the unnormalized real holomorphic function on a horizontal strip

\[
F_\theta(z)=M_\theta(1/2+iz)+M_\theta(1/2-iz).
\]

At a real double zero z=t0 and theta=theta0, assume F_zz !=0 and F_theta !=0. A local two-zero factor is ((z-c(theta))^2-D(theta)) times a nonvanishing factor, with real coefficients for real theta. Its discriminant derivative is

\[
D'(\theta_0)=-2F_\theta/F_{zz}.
\tag{42}
\]

Set p=1/4+it0/2, c=pi/6, and

\[
A_\theta(t)=\Re\{c^p p(p-1)(p-2)E R_\theta^{p-3}\},\qquad
Q_\theta(t)=\Re E[V_\theta^p(\log V_\theta)^2].
\]

Equations (28),(30) give EXACTLY

\[
F_\theta=4\chi_\theta A_\theta(t),\qquad
F_{zz}=-\tfrac12Q_\theta(t),\qquad
\boxed{D'(\theta_0)=16\chi_\theta\,A_\theta(t_0)/Q_\theta(t_0).}
\tag{43}
\]

The simultaneous double-zero constraints are

\[
\Re E V_\theta^p=0,\qquad
\Im E[V_\theta^p\log V_\theta]=0.
\tag{44}
\]

A positive value in (43) describes a nonreal pair becoming two real roots as theta increases; a negative value describes birth of a nonreal conjugate pair. This is the ordinary fold convention in z, not an assertion about the sign at an actual source collision. C1 parameter dependence and holomorphy in z suffice: the two-zero polynomial coefficients may be constructed by contour power sums. No analyticity in a complex theta neighborhood is assumed.

At a positive-height fold, with center c(theta)>0 and sufficiently small |D|, the full reflected quartet contributes exactly

\[
\boxed{(-D(\theta))_+\,[1+4D(\theta)]e^{-\pi c(\theta)}}
\tag{44a}
\]

to (38). For D<0 the four zeros have horizontal displacements +/-sqrt(-D) in s and heights +/-c; their four weights sum to the displayed expression. For D>=0 they are central and contribute zero. Thus an ordinary fold is accounted for with its entire quartet, not by deleting two roots. This formula is local near D=0 and is not extended past the vertical critical-strip boundary D=-1/4.

For a simple off-central root, the derivative of its weight in (38) is likewise explicit. If h(sigma)=(sigma-1/2)^2 sigma(1-sigma), it is

\[
e^{-\pi|t|}\{h'(\sigma)\Re\rho'
 -\pi\operatorname{sgn}(t)h(\sigma)\Im\rho'\}.
\tag{45}
\]

The formula holds where the root is simple, t!=0, and remains in the open strip. At collisions or boundary crossings use the complete multiplicity-weighted functional, not an unproved termwise differentiated infinite series.

### What was attempted, and what does not follow

The hopeful step was to use positivity of the resolvent measure in (27) to deduce a nonnegative value of (43) at every actual double zero, or a nonpositive TOTAL production of Delta over the homotopy. Neither implication has been established. In (43), A and Q are oscillatory real parts of two different, source-defined measures. Their positive underlying measures do not determine the sign of their product. The conditions (44) must be used, not discarded.

Even a proof of the desired sign at every nondegenerate double zero would need handling of higher collisions and boundary entry. The uniform tail (39) removes an unpriced infinite sum from the weighted problem, but does not by itself prove a favorable signed flux. Monotonicity of Delta would be sufficient and possibly stronger than RH: intermediate homotopy laws might have transient nonreal zeros even if the endpoint is entirely central.

A valid end-to-end statement is that a proof of nonpositive NET weighted production Delta(1)-Delta(0), retaining every event and the entire tail, would imply RH by (40). This packet does NOT prove that statement. Nor does it claim that the source's stable response inverse is a positive-metric realization of the Xi zero spectrum.

## 8. What this changes relative to the earlier window programme

The old discrete orbit had a known limit but an unresolved simultaneous depth/height zero theorem. Here every parameter is already a fully defined fixed law, and the endpoint is exactly xi. The source derivative has a uniform norm inverse <2 and an explicitly samplable positive measure. A global nonnegative zero diagnostic has a uniform spectral tail over the whole parameter interval. These are positive, all-parameter results, not merely a finite moment fit.

Nevertheless the previous #860/#870 high/low zero theorems concern DIFFERENT intermediate functions and are not transferred here. No protected height has increased in this pass, and no actual zero collision or new Xi value has been numerically evaluated. The new route's remaining task is source-specific complex zero production, with (43) as a concrete local test and (38)-(39) as complete global accounting. Its sign remains substantial research.

## References and reading boundaries

[B] P. Biane, J. Pitman, M. Yor, *Probability laws related to the Jacobi theta and Riemann zeta function and Brownian excursions*, arXiv:math/9912170. The abstract/metadata were freshly read; the normalization needed here is derived above from the displayed Laplace transform, rather than depending on an unread numbered proposition.

[D1] NIST DLMF 5.12.1, Euler's beta integral: https://dlmf.nist.gov/5.12 .
[D2] NIST DLMF 25.4, xi completion and functional equation: https://dlmf.nist.gov/25.4 .
[D3] NIST DLMF 5.9, Binet/digamma integrals: https://dlmf.nist.gov/5.9 .
[D4] NIST DLMF 25.10, the classical location of all nontrivial zeta zeros in the open critical strip: https://dlmf.nist.gov/25.10 .

Repository sources: #874 at 80844a3778390ff744235cf2b021cfaea80ff512 (fresh publication metadata; motivation, not a premise of the new proofs); #853 beta/uniform order and #850 gamma starting law (their supplied manuscripts and the conversation's exact constructions informed the rederivations); #872 at 45281093179434e08d28d8e589a8c70d70ead5b9 (principal proof read for the separate fixed-source linearization; its spectral assertions are not imported); #856 at f21012f63adac789653e9bf6dbb8c309fa5fe7c5 (fresh body-level failure boundary only, not a replay). No exhaustive repository review or novelty search is claimed.
