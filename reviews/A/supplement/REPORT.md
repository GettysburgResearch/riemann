# Reviewer A: targeted omissions supplement

Status: **COMPLETED INDEPENDENT DISPOSITION OF THE NAMED FOLLOW-UP ITEMS, WITH EXPLICIT ACCEPTANCE HOLDS**.

This supplement follows review PR #795 at `e44b6d072ac82d014717454635df96da9c0e115f`.
It does not supersede valid earlier arguments or convert an unlisted branch into
accepted mathematics. Main and every original research branch are unchanged.
The research boundary remains PR #707. Source identities below join to the root
`SOURCES.tsv`; the new claim and implication rows join the existing ledgers.
No unpublished reviewer report is a premise.

## Summary for the integrator

The principal finite omission is now closed by a **new independent primitive
computation**: the seven-point Montgomery–Taylor pressure inequality passes a
complete 713,315-node interval exhaustion. The kernel backend is newly written
128-bit outward dyadic arithmetic, not Arb. The search design is credited to the
pinned ainta source. This is not a claim to have reproduced its different
707,901-node transcript or its table hashes. The 269- and 280-block deductions
are reconstructed below with the bounded-separation, trace-normalization and
endpoint errors made explicit. The resulting zeta statement retains its named
classical analytic inputs; the finite program does not prove those inputs.

The interrupted optimized rank-two Cauchy replay is completed. The changed
#568 implementation and result receive a semantic/algebraic audit. The fifth
Conrey trial functional is freshly enclosed, while the published optimized
Conrey table and its original analytic proof remain separate imports. Three
CRT/Cartan statements are reconstructed. The all-depth safe-ray claim receives
a fixed-parameter correction and an explicit replacement proof of the formerly
sketched uniform tilt estimates.

The LongGaps mathematical proof chain is reconstructed through the growing
translate count, coefficient bounds, finite sieve, covering and consecutive-prime
conversion. This is an analytic/source review, not a Lean build or a check of
every tactic. PrimeGaps186's physical-integral axioms and the distinction between
weighted finite mass and finitely many fragments are retained explicitly. The
Catalan objection remains a refutation of a specified proof majorant under its
quoted v1 inputs, not a fresh original-PDF audit or a rationality theorem.

The unresolved list at the end is an acceptance handoff, not a claim that another
reviewer failed. In particular, A cannot make its own #793 mathematics independently
reviewed by repeating its original computations.

<a id="S01"></a>
## S01. Independent seven-point pressure certificate

**Source:** `ainta/zeta-simple-zeros@040c5e899e658aed7b56a2a87f501798fe10761d`,
`src/zeta_simple_zeros/{kernel,verify_seven,rounding}.py`, `docs/proof.md`, and
`paper/riemann.tex`. The exact blobs are in `SOURCES.tsv`. The source kernel and
weights, not a PR summary, were compared with the new implementation.

Put

\[
K(x)=\int_{-1/2}^{1/2}\cos(\sqrt2t)\cos(2\pi xt)\,dt,
\quad K(0)=\sqrt2\sin(1/\sqrt2),\quad w(x)=(K(x)/K(0))^2.
\]

The theorem checked is, for **all** six nonnegative real gaps,

\[
\mathcal F(g)=\frac1{3000}\sum_{i=1}^6g_i+
\sum_{s=1}^6\frac2{7-s}\sum_{i=1}^{7-s}
 w(g_i+\cdots+g_{i+s-1})\ge\frac{19}{5000}.                 \tag{S1}
\]

### Primitive arithmetic and its trust boundary

`dyadic_interval.py` stores integer endpoints over `2^128`. Addition and
subtraction are exact; multiplication and division round outward by integer
floor/ceiling; square roots use integer square roots with an outward upper
endpoint. Division rejects a denominator interval containing zero. Pi is
obtained from Machin's identity using alternating rational arctangent sums and
explicit next-term remainder bounds. No precomputed floating value of pi is a
primitive input.

Sine/cosine range reduction subtracts an integer multiple of an **enclosure**
of pi/2. The midpoint of the remaining interval is checked to lie in [-1,1].
The degree-49 sine and degree-48 cosine polynomials have remainders bounded by
`1/51!` and `1/50!` respectively; the interval radius is added using their
unit Lipschitz bounds. For sinc on [-1,1], the even degree-48 polynomial has
remainder at most `1/51!`; elsewhere sine is divided by a zero-free argument.
The kernel is evaluated by

\[
K(x)=\tfrac12\{\operatorname{sinc}(\pi x-1/\sqrt2)
                      +\operatorname{sinc}(\pi x+1/\sqrt2)\}.
\]

