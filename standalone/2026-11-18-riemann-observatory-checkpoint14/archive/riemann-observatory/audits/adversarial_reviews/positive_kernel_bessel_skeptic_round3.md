# Independent skeptic reconstruction: Bessel kernel with four off-line zeros

Date: 2026-11-17. Reviewer `/root/li_skeptic`; the advocate's draft was not read. Status: independently reconstructed, with no issue found in the statement below. This is a generic analytic-class obstruction, **not** an RH result; novelty is unassessed. It repairs the divisor-product model's large off-line count and coarse zero-count remainder.

## Precise model

Fix `c=2pi`, `a=1/4`, `T>=32`, and define

\[
 f(u)=e^{-c\cosh(2u)},\quad G(w)=K_{w/2}(c)
       =\int_{\mathbb R} f(u)e^{wu}\,du,
\]
\[
 Q_T(w)=((w-a)^2+T^2)((w+a)^2+T^2)
       =w^4+2(T^2-a^2)w^2+(T^2+a^2)^2,
\]
\[
 F_T(s)=\frac{G(s-1/2)Q_T(s-1/2)}{G(1/2)Q_T(1/2)}.
\]

The denominator is strictly positive. This function is real entire, symmetric under `s -> 1-s`, normalized by `F_T(0)=F_T(1)=1`, and has order one and infinite exponential type. Its centered Laplace kernel is even, `C^infinity`, and everywhere strictly positive. It has exactly four off-line zeros, at `s=1/2 +/- a +/- iT`; its other zeros are simple and on the line. Counting positive ordinates with multiplicity,

\[
 N_{F_T}(X)=\frac{X}{2\pi}\log\frac{X}{2\pi}
              -\frac{X}{2\pi}+O(1),\qquad X\to\infty.
\]

For every fixed finite `N`, one can take `T` sufficiently large that `lambda_1(F_T),...,lambda_N(F_T)` are all strictly positive. The parameter `T` depends on `N`; the claim is not positivity of all Li coefficients for one countermodel.

## Entire integral and growth

The integral identity follows from the standard integral for `K_nu(c)`, substituting `t=2u`; see Paris [S01], equation (1.1), with imaginary order first, followed by entire continuation (or the same absolutely convergent cosh integral for arbitrary order). Every compact set in `w` admits a common integrable majorant, since `f` has double exponential tails. Thus it is an even real entire bilateral Laplace transform.

For `r>0`, `|G(w)|<=G(r)` on `|w|<=r`, and

\[
 G(r)\le 2\int_0^\infty e^{-(c/2)e^{2u}+ru}\,du
       \le(c/2)^{-r/2}\Gamma(r/2).
\]

Stirling gives `log M_G(r)<= (r/2)logr+O(r)`, hence order at most one. The zero count proved below forces order at least one and rules out finite exponential type: Jensen's inequality would give `n(r)=O(r)` for finite exponential type, whereas here `n(r)` is of order `rlogr`. Polynomial multiplication and translation preserve these conclusions.

## All complex order zeros are imaginary, and simple

This is independently proved rather than inferred from a source's assertion that there are infinitely many real `nu` zeros. The following standard operator facts are explicit dependencies: closed positive quadratic forms define Friedrichs operators; Rellich compactness on finite intervals; and the elementary second-order ODE uniqueness theorem.

On `L^2(0,infinity)`, take the Dirichlet form realization of

\[
 H=-d^2/dt^2+c^2e^{2t},\quad u(0)=0.
\]

Its form domain is `H_0^1(0,infinity)` intersected with the space having `integral c^2e^{2t}|u|^2<infinity`. The form is closed, and its embedding into `L^2` is compact: the potential uniformly bounds the tail by a quantity tending to zero, and Rellich controls every bounded interval. Its spectrum is therefore discrete, positive, and unbounded. It is strictly above `c^2`: equality in the energy bound would force both derivative and `(V-c^2)` contributions to vanish. There are infinitely many eigenvalues, for example by testing arbitrarily large finite-dimensional spaces of compactly supported functions.

The modified Bessel ODE, DLMF 10.25.1, implies that

\[
 u(t)=K_\nu(ce^t),\qquad Hu=-\nu^2u.
\]

