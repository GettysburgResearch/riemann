# Spectral growth bounds and tight positive resolvent selection

Status: proposed component theorems with complete proofs; the source-specific spectral bound and positive-selector existence remain OPEN.
Scope: the actual full semilocal Weil form of PR #1017, with the theta source and normalization of PR #1021. No new zero-free boundary is claimed.
Exact dependencies: PR #1017 at `450dd8abecf58dfe60b3bc39bda0f792ea82ce95`; PR #1021 mathematical packet at `742e952be4ef7843de86ea12678c0bdd3d3579c3`. All prime powers and both pole terms are retained.
Smallest remaining gap: either the spectral growth estimate (3) at eta below the current source-qualified zero-strip width, or existence of a cofinal family of legal normalized resolvents satisfying the tightness/positivity hypothesis of Theorem 2.

The new deduction is that **identifying a limiting entire function with Xi is not necessary** for either consumer below. The full arithmetic source itself supplies the zero detector. This removes one task from the positive variance-selector route, but does not prove the positive selector exists.

## 1. Source conventions

Let `K_W` be the complete real, even Weil convolution distribution, and let

\[
q[f]=\langle f,K_W*f\rangle,
\qquad f\in C_c^\infty(\mathbb R).
\tag{1}
\]

On `[-a,a]`, its closed, lower-bounded realization is `A_a`, with lowest eigenvalue `lambda_0(a)`. The Fourier convention is `G(z)=integral g(x)exp(-izx)dx`. If `rho=beta+i gamma` is a nontrivial zeta zero, write

\[
z_\rho=(\rho-1/2)/i=\gamma+i(1/2-\beta),
\qquad i z_\rho=\beta-1/2+i\gamma.
\tag{2}
\]

The classical explicit formula, tested against a compact smooth function, is the zero-side representation of `K_W`. No RH premise is involved. Each zero is counted with its actual multiplicity. The unconditional strip `0<beta<1` and count `N(T)=O(T log(2+T))` are enough for every convergent series below.

## 2. A quantitative negative-spectrum bound excludes zeros

**Theorem 1 (spectral growth consumer).** Fix `eta>=0`. Suppose that for every `epsilon>0` there is a constant `C_epsilon` such that, for all sufficiently large `a`,

\[
\boxed{
\lambda_0(a)\ge -C_\epsilon\exp((2\eta+\epsilon)a).}
\tag{3}
\]

Then zeta has no zero with `Re rho>1/2+eta`. By the functional equation it has none with `Re rho<1/2-eta` either.

In particular, **subexponential growth of the negative spectral bottom is sufficient for RH**. A uniform finite lower bound is a special case. The concrete target

\[
\lambda_0(a)\ge-C_\epsilon e^{(1/2+\epsilon)a}
\tag{4}
\]

would give the half-plane `Re s>3/4`.

### Proof: two translates, followed by an exact Laplace pole

Fix `g in C_c^infinity([-R,R])`, and let `h=g*tilde g`, where `tilde g(x)=conjugate(g(-x))`. Define

\[
C_g(t)=(K_W*h)(t).
\tag{5}
\]

The function is smooth. Its value is a polarized pairing between two translates of `g`. For `t>2R`, center those two translates at `-t/2` and `t/2`. They have disjoint supports in `[-a,a]` with `a=t/2+R`. Their diagonal form values are both `q[g]`, by translation invariance. The lower bound (3), applied to their two-dimensional span, therefore gives

\[
|C_g(t)|
\le q[g]+C_\epsilon e^{(2\eta+\epsilon)(t/2+R)}\|g\|_2^2.
\tag{6}
\]

For clarity, the corresponding Hermitian matrix has diagonal `q[g]` and off-diagonal `C_g(t)` or its conjugate. Its smallest eigenvalue is `q[g]-|C_g(t)|`; the two vectors have the same norm and are orthogonal because their supports are disjoint. This proves (6) with no generic matrix positivity assumption about the complete operator.

