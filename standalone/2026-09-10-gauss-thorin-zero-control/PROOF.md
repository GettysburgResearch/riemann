# GZC26 — Positive source defects give local complex-zero control

2026-09-10. **Proposed component proofs and directed finite certificates; independent mathematical/code review is required. This is not a proof of RH.**

This continuation of GTP26 changes no previous statement or evidence. It obtains actual zero counts, rather than treating a small complex value or a derivative sign as a zero. It also disproves a possible strengthening of the original programme: the third *unsymmetrized* quadrature seed has a zero strictly inside the left half of the critical strip. Reflection protects the particular simple zero treated below. It is not proved to protect every zero at every order or height.

## 1. Exact source and scope

Parent: PR #851, `283f110808eb4865dc1f827c2858a0cccfadd3dc`, `standalone/2026-09-10-gauss-thorin-positive-defect/PROOF.md`, especially Sections 1–2, (18), and the Mellin defect. Base main: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

All variables below are positive, powers use the real logarithm, and gamma parameters are shape and scale. All copies appearing in a sum are independent. Write

\[
\alpha_j=6/(\pi^2j^2),\quad X_*=\sum_{j\ge1}\alpha_jE_j,
\quad L_*(t)=\sqrt{6t}/\sinh\sqrt{6t},\quad c=\pi/6.
\tag{1}
\]

The classical Biane–Pitman–Yor identity, with this scaling, is

