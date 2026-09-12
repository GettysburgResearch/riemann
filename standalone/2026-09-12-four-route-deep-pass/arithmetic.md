# Native arithmetic cancellation: proof review and a growing counterfamily

The arithmetic route has a valid-looking chain from an upper bound on one
explicit native scalar quantity to RH. Its current advance is a sharper
description of that quantity, not a new bound of the required size. The
generalized Littlewood argument, every-prefix energy lower bound, polynomial
trace criterion, and fourth-logarithmic collision diagonal survive the
checks below. None supplies the signed covariance estimate.

Two deductions clarify the next step. First, the native covariance is the
annular reciprocal-Mobius energy minus its diagonal, up to an error smaller
than four. Second, a nonnative family preserving normalization, coefficient
caps, Liouville signs, exact balance and its own reciprocal crossing has
covariance-to-diagonal ratio tending to positive infinity. Consequently even
a bounded positive covariance ratio cannot follow from those structural
conditions alone. The new counterfamily has a proof independent of numerical
extrapolation; its small examples still have negative covariance.

The deductions here are proposed mathematical arguments, not external referee
acceptance or a formal proof. Their exact hypotheses distinguish native
statements from changed-source obstructions.

## 1. Source map and current status

The following frozen objects were used. All four packets are proposed
research components, and none asserts that RH has been completed.

| Source | Frozen head and manuscript | Mathematical role |
|---|---|---|
| XCC26, #848 | `99101457b32b6f10f4eda88ca998048404b860ea`, `standalone/2026-09-12-astra-crossing-cofinal/PROOF.md` | Exact native energy exponent, cofinal crossings, completed Newton source and covariance |
| DG26, #866 | `cb05d3052611bd1804459887e84fdec3cb7064af`, `standalone/2026-09-12-astra-polynomial-degree-growth/PROOF.md` | Positive polynomial trace and RH-equivalent sparse subpower target |
| #869 | `6603f8b04f9a2d073123a328ac0298a498c93a96`, `standalone/2026-09-12-three-route-completion/arithmetic/PROOF.md` and `BOUNDARY_CHANNELS.md` | Sharp trace/operator exponent and complete finite source adapters |
| #875 | `be149104721ae7b65b624c100118edfd7b76b69b`, `standalone/2026-09-12-astra-collision-chain-flow/ARITHMETIC.md` | Matching lower bound for the collision diagonal |

The current #866 proof is byte-identical to its earlier head `14b20cc...`:
both give Git blob `c68170e2dacd23c188c9e71482e51fe63566b587`. The changed
head adds its previously absent checker and revises reproduction documents;
it does not change the theorem or obtain a stronger upper estimate.

Throughout, mu is ordinary Mobius, lambda is Liouville, and

\[
 m(x)=\sum_{n\le x}\mu(n)/n,\quad M(x)=\sum_{n\le x}\mu(n),\quad
 F_Y=\sum_{k\le Y}m(k)^2,\quad
 E_Y=\sum_{k\le Y}\frac{M(k)^2}{k(k+1)}.
\]

Write Theta for the supremum of the real parts of nontrivial zeta zeros and
kappa=2Theta-1, so 0<=kappa<=1. The endpoint Theta=1 is possible in an
unconditional argument and must not be silently replaced by a fixed gap.

## 2. Audit of the complete analytic chain

### 2.1 The generalized Littlewood implication is correctly interior

The needed implication is: if zeta has no zeros in Re(s)>theta, with
1/2<=theta<1, then M(x)=O_epsilon(x^(theta+epsilon)). XCC26 reconstructs it
rather than assuming the critical-line case at a displaced boundary.

Fix sigma0 in (theta,1). At height t, center disks at 2+it with radii
r1<1<2-sigma0<r2<R<2-theta. For large |t|, the largest disk is zero-free
and avoids the pole at one. Its branch g=log zeta is fixed by the Euler
logarithm at the center. Euler summation bounds Re(g) by O(log|t|) there;
Borel--Caratheodory bounds |g| on the smaller r2 disk. On the r1 disk,
the absolutely convergent Euler logarithm is O(1). Three circles therefore
gives |g|=O((log|t|)^nu), nu<1, throughout sigma0<=Re(s)<=2.

Exponentiation yields |1/zeta(s)|=O_eta(|t|^eta) for every eta>0 in this
interior region. It is not an estimate on Re(s)=theta. The zero of 1/zeta
at s=1 is harmless at bounded height. The radii exist for each fixed sigma0;
their deterioration as sigma0 approaches theta is permitted.