The bounded range of `t` is absorbed into the constant. Consequently, for every `epsilon>0`,

\[
|C_g(t)|\ll_{g,\epsilon}
e^{(\eta+\epsilon/2)t}\qquad(t\ge0).
\tag{7}
\]

The explicit formula gives an independent expression

\[
C_g(t)=\sum_\rho
G(z_\rho)\overline{G(\overline{z_\rho})}\,e^{i z_\rho t}.
\tag{8}
\]

Since `g` is compact and smooth, `G(z)` decreases faster than any inverse power of `|Re z|`, uniformly in the closed strip `|Im z|<=1/2`. The coefficient series in (8) is therefore absolutely summable and converges locally uniformly in `t`. Multiplicities cause no difficulty because of the stated zero count.

For `Re w>1/2`, termwise Laplace transformation is justified and gives

\[
\mathcal L_g(w)
=\int_0^\infty C_g(t)e^{-wt}\,dt
=\sum_\rho
\frac{G(z_\rho)\overline{G(\overline{z_\rho})}}
 {w-(\beta-1/2+i\gamma)}.
\tag{9}
\]

The series on the right is meromorphic on the entire `w` plane. It converges normally on every compact set avoiding its discrete poles, since its numerators decrease rapidly and its large-height denominators grow linearly. A zero of multiplicity `m` produces the residue

\[
m\,G(z_\rho)\overline{G(\overline{z_\rho})}.
\tag{10}
\]

Now suppose `beta-1/2>eta`. Choose `epsilon>0` with `eta+epsilon/2<beta-1/2`. Equation (7) makes the left side of (9) holomorphic on `Re w>eta+epsilon/2`. Choose `g` so that the residue (10) is nonzero. Such a compact smooth `g` always exists: a nonnegative even smooth bump of integral one, supported in a sufficiently small neighborhood of zero, has `G(z_rho)` and `G(conjugate z_rho)` arbitrarily close to one. The choice may depend on this single hypothetical zero; no simultaneous nonvanishing or numerical zero list is needed.

Identity continuation from `Re w>1/2` makes the meromorphic right side agree with the holomorphic Laplace transform throughout that connected half-plane away from its poles. The nonzero residue at `w=beta-1/2+i gamma` is then impossible. Distinct zeros have distinct pole locations; repeated zeros multiply the nonzero residue rather than cancel it. This contradiction proves the theorem. QED.

### Scope and usable variants

1. A legal shift `kappa_a<lambda_0(a)` with `-kappa_a<=C_epsilon exp((2eta+epsilon)a)` supplies (3) directly. No convergence of the corresponding resolvent columns is required for this consumer.
2. A bound on all sufficiently large intervals is enough. A cofinal sequence also suffices with the same exponent if successive interval half-widths have ratio tending to one, by domain monotonicity. For the uniform-bounded-below special case, an arbitrary cofinal sequence suffices.
3. The known elementary lower bound in PR #1017 is of size `-O(a e^a)`. It gives only `eta=1/2`, consistent with the ordinary trivial zero strip. Improving that exponent is an actual arithmetic task.
4. No converse asserting that a known zero strip automatically proves (3) is used or claimed. The implication proved here goes from a bound on the full operator to a zero strip.

## 3. Tight positive legal resolvents already suffice for RH

Let `a_j` tend to infinity, choose a legal real shift `kappa_j<lambda_0(a_j)`, and put

\[
u_j=(A_{a_j}-\kappa_j)^{-1}1,
\qquad f_j=\frac{u_j}{\int u_j},
\qquad c_j=\frac1{\int u_j}>0.
\tag{11}
\]

The normalized vector has mass one and satisfies, in the actual operator/form sense,

\[
(A_{a_j}-\kappa_j)f_j=c_j1.
\tag{12}
\]