For every fixed complex `nu`, this solution and its derivative decay rapidly as `t` tends to infinity (DLMF 10.25.3 or the integral asymptotics). If `K_nu(c)=0`, it belongs to the Dirichlet operator domain. Its energy identity forces `-nu^2` to be a positive real eigenvalue, so `nu=+/- i tau`, `tau>c`. No nonimaginary complex zeros can have escaped this argument.

Conversely a Dirichlet eigenfunction must be proportional to the decaying `K` solution: a second independent solution grows at infinity, or equivalently the Wronskian of two decaying solutions vanishes. This is also the exact substitution described in [S02], Section 3, pages 3–4. The eigenvalues are simple by second-order uniqueness and the separated boundary condition.

To check that the *analytic determinant zeros* are simple as well, let `u(t,lambda)=K_{sqrt(-lambda)}(ce^t)`. Evenness in the order makes this locally analytic in `lambda`, independently of square-root choice. At an eigenvalue, choose the real solution. Differentiating its ODE gives, with `W=u_lambda u'-u_lambda' u`,

\[
 W'=u^2,\qquad
 -u_\lambda(0)u'(0)=\int_0^\infty u(t)^2dt>0.
\]

The boundary term at infinity vanishes, also for the parameter derivative; fixed-order asymptotics hold locally uniformly in the order. Thus `u_lambda(0)!=0`. Since `d(-nu^2)/dnu=-2nu!=0`, the order zeros of `K_nu(c)` are simple. Consequently the zeros `w=+/-2i tau_j` of `G` are all simple. This also shows why the determinant-multiplicity issue cannot be settled merely by saying the eigenspaces are one dimensional.

## A rigorous `O(1)` counting remainder without assuming WKB exactness

Put `z=c^2/4`. From DLMF 10.25.2, for real `tau>0`,

\[
 I_{i\tau}(c)=\frac{(c/2)^{i\tau}}{\Gamma(1+i\tau)}P(\tau),\quad
 P(\tau)=\sum_{k=0}^\infty\frac{z^k}{k!\prod_{m=1}^k(m+i\tau)}.
\]

The following bounds come directly from this absolutely convergent series, including termwise differentiation:

\[
 |P-1|\le e^{z/\tau}-1=O(1/\tau),\qquad
 |P'|\le z e^{z/\tau}/\tau^2=O(1/\tau^2).
\]

Thus `P` is nonzero for all sufficiently large `tau` and has a continuous logarithm with `argP=O(1/tau)` and derivative `O(1/tau^2)`. Choose the analytic branch of `logGamma` in `Re(z)>0`, continued from `logGamma(1)=0`. Stirling's log-gamma and digamma expansions, DLMF 5.11.1–2, valid in sectors separated from the negative real axis, give

\[
 \arg\Gamma(1+i\tau)=\tau\log\tau-\tau+\pi/4+O(1/\tau),\quad
 \Re\psi(1+i\tau)=\log\tau+O(1/\tau^2).
\]

Therefore a continuous phase of `I_{i tau}(c)` is

\[
 \theta(\tau)=-\tau\log(2\tau/c)+\tau-\pi/4+O(1/\tau),
 \quad\theta'(\tau)=-\log(2\tau/c)+O(1/\tau^2)<0
\]

for sufficiently large `tau`. The derivative is justified by the separate digamma and series estimates, **not** by formally differentiating an uncontrolled remainder.

The connection formula DLMF 10.27.4 and conjugation give

\[
 K_{i\tau}(c)=-\frac{\pi}{\sinh\pi\tau}\Im I_{i\tau}(c).
\]

Since the amplitude is nonzero, zeros are exactly the crossings `theta(tau) in pi Z`. Eventual strict phase monotonicity counts these crossings with an error bounded by one, while finitely many lower zeros change only an additive constant. Hence

\[
 \#\{j:0<\tau_j\le R\}
 =\frac R\pi\log(2R/c)-\frac R\pi+O(1).
\]

Set `R=X/2` and `c=2pi`. This gives the RVM smooth main term through its linear term, with `O(1)` error for `G(s-1/2)`. Multiplication by `Q_T` adds exactly two positive-ordinate zeros when `X>=T`, which changes the count by a bounded quantity. Endpoint conventions likewise change only a bounded term.