At half-integer x, take c=1+1/log x and T=x^2 in truncated Perron. The
near-diagonal terms pay |x-n|>=1/2; the off-diagonal terms pay the entire
absolutely convergent sum. The stated O(x log^2(x)/T) error is conservative.
Moving to sigma0=theta+epsilon/2 and using eta=epsilon/8 yields a vertical
cost O(x^(theta+3epsilon/4)) and smaller horizontal costs. No circular
square-root Mertens estimate enters this proof.

The classical critical-line implication is explicitly summarized at the
start of Soundararajan's paper [L2]. The extension just reviewed follows
from the displayed disk argument. Euler summation's continuation domain
and remainder are available in DLMF 25.2.8 [L4].

### 2.2 The lower exponent holds at every prefix

For each Y use the finite source

\[
 C_Y(s)=\sum_{n\le Y}\mu(n)n^{-s}-M(Y)(Y+1)^{-s}.
\]

Its complete energy is E_Y; its cumulative source vanishes after Y+1.
In logarithmic coordinates h_a(t)=e^(-t/2) A_a(e^t), the source norm is
exactly the energy norm. The causal factorial kernel

\[
 d(t)=e^{-t/2}\{\lfloor e^t\rfloor(1-t)+\log(\lfloor e^t\rfloor!)\}
\]

has L1 norm at most six. Its Laplace transform, with s=z+1/2, is
(s-1)zeta(s)/s^2. The pole at one is removed. The convolution y_Y=d*h_C
therefore has norm at most 6sqrt(E_Y), and its transform vanishes at every
nontrivial zero rho with Re(rho)>1/2.

Divisor inversion forces y_Y(t)=h_*(t)=e^(-t/2)(t-t^2/2) before
T=log(Y+1). Direct integration gives norm(h_*)=sqrt(2) and transform
(s-1)/s^3. For rho=beta+i gamma and alpha=beta-1/2>0, Cauchy--Schwarz on
the complete tail gives

\[
 6\sqrt{E_Y}+\sqrt2\ \ge\
 \sqrt{2\alpha}\frac{|\rho-1|}{|\rho|^3}(Y+1)^\alpha.
\]

This applies to every Y, not only an Omega subsequence. Multiplicity and
whether the supremum Theta is attained do not matter. Taking a supremum over
fixed zeros gives the lower exponent kappa. The exact identity
F_Y=E_Y+(Y+1)u_Y^2 gives the same lower exponent for F.

The interior Littlewood estimate supplies the upper exponent when Theta<1.
For Theta=1, the elementary divisor identity gives |m(k)|<=1 and F_Y<=Y.
Together these arguments support the actual limits

\[
 \frac{\log(1+E_Y)}{\log(Y+1)},\quad
 \frac{\log(1+F_Y)}{\log(Y+1)}\ \longrightarrow\ \kappa.
\tag{1}
\]

This is an identity involving an unknown zero abscissa. It evaluates neither
that abscissa nor the size of the native energy.

### 2.3 Crossings, collars and product support

The set X of native weak crossings has mu(Y)!=0 and m(Y-1)m(Y)<=0.
XCC26's Landau argument is sound at the stated scope: the Mellin transform
1/[z zeta(z+1)] is analytic on the real interval z>-1 but has a nonreal pole
in that half-plane. Eventual one-sidedness would give a real convergence
singularity, a contradiction. Hence X is unbounded.

At Y in X, complete c_n=mu(n), n<=Y, by c_(2Y)=-2Y m(Y). Then
|m(Y)|<=1/Y, P_c(1)=0, coefficient cap two, and c_n=lambda(n)b_n with
b_n>=0. Its added complete energy is (Y-1)m(Y)^2<=1/Y. These assertions
remain valid at an exact zero crossing, when the added atom is absent.

Put z=c*c and B=(Y+1)^2-1. The Newton source v=2c-1*z equals mu through
B, because delta-1*c starts at Y+1. It need not agree at (Y+1)^2. The
covariance diagonal must include every product in z, including products
above B whose harmonic-floor term vanishes but whose centered kernel does
not. Dropping such products from the diagonal would change the quantity.

### 2.4 The polynomial trace is a correct alternative coordinate