Derivatives are evaluated from the exact differentiated sinc expressions only
on cells with x >= 0.95; no removable singularity is divided through. Bounds
for w'' enclose `2(K'^2+KK'')/K(0)^2`, not the square of a derivative of w.

The finite range-minimum and nonnegative accumulation layers use widened
binary64 numbers. Every conversion and accepting addition/multiplication is
moved outward with `nextafter`. Negative Hessian coefficients use upper
coefficient bounds before rounding downward. This relies on CPython's
round-to-nearest binary64 operations and `nextafter`; it is **not** an assertion
that the entire program uses rational arithmetic only. Underflow-to-zero is
safe only in the explicitly nonnegative lower-bound operations. All numerical
ranges used here are bounded and far from overflow. The ordinary floating LDL
is only a rejection screen. Every accepting Hessian test is repeated by the
outward dyadic LDL routine. Consequently no floating eigensolver or optimistic
midpoint pivot licenses a box.

### Why the finite search covers a continuum

If the sum of the gaps is at least 57/5, the linear term alone proves (S1).
Otherwise each gap is in [0,57/5]. Divide that interval into closed cells of
width 1/4000. A one-gap lower bound discards every cell outside the three
retained index components

```
[3809,4778], [7221,9364], [10571,44827].
```

The 3^6 initial rectangular boxes cover all remaining possibilities. Boundary
points may be covered twice, which is harmless; no endpoint is omitted.
For a span of s gaps whose component cell ranges are [a_i,b_i], the sum lies
in the closed cells from `sum a_i` through `sum b_i+s-1`. The range-minimum
queries use precisely this extra `s-1`, not just the sum of the upper indices.
A query beyond the table uses the valid fallback w >= 0; it cannot certify
convexity there from unavailable second derivatives.

A box is accepted in one of three ways: its linear lower bound suffices; the
sum of enclosed kernel minima suffices; or a certified Hessian floor makes
F convex on the box and its midpoint tangent plane has a sufficient lower
bound. For the last test each span contributes `c vv^T`, where v is its
0/1 incidence vector and c is a rigorous lower bound on its weighted w''.
Thus the difference between the actual Hessian and the assembled floor is a
sum of **nonnegative multiples of vv^T**. This justifies the Loewner inequality;
it is not the false inference that arbitrary entrywise lower bounds give a
PSD difference. A positive definite floor is certified by dyadic LDL.
The tangent bound retains all six gradient-radius charges.

Every unaccepted box is split into its two closed cell-index children along
a widest coordinate. A remaining single-cell box causes an error, not a PASS.
Stack exhaustion is therefore an exhaustive proof under the arithmetic
contracts above, not a positive sampled mesh.

### Fresh result

```
initial boxes                  729
processed nodes            713315
linear-pressure leaves       3072
interval leaves            259807
convex-tangent leaves       94143
splits                     356293
unclosed terminal cells         0
```

The identities `nodes=729+2*splits` and `leaves=729+splits` independently check
the binary-tree accounting. The kernel-table hash is
`2a68fbb3ba1da02a5c3b66589ad07bc2c21de1317d42a5f3832cad2333906fa4`;
the second-derivative-table hash is
`e3be7c6d5250f26f6adc3ec6a998710a7f3aba95b3badd9378ecaf54418ee7a7`;
the ordered traversal hash is
`4c5c0d7ddd7f34f045f16474de38c8eb0f33abd1b3d4be24066e1f84ae297abf`.
These hashes identify this computation; they are not a substitute for it.

**Disposition:** accept (S1) as a newly reproduced finite analytic inequality,
subject to the stated Python/rounding trust boundary and review of this small
backend. The exact original Arb production record remains a different object.
An uncached attempt was interrupted without a verdict; the cached version
caches only exact-point derivative enclosures and completed the same search.
Execution details and mode comparisons are in `EXECUTION_RECEIPT.json`.

<a id="S02"></a>
## S02. From seven gaps to 269/280 blocks, with the analytic interfaces retained

**Sources:** #726 `L-105562`, `T-105560`; #731 `L-105211`, `L-106550`,
`L-106551`; and the pinned external `paper/riemann.tex`.

For ordered points y_1,...,y_m, let E_m=2 sum_{i<j}w(y_j-y_i). Sum (S1) over
all consecutive seven-point windows. A pair of separation s occurs at most
7-s times, and a gap occurs at most six times. All omitted pair terms are
nonnegative. Hence

\[
E_m+\operatorname{span}/500\ge19(m-6)/5000.                 \tag{S2}
\]

The factor six in the span charge is mandatory.

