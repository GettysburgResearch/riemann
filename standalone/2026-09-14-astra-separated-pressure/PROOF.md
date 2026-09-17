# Separated-core transfer of seven-point pressure

Date: 2026-09-14. Status: **proposed analytic improvement, requiring independent
mathematical review. RH is not proved.**

This is an add-only continuation for PR #875, based on its inspected head
`00af30b4b3f810c7cd03fe94ba2f43b6c6b90538`. It changes none of the previous
research packets or their acceptance status.

The proposed improvement is

\[
 \liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
 \ge h_{\rm sep}:=\frac{5000h_{\rm MT}-10}{4981}
 =0.6730583253156109\ldots,
\]
where
\[
 h_{\rm MT}=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\]
Here the numerator counts simple zeros on the critical line; the denominator
counts all nontrivial zeros with their multiplicities. The distinct-zero
consequence is `(1+h_sep)/2 = 0.8365291626578054...`.

The analytic zeta inputs are exactly the finite-Gabor explicit-formula,
prime-side trace/mean-square and zero-tail inputs used in the August 10, 2026
paper cited as [Z]. Its Theorem D supplies the optimized window. The
seven-point inequality is the existing computer-assisted theorem [7], with
its independently implemented repository replay [A]. No new zero-density,
Mertens, unbounded matrix-positivity, or RH hypothesis is assumed. These
imports have their own review status; reproducing the finite computation is
not a new proof of [Z]'s number-theoretic estimates.

The new deduction is an all-cardinality lower bound for the spectral defect.
It removes the loss from fixed 269/280-point blocks by separating a sparse
core from close pairs. The growing actual matrix is controlled by pointwise
Fourier majorization, NOT by summing entrywise approximation errors. The
constant is a proposed improvement over the pinned repository deduction, not
an asserted world record or exhaustive priority determination.

## 1. Kernel, spectral defect and the exact imported pressure

Put
\[
 q(t)=\cos(\sqrt2t)\mathbf1_{[-1/2,1/2]}(t),\qquad
 K(x)=\int q(t)e^{2\pi ixt}\,dt,
 \quad K_0=K(0)=\sqrt2\sin(1/\sqrt2),
\]
\[
 k(x)=K(x)/K_0,\qquad w(x)=k(x)^2.
\]
These are real even functions. The kernel Gram matrix
`M_X=(k(x_i-x_j))` is positive semidefinite and has diagonal one. In particular
`|k(x)| <= 1`.

For a positive semidefinite matrix define
\[
 \Delta(M)=\operatorname{tr}\Psi(M),\qquad
 \Psi(t)=\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2.\end{cases}
 \tag{1}
\]
The scalar function is convex and nonnegative. Trace pinching therefore gives
`Delta(M) >= sum Delta(M_B)` for any partition of its coordinates: pinching
is an average of unitary conjugations and `tr Psi` is convex and unitarily
invariant. Operator convexity of Psi is not being asserted.

Use `a=19/5000`, `b=1/500`. The EXACT imported inequality is, for every six
nonnegative gaps,
\[
 \frac1{3000}\sum_{i=1}^6g_i+
 \sum_{s=1}^6\frac2{7-s}\sum_{i=1}^{7-s}
 w(g_i+\cdots+g_{i+s-1})\ge a.                 \tag{2}
\]
Its continuum coverage comes from the exhaustive interval proof in [7]/[A],
not from a sampled gap grid. Our local replay preserves the upstream bytes
and arithmetic convention. See VALIDATION.md for the modes actually run.

Summing (2) over consecutive seven-point windows of an ordered set of `m`
points gives
\[
 E_X+b\,\operatorname{span}X\ge a(m-6),\qquad
 E_X=2\sum_{i<j}w(x_i-x_j).                    \tag{3}
\]
Indeed a pair of index separation `s<=6` occurs at most `7-s` times; each gap
occurs at most six times; and every omitted summand is nonnegative. For
`m<7`, (3) follows directly because its right side is nonpositive. The span
of an empty or one-point set is zero.

The earlier proof converts E to Delta inside fixed-size blocks. That loses
energy when eigenvalues exceed two. The next two lemmas avoid that loss.

