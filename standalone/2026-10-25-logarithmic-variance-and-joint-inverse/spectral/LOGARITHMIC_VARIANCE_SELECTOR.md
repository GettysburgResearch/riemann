# A logarithmic variance target on nearly linear finite matrices

Status: proposed analytic component, with complete proof below; independent review is recorded separately.
Scope: the exact complete Weil source, full finite legality, and a conditional all-scale selector theorem. **No source-specific variance upper bound or new zero-free region is proved.**
Dependencies: PR #1017 at 450dd8abecf58dfe60b3bc39bda0f792ea82ce95 for the full source and its finite real-zero theorem; PR #1021 at 742e952be4ef7843de86ea12678c0bdd3d3579c3 for the positive theta density and its full-source annihilation. The companion SIGNED_GAUSSIAN_SELECTOR.md gives the fixed-variance Gaussian argument and the complete-source residual lemma reproduced here.
New deduction: compulsory Fourier zeros bound the entire sampled transform by one. This permits a signed selector with a variance growing like a/log(a), on a mode schedule of order a log(a). A fixed test with doubly exponential Fourier decay supplies the finite RH consumer.
Smallest open hypothesis: the actual full-matrix resolvents in (3) must exist with the inequality (4) for every sufficiently large integer a.

## 1. Statement with every source condition retained

Use the Fourier convention

\[
\widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx.
\]

Let \(q_a\) be the complete semilocal Weil form on zero-extended functions on
\([-a,a]\):

\[
\begin{aligned}
q_a[f]={}&\frac1{2\pi}\int_{\mathbb R}
 \{\Re\psi(1/4+it/2)-\log\pi\}|\widehat f(t)|^2\,dt\\
&+2\Re\{\widehat f(i/2)\overline{\widehat f(-i/2)}\}\\
&-\sum_{2\le n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}
 \{C_f(\log n)+C_f(-\log n)\},
\end{aligned}
\tag{1}
\]

where \(C_f(t)=\int\overline{f(x)}f(x+t)\,dx\).
The form domain is the logarithmically weighted Fourier \(L^2\) domain
specified by the pinned source. No prime power, pole term, or archimedean
term is discarded.

For each sufficiently large integer \(a\), set

\[
M_a=\frac{a}{10\log a},\qquad N_a=\lceil4a\log a\rceil,\qquad
\mathcal T_a=\operatorname{span}\{e^{in\pi x/a}:|n|\le N_a\}.
\tag{2}
\]

Let \(T_a\) be the exact compression of (1) to \(\mathcal T_a\), with
the physical \(L^2[-a,a]\) inner product. Its minimum eigenvalue
\(\lambda_a\) includes **both** parity blocks.
Choose a real \(\kappa_a<\lambda_a\), and put

\[
u_a=(T_a-\kappa_a)^{-1}1,\qquad
f_a=\frac{u_a}{\int_{-a}^a u_a},\qquad F_a=\widehat f_a.
\tag{3}
\]

Coercivity makes the denominator positive; reflection and conjugation
make \(f_a\) real and even. The finite real-zero theorem for this specific
convolution-distribution matrix class, imported in PR #1017 from
Connes--van Suijlekom, Theorem 5.6, gives only real zeros for \(F_a\).
This is not a theorem about generic positive matrices. It requires the
full legality condition in (3), not legality only below the even minimum.

More explicitly, let \(A=T_a-\kappa_a I>0\) and
\(c=\langle1,A^{-1}1\rangle^{-1}\).
Cauchy--Schwarz in the \(A\) inner product makes
\(A-c|1\rangle\langle1|\) positive semidefinite, with the one-dimensional
kernel spanned by \(A^{-1}1\). This kernel is even. The scalar identity
shift and the constant convolution kernel representing
\(-c|\int h|^2\) preserve the distribution-matrix class in Theorem 5.6.
Its conclusion therefore applies to this resolvent, by exactly that
rank-one reduction. Positivity of an unrelated matrix would not suffice.

**Theorem 1.** Suppose the exact resolvents (3) satisfy

\[
\boxed{\quad -F_a''(0)=\int_{-a}^a x^2f_a(x)\,dx
       \le \frac{a}{10\log a}\quad}
\tag{4}
\]