For a trace-m PSD matrix let x_i=lambda_i-1, E=sum x_i^2 and
Delta=sum Psi(lambda_i), with Psi(t)=(t-1)^2 for 0<=t<=2 and 2t-3 for t>=2.
When E<2 at most one x_i exceeds 1. If none does, Delta=E. If a>1 does,
Delta=E-(a-1)^2 and Cauchy gives a^2 <= (m-1)E/m. Therefore

\[
\Delta\ge\phi_m(E)=
\begin{cases}E,&E\le m/(m-1),\\
2\sqrt{(m-1)E/m}-1+E/m,&m/(m-1)<E<2.
\end{cases}                                               \tag{S3}
\]

Equality in the second case is attained by x_1=a and all other x_i=-a/(m-1).
For E>=2, separating zero, one, and at least two coordinates above 1 gives
Delta>=2sqrt(2)-1. For z>=0, E+z>=q, and
m/(m-1)<q<2 with phi_m(q)<=2sqrt(2)-1, monotonicity of phi_m and of
phi_m(E)-E imply Delta+z>=phi_m(q). These are finite spectral inequalities;
no kernel or zeta assumption enters them.

For m=269, q=4997/5000<1, the older min(E,1) bound suffices.
For m=280,

\[
q=2603/2500,\qquad
c_{280}=2\sqrt{726237/700000}-1+2603/700000.
\]

It remains to connect this algebra to the **actual** finite Gram matrices.
The external construction supplies unit-bounded vectors with full-grid overlap
converging to k(x)=K(x)/K(0), uniformly on every fixed separation interval.
Its finite grid loses O(L^-2) for retained points at normalized distance L^2
from either end. The taper converges in L1 after scaling. Deleting these end
strips costs O(L^2)=o(N) zeros using the usual unit-interval zero count.

Two repairs must accompany an extraction:

1. The finite actual Gram has diagonal 1+o(1), not exactly 1. Compare each
   fixed-size block to the exact kernel Gram, whose diagonal is exactly 1.
   The function Psi is globally 2-Lipschitz on [0,infinity), so fixed-size
   perturbations change Delta by o(1). Do not apply the trace-m hypothesis
   literally to the unnormalized actual block.
2. Compact-separation convergence is enough: blocks of span at least 500q
   are already paid by their span variable. The remaining blocks lie in one
   fixed compact separation range. There are O(N) blocks, each with a
   **uniform** o(1) error; summation therefore gives o(N).

Convex trace pinching and averaging the m block offsets give

\[
\Delta(M)\ge(c_m/m)S-\frac{m-1}{500m}N-o(N).                \tag{S4}
\]

Each interior gap appears at most m-1 times across offsets; the whole
normalized span is N+o(N). At most O(m) boundary points per offset are lost.
This is not a claim that every arbitrary long block has a uniform kernel
approximation without the span split.

The stability-enhanced rank inequality and the named external trace,
mean-square, and tail estimates give S >= H_MT N + Delta(M)-o(N), where

\[
H_{MT}=3/2-\cot(1/\sqrt2)/\sqrt2.
\]

Combining with (S4) yields the respective constants

\[
H_{269}=\frac{1345000H_{MT}-2680}{1340003}
       =0.6730085279277797613\ldots,
\]
\[
H_{280}=\frac{H_{MT}-279/140000}{1-c_{280}/280}
       =0.6730096522791369\ldots.                           \tag{S5}
\]

Fresh outward dyadic evaluation proves H_280>H_269>673/1000. The different
269 decimal displayed in #726 (ending `...7557...`) should be corrected; its
strict 67.3 percent conclusion is unaffected. The 280 lift does not require
rerunning a different seven-gap theorem.

**Disposition:** the finite premise and the complete block deduction are now
reconstructed. The zeta conclusion is recorded with its external analytic
trace/mean-square/tail assumptions, not as a consequence of a finite Python
PASS alone. No originality or current world-record claim is made. The entire
original analytic proof behind those inputs and its formalization are not
silently certified by this supplement.

<a id="S03"></a>
## S03. Closing the rank-two execution and #568 semantic-delta holds

The parent report's rank-two invariant-cone repair is unchanged. Its original
source checker still fails at formal symmetric-symbol substitution, and fixing
that alone still exposes negative numerator coefficients. The successful
repair uses P^2-4R=(A-B)^2>=0. A fresh optimized execution reproduces the
ordinary polynomial certificate byte for byte. This closes the previously
interrupted execution item, **not** arbitrary-rank CTI or actual-Xi transfer.
The historical failure and interruption receipts remain intact.

For #568, compare
`085d046905bfd32a5725632650039e58bb7fc1f7` with
`3a70470e3a8bbd60e0b7387ea46fd391cfb1d2e2` at
`experiments/X-97010-parity-grouping-hardening/verify.py` and its result JSON.
The implementation change replaces an unused `for L,row in ...items()` key
by `for row in ...values()` and adds explanatory comments. The result changes
formatting, not parsed values. The exact checks include