## 2. A rationally certified Fourier majorant

Define
\[
 \delta=\frac23,\qquad
 U(t)=\frac65\left(\frac{\sin(2\pi t/3)}{2\pi t/3}\right)^2.
 \tag{4}
\]
The removable value at zero is used. Then
\[
 U\ge q,\quad U\ge0,\quad
 \widehat U(\xi)=\frac95(1-|\xi|/\delta)_+,\quad
 \int U=\frac95.                                      \tag{5}
\]
The Fourier transform in this section uses `exp(-2 pi i xi t)`. The triangular
transform is the elementary convolution of two interval indicators. In
particular it is ZERO at the endpoints `|xi|=delta`, not just outside them.

Here is a complete elementary proof of the majorization. Outside
`[-1/2,1/2]` it is immediate. On that interval set `y=t^2`, `u=2 pi t/3`.
Alternating sine and cosine estimates give
\[
 \operatorname{sinc}u\ge1-u^2/6>0,\qquad
 \cos(\sqrt2t)\le1-y+y^2/6.
\]
Squaring the first lower bound and using `9<pi^2<10` gives
\[
 \operatorname{sinc}^2u\ge1-\frac{40}{27}y+\frac49y^2.
\]
Therefore
\[
 U(t)-q(t)\ge P(y):=\frac15-\frac79y+\frac{11}{30}y^2
 \ge P(1/4)=\frac{41}{1440}>0.                         \tag{6}
\]
The last inequality follows from `P'(y)<0` on `[0,1/4]`. Every coefficient and
endpoint in (6) is checked with rational arithmetic. The use of `pi^2<10`
in the negative coefficient and `pi^4>81` in the positive coefficient has the
correct direction.

**Lemma 1 (whole separated block).** If `|x_i-x_j|>=2/3` for all distinct
indices, then
\[
 \|M_X\|\le\frac9{5K_0}<\frac{108}{55}<2,
 \qquad \Delta(M_X)=E_X.                               \tag{7}
\]
For arbitrary complex `c_i`, integrate `q(t)|sum c_i exp(2 pi i x_i t)|^2`.
Replacing q by U increases this integral. All off-diagonal Fourier terms of
U vanish by separation, leaving `(9/5) sum |c_i|^2`. Divide by K0. The strict
bound `K0>11/12` follows from `sin x>x-x^3/6` at `x=1/sqrt(2)`.
Because every eigenvalue is in `[0,2)`, Psi is exactly the square in (1).
The diagonal of M_X is one, giving the final equality.

This bound holds for every finite cardinality with the SAME constant. It is
not an estimate on finitely many computed Gram matrices.

## 3. Nearby points pay more than their pressure share

**Lemma 2 (a close pair).** For `0<=x<=2/3`, `k(x)>1/3`.

On `[0,1/2]` both `cos(sqrt(2)t)` and `cos(2 pi x t)` are decreasing.
The integral Chebyshev inequality (obtained by integrating the product of
their two differences) gives
\[
 k(x)\ge\frac{\sin(\pi x)}{\pi x}
 \ge\frac{3\sqrt3}{4\pi}>\frac13.                       \tag{8}
\]
The sinc function decreases on `[0,2 pi/3]`: the derivative numerator
`u cos u - sin u` decreases from zero on `(0,pi)`. Chebyshev's inequality does
not require the second cosine to remain positive. For a rational check of
the last strict inequality, use `sqrt(3)>5/3`, `pi<22/7`, so the preceding
quantity exceeds `35/88>1/3`.

The two-point Gram has eigenvalues `1+k` and `1-k` in `[0,2]`. Its defect is
exactly `2k^2>2/9`.

**Theorem 3 (global pressure transfer).** For every ordered finite set X of
m distinct real points,
\[
 \boxed{\Delta(M_X)+\frac{\operatorname{span}X}{500}
             \ge\frac{19}{5000}(m-6).}                   \tag{9}
\]

**Proof.** Break the ordered points into maximal clusters connected by
adjacent gaps STRICTLY less than `2/3`. Equality gaps separate clusters.
Let G be the points in singleton clusters and let B count all other points.
The set G is `2/3`-separated. In each nonsingleton cluster pair consecutive
points, leaving one singleton if necessary. Each pair has separation less
than `2/3`. A cluster of size ell has `floor(ell/2)>=ell/3` such pairs, so the
total number of pairs is at least B/3.