The exact classical turning-point action is

\[
 A(R)=R\,\operatorname{arcosh}(R/c)-\sqrt{R^2-c^2}
     =R\log(2R/c)-R+O(1/R).
\]

It is therefore compatible with the count above, but the proof does not assume the Bohr–Sommerfeld equation is exact. [S02] uses that semiclassical approximation in Section 2; [S01], equations (2.1)–(2.4) and Theorem 1, supplies a refined asymptotic zero expansion. Those original papers support provenance, while the elementary phase proof above is the independent counting argument.

## Strict kernel positivity after the quartet

Integration by parts, justified by the double exponential tails of every derivative, gives `Q_T(w)G(w)=integral Q_T(D)f(u)e^{wu}du`, where `D=d/du`.

Let `v=cosh(2u)>=1`. Direct differentiation gives

\[
 \frac{f''}{f}=4c^2(v^2-1)-4cv\ge-4c
\]

for `c>=1/2`, since the right side as a function of `v` is increasing on `[1,infinity)`. Also

\[
 \frac{f''''}{16f}=
 c^4(v^2-1)^2-6c^3v(v^2-1)+7c^2v^2-4c^2-cv.
\]

For `v>=2,c>=4`, the first two terms combine to
`c^3(v^2-1)[c(v^2-1)-6v]>=0`, since `v-1/v>=3/2`. The remaining expression is positive, since `7v^2-v/c-4>0`. For `1<=v<=2`, discarding positive terms gives the uniform lower bound

\[
 f''''/f\ge-576c^3-32c.
\]

Since `T>=32>a`, the coefficient `2(T^2-a^2)` is positive, and

\[
 \frac{Q_T(D)f}{f}
 \ge (T^2+a^2)^2-8c(T^2-a^2)-576c^3-32c
 >T^4-56T^2-197792>0.
\]

Here `c=2pi<7` and the final polynomial is increasing for `T>=32`, taking the exact integer value `793440` at 32. Thus the new kernel is everywhere strictly positive; it is plainly even and smooth and has the same kind of double exponential integrability. This is an analytic sign certificate, not a floating-point plot.

## Finite Li positivity and absence of hidden exponential terms

The even entire order-one function `G` has the paired Hadamard product

\[
 G(w)=G(0)\prod_j(1+w^2/\gamma_j^2),\quad\gamma_j=2\tau_j,
\]

because `sum gamma_j^-2<infinity` and the remaining degree-at-most-one exponential factor is constant by evenness. Thus the usual paired line-zero formula for Li coefficients is exact after normalization. Each conjugate pair contributes `2(1-cos(n theta_j))>=0`, with `theta_j=2arctan(1/(2gamma_j))`. For each fixed `n`, the ordinates are unbounded, so some pair has `0<n theta_j<1`, proving strict positivity. Normal convergence of paired logarithms near `s=1` justifies each derivative.

Write `m_N=min_{1<=n<=N}lambda_n(G(s-1/2)/G(1/2))>0`. The four roots of `Q_T(s-1/2)` have modulus at least `T`. Reflection symmetry converts the rootwise derivative expression to the usual polynomial zero sum. Consequently

\[
 |\lambda_n(Q_T)|\le\frac{4n}{T}(1+1/T)^{n-1}.
\]

This follows from `|1-z^n|<=n|1-z|max(1,|z|)^{n-1}` with `z=1-1/rho`; it deliberately uses a crude bound that suffices. For example any

\[
 T>\max\{32,8Ne^{N-1}/m_N\}
\]

makes the perturbation less than `m_N/2` for every `n<=N`. All these Li coefficients remain positive, while exactly four zeros are off line. This bound is an existence certificate expressed in terms of baseline coefficients; no numerical value of `m_N` is asserted.

## Scope and consequences

The model has a positive smooth even kernel, order one/infinite type, exact symmetry/normalization, the RVM smooth main term with even an `O(1)` count remainder, simple baseline zeros, finitely many off-line exceptions, and arbitrarily long finite positive Li prefixes. Its fixed-strip off-line counts are bounded, so the previous divisor model's linear-density obstruction is removed. These listed analytic conditions and any fixed finite Li prefix cannot alone certify that every zero is on the line throughout this broader class.

This is **not** the zeta function. No Euler product, arithmetic Dirichlet series, correct gamma factor or prime explicit formula, exact individual zeta zeros, pair-correlation law, or all Li coefficients are claimed. In particular, matching the smooth zero-count main term is far weaker than matching the arithmetic oscillatory term. This construction does not invalidate a criterion which uses those extra inputs. Priority of polynomial perturbations of this classical kernel has not been resolved.

## Primary sources actually read and independent-check boundary

[S01] R. B. Paris, *On the nu-zeros of the modified Bessel function K_{i nu}(x) of positive argument*, arXiv:2108.01447v2, 7 April 2022. Entire 6-page preprint read, including Appendix and references. Equation (1.1): integral. Equations (2.1)–(2.4): saddle/phase zero expansion. Theorem 1, equation (3.5), page 4: Lambert-W refined expansion. The higher coefficient algebra and numerical table were read but not independently recomputed. PDF: https://arxiv.org/pdf/2108.01447v2 .

[S02] Yuri Krynytskyi and Andrij Rovenchak, *Asymptotic Estimation for Eigenvalues in the Exponential Potential and for Zeros of K_{i nu}(z) with Respect to Order*, SIGMA 17 (2021), 057, 7 pages; DOI https://doi.org/10.3842/SIGMA.2021.057 . Entire 7-page publisher PDF read. Section 2, pages 2–3: action and semiclassical quantization. Section 3, pages 3–4: exact exponential-potential/Bessel substitution. Equation (7), page 4: asymptotic formula. Numerical data and the claimed precision of the full asymptotic expansion have not been independently validated.

DLMF entries actually inspected: 10.25.1–3 (ODE, series, fixed-order large-argument asymptotic), 10.27.3–4 (order symmetry and connection), and 5.11.1–2 (log-gamma/digamma sector expansions and branch conventions). These are cited formula-level sources, not entire DLMF chapters audited.

Primary PDFs, extracted text, retrieval hashes are in `sources/positive_kernel_bessel_skeptic_round3/`. Bagirova–Khanmamedov 2020 was discovered through metadata and cited references only; its original paper was not accessed/read and is not credited as audited. Its exact theorem is not needed as a black box for the reconstruction above.

Exact reproducibility: `python experiments/code/positive_kernel_bessel_skeptic_round3.py` uses only Python standard-library integer/Fraction arithmetic. A separate polynomial derivative recurrence (`v'=2sinh(2u)`, `(sinh(2u))'=2v`, `f'/f=-2c sinh(2u)`) independently reconstructs `f''/f` and `f''''/f`, then checks the exact kernel margin `793440`. Output is `experiments/results/positive_kernel_bessel_skeptic_round3.json`. The spectral and infinite phase-count arguments remain analytic proofs, not finite numerical tests.

## Addendum: a portable exact strict-log-concavity certificate

A further property can be proved without changing `a=1/4` or the conservative threshold `T>=32`: the positive kernel `k_T(u)=Q_T(D)f(u)` is **strictly log-concave on all of `R`**, and hence, by evenness, strictly decreasing for `u>0`. This addendum was independently found by the skeptic. It awaits independent third review; it is not a novelty claim.

Let `P(v)=Q_T(D)f/f`, the quartic polynomial displayed by the derivative calculations above. Since `v=cosh(2u)`, the exact chain rule gives

\[
 \frac{d^2}{du^2}\log k_T(u)=-\frac{4R(v)}{P(v)^2},
\]
\[
 R(v)=cvP(v)^2-vP(v)P'(v)
       -(v^2-1)\big(P''(v)P(v)-P'(v)^2\big).
\]

It remains to prove `R>0` for `v>=1`, `T>=32`, `c=2pi`. There is a finite rational polynomial certificate for the larger parameter interval `6<=c<=7`. Substitute

\[
 v=1+x,\quad T^2=1024+y,\quad c=6+z,
 \qquad x,y\ge0,\quad0\le z\le1.
\]

Expanding `R` over exact rational arithmetic yields 199 nonzero monomials, grouped as

\[
 R=\sum_{i,j} x^i y^j r_{ij}(z)
\]

with 30 nonzero coefficient polynomials `r_ij`, each of degree at most nine. All Bernstein coefficients of every `r_ij` on `[0,1]` are strictly positive. The smallest of all of them is exactly 6. In particular the `(i,j)=(0,0)` group is present and strictly positive; thus `R>0` even when `x=y=0`.

The complete coefficients and their exact rational Bernstein transforms are preserved in `experiments/results/positive_kernel_bessel_logconcavity_skeptic_round3.json`. The standard-library verifier `experiments/code/positive_kernel_bessel_logconcavity_skeptic_round3.py` constructs `P` and `R` directly as sparse rational polynomial dictionaries; it does not trust the stored coefficients and uses no CAS, numerical transcendental functions, sampled points, or rounding. The only basis identity it uses is

\[
 z^k=\sum_{\ell=k}^n
       \frac{\binom\ell k}{\binom n k}
       B_{\ell,n}(z),\qquad
 B_{\ell,n}(z)=\binom n\ell z^\ell(1-z)^{n-\ell}.
\]

The Bernstein basis is nonnegative and sums to one on `[0,1]`, so its positive coefficients give a rigorous interval-uniform sign, including both endpoints. Run

```
python experiments/code/positive_kernel_bessel_logconcavity_skeptic_round3.py
```

from the archive root to reconstruct every coefficient and replay the certificate. Positivity of `P` has already been proved analytically above, so the strict second logarithmic derivative follows. This is a finite exact algebra certificate combined with a chain-rule proof, not a floating-point concavity scan. The independent derivative recurrence in the separate algebra check supports the quartic input coefficients.

This strengthens the model obstruction to include strict log-concavity and unimodality of the kernel. It still supplies no missing arithmetic structure and no conclusion about RH.

## Priority correction from the original 1926 source

After the independent reconstruction above, the original Pólya article was obtained and read in full: **G. Pólya, *Bemerkung über die Integraldarstellung der Riemannschen ξ-Funktion*, Acta Mathematica48 (1926),305–317, DOI10.1007/BF02565336**, now `PAPER-BESSEL-S03`. The exact formula and conclusion were additionally checked against rendered images of pages306 and315.

His equation(7),page306 defines

\[
 \mathfrak G(z;a)=\int_{\mathbb R}
       e^{-a(e^u+e^{-u})+zu}\,du=2K_z(2a),\quad a>0.
\]

Sections1–3 prove all its zeros simple and purely imaginary; page315 explicitly states the positive-ordinate count

\[
 (y/\pi)\log(y/a)-y/\pi+O(1).
\]

Our baseline `K_{w/2}(2pi)=mathfrakG(w/2;pi)/2` is therefore exactly a rescaling of this prior theorem. **Both its all-line/simple-zero result and the `O(1)` counting main term were already proved in1926.** The operator/phase derivations in this audit are independent reconstructions of established mathematics, not new baseline theorems. The priority of the quartet perturbation, strict-log-concavity certificate and finite-Li assembly remains unassessed.

Pólya's proof architecture is different: integration-by-parts recurrence(9), gamma expansion(11), strip exclusion via asymptotics and continuation in the positive parameter, followed by argument-principle rectangles in Section3. His Section4 additionally explains why naive nonsymmetric finite kernel truncations fail: a first nonzero odd derivative at zero produces an eventual fixed-sign algebraic cosine-transform tail (HilfssatzI,pp315–316). Real analyticity at zero is essential to that inference; it must not be generalized merely from smoothness. This is useful negative knowledge independent of the modern quartet construction.

Source identity deduplication: `PAPER-BESSEL-S02` and `PAPER-BK001` are the same Krynytskyi–Rovenchak2021 work and mathematical version. Their actual publisher/arXivv2 extracted texts agree after removing only whitespace and the arXiv date stamp, though binary PDF hashes differ. The canonical work is `PAPER-BK001`; `quality/paper_aliases.jsonl` preserves the alias and evidence. `PAPER-BESSEL-S01` is Paris2108.01447v2 and is a **different paper** from `PAPER-BK002`, Paris2204.09306v1.