It uniquely minimizes `q[f]-kappa_j||f||_2^2` among mass-one vectors, with minimum `c_j`.

**Theorem 2 (positive tightness removes Xi identification).** Suppose

- `f_j(x)>=0` almost everywhere;
- the probability measures `f_j(x)dx` are uniformly tight.

Then `kappa_j` tends to zero, the full Weil form is nonnegative, and RH holds. In particular it is enough that the physical resolvents be nonnegative and have uniformly bounded second moments.

The conclusion does not require convergence to the theta density, matching all Xi Taylor coefficients, a simple-even bottom eigenspace, or a numerical zero table.

### Proof

Let `phi` be the fixed positive theta probability density from PR #1021, so `K_W*phi=0`. Let `v_a` be its smooth cutoff to `[-a,a]`, normalized to have mass one. The complete source estimates from that packet, with no broad convolution, give

\[
\|A_a v_a\|_{L^\infty([-a,a])}\le\epsilon_a^{\rm tight},
\qquad \epsilon_a^{\rm tight}\longrightarrow0,
\tag{13}
\]

in fact super-exponentially. The proof is the same explicit tail calculation: the cutoff error and its first derivative are bounded by a constant times
`exp(Ca-c exp(2a)) exp(-2|x|)`, and every pole, archimedean, and prime-power term is then bounded as in PR #1021. Slightly reducing the positive constant `c` absorbs the fixed-width cutoff transition.

Uniform tightness supplies a fixed `R` with `integral_[-R,R] f_j>=1/2` for every sufficiently large `j`. On that fixed interval `v_a` converges uniformly to the strictly positive `phi`. Thus

\[
\langle f_j,v_{a_j}\rangle\ge m>0
\tag{14}
\]

with one fixed `m`. Pair (12) with `v_a` and use its unit mass. Since `f_j` is nonnegative of mass one, (13) gives

\[
c_j=-\kappa_j\langle f_j,v_{a_j}\rangle+r_j,
\qquad |r_j|\le\epsilon_{a_j}^{\rm tight}.
\tag{15}
\]

Independently, the broad mass-one theta competitors `w_a` constructed in PR #1021 satisfy

\[
\|w_a\|_2^2\le C/a,
\qquad |q_a[w_a]|\le\epsilon_a^{\rm broad},
\qquad \epsilon_a^{\rm broad}\longrightarrow0.
\tag{16}
\]

The available source rate is `epsilon_broad<=C exp(Ca-c exp(a))`;
in particular `a epsilon_broad->0`, as used in the nonnegative-shift
branch below.

If `kappa_j<0`, their variational comparison with (11) gives

\[
c_j\le\epsilon_{a_j}^{\rm broad}+C|\kappa_j|/a_j.
\tag{17}
\]

Combining (14)--(17) yields

\[
|\kappa_j|(m-C/a_j)
\le\epsilon_{a_j}^{\rm tight}+\epsilon_{a_j}^{\rm broad}.
\tag{18}
\]

Hence the negative shifts tend to zero. For a nonnegative legal shift, the same broad competitor and Cauchy--Schwarz give

\[
0\le\kappa_j<\lambda_0(a_j)
\le\frac{q[w_{a_j}]}{\|w_{a_j}\|_2^2}
\le 2a_j\epsilon_{a_j}^{\rm broad}\longrightarrow0,
\tag{19}
\]

where `||w_a||_2^2>=1/(2a)` follows from its mass and support. Thus all shifts tend to zero.

For any fixed compact smooth `g`, its support is contained in `[-a_j,a_j]` for large `j`, and legality gives `q[g]>=kappa_j||g||_2^2`. Letting `j` tend to infinity proves `q[g]>=0`. Theorem 1 with `eta=0`, or the classical Weil criterion, now proves RH. QED.

**Corollary 2.1.** If the variance equation proposed in PR #1021,

\[
\int x^2 f_j(x)\,dx=V_X,
\tag{20}
\]

