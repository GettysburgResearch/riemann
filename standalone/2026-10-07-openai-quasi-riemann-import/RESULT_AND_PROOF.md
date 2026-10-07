# What the new work claims and how its argument works

Status: a source-grounded explanation of imported theorems, with selective mathematical review.
Source pin: **adc7f1241b42e322a6451854ab7e4b4c146bf78a** in [openai/math](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a).
Our verification scope is stated in [MATHEMATICAL_AUDIT.md](MATHEMATICAL_AUDIT.md) and [FORMALIZATION_AUDIT.md](FORMALIZATION_AUDIT.md).

## 1. Three distinct results

| Manuscript | Stated conclusion | Method |
| --- | --- | --- |
| [30 September: $7/8$](upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) | Every finite-order Hecke $L$-function over the Eisenstein field, and every Dirichlet $L$-function, is zero-free for $\Re s>7/8$; principal poles allowed | Two-stage common-probe continuation, cubic theta reflection, selected-prime compensation, and separate inverse/plain moment inductions |
| [5 October: $11/12$](upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf) | The same families are zero-free for $\Re s>11/12$ | Sextic-twisted ideal Möbius mean square, cubic theta, cube inversion, two-Poisson descent, and sixth-power extraction |
| [1 October: real-zero gap](upstream/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf) | There exists one $c>0$ such that every real zero $\beta\in(0,1)$ of every primitive nonprincipal real Dirichlet character of conductor $q\ge3$ obeys $(1-\beta)\log q\ge c$ | Prime bias from an exceptional zero, anisotropic interpolation, Frobenius divisibility, and a determinant-size contradiction |

The later date on the simpler $11/12$ paper does not withdraw the $7/8$ claim. The supplied formalization targets $7/8$ and the separate real-zero-gap theorem. OpenAI's README says the $11/12$ writeup was human edited for readability and that the zero-free-region project was an exception to its usual fixed evaluation procedure.

A fixed half-plane differs qualitatively from classical zero-free regions whose widths shrink as height or conductor increases. For zeta, the claimed theorem and the functional equation confine the nontrivial zeros to
\[
1/8\le\Re\rho\le7/8.
\]
The endpoints are included in this possible-zero strip. The desired RH statement is still $\Re\rho=1/2$ for every nontrivial zero.

The theorem makes no density or percentage assertion. In particular, the fractions $7/8$ and $11/12$ are horizontal coordinates, not proportions of zeros. The effect is uniform in height and in the family index; numerical zero checks cannot establish that quantifier.

## 2. Why the Eisenstein field appears

Both zero-free papers work over
\[
K=\mathbb Q(\sqrt{-3}),\qquad \mathcal O_K=\mathbb Z[\omega],
\qquad \omega=e^{2\pi i/3}.
\]
This supplies sextic residue characters and cubic Gauss sums in a setting where the appropriate cubic theta function has useful transformation laws.

Here $\mu_K$ is the ideal Möbius function. It vanishes on ideals divisible by a square, and is $(-1)^r$ on products of $r$ distinct prime ideals. Norm $N\mathfrak n$ takes the place of the size of an integer. These are not the real-integer coefficients in our native Newton programme; transferring estimates between the two sources needs an explicit argument.

Primary generators, the primes above 2 and 3, ramified primes, and zero-on-nonunit character conventions are part of the arithmetic. The proofs repeatedly need those zeros as support conditions.

## 3. The readable $11/12$ argument

This section follows the October 5 manuscript's outline and the referenced detailed lemmas. The displayed simpler formulas suppress only the auxiliary characters and common-factor labels explicitly suppressed by that outline. The paper's exact family is larger.

### 3.1 Reduce nonvanishing to actual Möbius cancellation

Fix a finite-order Hecke character $\nu$ and a smooth compactly supported profile $W$. Consider
\[
A_1(D)=\sum_{\mathfrak n}\mu_K(\mathfrak n)\nu(\mathfrak n)
 W(N\mathfrak n/D),
\]
with the prescribed finite prime exclusions.