\[
5(2x-1-y)+(5y-x-1-3x^2)=-3(x-1)(x-2),
\]

accumulated parity, and the incompatibility between the retained recursive
parity and the desired positive leading sign. The supplied scalar upper
endpoints combine to
`-62.71816781856588773240782086465`. Their directed primitive production was
not rerun; the sign implication from those **supplied** endpoints was checked
by exact rationals. An assert-based fixed-fixture driver is not being advertised
as a general production certificate parser. No mathematical change in this
old-head delta was found within these two files.

<a id="S04"></a>
## S04. Fifth-derivative Conrey fallback: finite inequality closed, analytic input separate

**Source:** #720 at `80779dd04ca64704744ef50dfcac964344e2445e`,
`L-104602` and `L-104634`. For the admissible trial phi(x)=1-x, m=5, R=1,
q=(1-x)(1-2x)^5. With

\[
\Phi=\int_0^1e^{2x}q(x)^2dx,\quad
\Psi=\int_0^1e^{2x}q'(x)^2dx,\quad
A^2=(\Psi-1-\Phi)/(4\Phi),
\]

the claimed trial value is F=2Phi A coth(A)+1/2. Reconstructing q and q'
over rational coefficients, using J_0=(e^2-1)/2 and
J_n=(e^2-nJ_{n-1})/2, reduces both integrals exactly to rational combinations
of e^2. Outward dyadic exp and sqrt bounds give

\[
F=1.0151455439229777\ldots<e^{1/50}.
\]

The exp helper reduces to [0,1], uses a rational Taylor polynomial with
remainder <=3/49!, then squares outward; negative arguments use reciprocal
intervals. Thus this is not a comparison of ordinary decimal evaluations.
Conditional on the reconstructed published Conrey functional implication,
alpha_5>49/50 follows. Strip invariance and conjugation give the real-window
height charge <=(N_5-R_5)/4, but transfer to companion zeros still requires
its separately named Rouché/endpoint theorem.

**Disposition:** remove the finite trial-evaluation hold. Do not replace the
stronger optimized `0.9970` input by this `0.98` result without changing every
consumer's budget. The original approximate-functional-equation/off-diagonal
proof, optimized coefficient tables and endpoint-31 approximation remain
outside this new finite replay.

<a id="S05"></a>
## S05. CRT selectors and normalized Cartan collars

**Source:** #723 at `7b01a312b06f6948e0ce15d6d8be5e8b57d8fe81`,
`L-105105`, `L-105114`, `L-105116`.

For P=F/F' and Q=F^2/(F'F''), the actual pole orders at a are
(r-m)_+ and (r+s-2m)_+, respectively. The manifest must include F''-only poles
and omit removable common events. At a real noncommon odd-order turn r,
P has leading coefficient rho and pole order r, while Q has leading
coefficient rho^2/r and pole order 2r-1. CRT selectors satisfying

\[
W_1\equiv(z-c)^{r-1}\pmod{(z-c)^r},\quad
W_2\equiv r(z-c)^{2r-2}\pmod{(z-c)^{2r-1}}
\]

and vanishing to each complete nontarget pole order give contour integrals
sum rho and sum rho^2. The factor r is essential: F=1+x^4/4 gives r=3,
rho=1, and replacing W_2 by W_1^2 gives residue 1/3 rather than 1.
A second exact polynomial fixture checks cancellation of every F''-only pole
and the second moment 41/32. The root-free squarefree-stratum CRT construction
encodes all embeddings; it does not isolate real-window roots without a
separate localization step. Finite interpolation existence gives no uniform
selector norm as the window grows.

For the Cartan lemma normalize h(z)=F(a+z)/F(a), and let
A=log(max_{|z|=r_3}|h(z)|), beta=log(r_3/r_2), r_1<r_2<r_3.
Jensen gives at most A/beta zeros in D(0,r_2). Remove their normalized finite
Blaschke product phi with phi(0)=1. The quotient psi=h/phi is zero-free and
Re log psi<=A on D(0,r_2). Borel–Carathéodory gives
Re log psi>=-2r_1 A/(r_2-r_1) on D(0,r_1). Outside disks of radius epsilon r_2,
each normalized Blaschke factor has modulus at least epsilon/2. Hence

\[
\log|F(z)/F(a)|\ge-
\left[\frac{2r_1}{r_2-r_1}+\frac{\log(2/\epsilon)}\beta\right]A.
\]