\[
\xi(s)=\tfrac12 c^{s/2}\mathbb E(X_*+X_*')^{s/2}.
\tag{2}
\]

Here xi denotes the entire completed zeta function, including removable values at 0 and 1. The source identity is an explicitly imported classical theorem, not a consequence of the computations or an asserted discovery. The source has all positive and negative moments. On `0<Re(s)<1` no removable-point evaluation is needed.

Let `nu=sum alpha_j delta_alpha_j`, a probability measure with infinite support in `(0,1)`. Its moments `mu_l` are generated exactly by

\[
S(t)=\sum_{j\ge0}\frac{6^jt^j}{(2j+1)!},\qquad
S'(t)/S(t)=\sum_{l\ge0}(-1)^l\mu_l t^l.
\tag{3}
\]

For order m, let p_m be the monic orthogonal polynomial for nu, x_i its m simple zeros, and w_i its Gaussian weights. Thus `0<x_i<1`, `w_i>0`, `sum w_i=1`. Define

\[
\begin{split}
X_m&=\sum_{i=1}^m\operatorname{Gamma}(w_i/x_i,x_i),\\
L_m(t)&=\prod_i(1+x_it)^{-w_i/x_i},\\
g_m(t)&=\sum_i\frac{w_i}{1+x_it},\\
Z_m&=X_m+X_m',\\
F_m(s)&=\tfrac12c^{q}\mathbb E Z_m^q,\\
A_m(s)&=\tfrac12\big(F_m(s)+F_m(1-s)\big),\\
q&=s/2,\qquad k=2m+1,\qquad
 d_m=\frac1k\int p_m(a)^2\,d\nu(a)>0.
\end{split}
\tag{4}
\]

These are the parent's depth-zero seeds. A_m differs from the parent's H_{m,0} only by a positive constant, so their zeros agree. No theorem about positive branching depth is claimed in this continuation. The mean of Z_m is exactly 2.

The three conclusions submitted for review are:

| Function | Exact disk centre | Exact radius | Proposed count |
|---|---|---|---|
| F_3 | `0.471003433 + 14.138525882 i` | `1/1000000` | one simple zero, strictly left of the critical line |
| A_3 | `1/2 + 14.138974966 i` | `1/1000000` | one simple zero, exactly on the critical line |
| xi, via A_10 | `1/2 + 14.134725 i` | `1/100000` | one simple zero, exactly on the critical line |

Every displayed finite decimal in this table denotes an exact rational, not a rounded root asserted to that precision. A count concerns the entire open disk and excludes boundary zeros. There is no assertion about the complementary region, no verification of all lower zeros, and no new height record. The xi disk reproduces a familiar low zero by a different source-bound certificate; no zeta evaluator or zero table is an accepting input.

## 2. The complete positive defect, recalled and checked

The parent gives the Gaussian remainder

\[
g(t)-g_m(t)
=t^{2m}\frac{\displaystyle\int p_m(a)^2(1+at)^{-1}\,d\nu(a)}
 {\displaystyle\prod_i(1+x_it)^2},
\qquad g=-L_*'/L_*.
\tag{5}
\]

Put R_m equal to the fraction on the right of (5). It is a positive Laplace transform of mass `k d_m`. Integration gives

\[
\delta_m(t)=\log L_m(t)-\log L_*(t)
=t^k Q_m(t),\quad
Q_m(t)=\int_0^1v^{k-1}R_m(vt)\,dv,
\quad 0\le\delta_m(t)\le d_m t^k.
\tag{6}
\]

For completeness, (5) follows by applying the orthogonality of p_m to the remainder of `1/(z-a)` and substituting `z=-1/t`. Positivity of R_m follows from products and mixtures of exponential and gamma Laplace transforms. Thus Q_m/d_m is a probability Laplace transform.

Since both L_m and L_* have explicit infinitely divisible gamma representations,

\[
\frac{L_m(t)-L_*(t)}{t^k}
=Q_m(t)\int_0^1L_m(t)^\theta L_*(t)^{1-\theta}\,d\theta
\tag{7}
\]

is a positive Laplace transform of mass d_m. Let B_m be the associated positive variable. If Y_m is an independent equal-probability mixture of X_m and X_*, then `C_m=B_m+Y_m` satisfies

\[
\Delta_m(t):=L_m(t)^2-L_*(t)^2
=2d_mt^k\mathbb E e^{-tC_m}.
\tag{8}
\]

These equations provide the whole error law. No finite moment match is substituted for (8). The positive-law construction is the proposed parent dependency, with its proof route reproduced here; the new execution does not constitute independent review of all other parent theorems.

## 3. GZC1: a nonoscillatory envelope for the complete complex error

Define, for `0<a<1`,

\[
J_m(a)=\int_0^\infty t^{-a-1}
             \min(2d_mt^k,1)L_m(t)^2\,dt.
\tag{9}
\]

This uses only the finite gamma seed and the exact rational d_m. It does not require evaluating a complex zeta function or even the infinite source transform.

### Theorem

For `0<Re(q)=a<1`,

\[
\boxed{
|F_m(s)-\xi(s)|
\le \frac{c^a}{2}|(q)_{\underline k}|\,
               \frac{J_m(a)}{\Gamma(k-a)}.}
\tag{10}
\]

For any `0<a_0<a_1<1`, if `a_0<=Re(q)<=a_1`,

\[
|F_m(s)-\xi(s)|
\le \frac{c^{a_0}}2 |(q)_{\underline k}|
 \max_{j=0,1}\frac{J_m(a_j)}{\Gamma(k-a_j)}.
\tag{11}
\]

The corresponding bound for A_m-xi is the average of the two reflected bounds, since `xi(1-s)=xi(s)`.

**Proof.** From (6),

\[
0\le\Delta_m=L_m^2(1-e^{-2\delta_m})
\le\min(2d_mt^k,1)L_m^2.
\tag{12}
\]

Also `g_m(t)>=1/(1+t)`, so `L_m(t)<=1/(1+t)`. Thus J_m converges at both endpoints. Tonelli applied to (8) gives

\[
2d_m\Gamma(k-a)\mathbb E C_m^{a-k}
=\int_0^\infty t^{-a-1}\Delta_m(t)\,dt\le J_m(a).
\tag{13}
\]

For `0<Re(q)<1`, the fractional-moment Laplace formula and (8), with absolute convergence, give the exact identity

\[
F_m(s)-\xi(s)
=-d_m c^q(q)_{\underline k}\,\mathbb E C_m^{q-k}.
\tag{14}
\]

Here k is odd; the sign follows from `Gamma(k-q)/Gamma(-q)=(-1)^k(q)_{under k}`. Taking the absolute value of the *positive-law Mellin transform after this exact cancellation* proves (10). Merely taking absolute values inside a Laplace integral before the gamma cancellation would give a weaker, different bound.

Finally `a -> E C_m^{a-k}` is log-convex by Holder and is bounded by the maximum of its endpoint values. Since `c<1`, (11) follows. This justifies use of two real anchors for a complete complex rectangle, not only evaluations on two vertical lines. QED.

### A fully rational gamma-free version used by the checker

Take

\[
a_0=3/16,\quad a_1=5/16,\quad |\Im q|\le707/100,
\]

and put

\[
P_m=\prod_{j=0}^{k-1}
 \sqrt{\max(|j-a_0|,|j-a_1|)^2+(707/100)^2}.
\]

The integral on `(0,1)` shows `Gamma(1-a)>=e^{-1}>1/3`. Consequently, throughout this rectangle,

\[
\boxed{\epsilon_m=
 \frac32 P_m\max_{a\in\{3/16,5/16\}}
 \frac{J_m(a)}{\prod_{j=1}^{k-1}(j-a)}}
\tag{15}
\]

is a valid upper bound for `|F_m-xi|`. Because reflection takes `Re(q)` to `1/2-Re(q)` and changes the sign of the imaginary part, the same epsilon bounds `|A_m-xi|` on this rectangle. Square roots, J_m, and products are evaluated outward, not rounded to nearest.

### Complete real-integral bound

In `u=log t` coordinates, (9) has integrand

\[
e^{-au}\min(2d_me^{ku},1)L_m(e^u)^2.
\]

On each cell `[u,u+h]`, monotonicity of the three factors gives the rigorous upper sum

\[
h e^{-au}\min(2d_me^{k(u+h)},1)L_m(e^u)^2.
\tag{16}
\]

The complete omitted intervals are bounded by

\[
\frac{2d_m e^{(k-a)U_-}}{k-a},\qquad
\frac{e^{-(a+2)U_+}}{a+2}.
\tag{17}
\]

The checker uses `h=1/32`, `U_-=-10`, `U_+=30`, exactly 1280 cells, and both tails. It proves `epsilon_10 < 1.379e-9`. Neither omitted Thorin atoms nor large positive t are discarded.

## 4. GZC2: an explicit complex evaluator without a zeta oracle

Set `B=2 sum_i w_i/x_i`, the total shape of Z_m. This section uses B as a scalar, not the positive defect variable B_m. All m are finite.

For `0<Re(q)<1`, integrating the fractional-moment formula by parts gives

\[
\begin{split}
I_m(q)&=\int_{\mathbb R}
    2e^{(1-q)u}L_m(e^u)^2g_m(e^u)\,du,\\
F_m(s)&=\frac12\frac{c^q}{\Gamma(1-q)}I_m(q).
\end{split}
\tag{18}
\]

Both endpoints in the integration by parts vanish. Differentiation in q is justified on compact substrips by exponential tails and inserts a factor `-u` in I_m. Therefore

\[
F_m'(s)=\frac14\frac{c^q}{\Gamma(1-q)}
\{I_m'(q)+(\log c+\psi(1-q))I_m(q)\}.
\tag{19}
\]

### Uniform infinite-trapezoidal remainder

Use the finite sum over `u=jh`, with `h=1/16`, `-100<=u<=40`, including both endpoints (2241 nodes). Let q range over a closed disk of radius `R=1/16` about the evaluation q. Put

\[
a_-=\Re q-R,\quad a_+=\Re q+R,\quad \tau_+=|\Im q|+R.
\]

The checker verifies `0<a_-<=a_+<1`. It reconstructs B and verifies `B<B_ub`, where `B_ub=28` for m=3 and `231` for m=10. No general formula for B is needed by the proof.

For `|v|<=1`,

\[
|1+r e^{iv}|\ge\cos(v/2)(1+r),\qquad r\ge0.
\]

Thus the integrand f_q in (18) is analytic for `|Im(u)|<pi`, decays uniformly in `|Im(u)|<=1`, and satisfies

\[
\int_{\mathbb R}|f_q(u+iv)|du
\le e^{\tau_+}\left(\frac87\right)^{B_{ub}+1}
 \Gamma(1-\Re q)\mathbb E Z_m^{\Re q}
\le\frac{2e^{\tau_+}}{1-a_+}
       \left(\frac87\right)^{B_{ub}+1}.
\tag{20}
\]

We used `cos(1/2)>7/8`, Jensen `E Z_m^a<=2^a<=2`, and log-convexity of gamma between 1 and 2, which gives `Gamma(1-a)<=1/(1-a)`.

The classical analytic-strip trapezoidal theorem consequently bounds the infinite-sum error by

\[
E_{alias}=\frac{4e^{\tau_+}}{1-a_+}
 \left(\frac87\right)^{B_{ub}+1}
 \frac1{e^{2\pi/h}-1}.
\tag{21}
\]

This theorem can be seen by shifting the Fourier integrals to heights `+/-1` and summing the nonzero Poisson aliases. Uniform exponential decay ensures the side integrals vanish and justifies the summation. Trefethen–Weideman, Theorem 5.1 and the contour formula (5.15), is the credited classical reference.

On the real line, `g_m<=1`, `L_m<=1` on the left. On the right, `g_m<=B/(2e^u)` and `L_m<=e^{-u}`. Hence the omitted *discrete* tails are at most

\[
E_- =\frac{2h e^{(1-a_+)(-100-h)}}{1-e^{-(1-a_+)h}},\qquad
E_+ =\frac{B_{ub}h e^{-(a_-+2)(40+h)}}{1-e^{-(a_-+2)h}}.
\tag{22}
\]

Let `E=E_alias+E_-+E_+`. This bounds the analytic difference between I_m and its finite sum throughout the full q-disk. Cauchy's estimate bounds the derivative of that difference at the centre by `E/R=16E`. The checker therefore uses separate, complete enclosures for I_m and I_m', not numerical differencing or a bare finite integration range.

### Directed elementary and gamma evaluation

`intervals.py` uses integer endpoints in units `2^-288`. Arithmetic operations, divisions and square roots round outward. The logarithm uses an atanh series after scaling to `[1,2]`. The exponential uses a Taylor series after reduction to `|x|<=1/8`, its full absolute remainder, and squaring. Complex exponentials reduce the imaginary part by an integer multiple of an *enclosed* `2pi`; no rounded phase is substituted. Machin's arctangent formula encloses pi.

For (18)–(19), `z=1-q` is shifted to `w=z+80`. The first 11 Bernoulli correction terms are used for log Gamma and psi. With `N=12`, the remainder bounds implemented are

\[
|R_{\log\Gamma}(w)|\le
\frac{2|B_{24}|}{24\cdot23(\Re w)^{23}},\qquad
|R_\psi(w)|\le\frac{2|B_{24}|}{24(\Re w)^{24}}.
\tag{23}
\]

The checker enforces `|Im(w)|<=Re(w)/4`. Then `|arg(w)|<1/4`, `cos(arg(w)/2)>127/128`, and `(128/127)^25<2`. The sector bounds of DLMF 5.11(ii), with `|w|>=Re(w)`, therefore imply (23). Recurrence shifts the result back; all logarithms have positive real part and use the principal branch. The factor 2 is deliberately retained. No asymptotic expansion is treated as an exact finite identity.

All rational node brackets are suggestions only: (3) reconstructs the exact monic polynomial; the checker proves m disjoint sign changes in `(0,1)`, bisects, reconstructs Gaussian weights from Lagrange integration, and checks moment containment through degree `2m-1`. Degree m plus m disjoint sign changes proves complete root coverage. Positivity, normalization and the shape upper bound are checked. No floating root finder participates in acceptance.

## 5. GZC3: continuum disk counts and exact critical-line confinement

### A uniform curvature bound

For `Re(s)/2` in `[3/16,5/16]`,

\[
F_m''(s)=\frac18\mathbb E (cZ_m)^{s/2}\log^2(cZ_m).
\]

For `0<y<=1`, `y^a log^2 y<=4/a^2`; for `y>=1`, `y^a log^2 y<=4y/(1-a)^2`. Since `E(cZ_m)=2c<2`,

\[
|F_m''(s)|\le\frac12\left\{(16/3)^2+2(16/11)^2\right\}<17.
\tag{24}
\]

The same bound holds for A_m where both reflected arguments are in this strip. It holds at all imaginary heights. The numerical certificate checks the whole disk lies in the stated strip.

### Disk theorem

Let h be holomorphic on a neighborhood of the closed disk `D(z_0,r)`, with `|h''|<=17` there. Suppose directed evaluations give

\[
|h(z_0)|\le v,\qquad |h'(z_0)|\ge\lambda>0.
\]

Let G be holomorphic there and satisfy `|G-h|<=epsilon` on the boundary. If

\[
\boxed{r\lambda-v-\frac{17r^2}{2}-\epsilon>0,}
\tag{25}
\]

then both h and G have exactly one zero, counted with multiplicity, in the open disk; neither has a boundary zero. In particular each zero is simple.

**Proof.** Taylor's integral remainder bounds `h(z)-h(z_0)-h'(z_0)(z-z_0)` by `17r^2/2`. On the boundary the displayed errors are strictly smaller than `|h'(z_0)(z-z_0)|`. Rouche applied to this linear function gives the counts for h and G separately. This is a whole-contour theorem, not a mesh-point sign test. QED.

For F_3 and A_3, use `G=h` and epsilon=0. For xi use `h=A_10`, `G=xi`, and the complete source envelope (15).

### Why the two reflected zeros are exactly on the line

Because all underlying measures are real,

\[
A_m(1-\bar s)=\overline{A_m(s)},\qquad
\xi(1-\bar s)=\overline{\xi(s)}.
\tag{26}
\]

A disk centred on `Re(s)=1/2` is invariant under `s -> 1-bar(s)`. Its unique zero must be fixed by that map, and therefore has real part exactly 1/2. This is an exact symmetry-plus-count argument. Small numerical real parts do not establish it.

At a centre on the line, `A_m(s)=Re F_m(s)` and `A_m'(s)=i Im F_m'(s)`. These identities explain the exact zeros in the real/imaginary components of the receipt; those components are not artificially rounded away.

## 6. Executed predicates

The exact dyadic enclosures and rational margins are in `results.json`. The following looser rational bounds are consequences, not additional accepting inputs:

| Predicate | v upper | lambda lower | curvature cost | source epsilon upper | strict margin lower |
|---|---:|---:|---:|---:|---:|
| F_3 disk | `6.312e-13` | `.00136188` | `8.5e-12` | 0 | `1.352e-9` |
| A_3 disk | `1.600e-15` | `.00136113` | `8.5e-12` | 0 | `1.352e-9` |
| xi via A_10 disk | `1.960e-10` | `.00138271` | `8.5e-10` | `1.379e-9` | `1.140e-8` |

The first disk is contained in `0<Re(s)<1/2`; this is a rigorous proposed counterexample to raw-seed critical-strip zero safety. It is not a zero of xi. The last disk contains a zero of xi only because the complete source error has been paid in (25). Source normalization and the gamma conventions are essential.

## 7. What reflection protects, and what remains open

There is a general local mechanism behind the result. Let a real-parameter family H_t be holomorphic in s and continuous in t, preserve (26), and initially have a single simple critical-line zero in a reflection-invariant disk. For any parameter range in which a strict boundary comparison preserves the count one, the zero remains simple and exactly on the line. This follows by repeating the disk theorem and symmetry argument. For an analytic parameter family the usual implicit-function theorem also gives the zero's local motion.

At a simple critical zero rho of a symmetric function H, an infinitesimal symmetric perturbation E has `E(rho)` real and `H'(rho)` purely imaginary. The first-order displacement `-E(rho)/H'(rho)` is therefore along the line. An unsymmetrized perturbation has no such restriction. This explains why the raw F_3 displacement is not a contradiction to the A_3 result. The actual finite certificates use full error bounds, not this first-order observation.

This is **local protection, not global preservation**. A family can acquire additional zeros through the boundary of a chosen region; multiple zeros can split while preserving reflection; and two simple critical-line zeros may collide. Ruling out those events at unbounded height is not supplied by positivity of C_m or by a small absolute approximation error.

A sufficient full-closing target remains: find unbounded orders and expanding windows in which the complete A_m have only critical-line zeros, with enough source convergence and boundary control to pass to xi. The parent supplies local-uniform convergence; this packet supplies explicit error envelopes and strict finite predicates. It does **not** establish the unbounded window premise or an all-order no-collision theorem. Such a premise may be stronger than RH for this particular approximating family; no converse is asserted. No simplicity conjecture for all xi zeros is assumed or proved.

The useful change from the previous packet is precise: complete positivity now pays a complex contour error and actual zero counts, while a tempting raw-seed shortcut is refuted by an isolated zero rather than a phase diagnostic. The all-height step is still a mathematical research problem, not a routine verification task assigned to reviewers.

## 8. Attribution and review boundary

Classical mechanisms: BPY's source identity; Gaussian quadrature/Stieltjes remainders; gamma infinite divisibility; Mellin and Laplace transforms; analytic-strip trapezoidal quadrature; Euler–Maclaurin gamma bounds; Cauchy estimates; Rouche; reflection and the implicit-function theorem. No general priority claim is made for these tools or rigorous zeta zero isolation.

Primary references inspected for this continuation:

* Biane, Pitman, Yor, *Probability laws related to the Jacobi theta and Riemann zeta function, and Brownian excursions*, arXiv:math/9912170. Source normalization inherited from the frozen parent; the external proof was not independently re-audited in full this pass.
* Trefethen and Weideman, *The Exponentially Convergent Trapezoidal Rule*, SIAM Review 56 (2014), Theorem 5.1 and (5.15). The relevant theorem and error-formula pages were read in text and rendered page images.
* NIST DLMF, Section 5.11(ii), remainder bounds for log Gamma and psi. This is an explicit analytic import, not a package implementation.

Review (8)–(15), the factor and tails in (20)–(23), the q-versus-s derivative in (19), curvature (24), and the exact scopes of (25)–(26). A flaw in any of these adapters can invalidate a certificate despite correct finite arithmetic. The seven test methods and duplicated execution modes are not independent mathematical review or a formal proof assistant.