For every $\epsilon>0$, an estimate
\[
A_1(D)\ll_{\nu,W,\epsilon}D^{11/12+\epsilon}
\]
would make its Mellin transform holomorphic to the right of $11/12$. In the region of absolute convergence, that transform is
\[
\int_0^\infty A_1(D)D^{-s}\frac{dD}{D}
=\frac{\widehat W(s)}{L_K^S(s,\nu)}.
\]
If $\rho$ were a zero in the alleged zero-free region, choose a complex smooth profile with $\widehat W(\rho)\ne0$. One concrete choice is $W(y)=y^{-\rho}\phi(y)$ with nonzero $\phi\ge0$ supported in $(1,2)$. The entire numerator then cannot cancel the reciprocal pole at $\rho$. This gives the contradiction.

This analytic step is close to our noncancelling Mellin detectors. The new work is in establishing the arithmetic estimate.

### 3.2 Embed the target in a sextic-character family

Introduce
\[
A_u(D)=\sum_{\mathfrak n}\mu_K(\mathfrak n)\nu(\mathfrak n)
\chi_{\mathfrak n}(u)W(N\mathfrak n/D),
\]
where $\chi_n(u)=(u/n)_6$. The central proposition states, for each fixed small $\vartheta>0$,
\[
\sum_{0<N(u)\le H}|A_u(D)|^2
 \ll_{\nu,W,\vartheta,\epsilon}D^{1+\epsilon}H,
\qquad H=D^{1+\vartheta}.
\]
The smooth-profile version controls a specified finite number of derivatives of $W$, so the estimate can survive the transforms used later.

The trivial individual bound from this mean square does not give the required power saving. Here the authors supply an arithmetic extraction mechanism. For a prime $p$,
\[
\chi_n(p^6)=\mathbf1_{p\nmid n},
\qquad A_{p^6}(D)=A_1(D)+O_W(D/Np).
\]
There are on the order of $Y/\log Y$ available prime ideals with $Np\asymp Y$. Taking $Y=H^{1/6}$ gives
\[
|A_1(D)|^2
 \ll D^{1+\epsilon}H^{5/6}+D^2H^{-1/3}.
\]
The first square-root exponent at $H=D^{1+\vartheta}$ is
\[
\frac12+\frac5{12}(1+\vartheta)
 =\frac{11}{12}+\frac5{12}\vartheta.
\]
The omitted-prime error has exponent $5/6-\vartheta/6$ and is smaller. Taking $\vartheta$ sufficiently small for the requested loss gives $11/12+\epsilon$.

This calculation explains the exponent. Merely repeating this extraction does not supply an iteration from $11/12$ to $1/2$.

### 3.3 Poisson summation changes the coefficients into automorphic data

After expanding the square and applying Poisson summation in the row variable, normalized sextic Gauss sums appear. A Gauss–Jacobi identity combines the Möbius factor with a Gauss sum:
\[
\mu_K(n)\gamma_{-1}(n)
 =\chi_n(-1)G(n)^{-1}\overline{\alpha(n)}\gamma_2(n),
\qquad \alpha(n)=n/|n|.
\]
Here $\gamma_j$ denotes the appropriate normalized Gauss sum and $G$ is a fixed ray-class factor. The remaining $\gamma_2(n)$ is a cubic Gauss coefficient.

Patterson's coefficient formula identifies these values with Fourier coefficients of Kubota's cubic theta function. Thus the transformed Möbius sum has an automorphic transformation law available to it.

### 3.4 Completion and reflection produce a quadratic family

The cubic theta expansion contains full indices $nb^3$. To use its transformation law, the proof completes the original squarefree-index sum by adding the cube factors. In the outline's normalization,
\[
P_h(X)=X^{-1/2}B_h(X),\qquad
T_h(X)=\sum_b\frac{w_h(b)}{N(b)}
 P_h\!\left(\frac{X}{N(b)^3}\right),
\]
where $w_h$ is completely multiplicative and $|w_h|\le1$.