Pinch into ONE block containing all of G, these pairs, and the remaining
singletons. Equations (7),(8) give
\[
 \Delta(M_X)\ge E_G+\frac2{27}B.
\]
Equation (3) for G and `span G<=span X` imply the stronger estimate
\[
 \Delta(M_X)+b\,\operatorname{span}X
 \ge a(m-6)+(2/27-a)B.                                  \tag{10}
\]
The surplus coefficient is positive. Dropping it proves (9). This includes
empty G and small m. No pair or leftover point is counted twice. QED.

The close clusters are not deleted. Their contribution is paid explicitly.
There is no hypothesis that the zeta zeros themselves have a minimum spacing.

The argument is an abstract transfer principle: for a unit-diagonal positive
kernel, an operator cap of two on delta-separated sets and a close-pair
squared overlap at least c transfer any energy pressure
`E+b span>=a(m-r)` to the SAME spectral-defect pressure whenever `2c/3>=a`.
Here every hypothesis is proved for the displayed literal kernel; this
abstract observation is not an added unproved zeta assumption.

## 4. Transfer to the ACTUAL finite zero vectors

This is necessary: entrywise `o(1)` on a growing matrix does not imply a small
operator norm. We do not make that inference.

Use the literal optimized window from [Z, Theorem D]. Let
`L=log(T/(2pi))`, `h=2pi/L`, `d=floor(T/h)`, `tau_k=T+kh`, and
\[
 \phi_L(u)=\sqrt{\cos(\sqrt2 u/L)}\,
                   \varrho(L/2-|u|),\qquad
 a_L=L^{-1}\int\phi_L(u)^2du.
\]
Here the fixed-width ramp satisfies `0<=varrho<=1`, vanishes to the left of
zero, and equals one to the right of one. Define
\[
 q_L(t)=\phi_L(Lt)^2\le q(t),\qquad a_L\longrightarrow K_0.
\]
Fourier transforms of phi_L use the convention of [Z], without `2pi` in the
exponent. For a real normalized ordinate `x=(gamma-T)/h`, put
\[
 v_x=\left(\frac{\widehat\phi_L(\gamma-\tau_k)}
                       {\sqrt{a_L}L}\right)_{0\le k<d}.
 \tag{11}
\]
The full-grid Poisson identity [Z, Lemma 2.2] gives the translation-invariant
Gram
\[
 M^{\rm full}_{ij}=a_L^{-1}\int q_L(t)e^{2\pi i(x_i-x_j)t}dt.
 \tag{12}
\]
It has diagonal one. The actual finite Gram is its restriction in the VECTOR
coordinates `0<=k<d`; hence
\[
 0\preceq M^{\rm actual}\preceq M^{\rm full},\qquad
 \|v_x\|\le1.                                          \tag{13}
\]
For any separated subset G, replace q_L by q and then U in its quadratic
form. Equations (5),(12),(13) give directly
\[
 \|M_G^{\rm actual}\|\le\frac9{5a_L}<2
 \quad\text{for all sufficiently large }T.              \tag{14}
\]
For example `a_L>=91/100` gives the rational ceiling `180/91<2`.
This is uniform in the size of G. It includes the finite-grid truncation and
all taper contributions.

Thus
\[
 \Delta(M_G^{\rm actual})=\|M_G^{\rm actual}-I\|_F^2
       \ge2\sum_{i<j\in G}|\langle v_i,v_j\rangle|^2.
 \tag{15}
\]
The actual diagonal is NOT replaced by one; its additional square is
nonnegative. Every actual pair block has trace at most two by (13), so its
whole spectrum lies in `[0,2]` and its defect is at least twice the squared
off-diagonal entry.

### The only entrywise approximation is used on O(N) local terms

Retain simple central zeros whose normalized ordinates lie at distance at
least `L^2` from the finite grid's two ends. The excluded ordinate length is
`O(L)`, so the classical unit-interval zero count discards `O(L^2)=o(N)` zeros.
The padded interval `I'=(T-sqrt(T),2T+sqrt(T)]` used for the global zero matrix
costs `O(sqrt(T) log T)=o(N)` when returning to `(T,2T]`.

