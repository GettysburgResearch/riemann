# BRN26: a Brownian renormalization and its native defect companion

**Status: PROPOSED component proofs and exploratory RH route; independent review required. RH is not proved.**

The new direction is to construct an exact, convergent nonlinear source flow and extract a companion from its *difference*, rather than self-adjointize the nonnormal theta operator. The companion below is prescribed by positive random variables, not fitted to zeta zeros. Its required phase inequality is OPEN, and could be false even if RH is true.

## 1. Attribution, normalization and the new scope

The Brownian/zeta identity and the distributional fixed point are classical. We use Biane–Pitman–Yor, *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*, arXiv:math/9912170, Proposition 1 and equations (43)–(45). Their paper already identifies the fixed law and notes uniqueness from moments. There is no priority claim for that identity, smoothing transforms, Wasserstein contraction, convex order, Mellin continuation, or the Hermite–Biehler mechanism.

Here those inputs are developed into an explicit two-seed squeeze, quantitative expanding-disk convergence, and an exact positive-law formula for the renormalized difference. The last formula supplies a specific new companion to investigate relative to the inspected repository programme. No exhaustive external or all-branch originality audit was performed.

Use the entire function

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
\xi(0)=\xi(1)=\tfrac12,\qquad \Xi(z)=\xi(\tfrac12+iz).
\]

The product formula initially holds away from its removable points. All identities with xi below concern its entire continuation. Probability powers use the real logarithm: \(x^q=\exp(q\log x)\) for \(x>0\). All copies appearing in a sum or a distributional recursion are independent unless explicitly coupled in a proof.

## 2. A completely specified source iteration

Let \(U\) be uniform on \([1,2]\), and set

