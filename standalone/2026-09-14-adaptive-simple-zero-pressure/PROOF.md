# Adaptive pressure blocks improve the seven-gap simple-zero deduction

Date: 2026-09-14. Status: **PROPOSED new component proofs; independent review required.**
RH is not proved. No world-record or external-priority claim is made.

This note improves a quantitative deduction, rather than introducing another
RH-equivalent condition. With exactly the retained seven-gap inequality and
the analytic/simple-zero Gram contract used in the earlier 269/280-point
arguments, its proposed lower proportion is

\[
 H_* = \frac{x_* H_0-1/500}{x_*-19/5000}
      =0.67304418043470187172\ldots,
 \quad x_* =\frac{1+\sqrt{1383/1250}}2,
 \quad H_0=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\tag{1}
\]

The previous 280-point deduction gives 0.67300965227913691201... from the
same inputs. The difference is about 0.000034528155565 in proportion, or
0.0034528155565 percentage points. This is a modest quantitative improvement,
not an RH-strength estimate. The finite seven-gap certificate and the full
external trace/mean-square analysis are inherited inputs, NOT re-proved by
this note's bounded checker. No new asymptotic correlation estimate is assumed.

## 1. Fixed inputs and what is new

Let

\[
 K(x)=\int_{-1/2}^{1/2}\cos(\sqrt2 t)\cos(2\pi xt)\,dt,
 \quad k(x)=K(x)/K(0),\quad K(0)=\sqrt2\sin(1/\sqrt2),
 \quad w(x)=k(x)^2.
\]

The integral defining k is the Fourier transform of a positive probability
density, so each finite matrix (k(y_i-y_j)) is positive semidefinite with
unit diagonal. All point configurations below are ordered on the real line.
Repeated points are allowed for the finite statements; actual simple zeros
have distinct ordinates.

**Finite input P7.** For all six nonnegative gaps,

\[
 \frac1{3000}\sum_{i=1}^6 g_i+
 \sum_{s=1}^6\frac{2}{7-s}\sum_{i=1}^{7-s}
    w(g_i+\cdots+g_{i+s-1})\ge\frac{19}{5000}.
\tag{2}
\]

This is the ainta seven-gap inequality. The integrated repository retains a
separate replacement computation in reviews/A/supplement, with its own
primitive arithmetic and closed-cover proof. This note imports (2) at that
stated review/execution boundary; it does not rehabilitate a defective old
wrapper, identify two different transcripts, or claim a fresh replay.

Put alpha=1/500, beta=19/5000 and ell=6. Summing (2) over all seven-point
windows of a consecutive m-point block B gives

\[
 E_B+\alpha L_B\ge\beta(m-\ell),\quad
 E_B=2\sum_{i<j\ \mathrm{in}\ B}w(y_j-y_i),\quad
 L_B=\max B-\min B.
\tag{3}
\]

A pair spanning s gaps occurs in at most 7-s windows; a gap in at most six.
All extra pair terms are nonnegative. For m<=6, (3) follows from
nonnegativity directly. The coefficient alpha includes the required factor
six; it is NOT 1/3000.

For a PSD matrix G define

\[
 \Delta(G)=\operatorname{Tr}\Psi(G),\qquad
 \Psi(t)=\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2.\end{cases}
\tag{4}
\]

The new part is an adaptive partition theorem in Sections 2--3, its
fixed-size localization in Section 4, and the constant (1). The stability
inequality, the kernel, the seven-gap input, and the 269-point lift already
appear in the external ainta source; they are not newly authored here.
The 280-point improvement is the source-pinned repository predecessor.

## 2. A global spectral envelope and exact pinching

Define

\[
 \varphi(E)=\begin{cases}E,&0\le E\le1,\\2\sqrt E-1,&E\ge1.\end{cases}
\]

For every PSD matrix G, without any trace normalization,

\[
 \Delta(G)\ge\varphi\bigl(\operatorname{Tr}(G-I)^2\bigr).
\tag{5}
\]