for every sufficiently large integer \(a\). Then
\(\kappa_a\to0\), and RH follows.

The integral in (4) is a signed second moment. Its nonnegativity follows
from the normalized real-zero product below; physical nonnegativity of
\(f_a\) is not assumed. The theorem does not require a limiting transform
to be identified with Xi.

Both the allowed variance and the number of modes differ substantially
from the earlier bounded-variance, quadratic-cutoff statement. They are
coupled: changing one independently invalidates the estimates used here.

## 2. Compulsory zeros give a polynomial total-variation bound

Here is the general elementary lemma responsible for the improved
schedule. Let \(f\) be a real even trigonometric polynomial of degree at
most \(N\) on \([-a,a]\), extended by zero, with integral one. Assume its
entire transform \(F\) has only real zeros, and put \(V=-F''(0)\).
Its normalized paired Hadamard product is

\[
F(z)=\prod_j(1-z^2/t_j^2),\qquad
V=2\sum_j t_j^{-2}.
\tag{5}
\]

Indeed the exponential type gives order at most one, opposite real zeros
can be paired in a locally convergent product, and evenness makes the
possible exponential factor constant.

Fourier orthogonality forces \(F(m\pi/a)=0\) for every integer \(|m|>N\).
Remove one copy of each compulsory pair from (5), and write

\[
\begin{gathered}
P_{a,N}(z)=\prod_{m>N}\left(1-\frac{a^2z^2}{\pi^2m^2}\right),\\
V_{\rm tail}=\frac{2a^2}{\pi^2}\sum_{m>N}m^{-2},\qquad
F(z)=P_{a,N}(z)H(z).
\end{gathered}
\tag{6}
\]

The remaining paired product \(H\) has nonnegative variance
\(V-V_{\rm tail}\), so
\(|H(z)|\le\exp((V-V_{\rm tail})|z|^2/2)\).
For real \(|t|<(N+1)\pi/a\), all the factors of \(P_{a,N}\) are positive
and \(\log(1-x)\le-x\) gives

\[
0<P_{a,N}(t)\le e^{-V_{\rm tail}t^2/2}.
\]

Consequently

\[
|F(t)|\le
\exp\!\left(\frac{V-2V_{\rm tail}}2t^2\right)
\quad\left(|t|<(N+1)\pi/a\right).
\tag{7}
\]

In particular, if

\[
V\le\frac{4a^2}{\pi^2(N+1)},
\tag{8}
\]

then \(|F(n\pi/a)|\le1\) for every \(|n|\le N\), because
\(\sum_{m>N}m^{-2}\ge1/(N+1)\). The exact Fourier coefficients of \(f\)
are \(F(n\pi/a)/(2a)\). Therefore

\[
\boxed{\quad \|f\|_1\le2N+1.\quad}
\tag{9}
\]

For (2), condition \(M_a\le4a^2/(\pi^2(N_a+1))\) holds eventually:

\[
\frac{M_a(N_a+1)}{a^2}
\le\frac25+\frac{1}{5a\log a}
<\frac4{\pi^2}.
\tag{10}
\]

The strict limiting inequality is \(2/5<4/\pi^2\). Thus (4) gives the
polynomial bound (9) for the actual resolvents.

### Compatibility is not selector existence

The compulsory zeros also require \(V\ge V_{\rm tail}\).
Here \(V_{\rm tail}\sim(5/\pi^2)M_a<M_a\), so the target is not
structurally impossible. More explicitly, normalize

\[
h_{a,N}(x)=c_{a,N}\cos^{2N}(\pi x/(2a))
\quad (|x|\le a)
\]

to have integral one. Its Fourier transform is exactly

\[
\widehat h_{a,N}(z)=
\frac{\Gamma(N+1)^2}
{\Gamma(N+1+az/\pi)\Gamma(N+1-az/\pi)}
=P_{a,N}(z).
\tag{11}
\]

This follows from the beta integral and the gamma recurrence. Its
variance is \(V_{\rm tail}\le2a^2/(\pi^2N_a)\le(5/\pi^2)M_a\).
It belongs to the prescribed space and has precisely the compulsory real
zeros. It is **not** asserted to solve (3). An explicit compatible
function cannot substitute for a source-dependent existence proof.