Uniformly for retained pairs with normalized separation at most `R_0=57/5`,
\[
 |\langle v_i,v_j\rangle-k(x_i-x_j)|\le\eta_T,
 \qquad \eta_T\longrightarrow0.                        \tag{16}
\]
This is [7]'s kernel comparison, also obtainable directly: `q_L->q` in L1
with error `O(1/L)`. The real Fourier bound
`|phiHat_L(r)|<=C/|r|` follows from its uniformly bounded total variation.
After normalizing (11), the missing square-sum beyond a grid distance L^2 is
`O(L^-2)`; Cauchy--Schwarz bounds the missing overlap. These two bounds yield
(16), without identifying a full growing operator by entrywise convergence.
Uniform bounded variation follows also from monotonicity on each half-line
for the stated ramp/window; a fixed bound suffices.

Both overlaps in (16) have modulus at most one, so their squared moduli
differ by at most `2 eta_T`. A seven-point window of span at least R0 is paid
by its linear term alone, since `R0/3000=a`. All other windows have every pair
in the compact range of (16). The sum of the 21 weighted coefficients in (2)
is twelve, so the actual local inequality loses at most `24 eta_T`.
Summing over windows of G gives
\[
 E_G^{\rm actual}\ge a(|G|-6)-b\,\operatorname{span}X
                              -24\eta_T|G|.             \tag{17}
\]
For `|G|<7` this still holds by nonnegativity.

Use the same cluster partition as Theorem 3. Each close actual pair costs at
least `2(1/3-eta_T)^2`. For sufficiently small eta_T this is positive, and
\[
 \frac23(1/3-\eta_T)^2>a.
\]
Pinching, (15),(17), and at least B/3 pairs therefore yield, for the actual
retained matrix M-circle with S-circle columns,
\[
 \Delta(M^\circ)\ge a(S^\circ-6)-b\,\operatorname{span}X
                                      -24\eta_TS^\circ.
 \tag{18}
\]
Every accumulated comparison error is charged O(S-circle), not O(S-circle^2).
Since `S-circle=S(T,2T)-o(N)` and
`span X<=LT/(2pi)=N(T,2T)+o(N)` by Riemann--von Mangoldt,
\[
 \boxed{\Delta(M^\circ)\ge aS(T,2T)-bN(T,2T)-o(N(T,2T)).}
 \tag{19}
\]

## 5. The rank--trace consumer and the improved zeta constant

For clarity we reproduce the attributed stability refinement [7]. If V has
r columns of norm at most one, `P=VV*`, `M=V*V`, and Q is Hermitian with
`n_+(Q)<=b_+`, then
\[
 \|P+Q\|_F^2\ge4\operatorname{tr}(P+Q)-3r-4b_++\Delta(M).
 \tag{20}
\]
Write `Q=Q_+-Q_-` with orthogonal positive/negative parts. The cross term
`2 tr(P Q_+)` is nonnegative. The positive eigenvalues of Q+ obey
`q^2>=4q-4`, giving `||Q+||^2>=4 tr Q+-4b_+`. Von Neumann's trace inequality
and minimization over eigenvalues n>=0 of Q- give
\[
 \min_{n\ge0}\{(p-n)^2+4n\}=2p-1+\Psi(p).
\]
Pad by zero dimensions when necessary. Summing yields
`||P-Q-||^2>=2 tr P-r+Delta(M)-4 tr Q-`. Adding the Q+ bound and using
`tr P<=r` proves (20). No spectral conclusion about Xi is a premise.