\[
\mathcal R(X)=U^{-2}(X+X'),\qquad
X_0^-=1,\quad X_0^+\sim\operatorname{Exp}(1),\qquad
X_{n+1}^\pm\stackrel d=\mathcal R(X_n^\pm).
\tag{1}
\]

Write \(L_n^\pm(t)=\mathbb E e^{-tX_n^\pm}\). Then

\[
L_{n+1}^\pm(t)=\int_1^2 L_n^\pm(t/u^2)^2\,du,
\qquad L_0^-(t)=e^{-t},\quad L_0^+(t)=(1+t)^{-1}.
\tag{2}
\]

Let

\[
a_k=\mathbb E U^{-2k}=\frac{1-2^{1-2k}}{2k-1}\ (k\ge1),\quad a_0=1,
\qquad r=2a_2=\frac7{12}.
\tag{3}
\]

Every iterate has mean one. A tree realization has \(2^n\) leaves, with coefficient of a leaf equal to the product of \(U^{-2}\) over its ancestors. Siblings share the multiplier at their parent. This sharing must not be replaced by independent multipliers on the two outgoing edges.

### BRN26-1: whole-law identification and contraction

The unique mean-one fixed law with finite second moment is

\[
X_* =\frac6{\pi^2}\sum_{j\ge1}\frac{E_j}{j^2},\qquad
L_*(t)=\frac{\sqrt{6t}}{\sinh\sqrt{6t}},\qquad
\operatorname{Var}X_*=\frac25,
\tag{4}
\]

where the \(E_j\) are independent mean-one exponentials. The series converges almost surely and in \(L^2\). The quotient in (4) has its removable value one at zero.

**Proof.** The coefficient sum is one and the squared-coefficient sum is \(2/5\), by the classical evaluations of \(\sum j^{-2}\) and \(\sum j^{-4}\). The Euler product for sinh gives the Laplace transform. For \(a=\sqrt{6t}\), direct integration gives

\[
\int_1^2 (a/u)^2\operatorname{csch}^2(a/u)\,du
=a[\coth(a/2)-\coth(a)]=a/\sinh a.
\]

This proves the fixed point for real \(t>0\), hence equality of probability laws. For any coupling \((X,Y)\) of mean-one laws, use independent copies of this coupling and the same \(U\). Since \(\mathbb E(X-Y)=0\),

\[
\mathbb E\big|U^{-2}(X+X'-Y-Y')\big|^2
=2a_2\mathbb E|X-Y|^2.
\]

Taking infima gives \(W_2(\mathcal R\mu,\mathcal R\nu)^2\le rW_2(\mu,\nu)^2\). This proves uniqueness and convergence to the already constructed fixed law, without assuming all moments for an arbitrary competing law. In particular

\[
W_2(X_n^-,X_*)^2\le\tfrac25r^n,\qquad
W_2(X_n^+,X_*)^2\le\tfrac75r^n.
\tag{5}
\]

The upper constant comes from an independent initial coupling, not an asserted optimal coupling. \(\square\)

The classical BPY normalization is \(X_*=3\Sigma_1\). With

\[
Z_n^\pm=(X_n^\pm+\widetilde X_n^\pm)/2,\quad Z_*=(X_*+\widetilde X_*)/2,
\]

one has \(Z_*=3Y^2/\pi\), where BPY's \(\mathbb E Y^s=2\xi(s)\). Consequently

\[
M_*(q):=\mathbb E Z_*^q=(3/\pi)^q\,2\xi(2q),\qquad
F_n^\pm(s):=\tfrac12(\pi/3)^{s/2}\mathbb E (Z_n^\pm)^{s/2}.
\tag{6}
\]

The critical line in **q coordinates is \(\Re q=1/4\)**, not \(1/2\). An approximant zero is not a zeta zero.

### BRN26-2: a two-sided Laplace squeeze, including its entire error

For every real \(t\ge0\),

\[
L_n^-(t)\uparrow L_*(t)\downarrow L_n^+(t),\qquad
0\le L_n^+(t)-L_n^-(t)\le\tfrac12t^2r^n.
\tag{7}
\]

Their variances are exactly

\[
v_n^-=\tfrac25(1-r^n),\qquad
v_n^+=\tfrac25+\tfrac35r^n.
\tag{8}
\]

For complex \(\Re t\ge0\), useful absolute bounds are

\[
|L_n^--L_*|\le\tfrac15|t|^2r^n,\qquad
|L_n^+-L_*|\le\tfrac7{10}|t|^2r^n.
\tag{9}
\]

**Proof.** The map (2) preserves order on nonnegative real Laplace transforms. Jensen and \(\mathbb E(2/U^2)=1\) give \(\mathcal R(e^{-t})\ge e^{-t}\). For the upper seed put \(J(t)=\int_1^2(u^2+t)^{-1}du\). Integration by parts gives

\[
\frac1{1+t}-\int_1^2\frac{u^4}{(u^2+t)^2}\,du
=\frac t2\left[3J(t)-\frac1{1+t}-\frac2{4+t}\right].
\tag{10}
\]

The random variable \(A=U^{-2}\) lies in \([1/4,1]\) and has mean \(1/2\). The concave function \(a/(1+ta)\) is above its endpoint chord. Averaging that chord gives
\(J(t)\ge[1/(1+t)+2/(4+t)]/3\), proving the upper supersolution. The monotone limits are (4) by (5).

For the error, condition on the tree weights \(c_v\). The lower law has conditional value \(S=\sum c_v\). The exponential-leaf law has conditional mean \(S\) and variance \(\sum c_v^2\); the fixed-law leaves have conditional variance \((2/5)\sum c_v^2\). For \(f(x)=e^{-tx}\), \(\Re t\ge0\), Taylor's integral remainder gives \(|f(x)-f(S)-f'(S)(x-S)|\le |t|^2(x-S)^2/2\). Also \(\mathbb E\sum c_v^2=r^n\). This gives (7),(9), with triangle inequality for the second bound in (9). It is not a relative error near a zero. Finally \(v_{n+1}=rv_n+1/6\), proving (8). \(\square\)

## 3. Quantitative convergence to the whole xi function

### BRN26-3: all complex moments and growing disks

The lower \(F_n^-\) is entire. The upper \(F_n^+\) is holomorphic at least in \(\Re s>-2^{n+2}\). Both converge locally uniformly on the entire plane to the literal \(\xi\), with eventual holomorphy on each compact set. More explicitly, for every integer \(n\ge1000\), put

\[
R_n=\frac{n}{100\log(n+2)}.
\]

Then

\[
\sup_{|q|\le R_n}|\mathbb E(Z_n^\pm)^q-M_*(q)|\le e^{-n/5},\qquad
\sup_{|s|\le2R_n}|F_n^\pm(s)-\xi(s)|\le e^{-n/5}.
\tag{11}
\]

The constants are deliberately conservative. This is a written all-depth theorem, not a numerical certificate for depth 1000.

**Proof.** For every nonnegative integer \(k\), all seeds, iterates and the limit have \(\mathbb E X^k\le k!\). For iterates use

\[
m_{n+1,k}=a_k\sum_{j=0}^k\binom kjm_{n,j}m_{n,k-j},
\tag{12}
\]

and \((k+1)a_k\le1\) for \(k\ge1\). For the fixed law use convexity on its positive weighted exponential sum. Jensen transfers the bound to \(Z\).

For inverse moments choose an integer \(k\) with \(2^k>p>0\). Monotonicity and the minimum tree weight give, for \(n\ge k\),