This proof remains scale invariant, includes multiplicity, and permits an
outer-circle zero by approaching the radius through regular circles. A finite
union of disks of total nominal radius S excludes at most 2S of either
positive horizontal/vertical side parameter. The strict condition
2S<min(Delta_T,Delta_eta) supplies a common safe rectangle. An origin anchor
cannot serve every Xi derivative because odd derivatives vanish there.

The radius optimization minimizes sum u_j log(2/epsilon_j) subject to
sum v_j epsilon_j<=R, 0<epsilon_j<=1. Strict convexity and KKT give

\[
\epsilon_j=\min\{1,u_j/(\lambda v_j)\}.
\]

For 0<R<sum v_j the budget is active and lambda is unique; for R>=sum v_j
all epsilons equal 1. A closed budget with fixed fractional slack is required
to obtain a minimizer compatible with the strict safe-boundary condition.

**Disposition:** these finite statements survive. A classical fixed-order
Xi growth load O(R log R) can still yield reciprocal losses
exp(O(R(log R)^2)); no estimate here absorbs them into the required cofinal
residue budget. Not every implementation on this long branch was replayed.

<a id="S06"></a>
## S06. All-depth safe-ray repair, with a frozen companion parameter

**Source:** #724 `L-105209` at
`452978883b0009f002cfec426dfd5eb10041a15c`.

There is a genuine notation/implication error. With F_r=Xi^(r),
mu_r=M_{r+1}/M_r and lambda_r=1/mu_r, defining
E_r=F_r-i lambda_r F_{r+1} does **not** give E'_r=E_{r+1}:

\[
\mu_{r+1}-\mu_r=\operatorname{Var}_{\nu_r}(U)/\mu_r>0.
\]

Use instead E_{j,lambda}=F_j-i lambda F_{j+1}, and keep lambda=lambda_r
fixed when differentiating. Then E'_{r,lambda_r}=E_{r+1,lambda_r}. The printed
G quotient already uses the same fixed lambda; this is a repair, not a new
identity for the varying-lambda chain.

Here is a replacement for the sketched uniform tilted-saddle estimates.
The actual positive theta density has, as u tends to infinity,

\[
(\log\Phi)'=9/2-2\pi e^{2u}+O(e^{-2u}),\quad
(\log\Phi)''=-4\pi e^{2u}+O(e^{-2u}).                       \tag{S6}
\]

On every bounded positive interval it is positive smooth, so the second log
derivative is bounded above. Let w be the mode of u^r Phi(u), mu its mean and
sigma^2 its variance. Local Laplace analysis gives w~(log r)/2,
mu~w and sigma^2=O(w/r). No all-deviation Gaussian inequality is needed.

For y>=0, the positive component has density proportional to
u^r Phi(u)(1+u/mu)e^{yu}. Its log density has negative second derivative

\[
r/u^2-(\log\Phi)''(u)+1/(u+\mu)^2,
\]

strictly positive everywhere for sufficiently large r. If v_y is its mode,
then v_y>=v_0~w and the saddle equation gives
2pi e^{2v_y}=r/v_y+y+O(1). On |u-v_y|<=1 the curvature is bounded above and
below by constant multiples of B_y=r/v_y+y+1. The central mass is comparable
to e^{S(v_y)}/sqrt(B_y). At distance one, the exponent has dropped by at
least c B_y and the slope has magnitude at least c B_y. Global concavity
then gives exterior exponential tails. Integrating the central Gaussian and
those exterior tails yields E[(U-v_y)^2]<=C/B_y.

For y<=r/w, comparison of the saddle derivative at w+C shows v_y<=w+C
for an absolute C; for y>=r/w simply B_y>=y. Therefore

\[
\operatorname{Var}_{+,y}(U)\le C/(r/w+y),\qquad y\ge0.     \tag{S7}
\]

All constants here are uniform in y; they are not numerically optimized.
This proof also handles the factor 1+u/mu, rather than silently applying a
variance theorem for a different tilted measure.

Write P(T,y) and N(T,y) for the two components in the source file, and A(y)
for the positive component's real mass. Centering its probability at m_y gives

\[
|P(T,y)|\ge A(y)(1-T^2\operatorname{Var}_{+,y}/2),\quad
P'_T/P=i m_y+O(|T|\operatorname{Var}_{+,y}).                 \tag{S8}
\]

The second formula follows from E(U-m_y)=0 and
|e^{iT(U-m_y)}-1|<=|T||U-m_y|. It is valid uniformly when
T^2 w/r tends to zero.

The reflected component can be controlled without any negative-tilt saddle.
Since e^{-yu}<=1 for u,y>=0,

\[
|N(T,y)|\le M_r\,\sigma/\mu,
\quad
|N'_T(T,y)|\le M_r\,\sigma\sqrt{\mu^2+\sigma^2}/\mu.       \tag{S9}
\]