Indeed, for each eigenvalue lambda>=0,
Psi(lambda)=varphi((lambda-1)^2). The scalar function varphi is increasing,
concave, and zero at zero. Concavity implies
varphi(a)+varphi(b)>=varphi(a+b): apply concavity between 0 and a+b at
weights a/(a+b) and b/(a+b), with the zero case separate. Iteration proves
(5). There is no inference of operator concavity and no assumption E<2.
For the exact kernel Gram, unit diagonal makes Tr(G-I)^2 precisely E_B.

For disjoint principal blocks G_B of a PSD matrix G, convexity of Psi gives

\[
 \Delta(G)\ge\sum_B\Delta(G_B).
\tag{6}
\]

To verify (6), choose an orthonormal eigenbasis of each principal block and
complete it on the unused coordinates. For each such unit vector u, scalar
Jensen applied to the spectral resolution of G gives
Psi(<u,Gu>)<=<u,Psi(G)u>. Sum, and discard only the nonnegative terms on
unused coordinates. This proves trace pinching without assuming Psi itself
is operator-convex.

## 3. The adaptive first-crossing theorem

This statement works for any alpha>=0, beta>0, integer ell>=1, and any
correlation kernel whose every consecutive block satisfies (3).

Fix c>0. Starting at the first unused point, enlarge a consecutive block until
its pressure

\[
 p(B)=\beta(|B|-\ell)-\alpha L_B
\]

first reaches c. Close that block and repeat. If the points end before the
next crossing, retain the remaining incomplete block. At the initial point
p=beta(1-ell)<=0. Appending a point with preceding gap g changes pressure by
beta-alpha g<=beta. Pressure is NOT assumed monotone: a large gap can lower
it by arbitrarily much. First crossing alone proves

\[
 c\le p(B)<c+\beta
\tag{7}
\]

for each closed block. By (3),(5), each such block contributes at least
varphi(c) to (6).

Let q be the number of closed blocks, m the total number of points, and L
the total span (zero for an empty/singleton configuration). The raw pressure
beta|B|-alpha L_B equals p(B)+ell beta. Thus each closed block has raw
pressure below c+(ell+1)beta, and the incomplete remainder has raw pressure
below c+ell beta. If it is empty its raw pressure is zero, still bounded by
that positive allowance. Interblock gaps are nonnegative. Therefore

\[
 \beta m-\alpha L
 =\sum_{\mathrm{blocks}}(\beta|B|-\alpha L_B)
        -\alpha\sum_{\mathrm{cut\ gaps}}g
 \le q\{c+(\ell+1)\beta\}+c+\ell\beta.
\tag{8}
\]

Combining the count from (8) with (6),(7) proves the COMPLETE finite bound

\[
 \boxed{\Delta(G_m)\ge
 \kappa(c)\{\beta m-\alpha L-c-\ell\beta\},\qquad
 \kappa(c)=\frac{\varphi(c)}{c+(\ell+1)\beta}.}
\tag{9}
\]

When the right side is negative it may be replaced by zero. There is exactly
one incomplete-remainder charge, not one per fixed-size block. No gap has
been omitted with a favorable sign, no count is rounded up, and no assumption
on a maximal block length is used. Adaptive blocks need not be optimal; (9)
is the guarantee of this particular explicit rule.

The improvement over fixed 269/280-point partitions comes from waiting for
pressure to accumulate rather than paying the six-point window loss at every
predetermined short block boundary. The spectral envelope (5) is in fact
weaker than the trace-aware 280-point envelope; the gain is in assembly.

## 4. Transfer to the actual zero Gram: keep the two limits separate

Write N=N(T,2T) for the number of nontrivial zeta zeros with T<Im rho<=2T,
counting multiplicity, and S=N_0^s(T,2T) for those that are simple and on the
critical line. The following is the EXACT imported analytic contract used
in the preceding source-qualified 269/280 deductions.