\[
L_n^+(t)\le L_k^+(t)\le(1+t/4^k)^{-2^k}.
\]

The same bound holds for \(L_n^-\) and \(L_*\). Tonelli and the gamma integral therefore give the complete bound

\[
\mathbb E X^{-p}\le N_{p,k}:=4^{kp}\frac{\Gamma(2^k-p)}{\Gamma(2^k)}.
\tag{13}
\]

Again Jensen transfers it to \(Z\). No small-variable tail is omitted. Lower tree values lie in \([2^{-n},2^n]\). For the upper \(Z_n\), its \(2^{n+1}\) exponential leaves and minimum coefficient \(4^{-n}/2\) give inverse moments for \(p<2^{n+1}\). These facts establish the stated holomorphic domains and differentiation under the integrals.

Independent averaging of a mean-zero difference coupling in (5) gives \(W_2(Z_n^\pm,Z_*)^2\le c_\pm r^n\), where \(c_-=1/5,c_+=7/10\). For \(|q|\le R\), take \(K=\lceil R\rceil+1\). For positive \(x,y\),

\[
|x^q-y^q|\le R|x-y|(x^K+y^K+x^{-K}+y^{-K}).
\]

Cauchy–Schwarz and (13) imply, whenever \(n\ge k\), \(2^k>2K\),

\[
\sup_{|q|\le R}|\mathbb E(Z_n^\pm)^q-M_*(q)|
\le R\sqrt{8c_\pm((2K)!+N_{2K,k})}\,r^{n/2}.
\tag{14}
\]

This proves local uniform convergence without invoking a finite zero table. To check the expanding constants, let \(R\ge1\) and choose the least \(k\) with \(2^k\ge4K\). Since each denominator factor of the gamma ratio is at least \(2^{k-1}\),
\(N_{2K,k}\le(16K)^{2K}\), so the prefactor in (14) is at most
\(4R(16K)^K\le4R(48R)^{3R}\).
For \(R=R_n,n\ge1000\), \(R\ge1\), \(k\le n\), \(48R\le n\) and \(\log(4R)\le\log(4n)\le n/100\). Thus its logarithm is at most \(n/25\). The atanh expansion gives \(\tfrac12\log(12/7)>5/19\). This proves an exponent stronger than \(-n/5\). Multiplication by \(\tfrac12(\pi/3)^q\) costs at most \(e^R\le e^{n/100}\), still leaving an exponent below \(-n/5\). \(\square\)

Moment matching accelerates the *Laplace* convergence further. If a positive seed agrees with \(X_*\) through integer moment \(m\), Taylor remainder and (2) give
\(|L_n-L_*|\le C|t|^{m+1}(2a_{m+1})^n\) on \(\Re t\ge0\), with \(C=(\mathbb E X_0^{m+1}+\mathbb E X_*^{m+1})/(m+1)!\). Lower moments remain matched by (12). For example, the mean-one gamma law of shape \(5/2\) matches the first two moments and gives factor \(2a_3=31/80\). This does not preserve Mellin zero geometry or establish an improved version of (11) without further estimates.

## 4. Extract a positive companion from the exact difference

This is the constructive step beyond merely observing that the cascade converges.

Let \(V\) have density \(u^{-4}/a_2\) on \([1,2]\), and let \(Y_n\) be an independent equiprobable mixture of \(X_n^-\) and \(X_n^+\). Define positive variables by

\[
f_{B_0}(x)=2[e^{-x}-(1-x)_+]\quad(x>0),\qquad
B_{n+1}=V^{-2}(B_n+Y_n),\quad C_n=B_n+\widehat Y_n.
\tag{15}
\]

The \(Y_n\) used inside a new recursion and the copy \(\widehat Y_n\) in \(C_n\) are independent of \(B_n,V\). The function in (15) is a probability density because \(e^{-x}\ge1-x\), and its integral is one. Its moments are explicitly

\[
\mathbb E B_0^k=2\left[k!-\frac1{(k+1)(k+2)}\right].
\tag{16}
\]

### BRN26-4: exact finite-depth defect factorization

For every \(n\ge0\), \(t\ge0\),

\[
L_n^+(t)-L_n^-(t)=\tfrac12r^nt^2\mathbb E e^{-tB_n},
\tag{17}
\]

and for every \(\Re q>0\),

\[
\boxed{\quad
\mathbb E(Z_n^+)^q-\mathbb E(Z_n^-)^q
=r^n2^{-q}q(q-1)\,\mathbb E C_n^{q-2}.
\quad}
\tag{18}
\]