These are Cauchy–Schwarz bounds. Meanwhile A(y)>=2M_r and
m_y A(y)>=2M_r mu. The ratios in (S9) to |P| and m_y|P| are consequently
O(sigma/mu)=o(1), uniformly for all y>=0. In particular,
E_{r,lambda_r}(T-iy) is nonzero and

\[
iE_{r,\lambda_r}/E'_{r,\lambda_r}
  =m_y^{-1}(1+o(1))
\]

uniformly on the complete lower ray. It lies in a single acute sector, so its
argument continued from large y cannot accumulate an unobserved winding.
The regime is T^2 log r/r -> 0; taking r=T^2 log T L(T), L(T)->infinity,
suffices. This does not cover a near-linear derivative-order regime.

**Disposition:** the corrected safe-ray theorem is supported by the replacement
proof above and should receive a new extraction identity. The false varying-
parameter derivative equality must not remain a dependency. The low-order
Levinson numerator and the global descent estimate remain open.

<a id="S07"></a>
## S07. LongGaps: end-to-end mathematical proof chain and uniformity audit

**Primary source:** `openai/LongGapsBetweenPrimes@8f5fa88c88b4750028c05b66b081d56a92418054`,
`LongGapsBetweenPrimes.lean`, blob `14467e08a1848a43c374b43001f172eab2a71d3c`.
The definitions, coefficient estimates, local Gram calculation, finite sieve,
parameter specialization, covering and terminal statements were read directly.
This section reconstructs the mathematical chain; it is not an assertion that
all Lean tactics were replayed or that an independent kernel accepted it.

### Coefficients and normalization

For a squarefree auxiliary modulus P define

\[
B=\sum_{d\mid P,d>1}\frac1{\varphi(d)\log d},\quad
a_1=1,\quad a_d=-1/(B\log d)\ (d>1),
\quad M_\gamma=\sum_{d\mid P}\frac{a_d^2d^\gamma}{\varphi(d)}.
\]

Thus sum a_d/phi(d)=0, the incomplete sum containing 1 is nonnegative, and
M_0>=1. These identities explain why the sign of the replaced coefficient
remainder is known; arbitrary Selberg weights could not be substituted.

The auxiliary primes lie in (Z,Y], with
Z=floor(x^6), log Y approximately x/(log x)^5 and beta=(log x)^5/x.
The normalizer has a fixed positive eventual lower bound. One way to see the
mechanism is to integrate the negatively tilted divisor Euler product:
B=integral_0^infinity(E_P(-t)-1)dt. For t log(Y+1)>=1, its comparison with
an ordinary Euler product gives E_P(-t)>=1/(2At), with
A=e^6(1+log Z). Integrating until t=1/(4A) leaves a positive constant,
since log log Y~log x while A has size log x. The source gives the explicit
lower constant 1/(100e^6). This is a uniform coefficient estimate, not an
assumption that the auxiliary product is large merely by definition.

For 0<=gamma<=2beta, gamma log Y<=2. Each Euler tilt is then bounded by a
fixed exponential using sum_{p<=Y}(log p)/p<=3log Y. Splitting the absolute
coefficient moment at Y and using the normalizer bound gives one fixed C with
absMoment_gamma<=CB and |a_d|<=1. In particular

\[
M_\gamma^k\le M_0^k\exp(kC\gamma).                        \tag{S10}
\]

The k in this estimate must be retained; it is not a fixed-parameter constant.

### Local covariance and the complete finite sieve

At a residue root a modulo p, put psi_a(a)=-1 and psi_a(t)=1/(p-1) elsewhere.
Its mean is zero, variance 1/(p-1), and distinct-root covariance
-1/(p-1)^2. The normalized nonconstant vectors thus have off-diagonal
correlation -1/(p-1), and are orthogonal to the constant vector. These three
identities were independently checked by exact finite sums.

The truncated divisor tuples are pairwise coprime and have product at most D.
The tuple-to-local-state map is injective under the distinct-root hypothesis.
The diagonal losses consist of the product cutoff and repeated-prime events:

\[
M_0^{k+1}-\mathrm{diagonalMass}
\le D^{-\beta}M_\beta^{k+1}
 +16(k+1)^2M_0^{k+1}/M,                                   \tag{S11}
\]

when every auxiliary prime exceeds M. The prime incidence bound <=4/p and
sum_{p>M}p^{-2}<=1/M justify the collision term. The tensor Gram row bound is

\[
\exp\{k\log D/[(M-1)\log M]\}.
\]