DG26 uses m_o(x)=sum_(n<=x, odd)mu(n)/n and
Kf(t)=integral_0^1 m_o(t/u)f(u)du/u, 1<t<3. The original endpoint gives
Ep=K(Ap) exactly. Since A is a bijection on odd polynomials through degree
2N-1, Lambda_N is the squared operator norm on that finite space. S_N is
the sum of complete column energies in the orthonormal odd Legendre basis.

The split at u=1/(2N-1) bounds the whole Hilbert--Schmidt norm, with no
dimension factor added to a columnwise bound. It gives the unconditional
ceiling S_N<=800(2N-1). DG26's Mellin coefficient product correctly gives
normal output convergence under a hypothetical power upper bound. Its
critical-line averaged cutoff proves Lambda_N>=c log N eventually, so a
uniform bounded trace is not an admissible completion target.

The smooth high-order Fourier construction in #869 removes DG26's factor-ten
loss: any fixed zero beta>1/2 forces Lambda_N>=c_b N^(b(2beta-1)) at every
sufficiently large N, for every fixed b<1. Its approximation threshold
(1-b)r>1+3b/2 is correct; constants are not uniform as b approaches one.
Consequently both trace and operator logarithmic exponents equal kappa.
The resulting effective-rank bound S_N/Lambda_N=N^o(1) does not bound the
largest mode. The finite boundary adapters keep every mixed term but likewise
do not reduce its magnitude.

### 2.5 The sharp diagonal is a lower theorem, not the missing upper theorem

For K_d(k)=[H_floor(k/d)-H_k+log d]/d, define

\[
 D_Y=\sum_d z(d)^2\sum_{k=Y+1}^{B}K_d(k)^2,\qquad
 C_Y=\sum_{d\ne e}z(d)z(e)\sum_{k=Y+1}^{B}K_d(k)K_e(k).
\]

The ordered-pair convention gives D_Y+C_Y=sum Q(k)^2. XCC26 proves
D_Y<=288 H_(4Y^2)^4. The new #875 lower bound is

\[
 \liminf_{Y\in X}\frac{D_Y}{(\log Y)^4}
 \ge\frac{A_4}{81\,15^4}>0,\qquad
 A_4=\prod_p(1-1/p)^4(1+4/p).
\tag{2}
\]

Its ordered quadruple map (g,h,r,s)->(gr,hs,gs,hr) is injective for pairwise
coprime squarefree variables. Their actual native signs contribute positively
inside each product fiber. For the resulting product d, the interval
d/8<=k<=d/4 lies inside the complete annulus eventually and pays at least
1/(81d). The four-variable Euler factor after removing four zeta factors
has no linear term, so its weighted coefficients are absolutely summable.
Dominated convergence for four harmonic sums proves (2), including the full
prime tail. No independence heuristic or PNT is required.

Thus D_Y is of order log^4Y. The new proof does not bound C_Y, F_Y or S_N
from above. The sufficient condition C_Y<=K D_Y already implied RH from
the earlier diagonal upper bound; (2) makes its denominator a faithful scale.

### 2.6 A classical refinement: the trace is unconditionally o(N)

The displayed DG26 ceiling is not the best unconditional conclusion already
available from classical source estimates. Tao's prime-subsemigroup theorem
gives |m_o(x)|<=1, and his PNT-based limit theorem gives m_o(x)->0 [L5,
Theorems 1.1 and 1.3]. Neither assertion assumes RH.

For completeness the bound has a short elementary proof in this special
case. For integer x, let L_x count powers of two through x and O_x count
positive odd integers through x. Divisor inversion gives
sum_(d<=x, odd)mu(d)floor(x/d)=L_x. Since {x/d}<=1-1/d,

\[
 |x m_o(x)|\le L_x+O_x-\sum_{d\le x,\ d\ {\rm odd}}1/d\le x.
\]

The last inequality uses L_x+O_x<=x+1 (the two sets intersect only at one)
and the harmonic sum at least one. Real x follows by taking its integer
part. In the unchanged DG26 estimate, M_1=1 therefore improves the explicit
constant from 800 to 200:

\[
 S_N\le200(2N-1).
\tag{2a}
\]

The following consequence of m_o(x)->0 is an additional deduction here.
Given epsilon>0 choose X>=3 with |m_o(x)|<=epsilon for x>=X, and split the
kernel into its x=t/u<X and x>=X pieces. The latter satisfies the same
finite-space Hilbert--Schmidt estimate with constant epsilon. The former
has a complete, unrestricted Hilbert--Schmidt norm bounded by