This retains the whole finite-depth probability laws, not a truncated moment expansion. It is a signed Mellin identity: the right side is negative for real \(0<q<1\), positive for real \(q>1\), and its complex phase is not determined by positivity of \(C_n\).

**Proof.** Direct integration of (15) gives
\(\mathbb E e^{-tB_0}=2[(1+t)^{-1}-e^{-t}]/t^2\), with its removable value one. Subtract (2) and factor a difference of squares. The tilted density of \(V\), \(r=2a_2\), and the Laplace transform of the mixture \(Y_n\) then prove (17) by induction. Multiplying (17) by \(L_n^++L_n^-\) gives

\[
(L_n^+)^2-(L_n^-)^2=r^nt^2\mathbb E e^{-tC_n}.
\]

For \(0<\Re q<1\), the Mellin–Laplace difference formula for the sums \(X_n+\widetilde X_n\) gives

\[
\frac{r^n}{\Gamma(-q)}\int_0^\infty t^{1-q}\mathbb E e^{-tC_n}\,dt
=r^nq(q-1)\mathbb E C_n^{q-2}.
\]

Scaling the sums by two proves (18). The integral is absolutely convergent: for \(n\ge1\), \(C_n\ge\widehat Y_n\) and each component of \(Y_n\) has inverse moments of order less than two; for \(n=0\), \(B_0\) has inverse moments of every order less than three, as its density is \(O(x^2)\) at zero. Positive moments of all orders are finite. Both sides are holomorphic on \(\Re q>0\), so the identity theorem extends the result throughout that half-plane, including the removable zero at \(q=1\). \(\square\)

### BRN26-5: an independent, limiting perpetuity companion

Let \(V_j\) be iid with the density just specified, and let \(X_{*,j}\) be independent copies of (4). The series

\[
B_*:=\sum_{j\ge1}\left(\prod_{i=1}^jV_i^{-2}\right)X_{*,j},\qquad
C_*:=B_*+X_{*,0}
\tag{19}
\]

converges almost surely and in \(L^1\), and

\[
\mathbb E B_*=\frac{93}{47},\quad \mathbb E C_*=\frac{140}{47}.
\tag{20}
\]

The \(C_*\) law has every positive and negative real moment. Its Mellin transform is entire. Moreover \(C_n\) converges in law to \(C_*\), with locally uniform convergence of their Mellin transforms once the necessary negative moments exist. Thus on \(\Re q>0\), locally uniformly,

\[
r^{-n}[\mathbb E(Z_n^+)^q-\mathbb E(Z_n^-)^q]
\longrightarrow 2^{-q}q(q-1)\mathbb E C_*^{q-2}.
\tag{21}
\]

**Proof.** Set \(b_j=\mathbb E V^{-2j}=a_{j+2}/a_2\). In particular \(b_1=93/140<1\). The expectation of the positive series (19) is \(\sum_{j\ge1}b_1^j=93/47\), proving convergence and (20). It satisfies \(B_*\stackrel d=V^{-2}(B_*+X_*)\).

For completeness, all moments can be controlled without an unquantified perpetuity theorem. Put \(D_0=1\) and recursively choose

\[
D_k=\max\left\{\mathbb E B_0^k,
\frac{b_k}{1-b_k}\sum_{j=0}^{k-1}\binom kjD_j(k-j)!\right\}.
\tag{22}
\]

These finite rational constants bound \(\sup_n\mathbb E B_n^k\), by (15), since \(\mathbb E Y_n^j\le j!\). They also bound moments of partial sums in (19), starting from zero, so bound \(B_*\) by monotone convergence. All positive moments of \(C_n,C_*\) are consequently uniformly bounded at each order. For inverse moments use \(C_n\ge\widehat Y_n\), (13), and \(C_*\ge X_{*,0}\).

Couple \(Y_n\) with \(X_*\) using the two couplings in (5), obtaining \(\mathbb E|Y_n-X_*|\le\sqrt{9/10}\,r^{n/2}\). Couple the affine recursions with the same independent \(V\). Their \(L^1\) distance satisfies
\(d_{n+1}\le b_1d_n+b_1\sqrt{9/10}\,r^{n/2}\). An independent initial coupling has finite \(d_0\), and this recursion tends to zero. Hence \(C_n\to C_*\) in \(W_1\). The uniform positive/inverse moments supply uniform integrability for each complex power and local bounds on every compact q-set. They justify locally uniform Mellin convergence by truncation to a positive compact x-interval and the same bounds on its two tails. This proves (21). \(\square\)

The fixed companion is calculable without iterating the two original laws. If \(P(t)=\mathbb E e^{-tB_*}\), then