Theta reflection transforms the column sum while keeping the row parameter. A local character calculation turns the relevant sextic twist into a quadratic one:
\[
\chi_p^{-1}\chi_p^{-2}=\chi_p^{-3}=\chi_p^3.
\]
The quadratic large sieve then supplies the stronger two-scale factor needed for
\[
\sum_{0<N(h)\ll\mathcal H}|T_h(X)|^2
 \ll_\epsilon(\mathcal H X)^\epsilon
 \left(\mathcal H+\frac{\mathcal H^2}{X}\right).
\]
The common profile, fixed ray classes, cusp coefficients, and all local exclusions must remain uniform over the moving rows for that step to apply.

The angular factor also has an analytic purpose: Appendix A.2 realizes it using a horizontal derivative of the theta series. This derivative kills the constant Fourier modes at both the original and reflected cusps. The resulting Mellin transform is entire, so the simplified reflection does not discard an unaccounted constant-mode residue.

### 3.5 The critical closure is removal of the cube completion

A bound on $T_h$ is not yet a bound on $P_h$, because the extra cube contributions may cancel the term we want. The proof uses exact Möbius inversion:
\[
P_h(X)=\sum_d\frac{\mu_K(d)w_h(d)}{N(d)}
 T_h\!\left(\frac{X}{N(d)^3}\right).
\]
The short divisors are handled by the reflected bound. The remaining long-divisor contribution is rewritten in the original class of sums, at smaller column scale.

Two further Poisson transforms, with a deliberate intermediate enlargement of a nonnegative row sum, return the coefficients to the same type. This produces a recursive child problem. In the simplified outline its scales are
\[
X'=\frac X{N(b)^3},\qquad
\mathcal H'=\frac{\mathcal H}{N(b)^3},
\qquad \frac{\mathcal H'}{X'}=\frac{\mathcal H}{X}.
\]
The cutoff is
\[
H_c=\min\left\{X^{1/3},(X/\mathcal H)^{2/3}\right\}.
\]
For the basic scales $X\asymp D$, $\mathcal H\asymp D^{1-\vartheta}$, each long-divisor child contracts the row size by a fixed power of $D$. The number of iterations is bounded in terms of the fixed $\vartheta$. Smooth-derivative costs and exponent losses are allocated over that finite depth.