\[
 \int_1^3\frac{dt}{t}\int_t^X |m_o(x)|^2dx\le X\log3.
\]

The triangle inequality for column norms, with d=2N-1, gives

\[
 \sqrt{S_N}\le\sqrt{200}\,\epsilon\sqrt d+\sqrt{X\log3}.
\]

First let N tend to infinity with epsilon and X fixed, then let epsilon
decrease to zero. Thus S_N=o(N), and consequently Lambda_N=o(N),
unconditionally. This is a qualitative PNT-level improvement. It supplies
no fixed delta>0 with S_N=O(N^(1-delta)); its logarithmic exponent can
still be one. It therefore neither narrows the unknown value Theta nor
meets the subpower completion criterion.

## 3. New exact native identity and normalized exponent

Let A_Y=F_B-F_Y and put

\[
 R_Y=4(Y-1)m(Y)^2-4m(Y)\sum_{k=Y+1}^{2Y-1}m(k).
\]

**Proposition 1.** At every native crossing,

\[
 C_Y=A_Y-D_Y+R_Y,\qquad |R_Y|<4.
\tag{3}
\]

**Proof.** The completed reciprocal source t(k) equals m(Y) for
Y<k<2Y and zero for k>=2Y. The native Newton identity gives Q=2t-m on
the entire annulus. Squaring and summing gives
sum Q^2=A_Y+4sum t^2-4sum tm=A_Y+R_Y. Subtract D_Y. Finally
|m(k)|<=1 and |m(Y)|<=1/Y imply

\[
 |R_Y|\le4(Y-1)(Y^{-2}+Y^{-1})=4(1-Y^{-2})<4.
\]

Every term and every annular endpoint is included. QED.

This identity is a deduction from the exact source relations, not a new
upper bound. It removes the appearance that covariance sign is independent
of the same annular energy being targeted. By (2),

\[
 \frac{C_Y}{D_Y}=\frac{F_B-F_Y}{D_Y}-1+O((\log Y)^{-4}).
\tag{4}
\]

Bounded positive C_Y/D_Y is therefore essentially a fourth-logarithmic
annular energy estimate on the selected crossings. In particular C_Y>=-D_Y
exactly by positivity of sum Q^2. Strongly negative normalized covariance
can occur simply because the complete energy is much smaller than its
chosen diagonal decomposition.

**Proposition 2.** Assuming the reviewed component theorems (1)--(2),

\[
 \lim_{Y\to\infty,\,Y\in X}
 \frac{\log(1+\max(C_Y,0)/D_Y)}{\log Y}=4\Theta-2.
\tag{5}
\]

If kappa>0, (1) gives F_B=Y^(2kappa+o(1)), F_Y=Y^(kappa+o(1)); hence
F_Y=o(F_B), D_Y=o(F_B), and the bounded R_Y is negligible. Equation (3)
gives C_Y/F_B->1, proving (5). If kappa=0, positivity and
max(C_Y,0)<=A_Y+4<=F_B+4 imply an upper exponent zero; the logarithm is
nonnegative. This proves the remaining case.

Thus subpower normalized covariance, even along any unbounded subsequence
of X, is RH-equivalent. A fixed bound C_Y<=K D_Y is a stronger sufficient
aspiration; it is not established here as necessary for RH.

## 4. New obstruction: balanced Liouville-coherent sources with unbounded C/D

The isolated positive-covariance fake source in #848 refutes a generic sign
argument. The following growing family refutes the stronger possibility of
deducing ANY fixed covariance-to-diagonal bound from the same relaxed
structural information. It does not satisfy the native divisor equations.

Define the fixed polynomial

\[
 P_0(s)=1-2^{-s}-3^{-s}-5^{-s}+\tfrac13 10^{-s},
 \qquad P_L(s)=P_0(s)\sum_{a=1}^{L}a^{-2s}.
\tag{6}
\]

Let c_L be its coefficients, Y=10L^2, B=(Y+1)^2-1, and z_L=c_L*c_L.
Define K_d, D_L, C_L and Q_L on (Y,B] by precisely the same kernel formulas
as above, but with this explicitly changed source.

**Theorem 3.** These sources have c_L(1)=1, |c_L(n)|<=1, Liouville-coherent
signs, exact P_L(1)=0, and a weak reciprocal crossing at their last support
point Y. Nevertheless