The logarithmic product cutoff controls how many local factors enter one row;
a naive factor proportional to the number of all auxiliary primes would not.
Replacing a missed root factor by its constant value produces a coefficient
remainder bounded by
C(m/D)^beta+4log D/(M log2). Squaring, using (S10), and retaining the complete
finite interval-average error yields the displayed `uncoveredBound`. The
integer/CRT averaging error is **16D^6/T**; it is not dropped before comparing
with the normalized mass, and M_0>=1 licenses its relative use.

The source's `finite_simultaneous_roots` is a finite weighted pigeonhole
argument. Its hypotheses separately bound diagonal loss by 1/2, Gram factor
by 5/4, averaging noise by 1/8, and the union of k+1 missed families by strictly
less than 1/4 of the normalized mass. The total weight then exceeds the missed
weight. These inequalities are the load-bearing strictness, not a positivity
claim for every source vector.

### Growing number of translates

Take D=e^{x/8}, T=floor(e^x), M=floor(x^6), beta=(log x)^5/x and
k+1<=delta x with delta=1/(64C). The product tail is exponentially small in
(log x)^5, hence eventually <=x^-3; the squared replacement tail is <=x^-6;
collisions are O(x^-4) or smaller; the Gram factor is 1+o(1); and
16D^6/T<=32e^{-x/4}. Multiplication by k+1=O(x) still leaves the missed-family
bound tending to zero. Thus **one threshold works for every allowed set of
translates at that x**, not just for each fixed finite set separately.

The affine roots modulo each auxiliary prime are distinct because p>x^6>H
and the translates lie in [1,H]. The primorial Q of primes <=x is invertible
modulo those primes; its size makes each forced prime divisor proper. With
n in [0,T), setting t=n+1 preserves 1<=t<=T. This proves the short-translates
statement in its growing-cardinality regime.

### Covering and the prime-gap endpoint

The covering uses W=floor((log x)^4) and a smoothness cutoff with
log Z proportional to log x log log log x/log log x. After excluding residue
zero for p<=W and Z<p<=x/2, each survivor is either prime or Z-smooth: a
composite with a prime factor >x/2 and another >W would exceed H<xW/2.
A Rankin tilt bounds the smooth survivors; the elementary prime-count bound
handles the prime survivors. Greedy residue selection for W<p<=Z reduces
the remaining cardinality by the product of (1-1/p).

For one sufficiently small fixed eta>0 this leaves at most delta x survivors
in an interval of length

\[
H=\left\lfloor\eta x(\log x)^2
       \frac{\log\log\log x}{(\log\log x)^2}\right\rfloor.
\]

CRT assigns all previously selected residues. The short-translates result
clears the remaining set simultaneously. The interval (N,N+H] is composite.
Choose the greatest prime <=N and the least prime >N; Bertrand bounds the
latter by 2N and the gap exceeds H. The source bounds 2N<=e^{8x}. Substituting
x=(log X)/8 and paying the fixed floor/scale constants gives consecutive
primes q<=X and

\[
q-p\ge c\log X(\log\log X)^2
          \frac{\log\log\log\log X}{(\log\log\log X)^2}
\]

for some fixed c>0 and all sufficiently large X.

**Disposition:** the former absence of an end-to-end mathematical route
reconstruction is closed at this explicit source and analytic granularity.
The finite sieve normalization, growing-k quantifier and final gap conversion
are not RH-dependent. A Lean/compiler/kernel/Comparator claim still requires
C's independent execution; the source's `formalization.yaml` is not execution
evidence. No new theorem transporting this construction to the native
Möbius/physical-restriction source, or to RH, is obtained. Unread implementation
lemmas receive no individual acceptance merely because this chain is coherent.

<a id="S08"></a>
## S08. PrimeGaps186 and weighted fragment semantics

**Primary pin:** `openai/PrimeGaps186@61340d0b74163003b32756bb16e91d9209a5e330`,
`Challenge.lean`, blob `2331eeeb808008cee37bac7aa0fb17e36f1f3c17`.
The owner is `openai`, not a guessed historical repository owner.

The comparison specification is explicitly post-solution and has three
intentional theorem placeholders. They are not proof bodies. Its three
project axioms include the normalized rank-three Kloosterman bound, the
shifted rank-two correlation bound, and the **actual physical-integral bounds**.
The last is not discharged by integer arithmetic on the printed budget table.
A successful comparison with an allowlist establishes a result conditional
on those axioms, not those axioms themselves.

The empirical random measure is weighted by the nonnegative sample locations,
not unit atom counts. For intensity du/u on one positive dyadic band below
zeta>0, the expected weighted mass is integral u(du/u), the band's length.
Summing all bands gives expected total weighted mass zeta. Monotone convergence
therefore gives finite total mass almost surely. This justifies why the
`finiteFragments` zero fallback occurs only on a null exceptional set for
this positive-parameter law. Empty bands have zero Poisson count and do not
require an arbitrary normalization convention to carry positive mass.
There may nevertheless be infinitely many atoms: finite total weighted mass
is not finite support. The declared factor e^gamma zeta multiplying the law
must be kept when matching the paper's measure.