For the normalized finite zero matrix in I', [Z, Sections 4 and 7] supplies
`Ahat=P_simple+Q_other`, `n_+(Q_other)<=s_2+p`, where s2 counts distinct
multiple central zeros and p counts off-line reflection pairs. The complete
count obeys `N(I')>=s_1+2s_2+2p`. Thus (20) gives
\[
 s_1\ge4\operatorname{tr}\widehat A-\|\widehat A\|_F^2
                     -2N(I')+\Delta(M).                  \tag{21}
\]
Pinch M to the retained central block and its complement. The complement's
defect is nonnegative. The named prime-side estimates and the complete
zero-tail estimate in [Z, Proposition 4.2, Theorem D] give
\[
 \operatorname{tr}\widehat G=N(1+o(1)),\qquad
 \|\widehat G\|_F^2=(2-h_{\rm MT})N+o(N),
\]
with trace and norm errors for replacing Ahat by Ghat absorbed in o(N).
These are imported analytic estimates, not inferred from numerical zero data.
Combining them with (21) and the interval/end-strip costs proves
\[
 S(T,2T)\ge h_{\rm MT}N(T,2T)+\Delta(M^\circ)-o(N).
 \tag{22}
\]
Insert (19), rearrange, and divide by N:
\[
 \liminf S/N\ge\frac{h_{\rm MT}-b}{1-a}
              =\frac{5000h_{\rm MT}-10}{4981}.             \tag{23}
\]
This is the claimed proposed improvement. In comparison, [A, S02] obtains
`0.6730096522791369...` using 280-point blocks. The difference is about
`0.0000486730364740` in the proportion, or `0.00486730364740` percentage
points. It is a small quantitative improvement, not a resolution of RH.

For distinct zeros, `2N_d(I')+N(I')>=3s_1+4s_2+4p`. Using (20) instead gives
\[
 N_d(T,2T)\ge\tfrac12(1+h_{\rm MT})N+\tfrac12\Delta(M^\circ)-o(N).
\]
Substitute (19),(23) and `a h_sep-b=h_sep-h_MT` to obtain
\[
 \liminf N_d/N\ge(1+h_{\rm sep})/2.                       \tag{24}
\]
This does not assert that all those distinct zeros lie on the critical line.
The same lower proportions on `(0,T]` follow by summing dyadic intervals:
for each epsilon>0 apply the eventual bound `(h-epsilon)N` to every interval
whose lower endpoint exceeds the corresponding fixed threshold. The omitted
bottom interval has bounded height, hence contributes o(N(T)); then let
epsilon decrease to zero.

## 6. What this changes, and what it does not

The deliverable is a proposed new finite-kernel inequality (9), its
whole-growing-matrix transfer (19), and a numerical increase of a genuine
asymptotic zeta proportion. It does not introduce a fresh RH-equivalent
criterion and leave its premise unproved. The nontrivial pressure premise is
the already certified fixed six-dimensional theorem (2); the asymptotic
analytic inputs are explicitly imported from [Z].

No RH proof, density-one result, new verification height, prime-counting error
bound, or absolute novelty record is claimed. The argument does not improve
the coefficient a in (2), the arithmetic trace estimate, or the old three
routes' missing native cancellation/all-order realization/defect-extinction
bounds. Its gain is specifically the removal of a spectral clipping and
block-boundary loss.

Independent review should concentrate on the pointwise majorant (6),
cluster accounting (10), finite-grid Loewner comparison (13)--(14), the
O(N) rather than O(N^2) use of (16), and the imported [Z] analytic interface.
Finite tests do not substitute for these arguments.

## References and exact source versions

[Z] Claude, *More than two thirds of the zeros of the Riemann zeta function lie
on the critical line*, August 10, 2026 version, 35-page primary-host PDF:
https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf .
Read the normalization, Lemma 2.2, Sections 4 and 7.1, and Theorem D. This is
an explicit preprint import, not a claim of peer-reviewed acceptance or a
fresh independent reproduction of every prime-side argument.

[7] ainta/zeta-simple-zeros at
`040c5e899e658aed7b56a2a87f501798fe10761d`, `paper/riemann.tex`, blob
`fed199bb7e641c718ac1f33d5e885c0b412d5080`: stability inequality, complete
seven-point pressure, and original 269-block consumer. No credit for these
mechanisms is claimed here.

[A] GettysburgResearch/riemann, main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`,
`reviews/A/supplement/REPORT.md`, blob
`e1359f93c399c783e01c86d614fa02e86666671a`, Sections S01--S02: independent
primitive seven-point proof and repaired 280-block consumer. The unchanged
replay sources are included in vendor/ with their exact hashes in SOURCES.json.