\[
 \sup_L D_L<\infty,\qquad
 \liminf_{L\to\infty}\frac{C_L}{(\log L)^2}>0,
 \qquad \frac{C_L}{D_L}\longrightarrow+\infty.
\tag{7}
\]

### 4.1 All claimed structural constraints hold exactly

The squarefree parts 1,2,3,5,10 are distinct, so (6) has no coefficient
collisions before squaring. Its coefficients at j a^2 are respectively
1,-1,-1,-1,1/3. Their signs equal lambda(j a^2), and their cap is one.
Since P_0(1)=0, the reciprocal sum through Y is zero; immediately before
Y it is -1/(3Y), and the final coefficient is +1/3. The source is already
balanced, so no added collar is required.

This is the crossing of its OWN reciprocal sum, not a claim that Y belongs
to the native set X: for L>=2, Y is not squarefree. Moreover c_L(4)=1 for
L>=2, and sum_(d|4)c_L(d)=1 instead of zero. It deliberately fails the
native divisor equations already at four. Thus (7) is not a counterexample
to the actual source conjecture or to RH.

### 4.2 Uniform bound for the entire diagonal

Let z_0=c_0*c_0, where c_0 denotes the five coefficients of P_0, and let
d_L(a) count factorizations a=bc with 1<=b,c<=L. Then 0<=d_L(a)<=tau(a),
and z_L is the Dirichlet convolution of z_0 with the sequence supported at
squares a^2 with coefficients d_L(a).

In the norm ||v||^2=sum_n |v(n)|^2/n, dilation by d has norm d^(-1/2).
The triangle inequality gives

\[
 \sum_n\frac{z_L(n)^2}{n}
 \le\left(\sum_d\frac{|z_0(d)|}{\sqrt d}\right)^2
       \sum_a\frac{\tau(a)^2}{a^2}
 \le\left(\sum_j\frac{|c_0(j)|}{\sqrt j}\right)^4
       \frac{\zeta(2)^4}{\zeta(4)}.
\]

The last Euler identity follows from sum_(e>=0)(e+1)^2 x^e=(1+x)/(1-x)^3.
The full kernel estimate sum_(k>=1)K_d(k)^2<=18/d therefore bounds D_L by
eighteen times this fixed finite constant. This controls the entire diagonal,
not just a selected subannulus.

### 4.3 A positive logarithmic mode in the complete output

Define the fixed step function

\[
 w(v)=\sum_d\frac{z_0(d)}d H_{\lfloor v/d\rfloor}.
\]

It vanishes for v<1. The identities P_0(1)^2=0 and
(P_0^2)'(1)=0 remove both the log(v) and constant terms of the harmonic
expansion, so w(v)=O(1/v) as v tends to infinity. It is bounded everywhere.

The two exact balance moments similarly imply

\[
 Q_L(x)=\sum_{a,b\le L}\frac{w(x/(ab)^2)}{a^2b^2}.
\tag{8}
\]

For the infinite version put

\[
 Q_\infty(x)=\sum_{n\ge1}\frac{\tau(n)}{n^2}w(x/n^2).
\]

This is finite at each x because w vanishes below one. With N=sqrt(x) and
psi(t)=t^(-2)w(t^(-2)) for 0<t<=1,

\[
 \frac{NQ_\infty(x)}{\log N}
 =\frac1{N\log N}\sum_{n\le N}\tau(n)\psi(n/N)
 \longrightarrow I:=\int_0^1\psi(t)dt.
\tag{9}
\]

Here psi is bounded near zero by the O(1/v) estimate. On each [epsilon,1]
it is piecewise continuous with finitely many jumps. The elementary divisor
average sum_(n<=u)tau(n)=u log u+O(u) gives the weighted Riemann-sum limit
there. The omitted interval contributes at most a constant times epsilon
in the limiting upper bound. Letting epsilon decrease to zero proves (9).
This requires no asymptotic divisor-error conjecture.

The integral has an exact nonzero value. For Re(s)>0, harmonic summation
gives

\[
 \int_0^\infty w(v)v^{-s-1}dv
       =\frac{\zeta(s+1)P_0(s+1)^2}{s}.
\]

The left side is holomorphic for Re(s)>-1, since w vanishes near zero and
is O(1/v) at infinity. On the right the apparent singularity at s=0 is
removable: the squared P_0 zero pays both displayed factors. Continue to
s=-1/2 and substitute v=t^(-2) to obtain