(A1) After deleting o(N) endpoint points, the retained simple zeros have a
PSD Gram M_T and ordered normalized ordinates y_i with total span <=N+o(N).
The retained count differs from S by o(N).

(A2) For every FIXED integer M and every FIXED finite separation bound L_0,
each consecutive M-point principal block with span <=L_0 converges entrywise
UNIFORMLY to (k(y_i-y_j)), with error o_T(1). This includes the diagonal;
the actual finite diagonal need not equal one exactly.

(A3) The external trace/mean-square/tail estimates and the stability-enhanced
rank--inertia argument give

\[
 S\ge H_0N+\Delta(M_T)-o(N).
\tag{10}
\]

These are not a new random-phase assumption or an RH hypothesis. Their
specific source derivation is inherited from the ainta proof and the
integrated supplement S02, using the Montgomery--Taylor test family and the
unconditional analytic inputs of the cited proportion theorem. Their full
external analytic proofs and formalization are NOT re-audited in this pass.
An independently accepted zeta proportion requires accepting this contract
and (2), not merely the new finite calculation.

For clarity, the elementary stability step underlying (A3) is as follows.
If V has r columns of norm at most one, P=VV*, M=V*V, and Q is Hermitian with
n_+(Q)<=b, then

\[
 \|P+Q\|_F^2\ge4\operatorname{Tr}(P+Q)-3r-4b+\Delta(M).
\tag{11}
\]

Write Q=Q_+-Q_-, with Q_+ Q_-=0. The positive part costs at least
4 Tr Q_+-4b. Von Neumann's trace inequality and minimization of
(p-n)^2+4n over n>=0 give 2p-1+Psi(p). Summing with zero padding and
Tr P<=r proves (11). The arithmetic trace values and source-overlap
normalizations still enter through (A1)--(A3). More explicitly, in the
external normalization one has a Hermitian H_T=P+Q with
Tr H_T=N+o(N), ||H_T||_F^2=(2-H_0)N+o(N), and
n_+(Q)<=(N-S)/2+o(N). The number of retained unit-bounded columns is
S+o(N). Substitution in (11) gives
S>=4 Tr H_T-2N-||H_T||_F^2+Delta(M_T)-o(N), which is (10).
These named trace/overlap statements, not an unproved new correlation
asymptotic, are exactly the analytic import.

## 4.1 Why an unbounded greedy block cannot be used directly

Although (9) is finite-exact at every size for the LIMIT kernel, (A2) only
allows fixed-size, fixed-span comparisons. Do not apply (A2) to the full
adaptive partition at growing height.

Instead fix an outer size M, independently of T, and set C_0=c+ell beta.
Apply (9) to each exact M-point kernel block. If beta M-alpha L_B-C_0<=0,
nonnegativity alone proves the needed lower bound for its actual block. If
the expression is positive, L_B<beta M/alpha when alpha>0, a fixed bound.
For the present alpha=1/500 this is finite. Hence (A2) applies uniformly.

Psi is globally 2-Lipschitz on the nonnegative axis. If the entrywise error
is <=delta_T(M), its spectral norm is <=M delta_T(M); Weyl's eigenvalue
bound then bounds the change of trace Psi by <=2M^2 delta_T(M)=o_M(1).
This treats the diagonal perturbation as well. Therefore each actual block
satisfies (9), with a uniform o_M(1) loss. No eigenvalue gap is needed.

## 4.2 Outer pinching and all boundary charges

For each offset j=0,...,M-1, discard the first j retained points, form full
M-point consecutive blocks, and discard the final remainder. At most 2M
points are discarded for that offset. By (6), the full defect dominates the
sum over its full blocks. There are at most S/M such blocks. Averaging over
offsets, each interior adjacent gap appears in at most M-1 block spans.
There are O(N) blocks for each fixed M and their uniform o_M(1) errors sum
to o_M(N). Equations (A1),(9) give