## 3. Positive overlap despite the signed density

Let \(\phi\) be the positive even theta probability density of the pinned
source:

\[
\widehat\phi(t)=X(t)=\Xi(t)/\Xi(0),\qquad
K_W*\phi=0,\qquad V_X=\int x^2\phi(x)\,dx<\infty.
\tag{12}
\]

All fixed derivatives of \(\phi\) have a bound
\(\exp(C|x|-c e^{2|x|})\); in particular they have every Gaussian moment.
These are unconditional source identities, with no assertion about the
zeros of Xi.

Write \(M=M_a\) temporarily and take \(a\) large enough that
\(M\ge\max(1,V_X)\). The canonical product gives, for all complex \(z\),

\[
|F_a(z)|\le e^{M|z|^2/2},\qquad
|F_a(t)-1|\le e^{Mt^2/2}-1\quad(t\in\mathbb R).
\tag{13}
\]

The latter follows by expanding finite products and passing to the
locally uniform limit. Let

\[
G_M(x)=(4\pi M)^{-1/2}e^{-x^2/(4M)},\qquad v_M=\phi*G_M.
\]

This is another complete-source null function, with transform
\(X(t)e^{-Mt^2}\). Since \(\phi\) is a probability density,
\(|X(t)|\le1\) and \(X(t)\ge1-V_Xt^2/2\).
It follows that

\[
F_a(t)X(t)\ge 2-\tfrac12 V_Xt^2-e^{Mt^2/2}.
\]

Parseval and the elementary Gaussian integrals give

\[
\begin{aligned}
\langle f_a,v_M\rangle
&\ge\frac{2-\sqrt2-V_X/(4M)}{2\sqrt{\pi M}}\\
&\ge\frac{7/4-\sqrt2}{2\sqrt{\pi M}}
=:\frac{c_*}{\sqrt M}>0.
\end{aligned}
\tag{14}
\]

All integrals are absolutely convergent by (13).
This overlap becomes smaller as \(M\) grows, but only by a power.

## 4. Uniform finite theta approximants

The constants in this section are independent of \(M\ge1\), except for
the displayed polynomial factors. Fix \(d_0=49/200\).
Completing the square in the Gaussian convolution shows

\[
|v_M(x)|+|v_M'(x)|\le C e^{-d_0x^2/M}.
\tag{15}
\]

For details, choose \(d_0<d_1<1/4\). The Gaussian and its derivative
are bounded by
\(C\exp(-d_0x^2/M+C_1y^2/M)\) at \(x-y\), after absorbing the derivative
factor using the fixed gap between \(d_0\) and \(d_1\).
The integral of \(\phi(y)e^{C_1y^2/M}\) is uniformly bounded by its value
with \(M=1\). This proves (15) without allowing a hidden growing
Gaussian-moment constant.

Periodize \(v_M\) with period \(2a\), truncate to \(|n|\le N_a\), subtract
the resulting value at \(a\), and normalize the integral to one.
Call this polynomial \(v_a\), extended by zero. Its derivative is zero
at both endpoints because it is an even trigonometric polynomial.
After subtraction the value is zero too, so the extension is \(C^1\).

The physical periodization error and its first derivative are bounded
by \(C e^{-d_0a^2/M}\). The omitted Fourier series and its derivative
are bounded by

\[
C a^C e^{-M\pi^2N_a^2/a^2}.
\tag{16}
\]

Gaussian tail integration proves (16) uniformly for the present
\(1\le M\le a\) and \(N_a\ll a^2\). The latter exponent is at least
\((4\pi^2/25)a^2/M\), since \(N_a\ge(2/5)a^2/M\).
It is strictly larger than \(d_0a^2/M\).
Endpoint subtraction and mass normalization multiply these errors by
at most a fixed power of \(a\); the normalizing integral tends to one.

Both inside and outside \([-a,a]\), these estimates imply

\[
\begin{gathered}
|v_a(x)-v_M(x)|+|(v_a-v_M)'(x)|
\le B_a e^{-2|x|},\\
B_a\le C a^C \exp(-d_0a^2/M+2a).
\end{gathered}
\tag{17}
\]

Outside the interval, maximize \(-d_0x^2/M+2|x|\).
Its maximum on \(|x|\ge a\) occurs at the boundary for all large \(a\),
because \(a/M=10\log a\to\infty\).