\[
P(t)=\frac1{a_2}\int_1^2u^{-4}P(t/u^2)L_*(t/u^2)\,du.
\tag{23}
\]

Iterating (23) from \(P_0=1\) gives the truncated series in (19). Its omitted mean is \((93/47)b_1^m\) after m steps; on \(\Re t\ge0\) its complete Laplace error is at most \(|t|(93/47)b_1^m\). This is an analytic truncation bound, not a directed quadrature certificate.

## 5. A concrete alternative to the bounded-metric strategy

Define, with no zero locations in its definition,

\[
G(s)=\tfrac12(\pi/6)^{s/2}(s/2)(s/2-1)\,
\mathbb E C_*^{s/2-2},
\tag{24}
\]

\[
A(z)=\Xi(z),\qquad
B(z)=\frac{G(1/2+iz)-G(1/2-iz)}{2i}.
\tag{25}
\]

Both \(A,B\) are real entire in z; \(A\) is even and \(B\) is odd. Equation (21) says that \(G\) is precisely the limit of \(r^{-n}(F_n^+-F_n^-)\), initially on \(\Re s>0\). Its independent definition (24) is entire. This is a native *defect companion*, not a fitted real-zero polynomial or an unspecified metric.

**The proposed closing target is the following band phase inequality:**

\[
\boxed{\quad
\operatorname{Im}\big(A(x+iy)\overline{B(x+iy)}\big)>0
\quad\text{for every real }x\text{ and }0<y<1/2.
\quad}\tag{OPEN-BRN}
\]

Its sufficiency is elementary: a zero of \(A\) in that band would make the left side zero. Classical zeta zero localization places every possible nonreal zero of \(\Xi\) in \(|\Im z|<1/2\); real-type reflection handles the lower half. Thus OPEN-BRN would imply RH. Equivalently, the strict inequality is
\(|A+iB|>|A-iB|\) on this band, by the exact difference-of-squares identity. This is a **band** Hermite–Biehler-type condition, not an asserted entire-upper-half-plane de Branges space or a canonical system already constructed. The companion might fail this stronger sufficient condition even under RH. No converse is asserted.

At real x, its infinitesimal boundary diagnostic is the Wronskian
\(A'(x)B(x)-A(x)B'(x)\). Neither its global sign nor the interior phase sign is proved. The exact recursion (23), together with the sinh source and reflection in (25), is the proposed place to attack this sign. Positive Laplace transforms and real-variable monotonicity alone do **not** prove it.

An alternative, weaker dynamic target would allow transient spurious zeros and establish a shrinking horizontal strip for **all** zeros of \(F_n\) on growing windows. Equation (11) would then supply the full limit passage, including multiplicities. Such a confinement theorem is also unproved; a plot of a few tracked roots is not one.

## 6. Computation-ready exact equations and the failed shortcut

For \(H_n(x)=L_n(e^x)\),

\[
H_{n+1}(x)=\tfrac12\int_0^{\log4}e^{y/2}H_n(x-y)^2\,dy,
\quad
(2t\partial_t-1)L_{n+1}(t)=L_n(t)^2-2L_n(t/4)^2.
\tag{26}
\]

The binary tree can therefore be evaluated through a one-dimensional nonlinear convolution. A differentiated version propagates \(D_n=\partial_xH_n\). For \(0<\Re q<1\),

\[
\mathbb E Z_n^q=
\frac{2^{-q}}{\Gamma(1-q)}
\int_{-\infty}^{\infty}e^{-qx}[-2H_n(x)D_n(x)]\,dx.
\tag{27}
\]

Equation (23) is a second, *linear* logarithmic convolution for the prescribed companion. These formulas are exact; the supplied floating implementations are not certified realizations of them.

Initial scouting suggested upper-seed roots approaching the quarter-line from the right. Broader scouting found apparent exceptions, including q approximately \(0.005828+15.112501i\) at depth four and \(0.215531+15.238210i\) at depth five. Those are zeros reported for changed approximants, **not** zeta zeros; they have not been interval isolated. They are sufficient reason not to adopt an all-depth one-sided zero-preservation conjecture. Some low-depth/high-frequency root searches were unstable or failed to converge; retain that evidence boundary.

In contrast, a small noncertifying scout of (25) found the proposed phase orientation positive at its inspected points. This is an entry diagnostic only, not a lower bound on a continuum region or evidence establishing OPEN-BRN. Its purpose is to test a *specified* companion before investing in a global sign proof.

The resulting research position is asymmetric and explicit: the whole-source construction, squeeze, convergence, and companion formulas have complete proposed proofs above. The all-band complex phase inequality remains the substantive RH-facing task.