\[
 \Delta(M_T)\ge\kappa(c)\left[
  \left(\beta-\frac{C_0}{M}\right)S
  -\alpha\left(1-\frac1M\right)N\right]-o_M(N).
\tag{12}
\]

The discarded O(M) point charge is constant in T and is absorbed in o_M(N).
If S=0 or fewer than M points occur the finite inequality has a harmless
constant boundary loss; it gives the same asymptotic conclusion. Formula
(12) does not rely on a distribution of individual gaps or mean spacing
inside a selected block.

Combine (10),(12). For every sufficiently large FIXED M,

\[
 \liminf_{T\to\infty}\frac SN\ge
 H_{M,c}:=
 \frac{H_0-\kappa(c)\alpha(1-1/M)}
 {1-\kappa(c)\{\beta-C_0/M\}}.
\tag{13}
\]

For the constants used below the denominator is strictly positive. First
take T to infinity at each fixed M. Only AFTERWARD let M go to infinity in
the numerical lower bounds (13). This is a supremum of already valid lower
bounds, not an exchange of two limits of Gram matrices. We obtain

\[
 \boxed{\liminf_{T\to\infty}\frac SN\ge
 H(c)=\frac{H_0-\kappa(c)\alpha}{1-\kappa(c)\beta}.}
\tag{14}
\]

No new uniform-in-M trace estimate or rate of kernel convergence is required.
For example, the rational threshold c=1 and fixed outer M=10^6 already give
H_{M,1}>0.673043, strictly above the previous 280-point figure. The optimized
limit below is stronger, but a strict improvement does not depend on using
an infinite outer size in an actual application.

## 5. Optimize a scalar, not a new zeta assumption

For the present constants beta H_0>alpha. Thus H(c) is increasing in kappa,
since its derivative with respect to kappa is
(beta H_0-alpha)/(1-kappa beta)^2>0.

Put A=(ell+1)beta. For 0<c<=1, kappa=c/(c+A) is increasing. For c=x^2>=1,

\[
 \kappa=\frac{2x-1}{x^2+A},\qquad
 \frac{d\kappa}{dx}=\frac{2(-x^2+x+A)}{(x^2+A)^2}.
\]

The unique maximum is at x_*=(1+sqrt(1+4A))/2. Since x_*^2=x_*+A,
the maximal kappa equals 1/x_*. Substitute ell=6, beta=19/5000 and
alpha=1/500 to obtain exactly (1). This is optimization ONLY within (9),
not a proof that (1) is the optimal consequence of the seven-gap inequality.

The checker encloses the constants by rational arithmetic. For q=1/sqrt(2),
q cot q=cos(q)/(sin(q)/q), and both numerator and denominator have alternating
rational Taylor series because q^2=1/2. Their complete next-term remainders
are included. Integer square-root bounds enclose sqrt(1383/1250) and the
older 280-point radical. No floating value defines an accepting endpoint.

## 6. What has and has not advanced

The new finite theorem (9) and its transfer (12)--(14) improve the previously
computed lower proportion from the SAME finite pressure input and SAME
analytic contract. There is no additional unproved asymptotic sign estimate
between those inputs and (1). This is the proposed advance relative to the
inspected sources, not another equivalence with RH and not a new kernel
certificate. Independent proof review is still required.

The record-lift prerequisites have not vanished: (2), (A1)--(A3), and the
correct simple-versus-distinct, multiplicity and endpoint conventions must
be retained. No fresh seven-gap exhaustive run, external theorem proof,
Lean build, zero computation, or external priority audit was performed.
The critical-line proportion remains far from one, and even density one
would not on its own imply RH.

A useful next mathematical improvement is to reduce the first-crossing
overshoot or the incomplete-window loss while retaining an auditable
partition and a uniform finite-block transfer. A stronger local pressure
inequality could also be inserted into the general theorem. Neither is
assumed to establish the present bound, and neither is claimed solved here.