For clarity, the complete-source residual bound used here is

\[
|r(x)|+|r'(x)|\le B e^{-2|x|}
\quad\Longrightarrow\quad
|(K_W*r)(x)|\le CB e^{2|x|}.
\tag{18}
\]

It follows directly from the unchanged physical formula

\[
\begin{aligned}
(K_W*r)(x)={}&2\int\cosh((x-y)/2)r(y)\,dy-c_0r(x)\\
&-\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}
\{r(x+t)+r(x-t)-2e^{-t/2}r(x)\}\,dt\\
&-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\{r(x+\log n)+r(x-\log n)\},
\end{aligned}
\tag{19}
\]

where \(c_0=\log(4\pi)+\gamma\).
The pole term is \(O(Be^{|x|/2})\); the archimedean bracket is \(O(Bt)\)
for \(0<t\le1\), and \(O(B)\) thereafter.
For the prime terms use
\(e^{-2|x\pm\log n|}\le e^{2|x|}n^{-2}\) and the convergent sum
\(\sum(\log n)n^{-5/2}\).

Since \(K_W*v_M=0\), (17)--(18) give

\[
\|A_av_a\|_\infty\le C a^C e^{-d_0a^2/M+4a}.
\tag{20}
\]

Here \(A_a\) is the full interval operator, not a substituted positive
matrix. These \(C^1\), zero-extended functions lie in its operator domain:
their Fourier decay suffices for the logarithmic multiplier in \(L^2\);
the remaining interval operators are bounded. In particular
\(q_a(f,v_a)=\langle f,A_av_a\rangle\).

Combining (9), (17), (20), and \(a^2/M=10a\log a\) yields

\[
\begin{gathered}
\|f_a\|_1\|A_av_a\|_\infty=o(M^{-1/2}),\\
|\langle f_a,v_a-v_M\rangle|=o(M^{-1/2}),\\
\langle f_a,v_a\rangle\ge c_*/(2\sqrt M)
\quad\text{eventually}.
\end{gathered}
\tag{21}
\]

In fact the first two errors decay faster than every fixed exponential
in \(a\).

For a broad mass-one comparator, take a fixed even smooth probability
density \(\eta\) supported in \((-1,1)\), and start with
\(w^{(a)}=v_M*\eta_{a/2}\), where
\(\eta_{a/2}(x)=(2/a)\eta(2x/a)\).
Its \(L^2\) norm squared is at most \(C/a\), and it remains a complete-source
null function. Repeat the same finite approximation, endpoint subtraction,
and normalization to obtain \(w_a\in\mathcal T_a\).
The physical boundary distance is now \(a/2\); the Fourier tail is
unchanged because \(|\widehat\eta|\le1\) on the real axis. Therefore

\[
\begin{gathered}
\int w_a=1,\qquad \|w_a\|_1\le C,\qquad
\|w_a\|_2^2\le C/a,\\
\|A_aw_a\|_\infty\le
C a^C e^{-d_0a^2/(4M)+4a}=:\epsilon_a,\qquad
|q_a[w_a]|\le C\epsilon_a.
\end{gathered}
\tag{22}
\]

Both \(a\epsilon_a\) and \(\sqrt M\,\epsilon_a\) tend to zero.

## 5. Convergence of the legal shifts

Let \(c_a=(\int u_a)^{-1}>0\).
The exact finite equation and mass-constrained minimum are

\[
(T_a-\kappa_a)f_a=c_a1,\qquad
c_a=\min_{\int h=1}\{q_a[h]-\kappa_a\|h\|_2^2\}.
\tag{23}
\]

Expanding about \(f_a\) proves the minimum: mass-zero perturbations have
zero cross term and \(T_a-\kappa_a\) is positive definite.

Pair with \(v_a\):

\[
c_a=-\kappa_a\langle f_a,v_a\rangle+r_a,\qquad
|r_a|\le\|f_a\|_1\|A_av_a\|_\infty.
\tag{24}
\]

If \(\kappa_a<0\), comparison with \(w_a\) gives

\[
|\kappa_a|\left(\frac{c_*}{2\sqrt M}-\frac Ca\right)
\le |r_a|+C\epsilon_a.
\tag{25}
\]