\[
 I=-\zeta(1/2)P_0(1/2)^2>0.
\tag{10}
\]

Indeed zeta(1/2)<0 follows from the positive alternating eta series and
1-sqrt(2)<0. Elementary square-root bounds give P_0(1/2)<-41/90, so it
does not vanish. No numerical zeta zero or RH assumption is involved.

### 4.4 Truncation and the lower energy bound

For x=tL^2 with fixed 10<=t<=20, an omitted pair a>L in Q_infinity has
b<=sqrt(20), because w vanishes below one. Boundedness of w and
sum_(a>L)a^(-2)<=1/L show

\[
 |Q_\infty(tL^2)-Q_L(tL^2)|=O(1/L),
\]

uniformly on that fixed t interval. Combining this with (9) gives, also with
an integer part inside x,

\[
 \frac{LQ_L(\lfloor tL^2\rfloor)}{\log L}
       \longrightarrow\frac I{\sqrt t}.
\]

Fatou's lemma on 10<=t<=20 now gives

\[
 \liminf_{L\to\infty}\frac{\sum_{k=Y+1}^{B}Q_L(k)^2}{(\log L)^2}
       \ge I^2\log2>0.
\tag{11}
\]

The first cell at k=Y can be removed harmlessly using the same pointwise
asymptotic, and the whole integration interval lies inside (Y,B] for large L.
Since C_L=sum Q_L^2-D_L and D_L is uniformly bounded, (11) proves (7).
Each D_L is positive, for example from its nonzero d=2 coefficient and
K_2, so the ratio is well-defined. QED.

The obstruction rules out a broad source-independent operator inequality
based only on the displayed sign, cap, balance and crossing information.
Any surviving native proof must make indispensable use of the missing
divisor equations, rather than restore them only after an absolute-value
bound has already lost the cancellation.

## 5. Bounded calculations and their evidentiary limits

[arithmetic-counterfamily.py](arithmetic-counterfamily.py) reconstructs six
native crossing cases Y<=17 with exact Fraction arithmetic. For each it
evaluates every harmonic-quotient term on the full annulus and verifies
sum Q^2=A_Y+R_Y and |R_Y|<4. It also checks normalization, Liouville signs,
coefficient caps, balance and the own-source crossing of all four synthetic
examples below with exact rational/integer arithmetic.

The larger synthetic norm values use ordinary binary64 arithmetic. The
diagonal is evaluated by complete quotient blocks using
sum_(k<=n)H_k=(n+1)H_n-n and
sum_(k<=n)H_k^2=(n+1)H_n^2-(2n+1)H_n+2n.
An independently evaluated harmonic-quotient formula agrees at six sample
points with the divisor-prefix output, with maximum discrepancy below
3.5e-13. This is a bounded consistency check, not a rigorous error enclosure.

| L | Y | Complete B | D, ordinary | C, ordinary | C/D, ordinary |
|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 120 | 0.199689 | -0.150228 | -0.752311 |
| 2 | 40 | 1680 | 0.392897 | -0.294945 | -0.750695 |
| 4 | 160 | 25920 | 0.547073 | -0.360235 | -0.658476 |
| 8 | 640 | 410880 | 0.653445 | -0.097659 | -0.149452 |

All four early covariances are negative despite the proved eventual
divergence to positive infinity of their ratio. The examples therefore
illustrate why finite negative panels cannot establish a generic sign law.
No first positive crossing or effective asymptotic onset is claimed.

The command executed was:

```text
python -S -B arithmetic-counterfamily.py --write arithmetic-counterfamily.json
```

The JSON result records complete coverage and separates exact identities
from ordinary norm diagnostics. No predecessor numerical campaign, native
large-scale covariance search, zero table or full repository build was run.

During the same session a second agent reviewed the complete arguments in
Sections 3--4, including the collar signs and endpoints, coefficient support,
uniform full-diagonal bound, continued Mellin integral, truncation estimate
and Fatou step, and found no defect. This is an independent reading within
the same team, not external refereeing or formal verification. That review
did not separately re-audit the primary literature. The analytical proof,
exact finite checks and ordinary numerical diagnostics have distinct roles.

## 6. What the next bound entails in established literature

Huxley and Watt's quadratic identity already rewrites M(N^2) as a quadratic
form in the Mobius prefix; their paper also develops spectral and other
decompositions of that form [L1, equation (1.5), Theorem 1, and Section 3].
They explicitly identify the unresolved step as extracting a useful Mertens
bound from the arithmetic vector. The new completed reciprocal-energy
formulation has different norms and a useful crossing mechanism, but it
does not turn a classical finite identity into an automatic cancellation
estimate. The native vector remains the important input.