**Disposition:** this semantic layer and the visible conditional proof contract
are now independently checked. The three external inputs, especially the
physical integrals, remain typed acceptance holds. Neither a table hash nor
a post-solution challenge specification proves them. There is no automatic
prime-gap-to-RH implication.

<a id="S09"></a>
## S09. Catalan max-summand objection: what is proved, and what is not

**Source:** #789 at `dba7d5aa2555ea1a921c28720dc045976fd7195d`,
`research/exploratory/catalan-irrationality-2026-09-03/HEIGHT_BOUND_COUNTERCHECK.md`.
The original arXiv:2609.04176v1 PDF could not be acquired for a page audit in
this pass. The following verdict is explicitly about the quoted inputs.

Set S=floor(rho B), and select I_0={0,...,S-1}. The Pascal evaluation minor
with columns binom(x,i), i<S, at distinct integer rows is a Vandermonde divided
by product i!, hence a nonzero integer of absolute value at least 1. The
selected Cauchy determinant has logarithm O_rho(B^2): the leading S^2 log S
terms in its two Vandermondes cancel those of its denominator. The selected
clearing factors have logarithm
2rho B^2 log B+O_rho(B^2), while the positive alternating tails cost only
O_rho(B log B).

Grant the cited prime-valuation package with singular coefficient
A_rho=2rho-rho^2/2 and error O_rho(B^2). Then the absolute largest-summand
majorant is bounded **below** by

\[
(2\rho-A_\rho)B^2\log B-O_\rho(B^2)
  =\tfrac12\rho^2 B^2\log B-O_\rho(B^2).
\]

At rho=1/20 the uncancelled coefficient is exactly 1/800. The finite
178-/235-cell quadratic coefficients cannot cancel this higher-order term.
If the quoted valuation package lacks the necessary uniformity, that is an
additional missing premise rather than an escape from the calculation.

**Disposition:** the specified max-summand proof mechanism cannot deliver the
claimed negative quadratic bound under its own quoted asymptotic package.
This is not a proof of Catalan rationality and not an unconditional falsification
of a theorem whose rationality premise could be false. Original attribution,
PDF bytes/pages and any later corrected preprint require separate review.

<a id="S10"></a>
## S10. Remaining acceptance holds and corrected route map

The old omission categories are all assigned a disposition in
`OMISSIONS_RECONCILIATION.tsv`. A closed item means the stated bounded task
is complete, not that its entire branch is accepted.

**Still requiring independent work:** the source-level Lean/kernel, Comparator
and Nanoda builds; original-PDF/page matching of the external imports;
PrimeGaps186's actual physical-integral axioms; the original analytic
trace/mean-square inputs of the simple-zero theorem; the optimized Conrey
coefficients/endpoint-31 approximation; near-linear/high-deviation Xi regimes
outside S06; full unlisted CRT implementations; B's automorphic, Segre/Chow,
finite-field and partial-Frobenius modules; #765's full 38-module acquisition
and transport closure; #790/#792's primitive continuum lower certificates;
and non-author review of #793/Architecture-E material.

The 17-route map in the parent REPORT remains the map for integration, with
these refinements:

- The simple-zero route no longer has the seven-gap numerical premise as an
  unreproduced bottleneck. Its 269/280 conversion is covered by S02; the
  analytic input contract and any further percentage-gain charge remain visible.
- The high-derivative route has the corrected frozen-parameter all-depth entry
  in the regime T^2 log r/r -> 0. Its **first RH-facing open theorem remains
  low-order signed residue/endpoint/winding control**, not high-order entry.
- The CRT/Cartan route now has a reconstructed finite collar and optimization
  layer. Its first open theorem is a cofinal bound that absorbs actual selector
  and reciprocal-modulus costs at the residue-moment scale.
- The arithmetic/common-source route still requires the literal signed native
  physical estimate. #568's semantic repair and LongGaps' separate finite sieve
  do not discharge it.
- F1/Frobenius–Hodge, theta total positivity, heat, Pick, Weil and the operator
  routes retain their source-specific cofinal positivity/sign or principal-
  binding burdens. A finite detection theorem remains different from proving
  that the detected obstruction is absent.

All cross-review questions are **pending integrator reconciliation**, not
failed reviews or accepted claims. No edge with only reviewed/closed premises
now proves RH. The integrator should extract the named surviving results and
newly reproduced finite inequality, assign new identities to the repairs, and
keep the exact remaining holds rather than repeating an unbounded review.