The bracket is at least \(c_*/(4\sqrt M)\) eventually.
Equations (21)--(22) prove that negative shifts tend to zero.
If \(\kappa_a\ge0\), legality and the comparator Rayleigh quotient give

\[
0\le\kappa_a<\lambda_a
\le\frac{q_a[w_a]}{\|w_a\|_2^2}
\le2a C\epsilon_a\longrightarrow0,
\tag{26}
\]

where mass one implies \(\|w_a\|_2^2\ge1/(2a)\).
Thus \(\kappa_a\to0\) in all cases. The even minimum of \(T_a\) is
eventually bounded below by a uniform constant.

## 6. A fixed test for the \(a\log a\) finite consumer

**Theorem 2.** Let \(N_a=\lceil4a\log a\rceil\), and let
\(\lambda_a^{\rm even}\) be the lowest eigenvalue of the exact even
compression of (1). If \(\lambda_a^{\rm even}\ge-C\) for every sufficiently
large integer \(a\), for some fixed \(C\), then RH holds.

This is a consumer for this exact integer sequence. No claim that finite
matrix minima are lower bounds for the continuum minimum is made.

Define a fixed entire transform and its inverse Fourier transform by

\[
G(z)=\exp(1-\cosh(z/10)),\qquad
g(x)=\frac1{2\pi}\int_{\mathbb R}G(t)e^{itx}\,dt.
\tag{27}
\]

Then \(g\) is real and even, but no sign is needed. Shift the integration
line to imaginary part \(12\) for \(x>0\), and to \(-12\) for \(x<0\).
On either line,

\[
|G(u\pm12i)|=\exp(1-\cosh(u/10)\cos(6/5)).
\]

Here \(\cos(6/5)>0\). The horizontal integrals of this expression times
any fixed power of \(|u|+12\) are finite; the closing vertical sides
vanish by their doubly exponential decay. Differentiating under the
integral thus proves, for every fixed \(j\),

\[
|g^{(j)}(x)|\le C_j e^{-12|x|}.
\tag{28}
\]

For \(t\ge0\), set

\[
h_t(x)=g(x-t/2)+g(x+t/2),\qquad a=\lceil t\rceil,
\tag{29}
\]

using any larger fixed starting integer when needed.
Both centers are at distance at least \(a/2\) from the boundary.
Periodize \(h_t\) with period \(2a\), truncate at \(N_a\), and subtract
the endpoint value. Let \(p_{a,t}\) be the resulting polynomial extended
by zero. It is even and \(C^1\) after extension.

The physical periodization error, its first derivative, and the endpoint
value are \(O(e^{-6a})\). The Fourier coefficients before truncation
are sampled values of
\(2G(n\pi/a)\cos(n\pi t/(2a))\), divided by \(2a\).
Since \(|G(u)|\le e\exp(-e^{|u|/10}/2)\), Gaussian-style tail integration
with the substitution \(y=e^{\pi n/(10a)}\) gives, also with one derivative,

\[
\text{Fourier tail}
\le C a^C
\exp\left(-\frac14 a^{\,2\pi/5}\right).
\tag{30}
\]

For example, the sum of
\((1+n/a)e^{-\frac12 e^{\pi n/(10a)}}\) beyond \(N_a\) is bounded by
its first term plus its integral. The polynomial and logarithmic factors
in that integral are absorbed by weakening \(1/2\) to \(1/4\).
The inequality \(N_a\pi/(10a)\ge(2\pi/5)\log a\) gives (30).
Since \(2\pi/5>1\), this is faster than every fixed exponential in \(a\).

Writing \(r=p_{a,t}-h_t\), (28)--(30) imply

\[
|r(x)|+|r'(x)|\le B_{a,t}e^{-2|x|},\qquad
B_{a,t}\le C e^{-4a}
+C a^C e^{2a-\frac14 a^{2\pi/5}}.
\tag{31}
\]