Soundararajan's RH-conditional result improves the pointwise Mertens bound
to sqrt(x) times a subpower exponential, using information about unusually
dense zero intervals [L2, main theorem]. It cannot be imported as an
unconditional source upper bound. Its role here is context for how much
analytic content lies in reducing the exponent to one half.

Ng proves a logarithmic mean-square Mertens estimate under RH and the
additional negative-moment condition J_(-1)(T)<<T [L3, Theorems 1 and 3].
His discussion also records that the weak Mertens conjecture implies RH,
simplicity and convergence of a reciprocal-zero-derivative sum. Thus a
logarithmic energy expectation must not be presented as a routine consequence
of RH alone. E_Y is the discrete version of this classical mean-square norm;
F_Y has the additional exact mean channel. The sparse fourth-logarithmic
annular target here is different, so these facts are context rather than
an assertion that the two conjectures are equivalent.

There is a clean conditional explanation for a ratio near -1: if the actual
F_Y=o(log^4Y), then (4) and (2) force C_Y/D_Y->-1 along crossings. This is
an implication from an explicitly stronger energy assumption, not a bound
proved in this review or inferred from the early panels.

## 7. Concrete next milestone and ranking judgment

The completion milestone remains a theorem for the literal native source:

\[
 \max(C_{Y_j},0)/D_{Y_j}\le Y_j^{\epsilon_j},\qquad
 Y_j\in X,\quad Y_j\to\infty,\quad\epsilon_j\to0.
\tag{12}
\]

An unbounded family of certified inequalities is needed. A bounded list,
however accurate, is not (12). The stronger bounded-ratio condition may be
worth attacking, but its apparent simplicity must not hide its annular
mean-square content in (4).

A useful intermediate analytic milestone is a source-specific bound for
the complete quotient-block output Q that survives square-dilation stress
tests like (6). Such a lemma must use sum_(d|n)c_d=delta_(n=1) for every
n<=Y inside the estimate. A bound derived before those equations are used
cannot distinguish the counterfamily. The first genuine progress toward
completion would be a native covariance or trace upper estimate beyond the
classical source consequences, including the o(N) trace bound in Section 2.6,
not a sharper diagonal, new basis, smaller finite truncation error or more
negative low-cutoff examples.

Arithmetic retains the clearest scalar completion interface among the routes
reviewed here, which supports prioritizing it as a research target. The new
obstruction lowers confidence in a generic positivity or spectral shortcut.
The analytic chain has no defect identified in this pass, but no fixed power
saving on the native magnitude has emerged. This is a reasoned priority
judgment, not evidence that the remaining inequality is close.

## Primary literature

1. **[L1]** M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of
   the Mobius function* (2018), [original paper](https://arxiv.org/pdf/1807.05890),
   equations (1.5), (1.8), (1.10), and Section 3. The quadratic identity and
   its decomposition context are the relevant inputs.
2. **[L2]** K. Soundararajan, *Partial sums of the Mobius function*, Journal
   fuer die reine und angewandte Mathematik 631 (2009), 141--152;
   [author preprint](https://arxiv.org/pdf/0705.0723), introduction and main
   theorem. The result is explicitly conditional on RH.
3. **[L3]** Nathan Ng, *The distribution of the summatory function of the
   Mobius function*, Proceedings of the London Mathematical Society 89
   (2004), 361--389; [author manuscript](https://www.cs.uleth.ca/~nathanng/RESEARCH/mobius2b.pdf),
   equation (8), Theorems 1 and 3, and equations (16)--(18). Publication year
   is 2004; the later publisher webpage date is not the research date.
4. **[L4]** NIST Digital Library of Mathematical Functions,
   [Section 25.2, especially equation 25.2.8](https://dlmf.nist.gov/25.2),
   Euler summation and zeta continuation. Classical continuation, reflection
   and real-axis sign facts are used with their stated domains.
5. **[L5]** Terence Tao, *A remark on partial sums involving the Mobius
   function* (2009), [author preprint](https://arxiv.org/pdf/0908.4323),
   Theorems 1.1 and 1.3. The prime-subsemigroup bound and limiting Euler
   product apply to the set of odd primes; that product is zero.
