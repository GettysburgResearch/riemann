# Critical prime energy and square-grid localization

[Guide](README.md) · [Proof library](SOURCE_INDEX.md) · [Evidence](EVIDENCE.md)

**Status:** reviewed component selections in an integration candidate. All prime-counting and source norms use ordinary primes and the declared physical measure. The cumulative upper bound remains open.

## 1. A complete source correction, not independent prime phases

For real $X\ge2$ let

$$A_X(s)=\frac{e^{-\gamma}\exp(\operatorname{Ein}((s-1)\log X))}{(\log X)s^2}
 \prod_{p\le X}(1-p^{-s})^{-1},\qquad
E(X)=\frac1\pi\int_{\mathbb R}\frac{\log^+|A_X(1/2+iy)|}{1+y^2}\,dy.$$

Every included prime brings all its powers. The causal construction preserves the exact initial arithmetic horizon. The [inward-shift transfer](../../../standalone/2026-09-07-astra-logarithmic-domain-transfer/PROOF.md) and the later [endpoint transfer](../../../standalone/2026-09-07-astra-endpoint-prime-discrepancy/PROOF.md) are different statements: the latter removes the positive auxiliary shift by a proved multiplier estimate, not by substituting zero into a divergent constant.

**Proof route.** Keep the literal signed prime/continuum source, separate the band-limited first-prime contribution from all higher powers, and apply the complete physical Cauchy-weighted Fourier identity. Convolution with the factorial source produces an admissible output with its exact horizon. The selected endpoint theorem retains the full horizontal depth and every zero multiplicity. Its hypothetical-zero lower bound still requires an arithmetic upper estimate to give a contradiction.

## 2. Exact discrepancy squares retain every mixed term

Write $\operatorname{Li}_2(x)=\int_2^xdu/\log u$ and $e(x)=\pi(x)-\operatorname{Li}_2(x)$, including prime 2. Define

$$R(x)=\sum_{p\le x}\sqrt p-\int_2^x\frac{\sqrt u}{\log u}\,du,\qquad
K=\int_2^\infty\frac{e(x)^2}{x^2}\,dx,\qquad
J=\int_2^\infty\frac{R(x)^2}{x^3}\,dx.$$

These quantities may initially be infinite. With the causal extension zero below $\log2$, put $z(t)=e^{-t/2}e(e^t)$, $v(t)=e^{-t}R(e^t)$, and $k_a(t)=e^{-at}\mathbf1_{t\ge0}$. The source identities are

$$v=z-\tfrac12 k_1*z,\qquad z=v+\tfrac12 k_{1/2}*v.$$

Thus $K<\infty$ iff $J<\infty$, and $K/4\le J\le K$ when finite. These are bounded invertible maps for the complete source. Cutting off a tail without its memory state is not the same statement.

The [forward discrepancy representation](../../../standalone/2026-09-07-astra-prime-discrepancy/PROOF.md) and [backward endpoint representation](../../../standalone/2026-09-07-astra-endpoint-prime-discrepancy/PROOF.md) encode the same real-part norm with the stated endpoint correction. Their prime-prime, prime-continuum and continuum-continuum terms cannot be replaced by independent phase averages or diagonal terms.

The finite-energy-to-RH implication uses an analytic logarithm identified first in the Euler half-plane, then a source-faithful continuation. Its converse imports the **RH-conditional Cramér mean-square theorem**. The [critical cutoff/taper proof](../../../standalone/2026-09-08-astra-critical-cutoff-taper/PROOF.md) retains endpoint and complex-logarithm hypotheses. Convergence of logarithms in $L^2$ does not justify exponentiation in $L^2$, and outer finite approximants do not automatically give an outer limit.

<a id="square-grid"></a>
## 3. An unconditional theorem pays all within-cell detail

For each integer $n\ge2$ let $m_n$ be the mean of $e$ on $[n^2,(n+1)^2]$ in measure $dx/x^2$, let $w_n=n^{-2}-(n+1)^{-2}$, and let

$$d_n=\int_{n^2}^{(n+1)^2}(e(x)-m_n)^2\frac{dx}{x^2}.$$

The selected all-scale theorem is

$$d_n\le\frac{(2n+1)^3}{n^2(n+1)^2\log^2(2n+1)},\qquad
\sum_{n\ge N}d_n<\frac{28}{\log N}\quad(N\ge2).$$

**Proof route.** Apply the classical interval Brun–Titchmarsh upper bound to the prime increment. The range of the difference of the two increasing source functions is bounded by their larger increment; weighted variance supplies the factor $1/4$. Sum the resulting complete tail. This theorem is unconditional and imports neither RH nor a prime-between-squares lower bound.

The exact extended-value decomposition is

$$K=\int_2^4 e(x)^2\frac{dx}{x^2}+\sum_{n\ge2}w_n m_n^2+\sum_{n\ge2}d_n.$$

The first and last terms are controlled. The accumulated coarse cell levels are not. Replacing $e(x)$ by endpoint samples $s_n=e(n^2)$ gives a complete squared-error tail below $112/\log N$. Consequently

$$K<\infty\quad\Longleftrightarrow\quad
\sum_{n\ge2}\frac{[\pi(n^2)-\operatorname{Li}_2(n^2)]^2}{n^3}<\infty.$$

The finiteness of that series is **open**, not a consequence of the detail estimate. See [full localization proof, source adapter and analytic consumer](../../../standalone/2026-09-08-astra-square-grid-localization/PROOF.md).

## 4. The stopped work exposes the missing arithmetic

Set $a_n=s_{n+1}-s_n$. Exact summation gives

$$\sum_{n=2}^{M-1}w_n s_n^2+\frac{s_M^2}{M^2}
 =\frac{s_2^2}{4}+\sum_{n=2}^{M-1}\frac{2s_n a_n+a_n^2}{(n+1)^2}.$$

The terminal future and old-level/new-increment cross term remain. A bound for increments is not a bound for the accumulated levels or their signed work. Resetting the level in every cell changes the source. A positive continuous counting-density control with similar local and PNT-shaped properties is a method counterexample, not ordinary primes or an RH counterexample.

The nonlinear [log-cosh feedback theorem](../../../standalone/2026-09-07-astra-entropy-feedback/PROOF.md) likewise gives the complete accounting identity

$$|2E(X)-W(X)|<8+24\log(1+\log X),$$

where $W$ is the source-defined pre-jump signed work. Its bounded feedback function and positive associated kernel do not bound the required off-diagonal work from above. The notation $W$ here does not denote the Weil kernel on the operator page.

## 5. What the numerical prefix does and does not certify

Six endpoint-energy prefixes are selected. The last satisfies

$$.565641628407<\sum_{n=2}^{127}w_n e(n^2)^2<.565641628409.$$

The reviewed replay checks the ordinary-prime sieve against trial division through 16,384 and reconstructs the logarithmic-integral differences with full numerical primitive remainders. This is a finite **sample** energy, not the orthogonal cell-mean energy, not full $J$, and not a certificate for the infinite coarse tail. Its increase with the cutoff is automatic for nonnegative summands. See [selected evidence and replay command](EVIDENCE.md#prime-prefix).

**Useful next task:** obtain a source-specific upper bound for the complete signed coarse work, or for the equivalent cumulative energy. Overlapping grids or a sharper local variance estimate alone do not control that missing channel.