Inside the interval multiply the uniform error by \(e^{2a}\).
Outside it use
\(|h_t(x)|+|h_t'(x)|\le C e^{-12(|x|-t/2)}\);
after multiplication by \(e^{2|x|}\), its maximum on \(|x|\ge a\)
is at the boundary and is at most \(C e^{-4a}\).

The \(L^1\) and \(L^2\) norms of \(h_t\) and \(p_{a,t}\) are uniformly
bounded, and their squared \(L^2\) norms differ by \(o(1)\).
Using (18), symmetry of the complete-source pairing, and (28), we obtain

\[
\begin{aligned}
|q[p_{a,t}]-q[h_t]|
&\le CB_{a,t}\int
 (|p_{a,t}(x)|+|h_t(x)|)e^{2|x|}\,dx\\
&\le C B_{a,t}e^{2a}=o(1).
\end{aligned}
\tag{32}
\]

The last bound also uses
\(\int |h_t(x)|e^{2|x|}dx\le C e^t\le C e^a\).
All pairings are absolutely defined with the cancellation in the
archimedean term; the fixed exponential decay rate exceeds the growth
of the prime measure and the pole kernels. This verifies the finite
approximation against the actual source.

Let \(z_\rho=(\rho-1/2)/i\), so \(iz_\rho=\beta-1/2+i\gamma\).
The explicit formula gives

\[
q[h_t]=2q[g]+2C_g(t),\qquad
C_g(t)=\sum_\rho G(z_\rho)^2e^{iz_\rho t}.
\tag{33}
\]

The series is real by the zero symmetries. It converges absolutely:
\[
|G(z_\rho)|\le
\exp\{1-\cos(1/20)\cosh(\gamma/10)\},
\]
using the unconditional strip \(0<\beta<1\).
Together with \(N(T)=O(T\log(2+T))\), this also justifies all local
derivatives and the Laplace transformation below. The compact-test
explicit formula extends to this fixed test by smooth cutoffs and
these source-side and zero-side bounds.

The hypothesized uniform finite lower bound, applied to \(p_{a,t}\),
and (32)--(33) give \(C_g(t)\ge-C'\) for every \(t\ge0\), after enlarging
the constant over a bounded initial interval. Hence
\(D(t)=C_g(t)+C'\) is nonnegative. Initially for \(\Re w>1/2\),

\[
\int_0^\infty D(t)e^{-wt}\,dt
=\sum_\rho\frac{G(z_\rho)^2}{w-iz_\rho}+\frac{C'}w.
\tag{34}
\]

The right side is meromorphic on the entire plane, normally convergent
away from its discrete poles, and has no real pole at \(w>0\).
Zeta has no real nontrivial zero: on \(0<s<1\), adjacent-term pairing
makes the alternating eta series positive while \(1-2^{1-s}<0\).

For a nonnegative function, its finite Laplace convergence abscissa is
a real singularity. A short proof is to expand its transform around a
real point just to the right of a hypothetical regular abscissa.
Every Taylor term evaluated to the left is nonnegative; Tonelli would
then give convergence to the left, a contradiction. Derivatives under
the integral are justified by the strict initial gap to the abscissa.
Applying this fact to (34), the abscissa is at most zero, or is minus
infinity. Thus (34) is holomorphic in \(\Re w>0\).

Every hypothetical zero with \(\beta>1/2\) would give a pole in that
half-plane, with nonzero residue \(m_\rho G(z_\rho)^2\).
The coefficient never vanishes because (27) is an exponential.
This contradiction proves Theorem 2. The functional equation gives RH.

Equations (25)--(26) supply the uniform finite lower bound required by
Theorem 2, completing the proof of Theorem 1.

## 7. Exact progress and the unresolved arithmetic

The new component replaces a uniform variance bound by the growing bound
\(a/(10\log a)\), removes physical positivity, and uses \(4a\log a\)
modes instead of a quadratic or cubic number. The complete arithmetic
source remains in every residual and variational comparison.

The proof establishes neither that such legal shifts exist nor that
their variance satisfies (4). Its compatible cosine-power witness is
not a solution of the source equation. The unconditional prime-discrepancy
floor in the companion packet also does not supply (4).

No extrapolation from finite numerical variances, sampled physical
signs, or a fitted matrix trend is used. No improvement to the imported
zero-free boundary is claimed.

The new assertion is an analytic implication, proved by the argument
above. A finite checker can verify its algebraic constants, canonical
products at selected finite cases, and normalizations; it cannot verify
the open all-scale source hypothesis.