The detailed second-transfer lemma has a particularly useful local mechanism. All representations of a transformed triple share one coupled kernel; at each prime in the new divisor,
\[
(1+\mathbf1_{p\mid k'})
-\mathbf1_{p\mid k'}-\mathbf1_{p\nmid k'}
=\mathbf1_{p\mid k'}.
\]
The signed sum therefore vanishes unless the full new divisor divides the transformed row. That support restriction is part of what makes the recursive bound close. The elementary identity is not enough by itself: common kernels, complete preimage enumeration, zero frequencies, and the rescaled family must all be proved.

### 3.6 Transfer back to the Riemann zeta function

For a Dirichlet character $\chi$, compose $\chi$ with the ideal norm to obtain a Hecke character. Quadratic base change gives, up to controlled nonzero finite Euler factors,
\[
L_K(s,\chi\circ N)
 =L(s,\chi)L(s,\chi\chi_{-3}).
\]
Away from the separately handled principal pole, nonvanishing of the product forces nonvanishing of each factor. This supplies every Dirichlet character and zeta.

## 4. How the stronger $7/8$ paper goes further

The September 30 paper is substantially longer. Its first $11/12$ stage is a balanced common-probe argument; it should not be identified with the later October 5 extraction proof merely because the endpoint is the same.

The common analytic principle considers
\[
\beta_*=\sup\!\left(\{1/2\}\cup
\{\Re\rho:\rho\text{ is a zero of a primitive finite-order Hecke }L\}\right).
\]
Poles are excluded from this set. If $\beta_*>\sigma_0$, the authors construct, for each target $\eta$, a sum $J_\eta(Z)$ and a Mellin signal
\[
f_\eta(Z)=\frac1{2\pi i}\int_{\Re s=2}
 Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_K^S(s,\eta)}\,ds,
\]
where $H_\eta$ is holomorphic and $|H_\eta-1|\le1/2$. Two estimates are required:
\[
|J_\eta(Z)|\ll_\eta Z^{C(\sigma_0)+\omega},
\qquad
|J_\eta(Z)-f_\eta(Z)|\ll_\eta Z^{C(\beta_*)-\sigma},
\]
with $0<\omega<\beta_*-\sigma_0$ and $\sigma>0$ chosen independently of the target character.

The two estimates imply a common positive saving for the signal. Its Mellin transform therefore continues every target reciprocal through the same distance left of $\beta_*$. The supremum definition then supplies a zero in that continued region, a contradiction. A supremum need not be attained; the proof uses a zero arbitrarily near it.

For the first stage,
\[
C_{\rm I}(s)=s-\frac23,\qquad C_{\rm I}(11/12)=\frac14.
\]
For the refined stage,
\[
C_{\rm II}(s)=s-\frac{11}{16},\qquad C_{\rm II}(7/8)=\frac3{16}.
\]
The change is not merely a new contour. The refined probe has selected-prime compensation and asymmetric scales. Compensation removes an unwanted local Euler contribution. Its principal residue is normalized by a factor that remains nonzero.

The zero detector produces two large polynomials for a retained row: a truncated inverse polynomial with ideal Möbius coefficients, and a plain character polynomial without them. They share the same row character and twist height. Separate moment arguments control those two polynomials, with short disjoint prime factors used as amplifiers. Their row-count estimates can then be combined at those common indices.

An important intermediate hypothesis is retained explicitly. The plain moment estimate with prime factors uses $\beta_*\le(1+\kappa)/2$ when $\kappa<1$. The final contradiction takes $\kappa=2\beta_*-1$, so this condition is satisfied by its definition. It is not an assumed RH or an unconditional improved moment valid at arbitrary smaller $\kappa$.

At the last optimization, the compensated endpoint lemma proves
\[
-E_*\ge\frac{49}{440640}>\frac1{10000}.
\]
Its proof is an exact polynomial completion of squares on a compact parameter range. With $\Delta=\beta_*-7/8$, the actual needed inequality retains the difference from the hypothetical rightmost-zero scale:
\[
E_{\rm actual}(13/16)-\Delta
 \le-\frac{49}{440640}-\frac{51}{64}\Delta
 +\epsilon_{\rm total}.
\]
The error allowances are chosen within this margin. This finite algebraic checkpoint was reproduced exactly in this import. That does not verify the analytic estimates feeding the parameters or the full moment inductions.

## 5. The independent Landau–Siegel route

The companion does not need the $7/8$ argument as a black box. It assumes for contradiction that a sequence of exceptional real zeros approaches one so rapidly that $(1-\beta)\log q$ tends to zero. An explicit-formula argument makes primes with character value $-1$ carry a large weighted mass.

The algebraic stage works in a biquadratic field and forms an interpolation determinant from related algebraic quantities. A coefficient-uniform interpolation theorem supplies a nonzero determinant, while weighted row selection makes its degrees strongly anisotropic. Frobenius congruences at the negatively biased primes force many powers of those primes to divide the determinant.

The proof compares a divisibility lower bound with an upper bound on the size of its algebraic norm. The anisotropic degree arrangement creates the strict exponent gap; the two bounds cannot both hold. This is why the companion's Lean implementation includes substantial interpolation and intersection theory.

The separate theorem is interesting for our determinant and Sylvester research, but the current packet does not construct a determinant that bounds our native covariance. Its conclusion concerns the uniform exceptional real-zero gap. It does not prove RH.

## 6. What the verification evidence does and does not say

The supplied zeta and Dirichlet implementation concludes nonvanishing for the standard functions, with no unproved analytic predicate in the exported theorem signatures. The full internal implementation closure contains no scanned proof-hole/escape tokens. The challenge files intentionally leave proofs blank and designate separate solution modules.

This is considerably stronger source evidence than an abstract or an unsupported proof outline. It still needs a fresh kernel/Comparator run, external-dependency verification, and a source-fidelity review of the constructed Hecke objects. The selective manuscript audit did not certify every line of either zero-free proof. Those are the present boundaries of our assessment, stated independently of the significance the theorem would have once verified.