has a cofinal family of legal solutions whose physical densities are nonnegative, then RH follows. The remaining problem is positive-selector existence. An additional identification theorem for the entire limit is unnecessary under these hypotheses.

For nonnegative mass-one vectors, (20) gives tightness directly by Chebyshev's inequality. This proof does not need to infer physical positivity from real Fourier zeros; that inference is false in general.

## 4. A signed relaxation retaining the actual theta overlap

Physical positivity can be replaced by two quantitative conditions. In the notation above, assume

\[
\liminf_j\langle f_j,v_{a_j}\rangle>0,
\qquad
\epsilon_{a_j}^{\rm tight}\|f_j\|_1\longrightarrow0.
\tag{21}
\]

Then (15) holds with error bounded by `epsilon_tight ||f_j||_1`. The same variational estimate (17) proves `kappa_j ->0`; the preceding argument again proves RH. Thus a positive theta overlap and sufficiently controlled total variation are another exact selector target.

The total-variation condition is very weak relative to the super-exponential theta cutoff residual, but it is not automatic. Normality of the Fourier transforms alone does not bound the total variation of signed physical densities. Likewise the overlap in (21) must not be inferred from normalization or a finite collection of matching moments.

There is also a useful alternative sufficient condition:

\[
\sup_j\int e^{\alpha|x|}|f_j(x)|\,dx<\infty
\quad\text{for some }\alpha>1/2.
\tag{22}
\]

It implies RH directly, without assuming the theta overlap. Here is a proof. Pass to a weakly convergent subsequence of the finite signed measures; the exponential variation bound preserves their total mass one. Call the limit `mu`. There exists a compact smooth `h` with `integral h dx=0` and `integral h dmu !=0`: otherwise `mu` would be a constant multiple of Lebesgue measure, incompatible with finite total variation and mass one.

The explicit arithmetic formula gives

\[
|(K_W*h)(x)|\ll_h(1+|x|)e^{|x|/2}.
\tag{23}
\]

The pole term has this growth; the distant archimedean term decays; and the prime sum uses only `Lambda(n)<=log n` and primes/powers with `log n` within a fixed distance of `|x|`. Thus (22) bounds `integral f_j(K_W*h)` uniformly. Pairing (12) with `h` gives

\[
\kappa_j\int f_jh=\int f_j(K_W*h).
\tag{24}
\]

The denominator tends to the nonzero `integral h dmu`, so the legal shifts are bounded along this cofinal subsequence. Hence the full form has a uniform finite lower bound, and Theorem 1 gives RH.

If one additionally uses the real-zero property of the legal resolvents and bounds their second coefficient by `V`, the paired canonical product gives `F_j(i alpha)<=exp(V alpha^2/2)`. Consequently a uniform bound on the **exponentially weighted negative part** alone suffices for (22), because

\[
\int e^{\alpha|x|}|f_j(x)|\,dx
\le2F_j(i\alpha)+4\int e^{\alpha|x|}f_j^-(x)\,dx.
\tag{25}
\]

Evenness is used here, and all `f_j` are real and even at the zero-frequency forcing. Equation (25) is an explicit possible replacement for proving exact nonnegativity.

## 5. What is still missing

No bound (3) with a useful new exponent has been established here. No cofinal family satisfying Theorem 2 or (21)--(22) has been constructed. The recent theta competitors supply upper Rayleigh bounds and small residuals; they do not supply a lower bound on the complete negative spectrum.

The positive-selector route now has fewer unresolved tasks: prove the legal variance selector exists and control its physical sign or negative variation. Once those are available, a separate theorem matching its entire limit to Xi is not needed. The quantitative alternative is equally explicit: prove (4) for the full source to obtain `Re s>3/4` directly.

The source-specific results above are analytic. No finite eigenvalue, grid positivity test, or fitted sequence of moments certifies their open hypotheses.
